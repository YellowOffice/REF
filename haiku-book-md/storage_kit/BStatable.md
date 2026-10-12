---
name: BStatable
type: class
kit: storage_kit
brief: "Pure abstract class that provides a wrapper interface to the POSIX® stat() function"
source: haiku-book
---

# BStatable Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Pure abstract class that provides a wrapper interface to the POSIX® stat() function. 


[BStatable](classBStatable.md) provides common functionality for the [BEntry](classBEntry.md) and [BNode](classBNode.md) classes. You can use this class to:


* Get the stat struct of a node with the [GetStat()](classBStatable.md#a0fd44591384a51393418c7360d67c51d) method.

* Identify a node as a file, directory, or symbolic link with the [IsFile()](classBStatable.md#acaa5a30c8a6ee1f8854a787958d13eaf), [IsDirectory()](classBStatable.md#a853345d2d3673b47f59dd655b6a3adca), and [IsSymLink()](classBStatable.md#aa07af7f2d36c453d00e101bc6c6a487e) methods.

* Get and set the UID ([GetOwner()](classBStatable.md#ae8cb57200fbeac9941622a33705d64a4) and [SetOwner()](classBStatable.md#a640ef9862775efaa6720691ed4b58256)), GID ([GetGroup()](classBStatable.md#ab27d67f089c0c4bd14cdc48f57c51a17) and [SetGroup()](classBStatable.md#af6e5ac17688536b3de2940a82349d043)), and permissions ([GetPermissions()](classBStatable.md#a6a8b0225646734f4528858c72a5f9073) and [SetPermissions()](classBStatable.md#aaf215f1b31486d4fd65dd96229b26f97)) of a node.

* Get the size of a node's data (not counting attributes) with the [GetSize()](classBStatable.md#a52975e361937ae26f7c854da34e6e51a) method.

* Get and set a node's modification time ([GetModificationTime()](classBStatable.md#a5571998c1d3ca9a59ad521556b3dee63) and [SetModificationTime()](classBStatable.md#a1f2b84cea7b32a238b41f97e0264a048)), creation time ([GetCreationTime()](classBStatable.md#ac80b82a49b8c757d4bf0034d70c33eb1) and [SetCreationTime()](classBStatable.md#a6a92b04cda608babf49f70ef4e3a2f36)), and access time ([GetAccessTime()](classBStatable.md#a55dea9fb7be6e844b6515f73ee0a929a) and [SetAccessTime()](classBStatable.md#aab2c65df1f1459d014a0a2ba9638411e)).

* Get a pointer to the [BVolume](classBVolume.md) object that a node lives on via the [GetVolume()](classBStatable.md#a2488e774eaa96bf07ae6156ea320fc0a) method.

* Get a [node_ref](structnode__ref.md) of a node to pass into [watch_node()](NodeMonitor_8h.md#aa47570f615a5e07a38f452a47f9a8f48) via the [GetNodeRef()](classBStatable.md#ad22f2b8b8b11b151bc94d63caeb16c95) method.




**Since:** BeOS R3

## Member List

### Public Member Functions

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

### `GetAccessTime()`

```cpp
status_t BStatable::GetAccessTime(time_t * atime)const
```

Fills out *atime* with the access time of the node. 



**See also:** [GetModificationTime()](classBStatable.md#a5571998c1d3ca9a59ad521556b3dee63)



**Since:** BeOS R3

---

### `GetCreationTime()`

```cpp
status_t BStatable::GetCreationTime(time_t * ctime)const
```

Fills out *ctime* with the creation time of the node. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ctime` | A pointer to a `time_t` variable to be set. |





**See also:** [SetCreationTime()](classBStatable.md#a6a92b04cda608babf49f70ef4e3a2f36)



**Since:** BeOS R3

---

### `GetGroup()`

```cpp
status_t BStatable::GetGroup(gid_t * group)const
```

Fills out the node's GID into *group*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `group` | a pointer to a `gid_t` variable to be set. |





**See also:** [SetGroup()](classBStatable.md#af6e5ac17688536b3de2940a82349d043)



**Since:** BeOS R3

---

### `GetModificationTime()`

```cpp
status_t BStatable::GetModificationTime(time_t * mtime)const
```

Fills out *mtime* with the last modification time of the node. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `mtime` | A pointer to a `time_t` variable to be set. |





**See also:** [SetModificationTime()](classBStatable.md#a1f2b84cea7b32a238b41f97e0264a048)



**Since:** BeOS R3

---

### `GetNodeRef()`

```cpp
status_t BStatable::GetNodeRef(node_ref * ref)const
```

Fills out *ref* with the `node_ref` of the node. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | the [node_ref](structnode__ref.md) to be set. |





**See also:** [GetStat()](classBStatable.md#a0fd44591384a51393418c7360d67c51d) for return codes.



**Since:** BeOS R3

---

### `GetOwner()`

```cpp
status_t BStatable::GetOwner(uid_t * owner)const
```

Fills out the node's UID into *owner*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `owner` | A pointer to a `uid_t` to be set. |





**See also:** [SetOwner()](classBStatable.md#a640ef9862775efaa6720691ed4b58256)



**Since:** BeOS R3

---

### `GetPermissions()`

```cpp
status_t BStatable::GetPermissions(mode_t * permissions)const
```

Fills out *perms* with the permissions of the node. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `permissions` | The permissions to get from the node. |





**See also:** [SetPermissions()](classBStatable.md#aaf215f1b31486d4fd65dd96229b26f97)



**Since:** BeOS R3

---

### `GetSize()`

```cpp
status_t BStatable::GetSize(off_t * size)const
```

Fills out the size of the node's data (not counting attributes) into *size*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `size` | A pointer to a `off_t` variable to be set. |





**See also:** [GetStat()](classBStatable.md#a0fd44591384a51393418c7360d67c51d) for return codes.



**Since:** BeOS R3

---

### `GetStat()`

```cpp
status_t BStatable::GetStat(struct stat * stat)const
```

Fills out the stat structure for the node. 


This method may be used to access the stat structure of a node directly.


Parameters

| Parameter | Description |
| :--- | :--- |
| `stat` | The stat structure to be filled in. |





**Returns:** `B_OK` on success, or an error code on failure.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | The node does not exist, possibly renamed or deleted. |
| B_FILE_ERROR | File descriptor not found. |
| B_ENTRY_NOT_FOUND | The node inside a directory could not be found. |
| B_NOT_A_DIRECTORY | The node is not a directory, but it should be. |





**Since:** BeOS R3


Implemented in [BNode](classBNode.md#aa8c7b4e488e8077aabc8f5fbe4504189), and [BEntry](classBEntry.md#a959fc90d95796a4b21001b248b30f709).

---

### `GetVolume()`

```cpp
status_t BStatable::GetVolume(BVolume * volume)const
```

Fills out *vol* with the the volume that the node lives on. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `volume` | A pointer to a [BVolume](classBVolume.md) object to be set. |





**See also:** [BVolume](classBVolume.md)



**Since:** Haiku R1

---

### `IsDirectory()`

```cpp
bool BStatable::IsDirectory()const
```

Returns whether or not the node is a directory. 



**Returns:** `true`, if the node is properly initialized and is a directory, `false` otherwise.



**Since:** BeOS R5

---

### `IsFile()`

```cpp
bool BStatable::IsFile()const
```

Returns whether or not the node is a file. 



**Returns:** `true`, if the node is properly initialized and is a file, `false` otherwise.



**Since:** BeOS R5

---

### `IsSymLink()`

```cpp
bool BStatable::IsSymLink()const
```

Returns whether or not the node is a symbolic link. 



**Returns:** `true`, if the node is properly initialized and is a symlink, `false` otherwise.



**Since:** BeOS R5

---

### `SetAccessTime()`

```cpp
status_t BStatable::SetAccessTime(time_t atime)
```

Sets the node's access time to *atime*. 



**See also:** [GetModificationTime()](classBStatable.md#a5571998c1d3ca9a59ad521556b3dee63)



**Since:** BeOS R3

---

### `SetCreationTime()`

```cpp
status_t BStatable::SetCreationTime(time_t ctime)
```

Sets the node's creation time to *ctime*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ctime` | The creation time to set the node to. |





**See also:** [GetStat()](classBStatable.md#a0fd44591384a51393418c7360d67c51d) for return codes.



**Since:** BeOS R3

---

### `SetGroup()`

```cpp
status_t BStatable::SetGroup(gid_t group)
```

Sets the node's GID to *group*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `group` | The GID to set the node to. |





**See also:** [GetStat()](classBStatable.md#a0fd44591384a51393418c7360d67c51d) for return codes.



**Since:** BeOS R3

---

### `SetModificationTime()`

```cpp
status_t BStatable::SetModificationTime(time_t mtime)
```

Sets the node's last modification time to *mtime*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `mtime` | The modification time to set the node to. |





**See also:** [GetStat()](classBStatable.md#a0fd44591384a51393418c7360d67c51d) for return codes.



**Since:** BeOS R3

---

### `SetOwner()`

```cpp
status_t BStatable::SetOwner(uid_t owner)
```

Sets the node's UID to *owner*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `owner` | The UID to set the node to. |





**See also:** [GetStat()](classBStatable.md#a0fd44591384a51393418c7360d67c51d) for return codes.



**Since:** BeOS R3

---

### `SetPermissions()`

```cpp
status_t BStatable::SetPermissions(mode_t permissions)
```

Sets the node's permissions to *perms*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `permissions` | The permissions to set the node to. |





**See also:** [GetStat()](classBStatable.md#a0fd44591384a51393418c7360d67c51d) for return codes.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBStatable.html).
