import socket
import sys
import argparse
import termcolor

# Função que realiza a varredura de portas em um host
def scan_ports(host, start_port, end_port):
    # Loop que itera sobre as portas especificadas
    for port in range(start_port, end_port + 1):
        try:
            # Cria um objeto socket para a conexão
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Define o tempo limite de conexão
            s.settimeout(0.1)
            # Tenta se conectar à porta especificada
            result = s.connect_ex((host, port))
            # Se a conexão for bem-sucedida, a porta está aberta
            if result == 0:
                print(termcolor.colored("[+] Porta {} aberta".format(port), "green"))
            # Fecha o objeto socket
            s.close()
        except KeyboardInterrupt:
            # Se o usuário pressionar Ctrl+C, encerra o programa
            print("\nPrograma encerrado pelo usuário.")
            sys.exit()
        except:
            # Se ocorrer um erro, continua para a próxima porta
            pass

# Função principal do programa
def main():
    # Define e parseia os argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Varredura de portas em um host")
    parser.add_argument("host", help="Endereço IP do host a ser verificado")
    parser.add_argument("--start", type=int, default=1, help="Número da primeira porta a ser verificada (padrão: 1)")
    parser.add_argument("--end", type=int, default=65535, help="Número da última porta a ser verificada (padrão: 65535)")
    args = parser.parse_args()

    # Executa a varredura de portas no host especificado
    print(termcolor.colored("[*] Iniciando varredura de portas em {}...".format(args.host), "yellow"))
    scan_ports(args.host, args.start, args.end)

# Executa a função principal do programa
if __name__ == "__main__":
    main()

