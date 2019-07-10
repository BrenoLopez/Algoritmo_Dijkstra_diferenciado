grafo = {
    'a':{'b':{'peso':5,'dir':'d'},'c':{'peso':3,'dir':'e'},'d':{'peso':2,'dir':'d'}},
    'b':{'c':{'peso':3,'dir':'e'},'d':{'peso':1,'dir':'d'}},
    'c':{'d':{'peso':2,'dir':'d'}},
    'd':{'c':{'peso':2,'dir':'d'},'e':{'peso':4,'dir':'d'}},
    'e':{}
    }


def caminhoMinimo(grafo, origem, destino): #retorna a menor distancia de um No origem até um No destino e o caminho até ele

    atual = origem # guarda o nó atual 
    nosNaoVisitados = [] # armazena os nos nao visitados
    pesos = {} # armazena os pesos corresponde distanciAtual
    vetorAux = {}    
    pesoNoAtual = { }
    pesoNoAtual[atual] = [0,'']

    for no in grafo.keys():
        nosNaoVisitados.append(no)
        pesos[no] = [float('inf'),'ind']
    print('Nós não visitados: {} '.format(nosNaoVisitados))
    print('Pesos iniciais: {}'.format(pesos))
    pesos[atual] = ['',0,'ind']
    print('Pesos : {} '.format(pesos))
    nosNaoVisitados.remove(atual)
    print('Nó conhecido: {} '.format(atual))
    print('Nós não visitados: {} '.format(nosNaoVisitados))
    while nosNaoVisitados:        
        for vizinho, dados in grafo[atual].items():    
            # print(pesoNoAtual)
            calcPeso = dados['peso'] + pesoNoAtual[atual][0]
            if pesos[vizinho][0] == float('inf') or pesos[vizinho][0]> calcPeso : 
                # and pesos[vizinho][1] != 'e' 
                if dados['dir'] != 'e':            
                    pesos[vizinho] = [calcPeso,atual,dados['dir']]
                print('Pesos atuais: {}'.format(pesos))
                vetorAux[vizinho] =  [calcPeso,dados['dir']]
        novoVetorAux = {key: vetorAux[key] for key in vetorAux if vetorAux[key][1] != 'e' and vetorAux[key][1] == 'd'}        
        if novoVetorAux == {}: break
        # print(vetorAux)           
        menorPeso = min(novoVetorAux.items(), key=lambda x: x[1])                     
        atual= menorPeso[0]                          
        pesoNoAtual[atual] = [menorPeso[1][0],menorPeso[1][1]] 
        # print(pesoNoAtual)  
        nosNaoVisitados.remove(atual)        
        del vetorAux[atual] 
       
    print("A menor distância de {} até {} é: {}" .format(origem, destino, pesos[destino][0]))    
    print("O menor caminho é: {}".format(mostrarCaminho(pesos,origem, destino)))          
    

def mostrarCaminho(distancias,inicio, fim):
        if  fim != inicio:
            return "{} -- > {}".format(mostrarCaminho(distancias,inicio, distancias[fim][1]),fim)
            # print(distancias[fim][1])
        else:
            return inicio
caminhoMinimo(grafo,'a','c')


   