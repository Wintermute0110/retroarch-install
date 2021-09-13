#!/usr/bin/python3 -B

# Clones the Libretro super repository.

import os
import common

# --- main ---------------------------------------------------------------------------------------
common.run_command(['git', 'clone', 'https://github.com/libretro/libretro-super.git'])
