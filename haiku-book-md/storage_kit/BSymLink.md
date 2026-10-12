---
name: BSymLink
type: class
kit: storage_kit
brief: "Provides an interface for creating, manipulating, and accessing the contents of symbolic links"
source: haiku-book
---

# BSymLink Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Provides an interface for creating, manipulating, and accessing the contents of symbolic links. 



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BSymLink](#abd9f5260a2d6eab5228c3eadde628fc3) () — Creates an uninitialized BSymLink object.
* [BSymLink](#ae215c7aa183934a2455fac2d4ee6371c) (const BDirectory *dir, const char *path) — Creates a BSymLink object and initializes it to the symbolic link referred to by the supplied path name relative to the specified BDirectory.
* [BSymLink](#a6a53a371d2868114de466a0ae879b93b) (const BEntry *entry) — Creates a BSymLink object and initializes it to the symbolic link referred to by the supplied BEntry.
* [BSymLink](#a3de9f6734c8808aedbefc19c534f11b7) (const BSymLink &other) — Creates a copy of the supplied BSymLink object.
* [BSymLink](#a41e53ec12d210408c9bb3465578ffeed) (const char *path) — Creates a BSymLink object and initializes it to the symbolic link referred to by the supplied path name.
* [BSymLink](#a735411fb0f3ec98f05586055aa459f30) (const entry_ref *ref) — Creates a BSymLink object and initializes it to the symbolic link referred to by the supplied entry_ref.
* `virtual` [~BSymLink](#a055b338bfed61a7193bae55f96b2e897) () — Destroys the object and frees all allocated resources.
* `bool` [IsAbsolute](#a2d8b53ea3a285a302fa0e074188bd307) () — Returns whether or not the object refers to an absolute path.
* `ssize_t` [MakeLinkedPath](#a280b28f0830a84aa0654475b0c032d3c) (const BDirectory *dir, BPath *path) — Combines a directory path and the contents of this symbolic link to form an absolute path.
* `ssize_t` [MakeLinkedPath](#a9169315b35636ef0adcd075fcce8958f) (const char *dirPath, BPath *path) — Combines a directory path and the contents of this symbolic link to form an absolute path.
* `ssize_t` [ReadLink](#a29306832c7d34d68265a3f65da11d5d7) (char *buf, size_t size) — Reads the contents of the symbolic link into buffer.
* [BNode](#a4c41333d8fc73a6c9f37f77ae7418528) () — Creates an uninitialized BNode object.
* [BNode](#a959e6d749cdd455524fec3a5feca6008) (const BDirectory *dir, const char *path) — Creates a BNode object and initializes it to the entry referred to by the specified path rooted in the specified directory.
* [BNode](#a2c8fd63c3e0e0d6d7596c1ca9c02cfc7) (const BEntry *entry) — Creates a BNode object and initializes it to the specified filesystem entry.
* [BNode](#a4cb06c36614e334a2ce3f132188f0b33) (const BNode &node) — Creates a copy of the given BNode.
* [BNode](#acfd887aa410f42347482347672de19c0) (const char *path) — Creates a BNode object and initializes it to the entry referred to by the specified path.
* [BNode](#a3ba1cd7e2d530124350485de1ccffbf6) (const entry_ref *ref) — Creates a BNode object and initializes it to the specified entry_ref.
* `virtual` [~BNode](#a2be9ef05bc8dc34f17982736a38e1adf) () — Frees all resources associated with the BNode.
* `int` [Dup](#a74637e73a9f75f68eb8455ad2b1d920a) () — Gets the POSIX file descriptor referred to by this node.
* `virtual status_t` [GetStat](#aa8c7b4e488e8077aabc8f5fbe4504189) (struct stat *st) const — Fills in the given stat structure with the stat() information for this object.
* `status_t` [InitCheck](#a8d1e28412f778e344e539946268fd03a) () const — Checks whether the object has been properly initialized or not.
* `status_t` [SetTo](#aa19fa8eac744cbbe8ef0cd67842fb350) (const entry_ref *ref) — Initializes the object to the specified entry_ref.
* `status_t` [SetTo](#a6a9ed4db588ce169e9d5f464e0db43c4) (const BEntry *entry) — Initializes the object to the specified filesystem entry.
* `status_t` [SetTo](#a11cc1bc7f4765f2ec5665f4d6f8c68fb) (const char *path) — Initializes the object to the specified path.
* `status_t` [SetTo](#aab2e862a78de7dac70ce8d6139b4e2a0) (const BDirectory *dir, const char *path) — Initializes the object to the entry referred by the specified path relative to the the specified directory.
* `void` [Unset](#a53045ffc7e7c8bf97487d0de2e925cc2) () — Returns the object to an uninitialized state.
* `status_t` [Lock](#ac323c1303a20a0eb21c11185bfc18039) () — Attains an exclusive lock on the data referred to by this node so that it may not be modified by any other objects or methods.
* `status_t` [Unlock](#af1aed40f239513e1001af2ee543dd9ec) () — Unlocks the date referred to by this node.
* `status_t` [Sync](#a14e67d77c99a4ede2a0bc2fe2bc46da5) () — Immediately performs any pending disk actions on the node.
* `ssize_t` [WriteAttr](#a48b845ef1eafdc729ca672bb112bf873) (const char *name, type_code type, off_t offset, const void *buffer, size_t length) — Writes data from a buffer to an attribute.
* `ssize_t` [ReadAttr](#a6ae0c729e21a32902b13d0c00b53abc2) (const char *name, type_code type, off_t offset, void *buffer, size_t length) const — Reads data from an attribute into buffer.
* `status_t` [RemoveAttr](#a29fec4dac3d10f0459f7d3eb333aaf76) (const char *name) — Deletes the attribute given by name.
* `status_t` [RenameAttr](#adacbbc1aef867abbf05c1f64941561bb) (const char *oldName, const char *newName) — Moves the attribute given by oldName to newName.
* `status_t` [GetAttrInfo](#a57b7c93cbf40df5b76b3c1aae2ad0201) (const char *name, struct attr_info *info) const — Fills in the pre-allocated attr_info struct pointed to by info with information about the attribute specified by name.
* `status_t` [GetNextAttrName](#a7ce18e673746f0f2c385ec533f10a015) (char *buffer) — Copies the name of the attribute into buffer and then advances the pointer to the next attribute.
* `status_t` [RewindAttrs](#a8848d2958c140f67e616415836835260) () — Resets the object's attribute pointer to the first attribute in the list.
* `status_t` [WriteAttrString](#aae3517eb2583c13ccf60e9488d5a198d) (const char *name, const BString *data) — Writes the specified string to the specified attribute, clobbering any previous data.
* `status_t` [ReadAttrString](#a92f9e44a87a4c5b2f20d8f6a2be89d5b) (const char *name, BString *result) const — Reads the data of the specified attribute into the pre-allocated result.
* `BNode &` [operator=](#a690260cffeb7310ecb0461ecc118e402) (const BNode &node) — Initializes the object as a copy of other.
* `bool` [operator==](#a19e5f2559d1a8649ad103cb559150897) (const BNode &node) const — Tests whether this and the supplied BNode object are equal.
* `bool` [operator!=](#a9fd78c56dd4a25fffc5d9f8f4ce7a594) (const BNode &node) const — Tests whether this and the supplied BNode object are not equal.
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

### `BSymLink()`

```cpp
BSymLink::BSymLink()
```

Creates an uninitialized [BSymLink](classBSymLink.md) object. 



**Since:** BeOS R3

---

### `BSymLink()`

```cpp
BSymLink::BSymLink(const BSymLink & other)
```

Creates a copy of the supplied [BSymLink](classBSymLink.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BSymLink](classBSymLink.md) object to be copied. |





**Since:** BeOS R3

---

### `BSymLink()`

```cpp
BSymLink::BSymLink(const entry_ref * ref)
```

Creates a [BSymLink](classBSymLink.md) object and initializes it to the symbolic link referred to by the supplied [entry_ref](structentry__ref.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | the [entry_ref](structentry__ref.md) referring to the symbolic link. |





**Since:** BeOS R3

---

### `BSymLink()`

```cpp
BSymLink::BSymLink(const BEntry * entry)
```

Creates a [BSymLink](classBSymLink.md) object and initializes it to the symbolic link referred to by the supplied [BEntry](classBEntry.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | The [BEntry](classBEntry.md) referring to the symbolic link. |





**Since:** BeOS R3

---

### `BSymLink()`

```cpp
BSymLink::BSymLink(const char * path)
```

Creates a [BSymLink](classBSymLink.md) object and initializes it to the symbolic link referred to by the supplied path name. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The path of the symbolic link. |





**Since:** BeOS R3

---

### `BSymLink()`

```cpp
BSymLink::BSymLink(const BDirectory * dir, const char * path)
```

Creates a [BSymLink](classBSymLink.md) object and initializes it to the symbolic link referred to by the supplied path name relative to the specified [BDirectory](classBDirectory.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The base [BDirectory](classBDirectory.md). |
| `path` | The path of the symbolic link relative to *dir*. |





**Since:** BeOS R3

---

### `~BSymLink()`

```cpp
BSymLink::~BSymLink()
```

Destroys the object and frees all allocated resources. 


If the [BSymLink](classBSymLink.md) was properly initialized, the file descriptor of the symbolic link is also closed.



**Since:** BeOS R3

---

### `IsAbsolute()`

```cpp
bool BSymLink::IsAbsolute()
```

Returns whether or not the object refers to an absolute path. 


/return `true` if the object is properly initialized and the symbolic link refers to an absolute path, `false` otherwise.



**Since:** BeOS R3

---

### `MakeLinkedPath()`

```cpp
ssize_t BSymLink::MakeLinkedPath(const BDirectory * dir, BPath * path)
```

Combines a directory path and the contents of this symbolic link to form an absolute path. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The base [BDirectory](classBDirectory.md) object to combine with the symbolic link. |
| `path` | the [BPath](classBPath.md) object to be set to the resulting absolute path. |





**Returns:** The length of the resulting path name or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | *dir* or *path* was `NULL` or the object didn't refer to a symbolic link. |
| B_FILE_ERROR | The object was not initialized. |
| B_NAME_TOO_LONG | The resulting path name was too long to fit. |





**Since:** BeOS R3

---

### `MakeLinkedPath()`

```cpp
ssize_t BSymLink::MakeLinkedPath(const char * dirPath, BPath * path)
```

Combines a directory path and the contents of this symbolic link to form an absolute path. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dirPath` | The base directory path to combine with the symbolic link. |
| `path` | The [BPath](classBPath.md) object to be set to the resulting absolute path. |





**Returns:** The length of the resulting path name or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | *dirPath* or *path* was `NULL` or the object didn't refer to a symbolic link. |
| B_FILE_ERROR | The object was not initialized. |
| B_NAME_TOO_LONG | The resulting path name was too long to fit. |





**Since:** BeOS R3

---

### `ReadLink()`

```cpp
ssize_t BSymLink::ReadLink(char * buffer, size_t size)
```

Reads the contents of the symbolic link into *buffer*. 


The string written to the buffer is guaranteed to be `NULL` terminated.


This function does not return the number of bytes written into the provided buffer. It returns the length of the symlink's contents, even if that contents does not fit within the provided buffer. If the buffer cannot contain the entire contents then it will be truncated to *size*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | The buffer to read the symlink's contents into. |
| `size` | The size of *buffer*. |





**Returns:** The length of the symlink's contents or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | *buf* was `NULL` or the object didn't refer to a symbolic link. |
| B_FILE_ERROR | The object was not initialized. |





**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBSymLink.html).
