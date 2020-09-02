import time
import math
import string
import random
import numpy as np
from sklearn.model_selection import train_test_split

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

# a b c => 3 4 5
# d e f g => 6 7 8 9

characters = 'abcdefghijklmnopqrstuvwxyz'

src_word2id = {'<pad>': 0, '<sos>': 1, '<eos>': 2}
trg_word2id = {'<pad>': 0, '<sos>': 1, '<eos>': 2}
for index, char in enumerate(characters):
    src_word2id[char] = index + 3
    trg_word2id[str(index + 3)] = index + 3

src_id2word = {id: char for char, id in src_word2id.items()}
trg_id2word = {id: char for char, id in trg_word2id.items()}
BATCH_SIZE = 64


def generate_sample(length):
    src_sample = []
    trg_sample = []

    for i in range(length):
        id = random.randint(3, len(src_id2word) - 1)
        src_sample.append(src_id2word[id])
        trg_sample.append(trg_id2word[id])
    return " ".join(src_sample).strip(), " ".join(trg_sample).strip()

def generate_data(num_samples):
    src = []
    trg = []

    for i in range(num_samples):
        length = random.randint(3, 10)
        src_sample, trg_sample = generate_sample(length)
        src.append(src_sample)
        trg.append(trg_sample)
    
    assert len(src) == len(trg)
    return src, trg

src, trg = generate_data(10000)
train_src, test_src, train_trg, test_trg = train_test_split(src, trg, test_size=0.1, random_state=42)
train_src, valid_src, train_trg, valid_trg = train_test_split(train_src, train_trg, test_size=0.2, random_state=42) # 0.9 * 0.2 = 0.18

print(f"Number of training examples: {len(train_src)}")
print(f"Number of validation examples: {len(valid_src)}")
print(f"Number of testing examples: {len(test_src)}")


class ToyDataset(Dataset):
    def __init__(self, src, trg):
        self.src = src
        self.trg = trg

        assert len(src) == len(trg)
        self.length = len(src)
    
    def __getitem__(self, index):
        src_seq, trg_seq = self.preprocess(self.src[index], self.trg[index])
        return src_seq, trg_seq

    def __len__(self):
        return self.length
    
    def preprocess(self, src_sent, trg_sent):
        src_seq = [src_word2id['<sos>']] + [src_word2id[word] for word in src_sent.split()] + [src_word2id['<eos>']]
        trg_seq = [trg_word2id['<sos>']] + [trg_word2id[word] for word in trg_sent.split()] + [trg_word2id['<eos>']]

        return torch.Tensor(src_seq), torch.Tensor(trg_seq)


def collate_fn(data):
    def merge(sequences):
        lengths = [len(seq) for seq in sequences]
        padded_seqs = torch.zeros(len(sequences), max(lengths)).long()
        for i, seq in enumerate(sequences):
            end = lengths[i]
            padded_seqs[i, :end] = seq[:end]
        return padded_seqs, lengths

    data.sort(key=lambda x: len(x[0]), reverse=True)
    src_seqs, trg_seqs = zip(*data)

    src_seqs, src_lengths = merge(src_seqs)
    trg_seqs, trg_lengths = merge(trg_seqs)

    return src_seqs, src_lengths, trg_seqs, trg_lengths


def get_loader(src_data, trg_data, train=True, batch_size=BATCH_SIZE):
    dataset = ToyDataset(src_data, trg_data)

    if train:
        shuffle = True
    else:
        shuffle = False
    
    dataloader = DataLoader(
        dataset=dataset,
        batch_size=BATCH_SIZE,
        shuffle=shuffle,
        collate_fn=collate_fn)

    return dataloader

train_loader = get_loader(train_src, train_trg, True, BATCH_SIZE)
valid_loader = get_loader(valid_src, valid_trg, False, BATCH_SIZE)
test_loader = get_loader(test_src, test_trg, False, BATCH_SIZE)


class Encoder(nn.Module):
    def __init__(self, input_dim, emb_dim, hidden_dim, dropout, pad_token):
        super().__init__()

        self.embedding = nn.Embedding(input_dim, emb_dim, padding_idx=pad_token)
        self.rnn = nn.GRU(emb_dim, hidden_dim)
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, input):
        # input => [src_len, batch_size]
        embedded = self.embedding(input)
        embedded = self.dropout(embedded)
        # embedded => [src_len, batch_size, emb_dim]

        output, hidden = self.rnn(embedded)
        # output => [src_len, batch_size, hidden_dim]
        # hidden => [num_layers * num_dir, batch_size, hidden_dim]
        #        => [1, batch_size, hidden_dim]

        return output, hidden


