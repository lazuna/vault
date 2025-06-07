#!/usr/bin/env python3
"""
Recon Chain Orchestrator - Python Version

Usage: python3 recon_chain.py domains.txt
"""

import sys
import subprocess
import os
from datetime import datetime

def run_command(cmd, out_file=None):
    print(f">>> Running: {cmd}")
    with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
        stdout, stderr = proc.communicate()
        if out_file:
            with open(out_file, 'w') as f:
                f.write(stdout)
        if stderr:
            print(f"[WARN] {stderr.strip()}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 recon_chain.py domains.txt")
        sys.exit(1)

    input_domains = sys.argv[1]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outdir = f"results/{timestamp}"
    os.makedirs(outdir, exist_ok=True)

    print(f">>> Output dir: {outdir}")

    # Subfinder
    run_command(f"subfinder -dL {input_domains} -silent", out_file=f"{outdir}/subfinder.txt")

    # httprobe
    run_command(f"cat {outdir}/subfinder.txt | httprobe", out_file=f"{outdir}/alive.txt")

    # nuclei
    run_command(f"nuclei -l {outdir}/alive.txt -o {outdir}/nuclei_results.txt")

    print(f">>> Recon chain complete. Results in {outdir}/")

if __name__ == "__main__":
    main()
