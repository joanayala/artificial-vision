#Developer: Joan C. Ayala
#Script: this program let us to generate one random number.

#randint => Generates Z numbers.
#uniform => Generates R numbers.

#libraries
import os
from random import randint, uniform 

#functions
def rand_integer() :
    nz = randint(1,10)
    return nz

def rand_real() :
    nr = uniform(1,10)
    return nr

def number_list() :
    i = 1
    while i <= 10 :
        x = randint(-100,100)
        print(x)
        i=i+1

#main
os.system("cls")
z = rand_integer()
r = rand_real()
print("The Z number generated is: ", z)
print("The R number generated is: ", r)
print("::::::::::::::::::::::::::::::::")
number_list()