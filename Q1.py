#Questao 1 retificada:

#letra a:




def lerdata(data):

    # recebe a data no formato AAAA/MM/DD

    lista_split = data.split('/')
    dia = int(lista_split[2])
    mes = int(lista_split[1])
    ano = int(lista_split[0])
    data_dic = {'Ano': ano, 'Mes': mes, 'Dia': dia}

    return data_dic




#letra b:




def temativo(ativo):

    if len(ativo) == 4:

        ativo = ativo[:3]

    if ativo[0] == 'S':

        return True

    return False




#letra c:






def separastring(valor):

    valor_split = valor.split(':')
    return valor_split





#letra d:





def lerarq(file):

    file.seek(0)
    listalinhas = file.readlines()
    return listalinhas






#letra e:



def main():

    pessoas = []
    arquivo = open('cadastro.txt', 'r')



    dcadastro = { 'CPF' : '' , 'Nome' : '' , 'Data_de_nascimento' : '' , 'Data_de_cadastro' : '' , 'Ativo' : ''}

    arqlinhas = lerarq(arq)

    for index in range(len(arq_linhas)):

        dlinha = dcadastro.copy()

        dados = separastring(arqlinhas[index])

        dlinha['CPF'] = dados[0]
        dlinha['Nome'] = dados[1]
        dlinha['Data_de_nascimento'] = lerdata(dados[2])
        dlinha['Data_de_cadastro'] = lerdata(dados[3])
        dlinha['Ativo'] = temativo(dados[4])
        pessoas.append(dlinha)

    print(pessoas)
    arquivo.close()



main()
