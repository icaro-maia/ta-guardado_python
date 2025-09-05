print ("alunos da aula sg paython")
lista  = ["clarice",
          "davi",
          "icaro",
          "joao",
          "niicolas",]
print(lista[0]) 
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
numero = input ("numero  da  chamada que o seu aluno esta ")
if 0<=int(numero)<=4:
    print (lista [int(numero)])
else:
    print("erro")
