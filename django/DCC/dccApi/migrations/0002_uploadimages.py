# Generated by Django 3.0.7 on 2020-12-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dccApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_Img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
