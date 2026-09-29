from django.core.management.base import BaseCommand

from store.models import Category, Product


class Command(BaseCommand):
    help = 'Seed the store with sample categories and products'

    def handle(self, *args, **options):
        categories_data = {
            'electronics': 'Electronics',
            'clothing': 'Clothing',
            'books': 'Books',
        }
        categories = {}
        for slug, name in categories_data.items():
            category, _ = Category.objects.get_or_create(slug=slug, defaults={'name': name})
            categories[slug] = category

        products = [
            ('electronics', 'Wireless Headphones', 'wireless-headphones', 1999.00, 25),
            ('electronics', 'Smartwatch', 'smartwatch', 3499.00, 15),
            ('clothing', 'Cotton T-Shirt', 'cotton-t-shirt', 499.00, 100),
            ('clothing', 'Denim Jacket', 'denim-jacket', 2299.00, 30),
            ('books', 'Python Crash Course', 'python-crash-course', 799.00, 50),
        ]
        created_count = 0
        for cat_slug, name, slug, price, stock in products:
            _, created = Product.objects.get_or_create(
                slug=slug,
                defaults={
                    'category': categories[cat_slug],
                    'name': name,
                    'price': price,
                    'stock': stock,
                    'description': f'Sample product: {name}',
                },
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Seeded store. {created_count} new products created.'))
