from django.contrib import admin
from contact import models
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'phone',)
    ordering = ('id',)
    list_filter = ('created_data',)
    list_per_page = 10
    list_max_show_all = 50
    
