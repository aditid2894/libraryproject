from django.conf.urls import url 
from apps.member import views
from library.apps.member.views import MemberCrud

urlpatterns = [
    url(r'^member/$',views.MemberCrud.as_view(), name="Membercrud"),
    url(r'^member/(?P<recno>[0-9]+\d)/$', views=MemberCrud.as_view(), name='Membercrud'),
            
]
