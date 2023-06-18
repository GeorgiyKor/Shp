from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from shp.form import UserRegistrationForm, LoginForm, CartAddItemForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
from shp.models import Item, Cheque, Purchases, User


def index(request):
    user_id = request.user.id
    head = Item.objects.filter(id=4)
    cheque = Cheque.objects.filter(user_id=user_id)
    item = Item.objects.all()
    total = cheque.aggregate(Sum('price'))['price__sum']
    return render(request, "shp/index.html", {"cheque": cheque, "item": item, "head": head, "total": total})


def about(request):
    user_id = request.user.id
    head = Item.objects.filter(id=4)
    cheque = Cheque.objects.filter(user_id=user_id)
    item = Item.objects.all()
    total = cheque.aggregate(Sum('price'))['price__sum']
    return render(request, "shp/about-us.html", {"cheque": cheque, "item": item, "head": head, "total": total})


def account(request):
    user_id = request.user.id
    cheque = Cheque.objects.filter(user_id=user_id)
    total = cheque.aggregate(Sum('price'))['price__sum']
    item = Item.objects.all()
    user = User.objects.get(id=user_id)
    return render(request, "shp/account.html", {"item": item, "user": user, "cheque": cheque, "total": total})


def account_log(request):
    user_id = request.user.id
    cheque = Cheque.objects.filter(user_id=user_id)
    total = cheque.aggregate(Sum('price'))['price__sum']
    item = Item.objects.all()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'shp/account.html')
                else:
                    return redirect("index")
            else:
                return redirect("index")
    else:
        form = LoginForm()
    return render(request, "shp/account-login.html", {"form": form, "cheque": cheque, "item": item, "total": total})


def account_reg(request):
    user_id = request.user.id
    cheque = Cheque.objects.filter(user_id=user_id)
    total = cheque.aggregate(Sum('price'))['price__sum']
    item = Item.objects.all()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()
            return render(request, 'shp/account-login.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'shp/account-register.html', {'user_form': user_form, "cheque": cheque, "item": item, "total": total})


def contact(request):
    user_id = request.user.id
    cheque = Cheque.objects.filter(user_id=user_id)
    item = Item.objects.all()
    total = cheque.aggregate(Sum('price'))['price__sum']
    return render(request, "shp/contact.html", {"item": item, "cheque": cheque, "total": total})


def page_not_found(request):
    user_id = request.user.id
    cheque = Cheque.objects.filter(user_id=user_id)
    item = Item.objects.all()
    total = cheque.aggregate(Sum('price'))['price__sum']
    return render(request, "shp/page-not-found.html", {"item": item, "cheque": cheque, "total": total})


def shop_checkout(request):
    user_id = request.user.id
    cheque = Cheque.objects.filter(user_id=user_id)
    item = Item.objects.all()
    total = cheque.aggregate(Sum('price'))['price__sum']
    return render(request, "shp/shop-checkout.html", {"item": item, "cheque": cheque, "total": total})


def shop_four_columns(request):
    user_id = request.user.id
    cheque = Cheque.objects.filter(user_id=user_id)
    item = Item.objects.all()
    total = cheque.aggregate(Sum('price'))['price__sum']
    return render(request, "shp/shop-four-columns.html", {"item": item, "cheque": cheque, "total": total})


def single_product(request, id):
    item = Item.objects.filter(id=id)
    user_id = request.user.id
    cheque = Cheque.objects.filter(user_id=user_id)
    items = Item.objects.all()
    total = cheque.aggregate(Sum('price'))['price__sum']
    return render(request, "shp/single-product.html", {"item": item, "cheque": cheque, "total": total, "items": items})


def shop(request):
    user_id = request.user.id
    cheque = Cheque.objects.filter(user_id=user_id)
    item = Item.objects.all()
    total = cheque.aggregate(Sum('price'))['price__sum']
    return render(request, "shp/shop.html", {"item": item, "cheque": cheque, "total": total})


@require_POST
def cart_add(request, id):
    item = Item.objects.get(id=id)
    user_id = request.user.id
    chq = Cheque()
    if request.method == 'POST':
        chq.item_id = item.id
        chq.image = item.image
        chq.quantity = 1
        chq.price = item.price
        chq.total_price = chq.quantity * chq.price
        chq.item_name_id = item.item_name
        chq.user_id = user_id
        chq.save()
    return redirect('/')


def cart_detail(request):
    user_id = request.user.id
    cheque = Cheque.objects.filter(user_id=user_id)
    item = Item.objects.all()
    total = cheque.aggregate(Sum('price'))['price__sum']

    return render(request, 'shp/shop-cart.html', {'cheque': cheque, 'item': item, 'total': total})


def cart_remove(request, id):
    cheque = get_object_or_404(Cheque, id=id)
    cheque.delete()
    return redirect('/')

