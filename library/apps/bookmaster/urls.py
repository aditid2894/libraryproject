from django.conf.urls import url 
from apps.bookmaster import views
from library.apps.bookmaster.views import BookmasterCrud

urlpatterns = [
    url(r'^bookmaster/$',views.BookmasterCrud.as_view(), name="Bookmastercrud"),
    url(r'^bookmaster/(?P<recno>[0-9]+\d)/$', views=BookmasterCrud.as_view(), name='Bookmastercrud'),
            
]
