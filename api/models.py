from django.db import models
# Create your models here.


class Material(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    stock = models.IntegerField()




# class Survey(models.Model):
#     date_time = models.DateTimeField()
#     name_person = models.CharField(max_length=100)
#     description = models.TextField()
#
# class Question(models.Model):
#     survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
#     text = models.TextField()
#
# class Response(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     text = models.TextField()
#
# class UserSurvey(models.Model):
#     name_person = models.ForeignKey(Survey, on_delete=models.CASCADE)
#     survey = models.ForeignKey(Survey, on_delete=models.CASCADE)