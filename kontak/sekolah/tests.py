from django.test import TestCase
from .models import sekolah
# Create your tests here.

class SekolahTestCase(TestCase):
    def setUp(self):
        sekolah.objects.create(npsn="310231x",nama ="SMKN 2 Sukabumi",status="Negeri")
        

