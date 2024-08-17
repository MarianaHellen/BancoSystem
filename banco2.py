import time
import os
import re
import random

CONTAS = {}


def limpar_terminal():
    os.system('clear')

def continuacao_boot():
    print("- Vamos lá! Crie uma senha de 5 dígitos, a senha deve conter pelo menos 2 letras ou símbolos.")
    senha = str(input())

    if len(senha) < 5:
        print("A senha deve conter no mínimo 5 caracteres.")
        senha = str(input())

    if len(re.findall(r'[a-zA-Z!@#$%^&*(),.?":{}|<>]', senha)) < 2:
        print("A senha deve ter pelo menos 2 letras ou símbolos.")
        senha = str(input())

    print("Verificando sua senha...")
    time.sleep(5)
    print("Senha válida!")
    limpar_terminal()
    print("- Perfeito! Para garantir que está tudo certo, preciso que confirme sua senha: ")
    confirma_senha = str(input())

    if confirma_senha == senha:
        print("Confirmando senha...")
        time.sleep(5)
        print("Senha confirmada!")
        CONTAS['Senha'] = confirma_senha
        limpar_terminal()
        criando_acesso()
    else:
        print("As senhas são diferentes! Crie sua senha novamente e confirme para desbloqueio de credenciais.")
        print("Aguarde o processamento ...")
        time.sleep(5)
        limpar_terminal()
        continuacao_boot()

def criando_acesso():
    num_conta = random.randint(1000,10000)
    num_agencia = random.randint(100,500)

    CONTAS['N° Conta'] = num_conta
    CONTAS['N° Agência'] = num_agencia

    print("- Suas credenciais de acesso foram criadas!\n")
    print("- A partir de agora você não irá mais precisar de mim...")
    print("- Mas saiba que adorei te ajudar neste processo!")
    print("- Ah! Só mais uma coisa! Após receber suas credenciais você irá precisar confirma-las logando em sua conta!")
    print("- Aguarde alguns segundos e veja você mesmo! Até logo!\n")
    time.sleep(7)
    print("Processando...")
    time.sleep(5)
    limpar_terminal()
    print("**** CREDENCIAIS DE ACESSO ****\n")
    print("------ Seja Bem-Vindo(a) ao seu primeiro acesso!-------\n")
    print("CREDENCIAIS PARA ACESSO:")
    print("N° Conta: ",num_conta)
    print("N° Agência:",num_agencia)

    print("Saia da sua conta para confirmar sua conta.")
    print("Clique 1 para sair...")
    sair = int(input())

    if sair == 1:
        limpar_terminal()
        abertura()
    else: 
        print("Pressione 1 para sair.")
        sair = int(input())

def abrir_conta():

    limpar_terminal()


    print("\n***** ABRIR CONTA | BANCO CENTRAL *****\n")
    print("- Olá! Me chamo Sara e irei te auxiliar na criação de sua primeira conta no Banco Central!")
    print("- Primeiro, preciso que me informe se voçê utiliza o Registro de Pessoa Física (CPF) ou Registro de Pessoa Jurídica (CNPJ):")
    tipo_registro = str(input())
    CONTAS['Registro'] = tipo_registro.upper()
    print("\nProcessando...")
    time.sleep(5)
    limpar_terminal()
    print("- Ótimo! Agora me diga o número de seu Registro (*Somente Números ): ")
    num_registro = int(input())
    CONTAS['N° Registro'] = num_registro
    print("\nProcessando...")
    time.sleep(5)
    limpar_terminal()
    print("- Perfeito! Agora me informe seu nome completo e sua data de nascimento :)")
    portador = str(input('Nome Completo: '))
    data_nasc = str(input('Data de Nascimento (utilize o formato 00/00/0000): '))
    CONTAS['Portador'] = portador
    CONTAS['DataNasc'] = data_nasc
    print("\nProcessando...")
    time.sleep(5)
    limpar_terminal()
    print("Você foi rápido! Antes de passarmos suas credenciais, preciso de confime seus dados:\n")
    print("Nome:",portador)
    print("Tipo de Registro:",tipo_registro)
    print("N° de Registro:",num_registro)
    print("Data de Nascimento:",data_nasc)
    print("\nSeus dados estão corretos?\n1-) Sim, confirmo meus dados\n2-) Não, há um dado incorreto")
    correcao = int(input())

    if correcao == 1:
        print("Seus dados estão sendo confirmados...")
        time.sleep(5)
        limpar_terminal()
        print("- Seus dados foram Confirmados!")
        print("- Eu e o Banco Central estamos felizes em ter você conosco!")
        print("- Agora irei te passar suas credenciais de acesso a sua conta...")
        print("- Mas antes preciso que você crie uma senha segura para seu acesso ser seguro!")
        print("- Evite utilizar nomes, como o seu e de pessoas próximas, números de telefone e datas de aniversários.")
        continuacao_boot()
    elif correcao == 2:
        limpar_terminal()
        print("- Pela nossa política de Veracidade, precisarei pedir que refaça seu cadastro com os dados corretos.\n")
        print("- Irei te redirecionar para nossa aba ' CRIAR CONTA ', para que possa preencher os campos com os dados corretos.")
        print("- Nos vemos em breve...")
        time.sleep(10)
        limpar_terminal()
        print("Aguarde alguns segundos que iremos te redirecionar...")
        time.sleep(5)
        limpar_terminal()
        CONTAS.clear()
        abrir_conta()
    else:
        print("Digite uma opção válida...\n")
        time.sleep(3)
        print("\nSeus dados estão corretos?\n1-) Sim, confirmo meus dados\n2-) Não, há um dado incorreto")
        correcao = int(input())

