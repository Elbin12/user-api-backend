from django.db.models import Q

from .serializers import UserSerializer
from .models import CustomUser

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class CustomPagination(PageNumberPagination):
    """
    Custom pagination class to support `limit` and `page` query parameters.
    Default page size is 5.
    """
    page_size = 5
    page_size_query_param = 'limit'
    page_query_param = 'page' 

    def get_paginated_response(self, data):
        """
        Returns paginated data without extra metadata.
        """
        return Response(data)

class UsersListCreateView(APIView):
    """
    API view to handle listing and creating users.
    Supports filtering by name, sorting, and pagination.
    """
    def get(self, request):
        """
        GET method to list users with support for:
        - name: substring match in first/last name (case-insensitive)
        - sort: order by any field, use '-' prefix for descending
        - pagination: page and limit
        """
        name_query = request.query_params.get('name')
        sort_by = request.query_params.get('sort')
        users = CustomUser.objects.all()

        # Filter by first_name or last_name if name query exists
        if name_query:
            users = users.filter(
                Q(first_name__icontains=name_query) | Q(last_name__icontains=name_query)
            )
        
        # Sort the queryset if sort parameter exists
        if sort_by:
            users = users.order_by(sort_by)

        paginator = CustomPagination()
        paginated_users = paginator.paginate_queryset(users, request)
        serializer = UserSerializer(paginated_users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        POST method to create a new user.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class UserDetailView(APIView):
    """
    API view to retrieve, update, or delete a user by ID.
    """
    def get(self, request, id):
        """
        GET method to retrieve a single user by ID.
        Returns 404 if not found.
        """
        try:
            user = CustomUser.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=200)
        except CustomUser.DoesNotExist:
            return Response({'error':'user not found.'}, status=404)
        
    def put(self, request, id):
        """
        PUT method to update a user (partial update supported).
        Returns 404 if not found.
        """
        try:
            user = CustomUser.objects.get(id=id)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        except CustomUser.DoesNotExist:
            return Response({'error':'user not found.'}, status=404)
        
    def delete(self, request, id):
        """
        DELETE method to remove a user by ID.
        Returns 404 if not found.
        """
        try:
            user = CustomUser.objects.get(id=id)
            user.delete()
            return Response(status=200)
        except CustomUser.DoesNotExist:
            return Response({'error':'user not found.'}, status=404)