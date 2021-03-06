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


class DetectedTerms(Model):
    """Detected Terms details.

    :param index: Index(Location) of the detected profanity term in the input
     text content.
    :type index: int
    :param original_index: Original Index(Location) of the detected profanity
     term in the input text content.
    :type original_index: int
    :param list_id: Matched Terms list Id.
    :type list_id: int
    :param term: Detected profanity term.
    :type term: str
    """

    _attribute_map = {
        'index': {'key': 'Index', 'type': 'int'},
        'original_index': {'key': 'OriginalIndex', 'type': 'int'},
        'list_id': {'key': 'ListId', 'type': 'int'},
        'term': {'key': 'Term', 'type': 'str'},
    }

    def __init__(self, index=None, original_index=None, list_id=None, term=None):
        super(DetectedTerms, self).__init__()
        self.index = index
        self.original_index = original_index
        self.list_id = list_id
        self.term = term
