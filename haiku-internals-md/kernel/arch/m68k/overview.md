# The m68k port

The Motorola 68000 is an old CPU and not a reasonable target for Haiku. However, later models
which are equipped with a memory management unit could work (slowly).

There is work in progress to target Atari, Amiga, and NeXT hardware platforms.

## Todo list

* optimization: remove M68KPagingStructures[*]::UpdateAllPageDirs() and just allocate all the kernel page root entries at boot and be done with it. It’s not very big anyway.

* possibly other optimizations in the VM code due to not supporting SMP?

## Target platforms information

* [The Amiga port](amiga.md)

* [The Atari ST port](atari.md)

    * [Atari ST executables](atari.md#atari-st-executables)

    * [Useful resources](atari.md#useful-resources)

Generated from the [original source documentation](https://pulkomandy.tk/drop/haiku_internals/kernel/arch/m68k/overview.html).
