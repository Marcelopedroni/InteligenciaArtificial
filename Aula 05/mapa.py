from cidade import Cidade
from adjacente import Adjacente

class Mapa:
    portoUniao = Cidade("Porto União")
    pauloFrontin = Cidade("Paulo Frontin")
    irati = Cidade("Irati")
    canoinhas = Cidade("Canoinhas")
    saoMatheus = Cidade("São Matheus")
    tresBarras = Cidade("Três Barras")
    palmeira = Cidade("Palmeira")
    contenda = Cidade("Contenda")
    lapa = Cidade("Lapa")
    mafra = Cidade("Mafra")
    balsaNova = Cidade("Balsa Nova")
    araucaria = Cidade("Araucária")
    tijucas = Cidade("Tijucas do Sul")
    campoLargo = Cidade("Campo Largo")
    curitiba = Cidade("Curitiba")
    saoJose = Cidade("São José dos Pinhais")
    
    portoUniao.addCidadeAdjacente(Adjacente(canoinhas))
    portoUniao.addCidadeAdjacente(Adjacente(pauloFrontin))

    portoUniao.addCidadeAdjacente(Adjacente(saoMatheus))

    pauloFrontin.addCidadeAdjacente(Adjacente(irati))
    pauloFrontin.addCidadeAdjacente(Adjacente(portoUniao))
    irati.addCidadeAdjacente(Adjacente(pauloFrontin))
    irati.addCidadeAdjacente(Adjacente(saoMatheus))
    irati.addCidadeAdjacente(Adjacente(palmeira))
    canoinhas.addCidadeAdjacente(Adjacente(portoUniao))
    canoinhas.addCidadeAdjacente(Adjacente(tresBarras))
    canoinhas.addCidadeAdjacente(Adjacente(mafra))
    saoMatheus.addCidadeAdjacente(Adjacente(portoUniao))
    saoMatheus.addCidadeAdjacente(Adjacente(tresBarras))
    saoMatheus.addCidadeAdjacente(Adjacente(lapa))
    saoMatheus.addCidadeAdjacente(Adjacente(irati))
    saoMatheus.addCidadeAdjacente(Adjacente(palmeira))
    tresBarras.addCidadeAdjacente(Adjacente(saoMatheus))
    tresBarras.addCidadeAdjacente(Adjacente(canoinhas))
    palmeira.addCidadeAdjacente(Adjacente(irati))
    palmeira.addCidadeAdjacente(Adjacente(saoMatheus))
    palmeira.addCidadeAdjacente(Adjacente(campoLargo))
    contenda.addCidadeAdjacente(Adjacente(lapa))
    contenda.addCidadeAdjacente(Adjacente(araucaria))
    contenda.addCidadeAdjacente(Adjacente(balsaNova))

    lapa.addCidadeAdjacente(Adjacente(contenda))
    lapa.addCidadeAdjacente(Adjacente(mafra))
    lapa.addCidadeAdjacente(Adjacente(saoMatheus))
    mafra.addCidadeAdjacente(Adjacente(lapa))
    mafra.addCidadeAdjacente(Adjacente(canoinhas))
    mafra.addCidadeAdjacente(Adjacente(tijucas))

    balsaNova.addCidadeAdjacente(Adjacente(contenda))
    balsaNova.addCidadeAdjacente(Adjacente(campoLargo))
    balsaNova.addCidadeAdjacente(Adjacente(curitiba))

    araucaria.addCidadeAdjacente(Adjacente(curitiba))
    araucaria.addCidadeAdjacente(Adjacente(contenda))
    tijucas.addCidadeAdjacente(Adjacente(mafra))
    tijucas.addCidadeAdjacente(Adjacente(saoJose))
    campoLargo.addCidadeAdjacente(Adjacente(palmeira))
    campoLargo.addCidadeAdjacente(Adjacente(balsaNova))
    campoLargo.addCidadeAdjacente(Adjacente(curitiba))

    curitiba.addCidadeAdjacente(Adjacente(campoLargo))
    curitiba.addCidadeAdjacente(Adjacente(balsaNova))
    curitiba.addCidadeAdjacente(Adjacente(araucaria))
    curitiba.addCidadeAdjacente(Adjacente(saoJose))
    saoJose.addCidadeAdjacente(Adjacente(tijucas))
    saoJose.addCidadeAdjacente(Adjacente(curitiba))
    


