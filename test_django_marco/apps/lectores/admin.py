from django.contrib import admin
from apps. import Lector,Preferencia

class PreferenciaInLine(admin.StackedInline):

    model = Preferencia
    max_num = 4
    extra = 0
    verbose_name = 'Preferencias'

class Lector_admin(admin.ModelAdmin):

    list_display = ('name','lastname')

    list_filter = ('name',)

    inlines = [PreferenciaInLine, ]

    fieldsets = (
        (None,{
            'fields':('name','lastname')
        }

        ),
        ('Extra_Data',{
            'fields':('address','email','bdate')
        })
    )

admin.site.register(Lector,Lector_admin)