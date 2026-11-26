"""Entry program for the make.fun "Roast the Smart Fridge: One Line, Best Laugh Wins" bounty.

It writes a single roasting line about a smart fridge to entry.txt
inside the output directory make.fun hands it through
MAKEFUN_OUTPUT_DIR.
"""

import os

ENTRY = "My smart fridge judges my 2am snacks, orders kale I never asked for, and still can\u2019t find the butter sitting right in front of it."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

if __name__ == "__main__":
    main()
