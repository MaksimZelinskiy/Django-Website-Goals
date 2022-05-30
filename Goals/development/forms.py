from django import forms
from .models import Goals, Routine, Theme_goal, Notes
import re
from django.core.exceptions import ValidationError


class GoalsForm(forms. ModelForm):
    class Meta:
        model = Goals
        fields = ['title_goal', 'content_goal', 'theme_goal']
        widgets = {
            'title_goal': forms.TextInput(attrs={'class': 'form-control', "placeholder":"Начать изучать JavaScript"}),
            'content_goal': forms.Textarea(attrs={'class': 'form-control' ,'rows': 3 , "placeholder":"Найти курсы по этому направлению. Найти ментора. Найти специальные книги"}),
            'theme_goal': forms.Select(attrs={"class": "form-select"})
        }
    
    def clean_title(self):
        title_goal=self.cleaned_data['title_goal']
        if re.match(r'\d', title_goal):
            raise ValidationError("Название не должно начинатся с цыфры")
        return title_goal

class ThemeGoalForm(forms.ModelForm):
    class Meta:
        model = Theme_goal
        fields = ['title_theme_goal']
        widgets = {
            'title_theme_goal': forms.TextInput(attrs={'class': 'form-control', "placeholder":"Карьера"}),
        }
    
    def clean_title(self):
        title_theme_goal=self.cleaned_data['title_theme_goal']
        if re.match(r'\d', title_theme_goal):
            raise ValidationError("Название не должно начинатся с цыфры")
        return title_theme_goal


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title_notes', 'content_notes', 'category_notes']
        widgets = {
            'title_notes': forms.TextInput(attrs={'class': 'form-control', "placeholder":"Не забыть позвонить шефу"}),
            'content_notes': forms.Textarea(attrs={'class': 'form-control' ,'rows': 5 , "placeholder":"Набрать по-поводу повышения"}),
            'category_notes': forms.Select(attrs={"class": "form-select"})
        }
    
    def clean_title(self):
        title_notes=self.cleaned_data['title_notes']
        if re.match(r'\d', title_notes):
            raise ValidationError("Название не должно начинатся с цыфры")
        return title_notes



class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['title_routine', 'text_routine', 'with_routine','before_routine' ,'category_routine']
        widgets = {
            'title_routine': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Подъем"}),
            'text_routine': forms.Textarea(attrs={'class': 'form-control' ,'rows': 5, "placeholder":"Проснутся, почистить зубы, принять ванную"}),
            'with_routine': forms.TimeInput(format='%H:%M', attrs={"class": "form-control", "placeholder":"9:00",}),
            'before_routine': forms.TimeInput(format='%H:%M', attrs={"class": "form-control", "placeholder":"9:30",}),
            'category_routine': forms.Select(attrs={"class": "form-select"})
        }
    
    def clean_title(self):
        title_routine=self.cleaned_data['title_routine']
        if re.match(r'\d', title_routine):
            raise ValidationError("Название не должно начинатся с цыфры")
        return title_routine





