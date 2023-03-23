#Exercicio 1
filmes = ['Um Sonho de Liberdade', 'O Poderoso Chefão', 'Batman: O Cavaleiro das Trevas', 'O Poderoso Chefão II', 
'12 Homens e uma Sentença', 'A Lista de Schindler', 'O Senhor dos Anéis: O Retorno do Rei', 
'Pulp Fiction: Tempo de Violência', 'O Senhor dos Anéis: A Sociedade do Anel', 'Três Homens em Conflito']

print(filmes)

filmes.insert(0,'O Poderoso Chefão')
filmes.pop(2)
print(filmes)

#Exercicio 2
filmes_duplicados = ['Pulp Fiction: Tempo de Violência', 'O Senhor dos Anéis: A Sociedade do Anel', 'Três Homens em Conflito']


#Juntando uma lista de filmes com valores duplicados
filmes_all = filmes + filmes_duplicados
print(f'Lista de Filmes{filmes_all}')

#Filmes set por se tratar de conjuntos, os valores duplicados não serão exibidos
filmes_set = set(filmes_all)
print(f'Filmes Set -> {filmes_set}')

#Exercicio 3
#Repita os exercícios da parte 1 (listas). Os elementos da lista filmes devem ser dicionários
#no seguinte formato: {'nome': <nome-do-filme>, 'ano': <ano do filme>},
#'sinopse': <sinopse do filme>} 

dict_filmes = []
filmes = {'nome':'Batman: O Cavaleiro das Trevas','ano':2008, 'sinopse':'blablabla'}, {'nome':'O Poderoso Chefão II',
    'ano':1974,'sinopse':'blablabla'},{'nome': '12 Homens e uma Sentença','ano':1957,'sinopse':'blablablabla'}, {'nome': '12 Homens e uma Sentença',
    'ano':1957,'sinopse':'blablablabla'},{'nome':'A Lista de Schindler','ano':1993,
    'sinopse':'blablablabla!'},{'nome': 'O Senhor dos Anéis: O Retorno do Rei', 'ano':2003,'sinopse': 'blablabla!'},{'nome':'Pulp Fiction: Tempo de Violência',
    'ano':1994, 'sinopse':'blablabla'},{'nome':' O Senhor dos Anéis: A Sociedade do Anel','ano':2001,'sinopse':'blablabla'},{'nome':'Três Homens em Conflito',
    'ano':1966,'sinopse':'blablabla'}

dict_filmes.append(filmes)
print(dict_filmes)






 