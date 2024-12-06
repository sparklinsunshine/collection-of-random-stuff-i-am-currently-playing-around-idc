import numpy as np
import matplotlib.pyplot as plt
from nnfs.datasets import spiral_data
import nnfs
from nnfs.datasets import vertical_data
import math

'''
input = [1,2,3,2.5]

weights1 = [0.2,0.8,-0.5,1.0]
weights2 = [0.5,-0.91,0.26,-0.5]
weights3 = [-0.26,-0.27,0.17,0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

output = [input[0]*weights1[0] +input[1]*weights1[1] +input[2]*weights1[2] +input[3]*weights1[3] + bias1, 
          input[0]*weights2[0] +input[1]*weights2[1] +input[2]*weights2[2] +input[3]*weights2[3] + bias2,
          input[0]*weights3[0] +input[1]*weights3[1] +input[2]*weights3[2] +input[3]*weights3[3] + bias3]
print(output)
'''

#the same above code but in shorter form lmao

'''
input = [1,2,3,2.5]
weights = [[0.2,0.8,-0.5,1.0],[0.5,-0.91,0.26,-0.5],[-0.26,-0.27,0.17,0.87]]
biases = [2,3,0.5]

layer_outputs = []
for neuron_weights, neuron_bias in zip(weights,biases):
    neuron_output=0
    for n_input, weight in zip(input,neuron_weights):
        neuron_output += n_input * weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)
print(layer_outputs)

'''

'''

input = [1,2,3,2.5]
weight = [0.2,0.8,-0.5,1.0]
bias = 2

output = np.dot(input,weight) + bias
print(output)
'''

'''
input = [[1,2,3,2.5],[2,5,-1.0,2.0],[-1.5,2.7,3.3,-0.8]]
weights1 = [[0.2,0.8,-0.5,1.0],[0.5,-0.91,0.26,-0.5],[-0.26,-0.27,0.17,0.87]]
weights2 = [[0.7,0.98,-0.9,1.0],[0.54,-0.1,0.36,-0.58],[0.26,-0.7,0.17,0.7]]
biases1 = [2,3,0.5]
biases2 = [8,2,0.47]
layer1_output = np.dot(input,np.array(weights1).T) + biases1
layer2_output = np.dot(input,np.array(weights2).T) + biases2

print(layer2_output)
'''

'''
np.random.seed(0)
x = [[1,2,3,2.5],[2,5,-1.0,2.0],[-1.5,2.7,3.3,-0.8]]
class Layer_Dense:
    def __init__(self,n_inputs, n_neurons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.biases

      
#print(0.1*np.random.randn(4,3))
layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,6)

layer1.forward(x)
print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)
'''

'''
np.random.seed(0)
x = [[1,2,3,2.5],[2,5,-1.0,2.0],[-1.5,2.7,3.3,-0.8]]
input = [0,2,-1,3.3,-2.7,1.1,2.2,-100]
output=[]

for i in input:
    if i > 0:
        output.append(i)
    elif i == 0:
        output.append(0)
print(output)
'''

'''
np.random.seed(0)
x = [[1,2,3,2.5],[2,5,-1.0,2.0],[-1.5,2.7,3.3,-0.8]]
input = [0,2,-1,3.3,-2.7,1.1,2.2,-100]
output=[]

for i in input:
    output.append(max(0,i))
print(output)
'''

'''
x = [[1,2,3,2.5],[2,5,-1.0,2.0],[-1.5,2.7,3.3,-0.8]]

class Layer_Dense:
    def __init__(self,n_inputs, n_neurons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.biases

class Activation_ReLU:
    def forward(self,input):
        self.output = np.maximum(0,input)

      
#print(0.1*np.random.randn(4,3))
layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,6)

layer1.forward(x)
print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)
'''

