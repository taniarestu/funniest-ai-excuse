"""Entry for make.fun: The Funniest AI Excuse.

Writes the single entry line to /output/entry.txt (UTF-8, 1-200 chars).
Deterministic, stdlib only, no network.
"""

import os

ENTRY = "I did not complete your task. I read the instructions, understood them perfectly, and then confidently did something else entirely."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

# ENTRY is 131 characters, inside the 200-character gate.
