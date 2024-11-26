import crud as c

def create_tables():
    c.Base.metadata.create_all(c.engine)
    
def menu_create():
    
    while True:
        print("\n O que deseja cadastrar? \n")
        print("1 - Cliente")
        print("2 - Produto")
        print("3 - Categoria")
        print("4 - Venda")
        print("0 - Voltar")
    
        op = int(input("Digite a opção desejada: "))
    
        if op == 1:
            c.criar_cliente()
        elif op == 2:
            c.criar_produto()
        elif op == 3:
            c.criar_categoria()
        elif op == 4:
            c.criar_venda()
        elif op == 0:
            break
        else:
            print("Opção inválida!")
            break
    
def menu_read():
    
    while True:  
        print("\n O que deseja listar? \n")
        print("1 - Clientes")
        print("2 - Produtos")
        print("3 - Categorias")
        print("4 - Vendas")
        print("0 - Voltar")
    
        op = int(input("Digite a opção desejada: "))

        if op == 1:
            c.ler_clientes()
        elif op == 2:
            c.ler_produtos()
        elif op == 3:
            c.ler_categorias()
        elif op == 4:
            c.ler_vendas()
        elif op == 0:
            break
        else:
            print("Opção inválida!")
            break
    
def menu_update():
    
    while True:
        print("\n O que deseja atualizar? \n")
        print("1 - Cliente")
        print("2 - Produto")
        print("3 - Categoria")
        print("4 - Venda")
        print("0 - Voltar")
    
        op = int(input("Digite a opção desejada: "))
    
        if op == 1:
            c.atualizar_cliente()
            break
        elif op == 2:
            c.atualizar_produto()
            break
        elif op == 3:
            c.atualizar_categoria()
            break
        elif op == 4:
            c.atualizar_venda()
            break
        elif op == 0:
            break
        else:
            print("Opção inválida!")
            break
    
    
def menu_delete():
    
    while True:
        print("\n O que deseja remover? \n")
        print("1 - Cliente")
        print("2 - Produto")
        print("3 - Categoria")
        print("4 - Venda")
        print("0 - Voltar")
    
        op = int(input("Digite a opção desejada: "))
    
        if op == 1:
            
            while True:
                #buscar o cliente primeiro
                id_cliente = c.buscar_cliente()
                
                #se existir, deletar
                if id_cliente: 
                    c.deletar_cliente(id_cliente)
                    break
                else:
                    break
                
        elif op == 2:
            while True:
                #buscar o produto primeiro
                id_produto = c.buscar_produto()
                
                #se existir, deletar
                if id_produto: 
                    c.deletar_produto(id_produto)
                    break
                else:
                    break
                
        elif op == 3:
            while True:
                #buscar a categoria primeiro
                id_categoria = c.buscar_categoria()
                
                #se existir, deletar
                if id_categoria: 
                    c.deletar_categoria(id_categoria)
                    break
                else:
                    break
                
        elif op == 4:
            while True:
                #buscar a venda primeiro
                id_venda = c.buscar_venda()
                
                #se existir, deletar
                if id_venda: 
                    c.deletar_venda(id_venda)
                    break
                else:
                    break
                
        elif op == 0:
            break
        
        else:
            print("Opção inválida!")
            break

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
            break
        
menu()