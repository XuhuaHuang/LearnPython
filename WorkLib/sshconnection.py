# Topic: Customized library file to connect to VM/equipments using SSH protocol
# Ask user questions for information and connect to host
# Author: Xuhua Huang
#
# Last updated: Aug 8, 2021
# Created on: Aug 8, 2021

import paramiko

# ----------------------------------------------------------------------------------------------------------------------
# custom dictionary to contains all the sensitive information
ssh_connection: dict = {
    'username': 'brainbox',
    'password': '',
    'server': '',
    'lea_vm': '',
    'crt_file_path': 'PATH/TO/KEY',  # default location: /Users//%USERNAME/.ssh/id_rsa
    'crt_password': ''
}
# ----------------------------------------------------------------------------------------------------------------------


class SSHConnection:
    def __init__(self) -> None:
        self._server: str = ssh_connection['server']  # connection to this host will be marked as `server_connection`
        self._lea_vm: str = ssh_connection['lea_vm']  # connection to this host will be marked as `lea_vm_connection`
        # Read information from the provided dictionary
        self._username: str = ssh_connection['username']
        self._password: str = ssh_connection['password']
        self._crt_path: str = ssh_connection['crt_file_path']
        self._crt_pass: str = ssh_connection['crt_password']

    def get_server_connection(self) -> paramiko.SSHClient:
        server = paramiko.SSHClient()
        server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        server.connect(hostname=self._server,
                       username=self._username,
                       password=self._crt_pass,
                       key_filename=self._crt_path)
        return server

    def get_lea_vm_connection(self) -> paramiko.SSHClient:
        lea_vm = paramiko.SSHClient()
        lea_vm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        lea_vm.connect(hostname=self._lea_vm,
                       username=self._username,
                       password=self._password,
                       key_filename=self._crt_path)
        return lea_vm


def main():
    my_server_conn = SSHConnection()
    my_server_conn.get_server_connection()


if __name__ == '__main__':
    main()
