from django.db import models

# Create your models here.
class FirstTry(models.Model):
    survay_question1 = models.CharField(max_length=200)
    survay_question2 = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.survay_question1},{self.survay_question2}"





class SecondTry(models.Model):
    second_survay1 = models.CharField(max_length=200)
    second_survay2 = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.second_survay1},{self.second_survay2}"


class DetailsFeed(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    phone_number = models.IntegerField(max_length=10)
    security_number = models.IntegerField(max_length=6)
    email = models.EmailField()


    def __str__(self):
        return f"""{self.first_name},
        {self.second_name     },
        {self.user_name},
        {self.phone_number},
        {self.security_number},
        {self.email}"""