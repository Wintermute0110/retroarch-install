**Retroarch Install** is a set of scripts and utilities that allow easy compilation and configuration
of Retroarch. It has been tested in Debian and Ubuntu.

## Table of Contents

* **[Readme me first](#readme-me-first)**
* **[Cloning this repository](#cloning-this-repository)**
* **[Preparing Retroarch source code](#Preparing-Retroarch-source-code)**
* **[Compiling Retroarch](#Compiling-Retroarch)**
* **[Additional repositories](#Additional-repositories)**
* **[Retroarch installation and configuration](#Retroarch-installation-and-configuration)**
* **[Updating Retroarch](#Updating-Retroarch)**
* **[Post installation notes](#Post-installation-notes)**

## Readme me first ##

In this tutorial it is assumed that the user running Retroarch is named `kodi` with home directory `/home/kodi/`. The user name is only used to determine the paths. The character `~` means the user home directory, `/home/kodi/` by default. The following table summarizes the default paths.

| Name                             | Path                            |
|----------------------------------|---------------------------------|
| These scripts directory          | `/home/kodi/retroarch-install/` |
| Retroarch installation directory | `/home/kodi/bin/`               |
| Libretro directory               | `/home/kodi/bin/libretro/`      |
| Configuration directory          | `/home/kodi/.config/retroarch/` |
| Retroarch data directory         | `/home/kodi/.retroarch/`        |
| Default ROMs directory           | `/home/kodi/AEL-ROMs/`          |

With these defaults you get:

| Name                         | Path                                          |
|------------------------------|-----------------------------------------------|
| Retroarch executable         | `/home/kodi/bin/retroarch`                    |
| Retroarch configuration file | `/home/kodi/.config/retroarch/retroarch.cfg`  |
| Configuration file backup    | `/home/kodi/.config/retroarch/retroarch.cxxzxzxfg` |

Defaults can be changed in the file `configuration.xml`. Feel free to change the default user name `kodi`, but do not change the final directories. For example, `<ConfigDir>/home/myuser/.config/retroarch</ConfigDir>`.
```
<!-- Configuration for Retroarch compilation utilities. -->
<Configuration>
    <!--
        Use a tag or branch name.
        'v' will be added automatically at the beginning of the tag name.
        In other words, for the git tag "v1.9.6" write here "1.9.6"
        Examples: 1.8.7, 1.8.8, 1.8.9, master
    -->
    <Version>1.9.9</Version>

    <!-- No trailing / here in directory names. -->
    <RetroBinDir>/home/kodi/bin</RetroBinDir>
    <LibRetroDir>/home/kodi/libretro</LibRetroDir>
    <ConfigDir>/home/kodi/.config/retroarch</ConfigDir>
    <RetroDataDir>/home/kodi/.retroarch</RetroDataDir>
    <ROMsDir>/home/kodi/AEL-ROMs</ROMsDir>
</Configuration>
```

## Cloning this repository

Before you start, make sure **git** is intalled on your machine. If you don't already have it, create the directory `~/bin/`. To clone this repository execute in:
```
$ cd /home/kodi
$ git clone https://github.com/Wintermute0110/retroarch-install.git
```

This will create a directory named `/home/kodi/retroarch-install`.

## Preparing Retroarch source code

Go to the directory `~/retroarch-install` and execute:
```
$ ./clone-libretro-super.sh
```

A new directory named `libretro-super` will be created inside `~/retroarch-install`. 

### Compile Retroarch and the Libretro cores

**This is not recommended anymore** because the Libretro compiled cores can be downloaded with the Retroarch **Online Core updater**, which saves a lot of time.

To customise the cores you want to download/compile, edit the file `~/retroarch-install/libretro-super/build-config.sh` and comment out the cores you don't want. Note that if you don't customise the cores you want, the source code of all the available libretro cores will be downloaded and compilation times may be very long. Some cores compile fast (about a minute) but each MAME core can take as long as on hour even in a fast machine.

### Compile only Retroarch

This is the preferred option. After the installation of Retroarch then you can download the Libretro cores you want with the **Online Core updater**.

Edit the file `~/retroarch-install/libretro-super/libretro-fetch.sh` and comment the following stuff at the end of the file:
```
# for a in $fetch_lutros; do
#       libretro_fetch "${a%%:*}"
# done

# for a in $fetch_devkits; do
#       libretro_fetch "${a%%:*}"
# done

# for a in $fetch_cores; do
#       libretro_fetch "${a%%:*}"
# done
```

### Download source code

Go to the directory `~/retroarch-install/` and execute `./update-retroarch.sh` This will download the source code of both Retroarch and the cores you configured.

Then, as *root* user execute `./setup-build-dependencies.sh` This will install the C/C++ compiler and some other dependencies such as libraries required to compile Retroarch.

## Compiling Retroarch

Before compilation, go to the directory `~/retroarch-install/` and execute `./show-retroarch-tags.py`. Each tag corresponds to a released version of Retroarch and usually the latest released version is the last one. Use `PgUp` and `PgDn` keys to scroll up and down, respectively:
```
...
v1.7.4
v1.7.5
v1.7.6
```

Pick the version you want (usually the latest released version), edit the file `~/retroarch-install/configuration.xml` and change the context of the `<Version>` tag:
```
    <Version>1.9.9</Version>
```

To compile the Retroarch executable, go to the directory  `~/retroarch-install/` and execute `./compile-retroarch.sh`.

## Additional repositories

Some cores require additional steps if you want to use them.

### PPSSPP

**<NOT WORKING AT THE MOMENT>**

If you want to execute the **ppsspp** core to run PSP games you need to clone an additional repository. This will create a directory named `ppsspp`.
```
./clone-ppsspp.py
```

The runtime files from the `ppsspp` directory will be copied by the `install-retroarch.sh` script into the Retroarch system directory.

### PSP fonts

**<NOT WORKING AT THE MOMENT>**

PPSSPP includes a set of custom fonts which are different from the PSP default fonts. If you happen to have the PSP fonts place them in the `psp-fonts` directory and the  `install-retroarch.sh` script will copy them to the appropiate place in the system directory.

## Retroarch installation and configuration

To install Retroarch, execute `./install-retroarch.sh` This will place the Retroarch executable file in `~/bin/retroarch` and all the libretro cores in `~/libretro/` (if you compiled them). Also, it will create the directory `~/.retroarch` and copy all Retroarch assets, databases, core info files, etc.

Finally, execute `./create-retroarch-default-config.py` to create the default Retroarch configuration file `~/.config/retroarch/retraoarch.cfg`. This configuration file is automatically edited so all paths will point to the correct places in `~/.retroarch/` and also many default options are edited to sensible values.

A backup of the original configuration file is created in `~/.config/retroarch/retroarch_initial.cfg`. To see the changes between both files, go to `~/.config/retroarch/` and execute `diff -u --color retroarch_initial.cfg retroarch.cfg`

## Updating Retroarch

It is recommended that you recompile Retroarch when you upgrade your system. This is specially important if you update the Mesa/OpenGL libraries to avoid problems.

Go to directory `~/Retroarch-Install/` and execute the following steps:

```
$ ./update-libretro-super-using-git.py
$ ./update-retroarch.py
$ nano configuration.xml
$ ./compile-retroarch.py
$ ./install-retroarch.py
$ ./create-retroarch-default-config.py
```

`nano` is the editor I use but feel free to use any other one such as `vim` or `emacs`.

To create a default configuration file required by `./create-retroarch-default-config.py`, first delete the current configuration file, then execute your new Retroarch (it will look ugly without a proper configuration file), and finally copy the default file with the retroarch version. For example, for Retroarch v1.9.9:
```
$ rm /home/kodi/.config/retroarch/retroarch.cfg
$ retroarch # (and press Esc key 2 times to quit)
$ cp /home/kodi/.config/retroarch/retroarch.cfg /home/kodi/retroarch-install/retroarch-1.9.9.cfg
```

### Optional stuff

Execute this optionally before upgrading Retroarch.
```
./update-ppsspp.py
```

## Post installation notes

 1. The **System directory** is located in `~/.retroarch/system/` Here you have to put BIOS files for the cores that require them.

 2. The option `sort_savefiles_enable` is activated. Your saved games will be stored in `~/.retroarch/savefiles/core_name/rom_name`.

 3. In order to use vulkan in cores I think Retroarch `video_driver` options must be set to `vulkan`, otherwise cores will use OpenGL if `video_driver = "glcore"`.

 4. If Retroarch is configured to use vulkan video driver and a OpenGL-only core is loaded, for example `mupen64plus_next_libretro.so`, Retroarch crashes with a **Segmentation fault**.

 5. A minimal `xorg.conf` with Section Device containing Identifier, Driver and VendorName is enough for Xorg to use the **intel** driver and not the **modesetting* driver. Keep in mind that Debian recommends to use the modeseting driver.

 6. The **intel** driver seems to have better performance compared to the **modesetting** driver.

### Problems in Linux Debian/Ubuntu and Intel graphic cards

XMB menu driver causes Retroarch to freeze. This freezing is rather random, sometimes happens, sometimes not. One solution is to use the rgui menu driver. Other users propose to set DRI option to **2**. Users report a loss of performance when using DRI **2**.

```
# In Debian file /etc/X11/xorg.conf
Section "Device"
  Identifier  "Device0"
  Driver      "intel"
  VendorName  "INTEL corporation"
  Option      "DRI" "2"
  Option      "TearFree" "false"
  Option      "TripleBuffer" "false"
EndSection
```

Lakka `xorg-i915.conf` for Intel video cards.

```
# https://github.com/libretro/Lakka-LibreELEC/blob/master/projects/Generic/filesystem/etc/X11/xorg-i915.conf
Section "Device"
  Identifier  "Device0"
  Driver      "intel"
  VendorName  "INTEL Corporation"
  Option      "TripleBuffer" "false"
  Option      "TearFree" "false"
EndSection
```

[Post in Retropie forum](https://retropie.org.uk/forum/post/184322)

> Yeah, i said it countless times on various forums (including this one i think), intel/nvidia
> open-source drivers on linux are kinda crappy, setting DRI to 2 in your xorg configuration
> files is also generally a good fix for this kind of issue.

### Testing Retroarch 1.7.7 with the intel driver in Ubuntu

First, create a file `/etc/X11/xorg.conf` for the X server to use the **intel** driver and not the **modesetting** driver. In this test Kodi uses the default video settings. The reason to use the intel driver is that it seems to have better performance than the modesetting driver (at least when Retroarch is running in the foreground and Kodi in the background).

| DRI | TripleBuffer | TearFree | Result                              |
|-----|--------------|----------|-------------------------------------|
| "3" | false        | false    | Seems to work OK, performance *---- |
| "3" | false        | true     | Seems to work OK, performance ***-- |
| "3" | true         | false    | Seems to work OK, performance ***-- |
| "3" | true         | true     | Seems to work OK, performance ****- |
| "2" | false        | false    | Seems to work OK, performance **--- |
| "2" | false        | true     | Seems to work OK, performance ***-- |
| "2" | true         | false    | Fails.                              |
| "2" | true         | true     | Seems to work OK, performance ***-- |

### Does Retroarch 1.7.7 works on Debian using RGUI and no xorg.conf?

Interesting: in Debian, if file `xorg.conf` does not exist then Xorg uses the `modesetting` driver. The list of drivers installed in the system is in the directory `/usr/lib/xorg/modules/drivers/`.
```
user $ cat /var/log/Xorg.0.log | grep modeset
[  3222.762] (==) Matched modesetting as autoconfigured driver 0
[  3222.762] (II) LoadModule: "modesetting"
[  3222.762] (II) Loading /usr/lib/xorg/modules/drivers/modesetting_drv.so
[  3222.763] (II) Module modesetting: vendor="X.Org Foundation"
[  3222.765] (II) modesetting: Driver for Modesetting Kernel Drivers: kms
[  3222.793] (II) modeset(0): using drv /dev/dri/card0
...
[  3222.818] (II) modeset(0): glamor X acceleration enabled on Mesa DRI Intel(R) Haswell Mobile
[  3222.818] (II) modeset(0): glamor initialized
...
[  3222.893] (==) modeset(0): DPMS enabled
[  3222.894] (II) modeset(0): [DRI2] Setup complete
[  3222.894] (II) modeset(0): [DRI2]   DRI driver: i965
[  3222.894] (II) modeset(0): [DRI2]   VDPAU driver: i965
```

OK... now it seems to work well with no xorg.conf file, the modeset driver, and xbm menu, for both standard and OpenGL cores. I have no idea what configuration option I changed to make it work.

## Internal notes

### Creating a new Retroarch default configuration file

After a clean Retroarch installation, delete `~/.config/retroarch/retraoarch.cfg` and then execute `~/bin/retroarch`. This will create a default configuration file. Copy this file with a name like `~/Retroarch-Install/retroarch-<version>.cfg`, `<version>` matching the Retroarch version.

### PPSSPP core assets

Write me.

### Dolphin core assets

Write me.

### Getting system information for debugging

```
user $ cat /var/log/Xorg.0.log | grep intel
```

```
user $ glxinfo | grep version
```

```
vulkaninfo | grep Version
```
