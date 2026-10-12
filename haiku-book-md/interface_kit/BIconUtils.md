---
name: BIconUtils
type: class
kit: interface_kit
brief: "The BIconUtils class provide utility methods for managing and drawing vector icons"
source: haiku-book
---

# BIconUtils Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

The [BIconUtils](classBIconUtils.md) class provide utility methods for managing and drawing vector icons. 


Haiku icons are stored in the HVIF (Haiku Vector Icon Format). This format was designed specifically for this purpose, and allows the icon data to be small enough to fit in file's inodes. This way, the icon can be displayed like any other file attribute, without extra disk access.


This class provide only static methods to allow access to the icon data and rendering to BBitmaps for later use in an application. It also supports older icons in bitmap format. These may still be useful at very small sizes. Note you can't create an instance of [BIconUtils](classBIconUtils.md), just call the static methods.



**Since:** Haiku R1

## Member List

### Static Public Member Functions

* `static status_t` [ConvertFromCMAP8](#af83e5eafeb50e2cc99174aef5c849522) (BBitmap *source, BBitmap *result) — Converts an old-style icon to another colorspace.
* `static status_t` [ConvertFromCMAP8](#af5c23a33394ffed219698b70adc8572a) (const uint8 *data, uint32 width, uint32 height, uint32 bytesPerRow, BBitmap *result) — Convert raw data in B_CMAP8 colorspace to a B_RGBA32 BBitmap.
* `static status_t` [ConvertToCMAP8](#a825b85295d102cf882e53feddf725781) (BBitmap *source, BBitmap *result) — Converts a true-color icon to CMAP8 colorspace.
* `static status_t` [ConvertToCMAP8](#acec2db32c0fd064ad24ba3290ff84fd8) (const uint8 *data, uint32 width, uint32 height, uint32 bytesPerRow, BBitmap *result) — Convert B_RGBA32 raw data into a B_CMAP8 BBitmap.
* `static status_t` [GetCMAP8Icon](#a1c86f2249cec405ba86cefaf57877190) (BNode *node, const char *smallIconAttrName, const char *largeIconAttrName, icon_size size, BBitmap *icon) — Utility function to import an "old" BeOS icon in B_CMAP8 colorspace.
* `static status_t` [GetIcon](#a892a955ed7a66348f7e36e764347db41) (BNode *node, const char *vectorIconAttrName, const char *smallIconAttrName, const char *largeIconAttrName, icon_size size, BBitmap *result) — Utility function to import an icon from a node.
* `static status_t` [GetVectorIcon](#adeaaa371ea8dad53906c7019803ff2a1) (BNode *node, const char *attrName, BBitmap *result) — Utility function to import a vector icon in "flat icon" format.
* `static status_t` [GetVectorIcon](#a049e211e3002526351a17f7f64df0d25) (const uint8 *buffer, size_t size, BBitmap *result) — Utility function to import a vector icon in "flat icon" format.

## Detailed Member Documentation

### `ConvertFromCMAP8()`

```cpp
static status_t BIconUtils::ConvertFromCMAP8(BBitmap * source, BBitmap * result)
```

Converts an old-style icon to another colorspace. 


Utility function to convert from old icon colorspace into colorspace of [BBitmap](classBBitmap.md) *result* 



> [!NOTE]
> result should be in B_RGBA32 colorspace, and source in B_CMAP8.



**Since:** Haiku R1

---

### `ConvertFromCMAP8()`

```cpp
static status_t BIconUtils::ConvertFromCMAP8(const uint8 * data, uint32 width, uint32 height, uint32 bytesPerRow, BBitmap * result)
```

Convert raw data in B_CMAP8 colorspace to a B_RGBA32 [BBitmap](classBBitmap.md). 



**Since:** Haiku R1

---

### `ConvertToCMAP8()`

```cpp
static status_t BIconUtils::ConvertToCMAP8(BBitmap * source, BBitmap * result)
```

Converts a true-color icon to CMAP8 colorspace. 


Utility function to convert data from source into *result* colorspace. Call this to convert a picture to a format suitable for storage as an old-style icon.



> [!NOTE]
> result should be in B_CMAP8 colorspace, and source in B_RGBA32.



**Since:** Haiku R1

---

### `ConvertToCMAP8()`

```cpp
static status_t BIconUtils::ConvertToCMAP8(const uint8 * data, uint32 width, uint32 height, uint32 bytesPerRow, BBitmap * result)
```

Convert B_RGBA32 raw data into a B_CMAP8 [BBitmap](classBBitmap.md). 



**Since:** Haiku R1

---

### `GetCMAP8Icon()`

```cpp
static status_t BIconUtils::GetCMAP8Icon(BNode * node, const char * smallIconAttrName, const char * largeIconAttrName, icon_size size, BBitmap * icon)
```

Utility function to import an "old" BeOS icon in B_CMAP8 colorspace. 


Utility function to import an "old" BeOS icon in B_CMAP8 colorspace from either the small icon attribute or the large icon attribute as given in *smallIconAttrName* and *largeIconAttrName*. Which icon is loaded depends on the given *size*.



**Since:** Haiku R1

---

### `GetIcon()`

```cpp
static status_t BIconUtils::GetIcon(BNode * node, const char * vectorIconAttrName, const char * smallIconAttrName, const char * largeIconAttrName, icon_size size, BBitmap * result)
```

Utility function to import an icon from a node. 


Utility function to import an icon from the node that has either of the provided attribute names. Which icon type is preferred (vector, small or large B_CMAP8 icon) depends on the colorspace of the provided bitmap.



> [!NOTE]
> If the colorspace is B_CMAP8, B_CMAP8 icons are preferred. In that case, the bitmap size must also match the provided icon_size "size"!



**Since:** Haiku R1

---

### `GetVectorIcon()`

```cpp
static status_t BIconUtils::GetVectorIcon(BNode * node, const char * attrName, BBitmap * result)
```

Utility function to import a vector icon in "flat icon" format. 


Utility function to import a vector icon in "flat icon" format from a [BNode](../storage_kit/classBNode.md) attribute into the preallocated [BBitmap](classBBitmap.md) *result*. The colorspace of result needs to be B_RGBA32 or at least B_RGB32 (though that makes less sense). The icon will be scaled from its "native" size of 64x64 to the size of the bitmap.



> [!NOTE]
> The scale is derived from the bitmap width, the bitmap should have square dimension, or the icon will be cut off at the bottom (or have room left).



**Since:** Haiku R1

---

### `GetVectorIcon()`

```cpp
static status_t BIconUtils::GetVectorIcon(const uint8 * buffer, size_t size, BBitmap * result)
```

Utility function to import a vector icon in "flat icon" format. 


Utility function to import a vector icon in "flat icon" format from the given *buffer* into the preallocated [BBitmap](classBBitmap.md) *result*. The colorspace of result needs to be B_RGBA32 or at least B_RGB32 (though that makes less sense). The icon will be scaled from its "native" size of 64x64 to the size of the bitmap.



> [!NOTE]
> The scale is derived from the bitmap width, the bitmap should have square dimension, or the icon will be cut off at the bottom (or have room left).



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBIconUtils.html).
