#!/usr/bin/env python

import os

from fabric.api import execute, local, prompt, task

def bootstrap(github_username='chagan', repository_name=None):
    """
    Execute the bootstrap tasks for a new project.
    """

    config = {}
    config['$NEW_PROJECT_SLUG'] = os.getcwd().split('/')[-1]
    config['$NEW_REPOSITORY_NAME'] = repository_name or config['$NEW_PROJECT_SLUG']
    config['$NEW_PROJECT_FILENAME'] = config['$NEW_PROJECT_SLUG'].replace('-', '_')

    confirm("Have you created a Github repository named \"%s\"?" % config['$NEW_REPOSITORY_NAME'])

    local('rm -rf .git')
    local('git init')
    local('rm *.pyc')
    local('git add .')
    local('git commit -am "Initial commit."')
    local('git remote add origin git@github.com:%s/%s.git' % (github_username, config['$NEW_REPOSITORY_NAME']))
    local('git push -u origin master')

def confirm(message):
    """
    Verify a users intentions.
    """
    answer = prompt(message, default="Not at all")

    if answer.lower() not in ('y', 'yes', 'buzz off', 'screw you'):
        exit()