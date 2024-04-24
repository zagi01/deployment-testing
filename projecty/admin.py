from django.contrib import admin

# Register your models here.

from . models import FirstTry,SecondTry,DetailsFeed

admin.site.register(FirstTry)
admin.site.register(DetailsFeed)
admin.site.register(SecondTry)

