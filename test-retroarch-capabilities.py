#!/usr/bin/python3 -B

# Clones the Libretro super repository.

# --- Python standard library
import os

# --- Import custom modules
import common

# --- main ---------------------------------------------------------------------------------------
common.run(['./libretro-super/retroarch/retroarch', '--features'])
