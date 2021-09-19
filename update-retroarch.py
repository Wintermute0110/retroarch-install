#!/usr/bin/python3 -B

# Updates the libretro-super repository using git.

# --- Python standard library
import os

# --- Import custom modules
import common

# --- main ---------------------------------------------------------------------------------------
# Make sure Retroarch repo is in master branch.
print('*** Changing Retroarch branch to master')
retroarch_path = 'libretro-super/retroarch'
common.run(['git', '-C', retroarch_path, 'checkout', 'master'])

# Update Retroarch and submodule repositories.
print('*** Calling libretro-fetch.sh')
lrsuper_repo_path = 'libretro-super'
os.chdir(lrsuper_repo_path)
common.run(['bash', 'libretro-fetch.sh'])
