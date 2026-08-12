import requests
import ipaddress


def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as error:
        print(f"Error: {error}")
        return None


def display_info(data):
    print("\n===== IP INFORMATION =====")
    print(f"IP Address : {data.get('ip', 'N/A')}")
    print(f"Hostname   : {data.get('hostname', 'N/A')}")
    print(f"City       : {data.get('city', 'N/A')}")
    print(f"Region     : {data.get('region', 'N/A')}")
    print(f"Country    : {data.get('country', 'N/A')}")
    print(f"Location   : {data.get('loc', 'N/A')}")
    print(f"Timezone   : {data.get('timezone', 'N/A')}")
    print(f"ISP/Org    : {data.get('org', 'N/A')}")
    print("===========================\n")


def main():
    ip = input("Enter an IP address: ").strip()

    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print("Invalid IP address.")
        return

    data = get_ip_info(ip)

    if data:
        display_info(data)


if __name__ == "__main__":
    main()