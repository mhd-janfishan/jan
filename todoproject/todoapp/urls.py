from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name="home"),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklist.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.taskdetail.as_view(),name='cbvedetail'),
    path('cbvupdte/<int:pk>/',views.taskupdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.taskdelete.as_view(),name='cbvdelete')

]