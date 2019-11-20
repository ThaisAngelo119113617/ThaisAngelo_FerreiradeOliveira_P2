#Qeuestao 2 retificada:


#lertra a:

import copy

def invM(matriz):

    matriz = copy.deepcopy(matriz)
    det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    matriz[0][0] = matriz[1][1]
    matriz[1][1]= matriz[0][0]
    det = 1/det



    matriz[0][1] = -matriz[0][1]

    matriz[1][0] = -matriz[1][0]



    for linha in range(2):

        matriz[linha][0] *= det

    
    matriz[linha][1] *= det
    return matriz


#letra b:


def main():

    a = float(input('Entre como elemento[0][0]: '))
    b = float(input('Entre como elemento[0][1]:'))
    c = float(input('Entre como elemento[1][0]:'))
    d = float(input('Entre como elemento[1][1]:'))

    matriz = [[a , b],[c , d]]
    inverte_matriz = invM(matriz)
    print('-------Matriz Anterior-------')
    for linha in range(2):
        for coluna in range(2):
            print(matriz[linha][coluna], end=('\t'))

        print()

    print()
    print('-------------Matriz Inversa----------')
    for linha in range(2):
        for coluna in range(2):
            print(inverte_matriz[linha][coluna], end=('\t'))

        print()



main()
