from django import template


register = template.Library()


def get_categories():
    return Category.objects.all()
