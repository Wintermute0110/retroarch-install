#!/usr/bin/python3
#

# Configuration  --------------------------------------------------------------
# >> Configure paths to your system
conf_source_path       = '/home/kodi/bin/source-retroarch/retroarch.cfg'
conf_dest_path         = '/home/kodi/.config/retroarch/retroarch.cfg'
conf_dest_initial_path = '/home/kodi/.config/retroarch/retroarch_initial.cfg'

# >> Retroarch replaces absolute user home dirs by '~'
retroarch_stuff_dir = '~/.retroarch'
ROMs_dir            = '~/Games/'
libretro_dir        = '~/bin/bin-libretro/'

# Import stuff  ---------------------------------------------------------------
import os
import shutil
import sys
import re

# Functions  ------------------------------------------------------------------
def edit_option(filename, option_name, option_value):
  new_line_str = option_name + ' = "' + option_value + '"'
  print("Option: {0} -> '{1}'".format(option_name.rjust(32), new_line_str))

  # --- Open file ---
  fin = open(filename, 'rt')
  fout = open('temp.cfg', 'wt')

  # --- Search and replace string ---
  option_line_found = False
  for line in fin:
    # Remove trailing \n for comparison
    line_stripped  = line.rstrip('\n')
    r_pattern = '^{0} = '.format(option_name)
    regex_result = re.findall(r_pattern, line_stripped)
    if regex_result:
      fout.write(new_line_str + '\n')
      option_line_found = True
    else:
      fout.write(line)

  # --- Close files ---
  fin.close()
  fout.close()

  # --- Check for errors ---
  if not option_line_found:
    print('Option name ''{0}'' not found. Abort.'.format(option_name))
    sys.exit(1)

  # --- Rename temp file into configuration file ---
  os.rename('temp.cfg', filename)

# Main  -----------------------------------------------------------------------
# --- Check if config file already exists (never overwrite it) ---
if os.path.isfile(conf_dest_path):
  print('Config file "{0}" already exists'.format(conf_dest_path))
  print('Aborting')
  sys.exit(1)

# --- Copy retroarch.cfg ---  
print("Copying Retroarch default config file...")
shutil.copyfile(conf_source_path, conf_dest_path)

