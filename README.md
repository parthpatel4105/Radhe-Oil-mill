# Parth Store

A simple full-stack e-commerce website built with Django.

## Features
- Product catalog with categories, search, and stock status
- User registration/login/logout (Django's built-in auth)
- Cart (add, update quantity, remove)
- Checkout that creates an order and clears the cart
- Order history per user
- Django admin for managing categories, products, and orders

## Setup

```
cd parth
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_store      # adds sample categories/products
python manage.py runserver
```

Visit http://127.0.0.1:8000/

Admin panel: http://127.0.0.1:8000/admin/
- Username: `admin`
- Password: `admin12345`

## Project layout
- `ecommerce/` — project settings, URLs
- `store/` — the app: models (Category, Product, Cart, CartItem, Order, OrderItem), views, templates, and a `seed_store` management command
