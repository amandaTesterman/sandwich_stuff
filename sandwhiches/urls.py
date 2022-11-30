from django.urls import path
from sandwhiches.views import SandwhichesView, IngredientsView, RandomView

urlpatterns = [
    path('', SandwhichesView.as_view(), name="sandwhich"),
    path('ingredient/<str:ingredient_type>', IngredientsView.as_view(), name='ingredients_list'),
    path('random', RandomView.as_view(), name="random")
]