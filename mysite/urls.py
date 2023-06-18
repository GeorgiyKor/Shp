"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from shp import views


urlpatterns = [

    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about-us/", views.about),
    path("account/", views.account),
    path("account-login/", views.account_log),
    path("account-register/", views.account_reg),
    path("contact/", views.contact),
    path("page-not-found/", views.page_not_found),
    path("shop-checkout/", views.shop_checkout),
    path("shop/", views.shop_four_columns),
    path("single-product/<int:id>", views.single_product),
    path("cart/", views.cart_detail),
    path("remove/<int:id>", views.cart_remove),
    path("add/<int:id>", views.cart_add),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
