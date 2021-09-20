#!/usr/bin/python3 -B

# Clones the Dolphin repository. It is required to install necessary runtime files
# into the retroarch system dir to execute the dolphin core.
# https://libretro.readthedocs.io/en/latest/library/dolphin/

import os
import sys
import common

# --- main ---------------------------------------------------------------------------------------
conf = common.read_config_file('configuration.xml')

# Configure paths
RetroBinDir = conf['RetroBinDir']
LibRetroDir = conf['LibRetroDir']
ConfigDir = conf['ConfigDir']
RetroDataDir = conf['RetroDataDir']
print('*** RetroBinDir  "{}"'.format(RetroBinDir))
print('*** LibRetroDir  "{}"'.format(LibRetroDir))
print('*** ConfigDir    "{}"'.format(ConfigDir))
print('*** RetroDataDir "{}"'.format(RetroDataDir))

# --- Create main directories
print("Creating RetroArch binary directory...")
common.run(['mkdir', '-p', RetroBinDir])

print("Creating Libretro cores directory...")
common.run(['mkdir', '-p', LibRetroDir]) # Option libretro_directory

print("Creating RetroArch configuration directory...")
common.run(['mkdir', '-p', ConfigDir])

print("Creating RetroArch data directory...")
common.run(['mkdir', '-p', RetroDataDir])

# --- Create RetroArch paths
# See https://github.com/libretro/RetroArch/blob/master/fetch-submodules.sh
# Use same order as create-retroarch-default-config.py (alphabetical by configuration name).
RDD = RetroDataDir
print("Creating RetroArch stuff directories...")
common.run(['mkdir', '-p', '{}/assets/'.format(RDD)])             # Option assets_directory
common.run(['mkdir', '-p', '{}/audio_filters/'.format(RDD)])      # Option audio_filter_dir
common.run(['mkdir', '-p', '{}/cache/'.format(RDD)])              # Option cache_directory
common.run(['mkdir', '-p', '{}/libretrodb/cht/'.format(RDD)])     # Option cheat_database_path
common.run(['mkdir', '-p', '{}/libretrodb/rdb/'.format(RDD)])     # Option content_database_path
                                                                  # Option content_history_dir
common.run(['mkdir', '-p', '{}/downloads/'.format(RDD)])          # Option core_assets_directory
                                                                  # Option core_options_path
common.run(['mkdir', '-p', '{}/libretrodb/cursors/'.format(RDD)]) # Option cursor_directory
common.run(['mkdir', '-p', '{}/wallpapers/'.format(RDD)])         # Option dynamic_wallpapers_directory
common.run(['mkdir', '-p', '{}/input_remappings/'.format(RDD)])   # Option input_remapping_directory
common.run(['mkdir', '-p', '{}/joypad_autoconfig/'.format(RDD)])  # Option joypad_autoconfig_dir
common.run(['mkdir', '-p', '{}/info/'.format(RDD)])               # Option libretro_info_path
common.run(['mkdir', '-p', '{}/logs/'.format(RDD)])               # Option log_dir
common.run(['mkdir', '-p', '{}/overlays/'.format(RDD)])           # Option overlay_directory
common.run(['mkdir', '-p', '{}/playlists/'.format(RDD)])          # Option playlist_directory
common.run(['mkdir', '-p', '{}/recording_config/'.format(RDD)])   # Option recording_config_directory
common.run(['mkdir', '-p', '{}/recording_output/'.format(RDD)])   # Option recording_output_directory
common.run(['mkdir', '-p', '{}/resampler/'.format(RDD)])          # Option resampler_directory
                                                                  # Option rgui_browser_directory (ROMs path)
common.run(['mkdir', '-p', '{}/configurations/'.format(RDD)])     # Option rgui_config_directory
common.run(['mkdir', '-p', '{}/runtime_log/'.format(RDD)])        # Option runtime_log_directory
common.run(['mkdir', '-p', '{}/savefiles/'.format(RDD)])          # Option savefile_directory
common.run(['mkdir', '-p', '{}/savestates/'.format(RDD)])         # Option savestate_directory
common.run(['mkdir', '-p', '{}/screenshots/'.format(RDD)])        # Option screenshot_directory
common.run(['mkdir', '-p', '{}/shaders_cg/'.format(RDD)])         # Option shaders_cg
common.run(['mkdir', '-p', '{}/system/'.format(RDD)])             # Option system_directory
common.run(['mkdir', '-p', '{}/thumbnails/'.format(RDD)])         # Option thumbnails_directory
common.run(['mkdir', '-p', '{}/video_filters/'.format(RDD)])      # Option video_filter_dir
                                                                  # Option video_font_path

