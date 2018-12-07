from django import template

register = template.Library()


@register.filter
def porcent(valor, total):
    return "{0:.2f}".format((valor*100)/total)
