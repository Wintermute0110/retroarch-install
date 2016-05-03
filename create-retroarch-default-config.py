#!/usr/bin/python3
#

# Configuration  --------------------------------------------------------------
file_source = '/home/kodi/bin/source-retroarch/libretro-super/retroarch/retroarch.cfg'
file_dest   = '/home/kodi/.config/retroarch/retroarch.cfg'
stuff_dir   = '/home/kodi/.retroarch/'

# Import stuff  ---------------------------------------------------------------
import os
import shutil
import sys

# Functions  ------------------------------------------------------------------
def edit_path(filename, option_name, stuff_dir, option_dir):
  stuff_dir = stuff_dir.rstrip('/')
  old_str = '# ' + option_name
  new_str = option_name + ' "' + stuff_dir + option_dir + '"'
  dir_name = stuff_dir + option_dir
  print("Directory option {0} -> '{1}'".format(option_name.rjust(32), dir_name))
  
  # --- Check that path exists ---
  if not os.path.isdir(dir_name):
    print("Directory '{0}' not found! Aborting".format(dir_name))
    sys.exit(0)

  # --- Open file ---
  fin = open(filename, 'rt')
  fout = open('temp.cfg', 'wt')

  # --- Search and replace string ---
  old_str_found = False
  for line in fin:
    # Remove trailing \n for comparison
    line_stripped  = line.rstrip('\n')
    if line_stripped == old_str:
      fout.write(new_str + '\n')
      old_str_found = True
    else:
      fout.write(line)

  # --- Close files ---
  fin.close()
  fout.close()

  # --- Check for errors ---
  if not old_str_found:
    print('String ''{0}'' not found. Abort.'.format(old_str))
    sys.exit(1)

  # --- Rename temp file into configuration file ---
  os.rename('temp.cfg', filename)

def edit_string(filename, old_str, new_str):
  print('Replacing "{0}"'.format(old_str))

  # --- Open file ---
  fin = open(filename, 'rt')
  fout = open('temp.cfg', 'wt')

  # --- Search and replace string ---
  old_str_found = False
  for line in fin:
    # Remove trailing \n for comparison
    line_stripped  = line.rstrip('\n')
    if line_stripped == old_str:
      fout.write(new_str + '\n')
      old_str_found = True
    else:
      fout.write(line)

  # --- Close files ---
  fin.close()
  fout.close()

  # --- Check for errors ---
  if not old_str_found:
    print('String ''{0}'' not found. Abort.'.format(old_str))
    sys.exit(1)

  # --- Rename temp file into configuration file ---
  os.rename('temp.cfg', filename)

# Main  -----------------------------------------------------------------------
# --- Check if config file already exists (never overwrite it) ---
if os.path.isfile(file_dest):
  print('Config file "{0}" already exists'.format(file_dest))
  print('Aborting')
  sys.exit(1)

# --- Copy retroarch.cfg ---  
print("Copying Retroarch default config file...")
shutil.copyfile(file_source, file_dest)

# --- Edit paths as they appear in RGUI 'Settings' -- 'Directory' ---
edit_path(file_dest, 'system_directory =',             stuff_dir, '/system/')
edit_path(file_dest, 'assets_directory =',             stuff_dir, '/assets/')
edit_path(file_dest, 'dynamic_wallpapers_directory =', stuff_dir, '/wallpapers/')
edit_path(file_dest, 'boxarts_directory =',            stuff_dir, '/boxarts/')
edit_path(file_dest, 'rgui_browser_directory =', '/home/kodi', '/Games/')
# Config dir keep <default>
edit_path(file_dest, 'libretro_directory =',     '/home/kodi/bin/', '/bin-libretro/')
edit_path(file_dest, 'libretro_info_path =',           stuff_dir, '/info/')
edit_path(file_dest, 'content_database_path =',        stuff_dir, '/libretrodb/rdb/')
# cursor_directory not in default retroarch.cfg (this is a bug...)
edit_path(file_dest, 'cheat_database_path =',          stuff_dir, '/libretrodb/cht/')
edit_path(file_dest, 'video_filter_dir =',             stuff_dir, '/video_filters/')
edit_path(file_dest, 'audio_filter_dir =',             stuff_dir, '/audio_filters/')
edit_path(file_dest, 'video_shader_dir =',             stuff_dir, '/shaders_cg/')
edit_path(file_dest, 'overlay_directory =',            stuff_dir, '/overlays/')
edit_path(file_dest, 'osk_overlay_directory =',        stuff_dir, '/overlays/')
edit_path(file_dest, 'screenshot_directory =',         stuff_dir, '/screenshots/')
edit_path(file_dest, 'joypad_autoconfig_dir =',        stuff_dir, '/autoconfig/')
edit_path(file_dest, 'input_remapping_directory =',    stuff_dir, '/remappings/')
edit_path(file_dest, 'playlist_directory =',           stuff_dir, '/playlists/')
edit_path(file_dest, 'savefile_directory =',           stuff_dir, '/savefiles/')
edit_path(file_dest, 'savestate_directory =',          stuff_dir, '/savestates/')
edit_path(file_dest, 'rgui_config_directory =',        stuff_dir, '/configurations/')

