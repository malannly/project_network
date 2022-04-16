from django.contrib import admin
from .models import Post, Group
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk','text','pub_date','author','group',) # pk - primary key - индификационный номер каждой записи
    search_fields = ('text',)
    list_filter = ('pub_date',)
    list_editable = ('group',)
admin.site.register(Post, PostAdmin) # регистрирует модель в админке

class GroupAdmin(admin.ModelAdmin):
    list_display = ('title','description','slug',)
    search_fields = ('title','description',)
admin.site.register(Group, GroupAdmin)