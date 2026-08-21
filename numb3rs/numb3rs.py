import re

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if valid_ip := re.search(r"^(0|(?!0)\d+)\.(0|(?!0)\d+)\.(0|(?!0)\d+)\.(0|(?!0)\d+)$", ip):
        octets = [
        int(valid_ip.group(1)),
        int(valid_ip.group(2)),
        int(valid_ip.group(3)),
        int(valid_ip.group(4))
        ]
        for octet in octets:
            if octet >= 0 and octet <= 255:
                continue
            else:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
