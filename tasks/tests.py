from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task

class TaskTests(APITestCase):
    def setUp(self):
        self.data = {
            "title": "learn django",
            "description": 'using udemy',
           
        }
        self.response = self.client.post(
            reverse('tasks:tasks-list'),
            self.data,
            format="json")


    def test_api_create_task(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'learn django')

    def test_api_list_tasks(self):
        url = reverse('tasks:tasks-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)

    def test_api_can_get_a_task(self):
        task = Task.objects.get()
        response = self.client.get(
            reverse('tasks:tasks-detail',
            kwargs={'pk': task.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, task)

    def test_api_can_update_a_task(self):
        task = Task.objects.get()
        new_data = {
            "title": "learn angular",
            "description": 'using freecodecamp',
        }
        response = self.client.put(
            reverse('tasks:tasks-detail',
            kwargs={'pk': task.id}), data=new_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().title, 'learn angular')

    def test_api_can_delete_a_task(self):
        task = Task.objects.get()
        response = self.client.delete(
            reverse('tasks:tasks-detail',
            kwargs={'pk': task.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)