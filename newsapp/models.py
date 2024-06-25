from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator , URLValidator

from django.contrib.auth.models import Group, Permission 

# Create your models here.

from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# class APIUsageLog(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     endpoint = models.CharField(max_length=255)
#     request_method = models.CharField(max_length=10)
#     ip_address = models.CharField(max_length=50)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user} - {self.endpoint} - {self.request_method}"




class Category(models.Model):
    title=models.CharField(max_length=100 , verbose_name='category of news')
    photos=models.ImageField(upload_to='photos/category/%Y/%m/%d/',blank=True , verbose_name="Rasm")#chislosi bilan saralab ketadi (blank=True bunda rasm qo'shmasaham bo'ladi)
    is_bool=models.BooleanField(verbose_name="Hoziroq saytga joylansinmi ?" , default=False) #default=True
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="Kirish vaqti")# ma'lumot qo'shgan paytizni qo'shib ketadi, yozib ketadi
    author_id=models.ForeignKey(User , on_delete=models.CASCADE , verbose_name="Categoriya muallifi")


    def __str__(self):
        return self.title
    
    # class Meta:
    #     verbose_name="Kategoriya"
    #     verbose_name_plural="Kategoriyalar"
    
    class Meta:
        verbose_name="Categoriya"
        verbose_name_plural="Categoriyalar"
        ordering=['created_at']


class News(models.Model):
    theme=models.CharField(max_length=1000,verbose_name="Mavzu")
    title=models.CharField(max_length=2000,verbose_name="Sarlavha")
    content = RichTextField(verbose_name='Content')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at=models.DateTimeField(auto_now=True, verbose_name="Ynagilangan vaqti")
    photo=models.ImageField(upload_to='photos/news/%Y/%m/%d/',blank=True , verbose_name="Rasm")
    # video_url=
    is_bool=models.BooleanField(default=False , verbose_name="Postni keyinroqqa rejalashtirasizmi ?")
    views=models.IntegerField(default=0,verbose_name="Ko'rinishlar soni")
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE , verbose_name="Post categoriyasi")
    author_id=models.ForeignKey(User , on_delete=models.CASCADE , verbose_name="Post muallifi")
    to_telegram=models.BooleanField(default=False, verbose_name="Postni Telegramga joylansinmi ?")

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name="Post"
        verbose_name_plural="Postlar"
        ordering=['created_at']
    

class Author(models.Model):
    phone_regex=RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Phone number nust be entered in the format: '+998906417999'. Up to 14 digits allowed")
    email_regex=RegexValidator(regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', message="email nust be entered in the format: 'example@demein'-> oqiljonnishonov@gmail.com.")
    first_name=models.CharField(max_length=100 , verbose_name='First name')
    last_name=models.CharField(max_length=100 , verbose_name='Last name')
    profession=models.CharField(max_length=100 , verbose_name='Profession')
    phone_number=models.CharField(validators=[phone_regex],max_length=20,unique=True)
    telegram=models.URLField(unique=True , validators=[RegexValidator(message="telegram url mast be : https://t.me/Oqil_islomov ")])
    email=models.CharField(validators=[email_regex],max_length=50,unique=True)
    photo=models.ImageField(upload_to='photos/authors/%Y/%m/%d/',blank=True , verbose_name="Rasm")
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="User id",null=True,default=None)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name="Author"
        verbose_name_plural="Authors"
        ordering=['created_at']
    