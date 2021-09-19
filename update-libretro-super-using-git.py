#!/usr/bin/python3 -B

# Updates the libretro-super repository using git.

# --- Python standard library
import os

# --- Import custom modules
import common

# --- main ---------------------------------------------------------------------------------------
lrsuper_repo_path = 'libretro-super'
common.run(['git', '-C', lrsuper_repo_path, 'pull', 'origin'])
