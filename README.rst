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

Add Django Rubricate's URL patterns:

.. code-block:: python

    from rubricate import urls as rubricate_urls


    urlpatterns = [
        ...
        url(r'^', include(rubricate_urls)),
        ...
    ]

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
