# NOME: Thais Angelo Ferreira de Oliveira
#PROVA COPIADA

#Questao 1 copiada :

# Letra a
data = input('Data:')
def lerdata(data):
    t_data=[data]
    lista_split = t_data.slipt('/')
    dia = lista_split[0]
    mes = lista_slipt[1]
    ano = lista_split[1:]
    dict_data={'Dia':dia,'Mes':mes,'Ano':ano}
    return dict_data

#letra b:

def temativo(ativo):
    listaativo = [ativo]
    if len(listaativo)== 4:
        listaativo=listaativo[-1:]
    listaativo[0].upper()= a
    if 'S' == a:
        return True
    else:
        return False

#letra c:

def separastring(valor):
    lista_valor=[valor]
    valor_split = lista_valor.split(':')
    listag = []
    index=(len(lista_valor)-1)/2
    for elem in range(index):
        listag+= valor_split[elem]
    listag+=valor_split[elem:]
    return listag


#letra d:

def lerarq(file):
    arq.seek(0)
    listalinha=arq.readline()
    return listalinhas


#letra e:

def main():
    file = open(arq.txt,'r')
    data = input('Data de nascimento: ')
    ativo = input('Possui ativo[s/n]:')
    cpf = int(input('CPF: '))
    nome = input('Nome: ')
    cadastro = input('Cadastro: ')
    dict= {'CPF': cpf , 'Nome': nome , 'Nasc': data , 'Ativo': ativo}



#Questao 2 copiada:
    
#letra a:

def InvM (a,b,c,d):
    det = (a*b)-(b*c)
    if det != 0:
        matriz[0][0] =(d/det)
        matriz[0][1] = (((-1)*b)/det)
        matriz[1][0] =(((-1)*b)/det)
        matriz[1][1] =(a/det)
        print('Matriz Inversa')
        for l in range (0 , 3):
            for c in range(0 , 3):
                print(matriz[l][c], \t )
            print()

#letra b:

def main():
    a = float(input('Entre com o numero da posiçao [0][0]: '))
    b = float(input('Entre com o numero da posiçao [0][1]: '))
    c = float(input('Entre com o numero da posiçao [1][0]: '))
    d = float(input('Entre com o numero da posiçao [1][1]: '))
    print('Matriz Anterior')
    matriz=[[a , b],[c , d]]
    for l1 in range(0 , 3):
        for c1 in range(0 ,3):
            print(matriz[l1][c1],/t)
    InvM(a , b , c, d)



#Questao 3 copiada:

def main():
    print('PRIMEIRO RETANCGULO:')

    rxbx= float(input('BLX: '))
    rxby= float(input('BLY: '))
    rxax= float(input('TRX: '))
    rxay= float(input('TRY: '))

    print('SEGUNDO RETANGULO:')

    rybx= float(input('BLX: '))
    ryby= float(input('BLY: '))
    ryax= float(input('TRX: '))
    ryay= float(input('TRY: '))

    posicao={'bottomleft':(rxbx,rxax,rybx,ryay),
             'TopRight':(rxby,rxay,ryby,ryay)}

    iscolisionDetected(rxbx, rxby, rxax, rxay, rybx, ryby, ryax, ryay)

def iscolisionDetected(rxbx, rxby, rxax, rxay, rybx, ryby, ryax, ryay):

    if (rxbx =< rybx =< rxax) and (rxby =< ryby =< rxay):

        print('Colisao detectda')
        return True

    if (rxbx =< ryax =< rxax) and (rxby =< ryay =< ryay):

         print('Colisao detectada')
         return True

    else:

        print('Colisao nao dtectada')
        return False
    



























































    
