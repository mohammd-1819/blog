# Django Blog Application

A simple and flexible blog application built with Django where users can read and comment on blog posts. Administrators can manage content and user comments through the admin panel.

## Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.1 or higher
- Django 5.1 or higher
- Virtualenv (optional but recommended)

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mohammd-1819/blog.git


2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate


3. **Install the required dependencies:**
   ```bash
    pip install -r requirements.txt


4. **Apply the migrations:**
   ```bash
    python manage.py migrate


5. **Create a superuser for the admin panel (optional but recommended):**
   ```bash
    python manage.py createsuperuser
    default is: admin@gmail.com
    password : admin


6. **Run the development server:**
    ```bash
    python manage.py runserver


7. **Access the application:**
    Open your browser and go to http://127.0.0.1:8000/ for the main page



## Features
    User registration and login with reset password
    Ability to create, edit, and delete blog posts (for admin users only)
    Comment system for each blog post (Only Authenticated User)
    Admin panel for managing posts, users, and comments
    Pagination for listing blog posts


## Usage
    Once the server is running, users can register, log in, or simply start reading blog posts. Each post can be tagged and categorized. Users can comment on posts, and administrators can manage the blog content from the admin panel


## Creating a Blog Post
    Only admin users can create a new blog post
    Posts can be tagged and categorized
    All posts are publicly viewable, but only admins can edit or delete them


## Technologies Used
    Backend: Django
    Database: PostgreSQL
    Authentication: Customized Django built-in authentication system
    Frontend: HTML, CSS, JavaScript (with Bootstrap)


## Author
    https://github.com/mohammd-1819
