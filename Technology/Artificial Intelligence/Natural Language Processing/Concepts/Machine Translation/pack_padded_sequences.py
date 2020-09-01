''' This contains the packing and unpacking the padded sequences for rnn.
we want to run a LSTM on a batch of 3 character sequences ['long_str', 'tiny', 'medium']
step 1 : construct vocabulary
step 2 : convert the sequences into numerical form
step 3 : define model
step 4 : prepare data, by padding with 0 (<pad> token), making the batch equal lengths
step 5 : sort the data in the batch in descending order by their original lengths
step 6 : apply the embedding layer for the batch
step 7 : call the pack_padded_sequences fn, with embeddings and lengths of original sentences
step 8 : call the forward method of the lstm model
step 9 : call the unpack_padded_sequences (pad_packed_sequence) method if required
'''

import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable

from torch import LongTensor
from torch.nn.utils.rnn import pad_packed_sequence, pack_padded_sequence, pad_sequence

data = ['long_str', 'tiny', 'medium']

# step 1 : construct vocabulary
vocab = ['<pad>'] + sorted(set([char for seq in data for char in seq]))
# vocab = ['<pad>', '_', 'd', 'e', 'g', 'i', 'l', 'm', 'n', 'o', 'r', 's', 't', 'u', 'y']

# step 2 : convert the sequences into numerical form
vectorized_data = [[vocab.index(tok) for tok in seq] for seq in data]
# vectorized_data = [[6, 9, 8, 4, 1, 11, 12, 10], [12, 5, 8, 14], [7, 3, 2, 5, 13, 7]]

# step 3 : define model

# input for embedding layer is lengths of inputs
# output for embedding layer is embedding shape of inputs
embedding_layer = nn.Embedding(len(vocab), 4)

# input_size is the embedding output size
# hidden_size is the hidden size of lstm
lstm = nn.LSTM(input_size=4, hidden_size=5, batch_first=True)

# step 4 : prepare data, by padding with 0 (<pad> token), making the batch equal lengths
seq_lengths = LongTensor([len(seq) for seq in vectorized_data])
sequence_tensor = Variable(torch.zeros(len(vectorized_data), seq_lengths.max(), dtype=torch.long))

for idx, (seq, seq_len) in enumerate(zip(vectorized_data, seq_lengths)):
    sequence_tensor[idx, :seq_len] = LongTensor(seq)

# sequence_tensor = ([[ 6,  9,  8,  4,  1, 11, 12, 10],
#                     [12,  5,  8, 14,  0,  0,  0,  0],
#                     [ 7,  3,  2,  5, 13,  7,  0,  0]])

# step 5 : sort the data in the batch in descending order by their original lengths
# seq_lengths = [8, 4, 6]
seq_lengths, perm_idx = seq_lengths.sort(0, descending=True)
# seq_lengths = [8, 6, 4]
# perm_idx = [0, 2, 1]

sequence_tensor = sequence_tensor[perm_idx]
# sequence_tensor = ([[ 6,  9,  8,  4,  1, 11, 12, 10],
#                     [ 7,  3,  2,  5, 13,  7,  0,  0],
#                     [12,  5,  8, 14,  0,  0,  0,  0]])

# step 6 : apply the embedding layer for the batch
# sequence_tensor shape => [batch_size, max_seq_len] => [3, 8]
embed = embedding_layer(sequence_tensor)
# embed shape is => [batch_size, max_seq_len, embedding_shape] => [3, 8, 4]

# step 7 : call the pack_padded_sequences fn, with embeddings and lengths of original sentences
packed_input = pack_padded_sequence(embed, seq_lengths, batch_first=True)
# packed_input is a namedtuple with 2 attributes: data, batch_sizes
# data.shape => [all_sequences_len_sum, embedding_size] => [18, 4]
# batch_sizes => [size_of_each_batch_input] => [3, 3, 3, 3, 2, 2, 1, 1]
# visualization :
# l  o  n  g  _  s  t  r   # (long_str)
# m  e  d  i  u  m         # (medium)
# t  i  n  y               # (tiny)
# 3  3  3  3  2  2  1  1   (sum = 18 [all_sequences_len_sum])

# step 8 : call the forward method of the lstm model
packed_output, (ht, ct) = lstm(packed_input)
# packed_output is a namedtuple with 2 attributes: data, batch_sizes
# data.shape => [all_sequences_len_sum, hidden_shape] => [18, 5]
# batch_sizes => [size_of_each_batch_input] => [3, 3, 3, 3, 2, 2, 1, 1]
# ht => [num_layers * num_directions, batch_size, hidden_size] => [1, 3, 5]
# ct => [num_layers * num_directions, batch_size, hidden_size] => [1, 3, 5]

# step 9 : call the unpack_padded_sequences (pad_packed_sequence) method if required
output, input_sizes = pad_packed_sequence(packed_output, batch_first=True)
# output shape => [batch_size, max_seq_len, hidden_dim] (if batch_first is true) => [3, 8, 5]
# input_sizes => [length_of_each_sequence] => [8, 6, 4]

# Summary of Shape Transformations #
# -------------------------------- #

# (batch_size X max_seq_len X embedding_dim) --> Sort by seqlen ---> (batch_size X max_seq_len X embedding_dim)
# (batch_size X max_seq_len X embedding_dim) --->      Pack     ---> (batch_sum_seq_len X embedding_dim)
# (batch_sum_seq_len X embedding_dim)        --->      LSTM     ---> (batch_sum_seq_len X hidden_dim)
# (batch_sum_seq_len X hidden_dim)           --->    UnPack     ---> (batch_size X max_seq_len X hidden_dim)