'''
np.random.seed(0)
def create_data(points,classes):
    x = np.zeros((points * classes, 2))
    y = np.zeros(points * classes, dtype = 'uint8')
    for class_number in range(classes):
        ix = range(points * class_number, points * (class_number+1))
        r = np.linspace(0.0,1,points) # radius
        t = np.linspace(class_number * 4, (class_number + 1)*4, points) * np.random.randn(points)*0.2
        x[ix] = np.c_[r * np.sin(t*2.5), r*np.cos(t*2.5)]
        y[ix] = class_number
    return x, y
print('here')
x,y = create_data(100,3)
plt.scatter(x[:,0], x[:,1])
plt.show()
plt.scatter(x[:,0], x[:,1],c = y, cmap = 'brg')
plt.show()
'''

'''
x = [[1,2,3,2.5],[2,5,-1.0,2.0],[-1.5,2.7,3.3,-0.8]]
x,y = spiral_data(100,3)
class Layer_Dense:
    def __init__(self,n_inputs, n_neurons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.biases

class Activation_ReLU:
    def forward(self,input):
        self.output = np.maximum(0,input)
layer1 = Layer_Dense(2,5)
activation1 = Activation_ReLU()
layer1.forward(x)
#print(layer1.output)
activation1.forward(layer1.output)
print(activation1.output)
'''

'''
layer_outputs = [4.8, 1.21, 2.385]
E =math.e
exp_values = []
for output in layer_outputs:
    exp_values.append(E ** output)
print(exp_values)
'''

'''
layer_outputs = [4.8, 1.21, 2.385]
E =math.e
exp_values = []
for output in layer_outputs:
    exp_values.append(E ** output)
print(exp_values)
norm_base = sum(exp_values)
norm_values = []

for value in exp_values:
    norm_values.append(value/norm_base)
print(norm_values)
print(sum(norm_values))
'''

'''
layer_outputs = [4.8, 1.21, 2.385]
E = math.e
exp_values = np.exp(layer_outputs)
norm_values = exp_values / np.sum(exp_values)
print(norm_values)
print(sum(norm_values))
'''

'''
layer_outputs = [[4.8, 1.21, 2.385],[8.9,-1.81,0.2],[1.41, 1.051, 0.026]]

exp_values = np.exp(layer_outputs)
print(exp_values)
norm_values = exp_values/np.sum(exp_values)
print(sum(norm_values))
'''

'''
layer_outputs = [[4.8, 1.21, 2.385],[8.9,-1.81,0.2],[1.41, 1.051, 0.026]]

exp_values = np.exp(layer_outputs)
print(np.sum(layer_outputs, axis = 0))
'''

'''
layer_outputs = [[4.8, 1.21, 2.385],[8.9,-1.81,0.2],[1.41, 1.051, 0.026]]

exp_values = np.exp(layer_outputs)
print(np.sum(layer_outputs, axis = 1, keepdims = True))
'''

'''
layer_outputs = [[4.8, 1.21, 2.385],[8.9,-1.81,0.2],[1.41, 1.051, 0.026]]

exp_values = np.exp(layer_outputs)
norm_values = exp_values / np.sum(exp_values, axis = 1, keepdims = True)
print(norm_values)
'''

'''
x = [[1,2,3,2.5],[2,5,-1.0,2.0],[-1.5,2.7,3.3,-0.8]]
x, y = spiral_data(100,3)

class Layer_Dense:
    def __init__(self,n_inputs, n_neurons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.biases

class Activation_ReLU:
    def forward(self,input):
        self.output = np.maximum(0,input)

class Activation_Softmax:
    def forward(self,inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims = True))
        probabilities = exp_values / np.sum(exp_values, axis = 0,keepdims = True)
        self.output = probabilities

x,y = spiral_data(samples = 100, classes = 3)
dense1 = Layer_Dense(2,3)
activation1 = Activation_ReLU()

dense2 = Layer_Dense(2,3)
activation2 = Activation_Softmax()

dense1.forward(x) 
activation1.forward(dense1.output)

dense2.forward(x)
activation2.forward(dense2.output)

print(activation2.output[:5])
'''

