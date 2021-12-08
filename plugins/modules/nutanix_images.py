#!/usr/bin/python

# Copyright: (c) 2021
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: nutanix_images

short_description: This module allows to communicate with the resource /images

version_added: "1.0.0"

description: This module allows to perform the following tasks on /images

options:
    action:
        description: This is the action used to indicate the type of request
        required: true
        type: str
    credentials:
        description: Credentials needed for authenticating to the subnet
        required: true
        type: dict (Variable from file)
    data:
        description: This acts as either the params or the body payload depending on the HTTP action
        required: false
        type: dict
    operation:
        description: This acts as the sub_url in the requested url
        required: false
        type: str
    ip_address:
        description: This acts as the ip_address of the subnet. It can be passed as a list in ansible using with_items
        required: True
        type: str (Variable from file)
    port:
        description: This acts as the port of the subnet. It can be passed as a list in ansible using with_items
        required: True
        type: str (Variable from file)

author:
 - Gevorg Khachatryan (@gevorg_khachatryan)
'''

EXAMPLES = r'''

#CREATE action, request to /images
- hosts: [hosts_group]
  tasks:
  - name: create Image
    nutanix_images:
      action: create
      credentials: str (Variable from file)
      ip_address: str (Variable from file)
      port: str (Variable from file)
      data:
        spec:
         name: string
         resources:
           image_type: string
           source_uri: string

#UPDATE action, request to /images/{uuid}
- hosts: [hosts_group]
  tasks:
  - name: update Image
    nutanix_images:
      action: update
      credentials: str (Variable from file)
      ip_address: str (Variable from file)
      port: str (Variable from file)
      data:
        metadata:
          uuid: string
        spec:
          name: string
          resources:
            image_type: string
            source_uri: string

#LIST action, request to /images/list
- hosts: [hosts_group]
  tasks:
  - name: List Images
    nutanix_images:
      action: list
      credentials: str (Variable from file)
      ip_address: str (Variable from file)
      port: str (Variable from file)
      data:
      - kind: string
      - sort_attribute: string
      - filter: string
      - length: integer
      - sort_order: string
      - offset: integer

#DELETE action, request to /images/{uuid}
- hosts: [hosts_group]
  tasks:
  - name: delete Image
    nutanix_images:
      action: delete
      credentials: str (Variable from file)
      ip_address: str (Variable from file)
      port: str (Variable from file)
      data:
        metadata:
          uuid: string
'''

RETURN = r'''

# CREATE /images
responses:
- default: Internal Error
- 202: Request Accepted

# UPDATE /images/{uuid}
responses:
- default: Internal Error
- 404: Invalid UUID provided
- 202: Request Accepted

# LIST /images/list
responses:
- default: Internal Error
- 200: Success

# DELETE /images/{uuid}
responses:
- default: Internal Error
- 404: Invalid UUID provided
- 202: Request Accepted
'''

from plugins.module_utils.entity import BaseModule

from plugins.module_utils.prism.images import Image


def run_module():
    module = BaseModule()
    module_builder = Image(module)
    module_builder.run_module(module)


def main():
    run_module()


if __name__ == '__main__':
    main()
