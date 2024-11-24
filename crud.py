from database import db_config as db

import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import date

# connection = db.connection
# cursor = db.connection.cursor()

#comando = ''
#cursor.execute(comando)
#connection.commit() #editar o banco de dados
#resultado = cursor.fetchall() #ler o banco de dados


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
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(80), nullable=False)
    telefone = Column(String(11), nullable=False)
    endereco = Column(String(200), nullable=False)

class Produto(Base):
    __tablename__ = 'Produto'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade_estoque = Column(Integer, nullable=False)
    
class Venda(Base):
    __tablename__ = 'Venda'
    
    id = Column(Integer, primary_key=True)
    data_venda = Column(Date, nullable=False)
    valor_total = Column(Float, nullable=False)
    cliente_id = Column(Integer, ForeignKey('Cliente.id'))

    cliente = relationship('Cliente')
    
class ItemVenda(Base):
    __tablename__ = 'ItemVenda'
    
    id = Column(Integer, primary_key=True)
    id_venda = Column(Integer, ForeignKey('Venda.id'))
    id_produto = Column(Integer, ForeignKey('Produto.id'))
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)
    
    venda = relationship('Venda')
    produto = relationship('Produto')
    
class Categoria(Base):
    __tablename__ = 'Categoria'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(100), nullable=False)
    

    
#creating tables
Base.metadata.create_all(engine)

#CRUD operations

#CREATE

def criar_cliente():
    cursor = db.connection.cursor()
    
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    
    cliente = Cliente(nome=nome, email=email, telefone=telefone, endereco=endereco)
    session.add(cliente)
    session.commit()
    print('Cliente criado com sucesso!')
    # cursor.close()
    
def criar_produto():
    cursor = db.connection.cursor()

    
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    preco = input("Digite o preço do produto: ")

    produto = Produto(nome=nome, descricao=descricao, preco=preco)
    session.add(produto)
    session.commit()
    print('Produto criado com sucesso!')
    
    cursor.close()
    
def criar_item_venda(id_venda, id_produto, quantidade, preco_unitario):
    cursor = db.connection.cursor()
    
    item_venda = ItemVenda(id_venda=id_venda, id_produto=id_produto, quantidade=quantidade, preco_unitario=preco_unitario)
    
    session.add(item_venda)
    session.commit()
    print('Item de venda criado com sucesso!')
    
    cursor.close()
    
def criar_venda(data_venda, valor_total, cliente_id):
    cursor = db.connection.cursor()

    
    #carregar a lista de produtos da venda por id
    #item_venda = session.query(ItemVenda).filter(ItemVenda.id_venda == id_venda).all()
    
    
    data_venda = date.today()
    cliente_id = input("Digite o id do cliente: ")
    valor_total = sum([item.preco_unitario * item.quantidade for item in item_venda])
    
    venda = Venda(data_venda=data_venda, valor_total=valor_total, cliente_id=cliente_id)
    session.add(venda)
    session.commit()
    print('Venda criada com sucesso!')
    
    cursor.close()
    
def criar_categoria(nome, descricao):
    cursor = db.connection.cursor()
    
    categoria = Categoria(nome=nome, descricao=descricao)
    session.add(categoria)
    session.commit()
    print('Categoria criada com sucesso!')
    
    cursor.close()
    
#READ
def ler_clientes():
    testar_conexao()
    
    cursor = db.connection.cursor()
    
    
    cursor.execute('SELECT * FROM Cliente')
    for linha in cursor.fetchall():
        print(linha)
        
    cursor.close()
        
    #clientes = session.query(Cliente).all()
    #for cliente in clientes:
        #print(cliente.id, cliente.nome, cliente.email, cliente.telefone)

def ler_produtos():
    cursor = db.connection.cursor()

    produtos = session.query(Produto).all()
    for produto in produtos:
        print(produto.id, produto.nome, produto.descricao, produto.preco)
        
    cursor.close()

def ler_vendas():
    cursor = db.connection.cursor()
    
    vendas = session.query(Venda).all()
    for venda in vendas:
        print(venda.id, venda.data_venda, venda.valor_total, venda.cliente_id)
        
    cursor.close()
        
def ler_categorias():
    cursor = db.connection.cursor()

    categorias = session.query(Categoria).all()
    for categoria in categorias:
        print(categoria.id, categoria.nome, categoria.descricao)
    
    cursor.close()

#UPDATE
def atualizar_cliente(id, nome, email, telefone):
    cursor = db.connection.cursor()

    cliente = session.query(Cliente).filter(Cliente.id == id).first()
    if cliente:
        cliente.nome = nome
        cliente.email = email
        cliente.telefone = telefone
        session.commit()
        print('Cliente atualizado com sucesso!')
    else:
        print('Cliente não encontrado!')
        
    cursor.close()

def atualizar_produto(id, nome, descricao, preco):
    cursor = db.connection.cursor()

    produto = session.query(Produto).filter(Produto.id == id).first()
    if produto:
        produto.nome = nome
        produto.descricao = descricao
        produto.preco = preco
        session.commit()
        print('Produto atualizado com sucesso!')
    else:
        print('Produto não encontrado!')
        
def atualizar_categoria(id, nome, descricao):
    categoria = session.query(Categoria).filter(Categoria.id == id).first()
    if categoria:
        categoria.nome = nome
        categoria.descricao = descricao
        session.commit()
        print('Categoria atualizada com sucesso!')
    else:
        print('Categoria não encontrada!')
        
#DELETE

def deletar_cliente_por_id(id):
    cliente = session.query(Cliente).filter(Cliente.id == id).first()
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
    produto = session.query(Produto).filter(Produto.id == id).first()
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
    venda = session.query(Venda).filter(Venda.id == id).first()
    if venda:
        session.delete(venda)
        session.commit()
        print('Venda deletada com sucesso!')
    else:
        print('Venda não encontrada!')
        
def deletar_categoria_por_id(id):
    categoria = session.query(Categoria).filter(Categoria.id == id).first()
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
        
        
# closing the connection
# connection.close()