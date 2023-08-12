from django.urls import path
from .views import HomeView, TYView, ContactFormmView, TeacherCreateView, TeacherListView, TeacherDetailView, TeacherUpdateView, TeacherDeleteView

app_name = 'classroom'

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('thank_you/', TYView.as_view(), name='ty'),
    path('contact/', ContactFormmView.as_view(), name = 'contact'),
    path('create_teacher/', TeacherCreateView.as_view(), name = 'create_teacher'),
    path('teachers_list/',TeacherListView.as_view(), name = 'teachers_list'),
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name="teacher_details"),
    path('update_teacher/<int:pk>', TeacherUpdateView.as_view(), name="update_teacher"),
    path('delete_teacher/<int:pk>', TeacherDeleteView.as_view(), name="delete_teacher"),
]
