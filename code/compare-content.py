import os

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

for z in iguais:
    if z[::-1] in iguais:
       iguais.remove(z[::-1])
if len(iguais) > 0:
    for x in iguais:
        print("O arquivo '{}' é igual ao '{}'".format(x[0],x[1]))
else:
    print("Todos os conteúdos são diferentes")