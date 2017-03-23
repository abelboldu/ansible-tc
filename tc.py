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

def add_control(data):

    device = data['device']

    # preliminar sample
    # tc = tcconfig.traffic_control.TrafficControl('eth1','outgoing','1M',shaping_algorithm='htb')

def del_control(data=None):


def main():
    module = AnsibleModule(
        argument_spec = dict(

        ),
        supports_check_mode = True,
        mutually_exclusive = []
    )



    choice_map = {
        "present": add_control,
        "absent": del_control,
    }

    changed = False
    res_args = dict()
    is_error, has_changed, result = choice_map.get(module.params['state'])(module.params)


if __name__ == "__main__":
    main()
