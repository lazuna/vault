#!/usr/bin/env python3
import os

BASE_DIR = "vault"

folders = [
    "knowledge/tools",
    "knowledge/learning-paths",
    "growth",
    "projects/recon-lab",
]

files_content = {
    "knowledge/tools/recon-tools.md": """# Recon Tools

 Subdomains Recon

- [Amass](https://github.com/OWASP/Amass)
- [subfinder](https://github.com/projectdiscovery/subfinder)
- [assetfinder](https://github.com/tomnomnom/assetfinder)
- [dnsgen](https://github.com/ProjectAnte/dnsgen)
- [shuffledns](https://github.com/projectdiscovery/shuffledns)
- [httprobe](https://github.com/tomnomnom/httprobe)
- [aquatone](https://github.com/michenriksen/aquatone)
""",
    "knowledge/tools/enumeration-tools.md": """# Enumeration / Crawling Tools

- [nmap](https://nmap.org/download.html)
- [ffuf](https://github.com/ffuf/ffuf)
- [hakrawler](https://github.com/hakluke/hakrawler)
- [gau](https://github.com/lc/gau)
- [paramspider](https://github.com/devanshbatham/ParamSpider)
- [arjun](https://github.com/s0md3v/Arjun)
- [parameth](https://github.com/maK-/parameth)
""",
    "knowledge/tools/manual-recon-tools.md": """# Manual Recon Tools / Sources

- [Shodan](https://www.shodan.io/)
- [Censys](https://censys.io/)
- [Google Dorks](https://www.google.com)
- [Pastebin](https://pastebin.com/)
- [GitHub](https://github.com)
""",
    "knowledge/tools/xss-tools.md": """# XSS Tools

- [XSSHunter](https://xsshunter.com)
- [xsscrapy](https://github.com/DanMcInerney/xsscrapy)
- [Dalfox](https://github.com/hahwul/dalfox)
""",
    "knowledge/tools/sql-injection-tools.md": """# SQL Injection Tools

- [SQLMap](https://github.com/sqlmapproject/sqlmap)
- [waybackSQLiScanner](https://github.com/ghostlulzhacks/waybackSqliScanner)
""",
    "knowledge/learning-paths/offensive-recon.md": """# Offensive Recon & Testing Learning Path

 Stage 1: Subdomain and Asset Discovery

1. Amass
2. subfinder
3. assetfinder
4. dnsgen
5. shuffledns
6. httprobe
7. aquatone

 Stage 2: Enumeration / Crawling

1. nmap
2. ffuf
3. hakrawler
4. gau
5. paramspider
6. arjun
7. parameth

 Stage 3: Manual Recon

1. Shodan
2. Censys
3. Google Dorks
4. Pastebin
5. GitHub

 Stage 4: Testing

# XSS Testing

1. XSSHunter
2. xsscrapy
3. Dalfox

# SQL Injection Testing

1. SQLMap
2. waybackSQLiScanner
""",
    "growth/learning-progress.md": """# Learning Progress - Offensive Recon Tools

| Tool                 | Status         | Notes                      |
|----------------------|----------------|---------------------------|
| Amass                | Not Started    |                           |
| subfinder            | In Progress    |                           |
| SQLMap               | Practiced      |                           |
| XSSHunter            | Not Started    |                           |
| ...                  |                |                           |
""",
    "projects/recon-lab/README.md": """# Recon Lab Project

Experimental scripts and workflows to orchestrate offensive recon tooling.

Possible ideas:

- Subdomain -> asset -> alive hosts -> JS crawl -> param discovery -> template scan -> report.
- Combining Amass + shuffledns + httprobe + nuclei.
""",
    "vault/tools_recon_plan.md": """# Recon & Offensive Tooling - Vault Index

This document tracks the tools and learning path used for structured offensive recon and attack surface enumeration.

 Tool Categories

- [Recon Tools](knowledge/tools/recon-tools.md)
- [Enumeration / Crawling Tools](knowledge/tools/enumeration-tools.md)
- [Manual Recon Tools](knowledge/tools/manual-recon-tools.md)
- [XSS Tools](knowledge/tools/xss-tools.md)
- [SQL Injection Tools](knowledge/tools/sql-injection-tools.md)

 Learning Path

- [Offensive Recon Path](knowledge/learning-paths/offensive-recon.md)

 Progress Tracker

- [Learning Progress](growth/learning-progress.md)

 Experimental Projects

- [Recon Lab Project](projects/recon-lab/README.md)
""",
}


def main():
    for folder in folders:
        os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)

    for file_path, content in files_content.items():
        full_path = os.path.join(BASE_DIR, file_path)
        if not os.path.exists(full_path):
            with open(full_path, "w") as f:
                f.write(content)
            print(f"Created {full_path}")
        else:
            print(f"Skipped (exists): {full_path}")

    print("Vault recon scaffold complete.")


if __name__ == "__main__":
    main()
