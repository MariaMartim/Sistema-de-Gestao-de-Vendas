import crud as c

def create_tables():
    c.Base.metadata.create_all(c.engine)
    
def menu_create():
    print("\n O que deseja cadastrar? \n")
    print("1 - Cliente")
    print("2 - Produto")
    print("3 - Categoria")
    
    op = int(input("Digite a opção desejada: "))
    
    while True:
        if op == 1:
            c.criar_cliente()
        elif op == 2:
            c.criar_produto()
        elif op == 3:
            c.criar_categoria()
        elif op == 0:
            break
    
def menu_read():
    print("\n O que deseja listar? \n")
    print("1 - Clientes")
    print("2 - Produtos")
    print("3 - Categorias")
    
    op = int(input("Digite a opção desejada: "))

    while True:
        if op == 1:
            c.ler_clientes()
            break
        elif op == 2:
            c.ler_produtos()
            break
        elif op == 3:
            c.ler_categorias()
            break
        elif op == 0:
            break
    
def menu_update():
    print("\n O que deseja atualizar? \n")
    print("1 - Cliente")
    print("2 - Produto")
    print("3 - Categoria")
    
    op = int(input("Digite a opção desejada: "))
    
    while True:
        if op == 1:
            print("\n O que deseja atualizar? \n")
            print("1 - Nome")
            print("2 - Email")
            print("3 - Telefone")
            
        elif op == 2:
            id = int(input("Digite o id do produto: "))
            
            c.atualizar_produto()
        elif op == 3:
            c.atualizar_categoria()
        elif op == 0:
            break
    
    
def menu_delete():
    print("\n O que deseja deletar? \n")
    print("1 - Cliente")
    print("2 - Produto")
    print("3 - Categoria")
    
    

def menu():
    while True:
        print("\n Sistema de Gerenciamento \n")
        print("1 - Cadastro")
        print("2 - Listagem")
        print("3 - Atualizar")
        print("4 - Remover")
        print("0 - Sair")
        
        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            while True:
                menu_create()
                opcao = int(input("Digite a opção desejada: "))
                
                if opcao == 1:
                    c.criar_cliente()
                elif opcao == 2:
                    c.criar_produto()
                elif opcao == 3:
                    c.criar_categoria()
                elif opcao == 0:
                    break
                
        elif opcao == 2:
            while True:
                menu_read()
                break
                
        elif opcao == 3:
            while True:
                menu_update()
                opcao = int(input("Digite a opção desejada: "))
                
                if opcao == 1:
                    c.atualizar_cliente()
                elif opcao == 2:
                    c.atualizar_produto()
                elif opcao == 3:
                    c.atualizar_categoria()
                elif opcao == 0:
                    break
        elif opcao == 4:
            while True:
                menu_delete()
        elif opcao == 0:
            break
        
menu()