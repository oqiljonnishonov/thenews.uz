from rest_framework import serializers
from django.forms import ValidationError
from newsapp.models import (Category , News , Author)


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id','title','photos','is_bool')


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model=News
        fields=('id','title','content','photo','is_bool','category_id','author_id')


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=('id','first_name','last_name','profession','phone_number','telegram','email','user_id')