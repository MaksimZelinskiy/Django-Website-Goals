from django import template

from development.models import Theme_goal, Category_notes, Category_routine
register = template.Library()


@register.inclusion_tag('development/goals/list_theme_goals.html')
def show_theme_goals ():
    theme = Theme_goal.objects.all()
    return { 
        "theme": theme,
    }


@register.inclusion_tag('development/notes/list_category_notes.html')
def show_category_notes ():
    category = Category_notes.objects.all()
    return { 
        "category": category,
    }

@register.inclusion_tag('development/routine/list_category_routine.html')
def show_category_routine ():
    category = Category_routine.objects.all()
    return { 
        "category": category,
    }