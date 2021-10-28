import time
import random
import math

aulas_atribuidas = {}

inicial = [3,2  , 8,9   , 1,12  , 10,14   ,  8,4]

for linha in open('tab_professores.txt'):

  valores = linha.split(',')
  valores.pop(len(valores)-1) # retira o \n
  
  #print (valores)
  _prof = int(valores.pop(0))
  #print (_prof)
  #print (valores)
  _custo = int(valores.pop(0))
  #print (_custo)
  #print (valores)
	
  for i in valores:
    aulas_atribuidas.setdefault(i, [])
    aulas_atribuidas[i].append((_prof, _custo))
  
print (aulas_atribuidas)


'''
def imprimir_agenda(agenda):
    id_voo = -1
    for i in range(len(agenda) // 2):
        professor = pessoas[i][0] 
        disciplina = pessoas[i][1]
        id_voo += 1
        ida = disciplinas[(professor, disciplina)][agenda[id_voo]]
        id_voo += 1
        
        print('%10s%10s %5s-%5s R$%3s ' % (nome, origem, ida[0], ida[1], ida[2]))
        
print('imprimindo agenda sem otimização...')
imprimir_agenda(agenda)

print ('fim da impressão da agenda sem otimização...')

def get_minutos(hora):
    x = time.strptime(hora, '%H:%M')
    minutos = x[3] * 60 + x[4]
    return minutos



def funcao_custo(solucao):
    preco_total = 0
    ultima_chegada = 0
    primeira_partida = 1439 # 23 horas e 59 min em minutos é 23*60 + 59 = 1439
    
    id_voo = -1
    for i in range(len(solucao) // 2):
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][solucao[id_voo]]
        id_voo += 1
        volta = voos[(destino, origem)][solucao[id_voo]]
        
     #   preco_total += ida[2]
      #  preco_total += volta[2]
        
        if ultima_chegada < get_minutos(ida[1]):
            ultima_chegada = get_minutos(ida[1])
            
        if primeira_partida > get_minutos(volta[0]):
            primeira_partida = get_minutos(volta[0])
            
    total_espera = 0
    id_voo = -1
    for i in range(len(solucao) // 2):
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][solucao[id_voo]]
        id_voo += 1
        volta = voos[(destino, origem)][solucao[id_voo]]
        
        total_espera += ultima_chegada - get_minutos(ida[1])# soma o tempo de espera para o inicio da reunião
        total_espera += get_minutos(volta[0]) - primeira_partida # soma o tempo de espera para embarque após o final da reunião
        
    #if ultima_chegada > primeira_partida:
     #   preco_total += 50
 #   print("inicio da reunião: ")
 #   print(ultima_chegada)
 #   print("fim da reunião: ")
 #   print(primeira_partida)    
 #   print(total_espera)    
    return total_espera
        
funcao_custo(agenda)  


    

                    



def mutacao(dominio, passo, solucao):
    i = random.randint(0, len(dominio) - 1)
    mutante = solucao
    
    if random.random() < 0.5:
        if solucao[i] != dominio[i][0]:
            mutante = solucao[0:i] + [solucao[i] - passo] + solucao[i + 1:]
    else:
        if solucao[i] != dominio[i][1]:
            mutante = solucao[0:i] + [solucao[i] + passo] + solucao[i + 1:]
    
    return mutante

#print (agenda)
#x = mutacao(dominio, 2, agenda)
#print (x)



def cruzamento(dominio, solucao1, solucao2):
    i = random.randint(1, len(dominio) - 2)
    return solucao1[0:i] + solucao2[i:]






def genetico(dominio, funcao_custo, tamanho_populacao = 50, passo = 1,
             probabilidade_mutacao = 0.2, elitismo = 0.1, numero_geracoes = 1000):
    
    populacao = []
    for i in range(tamanho_populacao):
        solucao = [random.randint(dominio[i][0], dominio[i][1]) for i in range(len(dominio))]
        populacao.append(solucao)
    
    numero_elitismo = int(elitismo * tamanho_populacao)
    
    for i in range(numero_geracoes):
        custos = [(funcao_custo(individuo), individuo) for individuo in populacao] 
        custos.sort()
        individuos_ordenados = [individuo for (custo, individuo) in custos]# ordenando a população de acordo com seu custo
        
        populacao = individuos_ordenados[0:numero_elitismo] # seleção dos individuos mais aptos
        
        while len(populacao) < tamanho_populacao:
            if random.random() < probabilidade_mutacao:
                m = random.randint(0, numero_elitismo)
                populacao.append(mutacao(dominio, passo, individuos_ordenados[m])) # faz a mutação no individuo 'M'
            else:
                c1 = random.randint(0, numero_elitismo)
                c2 = random.randint(0, numero_elitismo)
                populacao.append(cruzamento(dominio, individuos_ordenados[c1], 
                                            individuos_ordenados[c2]))
                
    return custos[0][1]


solucao_genetico = genetico(dominio, funcao_custo)
custo_genetico = funcao_custo(solucao_genetico)
#print('imprimindo agenda otimizada...')
#imprimir_agenda(solucao_genetico)
#print('...com custo inicial total de:')
#print(funcao_custo(agenda))
#print('...com custo total de:')
print(funcao_custo(solucao_genetico))
#print('solucao:')
#print(solucao_genetico)

'''