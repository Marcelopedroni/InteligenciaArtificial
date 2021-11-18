# -*- coding: utf-8 -*-

import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)



entradas = np.array([[0,0],
                     [0,1],
                     [1,0],
                     [1,1]])

saidas = np.array([[1],[0],[0],[1]])

pesos1 = np.array([[-0.424, -0.740, -0.961], # pesos de p1 a p6
                   [0.358, -0.577, -0.469]])
    
pesos2 = np.array([[-0.017], [-0.893], [0.148]])



ciclos_treinamento = 10000
taxaAprendizagem = 10


for j in range(ciclos_treinamento):
    
    camadaEntrada = entradas

    # faz o produto escalar da primeira camada e calcula saida da primeira camada

    somaSinapse1 = camadaEntrada.dot(pesos1)
    camadaOculta = sigmoid(somaSinapse1)
  #  print("camada oculta")
   # print(camadaOculta)

    # faz o produto escalar da sengunda camada e calcula saida da segunda camada
    somaSinapse2 = camadaOculta.dot(pesos2)
    camadaSaida = sigmoid(somaSinapse2)
    print("camada saida")
    print(camadaSaida)

    # calcula erro na camada de saida
    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida)) # usa obsoluto para considerar erros negativos e positivos
    print("Erro: " + str(mediaAbsoluta))

    # calcula a derivada da saida e encontra o Delta de saida, dado ´pelo erro da camada x a derivada
    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida
   # print ("delta saida")
   # print (deltaSaida)
    
    
    pesos2Transposta = pesos2.T
    #print ("pesos2")
   # print (pesos2)
   # print ("pesos2.T")    
   # print(pesos2Transposta)
    deltaSaidaXPeso = deltaSaida.dot(pesos2Transposta)
    #print (".dot de pesos2. T por deltaSaida")
    #print (deltaSaidaXPeso)
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)

     # atualização dos pesos por backpropagation
    camadaOcultaTransposta = camadaOculta.T
    pesosNovo2 = camadaOcultaTransposta.dot(deltaSaida)
    pesos2 = (pesos2) + (pesosNovo2 * taxaAprendizagem)
    
    camadaEntradaTransposta = camadaEntrada.T
    pesosNovo1 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos1 = (pesos1) + (pesosNovo1 * taxaAprendizagem)

print ("Peso 1 {}".format(pesos1))
print ("Peso 2{}".format(pesos2))
