{
  'targets' : [
    {
      'target_name' : 'odbc_bindings',
      'sources' : [ 
        'src/odbc.cpp',
        'src/odbc_connection.cpp',
        'src/odbc_statement.cpp',
        'src/odbc_result.cpp',
        'src/dynodbc.cpp'
      ],
      'cflags' : ['-Wall', '-Wextra', '-Wno-unused-parameter', '-Wno-deprecated-declarations', '-Wno-gnu-designator'],
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'defines' : [
        'UNICODE'
      ],
      'conditions' : [
        [ 'OS == "linux"', {
          'libraries' : [ 
            '-lodbc' 
          ],
          'cflags' : [
            '-g', '-Wno-deprecated-declarations', '-Wno-gnu-designator'
          ]
        }],
        [ 'OS == "mac"', {
          'include_dirs': [
            '/usr/local/include'
          ],
          'libraries' : [
            '-L/usr/local/lib',
            '-lodbc' 
          ],
          'cflags' : [
             '-g', '-Wno-deprecated-declarations', '-Wno-gnu-designator'
           ],
           'cflags_cc' : [
             '-g', '-Wno-deprecated-declarations', '-Wno-gnu-designator'
           ]
        }],
        [ 'OS=="win"', {
          'sources' : [
            'src/strptime.c',
            'src/odbc.cpp'
          ],
          'libraries' : [ 
            '-lodbccp32.lib' 
          ]
        }]
      ]
    }
  ]
}
