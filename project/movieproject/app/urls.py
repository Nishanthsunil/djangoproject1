from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name='first'),
    path("detail/<int:movie_id>/",views.detail,name='detail'),
    path("update/<int:id>",views.update,name='update'),
    path("delete/<int:id>",views.delete,name='delete'),
    path('add',views.add,name='add'),
]