from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name', 'score_homework_1', 'score_homework_2', 'score_homework_3','score_homework_4', 'total_score')