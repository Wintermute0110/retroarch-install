#!/bin/bash
# List of tags ("git tag" to get a full list):
# v1.7.0
# v1.7.6
cd libretro-super
cd retroarch

# --- Switch to master HEAD ---
# git checkout master

# --- Or switch to a specific release tag ---
git checkout tags/v1.7.6

# --- Build ---
cd ..
./retroarch-build.sh
cd ..
