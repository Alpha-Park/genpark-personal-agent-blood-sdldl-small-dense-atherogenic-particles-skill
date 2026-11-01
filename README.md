# genpark-personal-agent-blood-sdldl-small-dense-atherogenic-particles-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

Small dense LDL (sdLDL-C) and LDL particle number (LDL-P) vs ApoB atherogenic particle discordance auditor.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `audit_sdldl_atherogenic_discordance`
- **Category**: `personal_agent`

### Method Documentation
Audit atherogenic cardiovascular particle burden using small dense LDL cholesterol (sdLDL-C, mg/dL) and Apolipoprotein B (ApoB, mg/dL).
sdLDL particles easily penetrate arterial endothelium and have high proteoglycan binding affinity, driving foam cell formation.
Identifies discordance where standard LDL-C appears 'normal' but sdLDL and particle counts are dangerously elevated.

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "audit_sdldl_atherogenic_discordance",
    "arguments": {
    "sdldl_c_mg_dl": 38.0,
    "standard_ldl_c_mg_dl": 95.0,
    "apob_mg_dl": 98.0,
    "triglycerides_mg_dl": 185
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
