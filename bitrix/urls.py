from django.urls import path
from .views import BitrixList,BitrixDetail


urlpatterns = [
    path('<int:pk>/',BitrixDetail.as_view()),
    path('', BitrixList.as_view())

]