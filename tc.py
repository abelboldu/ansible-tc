#!/usr/bin/python
# -*- coding: utf-8 -*-

# 2017, Abel Boldú <abel.boldu () gmx.com>

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'version': '0.1'}

DOCUMENTATION = '''
---
module: uri
short_description: Network traffic control
description:
  - Module to control bandwidth/latency/packet-loss to a network interface.
options:
  device:

  delay:

  loss:

  rate:

  delay-distro:

  direction:
    required: false
    default: outgoing
    choices: ["outgoing", "incoming"]

  corrupt:

  port:

  network:

  shaping-algo:

author: "Abel Boldú <abel.boldu () gmx.com>"
'''

EXAMPLES = '''

- tc:
    device: eth1
    rate: 1M
  delegate_to: localhost
'''

from ansible.module_utils.basic import AnsibleModule

HAS_PYTHON_TCCONFIG = True
try:
    import tcconfig
    import tcconfig.traffic_control
except ImportError:
    HAS_PYTHON_TCCONFIG = False

def add_control():


def main():
    module = AnsibleModule(
        argument_spec = dict(

        ),
        supports_check_mode = True,
        mutually_exclusive = []
    )

    device = module.params['device']

    # Do stuff

    changed = False
    res_args = dict()


if __name__ == "__main__":
    main()
