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

from .resource import Resource


class ManagedCluster(Resource):
    """Managed cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar provisioning_state: The current deployment or provisioning state,
     which only appears in the response.
    :vartype provisioning_state: str
    :param dns_prefix: DNS prefix specified when creating the managed cluster.
    :type dns_prefix: str
    :ivar fqdn: FDQN for the master pool.
    :vartype fqdn: str
    :param kubernetes_version: Version of Kubernetes specified when creating
     the managed cluster.
    :type kubernetes_version: str
    :param agent_pool_profiles: Properties of the agent pool.
    :type agent_pool_profiles:
     list[~azure.mgmt.containerservice.models.ContainerServiceAgentPoolProfile]
    :param linux_profile: Profile for Linux VMs in the container service
     cluster.
    :type linux_profile:
     ~azure.mgmt.containerservice.models.ContainerServiceLinuxProfile
    :param service_principal_profile: Information about a service principal
     identity for the cluster to use for manipulating Azure APIs. Either secret
     or keyVaultSecretRef must be specified.
    :type service_principal_profile:
     ~azure.mgmt.containerservice.models.ContainerServiceServicePrincipalProfile
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'fqdn': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'dns_prefix': {'key': 'properties.dnsPrefix', 'type': 'str'},
        'fqdn': {'key': 'properties.fqdn', 'type': 'str'},
        'kubernetes_version': {'key': 'properties.kubernetesVersion', 'type': 'str'},
        'agent_pool_profiles': {'key': 'properties.agentPoolProfiles', 'type': '[ContainerServiceAgentPoolProfile]'},
        'linux_profile': {'key': 'properties.linuxProfile', 'type': 'ContainerServiceLinuxProfile'},
        'service_principal_profile': {'key': 'properties.servicePrincipalProfile', 'type': 'ContainerServiceServicePrincipalProfile'},
    }

    def __init__(self, location, tags=None, dns_prefix=None, kubernetes_version=None, agent_pool_profiles=None, linux_profile=None, service_principal_profile=None):
        super(ManagedCluster, self).__init__(location=location, tags=tags)
        self.provisioning_state = None
        self.dns_prefix = dns_prefix
        self.fqdn = None
        self.kubernetes_version = kubernetes_version
        self.agent_pool_profiles = agent_pool_profiles
        self.linux_profile = linux_profile
        self.service_principal_profile = service_principal_profile
