from database import db_config as db

import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.orm.exc import NoResultFound
from datetime import date

connection = db.connection

# `create_engine` é usado para estabelecer a conexão com o banco de dados.
# Ele cria um objeto que gerencia a comunicação com o banco especificado por sua URI.
# Aqui, estamos configurando para usar mysql como banco de dados, que se encontram no arquivo db_config.py
engine = create_engine(db.database_url)
# `declarative_base` é uma classe base fornecida pelo ORM do SQLAlchemy.
# Ela permite que as classes Python sejam associadas a tabelas no banco de dados.
Base = declarative_base()
# `sessionmaker` cria um gerenciador de sessões.
# Ele facilita transações e operações no banco de dados, mantendo a consistência.
Session = sessionmaker(bind=engine)
# Início de uma nova sessão.
# A sessão gerencia todas as operações no banco como inserções, consultas, atualizações e exclusões.
# Ela é executada sempre que uma operação é realizada no banco de dados.
session = Session()

#Exemplo de uso
# - Inserção: session.add(objeto) e session.commit()

# - Consulta: session.query(Classe).all() ou session.query(Classe).filter(Classe.atributo == valor).all()

# - Atualização: objeto.atributo = novo_valor e session.commit()

# - Remoção: session.delete(objeto) e session.commit()


#Modelos
#criar as classes Cliente, Venda, Categoria, Produto e ItemVenda
class Cliente(Base):
    __tablename__ = 'Cliente'
    
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(80), nullable=False)
    telefone = Column(String(11), nullable=False)
    endereco = Column(String(200), nullable=False)
    
class Venda(Base):
    __tablename__ = 'Venda'
    
    id_venda = Column(Integer, primary_key=True, autoincrement=True)
    data_venda = Column(Date, nullable=False)
    valor_total = Column(Float, nullable=False)
    id_cliente = Column(Integer, ForeignKey('Cliente.id_cliente'))

    cliente = relationship('Cliente')

class Categoria(Base):
    __tablename__ = 'Categoria'
    
    id_categoria = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(100), nullable=False)
    
class Produto(Base):
    __tablename__ = 'Produto'
    
    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    id_categoria = Column(Integer, ForeignKey('Categoria.id_categoria'))
    estoque_quantidade = Column(Integer, nullable=False)
    
    categoria = relationship('Categoria')

class ItemVenda(Base):
    __tablename__ = 'ItemVenda'
    
    id_item = Column(Integer, primary_key=True, autoincrement=True)
    id_venda = Column(Integer, ForeignKey('Venda.id_venda'))
    id_produto = Column(Integer, ForeignKey('Produto.id_produto'))
    quantidade = Column(Integer, nullable=False)
    preco_un = Column(Float, nullable=False)
    
    venda = relationship('Venda')
    produto = relationship('Produto')

    
#criar as tabelas
Base.metadata.create_all(engine)

#funções para realizar as operações de CRUD
def buscar_cliente():
    escolha = int(input("Você deseja informar o ID ou o nome do cliente?: \n1) ID \n2)Nome \n"))

    while True:
        if escolha == 1:
            # Solicitar o ID do cliente
            id_cliente = int(input("Digite o ID do cliente: "))
            
            #busca se o cliente existe
            try:
                cliente = session.query(Cliente).filter(Cliente.id_cliente == id_cliente).one() 
                return id_cliente
            except NoResultFound:
                print("Cliente não encontrado!")
                return None
    
        elif escolha == 2:
            # Solicitar o nome do cliente
            nome_cliente = input("Digite o nome do cliente: ").strip()

            try:
                # Buscar o cliente pelo nome (retorna o primeiro cliente encontrado)
                cliente = session.query(Cliente).filter(Cliente.nome == nome_cliente).one()
                return cliente.id_cliente  # Retorna o ID do cliente encontrado
            except NoResultFound:
                print("Cliente não encontrado!")
                return None
        else:
            print("Opção inválida!")
        
