# Generated by Django 5.0.7 on 2024-07-31 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_products_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='Category_name',
            new_name='category_name',
        ),
    ]
