from django.urls import path
from .  import views

urlpatterns= [
    path('', views.apioverview, name="api-overview"),
         path('task-list/', views.tasklist, name="task-list"
              ),
    path('taskdetail/<int:pk>', views.taskdetail, name="task-detail"),
    path('Create-task', views.Createtask, name="Create-task"),
    path('Update-task/<int:pk>', views.Updatetask, name="update-task"),
    path('Delete-task/<int:pk>', views.deleteTask, name="Delete-task"),
]
