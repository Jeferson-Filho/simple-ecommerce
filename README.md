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

![Django_MVC](https://github.com/user-attachments/assets/e7332b4d-a55a-4478-87f0-10f7084377ae)

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
  ![Cadastro_1](https://github.com/user-attachments/assets/80ba6368-bc89-417a-adfa-820ba3619faa)
  ![Cadastro_2](https://github.com/user-attachments/assets/4f536787-bd3d-4cca-b5a0-a6aec5105a32)

- **Login:**  
  Após cadastrar, o usuário pode efetuar login na plataforma e terá acesso ao menu de opções do usuário.
  ![Login_2](https://github.com/user-attachments/assets/7aefb24c-5ca7-4313-8a95-55eb17e40988)
  ![Login_1](https://github.com/user-attachments/assets/8ccae598-7b82-47ea-a6ef-62d007613eb8)

- **Edição de informações pessoais:**  
  O usuário pode editar suas informações cadastradas e também o endereço. Ter um endereço cadastrado é obrigatório para finalizar compras.
  ![Info_Pessoal_1](https://github.com/user-attachments/assets/0c4002b7-c19e-448a-aa7e-3ab8eb77cf8c)
  ![Info_Pessoal_2](https://github.com/user-attachments/assets/4431c35f-0e8f-43de-b038-1bad1bf9032d)


- **Visualizar produtos:**  
  Clicando em "Produtos", o usuário é levado à página de listagem de produtos. Ao clicar em um card de produto, é redirecionado para a página de detalhes, onde pode ver mais informações e adicionar uma quantidade desejada ao carrinho.
  ![Produtos_2](https://github.com/user-attachments/assets/1bca600f-0880-4534-9e7f-36027f12af18)
  ![Produtos_1](https://github.com/user-attachments/assets/c28a8395-5326-434f-94df-8e85f461832e)

- **Adicionar ao carrinho:**  
  Ao clicar em "Adicionar ao carrinho", a quantidade selecionada do produto é adicionada ao carrinho.
  ![Detalhes_Produto_1](https://github.com/user-attachments/assets/3768ff74-933b-4703-acea-6289c41096a6)
  ![Detalhes_Produto_2](https://github.com/user-attachments/assets/ea384e7a-efcc-42a0-8a06-feb99260fa9a)
  ![Detalhes_Produto_3](https://github.com/user-attachments/assets/f5328199-a652-46e6-8d08-e1299e9ff9e5)

- **Adicionar novos produtos ao carrinho:**  
  O usuário pode navegar por outros produtos e adicionar diferentes itens ao mesmo carrinho, desde que não tenha finalizado a compra.

- **Ver o carrinho:**  
  No menu do perfil, em "Meu carrinho", o usuário visualiza todos os itens adicionados.
  ![Carrinho_2](https://github.com/user-attachments/assets/aa1b2795-7848-4539-9f60-2e07c0ef1c82)

- **Finalizar a compra:**  
  Na página do carrinho, ao clicar em "Finalizar Compra", o usuário é redirecionado para a página de checkout, onde é exibido um QR Code Pix para efetuar o pagamento (apenas para teste no momento).
  ![Carrinho_1](https://github.com/user-attachments/assets/13766bf1-f967-4288-ae09-e116bfae8ee0)
  ![Checkout_1](https://github.com/user-attachments/assets/aa48fc23-8530-4ee4-a712-92c6e5d74243)

- **Visualizar pedidos:**  
  No menu do usuário, em "Meus pedidos", o usuário vê a lista de pedidos realizados. Ao clicar no número do pedido, vê os detalhes da compra.
  ![Pedidos_1](https://github.com/user-attachments/assets/74b48952-d11d-47c7-ae7c-408197f3b5ac)
  ![Pedidos_2](https://github.com/user-attachments/assets/26566078-b0ad-45c0-9dca-e4cc7a0b6571)

- **Detalhes do pedido:**  
  Na página de detalhes do pedido, ao clicar no nome do produto, o usuário é levado à página do produto. Ao clicar em "Voltar para pedidos", retorna à listagem de pedidos.
  ![Pedidos_3](https://github.com/user-attachments/assets/afad9697-1679-4c28-a5d3-426fd455e8d3)
  ![Pedidos_4](https://github.com/user-attachments/assets/aa038c84-70f4-4ea7-a440-93654f4e023f)

- **Enviar mensagem:**  
  No footer, ao clicar em "Contato", o usuário acessa um formulário para enviar uma mensagem para o e-mail do sistema.
  ![Contato_1](https://github.com/user-attachments/assets/fbd04f43-e2d6-49a4-9481-f6596ca726c5)
  ![Contato_2](https://github.com/user-attachments/assets/d584af3c-8492-440b-bbe6-7af34289a747)

- **Ver notícias:**  
  No menu superior, em "Notícias", o usuário acessa a listagem de notícias. Clicando em "Leia Mais", vê a notícia completa.
  ![Notícias_1](https://github.com/user-attachments/assets/bbe41b37-7ac9-4a47-8c1e-ec76608ca8ec)
  ![Notícias_2](https://github.com/user-attachments/assets/39c0e896-a40d-4e59-84a0-7b21bb361f99)
  ![Notícias_3](https://github.com/user-attachments/assets/3f810559-5ea7-4724-b409-04745c84c114)

- **Logout:**  
  No menu do usuário, ao clicar em "Logout", o usuário encerra a sessão e retorna para a página anterior.
  ![Logout_1](https://github.com/user-attachments/assets/41b55703-2d0c-425e-81e7-9137ee9d533e)

---

#### Fluxo do Administrador

- **Cadastrar produtos:**  
  No menu do admin, em "Cadastrar produtos", o administrador acessa um formulário para cadastrar novos produtos no sistema.
  ![Cadastrar_Produtos_1](https://github.com/user-attachments/assets/5567d7cf-998c-48f5-9bd7-896867659a42)
  ![Cadastrar_Produtos_2](https://github.com/user-attachments/assets/aeb51cf7-db93-45f8-b05a-9a916976ace4)

- **Cadastrar notícias:**  
  No menu do admin, em "Cadastrar notícias", o administrador acessa um formulário para postar novas notícias no blog.
  ![Cadastrar_Noticias_1](https://github.com/user-attachments/assets/4ba37779-5da8-4e85-a2d9-a0b75759bbe7)
  ![Cadastrar_Noticias_2](https://github.com/user-attachments/assets/7ab53311-65aa-4370-8931-a545408a08a7)

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
