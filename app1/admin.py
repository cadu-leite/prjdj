from django.contrib import admin

from app1.models import Emissor, Lancamento


class EmissorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Emissor, EmissorAdmin)


class LancamentoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Lancamento, LancamentoAdmin)