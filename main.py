import pandas as pd
import ast
import os

def exibir_menu():
    print( 
    '''
    
    ***Academia FormaFit*** 
          
    Escolha uma opção:

    1. Cadastrar uma pessoa na academia
    2. Listar pessoas cadastradas
    3. Procurar dados de uma pessoa cadastrada
    
    ''')

def login_sistema():
    user = input("Usuário: ")
    password = input("Senha: ")
    
    if user == 'Admin' and password == 'admin':
        main()
    else:
        print("Tente novamente! O usuário ou a senha está errado.")

def verifyArchive(name_archive):
    path = os.path.join(str(os.getcwd()),name_archive)

    fileexists = os.path.isfile(path=path)
    
    if not fileexists:
        df = pd.DataFrame(columns=['id', 'nome', 'idade', 'peso', 'valor'])
        df.to_excel(name_archive, index=False)

def salvarArquivo(dados):
    df = pd.DataFrame(data=dados)
    
    if dados == []:
        print("Não foi possível salvar!")
    else:
        print("Salvo com sucesso")
        with pd.ExcelWriter('Dados da academia.xlsx', mode='a',if_sheet_exists='replace') as arquivo:
            df.to_excel(arquivo, index=False)

def readArchive(name_archive):
    df = pd.read_excel(name_archive, index_col=False)
    dataJson = df.to_json(orient="records")
    if len(dataJson) == 0:
        return []
    else:
        return ast.literal_eval(dataJson)

def main():
    file = "Dados da academia.xlsx"
    
    verifyArchive(file)

    pessoas = readArchive(file)

    while True:
        exibir_menu()
        opcao = int(input('Opção? '))
        if opcao == 1:
            cadastrar(pessoas)
        elif opcao == 2:
            listar()
        elif opcao == 3:
            buscar(pessoas)
        else:
            print('Opção inválida')

    
def cadastrar(pessoas):
    identificador = input('Id? ')
    nome = input('Nome? ')
    idade = int(input('Idade? '))
    peso = input('Peso? ')
    valor_pago = input('Valor pago? ')
    
    dados = {'id':identificador, 'nome':nome, 'idade':idade, 'peso':peso,'valor':valor_pago}
    pessoas.append(dados)
    salvarArquivo(pessoas)
    
def listar():
    dfs = pd.read_excel('Dados da academia.xlsx', sheet_name=0, header=0)
    print(dfs)  

def buscar(pessoas):
    identificador_pessoa = input('Id? ')
    for pessoa in pessoas:
        if pessoa['id'] == identificador_pessoa:
            id = pessoa['id']
            nome = pessoa['nome']
            idade = pessoa['idade']
            peso = pessoa['peso']
            valor = pessoa['valor']
            print(f'id: {id}, nome: {nome}, idade: {idade} peso: {peso}, valor mensal: {valor}')
            break
        else:
            print(f'Pessoa com id {identificador_pessoa} não encontrada')
        
login_sistema()