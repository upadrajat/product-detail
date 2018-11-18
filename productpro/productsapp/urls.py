from django.conf.urls import url
from . import views
app_name="productsapp"

urlpatterns=[
    url('^$',views.home,name='home'),
    url('^insert$',views.insert,name='insert'),
    url('^display$',views.display,name='display'),
    url('^update$',views.update,name='update'),
    url('^delete$',views.delete,name='delete'),
]
