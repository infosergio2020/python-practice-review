import os


numb = int(input("ingrese la cantidad de archivos a crear \n"))

for item in range(numb):
    # print("p-0{number}.py".format(number = item+1))
    if(item+1 >= 10):
        file = open("p-{number}.py".format(number = item+1), "w")
    else:
        file = open("p-0{number}.py".format(number = item+1), "w")
    file.close()