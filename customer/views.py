from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from .serializers import CustomerSerializer
from rest_framework.response import Response
# Create your views here.


class CustomerCreateView(CreateAPIView):
    """Vista Crear Customer"""

    permission_classes = (AllowAny,)
    serializer_class = CustomerSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = CustomerSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     obj = serializer.save()
    #     new_serializer = self.get_serializer(obj, context={
    #         'request': request})
    #     return Response(new_serializer.data, status=status.HTTP_201_CREATED)