class BahdanauAttention(nn.Module):
    def __init__(self, hidden_size):
        super().__init__()

        self.hidden_size = hidden_size
        self.w1 = nn.Linear(hidden_size, hidden_size)
        self.w2 = nn.Linear(hidden_size, hidden_size)
        self.v = nn.Parameter(torch.rand(hidden_size * 2))
        stdv = 1. / math.sqrt(hidden_size)
        self.v.data.normal_(mean=0, std=stdv)
    
    def forward(self, hidden, encoder_outputs):
        # hidden => [1, batch_size, hidden_dim]
        # encoder_outputs => [seq_len, batch_size, hidden_dim]

        src_len = encoder_outputs.shape[0]
        hidden = hidden.expand(src_len, -1, -1)
        # hidden => [src_len, batch_size, hidden_dim]

        hidden_energy = self.w1(hidden)
        # hidden_energy => [src_len, batch_size, hidden_dim]

        encoder_outputs_energy = self.w2(encoder_outputs)
        # encoder_outputs_energy => [src_len, batch_size, hidden_dim]

        energy = torch.cat((hidden_energy, encoder_outputs_energy), dim=2)
        # energy => [src_len, batch_size, hidden_dim * 2]

        v = (self.v * energy)
        # v => [src_len, batch_size, hidden_dim * 2]

        v = torch.sum(v, dim=2)
        # v => [src_len, batch_size]

        attention_energies = F.softmax(v, dim=0)
        # attention_energies => [src_len, batch_size]

        return attention_energies


class Decoder(nn.Module):
    def __init__(self, input_dim, emb_dim, hidden_dim, attn, dropout, pad_token):
        super().__init__()

        self.output_dim = input_dim
        self.embedding = nn.Embedding(input_dim, emb_dim, padding_idx=pad_token)
        self.rnn = nn.GRU(emb_dim + hidden_dim, hidden_dim)
        self.attn = attn
        self.out = nn.Linear(hidden_dim, input_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, trg, hidden, encoder_outputs):
        # trg => [batch_size]
        # hidden => [num_layers * num_dir, batch_size, hidden_dim]
        #        => [1, batch_size, hidden_dim]
        # encoder_outputs => [src_len, batch_size, hidden_dim]

        inputs = trg.unsqueeze(0)
        # inputs => [1, batch_size]

        embedded = self.embedding(inputs)
        embedded = self.dropout(embedded)
        # embedded => [1, batch_size, emb_dim]

        attention_energies = self.attn(hidden, encoder_outputs)
        # attention_energies => [src_len, batch_size]

        attention_energies = attention_energies.transpose(1, 0)
        # attention_energies => [batch_size, src_len]

        attention_energies = attention_energies.unsqueeze(1)
        # attention_energies => [batch_size, 1, src_len]

        encoder_outputs = encoder_outputs.transpose(1, 0)
        # encoder_outputs => [batch_size, src_len, hidden_dim]

        context = torch.bmm(attention_energies, encoder_outputs)
        # context => [batch_size, 1, hidden_dim]

        context = context.transpose(1, 0)
        # context => [1, batch_size, hidden_dim]

        rnn_input = torch.cat((embedded, context), dim=2)
        # rnn_input => [1, batch_size, hidden_dim + emb_dim]

        output, hidden = self.rnn(rnn_input, hidden)
        # output => [1, batch_size, hidden_dim]
        # hidden => [1, batch_size, hidden_dim]

        logits = self.out(output.squeeze(0))
        # logits => [batch_size, output_dim]

        return logits, hidden


class Seq2Seq(nn.Module):
    def __init__(self, encoder, decoder):
        super().__init__()

        self.encoder = encoder
        self.decoder = decoder

    def forward(self, src, trg, teacher_forcing_ratio=0.5):
        # src => [seq_len, batch_size]
        # trg => [seq_len, batch_size]

        encoder_outputs, hidden = self.encoder(src)
        trg_len = trg.shape[0]
        batch_size = trg.shape[1]
        output_dim = self.decoder.output_dim

        outputs = torch.zeros(trg_len, batch_size, output_dim)
        dec_inp = trg[0, :]

        for i in range(trg_len):
            output, hidden = self.decoder(dec_inp, hidden, encoder_outputs)
            outputs[i] = output
            teacher_force = random.random() < teacher_forcing_ratio
            top1 = output.argmax(1)
            dec_inp = trg[i] if teacher_force else top1
        return outputs

INPUT_DIM = len(src_word2id)
OUTPUT_DIM = len(trg_word2id)
EMBEDDING_DIM = 10
HIDDEN_DIM = 20
DROPOUT = 0.5
PAD_TOKEN = trg_word2id['<pad>']

