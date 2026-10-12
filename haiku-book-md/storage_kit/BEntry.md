---
name: BEntry
type: class
kit: storage_kit
brief: "A location in the filesystem"
source: haiku-book
---

# BEntry Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A location in the filesystem. 


The [BEntry](classBEntry.md) class defines objects that represent "locations" in the file system hierarchy. Each location (or entry) is given as a name within a directory. For example, if you create a [BEntry](classBEntry.md) like this:



```cpp
BEntry entry("/boot/home/fido");
```

the resulting [BEntry](classBEntry.md) object represents the location of the file `fido` within the `/boot/home` directory.

## Member List

### Public Member Functions

* [BEntry](#a1448e81e2138396d5a3b8e755044b40b) () — Creates an uninitialized BEntry object.
* [BEntry](#a678cb2d9f7f404fdaafcfe1948042332) (const BDirectory *dir, const char *path, bool traverse=false) — Creates a BEntry initialized to the given directory and path combination.
* [BEntry](#a9d98e3bb78102f76756664bb112e5794) (const BEntry &entry) — Creates a copy of the given BEntry.
* [BEntry](#a75ffe08fca4a04fc9c318fe999890d52) (const char *path, bool traverse=false) — Creates a BEntry initialized to the given path.
* [BEntry](#a4307a4b68be87e2194cc9546b4fbfbfc) (const entry_ref *ref, bool traverse=false) — Creates a BEntry for the file referred to by the passed in entry_ref.
* `virtual` [~BEntry](#ac7f297816e85d19ee0a4a2603928c6c0) () — Frees all of the allocated resources of the BEntry.
* `bool` [Exists](#ae5a3c25502bb0025910739164d7261e6) () const — Returns whether or not the entry exists in the filesystem.
* `status_t` [GetName](#ae1ebcff7dde858765c3bbe3ea83edf4a) (char *buffer) const — Gets the name of the leaf of the BEntry object.
* `status_t` [GetParent](#a8cd10a538a30cc94edc87e7b96551e69) (BDirectory *dir) const — Gets the parent of the BEntry as a BDirectory.
* `status_t` [GetParent](#ae10d5c12f6ef3a89b7f9810514fa4123) (BEntry *entry) const — Gets the parent of the BEntry as a BEntry.
* `status_t` [GetPath](#a95bf275869e2807808bd7785fadb132b) (BPath *path) const — Gets the path for the BEntry.
* `status_t` [GetRef](#aeeb2f15b9b3816c28df9c1450e1ae91c) (entry_ref *ref) const — Gets an entry_ref structure for the BEntry.
* `virtual status_t` [GetStat](#a959fc90d95796a4b21001b248b30f709) (struct stat *stat) const — Fills in a stat structure for the entry.
* `status_t` [InitCheck](#afd4ad2a7a6e6bd63f565b8243eff6edf) () const — Returns the result of the most recent constructor or SetTo() call.
* `status_t` [MoveTo](#afc2ae2e0cd12df46f6db8fe3183657e2) (BDirectory *dir, const char *path=NULL, bool clobber=false) — Moves the BEntry to directory or directory and path combination, replacing an existing entry if clobber is true.
* `bool` [operator!=](#a255ee1c4a4a6edfc73c2b030765fbd6e) (const BEntry &item) const — Returns false if the BEntry and item refer to the same entry or if they are both uninitialized.
* `BEntry &` [operator=](#a25452b45b354b58eae987b2bb1445316) (const BEntry &item) — Reinitializes the BEntry to be a copy of item.
* `bool` [operator==](#a0359e0e7d03ee6eb1297688d0d2dd339) (const BEntry &item) const — Returns true if the BEntry and item refer to the same entry or if they are both uninitialized.
* `status_t` [Remove](#a8ac144783f19f65c51b39048dc682572) () — Removes the entry from the file system.
* `status_t` [Rename](#a383c32766e863ac0e894d9b24449beb0) (const char *path, bool clobber=false) — Renames the BEntry to path replacing an existing entry if clobber is true.
* `status_t` [SetTo](#af3d01795ef093ac81ac45baf50b7597e) (const BDirectory *dir, const char *path, bool traverse=false) — Reinitializes the BEntry to the path or directory path combination, resolving symlinks if traverse is true.
* `status_t` [SetTo](#a205c03c6a32622d2fe79d8c8e189bbb6) (const char *path, bool traverse=false) — Reinitializes the BEntry object to the path, resolving symlinks if traverse is true.
* `status_t` [SetTo](#a57d22e1aa77f89ed34260ec1b7af32a1) (const entry_ref *ref, bool traverse=false) — Reinitializes the BEntry to the passed in entry_ref object resolving symlinks if traverse is true.
* `void` [Unset](#ab3a42dc9f04fcc655daff30222710a29) () — Reset the BEntry to the uninitialized state.
* `status_t` [GetAccessTime](#a55dea9fb7be6e844b6515f73ee0a929a) (time_t *atime) const — Fills out atime with the access time of the node.
* `status_t` [GetCreationTime](#ac80b82a49b8c757d4bf0034d70c33eb1) (time_t *ctime) const — Fills out ctime with the creation time of the node.
* `status_t` [GetGroup](#ab27d67f089c0c4bd14cdc48f57c51a17) (gid_t *group) const — Fills out the node's GID into group.
* `status_t` [GetModificationTime](#a5571998c1d3ca9a59ad521556b3dee63) (time_t *mtime) const — Fills out mtime with the last modification time of the node.
* `status_t` [GetNodeRef](#ad22f2b8b8b11b151bc94d63caeb16c95) (node_ref *ref) const — Fills out ref with the node_ref of the node.
* `status_t` [GetOwner](#ae8cb57200fbeac9941622a33705d64a4) (uid_t *owner) const — Fills out the node's UID into owner.
* `status_t` [GetPermissions](#a6a8b0225646734f4528858c72a5f9073) (mode_t *permissions) const — Fills out perms with the permissions of the node.
* `status_t` [GetSize](#a52975e361937ae26f7c854da34e6e51a) (off_t *size) const — Fills out the size of the node's data (not counting attributes) into size.
* `virtual status_t` [GetStat](#a0fd44591384a51393418c7360d67c51d) (struct stat *stat) const =0 — Fills out the stat structure for the node.
* `status_t` [GetVolume](#a2488e774eaa96bf07ae6156ea320fc0a) (BVolume *volume) const — Fills out vol with the the volume that the node lives on.
* `bool` [IsDirectory](#a853345d2d3673b47f59dd655b6a3adca) () const — Returns whether or not the node is a directory.
* `bool` [IsFile](#acaa5a30c8a6ee1f8854a787958d13eaf) () const — Returns whether or not the node is a file.
* `bool` [IsSymLink](#aa07af7f2d36c453d00e101bc6c6a487e) () const — Returns whether or not the node is a symbolic link.
* `status_t` [SetAccessTime](#aab2c65df1f1459d014a0a2ba9638411e) (time_t atime) — Sets the node's access time to atime.
* `status_t` [SetCreationTime](#a6a92b04cda608babf49f70ef4e3a2f36) (time_t ctime) — Sets the node's creation time to ctime.
* `status_t` [SetGroup](#af6e5ac17688536b3de2940a82349d043) (gid_t group) — Sets the node's GID to group.
* `status_t` [SetModificationTime](#a1f2b84cea7b32a238b41f97e0264a048) (time_t mtime) — Sets the node's last modification time to mtime.
* `status_t` [SetOwner](#a640ef9862775efaa6720691ed4b58256) (uid_t owner) — Sets the node's UID to owner.
* `status_t` [SetPermissions](#aaf215f1b31486d4fd65dd96229b26f97) (mode_t permissions) — Sets the node's permissions to perms.

## Detailed Member Documentation

### `BEntry()`

```cpp
BEntry::BEntry()
```

Creates an uninitialized [BEntry](classBEntry.md) object. 


Should be followed by a call to one of the [SetTo()](classBEntry.md#af3d01795ef093ac81ac45baf50b7597e) methods, or an assignment.



**See also:** [SetTo(const BDirectory*, const char*, bool)](classBEntry.md#af3d01795ef093ac81ac45baf50b7597e)



**Since:** BeOS R3

---

### `BEntry()`

```cpp
BEntry::BEntry(const BDirectory * dir, const char * path, bool traverse = false)
```

Creates a [BEntry](classBEntry.md) initialized to the given directory and path combination. 


If traverse is `true` and *path* refers to a symlink, the [BEntry](classBEntry.md) will refer to the linked file; if `false`, the [BEntry](classBEntry.md) will refer to the symlink itself.


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The base directory in which the *path* resides. |
| `path` | Relative path based off of *dir*. |
| `traverse` | Whether or not to traverse symbolic links. |





**See also:** [BEntry::SetTo(const BDirectory*, const char *, bool)](classBEntry.md#af3d01795ef093ac81ac45baf50b7597e)



**Since:** BeOS R3

---

### `BEntry()`

```cpp
BEntry::BEntry(const entry_ref * ref, bool traverse = false)
```

Creates a [BEntry](classBEntry.md) for the file referred to by the passed in [entry_ref](structentry__ref.md). 


If traverse is `true` and *ref* refers to a symlink, the [BEntry](classBEntry.md) will refer to the linked file; if `false`, the [BEntry](classBEntry.md) will refer to the symlink itself.


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The `entry_ref` referring to the given file. |
| `traverse` | Whether or not symlinks are to be traversed. |





**See also:** [BEntry::SetTo(const entry_ref*, bool)](classBEntry.md#a57d22e1aa77f89ed34260ec1b7af32a1)



**Since:** BeOS R3

---

### `BEntry()`

```cpp
BEntry::BEntry(const char * path, bool traverse = false)
```

Creates a [BEntry](classBEntry.md) initialized to the given path. 


If *path* is relative, it will be reckoned off the current working directory. If *path* refers to a symlink and traverse is `true`, the [BEntry](classBEntry.md) will refer to the linked file. If traverse is `false`, the [BEntry](classBEntry.md) will refer to the symlink itself.


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The *path* of the file. |
| `traverse` | Whether or not symlinks are to be traversed. |





**See also:** [BEntry::SetTo(const char*, bool)](classBEntry.md#a205c03c6a32622d2fe79d8c8e189bbb6)



**Since:** BeOS R3

---

### `BEntry()`

```cpp
BEntry::BEntry(const BEntry & entry)
```

Creates a copy of the given [BEntry](classBEntry.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | The *entry* to be copied. |





**See also:** [operator=(const BEntry&)](classBEntry.md#a25452b45b354b58eae987b2bb1445316)



**Since:** BeOS R3

---

### `~BEntry()`

```cpp
BEntry::~BEntry()
```

Frees all of the allocated resources of the [BEntry](classBEntry.md). 



**See also:** [Unset()](classBEntry.md#ab3a42dc9f04fcc655daff30222710a29)



**Since:** BeOS R3

---

### `Exists()`

```cpp
bool BEntry::Exists()const
```

Returns whether or not the entry exists in the filesystem. 


An entry [Exists()](classBEntry.md#ae5a3c25502bb0025910739164d7261e6) if the file referenced by the entry has not been deleted or renamed and the entry's parent directory has not been deleted.



**Returns:** `true` if the entry exists, or `false` otherwise.



**See also:** [BStatable::GetStat()](classBStatable.md#a0fd44591384a51393418c7360d67c51d)



**Since:** BeOS R3

---

### `GetName()`

```cpp
status_t BEntry::GetName(char * buffer)const
```

Gets the name of the leaf of the [BEntry](classBEntry.md) object. 


`buffer` must be pre-allocated and of sufficient length to hold the entire string. A length of `B_FILE_NAME_LENGTH` is recommended.


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | A pointer to a pre-allocated string into which the result is copied. |





**Returns:** `B_OK` on success, or an error code on failure.



**Since:** BeOS R3

---

### `GetParent()`

```cpp
status_t BEntry::GetParent(BDirectory * dir)const
```

Gets the parent of the [BEntry](classBEntry.md) as a [BDirectory](classBDirectory.md). 


If the function fails, the argument is [Unset()](classBEntry.md#ab3a42dc9f04fcc655daff30222710a29).


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | A pointer to a pre-allocated [BDirectory](classBDirectory.md) object into which the result is copied. |





**Returns:** `B_OK` on success, or an error code on failure.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Success |
| B_ENTRY_NOT_FOUND | Attempted to get the parent of the root directory. |





**Since:** BeOS R3

---

### `GetParent()`

```cpp
status_t BEntry::GetParent(BEntry * entry)const
```

Gets the parent of the [BEntry](classBEntry.md) as a [BEntry](classBEntry.md). 


If the function fails, the argument is [Unset()](classBEntry.md#ab3a42dc9f04fcc655daff30222710a29). Destructive calls to [GetParent()](classBEntry.md#ae10d5c12f6ef3a89b7f9810514fa4123) are allowed, i.e.:



```cpp
BEntry entry("/boot/home/fido");
status_t err;
char name[B_FILE_NAME_LENGTH];
 
// Spit out the path components backwards, one at a time.
do {
    entry.GetName(name);
    printf("> %s\n", name);
} while ((err=entry.GetParent(&entry)) == B_OK);
 
// Complain for reasons other than reaching the top.
if (err != B_ENTRY_NOT_FOUND)
    printf(">> Error: %s\n", strerror(err));
```

will output:



```cpp
> fido
> home
> boot
> .
```

Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | A pointer to a pre-allocated [BEntry](classBEntry.md) object into which the result is stored. |





**Returns:** `B_OK` on success, or an error code on failure.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Success |
| B_ENTRY_NOT_FOUND | Attempted to get the parent of the root directory. |





**Since:** BeOS R3

---

### `GetPath()`

```cpp
status_t BEntry::GetPath(BPath * path)const
```

Gets the path for the [BEntry](classBEntry.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | A pointer to a pre-allocated [BPath](classBPath.md) object into which the result is copied. |





**Returns:** `B_OK` on success, or an error code on failure.



**Since:** BeOS R3

---

### `GetRef()`

```cpp
status_t BEntry::GetRef(entry_ref * ref)const
```

Gets an [entry_ref](structentry__ref.md) structure for the [BEntry](classBEntry.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | A pointer to a pre-allocated `entry_ref` object into which the result is copied. |





**Returns:** `B_OK` on success, or an error code on failure.



**Since:** BeOS R3

---

### `GetStat()`

```cpp
status_t BEntry::GetStat(struct stat * result)const
```

Fills in a stat structure for the entry. 


The information is copied into the `stat` structure pointed to by *result*.



> [!NOTE]
> The [BStatable](classBStatable.md) object does not cache the stat structure – each time you call [GetStat()](classBEntry.md#a959fc90d95796a4b21001b248b30f709) fresh stat information is retrieved.


Parameters

| Parameter | Description |
| :--- | :--- |
| `result` | A pointer to a pre-allocated structure into which the stat information is copied. |





**Returns:** `B_OK` on success, or an error code on failure.



**Since:** BeOS R3


Implements [BStatable](classBStatable.md#a0fd44591384a51393418c7360d67c51d).

---

### `InitCheck()`

```cpp
status_t BEntry::InitCheck()const
```

Returns the result of the most recent constructor or [SetTo()](classBEntry.md#af3d01795ef093ac81ac45baf50b7597e) call. 



**Returns:** `B_OK` on success of an error status code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Success. |
| B_NO_INIT | The object has been [Unset()](classBEntry.md#ab3a42dc9f04fcc655daff30222710a29) or is uninitialized. |





**See also:** [SetTo()](classBEntry.md#af3d01795ef093ac81ac45baf50b7597e) for more error codes.



**Since:** BeOS R3

---

### `MoveTo()`

```cpp
status_t BEntry::MoveTo(BDirectory * dir, const char * path = NULL, bool clobber = false)
```

Moves the [BEntry](classBEntry.md) to directory or directory and path combination, replacing an existing entry if clobber is true. 



> [!NOTE]
> The [BEntry](classBEntry.md) object must refer to an existing file, if it is abstract, this method will fail.


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | A pointer to a pre-allocated [BDirectory](classBDirectory.md) into which the entry should be moved. |
| `path` | (optional) new leaf name for the entry. May be a simple leaf or a relative path; either way, `path` is reckoned off of `dir`. If `NULL`, the entry retains its previous leaf name. |
| `clobber` | If `false` and an entry already exists at the specified Spdestination, the method will fail. If `true` and such an entry exists, it will be overwritten. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Success |
| B_ENTRY_EXISTS | The new location already exists and `clobber` is `false`. |
| B_ENTRY_NOT_FOUND | Attempted to rename an abstract entry. |





**Since:** BeOS R3

---

### `operator!=()`

```cpp
bool BEntry::operator!=(const BEntry & item)const
```

Returns false if the [BEntry](classBEntry.md) and `item` refer to the same entry or if they are both uninitialized. 



**Returns:** Whether or not the items do NOT refer to the same entry.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The [BEntry](classBEntry.md) objects refer to different entries. |
| false | Both [BEntry](classBEntry.md) objects refer to the same entry or they are both uninitialized. |





**Since:** BeOS R3

---

### `operator=()`

```cpp
BEntry & BEntry::operator=(const BEntry & item)
```

Reinitializes the [BEntry](classBEntry.md) to be a copy of *item*. 



**Returns:** A pointer to the copy.



**Since:** BeOS R3

---

### `operator==()`

```cpp
bool BEntry::operator==(const BEntry & item)const
```

Returns `true` if the [BEntry](classBEntry.md) and *item* refer to the same entry or if they are both uninitialized. 



**Returns:** Whether or not the items refer to the same entry.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | Both [BEntry](classBEntry.md) objects refer to the same entry or they are both uninitialized. |
| false | The [BEntry](classBEntry.md) objects refer to different entries. |





**Since:** BeOS R3

---

### `Remove()`

```cpp
status_t BEntry::Remove()
```

Removes the entry from the file system. 



> [!NOTE]
> If any file descriptors are open on the file when [Remove()](classBEntry.md#a8ac144783f19f65c51b39048dc682572) is called the chunk of data they refer to will continue to exist until all such file descriptors are closed. The [BEntry](classBEntry.md) object, however, becomes abstract and no longer refers to any actual data in the filesystem.



**Returns:** `B_OK` on success, or an error code on failure.



**Since:** BeOS R3

---

### `Rename()`

```cpp
status_t BEntry::Rename(const char * path, bool clobber = false)
```

Renames the [BEntry](classBEntry.md) to *path* replacing an existing entry if *clobber* is `true`. 



> [!NOTE]
> The [BEntry](classBEntry.md) object must refer to an existing file, if it is abstract, this method will fail.


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | A pointer to a string containing the new name for the entry. It may be an absolute or relative path. If it is a relative path the entry is renamed within its current directory. |
| `clobber` | If `false` and a file with the name given by `path` already exists, the method will fail. If `true` and such a file exists, it will be overwritten. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Success |
| B_ENTRY_EXISTS | The new location already exists and `clobber` is `false`. |
| B_ENTRY_NOT_FOUND | Attempted to rename an abstract entry. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BEntry::SetTo(const BDirectory * dir, const char * path, bool traverse = false)
```

Reinitializes the [BEntry](classBEntry.md) to the path or directory path combination, resolving symlinks if traverse is `true`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The base directory in which the *path* resides. |
| `path` | Relative path based off of *dir*. |
| `traverse` | Whether or not to traverse symbolic links. |





**Returns:** `B_OK` on success, or an error code on failure.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_MEMORY | Could not allocate enough memory for entry. |
| B_BAD_VALUE | `NULL` dir passed in or the entry's parent directory file descriptor does not exist. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BEntry::SetTo(const char * path, bool traverse = false)
```

Reinitializes the [BEntry](classBEntry.md) object to the path, resolving symlinks if traverse is `true`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The *path* of the file. |
| `traverse` | Whether or not symlinks are to be traversed. |





**Returns:** `B_OK` on success, or an error code on failure.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *path*. |





**See also:** fcntl(2) man page for possible POSIX error codes



**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BEntry::SetTo(const entry_ref * ref, bool traverse = false)
```

Reinitializes the [BEntry](classBEntry.md) to the passed in [entry_ref](structentry__ref.md) object resolving symlinks if traverse is `true`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The `entry_ref` referring to the given file. |
| `traverse` | Whether or not symlinks are to be traversed. |





**Returns:** `B_OK` on success, or an error code on failure.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_MEMORY | Could not allocate enough memory for entry. |
| B_BAD_VALUE | The entry's parent directory file descriptor does not exist. |





**See also:** [BEntry::BEntry(const entry_ref* ref, bool traverse)](classBEntry.md#a4307a4b68be87e2194cc9546b4fbfbfc)



**Since:** BeOS R3

---

### `Unset()`

```cpp
void BEntry::Unset()
```

Reset the [BEntry](classBEntry.md) to the uninitialized state. 


The [BEntry](classBEntry.md) forgets any information about the entry it was referencing. Any attempt to get information from it after this will return `B_NO_INIT`. The [BEntry](classBEntry.md) can later be pointed to another entry using [SetTo()](classBEntry.md#af3d01795ef093ac81ac45baf50b7597e).



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBEntry.html).
