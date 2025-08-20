from django.urls import path
from .views import RegisterView, QuestionListCreateView, QuestionDetailView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('questions/', QuestionListCreateView.as_view(), name='question_list_create'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
]

