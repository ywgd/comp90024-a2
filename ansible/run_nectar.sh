#!/usr/bin/env bash

. ./openrc.sh; ansible-playbook -i hosts nectar.yaml
