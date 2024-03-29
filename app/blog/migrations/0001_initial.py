# Generated by Django 2.2.6 on 2019-10-15 07:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='标题', max_length=200)),
                ('desc', models.CharField(help_text='描述,小标题', max_length=200)),
                ('content', ckeditor.fields.RichTextField(help_text='内容')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
            ],
            options={
                'db_table': 'article',
                'ordering': ('-id',),
            },
        ),
    ]
