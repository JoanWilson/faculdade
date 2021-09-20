"""Trabalho final- Turma - Programação Computacional para Engenharia
Código:CK0179 Professor: Narcisio Arruda
Programa: Banco Virtual
Grupo 8
Joan Wilson Martins de Oliveira - 500671
Matheus Arrais Maia - 494050
Pedro Sanford Sampaio - 498931
Pedro de Souza Santos - 493445
Pedro Colares Carvalho - 493834
Comentários: O Programa é um banco virtual, que irá receber as contas dos usuários e será capaz
de realizar transações entre as contas desse banco, bem como saque e depósito.
Funções do Banco Virtual:
- Cadastro de contas
- Cancelamento de contas
- Saque
- Depósito
- Transação """


# BIBLIOTECAS

# Nenhuma Biblioteca externa foi usada

# FUNÇÕES

# Recebe a conta e a senha e cadastra uma conta
def cadastrar_conta(x, senha):
    conta = {'nome': x, 'senha': senha, 'saldo': float(0)}
    return contas.append(conta)


# Recebe a conta e a senha e remove a conta escolhida
def remover_conta(x, y):
    cont = 0
    for i in range(len(contas)):
        if contas[i]['nome'] == x:
            if contas[i]['senha'] == y:
                contas.pop(i)
                cont += 1
                print('Conta removida com sucesso!')
                break
    if cont == 0:
        print('Conta não encontrada')
    return 0


# Recebe a conta e a senha e retorna o saldo
def consultar_saldo(x, y):
    saldo = 0
    aux = 0
    for i in range(len(contas)):
        if contas[i]['nome'] == x:
            if contas[i]['senha'] == y:
                saldo = contas[i]['saldo']
                aux += 1
            else:
                saldo = 'Senha incorreta!'
                aux += 1
    if aux == 0:
        saldo = 'Conta não encontrada! '
    return saldo


# Recebe a conta, a senha e um valor, caso tenha saldo suficiente, irá subtrair o valor do saldo da conta digitada. Caso não tenha, retornará uma mensagem dizendo "Saldo insuficiente".
def realizar_saque(x, y, z):
    saldo = 0
    aux = 0
    for i in range(len(contas)):
        if contas[i]['nome'] == x:
            if contas[i]['senha'] == y:
                if contas[i]['saldo'] - z < 0:
                    saldo = 'Você não tem saldo suficiente!'
                else:
                    contas[i]['saldo'] -= z
                    saldo = contas[i]['saldo']
                aux += 1
    if aux == 0:
        saldo = 'Conta não encontrada!'
    return saldo


# Recebe a conta, a senha e um valor. Então, irá acrescentar o valor ao saldo da conta escolhida, retornando o saldo atual
def realizar_deposito(x, y, z):
    saldo = 0
    aux = 0
    for i in range(len(contas)):
        if contas[i]['nome'] == x:
            if contas[i]['senha'] == y:
                contas[i]['saldo'] = contas[i]['saldo'] + z
                saldo = contas[i]['saldo']
                aux += 1
            else:
                saldo = 'Senha incorreta!'
                aux += 1
    if aux == 0:
        saldo = 'Conta não encontrada! '
    return saldo


# Recebe duas contas, a senha da primeira conta e um valor. Então subtrai o valor da primeira conta, acrescentando na segunda conta e retorna o saldo atual da primeira conta
def transferencia(x, y, k, z):
    saldo = 0
    aux = 0
    for i in range(len(contas)):
        if contas[i]['nome'] == x:
            if contas[i]['senha'] == y:
                for j in range(len(contas)):
                    if contas[j]['nome'] == k:
                        if contas[i]['saldo'] - z < 0:
                            saldo = 'Você não tem saldo suficiente!'
                            break
                        else:
                            contas[i]['saldo'] -= z
                            contas[j]['saldo'] += z
                            saldo = contas[i]['saldo']
                            break
                    else:
                        saldo = 'Conta a ser receber transferência, não encontrada!'
                aux += 1
            else:
                saldo = 'Senha incorreta!'
                aux += 1
            aux += 1
    if aux == 0:
        saldo = 'Conta não encontrada! '
    return saldo


# REGISTROS

# Declara o array que irá armazenar as contas e sua quantidade
contas = []
quantidade_contas = len(contas)

# Carrega o arquivo 'dados.txt' em modo leitura e verifica se existe alguma informação dentro dele. Caso exista, irá criar registros com as informações do arquivo e acrescentar no vetor contas.
carregador = open('dados.txt', 'r')
tamanho = len(carregador.readlines())

# Retorna cursor para o inicio do arquivo
carregador.seek(0, 0)

# Verifica e realiza loop para acrescentar contas, caso existam.
if tamanho >= 1:
    for line in carregador:
        x = line.split()
        conta = {}
        conta['nome'] = x[0]
        conta['senha'] = x[1]
        conta['saldo'] = float(x[2])
        contas.append(conta)

# Fecha o arquivo.
carregador.close()

# CÓDIGO PRINCIPAL

# Inicializando o banco
print(''' 
====================================================================
-----    ----   --    -   -----   -----     -     -  ------   -----
|    |  |    |  | \   |  |       |     |    |     |  |       |
|----   |----|  |  \  |  |       |     |    |     |  |----   |
|    |  |    |  |   \ |  |       |     |    |     |  |       |
-----   |    |  |    \|	 |_____	 |_____|    |_____|  |       |_____

====================================================================
	   (Bem-vindo ao sistema de acesso do Banco Virtual UFC)''')

