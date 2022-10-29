from django.contrib import admin
from django.urls import path
from simFindah.views import search_view, search_result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search_view, name = 'home'),
path('search_result/', search_result, name = 'search-result')
]