def buscar_produto():
    escolha = int(input("Você deseja informar o ID ou o nome do produto?: \n1) ID \n2)Nome \n"))

    while True:
        if escolha == 1:
            # Solicitar o ID do produto
            id_produto = int(input("Digite o ID do produto: "))
            
            #busca se o produto existe
            try:
                produto = session.query(Produto).filter(Produto.id_produto == id_produto).one()
                return id_produto
            except NoResultFound:
                print("Produto não encontrado!")
                return None
    
        elif escolha == 2:
            # Solicitar o nome do produto
            nome_produto = input("Digite o nome do produto: ").strip()

            try:
                # Buscar o produto pelo nome (retorna o primeiro produto encontrado)
                produto = session.query(Produto).filter(Produto.nome == nome_produto).one()
                return produto.id_produto  # Retorna o ID do produto encontrado
            except NoResultFound:
                print("Produto não encontrado!")
                return None
        else:
            print("Opção inválida!")
            
def buscar_produto_por_id(id_produto):
    try:
        # Buscar o produto pelo ID
        produto = session.query(Produto).filter(Produto.id_produto == id_produto).one()
        return produto  # Retorna o produto encontrado
    except NoResultFound:
        print("Produto não encontrado!")
        return None
    
def buscar_categoria_por_id(id_categoria):
    try:
        # Buscar a categoria pelo ID
        categoria = session.query(Categoria).filter(Categoria.id_categoria == id_categoria).one()
        return categoria  # Retorna a categoria encontrada
    except NoResultFound:
        print("Categoria não encontrada!")
        return None
    
def buscar_categoria():
    escolha = input("Você deseja informar o ID ou o nome da categoria?: \n1) ID \n2)Nome ")

    while True:
        if escolha == 1:
            # Solicitar o ID da categoria
            id_categoria = int(input("Digite o ID da categoria: "))
            
            #busca se a categoria existe
            try:
                categoria = session.query(Categoria).filter(Categoria.id_categoria == id_categoria).one()
                return id_categoria
            except NoResultFound:
                print("Categoria não encontrada!")
                return None
    
        elif escolha == 2:
            # Solicitar o nome da categoria
            nome_categoria = input("Digite o nome da categoria: ").strip()

            try:
                # Buscar a categoria pelo nome (retorna a primeira categoria encontrada)
                categoria = session.query(Categoria).filter(Categoria.nome == nome_categoria).one()
                return categoria.id  # Retorna o ID da categoria encontrada
            except NoResultFound:
                print("Categoria não encontrada!")
                return None
        else:
            print("Opção inválida!")
            
def buscar_venda():
    # Solicitar o ID da venda
    id_venda = int(input("Digite o ID da venda: "))
    
    #busca se a venda existe
    try:
        venda = session.query(Venda).filter(Venda.id_venda == id_venda).one()
        return id_venda
    except NoResultFound:
        print("Venda não encontrada!")
        return None

#CRUD operations

#CREATE

def criar_cliente():
    
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    
    cliente = Cliente(nome=nome, email=email, telefone=telefone, endereco=endereco)
    session.add(cliente)
    session.commit()
    print('Cliente criado com sucesso!')
    
def criar_produto():
    
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    preco = input("Digite o preço do produto: ")
    estoque_quantidade = input("Digite a quantidade em estoque: ")
    
    #mostrar as categorias disponíveis
    categorias = session.query(Categoria).all()
    for categoria in categorias:
        print(f"{categoria.id_categoria}, {categoria.nome}")
        
    #laço para verificar se a categoria existe
    while True:
        try:
            input_categoria = int(input("Digite o ID da categoria do produto: "))
            categoria = session.query(Categoria).filter(Categoria.id_categoria == input_categoria).one()
            break
        except NoResultFound:
            print("Categoria não encontrada!")
            input_categoria = int(input("Digite o ID da categoria do produto: "))
    
    
    #laço para procurar se o produto já existe por nome e pedir novamente se já existir
    while True:
        try:
            produto = session.query(Produto).filter(Produto.nome == nome).one()
            print("Produto já existe!")
            nome = input("Digite o nome do produto: ")
        except NoResultFound:
            break
    
    #criar o produto
    produto = Produto(nome=nome, descricao=descricao, preco=preco, estoque_quantidade=estoque_quantidade, id_categoria=input_categoria)
    session.add(produto)
    session.commit()
    print('Produto criado com sucesso!')
    
