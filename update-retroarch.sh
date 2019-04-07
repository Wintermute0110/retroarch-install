#!/bin/bash
#

# Make sure Retroarch repo is in master branch.
cd libretro-super
cd retroarch
git checkout master
cd ..
cd ..

# Update Retroarch and submodule repositories.
cd libretro-super
bash libretro-fetch.sh
cd ..

