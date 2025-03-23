from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import BaseViewSerializer
from drf_spectacular.utils import extend_schema

# Create your views here.

class BaseView(APIView):

    @extend_schema(request=None, parameters=[BaseViewSerializer], responses={200: BaseViewSerializer})
    
    def get(self, request):

        name = self.request.GET.get('name')
        serilizer = BaseViewSerializer(data={"name" : name})
        if serilizer.is_valid():
            print(name)

            return HttpResponse("<h1>Welcome Asuraking</h1>")
        return HttpResponse("An error occured")
    
