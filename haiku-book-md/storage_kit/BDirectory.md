---
name: BDirectory
type: class
kit: storage_kit
brief: "A directory in the file system"
source: haiku-book
---

# BDirectory Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A directory in the file system. 



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BDirectory](#a785e87332e1947d603f6df2b0d05b3bb) () — Creates an uninitialized BDirectory object.
* [BDirectory](#ab7f15aadd54d73b15872ecd035d1c4c9) (const BDirectory &dir) — Creates a copy of the supplied BDirectory object.
* [BDirectory](#a47f53e8bf964d1a19fd6ae03087adf3b) (const BDirectory *dir, const char *path) — Creates a BDirectory and initializes it to the directory referred to by the supplied path name relative to the specified BDirectory.
* [BDirectory](#a7f27c8eade45a907ba3b7f47a7d9cba0) (const BEntry *entry) — Creates a BDirectory and initializes it to the directory referred to by the supplied BEntry.
* [BDirectory](#a389e65b24033d678255af171ca4de360) (const char *path) — Creates a BDirectory and initializes it to the directory referred to by the supplied path name.
* [BDirectory](#a05ff779b68659c03e5572caa41d68736) (const entry_ref *ref) — Creates a BDirectory and initializes it to the directory referred to by the supplied entry_ref.
* [BDirectory](#a7ee32ea09a7dff856d8287186a13e247) (const node_ref *nref) — Creates a BDirectory and initializes it to the directory referred to by the supplied node_ref.
* `virtual` [~BDirectory](#a6cb87cbac26348cb35179f623046544b) () — Destroys the BDirectory object.
* `bool` [Contains](#a7c654287b2781a44d65f4a207829b0b6) (const BEntry *entry, int32 nodeFlags=B_ANY_NODE) const — Returns whether or not this directory or any of its subdirectories at any level contain the entry referred to by the supplied BEntry.
* `bool` [Contains](#a5377f63f3451f96dbb39ed3b3c2fa454) (const char *path, int32 nodeFlags=B_ANY_NODE) const — Returns whether or not this directory or any of its subdirectories at any level contain the entry referred to by the supplied path name.
* `virtual int32` [CountEntries](#a9408e42d1c0683cd97991e8d3ac0b41f) () — Returns the number of entries in this directory.
* `status_t` [CreateDirectory](#a7965b93bf1c47e5c1dd33c071ee325ba) (const char *path, BDirectory *dir) — Creates a new directory.
* `status_t` [CreateFile](#ad14b083e3e702ba8626552567022f0b2) (const char *path, BFile *file, bool failIfExists=false) — Creates a new file.
* `status_t` [CreateSymLink](#a515a92f02cf5bcc7ef28bb9e33719476) (const char *path, const char *linkToPath, BSymLink *link) — Creates a new symbolic link.
* `status_t` [FindEntry](#ad0e086ab2841d3ebc8f99dd716974dd4) (const char *path, BEntry *entry, bool traverse=false) const — Finds an entry referred to by a path relative to the directory represented by this BDirectory.
* `status_t` [GetEntry](#ab0d42ac72c4e1e720143ebfccc3ff9c1) (BEntry *entry) const — Gets a BEntry object referring to the directory. If the initialization of entry fails, it is Unset().
* `virtual int32` [GetNextDirents](#ad163bac44f24104b1cd336487114e2fe) (dirent *buf, size_t bufSize, int32 count=INT_MAX) — Returns the next entries of the BDirectory object as a pointer to dirent structures.
* `virtual status_t` [GetNextEntry](#afc19ccbfe069ccd6d800d368eab24008) (BEntry *entry, bool traverse=false) — Returns the next entry as a BEntry object.
* `virtual status_t` [GetNextRef](#a915d4da2de8eebd949f9feb2d3407c32) (entry_ref *ref) — Returns the BDirectory's next entry as an entry_ref.
* `status_t` [GetStatFor](#a81d2641c7e077b3c092b2bdf6931d392) (const char *path, struct stat *st) const — Returns the stat structure of the entry referred to by the supplied path name.
* `bool` [IsRootDirectory](#ac4733f649de3216a646837756168515f) () const — Returns whether the directory is the root directory of a volume.
* `BDirectory &` [operator=](#ae5a911700daaae50e052463c03ca8fb7) (const BDirectory &dir) — Assigns another BDirectory to this BDirectory.
* `virtual status_t` [Rewind](#a741e1b95a65ce83edad07baa11e5aa81) () — Rewinds the directory iterator.
* `status_t` [SetTo](#a4408f4b96d16fbed8c0aceebd2cf5885) (const BDirectory *dir, const char *path) — Re-initializes the BDirectory to the directory referred to by the supplied path name relative to the specified BDirectory.
* `status_t` [SetTo](#aa5ccde8f60a83e1eb9abeeeea26714a1) (const BEntry *entry) — Re-initializes the BDirectory to the directory referred to by the supplied BEntry.
* `status_t` [SetTo](#ae8b830116a1fbc5a79c1f65cd25aedac) (const char *path) — Re-initializes the BDirectory to the directory referred to by the supplied path name.
* `status_t` [SetTo](#a850625e878c321af0e4b014e518d84ff) (const entry_ref *ref) — Re-initializes the BDirectory to the directory referred to by the supplied entry_ref.
* `status_t` [SetTo](#adab78ee96777e45d92c1b1c3f110705d) (const node_ref *nref) — Re-initializes the BDirectory to the directory referred to by the supplied node_ref.
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
* [BEntryList](#adf5344c4229922691642b6e07c29bcaa) () — Creates a BEntryList object.
* `virtual` [~BEntryList](#ac239f4229be2d0a1c9a58c83f503be4c) () — Frees all resources associated with the BEntryList object.
* `virtual int32` [CountEntries](#a290b792f7b12265c10ba589aa969b862) ()=0 — Returns the number of entries in the list.
* `virtual int32` [GetNextDirents](#a2f8498249c876866d5f53a8b89044871) (struct dirent *direntBuffer, size_t bufferSize, int32 maxEntries=INT_MAX)=0 — Returns the BEntryList's next entries as dirent structures.
* `virtual status_t` [GetNextEntry](#a52e6c79344a6e511e7890f008e7281d1) (BEntry *entry, bool traverse=false)=0 — Returns the BEntryList's next entry as a BEntry.
* `virtual status_t` [GetNextRef](#a908ff7149239ab66683b12b27be917ee) (entry_ref *ref)=0 — Returns the BEntryList's next entry as an entry_ref.
* `virtual status_t` [Rewind](#a6cbcd041425e5a1225a762c72a4eb8af) ()=0 — Rewinds the list pointer to the beginning of the list.

## Detailed Member Documentation

### `BDirectory()`

```cpp
BDirectory::BDirectory()
```

Creates an uninitialized [BDirectory](classBDirectory.md) object. 



**Since:** BeOS R3

---

### `BDirectory()`

```cpp
BDirectory::BDirectory(const BDirectory & dir)
```

Creates a copy of the supplied [BDirectory](classBDirectory.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The [BDirectory](classBDirectory.md) object to be copied. |





**Since:** BeOS R3

---

### `BDirectory()`

```cpp
BDirectory::BDirectory(const entry_ref * ref)
```

Creates a [BDirectory](classBDirectory.md) and initializes it to the directory referred to by the supplied [entry_ref](structentry__ref.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The [entry_ref](structentry__ref.md) that refers to the directory. |





**Since:** BeOS R3

---

### `BDirectory()`

```cpp
BDirectory::BDirectory(const node_ref * nref)
```

Creates a [BDirectory](classBDirectory.md) and initializes it to the directory referred to by the supplied [node_ref](structnode__ref.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `nref` | The [node_ref](structnode__ref.md) that refers to the directory. |





**Since:** BeOS R3

---

### `BDirectory()`

```cpp
BDirectory::BDirectory(const BEntry * entry)
```

Creates a [BDirectory](classBDirectory.md) and initializes it to the directory referred to by the supplied [BEntry](classBEntry.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | The [BEntry](classBEntry.md) that refers to the directory. |





**Since:** BeOS R3

---

### `BDirectory()`

```cpp
BDirectory::BDirectory(const char * path)
```

Creates a [BDirectory](classBDirectory.md) and initializes it to the directory referred to by the supplied *path* name. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The *path* name of the directory. |





**Since:** BeOS R3

---

### `BDirectory()`

```cpp
BDirectory::BDirectory(const BDirectory * dir, const char * path)
```

Creates a [BDirectory](classBDirectory.md) and initializes it to the directory referred to by the supplied path name relative to the specified [BDirectory](classBDirectory.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The base [BDirectory](classBDirectory.md) object. |
| `path` | The *path* of the directory relative to *dir* |





**Since:** BeOS R3

---

### `~BDirectory()`

```cpp
BDirectory::~BDirectory()
```

Destroys the [BDirectory](classBDirectory.md) object. 


If the [BDirectory](classBDirectory.md) is properly initialized, the directory's file descriptor is closed.



**Since:** BeOS R3

---

### `Contains()`

```cpp
bool BDirectory::Contains(const BEntry * entry, int32 nodeFlags = B_ANY_NODE)const
```

Returns whether or not this directory or any of its subdirectories at any level contain the entry referred to by the supplied [BEntry](classBEntry.md). 


Only entries that match the node flavor specified by *nodeFlags* are considered.



> [!NOTE]
> If the paths are identical, this method returns `true` to stay consistent with BeOS 5.


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | a [BEntry](classBEntry.md) referring to the entry |
| `nodeFlags` | Any of the following: * `B_FILE_NODE:` The entry must be a file.  * `B_DIRECTORY_NODE:` The entry must be a directory.  * `B_SYMLINK_NODE:` The entry must be a symbolic link.  * `B_ANY_NODE:` The entry may be of any kind. |





**Returns:** `true` if the [BDirectory](classBDirectory.md) is properly initialized and the entry of the matching kind was found, `false` otherwise.



**Since:** BeOS R3

---

### `Contains()`

```cpp
bool BDirectory::Contains(const char * path, int32 nodeFlags = B_ANY_NODE)const
```

Returns whether or not this directory or any of its subdirectories at any level contain the entry referred to by the supplied path name. 


Only entries that match the node flavor specified by *nodeFlags* are considered.


If the [BDirectory](classBDirectory.md) is not properly initialized, the method returns `false`. A non-absolute path is considered relative to the current directory.



> [!NOTE]
> BeOS R5's implementation always returns `true` given an absolute path or an initialized directory. This implementation is not compatible with that behavior. Instead it converts the path into a [BEntry](classBEntry.md) and passes it to the other version of [Contains()](classBDirectory.md#a5377f63f3451f96dbb39ed3b3c2fa454).


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The entry's *path* name. May be relative to this directory or may be an absolute *path*. |
| `nodeFlags` | Any of the following: * `B_FILE_NODE:` The entry must be a file.  * `B_DIRECTORY_NODE:` The entry must be a directory.  * `B_SYMLINK_NODE:` The entry must be a symbolic link.  * `B_ANY_NODE:` The entry may be of any kind. |





**Returns:** `true` if the entry exists and its kind does match *nodeFlags* and the [BDirectory](classBDirectory.md) is properly initialized and does contain the entry at any level, `false` otherwise.



**Since:** BeOS R3

---

### `CountEntries()`

```cpp
int32 BDirectory::CountEntries()
```

Returns the number of entries in this directory. 


[CountEntries()](classBDirectory.md#a9408e42d1c0683cd97991e8d3ac0b41f) uses the directory iterator also used by [GetNextEntry()](classBDirectory.md#afc19ccbfe069ccd6d800d368eab24008), [GetNextRef()](classBDirectory.md#a915d4da2de8eebd949f9feb2d3407c32) and [GetNextDirents()](classBDirectory.md#ad163bac44f24104b1cd336487114e2fe). It does a [Rewind()](classBDirectory.md#a741e1b95a65ce83edad07baa11e5aa81), iterates through the entries and [Rewind()](classBDirectory.md#a741e1b95a65ce83edad07baa11e5aa81)s again. The entries "." and ".." are not counted.



**Returns:** The number of entries in the directory (not counting "." and "..") or a status code on error.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**See also:** [BDirectory::GetNextEntry()](classBDirectory.md#afc19ccbfe069ccd6d800d368eab24008)



**Since:** BeOS R3


Implements [BEntryList](classBEntryList.md#a290b792f7b12265c10ba589aa969b862).

---

### `CreateDirectory()`

```cpp
status_t BDirectory::CreateDirectory(const char * path, BDirectory * dir)
```

Creates a new directory. 


If an entry with the supplied name already exists this method returns an error status code.


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The new path name of the directory. May be a relative path to this directory or an absolute path. |
| `dir` | A pointer to a [BDirectory](classBDirectory.md) to be initialized to the newly created directory. May be `NULL`. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *path*. |
| B_ENTRY_NOT_FOUND | *path* does not refer to a possible entry. |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_FILE_EXISTS | An entry with that name does already exist. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**Since:** BeOS R3

---

### `CreateFile()`

```cpp
status_t BDirectory::CreateFile(const char * path, BFile * file, bool failIfExists = false)
```

Creates a new file. 


If a file with the supplied name does already exist, the method fails, unless it is passed `false` to *failIfExists* – in that case the file is truncated to zero size. The new [BFile](classBFile.md) will operate in `B_READ_WRITE` mode.


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The new file's path name. May be relative to this directory or an absolute path. |
| `file` | A pointer to a [BFile](classBFile.md) to be initialized to the newly created file. May be `NULL`. |
| `failIfExists` | Whether or not to fail if the file already exists. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *path*. |
| B_ENTRY_NOT_FOUND | *path* does not refer to a possible entry. |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_FILE_EXISTS | A file with that name does already exist and `true` has been passed for *failIfExists*. |
| B_IS_A_DIRECTORY | A directory with the supplied name already exists. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**Since:** BeOS R3

---

### `CreateSymLink()`

```cpp
status_t BDirectory::CreateSymLink(const char * path, const char * linkToPath, BSymLink * link)
```

Creates a new symbolic link. 


This method fails if an entry with the supplied name already exists.


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | the new symbolic link's path name. May be relative to this directory or absolute. |
| `linkToPath` | the path the symbolic link shall point to. |
| `link` | a pointer to a [BSymLink](classBSymLink.md) to be initialized to the newly created symbolic link. May be `NULL`. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *path* or *linkToPath*. |
| B_ENTRY_NOT_FOUND | *path* does not refer to a possible entry. |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_FILE_EXISTS | An entry with that name does already exist. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**Since:** BeOS R3

---

### `FindEntry()`

```cpp
status_t BDirectory::FindEntry(const char * path, BEntry * entry, bool traverse = false)const
```

Finds an entry referred to by a path relative to the directory represented by this [BDirectory](classBDirectory.md). 


*path* may represent an absolute path. If the [BDirectory](classBDirectory.md) is not properly initialized then the entry is relative to the current directory. If the entry couldn't be found, *entry* is [Unset()](classBNode.md#a53045ffc7e7c8bf97487d0de2e925cc2).



> [!NOTE]
> The functionality of this method differs from BEntry::SetTo(BDirectory *, const char *, bool) in that it doesn't require the entry to exist, whereas this method does.


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The entry's *path* name. May be relative to this directory or an absolute path. |
| `entry` | A pointer to a [BEntry](classBEntry.md) to be initialized with the found entry. |
| `traverse` | Whether or not to follow a symbolic link. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *path* or *entry*. |
| B_ENTRY_NOT_FOUND | Entry not found. |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_NAME_TOO_LONG | The supplied path name (*path*) is too long. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |
| B_NOT_A_DIRECTORY | *path* includes a non-directory. |





**See also:** BEntry::SetTo(BDirectory *, const char *, bool)



**Since:** BeOS R3

---

### `GetEntry()`

```cpp
status_t BDirectory::GetEntry(BEntry * entry)const
```

Gets a [BEntry](classBEntry.md) object referring to the directory. If the initialization of *entry* fails, it is [Unset()](classBNode.md#a53045ffc7e7c8bf97487d0de2e925cc2). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | A pointer to the *entry* that will refer to the directory. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *entry*. |
| B_ENTRY_NOT_FOUND | Directory not found. |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**Since:** BeOS R3

---

### `GetNextDirents()`

```cpp
int32 BDirectory::GetNextDirents(dirent * buf, size_t bufSize, int32 count = INT_MAX)
```

Returns the next entries of the [BDirectory](classBDirectory.md) object as a pointer to dirent structures. 


Unlike [GetNextEntry()](classBDirectory.md#afc19ccbfe069ccd6d800d368eab24008) and [GetNextRef()](classBDirectory.md#a915d4da2de8eebd949f9feb2d3407c32), this method returns also the entries "." and "..".



> [!NOTE]
> The iterator used by this method is the same one used by [GetNextEntry()](classBDirectory.md#afc19ccbfe069ccd6d800d368eab24008), [GetNextRef()](classBDirectory.md#a915d4da2de8eebd949f9feb2d3407c32), [Rewind()](classBDirectory.md#a741e1b95a65ce83edad07baa11e5aa81) and [CountEntries()](classBDirectory.md#a9408e42d1c0683cd97991e8d3ac0b41f).


Parameters

| Parameter | Description |
| :--- | :--- |
| `buf` | A pointer to a buffer filled with dirent structures containing the found entries. |
| `bufSize` | The size of *buf*. |
| `count` | The maximum number of entries to be returned. |





**Returns:** The number of dirent structures stored in the buffer, 0 when there are no more entries to be returned or a status code on error.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | `NULL` *buf*. |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_NAME_TOO_LONG | The entry's name is too long for the buffer. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**Since:** BeOS R3


Implements [BEntryList](classBEntryList.md#a2f8498249c876866d5f53a8b89044871).

---

### `GetNextEntry()`

```cpp
status_t BDirectory::GetNextEntry(BEntry * entry, bool traverse = false)
```

Returns the next entry as a [BEntry](classBEntry.md) object. 


Unlike [GetNextDirents()](classBDirectory.md#ad163bac44f24104b1cd336487114e2fe) this method ignores "." and "..".



> [!NOTE]
> The iterator used by this method is the same one used by [GetNextRef()](classBDirectory.md#a915d4da2de8eebd949f9feb2d3407c32), [GetNextDirents()](classBDirectory.md#ad163bac44f24104b1cd336487114e2fe), [Rewind()](classBDirectory.md#a741e1b95a65ce83edad07baa11e5aa81) and [CountEntries()](classBDirectory.md#a9408e42d1c0683cd97991e8d3ac0b41f).


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | A pointer to a [BEntry](classBEntry.md) to be initialized to the found entry |
| `traverse` | Specifies whether or not to follow a symbolic link. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *entry*. |
| B_ENTRY_NOT_FOUND | No more entries found. |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**Since:** BeOS R3


Implements [BEntryList](classBEntryList.md#a52e6c79344a6e511e7890f008e7281d1).

---

### `GetNextRef()`

```cpp
status_t BDirectory::GetNextRef(entry_ref * ref)
```

Returns the [BDirectory](classBDirectory.md)'s next entry as an [entry_ref](structentry__ref.md). 


Unlike [GetNextDirents()](classBDirectory.md#ad163bac44f24104b1cd336487114e2fe) this method ignores "." and "..".



> [!NOTE]
> The iterator used be this method is the same one used by [GetNextEntry()](classBDirectory.md#afc19ccbfe069ccd6d800d368eab24008), [GetNextDirents()](classBDirectory.md#ad163bac44f24104b1cd336487114e2fe), [Rewind()](classBDirectory.md#a741e1b95a65ce83edad07baa11e5aa81) and [CountEntries()](classBDirectory.md#a9408e42d1c0683cd97991e8d3ac0b41f).


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | A pointer to an [entry_ref](structentry__ref.md) to be filled in with the data from the found entry. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *ref*. |
| B_ENTRY_NOT_FOUND | No more entries found. |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**Since:** BeOS R3


Implements [BEntryList](classBEntryList.md#a908ff7149239ab66683b12b27be917ee).

---

### `GetStatFor()`

```cpp
status_t BDirectory::GetStatFor(const char * path, struct stat * st)const
```

Returns the stat structure of the entry referred to by the supplied path name. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The entry's path name. May be relative to this directory or absolute, or `NULL` to get the directories stat info. |
| `st` | A pointer to the stat structure to be filled in by this method. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *st*. |
| B_ENTRY_NOT_FOUND | Entry not found. |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_NAME_TOO_LONG | The supplied path name (*path*) is too long. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |
| B_NOT_A_DIRECTORY | *path* includes a non-directory. |





**Since:** BeOS R3

---

### `IsRootDirectory()`

```cpp
bool BDirectory::IsRootDirectory()const
```

Returns whether the directory is the root directory of a volume. 



**Returns:** `true` if the [BDirectory](classBDirectory.md) is properly initialized and represents a root directory of a volume, `false` otherwise.



**Since:** BeOS R3

---

### `operator=()`

```cpp
BDirectory & BDirectory::operator=(const BDirectory & dir)
```

Assigns another [BDirectory](classBDirectory.md) to this [BDirectory](classBDirectory.md). 


If the passed in [BDirectory](classBDirectory.md) object is uninitialized, the returned object will be too. Otherwise it will refer to the same directory, unless an error occurs.


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The original [BDirectory](classBDirectory.md) object. |





**Returns:** A reference to this [BDirectory](classBDirectory.md) object.



**Since:** BeOS R3

---

### `Rewind()`

```cpp
status_t BDirectory::Rewind()
```

Rewinds the directory iterator. 



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**See also:** [BDirectory::GetNextEntry()](classBDirectory.md#afc19ccbfe069ccd6d800d368eab24008)



**Since:** BeOS R3


Implements [BEntryList](classBEntryList.md#a6cbcd041425e5a1225a762c72a4eb8af).

---

### `SetTo()`

```cpp
status_t BDirectory::SetTo(const BDirectory * dir, const char * path)
```

Re-initializes the [BDirectory](classBDirectory.md) to the directory referred to by the supplied path name relative to the specified [BDirectory](classBDirectory.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The base directory. |
| `path` | The directory path name relative to *dir*. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *dir* or *path*, or *path* is absolute. |
| B_ENTRY_NOT_FOUND | Directory not found. |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_NAME_TOO_LONG | The supplied path name (*path*) is too long. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |
| B_NOT_A_DIRECTORY | *path* includes a non-directory. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BDirectory::SetTo(const BEntry * entry)
```

Re-initializes the [BDirectory](classBDirectory.md) to the directory referred to by the supplied [BEntry](classBEntry.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | The [BEntry](classBEntry.md) referring to the directory. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *entry*. |
| B_ENTRY_NOT_FOUND | Directory not found. |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BDirectory::SetTo(const char * path)
```

Re-initializes the [BDirectory](classBDirectory.md) to the directory referred to by the supplied path name. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The directory's *path* name. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *path*. |
| B_ENTRY_NOT_FOUND | Directory not found. |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_NAME_TOO_LONG | The supplied path name (*path*) is too long. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |
| B_NOT_A_DIRECTORY | *path* includes a non-directory. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BDirectory::SetTo(const entry_ref * ref)
```

Re-initializes the [BDirectory](classBDirectory.md) to the directory referred to by the supplied [entry_ref](structentry__ref.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The [entry_ref](structentry__ref.md) referring to the directory. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *ref*. |
| B_ENTRY_NOT_FOUND | Directory not found. |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BDirectory::SetTo(const node_ref * nref)
```

Re-initializes the [BDirectory](classBDirectory.md) to the directory referred to by the supplied [node_ref](structnode__ref.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `nref` | The [node_ref](structnode__ref.md) referring to the directory. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *nref*. |
| B_ENTRY_NOT_FOUND | Directory not found. |
| B_PERMISSION_DENIED | Directory permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBDirectory.html).