def conta_usuário():

    conta_poupança = 0
    conta_corrente = 0

    print("----- Para onde Vamos? -----\n")
    print("1-) Verificar meu Saldo Atual\n2-) Realizar Saque\n3-) Realizar Depósito\n4-) Sair")
    acao = int(input())

    if acao == 1:
        limpar_terminal()
        print("**** VERIFICAÇÃO DE SALDO ****\n")
        print("- Olá, seja bem-vindo(a) a sua verificação de saldo!")
        print("- Qual saldo gostaria de verificar?\n1-) CONTA CORRENTE\n2-) CONTA POUPANÇA")
        acao_saldo = int(input())

        if acao_saldo == 1:
            print(f"- Seu saldo atual em CONTA CORRENTE é de: R$ {conta_corrente}")
            print("1-) Voltar.")
            voltar = int(input())
            if voltar == 1:
                conta_usuário()
            else:
                print("Digite uma opção válida")
                acao_saldo = 1
        elif acao_saldo == 2:
            print(f"- Seu saldo atual em CONTA CORRENTE é de: R$ {conta_poupança}")
            print("1-) Voltar.")
            voltar = int(input())
            if voltar == 1:
                conta_usuário()
            else:
                print("Digite uma opção válida")
                acao_saldo = 2
    elif acao == 2:

        print("**** SAQUES ****\n")
        print("- De qual conta gostaria de realizar o saque?\n1-) CONTA CORRENTE\n2-) CONTA POUPANÇA")
        conta_saque = int(input())

        if conta_saque == 1:
            print("** REALIZAR SAQUE EM : CONTA CORRENTE **\n")
            print("- Valor de Saque: ")
            valor_saque: float(input())

            if conta_corrente < valor_saque:
                print("Realize um depósito a sua conta para realizar saques.")
                print(f"- Seu saldo atual em CONTA CORRENTE é de: R$ {conta_corrente}")
                print("Iremos te redirecionar para o início...")
                time.sleep(7)
                limpar_terminal()
                print("Aguarde...")
                time.sleep(5)
                limpar_terminal()
                conta_usuário()
            elif conta_corrente > valor_saque:
                conta_corrente = conta_corrente - valor_saque

                print("Saque sendo efetuado...")
                time.sleep(5)
                limpar_terminal()
                print("Saque realizado com sucesso!")
                time.sleep(3)
                print(f"- Seu saldo atual em CONTA CORRENTE é de: R$ {conta_corrente}")
                print("\nEstamos de redirecionando para o início...")
                time.sleep(7)
                print("Aguarde...")
                time.sleep(5)
                limpar_terminal()
                conta_usuário()
            else:
                print("Digite uma opção válida.")
                print("Iremos te redirecionar para o início...")
                time.sleep(7)
                limpar_terminal()
                print("Aguarde...")
                time.sleep(5)
                limpar_terminal()
                conta_usuário()
        elif conta_saque == 2:

            print("** REALIZAR SAQUE EM : CONTA POUPANÇA **\n")
            print("- Valor de Saque: ")
            valor_saque: float(input())

            if conta_poupança < valor_saque:
                print("Realize um depósito a sua conta para realizar saques.")
                print(f"- Seu saldo atual em CONTA CORRENTE é de: R$ {conta_corrente}")
                print("Iremos te redirecionar para o início...")
                time.sleep(7)
                limpar_terminal()
                print("Aguarde...")
                time.sleep(5)
                limpar_terminal()
                conta_usuário()
            elif conta_poupança > valor_saque:
                conta_poupança = conta_poupança - valor_saque

                print("Saque sendo efetuado...")
                time.sleep(5)
                limpar_terminal()
                print("Saque realizado com sucesso!")
                time.sleep(3)
                print(f"- Seu saldo atual em CONTA CORRENTE é de: R$ {conta_poupança}")
                print("\nEstamos de redirecionando para o início...")
                time.sleep(7)
                print("Aguarde...")
                time.sleep(5)
                limpar_terminal()
                conta_usuário()
            else:
                print("Digite uma opção válida.")
                print("Iremos te redirecionar para o início...")
                time.sleep(7)
                limpar_terminal()
                print("Aguarde...")
                time.sleep(5)
                limpar_terminal()
                conta_usuário()
    elif acao == 3:
        print("*** REALIZAR DEPÓSITO ***\n")
        print("- Em qual conta gostaria de realizar o depósito?\n1-) CONTA CORRENTE\n2-) CONTA POUPANÇA")
        conta_deposito = int(input())

        if conta_deposito == 1:
            limpar_terminal()

            valor_deposito = float(input('Valor a ser depositado: '))
            conta_corrente = conta_corrente + valor_deposito

            print("Realizando Depósito...")
            time.sleep(7)
            print("Depósito realizado com Sucesso!")
            print(f"- Saldo atual da sua CONTA CORRENTE é de: R$ {conta_corrente}.")
            print("Iremos te redirecionar para a aba inicial...")
            time.sleep(7)
            limpar_terminal()
            conta_usuário()
        elif conta_deposito == 2:
            limpar_terminal()

            valor_deposito = float(input('Valor a ser depositado: '))
            conta_poupança = conta_poupança + valor_deposito

            print("Realizando Depósito...")
            time.sleep(7)
            print("Depósito realizado com Sucesso!")
            print(f"- Saldo atual da sua CONTA CORRENTE é de: R$ {conta_corrente}.")
            print("Iremos te redirecionar para a aba inicial...")
            time.sleep(7)
            limpar_terminal()
            conta_usuário()
        else:
            print("Digite uma opção válida.")
            print("Iremos te redirecionar para a aba inicial...")
            time.sleep(7)
            limpar_terminal()
            conta_usuário()
    elif acao == 4:
        limpar_terminal()
        print("Saindo da sua conta...")
        time.sleep(5)
        limpar_terminal()
        abertura()

