def auto_fill_NN():
    f = open("layers_size.txt")
    layers_size = eval(f.read())
    f.close()

    z = []
    for i in range(1, len(layers_size)):
        y = []
        for a in range(layers_size[i]):
            x = []
            for b in range(layers_size[i-1]):
                x.append(0)
            y.append(x)
        z.append(y)
    
    f = open("weights.txt", "w")
    f.write(str(z))
    f.close()

    z = []
    for i in range(1, len(layers_size)):
        y = []
        for a in range(layers_size[i]):
            y.append(0)
        z.append(y)
    
    f = open("biases.txt", "w")
    f.write(str(z))
    f.close()