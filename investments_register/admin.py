from django.contrib import admin
from .models import LevelRegister, ShareholderRegister, Rate


admin.site.register(LevelRegister)
admin.site.register(Rate)


@admin.register(ShareholderRegister)
class ShareholderRegisterAdmin(admin.ModelAdmin):
	list_display = ('lastname', 'name', 'patronymic', 'levelUser', 'rate', 'uniqueNumber', 'following', 'created',)
	list_filter = ('levelUser', 'rate', 'created', 'following',)
	search_fields = ('lastname', 'uniqueNumber',)
	prepopulated_fields = {'slug': ('lastname', 'uniqueNumber',)}
	ordering = ('uniqueNumber', 'lastname', 'following',)



