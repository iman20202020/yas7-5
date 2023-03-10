# Generated by Django 3.1.4 on 2021-03-30 14:48

import accounts.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210328_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='degree_image',
            field=models.ImageField(blank=True, help_text='عکس مدرک تحصیلی خود را بارگذاری کنید', upload_to='images/', validators=[accounts.validators.validate_image_size]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', validators=[accounts.validators.validate_image_size]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='national_card_image',
            field=models.ImageField(blank=True, help_text='عکس خود را اینجا بارگذاری کنید', upload_to='images/', validators=[accounts.validators.validate_image_size]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='sample_video',
            field=models.FileField(blank=True, help_text='یک ویدیو حداکثر سه دقیقه از تدریس خود بارگذاری کنید', upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'wmv']), accounts.validators.validate_video_size]),
        ),
    ]
