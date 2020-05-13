#!/usr/bin/python3 -B

# Compiles Retroarch.

# --- Python standard library --------------------------------------------------------------------
import os

# --- Import custom modules ----------------------------------------------------------------------
import common

# --- main ---------------------------------------------------------------------------------------
configuration = common.read_config_file('configuration.xml')
if configuration['Version'] == 'master':
    retroarch_version = 'master'
else:
    retroarch_version = 'tags/v{}'.format(configuration['Version'])
print('>>> retroarch_version "{}"'.format(retroarch_version))
current_dir = os.getcwd()
print('>>> Current Working Directory "{}"'.format(current_dir))

# Switch source code to requested tag
print('>>> Checking out Retroarch tag {}'.format(retroarch_version))
os.chdir('libretro-super/retroarch')
# common.run_command(['git', 'checkout', 'master'])
common.run_command(['git', 'checkout', retroarch_version])
os.chdir(current_dir)

print('>>> Bulding Retroarch...')
os.chdir('libretro-super')
common.run_command(['./retroarch-build.sh'])
os.chdir(current_dir)
