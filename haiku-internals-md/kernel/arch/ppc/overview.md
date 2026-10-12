# The PowerPC port

PowerPC was the first non-x86architecture for which a port of Haiku was attempted. The initial
target was the (then recently released) Mac Mini, but of course the BeBox was in everyone’s mind
as a possible target for this port.

This port went as far as starting the kernel, but then difficulties in implementing the Mac Mini
PCI bus driver stopped it.

Later on, some work as done on adding support for the Sam460ex development board, after a donation
of one to one of the Haiku developers.

Recently, the lack of easily available and affordable PowerPC hardware has reduced interest in this
port.

## Platform specific details

* [Notes on a possible BeBox Haiku port](bebox.md)

    * [Bootloader](bebox.md#bootloader)

    * [references](bebox.md#references)

    * [QEMU target](bebox.md#qemu-target)

* [The Apple Macintosh port](mac.md)

* [The Sam460ex Haiku port](sam460ex.md)

    * [U-Boot commands](sam460ex.md#u-boot-commands)

        * [no-fdt no-initrd](sam460ex.md#no-fdt-no-initrd)

        * [with FDT and tgz as initrd](sam460ex.md#with-fdt-and-tgz-as-initrd)

        * [for environment](sam460ex.md#for-environment)

    * [TODOs](sam460ex.md#todos)

    * [Other ports](sam460ex.md#other-ports)

    * [PowerPC information](sam460ex.md#powerpc-information)

        * [Classic](sam460ex.md#classic)

        * [Book-E](sam460ex.md#book-e)

        * [ePAPR](sam460ex.md#epapr)

        * [amcc 4x0](sam460ex.md#amcc-4x0)

        * [Freescale 440](sam460ex.md#freescale-440)

    * [FDT](sam460ex.md#fdt)

        * [Sam440 dts](sam460ex.md#sam440-dts)

        * [OpenFirmware framebuffer](sam460ex.md#openfirmware-framebuffer)

Generated from the [original source documentation](https://pulkomandy.tk/drop/haiku_internals/kernel/arch/ppc/overview.html).
