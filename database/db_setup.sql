CREATE DATABASE LojaRoupas;
CREATE SCHEMA LojadeRoupas;
USE LojaRoupas;

CREATE TABLE Cliente(
	id_cliente INT PRIMARY KEY auto_increment,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(80) NOT NULL,
    telefone VARCHAR(11) NOT NULL,
    endereco VARCHAR(200) NOT NULL
);

CREATE TABLE Venda(
	id_venda INT PRIMARY KEY auto_increment,
    data_venda DATE NOT NULL,
    valor_total DECIMAL(10, 2),
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

CREATE TABLE Categoria(
	id_categoria INT PRIMARY KEY auto_increment,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(100) NOT NULL
);

CREATE TABLE Produto(
	id_produto INT PRIMARY KEY auto_increment,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    id_categoria INT,
    estoque_quantidade INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);

CREATE TABLE ItemVenda(
	id_item INT PRIMARY KEY auto_increment,
    id_venda INT,
    id_produto INT,
    quantidade INT NOT NULL,
    preco_un DECIMAL(10, 2) NOT NULL,
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

INSERT INTO Categoria (nome, descricao) VALUES 
('Camisetas', 'Roupas confortáveis para o dia a dia com estilo surfista'),
('Bermudas', 'Bermudas casuais e para surfe, com materiais resistentes à água'),
('Rash Guards', 'Camisetas de proteção UV para prática de esportes aquáticos'),
('Wetsuits', 'Roupas de neoprene para surfe em águas frias'),
('Chinelos', 'Calçados leves e confortáveis para ambientes de praia'),
('Acessórios de Praia', 'Itens como toalhas, mochilas e sacolas para praia'),
('Pranchas de Surfe', 'Pranchas para iniciantes e profissionais, de várias dimensões'),
('Equipamentos de Surfe', 'Itens como leash, parafina e quilhas para pranchas'),
('Bonés e Chapéus', 'Proteção contra o sol com estilo surfista'),
('Roupas Femininas', 'Roupas como biquínis e vestidos com temática de praia e surfe');

INSERT INTO Produto (nome, descricao, preco, id_categoria, estoque_quantidade) VALUES
('Camiseta Waves', 'Camiseta com estampa de ondas', 89.99, 1, 50),
('Bermuda Boardshort', 'Bermuda leve e resistente à água', 119.99, 2, 30),
('Rash Guard Pro', 'Proteção UV com tecido respirável', 129.90, 3, 25),
('Wetsuit Thermal', 'Wetsuit de neoprene para águas frias', 499.99, 4, 10),
('Chinelo Praia', 'Chinelo confortável com sola antiderrapante', 39.90, 5, 100),
('Toalha Grande', 'Toalha de secagem rápida para praia', 69.90, 6, 45),
('Prancha Iniciante', 'Prancha de surfe ideal para iniciantes', 899.99, 7, 15),
('Leash Pro', 'Leash de alta resistência para pranchas', 79.90, 8, 40),
('Boné Surf Style', 'Boné com proteção UV', 59.90, 9, 35),
('Biquíni Tropical', 'Biquíni com estampas tropicais', 149.90, 10, 20),
('Camiseta Surf Life', 'Camiseta básica com estampa temática', 99.90, 1, 70),
('Bermuda Cargo', 'Bermuda com bolsos laterais', 139.90, 2, 20),
('Rash Guard Fit', 'Camiseta UV com ajuste atlético', 119.90, 3, 30),
('Wetsuit Pro', 'Wetsuit para profissionais', 799.90, 4, 5),
('Chinelo Surf Wave', 'Chinelo com logo surfista', 49.90, 5, 80),
('Mochila Praia', 'Mochila resistente à areia e água', 129.90, 6, 15),
('Prancha Avançada', 'Prancha para surfistas experientes', 1599.99, 7, 8),
('Parafina Classic', 'Parafina para melhorar a aderência', 19.90, 8, 200),
('Chapéu de Palha', 'Chapéu leve com proteção solar', 69.90, 9, 25),
('Vestido Floral', 'Vestido com estampas florais de praia', 189.90, 10, 15);

INSERT INTO Venda (data_venda, valor_total, id_cliente) VALUES
('2024-11-01', 249.88, 1),
('2024-11-02', 169.80, 2),
('2024-11-03', 799.90, 3),
('2024-11-04', 89.99, 4),
('2024-11-05', 989.70, 5),
('2024-11-06', 69.90, 6),
('2024-11-07', 149.90, 7),
('2024-11-08', 1099.89, 8),
('2024-11-09', 999.49, 9),
('2024-11-10', 299.70, 10);

INSERT INTO ItemVenda (id_venda, id_produto, quantidade, preco_un) VALUES
-- Venda 1
(1, 1, 2, 89.99),
(1, 5, 1, 69.90),
-- Venda 2
(2, 10, 1, 149.90),
(2, 8, 1, 19.90),
-- Venda 3
(3, 4, 1, 799.90),
-- Venda 4
(4, 1, 1, 89.99),
-- Venda 5
(5, 7, 1, 899.99),
(5, 6, 1, 69.90),
(5, 8, 1, 19.90),
-- Venda 6
(6, 6, 1, 69.90),
-- Venda 7
(7, 10, 1, 149.90),
-- Venda 8
(8, 7, 1, 899.99),
(8, 4, 1, 199.90),
-- Venda 9
(9, 7, 1, 899.99),
(9, 8, 5, 19.90),
-- Venda 10
(10, 3, 2, 129.90),
(10, 5, 1, 39.90);


SELECT * FROM Cliente;

SELECT * FROM Produto;

DESCRIBE Produto;
