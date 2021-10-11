"""librarybooktrackapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from librarybooks import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('library',views.LibraryViewSet)
router.register('book',views.BookViewSet)
router.register('user',views.UserViewSet)
router.register('library-book',views.LibraryBookViewSet)
router.register('library-activity',views.LibraryActivityViewSet)
router.register('book-checkout-user',views.BookCheckoutByUserviewset)
router.register('book-checkout-library',views.BookCheckoutFromLibraryviewset)
router.register('checkout-library-book',views.CheckoutLibraryBookViewSet)
router.register('checkin-library-book',views.CheckinLibraryBookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
     path('',include(router.urls))
]
