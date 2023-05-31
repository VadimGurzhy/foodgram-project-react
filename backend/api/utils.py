from django.shortcuts import HttpResponse


def list_ingredients(self, request, ingredients):
    shopping_cart = '\n'.join([
            f'{ingredient["ingredients__name"]} - {ingredient["total"]} '
            f'{ingredient["ingredients__measurement_unit"]}'
            for ingredient in ingredients
        ])
    filename = 'shopping_cart.txt'
    response = HttpResponse(shopping_cart, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response