# --- Copy libretro cores
# Clean the currently installed cores before copying.
# NOTE Do not clean the cores because cores are downloaded with the online updater.
# echo "Cleaning old LibRetro cores..."
# rm -f ${PATH_LIBRETRO}/*.so
# echo "Installing LibRetro cores..."
# cp ./libretro-super/dist/unix/*.so ${PATH_LIBRETRO}

# --- Install Retroarch binary
# Based on Lakka retroarch installation script
# Have a look at https://github.com/libretro/Lakka/blob/lakka/packages/libretro/retroarch/package.mk
print("Installing Retroarch binary...")
source_file, dest_dir = './libretro-super/retroarch/retroarch', RetroBinDir
# print('cp "{}" -> "{}"'.format(source_file, dest_dir))
common.run(['mkdir', '-p', dest_dir])
common.run(['cp', '-p', source_file, dest_dir])

# --- Copy core INFO files
print("rsync LibRetro core info files...")
source_dir, dest_dir = './libretro-super/dist/info/', '{}/info/'.format(RetroDataDir)
# print('rsync "{}" -> "{}"'.format(source_dir, dest_dir))
common.run(['rsync', '-a', '--delete-excluded', source_dir, dest_dir])

# --- Copy Retroarch stuff (assets, databases, etc.) ---
# NOTE submodules in git does not have the .git directory.
print("rsync shaders_cg...")
source_dir, dest_dir = './libretro-super/retroarch/media/shaders_cg/', '{}/shaders_cg/'.format(RetroDataDir)
# print('rsync "{}" -> "{}"'.format(source_dir, dest_dir))
common.run(['rsync', '-a', '--exclude', '.git', '--delete-excluded', source_dir, dest_dir])

print("rsync overlays...")
source_dir, dest_dir = './libretro-super/retroarch/media/overlays/', '{}/overlays/'.format(RetroDataDir)
# print('rsync "{}" -> "{}"'.format(source_dir, dest_dir))
common.run(['rsync', '-a', '--exclude', '.git', '--delete-excluded', source_dir, dest_dir])

print("rsync assets...")
source_dir, dest_dir = './libretro-super/retroarch/media/assets/', '{}/assets/'.format(RetroDataDir)
# print('rsync "{}" -> "{}"'.format(source_dir, dest_dir))
common.run(['rsync', '-a', '--exclude', '.git', '--delete-excluded', source_dir, dest_dir])

print("rsync joystick autoconfig...")
source_dir, dest_dir = './libretro-super/retroarch/media/autoconfig/', '{}/joypad_autoconfig/'.format(RetroDataDir)
# print('rsync "{}" -> "{}"'.format(source_dir, dest_dir))
common.run(['rsync', '-a', '--exclude', '.git', '--delete-excluded', source_dir, dest_dir])

print("rsync libretrodb ...")
source_dir, dest_dir = './libretro-super/retroarch/media/libretrodb/', '{}/libretrodb/'.format(RetroDataDir)
# print('rsync "{}" -> "{}"'.format(source_dir, dest_dir))
common.run(['rsync', '-a', '--exclude', '.git', '--delete-excluded', source_dir, dest_dir])

# --- Installing core specific stuff
# See http://wiki.libretro.com/index.php?title=PPSSPP
if os.path.isdir('./libretro-super/libretro-ppsspp/assets/'):
    print("Installing PPSSPP assets...")
else:
    print("PPSSPP assets not available.")

# if [ -d ./libretro-super/libretro-ppsspp/assets/ ]; then
#     echo "Installing PPSSPP assets..."
#     mkdir -p ${PATH_RETROARCH_STUFF}/system/PPSSPP/
#     cp -r ./libretro-super/libretro-ppsspp/assets/* ${PATH_RETROARCH_STUFF}/system/PPSSPP/
#     cp -r ./libretro-super/libretro-ppsspp/flash0/* ${PATH_RETROARCH_STUFF}/system/PPSSPP/
# else
#     echo "PPSSPP assets not available."
# fi

# --- So long and thanks for all the fish
print('Done')
sys.exit(0)
