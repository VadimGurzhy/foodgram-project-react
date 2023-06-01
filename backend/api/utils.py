from django.db.models import Sum
from recipes.models import IngredientAmount


def list_ingredients(request):
    ingredients = IngredientAmount.objects.filter(
            recipe__cart__user=request.user).values(
            'ingredients__name',
            'ingredients__measurement_unit').annotate(total=Sum('amount'))
    shopping_cart = '\n'.join([
            f'{ingredient["ingredients__name"]} - {ingredient["total"]} '
            f'{ingredient["ingredients__measurement_unit"]}'
            for ingredient in ingredients
        ])
    return shopping_cart
