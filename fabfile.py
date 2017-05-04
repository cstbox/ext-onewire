# -*- coding: utf-8 -*-

from cstbox_devtools.fabtasks import *

__author__ = 'Eric Pascual - CSTB (eric.pascual@cstb.fr)'

REPOS_PATH.update({
    'dropbox': os.path.expanduser("~/Dropbox-private/Dropbox/cstbox/"),
    'ppa': os.path.expanduser("~/cstbox-workspace/ppa/public"),
})


@task(alias='ppa')
def update_ppa():
    do_update_ppa(ppa_name='public', ppa_servers=['public', 'private'])
