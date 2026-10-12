# The ARM port

Note: there are in fact two ports to the ARM architecture, one for 32-bit, and one for 64-bit
systems. They don’t have a lot of shared code as the two architectures are very different from
one another.

ARM devices are very popular, and especially since the release of the Raspberry Pi, people have
been requesting that Haiku is ported to it. Unfortunately, limitations in the architecture itself
and the wide diversity of hardware have made this task more complicated, and progress has been
slow. For example, ARM has no standard like the PC is for x86, so concepts as basic as a system
timer, a bootloader, or a serial port, are different from one machine to another. The situation
has improved with the later generations, as more things were integrated in the CPU core, and u-boot
is now well established as the main bootloader for ARM devices.

## Limitations

There will be no support for hardware using architectures older than ARMv5. There will probably be
no support for architectures before ARMv7, which require more work on the compiler and OS, for
example due to lack of atomic instructions.

Support for high vectors (interrupt vectors stored at the end of the memory space) is required.

## Information about specific hardware targets

Over the years, various possible ARM targets have been considered for the Haiku ARM port.
We have accumulated some notes and documentation on some of them.

* [Allwinner A10 hardware notes](allwinner_a10.md)

    * [Hardware Information](allwinner_a10.md#hardware-information)

    * [Setting up the Haiku SD card](allwinner_a10.md#setting-up-the-haiku-sd-card)

        * [Boot Partition](allwinner_a10.md#boot-partition)

            * [Required Files](allwinner_a10.md#required-files)

    * [Booting](allwinner_a10.md#booting)

        * [Script.bin](allwinner_a10.md#script-bin)

    * [Emulation support](allwinner_a10.md#emulation-support)

    * [Useful links](allwinner_a10.md#useful-links)

* [BeagleBone Black](beagle.md)

* [Hardware information (Rev A5A)](beagle.md#hardware-information-rev-a5a)

* [Setting up the Haiku SD card](beagle.md#setting-up-the-haiku-sd-card)

    * [Boot Partition](beagle.md#boot-partition)

        * [Required files](beagle.md#required-files)

        * [Optional files](beagle.md#optional-files)

* [Compiling](beagle.md#compiling)

* [Booting](beagle.md#booting)

* [Emulation](beagle.md#emulation)

* [Additional information](beagle.md#additional-information)

* [Efika MX](efikamx.md)

    * [FDT](efikamx.md#fdt)

* [iPaq](ipaq.md)

    * [RS232](ipaq.md#rs232)

* [Raspberry Pi](rpi1.md)

    * [Hardware Information](rpi1.md#hardware-information)

    * [Setting up the Haiku SD card](rpi1.md#setting-up-the-haiku-sd-card)

        * [Boot Partition](rpi1.md#boot-partition)

            * [Required Files](rpi1.md#required-files)

            * [Optional Files](rpi1.md#optional-files)

    * [Compiling](rpi1.md#compiling)

    * [Booting](rpi1.md#booting)

        * [config.txt Options](rpi1.md#config-txt-options)

        * [u-boot startup](rpi1.md#u-boot-startup)

    * [Additional Information](rpi1.md#additional-information)

* [Raspberry Pi 2](rpi2.md)

    * [Hardware Information](rpi2.md#hardware-information)

    * [Setting up the Haiku SD card](rpi2.md#setting-up-the-haiku-sd-card)

        * [Boot Partition](rpi2.md#boot-partition)

            * [Required Files](rpi2.md#required-files)

            * [Optional Files](rpi2.md#optional-files)

    * [Compiling](rpi2.md#compiling)

    * [Booting](rpi2.md#booting)

        * [config.txt Options](rpi2.md#config-txt-options)

        * [u-boot startup](rpi2.md#u-boot-startup)

    * [Additional Information](rpi2.md#additional-information)

## TODO list

### Fix pre-ARMv7 support

The ARM instruction set has evolved a lot over time, and we have to make a choice: use the oldest
versions of the instruction set gives us maximal compatibility, but at the cost of a large
performance hit on newer systems, as well as extra code being needed in the OS to compensate for
the missing instructions.

Currently the cross-tools are compiled to default to ARMv7, Cortex-A8, and
hardware floating point. This works around the missing atomic support, see
below. This should be done by setting the -mcpu,-march and -mfloat-abi
switches at build time, however, they aren’t passed on to haikuporter
during the bootstrap build, leading to the ports failing to find the
gcc atomic ops again.

It seems this create other problems, mainly because the UEFI environment for ARM is not supposed to
handle floating point registers. So, the softfloat ABI should be used there instead. To be able
to build both “soft float” and “hard float” code, we need multilib support, see below.

### Determine how to handle atomic functions on ARM

GCC inlines are not supported, since the instructionset is ill-equiped for
this on older (pre-ARMv7) architectures. We possibly have to do something
similar to the linux kernel helper functions for this….

On ARMv7 and later, this is not an issue. Not sure about ARMv6, we may get
it going there. ARMv5 definitely needs us to write some code, but is it
worth the trouble?

### Fix multilib support

ARM-targetting versions of gcc are usually built with multilib support, to
allow targetting architectures with or without FPU, and using either ARM
or Thumb instructions. This bascally means a different libgcc and libstdc++
are built for each combination.

The cross-tools can be built with multilib support. However, we do some
tricks to get a separate libgcc and libstdc++ for the kernel (without C++11
threads support, as that would not build in the kernel). Building this lib
is not done in a multilib-aware way, so you get one only for the default
arch/cpu/abi the compiler is targetting. This is good enough, as long as that
arch is the one we want to use for the kernel…

Later on, the bootstrap build of the native gcc compiler will fail, because
it tries to build its multilib library set by linking against the different
versions of libroot (with and without fpu, etc). We only build one libroot,
so this also fails.

The current version of the x86_64 compiler appears is using multilib (to build for both 32 and 64
bit targets) and is working fine, so it’s possible that most of the issues in this area have
already been fixed.

### Figure out how to get page flags (modified/accessed) and implement it

use unmapped/read-only mappings to trigger soft faults for tracking used/modified flags for ARMv5 and ARMv6

### Fix serial port mapping

Currently kernel uses the haiku_loader identity
mapping for it, but this lives in user virtual address space…
(Need to not use identity mapping in haiku_loader but just
map_physical_memory() there too so it can be handed over without issues).

### Seperate ARM architecture/System-On-Chip IP code

The early work on the ARM port resulted in lots of board specific code being added to early stages
of the kernel. Ideally, this would not be needed, the kernel would manage to initialize itself
mostly in a platform independant way, and get the needed information from the FDT passed by the
bootloader. The difficulty is that on older ARM versions, even the interrupt controller and timers
can be different on each machine.

### KDL disasm module

Currently it is not possible to disassemble code in the kernel debugger.

The [NetBSD disassembler](http://fxr.watson.org/fxr/source/arch/arm/arm/disassem.c?v=NETBSD) could be ported and used for this.

### Add KDL hangman to the boot image

for more enjoyment during porting….

### Userland

Even if KDL hangman is fun, users will want to run real applications someday.

### Bootloader TODOs

* Better handling of memory ranges. Currently no checks are done, and memory is assumed to be a single contiguous range, and the “input” ranges for mmu_init are setup, but never considered.

* Allocate the pagetable range using mmu_allocate() instead of identity mapping it. That way, there’s a bit more flexibility in where to place it both physically and virtually. This will need a minor change on the kernel side too (in the early pagetable allocator).

## Other resources

### About flatenned device trees

* [http://www.denx.de/wiki/U-Boot/UBootFdtInfo](http://www.denx.de/wiki/U-Boot/UBootFdtInfo)

* [http://wiki.freebsd.org/FlattenedDeviceTree#Supporting_library_.28libfdt.29](http://wiki.freebsd.org/FlattenedDeviceTree#Supporting_library_.28libfdt.29)

* [http://elinux.org/images/4/4e/Glikely-powerpc-porting-guide.pdf](http://elinux.org/images/4/4e/Glikely-powerpc-porting-guide.pdf)

* [http://ols.fedoraproject.org/OLS/Reprints-2008/likely2-reprint.pdf](http://ols.fedoraproject.org/OLS/Reprints-2008/likely2-reprint.pdf)

* [http://www.bsdcan.org/2010/schedule/events/171.en.html](http://www.bsdcan.org/2010/schedule/events/171.en.html)

* [http://www.devicetree.org/](http://www.devicetree.org/) (unofficial bindings)

* [http://www.devicetree.org/Device_Tree_Usage](http://www.devicetree.org/Device_Tree_Usage)

* [http://elinux.org/Device_Trees](http://elinux.org/Device_Trees)

### About openfirmware

[http://www.openfirmware.info/Bindings](http://www.openfirmware.info/Bindings)

### About floating point numbers handling on ARM

[https://wiki.debian.org/ArmHardFloatPort/VfpComparison](https://wiki.debian.org/ArmHardFloatPort/VfpComparison)

Generated from the [original source documentation](https://pulkomandy.tk/drop/haiku_internals/kernel/arch/arm/overview.html).
