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

""" 1-Wire hardware abstraction layer.  """

import sys
import logging
import serial
import os.path

import pycstbox.log as log
import pycstbox.cli as cli
import pycstbox.dbuslib as dbuslib
import pycstbox.onewire as ow
from pycstbox.onewiresvc import OneWireSvc
import pycstbox.devcfg as devcfg

if __name__ == '__main__':
    log.setup_logging(os.path.basename(__file__))

    parser = cli.get_argument_parser('CSTBox 1-Wire HAL')
    args = parser.parse_args()

    try:
        ow.init()
    except ow.exError as e:
        logging.critical('Fatal error: %s', str(e))
        sys.exit(1)

    try:
        dbuslib.dbus_init()

        cfg = devcfg.DeviceNetworkConfiguration(autoload=True)
        svc = OneWireSvc(dbuslib.get_bus())

        svc.log_setLevel_from_args(args)
        # load the configuration data for 1-Wire coordinators
        svc.load_configuration(
            dict([(k, v) for k, v in cfg.iteritems() if v.type == 'onewire'])
        )
        svc.start()

    except serial.SerialException as e:
        logging.critical(e)
        sys.exit(1)

    except Exception as e: #pylint: disable=W0703
        logging.exception(e)
        sys.exit(e)

    finally:
        ow.finish()

