# # Funcoes (def) em python - return 

# def funcao (var):
#     return var
#     print('Isso não será executado') #Quando encontra o return, acaba a função

# variavel = funcao('Valor que eu quero')
# print(variavel)

# if variavel:
#     print(variavel)
# else:
#     print('Nenhum valor!')


def divisao (n1, n2):
    if n2 == 0:      
        return
    return  n1 / n2

divide = divisao(8,0)

if divide:
    print(divide)
else:
    print('Conta inválida!')