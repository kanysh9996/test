from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin
from .models import *
import nested_admin


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1

class CarImageInline(nested_admin.NestedStackedInline):
    model = CarImage
    extra = 1

class StateNumberInline(nested_admin.NestedStackedInline):
    model = StateNumber
    extra = 1


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    inlines = [ContactInline]


@admin.register(Car)
class CarAdmin(TranslationAdmin, nested_admin.NestedModelAdmin):
    inlines = [CarImageInline, StateNumberInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Category, CarMake, CarModel)
class AllAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Client)
admin.site.register(Generation)
admin.site.register(Favorite)
admin.site.register(FavoriteItem)
admin.site.register(Review)