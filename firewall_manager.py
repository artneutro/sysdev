
import subprocess
import sys

class FirewallManager:

    def __init__(self) :
        # Fixed port for SFTP container service
        self.port = '18900'

    def list_rules(self) :
        # Definition to list all the firewall rules
        # Input: None
        # Output: None
        try :
            output = subprocess.check_output(["/usr/sbin/iptables", "-L", "-n"])
            print(output)
        except subprocess.CalledProcessError as e :
            raise FWException("Error listing rules: ") from e

    def add_rule(self, ip, action="ACCEPT") :
        # Definition to add firewall rules using the port 18900
        # Input: IP address to add in the firewall
        # Output: None
        try :
            subprocess.check_call([
                "/usr/sbin/iptables", "-A", "INPUT", "-p", "tcp", "--dport", self.port, "-s", ip, "-j", action
            ])
            print("Rule added successfully")
        except subprocess.CalledProcessError as e :
            raise FWException("Error adding rule: ") from e

    def delete_rule(self, ip) :
        # Definition to delete firewall rules using the port 18900
        # Input: IP address to delete in the firewall
        # Output: None
        try:
            subprocess.check_call([
                "/usr/sbin/iptables", "-D", "INPUT", "-p", "tcp", "--dport", self.port, "-s", ip, "-j", "ACCEPT"
            ])
            print("Rule deleted successfully")
        except subprocess.CalledProcessError as e :
            raise FWException("Error deleting rule: ") from e

class FWException(Exception) :
    pass

