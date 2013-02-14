#!/usr/bin/python
# -*- coding: utf-8 -*-

# Authenticate against redmine server
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from redmine import Redmine

import json
import os

# set the redmine url here
REDMINE_URL="https://example.com/redmine"

# Name of the group to allow Jenkins access
JENKINS_ACCESS="jenkins_users"

if __name__=="__main__":
  if 'REDMINE_URL' in os.environ:
    REDMINE_URL=os.environ['REDMINE_URL']

  username = os.environ['U']
  password = os.environ['P']

  instance = Redmine(REDMINE_URL, username=username, password=password)
  
  # This will fail if the authentication failed
  details = json.loads(instance.get("users/current.json?include=groups"))
  
  # Do the actual authorization logic
  for group in details['user']['groups']:
    if group['name'] == JENKINS_ACCESS:
      print("Authorization successful")
      exit(0)

  exit(1)
