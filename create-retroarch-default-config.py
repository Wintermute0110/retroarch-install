#!/usr/bin/python3
#

# Configuration  --------------------------------------------------------------
# Configure paths to match your system (you can use ~ or absolute paths)
conf_source_path = '/home/kodi/Retroarch-Install/retroarch-1.7.6.cfg'
conf_dest_path = '~/.config/retroarch/retroarch.cfg'
conf_dest_initial_path = '~/.config/retroarch/retroarch_initial.cfg'

# Retroarch replaces absolute user home dirs by '~'
retroarch_stuff_dir = '~/.retroarch/'
libretro_dir = '/home/kodi/bin/libretro/'

# Directory where you have your ROMs.
ROMs_dir = '/home/kodi/AEL-ROMs/'

# Import stuff  ---------------------------------------------------------------
import os
import shutil
import sys
import re

# Functions  ------------------------------------------------------------------
def edit_option(filename, option_name, option_value):
  new_line_str = option_name + ' = "' + option_value + '"'
  print("{0} -> '{1}'".format(option_name.ljust(34), new_line_str))

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
# --- Resolve ~ directories into /home/user/ ---
conf_source_path = os.path.expanduser(conf_source_path)
conf_dest_path = os.path.expanduser(conf_dest_path)
conf_dest_initial_path = os.path.expanduser(conf_dest_initial_path)
# retroarch_stuff_dir = os.path.expanduser(retroarch_stuff_dir)
ROMs_dir = os.path.expanduser(ROMs_dir)
libretro_dir = os.path.expanduser(libretro_dir)
print('conf_source_path        "{0}"'.format(conf_source_path))
print('conf_dest_path          "{0}"'.format(conf_dest_path))
print('conf_dest_initial_path  "{0}"'.format(conf_dest_initial_path))
print('retroarch_stuff_dir     "{0}"'.format(retroarch_stuff_dir))
print('ROMs_dir                "{0}"'.format(ROMs_dir))
print('libretro_dir            "{0}"'.format(libretro_dir))

# --- Check if config file already exists (never overwrite it) ---
if os.path.isfile(conf_dest_path):
  print('>> Config file "{0}" already exists'.format(conf_dest_path))
  # print('>> Aborting')
  # sys.exit(1)

# --- Copy retroarch.cfg ---
print(">> Copying Retroarch default config file ...")
shutil.copyfile(conf_source_path, conf_dest_path)

# --- Edit paths on the order they appear in RGUI 'Settings' -- 'Directory' ---
print(">> Editing Retroarch configuration file ...")
# >> Make sure this matches the directory creation in install-retroarch.
# >> To have a look at orphan directories in retroarch.cfg:
#    $ cat retroarch.cfg | grep directory
#    $ cat retroarch.cfg | grep path
# >> There is a bug in Retroarch, some directories end in _path (for files) instead of _directory.
# >> Named System/BIOS in Retroarch
edit_option(conf_dest_path, 'system_directory',             os.path.join(retroarch_stuff_dir, 'system/'))
# >> Named Downloads
edit_option(conf_dest_path, 'core_assets_directory',        os.path.join(retroarch_stuff_dir, 'downloads/'))
edit_option(conf_dest_path, 'assets_directory',             os.path.join(retroarch_stuff_dir, 'assets/'))
# >> Named Dynamic Backgrounds
edit_option(conf_dest_path, 'dynamic_wallpapers_directory', os.path.join(retroarch_stuff_dir, 'wallpapers/'))
edit_option(conf_dest_path, 'thumbnails_directory',         os.path.join(retroarch_stuff_dir, 'thumbnails/'))
# >> Named File Browser (default ROMs directory)
edit_option(conf_dest_path, 'rgui_browser_directory',       os.path.join(ROMs_dir))
# >> Named Config
edit_option(conf_dest_path, 'rgui_config_directory',        os.path.join(retroarch_stuff_dir, 'configurations/'))
# >> Named Core. Apparently ':/' means '/home/user_name/bin/'
# edit_option(conf_dest_path, 'libretro_directory',           os.path.join(libretro_dir))
edit_option(conf_dest_path, 'libretro_directory',           ':/libretro/')
# >> Named Core Info
edit_option(conf_dest_path, 'libretro_info_path',           os.path.join(retroarch_stuff_dir, 'info/'))
edit_option(conf_dest_path, 'content_database_path',        os.path.join(retroarch_stuff_dir, 'libretrodb/rdb/'))
edit_option(conf_dest_path, 'cursor_directory',             os.path.join(retroarch_stuff_dir, 'libretrodb/cursors/'))
edit_option(conf_dest_path, 'cheat_database_path',          os.path.join(retroarch_stuff_dir, 'libretrodb/cht/'))
edit_option(conf_dest_path, 'video_filter_dir',             os.path.join(retroarch_stuff_dir, 'video_filters/'))
edit_option(conf_dest_path, 'audio_filter_dir',             os.path.join(retroarch_stuff_dir, 'audio_filters/'))
edit_option(conf_dest_path, 'video_shader_dir',             os.path.join(retroarch_stuff_dir, 'shaders_cg/'))
edit_option(conf_dest_path, 'recording_output_directory',   os.path.join(retroarch_stuff_dir, 'recording_output/'))
edit_option(conf_dest_path, 'recording_config_directory',   os.path.join(retroarch_stuff_dir, 'recording_config/'))
edit_option(conf_dest_path, 'overlay_directory',            os.path.join(retroarch_stuff_dir, 'overlays/'))
edit_option(conf_dest_path, 'screenshot_directory',         os.path.join(retroarch_stuff_dir, 'screenshots/'))
# Named Input Autoconfig
edit_option(conf_dest_path, 'joypad_autoconfig_dir',        os.path.join(retroarch_stuff_dir, 'joypad_autoconfig/'))
edit_option(conf_dest_path, 'input_remapping_directory',    os.path.join(retroarch_stuff_dir, 'input_remappings/'))
edit_option(conf_dest_path, 'playlist_directory',           os.path.join(retroarch_stuff_dir, 'playlists/'))
edit_option(conf_dest_path, 'savefile_directory',           os.path.join(retroarch_stuff_dir, 'savefiles/'))
edit_option(conf_dest_path, 'savestate_directory',          os.path.join(retroarch_stuff_dir, 'savestates/'))
edit_option(conf_dest_path, 'cache_directory',              os.path.join(retroarch_stuff_dir, 'cache/'))

