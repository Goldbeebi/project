# Generated by Django 4.1.3 on 2022-12-18 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=500)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]