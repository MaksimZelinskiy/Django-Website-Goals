from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Goals, Notes, Routine, Theme_goal, Category_notes, Category_routine
from .models import Goals as GoalsModel
from .models import Notes as NotesModel
from .models import Routine as RoutineModel
from .forms import GoalsForm, NotesForm, RoutineForm, ThemeGoalForm
from django.urls import reverse, reverse_lazy


# *****************
# ***** GOALS *****
# *****************

class Goals (ListView):
    model = Goals
    template_name= 'development/goals/goals.html'
    context_object_name= 'goals'

class Themegoals(ListView):
    model = Goals
    template_name= 'development/goals/goals.html'
    context_object_name= 'goals'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_theme_goal"] =  'Категория'
        return context

    def get_queryset(self):
        return GoalsModel.objects.filter(theme_goal_id=self.kwargs['theme_goal_id'])

class CreateGoal(CreateView):
    form_class = GoalsForm
    template_name = 'development/goals/add_goals.html'
    success_url= reverse_lazy('goals')

class DeleteGoal(DeleteView):
    model = GoalsModel
    template_name = 'development/delete_dev.html'
    success_url= reverse_lazy('goals')

class EditGoal(UpdateView):
    model = GoalsModel
    form_class = GoalsForm
    template_name = 'development/edit_dev.html'
    # fields = ['title_goal', 'content_goal', 'theme_goal']
    
class CreateThemeGoal(CreateView):
    form_class = ThemeGoalForm
    template_name = 'development/goals/add_theme_goal.html'
    success_url= reverse_lazy('goals')


# *****************
# ***** Notes *****
# *****************

class Notes(ListView):
    model= Notes
    template_name= 'development/notes/notes.html'
    context_object_name='notes'

class Category_notes(ListView):
    model= Notes
    template_name= 'development/notes/notes.html'
    context_object_name= 'notes'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_category_notes"] =  'Категория'
        return context

    def get_queryset(self):
        return NotesModel.objects.filter(category_notes_id=self.kwargs['category_notes_id'])


class CreateNote(CreateView):
    form_class = NotesForm
    template_name = 'development/notes/add_notes.html'
    success_url= reverse_lazy('notes')

class DeleteNotes(DeleteView):
    model = NotesModel
    template_name = 'development/delete_dev.html'
    success_url= reverse_lazy('notes')

class EditNotes(UpdateView):
    model = NotesModel
    form_class = NotesForm
    template_name = 'development/edit_dev.html'

# *****************
# **** Routine ****
# *****************

class Routine(ListView):
    model= Routine
    template_name= 'development/routine/routine.html'
    context_object_name='routine'

class Category_routine(ListView):
    model= Routine
    template_name= 'development/routine/routine.html'
    context_object_name= 'routine'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_category_routine"] =  'Категория'
        return context

    def get_queryset(self):
        return RoutineModel.objects.filter(category_routine_id=self.kwargs['category_routine_id'])

class CreateRoutine(CreateView):
    form_class = RoutineForm
    template_name = 'development/routine/add_routine.html'
    success_url= reverse_lazy('routine')

class DeleteRoutine(DeleteView):
    model = RoutineModel
    template_name = 'development/delete_dev.html'
    success_url= reverse_lazy('routine')

class EditRoutine(UpdateView):
    model = RoutineModel
    form_class = RoutineForm
    template_name = 'development/edit_dev.html'


# *****************
# ** Development **
# *****************

def Development(request):
    context={}
    return render(request, 'development/development.html', context)
