from django.contrib import admin
from .models import Product,TeamMember , Contact ,Categories







class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description') 
class teamadmin(admin.ModelAdmin):
     list_display = ('name', 'designation')
class contactadmin (admin.ModelAdmin):
    list_display = ('name', 'email','message')
class Categories_items (admin.ModelAdmin):
    list_display = ('name', 'description', 'image')


admin.site.register(Product,ProductAdmin)
admin.site.register(TeamMember,teamadmin)
admin.site.register(Contact,contactadmin)
admin.site.register(Categories,Categories_items)



