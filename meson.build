project(
	'gamjectfolder',
	version: '0.2.0',
  	meson_version: '>= 0.40.0',
)

application_id = 'org.gnome.Gamjectfolder'

i18n = import('i18n')


subdir('data')
subdir('src')
subdir('po')

meson.add_install_script('build-aux/meson/postinstall.py')