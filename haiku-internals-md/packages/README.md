# Package Management

This is a short index of the available package management related documentation.

* [Package Management Infrastructure](Infrastructure.rst) provides an overview of what components belong to Haiku’s package management infrastructure and how they work and interact.

* [Building Packages](BuildingPackages.rst) gives information on various aspects of the package building process.

* [Boot Volume Directory Structure](DirectoryStructure.rst) outlines the directory structure of a package management powered Haiku boot volume.

* [Haiku Package File Format](FileFormat.rst) specifies in detail the file format of Haiku package files (HPKG) and Haiku package repository files (HPKR).

* [Packaging Policy](PackagingPolicy.rst) defines the policy for creating Haiku packages.

* [Packages Status](PackagesStatus.rst) gives an overview of the packages needed for a Haiku standard build and their current status.

* [Hybrid Builds](HybridBuilds.rst) provides some information regarding hybrid builds.

* [HaikuDepot](HaikuDepot.rst) explains the concept and ideas behind HaikuDepot, the GUI package manager in the making.

* [Migration](Migration.rst) lists the changes that users should expect when migrating to a package management Haiku.

* [Bootstrapping Haiku](Bootstrapping.rst) explains the process of bootstrapping Haiku and third-party packages.

* [TODO](TODO.rst) is a list of package management related work still to be done.

