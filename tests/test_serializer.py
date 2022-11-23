from asosiy.serializers import *
from asosiy.models import *
from unittest import TestCase
from django.contrib.auth.models import User


class TestSuvSer(TestCase):
    def setUp(self) -> None:
        self.data = {"brend": "Fanta", "narx": 3000,
                             "litr":1,"batafsil":"Great water"}

    def test_suv_ser(self):
        assert self.data['brend'] == "Fanta"
        assert self.data['narx'] == 3000
        assert self.data['litr'] == 1
        assert self.data['batafsil'] == "Great water"

class TestMijozSer(TestCase):
    def setUp(self) -> None:
        self.data = {"ism": "Aziz", "tel": "1555",
                             "manzil":"margilan", "qarz":15, "user":User.objects.get(id=1)}

    def test_suv_mijoz(self):
        assert self.data['ism'] == "Aziz"
        assert self.data['tel'] == "1555"
        assert self.data['manzil'] == "margilan"
        assert self.data['qarz'] == 15
        assert self.data['user'] == User.objects.get(id=1)

