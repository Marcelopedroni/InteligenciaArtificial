from pilha import Pilha
class Profundidade:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Pilha(3)
        self.fronteira.empilhar(inicio)
        
    def buscar(self):
        topo = self.fronteira.getTopo()
        print('Topo: {}'.format(topo.nome))
        for a in topo.adjacentes:
            print('Verificando se já visitado: {}'.format(a.cidade.nome))
            if a.cidade.visitado == False:
                a.cidade.visitado = True
                self.fronteira.empilhar(a.cidade)
                Profundidade.buscar(self)
            temp = self.fronteira.desempilhar()
            if temp is None:
                break
            else:
                print('Desempilhou: {}'.format(temp.nome))
                

from mapa import Mapa
mapa = Mapa()
profundidade = Profundidade(mapa.portoUniao, mapa.curitiba)
profundidade.buscar()

