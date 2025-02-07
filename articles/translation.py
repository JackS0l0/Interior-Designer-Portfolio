from .models import Categories,Products
from modeltranslation.translator import register, TranslationOptions
@register(Categories)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ['name']
@register(Products)
class ProductsTranslationOptions(TranslationOptions):
    fields = ['name']