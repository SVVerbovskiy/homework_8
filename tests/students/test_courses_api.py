from model_bakery import baker
from rest_framework.test import APIClient
import pytest

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def courses():
    return baker.make(Course, _quantity=10)


@pytest.fixture
def student():
    return Student.objects.create(name='Ivan', birth_date='1988-08-02')


