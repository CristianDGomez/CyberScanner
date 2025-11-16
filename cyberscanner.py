import socket
import datetime

def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)
    try:
        scanner.connect((ip, port))
        return True
    except:
        return False

def run_scan():
    print("=== CYBER SCANNER – Escáner básico de puertos ===")
    target_ip = input("👉 Ingrese la IP o dominio a escanear: ")
    start_port = int(input("👉 Puerto inicial: "))
    end_port = int(input("👉 Puerto final: "))

    print(f"\n🔎 Escaneando {target_ip} del puerto {start_port} al {end_port}...\n")

    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port):
            print(f"[OPEN]  Puerto {port} está abierto")
            open_ports.append(port)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_name = f"reporte_scan_{timestamp}.txt"

    with open(report_name, "w") as report:
        report.write(f"Reporte de escaneo – CyberScanner\n")
        report.write(f"Objetivo: {target_ip}\n")
        report.write(f"Rango: {start_port}-{end_port}\n")
        report.write(f"Fecha: {timestamp}\n\n")
        if open_ports:
            report.write("Puertos abiertos detectados:\n")
            for p in open_ports:
                report.write(f"- Puerto {p}\n")
        else:
            report.write("No se detectaron puertos abiertos.\n")

    print(f"\n📄 Reporte generado: {report_name}")
    print("✨ Escaneo finalizado.")

if __name__ == "__main__":
    run_scan()
