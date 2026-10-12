---
name: BNode
type: class
kit: storage_kit
brief: "A BNode represents a chunk of data in the filesystem"
source: haiku-book
---

# BNode Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A [BNode](classBNode.md) represents a chunk of data in the filesystem. 


The [BNode](classBNode.md) class provides an interface for manipulating the data and attributes belonging to filesystem entries. The [BNode](classBNode.md) is unaware of the name that refers to it in the filesystem (i.e. its entry), instead, a [BNode](classBNode.md) is concerned solely with the entry's data and attributes.



**Since:** BeOS R3

## Member List

### Public Member Functions

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

### `BNode()`

```cpp
BNode::BNode()
```

Creates an uninitialized [BNode](classBNode.md) object. 



**See also:** [SetTo()](classBNode.md#aa19fa8eac744cbbe8ef0cd67842fb350)



**Since:** BeOS R3

---

### `BNode()`

```cpp
BNode::BNode(const entry_ref * ref)
```

Creates a [BNode](classBNode.md) object and initializes it to the specified [entry_ref](structentry__ref.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The [entry_ref](structentry__ref.md) referring to the node. |





**Since:** BeOS R3

---

### `BNode()`

```cpp
BNode::BNode(const BEntry * entry)
```

Creates a [BNode](classBNode.md) object and initializes it to the specified filesystem entry. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | The [BEntry](classBEntry.md) referring to the node. |





**Since:** BeOS R3

---

### `BNode()`

```cpp
BNode::BNode(const char * path)
```

Creates a [BNode](classBNode.md) object and initializes it to the entry referred to by the specified path. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The *path* referring to the node. |





**Since:** BeOS R3

---

### `BNode()`

```cpp
BNode::BNode(const BDirectory * dir, const char * path)
```

Creates a [BNode](classBNode.md) object and initializes it to the entry referred to by the specified path rooted in the specified directory. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The base [BDirectory](classBDirectory.md). |
| `path` | The *path* name relative to *dir*. |





**Since:** BeOS R3

---

### `BNode()`

```cpp
BNode::BNode(const BNode & other)
```

Creates a copy of the given [BNode](classBNode.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BNode](classBNode.md) to be copied. |





**Since:** BeOS R3

---

### `~BNode()`

```cpp
BNode::~BNode()
```

Frees all resources associated with the [BNode](classBNode.md). 



**Since:** BeOS R3

---

### `Dup()`

```cpp
int BNode::Dup()
```

Gets the POSIX file descriptor referred to by this node. 


Remember to call close() on the file descriptor when you're through with it.



**Returns:** A valid file descriptor, or -1 if something went wrong.



**Since:** Haiku R1

---

### `GetAttrInfo()`

```cpp
status_t BNode::GetAttrInfo(const char * name, struct attr_info * info)const
```

Fills in the pre-allocated attr_info struct pointed to by *info* with information about the attribute specified by *name*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the attribute. |
| `info` | The attr_info structure to be filled in. |





**Returns:** `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *name* was `NULL`. |
| B_FILE_ERROR | The object was not initialized. |
| B_ENTRY_NOT_FOUND | The node had no attribute *name*. |





**Since:** BeOS R3

---

### `GetNextAttrName()`

```cpp
status_t BNode::GetNextAttrName(char * buffer)
```

Copies the name of the attribute into `buffer` and then advances the pointer to the next attribute. 


The name of the node is first copied into *buffer*, which should be at least `B_ATTR_NAME_LENGTH` characters long. The copied node name is \0 terminated. Once the name is copied the attribute list pointer is advanced to the next attribute in the list. When [GetNextAttrName()](classBNode.md#a7ce18e673746f0f2c385ec533f10a015) reaches the end of the list it returns `B_ENTRY_NOT_FOUND`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | A buffer to copy the name of the attribute into. |





**Returns:** `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The Attribute name was copied and there are more attribute names to copy. |
| B_BAD_VALUE | passed in *buffer* was `NULL`. |
| B_FILE_ERROR | The object was not initialized. |
| B_ENTRY_NOT_FOUND | There were no more attributes, the last attribute name had already been copied. |





**Since:** BeOS R3

---

### `GetStat()`

```cpp
status_t BNode::GetStat(struct stat * stat)const
```

Fills in the given stat structure with the `stat()` information for this object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `stat` | A pointer to a stat structure to be filled in. |





**Returns:** `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *stat*. |





**Since:** Haiku R1


Implements [BStatable](classBStatable.md#a0fd44591384a51393418c7360d67c51d).

---

### `InitCheck()`

```cpp
status_t BNode::InitCheck()const
```

Checks whether the object has been properly initialized or not. 



**Returns:** `B_OK` if the object has been properly initialized, or `B_NO_INIT` otherwise.



**Since:** BeOS R3

---

### `Lock()`

```cpp
status_t BNode::Lock()
```

Attains an exclusive lock on the data referred to by this node so that it may not be modified by any other objects or methods. 



**Returns:** `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_FILE_ERROR | The object is not initialized. |
| B_BUSY | The node is already locked. |





**Since:** BeOS R3

---

### `operator!=()`

```cpp
bool BNode::operator!=(const BNode & node)const
```

Tests whether this and the supplied [BNode](classBNode.md) object are not equal. 


Two [BNode](classBNode.md) objects are said to be equal if they're set to the same node, or if they're both unintialized.


Parameters

| Parameter | Description |
| :--- | :--- |
| `node` | The [BNode](classBNode.md) to be compared with |





**Returns:** `false`, if the [BNode](classBNode.md) objects are equal, `true` otherwise.



**Since:** BeOS R3

---

### `operator=()`

```cpp
BNode & BNode::operator=(const BNode & other)
```

Initializes the object as a copy of *other*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | the [BNode](classBNode.md) to be copied. |





**Returns:** A reference to this [BNode](classBNode.md) object.



**Since:** BeOS R3

---

### `operator==()`

```cpp
bool BNode::operator==(const BNode & node)const
```

Tests whether this and the supplied [BNode](classBNode.md) object are equal. 


Two [BNode](classBNode.md) objects are said to be equal if they're set to the same node, or if they're both unintialized


Parameters

| Parameter | Description |
| :--- | :--- |
| `node` | The [BNode](classBNode.md) to be compared against. |





**Returns:** `true`, if the [BNode](classBNode.md) objects are equal, `false` otherwise.



**Since:** BeOS R3

---

### `ReadAttr()`

```cpp
ssize_t BNode::ReadAttr(const char * attr, type_code type, off_t offset, void * buffer, size_t length)const
```

Reads data from an attribute into *buffer*. 


Reads *length* bytes of data from the attribute given by *name* into *buffer*. *type* and *offset* are currently ignored.


Parameters

| Parameter | Description |
| :--- | :--- |
| `attr` | The name of the attribute. |
| `type` | The type of the attribute (currently ignored). |
| `offset` | The index from which to read the data (currently ignored). |
| `buffer` | The buffer for the data to be read. |
| `length` | The number of bytes to be read. |





**Returns:** The number of bytes actually read.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | *attr* or *buffer* was `NULL`. |
| B_FILE_ERROR | The object was not initialized. |
| B_ENTRY_NOT_FOUND | The node had no attribute *attr*. |





**Since:** BeOS R3

---

### `ReadAttrString()`

```cpp
status_t BNode::ReadAttrString(const char * name, BString * result)const
```

Reads the data of the specified attribute into the pre-allocated *result*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | the name of the attribute. |
| `result` | the [BString](../support_kit/classBString.md) to be set to the value of the attribute. |





**Returns:** `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *name* or *result* was `NULL`. |
| B_FILE_ERROR | The object was not initialized. |
| B_ENTRY_NOT_FOUND | The node had no attribute *attr*. |





**Since:** Haiku R1

---

### `RemoveAttr()`

```cpp
status_t BNode::RemoveAttr(const char * name)
```

Deletes the attribute given by *name*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the attribute to remove. |





**Returns:** `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *name* was `NULL`. |
| B_FILE_ERROR | The object was not initialized or the node it referred to was read-only. |
| B_ENTRY_NOT_FOUND | The node had no attribute *name*. |
| B_NOT_ALLOWED | The node resided on a read-only volume. |





**Since:** BeOS R3

---

### `RenameAttr()`

```cpp
status_t BNode::RenameAttr(const char * oldName, const char * newName)
```

Moves the attribute given by *oldName* to *newName*. 


If *newName* already exists, the data is clobbered.


Parameters

| Parameter | Description |
| :--- | :--- |
| `oldName` | The name of the attribute to be renamed. |
| `newName` | The new name for the attribute. |





**Returns:** `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *oldName* or *newName* was `NULL`. |
| B_FILE_ERROR | The object was not initialized or the node it referred to was read only. |
| B_ENTRY_NOT_FOUND | The node had no attribute *oldName*. |
| B_NOT_ALLOWED | The node resided on a read-only volume. |





**Since:** BeOS R3

---

### `RewindAttrs()`

```cpp
status_t BNode::RewindAttrs()
```

Resets the object's attribute pointer to the first attribute in the list. 



**Returns:** `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_FILE_ERROR | Some other error occurred. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BNode::SetTo(const BDirectory * dir, const char * path)
```

Initializes the object to the entry referred by the specified *path* relative to the the specified directory. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The base [BDirectory](classBDirectory.md). |
| `path` | The path name relative to *dir*. |





**Returns:** `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *dir* was `NULL`. |
| B_ENTRY_NOT_FOUND | The entry could not be found. |
| B_BUSY | The entry was locked. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BNode::SetTo(const BEntry * entry)
```

Initializes the object to the specified filesystem *entry*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | The [BEntry](classBEntry.md) representing the entry. |





**Returns:** `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *entry* was `NULL`. |
| B_ENTRY_NOT_FOUND | The *entry* could not be found. |
| B_BUSY | The *entry* was locked. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BNode::SetTo(const char * path)
```

Initializes the object to the specified *path*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The entry's path name; *path* can be relative or absolute, and can contain "." and ".." elements. If path is relative, it uses the current working directory as the base directory. |





**Returns:** `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *path* was `NULL`. |
| B_ENTRY_NOT_FOUND | The entry could not be found. |
| B_BUSY | The entry of was locked. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BNode::SetTo(const entry_ref * ref)
```

Initializes the object to the specified [entry_ref](structentry__ref.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The [entry_ref](structentry__ref.md) referring to the entry. |





**Returns:** `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *ref* was `NULL`. |
| B_ENTRY_NOT_FOUND | The entry could not be found. |
| B_BUSY | The entry was locked. |





**Since:** BeOS R3

---

### `Sync()`

```cpp
status_t BNode::Sync()
```

Immediately performs any pending disk actions on the node. 



**Returns:** `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_FILE_ERROR | Something went wrong. |





**Since:** BeOS R3

---

### `Unlock()`

```cpp
status_t BNode::Unlock()
```

Unlocks the date referred to by this node. 



**Returns:** `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_FILE_ERROR | The object is not initialized. |
| B_BAD_VALUE | The node is not locked. |





**Since:** BeOS R3

---

### `Unset()`

```cpp
void BNode::Unset()
```

Returns the object to an uninitialized state. 



**Since:** BeOS R3

---

### `WriteAttr()`

```cpp
ssize_t BNode::WriteAttr(const char * attr, type_code type, off_t offset, const void * buffer, size_t length)
```

Writes data from a buffer to an attribute. 


Write *length* bytes of data from *buffer* to the attribute specified by *name* after erasing any data that existed previously. The type specified by *type* *is* remembered, and may be queried with [GetAttrInfo()](classBNode.md#a57b7c93cbf40df5b76b3c1aae2ad0201). The value of *offset* is currently ignored.


Parameters

| Parameter | Description |
| :--- | :--- |
| `attr` | The name of the attribute. |
| `type` | The type of the attribute. |
| `offset` | The index at which to write the data (currently ignored). |
| `buffer` | The buffer containing the data to be written. |
| `length` | The number of bytes to be written. |





**Returns:** The number of bytes actually written.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | *attr* or *buffer* was `NULL`. |
| B_FILE_ERROR | The object was not initialized or the node it refers to was read only. |
| B_NOT_ALLOWED | The node resides on a read only volume. |
| B_DEVICE_FULL | There was insufficient disk space to complete the operation. |
| B_NO_MEMORY | There was insufficient memory to complete the operation. |





**Since:** BeOS R3

---

### `WriteAttrString()`

```cpp
status_t BNode::WriteAttrString(const char * name, const BString * data)
```

Writes the specified string to the specified attribute, clobbering any previous data. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | the name of the attribute. |
| `data` | the [BString](../support_kit/classBString.md) to be written to the attribute. |





**Returns:** `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *name* or *data* was `NULL`. |
| B_FILE_ERROR | The object was not initialized or the node it referred to was read-only. |
| B_NOT_ALLOWED | The node resided on a read-only volume. |
| B_DEVICE_FULL | There was insufficient disk space to complete the operation. |
| B_NO_MEMORY | There was insufficient memory to complete the operation. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBNode.html).
