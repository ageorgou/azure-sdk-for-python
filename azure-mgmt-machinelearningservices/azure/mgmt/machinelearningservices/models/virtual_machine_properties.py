# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachineProperties(Model):
    """VirtualMachineProperties.

    :param virtual_machine_size: Virtual Machine size
    :type virtual_machine_size: str
    :param administrator_account: Admin credentials for virtual machine
    :type administrator_account:
     ~azure.mgmt.machinelearningservices.models.VirtualMachineSshCredentials
    """

    _attribute_map = {
        'virtual_machine_size': {'key': 'virtualMachineSize', 'type': 'str'},
        'administrator_account': {'key': 'administratorAccount', 'type': 'VirtualMachineSshCredentials'},
    }

    def __init__(self, **kwargs):
        super(VirtualMachineProperties, self).__init__(**kwargs)
        self.virtual_machine_size = kwargs.get('virtual_machine_size', None)
        self.administrator_account = kwargs.get('administrator_account', None)
