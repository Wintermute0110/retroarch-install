#!/usr/bin/python3 -B

# Clones the PPSSPP repository. It is required to install necessary runtime files
# into the retroarch system dir to execute the ppsspp core.
# https://docs.libretro.com/library/ppsspp/

# --- Python standard library --------------------------------------------------------------------
import os

# --- Import custom modules ----------------------------------------------------------------------
import common

# --- main ---------------------------------------------------------------------------------------
# https://www.perforce.com/blog/vcs/git-beyond-basics-using-shallow-clones
common.run_command(['git', 'clone', '--depth=1', 'https://github.com/hrydgard/ppsspp.git'])
