from modeltranslation.translator import register, TranslationOptions
from .models import Furniture

@register(Furniture)
class FurnitureTranslationOptions(TranslationOptions):
    fields = ("furniture_name", "furniture_description" )

