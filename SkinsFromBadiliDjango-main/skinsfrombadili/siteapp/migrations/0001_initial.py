# Generated by Django 5.0 on 2023-12-14 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frontIMG', models.ImageField(upload_to='')),
            ],
        ),
    ]
