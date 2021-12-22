#!/usr/bin/python
#
# Usage: packer-config my-template.yaml | packer build -
#
# Constructs a Packer JSON configuration file from the specified YAML
# template file and writes it to STDOUT.
# 
# The YAML template format adds some flexibility and readability by
# adding comments and an !include directive, allowing for the
# following template syntax:
# 
#     variables:
#      - ssh_user: ubuntu
#      - ssh_pass: ubuntu
#      - hostname: host
#     builders:
#      - !include build/ubuntu-12.04.kvm.yaml
#      - !include build/ubuntu-12.04.ami.yaml
#     provisioners:
#      - !include provision/ubuntu-12.04-base.yaml
#      - !include provision/ops-deploy.yaml
#      - !include provision/java7.yaml
#      - type: shell
#        environment_vars: [ 'HOST_NAME={{user `hostname`}}' ]
#        script: host/setup.sh
# 
# In addition to the !include directive, the resulting YAML is
# post-processed to flatten lists-of-lists in the top level sections,
# allowing includes to contain multiple entries (i.e. running two shell
# scripts in a common provisioner.)
#
# Author: jeremy@jongsma.org
# License: MPLv2

import sys
import os
import yaml
import json


class IncludeLoader(yaml.Loader):
    """
    Custom YAML loader that adds an !include constructor for including
    other YAML files relative to the current file being parsed.

    Example:

        section: !include other/file.yaml

    """

    def __init__(self, stream):
        self._root = os.path.abspath(os.path.split(stream.name)[0])
        super(IncludeLoader, self).__init__(stream)

    def include(self, node):
        path = self.construct_scalar(node)
        filename = path if path[0] == '/' else os.path.join(self._root, path)
        with open(filename, 'r') as f:
            return yaml.load(f, IncludeLoader)

IncludeLoader.add_constructor('!include', IncludeLoader.include) 


def parse_yaml(template):
    """
    Constructs a Packer JSON configuration file from the specified YAML
    template and returns it as a string.

    The YAML template format adds some flexibility and readability by
    adding comments and an !include directive, allowing for the
    following template syntax:

        builders:
         - !include build/ubuntu-12.04.kvm.yaml
         - !include build/ubuntu-12.04.ami.yaml
        provisioners:
         - !include provision/ubuntu-12.04-base.yaml
         - !include provision/ops-deploy.yaml
         - !include provision/java7.yaml
         - type: shell
           script: app/setup.sh

    In addition to the !include directive, the resulting YAML is
    post-processed to flatten lists-of-lists in the top level sections,
    allowing includes to contain lists of multiple entries (i.e. running
    two shell scripts in a common provisioner.)
    """
    
    with open(template, 'r') as infile:
        parsed = yaml.load(infile, IncludeLoader)
        # Flatten sections to allow including lists of steps in each include
        for section in ('builders', 'provisioners', 'post-processors'):
            if section in parsed:
                parsed[section] = [f for l in [e if isinstance(e, list) else [e]
                    for e in parsed[section]] for f in l]
        return json.dumps(parsed)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        sys.stderr.write("ERROR: No template specified")
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        std.stderr.write("ERROR: Template not found: %s" % sys.argv[1])
        sys.exit(2)

    sys.stdout.write(parse_yaml(sys.argv[1]))