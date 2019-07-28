from django.contrib import admin

from .models import QuizForEY, QuizForSY, Bundle

# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'birthday')
#     list_display_links = ('id', 'first_name')

# class StoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'teller', 'is_published')
#     list_display_links = ('id', 'title')
#     list_editable = ('is_published', )
#     list_filter = ('teller',)
#     search_fields = ('title', 'teller', 'description')
#     list_per_page = 30

admin.site.register(QuizForEY)
admin.site.register(QuizForSY)
admin.site.register(Bundle)
# admin.site.register(Story, StoryAdmin)
