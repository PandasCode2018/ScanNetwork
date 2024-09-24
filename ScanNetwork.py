from scapy.all import ARP, Ether, srp, conf

def scanNetwork(rangoIp):
    print(f"Escaneando dispositivos en la red {rangoIp}...")
    conf.L3socket()
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=rangoIp), timeout=2, verbose=0)
    activeHost = [res[1].psrc for res in ans]
    print("Dispositivos activos:")
    for host in activeHost:
        print(f"- {host}")

if __name__ == "__main__":
    target_network = "192.168.1.0/24"
    scanNetwork(target_network)
