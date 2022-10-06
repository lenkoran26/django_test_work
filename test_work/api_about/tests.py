from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api_about.models import Resume
from api_about.serializers import ResumeSerializer
from django.contrib.auth.models import User

class ResumeApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='user')
        self.data = {
            "id": 1,
            "status": "free",
            "grade": "junior",
            "specialty": "Java",
            "salary": 50000.0,
            "education": "High school",
            "experience": "No",
            "portfolio": "",
            "title": "resume_1",
            "phone": "354565",
            "email": "user@example.com",
            "user": self.user
        }
        resume_1 = Resume.objects.create(**self.data)
        self.serializer_data = ResumeSerializer([resume_1, ], many=True).data

    def test_get(self):
        url = reverse('resume-list')
        response = self.client.get(url)
        self.assertEqual(self.serializer_data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_path(self):
        user = User.objects.get(pk=self.user.id)
        self.client.force_login(user=user)
        url = reverse('resume-detail', kwargs={'pk': 1}, )
        data = {"grade": "middle",
                "specialty": "Python"
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Resume.objects.get().grade, response.data['grade'])
        self.assertEqual(Resume.objects.get().specialty, response.data['specialty'])

