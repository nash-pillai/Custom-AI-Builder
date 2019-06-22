from functions import auto_fill_NN, man_fill_NN, run_NN


msg = """
What would you like to do?

You may:
a: Automatically fill the NN,
m: Manually fill the NN,
r: Run the NN,
c: Or Close the program.

Warning: When you automatically fill the NN ,it will not work until you backpropagate
"""


while True:
    user_req = input(msg)
    if user_req == "a":
        f = open("layers_size.txt", "w")
        f.write(input("Enter the size of the layers: \n"))
        f.close()
        auto_fill_NN()
    if user_req == "m":
        man_fill_NN()
    if user_req == "r": print(run_NN())
    if user_req == "c": break
    else: print("Please enter 'a', 'm', 'r', or 'c'.")