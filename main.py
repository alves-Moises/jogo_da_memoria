# import random
import functions

def main():
    # lista_imprimir = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
    # lista_final = functions.lista_resultado #gabarito
    print('x' * 10, 'Jodo da memória', 'x' * 10)

    #======= looping do jogo ========
    game = True
    i = 0
    while game == True:

        functions.imprimir_quadro(functions.linha_1, functions.linha_2, functions.linha_3, functions.linha_4)
        print('Digite a primeira posição')
        print('=' * 30)
        posicao_1 = functions.pegar_posicao() #pegar posição e validar (x, y)
        print('Digite a segunda posição')
        print('=' * 30)
        posicao_2 = functions.pegar_posicao() #pegar posição e validar
        print('posicação: ', posicao_1, posicao_2)   #testando posicoes

        linha_verificando_1 = [] #linha de teste conferir (1)
        if posicao_1[0] == 0:
            linha_verificando_1 = functions.linhaf_1
        elif posicao_1[0] == 1:
            linha_verificando_1 = functions.linhaf_2
        elif posicao_1[0] == 2:
            linha_verificando_1 = functions.linhaf_3
        elif posicao_1[0] == 3:
            linha_verificando_1 = functions.linhaf_4
       
       
        linha_verificando_2 = [] #linha de teste conferir (2)
        if posicao_2[0] == 0:
            linha_verificando_2 = functions.linhaf_1
        elif posicao_2[0] == 1:
            linha_verificando_2 = functions.linhaf_2
        elif posicao_2[0] == 2:
            linha_verificando_2 = functions.linhaf_3
        elif posicao_2[0] == 3:
            linha_verificando_2 = functions.linhaf_4
       
        # print(posicao_1[0])
        # print(posicao_2[0])

        if (posicao_1[0] == posicao_2[0]):   #mesma linha
            print('mesma linha')

            if posicao_1[0] == 0:
                nova_linha = functions.linha_1
                nova_linha[posicao_1[1]] = functions.linhaf_1[posicao_1[1]]
                nova_linha[posicao_2[1]] = functions.linhaf_1[posicao_2[1]]
                if linha_verificando_1[posicao_1[1]] == linha_verificando_2[posicao_2[1]]:   #acertou
                    functions.imprimir_quadro(nova_linha, functions.linha_2, functions.linha_3, functions.linha_4)
                    print(linha_verificando_1, linha_verificando_2)
                    functions.linha_1[posicao_1[1]] = functions.linhaf_1[posicao_1[1]]
                    functions.linha_1[posicao_2[1]] = functions.linhaf_1[posicao_2[1]]
                    print('Acertou')
                else:
                    print('Errou')

            # elif posicao_1[0] == 1:
            #     functions.linha_1[posicao_1[0]] = functions.linhaf_1[posicao_1[0]]

            # elif posicao_1[0] == 2:
            #     functions.linha_2[posicao_1[0]] = functions.linhaf_2[posicao_1[0]]

            # elif posicao_1[0] == 3:
            #     functions.linha_3[posicao_1[0]] = functions.linhaf_3[posicao_1[0]]

                # imprimir tabela final
            # print(functions.linhaf_1)
            # print(functions.linhaf_2)
            # print(functions.linhaf_3)
            # print(functions.linhaf_4)


        # else:
            
        
        

        print('asd', linha_verificando_1, linha_verificando_2)

        i += 1
    print('Fim de jogo')
main()
