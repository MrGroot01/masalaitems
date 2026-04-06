from django.views import View
from django.http import JsonResponse
from .models import MasalItems

class MasalItemsView(View):
    def get(self, request):
        items = MasalItems.objects.all()

        category = request.GET.get('category')
        search = request.GET.get('search')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        rating = request.GET.get('rating')

        if category:
            items = items.filter(category__iexact=category)

        if search:
            items = items.filter(name__icontains=search)

        if min_price:
            items = items.filter(price__gte=int(min_price))

        if max_price:
            items = items.filter(price__lte=int(max_price))

        if rating:
            items = items.filter(rating__gte=float(rating))

        data = []
        for item in items:
            image_url = request.build_absolute_uri(item.images.url) if item.images else None

            data.append({
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "description": item.description,
                "category": item.category,
                "rating": item.rating,
                "image": image_url
            })

        return JsonResponse(data, safe=False)