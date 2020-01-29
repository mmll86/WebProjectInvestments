from django.contrib import admin
from .models import ShareholderRegister, Rate

admin.site.register(Rate)

@admin.register(ShareholderRegister)
class ShareholderRegisterAdmin(admin.ModelAdmin):
	list_display = ('lastname', 'name', 'patronymic',
	                'uniqueNumber', 'level', 'rate',
	                'sumInveted', 'interest', 'sumRevenue',
	                'invitee', 'invited', 'created',
	                'checkUpdate',)
	list_filter = ('created', 'invitee', 'invited',)
	search_fields = ('lastname', 'name', 'patronymic', 'uniqueNumber',)
	prepopulated_fields = {'slug': ('lastname', 'name', 'patronymic', 'uniqueNumber',)}
	ordering = ('uniqueNumber', 'lastname', 'invitee', 'invited',)



