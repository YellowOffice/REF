---
name: BEntryList
type: class
kit: storage_kit
brief: "Interface for iterating through a list of filesystem entries"
source: haiku-book
---

# BEntryList Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Interface for iterating through a list of filesystem entries. 


Interface for iterating through a list of filesystem entries Defines a general interface for iterating through a list of entries (i.e. files in a folder


Defines a general interface for iterating through a list of entries i.e. files in a folder.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BEntryList](#adf5344c4229922691642b6e07c29bcaa) () — Creates a BEntryList object.
* `virtual` [~BEntryList](#ac239f4229be2d0a1c9a58c83f503be4c) () — Frees all resources associated with the BEntryList object.
* `virtual int32` [CountEntries](#a290b792f7b12265c10ba589aa969b862) ()=0 — Returns the number of entries in the list.
* `virtual int32` [GetNextDirents](#a2f8498249c876866d5f53a8b89044871) (struct dirent *direntBuffer, size_t bufferSize, int32 maxEntries=INT_MAX)=0 — Returns the BEntryList's next entries as dirent structures.
* `virtual status_t` [GetNextEntry](#a52e6c79344a6e511e7890f008e7281d1) (BEntry *entry, bool traverse=false)=0 — Returns the BEntryList's next entry as a BEntry.
* `virtual status_t` [GetNextRef](#a908ff7149239ab66683b12b27be917ee) (entry_ref *ref)=0 — Returns the BEntryList's next entry as an entry_ref.
* `virtual status_t` [Rewind](#a6cbcd041425e5a1225a762c72a4eb8af) ()=0 — Rewinds the list pointer to the beginning of the list.

## Detailed Member Documentation

### `BEntryList()`

```cpp
BEntryList::BEntryList()
```

Creates a [BEntryList](classBEntryList.md) object. 


Does nothing at this time.



**Since:** Haiku R1

---

### `~BEntryList()`

```cpp
BEntryList::~BEntryList()
```

Frees all resources associated with the [BEntryList](classBEntryList.md) object. 


Does nothing at this time.



**Since:** Haiku R1

---

### `CountEntries()`

```cpp
int32 BEntryList::CountEntries()
```

Returns the number of entries in the list. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | if successful |
| B_ENTRY_NOT_FOUND | when at the end of the list |
| B_ERROR | or another error code (depending on the implementation of the derived class). |





**Since:** BeOS R3


Implemented in [BDirectory](classBDirectory.md#a9408e42d1c0683cd97991e8d3ac0b41f), and [BQuery](classBQuery.md#ab57f2b6d7a84c557f77a77d3baaca421).

---

### `GetNextDirents()`

```cpp
int32 BEntryList::GetNextDirents(struct dirent * buf, size_t length, int32 count = INT_MAX)
```

Returns the [BEntryList](classBEntryList.md)'s next entries as dirent structures. 


Reads a number of entries into the array of dirent structures pointed to by *buf*. Reads as many but no more than *count* entries, as many entries as remain, or as many entries as will fit into the array at *buf* with given length *length* (in bytes), whichever is smallest.


Parameters

| Parameter | Description |
| :--- | :--- |
| `buf` | A pointer to a buffer to be filled with dirent structures of the found entries. |
| `length` | The length of the *buf* array. |
| `count` | the maximum number of entries to be read. |





> [!NOTE]
> The iterator used by this method is the same one used by [GetNextEntry()](classBEntryList.md#a52e6c79344a6e511e7890f008e7281d1), [GetNextRef()](classBEntryList.md#a908ff7149239ab66683b12b27be917ee), [Rewind()](classBEntryList.md#a6cbcd041425e5a1225a762c72a4eb8af) and [CountEntries()](classBEntryList.md#a290b792f7b12265c10ba589aa969b862).



**Returns:** * The number of dirent structures stored in the buffer or 0 when there are no more entries to be read.

* an error code (depending on the implementation of the derived class) if an error occurred.



**Since:** BeOS R3


Implemented in [BDirectory](classBDirectory.md#ad163bac44f24104b1cd336487114e2fe), and [BQuery](classBQuery.md#af5a9ba3e24f68c59b1247b7181433d23).

---

### `GetNextEntry()`

```cpp
status_t BEntryList::GetNextEntry(BEntry * entry, bool traverse = false)
```

Returns the [BEntryList](classBEntryList.md)'s next entry as a [BEntry](classBEntry.md). 


Places the next entry in the list in *entry*, traversing symlinks if *traverse* is `true`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | a pointer to a [BEntry](classBEntry.md) to be initialized with the found entry. |
| `traverse` | specifies whether to follow it, if the found entry is a symbolic link. |





> [!NOTE]
> The iterator used by this method is the same one used by [GetNextRef()](classBEntryList.md#a908ff7149239ab66683b12b27be917ee), [GetNextDirents()](classBEntryList.md#a2f8498249c876866d5f53a8b89044871), [Rewind()](classBEntryList.md#a6cbcd041425e5a1225a762c72a4eb8af) and [CountEntries()](classBEntryList.md#a290b792f7b12265c10ba589aa969b862).


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | if successful |
| B_ENTRY_NOT_FOUND | when at the end of the list |
| B_ERROR | or another error code (depending on the implementation of the derived class). |





**Since:** BeOS R3


Implemented in [BDirectory](classBDirectory.md#afc19ccbfe069ccd6d800d368eab24008), and [BQuery](classBQuery.md#ab30c05e8425a5c39dd35bd5fe5b05748).

---

### `GetNextRef()`

```cpp
status_t BEntryList::GetNextRef(entry_ref * ref)
```

Returns the [BEntryList](classBEntryList.md)'s next entry as an [entry_ref](structentry__ref.md). 


Places an [entry_ref](structentry__ref.md) to the next entry in the list into *ref*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | a pointer to an [entry_ref](structentry__ref.md) to be filled in with the data of the found entry. |





> [!NOTE]
> The iterator used by this method is the same one used by [GetNextEntry()](classBEntryList.md#a52e6c79344a6e511e7890f008e7281d1), [GetNextDirents()](classBEntryList.md#a2f8498249c876866d5f53a8b89044871), [Rewind()](classBEntryList.md#a6cbcd041425e5a1225a762c72a4eb8af) and [CountEntries()](classBEntryList.md#a290b792f7b12265c10ba589aa969b862).


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | if successful |
| B_ENTRY_NOT_FOUND | when at the end of the list |
| B_ERROR | or another error code (depending on the implementation of the derived class). |





**Since:** BeOS R3


Implemented in [BDirectory](classBDirectory.md#a915d4da2de8eebd949f9feb2d3407c32), and [BQuery](classBQuery.md#a40b44c5c8e047d005572334dd681bd37).

---

### `Rewind()`

```cpp
status_t BEntryList::Rewind()
```

Rewinds the list pointer to the beginning of the list. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | if successful |
| B_ERROR | or another error code (depending on the implementation of the derived class). |





**Since:** BeOS R3


Implemented in [BDirectory](classBDirectory.md#a741e1b95a65ce83edad07baa11e5aa81), and [BQuery](classBQuery.md#a42e73f8b1328e0a0bf42610a87a97e4a).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBEntryList.html).