# --- Edit paths on the order they appear in RGUI 'Settings' -- 'Directory' ---
# >> Update to Retroarch 1.3.0
# To have a look at orphan directories in retroarch.cfg: 
#  $ less retroarch.cfg | grep directory
#  $ less retroarch.cfg | grep path
# There is a bug in Retroarch, some directories end in _path (for files) instead of _directory.
edit_option(conf_dest_path, 'system_directory',             os.path.join(retroarch_stuff_dir, 'system/'))
edit_option(conf_dest_path, 'core_assets_directory',        os.path.join(retroarch_stuff_dir, 'core_assets/'))
edit_option(conf_dest_path, 'assets_directory',             os.path.join(retroarch_stuff_dir, 'assets/'))
edit_option(conf_dest_path, 'dynamic_wallpapers_directory', os.path.join(retroarch_stuff_dir, 'wallpapers/'))
edit_option(conf_dest_path, 'boxarts_directory',            os.path.join(retroarch_stuff_dir, 'boxarts/'))
edit_option(conf_dest_path, 'rgui_browser_directory',       os.path.join(ROMs_dir))
edit_option(conf_dest_path, 'rgui_config_directory',        os.path.join(retroarch_stuff_dir, 'configurations/'))
edit_option(conf_dest_path, 'libretro_directory',           os.path.join(libretro_dir))
edit_option(conf_dest_path, 'libretro_info_path',           os.path.join(retroarch_stuff_dir, 'info/'))
edit_option(conf_dest_path, 'content_database_path',        os.path.join(retroarch_stuff_dir, 'libretrodb/rdb/'))
edit_option(conf_dest_path, 'cursor_directory',             os.path.join(retroarch_stuff_dir, 'libretrodb/cursors/'))
edit_option(conf_dest_path, 'cheat_database_path',          os.path.join(retroarch_stuff_dir, 'libretrodb/cht/'))
edit_option(conf_dest_path, 'video_filter_dir',             os.path.join(retroarch_stuff_dir, 'video_filters/'))
edit_option(conf_dest_path, 'audio_filter_dir',             os.path.join(retroarch_stuff_dir, 'audio_filters/'))
edit_option(conf_dest_path, 'video_shader_dir',             os.path.join(retroarch_stuff_dir, 'shaders_cg/'))
edit_option(conf_dest_path, 'overlay_directory',            os.path.join(retroarch_stuff_dir, 'overlays/'))
edit_option(conf_dest_path, 'osk_overlay_directory',        os.path.join(retroarch_stuff_dir, 'osk_overlays/'))
edit_option(conf_dest_path, 'screenshot_directory',         os.path.join(retroarch_stuff_dir, 'screenshots/'))
edit_option(conf_dest_path, 'joypad_autoconfig_dir',        os.path.join(retroarch_stuff_dir, 'joypad_autoconfig/'))
edit_option(conf_dest_path, 'input_remapping_directory',    os.path.join(retroarch_stuff_dir, 'input_remappings/'))
edit_option(conf_dest_path, 'playlist_directory',           os.path.join(retroarch_stuff_dir, 'playlists/'))
edit_option(conf_dest_path, 'savefile_directory',           os.path.join(retroarch_stuff_dir, 'savefiles/'))
edit_option(conf_dest_path, 'savestate_directory',          os.path.join(retroarch_stuff_dir, 'savestates/'))
edit_option(conf_dest_path, 'recording_output_directory',   os.path.join(retroarch_stuff_dir, 'recording_output/'))
edit_option(conf_dest_path, 'recording_config_directory',   os.path.join(retroarch_stuff_dir, 'recording_config/'))
edit_option(conf_dest_path, 'cache_directory',              os.path.join(retroarch_stuff_dir, 'cache/'))

# --- These directories are not in 'Settings' -- 'Directory' --- in RGUI ---
edit_option(conf_dest_path, 'resampler_directory',          os.path.join(retroarch_stuff_dir, 'resampler/'))

# --- Other options -----------------------------------------------------------
# >> For idead have a look at https://github.com/libretro/Lakka/blob/lakka/packages/libretro/retroarch/package.mk
edit_option(conf_dest_path, 'menu_driver', 'xmb')
edit_option(conf_dest_path, 'rgui_show_start_screen', 'false')
edit_option(conf_dest_path, 'video_font_path', os.path.join(retroarch_stuff_dir, 'assets/xmb/monochrome/font.ttf'))
edit_option(conf_dest_path, 'video_font_size', '22.000000')
edit_option(conf_dest_path, 'input_max_users', '2')
edit_option(conf_dest_path, 'input_autodetect_enable', 'true')
edit_option(conf_dest_path, 'video_fullscreen', 'true')
edit_option(conf_dest_path, 'video_aspect_ratio_auto', 'true')
edit_option(conf_dest_path, 'video_smooth', 'false')
edit_option(conf_dest_path, 'video_threaded', 'true')
edit_option(conf_dest_path, 'video_gpu_screenshot', 'false')
edit_option(conf_dest_path, 'audio_driver', 'alsathread')
edit_option(conf_dest_path, 'input_driver', 'udev')

edit_option(conf_dest_path, 'sort_savefiles_enable', 'true')
edit_option(conf_dest_path, 'sort_savestates_enable', 'true')

# --- Custom options ---
# >> Logitech F710 joystick
edit_option(conf_dest_path, 'input_exit_emulator_btn', '10')
edit_option(conf_dest_path, 'input_menu_toggle_btn', '12')

# --- Copy newly edite retroarch.cfg into retroarch_initial.cfg as a backup ---  
print("Creating retroarch.cfg initial backup...")
shutil.copyfile(conf_dest_path, conf_dest_initial_path)