* [Blog posts](https://www.haiku-os.org/tags/package-management/) on package management (the Batisseur ones are only indirectly package management related).

* [(Old) Package Management Ideas](OldIdeas.rst) is a collection of thoughts and discussions regarding package management. It has been partially obsoleted by the progress on the package management implementation.

* [http://www.youtube.com/watch?v=rNZQQM5zU-Q&list=PL3FFCD4C6D384A302](http://www.youtube.com/watch?v=rNZQQM5zU-Q&list=PL3FFCD4C6D384A302) is a video playlist of Ingo and Oliver explaining and demonstrating the package management branch at BeGeistert 2011.

Below are links to source code related to Haiku’s package management.

* Package management has been merged into “master”, so see the [Haiku](http://cgit.haiku-os.org/haiku/) and [Buildtools](http://cgit.haiku-os.org/buildtools/) repositories for that

* [HaikuPorts](https://github.com/haikuports/haikuports) contains the build recipes of various ports.

* [haikuports.cross](https://github.com/haikuports/haikuports.cross) contains the minimal set of build recipes to bootstrap a new Haiku architecture.

* [haikuporter](https://github.com/haikuports/haikuporter) is the tool to create binary packages from build recipes.

* [Building Packages](BuildingPackages.md)

    * [Building a Package with the “package” Command](BuildingPackages.md#building-a-package-with-the-package-command)

        * [The .PackageInfo](BuildingPackages.md#the-packageinfo)

        * [Version Strings](BuildingPackages.md#version-strings)

        * [Package File Names](BuildingPackages.md#package-file-names)

        * [Example package file](BuildingPackages.md#example-package-file)

    * [Building a Package with “haikuporter”](BuildingPackages.md#building-a-package-with-haikuporter)

* [Boot Volume Directory Structure](DirectoryStructure.md)

* [Haiku Package File Format](FileFormat.md)

    * [The Data Container Format](FileFormat.md#the-data-container-format)

        * [Header](FileFormat.md#header)

        * [Heap](FileFormat.md#heap)

        * [TOC](FileFormat.md#toc)

            * [Attribute Data Types](FileFormat.md#attribute-data-types)

            * [Strings](FileFormat.md#strings)

            * [Main TOC](FileFormat.md#main-toc)

            * [Attribute Values](FileFormat.md#attribute-values)

        * [Package Attributes](FileFormat.md#package-attributes)

    * [The Archive Format](FileFormat.md#the-archive-format)

        * [Attribute IDs](FileFormat.md#attribute-ids)

        * [TOC Attributes](FileFormat.md#toc-attributes)

    * [The Package Format](FileFormat.md#the-package-format)

        * [Attribute IDs](FileFormat.md#the-package-format-attribute-ids)

    * [Haiku Package Repository Format](FileFormat.md#haiku-package-repository-format)

        * [The Data Container Format](FileFormat.md#id2)

            * [Header](FileFormat.md#id3)

        * [Attribute IDs](FileFormat.md#id4)

* [Hybrid Builds](HybridBuilds.md)

    * [General Requirements](HybridBuilds.md#general-requirements)

    * [Secondary Architecture Package Requirements](HybridBuilds.md#secondary-architecture-package-requirements)

* [Package Management Infrastructure](Infrastructure.md)

    * [Software Installation Locations](Infrastructure.md#software-installation-locations)

    * [Software Installation](Infrastructure.md#software-installation)

        * [Manual Installation](Infrastructure.md#manual-installation)

        * [Installation via Package Manager](Infrastructure.md#installation-via-package-manager)

        * [Application Bundles](Infrastructure.md#application-bundles)

        * [Installation Location Order and Consistency](Infrastructure.md#installation-location-order-and-consistency)

    * [Software Repositories](Infrastructure.md#software-repositories)

        * [Standard Repositories](Infrastructure.md#standard-repositories)

    * [The Package Kit](Infrastructure.md#the-package-kit)

    * [Localization](Infrastructure.md#localization)

* [Migration to Package Management](Migration.md)

    * [Changes for Users](Migration.md#changes-for-users)

    * [Changes for Application Developers](Migration.md#changes-for-application-developers)

    * [Changes for Haiku Developers](Migration.md#changes-for-haiku-developers)

    * [Changes for Porters](Migration.md#changes-for-porters)

* [Packaging Policy](PackagingPolicy.md)

    * [Multiple Packages per Software](PackagingPolicy.md#multiple-packages-per-software)

    * [Provides Declaration](PackagingPolicy.md#provides-declaration)

    * [Documentation](PackagingPolicy.md#documentation)

    * [Data Files](PackagingPolicy.md#data-files)

    * [Writable and Settings Files and Directories](PackagingPolicy.md#writable-and-settings-files-and-directories)

    * [Post-Installation Scripts](PackagingPolicy.md#post-installation-scripts)

    * [Pre-Uninstallation Scripts](PackagingPolicy.md#pre-uninstallation-scripts)

* [Bootstrapping Haiku](Bootstrapping.md)

    * [Prerequisites](Bootstrapping.md#prerequisites)

    * [Configuring and Building](Bootstrapping.md#configuring-and-building)

    * [How it works](Bootstrapping.md#how-it-works)

    * [Haiku Architecture Ports](Bootstrapping.md#haiku-architecture-ports)

* [packagefs](TODO.md)

* [Package Daemon](TODO.md#package-daemon)

* [Package building](TODO.md#package-building)

* [Package kit/manager](TODO.md#package-kit-manager)

* [Boot loader](TODO.md#boot-loader)

* [Package/package repository format](TODO.md#package-package-repository-format)

* [Miscellaneous](TODO.md#miscellaneous)

* [Package Management Ideas](OldIdeas.md)

    * [Requirements](OldIdeas.md#requirements)

        * [HaikuBits](OldIdeas.md#haikubits)

        * [Bundles](OldIdeas.md#bundles)

        * [Management](OldIdeas.md#management)

        * [Dependencies](OldIdeas.md#dependencies)

        * [Updates](OldIdeas.md#updates)

    * [Implementation](OldIdeas.md#implementation)

        * [Bundles](OldIdeas.md#id1)

        * [Install or not?](OldIdeas.md#install-or-not)

        * [Merged](OldIdeas.md#merged)

        * [Self-contained](OldIdeas.md#self-contained)

        * [Settings](OldIdeas.md#settings)

            * [Multiple Application Version](OldIdeas.md#multiple-application-version)

        * [Dependency Hell](OldIdeas.md#dependency-hell)

            * [Avoiding](OldIdeas.md#avoiding)

            * [Tacking](OldIdeas.md#tacking)

        * [libalpm](OldIdeas.md#libalpm)

            * [Pros](OldIdeas.md#pros)

            * [Cons](OldIdeas.md#cons)

    * [Brainstorming Results from BeGeistert](OldIdeas.md#brainstorming-results-from-begeistert)

    * [Package Format](OldIdeas.md#package-format)

    * [References](OldIdeas.md#references)

Generated from the [original source documentation](https://pulkomandy.tk/drop/haiku_internals/packages/README.html).
