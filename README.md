
## What is PowerHell?

PowerHell is a Python-based PowerShell payload generator built for penetration testers and red teamers. It generates reverse shell payloads, obfuscates them through multiple encoding/encryption methods, and includes an interactive listener — all from one CLI.

No GUI. No bloat. Just clean, fast payloads.

**PowerShell payload generator, obfuscator, and AV bypass tool for red teamers.**

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-GPL%20v3-green?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## Features

| Feature | Status |
|---|---|
| Reverse shell payload generation | ✅ |
| Base64 obfuscation | ✅ |
| XOR obfuscation | ✅ |
| Random string obfuscation | ✅ |
| No obfuscation (raw) | ✅ |
| Interactive listener with autocomplete | ✅ *(experimental)* |
| Shellcode payload generation | 🔜 *(planned)* |

---

## Installation

```bash
git clone https://github.com/vibebhavv/Powerhell
cd Powerhell
pip3 install -r requirements.txt
```

---

## Usage

```
python3 main.py [-h] [-l HOST] [-p PORT] [-o FILE] [-obf METHOD] [-payload TYPE] [-s]
```

### Arguments

| Flag | Description | Default |
|---|---|---|
| `-l`, `--listen` | Host to bind/connect back to | `0.0.0.0` |
| `-p`, `--port` | Port number | `4444` |
| `-o`, `--output` | Output file path for generated payload | — |
| `-obf`, `--obfuscation` | Obfuscation method: `none`, `base64`, `xor`, `random` | `none` |
| `-payload`, `--payload` | Payload type: `reverseshell`, `shellcode` | `reverseshell` |
| `-s`, `--start-listener` | Start the interactive listener immediately | — |

---

## Examples

**Generate a raw reverse shell:**
```bash
python3 main.py -l 192.168.1.10 -p 4444 -o shell.ps1
```

**Generate a base64-obfuscated payload:**
```bash
python3 main.py -l 192.168.1.10 -p 4444 -obf base64 -o shell_b64.ps1
```

**Generate an XOR-obfuscated payload:**
```bash
python3 main.py -l 192.168.1.10 -p 4444 -obf xor -o shell_xor.ps1
```

**Generate with random string obfuscation:**
```bash
python3 main.py -l 192.168.1.10 -p 4444 -obf random -o shell_rand.ps1
```

**Start the interactive listener directly:**
```bash
python3 main.py -s -l 0.0.0.0 -p 4444
```

**Generate payload and then start listener in one shot:**
```bash
python3 main.py -l 192.168.1.10 -p 4444 -obf base64 -o shell.ps1
# After generation, it'll prompt: "Do you want to start the listener now? (y/N)"
```

---

## Project Structure

```
Powerhell/
├── main.py               # Entry point, argument parsing, flow control
├── requirements.txt      # Python dependencies
├── modules/
│   ├── listener.py       # Interactive reverse shell listener
│   ├── obf.py            # Obfuscation engine (base64, xor, random)
│   └── payloads/
│       └── rvs.txt       # Reverse shell payload template
└── LICENSE
```

---

## Obfuscation Methods

| Method | Description |
|---|---|
| `none` | Raw PowerShell payload, no encoding |
| `base64` | Encodes the payload in Base64, decoded at runtime |
| `xor` | XOR-encrypts the payload bytes |
| `random` / `randomstring` | Randomizes variable names and string patterns to break static signatures |

---

## Disclaimer

> PowerHell is intended for **authorized penetration testing and security research only**.
> Using this tool against systems you do not have explicit permission to test is illegal.
> The author is not responsible for any misuse or damage caused by this tool.

---

## License

Distributed under the **GNU General Public License v3.0**.
See [`LICENSE`](./LICENSE) for full terms.

---

## Author

**vibebhavv** — [github.com/vibebhavv](https://github.com/vibebhavv)