# --- These directories are not in RGUI menu 'Settings' -- 'Directory' ---
# edit_option(conf_dest_path, 'resampler_directory',           os.path.join(retroarch_stuff_dir, 'nodir/'))
# edit_option(conf_dest_path, 'core_options_path',             os.path.join(retroarch_stuff_dir, 'nodir/'))
# edit_option(conf_dest_path, 'bundle_assets_src_path',        os.path.join(retroarch_stuff_dir, 'nodir/'))
# edit_option(conf_dest_path, 'bundle_assets_dst_path',        os.path.join(retroarch_stuff_dir, 'nodir/'))
# edit_option(conf_dest_path, 'bundle_assets_dst_path_subdir', os.path.join(retroarch_stuff_dir, 'nodir/'))

# --- Other options -----------------------------------------------------------
# For ideas have a look at https://github.com/libretro/Lakka/blob/lakka/packages/libretro/retroarch/package.mk
edit_option(conf_dest_path, 'menu_driver', 'xmb')
edit_option(conf_dest_path, 'rgui_show_start_screen', 'false')
edit_option(conf_dest_path, 'video_font_path', os.path.join(retroarch_stuff_dir, 'assets/xmb/monochrome/font.ttf'))
edit_option(conf_dest_path, 'video_font_size', '22.000000')
edit_option(conf_dest_path, 'input_max_users', '2')
edit_option(conf_dest_path, 'input_autodetect_enable', 'true')
# edit_option(conf_dest_path, 'video_fullscreen', 'true')
edit_option(conf_dest_path, 'video_aspect_ratio_auto', 'true')
edit_option(conf_dest_path, 'video_smooth', 'false')
edit_option(conf_dest_path, 'video_threaded', 'true')
edit_option(conf_dest_path, 'video_gpu_screenshot', 'false')
edit_option(conf_dest_path, 'audio_driver', 'sdl2')
edit_option(conf_dest_path, 'input_axis_threshold', '0.050000')
edit_option(conf_dest_path, 'input_overlay_show_physical_inputs', 'true')
edit_option(conf_dest_path, 'video_message_pos_x', '0.010000')
edit_option(conf_dest_path, 'video_message_pos_y', '0.969999')

# Separate savestates and savefiles per-core. Important because different cores can be used to
# run the same ROM.
edit_option(conf_dest_path, 'sort_savefiles_enable', 'true')
edit_option(conf_dest_path, 'sort_savestates_enable', 'true')

# --- Custom options ---
# Keep old keys Z and X for nagivating Retroarch GUI
edit_option(conf_dest_path, 'menu_unified_controls', 'true')
edit_option(conf_dest_path, 'all_users_control_menu', 'true')
edit_option(conf_dest_path, 'menu_swap_ok_cancel_buttons', 'true')
edit_option(conf_dest_path, 'xmb_menu_color_theme', '8')
edit_option(conf_dest_path, 'menu_shader_pipeline', '3')

# Options not in 1.7.4
# edit_option(conf_dest_path, 'xmb_show_favorites', 'false')
# edit_option(conf_dest_path, 'xmb_show_images', 'false')
# edit_option(conf_dest_path, 'xmb_show_music', 'false')

# --- Logitech F710 joystick, xpad option triggers as buttons OFF ---
# In the future use joypad autoconfigs to configure gamepads.
#
# Guide button closes Retroarch
# edit_option(conf_dest_path, 'input_exit_emulator_btn', '8')
# R3 opens/closes Retroarch menu
# edit_option(conf_dest_path, 'input_menu_toggle_btn', '10')
# L3 toggles fullscreen mode
# edit_option(conf_dest_path, 'input_toggle_fullscreen_btn', '9')

# --- Copy newly edited retroarch.cfg into retroarch_initial.cfg as a backup ---
print(">> Backing up initial configuration file ...")
shutil.copyfile(conf_dest_path, conf_dest_initial_path)
