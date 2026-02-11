#==================================================================
# PyAI_v1\utils\logger.py - ETI Patagonia - prof.martintorres@educ.ar
#==================================================================

import datetime

def log(msg):
    print(f"[{datetime.datetime.now().isoformat()}] {msg}")
