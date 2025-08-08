ingresso = input ("tem ingresso? ")
idade = float(input ("qual idade? "))
autorisacao = input ("tem autorisacao? ")
vip = input ("voce esta na lista vip? ")


if (vip=="True" or ingresso=="True" ) and (int(idade) >= 18):
     print ("pode entrar")
elif (int(idade) < 12) :
     print("nao pode entar")
elif (autorisacao=="True") and (int(idade) >12 and (int(idade)<18)):
     print ("pode entrar com essa autorisacao")
else :
     print("voce nao vai entrar")