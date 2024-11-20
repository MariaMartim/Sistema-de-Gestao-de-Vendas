import mysql.connector
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import date

# Connect to the database
connection = mysql.connector.connect(
    user= 'root',
    password= '1703Lunna@',
    host= '127.0.0.1',
    database= 'LojaRoupas',
)

cursor = connection.cursor()

comando = ''
cursor.execute(comando)
connection.commit() #editar o banco de dados
resultado = cursor.fetchall() #ler o banco de dados



engine = create_engine('sqlite:///LojaRoupas.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

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
    
class Estoque(Base):
    __tablename__ = 'Estoque'
    
    id = Column(Integer, primary_key=True)
    id_produto = Column(Integer, ForeignKey('Produto.id'))
    quantidade = Column(Integer, nullable=False)
    referencia = Column(String(15), nullable=False)
    
    produto = relationship('Produto')
    
#creating tables
Base.metadata.create_all(engine)

#CRUD operations

#CREATE
def criar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    
    cliente = Cliente(nome=nome, email=email, telefone=telefone)
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
    
def criar_venda(data_venda, valor_total, cliente_id):
    data_venda = date.today()
    valor_total = input("Digite o valor total da venda: ")
    cliente_id = input("Digite o id do cliente: ")
    
    venda = Venda(data_venda=data_venda, valor_total=valor_total, cliente_id=cliente_id)
    session.add(venda)
    session.commit()
    print('Venda criada com sucesso!')
    
def criar_item_venda(id_venda, id_produto, quantidade, preco_unitario):
    item_venda = ItemVenda(id_venda=id_venda, id_produto=id_produto, quantidade=quantidade, preco_unitario=preco_unitario)
    session.add(item_venda)
    session.commit()
    print('Item de venda criado com sucesso!')
    
def criar_categoria(nome, descricao):
    categoria = Categoria(nome=nome, descricao=descricao)
    session.add(categoria)
    session.commit()
    print('Categoria criada com sucesso!')
    
#READ
def ler_clientes():
    clientes = session.query(Cliente).all()
    for cliente in clientes:
        print(cliente.id, cliente.nome, cliente.email, cliente.telefone)

def ler_produtos():
    produtos = session.query(Produto).all()
    for produto in produtos:
        print(produto.id, produto.nome, produto.descricao, produto.preco)
        
def ler_vendas():
    vendas = session.query(Venda).all()
    for venda in vendas:
        print(venda.id, venda.data_venda, venda.valor_total, venda.cliente_id)
        
def ler_categorias():
    categorias = session.query(Categoria).all()
    for categoria in categorias:
        print(categoria.id, categoria.nome, categoria.descricao)
    
#UPDATE
def atualizar_cliente(id, nome, email, telefone):
    cliente = session.query(Cliente).filter(Cliente.id == id).first()
    if cliente:
        cliente.nome = nome
        cliente.email = email
        cliente.telefone = telefone
        session.commit()
        print('Cliente atualizado com sucesso!')
    else:
        print('Cliente não encontrado!')
        
def atualizar_produto(id, nome, descricao, preco):
    produto = session.query(Produto).filter(Produto.id == id).first()
    if produto:
        produto.nome = nome
        produto.descricao = descricao
        produto.preco = preco
        session.commit()
        print('Produto atualizado com sucesso!')
    else:
        print('Produto não encontrado!')
        
#DELETE



cursor.close()
connection.close()