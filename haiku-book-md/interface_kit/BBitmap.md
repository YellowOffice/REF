---
name: BBitmap
type: class
kit: interface_kit
brief: "Access and manipulate digital images commonly known as bitmaps"
source: haiku-book
---

# BBitmap Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Access and manipulate digital images commonly known as bitmaps. 


A [BBitmap](classBBitmap.md) is a rectangular map of pixel data. The [BBitmap](classBBitmap.md) class allows you to create a bitmap by specifying its pixel data and has operations for altering and accessing the properties of bitmaps.


To create a [BBitmap](classBBitmap.md) object use one of the constructor methods below. You can determine if initialization was successful by calling the [InitCheck()](classBBitmap.md#aba3ee96f8d1510df437a29dc000031ae) method. You can determine if a [BBitmap](classBBitmap.md) object is valid at any time by calling the [IsValid()](classBBitmap.md#ac8212018930f325d55c105fb4e3514ee) method.


An example of creating a new 32x32 pixel [BBitmap](classBBitmap.md) object and assigning the icon of the current application looks like this:



```cpp
BBitmap iconBitmap = new BBitmap(BRect(0, 0, 31, 31), B_RGBA32));
appFileInfo.GetIcon(iconBitmap, B_LARGE_ICON);
```

You can access the properties of a bitmap by calling the [Bounds()](classBBitmap.md#a1bdea44a85dfc1c8743d2ac30a324be6), [Flags()](classBBitmap.md#a8297355bf7c5374ec81fce8ea30d14f1), [ColorSpace()](classBBitmap.md#a2edc3ddc95fb6f2d09deda6ab3804ec8), [Area()](classBBitmap.md#ab345582f0870304b2800e4ed38880cd7), [Bits()](classBBitmap.md#afaee868ddc68f625fbf0ef99a5c0af8b), [BitsLength()](classBBitmap.md#a84afbb2b49a461d309d1a3b7a10c4c0e), [BytesPerRow()](classBBitmap.md#a4520f3a1dd50e093929d03dfb9e4e578), and [GetOverlayRestrictions()](classBBitmap.md#a75626d082fae29e89e29e7fb1317cd27) methods.


To directly set the pixel data of a bitmap call the [Bits()](classBBitmap.md#afaee868ddc68f625fbf0ef99a5c0af8b) or [SetBits()](classBBitmap.md#a33e76109224b86faa983cbe9c2f17cd0) methods or you can use the [ImportBits()](classBBitmap.md#a5c8636bc49535adf6fb5de8c492c976a) method to copy the bits from an existing bitmap.


You can also draw into a bitmap by attaching a child [BView](classBView.md) to the bitmap. To add and remove child [BView](classBView.md)'s to a bitmap call the [AddChild()](classBBitmap.md#a6ff37d55938b549ce17f98421261c677) and [RemoveChild()](classBBitmap.md#a280a222002a796ecb83ba89e3e37c6d8) methods respectively. You can access the child views of a bitmap by calling the [CountChildren()](classBBitmap.md#a8b3ba846da36f10f700c188f9337d78c), [ChildAt()](classBBitmap.md#af20f52333b3ec788b5b6345f5e659ab7), and [FindView()](classBBitmap.md#aa59171fe5e7e28e1502f27b2b294d09c) methods.


For off-screen bitmaps it is important to lock the bitmap before drawing the pixels and then unlock the bitmap when you are done to prevent flickering. To lock and unlock a bitmap call the [LockBits()](classBBitmap.md#a9b3ee36e63ffe3c2b65cc73e77232a4d) and UnLockBits() methods respectively. To lock and unlock the off-screen window that a bitmap resides in you should call the [Lock()](classBBitmap.md#a2ff4163d458a95c91fbc9f09de6a1043) and UnLock() methods. To determine is a bitmap is currently locked you can call the [IsLocked()](classBBitmap.md#a2249dd4cc01a8e26dd9d6858a894a189) method.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BBitmap](#aa14f1d313a76877cc8e4f39a6948ca0b) (area_id area, ptrdiff_t areaOffset, BRect bounds, uint32 flags, color_space colorSpace, int32 bytesPerRow=B_ANY_BYTES_PER_ROW, screen_id screenID=B_MAIN_SCREEN_ID) — Creates a BBitmap object inside of an existing memory area.
* [BBitmap](#aef910245967d6003df3fa84c3dc84821) (BMessage *data) — Unarchives a bitmap from a BMessage.
* [BBitmap](#a51c04ac9c8a86d002ed1b5e6e5edc248) (BRect bounds, color_space colorSpace, bool acceptsViews=false, bool needsContiguous=false) — Creates and initializes a BBitmap object.
* [BBitmap](#a44075e2478d2dc2189bd5cb1e8a3b4c8) (BRect bounds, uint32 flags, color_space colorSpace, int32 bytesPerRow=B_ANY_BYTES_PER_ROW, screen_id screenID=B_MAIN_SCREEN_ID) — Creates and initializes a BBitmap object.
* [BBitmap](#a6814786d752908d0430b647eb8d91ad8) (const BBitmap &source) — Creates a BBitmap object as a clone of another bitmap.
* [BBitmap](#ac4fea6b475b44ae26b4a772e569cf9ca) (const BBitmap &source, uint32 flags) — Creates a BBitmap object as a clone of another bitmap.
* [BBitmap](#a3eba6423633f71901121936ae614dc03) (const BBitmap *source, bool acceptsViews=false, bool needsContiguous=false) — Creates a BBitmap object as a clone of another bitmap.
* `virtual` [~BBitmap](#a29690d46af87471d8a478d559249dbbd) () — Destructor Method.
* `status_t` [InitCheck](#aba3ee96f8d1510df437a29dc000031ae) () const — Gets the status of the constructor.
* `bool` [IsValid](#ac8212018930f325d55c105fb4e3514ee) () const — Determines whether or not the BBitmap object is valid.
* `status_t` [LockBits](#a9b3ee36e63ffe3c2b65cc73e77232a4d) (uint32 *state=NULL) — Locks the bitmap bits so that they cannot be relocated.
* `void` [UnlockBits](#a43e2f9b6606e0a6681701688259b87a6) () — Unlocks the bitmap's buffer.
* `bool` [Lock](#a2ff4163d458a95c91fbc9f09de6a1043) () — Locks the off-screen window that belongs to the bitmap.
* `void` [Unlock](#a49f7e85512bc9f8013b1561e0056e283) () — Unlocks the off-screen window that belongs to the bitmap.
* `bool` [IsLocked](#a2249dd4cc01a8e26dd9d6858a894a189) () const — Determines whether or not the bitmap's off-screen window is locked.
* `area_id` [Area](#ab345582f0870304b2800e4ed38880cd7) () const — Gets the ID of the area the bitmap data reside in.
* `void *` [Bits](#afaee868ddc68f625fbf0ef99a5c0af8b) () const — Gets the pointer to the bitmap data.
* `size_t` [BitsLength](#a84afbb2b49a461d309d1a3b7a10c4c0e) () const — Gets the length of the bitmap data.
* `int32` [BytesPerRow](#a4520f3a1dd50e093929d03dfb9e4e578) () const — Gets the number of bytes used to store a row of bitmap data.
* `color_space` [ColorSpace](#a2edc3ddc95fb6f2d09deda6ab3804ec8) () const — Gets the bitmap's color space.
* `BRect` [Bounds](#a1bdea44a85dfc1c8743d2ac30a324be6) () const — Gets a BRect the size of the bitmap's dimensions.
* `uint32` [Flags](#a8297355bf7c5374ec81fce8ea30d14f1) () const — Accesses the bitmap's creation flags.
* `status_t` [GetOverlayRestrictions](#a75626d082fae29e89e29e7fb1317cd27) (overlay_restrictions *restrictions) const — Gets the overlay_restrictions structure for this bitmap.
* `virtual void` [AddChild](#a6ff37d55938b549ce17f98421261c677) (BView *view) — Adds a BView to the bitmap's view hierarchy.
* `virtual bool` [RemoveChild](#a280a222002a796ecb83ba89e3e37c6d8) (BView *view) — Removes a BView from the bitmap's view hierarchy.
* `int32` [CountChildren](#a8b3ba846da36f10f700c188f9337d78c) () const — Gets the number of BViews currently belonging to the bitmap.
* `BView *` [ChildAt](#af20f52333b3ec788b5b6345f5e659ab7) (int32 index) const — Gets the BView at a certain index in the bitmap's list of views.
* `BView *` [FindView](#aa59171fe5e7e28e1502f27b2b294d09c) (const char *viewName) const — Accesses a bitmap's child BView with the name viewName.
* `BView *` [FindView](#a10cd18788485595277d17f66cb974af7) (BPoint point) const — Accesses a bitmap's BView at a certain location.
* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).

### Archiving

* `virtual status_t` [Archive](#a331444d4bc838444f65f534cbbd66f41) (BMessage *data, bool deep=true) const — Archives the BBitmap object.
* `static BArchivable *` [Instantiate](#a224387ddb9077e37f917c15a3be85ed0) (BMessage *data) — Instantiates a BBitmap from an archive.

### Setters

* `status_t` [ImportBits](#a5c8636bc49535adf6fb5de8c492c976a) (const void *data, int32 length, int32 bpr, int32 offset, color_space colorSpace) — Assigns data to the bitmap.
* `status_t` [ImportBits](#aff7c2bfbc397e6df76e4f0633631f0bc) (const BBitmap *bitmap) — Assigns another bitmap's data to this bitmap.
* `void` [SetBits](#a33e76109224b86faa983cbe9c2f17cd0) (const void *data, int32 length, int32 offset, color_space colorSpace) — Assigns data to the bitmap.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BBitmap()`

```cpp
BBitmap::BBitmap(BRect bounds, uint32 flags, color_space colorSpace, int32 bytesPerRow = B_ANY_BYTES_PER_ROW, screen_id screenID = B_MAIN_SCREEN_ID)
```

Creates and initializes a [BBitmap](classBBitmap.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bounds` | The bitmap dimensions. |
| `flags` | Creation flags. |
| `colorSpace` | The bitmap's color space. |
| `bytesPerRow` | The number of bytes per row the bitmap should use. `B_ANY_BYTES_PER_ROW` to let the constructor choose an appropriate value. |
| `screenID` | Currently unused. May be used for multi-monitor support in the future. |





**Since:** Haiku R1

---

### `BBitmap()`

```cpp
BBitmap::BBitmap(BRect bounds, color_space colorSpace, bool acceptsViews = false, bool needsContiguous = false)
```

Creates and initializes a [BBitmap](classBBitmap.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bounds` | The bitmap dimensions. |
| `colorSpace` | The bitmap's color space. |
| `acceptsViews` | `true`, if the bitmap shall accept BViews, i.e. if it shall be possible to attach [BView](classBView.md) to the bitmap and draw into it. |
| `needsContiguous` | If `true` a physically contiguous chunk of memory will be allocated. |





**Since:** BeOS R3

---

### `BBitmap()`

```cpp
BBitmap::BBitmap(const BBitmap & source, uint32 flags)
```

Creates a [BBitmap](classBBitmap.md) object as a clone of another bitmap. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `source` | The source bitmap. |
| `flags` | Creation flags. |





**Since:** Haiku R1

---

### `BBitmap()`

```cpp
BBitmap::BBitmap(const BBitmap & source)
```

Creates a [BBitmap](classBBitmap.md) object as a clone of another bitmap. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `source` | The source bitmap. |





**Since:** Haiku R1

---

### `BBitmap()`

```cpp
BBitmap::BBitmap(const BBitmap * source, bool acceptsViews = false, bool needsContiguous = false)
```

Creates a [BBitmap](classBBitmap.md) object as a clone of another bitmap. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `source` | The source bitmap. |
| `acceptsViews` | `true`, if the bitmap shall accept BViews, i.e. if it shall be possible to attach [BView](classBView.md) to the bitmap and draw into it. |
| `needsContiguous` | If `true` a physically contiguous chunk of memory will be allocated. |





**Since:** Haiku R1

---

### `BBitmap()`

```cpp
BBitmap::BBitmap(area_id area, ptrdiff_t areaOffset, BRect bounds, uint32 flags, color_space colorSpace, int32 bytesPerRow = B_ANY_BYTES_PER_ROW, screen_id screenID = B_MAIN_SCREEN_ID)
```

Creates a [BBitmap](classBBitmap.md) object inside of an existing memory area. 


This method is useful if you want to create a [BBitmap](classBBitmap.md) on top of existing memory or want to share a [BBitmap](classBBitmap.md) between two or more applications.


This [BBitmap](classBBitmap.md) should be deleted before the area is deleted.


Parameters

| Parameter | Description |
| :--- | :--- |
| `area` | The memory area to use |
| `areaOffset` | Offset within the memory area to place bitmap. |
| `bounds` | The bitmap dimensions. |
| `flags` | Creation flags. |
| `colorSpace` | The bitmap's color space. |
| `bytesPerRow` | The number of bytes per row the bitmap should use. `B_ANY_BYTES_PER_ROW` to let the constructor choose an appropriate value. |
| `screenID` | Currently unused. May be used for multi-monitor support in the future. |





**Since:** Haiku R1

---

### `~BBitmap()`

```cpp
BBitmap::~BBitmap()
```

Destructor Method. 


Frees all resources associated with this object.



**Since:** BeOS R3

---

### `BBitmap()`

```cpp
BBitmap::BBitmap(BMessage * data)
```

Unarchives a bitmap from a [BMessage](../application_kit/classBMessage.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The archive. |





**Since:** BeOS R3

---

### `AddChild()`

```cpp
void BBitmap::AddChild(BView * view)
```

Adds a [BView](classBView.md) to the bitmap's view hierarchy. 


The bitmap must accept views and the supplied view must not be child of another parent.


Parameters

| Parameter | Description |
| :--- | :--- |
| `view` | The view to be added. |





**Since:** BeOS R3

---

### `Archive()`

```cpp
status_t BBitmap::Archive(BMessage * data, bool deep = true)const
```

Archives the [BBitmap](classBBitmap.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The archive. |
| `deep` | if `true`, child object will be archived as well. |





**Returns:** `B_OK`, if everything went fine, an error code otherwise.



**Since:** BeOS R3


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44).

---

### `Area()`

```cpp
area_id BBitmap::Area()const
```

Gets the ID of the area the bitmap data reside in. 



**Returns:** The ID of the area the bitmap data reside in.



**Since:** Haiku R1

---

### `Bits()`

```cpp
void * BBitmap::Bits()const
```

Gets the pointer to the bitmap data. 



**Returns:** The pointer to the bitmap data.



**Since:** BeOS R3

---

### `BitsLength()`

```cpp
int32 BBitmap::BitsLength()const
```

Gets the length of the bitmap data. 



**Returns:** The length of the bitmap data as an int32.



**Since:** BeOS R3

---

### `Bounds()`

```cpp
BRect BBitmap::Bounds()const
```

Gets a [BRect](classBRect.md) the size of the bitmap's dimensions. 



**Returns:** A [BRect](classBRect.md) the size of the bitmap's dimensions.



**Since:** BeOS R3

---

### `BytesPerRow()`

```cpp
int32 BBitmap::BytesPerRow()const
```

Gets the number of bytes used to store a row of bitmap data. 



**Returns:** The number of bytes used to store a row of bitmap data.



**Since:** BeOS R3

---

### `ChildAt()`

```cpp
BView * BBitmap::ChildAt(int32 index)const
```

Gets the [BView](classBView.md) at a certain index in the bitmap's list of views. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index of the [BView](classBView.md) to be returned. |





**Returns:** The [BView](classBView.md) at index *index* or `NULL` if the index is out of range.



**Since:** BeOS R3

---

### `ColorSpace()`

```cpp
color_space BBitmap::ColorSpace()const
```

Gets the bitmap's color space. 



**Returns:** The bitmap's color space.



**Since:** BeOS R3

---

### `CountChildren()`

```cpp
int32 BBitmap::CountChildren()const
```

Gets the number of BViews currently belonging to the bitmap. 



**Returns:** The number of BViews currently belonging to the bitmap.



**Since:** BeOS R3

---

### `FindView()`

```cpp
BView * BBitmap::FindView(BPoint point)const
```

Accesses a bitmap's [BView](classBView.md) at a certain location. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The location. |





**Returns:** The [BView](classBView.md) with located at *point* or `NULL` if the bitmap doesn't know a view at this location.



**Since:** BeOS R3

---

### `FindView()`

```cpp
BView * BBitmap::FindView(const char * viewName)const
```

Accesses a bitmap's child [BView](classBView.md) with the name *viewName*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `viewName` | The name of the [BView](classBView.md) to be returned. |





**Returns:** The [BView](classBView.md) with the name *name* or `NULL` if the bitmap doesn't know a view with that name.



**Since:** BeOS R3

---

### `Flags()`

```cpp
uint32 BBitmap::Flags()const
```

Accesses the bitmap's creation flags. 


This method informs about which flags have been used to create the bitmap. It would for example tell you wether this is an overlay bitmap. If bitmap creation succeeded, all flags are fulfilled.



**Returns:** The bitmap's creation flags.



**Since:** Haiku R1

---

### `GetOverlayRestrictions()`

```cpp
status_t BBitmap::GetOverlayRestrictions(overlay_restrictions * restrictions)const
```

Gets the overlay_restrictions structure for this bitmap. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `restrictions` | The overlay restrictions flag |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The overlay restriction structure was found. |
| B_BAD_TYPE | The overlay restriction structure for the bitmap could not be found. |





**Since:** Haiku R1

---

### `ImportBits()`

```cpp
status_t BBitmap::ImportBits(const BBitmap * bitmap)
```

Assigns another bitmap's data to this bitmap. 


The supplied bitmap must have the exact same dimensions as this bitmap. Its data is converted to the color space of this bitmap.


The currently supported source/target color spaces are `B_RGB{32,24,16,15}[_BIG]`, `B_CMAP8` and `B_GRAY{8,1}`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The source bitmap. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The bits were imported into the bitmap. |
| B_BAD_VALUE | `NULL` *bitmap*, or *bitmap* has other dimensions, or the conversion from or to one of the color spaces is not supported. |





**Since:** Haiku R1

---

### `ImportBits()`

```cpp
status_t BBitmap::ImportBits(const void * data, int32 length, int32 bpr, int32 offset, color_space colorSpace)
```

Assigns data to the bitmap. 


Data are directly written into the bitmap's data buffer, being converted beforehand, if necessary. Unlike for [SetBits()](classBBitmap.md#a33e76109224b86faa983cbe9c2f17cd0), the meaning of *colorSpace* is exactly the expected one here, i.e. the source buffer is supposed to contain data of that color space. *bpr* specifies how many bytes the source contains per row. `B_ANY_BYTES_PER_ROW` can be supplied, if standard padding to int32 is used.


The currently supported source/target color spaces are `B_RGB{32,24,16,15}[_BIG]`, `B_CMAP8` and `B_GRAY{8,1}`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The data to be copied. |
| `length` | The length in bytes of the data to be copied. |
| `bpr` | The number of bytes per row in the source data. |
| `offset` | The offset (in bytes) relative to beginning of the bitmap data specifying the position at which the source data shall be written. |
| `colorSpace` | Color space of the source data. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The bits were imported into the bitmap. |
| B_BAD_VALUE | `NULL` *data*, invalid *bpr* or *offset*, or unsupported *colorSpace*. |





**Since:** Haiku R1

---

### `InitCheck()`

```cpp
status_t BBitmap::InitCheck()const
```

Gets the status of the constructor. 



**Returns:** B_OK if initialization succeeded, otherwise returns an error status.



**Since:** Haiku R1

---

### `Instantiate()`

```cpp
BArchivable * BBitmap::Instantiate(BMessage * data)
```

Instantiates a [BBitmap](classBBitmap.md) from an archive. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The archive. |





**Returns:** A bitmap reconstructed from the archive or `NULL` if an error occurred.



**Since:** BeOS R3

---

### `IsLocked()`

```cpp
bool BBitmap::IsLocked()const
```

Determines whether or not the bitmap's off-screen window is locked. 


The bitmap must accept views, if locking should work.



**Returns:** `true`, if the caller owns a lock , `false` otherwise.



**Since:** BeOS R4

---

### `IsValid()`

```cpp
bool BBitmap::IsValid()const
```

Determines whether or not the [BBitmap](classBBitmap.md) object is valid. 



**Returns:** `true`, if the object is properly initialized, `false` otherwise.



**Since:** BeOS R3

---

### `Lock()`

```cpp
bool BBitmap::Lock()
```

Locks the off-screen window that belongs to the bitmap. 


The bitmap must accept views, if locking should work.



**Returns:** `true`, if the lock was acquired successfully.



**Since:** BeOS R3

---

### `LockBits()`

```cpp
status_t BBitmap::LockBits(uint32 * state = NULL)
```

Locks the bitmap bits so that they cannot be relocated. 


This is currently only used for overlay bitmaps; whenever you need to access their [Bits()](classBBitmap.md#afaee868ddc68f625fbf0ef99a5c0af8b) you must lock them first. On resolution change overlay bitmaps can be relocated in memory; using this call prevents you from accessing an invalid pointer and clobbering memory that doesn't belong you.


Parameters

| Parameter | Description |
| :--- | :--- |
| `state` | Unused |





**Returns:** `B_OK` on success or an error status code.



**Since:** Haiku R1

---

### `RemoveChild()`

```cpp
bool BBitmap::RemoveChild(BView * view)
```

Removes a [BView](classBView.md) from the bitmap's view hierarchy. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `view` | The view to be removed. |





**Since:** BeOS R3

---

### `SetBits()`

```cpp
void BBitmap::SetBits(const void * data, int32 length, int32 offset, color_space colorSpace)
```

Assigns data to the bitmap. 


Data are directly written into the bitmap's data buffer, being converted beforehand, if necessary. Some conversions do not work intuitively:


* `B_RGB32:` The source buffer is supposed to contain `B_RGB24_BIG` data without padding at the end of the rows.

* `B_RGB32:` The source buffer is supposed to contain `B_CMAP8` data without padding at the end of the rows.

* other color spaces: The source buffer is supposed to contain data according to the specified color space being padded to int32 row-wise.



The currently supported source/target color spaces are `B_RGB{32,24,16,15}[_BIG]`, `B_CMAP8` and `B_GRAY{8,1}`.



> [!NOTE]
> Since this methods is a bit strange to use, Haiku has introduced the [ImportBits()](classBBitmap.md#a5c8636bc49535adf6fb5de8c492c976a) method which is the recommended replacement.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The data to be copied. |
| `length` | The length in bytes of the data to be copied. |
| `offset` | The offset (in bytes) relative to beginning of the bitmap data specifying the position at which the source data shall be written. |
| `colorSpace` | Color space of the source data. |





**Since:** BeOS R3

---

### `Unlock()`

```cpp
void BBitmap::Unlock()
```

Unlocks the off-screen window that belongs to the bitmap. 


The bitmap must accept views, if locking should work.



**Since:** BeOS R3

---

### `UnlockBits()`

```cpp
void BBitmap::UnlockBits()
```

Unlocks the bitmap's buffer. 


Counterpart to [BBitmap::LockBits()](classBBitmap.md#a9b3ee36e63ffe3c2b65cc73e77232a4d).



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBBitmap.html).
