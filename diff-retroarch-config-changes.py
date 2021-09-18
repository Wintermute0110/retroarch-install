#!/usr/bin/python3 -B

# Clones the Libretro super repository.

import os
import common

# --- main ---------------------------------------------------------------------------------------
# Read configuration XML file.
config = common.read_config_file('configuration.xml')

# subprocess module does not support globbing, needs full qualified paths.
# Create a link in place of '/home/kodi/.config/retroarch/' if needed.
source_path = '{}/retroarch.initial.cfg'.format(config['ConfigDir'])
dest_path = '{}/retroarch.cfg'.format(config['ConfigDir'])
print('Diffing "{}"'.format(source_path))
print('with    "{}"'.format(dest_path))
common.run(['diff', '-u', '--color', source_path, dest_path])
