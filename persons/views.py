# persons/views.py

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    """
    A simple ViewSet for listing, retrieving, creating, updating, and deleting Persons.
    """

    def list(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            person = Person.objects.get(pk=pk)
            serializer = PersonSerializer(person)
            return Response(serializer.data)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            person = serializer.save()
            headers = {'Location': f'/api/v1/persons/{person.id}'}
            return Response(status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            person = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            person = Person.objects.get(pk=pk)
            person.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
