# Generated by Django 4.2.2 on 2023-06-15 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_file_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to=settings.AUTH_USER_MODEL),
        ),
    ]