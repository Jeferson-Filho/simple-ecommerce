<a id="readme-top"></a>

<div align="center">
  <h1 align="center">User-Centric eCommerce</h1>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributors">Contributors</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
A modern and responsive eCommerce web application focused on usability and user experience. This project aims to deliver a fluid and intuitive navigation interface, adaptable to various devices, ensuring accessibility across different age groups and levels of digital literacy.

Beyond user-centric design, the application emphasizes data privacy and legal compliance, aligning with regulations such as the LGPD.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

![HTML][HTML-shield]
![CSS][CSS-shield]
![JavaScript][JavaScript-shield]

[![Python][Python-shield]][Python-url]
[![Django][Django-shield]][Django-url]

[![PostgreSQL][PostgreSQL-shield]][PostgreSQL-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
### Installation

1. Clone the repository:
```bash
git clone https://github.com/Jeferson-Filho/simple-ecommerce.git
cd simple-ecommerce
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure database in `settings.py`

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Access the app:
- App: http://127.0.0.1:8000/

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap
### 1. Planning and Setup
- [X] Create Python virtual environment  
- [X] Install Django and dependencies (`psycopg2`, etc.)  
- [X] Initialize Django project and main app (`app`)  
- [X] Connect to PostgreSQL database  
- [X] Set up `.gitignore`, `requirements.txt`, and Git versioning  
- [X] Structure project folders: `templates/`, `static/`


### 2. Authentication and User Management
- [ ] User registration, login, and logout  
- [ ] Password reset via email  
- [ ] Distinguish user and admin permissions  
- [ ] Route protection middleware


### 3. Product Management
- [ ] Product modeling (name, description, price, store, image)  
- [ ] CRUD operations via admin  
- [ ] Store updates
- [ ] Product detail page


### 4. Shopping Cart and Orders
- [ ] Add/remove items from cart  
- [ ] Clear cart  
- [ ] Create order from cart  
- [ ] Cancel order


### 5. Shipping and Address Management
- [ ] Register and edit delivery addresses
- [ ] Freight calculation (flat or based on CEP code range) (optional)


### 6. Payment Simulation
- [ ] Order status updates  
- [ ] Payment receipt generation
- [ ] Payment simulation (credit card, bank slip, etc.) (optional)


### 7. Blog and Posts
- [ ] CRUD for posts (admin and users)  
- [ ] Post detail page  
- [ ] Edit and delete posts


### 8. Product Catalog and Search
- [ ] Sorting  products by name or price
- [ ] Search field for name 
- [ ] Dynamic results display


### 9. Admin Dashboard
- [ ] Update list of store
- [ ] Update list of products
- [ ] Create posts and produts

### 10. Frontend and UI
- [ ] Layout using pure HTML, CSS, and JS  
- [ ] Reusable components (header, footer, cards)  
- [ ] Responsive design for mobile/tablet  
- [ ] JavaScript interactivity (modals, validation, dynamic cart)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributors

<a href="https://github.com/Jeferson-Filho/ChestXRayClassification/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Jeferson-Filho/ChestXRayClassification" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Caio Bolhalter <br>
[![LinkedIn][linkedin-shield]][caio-linkedin-url]

Jeferson Filho <br>
[![LinkedIn][linkedin-shield]][jeferson-linkedin-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

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