from django.db import models

# Create your models here.
class QuestionData(models.Model):
    
    QuestionText=models.CharField(default=None, max_length=500,null=False,blank=True)
    QuestionImg=models.ImageField(upload_to="static/question",default=None,null=True,blank=True)
    Option1Text=models.CharField(default=None, max_length=100,null=False,blank=True)
    Option1Img=models.ImageField(default=None, upload_to='static/options',null=True,blank=True)
    Option2Text=models.CharField(default=None, max_length=100,null=False,blank=True)
    Option2Img=models.ImageField(default=None, upload_to='static/options',null=True,blank=True)
    Option3Text=models.CharField(default=None, max_length=100,null=False,blank=True)
    Option3Img=models.ImageField(default=None, upload_to='static/options',null=True,blank=True)
    Option4Text=models.CharField(default=None, max_length=100,null=False,blank=True)
    Option4Img=models.ImageField(default=None, upload_to='static/options',null=True,blank=True)
    CorrectOptionText=models.CharField(default=None, max_length=100,null=False,blank=True)
    CorrectOptionImg=models.ImageField(default=None, upload_to='static/correctoptions',null=True,blank=True)
    QuestionType=models.CharField(default=None, max_length=50,null=False,blank=True)
    QuestionSubject=models.CharField(default=None, max_length=50,null=False,blank=True)

class AddBanner(models.Model):
    BannerImg= models.ImageField(upload_to='static/Banner',default="BannerImage")
    BannerType= models.CharField(max_length=50)

class QuoteCounter(models.Model):
    Quote=models.CharField(max_length=100)