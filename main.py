# código que agenda tarefas

import subprocess # Eu estou utilizando este módulo para limpar o console

tarefas = []

def listarTarefas2():
    for i, (tarefa) in enumerate(tarefas, 1):
        print(f'{i}. {tarefa}')

def listarTarefas():
    removerPrint()
    tamanho = len(tarefas)
    if tamanho == 0:
        print('\nNão existem tarefas\n')
        main()
    for i, (tarefa) in enumerate(tarefas, 1):
        print(f'{i}. {tarefa}') # VERSÃO JAVASCRIPT --> console.log(`${i}. ${tarefa} (Data: ${data})`)
    print('')
    main()

def adicionarTarefa():
    removerPrint()
    tarefa = input('Nome da tarefa: ')
    tarefas.append((tarefa))
    choice = int(input('tarefa adicionada com sucesso!\nDeseja adicionar mais uma tarefa?\n1 - sim | 2 - não"\n'))
    if choice == 1:
        adicionarTarefa()
    if choice == 2:
        main()
    else:
        print('Erro')
    
# Função para remover um item da lista
def teste():
    removerPrint()
    listarTarefas2()
    indice = int(input('\nDigite qual tarefa você deseja remover: '))
    del tarefas[indice]
    choice = int(input('Deseja remover outra tarefa?\n1 - Sim | 2 - Não'))
    if choice == 1:
        removerTarefa()
    elif choice == 2:
        main()
    else:
        print('erro')

def removerTarefa():
    removerPrint()
    listarTarefas2()
    
    if len(tarefas) == 0:
        print("A lista de tarefas está vazia.")
        main()
        return
    
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


# Função para limpar o console
def removerPrint():
    # Este módulo escreve um código no console. Neste caso, o comando é o 'cls'
    subprocess.run(["cls"], shell=True) # limpa o console (funciona)

# Função principal que funciona como uma espécie de "Menu"
def main():
    valor = int(input('Agendador de tarefas\nSelecione a opção:\n1 - listar tarefas | 2 - adicionar tarefa | 3 - remover tarefa\n'))
    
    if valor == 1:
        listarTarefas()
    if valor == 2:
        adicionarTarefa()
    if valor == 3:
        removerTarefa()

main()