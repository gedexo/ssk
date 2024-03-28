from django.contrib import admin
from .models import Product,Category,Testimonial,Updates,ClientLogo,ProductEnquiry,Contact,Organization
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category')
    
# @admin.register(Testimonial)
# class TestimonialAdmin(admin.ModelAdmin):
#     list_display = ('name',)
    
@admin.register(Updates)
class UpdatesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug": ("title",)}
  
  
@admin.register(ProductEnquiry)
class ProductEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name','phone','email')  
    
admin.site.register(ClientLogo)
admin.site.register(Contact)
# admin.site.register(Organization)