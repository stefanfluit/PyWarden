PyWarden
==============

[![Github Issues](https://img.shields.io/github/issues/stefanfluit/PyWarden?label=Github%20issues%3A)](https://github.com/stefanfluit/PyWarden/issues)
[![PyPi Downloads](https://img.shields.io/pypi/dm/PyWarden?label=PyPi%20downloads%3A)](https://pypi.org/project/PyWarden/)
[![License](https://img.shields.io/github/license/stefanfluit/PyWarden?label=license%3A)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![Current Release](https://img.shields.io/pypi/v/PyWarden?label=current%20release%3A)](https://pypi.org/project/PyWarden/)

PyWarden is a Python CLI application that interacts with both the Bitwarden API and CLI to provide a simple interface for managing your Bitwarden vault. It's main purpose is to provide a simple way to manage your Bitwarden vault from the command line without having to worry about B64 encoded JSON strings and templates.

Table of Contents:
============
- [Purpose](#Purpose)
- [Prerequisites](#Prerequisites)
- [Installation](#Installation)
- [Configuration](#Configuration)
- [Usage on the command line](#UsageCommandLine)
- [Usage in Ansible](#UsageAnsible)

Purpose
============
PyWarden is used to incorporate in Ansible plays to easily create Organization Collections and Items in those collections, in plain text. PyWarden takes care of the encoding and decryption of the data and the creation of the JSON templates that are required by the Bitwarden CLI.

Prerequisites
============
- Bitwarden CLI
- Bitwarden account with access to the API
- Bitwarden Organization API key
- Master Password
- WSL 2.0, or Linux environment.

#### How to install the CLI:
* Using NPM: `npm install -g @bitwarden/cli`
* Using Snap: `sudo snap install bw`
* Using Chocolatey: `choco install bitwarden-cli`

#### Or native installers:
* Download native executable for Windows from [here](https://vault.bitwarden.com/download/?app=cli&platform=windows)
* Download native executable for Mac from [here](https://vault.bitwarden.com/download/?app=cli&platform=macos)
* Download native executable for Linux from [here](https://vault.bitwarden.com/download/?app=cli&platform=linux)

Installation
============

#### Using pip:
* PyWarden can be installed using pip: `pip install PyWarden`
* PyWarden can be updated using pip: `pip install PyWarden --upgrade`
After this, you can use the `pywarden` command to run the application. 
If not, you can add the path to the `pywarden` executable to your PATH environment variable. 
This can be done by adding the following line to your `.bashrc` or `.zshrc` file: `export PATH="$HOME/.local/bin:$PATH"`
Restart your terminal and you should be able to run the `pywarden` command.

#### Using git:
* PyWarden can be installed using git: 
```
git clone https://github.com/stefanfluit/PyWarden.git
cd PyWarden && ./build.sh test
```
* PyWarden can be updated using git:
```
cd PyWarden && git pull
./build.sh test
```

Configuration
============
PyWarden requires a configuration file to be able to interact with the Bitwarden API and CLI.
The configuration file is hosted in this repository and can be downloaded using the following command:
```
curl -o ~/pywarden_config.yml https://raw.githubusercontent.com/stefanfluit/PyWarden/main/pywarden_config_template.yaml
```
Or, you can manage the configuration using PyWarden:
```
pywarden --gen-config
```
This will generate a configuration file in your home directory and ask you to fill in the required information.

#### Where to find the information:
Bitwarden Organization API key:
* Log in to your Bitwarden account
* Go to Organizations > Settings
* The menu `API Key` has a button `View API Key` that will show the API key.
* Copy the `client_id` and `client_secret` values and add them to the configuration file.

Bitwarden personal API key:
* Log in to your Bitwarden account
* Go to `Account Settings` > `Security` > `Keys`
* The menu `API Key` has a button `View API Key` that will show the API key.
* Copy the `client_id` and `client_secret` values and add them to the configuration file.

The other questions PyWarden will ask should be simple enough to not rquire further explanation.

Usage on the command line
============
PyWarden can be used on the command line to create Organization Collections and Items in those collections.
The following commands are available:
```
  -h, --help            show this help message and exit
  --version             show version
  --debug               enable debug mode
  --status              Show status of PyWarden
  --check-config        Check configuration validity
  --gen-password        Generate a password
  --gen-config          Generate a configuration file
  --add-org-entry       Add an entry to your vault
  --check-exists        Check if an entry exists in your vault
  --list-org-item       List an item from your organization
  --list-item           List an item from your personal vault
```

#### Example usage:
* Creating a new Organization Collection:
```
pywarden --add-org-collection --name "MyCollection" --access-group "MyGroup"
```

* Creating a new Organization Item:
```
--add-org-entry --name test-28 --username test-pywarden --password test-28 --url https://url.domain.com --org-collection test-28 --access-group "System Administrators" 
```

Usage in Ansible
============
PyWarden can be used in Ansible to create Organization Collections and Items in those collections.
```
- name: Ensure python3-pip is installed
  ansible.builtin.package:
    name: python3-pip
    state: present

- name: Ensure pip3 is upgraded
  ansible.builtin.pip:
    name: pip
    state: latest

- name: Ensure PyWarden is installed
  ansible.builtin.pip:
      name: PyWarden
      state: latest

- name: Copy template configuration file
  ansible.builtin.template:
    src: pywarden_config_template.yaml.j2
    dest: /root/pywarden_config.yaml
    mode: 0600
    remote_src: no

- name: Create Organization Collection
  ansible.builtin.command:
    cmd: pywarden --add-org-collection --name "{{ item.name }}" --access-group "{{ item.access_group }}"
  loop:
      - { name: "MyCollection", access_group: "MyGroup" }
      - { name: "MyCollection2", access_group: "MyGroup" }
      - { name: "MyCollection3", access_group: "MyGroup" }

- name: Create Organization Item
    ansible.builtin.command:
        cmd: pywarden --add-org-entry --name "{{ item.name }}" --username "{{ item.username }}" --password "{{ item.password }}" --url "{{ item.url }}" --org-collection "{{ item.org_collection }}" --access-group "{{ item.access_group }}"
    loop:
        - { name: "test-28", username: "test-pywarden", password: "test-28", url: "https://url.domain.com", org_collection: "MyCollection", access_group: "MyGroup" }
        - { name: "test-29", username: "test-pywarden", password: "test-29", url: "https://url.domain.com", org_collection: "MyCollection", access_group: "MyGroup" }
        - { name: "test-30", username: "test-pywarden", password: "test-30", url: "https://url.domain.com", org_collection: "MyCollection", access_group: "MyGroup" }
```

Issues
============
If you encounter any issues, please create an issue on the [GitHub repository](https://github.com/stefanfluit/PyWarden/issues).

Contributing
============
If you want to contribute to this project, please create a pull request on the [GitHub repository](https://github.com/stefanfluit/PyWarden).
