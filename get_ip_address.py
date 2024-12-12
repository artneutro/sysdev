import socket
import struct
import fcntl

def get_ip_address(interface: str) -> str:
    """
    Uses a combination of the socket, struct and fcntl modules to get the IP 
    address of the provided interface. Works only in Linux/Unix. 
    Returns:
        The IP address in quad-dotted notation of four decimal integers.
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packed_iface = struct.pack('256s', interface.encode('utf_8'))
    packed_addr = fcntl.ioctl(sock.fileno(), 0x8915, packed_iface)[20:24]
    return socket.inet_ntoa(packed_addr)

# Sample usage
# get_ip_address('eth0')








