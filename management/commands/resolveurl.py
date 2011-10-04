from django.core.management.base		import BaseCommand
from django.core.urlresolvers			import resolve, Resolver404

class Command( BaseCommand ):
	args = '<url url ...>'
	help = 'URL-name lookup function. The Django-resolved name (plus some other details) will be printed for each URL supplied.'

	def handle( self, *args, **options ):
		for url in args:
			try:
				resolved = resolve( url )
				print( "%s => %s" % ( url, resolved.url_name ) )
				print( "\t%s" % resolved )
			except Resolver404:
				print( "%s => Not Found" % url )

			print