def criar_item_venda(id_venda, id_produto, quantidade, preco_unitario):
    
    item_venda = ItemVenda(id_venda=id_venda, id_produto=id_produto, quantidade=quantidade, preco_unitario=preco_unitario)
    
    session.add(item_venda)
    session.commit()
    print('Item de venda criado com sucesso!')
    
def criar_venda():
    #registrar um cliente
    id_cliente = buscar_cliente()
    
    #calcular o valor total da venda
    total = 0.0
    
    #lista de itens de venda
    itens_venda =[]
    
    if id_cliente is None:
        return # Retorna caso o cliente não seja encontrado
    else:
            #criar a venda
            venda = Venda(id_cliente=id_cliente, valor_total=0.0, data_venda=date.today())
            session.add(venda)
            session.commit() #salvar a venda no banco de dados para obter o id
            
            print('Olá {cliente.nome}!')
            
            #mostrar os produtos disponíveis
            print("\nProdutos disponíveis: \n")
            produtos = session.query(Produto).all()
            for produto in produtos:
                print(f"ID do produto: {produto.id_produto}, Nome do produto: {produto.nome}, Preço do produto: {produto.preco}, Quantidade em estoque: {produto.estoque_quantidade}")
                
            #adicionar itens à venda (laço para adicionar vários itens até que o usuário deseje parar)
            while True:
                id_produto = buscar_produto()
                quantidade = int(input("Digite a quantidade: "))
                
                #verificar se o produto existe
                produto = session.query(Produto).filter(Produto.id_produto == id_produto).first()
                if produto:
                    #verificar se a quantidade em estoque é suficiente
                    if produto.estoque_quantidade < quantidade:
                        print('Quantidade em estoque insuficiente!')
                        continue
                    else:
                        produto.estoque_quantidade -= quantidade
                        session.commit()
                        preco_unitario = produto.preco
                        total += preco_unitario * quantidade
                        itens_venda.append((id_produto, quantidade, preco_unitario))
                        print('Item adicionado com sucesso!')
                else:
                    print('Produto não encontrado!')
                    break
                
                #perguntar se deseja adicionar mais itens
                op = input("Deseja adicionar mais itens? (s/n): ")
                if op == 'n':
                    session.query(Venda).filter(Venda.id_venda == venda.id_venda).update({Venda.valor_total: total})
                    session.commit()
                    print('Valor total da venda: ', total)
                    print('Venda finalizada!')
                    break
     
def criar_categoria():
    nome = input("Digite o nome da categoria: ")
    descricao = input("Digite a descrição da categoria: ")
    
    categoria = Categoria(nome=nome, descricao=descricao)
    session.add(categoria)
    session.commit()
    print('Categoria criada com sucesso!')
    
#READ

def ler_clientes():   
    clientes = session.query(Cliente).all()
    for cliente in clientes:
        print(f"ID: {cliente.id_cliente}, Nome: {cliente.nome}, Email: {cliente.email}, Telefone: {cliente.telefone}")

def ler_produtos():
    produtos = session.query(Produto).all()
    #pegar o id da categoria do produto e mostrar o nome da categoria    
    
    for produto in produtos:
        categoria = session.query(Categoria).filter(Categoria.id_categoria == produto.id_categoria).first()
        print(f"ID: {produto.id_produto}, Nome do produto: {produto.nome}, Descricao do produto: {produto.descricao}, Preco do produto: {produto.preco}, Quantidade em estoque: {produto.estoque_quantidade}, Categoria: {categoria.nome}")

