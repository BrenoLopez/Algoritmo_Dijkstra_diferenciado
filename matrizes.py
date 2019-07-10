# lista tuplas e dicionarios 

# lista
lista = ['livro1',['livro2',2],['livro3',3]]
# print(lista)

# tuplas
grafo = {
    'a':{'b':{'peso':2,'dir':'e'},'c':{'peso':3,'dir':'e'}} ,'b':{'x':1}
}

dic = {
    'a': 13,
    'b': 0,
    'c': 52,
    'd': 0,
    'e': 0,
    'f': 79
}

newDic = { key: dic[key] for key in dic if dic[key] != 0 }

print(len(newDic))