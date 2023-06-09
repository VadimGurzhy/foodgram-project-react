from django.db.models import Sum
from recipes.models import IngredientAmount


def list_ingredients(request):
    ingredients = IngredientAmount.objects.filter(
        recipe__shopping_cart__user=request.user
    ).values(
        'ingredient__name', 'ingredient__measurement_unit'
    ).annotate(amount=Sum('amount'))
    return ingredients
