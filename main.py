from functions import auto_fill, man_fill, run, backpropagate


msg = """
What would you like to do?

You may:
a: Automatically fill the NN,
m: Manually fill the NN,
r: Run the NN,
b: Backpropagate,
c: Or Close the program.
"""


while True:
  user_req = input(msg)
  if user_req == "a":
    with open("data/layers_size.txt", "w") as f:
      f.write(input("Enter the size of the layers(as a list): \n"))
    auto_fill.function()
  elif user_req == "m": man_fill.function()
  elif user_req == "r": print(run.function(eval(input("Enter the is the input(as a list): \n")))[-1])
  elif user_req == "b": backpropagate.function(int(input("Accuracy: ")), int(input("Times: ")))
  elif user_req == "c": break
  else: print("Please enter 'a', 'm', 'r', or 'c'.")