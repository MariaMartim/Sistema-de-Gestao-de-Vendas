CREATE DATABASE LojaRoupas;
CREATE SCHEMA LojadeRoupas;
USE LojaRoupas;

-- Tabela Cliente
CREATE TABLE Cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(80) NOT NULL,
    telefone VARCHAR(11) NOT NULL,
    endereco VARCHAR(200) NOT NULL
);

-- Tabela Venda
CREATE TABLE Venda (
    id_venda INT PRIMARY KEY AUTO_INCREMENT,
    data_venda DATE NOT NULL,
    valor_total DECIMAL(10, 2),
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

-- Tabela Categoria
CREATE TABLE Categoria (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(100) NOT NULL
);

-- Tabela Produto
CREATE TABLE Produto (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    id_categoria INT,
    estoque_quantidade INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);

-- Tabela ItemVenda
CREATE TABLE ItemVenda (
    id_item INT PRIMARY KEY AUTO_INCREMENT,
    id_venda INT,
    id_produto INT,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_venda) REFERENCES Venda(id_venda),
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto)
);

INSERT INTO Cliente (nome, email, telefone, endereco) VALUES
('Carlos Silva', 'carlos.silva@email.com', '11987654321', 'Rua das Flores, 123, São Paulo, SP'),
('Maria Oliveira', 'maria.oliveira@email.com', '11998765432', 'Avenida Brasil, 456, Rio de Janeiro, RJ'),
('José Santos', 'jose.santos@email.com', '11999887766', 'Rua 7 de Setembro, 789, Belo Horizonte, MG'),
('Ana Souza', 'ana.souza@email.com', '11991122334', 'Rua das Palmeiras, 101, Salvador, BA'),
('Pedro Lima', 'pedro.lima@email.com', '11990011223', 'Rua do Sol, 202, Fortaleza, CE'),
('Fernanda Rocha', 'fernanda.rocha@email.com', '11993334455', 'Avenida Paulista, 303, São Paulo, SP'),
('Lucas Pereira', 'lucas.pereira@email.com', '11994455666', 'Rua dos Limoeiros, 404, Curitiba, PR'),
('Paula Costa', 'paula.costa@email.com', '11995566777', 'Rua dos Girassóis, 505, Recife, PE'),
('Rafael Almeida', 'rafael.almeida@email.com', '11996677888', 'Rua do Campo, 606, Porto Alegre, RS'),
('Mariana Fernandes', 'mariana.fernandes@email.com', '11997788999', 'Rua da Liberdade, 707, Florianópolis, SC');

