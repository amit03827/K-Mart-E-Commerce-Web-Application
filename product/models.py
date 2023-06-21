from typing import Iterable, Optional
from django.db import models
from django.template .defaultfilters import slugify


class ProductCategory(models.Model):
    """Product Category Models"""
    name=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255, null=True, blank=True)
    image=models.ImageField(upload_to='product_categorys')
    status=models.BooleanField(default=True)
    show_on_homepage=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """ Override Save method of super model"""
        self.slug= slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)
        
class ProductVariation(models.Model):
    name=models.CharField(max_length=255)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ProductTag(models.Model):   
    name=models.CharField(max_length=255)
    status=models.BooleanField(default=True, null=True, blank=True)
    slug=models.SlugField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        """ Override Save method of super model"""
        self.slug= slugify(self.name)
        super(ProductTag, self).save(*args, **kwargs)

class Product(models.Model):
    product_category =models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255, null=True, blank=True)
    cover_image=models.ImageField(upload_to='media')
    price=models.DecimalField(max_digits=7, decimal_places=2)
    discription=models.TextField()
    variation=models.ManyToManyField(ProductVariation)
    tags=models.ManyToManyField(ProductTag)
    status=models.BooleanField(default=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """ Override Save method of super model"""
        self.slug= slugify(self.name)
        super(Product, self).save(*args, **kwargs)
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ProductImage")  
    image = models.ImageField(upload_to='products')  
  
    def __str__(self):
        return str(self.id)
    


