from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class Group(models.Model):
    title = models.TextField()
    description = models.TextField()
    slug = models.SlugField() # ограничение по символам (ascii)/адресс
    def __str__(self) -> str:
        return self.title
    
class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True) # дата публикации
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts') # ForeignKey = id
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name = 'posts', blank = True, null = True)