import crud as c

def create_tables():
    c.Base.metadata.create_all(c.engine)
    
def menu_create():
    
    while True:
        print("\n O que deseja cadastrar? \n")
        print("1 - Cliente")
        print("2 - Produto")
        print("3 - Categoria")
        print("0 - Voltar")
    
        op = int(input("Digite a opção desejada: "))
    
        if op == 1:
            c.criar_cliente()
        elif op == 2:
            c.criar_produto()
        elif op == 3:
            c.criar_categoria()
        elif op == 0:
            break
        else:
            print("Opção inválida!")
    
def menu_read():
    
    while True:  
        print("\n O que deseja listar? \n")
        print("1 - Clientes")
        print("2 - Produtos")
        print("3 - Categorias")
        print("0 - Voltar")
    
        op = int(input("Digite a opção desejada: "))

    
        if op == 1:
            c.ler_clientes()
        elif op == 2:
            c.ler_produtos()
            break
        elif op == 3:
            c.ler_categorias()
            break
        elif op == 0:
            break
        else:
            print("Opção inválida!")
    
def menu_update():
    
    while True:
        print("\n O que deseja atualizar? \n")
        print("1 - Cliente")
        print("2 - Produto")
        print("3 - Categoria")
        print("0 - Voltar")
    
        op = int(input("Digite a opção desejada: "))
    
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
        else:
            print("Opção inválida!")
    
    
def menu_delete():
    
    while True:
        print("\n O que deseja deletar? \n")
        print("1 - Cliente")
        print("2 - Produto")
        print("3 - Categoria")
        print("0 - Voltar")
    
        op = int(input("Digite a opção desejada: "))
    
        if op == 1:
            c.deletar_cliente()
        elif op == 2:
            c.deletar_produto()
        elif op == 3:
            c.deletar_categoria()
        elif op == 0:
            break
        else:
            print("Opção inválida!")
    
    

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
                    break
                elif opcao == 2:
                    c.criar_produto()
                    break
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
                break
            
        elif opcao == 4:
            while True:
                menu_delete()
                break
            
        elif opcao == 0:
            break
        
        else:
            print("Opção inválida!")
        
menu()