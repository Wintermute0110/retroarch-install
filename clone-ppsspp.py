#!/usr/bin/python3 -B

# Clones the PPSSPP repository. It is required to install necessary runtime files
# into the retroarch system dir to execute the ppsspp core.
# https://docs.libretro.com/library/ppsspp/

import os
import common

# --- main ---------------------------------------------------------------------------------------
# https://www.perforce.com/blog/vcs/git-beyond-basics-using-shallow-clones
common.run(['git', 'clone', '--depth=1', 'https://github.com/hrydgard/ppsspp.git'])
