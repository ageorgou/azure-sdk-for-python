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


class KeyOperationsParameters(Model):
    """The key operations parameters.

    :param algorithm: algorithm identifier. Possible values include:
     'RSA-OAEP', 'RSA-OAEP-256', 'RSA1_5'
    :type algorithm: str or :class:`JsonWebKeyEncryptionAlgorithm
     <azure.keyvault.models.JsonWebKeyEncryptionAlgorithm>`
    :param value:
    :type value: bytes
    """

    _validation = {
        'algorithm': {'required': True, 'min_length': 1},
        'value': {'required': True},
    }

    _attribute_map = {
        'algorithm': {'key': 'alg', 'type': 'str'},
        'value': {'key': 'value', 'type': 'base64'},
    }

    def __init__(self, algorithm, value):
        self.algorithm = algorithm
        self.value = value
