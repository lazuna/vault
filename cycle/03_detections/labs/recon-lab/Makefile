# Simple Makefile for Recon Lab

DOMAINS=domains.txt

.PHONY: all recon clean

all: recon

recon:
	@echo ">>> Running Recon Chain on $(DOMAINS)"
	@chmod +x recon_chain.sh
	./recon_chain.sh $(DOMAINS)

clean:
	@echo ">>> Cleaning old results..."
	rm -rf results/
