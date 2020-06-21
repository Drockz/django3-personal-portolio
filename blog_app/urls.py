
from django.urls import path
from . import views
#blog_app_

app_name = 'blog'

urlpatterns = [
    path('',views.all_blogs,name='all_blogs'),
    path('<int:blog_app_id>',views.detail,name='detail'),
]
