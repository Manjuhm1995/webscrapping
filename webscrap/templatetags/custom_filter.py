from django import template

register = template.Library()

@register.filter
def zip_lists(dis_authors, dis_quotes):
    return zip(dis_authors, dis_quotes)
