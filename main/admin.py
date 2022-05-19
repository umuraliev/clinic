from django.contrib import admin
from .models import Doctor, Speciality, Direction

# class SpecialityAdmin(admin.ModelAdmin):
#     list_display = ('title','slug', 'direction')
#     list_display_links = ('title', 'direction')
#     prepopulated_fields = {'slug': ('title', )}


admin.site.register(Doctor)
admin.site.register(Speciality)
admin.site.register(Direction)
