from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

@register.simple_tag
def nota_corte_curso(curso, perfil):
    nota = curso.calcula_nota_corte(perfil)
    return nota

@register.simple_tag
def sub(a, b):
    if (type(a) is float or type(a) is int) and (type(b) is float or type(b) is int):
        if a > 0 and b > 0:
            return a - b
        else:
            return 0.00
    else:
        return