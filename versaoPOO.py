class Gerente():
    def __init__(self):
        self._clientes = []
    def adcionarCliente(self, cliente):
        self._clientes.append(cliente)
    def obter_clientes(self):
        return self._clientes
    def obter_cliente(self,cpf,password):
        conta_em_questao = self._contas[cpf]
        if(conta_em_questao[password] == password):
            return conta_em_questao
        else:
            return False
    
class Cliente():
    def __init__(self):
        self.contas = []
        
    def adcionar_conta(self,conta):
        self.contas.append(conta)
        
    def obter_contas(self,cpf):
        return self.contas[cpf]
        
class PessoaFisica(Cliente):
    def __init__(self, cpf, data_nasc,nome,endereco,password):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nasc = data_nasc
        self._password = password
        
class Conta():
    def __init__(self, saldo, numero, cliente,historico,endereco):
        self._numero = numero
        self._agencia = 42
        self._historico = historico
        self._saldo = saldo
        self._endereco = endereco
        cliente.adcionar_conta(self)
        
    def realizar_transacao(self,valor,metodo):
        if(metodo == 'sacar'):
            if(valor > self._saldo):
                print('Impossível sacar, saldo insuficiente')
            else:
                self._saldo -= valor
        elif(metodo == 'depositar'):
            self._saldo += valor
        
class ContaCorrente(Conta):
    def __init__(self,saldo,numero,cliente,historico):
        super().__init__(saldo, numero, cliente,historico)
        
class Historico():
    def __init__(self):
        self.historico=[]
    
    def adcionarTransacao(self, valor, metodo):
        self.historico.append({'valor': valor, 'metodo': metodo})
        
class Interface():
    def __init__(self):
        pass
    
    def sacar(self,conta,valor):
        if(valor >= conta._saldo):
            print('Impossivel sacar, fundos insuficientes')
        else:
            conta._saldo -= valor
    def depositar(self,conta,valor):
        if(valor > 0):
            conta._saldo += valor   
            
class Main():
    def __init__(self):
        self.login()
            
    def criarUsuario (self):        
        cpf_pessoa = input('\nInsira seu CPF:\n\n')
        nome_pessoa = input('\nInsira seu nome completo:\n\n')
        primeiro_nome = nome_pessoa.split(' ')[0]
        data_nasc_pessoa = input('\nInsira sua data de nascimento\n\n')
        endereco_pessoa = input('\nInsira seu endereço:\n\n')
        confirmation_pessoa = input(f'\n{primeiro_nome}, você confirma os dados abaixo?\n\nNome: {nome_pessoa}\nCPF: {cpf_pessoa}\nData de nascimento: {data_nasc_pessoa}\nEndereço: {endereco_pessoa}\n\n[1]Sim, confirmo\n[2]Não, corrigir\n\n')
        if(confirmation_pessoa == '1'):            
            self.cliente = PessoaFisica(cpf=cpf_pessoa, data_nasc=data_nasc_pessoa,nome=nome_pessoa,endereco=endereco_pessoa)
        if(len(self.cliente.contas) < 1):
            self.criarConta(self.cliente)
    
    def criarConta (self,cliente):
        numeroConta = input('\nInsira um número para representar sua conta:\n\n')
        saldoInicial = float(input('\nDeseja adcionar um saldo inicial? Insira um valor ou zero para continuar:\n\n'))
        historico_conta_corrente = Historico()
        self.cliente.adcionar_conta(ContaCorrente(saldo=saldoInicial,cliente=self.cliente,numero=numeroConta,historico=historico_conta_corrente))
        print('\nConta criada com sucesso!\n\n')
        if(cliente):
            self.main_menu
        else:
            self.login()
        
    def login(self):
        comand = input('\nSeja bem vindo ao banco Exemplo!\n\n[1]Criar uma nova conta de usuário\n[2]Entrar em uma conta existente\n\n')
        if(comand == '1'):
            self.criarUsuario()
        elif(comand == '2'):
            cpf = input('\nPara acessar sua conta, insira seu CPF por favor:\n\n')
            senha = input('\nInsira sua senha, por favor\n\n')
            conta_em_questao = Gerente.obter_cliente(cpf,senha)
            if(conta_em_questao == False):
                print('\nDados incorretos, tente novamente\n\n')
                self.login()
            else:
                print(f'\nSeja bem vindo {conta_em_questao.nome.split(' ')[0]}!\n\n')
                self.main_menu(conta_em_questao)
                
    def main_menu(self,conta):
        comand = input(f'\nO que deseja fazer {conta._nome.split(' ')[0]}?\n\n[1]Extrato das contas:\n[2]Sacar:\n[3]Depositar:\n[4]Sobre minha conta:\n[5]Criar nova conta:\n\n')
        if(comand == '1'):
            contas = conta.obter_contas(conta._cpf)
            for conta in contas:
                print(f'Numero da conta: {Conta(conta)._numero}\nSaldo atual: {Conta(conta)._saldo}\n')
                for operacao in Conta(conta)._historico:
                    print(f'\n{operacao}\n')
            self.main_menu
        elif(comand == '2'):
            valor = float(input('\nInsira o valor a ser sacado:\n'))
            Interface.sacar(conta,valor)
            self.main_menu
        elif(comand == '3'):
            valor = float(input('\nInsira o valor a ser depositado:\n'))
            Interface.depositar(conta,valor)
            self.main_menu
        elif(comand == '4'):
            print(f'\nInformações da conta:\n\nNome do titular: {Cliente._nome}\nCPF: {Cliente._cpf}\nEndereço: {Cliente._endereco}\nData de nascimento: {Cliente._data_nasc}')
            self.main_menu
        elif(comand == '5'):
            self.criarConta(self.cliente)
            