def function():
  with open("data/layers_size.txt") as f: layers_size = eval(f.read())

  z = []
  for i in range(1, len(layers_size)):
    y = []
    for a in range(layers_size[i]):
      x = []
      for b in range(layers_size[i-1]):
        x.append(0)
      y.append(x)
    z.append(y)
  
  with open("data/weights.txt", "w") as f: f.write(str(z))

  z = []
  for i in range(1, len(layers_size)):
    y = []
    for a in range(layers_size[i]):
      y.append(0)
    z.append(y)
  
  with open("data/biases.txt", "w") as f: f.write(str(z))