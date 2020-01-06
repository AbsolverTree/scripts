import os, glob

path = os.getcwd()
name = input("Nome('*' caso o nome não importe):\n")
formato = input("Formato(incluir o '.' antes):\n")
files = glob.glob(path+"/"+name+formato)

for i in files:
    os.unlink(i)