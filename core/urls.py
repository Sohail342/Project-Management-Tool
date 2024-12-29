from django.urls import path
from . import views

urlpatterns = [
    path('api/projects/', views.ListCreateProjectView.as_view(), name='project-list-create'),
    path('api/projects/<int:pk>/', views.RetrieveUpdateDeleteProjectView.as_view(), name='project-detail'),
    
    # Tasks URLS
    path('projects/<int:project_id>/tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:id>/', views.TaskDetailView.as_view(), name='task-detail'),
    
    # Comment URLS
    path('api/tasks/<int:task_id>/comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    path('api/comments/<int:id>/', views.CommentDetailView.as_view(), name='comment-detail'),
]
