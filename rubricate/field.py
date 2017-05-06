import json
from django.db.models import Field
from django.forms import HiddenInput
from jsonfield.fields import JSONField
from rubricate.uploads import uploads_process


class RubricateWidget(HiddenInput):

    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/dropzone/4.3.0/min/dropzone.min.css',
                'rubricate/rubricate.css',
                'rubricate/rubricate.plugins.css',
                'rubricate/rubricate.draggable.css',
            )
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/dropzone/4.3.0/min/dropzone.min.js',
            'rubricate/rubricate.draggable.js',
            'rubricate/rubricate.plugins.js',
            'rubricate/rubricate.js',
            'rubricate/rubricate.django.js'
        )

    def render(self, name, value, attrs=None):
        attrs.update({'class': 'rubricate-input'})
        return super().render(name, value, attrs)


class RubricateField(JSONField):

    def save_form_data(self, instance, data):

        json_string = json.loads(data)
        json_string = uploads_process(json_string)
        data = json.dumps(json_string, self.dump_kwargs)
        super().save_form_data(instance, data)

    def __init__(self, *args, **kwargs):
        kwargs['default'] = '{}'
        super(RubricateField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):

        defaults = {'max_length': self.max_length, 'widget': RubricateWidget}
        kwargs.update(defaults)
        return Field.formfield(self, **kwargs)
