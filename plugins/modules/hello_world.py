#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2022 Thales Group. All rights reserved.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: hello_world
short_description: Test Hello World module.
description:
  - Prints firstname, lastname, age, and profession in JSON format.
author:
  - Asim Dinda (@asim10)
version_added: "1.0.0"
options:
  firstname:
    description: The first name of the user.
    type: str
    required: true
  lastname:
    description: The last name of the user.
    type: str
    required: true
  age:
    description: The age of the user.
    type: int
    required: true
  profession:
    description: The profession of the user.
    type: str
    required: true
'''

EXAMPLES = r'''
- name: Test hello_world module with valid data
  adinda.test.hello_world:
    firstname: "Adinda"
    lastname: "Test"
    age: 25
    profession: "Engineer"
  register: result

- debug:
    var: result.user_data
'''

RETURN = r'''
user_data:
    description: The dictionary containing user info.
    returned: always
    type: dict
    sample:
        firstname: "Adinda"
        lastname: "Test"
        age: 25
        profession: "Engineer"
'''

# import required Python libraries as well as required Ansible core modules

# import os
# import requests
# import urllib3
# import json
# import ast
# import re

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(
            firstname=dict(type='str', required=True),
            lastname=dict(type='str', required=True),
            age=dict(type='int', required=True),
            profession=dict(type='str', required=True),
        ),
    )
    # Extracting parameters passed from the playbook
    firstname = module.params.get('firstname')
    lastname = module.params.get('lastname')
    age = module.params.get('age')
    profession = module.params.get('profession')

    # 3. Create the nested JSON structure
    user_info = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age,
        "profession": profession
    }

    result = dict(
        changed=False,
        user_data=user_info
    )

    # Return the encrypted data as result
    module.exit_json(**result)


if __name__ == '__main__':
    main()