enc = Encoder(INPUT_DIM, EMBEDDING_DIM, HIDDEN_DIM, DROPOUT, PAD_TOKEN)
attn = BahdanauAttention(HIDDEN_DIM)
dec = Decoder(OUTPUT_DIM, EMBEDDING_DIM, HIDDEN_DIM, attn, DROPOUT, PAD_TOKEN)
model = Seq2Seq(enc, dec)

def init_weights(model):
    for name, param in model.named_parameters():
        nn.init.uniform_(param.data, -0.08, 0.08)

model.apply(init_weights)

def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

print(f'The model has {count_parameters(model)} trainable parameters')

optimizer = optim.Adam(model.parameters())
criterion = nn.CrossEntropyLoss(ignore_index=PAD_TOKEN)


def train(model, iterator, criterion, optimizer, clip):
    epoch_loss = 0
    model.train()

    for batch in iterator:
        src, src_lengths, trg, trg_lengths = batch
        src = src.transpose(1, 0)
        trg = trg.transpose(1, 0)
        output = model(src, trg)

        output_dim = output.shape[-1]
        output = output[1:].view(-1, output_dim)
        trg = trg[1:].contiguous().view(-1)
        loss = criterion(output, trg)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), clip)
        optimizer.step()

        epoch_loss += loss.item()
    return epoch_loss / len(iterator)


def evaluate(model, iterator, criterion):
    epoch_loss = 0
    model.eval()
    with torch.no_grad():
        for batch in iterator:
            src, src_lengths, trg, trg_lengths = batch
            src = src.transpose(1, 0)
            trg = trg.transpose(1, 0)
            output = model(src, trg)

            output_dim = output.shape[-1]
            output = output[1:].view(-1, output_dim)
            trg = trg[1:].contiguous().view(-1)

            loss = criterion(output, trg)

            epoch_loss += loss.item()
    return epoch_loss / len(iterator)


def epoch_time(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_mins = int(elapsed_time / 60)
    elapsed_secs = elapsed_time - (elapsed_mins * 60)
    return elapsed_mins, elapsed_secs


def inference(src_sentence, model, max_len=10):
    model.eval()

    tokens = [src_word2id['<sos>']] + [src_word2id[word] for word in src_sentence.split()] + [src_word2id['<eos>']]
    src_tensor = torch.tensor(tokens).unsqueeze(1)
    with torch.no_grad():
        encoder_outputs, hidden = model.encoder(src_tensor)
    trg_ids = [trg_word2id['<sos>']]
    for i in range(max_len):
        trg_tensor = torch.LongTensor([trg_ids[-1]])
        with torch.no_grad():
            output, hidden = model.decoder(trg_tensor, hidden, encoder_outputs)
        
        pred_token = output.argmax(1).item()
        trg_ids.append(pred_token)
        
        if pred_token == trg_word2id['<eos>']:
            break
    trg_seq = [trg_id2word[id] for id in trg_ids[1:]]
    trg_ids = [src_word2id[word] for word in src_sentence.split()]
    trg_org = [trg_id2word[id] for id in  trg_ids]
    predicted = " ".join(trg_seq).strip()
    truth = " ".join(trg_org).strip()
    print(f"Src sent: {src_sentence}, Predicted: {predicted}, Ground Truth: {truth}")


N_EPOCHS = 1000
CLIP = 1

best_valid_loss = float('inf')

for epoch in range(N_EPOCHS):
    start_time = time.time()

    train_loss = train(model, train_loader, criterion, optimizer, CLIP)
    valid_loss = evaluate(model, valid_loader, criterion)

    end_time = time.time()
    epoch_mins, epoch_secs = epoch_time(start_time, end_time)

    if valid_loss < best_valid_loss:
        best_valid_loss = valid_loss
        torch.save(model.state_dict(), 'model.pt')
    
    print(f"Epoch {epoch + 1} | Time: {epoch_mins}m {epoch_secs}s")
    print(f"\tTrain Loss: {train_loss:.3f} | Train PPL: {math.exp(train_loss):7.3f} |")
    print(f"\tValid Loss: {valid_loss:.3f} | Valid PPL: {math.exp(valid_loss):7.3f} |")
    sentence = "a g h i k"
    inference(sentence, model, len(sentence.split()))

model.load_state_dict(torch.load('model.pt'))
test_loss = evaluate(model, test_loader, criterion)
print(f"\tTest Loss: {test_loss:.3f} | Test PPL: {math.exp(test_loss):7.3f} |")
