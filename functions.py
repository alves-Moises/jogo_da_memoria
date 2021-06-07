# =================== variaveis de inicio =========================
lista_itens = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
linha_1 = ['x', 'x', 'x', 'x']
linha_2 = ['x', 'x', 'x', 'x']
linha_3 = ['x', 'x', 'x', 'x']
linha_4 = ['x', 'x', 'x', 'x']

game = True

# ========functions ========
def imprimir_quadro(line_1, line_2, line_3, line_4): 
    print('='  * 20)
    
    print('')
    i = 0
    print('| ', end = '')
    while i < 4:
        print(line_1[i], '', end = '')
        i += 1
    print('|')

    i = 0
    print('| ', end = '')
    while i < 4:
        print(line_2[i], '', end = '')
        i += 1
    print('|')

    i = 0
    print('| ', end = '')
    while i < 4:
        print(line_3[i], '', end = '')
        i += 1
    print('|')

    i = 0
    print('| ', end = '')
    while i < 4:
        print(line_4[i], '', end = '')
        i += 1
    print('|')