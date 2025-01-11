# persons/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Person


class PersonAPITests(APITestCase):

    def setUp(self):
        self.person = Person.objects.create(name="Ali Dalla", age=30 ,address="moscow", work="student")

    def test_get_all_persons(self):
        url = reverse('person-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Ali Dalla")

    def test_get_person_by_id(self):
        url = reverse('person-detail', args=[self.person.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Ali Dalla")

    def test_create_person(self):
        url = reverse('person-list')
        data = {'name': 'Maria Dalla', 'age': 25 , 'address' : 'moscow', 'work' : 'student'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('Location', response.headers)
        self.assertEqual(Person.objects.count(), 2)
        self.assertEqual(Person.objects.get(id=2).name, 'Maria Dalla')

    def test_update_person(self):
        url = reverse('person-detail', args=[self.person.id])
        data = {'age': 31}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.person.refresh_from_db()
        self.assertEqual(self.person.age, 31)

    def test_delete_person(self):
        url = reverse('person-detail', args=[self.person.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)

    def test_get_nonexistent_person(self):
        url = reverse('person-detail', args=[999])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
