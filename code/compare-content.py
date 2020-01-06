import glob, os

mypath = os.getcwd()
files = []

for (paths, dirs, file) in os.walk(mypath):
    files.extend(file)

iguais = []
for i in files:
    c = 0
    with open(i, 'r') as arq:
        for j in files:
            with open(j, 'r') as arq2:
                if i != j:
                    if arq.read() == arq2.read():
                        add = [i,j]
                        iguais.append(add)
                else:
                    pass
print(iguais)