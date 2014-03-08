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

""" HAL interface classes for 1-Wire supported products.

Since hw device interface is very simple, and since the 1-Wire world is quite
small and not evolving, unlike for other device families all the parts of the
implementation (ie HAL layer and concrete HW classes) are packaged in this
single module.
"""

import logging
from collections import namedtuple

import pycstbox.hal.device as haldev
import pycstbox.onewire as ow
from pycstbox.hal import hal_device, HalError

_logger = logging.getLogger('onewire')

DEFAULT_PRECISION = 3


@hal_device(device_type="ds1820", coordinator_type="onewire")
class DS1820(haldev.PolledDevice):
    """ HAL device modeling the DS1820 temperature sensor.

    The extension adds the support of polling requests and CSTBox events
    publishing on D-Bus.
    """
    DEVICE_TYPE = 'ds1820'

    class HWDevice(object):
        OutputValues = namedtuple('OutputValues', [
            'temp'          # temperature
        ])

        def __init__(self, addr):
            # beware to cast to str, since C lib does not like unicode at all
            self._sensor = ow.Sensor(str('/' + addr))

        def poll(self):
            value = float(self._sensor.temperature)
            return self.OutputValues(value)

    def __init__(self, coord, cfg):
        super(DS1820, self).__init__(coord, cfg)
        try:
            self._hwdev = self.HWDevice(cfg.address)
        except ow.exUnknownSensor:
            raise HalError('unknown sensor : %s' % cfg.address)