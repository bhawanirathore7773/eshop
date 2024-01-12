from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=200)

    def ragister(self):
        self.save()

    @property
    def IsExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    @property
    def IsExistsPhone(self):
        if Customer.objects.filter(phone=self.phone):
            return True
        return False

    @staticmethod
    def login_by_email_id(email):
        try:
            return Customer.objects.get(email=email)
        except :
            return False

