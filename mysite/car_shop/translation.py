from .models import Category, CarMake, CarModel, Car
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', )


@register(CarMake)
class CareMakeTranslationOptions(TranslationOptions):
    fields = ('carmake_name', )


@register(CarModel)
class CarModelTranslationOptions(TranslationOptions):
    fields = ('carmodel_name', )


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('description', )