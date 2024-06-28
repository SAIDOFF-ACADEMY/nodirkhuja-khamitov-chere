from modeltranslation.translator import register, TranslationOptions

from .models import Product

@register(Product)
class ProductTranslationObject(TranslationOptions):
    fields = ('name', 'content')

