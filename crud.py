from database import db_config as db

import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.orm.exc import NoResultFound
from datetime import date

connection = db.connection

engine = create_engine(db.database_url)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

def testar_conexao():
    try:
        # Verificando se a conexão foi bem-sucedida
        if db.connection.is_connected():
            print("Conexão bem-sucedida com o banco de dados!")
            db_info = db.connection.get_server_info()
            print("Versão do servidor MySQL:", db_info)
            return True  # Retorna True para indicar que a conexão foi bem-sucedida

    except Error as err:
        print("Erro ao conectar ao banco de dados:", err)
        return False  # Retorna False caso haja erro na conexão

    finally:
        if db.connection.is_connected():
            db.connection.close()  # Fecha a conexão
            print("Conexão com o MySQL encerrada.")
            

#Modelos
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

    
#creating tables
Base.metadata.create_all(engine)

#funções para realizar as operações de CRUD
def buscar_cliente():
    escolha = input("Você deseja informar o ID ou o nome do cliente?: \n1) ID \n2)Nome ")

    while True:
        if escolha == 1:
            # Solicitar o ID do cliente
            id_cliente = int(input("Digite o ID do cliente: "))
            return id_cliente
    
        elif escolha == 2:
            # Solicitar o nome do cliente
            nome_cliente = input("Digite o nome do cliente: ").strip()

            try:
                # Buscar o cliente pelo nome (retorna o primeiro cliente encontrado)
                cliente = session.query(Cliente).filter(Cliente.nome == nome_cliente).one()
                return cliente.id  # Retorna o ID do cliente encontrado
            except NoResultFound:
                print("Cliente não encontrado!")
                return None
        else:
            print("Opção inválida!")
        
def buscar_produto():
    escolha = input("Você deseja informar o ID ou o nome do produto?: \n1) ID \n2)Nome ")

    while True:
        if escolha == 1:
            # Solicitar o ID do produto
            id_produto = int(input("Digite o ID do produto: "))
            return id_produto
    
        elif escolha == 2:
            # Solicitar o nome do produto
            nome_produto = input("Digite o nome do produto: ").strip()

            try:
                # Buscar o produto pelo nome (retorna o primeiro produto encontrado)
                produto = session.query(Produto).filter(Produto.nome == nome_produto).one()
                return produto.id  # Retorna o ID do produto encontrado
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
    
    #procurar se o produto já existe por nome
    produto = session.query(Produto).filter(Produto.nome == nome).first()
    if produto:
        print('O produto com este nome já existe!')
        return

    else:
        produto = Produto(nome=nome, descricao=descricao, preco=preco, estoque_quantidade=estoque_quantidade)
        session.add(produto)
        session.commit()
        print('Produto criado com sucesso!')
    
def criar_item_venda(id_venda, id_produto, quantidade, preco_unitario):
    
    item_venda = ItemVenda(id_venda=id_venda, id_produto=id_produto, quantidade=quantidade, preco_unitario=preco_unitario)
    
    session.add(item_venda)
    session.commit()
    print('Item de venda criado com sucesso!')
    
def criar_venda():
    #criar a venda
    venda = Venda(id_cliente=id_cliente, valor_total=0.0, data_venda=date.today())
    session.add(venda)
    session.commit() #salvar a venda no banco de dados para obter o id
    
    #calcular o valor total da venda
    total = 0.0
    #lista de itens de venda
    itens_venda =[]
    
    id_cliente = buscar_cliente()
    
    if id_cliente is None:
        return # Retorna caso o cliente não seja encontrado
    else:
        while True:
            id_produto = int(input("Digite o ID do produto: "))
            quantidade = int(input("Digite a quantidade: "))
            
            #buscar o produto no banco de dados
            produto = buscar_produto_por_id(id_produto)
            if produto is None:
                print("Produto não encontrado!")
                continue
            
            if produto.estoque_quantidade < quantidade:
                print("Quantidade indisponível em estoque!")
                continue
            
            #criar o item de venda
            item_venda = ItemVenda(id_venda=venda.id_venda, id_produto=id_produto, quantidade=quantidade, preco_unitario=preco_unitario)
            itens_venda.append(item_venda)
            
            #atualizar o valor total da venda
            total += quantidade * produto.preco
            
            #atualizar o estoque do produto
            produto.estoque_quantidade -= quantidade
            session.commit()
            
            continuar = input("Deseja adicionar mais produtos? (s/n): ")
            if continuar.lower() == 'n':
                break
    
    venda.valor_total = total
    session.commit()
     
