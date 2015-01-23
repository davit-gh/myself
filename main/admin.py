from django.contrib import admin
from main.models import IconBlurb
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from main.models import PortfolioItem, PortfolioItemImage, PortfolioItemCategory

admin.site.register(IconBlurb,admin.ModelAdmin)

class PortfolioItemImageInline(TabularDynamicInlineAdmin):
	model=PortfolioItemImage

class PortfolioItemAdmin(admin.ModelAdmin):
	inlines=(PortfolioItemImageInline, )

admin.site.register(PortfolioItem,PortfolioItemAdmin)
admin.site.register(PortfolioItemCategory)

from main.models import Contactus
class ContactusAdmin(admin.ModelAdmin):
	list_display=('name','email','title','description', 'message_date')

admin.site.register(Contactus,ContactusAdmin)
