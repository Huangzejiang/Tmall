from django.conf.urls import url

from home import views

urlpatterns = [
    url('search/', views.get_search_shop)
]
