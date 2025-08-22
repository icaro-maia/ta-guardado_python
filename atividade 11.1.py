import random
numeroescolhido = 0 
numerodeaaleatorio = int(input("de qual a qual numero voce quer "))
numerodechanses = int(input("quantas tentativas voce quer "))
numerocoreto = random.randint(1,numerodeaaleatorio)

while (numeroescolhido != numerocoreto) and numerodechanses > 0 : 
    numeroescolhido = int(input("coloque um numero: "))
    if numeroescolhido == numerocoreto:
        print("bom trabalho o numero era " + str(numeroescolhido))
    elif numeroescolhido > numerocoreto:
       print("tente um numero menor")
    else:  
      print("tente um numero maior")
    numerodechanses -= 1
    if numerodechanses == 0 and (numeroescolhido != numerocoreto):
        print("acabaram suas tentativas e o numero era " + str("numerodeaaleatorio"))
