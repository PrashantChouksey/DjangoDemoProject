from django.db import models

# Create your models here.
class Question(models.Model):

    qus_text= models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")

    def __str__(self):
        return self.qus_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    qus_id = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

