from django.conf.urls import url 
from apps.entity import views
from library.apps.entity.views import EntityCrud

urlpatterns = [
    url(r'^entity/$',views.EntityCrud.as_view(), name="Entitycrud"),
    url(r'^entity/(?P<recno>[0-9]+\d)/$', views=EntityCrud.as_view(), name='Entitycrud'),
            
]
