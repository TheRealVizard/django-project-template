# Django Project Template

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![Django](https://img.shields.io/badge/django-3.2%7C4.0-blue)

This is a Django 3.2+/4.0+ project template with my preferred setup.

## Installation

Installing the template is easy, just run:

```bash
django-admin startproject <project_name> \
--template=https://github.com/TheRealVizard/django-project-template/archive/main.zip \
--extension py,cfg,yml,ini,toml,env,example,prod,conf,json \
--name Dockerfile
```

## Features

- Comes with Django 4.0.6 by default.
- More comfortable project structure.
- Uses [Poetry](https://python-poetry.org/) to manage the packages installation.
- Settings divided for develop and production.
- [pre-commit](https://pre-commit.com/) configured with many useful hooks.
- Docker file configured for production environment.
- Base custom HTML template with [Bootstrap 5](https://getbootstrap.com/), [Font Awesome 6](https://fontawesome.com/), [jQuery 3.6](https://jquery.com/) and [Select2](https://select2.org/)
- Base [TrackedModel](https://github.com/TheRealVizard/django-project-template/blob/9816a8a059f2fb7c793fb7e56701f0f9b87f27da/apps/core/models.py#L5) class to track model changes.
- Few third party packages really useful for develop and production.

1. [django-filter](https://django-filter.readthedocs.io/en/stable/) for the useful filtering features that provides.
2. [django-select2](https://django-select2.readthedocs.io/en/latest/) to simplify the selection to the end user interface. For this package I also include a custom CSS and JS to add the look and feel of Bootstrap 5 and the Spanish language to the UI. You can change these in the widget declaration as follows.
   ```python
   widget=ModelSelect2Widget(
    attrs={
        "data-theme": "bootstrap-5",
        "data-language": "es",
        "data-width": "style",
    },

   ```
3. [python-dotenv](https://github.com/theskumar/python-dotenv) to set and access environment variables  in your settings file.
4. [python-dateutil](https://dateutil.readthedocs.io/en/stable/) to handle date and time manipulations.
5. [django-version-checks](https://pypi.org/project/django-version-checks/) to ensure you and your team are using the correct Python and DB version.
6. [django-extensions](https://django-extensions.readthedocs.io/en/latest/) collection of custom extensions for the Django Framework.
7. [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) is a configurable set of panels that display various debug information about the current request/response.
8. [django-linear-migrations](https://pypi.org/project/django-linear-migrations/) so you and your team keep the migration history clean.
9. [factory-boy](https://factoryboy.readthedocs.io/en/stable/) super useful to handle Models instance creation for test mostly but also to have a dummy data for demos.
10. [pytest](https://docs.pytest.org/) to write all your test for the project. Comes with several plugins (pytest-cov, pytest-django,pytest-randomly, pytest-restrict, pytest-xdist, pytest-env)

## Deployment

For the deployment it uses [Gunicorn](https://gunicorn.org/), [Nginx](https://www.nginx.com/) to handle the server, by default uses [PostgreSQL](https://www.postgresql.org/) for the database. In the [Dockerfile](/Dockerfile) you will se this `--with production` in the poetry decencies installation, production is a custom group that you can use to manage the production dependencies. For the production environment the default .env file used is the .env.prod file.

## License

Copyright © Eduardo Leyva. Licensed under the [BSD 3-Clause License](/LICENSE).
