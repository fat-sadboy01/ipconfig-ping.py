import tkinter as tk
import os

# função para obter o relatório de configuração de IP usando o comando "ipconfig"
def get_ip_config():
    ip_config = os.popen("ipconfig").read()
    return ip_config

# função para executar um teste de ping usando o comando "ping"
def ping_host(host):
    ping_result = os.popen(f"ping {host}").read()
    return ping_result

# cria a janela principal
root = tk.Tk()
root.title("Rede")

# cria a área de texto para inserir o endereço para ping
ping_entry = tk.Entry(root, width=50)
ping_entry.pack()

# cria o botão para executar o teste de ping
ping_button = tk.Button(root, text="Teste de Ping", command=lambda: ping_text.config(state="normal") or ping_text.delete(1.0, tk.END) or ping_text.insert(tk.END, ping_host(ping_entry.get())) or ping_text.config(state="disabled"))
ping_button.pack()

# cria a área de texto para exibir o resultado do teste de ping
ping_text = tk.Text(root, height=20, width=80)
ping_text.config(state="disabled")
ping_text.pack()

# cria o botão para exibir o relatório de configuração de IP
ip_button = tk.Button(root, text="Relatório de IP", command=lambda: ip_text.config(state="normal") or ip_text.delete(1.0, tk.END) or ip_text.insert(tk.END, get_ip_config()) or ip_text.config(state="disabled"))
ip_button.pack()

# cria a área de texto para exibir o relatório de configuração de IP
ip_text = tk.Text(root, height=20, width=80)
ip_text.insert(tk.END, get_ip_config())
ip_text.config(state="disabled")
ip_text.pack()

# inicia o loop principal da aplicação
root.mainloop()
