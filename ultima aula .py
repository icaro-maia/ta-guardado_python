voce = 10
inimigo = 10 
espada = 3 
cura = 6
raionoinimigo = 6
ataquedomonstro = 5
print ("ola esse jogo e um rpg voce pode usar a espada curar ou jogar um raio qual assao voce tomara?")

for i in range(4):
    e = input("qual asao voce tomara?")
    
    if e == "raio":
        inimigo -= raionoinimigo
        print ("voce deu 6 de dano")
    elif  e == "espada":
        inimigo -= espada
        print ("voce deu 3 de dano")
    elif e == "cura":
        voce += cura
        print ("voce curou 6 de vida")
    else:
        print ("voce escreveu errado")
        break
    if inimigo <= 0:
        print ("inimigo derrotado")
        break
    
    voce -= ataquedomonstro
    print ("inimigo causou 5 de dano")

    if voce <= 0:
        print("voce morreu")
        break
    
