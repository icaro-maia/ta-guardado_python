perguntas = ["qual o maior planeta do sistema solar", "qual o maior pais do planeta", "qual o maior continente da terra"]
resposta = ["jupter", "rusia","eurasia"]
ponto = 0

for i in range(3):
    print (perguntas [i])
    valor =  input ("qual sua resposta ")
    
    if valor == resposta[i]:
        ponto+= 1
        print ("resposta correta ")
    elif valor == "":
        print ("ta faltando nada nao?")
    else :
         print ("errou tente denovo")


print ("parabems voce acertou com " + str(ponto) + " pontos")
