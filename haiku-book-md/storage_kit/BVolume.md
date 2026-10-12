---
name: BVolume
type: class
kit: storage_kit
brief: "Provides an interface for querying information about a volume"
source: haiku-book
---

# BVolume Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Provides an interface for querying information about a volume. 


The class is a simple wrapper for a `dev_t` and the function fs_stat_dev(). The sole exception is the [SetName()](classBVolume.md#ae8859832bad50bdbca612a6fc8d4d28d) method which sets the name of the volume.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BVolume](#a8f6173dffb815b5ef2c2e0e620f016c9) () — Creates an uninitialized BVolume object.
* [BVolume](#aec15671d19785fe1f9233b990709fbfa) (const BVolume &volume) — Creates a copy of the supplied BVolume object.
* [BVolume](#af555371e8b3fb6168a9d8c95270c0925) (dev_t device) — Creates a BVolume and initializes it to the volume specified by the supplied device ID.
* `virtual` [~BVolume](#aa410e15258ee5f43e7cbb89e748da41e) () — Destroys the object and frees all associated resources.
* `status_t` [InitCheck](#a71b630674769adcf5165bf1f255cb36e) () const — Returns the initialization status.
* `status_t` [SetTo](#a8e7fb58eeb125c8d3df8b4e147d4e799) (dev_t device) — Initializes the object to refer to the volume specified by the supplied device ID.
* `void` [Unset](#a04a707681b76b9ca5d065cb139df1624) () — Brings the BVolume object to an uninitialized state.
* `dev_t` [Device](#ad32bd56756869253d453462db83c9736) () const — Returns the device ID of the volume the object refers to.
* `status_t` [GetRootDirectory](#ae6d852cc0abc041c61faa6ae1eec821d) (BDirectory *directory) const — Writes the root directory of the volume referred to by this object into directory.
* `off_t` [Capacity](#a2297feebf44070937968baf5cee423b9) () const — Returns the total storage capacity of the volume.
* `off_t` [FreeBytes](#adc1455af7c2965cff25ce27aee2a6a1c) () const — Returns the amount of unused space on the volume (in bytes).
* `off_t` [BlockSize](#aaba08f5d228e1eae2394c98b159d3892) () const — Returns the size of one block (in bytes). The meaning of this depends on the underlying file system.
* `status_t` [GetName](#aeb6276fe72466393d6d70e913c248a98) (char *name) const — Writes the volume's name into the provided buffer.
* `status_t` [SetName](#ae8859832bad50bdbca612a6fc8d4d28d) (const char *name) — Sets the volume's name to name.
* `status_t` [GetIcon](#a019efbe0a8b1c7e14114c0548bb53f26) (BBitmap *icon, icon_size which) const — Writes the volume's icon into the supplied BBitmap.
* `status_t` [GetIcon](#ab75f70af9be3707acb2e6679b99972ce) (uint8 **_data, size_t *_size, type_code *_type) const — Writes the volume's icon data into the supplied uint8 array.
* `bool` [IsRemovable](#a683a6da4ffddc999046b300a67bf50d0) () const — Returns whether or not the volume is removable.
* `bool` [IsReadOnly](#aefb65574a89b9334138a1f91e5b9c553) () const — Returns whether or not the volume is read-only.
* `bool` [IsPersistent](#a17fc9a8ce1faff8d5c66204c7f6a5136) () const — Returns whether or not the volume is persistent.
* `bool` [IsShared](#ae4bb784b1ec4e223c48b325ec3da1629) () const — Returns whether or not the volume is shared.
* `bool` [KnowsMime](#a922bf20e0534d25f7c9a60018466165e) () const — Returns whether or not the volume supports MIME-types.
* `bool` [KnowsAttr](#ad3915085dd2c050fba991df8b1b03efb) () const — Returns whether or not the volume supports attributes.
* `bool` [KnowsQuery](#a942229b70906574c9d1c6e889eebc9f4) () const — Returns whether or not the volume supports queries.
* `bool` [operator==](#a79e29ad11342ace8b169068d2cedf145) (const BVolume &volume) const — Returns whether or not the supplied BVolume object is equal to this object.
* `bool` [operator!=](#a137a479c41a98ba1e6cfaade22651edc) (const BVolume &volume) const — Returns whether or not the supplied BVolume object is NOT equal to this object.
* `BVolume &` [operator=](#a17819662a45f1a700dbfeb2490b7faf3) (const BVolume &volume) — Assigns the supplied BVolume object to this volume, this object is made to be an exact clone of the supplied one.

## Detailed Member Documentation

### `BVolume()`

```cpp
BVolume::BVolume()
```

Creates an uninitialized [BVolume](classBVolume.md) object. 


[InitCheck()](classBVolume.md#a71b630674769adcf5165bf1f255cb36e) will return `B_NO_INIT`.



**See also:** [SetTo()](classBVolume.md#a8e7fb58eeb125c8d3df8b4e147d4e799)



**Since:** BeOS R3

---

### `BVolume()`

```cpp
BVolume::BVolume(dev_t device)
```

Creates a [BVolume](classBVolume.md) and initializes it to the volume specified by the supplied device ID. 


[InitCheck()](classBVolume.md#a71b630674769adcf5165bf1f255cb36e) should be called afterwards to check if initialization was successful.


Parameters

| Parameter | Description |
| :--- | :--- |
| `device` | The device ID of the volume. |





**Since:** BeOS R3

---

### `BVolume()`

```cpp
BVolume::BVolume(const BVolume & volume)
```

Creates a copy of the supplied [BVolume](classBVolume.md) object. 


Afterwards the object refers to the same device the supplied object does. If the latter is not properly initialized, this result isn't either.


Parameters

| Parameter | Description |
| :--- | :--- |
| `volume` | The volume object to be copied. |





**Since:** BeOS R3

---

### `~BVolume()`

```cpp
BVolume::~BVolume()
```

Destroys the object and frees all associated resources. 



**Since:** BeOS R3

---

### `BlockSize()`

```cpp
off_t BVolume::BlockSize()const
```

Returns the size of one block (in bytes). The meaning of this depends on the underlying file system. 



**Returns:** The block size in bytes, `B_NO_INIT` if the volume is not initialized or other errors forwarded from the file system.



**Since:** Haiku R1

---

### `Capacity()`

```cpp
off_t BVolume::Capacity()const
```

Returns the total storage capacity of the volume. 



**Returns:** The volume's total storage capacity (in bytes), or `B_BAD_VALUE` if the object is not properly initialized.



**See also:** [FreeBytes()](classBVolume.md#adc1455af7c2965cff25ce27aee2a6a1c)



**Since:** BeOS R3

---

### `Device()`

```cpp
dev_t BVolume::Device()const
```

Returns the device ID of the volume the object refers to. 



**Returns:** Returns the device ID of the volume the object refers to or -1 if the object was not properly initialized.



**Since:** BeOS R3

---

### `FreeBytes()`

```cpp
off_t BVolume::FreeBytes()const
```

Returns the amount of unused space on the volume (in bytes). 



**Returns:** The amount of unused space on the volume (in bytes), or `B_BAD_VALUE` if the object is not properly initialized.



**Since:** BeOS R3

---

### `GetIcon()`

```cpp
status_t BVolume::GetIcon(BBitmap * icon, icon_size which)const
```

Writes the volume's icon into the supplied [BBitmap](../interface_kit/classBBitmap.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `icon` | A pointer to a pre-allocated [BBitmap](../interface_kit/classBBitmap.md) of the correct dimension to store the requested icon (16x16 for the mini and 32x32 for the large icon). |
| `which` | The icon size to be retrieved: `B_MINI_ICON` for the mini or `B_LARGE_ICON` for the large icon. |





**Since:** BeOS R4

---

### `GetIcon()`

```cpp
status_t BVolume::GetIcon(uint8 ** _data, size_t * _size, type_code * _type)const
```

Writes the volume's icon data into the supplied `uint8` array. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `_data` | A pointer to a pointer to a pre-allocated `uint8` array of the correct size to store the requested icon. |
| `_size` | The size of the retrieved icon (in bytes). |
| `_type` | The type code of the retrieve icon. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | Object was not properly initialized. |





**See also:** fs_stat_dev() for more return codes.



**Since:** Haiku R1

---

### `GetName()`

```cpp
status_t BVolume::GetName(char * name)const
```

Writes the volume's name into the provided buffer. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | A pointer to a pre-allocated character buffer of size `B_FILE_NAME_LENGTH` or larger into which the name of the volume is written. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *name* was `NULL` or the object was not properly initialized. |





**See also:** [SetName()](classBVolume.md#ae8859832bad50bdbca612a6fc8d4d28d)



**Since:** BeOS R3

---

### `GetRootDirectory()`

```cpp
status_t BVolume::GetRootDirectory(BDirectory * directory)const
```

Writes the root directory of the volume referred to by this object into *directory*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `directory` | A pointer to a pre-allocated [BDirectory](classBDirectory.md) to be initialized to the volume's root directory. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *directory* was `NULL` or the object was not properly initialized. |





**Since:** BeOS R3

---

### `InitCheck()`

```cpp
status_t BVolume::InitCheck(void)const
```

Returns the initialization status. 



**Returns:** `B_OK` if the object was properly initialized, or an error code otherwise.



**Since:** BeOS R3

---

### `IsPersistent()`

```cpp
bool BVolume::IsPersistent(void)const
```

Returns whether or not the volume is persistent. 



**Returns:** `true`, if the volume was properly initialized and is persistent, `false` otherwise.



**Since:** BeOS R3

---

### `IsReadOnly()`

```cpp
bool BVolume::IsReadOnly(void)const
```

Returns whether or not the volume is read-only. 



**Returns:** `true`, if the volume was properly initialized and is read-only, `false` otherwise.



**Since:** BeOS R3

---

### `IsRemovable()`

```cpp
bool BVolume::IsRemovable()const
```

Returns whether or not the volume is removable. 



**Returns:** `true`, if the volume was properly initialized and is removable, `false` otherwise.



**Since:** BeOS R3

---

### `IsShared()`

```cpp
bool BVolume::IsShared(void)const
```

Returns whether or not the volume is shared. 


return `true`, if the volume was properly initialized and is shared, `false` otherwise.



**Since:** BeOS R3

---

### `KnowsAttr()`

```cpp
bool BVolume::KnowsAttr(void)const
```

Returns whether or not the volume supports attributes. 



**Returns:** `true`, if the volume was properly initialized and supports attributes, `false` otherwise.



**Since:** BeOS R3

---

### `KnowsMime()`

```cpp
bool BVolume::KnowsMime(void)const
```

Returns whether or not the volume supports MIME-types. 



**Returns:** `true`, if the volume was properly initialized and supports MIME-types, `false` otherwise.



**Since:** BeOS R3

---

### `KnowsQuery()`

```cpp
bool BVolume::KnowsQuery(void)const
```

Returns whether or not the volume supports queries. 



**Returns:** `true`, if the volume was properly initialized and supports queries, `false` otherwise.



**Since:** BeOS R3

---

### `operator!=()`

```cpp
bool BVolume::operator!=(const BVolume & volume)const
```

Returns whether or not the supplied [BVolume](classBVolume.md) object is NOT equal to this object. 


Two volume objects are said to be unequal if one is initialized and the other is not or if they are both initialized and refer to the different volumes.


Parameters

| Parameter | Description |
| :--- | :--- |
| `volume` | The volume to be tested for inequality. |





**Returns:** `true`, if the objects and unequal, `false` otherwise.



**Since:** BeOS R3

---

### `operator=()`

```cpp
BVolume & BVolume::operator=(const BVolume & volume)
```

Assigns the supplied [BVolume](classBVolume.md) object to this volume, this object is made to be an exact clone of the supplied one. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `volume` | The volume to be assigned. |





**Returns:** A reference to this object.



**Since:** BeOS R3

---

### `operator==()`

```cpp
bool BVolume::operator==(const BVolume & volume)const
```

Returns whether or not the supplied [BVolume](classBVolume.md) object is equal to this object. 


Two volume objects are said to be equal if they are both uninitialized, or they are both initialized and refer to the same volume.


Parameters

| Parameter | Description |
| :--- | :--- |
| `volume` | The volume to be tested for equality. |





**Returns:** `true`, if the objects are equal, `false` otherwise.



**Since:** BeOS R3

---

### `SetName()`

```cpp
status_t BVolume::SetName(const char * name)
```

Sets the volume's name to *name*. 



> [!NOTE]
> The R5 implementation checks if an entry with the volume's old name exists in the root directory and renames that entry, if it is indeed the mount point of the volume (or a link referring to it). In all other cases, nothing is done (even if the mount point is named like the volume, but lives in a different directory). We follow suit for the time being.



> [!WARNING]
> If the volume name is set to "boot" this method tries to rename it to /boot, but is prevented by the kernel.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The new name of the volume, must not be longer than `B_FILE_NAME_LENGTH` (including the terminating `NULL`). |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *name* was `NULL` or the object was not properly initialized. |
| B_NAME_TOO_LONG | *name* was >= `B_FILE_NAME_LENGTH`. |





**Since:** BeOS R4

---

### `SetTo()`

```cpp
status_t BVolume::SetTo(dev_t device)
```

Initializes the object to refer to the volume specified by the supplied device ID. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `device` | The device ID of the volume to set. |





**Returns:** `B_OK` if the object was properly initialized, or an error code otherwise.



**Since:** BeOS R3

---

### `Unset()`

```cpp
void BVolume::Unset()
```

Brings the [BVolume](classBVolume.md) object to an uninitialized state. 


[InitCheck()](classBVolume.md#a71b630674769adcf5165bf1f255cb36e) will return `B_NO_INIT`.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBVolume.html).
