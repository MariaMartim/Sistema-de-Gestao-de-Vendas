import crud

def menu():
    while True:
        print("\n Sistema de Gerenciamento \n")
        print("\n1 - Cadastrar Cliente\n")
        print("2 - Cadastrar Produto\n")
        print("3 - Cadastrar Categoria\n")
        print("4 - Cadastrar Venda\n")
        print("5 - Listar Clientes\n")
        print("6 - Listar Produtos\n")
        print("7 - Listar Categorias\n")
        print("8 - Listar Vendas\n")
        print("9 - Atualizar Cliente\n")
        print("10 - Atualizar Produto\n")
        print("11 - Sair")
        
        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            criar_cliente()
        elif opcao == 2:
            criar_produto()
        elif opcao == 3:
            criar_venda()