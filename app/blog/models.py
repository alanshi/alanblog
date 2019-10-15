from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=200, help_text='标题')
    desc = models.CharField(max_length=200, help_text='描述,小标题')
    content = RichTextField(help_text='内容')
    created = models.DateTimeField(auto_now_add=True, help_text='创建时间')

    class Meta:
        db_table = 'article'
        ordering = ('-id',)