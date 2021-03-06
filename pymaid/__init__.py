from __future__ import absolute_import
__all__ = [
    'ServiceAgent', 'Channel', 'Controller', 'Connection',
    'Error', 'Warning', 'logger', 'pool', 'profiler'
]

__version__ = '0.0.1'
VERSION = tuple(map(int, __version__.split('.')))

import gevent
from gevent import monkey
monkey.patch_all()

import sys
platform = sys.platform
if 'linux' in platform or 'darwin' in platform:
    import os
    if 'GEVENT_RESOLVER' not in os.environ:
        from gevent import resolver_ares
        hub = gevent.get_hub()
        hub.resolver = resolver_ares.Resolver()
        hub.resolver_class = resolver_ares.Resolver
    else:
        gevent_resolver = os.environ['GEVENT_RESOLVER']
        if 'ares' not in gevent_resolver:
            sys.stdout.write(
                'ares-resolver is better, just `export GEVENT_RESOLVER=ares`\n'
            )
    if 'cpp' != os.environ.get('PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'):
        sys.stdout.write(
            'C++ implementation protocol buffer has overall performance, see'
            '`https://github.com/google/protobuf/blob/master/python/README.txt#L84-L105`\n'
        )
    if '2' != os.environ.get('PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION_VERSION'):
        sys.stdout.write(
            'pb>=2.6 new C++ implementation also require to '
            '`export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION_VERSION=2`'
        )

from pymaid.agent import ServiceAgent
from pymaid.channel import Channel
from pymaid.controller import Controller
from pymaid.connection import Connection
from pymaid.error import Error, Warning
from pymaid.utils import logger, pool, profiler
