from django.db import models
from django.contrib.auth.models import User

MAX_TITLE_LEN = 255

class QuestionManager(models.Manager):
    def popular(self):
        return self.oreder_by('-likes')

    def new(self):
        return self.order_by('-created_at')

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(blank=True, null=True)

class Question(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    title = models.CharField(max_length=MAX_TITLE_LEN)
    text = models.TextField()
    image = models.ImageField()
    tags = models.ManyToManyField('Tag', related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    correct = models.BooleanField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=MAX_TITLE_LEN, unique=True)


class QuestionLike(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user', 'question')


class AnswerLike(models.Model):
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user', 'answer')
