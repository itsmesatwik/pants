# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
  name = 'executor',
  sources = ['executor.py'],
  dependencies = [
    '3rdparty/python/twitter/commons:twitter.common.collections',
    'src/python/pants/base:build_environment',
    'src/python/pants/util:contextutil',
    'src/python/pants/util:dirutil',
  ]
)

python_library(
  name = 'nailgun_client',
  sources = ['nailgun_client.py'],
  dependencies = [
    '3rdparty/python:psutil',
    ':nailgun_io',
    ':nailgun_protocol',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:osutil',
    'src/python/pants/util:socket',
    'src/python/pants/util:strutil',
  ]
)

python_library(
  name = 'nailgun_io',
  sources = ['nailgun_io.py'],
  dependencies = [
    '3rdparty/python:contextlib2',
    ':nailgun_protocol'
  ]
)

python_library(
  name = 'nailgun_protocol',
  sources = ['nailgun_protocol.py'],
  dependencies = [
    'src/python/pants/util:objects',
    'src/python/pants/util:osutil',
  ]
)

python_library(
  name = 'nailgun_executor',
  sources = ['nailgun_executor.py'],
  dependencies = [
    ':executor',
    ':nailgun_client',
    '3rdparty/python/twitter/commons:twitter.common.collections',
    'src/python/pants/base:build_environment',
    'src/python/pants/pantsd:process_manager',
    'src/python/pants/util:dirutil',
  ],
)

python_library(
  name = 'util',
  sources = ['util.py'],
  dependencies = [
    ':executor',
    ':nailgun_executor',
    'src/python/pants/base:workunit',
    'src/python/pants/java/jar',
    'src/python/pants/util:contextutil',
    'src/python/pants/util:process_handler',
  ],
)
