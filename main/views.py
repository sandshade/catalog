from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from main.serializers import UserSerializer, LinkSerializer, ColorSerializer, ProductSerializer, OrderedItemSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from main.models import Link, Color, Product, OrderedItem


# Create your views here.

def index(request):
    return HttpResponse("Hello World")

class UserRegisterApiView(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            token = Token.objects.create(user=user)
            return Response({'user': serializer.data, 'token': token.key}, status=status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogingApiView(APIView):

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')

        authenticated_user = authenticate(request, username=username, password=password)

        if authenticated_user is not None:
            serializer = UserSerializer(authenticated_user)
            token = Token.objects.get(user=authenticated_user).key
            return Response({'user': serializer.data, 'token': token}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)

class UserLogOutView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class LinksApiView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LinkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LinkApiView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Link.objects.get(pk=id)
        except Link.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        linkObj = self.get_object(id)
        serializer = LinkSerializer(linkObj)
        return Response(serializer.data)

    def put(self, request, id):
        linkObj = self.get_object(id)
        serializer = LinkSerializer(linkObj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        linkObj = self.get_object(id)
        linkObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ColorsApiView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        colors = Color.objects.all()
        serializer = ColorSerializer(colors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ColorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ColorApiView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Color.objects.get(pk=id)
        except Color.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        colorObj = self.get_object(id)
        serializer = ColorSerializer(colorObj)
        return Response(serializer.data)

    def put(self, request, id):
        colorObj = self.get_object(id)
        serializer = ColorSerializer(colorObj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        colorObj = self.get_object(id)
        colorObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductsApiView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductApiView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        productObj = self.get_object(id)
        serializer = ProductSerializer(productObj)
        return Response(serializer.data)

    def put(self, request, id):
        productObj = self.get_object(id)
        serializer = ProductSerializer(productObj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        productObj = self.get_object(id)
        productObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderedItemsApiView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = OrderedItem.objects.all()
        serializer = OrderedItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderedItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderedItemApiView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return OrderedItem.objects.get(pk=id)
        except OrderedItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        itemObj = self.get_object(id)
        serializer = OrderedItemSerializer(itemObj)
        return Response(serializer.data)

    def put(self, request, id):
        itemObj = self.get_object(id)
        serializer = OrderedItemSerializer(itemObj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        itemObj = self.get_object(id)
        itemObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
