#!/usr/bin/python3 -B

# Clones the Libretro super repository.

import os
import common

# --- main ---------------------------------------------------------------------------------------
# Read configuration XML file.
config = common.read_config_file('configuration.xml')

# subprocess module does not support globbing, needs full qualified paths.
# Create a link in place of '/home/kodi/.config/retroarch/' if needed.
source_path = '{}/.config/retroarch/retroarch.initial.cfg'.format(config['HomeDir'])
dest_path = '{}/.config/retroarch/retroarch.cfg'.format(config['HomeDir'])
common.run_command(['diff', '-u', '--color', source_path, dest_path])
