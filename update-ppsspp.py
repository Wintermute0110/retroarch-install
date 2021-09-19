#!/usr/bin/python3 -B

# Updates the PPSSPP repository. It is required to install necessary runtime files
# into the retroarch system dir to execute the ppsspp core.

# --- Python standard library --------------------------------------------------------------------
import os

# --- Import custom modules ----------------------------------------------------------------------
import common

# --- main ---------------------------------------------------------------------------------------
current_dir = os.getcwd()
print('>>> Current Working Directory "{}"'.format(current_dir))
os.chdir('ppsspp')
print('>>> Updating ppsspp repository with git...')
common.run(['git', 'pull', 'origin'])
os.chdir(current_dir)
