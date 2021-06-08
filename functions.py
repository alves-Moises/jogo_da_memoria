import random

# =================== variaveis de inicio =========================
lista_itens = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]  
lista_resultado = random.sample(lista_itens, 16)

#l --- linhas apresentadas ---
linha_1 = ['x', 'x', 'x', 'x']
linha_2 = ['x', 'x', 'x', 'x']
linha_3 = ['x', 'x', 'x', 'x']
linha_4 = ['x', 'x', 'x', 'x']

# ----- linhas gabarito --------
linhaf_1 = lista_resultado[0:4]
linhaf_2 = lista_resultado[4:8]
linhaf_3 = lista_resultado[8:12]
linhaf_4 = lista_resultado[12:]


# ========functions ========
def imprimir_quadro(line_1 = linha_1, line_2 = linha_2, line_3 = linha_3, line_4 = linha_4): 
    print('='  * 30)
    lista_linhas = [line_1, line_2, line_3, line_4]
    for lista in lista_linhas:
        print('')
        i = 0
        print('| ', end = '')
        while i < 4:
            print(lista[i], '', end = '')
            i += 1
        print('|', end = '')
    print('\n')
    print('='  * 30)

def pegar_posicao():
    #pega posição  
    def main():  
        valid = False    
        while not valid:
            x = validar_inteiro('linha ')
            y = validar_inteiro('coluna')
            valid = verificar_posicao(x, y)

        posicao = [x, y]
        return posicao

    def validar_inteiro(texto):  #valida as entradas
        valid = False
        while not valid:
            try:
                x = int(input(f'Digite um valor para a {texto}: '))
            except ValueError:
                print('\nValor inválido. Digite novamente')
            else:
                return x

    def verificar_posicao(x, y): #verificar se posição é válida
        if ((x != 0) and (x != 1) and (x != 2) and (x != 3)) or ((y != 0) and (y != 1) and (y != 2) and (y != 3)):
            print('posição inválida')
            return False
        else:
            if x == 0:
                if linha_1[y] != 'x':
                    print('Célula já revelada. Digite uma posição válida.')
                    return False
                else:
                    return True

            elif x == 1:
                if linha_2[y] != 'x':
                    print('Célula já revelada. Digite uma posição válida.')
                    return False
                else:
                    return True
            elif y == 2:
                if linha_3[y] != 'x':
                    print('Célula já revelada. Digite uma posição válida.')
                    return False
                else:
                    return True
            elif x == 3:
                if linha_3[y] != 'x':
                    print('Célula já revelada. Digite uma posição válida.')
                    return False
                else:
                    return True
            else:
                return True

    return main()





