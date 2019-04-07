#!/bin/bash
#
cd libretro-super

# Do not execute 'make clean' before 'make'
NOCLEAN=1 ./libretro-build.sh

cd ..
