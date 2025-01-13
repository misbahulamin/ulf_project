from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
class Color(models.Model):
    COLOR_CHOICES = [
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Green', 'Green'),
    ('Yellow', 'Yellow'),
    ('Black', 'Black'),
    ('White', 'White'),
    ('Gray', 'Gray'),
    ('Pink', 'Pink'),
    ('Purple', 'Purple'),
    ('Orange', 'Orange'),
    ('Brown', 'Brown'),
    ('Cyan', 'Cyan'),
    ('Magenta', 'Magenta'),
    ('Lime', 'Lime'),
    ('Teal', 'Teal'),
    ('Navy', 'Navy'),
    ('Maroon', 'Maroon'),
    ('Olive', 'Olive'),
    ('Gold', 'Gold'),
    ('Silver', 'Silver'),
    ('Beige', 'Beige'),
    ('Ivory', 'Ivory'),
    ('Turquoise', 'Turquoise'),
    ('Coral', 'Coral'),
    ('Lavender', 'Lavender'),
    ('Mint', 'Mint'),
    ('Peach', 'Peach'),
    ('Chocolate', 'Chocolate'),
    ('Crimson', 'Crimson'),
    ('Fuchsia', 'Fuchsia'),
    ('Khaki', 'Khaki'),
    ('Aquamarine', 'Aquamarine'),
    ('Indigo', 'Indigo'),
    ('Plum', 'Plum'),
    ('Chartreuse', 'Chartreuse'),
    ('Amber', 'Amber'),
    ('Sapphire', 'Sapphire'),
    ('Emerald', 'Emerald'),
    ('Ruby', 'Ruby'),
    ('Slate', 'Slate'),
    ]
    name = models.CharField(
        max_length=255, 
        choices=COLOR_CHOICES,
        help_text="Comma-separated list of colors (e.g., 'Red,Blue,Green')"
    )
    hex_code = models.CharField(max_length=7, unique=True)  # Optional HEX code, e.g., #FF5733

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)  # New image field
    colors = models.ManyToManyField(Color, related_name='products')
    description = models.TextField()
    size = models.CharField(max_length=100)
    sold_item = models.PositiveIntegerField(default=0)
    available_item = models.PositiveIntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    special_offers = models.TextField(null=True, blank=True)
    delivery_time = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product_code} - {self.title} - Quantity: {self.quantity}"