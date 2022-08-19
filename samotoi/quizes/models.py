from django.db import models

DIF_CHOICES = (
    ('easy', 'easy')
    ('medium', 'medium')
    ('hard', 'hard')
)

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField()
    difficluty = models.CharField(max_length=6, choices=DIF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        pass