def criar_categoria(nome, descricao):
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
    for produto in produtos:
        print(f"ID: {produto.id_produto}, Nome do produto: {produto.nome}, Descricao do produto: {produto.descricao}, Preco do produto: {produto.preco}, Estoque do produto: {produto.estoque_quantidade}")

def ler_vendas():    
    vendas = session.query(Venda).all()
    for venda in vendas:
        print(f"{venda.id_venda}, {venda.data_venda}, {venda.valor_total}, {venda.id_cliente}")       
        
def ler_categorias():
    categorias = session.query(Categoria).all()
    for categoria in categorias:
        print(f"{categoria.id_categoria}, {categoria.nome}, {categoria.descricao}")
    

#UPDATE
def atualizar_cliente(id, nome, email, telefone):
    cliente = session.query(Cliente).filter(Cliente.id_cliente == id).first()
    if cliente:
        cliente.nome = nome
        cliente.email = email
        cliente.telefone = telefone
        session.commit()
        print('Cliente atualizado com sucesso!')
    else:
        print('Cliente não encontrado!')
        

def atualizar_produto(id, nome, descricao, preco):
    produto = session.query(Produto).filter(Produto.id_produto == id).first()
    if produto:
        produto.nome = nome
        produto.descricao = descricao
        produto.preco = preco
        session.commit()
        print('Produto atualizado com sucesso!')
    else:
        print('Produto não encontrado!')
        
def atualizar_categoria(id, nome, descricao):
    categoria = session.query(Categoria).filter(Categoria.id_categoria == id).first()
    if categoria:
        categoria.nome = nome
        categoria.descricao = descricao
        session.commit()
        print('Categoria atualizada com sucesso!')
    else:
        print('Categoria não encontrada!')
        
#DELETE

def deletar_cliente_por_id(id):
    cliente = session.query(Cliente).filter(Cliente.id_cliente == id).first()
    if cliente:
        session.delete(cliente)
        session.commit()
        print('Cliente deletado com sucesso!')
    else:
        print('Cliente não encontrado!')
        
def deletar_cliente_por_nome(nome):
    cliente = session.query(Cliente).filter(Cliente.nome == nome).first()
    if cliente:
        session.delete(cliente)
        session.commit()
        print('Cliente deletado com sucesso!')
    else:
        print('Cliente não encontrado!')
        
def deletar_produto_por_id(id):
    produto = session.query(Produto).filter(Produto.id_produto == id).first()
    if produto:
        session.delete(produto)
        session.commit()
        print('Produto deletado com sucesso!')
    else:
        print('Produto não encontrado!')
        
def deletar_produto_por_nome(nome):
    produto = session.query(Produto).filter(Produto.nome == nome).first()
    if produto:
        session.delete(produto)
        session.commit()
        print('Produto deletado com sucesso!')
    else:
        print('Produto não encontrado!')
        
def deletar_venda(id):
    venda = session.query(Venda).filter(Venda.id_venda == id).first()
    if venda:
        session.delete(venda)
        session.commit()
        print('Venda deletada com sucesso!')
    else:
        print('Venda não encontrada!')
        
def deletar_categoria_por_id(id):
    categoria = session.query(Categoria).filter(Categoria.id_categoria == id).first()
    if categoria:
        session.delete(categoria)
        session.commit()
        print('Categoria deletada com sucesso!')
    else:
        print('Categoria não encontrada!')
        
def deletar_categoria_por_nome(nome):
    categoria = session.query(Categoria).filter(Categoria.nome == nome).first()
    if categoria:
        session.delete(categoria)
        session.commit()
        print('Categoria deletada com sucesso!')
    else:
        print('Categoria não encontrada!')

        
#closing the connection

connection.close()