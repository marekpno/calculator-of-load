from front_semi import front_semi
from front_semi_truck import front_semi_truck
import subprocess


# Welcome
print("Hallo! Here is caculator of maximium load weight for semitrailers")
# empty command to start
command = ""
# while loop to input values
while command != "exit":
    # input coomand
    command = input("Choice what do you want calculated?\n1. Semitrailer +"
                    " tractor unit \n2.Only Semitrailer\n>")
    # condition for semitrailer
    if command == "1":
        print("Your choice Semitrailer + tractor unit")
        # def from semi_truck
        b = front_semi_truck()
        # lunch script --> sympy_load.py
        subprocess.run(['python', 'sympy_load.py'])
        # break loop
        break
    # condition for semitrailer
    elif command == "2":
        print("Your choice semitrailer")
        # def from semi(without truck)
        a = front_semi()
        # lunch script --> sympy_load.py
        subprocess.run(['python', 'sympy_load_semitrailer.py'])
        # break loop
        break
    # for incorrect value
    else:
        print("Incorrect value!")
