from django.contrib import admin
from newsapp.models import (Category , News , Author)
# Register your models here.




# list_display=('title','content','created_at','updated_at','photos','is_bool')
#     list_display_links=('title','content') #link qib beradi
    # search_fields=('title','content') # search qo'shib beradi
class NewsAdmin(admin.ModelAdmin):
    ordering=['created_at']
    list_display=(
        ['id' , 'title' , 'photo' , 'created_at' , 'views' , 'author_id']
    )
    list_display_links=('id',) #link qib beradi
    search_fields=('id','title','content','author_id') # search qo'shib beradi

admin.site.site_header="TheNews.Uz"
admin.site.index_title="manage News"


class CategoryAdmin(admin.ModelAdmin):
    ordering=['created_at']
    list_display=(
        ['id' , 'title' , 'photos' , 'created_at' , 'author_id']
    )
    list_display_links=('id',) #link qib beradi
    search_fields=('id','title','author_id') # search qo'shib beradi


class AuthorAdmin(admin.ModelAdmin):
    ordering=['created_at']
    list_display=(
        ['id' , 'first_name' , 'last_name' , 'profession' , 'phone_number','telegram','email','photo','created_at','user_id']
    )
    list_display_links=('id',) #link qib beradi
    search_fields=('id','first_name','last_name','profession','phone_number','user_id') # search qo'shib beradi



admin.site.register(News,NewsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Author,AuthorAdmin)

