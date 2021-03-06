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

from .workload_protectable_item import WorkloadProtectableItem


class AzureVmWorkloadProtectableItem(WorkloadProtectableItem):
    """Azure VM workload-specific protectable item.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AzureVmWorkloadSQLAvailabilityGroupProtectableItem,
    AzureVmWorkloadSQLDatabaseProtectableItem,
    AzureVmWorkloadSQLInstanceProtectableItem

    All required parameters must be populated in order to send to Azure.

    :param backup_management_type: Type of backup managemenent to backup an
     item.
    :type backup_management_type: str
    :param workload_type: Type of workload for the backup management
    :type workload_type: str
    :param friendly_name: Friendly name of the backup item.
    :type friendly_name: str
    :param protection_state: State of the back up item. Possible values
     include: 'Invalid', 'NotProtected', 'Protecting', 'Protected',
     'ProtectionFailed'
    :type protection_state: str or
     ~azure.mgmt.recoveryservicesbackup.models.ProtectionStatus
    :param protectable_item_type: Required. Constant filled by server.
    :type protectable_item_type: str
    :param parent_name: Name for instance or AG
    :type parent_name: str
    :param parent_unique_name: Parent Unique Name is added to provide the
     service formatted URI Name of the Parent
     Only Applicable for data bases where the parent would be either Instance
     or a SQL AG.
    :type parent_unique_name: str
    :param server_name: Host/Cluster Name for instance or AG
    :type server_name: str
    :param is_auto_protectable: Indicates if protectable item is
     auto-protectable
    :type is_auto_protectable: bool
    :param subinquireditemcount: For instance or AG, indicates number of DB's
     present
    :type subinquireditemcount: int
    :param subprotectableitemcount: For instance or AG, indicates number of
     DB's to be protected
    :type subprotectableitemcount: int
    :param prebackupvalidation: Pre-backup validation for protectable objects
    :type prebackupvalidation:
     ~azure.mgmt.recoveryservicesbackup.models.PreBackupValidation
    """

    _validation = {
        'protectable_item_type': {'required': True},
    }

    _attribute_map = {
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'workload_type': {'key': 'workloadType', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'protection_state': {'key': 'protectionState', 'type': 'str'},
        'protectable_item_type': {'key': 'protectableItemType', 'type': 'str'},
        'parent_name': {'key': 'parentName', 'type': 'str'},
        'parent_unique_name': {'key': 'parentUniqueName', 'type': 'str'},
        'server_name': {'key': 'serverName', 'type': 'str'},
        'is_auto_protectable': {'key': 'isAutoProtectable', 'type': 'bool'},
        'subinquireditemcount': {'key': 'subinquireditemcount', 'type': 'int'},
        'subprotectableitemcount': {'key': 'subprotectableitemcount', 'type': 'int'},
        'prebackupvalidation': {'key': 'prebackupvalidation', 'type': 'PreBackupValidation'},
    }

    _subtype_map = {
        'protectable_item_type': {'SQLAvailabilityGroupContainer': 'AzureVmWorkloadSQLAvailabilityGroupProtectableItem', 'SQLDataBase': 'AzureVmWorkloadSQLDatabaseProtectableItem', 'SQLInstance': 'AzureVmWorkloadSQLInstanceProtectableItem'}
    }

    def __init__(self, **kwargs):
        super(AzureVmWorkloadProtectableItem, self).__init__(**kwargs)
        self.parent_name = kwargs.get('parent_name', None)
        self.parent_unique_name = kwargs.get('parent_unique_name', None)
        self.server_name = kwargs.get('server_name', None)
        self.is_auto_protectable = kwargs.get('is_auto_protectable', None)
        self.subinquireditemcount = kwargs.get('subinquireditemcount', None)
        self.subprotectableitemcount = kwargs.get('subprotectableitemcount', None)
        self.prebackupvalidation = kwargs.get('prebackupvalidation', None)
        self.protectable_item_type = 'AzureVmWorkloadProtectableItem'
