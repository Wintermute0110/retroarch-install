#!/usr/bin/python3 -B

# Clones the Libretro super repository.

import os
import common

# --- main ---------------------------------------------------------------------------------------
retroarch_source_dir = 'libretro-super/retroarch'
common.run_command(['git', '-C', retroarch_source_dir, 'tag'])
