from django.contrib import admin
from .models import Project, Certificate, Contact, Skill, Timeline, Testimonial

# Existing registrations
admin.site.register(Project)
admin.site.register(Contact)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'date_earned')
    search_fields = ('name', 'issuer')
    list_filter = ('issuer',)

# --- ADD THESE LINES ---
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)

@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'category', 'start_date')
    list_filter = ('category',)

admin.site.register(Testimonial)