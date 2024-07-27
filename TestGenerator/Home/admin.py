from django.contrib import admin

# Register your models here.
from .models import *

class QuestionDataAdmin(admin.ModelAdmin):
    list_display=("QuestionText","QuestionImg","Option1Text","Option1Img","Option2Text","Option2Img","Option3Text","Option3Img","Option4Text","Option4Img","CorrectOptionText","CorrectOptionImg","QuestionType","QuestionSubject")

class AddBaneerAdmin(admin.ModelAdmin):
    list_display=("BannerImg","BannerType")


class QuoteCounterAdmin(admin.ModelAdmin):
    list_display=("Quote",)

admin.site.register(QuoteCounter,QuoteCounterAdmin)
admin.site.register(AddBanner,AddBaneerAdmin)
admin.site.register(QuestionData,QuestionDataAdmin)