# Ansible Collection - adinda.test

![CI](https://github.com/asim10/adinda.test/workflows/CI/badge.svg)
[![Codecov](https://img.shields.io/codecov/c/github/asim10/adinda.test)](https://codecov.io/gh/asim10/adinda.test)

This repository contains the `adinda.test` Ansible Collection. The collection is a test ansible collection to start my journey into the custom ansible collection world and contribute to upstream ansible community collections.

Please note that this collection does **not** support Windows targets.

## Tested with Ansible

Tested with the ansible-core 2.13, ansible-core 2.14, ansible-core 2.15 and ansible-core 2.16

## Using this collection

This collection is not shipped with the ansible package. Below are the steps to install the collection:
You can install it manually with the `ansible-galaxy` command-line tool:

    ansible-galaxy collection install adinda.test

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
collections:
- name: adinda.test
```

## Licensing

In Progress...