# Generated by Django 4.2.7 on 2023-11-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_course_seen_lesson_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='entries_count',
            field=models.IntegerField(default=0),
        ),
    ]
