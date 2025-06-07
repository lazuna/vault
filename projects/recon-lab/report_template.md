# Recon Run Report

 Run Metadata

- Date: {{date}}
- Target domains: {{domains}}
- Recon Operator: {{operator}}

 Summary

| Stage               | Result Summary |
|---------------------|----------------|
| Subdomain Discovery | X domains found |
| Alive Hosts         | Y hosts alive   |
| Nuclei Findings     | Z issues found  |
| Manual Recon        | In Progress / Completed |

 Detailed Findings

# Subdomain Discovery

- Results: `results/{{run_id}}/subfinder.txt`

# Alive Hosts

- Results: `results/{{run_id}}/alive.txt`

# Nuclei Scan

- Results: `results/{{run_id}}/nuclei_results.txt`
- Key findings:
    - [ ] High
    - [ ] Medium
    - [ ] Low

# Manual Recon Notes

- OSINT Sources:
    - Shodan:
    - Censys:
    - GitHub:
    - Pastebin:

# Recommendations

- TBD based on findings

 Next Steps

- Run extended scan
- Add nuclei templates
- Investigate manual findings
