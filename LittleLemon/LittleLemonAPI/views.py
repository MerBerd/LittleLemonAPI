from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import IsManager
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group


class UserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentUser(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        if request.user:
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'no user found'}, status=status.HTTP_401_UNAUTHORIZED)


class MenuItemsView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsManager()]
    
    
    def get(self, request):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuItemsDetailView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsManager()]
          
    def get(self, request, pk):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        serializer = MenuItemSerializer(menu_item)
        return Response(serializer.data)
    

    def put(self, request, pk):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        serializer = MenuItemSerializer(menu_item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        serializer = MenuItemSerializer(menu_item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        menu_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ManagerView(APIView):
    permission_classes = [IsManager]

    def get(self, request):
        try:
            manager_group = Group.objects.get(name='Manager')
        except Group.DoesNotExist:
            return Response({"detail": "Manager group not found."}, status=404)
    
        managers = User.objects.filter(groups=manager_group)

        manager_list = [
            {
                "id": manager.id,
                "username": manager.username,
                "email": manager.email,
                "first_name": manager.first_name,
                "last_name": manager.last_name,
            }
            for manager in managers
        ]

        return Response(manager_list)
    
    def post(self, request):
        user_id = request.data.get('id')

        if user_id is not None:
            try:
                # Retrieve the user by ID
                user = User.objects.get(id=user_id)

                # Retrieve or create the 'Manager' group
                manager_group, created = Group.objects.get_or_create(name='Manager')

                # Add the user to the 'Manager' group
                user.groups.add(manager_group)

                return Response({'message': f'User {user.username} has been added to the Manager group.'}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'User ID not provided.'}, status=status.HTTP_400_BAD_REQUEST)
    

    
    
class ManagerDeleteView(APIView):
    permission_classes = [IsManager]
    def delete(self, request, pk):
        try:
            user = User.objects.get(id=pk)

            try:
                manager_group = Group.objects.get(name='Manager')

                
                user.groups.remove(manager_group)

                return Response({'message': f'User {user.username} has been removed from the Manager group.'}, status=status.HTTP_200_OK)
            except Group.DoesNotExist:
                return Response({'error': 'Manager group does not exist.'}, status=status.HTTP_404_NOT_FOUND)
            
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    



class DeliveryCrewView(APIView):
    permission_classes = [IsManager]

    def get(self, request):
        try:
            delivery_crew_group = Group.objects.get(name='Delivery Crew')
        except Group.DoesNotExist:
            return Response({"detail": "Delivery Crew group not found."}, status=404)
    
        delivery_crews = User.objects.filter(groups=delivery_crew_group)

        delivery_crews_list = [
            {
                "id": crew.id,
                "username": crew.username,
                "email": crew.email,
                "first_name": crew.first_name,
                "last_name": crew.last_name,
            }
            for crew in delivery_crews
        ]

        return Response(delivery_crews_list)
    
    def post(self, request):
        user_id = request.data.get('id')

        if user_id is not None:
            try:
                # Retrieve the user by ID
                user = User.objects.get(id=user_id)

                # Retrieve or create the 'Manager' group
                delivery_group, created = Group.objects.get_or_create(name='Delivery Crew')

                # Add the user to the 'Manager' group
                user.groups.add(delivery_group)

                return Response({'message': f'User {user.username} has been added to the Delivery Crew group.'}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'User ID not provided.'}, status=status.HTTP_400_BAD_REQUEST)
    

    
    
class DeliveryCrewDeleteView(APIView):
    permission_classes = [IsManager]
    def delete(self, request, pk):
        try:
            user = User.objects.get(id=pk)

            try:
                delivery_crew_group = Group.objects.get(name='Delivery Crew')

                
                user.groups.remove(delivery_crew_group)

                return Response({'message': f'User {user.username} has been removed from the Delivery Crew group.'}, status=status.HTTP_200_OK)
            except Group.DoesNotExist:
                return Response({'error': 'Delivery Crew group does not exist.'}, status=status.HTTP_404_NOT_FOUND)
            
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer