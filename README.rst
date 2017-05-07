.. image:: https://travis-ci.org/xcono/django-rubricate.svg?branch=master
    :target: https://travis-ci.org/xcono/django-rubricate

=============================
Django Rubricate
=============================

Clean way to build content via custom blocks.

Documentation
-------------

The full documentation is at https://django-rubricate.readthedocs.io.

Quickstart
----------

Install Django Rubricate::

    pip install django-rubricate

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'rubricate',
        ...
    )

Configure your `MEDIA_ROOT` and `MEDIA_URL`:

.. code-block:: python

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

Add Django Rubricate's URL patterns:

.. code-block:: python

    from rubricate import urls as rubricate_urls


    urlpatterns = [
        ...
        url(r'^', include(rubricate_urls)),
        ...
    ]

    # you also may want to add MEDIA_URL
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
