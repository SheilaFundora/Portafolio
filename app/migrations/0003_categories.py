# Generated by Django 4.1.3 on 2023-02-21 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_delete_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('portafolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.portafolio')),
            ],
        ),
    ]
