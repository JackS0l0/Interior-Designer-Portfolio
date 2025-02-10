from modeltranslation.translator import TranslationOptions,register
from .models import MainTexts,AboutInFooter
@register(MainTexts)
class MainTextsTranslationOptions(TranslationOptions):
    fields = ['float1','float2','float3','about','addressTxt']
@register(AboutInFooter)
class AboutInFooterTranslationOptions(TranslationOptions):
    fields = ['txt']