#Functions => def

import os

os.system("cls")

def add_placa (x) :
    placas_list.append(x)
    print ("Placas actualizadas: ", placas_list)
    print ("Len: ", len(placas_list)) #Show list lenght

#Declarando mis listas
placas_list = [123, 'AXZ123', 1234, 1000, 'WWW009'] 
fruits_list = ['APPLE', 'ORANGE', 'BANANA']
numbers_list = [1, 2, 3, '4' , 5 ,6, 7]

print ("Placas: ", placas_list)
print ("Len: ", len(placas_list)) #Show list lenght
print ("Frutas: ", fruits_list)
print ("Len: ", len(fruits_list)) #Show list lenght
print ("Números: ", numbers_list)
print ("Len: ", len(numbers_list)) #Show list lenght

for element in range(len(placas_list)) :
    print (placas_list[element])

#main
print(":::::::::::::::::::::::::::::::::::::::::::::::")
placa = input("Ingrese la placa del vehículo: ")
add_placa(placa)    