import os, glob, shutil

path = os.getcwd()
# print(os.listdir())
name = input("Nome('*' caso o nome não importe):\n")
formato = input("Formato(incluir o '.' antes):\n")
files = glob.glob(path+"/"+name+formato)

for i in files:
    os.unlink(i)