def ler_vendas():    
    vendas = session.query(Venda).all()
    for venda in vendas:
        print(f"ID da venda: {venda.id_venda}, Data da venda: {venda.data_venda}, Valor total: {venda.valor_total}, ID do cliente: {venda.id_cliente}")      
        #mostrar os itens da venda
        itens_venda = session.query(ItemVenda).filter(ItemVenda.id_venda == venda.id_venda).all()
        for item in itens_venda:
            print(f"    ID do produto: {item.id_produto}, Quantidade: {item.quantidade}, Preco unitario: {item.preco_un}") 
        
def ler_categorias():
    categorias = session.query(Categoria).all()
    for categoria in categorias:
        print(f"{categoria.id_categoria}, {categoria.nome}, {categoria.descricao}")
    
#UPDATE

def atualizar_cliente():
    id_cliente = buscar_cliente()
    
    if id_cliente is None:
        return
    else:
        #mostrar o cliente
        cliente = session.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
        print(f"ID: {cliente.id_cliente}, Nome: {cliente.nome}, Email: {cliente.email}, Telefone: {cliente.telefone}")
        
        #o que deseja atualizar?
        while True:
            print("O que deseja atualizar?")
            print("1 - Nome")
            print("2 - Email")
            print("3 - Telefone")
            print("4 - Endereço")
            print("0 - Voltar")
            
            op = int(input("Digite a opção desejada: "))
            
            if op == 1:
                nome = input("Digite o novo nome: ")
                cliente.nome = nome
                session.commit()
                print('Nome atualizado com sucesso!')
            elif op == 2:
                email = input("Digite o novo email: ")
                cliente.email = email
                session.commit()
                print('Email atualizado com sucesso!')
            elif op == 3:
                telefone = input("Digite o novo telefone: ")
                cliente.telefone = telefone
                session.commit()
                print('Telefone atualizado com sucesso!')
            elif op == 4:
                endereco = input("Digite o novo endereço: ")
                cliente.endereco = endereco
                session.commit()
                print('Endereço atualizado com sucesso!')
            elif op == 0:
                break
            else:
                print("Opção inválida!")
        

def atualizar_produto():
    id_produto = buscar_produto()
    
    if id_produto is None:
        return
    else:
        #mostrar o produto
        produto = session.query(Produto).filter(Produto.id_produto == id_produto).first()
        print(f"ID: {produto.id_produto}, Nome: {produto.nome}, Descrição: {produto.descricao}, Preço: {produto.preco}, Quantidade em estoque: {produto.estoque_quantidade}")
        
        #o que deseja atualizar?
        while True:
            print("O que deseja atualizar?")
            print("1 - Nome")
            print("2 - Descrição")
            print("3 - Preço")
            print("4 - Quantidade em estoque")
            print("5 - Categoria")
            print("0 - Voltar")
            
            op = int(input("Digite a opção desejada: "))
            
            if op == 1:
                nome = input("Digite o novo nome: ")
                produto.nome = nome
                session.commit()
                print('Nome atualizado com sucesso!')
            elif op == 2:
                descricao = input("Digite a nova descrição: ")
                produto.descricao = descricao
                session.commit()
                print('Descrição atualizada com sucesso!')
            elif op == 3:
                preco = input("Digite o novo preço: ")
                produto.preco = preco
                session.commit()
                print('Preço atualizado com sucesso!')
            elif op == 4:
                estoque_quantidade = input("Digite a nova quantidade em estoque: ")
                produto.estoque_quantidade = estoque_quantidade
                session.commit()
                print('Quantidade em estoque atualizada com sucesso!')
            elif op == 5:
                #mostrar as categorias disponíveis
                categorias = session.query(Categoria).all()
                for categoria in categorias:
                    print(f"{categoria.id_categoria}, {categoria.nome}")
                    
                #laço para verificar se a categoria existe
                while True:
                    try:
                        input_categoria = int(input("Digite o ID da categoria do produto: "))
                        categoria = session.query(Categoria).filter(Categoria.id_categoria == input_categoria).one()
                        break
                    except NoResultFound:
                        print("Categoria não encontrada!")
                        input_categoria = int(input("Digite o ID da categoria do produto: "))
                
                produto.id_categoria = input_categoria
                session.commit()
                print('Categoria atualizada com sucesso!')
            elif op == 0:
                break
        
