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
            #entrar ou com id do cliente ou com o nome para buscar o id
            c.criar_venda()
                    
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
            while True:
                nome = input("\n Digite o novo nome \n")
                email = input("Digite o novo email \n")
                telefone = input("Digite o novo telefone \n")
                endereco = input("Digite o novo endereço \n")
                c.atualizar_cliente(nome, email, telefone, endereco)
                
                print("Cliente atualizado com sucesso!")
            
        elif op == 2:
            
            while True:
                #buscar o produto primeiro
                id_produto = c.buscar_produto()
                
                #se existir, atualizar
                if id_produto: 
                    nome = input("\n Digite o novo nome \n")
                    descricao = input("Digite a nova descricao \n")
                    preco = input("Digite o novo preco \n")
                    quantidade_estoque = input("Digite a quantidade em estoque \n")
                    id_categoria = input("Digite o id da categoria \n")
                    
                    c.atualizar_produto(id_produto, nome, descricao, preco, quantidade_estoque, id_categoria)
                    
                    print("Produto atualizado com sucesso!")
                else:
                    print("Produto não encontrado")
                    break
        elif op == 3:
            
            while True:
                #buscar a categoria primeiro
                id_categoria = c.buscar_categoria()
                
                #se existir, atualizar
                if id_categoria: 
                    nome = input("\n Digite o novo nome \n")
                    descricao = input("Digite a nova descricao \n")
                    
                    c.atualizar_categoria(id_categoria, nome, descricao)
                    
                    print("Categoria atualizada com sucesso!")
                else:
                    print("Categoria não encontrada")
                    break
        elif op == 4:
            
            while True:
                #buscar a venda primeiro
                id_venda = c.buscar_venda()
                
                #se existir, atualizar
                if id_venda: 
                    id_cliente = input("\n Digite o id do cliente \n")
                    data = input("Digite a nova data \n")
                    valor_total = input("Digite o novo valor total \n")
                    
                    c.atualizar_venda(id_venda, id_cliente, data, valor_total)
                    
                    print("Venda atualizada com sucesso!")
                else:
                    print("Venda não encontrada")
                    break
        elif op == 0:
            break
        else:
            print("Opção inválida!")
    
    
def menu_delete():
    
    while True:
        print("\n O que deseja apagar? \n")
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
                    
                    print("Cliente deletado com sucesso!")
                else:
                    print("Cliente não encontrado")
                    break
        elif op == 2:
            
            while True:
                #buscar o produto primeiro
                id_produto = c.buscar_produto()
                
                #se existir, deletar
                if id_produto: 
                    c.deletar_produto(id_produto)
                    
                    print("Produto deletado com sucesso!")
                else:
                    print("Produto não encontrado")
                    break
        elif op == 3:
            
            while True:
                #buscar a categoria primeiro
                id_categoria = c.buscar_categoria()
                
                #se existir, deletar
                if id_categoria: 
                    c.deletar_categoria(id_categoria)
                    
                    print("Categoria deletada com sucesso!")
                else:
                    print("Categoria não encontrada")
        elif op == 4:
            
            while True:
                #buscar a venda primeiro
                id_venda = c.buscar_venda()
                
                #se existir, deletar
                if id_venda: 
                    c.deletar_venda(id_venda)
                    
                    print("Venda deletada com sucesso!")
                else:
                    print("Venda não encontrada")
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