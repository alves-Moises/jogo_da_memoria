# import random
import functions
import os
import datetime




def main():
    print('x' * 10, 'Jodo da memória', 'x' * 10)

    #======= looping do jogo ========
    game = True
    i = 0

    while game == True:
        print('\n' * 150)
        #========================= IMPRIMIR A TABELA ====================================
        functions.imprimir_quadro(functions.linha_1, functions.linha_2, functions.linha_3, functions.linha_4)
        # imprimir todos os resultados: 
        # print(functions.linhaf_1)
        # print(functions.linhaf_2)
        # print(functions.linhaf_3)
        # print(functions.linhaf_4)
    #==== Pegar as coordenadas =====
        valid = False
        while not valid:
            print('Digite a primeira posição')
            print('=' * 30)
            posicao_1 = functions.pegar_posicao() #pegar posição e validar (x, y)
            print('Digite a segunda posição')
            print('=' * 30)
            posicao_2 = functions.pegar_posicao() #pegar posição e validar
            print('posicação: ', posicao_1, posicao_2)   #testando posicoes
            if posicao_1 != posicao_2:
                valid = True
            else:
                print('\nValores iguais. Digite novamente\n')

    #linha de teste conferir (1)
        linha_verificando_1 = [] 
        if posicao_1[0] == 0:
            linha_verificando_1 = functions.linhaf_1
        elif posicao_1[0] == 1:
            linha_verificando_1 = functions.linhaf_2
        elif posicao_1[0] == 2:
            linha_verificando_1 = functions.linhaf_3
        elif posicao_1[0] == 3:
            linha_verificando_1 = functions.linhaf_4
       
    # linha de teste conferir (2)
        linha_verificando_2 = [] 
        if posicao_2[0] == 0:
            linha_verificando_2 = functions.linhaf_1
        elif posicao_2[0] == 1:
            linha_verificando_2 = functions.linhaf_2
        elif posicao_2[0] == 2:
            linha_verificando_2 = functions.linhaf_3
        elif posicao_2[0] == 3:
            linha_verificando_2 = functions.linhaf_4
       
    #============== mesma linha =================
        if (posicao_1[0] == posicao_2[0]):  
            print('mesma linha')

            #posicao 0
            if posicao_1[0] == 0:  # pos_1 = x = 0
                temp_1 = ''
                temp_2 = ''
                temp_1 = functions.linhaf_1[posicao_1[1]]
                temp_2 = functions.linhaf_1[posicao_2[1]]
                nova_linha = [functions.linha_1[0], functions.linha_1[1], functions.linha_1[2], functions.linha_1[3]] #imprimir a grade com linha 0
               
                nova_linha[posicao_1[1]] = temp_1
                nova_linha[posicao_2[1]] = temp_2
                print(linha_verificando_1[posicao_1[1]], linha_verificando_2[posicao_2[1]])
                functions.imprimir_quadro(nova_linha, functions.linha_2, functions.linha_3, functions.linha_4)  #imprimir a grade com linha 0
                
                if linha_verificando_1[posicao_1[1]] == linha_verificando_2[posicao_2[1]]: #acertou
                    # print("verify", linha_verificando_1, linha_verificando_2)
                    print('linhas? ', linha_verificando_1, linha_verificando_2)
                    functions.linha_1[posicao_1[1]] = functions.linhaf_1[posicao_1[1]]
                    functions.linha_1[posicao_2[1]] = functions.linhaf_1[posicao_2[1]]
                    print('Acertou')
                else:
                    print('Errou')

            #posicao  1
            elif posicao_1[0] == 1:  # pos_2 = x = 1
                temp_1 = ''
                temp_2 = ''
                temp_1 = functions.linhaf_2[posicao_1[1]]
                temp_2 = functions.linhaf_2[posicao_2[1]]
                nova_linha = [functions.linha_2[0], functions.linha_2[1], functions.linha_2[2], functions.linha_2[3]] #pegar linha (nova)
               
                nova_linha[posicao_1[1]] = temp_1
                nova_linha[posicao_2[1]] = temp_2
                print(linha_verificando_1[posicao_1[1]], linha_verificando_2[posicao_2[1]])
                functions.imprimir_quadro(functions.linha_1, nova_linha, functions.linha_3, functions.linha_4)   #imprimir a grade com linha 1

                if linha_verificando_1[posicao_1[1]] == linha_verificando_2[posicao_2[1]]: #acertou
                    print("verify", linha_verificando_1, linha_verificando_2)
                    print('linhas? ', linha_verificando_1, linha_verificando_2)
                    functions.linha_2[posicao_1[1]] = functions.linhaf_2[posicao_1[1]]
                    functions.linha_2[posicao_2[1]] = functions.linhaf_2[posicao_2[1]]
                    print('Acertou')
                else:
                    print('Errou')
                
            #posicao 2
            elif posicao_1[0] == 2:  # pos_2 = x = 3
                temp_1 = ''
                temp_2 = ''
                temp_1 = functions.linhaf_3[posicao_1[1]]
                temp_2 = functions.linhaf_3[posicao_2[1]]
                nova_linha = [functions.linha_3[0], functions.linha_3[1], functions.linha_3[2], functions.linha_3[3]] #pegar linha (nova)
               
                nova_linha[posicao_1[1]] = temp_1
                nova_linha[posicao_2[1]] = temp_2
                print(linha_verificando_1[posicao_1[1]], linha_verificando_2[posicao_2[1]])
                functions.imprimir_quadro(functions.linha_1, functions.linha_2, nova_linha, functions.linha_4)   #imprimir a grade com linha 1

                if linha_verificando_1[posicao_1[1]] == linha_verificando_2[posicao_2[1]]: #acertou
                    print("verify", linha_verificando_1, linha_verificando_2)
                    print('linhas? ', linha_verificando_1, linha_verificando_2)
                    functions.linha_3[posicao_1[1]] = functions.linhaf_3[posicao_1[1]]
                    functions.linha_3[posicao_2[1]] = functions.linhaf_3[posicao_2[1]]
                    del linha_verificando_1
                    del linha_verificando_2
                    print('Acertou')
                else:
                    del linha_verificando_1
                    del linha_verificando_2
                    print('Errou')
            
            #posicao 3
            elif posicao_1[0] == 3:  # pos_2 = x = 4
                temp_1 = ''
                temp_2 = ''
                temp_1 = functions.linhaf_4[posicao_1[1]]
                temp_2 = functions.linhaf_4[posicao_2[1]]
                nova_linha = [functions.linha_4[0], functions.linha_4[1], functions.linha_4[2], functions.linha_4[3]] #pegar linha (nova) 
               
                nova_linha[posicao_1[1]] = temp_1
                nova_linha[posicao_2[1]] = temp_2
                print(linha_verificando_1[posicao_1[1]], linha_verificando_2[posicao_2[1]])
                functions.imprimir_quadro(functions.linha_1, functions.linha_2, functions.linha_3, nova_linha)   #imprimir a grade com linha 1

                if linha_verificando_1[posicao_1[1]] == linha_verificando_2[posicao_2[1]]: #acertou
                    print("verify", linha_verificando_1, linha_verificando_2)
                    print('linhas? ', linha_verificando_1, linha_verificando_2)
                    functions.linha_3[posicao_1[1]] = functions.linhaf_3[posicao_1[1]]
                    functions.linha_3[posicao_2[1]] = functions.linhaf_3[posicao_2[1]]
                    del linha_verificando_1
                    del linha_verificando_2
                    print('Acertou')
                else:
                    del linha_verificando_1
                    del linha_verificando_2
                    print('Errou')

        else: #linhas diferentes
        #================================= primeira posição ==================================================

            # pos_1:
            if posicao_1[0] == 0:
                temp_1 = functions.linhaf_1[posicao_1[1]]
                nova_linha_1 = [functions.linha_1[0], functions.linha_1[1], functions.linha_1[2], functions.linha_1[3]]
                nova_linha_1[posicao_1[1]] = temp_1
                
            #pos_2
            elif posicao_1[0] == 1:
                temp_1 = functions.linhaf_2[posicao_1[1]]
                nova_linha_1 = [functions.linha_2[0], functions.linha_2[1], functions.linha_2[2], functions.linha_2[3]]
                nova_linha_1[posicao_1[1]] = temp_1
                
            #pos_3
            elif posicao_1[0] == 2:
                temp_1 = functions.linhaf_3[posicao_1[1]]
                nova_linha_1 = [functions.linha_3[0], functions.linha_3[1], functions.linha_3[2], functions.linha_3[3]]
                nova_linha_1[posicao_1[1]] = temp_1
                
            #pos_4
            elif posicao_1[0] == 3:
                temp_1 = functions.linhaf_4[posicao_1[1]]
                nova_linha_1 = [functions.linha_4[0], functions.linha_4[1], functions.linha_4[2], functions.linha_4[3]]
                nova_linha_1[posicao_1[1]] = temp_1
                
            print(linha_verificando_1[posicao_1[1]], linha_verificando_2[posicao_2[1]]) #teste

        #================================= segunda posição ==================================================

            if posicao_2[0] == 0:
                temp_2 = functions.linhaf_1[posicao_2[1]]
                nova_linha_2 = [functions.linha_1[0], functions.linha_1[1], functions.linha_1[2], functions.linha_1[3]]
                nova_linha_2[posicao_2[1]] = temp_2

            #pos_2
            elif posicao_2[0] == 1:
                temp_2 = functions.linhaf_2[posicao_2[1]]
                nova_linha_2 = [functions.linha_2[0], functions.linha_2[1], functions.linha_2[2], functions.linha_2[3]]
                nova_linha_2[posicao_2[1]] = temp_2

            #pos_3
            elif posicao_2[0] == 2:
                temp_2 = functions.linhaf_3[posicao_2[1]]
                nova_linha_2 = [functions.linha_3[0], functions.linha_3[1], functions.linha_3[2], functions.linha_3[3]]
                nova_linha_2[posicao_2[1]] = temp_2

            elif posicao_2[0] == 3:
                temp_2 = functions.linhaf_4[posicao_2[1]]
                nova_linha_2 = [functions.linha_4[0], functions.linha_3[1], functions.linha_3[2], functions.linha_3[3]]
                nova_linha_2[posicao_2[1]] = temp_2

                print(linha_verificando_1[posicao_2[1]], linha_verificando_2[posicao_2[1]]) #teste

        #============================   imprimir linhas diferentes ======================================

            #pos_1 = 0
            if posicao_1[0] == 0 and posicao_2[0] == 1:
                functions.imprimir_quadro(nova_linha_1, nova_linha_2, functions.linha_3, functions.linha_4)

            elif posicao_1[0] == 0 and posicao_2[0] == 2:
                functions.imprimir_quadro(nova_linha_1, functions.linha_2, nova_linha_2, functions.linha_4)
                
            elif posicao_1[0] == 0 and posicao_2[0] == 3:
                functions.imprimir_quadro(nova_linha_1, functions.linha_2, functions.linha_3, nova_linha_2)

            #pos_1 = 1
            if posicao_1[0] == 1 and posicao_2[0] == 0:
                functions.imprimir_quadro(nova_linha_2, nova_linha_1, functions.linha_3, functions.linha_4)

            elif posicao_1[0] == 1 and posicao_2[0] == 2:
                functions.imprimir_quadro(functions.linha_1, nova_linha_1, nova_linha_2, functions.linha_4)

            elif posicao_1[0] == 1 and posicao_2[0] == 3:
                functions.imprimir_quadro(functions.linha_1, nova_linha_1, functions.linha_3, nova_linha_2)
                

            #pos_1 = 2
            if posicao_1[0] == 2 and posicao_2[0] == 0:
                functions.imprimir_quadro(nova_linha_2, functions.linha_2, nova_linha_1, functions.linha_4)

            elif posicao_1[0] == 2 and posicao_2[0] == 1:
                functions.imprimir_quadro(functions.linha_1, nova_linha_2, nova_linha_1, functions.linha_4)

            elif posicao_1[0] == 2 and posicao_2[0] == 3:
                functions.imprimir_quadro(functions.linha_1, functions.linha_2, nova_linha_1, nova_linha_2)
                
            #pos_1 = 3
            if posicao_1[0] == 3 and posicao_2[0] == 0:
                functions.imprimir_quadro(nova_linha_2, functions.linha_2, functions.linha_3, nova_linha_1)

            elif posicao_1[0] == 3 and posicao_2[0] == 1:
                functions.imprimir_quadro(functions.linha_1, nova_linha_2, functions.linha_3, nova_linha_1)

            elif posicao_1[0] == 3 and posicao_2[0] == 2:
                functions.imprimir_quadro(functions.linha_1, functions.linha_2, nova_linha_2, nova_linha_1)


            print(nova_linha_1, nova_linha_2)
            print(f'temp1: {temp_1}')
            print(f'temp1: {temp_2}')
        input('Digite enter para continuar')
    # ======= salvar as posições ===========
        if temp_1 == temp_2:

            # pos_1
            if posicao_1[0] == 0:
                functions.linha_1 = nova_linha_1
            elif posicao_1[0] == 1: 
                functions.linha_2 = nova_linha_1
            elif posicao_1[0] == 2: 
                functions.linha_3 = nova_linha_1
            elif posicao_1[0] == 3: 
                functions.linha_4 = nova_linha_1

            #pos_2
            if posicao_2[0] == 0:
                functions.linha_1 = nova_linha_2
            elif posicao_2[0] == 1: 
                functions.linha_2 = nova_linha_2
            elif posicao_2[0] == 2: 
                functions.linha_3 = nova_linha_2
            elif posicao_2[0] == 3: 
                functions.linha_4 = nova_linha_2
        
            print('acertou')
        if not ('x' in functions.linha_1) and not('x' in functions.linha_2) and not('x' in functions.linha_3) and not('x' in functions.linha_4):
            game = False


     
        
        


        i += 1
    print('Fim de jogo')
    print(f'Você completou o jogo em {i} jogadas.')
main()
