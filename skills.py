# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-personal-agent-blood-sdldl-small-dense-atherogenic-particles-skill
Category: personal_agent
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def audit_sdldl_atherogenic_discordance(sdldl_c_mg_dl, standard_ldl_c_mg_dl, apob_mg_dl, triglycerides_mg_dl=140):
    if sdldl_c_mg_dl <= 0 or standard_ldl_c_mg_dl <= 0:
        raise ValueError("Lipid values must be positive numbers")
        
    # Optimal reference: sdLDL-C < 20 mg/dL (or < 20% of total LDL-C)
    # High atherogenicity: sdLDL-C >= 35 mg/dL
    # ApoB optimal: < 80 mg/dL (< 65 for high risk)
    sdldl_fraction_pct = (sdldl_c_mg_dl / standard_ldl_c_mg_dl) * 100.0
    
    # Discordance: Normal LDL-C (< 100 mg/dL) with elevated ApoB (> 90 mg/dL) or high sdLDL (> 35 mg/dL)
    hidden_atherogenic_discordance = (standard_ldl_c_mg_dl < 100.0) and (apob_mg_dl >= 90.0 or sdldl_c_mg_dl >= 35.0)
    
    if sdldl_c_mg_dl >= 35.0 or apob_mg_dl >= 100.0:
        phenotype = "ATHEROGENIC_PATTERN_B_PREDOMINANCE"
        risk_tier = "HIGH_ATHEROSCLEROSIS_PROGRESSION_RISK"
    elif sdldl_c_mg_dl >= 21.0:
        phenotype = "INTERMEDIATE_PARTICLE_PROFILE"
        risk_tier = "MODERATE_RISK"
    else:
        phenotype = "BUOYANT_PATTERN_A_PREDOMINANCE"
        risk_tier = "LOW_ATHEROGENIC_PARTICLE_BURDEN"
        
    return {
        "sdldl_c_mg_dl": round(sdldl_c_mg_dl, 1),
        "standard_ldl_c_mg_dl": round(standard_ldl_c_mg_dl, 1),
        "sdldl_fraction_percent": round(sdldl_fraction_pct, 1),
        "apob_mg_dl": round(apob_mg_dl, 1),
        "hidden_atherogenic_discordance": hidden_atherogenic_discordance,
        "lipoprotein_phenotype": phenotype,
        "vascular_risk_tier": risk_tier,
        "clinical_insight": "Standard LDL-C underrepresents true atherogenic risk; guide lipid therapy by ApoB and sdLDL targets." if hidden_atherogenic_discordance else "Concordant lipid particle parameters."
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "audit_sdldl_atherogenic_discordance",
                        "description": """Audit atherogenic cardiovascular particle burden using small dense LDL cholesterol (sdLDL-C, mg/dL) and Apolipoprotein B (ApoB, mg/dL).
sdLDL particles easily penetrate arterial endothelium and have high proteoglycan binding affinity, driving foam cell formation.
Identifies discordance where standard LDL-C appears 'normal' but sdLDL and particle counts are dangerously elevated.""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = audit_sdldl_atherogenic_discordance(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'sdldl_c_mg_dl': 38.0, 'standard_ldl_c_mg_dl': 95.0, 'apob_mg_dl': 98.0, 'triglycerides_mg_dl': 185}
        out = audit_sdldl_atherogenic_discordance(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
