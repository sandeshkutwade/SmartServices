from django.contrib import admin

# Register your models here.
from . models import Partners,Category,Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    lis_display = ['Name','slug']
    prepopulated_fields={'slug':('Name',)}

@admin.register(Partners)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['Name','Address','Contact','price','category']
    list_editable = ['price']
    prepopulated_fields = {'slug':('Name',)}

  
admin.site.register(Order)
