from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count, F

MAX_TITLE_LEN = 255

class QuestionManager(models.Manager):
    def popular(self):
        return self.annotate(likes_count=Count('likes')).order_by('-likes_count')

    def new(self):
        return self.order_by('-created_at')

    def tag(self, tag):
        return self.filter(tags=tag)


class ProfileManager(models.Manager):
    def best(self):
        return self.annotate(
            question_likes=Count('questions__likes', distinct=True),
            answer_likes=Count('answers__likes', distinct=True)
        ).annotate(
            total_likes=F('question_likes') + F('answer_likes')
        ).order_by('-total_likes')[:5]


class TagsManager(models.Manager):
    def popular(self):
        return self.annotate(num_questions=Count('questions')).order_by('-num_questions')[:8]


class AnswerManager(models.Manager):
    def answers(self, question):
        return self.filter(question=question)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(blank=True, null=True)
    objects = ProfileManager()


class Question(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    title = models.CharField(max_length=MAX_TITLE_LEN)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)
    objects = QuestionManager()


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
    correct = models.BooleanField(default=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = AnswerManager()


class Tag(models.Model):
    name = models.CharField(max_length=MAX_TITLE_LEN, unique=True)
    objects = TagsManager()


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
