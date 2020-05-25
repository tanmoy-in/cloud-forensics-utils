# -*- coding: utf-8 -*-
# Copyright 2020 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Common utilities."""
import logging
import re

EC2_SERVICE = 'ec2'
ACCOUNT_SERVICE = 'sts'
KMS_SERVICE = 'kms'
CLOUDTRAIL_SERVICE = 'cloudtrail'

# Default Amazon Machine Image to use for bootstrapping instances
UBUNTU_1804_AMI = 'ami-0013b3aa57f8a4331'
REGEX_TAG_VALUE = re.compile('^.{1,255}$')

LOGGER = logging.getLogger()


def GetTagForResourceType(resource, name):
  """Create a dictionary for AWS Tag Specifications.

  Args:
    resource (str): The type of AWS resource.
    name (str): The name of the resource.

  Returns:
    dict: A dictionary for AWS Tag Specifications.
  """

  return {
      'ResourceType': resource,
      'Tags': [
          {
              'Key': 'Name',
              'Value': name
          }
      ]
  }


def GetInstanceTypeByCPU(cpu_cores):
  """Return the instance type for the requested number of  CPU cores.

  Args:
    cpu_cores (int): The number of requested cores.

  Returns:
    str: The type of instance that matches the number of cores.

  Raises:
    ValueError: If the requested amount of cores is unavailable.
  """

  cpu_cores_to_instance_type = {
      1: 't2.small',
      2: 'm4.large',
      4: 'm4.xlarge',
      8: 'm4.2xlarge',
      16: 'm4.4xlarge',
      32: 'm5.8xlarge',
      40: 'm4.10xlarge',
      48: 'm5.12xlarge',
      64: 'm4.16xlarge',
      96: 'm5.24xlarge',
      128: 'x1.32xlarge'
  }
  if cpu_cores not in cpu_cores_to_instance_type:
    raise ValueError(
        'Cannot start a machine with {0:d} CPU cores. CPU cores should be one'
        ' of: {1:s}'.format(
            cpu_cores, ', '.join(map(str, cpu_cores_to_instance_type.keys()))
        ))
  return cpu_cores_to_instance_type[cpu_cores]