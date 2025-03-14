# DietTrackerAPI

A **DietTrackerAPI** é uma API desenvolvida para controlar e monitorar a dieta diária de usuários, oferecendo funcionalidades como registro de refeições, visualização de médias semanais de cada usuário e controle por tipos de acesso, como administradores e usuários comuns.

## Funcionalidades

- **Cadastro de Refeições**: O usuário pode registrar suas refeições, com os seguintes dados:
  - Nome da refeição
  - Descrição
  - Data e hora
  - Indicação se está dentro ou fora da dieta
- **Edição de Refeições**: O usuário pode editar qualquer refeição registrada anteriormente.
- **Exclusão de Refeições**: O usuário pode apagar refeições registradas.
- **Visualização de Refeições**: O usuário pode visualizar todas as refeições registradas ou detalhes de uma refeição específica.
- **Média Semanal do Usuário**: A cada 7 dias, a API calcula a média das refeições registradas pelo usuário, armazenando e retornando a porcentagem de refeições que estão dentro da dieta.
- **Média Geral de Todos os Usuários**: A cada 7 dias, a API calcula a média geral de todos os usuários e salva essa informação para exibição.
- **Tipos de Acesso**: A API conta com diferentes tipos de acesso:
  - **Admin**: Pode visualizar todos os registros de refeições de todos os usuários.
  - **User**: Pode visualizar, registrar, editar e excluir suas próprias refeições, além de acessar sua própria média semanal.

## Tecnologias Utilizadas

- **Flask**: Framework web para construção da API.
- **MySQL**: Banco de dados relacional para armazenar as informações de refeições e usuários.
- **Flask-Login**: Para controle de login e sessões dos usuários.
- **Flask-Bcrypt**: Para criptografia de senhas de usuários.
- **Flask-SQLAlchemy**: ORM para facilitar o trabalho com o banco de dados.

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/DietTrackerAPI.git
cd DietTrackerAPI
