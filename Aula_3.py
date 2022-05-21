"""
Funções (def) - *args ** kwargs
"""

def func(*args,**kwargs):
    print(args)

    idade = kwargs['idade']
    print(idade)

lista = [1,2,3,4,5]
lista2 = [30,40,50,70]
func(*lista,*lista2,nome = 'Raul', sobrenome = 'Teles', idade = 23)