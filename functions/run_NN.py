def Node(weights, previous_layer, bias):
  e = 2.71828
  x = 0
  for b in range(len(previous_layer)):
    x = x + weights[b] * previous_layer[b]
  return(1 / (1 + e ** (-(x - bias))))


def function(previous_layer):
  NN = []
  with open("data/layers_size.txt") as f: layers_size = eval(f.read())
  with open("data/weights.txt") as f: all_weights = eval(f.read())
  with open("data/biases.txt") as f: all_biases = eval(f.read())

  NN.append(previous_layer)
  for i in range(len(layers_size) - 1):
    current_layer = []
    for a in range(layers_size[i + 1]):
      current_layer.append(Node(all_weights[i][a], previous_layer, all_biases[i][a]))
    previous_layer = current_layer
    NN.append(current_layer)

  return(NN)