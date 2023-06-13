# Website de Perguntas e Opções - Django & SQLite

Bem-vindo ao repositório do meu projeto de website de perguntas e opções! Este é um projeto que desenvolvi utilizando o framework Django e o banco de dados SQLite. Foi criado com o intuito de aprimorar minhas habilidades em desenvolvimento web e serve como um exemplo de trabalho para o meu portfólio.

## Visão Geral do Projeto

O projeto consiste em um website no qual os usuários podem fazer perguntas e receber respostas de outros usuários. Cada pergunta pode ter várias opções de resposta, e os usuários podem votar em suas opções preferidas. O objetivo é proporcionar um ambiente interativo para compartilhamento de opiniões e conhecimento.

## Funcionalidades Principais

O website possui as seguintes funcionalidades principais:

1. **Cadastro de Usuários**: Os usuários podem se cadastrar utilizando um nome de usuário e senha. Esse cadastro permite que eles façam perguntas, respondam a perguntas de outros usuários e participem de votações.

2. **Perguntas e Respostas**: Os usuários podem fazer perguntas sobre qualquer assunto e receber respostas de outros usuários. As perguntas são exibidas em uma página principal e os usuários podem filtrá-las por categorias.

3. **Votação**: Para cada pergunta, os usuários podem escolher uma opção de resposta e votar nela. As opções são exibidas de forma clara e intuitiva, facilitando a participação dos usuários.

4. **Gerenciamento de Contas**: Os usuários têm a opção de editar suas informações de perfil, como nome de usuário, senha e foto de perfil. Além disso, eles podem visualizar o histórico de suas perguntas e respostas.

## Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Django**: Utilizei o framework Django devido à sua facilidade de configuração e ao suporte robusto para desenvolvimento web. Ele fornece recursos como roteamento de URLs, gerenciamento de formulários e integração com banco de dados.

- **SQLite**: O banco de dados SQLite foi escolhido por ser leve e de fácil configuração. É uma boa opção para projetos menores e proporciona um bom desempenho.

## Configuração do Ambiente de Desenvolvimento

Para executar o projeto em seu ambiente de desenvolvimento local, siga as etapas abaixo:

1. **Clone o repositório**: Faça um clone deste repositório em sua máquina local utilizando o comando `git clone <URL do repositório>`.

2. **Instale as dependências**: Certifique-se de ter o Python e o Django instalados em sua máquina. Navegue até o diretório do projeto clonado e execute o seguinte comando para instalar as dependências do projeto: `pip install -r requirements.txt`


3. **Execute as migrações**: Aplique as migrações para criar as tabelas do banco de dados SQLite. No diretório do projeto, execute o seguinte comando:
`python manage.py migrate`


4. **Inicie o servidor de desenvolvimento**: Inicie o servidor de desenvolvimento do Django

