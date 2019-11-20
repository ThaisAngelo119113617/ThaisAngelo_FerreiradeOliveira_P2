


#Questao 3 retificada:

def main():

    print('PRIMEIRO RETANGULO:')

    rxbx= float(input('BLX: '))
    rxby= float(input('BLY: '))
    rxax= float(input('TRX: '))
    rxay= float(input('TRY: '))

    print('SEGUNDO RETANGULO:')

    rybx= float(input('BLX: '))
    ryby= float(input('BLY: '))
    ryax= float(input('TRX: '))
    ryay= float(input('TRY: '))

    posicao1={'bottomleft':(rxbx,rxax),
             'TopRight':(rxby,rxay)}
    posiçao2={'bottomleft':(rybx,ryax),
             'TopRight':(ryby,ryay)}

    iscolisionDetected(rxbx, rxby, rxax, rxay, rybx, ryby, ryax, ryay)

def iscolisionDetected(rxbx, rxby, rxax, rxay, rybx, ryby, ryax, ryay):

    if (rxbx <= rybx <= rxax) and (rxby <= ryby <= rxay):

        print('Colisao detectda')
        return True

    if (rxbx <= ryax <= rxax) and (rxby <= ryay <= ryay):

         print('Colisao detectada')
         return True

    else:

        print('Colisao nao detectada')
        return False





main()
