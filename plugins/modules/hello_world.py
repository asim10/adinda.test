#######################################################################################################################
# File:             hello_world.py                                                                            #
# Author:           Anurag Jain, Developer Advocate                                                                   #
# Publisher:        Thales Group                                                                                      #
# Copyright:        (c) 2022 Thales Group. All rights reserved.                                                       #
#######################################################################################################################

# Create file as below
# anugram/ciphertrust/plugins/modules/hello_world.py

# import required Python libraries as well as required Ansible core modules

import os
import requests
import urllib3
import json
import ast
import re

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