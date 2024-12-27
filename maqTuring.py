# Definindo os estados da máquina de Turing e suas ações
def maquina_turing(fita):
    # Configuração inicial
    estado = 'início'  # Estado inicial
    posicao = 0  # Posição inicial do cabeçote na fita

    while estado != 'parada':
        simbolo = fita[posicao]  # Ler o símbolo atual da fita

        # Início (estado inicial)
        if estado == 'início':
            if simbolo == '●':
                fita[posicao] = '●'  # Escreve o mesmo símbolo
                posicao += 1  # Move para a direita
                estado = '0'  # Próximo estado

        # Estado 0
        elif estado == '0':
            if simbolo == '0':
                fita[posicao] = '1'  # Escreve 1
                posicao += 1  # Move para a direita
            elif simbolo == '1':
                fita[posicao] = '0'  # Escreve 0
                posicao += 1  # Move para a direita
            elif simbolo == '⌂':  # Fim da leitura
                posicao -= 1  # Move para a esquerda
                estado = '1'  # Vai para o estado 1

        # Estado 1
        elif estado == '1':
            if simbolo == '0' or simbolo == '1':
                # Mantém o símbolo e move para a esquerda
                posicao -= 1
            elif simbolo == '●':
                # Quando encontra ●, para a máquina
                estado = 'parada'

    # Exibe o resultado final da fita após a execução da máquina
    return fita


# Exemplo de fita inicial
fita = ['●', '1', '0', '0', '0', '1', '1', '0', '0',
        '1', '0', '0', '1', '1', '1', '1', '0',
        '1', '0', '0', '0', '0', '1', '1', '0',
        '1', '0', '0', '0', '1', '0', '1', '0',
        '1', '0', '0', '0', '1', '1', '0', '1',
        '1', '0', '0', '1', '0', '1', '1', '0',
        '⌂']
resultado = maquina_turing(fita)

# Resultado da fita após a execução
print('Fita final:', ''.join(resultado))