def atualizar_categoria():
    id_categoria = buscar_categoria()
    
    if id_categoria is None:
        return
    else:
        #mostrar a categoria
        categoria = session.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()
        print(f"ID: {categoria.id_categoria}, Nome: {categoria.nome}, Descrição: {categoria.descricao}")
        
        #o que deseja atualizar?
        while True:
            print("O que deseja atualizar?")
            print("1 - Nome")
            print("2 - Descrição")
            print("0 - Voltar")
            
            op = int(input("Digite a opção desejada: "))
            
            if op == 1:
                nome = input("Digite o novo nome: ")
                categoria.nome = nome
                session.commit()
                print('Nome atualizado com sucesso!')
            elif op == 2:
                descricao = input("Digite a nova descrição: ")
                categoria.descricao = descricao
                session.commit()
                print('Descrição atualizada com sucesso!')
            elif op == 0:
                break
            else:
                print("Opção inválida!")
        
def atualizar_venda():
    id_venda = buscar_venda()
    
    if id_venda is None:
        return # Retorna caso a venda não seja encontrada
    else:
        #mostra a venda
        venda = session.query(Venda).filter(Venda.id_venda == id_venda).first()
        print(f"ID da venda: {venda.id_venda}, Data da venda: {venda.data_venda}, Valor total: {venda.valor_total}, ID do cliente: {venda.id_cliente}")
        
        #mostrar os itens da venda
        itens_venda = session.query(ItemVenda).filter(ItemVenda.id_venda == id_venda).all()
        for item in itens_venda:
            print(f"    ID do produto: {item.id_produto}, Quantidade: {item.quantidade}, Preco unitario: {item.preco_un}")
            
        #o que deseja atualizar?
        while True:
            print("O que deseja atualizar?")
            print("1 - Cliente")
            print("2 - Itens da venda")
            print("0 - Voltar")
            
            op = int(input("Digite a opção desejada: "))
            
            if op == 1:
                id_cliente = buscar_cliente()
                
                if id_cliente is None:
                    return # Retorna caso o cliente não seja encontrado
                else:
                    venda.id_cliente = id_cliente
                    session.commit()
                    print('Cliente atualizado com sucesso!')
            elif op == 2:
                #atualizar os itens da venda
                #deseja remover, adicionar ou atualizar a quantidade?
                while True:
                    print("O que deseja fazer com os itens da venda?")
                    print("1 - Adicionar item")
                    print("2 - Remover item")
                    print("3 - Atualizar quantidade")
                    print("0 - Voltar")
                    
                    op = int(input("Digite a opção desejada: "))
                    
                    if op == 1:
                        id_produto = buscar_produto()
                        produto = session.query(Produto).filter(Produto.id_produto == id_produto).first()
                        preco_unitario = produto.preco
                        
                        
                        quantidade = int(input("Digite a quantidade: "))
                        
                        #verificar se o produto já existe na venda
                        item_venda = session.query(ItemVenda).filter(ItemVenda.id_venda == id_venda, ItemVenda.id_produto == id_produto).first()
                        
                        #se o produto já existe na venda, atualizar a quantidade, se não, criar o novo item na venda
                        if item_venda:
                            item_venda.quantidade += quantidade
                            session.commit()
                            print('Quantidade atualizada com sucesso!')
                        else:
                            criar_item_venda(id_venda, id_produto, quantidade, preco_unitario)
                            session.commit()
                    
                    elif op == 2:
                        id_produto = buscar_produto()
                        quantidade = int(input("Digite a quantidade: "))
                        
                        #verificar se o produto existe na venda
                        item_venda = session.query(ItemVenda).filter(ItemVenda.id_venda == id_venda, ItemVenda.id_produto == id_produto).first()
                        if item_venda:
                            deletar_item_venda(id_venda, id_produto, quantidade)
                            session.commit()
                            print('Item removido com sucesso!')
                        else:
                            print('Item não encontrado na venda!')
                        
                    elif op == 3:
                        id_produto = buscar_produto()
                        quantidade = int(input("Digite a nova quantidade: "))
                        
                        #verificar se o produto existe na venda
                        item_venda = session.query(ItemVenda).filter(ItemVenda.id_venda == id_venda, ItemVenda.id_produto == id_produto).first()
                        if item_venda:
                            item_venda.quantidade = quantidade
                            session.commit()
                            print('Quantidade atualizada com sucesso!')
                        else:
                            print('Item não encontrado na venda!')
                    elif op == 0:
                        break
                    else:
                        print("Opção inválida!")
            elif op == 0:
                break
            else:
                print("Opção inválida!")
                        