'''
softmax_output = [0.7,0.1,0.2]
target_output = [1,0,0]
loss_list = []
for i in range(0,len(softmax_output)):
    loss_list.append(-math.log(softmax_output[i]) * target_output[i])
print(sum(loss_list))
#loss = -(math.log(softmax_output[0]) * target_output[0] + 
#       math.log(softmax_output[1]) * target_output[1] +
#      math.log(softmax_output[2]) * target_output[2])
'''

'''
softmax_outputs = [[0.7, 0.1, 0.2],[0.1,0.5,0.4],[0.02,0.9,0.08]]
class_targets = [0,1,1]
for targ_idx, distribution in zip(class_targets,softmax_outputs):
    print(distribution[targ_idx])
    '''

'''
softmax_outputs = np.array([[0.7, 0.1, 0.2],[0.1,0.5,0.4],[0.02,0.9,0.08]])
class_targets = [0,1,1]
#print(softmax_outputs[[0,1,2], class_targets])
#or
print(softmax_outputs[range(len(softmax_outputs)), class_targets])
'''

'''
softmax_outputs = np.array([[0.7, 0.1, 0.2],[0.1,0.5,0.4],[0.02,0.9,0.08]])
class_targets = [0,1,1]
neg_log = -np.log(softmax_outputs[range(len(softmax_outputs)), class_targets])
average_loss = np.mean(neg_log)
print(average_loss)
'''

'''
nnfs.init()

x = [[1,2,3,2.5],[2,5,-1.0,2.0],[-1.5,2.7,3.3,-0.8]]

class Layer_Dense:
    def __init__(self,n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights)
        self.output += self.biases

class Activation_ReLU:
    def forward(self,input):
        self.output = np.maximum(0,input)

class Activation_Softmax:
    def forward(self,inputs):
        exp_values = np.exp(inputs - np.max(inputs,axis = 1, keepdims = True))
        probabilities = exp_values / np.sum(exp_values, axis = 1, keepdims = True)
        self.output = probabilities

class Loss:
    def calculate(self,output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss

class Loss_CategoricalCrossEntropy(Loss):
    def forward(self,y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)
        if len(y_true.shape) == 1:
            correct_confidence = y_pred_clipped[range(samples), y_true]
        elif len(y_true.shape) == 2:
            correct_confidence = np.sum(y_pred_clipped * y_true, axis = 1)
        negative_log_likelihoods = -np.log(correct_confidence)
        return negative_log_likelihoods

x,y = spiral_data(samples = 100, classes = 3)
dense1 = Layer_Dense(2,3)
activation1 = Activation_ReLU()
dense2 = Layer_Dense(3,3)
activation2 = Activation_Softmax()
dense1.forward(x)
activation1.forward(dense1.output)
dense2.forward(activation1.output)
activation2.forward(dense2.output)
print(activation2.output[:5])

loss_function = Loss_CategoricalCrossEntropy()
loss = loss_function.calculate(activation2.output, y)
print('Loss: ', loss)
'''

'''
softmax_outputs = np.array([[0.7,0.2,0.1],[0.5,0.1,0.4],[0.02,0.9,0.08]])
class_targets = [0,1,1]
predictions = np.argmax(softmax_outputs, axis = 1)
accuracy = np.mean(predictions == class_targets)
print('Accuracy: ', accuracy)
'''

