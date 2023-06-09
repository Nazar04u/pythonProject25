# Generated by Django 4.1.4 on 2023-05-23 18:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('realization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=10000)),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 5, 23, 18, 30, 34, 719788, tzinfo=datetime.timezone.utc))),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assess', models.IntegerField()),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 5, 23, 18, 30, 34, 718789, tzinfo=datetime.timezone.utc))),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realization.goods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='BasketItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('basket', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='realization.basket')),
                ('goods', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='realization.goods')),
            ],
        ),
        migrations.AddField(
            model_name='basket',
            name='items',
            field=models.ManyToManyField(through='realization.BasketItems', to='realization.goods'),
        ),
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
