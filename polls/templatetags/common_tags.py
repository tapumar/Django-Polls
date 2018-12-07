from django import template

register = template.Library()


@register.filter
def porcent(valor, total):
    if total != 0:
        return "{0:.2f}".format((valor*100)/total)
    else:
        return 0
