#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CSTBox.
#
# CSTBox is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CSTBox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with CSTBox.  If not, see <http://www.gnu.org/licenses/>.

""" System wide configuration and tools weblet """

__author__ = 'Eric PASCUAL - CSTB (eric.pascual@cstb.fr)'
__copyright__ = 'Copyright (c) 2013 CSTB'
__vcs_id__ = '$Id$'
__version__ = '1.0.0'

# allows catching Exception instances
#pylint: disable=W0703

from collections import namedtuple

import pycstbox.log as log
import pycstbox.webui as webui
import pycstbox.onewire as ow

_logger = None
ow.init()


class DisplayHandler(webui.WebletUIRequestHandler):
    """ UI display request handler """
    def get(self):
        self.render(
            "onewire.html"
        )
        if self.application.settings['debug']:
            _logger.setLevel(log.DEBUG)


class GetDevicesList(webui.WSHandler):
    def do_get(self):
        devices = [(dev.address, dev.type) for dev in ow.Sensor('/').sensors()]
        reply = { 'devices' : devices }
        self.finish(reply)


_logger = log.getLogger('wblt-systools')
handlers = [
    (r"/ls", GetDevicesList, dict(logger=_logger)),

    (r"[/]?", DisplayHandler)
]


