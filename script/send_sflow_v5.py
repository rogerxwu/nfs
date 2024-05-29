from scapy.all import *


def create_sflow_packet():
    # Combine all parts into a single payload
    payload = (
        b"\x00\x00\x00\x05\x00\x00"
        b"\x00\x01\x0a\xac\x00\x03\x00\x00\x00\x00\xb7\x24\x7c\x6f\x41\x13"
        b"\x22\xb8\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x01\x2c\x1b\xa4"
        b"\xf2\xc0\x00\x0f\x42\x41\x00\x00\x20\x00\x15\x51\x60\x00\x00\x00"
        b"\x00\x00\x00\x0f\x42\x41\x00\x0f\x43\xd2\x00\x00\x00\x04\x00\x00"
        b"\x03\xe9\x00\x00\x00\x10\x00\x00\x02\x69\x00\x00\x00\x00\x00\x00"
        b"\x02\x69\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x90\x00\x00"
        b"\x00\x01\x00\x00\x05\xf2\x00\x00\x00\x04\x00\x00\x00\x80\x00\x00"
        b"\x5e\x00\x01\x01\x3c\xec\xef\xcb\xbd\x8e\xa1\x00\x02\x69\x08\x00"
        b"\x45\x00\x05\xdc\x27\x22\x40\x00\x40\x06\x83\xd1\x0a\xac\x6b\x32"
        b"\x0a\xd1\x09\x7a\x23\x84\x06\x45\xaf\x46\x47\x5e\xec\x49\xfe\xf5"
        b"\x80\x10\x10\x05\x7a\x0e\x00\x00\x01\x01\x08\x0a\x28\x8a\xbe\x5c"
        b"\xcd\xbd\x1d\xbe\xc2\x3e\xd2\x0e\xaa\x06\xfe\xbe\x1e\x08\x32\x89"
        b"\x18\x00\xc0\xfe\x1e\x08\x12\x1e\x08\x00\x39\x31\xeb\x1a\x1e\x08"
        b"\x08\x47\x30\x47\xae\x1e\x08\x19\x92\x1a\x3a\x10\xfe\x89\x18\xfe"
        b"\x89\x18\xfe\x89\x18\xfe\x89\x18\x92\x89\x18\x26\x1e\x08\x00\x00"
        b"\x03\xeb\x00\x00\x00\x3c\x00\x00\x00\x01\x0a\xac\x00\xf3\x00\x00"
        b"\xff\xdf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00"
        b"\x00\x02\x00\x00\x00\x05\xff\xdf\x00\x01\x00\x00\xff\xfe\xff\xdf"
        b"\xff\xdf\xff\xdf\xff\xdf\xff\xdf\xff\xdf\x00\x00\x00\x00\x00\x00"
        b"\x00\x64\x00\x00\x03\xea\x00\x00\x00\x10\x00\x00\x00\x01\x0a\xac"
        b"\x00\xf3\x00\x00\x00\x15\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00"
        b"\x00\x98\x21\x6d\xed\xc4\x00\x0f\x42\xa4\x00\x00\x20\x00\x27\xbc"
        b"\x80\x00\x00\x00\x00\x00\x00\x0f\x42\xa4\x00\x0f\x42\x41\x00\x00"
        b"\x00\x02\x00\x00\x03\xe9\x00\x00\x00\x10\x00\x00\x02\x79\x00\x00"
        b"\x00\x00\x00\x00\x02\x79\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00"
        b"\x00\x58\x00\x00\x00\x01\x00\x00\x00\x4a\x00\x00\x00\x04\x00\x00"
        b"\x00\x46\x00\x00\x5e\x00\x01\x01\xb4\x7a\xf1\x65\x23\x87\x81\x00"
        b"\x02\x79\x08\x00\x45\x00\x00\x34\xe4\xb0\x40\x00\x40\x06\xce\xde"
        b"\x0a\xae\x08\x6e\x0a\xac\x69\x6d\xbe\xe2\x23\x84\x0c\x0a\xaa\x8f"
        b"\xf1\x47\x19\xb9\x80\x10\xc7\x43\xa5\xf0\x00\x00\x01\x01\x08\x0a"
        b"\x35\xe9\x8e\x21\x06\x6d\x13\xdb\x01\x24\x00\x00\x00\x01\x00\x00"
        b"\x00\xd0\x21\x6d\xeb\xc5\x00\x0f\x42\xa4\x00\x00\x20\x00\x27\xbc"
        b"\xa0\x00\x00\x00\x00\x00\x00\x0f\x42\xa4\x00\x0f\x42\x41\x00\x00"
        b"\x00\x02\x00\x00\x03\xe9\x00\x00\x00\x10\x00\x00\x02\x6f\x00\x00"
        b"\x00\x00\x00\x00\x02\x6f\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00"
        b"\x00\x90\x00\x00\x00\x01\x00\x00\x05\xf2\x00\x00\x00\x04\x00\x00"
        b"\x00\x80\x00\x00\x5e\x00\x01\x01\x3c\xec\xef\xc6\xd3\xfe\x81\x00"
        b"\x02\x6f\x08\x00\x45\x00\x05\xdc\xe5\x65\x40\x00\x3e\x06\xfa\x84"
        b"\x0a\xae\x00\x58\x0a\xb1\x41\x7b\x3b\x68\x23\x52\x57\xcc\x85\x36"
        b"\x88\x23\x77\x91\x80\x10\x01\xe6\x0b\x1a\x00\x00\x01\x01\x08\x0a"
        b"\x0f\xcb\x9b\x88\x95\xfa\xe7\xec\x04\x00\x34\x00\x0d\x00\x00\x0a"
        b"\x60\x01\x00\x05\x01\x00\x10\x9c\x95\xab\x12\xf4\xde\x2f\xb9\xc7"
        b"\xa9\x92\xa6\x9e\xda\x30\x32\x00\x0b\x00\x00\x00\x33\x70\x69\x64"
        b"\x3a\x34\x39\x31\x62\x36\x36\x62\x64\x32\x33\x61\x39\x34\x31\x39"
        b"\x61\x62\x00\x00\x00\x01\x00\x00\x01\x2c\x1b\xa4\xf2\xc1\x00\x0f"
        b"\x42\x41\x00\x00\x20\x00\x15\x51\x80\x0f\x00\x00\x00\x00\x00\x00"
        b"\x42\x41\x00\x0f\x43\xd4\x00\x00\x00\x04\x00\x00\x03\xe9\x00\x00"
        b"\x00\x10\x00\x00\x02\x69\x00\x00\x00\x00\x00\x00\x02\x69\x00\x00"
        b"\x00\x00\x00\x00\x00\x01\x00\x00\x00\x90\x00\x00\x00\x01\x00\x00"
        b"\x05\xf2\x00\x00\x00\x04\x00\x00\x00\x80\x00\x00\x5e\x00\x01\x01"
        b"\x3c\xec\xef\xcb\xc1\x8c\x81\x00\x02\x69\x08\x00\x45\x00\x05\xdc"
        b"\x44\x09\x40\x00\x40\x06\x66\xe4\x0a\xac\x6b\x41\x0a\xd1\x09\x71"
        b"\x23\x84\xcb\x5a\x65\x23\x82\x67\xba\x41\x21\xaa\x80\x10\x10\x05"
        b"\x67\xac\x00\x00\x01\x01\x08\x0a\x5b\x0a\xcc\xba\x47\xec\x30\xae"
        b"\x43\x61\x94\xca\xfb\x16\xd0\xa8\xce\xad\x1a\xec\x26\x3e\x81\x15"
        b"\x42\x27\x00\x04\xf5\xb7\x0e\x51\x15\x12\x42\x0b\x48\x36\x35\x61"
        b"\x33\x33\x62\x32\x31\x2d\x36\x61\x31\x30\x2d\x34\x36\x30\x62\x2d"
        b"\x0e\x14\x69\x3c\x2d\x30\x33\x31\x39\x66\x00\x00\x03\xed\x00\x00"
        b"\x00\x3c\x00\x00\x00\x01\x0a\xac\x00\xf7\x00\x00\xff\xdf\x00\x00"
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00"
        b"\x00\x05\xff\xdf\x00\x01\x00\x00\xff\xfe\xff\xdf\xff\xdf\xff\xdf"
        b"\xff\xdf\xff\xdf\xff\xdf\x00\x00\x00\x00\x00\x00\x00\x64\x00\x00"
        b"\x03\xea\x00\x00\x00\x10\x00\x00\x00\x01\x0a\xac\x00\xf7\x00\x00"
        b"\x00\x15\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x24\x1b\xa4"
        b"\xf2\xc2\x00\x0f\x42\x41\x00\x00\x20\x00\x15\x51\xa0\x00\x00\x00"
        b"\x00\x00\x00\x0f\x42\x41\x00\x0f\x43\xd4\x00\x00\x00\x04\x00\x00"
        b"\x03\xe9\x00\x00\x00\x10\x00\x00\x02\x69\x00\x00\x00\x00\x00\x00"
        b"\x02\x69\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x90\x00\x00"
        b"\x00\x01\x00\x00\x00\xad\x00\x00\x00\x04\x00\x00\x00\x80\x00\x00"
        b"\x5e\x00\x01\x01\x3c\xec\xef\xcb\x9b\xf2\x81\x00\x02\x69\x08\x00"
        b"\x45\x00\x00\x97\x76\xb8\x40\x00\x40\x06\xf5\x29\x0a\xac\x6a\xe6"
        b"\x0a\xad\x4e\x60\x23\x84\xc5\x71\x41\x7b\x4e\x26\x6f\x9b\x4a\x83"
        b"\x80\x18\x10\x05\x7e\x8a\x00\x00\x01\x01\x08\x0a\x2b\xb2\xd6\x26"
        b"\x54\xbd\x6a\x13\x00\x00\x08\x32\x00\x51\x2e\x55\x00\x00\x00\x00"
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x1d\x63\x73\x6d\x2d"
        b"\x73\x30\x30\x31\x2d\x30\x37\x64\x2d\x30\x34\x2d\x70\x6f\x64\x2d"
        b"\x6d\x75\x74\x61\x74\x69\x6f\x6e\x73\x00\x00\x00\x01\x00\x00\x00"
        b"\x03\xeb\x00\x00\x00\x34\x00\x00\x00\x01\x0a\xac\x88\xf7\x00\x00"
        b"\xff\xdf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00"
        b"\x00\x02\x00\x00\x00\x03\xff\xdf\x00\x01\xff\xdf\x00\x0b\xff\xdf"
        b"\x00\x65\x00\x00\x00\x00\x00\x00\x00\x64\x00\x00\x03\xea\x00\x00"
        b"\x00\x10\x00\x00\x00\x01\x0a\xac\x00\xf7\x00\x00\x00\x15\x00\x00"
        b"\x00\x11"
    )

    return payload


def send_sflow_packet(payload):
    packet = IP(dst="127.0.0.1") / UDP(dport=6343) / Raw(load=payload)
    send(packet)


# Create sFlow packet payload
payload = create_sflow_packet()

# Send the sFlow packet
send_sflow_packet(payload)
