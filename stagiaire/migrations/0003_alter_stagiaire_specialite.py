# Generated by Django 3.2.4 on 2021-06-16 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stagiaire', '0002_alter_stagiaire_formateur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stagiaire',
            name='specialite',
            field=models.CharField(max_length=20, null=True),
        ),
    ]