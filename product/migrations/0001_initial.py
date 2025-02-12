# Generated by Django 5.1.4 on 2025-01-12 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Black', 'Black'), ('White', 'White'), ('Gray', 'Gray'), ('Pink', 'Pink'), ('Purple', 'Purple'), ('Orange', 'Orange'), ('Brown', 'Brown'), ('Cyan', 'Cyan'), ('Magenta', 'Magenta'), ('Lime', 'Lime'), ('Teal', 'Teal'), ('Navy', 'Navy'), ('Maroon', 'Maroon'), ('Olive', 'Olive'), ('Gold', 'Gold'), ('Silver', 'Silver'), ('Beige', 'Beige'), ('Ivory', 'Ivory'), ('Turquoise', 'Turquoise'), ('Coral', 'Coral'), ('Lavender', 'Lavender'), ('Mint', 'Mint'), ('Peach', 'Peach'), ('Chocolate', 'Chocolate'), ('Crimson', 'Crimson'), ('Fuchsia', 'Fuchsia'), ('Khaki', 'Khaki'), ('Aquamarine', 'Aquamarine'), ('Indigo', 'Indigo'), ('Plum', 'Plum'), ('Chartreuse', 'Chartreuse'), ('Amber', 'Amber'), ('Sapphire', 'Sapphire'), ('Emerald', 'Emerald'), ('Ruby', 'Ruby'), ('Slate', 'Slate')], help_text="Comma-separated list of colors (e.g., 'Red,Blue,Green')", max_length=255)),
                ('hex_code', models.CharField(max_length=7, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('size', models.CharField(max_length=100)),
                ('sold_item', models.PositiveIntegerField(default=0)),
                ('available_item', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('wholesale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('special_offers', models.TextField(blank=True, null=True)),
                ('delivery_time', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category')),
                ('colors', models.ManyToManyField(related_name='products', to='product.color')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.subcategory')),
            ],
        ),
    ]