#DELETE

def deletar_cliente(id):
    cliente = session.query(Cliente).filter(Cliente.id_cliente == id).first()
    if cliente:
        session.delete(cliente)
        session.commit()
        print('Cliente deletado com sucesso!')
    else:
        print('Cliente não encontrado!')
        
def deletar_produto(id):
    produto = session.query(Produto).filter(Produto.id_produto == id).first()
    if produto:
        #mostrar o produto, e pedir quantos itens deseja remover
        print(f"ID: {produto.id_produto}, Nome: {produto.nome}, Descrição: {produto.descricao}, Preço: {produto.preco}, Quantidade em estoque: {produto.estoque_quantidade}")
        quantidade = int(input("Digite a quantidade a ser removida: "))
        if produto.estoque_quantidade > quantidade:
            produto.estoque_quantidade -= quantidade
            print('Quantidade atualizada com sucesso!')
            session.commit()
            print('Quantidade atualizada com sucesso!')
        elif produto.estoque_quantidade == quantidade:
            session.delete(produto)
            session.commit()
            print('Produto deletado com sucesso!')
        else:
            print('Quantidade em estoque insuficiente!')
    else:
        print('Produto não encontrado!')
        
def deletar_item_venda(id_venda, id_produto, quantidade):
    item_venda = session.query(ItemVenda).filter(ItemVenda.id_venda == id_venda, ItemVenda.id_produto == id_produto).first()
    #verificar se o item existe
    if item_venda:
        #verificar se a quantidade a ser removida é menor que a quantidade do item
        if item_venda.quantidade > quantidade:
            item_venda.quantidade -= quantidade
            session.commit()
            print('Quantidade atualizada com sucesso!')
        elif item_venda.quantidade == quantidade:
            session.delete(item_venda)
            session.commit()
            print('Item deletado com sucesso!')
        else:
            session.delete(item_venda)
            session.commit()
            print('Item deletado com sucesso!')
    else:
        print('Item não encontrado na venda!')
        
def deletar_venda(id):
    venda = session.query(Venda).filter(Venda.id_venda == id).first()
    if venda:
        itens_venda = session.query(ItemVenda).filter(ItemVenda.id_venda == id).all()
        #mostrar a venda e os itens da venda
        print(f"ID da venda: {venda.id_venda}, Data da venda: {venda.data_venda}, Valor total: {venda.valor_total}, ID do cliente: {venda.id_cliente}")
        for item in venda.itens_venda:
            print(f"    ID do produto: {item.id_produto}, Quantidade: {item.quantidade}, Preco unitario: {item.preco_un}")
        #apagar os itens da venda
        
        for item in itens_venda:
            session.delete(item)
        session.delete(venda)
        session.commit()
        print('Venda deletada com sucesso!')
    else:
        print('Venda não encontrada!')
        
def deletar_categoria(id):
    categoria = session.query(Categoria).filter(Categoria.id_categoria == id).first()
    if categoria:
        session.delete(categoria)
        session.commit()
        print('Categoria deletada com sucesso!')
    else:
        print('Categoria não encontrada!')
        
#closing the connection
connection.close()