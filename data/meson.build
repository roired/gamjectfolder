# installing the icons
icon_dir = join_paths('icons', 'hicolor', 'scalable', 'apps')
install_data(
	join_paths(icon_dir, 'org.gnome.Gamjectfolder.svg'),
	install_dir: join_paths(get_option('datadir'), icon_dir)
	)

# installing the desktop file
desktop_file = i18n.merge_file(
  input: 'org.gnome.Gamjectfolder.desktop.in',
  output: 'org.gnome.Gamjectfolder.desktop',
  type: 'desktop',
  po_dir: '../po',
  install: true,
  install_dir: join_paths(get_option('datadir'), 'applications')
)

# validate the desktop file
desktop_utils = find_program('desktop-file-validate', required: false)
if desktop_utils.found()
  test('Validate desktop file', desktop_utils,
    args: [desktop_file]
  )
endif

# installing the appstream file
appstream_file = i18n.merge_file(
  input: 'org.gnome.Gamjectfolder.appdata.xml.in',
  output: 'org.gnome.Gamjectfolder.appdata.xml',
  po_dir: '../po',
  install: true,
  install_dir: join_paths(get_option('datadir'), 'appdata')
)

# validate the appstream file
appstream_util = find_program('appstream-util', required: false)
if appstream_util.found()
  test('Validate appstream file', appstream_util,
    args: ['validate', appstream_file]
  )
endif

# installing the schema file
install_data('org.gnome.Gamjectfolder.gschema.xml',
  install_dir: join_paths(get_option('datadir'), 'glib-2.0/schemas')
)

# validate the schema file
compile_schemas = find_program('glib-compile-schemas', required: false)
if compile_schemas.found()
  test('Validate schema file', compile_schemas,
    args: ['--strict', '--dry-run', meson.current_source_dir()]
  )
endif