#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers
"""

from fabric.api import env, local, put, run
from os.path import exists
from datetime import datetime

# Servers
env.hosts = ['<IP web-01>', '<IP web-02>']

# Username
env.user = 'username'

def do_pack():
    """
    Compress files into .tgz archive
    """
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception as e:
        return None

def do_deploy(archive_path):
    """
    Distribute archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        filename = archive_path.split('/')[-1]
        path = '/data/web_static/releases/{}'.format(filename.split('.')[0])
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path))
        run("tar -xzf /tmp/{} -C {}/".format(filename, path))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}/".format(path, path))
        run("rm -rf {}/web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path))
        return True
    except Exception as e:
        return False

def deploy():
    """
    Create and distribute archive to web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)

