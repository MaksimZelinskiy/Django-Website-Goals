from django.contrib import admin

from .models import Goals, Routine, Notes, Theme_goal, Category_notes, Category_routine

class GoalsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_goal', 'created_at_goal','theme_goal')
    list_display_links=('id', 'title_goal')
    search_fields = ('title', 'content_goal','theme_goal')

class Theme_goalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_theme_goal')
    list_display_links=('id', 'title_theme_goal')



class NotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_notes', 'created_at_notes','category_notes')
    list_display_links=('id', 'content_notes')

class Category_notesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_category_notes')
    list_display_links=('id', 'title_category_notes')



class RoutineAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_routine', 'created_at_routine','category_routine')
    list_display_links=('id', 'title_routine')
    search_fields = ('title_routine', 'text_routine','category_routine')

class Category_routineAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_category_routine')
    list_display_links=('id', 'title_category_routine')

admin.site.register(Goals, GoalsAdmin)
admin.site.register(Theme_goal, Theme_goalAdmin)

admin.site.register(Routine, RoutineAdmin)
admin.site.register(Category_routine, Category_routineAdmin)

admin.site.register(Notes, NotesAdmin)
admin.site.register(Category_notes, Category_notesAdmin)
