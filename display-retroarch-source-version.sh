#!/bin/bash
# Everytime branches are switched with checkout mame does a clean of the project. Be aware!
#
retroarch_source_dir=./libretro-super/retroarch/
current_dir=`pwd`
echo "Current directory $current_dir"
echo "Retroarch source directory $retroarch_source_dir"
git -C $retroarch_source_dir status