# Armazenando escolha do usuário
escolha = 1

# Loop de escolhas. O Programa inteiro é baseado num Loop, enquanto a operação não for igual a 0, o programa continuará num loop infinito.
while escolha != '0' or escolha >= 7:
    print('''===================================================================	
Operações disponiveis:
1. Cadastrar Conta
2. Remover Conta
3. Saldo 
4. Saque
5. Depósito
6. Transferência
0. Sair.
====================================================================''')

    # Receberá o valor da operação, em string, digitado pelo usuário
    escolha = input('Por favor, digite sua operação: \n')
    quantidade_contas = len(contas)

    # Cadastrar nova conta
    if escolha == '1':
        print('Cadastrar conta')
        name = input('Digite seu nome: ')
        name = name.upper()
        password = input('Digite sua senha: ')
        password = password.lower()
        aux = 0
        for i in range(len(contas)):
            if contas[i]['nome'] == name:
                aux += 1
        if aux == 0:
            cadastrar_conta(name, password)
            print('Conta cadastrada com sucesso!')
        else:
            print('Conta já existente')


    # Remover uma conta
    elif escolha == '2':
        print('Remover conta')
        if quantidade_contas == 0:
            print('Não existem contas para remover')
        else:
            name = input('Qual o nome da conta deseja remover? ')
            name = name.upper()
            password = input('Qual a senha dessa conta? ')
            password = password.lower()
            remover_conta(name, password)
            print('Conta removida com sucesso!')


    # Consultar saldo
    elif escolha == '3':
        print('Consultar saldo')
        if quantidade_contas == 0:
            print('Não existem contas para consultar!')
        else:
            name = input('Qual o nome da conta deseja consultar? ')
            name = name.upper()
            password = input('Qual é a senha da conta? ')
            password = password.lower()
            resultad = consultar_saldo(name, password)
            if type(resultad) == str:
                print(resultad)
            else:
                print('Seu saldo é de R${:.2f}'.format(consultar_saldo(name, password)))

    # Realizar saque
    elif escolha == '4':
        print('Realizar saque')
        if quantidade_contas == 0:
            print('Não existem contas para realizar o saque!')
        else:
            name = input('Qual conta deseja realizar o saque? ')
            name = name.upper()
            password = input('Qual é a senha da conta? ')
            password.lower()
            value = float(input('Quanto deseja retirar? '))
            resultado = realizar_saque(name, password, value)

            # O type serve para conferir o tipo de dado que a função irá retornar, caso for
            # String, não deu certo.
            if type(resultado) == str:
                print(resultado)
                conferir_saldo = input('Deseja conferir seu saldo?(s/n) ')
                conferir_saldo = conferir_saldo.lower()
                if conferir_saldo == 's':
                    saldo_saque_conferir = consultar_saldo(name, password)
                    if type(saldo_saque_conferir) == str:
                        print(saldo_saque_conferir)
                    else:
                        print('Seu saldo é de R$ {:.2f}'.format(saldo_saque_conferir))
                elif conferir_saldo == 'n':
                    print('Retornando ao menu principal')
                else:
                    print('Comando inválido, retornado ao menu principal')
            else:
                print('Seu saldo é de R$ {:.2f}'.format(resultado))

    # Realizar depósito
    elif escolha == '5':
        print('Realizar depósito')
        if quantidade_contas == 0:
            print('Não existem contas para realizar depósito!')
        else:
            name = input('Qual conta deseja depósitar? ')
            name = name.upper()
            password = input('Qual é a senha da conta? ')
            password = password.lower()
            value = float(input('Quanto deseja depositar? '))
            saldo_deposito = realizar_deposito(name, password, value)
            if type(saldo_deposito) == str:
                print(saldo_deposito)
            else:
                print('Depósito realizado com sucesso!')
                print('Seu saldo é de R$ {:.2f}'.format(saldo_deposito))




    # Transferência
    elif escolha == '6':
        print('Transferência')
        if quantidade_contas <= 1:
            print('Não existem contas para transferir! ')
        else:
            name = input('Qual a sua conta? ')
            name = name.upper()
            password = input('Qual é a senha da conta? ')
            password = password.lower()
            toname = input('Para qual conta deseja transferir? ')
            toname = toname.upper()
            value = float(input('Quanto deseja transferir? '))
            saldo_transferencia = transferencia(name, password, toname, value)
            if type(saldo_transferencia) == str:
                print(saldo_transferencia)
            else:
                print('Transferência realizada com sucesso!')
                print('Seu saldo ficou {:.2f}'.format(saldo_transferencia))

    # Sair do sistema
    elif escolha == '0':
        print('Obrigado por utilizar o sistema!')
        break

    # Em caso de erro
    else:
        print('Comando não reconhecido, tente novamente.')

# Essa parte irá atualizar todos os valores modificados, acrescentados e removidos no arquivo 'dados.txt'
if len(contas) > 0:
    # Abrirá o arquivo no modo escrita
    manipulador = open('dados.txt', 'w')

    # Escreverá as informações no arquivo, substituindo tudo!
    for i in range(len(contas)):
        manipulador.write('{0} {1} {2}\n'.format(contas[i]['nome'], contas[i]['senha'], contas[i]['saldo']))
    manipulador.close()

# Caso não tenha nada a acrescentar
else:
    print('')
