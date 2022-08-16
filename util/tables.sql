SELECT * FROM clientes;
CREATE TABLE IF NOT EXISTS empresas(
	id serial PRIMARY KEY,
	nome varchar(50),
	cnpj varchar(14)
	
);

CREATE TABLE IF NOT EXISTS confiabilidades(
	id serial PRIMARY KEY,
	pontos integer,
	selo varchar(10), 
	qtd_livros_permitidos integer,
	qtd_livros_emprestados integer
		
);

CREATE TABLE IF NOT EXISTS clientes(
	id serial PRIMARY KEY,
	
	empresa_id integer,
	CONSTRAINT fk_empresa
      FOREIGN KEY(empresa_id) 
	  	REFERENCES empresas(id)
			ON DELETE CASCADE,
	
	confiabilidade_id integer,
	CONSTRAINT fk_confiabilidade
      FOREIGN KEY(confiabilidade_id) 
	  	REFERENCES confiabilidades(id)
			ON DELETE CASCADE,
 
	cpf varchar(11),
	nome varchar(50), 
	telefone varchar(20),
	email varchar(50), 
	data_nascimento varchar(10)	
);


CREATE TABLE IF NOT EXISTS enderecos(
	id serial PRIMARY KEY,
	tipo_logradouro varchar(15),
	logradouro varchar(100), 
	numero integer,
	bairro varchar(30), 
	cidade varchar(30), 
	cep varchar(8), 
	estado varchar(50),
	cliente_id integer,
	CONSTRAINT fk_cliente
      FOREIGN KEY(cliente_id) 
	  	REFERENCES clientes(id) 
			ON DELETE CASCADE
);
			
CREATE TABLE IF NOT EXISTS localizacoes(
	id serial PRIMARY KEY,
	estante integer,
	prateleira integer
);

CREATE TABLE IF NOT EXISTS autores(
	id serial PRIMARY KEY,
	nome varchar(100)
	
);

CREATE TABLE IF NOT EXISTS funcionarios(
	id serial PRIMARY KEY,
	
	empresa_id integer,
	CONSTRAINT fk_empresa
      FOREIGN KEY(empresa_id) 
	  	REFERENCES empresas(id) 
			ON DELETE CASCADE,
	--Caso excluir uma empresa, todos os funcionÃ¡rios com chave 
	--estrangeira da mesma serÃ£o excluidos
	
	matricula varchar(5),
	senha varchar(20), 
	cpf varchar(11),
	nome varchar(50), 
	telefone varchar(11),
	email varchar(50), 
	data_nascimento varchar(10)	
);


CREATE TABLE IF NOT EXISTS livros(
	id serial PRIMARY KEY,
	
	empresa_id integer,
	CONSTRAINT fk_empresa
      FOREIGN KEY(empresa_id) 
	  	REFERENCES empresas(id)
			ON DELETE CASCADE,

	localizacao_id integer,
	CONSTRAINT fk_localizacao
      FOREIGN KEY(localizacao_id) 
	  	REFERENCES localizacoes(id)
			ON DELETE CASCADE,
	
	titulo varchar(50),
	edicao integer,
	editora varchar(50),
	ano_publicacao integer,
	num_paginas integer,
	cod_barras varchar(50),
	genero varchar(50),
	quantidade integer,
	isbn varchar(30),
	disponivel bit
	
);

CREATE TABLE IF NOT EXISTS emprestimos(
	id serial PRIMARY KEY,
	
	cliente_id integer,
	CONSTRAINT fk_cliente
      FOREIGN KEY(cliente_id) 
	  	REFERENCES clientes(id)
			ON DELETE CASCADE,
	
	funcionario_id integer,
	CONSTRAINT fk_funcionario
      FOREIGN KEY(funcionario_id) 
	  	REFERENCES funcionarios(id)
			ON DELETE SET NULL,
	
	livro_id integer,
	CONSTRAINT fk_livro
      FOREIGN KEY(livro_id) 
	  	REFERENCES livros(id)
			ON DELETE CASCADE,

	data_inicio varchar(10),
	prazo_devolucao integer,
	data_devolucao varchar(10),
	status varchar(50)
	
);

CREATE TABLE IF NOT EXISTS autores_livros(
	id serial PRIMARY KEY,
	
	livro_id integer,
	CONSTRAINT fk_livro
      FOREIGN KEY(livro_id) 
	  	REFERENCES livros(id)
			ON DELETE CASCADE,
	
	autor_id integer,
	CONSTRAINT fk_autor
      FOREIGN KEY(autor_id) 
	  	REFERENCES autores(id)
			ON DELETE CASCADE
	
);

--alter table funcionarios alter column telefone type varchar(11);
--alter table livros add column isbn varchar(255);

--alter table localizacoes add column livro_id integer;--ok
--alter table localizacoes add CONSTRAINT fk_livro
--      FOREIGN KEY(livro_id) 
--	  	REFERENCES livros(id) 
--			ON DELETE CASCADE;--ok
			
--alter table clientes drop column empresa_id;