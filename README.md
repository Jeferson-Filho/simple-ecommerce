<a id="readme-top"></a>

<div align="center">
  <h1 align="center">TUG Tag eCommerce</h1>
</div>

<!-- SUMÁRIO -->
<details>
  <summary>Sumário</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o Projeto</a>
      <ul>
        <li><a href="#tecnologias-utilizadas">Tecnologias Utilizadas</a></li>
        <li><a href="#arquitetura">Arquitetura</a></li>
        <li><a href="#instalação">Instalação</a></li>
        <li><a href="#funcionalidades-principais">Funcionalidades Principais</a></li>
      </ul>
    </li>
    <li><a href="#contribuidores">Contribuidores</a></li>
    <li><a href="#contato">Contato</a></li>
  </ol>
</details>

<!-- SOBRE O PROJETO -->
## Sobre o Projeto
Uma aplicação web de eCommerce moderna e responsiva, focada em usabilidade e experiência do usuário. Este projeto visa oferecer uma navegação fluida e intuitiva, adaptável a diversos dispositivos, garantindo acessibilidade para diferentes faixas etárias e níveis de letramento digital.

Além do design centrado no usuário, a aplicação enfatiza a privacidade de dados e conformidade legal, alinhando-se a regulamentações como a LGPD.

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

### Tecnologias Utilizadas
![HTML][HTML-shield]
![CSS][CSS-shield]
![JavaScript][JavaScript-shield]

[![Python][Python-shield]][Python-url]
[![Django][Django-shield]][Django-url]

[![PostgreSQL][PostgreSQL-shield]][PostgreSQL-url]

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

### Arquitetura
#### Diagrama de Arquitetura (MVC)
O projeto segue o padrão **MVC (Model-View-Controller)**, conforme a arquitetura do Django:

-- Colocar imagem MVC --

- **Model:** Representa as estruturas de dados e regras de negócio (ex: User, Product, Order, Post).
- **View:** Controla o fluxo da aplicação, processa requisições, manipula dados e retorna respostas.
- **Template:** Responsável pela apresentação (HTML/CSS/JS) exibida ao usuário.

#### Principais Módulos
- **app:**  
  Módulo principal, gerencia a página inicial, base de templates e configurações globais.

- **blog:**  
  Gerencia as notícias e posts do blog. Permite:
  * Criar, listar e visualizar notícias.

- **cart:**  
  Controla o fluxo de compra do usuário.
  Responsável pelo:
  * Carrinho de compras
  * Pedidos
  * Checkout e integração de pagamento.

- **contacts:**  
  Gerencia o formulário de contato, recebendo dúvidas, sugestões e reclamações dos usuários.

- **products:**  
  Gerencia o catálogo de produtos
  Permite:
  * Cadastro e listagemd de produtos
  * Exibir detalhes de cada produto.

- **user:**  
  Gerencia informações pessoais do usuário.
  Permite:
  * Cadastro
  * Autenticação
  * Gerenciamento do perfil e endereços.

#### Integração Externa: Mercado Pago
O sistema está integrado à API do **Mercado Pago: CheckoutBricks** para processar pagamentos via Pix inicialmente, podendo ser expandido para permitir geração de boletos.
- Ao finalizar a compra, a aplicação se comunica com a API do Mercado Pago, gera um QR Code Pix e exibe para o usuário.
- O fluxo de pagamento é seguro e segue as melhores práticas de integração, utilizando tokens de acesso e ambiente de sandbox para testes.
- O sistema está preparado para produção, bastando trocar as credenciais para o ambiente real.

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

### Instalação
1. Clone o repositório:
```bash
git clone https://github.com/Jeferson-Filho/simple-ecommerce.git
cd simple-ecommerce
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o banco de dados em `settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. Execute as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

7. Acesse o aplicativo:
- App: http://127.0.0.1:8000/

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

### Funcionalidades Principais

#### Fluxo do Usuário

- **Cadastro:**  
  O usuário pode se cadastrar pelo menu de login/cadastro. Após o cadastro, é redirecionado para a página inicial.

- **Login:**  
  Após cadastrar, o usuário pode efetuar login na plataforma e terá acesso ao menu de opções do usuário.

- **Edição de informações pessoais:**  
  O usuário pode editar suas informações cadastradas e também o endereço. Ter um endereço cadastrado é obrigatório para finalizar compras.

- **Visualizar produtos:**  
  Clicando em "Produtos", o usuário é levado à página de listagem de produtos. Ao clicar em um card de produto, é redirecionado para a página de detalhes, onde pode ver mais informações e adicionar uma quantidade desejada ao carrinho.

- **Adicionar ao carrinho:**  
  Ao clicar em "Adicionar ao carrinho", a quantidade selecionada do produto é adicionada ao carrinho.

- **Adicionar novos produtos ao carrinho:**  
  O usuário pode navegar por outros produtos e adicionar diferentes itens ao mesmo carrinho, desde que não tenha finalizado a compra.

- **Ver o carrinho:**  
  No menu do perfil, em "Meu carrinho", o usuário visualiza todos os itens adicionados.

- **Finalizar a compra:**  
  Na página do carrinho, ao clicar em "Finalizar Compra", o usuário é redirecionado para a página de checkout, onde é exibido um QR Code Pix para efetuar o pagamento (apenas para teste no momento).

- **Visualizar pedidos:**  
  No menu do usuário, em "Meus pedidos", o usuário vê a lista de pedidos realizados. Ao clicar no número do pedido, vê os detalhes da compra.

- **Detalhes do pedido:**  
  Na página de detalhes do pedido, ao clicar no nome do produto, o usuário é levado à página do produto. Ao clicar em "Voltar para pedidos", retorna à listagem de pedidos.

- **Enviar mensagem:**  
  No footer, ao clicar em "Contato", o usuário acessa um formulário para enviar uma mensagem para o e-mail do sistema.

- **Ver notícias:**  
  No menu superior, em "Notícias", o usuário acessa a listagem de notícias. Clicando em "Leia Mais", vê a notícia completa.

- **Logout:**  
  No menu do usuário, ao clicar em "Logout", o usuário encerra a sessão e retorna para a página anterior.

---

#### Fluxo do Administrador

- **Cadastrar produtos:**  
  No menu do admin, em "Cadastrar produtos", o administrador acessa um formulário para cadastrar novos produtos no sistema.

- **Cadastrar notícias:**  
  No menu do admin, em "Cadastrar notícias", o administrador acessa um formulário para postar novas notícias no blog.

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

<!-- CONTRIBUIDORES -->
## Contribuidores

<a href="https://github.com/Jeferson-Filho/simple-ecommerce/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Jeferson-Filho/simple-ecommerce" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

<!-- CONTATO -->
## Contato

Caio Bolhalter <br>
[![LinkedIn][linkedin-shield]][caio-linkedin-url]

Jeferson Filho <br>
[![LinkedIn][linkedin-shield]][jeferson-linkedin-url]

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

<!-- LINKS & IMAGENS MARKDOWN -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[Python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[HTML-shield]: https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[CSS-shield]: https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[JavaScript-shield]: https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[Django-shield]: https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[PostgreSQL-shield]: https://img.shields.io/badge/postgresql-316192?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/docs/current/app-psql.html

<!-- -------------------------------------------------------------------------------- -->
[caio-linkedin-url]: https://www.linkedin.com/in/caio-bohlhalter-de-souza-202646232/
[jeferson-linkedin-url]: https://www.linkedin.com/in/jdietrichfho/