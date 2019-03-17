# default definitions
pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'gamjectfolder')
gnome = import('gnome')

# installing resources
gnome.compile_resources('gamjectfolder',
  'gamjectfolder.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python3 = import('python3')

# python configuration
conf = configuration_data()
conf.set('PYTHON', python3.find_python().path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)


configure_file(
  input: 'gamjectfolder.in',
  output: 'gamjectfolder',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

# python code project files
gamjectfolder_sources = [
  '__init__.py',
  'main.py',
  'makefolders.py',
  'makereadme.py',
  'makedbplan.py'
]

install_data(gamjectfolder_sources, install_dir: moduledir)