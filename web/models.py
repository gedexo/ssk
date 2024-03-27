from django.db import models
from django.urls import reverse_lazy
from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=255) 
  image = models.ImageField(upload_to='media')
  
  def __str__(self):
      return self.name
  
  
class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  image = models.ImageField(upload_to='media')
  description = models.TextField(null=True,blank=True)
  
  def __str__(self):
      return self.name
  
    

class Testimonial(models.Model):
  image = models.ImageField(upload_to='media',null=True,blank=True)
  name = models.CharField(max_length=255)
  designation = models.CharField(max_length=255,null=True,blank=True)
  description = models.TextField()
  
  
  def __str__(self):
      return self.name
  
  
class Updates(models.Model):
    image = models.ImageField(upload_to = "event")
    date  = models.DateField(blank=True,null=True)
    title = models.CharField(max_length=100)
    slug= models.SlugField()
    description = HTMLField()
    
    
    def get_absolute_url(self):
        return reverse_lazy("web:update_detail", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = ('Update')
        verbose_name_plural = ('Updates')

    def __str__(self):
        return self.title
      
      
      
  
class ClientLogo(models.Model):
    image = models.ImageField(upload_to="media")
    
    def __str__(self):
        return str(self.image)
      
      

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    
    def __str__(self):
        return self.name
      
  
class ProductEnquiry(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email= models.EmailField(null=True,blank=True)
    message = models.TextField()
    
    
    class Meta:
        verbose_name = ('Product Enquiry')
        verbose_name_plural = ('Product Enquiries')

    def __str__(self):
        return self.name
      
  
class Organization(models.Model):
    image = models.ImageField(upload_to="media",null=True,blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.name