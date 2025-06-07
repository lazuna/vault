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
    "knowledge/tools/recon-tools.md": "# Recon Tools\n\n Subdomains Recon\n\n- [Amass](https://github.com/OWASP/Amass)\n- [subfinder](https://github.com/projectdiscovery/subfinder)\n- [assetfinder](https://github.com/tomnomnom/assetfinder)\n- [dnsgen](https://github.com/ProjectAnte/dnsgen)\n- [shuffledns](https://github.com/projectdiscovery/shuffledns)\n- [httprobe](https://github.com/tomnomnom/httprobe)\n- [aquatone](https://github.com/michenriksen/aquatone)\n",
    "knowledge/tools/enumeration-tools.md": "# Enumeration / Crawling Tools\n\n- [nmap](https://nmap.org/download.html)\n- [ffuf](https://github.com/ffuf/ffuf)\n- [hakrawler](https://github.com/hakluke/hakrawler)\n- [gau](https://github.com/lc/gau)\n- [paramspider](https://github.com/devanshbatham/ParamSpider)\n- [arjun](https://github.com/s0md3v/Arjun)\n- [parameth](https://github.com/maK-/parameth)\n",
    "knowledge/tools/manual-recon-tools.md": "# Manual Recon Tools / Sources\n\n- [Shodan](https://www.shodan.io/)\n- [Censys](https://censys.io/)\n- [Google Dorks](https://www.google.com)\n- [Pastebin](https://pastebin.com/)\n- [GitHub](https://github.com)\n",
    "knowledge/tools/xss-tools.md": "# XSS Tools\n\n- [XSSHunter](https://xsshunter.com)\n- [xsscrapy](https://github.com/DanMcInerney/xsscrapy)\n- [Dalfox](https://github.com/hahwul/dalfox)\n",
    "knowledge/tools/sql-injection-tools.md": "# SQL Injection Tools\n\n- [SQLMap](https://github.com/sqlmapproject/sqlmap)\n- [waybackSQLiScanner](https://github.com/ghostlulzhacks/waybackSqliScanner)\n",
    "knowledge/learning-paths/offensive-recon.md": "# Offensive Recon & Testing Learning Path\n\n Stage 1: Subdomain and Asset Discovery\n\n1. Amass\n2. subfinder\n3. assetfinder\n4. dnsgen\n5. shuffledns\n6. httprobe\n7. aquatone\n\n Stage 2: Enumeration / Crawling\n\n1. nmap\n2. ffuf\n3. hakrawler\n4. gau\n5. paramspider\n6. arjun\n7. parameth\n\n Stage 3: Manual Recon\n\n1. Shodan\n2. Censys\n3. Google Dorks\n4. Pastebin\n5. GitHub\n\n Stage 4: Testing\n\n# XSS Testing\n\n1. XSSHunter\n2. xsscrapy\n3. Dalfox\n\n# SQL Injection Testing\n\n1. SQLMap\n2. waybackSQLiScanner\n",
    "growth/learning-progress.md": "# Learning Progress - Offensive Recon Tools\n\n| Tool                 | Status         | Notes                      |\n|----------------------|----------------|---------------------------|\n| Amass                | Not Started    |                           |\n| subfinder            | In Progress    |                           |\n| SQLMap               | Practiced      |                           |\n| XSSHunter            | Not Started    |                           |\n| ...                  |                |                           |\n",
    "projects/recon-lab/README.md": "# Recon Lab Project\n\nExperimental scripts and workflows to orchestrate offensive recon tooling.\n\nPossible ideas:\n\n- Subdomain -> asset -> alive hosts -> JS crawl -> param discovery -> template scan -> report.\n- Combining Amass + shuffledns + httprobe + nuclei.\n",
    "vault/tools_recon_plan.md": "# Recon & Offensive Tooling - Vault Index\n\nThis document tracks the tools and learning path used for structured offensive recon and attack surface enumeration.\n\n Tool Categories\n\n- [Recon Tools](knowledge/tools/recon-tools.md)\n- [Enumeration / Crawling Tools](knowledge/tools/enumeration-tools.md)\n- [Manual Recon Tools](knowledge/tools/manual-recon-tools.md)\n- [XSS Tools](knowledge/tools/xss-tools.md)\n- [SQL Injection Tools](knowledge/tools/sql-injection-tools.md)\n\n Learning Path\n\n- [Offensive Recon Path](knowledge/learning-paths/offensive-recon.md)\n\n Progress Tracker\n\n- [Learning Progress](growth/learning-progress.md)\n\n Experimental Projects\n\n- [Recon Lab Project](projects/recon-lab/README.md)\n"
}

# Execution
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
