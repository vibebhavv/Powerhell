import re
import base64
import random
import string

def xor_string(s, key=0x42):
    return ''.join(f'{chr(ord(c) ^ key):x}' for c in s)

def obfuscate_vars_base64(script):
    vars_found = set(re.findall(r'\$(var\d+)', script))
    mapping = {var: '$' + base64.b64encode(var.encode()).decode().replace('=', '') for var in vars_found}
    for orig, obf in mapping.items():
        script = script.replace(f'${orig}', obf)
    return script

def obfuscate_vars_xor(script, key=0x42):
    vars_found = set(re.findall(r'\$(var\d+)', script))
    mapping = {var: '$' + ''.join(f'{ord(c) ^ key:02x}' for c in var) for var in vars_found}
    for orig, obf in mapping.items():
        script = script.replace(f'${orig}', obf)
    return script

def obfuscate_vars_random(script, length=10):
    vars_found = set(re.findall(r'\$(var\d+)', script))
    def random_str():
        return ''.join(random.choices(string.ascii_letters, k=length))
    mapping = {var: '$' + random_str() for var in vars_found}
    for orig, obf in mapping.items():
        script = script.replace(f'${orig}', obf)
    return script

def obfuscate_reverse_shell(method, input_file='modules/payloads/rvs.txt', output_file=None):
    with open(input_file, 'r') as f:
        script = f.read()
    if method == 'base64':
        obf_script = obfuscate_vars_base64(script)
    elif method == 'xor':
        obf_script = obfuscate_vars_xor(script)
    elif method == 'random' or method == 'randomstring' or method == 'random-string':
        obf_script = obfuscate_vars_random(script)
    else:
        raise ValueError('Unknown obfuscation method')
    if output_file:
        with open(output_file, 'w') as f:
            f.write(obf_script)
    return obf_script
