from django.contrib import admin
from django.utils.html import format_html
from .models import Category, SubCategory, Color, Product

# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Display fields in the admin list view
    search_fields = ('name',)  # Search by name
    ordering = ('name',)  # Default ordering by name


# SubCategory Admin
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')  # Display fields in the admin list view
    search_fields = ('name',)  # Search by name
    list_filter = ('category',)  # Add filter by category
    ordering = ('name',)  # Default ordering by name


# Color Admin
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hex_code')  # Display fields in the admin list view
    search_fields = ('name', 'hex_code')  # Search by name and hex code
    ordering = ('name',)  # Default ordering by name


# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product_code', 'title', 'quantity', 'available_item', 'price', 
        'category', 'sub_category', 'image_preview'
    )  # Display key fields in the list view, including an image preview
    search_fields = ('product_code', 'title', 'description')  # Enable search for product_code, title, and description
    list_filter = ('category', 'sub_category', 'colors')  # Add filters for category, subcategory, and colors
    autocomplete_fields = ('category', 'sub_category', 'colors')  # Enable autocomplete for ForeignKey and ManyToManyField
    list_editable = ('quantity', 'price')  # Allow editing these fields directly in the list view
    ordering = ('product_code',)  # Default ordering by product code
    fieldsets = (
        ("Basic Information", {
            'fields': ('product_code', 'title', 'description', 'category', 'sub_category')
        }),
        ("Stock Details", {
            'fields': ('quantity', 'sold_item', 'available_item', 'size')
        }),
        ("Pricing", {
            'fields': ('price', 'wholesale_price', 'special_offers')
        }),
        ("Additional Information", {
            'fields': ('colors', 'delivery_time', 'image')
        }),
    )  # Organize fields into sections in the admin form
    filter_horizontal = ('colors',)  # Improve the ManyToMany field UI in the admin form

    def image_preview(self, obj):
        """Display a thumbnail preview of the product image in the admin list view."""
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;" />'.format(obj.image.url))
        return "No Image"
    image_preview.short_description = "Image Preview"
