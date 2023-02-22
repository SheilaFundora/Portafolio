# Generated by Django 4.1.3 on 2023-02-21 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_categories_portafolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portafolio',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.categories'),
            preserve_default=False,
        ),
    ]
