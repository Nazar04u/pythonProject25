# Generated by Django 4.1.4 on 2023-05-23 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realization', '0007_alter_comment_date_alter_question_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 23, 15, 24, 6, 627689, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 23, 15, 24, 6, 627689, tzinfo=datetime.timezone.utc)),
        ),
    ]
