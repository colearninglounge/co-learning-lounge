<details>
 <summary>Why do we need non-linear activation function?</summary>
If we only allow linear activation functions in a neural network, the output will just be a [linear transformation](https://en.wikipedia.org/wiki/Linear_map#Matrices) of the input, which is not enough to form a [universal function approximator](https://en.wikipedia.org/wiki/Universal_approximation_theorem). Such a network can just be represented as a matrix multiplication, and you would not be able to obtain very interesting behaviors from such a network.
Activation functions cannot be linear because neural networks with a linear activation function are effective only one layer deep, regardless of how complex their architecture is. And real world and problems are non-linear. Non-linearity is needed in activation functions because its aim in a neural network is to produce a nonlinear decision boundary via non-linear combinations of the weight and inputs.

[Ref 1](https://stackoverflow.com/questions/9782071/why-must-a-nonlinear-activation-function-be-used-in-a-backpropagation-neural-net)
[Ref 2](https://www.quora.com/Why-do-we-need-non-linear-activation-functions-in-a-neural-network)

</details>

