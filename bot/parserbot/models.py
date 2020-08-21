from django.db import models


# Create your models here.


class Profile(models.Model):
    external_id = models.PositiveBigIntegerField(
        verbose_name='ID of user\'s telegram',
        unique=True,
    )
    name = models.TextField(
        verbose_name='nickname of user\'s telegram',
    )
    score_homework_1 = models.PositiveIntegerField(
        verbose_name='homework_1',
    )
    score_homework_2 = models.PositiveIntegerField(
        verbose_name='homework_2',
    )
    score_homework_3 = models.PositiveIntegerField(
        verbose_name='homework_3',
    )
    total_score = models.PositiveIntegerField(
        verbose_name='total_score'
    )

    def save(self, *args, **kwargs):
        self.total_score = self.score_homework_1 + self.score_homework_2 + self.score_homework_3
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Profile'
