from . import views
from django.urls import path
from django.views.generic import TemplateView

app_name = 'featureflags'

urlpatterns = [
     path(r'mypage/', TemplateView.as_view(template_name='test.html'))
]
