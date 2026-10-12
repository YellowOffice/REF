---
name: Application Level API Incompatibilities with BeOS
type: topic
kit: special_topics
brief: "Haiku R1 (x86) was designed and is being implemented to be binary and source compatible with applications written for BeOS R5 (x86) to a large extent, but not the other way around"
source: haiku-book
---

# Application Level API Incompatibilities with BeOS
## Description

Haiku R1 (x86) was designed and is being implemented to be binary and source compatible with applications written for BeOS R5 (x86) to a large extent, but not the other way around. In some cases we deliberately broke source compatibility while at the same time maintaining binary compatibility. Here are some specific examples:



* The `"be"` header path is gone - it's called `"os"` in Haiku; since it is always part of the default header search path anyway, you can always just remove it to let your software compile on both platforms, ie. replace: 
```cpp
#include <be/interface/View.h>
```

 with: 
```cpp
#include <interface/View.h>
```

 or rather use the preferred method of omitting the first part and use: 
```cpp
#include <View.h>
```

* BeOS contains a deprecated `add-ons/TrackerAddons.h` header, and a header called `add-ons/TrackerAddOns.h` - Haiku only contains the latter.

* Likewise, you'll find `support/byteorder.h` and `support/ByteOrder.h` in BeOS; Haiku only has ByteOrder.h.

* If you have subclassed [BString](../support_kit/classBString.md) and if you are using its `_privateData` member, you might notice that it is no longer mentioned in the documentation. This is because it has been marked as private.

* The undocumented functions defined in Alias.h from the storage kit are not implemented.

* The private Device Map API (used by OpenTracker) has been replaced by a different API (Disk Device API).

* The application debugging interface is conceptually similar, but nevertheless source and binary incompatible.

* The file system API has changed; file systems that worked on BeOS will no longer work on Haiku.

* Haiku is binary compatible with the Network Kit in BeOS R5 as well as BONE, ie. the BSD socket API as well as Be's proprietary C++ API. However, the [ioctl()](unistd_8h.md#a0b2d815e153aa69279c6308b282cd65f) interface is not compatible with BONE (BeOS R5 did not have such an interface in the first place).

* In several places we also dropped compatibility support for older BeOS versions (PR2, R3, R4), which BeOS R5 still featured.

* The [BArchivable](../support_kit/classBArchivable.md) class has been updated, and for some classes, unarchiving is slightly different.

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/compatibility.html).
