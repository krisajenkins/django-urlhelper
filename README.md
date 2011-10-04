Django-URLHelper
====

A simple manage.py command to make it easy to query Django's URL dispatcher.

Figuring out the correct name for a given URL - for use in a `{% url ... %}` tag,
for instance - can be a bit of a pain. You can always run:

	./manage.py shell
	> from django.core.urlresolvers import resolve
	> resolve( '/some/where' )

...but that's fairly long-winded. This simple project installs a Django command
to make it as easy as:

	./manage.py resolveurl /some/where

Installation
----

	cd my-django-app
	git submodule add git://github.com/krisajenkins/django-urlhelper.git

Then edit settings.py and add 'django-urlhelper' to your INSTALLED_APPS.
