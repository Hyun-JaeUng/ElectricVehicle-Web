from django.db import models

# Create your models here.
class ElectricCarList(models.Model) :
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=True)
    subname = models.CharField(max_length=30, null=True)
    chargetype = models.CharField(max_length=30, null=True)
    onedistance = models.IntegerField(null=True)
    battery = models.IntegerField(null=True)
    fastcharge = models.CharField(max_length=30, null=True)
    slowcharge = models.CharField(max_length=30, null=True)
    rank = models.IntegerField(null=True)
    price = models.CharField(max_length=30, null=True)

class Question(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    # modify_date = models.DateTimeField(null=True, blank=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    # modify_date = models.DateTimeField(null=True, blank=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.content

## 영민
class User(models.Model):
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=100)
    name = models.CharField(max_length=10)
    Car_Model = models.CharField(max_length=30)
