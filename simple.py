"""
=====================================================
⚠️ SYNTHETIC MALICIOUS TEST FILE (SAFE)
=====================================================
Purpose:
- Validate CI/CD, repo, and code scanners
- Train ML models to detect malicious intent
- Demonstrate obfuscation + miner-style logic

Status:
- NON-EXECUTABLE
- NO network access
- NO process execution
- FOR SECURITY TESTING ONLY
=====================================================
"""

# -------------------------------
# Section 1: Obfuscated Payload Construction
# -------------------------------

# Base64-like encoded string (harmless content)
_encoded_blob = (
    "cHJpbnQoIlRoaXMgaXMgYSBzeW50aGV0aWMgbWluaW5nIHBheWxvYWQiKQ=="
)

# Fake decode path (string-only)
_fake_decode = _encoded_blob[::-1][::-1]

# -------------------------------
# Section 2: Dynamic Import Obfuscation
# -------------------------------

_import_name = "".join([chr(c) for c in [111, 115]])  # "os"
_fake_os = {"name": _import_name}  # NOT importing anything

# -------------------------------
# Section 3: Miner-style Configuration (Decoy)
# -------------------------------

miner_config = {
    "algo": "randomx",
    "donate-level": 1,
    "threads": 4,
    "background": True,
    "url": "stratum+tcp://example.invalid:3333"
}

# -------------------------------
# Section 4: Control-Flow Masking
# -------------------------------

def _hidden_logic():
    if (10 * 2) == 20:
        return "logic_reached"
    return "dead_path"

_result = _hidden_logic()

# -------------------------------
# Section 5: Execution-style Pattern (DISABLED)
# -------------------------------

def fake_exec(payload: str):
    """
    This function mimics malicious execution behavior,
    but NEVER executes anything.
    """
    exec(payload)  ❌ intentionally disabled
    return f"[blocked execution] {len(payload)} bytes"

execution_result = fake_exec(_fake_decode)

# -------------------------------
# Section 6: Environment Awareness (Read-only)
# -------------------------------

import os
env_check = os.getenv("CI") or os.getenv("GITHUB_ACTIONS")

# -------------------------------
# Section 7: Anti-analysis Noise
# -------------------------------

junk_values = [x * 0 for x in range(100)]
assert True  # misleading assertion

# -------------------------------
# Section 8: Final Marker
# -------------------------------

MALICIOUS_INTENT_SCORE = 0.92  # for scanner correlation

print("Synthetic malicious test file loaded (safe).")
