from django.conf.urls import url 
from apps.authorization import views
from library.apps.authorization.views import Login

urlpatterns = [
    url(r'^login/$',views.Login.as_view(), name="login"),
   
            
]
