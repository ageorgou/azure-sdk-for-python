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


class Operation(Model):
    """An available operation for Data Lake Analytics.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the operation.
    :vartype name: str
    :ivar display: The display information for the operation.
    :vartype display:
     ~azure.mgmt.datalake.analytics.account.models.OperationDisplay
    :ivar origin: The intended executor of the operation. Possible values
     include: 'user', 'system', 'user,system'
    :vartype origin: str or
     ~azure.mgmt.datalake.analytics.account.models.OperationOrigin
    """

    _validation = {
        'name': {'readonly': True},
        'display': {'readonly': True},
        'origin': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(self):
        super(Operation, self).__init__()
        self.name = None
        self.display = None
        self.origin = None
