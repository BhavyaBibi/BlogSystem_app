# Generated by Django 3.0.5 on 2021-03-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_read'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pk']},
        ),
        migrations.AddField(
            model_name='author',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
