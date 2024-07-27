from django.shortcuts import render
from .models import *
import random

# Create your views here.
def HomePage(request):
    Quote=list(QuoteCounter.objects.all())
    BannerImgs= list(AddBanner.objects.all())
    BannerImg1=random.choice(BannerImgs)
    Quote= random.choice(Quote)
    data={"Quote":Quote,"BannerImg1":BannerImg1}
    return render(request,"Home.html",data)