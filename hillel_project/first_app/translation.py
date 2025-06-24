from modeltranslation.translator import TranslationOptions, register, translator

from first_app.models import Position


@register(Position)
class PositionTranslationOption(TranslationOptions):
    fields = ("title", "description")