def entrar_conta():
    limpar_terminal()
    print("\n***** ENTRAR NA MINHA CONTA | BANCO CENTRAL *****\n")

    print(CONTAS)

    entrada_agencia = int(input('* N° Agência: '))
    entrada_conta = int(input('* N° Conta: '))


    if CONTAS['N° Agência'] == entrada_agencia and CONTAS['N° Conta'] == entrada_conta:
        recebe_senha = input('Senha de acesso: ')
        if recebe_senha == CONTAS["Senha"]:
            limpar_terminal()
            print(f"\n**** SEJA BEM-VINDO(A) {CONTAS['Portador']}! ****\n")
            conta_usuário()
        else:
            print("Senha incorreta.")
            entrar_conta()
        
    else:
        limpar_terminal()
        print("Conta não encontrada.")
        print("\n- Crie sua conta para realizar transações, depósitos, pagamentos e muito mais!\n")
        print("1- Criar Conta.\n2- Sair.")
        escolha = int(input())

        if escolha == 1:
            abrir_conta()
        elif escolha == 2:
            print("\nSaindo...")
            time.sleep(5)
            print("*** BANCO CENTRAL FECHADO ***\n")
            exit()
        else:
            print("Valor inválido...")
            exit()

def abertura():

    CONTAS = {}

    print("\n***** SEJA BEM-VINDO(A) AO BANCO CENTRAL *****\n")
    print("Qual ação gostaria de tomar?:\n")
    print(" _______________________________\n")
    print("| ID |        AÇÃO              |\n")
    print("|----|--------------------------|\n")
    print("| 1  |    ABRIR CONTA           |\n")
    print("| 2  | ENTRAR NA MINHA CONTA    |\n")
    print("|----|--------------------------|\n")

    acao = int(input('\n*Utilize o ID para indicar a ação desejada: '))

    if acao == 1:
        abrir_conta()
    elif acao == 2:
        entrar_conta()
    else:
        print("Por favor, solicite um ID existente.")
        print("Aguarde...")
        time.sleep(5)
        limpar_terminal()
        abertura()

abertura()

