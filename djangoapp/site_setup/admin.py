from django.contrib import admin
from site_setup.models import MenuLink, SiteSetup


class MenuLinkInLine(admin.TabularInline):
    model = MenuLink
    extra = 1


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',
    inlines = MenuLinkInLine,

    # Função padrão do Django que permite ou não adicionar novos valores
    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()
