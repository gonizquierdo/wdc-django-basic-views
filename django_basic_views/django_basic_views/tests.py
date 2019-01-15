from django.test import TestCase


class TasksTestCase(TestCase):

    def test_task_1(self):
        """Should return Hello World while GETing to /hello-world URL"""
        response = self.client.get('/hello-world/')
        assertEqual(response.status_code, 200)
        assertIn('Hello World', str(response.content))
