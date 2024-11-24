from database import db_config as db

import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import date

connection = db.connection

engine = create_engine('sqlite:///LojaRoupas.db')
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
    quantidade_estoque = Column(Integer, nullable=False)
    
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

    produto = Produto(nome=nome, descricao=descricao, preco=preco)
    session.add(produto)
    session.commit()
    print('Produto criado com sucesso!')
    
def criar_item_venda(id_venda, id_produto, quantidade, preco_unitario):
    
    item_venda = ItemVenda(id_venda=id_venda, id_produto=id_produto, quantidade=quantidade, preco_unitario=preco_unitario)
    
    session.add(item_venda)
    session.commit()
    print('Item de venda criado com sucesso!')
    
def criar_venda(data_venda, valor_total, cliente_id):

    
    #carregar a lista de produtos da venda por id
    
    
    item_venda = session.query(ItemVenda).filter(ItemVenda.id_venda == id_venda).all()
    
    
    
    data_venda = date.today()
    id_cliente = input("Digite o id do cliente: ")
    valor_total = sum([item.preco_un * item.quantidade for item in item_venda])
    
    venda = Venda(data_venda=data_venda, valor_total=valor_total, id_cliente=id_cliente)
    session.add(venda)
    session.commit()
    print('Venda criada com sucesso!')
     
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
        print(produto.id_produto, produto.nome, produto.descricao, produto.preco)

def ler_vendas():    
    vendas = session.query(Venda).all()
    for venda in vendas:
        print(venda.id_venda, venda.data_venda, venda.valor_total, venda.id_cliente)       
        
def ler_categorias():
    categorias = session.query(Categoria).all()
    for categoria in categorias:
        print(categoria.id_categoria, categoria.nome, categoria.descricao)
    

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