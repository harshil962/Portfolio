from django.contrib import admin
from .models import Project, Certificate, Contact

admin.site.register(Project)
admin.site.register(Contact)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'date_earned')
    search_fields = ('name', 'issuer')
    list_filter = ('issuer',)