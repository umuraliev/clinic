from django.contrib import admin
from .models import Doctor, Speciality, Direction, Review

# class SpecialityAdmin(admin.ModelAdmin):
#     list_display = ('title','slug', 'direction')
#     list_display_links = ('title', 'direction')
#     prepopulated_fields = {'slug': ('title', )}


admin.site.register(Speciality)
admin.site.register(Direction)

class ReviewInlineAdmin(admin.TabularInline):
    model = Review
    fields = ('body', 'author')
    max_num = 10

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    inlines = [ ReviewInlineAdmin, ]