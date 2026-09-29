from decimal import Decimal

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CheckoutForm, RegisterForm
from .models import Cart, CartItem, Category, Order, OrderItem, Product


def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)

    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)

    return render(request, 'store/home.html', {
        'categories': categories,
        'products': products,
        'active_category': category_slug,
        'query': query or '',
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'store/product_detail.html', {'product': product})


def radhe_home(request):
    return render(request, 'store/radhe_home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Cart.objects.get_or_create(user=user)
            login(request, user)
            messages.success(request, 'Account created. Welcome!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'store/register.html', {'form': form})


def _get_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return cart


@login_required
def cart_detail(request):
    cart = _get_cart(request)
    return render(request, 'store/cart.html', {'cart': cart})


@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    cart = _get_cart(request)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
    item.save()
    messages.success(request, f'{product.name} added to cart.')
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def cart_update(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    if quantity <= 0:
        item.delete()
    else:
        item.quantity = quantity
        item.save()
    return redirect('cart_detail')


@login_required
def cart_remove(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('cart_detail')


@login_required
def checkout(request):
    cart = _get_cart(request)
    if not cart.items.exists():
        messages.error(request, 'Your cart is empty.')
        return redirect('home')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                order = Order.objects.create(
                    user=request.user,
                    shipping_address=form.cleaned_data['shipping_address'],
                    total_price=Decimal('0.00'),
                )
                total = Decimal('0.00')
                for item in cart.items.select_related('product'):
                    OrderItem.objects.create(
                        order=order,
                        product=item.product,
                        product_name=item.product.name,
                        price=item.product.price,
                        quantity=item.quantity,
                    )
                    total += item.subtotal()
                order.total_price = total
                order.status = 'paid'
                order.save()
                cart.items.all().delete()
            messages.success(request, 'Order placed successfully!')
            return redirect('order_detail', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(request, 'store/checkout.html', {'form': form, 'cart': cart})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'store/order_detail.html', {'order': order})


@login_required
def order_list(request):
    orders = request.user.orders.all()
    return render(request, 'store/order_list.html', {'orders': orders})
