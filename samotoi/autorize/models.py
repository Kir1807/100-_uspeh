from django.db import models
from django.contrib.auth.models import User

class users(models.Model):
    name = models.CharField('Имя', max_length=50)
    password = models.CharField('Пароль', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_questions = models.IntegerField()
    time = models.IntegerField()
    time = models.IntegerField()
    def __str__(self):
        return f"{self.name}-{self.topic}"

    def questions(self):
        return self.question_set.all()[:self.number_questions]

class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)

    def answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=220)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)