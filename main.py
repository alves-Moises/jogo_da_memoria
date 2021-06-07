import random
import functions
from functions import game
def main():
    lista_resultado = random.sample(functions.lista_itens, 16)
    lista_imprimir = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
    print('x' * 10, 'Jodo da memória', 'x' * 10)

    #======= jogo looping ========
    while game == True:
        functions.imprimir_quadro(functions.linha_1, functions.linha_2, functions.linha_3, functions.linha_4)
        
        
        input()
        print('FimJogo')
main()
print()