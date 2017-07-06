from django.template.defaulttags import register


@register.filter
def rubric_css(rubric_type):
    return rubric_type.replace('_', '-')
