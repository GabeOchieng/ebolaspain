from fabric.api import *

from local_fabfile import local_vars
import os

#################################################################################
env.remotedir = '/home/ebola/repo/ebolaspain/src/'
env.remote_activate = 'source /home/ebola/envs/ebolaspain/bin/activate'
env.remotename = 'origin'
env.hosts = ['ebola@107.170.86.54:22']

#Import for custom developer's settings
local_vars(env)

#################################################################################

def local_virtualenv(command):
    with prefix(env.local_activate):
        local(command)

def virtualenv(command):
    with prefix(env.remote_activate):
        run(command)

@task(alias='pp')
def pushpull(branch='next'):
    #Local commands
    with lcd(env.localfolder):
        #local('git commit -am \"test\"')
        local('git push %s %s'% (env.remotename,branch))
    #Remote commands
    with cd(env.remotedir):
        #update git repository
        run('git checkout %s' % (branch))
        run('git pull %s %s' % (env.remotename,branch))

def install_requirements():
    with cd(env.remotedir):
        virtualenv('pip install -r %srequirements.txt' % (env.remotedir))

@task(alias='dp', default=True)
def deploy(branch='next'):
    #local push, remote pull at the appropriate branch
    pushpull(branch)

@task(alias='gf')
def getFile(remote, local):
    get(remote,local)

@task(alias='put')
def putFile(local, remote):
    put(local,remote)