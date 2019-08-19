manual_msg = """
What would you like to fill?

You may:
l: Fill size of the layers,
w: Fill the weights,
b: Fill the biases,
c: Or Cancel this action.
"""

def function():
  while True:
    user_req = input(manual_msg)
    if user_req == "l":
      with open("data/layers_size.txt", "w") as f:
        f.write(input("Enter the size of the layers: \n"))
      break
    elif user_req == "w":
      with open("data/weights.txt", "w") as f:
        f.write(input("Enter the weights: \n"))
      break
    elif user_req == "b":
      with open("data/biases.txt", "w") as f:
        f.write(input("Enter the biases: \n"))
      break
    elif user_req == "c": break
    else: print("Please enter 'l', 'w', or 'b'.")