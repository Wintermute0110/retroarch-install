#!/usr/bin/python3 -B

# Clones the Dolphin repository. It is required to install necessary runtime files
# into the retroarch system dir to execute the dolphin core.
# https://libretro.readthedocs.io/en/latest/library/dolphin/

import os
import common

# --- main ---------------------------------------------------------------------------------------
common.run(['git', 'clone', '--depth=1', 'https://github.com/libretro/dolphin.git'])
