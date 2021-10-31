import time
import random
import math

aulas_atribuidas = {}
professores_preco = [ #Equivalente à pessoas[] 
  ('prof1', '89'),
  ('prof2', '80'),
  ('prof3', '60'),
  ('prof4', '50'),
  ('prof5', '85'),
  ('prof6', '65'),
  ('prof7', '70'),
  ('prof8', '69'),
  ('prof9', '88'),
  ('prof10',' 76')]

inicial = [3,2  , 8,9   , 1,12  , 10,14   ,  8,4]
dominio = [(0,20)] * (len(professores_preco))

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
  
#print (aulas_atribuidas)


''' def funcao_custo(solucao):
    preco = 0
    prof_in = []
    id_aula = 0
    for i in range(len(solucao) // 2):
        professor = professores_preco[i][0]
        prof_in[i] = professor
        preco_aula = professores_preco[i][1]
        id_aula += 1
        preco = aulas_atribuidas([solucao[id_aula]])

       
        for j in range(len(prof_in)):
          #Calculando preço total
          if prof_in[i] == prof_in[j]:
            repetido = True
        if repetido:    
          preco_total = (1.5) * (preco_total + professores_preco[i][1])
        
        id_aula += 1
        

#funcao_custo(inicial)
'''

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

print (inicial)
x = mutacao(dominio, 1, inicial)
print (x)


def cruzamento(dominio, solucao1, solucao2):
    i = random.randint(1, len(dominio) - 1)
    return solucao1[0:i] + solucao2[i:]


def genetico(dominio, funcao_custo, tamanho_populacao = 50, passo = 1,
             probabilidade_mutacao = 0.2, elitismo = 0.1, numero_geracoes = 50):
    
  populacao = []
  for i in range(tamanho_populacao):
      solucao = [random.randint(dominio[i][0], dominio[i][1]) for i in range(len(dominio))]
      populacao.append(solucao)
  
  numero_elitismo = int(elitismo * tamanho_populacao)
  
  for i in range(numero_geracoes):
      custos = [(funcao_custo(individuo), individuo) for individuo in populacao] 
      custos.sort()
      individuos_ordenados = [individuo for (custo, individuo) in custos]
      
      populacao = individuos_ordenados[0:numero_elitismo] 
      
      while len(populacao) < tamanho_populacao:
          if random.random() < probabilidade_mutacao:
              m = random.randint(0, numero_elitismo)
              populacao.append(mutacao(dominio, passo, individuos_ordenados[m])) 
          else:
              c1 = random.randint(0, numero_elitismo)
              c2 = random.randint(0, numero_elitismo)
              populacao.append(cruzamento(dominio, individuos_ordenados[c1], 
                                          individuos_ordenados[c2]))
              
  return custos[0][1]


#solucao_genetico = genetico(dominio, funcao_custo)
#custo_genetico = funcao_custo(solucao_genetico)
#print('imprimindo agenda otimizada...')
#imprimir_agenda(solucao_genetico)
#print('...com custo inicial total de:')
#print(funcao_custo(agenda))
#print('...com custo total de:')
#print(funcao_custo(solucao_genetico))
#print('solucao:')
#print(solucao_genetico)
