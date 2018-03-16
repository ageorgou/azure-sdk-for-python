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


class ContainerServiceMasterProfile(Model):
    """Profile for the container service master.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param count: Number of masters (VMs) in the container service cluster.
     Allowed values are 1, 3, and 5. The default value is 1. Default value: 1 .
    :type count: int
    :param dns_prefix: Required. DNS prefix to be used to create the FQDN for
     the master pool.
    :type dns_prefix: str
    :param vm_size: Required. Size of agent VMs. Possible values include:
     'Standard_A0', 'Standard_A1', 'Standard_A10', 'Standard_A11',
     'Standard_A1_v2', 'Standard_A2', 'Standard_A2_v2', 'Standard_A2m_v2',
     'Standard_A3', 'Standard_A4', 'Standard_A4_v2', 'Standard_A4m_v2',
     'Standard_A5', 'Standard_A6', 'Standard_A7', 'Standard_A8',
     'Standard_A8_v2', 'Standard_A8m_v2', 'Standard_A9', 'Standard_D1',
     'Standard_D11', 'Standard_D11_v2', 'Standard_D11_v2_Promo',
     'Standard_D12', 'Standard_D12_v2', 'Standard_D12_v2_Promo',
     'Standard_D13', 'Standard_D13_v2', 'Standard_D13_v2_Promo',
     'Standard_D14', 'Standard_D14_v2', 'Standard_D14_v2_Promo',
     'Standard_D15_v2', 'Standard_D16_v3', 'Standard_D16s_v3',
     'Standard_D1_v2', 'Standard_D2', 'Standard_D2_v2', 'Standard_D2_v2_Promo',
     'Standard_D2_v3', 'Standard_D2s_v3', 'Standard_D3', 'Standard_D3_v2',
     'Standard_D3_v2_Promo', 'Standard_D4', 'Standard_D4_v2',
     'Standard_D4_v2_Promo', 'Standard_D4_v3', 'Standard_D4s_v3',
     'Standard_D5_v2', 'Standard_D5_v2_Promo', 'Standard_D8_v3',
     'Standard_D8s_v3', 'Standard_DS1', 'Standard_DS11', 'Standard_DS11_v2',
     'Standard_DS11_v2_Promo', 'Standard_DS12', 'Standard_DS12_v2',
     'Standard_DS12_v2_Promo', 'Standard_DS13', 'Standard_DS13_v2',
     'Standard_DS13_v2_Promo', 'Standard_DS14', 'Standard_DS14_v2',
     'Standard_DS14_v2_Promo', 'Standard_DS15_v2', 'Standard_DS1_v2',
     'Standard_DS2', 'Standard_DS2_v2', 'Standard_DS2_v2_Promo',
     'Standard_DS3', 'Standard_DS3_v2', 'Standard_DS3_v2_Promo',
     'Standard_DS4', 'Standard_DS4_v2', 'Standard_DS4_v2_Promo',
     'Standard_DS5_v2', 'Standard_DS5_v2_Promo', 'Standard_E16_v3',
     'Standard_E16s_v3', 'Standard_E2_v3', 'Standard_E2s_v3',
     'Standard_E32_v3', 'Standard_E32s_v3', 'Standard_E4_v3',
     'Standard_E4s_v3', 'Standard_E64_v3', 'Standard_E64s_v3',
     'Standard_E8_v3', 'Standard_E8s_v3', 'Standard_F1', 'Standard_F16',
     'Standard_F16s', 'Standard_F1s', 'Standard_F2', 'Standard_F2s',
     'Standard_F4', 'Standard_F4s', 'Standard_F8', 'Standard_F8s',
     'Standard_G1', 'Standard_G2', 'Standard_G3', 'Standard_G4', 'Standard_G5',
     'Standard_GS1', 'Standard_GS2', 'Standard_GS3', 'Standard_GS4',
     'Standard_GS5', 'Standard_H16', 'Standard_H16m', 'Standard_H16mr',
     'Standard_H16r', 'Standard_H8', 'Standard_H8m', 'Standard_L16s',
     'Standard_L32s', 'Standard_L4s', 'Standard_L8s', 'Standard_M128s',
     'Standard_M64ms', 'Standard_NC12', 'Standard_NC24', 'Standard_NC24r',
     'Standard_NC6', 'Standard_NV12', 'Standard_NV24', 'Standard_NV6'
    :type vm_size: str or
     ~azure.mgmt.containerservice.models.ContainerServiceVMSizeTypes
    :param os_disk_size_gb: OS Disk Size in GB to be used to specify the disk
     size for every machine in this master/agent pool. If you specify 0, it
     will apply the default osDisk size according to the vmSize specified.
    :type os_disk_size_gb: int
    :param vnet_subnet_id: VNet SubnetID specifies the vnet's subnet
     identifier. If you specify either master VNet Subnet, or agent VNet
     Subnet, you need to specify both. And they have to be in the same VNet.
    :type vnet_subnet_id: str
    :param first_consecutive_static_ip: FirstConsecutiveStaticIP used to
     specify the first static ip of masters. Default value: "10.240.255.5" .
    :type first_consecutive_static_ip: str
    :param storage_profile: Storage profile specifies what kind of storage
     used. Choose from StorageAccount and ManagedDisks. Leave it empty, we will
     choose for you based on the orchestrator choice. Possible values include:
     'StorageAccount', 'ManagedDisks'
    :type storage_profile: str or
     ~azure.mgmt.containerservice.models.ContainerServiceStorageProfileTypes
    :ivar fqdn: FDQN for the master pool.
    :vartype fqdn: str
    """

    _validation = {
        'dns_prefix': {'required': True},
        'vm_size': {'required': True},
        'fqdn': {'readonly': True},
    }

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'dns_prefix': {'key': 'dnsPrefix', 'type': 'str'},
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'os_disk_size_gb': {'key': 'osDiskSizeGB', 'type': 'int'},
        'vnet_subnet_id': {'key': 'vnetSubnetID', 'type': 'str'},
        'first_consecutive_static_ip': {'key': 'firstConsecutiveStaticIP', 'type': 'str'},
        'storage_profile': {'key': 'storageProfile', 'type': 'str'},
        'fqdn': {'key': 'fqdn', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ContainerServiceMasterProfile, self).__init__(**kwargs)
        self.count = kwargs.get('count', 1)
        self.dns_prefix = kwargs.get('dns_prefix', None)
        self.vm_size = kwargs.get('vm_size', None)
        self.os_disk_size_gb = kwargs.get('os_disk_size_gb', None)
        self.vnet_subnet_id = kwargs.get('vnet_subnet_id', None)
        self.first_consecutive_static_ip = kwargs.get('first_consecutive_static_ip', "10.240.255.5")
        self.storage_profile = kwargs.get('storage_profile', None)
        self.fqdn = None
