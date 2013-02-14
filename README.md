authredmine
===========

A small python script to authenticate against redmine

Usage
-----

This script is intended to be used by jenkins script-based authentication module (https://wiki.jenkins-ci.org/display/JENKINS/Script+Security+Realm)

### Install

This script requires pyredmine: http://pypi.python.org/pypi/pyredmine

### Test

Simply set the environment variables U (username) P (password) and REDMINE_URL (well, the redmine url) accordingly and run the script. If everything works, you will get a success notification.

