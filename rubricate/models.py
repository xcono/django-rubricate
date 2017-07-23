from django.db import models


class RubricatePermissionsSupport(models.Model):

    class Meta:

        managed = False  # No database table creation or deletion operations \
                         # will be performed for this model.

        permissions = (
            ('upload_files', 'Allowed to upload files attached to rubrics'),
        )
