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

""" 1-Wire devices helpers.
"""

import subprocess
import ow
import sys

# Pass-through to original functions and definitions, so that we can use our
# module as a drop-in replacement of original one
_current_module = sys.modules[__name__]
for attr in [
    ow.finish,
    ow.Sensor,
    ow.exError,
    ow.exErrorValue,
    ow.exNoController,
    ow.exNotInitialized,
    ow.exUnknownSensor]:
    setattr(_current_module, attr.__name__, attr)


def init():
    """ Wrapper of ow library init() function, hard linked to owserver."""
    # check if owserver is currently running
    try:
        subprocess.check_output(['pgrep', 'owserver'])
        ow.init('localhost:4304')
    except subprocess.CalledProcessError:
        raise ow.exError('owserver not running')

