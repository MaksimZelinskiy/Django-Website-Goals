from django.urls import path

from .views import *

urlpatterns = [
    path('',  Development, name='development'),

    path('goals', Goals.as_view(), name='goals'),
    path('goals/theme/<int:theme_goal_id>', Themegoals.as_view(), name='theme_goal'),
    path('goals/create/goal/', CreateGoal.as_view(), name='add_goals'),
    path('goals/delete/<int:pk>', DeleteGoal.as_view(), name='deletegoals'),
    path('goals/create/theme/', CreateThemeGoal.as_view(), name='add_theme_goal'),
    path('goals/edit/<int:pk>', EditGoal.as_view(), name='edit_goal'),

    path('routine', Routine.as_view(), name='routine'),
    path('routine_category/<int:category_routine_id>', Category_routine.as_view(), name='category_routine'),
    path('routine/create', CreateRoutine.as_view(), name='add_routine'),
    path('routine/delete/<int:pk>', DeleteRoutine.as_view(), name='deleteroutine'),
    path('routine/edit/<int:pk>', EditRoutine.as_view(), name='edit_routine'),

    path('notes', Notes.as_view(), name='notes'),
    path('notes_category/<int:category_notes_id>', Category_notes.as_view(), name='category_notes'),
    path('notes/create/', CreateNote.as_view(), name='add_notes'),
    path('notes/delete/<int:pk>', DeleteNotes.as_view(), name='deletenotes'),
    path('notes/edit/<int:pk>', EditNotes.as_view(), name='edit_notes'),

]

