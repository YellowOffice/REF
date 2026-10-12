---
name: entry_ref
type: struct
kit: storage_kit
brief: "A filesystem entry represented as a name in a concrete directory"
source: haiku-book
---

# entry_ref Struct
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A filesystem entry represented as a name in a concrete directory. 


entry_refs may refer to pre-existing (concrete) files, as well as non-existing (abstract) files. However, the parent directory of the file **must** exist.


The result of this dichotomy is a blending of the persistence gained by referring to entries with a reference to their internal filesystem node and the flexibility gained by referring to entries by name.


For example, if the directory in which the entry resides (or a directory further up in the hierarchy) is moved or renamed, the [entry_ref](structentry__ref.md) will still refer to the correct file (whereas a pathname to the previous location of the file would now be invalid).


On the other hand, say that the [entry_ref](structentry__ref.md) refers to a concrete file. If the file itself is renamed, the [entry_ref](structentry__ref.md) now refers to an abstract file with the old name (the upside in this case is that abstract entries may be represented by entry_refs without preallocating an internal filesystem node for them).



**Since:** BeOS R3

## Member List

### Public Member Functions

* [entry_ref](#a39ba3aeac531e62b763652d472eb7966) () — Creates an uninitialized entry_ref object.
* [entry_ref](#a86eda326144993e27c641ae9375e4158) (const entry_ref &ref) — Returns a copy of the passed in entry_ref object.
* [entry_ref](#aca0272efd9c83fe7c277924665c94f2a) (dev_t dev, ino_t dir, const char *name) — Creates an entry_ref object initialized to the given file name in the given directory on the given device.
* [~entry_ref](#a0e47f2daa48291c66c67e05e523303a1) () — Destroys the object and frees the storage allocated for the leaf name, if necessary.
* `bool` [operator!=](#a191c15337dc3ea9d2d6bee9bff4854f1) (const entry_ref &ref) const — Compares the entry_ref object with the passed in entry_ref, returning true if they are NOT equal.
* `entry_ref &` [operator=](#aba8ea743e1330f8974265dff71ed6f7f) (const entry_ref &ref) — Makes the entry_ref object a copy of the passed in entry_ref.
* `bool` [operator==](#aab525d740557f80a178348a201da2a1e) (const entry_ref &ref) const — Compares the entry_ref object with the passed in entry_ref, returning true if they are equal.
* `status_t` [set_name](#a133891c3bf1cf3f41026a3d43ac466cb) (const char *name) — Set the leaf name of entry_ref freeing the storage allocated for any previous name and then making a copy of the new name.

### Public Attributes

* `dev_t` [device](#ac7e65996d6b3ff031dd6d529e4387c08)
* `ino_t` [directory](#a3cb9497db4d8f1f842dbe9ab4fe04703)
* `char *` [name](#a1b166a335d750f337cd531c43b09d49b)

## Detailed Member Documentation

### `entry_ref()`

```cpp
entry_ref::entry_ref()
```

Creates an uninitialized `entry_ref` object. 



**Since:** BeOS R3

---

### `entry_ref()`

```cpp
entry_ref::entry_ref(dev_t dev, ino_t dir, const char * name)
```

Creates an `entry_ref` object initialized to the given file name in the given directory on the given device. 


*name* may refer to either a pre-existing file in the given directory, or a non-existent file. No explicit checking is done to verify validity of the given arguments, but later use of the `entry_ref` will fail if `dev` is not a valid device or *dir* is a not a directory on `dev`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `dev` | The *device* on which the entry's parent directory resides. |
| `dir` | The directory in which the entry resides. |
| `name` | The leaf name of the entry, which is not required to exist. |





**Since:** BeOS R3

---

### `entry_ref()`

```cpp
entry_ref::entry_ref(const entry_ref & ref)
```

Returns a copy of the passed in `entry_ref` object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | A reference to an `entry_ref` to copy. |





**Since:** BeOS R3

---

### `~entry_ref()`

```cpp
entry_ref::~entry_ref()
```

Destroys the object and frees the storage allocated for the leaf name, if necessary. 



**Since:** BeOS R3

---

### `operator!=()`

```cpp
bool entry_ref::operator!=(const entry_ref & ref)const
```

Compares the [entry_ref](structentry__ref.md) object with the passed in `entry_ref`, returning `true` if they are NOT equal. 



**Returns:** `true` if the *ref* is NOT equal to this `entry_ref`, `false` otherwise.



**Since:** BeOS R3

---

### `operator=()`

```cpp
entry_ref & entry_ref::operator=(const entry_ref & ref)
```

Makes the `entry_ref` object a copy of the passed in `entry_ref`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The `entry_ref` to copy. |





**Returns:** A pointer to the resulting `entry_ref` copy.



**Since:** BeOS R5

---

### `operator==()`

```cpp
bool entry_ref::operator==(const entry_ref & ref)const
```

Compares the `entry_ref` object with the passed in `entry_ref`, returning `true` if they are equal. 



**Returns:** `true` if the *ref* is equal to this `entry_ref`, `false` otherwise.



**Since:** BeOS R3

---

### `set_name()`

```cpp
status_t entry_ref::set_name(const char * name)
```

Set the leaf name of `entry_ref` freeing the storage allocated for any previous name and then making a copy of the new name. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | Pointer to a null-terminated string containing the new name for the entry. May be `NULL`. |





**Since:** BeOS R3

---

### `device`

```cpp
dev_t entry_ref::device
```

The device id of the storage device on which the entry resides.



**Since:** BeOS R3

---

### `directory`

```cpp
ino_t entry_ref::directory
```

The inode number of the directory in which the entry resides.



**Since:** BeOS R3

---

### `name`

```cpp
char * entry_ref::name
```

The leaf name of the entry



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structentry__ref.html).
