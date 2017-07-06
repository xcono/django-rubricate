from django.template.defaulttags import register


@register.filter
def rubric_css(dictionary):
    return dictionary.get('type', '').replace('_', '-')
