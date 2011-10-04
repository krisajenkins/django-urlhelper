Django-URLHelper
====

A simple manage.py command to make it easy to query Django's URL dispatcher.

Figuring out the correct name for a given URL - for use in a `{% url ... %}` tag,
for instance - in Django can be a bit of a pain. You can always run:

	./manage.py shell
	> from django.core.urlresolvers import resolve
	> resolve( '/some/where' )

This repo installs a Django command to make it as easy as:

	./manage.py resolveurl /some/where
