from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import FoodSerializer
from .models import Food

# Create your views here.
class FoodList(APIView):
    def get(self, request):
        food = Food.objects.all()
        query = self.request.GET.get('search')
        if query is not None:
            food = food.filter(name__contains=query) | food.filter(creator__contains=query)
        serializer = FoodSerializer(food, many=True)
        return Response(serializer.data)
