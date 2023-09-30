from django.contrib import admin

from app.models import Owner, Product, Lesson

admin.site.register(Lesson)
admin.site.register(Owner)
admin.site.register(Product)