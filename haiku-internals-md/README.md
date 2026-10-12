# Welcome to Haiku internals’s documentation!

## Target audience

This documentation is aimed at people who want to contribute to Haiku by modifying the operating
system itself. It covers various topics, both technical (how things work) and organizational
(patch submission process, for example).

This document might also be useful to application developers trying to understand the behavior of
the operating system in some specific cases, however, the [API documentation](https://api.haiku-os.org) should answer most of
the questions in this area already.

This documentation assumes basic knowledge of C++ and the Be API, if you need more information
about that, please see the [Learning to program with Haiku](https://github.com/theclue/programming-with-haiku/releases/tag/v1.1) book.

## Status of this document

The work on this book has just started, many sections are incomplete or missing. Here is a list of
other resources that could be useful:

* The [Haiku website](https://www.haiku-os.org) has several years of blog posts and articles documenting many aspects of the system,

* The [Coding guidelines](https://www.haiku-os.org/development/coding-guidelines/) describes how code should be formatted,

* The [User guide](https://www.haiku-os.org/docs/userguide/en/contents.html) documents Haiku from the users’ point of view and can be useful to understand how things are supposed to work,

* The [Haiku Interface Guidelines](https://www.haiku-os.org/docs/HIG/index.xml) document graphical user interface conventions,

* The [Haiku Icon Guidelines](https://www.haiku-os.org/development/icon-guidelines) gives some rules for making icons fitting with the style of the existing ones.

## Table of contents

* [Search Page](search.md)

Contents:

* [The configure script](build/configure.md)

* [Building Haiku with Jam](build/jam.md)

* [HaikuPorts build-packages repository](build/repositories/README.md)

    * [Updating](build/repositories/README.md#updating)

    * [Container Process](build/repositories/README.md#container-process)

    * [Prepare the build-packages repository](build/repositories/README.md#prepare-the-build-packages-repository)

    * [Pull the repostory file and commit it](build/repositories/README.md#pull-the-repostory-file-and-commit-it)

* [HaikuDepot and Server Interactions](apps/haikudepot/server.md)

    * [Introduction](apps/haikudepot/server.md#introduction)

    * [Process, ProcessNode and Coordinator](apps/haikudepot/server.md#process-processnode-and-coordinator)

    * [Bulk Load Processes](apps/haikudepot/server.md#bulk-load-processes)

    * [Process / ProcessNode / Coordinator](apps/haikudepot/server.md#process-processnode-coordinator)

    * [Failure](apps/haikudepot/server.md#failure)

    * [Concurrency](apps/haikudepot/server.md#concurrency)

* [The MIDI Kit](midi/README.md)

    * [Midi Kit design](midi/design.md)

    * [How libmidi1 works](midi/midi1.md)

    * [The softsynth](midi/midi1.md#the-softsynth)

    * [The BeOS R5 Midi Kit protocol](midi/oldprotocol.md)

    * [Misc notes](midi/stuff.md)

    * [Testing the Midi Kit](midi/testing.md)

    * [Midi Kit TO DO List](midi/todo.md)

* [Haiku Network Stack Architecture](net/NetworkStackOverview.md)

    * [The Structures and Classes](net/NetworkStackOverview.md#the-structures-and-classes)

* [How to Merge Patches from NetBSD Trunk](net/HowTo-Synchronize_with_NetBSD.md)

* [Package Management](packages/README.md)

    * [Building Packages](packages/BuildingPackages.md)

    * [Boot Volume Directory Structure](packages/DirectoryStructure.md)

    * [Haiku Package File Format](packages/FileFormat.md)

    * [Hybrid Builds](packages/HybridBuilds.md)

    * [Package Management Infrastructure](packages/Infrastructure.md)

    * [Migration to Package Management](packages/Migration.md)

    * [Packaging Policy](packages/PackagingPolicy.md)

    * [Bootstrapping Haiku](packages/Bootstrapping.md)

    * [packagefs](packages/TODO.md)

    * [Package Daemon](packages/TODO.md#package-daemon)

    * [Package building](packages/TODO.md#package-building)

    * [Package kit/manager](packages/TODO.md#package-kit-manager)

    * [Boot loader](packages/TODO.md#boot-loader)

    * [Package/package repository format](packages/TODO.md#package-package-repository-format)

    * [Miscellaneous](packages/TODO.md#miscellaneous)

    * [Package Management Ideas](packages/OldIdeas.md)

* [Application Server](servers/app_server/toc.md)

    * [Class Descriptions](servers/app_server/toc.md#class-descriptions)

    * [Other Documents](servers/app_server/toc.md#other-documents)

* [Registrar Protocols](servers/registrar/Protocols.md)

    * [Standard Replies](servers/registrar/Protocols.md#standard-replies)

    * [General Requests](servers/registrar/Protocols.md#general-requests)

    * [Roster Requests](servers/registrar/Protocols.md#roster-requests)

    * [MIME Database Requests](servers/registrar/Protocols.md#mime-database-requests)

    * [Message Runner Requests](servers/registrar/Protocols.md#message-runner-requests)

    * [Clipboard Handler Requests](servers/registrar/Protocols.md#clipboard-handler-requests)

    * [Disk Device Requests](servers/registrar/Protocols.md#disk-device-requests)

* [Device Driver Architecture](kernel/device_manager_introduction.md)

    * [1. The Basics](kernel/device_manager_introduction.md#the-basics)

    * [2. Exploring the Device Tree](kernel/device_manager_introduction.md#exploring-the-device-tree)

    * [3. Writing a Driver](kernel/device_manager_introduction.md#writing-a-driver)

    * [4. Publishing a Device](kernel/device_manager_introduction.md#publishing-a-device)

    * [5. Writing a Bus Driver](kernel/device_manager_introduction.md#writing-a-bus-driver)

    * [The generic bus](kernel/device_manager_introduction.md#the-generic-bus)

    * [6. Open Issues](kernel/device_manager_introduction.md#open-issues)

* [Plug and Play Manager](kernel/obsolete_pnp_manager.md)

    * [PNP Manager](kernel/obsolete_pnp_manager.md#pnp-manager)

    * [PNP Driver](kernel/obsolete_pnp_manager.md#pnp-driver)

    * [PNP Bus](kernel/obsolete_pnp_manager.md#pnp-bus)

* [Swap file](kernel/vm/swap_file_support.md)

    * [How to use a swap file?](kernel/vm/swap_file_support.md#how-to-use-a-swap-file)

    * [How swap system works?](kernel/vm/swap_file_support.md#how-swap-system-works)

* [Notes on long double support](kernel/arch/long_double.md)

    * [128-bit IEEE](kernel/arch/long_double.md#bit-ieee)

    * [64-bit IEEE](kernel/arch/long_double.md#bit-ieee-1)

    * [80-bit](kernel/arch/long_double.md#bit)

    * [double double](kernel/arch/long_double.md#double-double)

* [The ARM port](kernel/arch/arm/overview.md)

    * [Limitations](kernel/arch/arm/overview.md#limitations)

    * [Information about specific hardware targets](kernel/arch/arm/overview.md#information-about-specific-hardware-targets)

    * [TODO list](kernel/arch/arm/overview.md#todo-list)

    * [Other resources](kernel/arch/arm/overview.md#other-resources)

* [The m68k port](kernel/arch/m68k/overview.md)

    * [Todo list](kernel/arch/m68k/overview.md#todo-list)

    * [Target platforms information](kernel/arch/m68k/overview.md#target-platforms-information)

* [The PowerPC port](kernel/arch/ppc/overview.md)

    * [Platform specific details](kernel/arch/ppc/overview.md#platform-specific-details)

* [The SPARC port](kernel/arch/sparc/overview.md)

    * [SPARC ABI](kernel/arch/sparc/overview.md#sparc-abi)

    * [Misaligned memory access](kernel/arch/sparc/overview.md#misaligned-memory-access)

    * [The Ultrasparc MMUs](kernel/arch/sparc/overview.md#the-ultrasparc-mmus)

    * [Software floating-point support](kernel/arch/sparc/overview.md#software-floating-point-support)

    * [Openboot bootloader](kernel/arch/sparc/overview.md#openboot-bootloader)

* [Node Monitoring](kernel/fs/node_monitoring.md)

    * [Requirements - Exported Functionality in BeOS](kernel/fs/node_monitoring.md#requirements-exported-functionality-in-beos)

    * [Meeting the Requirements in an Optimal Way - Implementation in OpenBeOS](kernel/fs/node_monitoring.md#meeting-the-requirements-in-an-optimal-way-implementation-in-openbeos)

    * [Differences Between Both Implementations](kernel/fs/node_monitoring.md#differences-between-both-implementations)

    * [And Beyond?](kernel/fs/node_monitoring.md#and-beyond)

* [Filesystem drivers](file_systems/overview.md)

    * [Implementation notes](file_systems/overview.md#implementation-notes)

    * [Development tools](file_systems/overview.md#development-tools)

* [Partitioning system for Sun Sparc machines](partitioning_systems/sun.md)

* [Disk driver ioctls](drivers/disk/ioctls.md)

    * [B_GET_DEVICE_SIZE](drivers/disk/ioctls.md#b-get-device-size)

    * [B_GET_GEOMETRY](drivers/disk/ioctls.md#b-get-geometry)

    * [B_GET_ICON_NAME](drivers/disk/ioctls.md#b-get-icon-name)

    * [B_GET_VECTOR_ICON](drivers/disk/ioctls.md#b-get-vector-icon)

    * [B_EJECT_DEVICE](drivers/disk/ioctls.md#b-eject-device)

    * [B_LOAD_MEDIA](drivers/disk/ioctls.md#b-load-media)

    * [B_FLUSH_DRIVE_CACHE](drivers/disk/ioctls.md#b-flush-drive-cache)

    * [B_TRIM_DEVICE](drivers/disk/ioctls.md#b-trim-device)

* [Intel video hardware generations](drivers/intel_extreme/generations.md)

    * [Generation 1](drivers/intel_extreme/generations.md#generation-1)

    * [Generation 2 / 2002](drivers/intel_extreme/generations.md#generation-2-2002)

    * [Generation 3 / 2004](drivers/intel_extreme/generations.md#generation-3-2004)

    * [Generation 4 / 2006](drivers/intel_extreme/generations.md#generation-4-2006)

    * [Generation 5 / 2010](drivers/intel_extreme/generations.md#generation-5-2010)

    * [Generation 6 / 2011](drivers/intel_extreme/generations.md#generation-6-2011)

    * [Generation 7 / 2012](drivers/intel_extreme/generations.md#generation-7-2012)

    * [Generation 8 / 2013](drivers/intel_extreme/generations.md#generation-8-2013)

    * [Generation 9 / 2015](drivers/intel_extreme/generations.md#generation-9-2015)

    * [Generation 10](drivers/intel_extreme/generations.md#generation-10)

    * [Generation 11](drivers/intel_extreme/generations.md#generation-11)

    * [Generation 12](drivers/intel_extreme/generations.md#generation-12)

* [AGP (and PCI-express) Graphics Address Re-Mapping Table](busses/agp_gart/ReadMe.md)

* [Bluetooth overview](busses/bluetooth/overview.md)

* [SDHCI MMC Driver](busses/sdhci/sdhci_mmc_driver.md)

    * [Loading and testing the driver](busses/sdhci/sdhci_mmc_driver.md#loading-and-testing-the-driver)

    * [Insight into the code and future tasks](busses/sdhci/sdhci_mmc_driver.md#insight-into-the-code-and-future-tasks)

* [The USB stack](busses/usb/USB_stack_design.md)

* [Haiku boot process specification](kernel/boot/boot_process_specs.md)

    * [Overview](kernel/boot/boot_process_specs.md#overview)

    * [Booting from BIOS](kernel/boot/boot_process_specs.md#booting-from-bios)

    * [Open Firmware](kernel/boot/boot_process_specs.md#open-firmware)

    * [U-Boot](kernel/boot/boot_process_specs.md#u-boot)

    * [EFI](kernel/boot/boot_process_specs.md#efi)

* [Bootloader debugging with GEF](kernel/boot/Debugging_Bootloaders_GEF.md)

    * [Building Haiku](kernel/boot/Debugging_Bootloaders_GEF.md#building-haiku)

    * [Launching Haiku in QEMU](kernel/boot/Debugging_Bootloaders_GEF.md#launching-haiku-in-qemu)

    * [Attaching GEF](kernel/boot/Debugging_Bootloaders_GEF.md#attaching-gef)

* [Using PCI serial ports for debugging](kernel/pci_serial_debug.md)

    * [Devices known to work](kernel/pci_serial_debug.md#devices-known-to-work)

    * [Devices to be tested](kernel/pci_serial_debug.md#devices-to-be-tested)

    * [Configuring](kernel/pci_serial_debug.md#configuring)

Generated from the [original source documentation](https://pulkomandy.tk/drop/haiku_internals/index.html).
