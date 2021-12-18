from .views import *
from django.urls import path,include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'tasks_vs', TasksViewSets)


urlpatterns = [
    path('tasks/', include(router.urls)),
    path('category/all', CategoryView.as_view()),
    path('category/detail/<int:pk>/', CategoryDetailUpdate.as_view() ),
    path('category/delete/<int:pk>/', CategoryDelete.as_view() ),
    path('taskstatus/', TaskStatus.as_view() ),


]
