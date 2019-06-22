manual_msg = """
What would you like to fill?

You may:
l: Fill size of the layers,
w: Fill the weights,
b: Or Fill the biases.
"""


def man_fill_NN():
    while True:
        user_req = input(manual_msg)
        if user_req == "l":
            f = open("layers_size.txt", "w")
            f.write(input("Enter the size of the layers: \n"))
            f.close()
            break
        elif user_req == "w":
            f = open("weights.txt", "w")
            f.write(input("Enter the weights: \n"))
            f.close()
            break
        elif user_req == "b":
            f = open("biases.txt", "w")
            f.write(input("Enter the biases: \n"))
            f.close()
            break
        else: print("Please enter 'l', 'w', or 'b'.")