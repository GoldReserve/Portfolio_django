from django.db import models
from django.urls import reverse


class Projects(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    description = models.TextField(max_length=2000, default='', verbose_name='Описание')
    # вот с видосами и изображениями надо разобраться я пока хз как это прописать
    image = models.ImageField(null=True, blank=True, upload_to="project_picture/", verbose_name='Изображение')
    video = models.CharField
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=5)
    type = models.ForeignKey('ProjectType', on_delete=models.PROTECT, null=True, verbose_name='Тип проекта')

    def __str__(self):
        return self.title

    # Это по идее метод присвающий странице id и открывающий запись с соответствующим id
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


# У меня будет несколько типов проектов web, diy и т п так что мы сделаем несколько категорий
class ProjectType(models.Model):
    project_type = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.project_type
