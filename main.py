import random
import functions
def main():
    lista_imprimir = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
    print('x' * 10, 'Jodo da memória', 'x' * 10)
    lista_final = functions.lista_resultado #gabarito

    #======= looping do jogo ========
    game = True
    i = 0
    while game == True:
        functions.imprimir_quadro(functions.linha_1, functions.linha_2, functions.linha_3, functions.linha_4)
        print('Digite a primeira posição')
        print('=' * 30)
        posicao_1 = functions.pegar_posicao() #pegar posição e validar
        print('Digite a segunda posição')
        print('=' * 30)
        posicao_2 = functions.pegar_posicao() #pegar posição e validar
        print('posicação: ',posicao_1, posicao_2)

        functions.verificar_posicao(functions.linha_1, functions.linha_2, functions.linha_3, functions.linha_4, posicao_1, posicao_2)
        i += 1
    print('Fim de jogo')
main()
