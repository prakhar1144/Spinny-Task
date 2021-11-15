from re import template
from django.urls import path
from .views import CreateBoxAPIView, MyBoxes, UpdateBoxAPIView, AllBoxes, MyBoxes, DeleteBox
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('create/', CreateBoxAPIView.as_view()),
    path('update/<int:pk>', UpdateBoxAPIView.as_view()),
    path('list/', AllBoxes.as_view()),
    path('my-boxes/', MyBoxes.as_view()),
    path('delete/<int:pk>', DeleteBox.as_view())
]