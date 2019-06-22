def Node(weights, previous_layer, bias):
    x = 0
    for b in range(len(previous_layer)):
        x = x + weights[b] * previous_layer[b]
    return(1 / (1 + e ** (-(x - bias))))


def run_NN():
    input_layer = [1, 1]
    previous_layer = input_layer

    f = open("layers_size.txt")
    layers_size = eval(f.read())
    f.close()

    f = open("weights.txt")
    all_weights = eval(f.read())
    f.close()

    f = open("biases.txt")
    all_biases = eval(f.read())
    f.close
    
    for i in range(len(layers_size) - 1):
        for a in range(layers_size[i + 1]):
            current_layer = []
            current_layer.append(Node(all_weights[i][a], previous_layer, all_biases[i][a]))
        previous_layer = current_layer
        NN.append(current_layer)

    return(current_layer)


e = 2.71828
NN = []