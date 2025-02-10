from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import HeaderBackgroud,MainTexts,AboutInFooter,Partners
admin.site.register(Partners)
admin.site.register(HeaderBackgroud)
@admin.register(MainTexts)
class MainTextsControl(TranslationAdmin):
    group_fieldsets = True
    fields=['float1','float2','float3','about','addressTxt','addressUrl','phone','whatsapp','telegram']
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
@admin.register(AboutInFooter)
class AboutInFooterControl(TranslationAdmin):
    group_fieldsets = True 
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }