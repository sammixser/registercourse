# Generated by Django 3.1.1 on 2020-09-23 15:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('cName', models.CharField(max_length=50)),
                ('term', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('year', models.IntegerField()),
                ('quota', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)])),
                ('flag', models.BooleanField()),
                ('enroll', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]