'''
nnfs.init()
class Layer_Dense:
    def __init__(self,n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights)
        self.output += self.biases

class Activation_ReLU:
    def forward(self,input):
        self.output = np.maximum(0,input)

class Activation_Softmax:
    def forward(self,inputs):
        exp_values = np.exp(inputs - np.max(inputs,axis = 1, keepdims = True))
        probabilities = exp_values / np.sum(exp_values, axis = 1, keepdims = True)
        self.output = probabilities

class Loss:
    def calculate(self,output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss

class Loss_CategoricalCrossEntropy(Loss):
    def forward(self,y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)
        if len(y_true.shape) == 1:
            correct_confidence = y_pred_clipped[range(samples), y_true]
        elif len(y_true.shape) == 2:
            correct_confidence = np.sum(y_pred_clipped * y_true, axis = 1)
        negative_log_likelihoods = -np.log(correct_confidence)
        return negative_log_likelihoods

x,y = vertical_data(samples = 100, classes = 3)
dense1 = Layer_Dense(2,3)
activation1 = Activation_ReLU()
dense2 = Layer_Dense(2,3)
activation2 = Activation_Softmax()

loss_function = Loss_CategoricalCrossEntropy()

lowest_loss = 9999999
best_dense1_weights = dense1.weights.copy()
best_dense1_biases = dense1.biases.copy()
best_dense2_weights = dense2.weights.copy()
best_dense2_weights = dense2.biases.copy()

for i in range(100000):
    dense1.weights = 0.05 * np.random.randn(2,3)
    dense1.biases = 0.05 * np.random.randn(1,3)
    dense2.weights = 0.05 * np.random.randn(3,3)
    dense2.biases = 0.05 * np.random.randn(1,3)
    
    '''
    '''dense1.forward(x)
    activation1.forward(dense1.output)
    dense2.forward(activation1.output)
    activation2.forward(dense2.output)
    '''
    '''
    layers_and_activations = [dense1, activation1, dense2, activation2]
    layer_input = x
    for layer in layers_and_activations:
        layer.forward(layer_input)
        layer_input =layer.output

    loss = loss_function.calculate(layer_input, y)

    predictions = np.argmax(layer_input,axis = 1)
    accuracy = np.mean(predictions == y)

    if loss < lowest_loss:
        print('New set of weights found, iteration: ', i, 'loss:', loss, 'acc:', accuracy)
        best_dense1_weights = dense1.weights.copy()
        best_dense1_biases = dense1.biases.copy()
        best_dense2_weights = dense2.weights.copy()
        best_dense2_biases = dense2.weights.copy()
        lowest_loss = loss


nnfs.init()
x,y = spiral_data(samples = 100, classes = 3)
dense1 = Layer_Dense(2,3)
activation1 = Activation_ReLU()
dense2 = Layer_Dense(2,3)
activation2 = Activation_Softmax()

loss_function = Loss_CAtegoricalCrossEntropy()

lowest_loss = 9999999
best_dense1_weights = dense1.weights.copy()
best_dense1_biases = dense1.biases.copy()
best_dense2_weights = dense2.weights.copy()
best_dense2_weights = dense1.biases.copy()

for i in range(100000):
    dense1.weights = 0.05 * np.random.randn(2,3)
    dense1.biases = 0.05 * np.random.randn(1,3)
    dense2.weights = 0.05 * np.random.randn(3,3)
    dense2.biases = 0.05 * np.random.randn(1,3)
    
    dense1.forward(x)
    activation1.forward(dense1.output)
    dense2.forward(x)
    activation2.forward(dense2.output)

    loss = loss_function.calculate(activation2.output, y)

    predictions = np.argmax(activation2.output,axis = 1)
    accuracy = np.mean(predictions == y)

    if loss < lowest_loss:
        print('New set of weights found, iteration: ', iteration, 'loss:', loss, 'acc:', accuracy)
        best_dense1_weights = dense1.weights.copy()
        best_dense1_biases = dense1.biases.copy()
        best_dense2_weights = dense2.weights.copy()
        best_dense2_biases = dense2.weights.copy()
        lowest_loss = loss
    else:
        dense1.weights = best_dense1_weights.copy()
        dense1.biases = best_dense1_biases.copy()
        dense2.weights = best_dense2_weights.copy()
        dense2.biases = best_dense2_biases.copy()

'''