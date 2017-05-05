=====
Usage
=====

To use Django Rubricate in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'rubricate.apps.RubricateConfig',
        ...
    )

Add Django Rubricate's URL patterns:

.. code-block:: python

    from rubricate import urls as rubricate_urls


    urlpatterns = [
        ...
        url(r'^', include(rubricate_urls)),
        ...
    ]
