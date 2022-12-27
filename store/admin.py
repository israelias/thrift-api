from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from versatileimagefield.fields import SizedImageCenterpointClickDjangoAdminField

from .models import Category, Image, Product

admin.site.register(Category, DraggableMPTTAdmin)
admin.site.register(Image)


class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'owner', 'title']


class ImageInline(admin.StackedInline):
    model = Image
    fk_name = "product"
    # image = SizedImageCenterpointClickDjangoAdminField(required=False)
    fields = ("name", "alt_text", "is_feature", "product",  "id")

# list_display = ('__str__',)
#     list_display_links = ()
#     list_filter = ()
#     list_select_related = False
#     list_per_page = 100
#     list_max_show_all = 200
#     list_editable = ()
#     search_fields = ()
#     date_hierarchy = None
#     save_as = False
#     save_as_continue = True
#     save_on_top = False
#     paginator = Paginator
#     preserve_filters = True
#     inlines = []


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display_links = ['id', 'vendor', 'category']
    list_select_related = True
    list_display = ['id', 'title', 'vendor', 'is_available', 'condition', 'category', 'created_at']
    list_fiter = ('category', 'is_available', 'vendor' 'condition')
    search_fields = ['title', 'vendor', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        ImageInline,
      
    ]
