# código que agenda tarefas

import subprocess # Eu estou utilizando este módulo para limpar o console
import time

tarefas = []

# Função principal que funciona como uma espécie de "Menu"
def main():
    removerPrint()
    valor = input('Agendador de tarefas\nSelecione a opção:\n1 - listar tarefas | 2 - adicionar tarefa | 3 - remover tarefa\n')
    
    if valor == '1':
        listarTarefas()
    elif valor == '2':
        adicionarTarefa()
    elif valor == '3':
        removerTarefa()
    else:
        removerPrint()
        print('Erro! Coloque algum valor')
        time.sleep(2)
        main()


def listarTarefas():
    removerPrint()
    tamanho = len(tarefas)
    if tamanho == 0:
        removerPrint()
        print('\nNão existem tarefas\n')
        time.sleep(1)
        main()
    else:
        for i, (tarefa) in enumerate(tarefas, 1):
            print(f'{i}. {tarefa}\n') # VERSÃO JAVASCRIPT --> console.log(`${i}. ${tarefa} (Data: ${data})`)
        input('Pressione \'Enter\' para voltar para o menu.')
    main()


def listarTarefas2():
    for i, (tarefa) in enumerate(tarefas, 1):
        print(f'{i}. {tarefa}')


def adicionarTarefa():
    removerPrint()
    tarefa = input('Nome da tarefa: ')
    tarefas.append((tarefa))

    if (tarefa == ''):
        removerPrint()
        print('Erro! Digite alguma coisa!')
        time.sleep(1)
        adicionarTarefa()

    choice = int(input('tarefa adicionada com sucesso!\nDeseja adicionar mais uma tarefa?\n1 - sim | 2 - não"\n'))
    if choice == 1:
        adicionarTarefa()
    elif choice == 2:
        main()
    else:
        removerPrint()
        print('Erro')
        time.sleep(1)
        main()
        

def removerTarefa():
    removerPrint()
    listarTarefas2()
    
    if len(tarefas) == 0:
        removerPrint()
        print("A lista de tarefas está vazia.")
        time.sleep(2)
        main()
    
    try:
        indice = int(input('\nDigite qual tarefa você deseja remover: ')) - 1  # Subtrai 1 do índice para corresponder ao índice da lista (que começa em 0)
        
        if 0 <= indice < len(tarefas):
            del tarefas[indice]
            choice = int(input('Tarefa removida com sucesso!\nDeseja remover outra tarefa?\n1 - Sim | 2 - Não: '))
            if choice == 1:
                removerTarefa()
            elif choice == 2:
                main()
            else:
                print('Erro')
        else:
            print('Índice fora dos limites da lista.')
            removerTarefa()
    except ValueError:
        print("Entrada inválida. Digite um número válido.")
        removerTarefa()


# Função para remover um item da lista
# def teste():
#     removerPrint()
#     listarTarefas2()
#     indice = int(input('\nDigite qual tarefa você deseja remover: '))
#     del tarefas[indice]
#     choice = input('Deseja remover outra tarefa?\n1 - Sim | 2 - Não')
#     if choice == '1':
#         removerTarefa()
#     elif choice == '2':
#         main()
#     else:
#         print('erro')


# Função para limpar o console
def removerPrint():
    # Este módulo escreve um código no console. Neste caso, o comando é o 'cls'
    subprocess.run(["cls"], shell=True) # limpa o console (funciona)


main()