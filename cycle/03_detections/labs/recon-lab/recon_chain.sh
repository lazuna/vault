#!/bin/bash
# Recon Chain Script
# Usage: ./recon_chain.sh domains.txt

set -euo pipefail
INPUT_DOMAINS="$1"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
OUTDIR="results/${TIMESTAMP}"
mkdir -p "${OUTDIR}"

echo ">>> Running subfinder..."
subfinder -dL "$INPUT_DOMAINS" -silent -o "${OUTDIR}/subfinder.txt"

echo ">>> Running shuffledns (resolvers required)..."
# Example assumes resolvers.txt exists
# shuffledns -dL "$INPUT_DOMAINS" -list "${OUTDIR}/subfinder.txt" -r resolvers.txt -o "${OUTDIR}/shuffledns.txt"

echo ">>> Probing alive hosts..."
cat "${OUTDIR}/subfinder.txt" | httprobe > "${OUTDIR}/alive.txt"

echo ">>> Running nuclei scan..."
nuclei -l "${OUTDIR}/alive.txt" -o "${OUTDIR}/nuclei_results.txt"

echo ">>> Recon chain complete. Results in ${OUTDIR}/"
You can add additional steps (gau, hakrawler, arjun, paramspider).
results/ folder will be created per run — timestamped.
