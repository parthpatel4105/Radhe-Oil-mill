# Radhe Mini Oil

A single-page marketing site for Radhe Mini Oil, built with Django.

## Features
- Hero, features, product, reviews, and contact sections (forest-green theme)
- "Buy Now" opens a modal with call / WhatsApp / email options (no cart or checkout — this is a lead-generation site, not an online store)
- Django admin available for future use, but no models are currently registered

## Setup

```
cd parth
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000/

Admin panel: http://127.0.0.1:8000/admin/
- Username: `admin`
- Password: `admin12345`

## Project layout
- `ecommerce/` — project settings, URLs
- `store/` — the app: the `radhe_home` view/template and its static assets (`store/static/store/css/radhe.css`, `store/static/store/js/radhe.js`)

## Contact info on the site
- Phone: 98794 16780
- Email: umaparth7@gmail.com
- Address: Mota Vadala, Kalavad, Jamnagar, Gujarat
