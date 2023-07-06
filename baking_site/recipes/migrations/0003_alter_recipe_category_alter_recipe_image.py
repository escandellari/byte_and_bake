# Generated by Django 4.2.2 on 2023-07-06 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(blank=True, choices=[('bread', 'bread'), ('biscuits', 'biscuits'), ('cakes', 'cakes'), ('worldwide', 'worldwide')], default='uncategorised', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
