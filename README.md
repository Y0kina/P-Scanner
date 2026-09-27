<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=00F7FF&center=true&vCenter=true&width=800&lines=P-Scanner+%F0%9F%94%8D;Mini+Port+Scanner+in+Python;Made+for+learning+%26+breaking+things+%E2%9A%A1" alt="Typing SVG" />

<br>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow?style=for-the-badge)
![Made with](https://img.shields.io/badge/Made%20with-%E2%98%95%20%26%20curiosity-orange?style=for-the-badge)

</div>

---

## 🛡️ What is P-Scanner?

**P-Scanner** is a lightweight TCP port scanner built from scratch in Python — no external libraries, just the standard `socket` module. It scans a range of ports on a target host, detects which ones are open, tries to grab the service banner, and saves a clean report.

Built as a learning project to understand what tools like **Nmap** actually do under the hood, one socket connection at a time.

> ⚠️ **Disclaimer:** Only scan hosts you own or have explicit permission to test. Unauthorized scanning may be illegal in your country!

---

## ✨ Features

- 🔎 Scans any port range on a target IP or hostname
- 🏷️ Grabs service banners from open ports when available
- 💾 Exports results to a `.txt` report automatically
- ⏱️ Configurable connection timeout to keep scans fast
- 🧠 Fully commented code — built as a hands-on learning project

---

## 🚀 Demo

```
$ python scanner.py

IP address or hostname to scan (e.g. 127.0.0.1): 127.0.0.1
Start port: 20
End port: 90

Starting scan on 127.0.0.1 — 2026-09-27 18:29:19
Ports tested: 20 to 90

[+] Port 22 OPEN — SSH-2.0-OpenSSH_9.6
[+] Port 80 OPEN — No banner available

Scan complete. 2 open port(s) found.
Results saved to 'scan_results.txt'
```

---

## 🛠️ Installation

```bash
# Clone the repo
git clone https://github.com/Y0kina/P-Scanner.git
cd P-Scanner

# No external dependencies — pure Python standard library
python3 scanner.py
```

**Requirements:** Python 3.8+

---

## ▶️ Usage

Run the script and follow the prompts:

```bash
python3 scanner.py
```

You'll be asked for:
1. A target IP address or hostname
2. The starting port of the range
3. The ending port of the range

Results are printed live and saved to `resultats_scan.txt` in the same folder.

---

## 🗺️ Roadmap

- [ ] Add a database of well-known ports (22 → SSH, 80 → HTTP, 443 → HTTPS...)
- [ ] Multi-threading for faster scans
- [ ] CLI arguments with `argparse` (`python scanner.py 192.168.1.1 -p 1-1000`)
- [ ] Export results to CSV / JSON
- [ ] Optional simple GUI

---

## 🧰 Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Sockets](https://img.shields.io/badge/Sockets-TCP%2FIP-4479A1?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

---

## 📫 Contact

<div align="center">

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ahmed.alaabqary08@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Y0kina)

</div>

<div align="center">

*"Break it to understand it, build it to protect it."* ⚡

</div>
