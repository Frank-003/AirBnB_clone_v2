#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives
"""

from fabric.api import env, local, run
from datetime import datetime
from os.path import exists
import os

# Servers
env.hosts = ['<IP web-01>', '<IP web-02>']

# Username
env.user = 'username'

def do_clean(number=0):
    """
    Delete out-of-date archives
    """
    try:
        number = int(number)
        if number < 1:
            number = 1

        # Clean local archives
        local_archives = sorted(local("ls -t versions", capture=True).split())
        if len(local_archives) > number:
            archives_to_delete = local_archives[number:]
            for archive in archives_to_delete:
                local("rm versions/{}".format(archive))

        # Clean remote archives
        remote_archives = sorted(run("ls -t /data/web_static/releases").split())
        if len(remote_archives) > number:
            archives_to_delete = remote_archives[number:]
            for archive in archives_to_delete:
                if archive != "test":
                    run("rm -rf /data/web_static/releases/{}".format(archive))

        return True
    except Exception as e:
        return False