# These options are not in the default config file (but are created by Retroarch when
# it writes a new config file on exit).
# To have a look at orphan directories: $ less retroarch.cfg | grep directory
# There is a bug in Retroarch, some directories end in _path (for files) instead of _directory.
os.system('echo \'cursor_directory = "~/.retroarch/libretrodb/cursors/"\' >> ' + file_dest)
os.system('echo \'core_assets_directory = "~/.retroarch/downloads/"\' >> ' + file_dest)
# rgui_config_directory = "default"
os.system('echo \'recording_output_directory = "~/.retroarch/recording_output/"\' >> ' + file_dest)
os.system('echo \'recording_config_directory = "~/.retroarch/recording_config/"\' >> ' + file_dest)
os.system('echo \'cache_directory = "~/.retroarch/cache/"\' >> ' + file_dest)
os.system('echo \'resampler_directory = "~/.retroarch/resampler/"\' >> ' + file_dest)

# --- Other options -----------------------------------------------------------
# edit_string(file_dest, '# menu_driver = "rgui"', 'menu_driver = "xmb"')
# sed -i -e "s/# video_font_path =/video_font_path =\"~\/bin\/retroarch\/assets\/xmb\/monochrome\/font.ttf\"/" ${RETROARCH_CFG}
# sed -i -e "s/# video_font_size = 48/video_font_size = 22/" ${RETROARCH_CFG}
# sed -i -e "s/# input_max_users = 16/input_max_users = 2/" ${RETROARCH_CFG}
# sed -i -e "s/# input_autodetect_enable = true/input_autodetect_enable = true/" ${RETROARCH_CFG}

# --- Extra options from Lakka (maybe added in the future) ---
# sed -i -e "s/# rgui_show_start_screen = true/rgui_show_start_screen = false/" ${RETROARCH_CFG}

# sed -i -e "s/# video_fullscreen = false/video_fullscreen = true/" ${RETROARCH_CFG}
# sed -i -e "s/# video_smooth = true/video_smooth = false/" ${RETROARCH_CFG}
# sed -i -e "s/# video_aspect_ratio_auto = false/video_aspect_ratio_auto = true/" ${RETROARCH_CFG}
# sed -i -e "s/# video_threaded = false/video_threaded = true/" ${RETROARCH_CFG}
# sed -i -e "s/# video_gpu_screenshot = true/video_gpu_screenshot = false/" ${RETROARCH_CFG}

# sed -i -e "s/# audio_driver =/audio_driver = \"alsathread\"/" ${RETROARCH_CFG}
# sed -i -e "s/# input_driver = sdl/input_driver = udev/" ${RETROARCH_CFG}
# sed -i -e "s/# input_menu_toggle_gamepad_combo =/input_menu_toggle_gamepad_combo = \"2\"/" ${RETROARCH_CFG}

# sed -i -e "s/# menu_core_enable = true/menu_core_enable = false/" ${RETROARCH_CFG}

# echo "playlist_names = \"$RA_PLAYLIST_NAMES\"" >> ${RETROARCH_CFG}
# echo "playlist_cores = \"$RA_PLAYLIST_CORES\"" >> ${RETROARCH_CFG}
