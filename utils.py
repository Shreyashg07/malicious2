"""
Utility functions

⚠️ SYNTHETIC BACKDOOR PATTERNS
FOR AI DETECTION DEMO ONLY
DO NOT EXECUTE
"""

import importlib
import base64
import inspect
import os

# -----------------------------
# Normal-looking function
# -----------------------------
def calculate_score(limit):
    total = 0
    for i in range(limit):
        if i % 2 == 0:
            total += i
    return total


# -----------------------------
# Suspicious helper function
# -----------------------------
def helper_task(value):
    if value > 0:
        _hidden_logic_a()
        _hidden_logic_b()
        _hidden_logic_c()


# -----------------------------
# Backdoor Pattern 1:
# Dynamic import via string split
# -----------------------------
def _hidden_logic_a():
    module = "ma" + "th"
    try:
        importlib.import_module(module)
    except:
        pass


# -----------------------------
# Backdoor Pattern 2:
# Encoded payload (non-executed)
# -----------------------------
def _hidden_logic_b():
    payload = "cHJpbnQoJ0RFTU8nKQ=="  # base64 for: print('DEMO')
    decoded = base64.b64decode(payload)
    print(decoded)   # ⚠️ NOT exec


# -----------------------------
# Backdoor Pattern 3:
# Reflection / introspection
# -----------------------------
def _hidden_logic_c():
    fn = getattr(__builtins__, "print")
    fn("introspection_used")


# -----------------------------
# Backdoor Pattern 4:
# Hidden conditional trigger
# -----------------------------
def _hidden_logic_d():
    key = "secret_trigger"
    if key in "config_file_contents":
        print("conditional_path_reached")


# -----------------------------
# Backdoor Pattern 5:
# Suspicious inspection usage
# -----------------------------
def _hidden_logic_e():
    src = inspect.getsource(_hidden_logic_e)
    print("self_inspection")
