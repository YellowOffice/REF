---
name: BFile
type: class
kit: storage_kit
brief: "Provides the ability to read and write the data of a file"
source: haiku-book
---

# BFile Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Provides the ability to read and write the data of a file. 


The file is automatically opened when you initialize a [BFile](classBFile.md) and is automatically closed when you re-initialize or destroy the object.


Symbolic links are automatically transversed by opening a [BFile](classBFile.md). The node that the [BFile](classBFile.md) ends up opening will be the file or directory that the link points to, not the symbolic link file itself.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BFile](#acc17c5761f831ff59ed1d2dddadbf283) () — Creates an uninitialized BFile object.
* [BFile](#a120ba3f6f81f2f4131e8dcd32d0224ba) (const BDirectory *dir, const char *path, uint32 openMode) — Creates a BFile and initializes it to the file referred to by the supplied path name relative to the specified BDirectory and according to the specified open mode.
* [BFile](#acebf09ac918ffe81c881e378a9615b08) (const BEntry *entry, uint32 openMode) — Creates a BFile and initializes it to the file referred to by the supplied BEntry and according to the specified open mode.
* [BFile](#ab62773e8f0dd1d26d3d02adf802f68f6) (const BFile &file) — Creates a copy of the supplied BFile.
* [BFile](#a5cb98566815e053433ea2d92e0ff40fb) (const char *path, uint32 openMode) — Creates a BFile and initializes it to the file referred to by the supplied path name and according to the specified open mode.
* [BFile](#a9c0e05772cf7e28eeeddb4f620d95766) (const entry_ref *ref, uint32 openMode) — Creates a BFile and initializes it to the file referred to by the supplied entry_ref and according to the specified open mode.
* `virtual` [~BFile](#a0f221ac5358eadc498b3563e415a5823) () — Destroys the BFile object and frees all allocated resources.
* `virtual status_t` [GetSize](#a9438a3e18c34008d98fbb56cae890645) (off_t *size) const — Gets the size of the file.
* `bool` [IsReadable](#a103056399a92d41a8fba6de47668826a) () const — Reports whether or not the file is readable.
* `bool` [IsWritable](#a504077adeb53381ebdb796532da8a005) () const — Reports whether or not the file is writable.
* `BFile &` [operator=](#aa7034cc7cc2eea72f33d2c390f29362c) (const BFile &file) — Assigns another BFile to this BFile.
* `virtual off_t` [Position](#aef5499cdc105ac4817f669bad3ca05b8) () const — Gets the current read/write position within the file.
* `virtual ssize_t` [Read](#a84879555b0c3bee54e36abdeeb2cb559) (void *buffer, size_t size) — Reads a number of bytes from the file into a buffer.
* `virtual ssize_t` [ReadAt](#aa66cbdba802924c4b5fbeac6a2765805) (off_t location, void *buffer, size_t size) — Reads a number of bytes from a certain position within the file into a buffer.
* `virtual off_t` [Seek](#a396e6721a72e8fbed4056e37741dcb8a) (off_t offset, uint32 seekMode) — Seeks to another read/write position within the file.
* `virtual status_t` [SetSize](#a5b8f0932cff0d50b6e0c7aea169a74ef) (off_t size) — Sets the size of the file.
* `status_t` [SetTo](#abef98fdf0011118625928c8efcaea8b6) (const BDirectory *dir, const char *path, uint32 openMode) — Re-initializes the BFile to the file referred to by the supplied path name relative to the specified BDirectory and according to the specified open mode.
* `status_t` [SetTo](#a35748205cd1aa8e18402c4ae6be2113d) (const BEntry *entry, uint32 openMode) — Re-initializes the BFile to the file referred to by the supplied BEntry and according to the specified open mode.
* `status_t` [SetTo](#ad706418be512a2aa27db95a738933b0c) (const char *path, uint32 openMode) — Re-initializes the BFile to the file referred to by the supplied path name and according to the specified open mode.
* `status_t` [SetTo](#a2897b1f33eea3c75f16311b37e6ee57a) (const entry_ref *ref, uint32 openMode) — Re-initializes the BFile to the file referred to by the supplied entry_ref and according to the specified open mode.
* `virtual ssize_t` [Write](#afcf216fde234f4fd0754409617bedc55) (const void *buffer, size_t size) — Writes a number of bytes from a buffer into the file.
* `virtual ssize_t` [WriteAt](#a43a09d7441f9fda29cc90c1f3612021c) (off_t location, const void *buffer, size_t size) — Writes a number of bytes from a buffer at a certain position into the file.
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
* [BPositionIO](#a08051e865cd2623fab56c3733ecbf099) () — This constructor does nothing.
* `virtual` [~BPositionIO](#a505defae83a1a6937c77b9acac2aaafe) () — This destructor does nothing.
* `virtual status_t` [GetSize](#a5be704340522f36f80697c6bc883a00d) (off_t *size) const — Get the size of the object or data.
* `virtual off_t` [Position](#a4ebc2cd7a7493767e79fa6d88657a84a) () const =0 — Pure virtual to return the current position of the cursor.
* `virtual ssize_t` [Read](#abce66c314f7cbd5ab6de0e6480bd7a00) (void *buffer, size_t size) — Read data from current position.
* `virtual ssize_t` [ReadAt](#a6eb7aff1d69bf3049b2b421da52fdf8f) (off_t position, void *buffer, size_t size)=0 — Pure virtual to read data from a certain position.
* `status_t` [ReadAtExactly](#a91bab7ae60926dbe3726bc73734318b6) (off_t position, void *buffer, size_t size, size_t *_bytesRead=NULL) — Reads an exact amount of data from the object at the specified position into a buffer.
* `virtual off_t` [Seek](#af8296875d9711dd498b0fbcace028abc) (off_t position, uint32 seekMode)=0 — Pure virtual to move the cursor to a certain position.
* `virtual status_t` [SetSize](#a35613c7ee06c7c9583ca2505e1fdff28) (off_t size) — Set the size of the object or data.
* `virtual ssize_t` [Write](#a50ec7f6b834893a153d46c0f3c0e09c4) (const void *buffer, size_t size) — Write data to the current position.
* `virtual ssize_t` [WriteAt](#a0efce1a07d1d6509e8ec00598244ace1) (off_t position, const void *buffer, size_t size)=0 — Pure virtual to write data to a certain position.
* `status_t` [WriteAtExactly](#a18100db340087226321c332182816d27) (off_t position, const void *buffer, size_t size, size_t *_bytesWritten=NULL) — Writes an exact amount of data from a buffer to the object at the specified position.
* [BDataIO](#a67891b7afe78d6a77845dd0352218801) () — This constructor does nothing.
* `virtual` [~BDataIO](#a45daa9db670dd2e5b83efcefcf8dbaed) () — This destructor does nothing.
* `virtual status_t` [Flush](#a38a8df63b367585fe5e6b6a85c406d05) () — Writes pending data to underlying storage.
* `virtual ssize_t` [Read](#a847ec8576c368bf9aada412e92aed623) (void *buffer, size_t size) — Reads data from the object into a buffer.
* `status_t` [ReadExactly](#a3a0b0fc36232531a1d8c1144a7d75741) (void *buffer, size_t size, size_t *_bytesRead=NULL) — Reads an exact amount of data from the object into a buffer.
* `virtual ssize_t` [Write](#a01692303eba7601c6a7cfa72c06d6afb) (const void *buffer, size_t size) — Writes data from a buffer to the object.
* `status_t` [WriteExactly](#a0095cfffa454a82eac3dedda2e187ab7) (const void *buffer, size_t size, size_t *_bytesWritten=NULL) — Writes an exact amount of data from a buffer to the object.

## Detailed Member Documentation

### `BFile()`

```cpp
BFile::BFile()
```

Creates an uninitialized [BFile](classBFile.md) object. 


Should be followed by a call to one of the [SetTo()](classBFile.md#a2897b1f33eea3c75f16311b37e6ee57a) methods, or an assignment:


* [SetTo(const entry_ref* ref, uint32 openMode)](classBFile.md#a2897b1f33eea3c75f16311b37e6ee57a)

* [SetTo(const BEntry* entry, uint32 openMode)](classBFile.md#a35748205cd1aa8e18402c4ae6be2113d)

* [SetTo(const char* path, uint32 openMode)](classBFile.md#ad706418be512a2aa27db95a738933b0c)

* [SetTo(const BDirectory* dir, const char* path, uint32 openMode)](classBFile.md#abef98fdf0011118625928c8efcaea8b6)

* [operator=(const BFile &file)](classBFile.md#aa7034cc7cc2eea72f33d2c390f29362c)




**Since:** BeOS R3

---

### `BFile()`

```cpp
BFile::BFile(const BFile & file)
```

Creates a copy of the supplied [BFile](classBFile.md). 


If *file* is uninitialized, the newly constructed [BFile](classBFile.md) will be too.


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | The [BFile](classBFile.md) object to be copied. |





**Since:** BeOS R3

---

### `BFile()`

```cpp
BFile::BFile(const entry_ref * ref, uint32 openMode)
```

Creates a [BFile](classBFile.md) and initializes it to the file referred to by the supplied [entry_ref](structentry__ref.md) and according to the specified open mode. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The [entry_ref](structentry__ref.md) referring to the file. |
| `openMode` | The mode in which the file should be opened. |





**See also:** [SetTo(const entry_ref* ref, uint32 openMode)](classBFile.md#a2897b1f33eea3c75f16311b37e6ee57a)



**Since:** BeOS R3

---

### `BFile()`

```cpp
BFile::BFile(const BEntry * entry, uint32 openMode)
```

Creates a [BFile](classBFile.md) and initializes it to the file referred to by the supplied [BEntry](classBEntry.md) and according to the specified open mode. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | The [BEntry](classBEntry.md) referring to the file. |
| `openMode` | The mode in which the file should be opened. |





**See also:** [SetTo(const BEntry* entry, uint32 openMode)](classBFile.md#a35748205cd1aa8e18402c4ae6be2113d)



**Since:** BeOS R3

---

### `BFile()`

```cpp
BFile::BFile(const char * path, uint32 openMode)
```

Creates a [BFile](classBFile.md) and initializes it to the file referred to by the supplied path name and according to the specified open mode. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The file's path name. |
| `openMode` | The mode in which the file should be opened. |





**See also:** [SetTo(const char* path, uint32 openMode)](classBFile.md#ad706418be512a2aa27db95a738933b0c)



**Since:** BeOS R3

---

### `BFile()`

```cpp
BFile::BFile(const BDirectory * dir, const char * path, uint32 openMode)
```

Creates a [BFile](classBFile.md) and initializes it to the file referred to by the supplied path name relative to the specified [BDirectory](classBDirectory.md) and according to the specified open mode. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The [BDirectory](classBDirectory.md), relative to which the file's path name is given. |
| `path` | The file's path name relative to *dir*. |
| `openMode` | The mode in which the file should be opened. |





**See also:** [SetTo(const BDirectory* dir, const char* path, uint32 openMode)](classBFile.md#abef98fdf0011118625928c8efcaea8b6)



**Since:** BeOS R3

---

### `~BFile()`

```cpp
BFile::~BFile()
```

Destroys the [BFile](classBFile.md) object and frees all allocated resources. 


If the file is properly initialized, the file descriptor is closed.



**Since:** BeOS R3

---

### `GetSize()`

```cpp
status_t BFile::GetSize(off_t * size)const
```

Gets the size of the file. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `size` | The file size to fill out. |





**Returns:** A status code.



**See also:** [BStatable::GetSize()](classBStatable.md#a52975e361937ae26f7c854da34e6e51a)



**Since:** BeOS R3


Reimplemented from [BPositionIO](../support_kit/classBPositionIO.md#a5be704340522f36f80697c6bc883a00d).

---

### `IsReadable()`

```cpp
bool BFile::IsReadable()const
```

Reports whether or not the file is readable. 



**Returns:** * `true`, if the [BFile](classBFile.md) has been initialized properly and the file has been been opened for reading,

* `false`, otherwise.



**Since:** BeOS R3

---

### `IsWritable()`

```cpp
bool BFile::IsWritable()const
```

Reports whether or not the file is writable. 



**Returns:** * `true`, if the [BFile](classBFile.md) has been initialized properly and the file has been opened for writing,

* `false`, otherwise.



**Since:** BeOS R3

---

### `operator=()`

```cpp
BFile & BFile::operator=(const BFile & file)
```

Assigns another [BFile](classBFile.md) to this [BFile](classBFile.md). 


If the other [BFile](classBFile.md) is uninitialized, this one will be too. Otherwise it will refer to the same file using the same mode, unless an error occurs.


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | The original [BFile](classBFile.md) to assign from. |





**Returns:** A reference to the assigned [BFile](classBFile.md).



**Since:** BeOS R3

---

### `Position()`

```cpp
off_t BFile::Position()const
```

Gets the current read/write position within the file. 



**Returns:** The current read/write position relative to the beginning of the file or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_ERROR | After a [Seek()](classBFile.md#a396e6721a72e8fbed4056e37741dcb8a) before the beginning of the file. |
| B_FILE_ERROR | The file has not been initialized. |





**Since:** BeOS R3


Implements [BPositionIO](../support_kit/classBPositionIO.md#a4ebc2cd7a7493767e79fa6d88657a84a).

---

### `Read()`

```cpp
ssize_t BFile::Read(void * buffer, size_t size)
```

Reads a number of bytes from the file into a buffer. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | The buffer the data from the file shall be written to. |
| `size` | The number of bytes that shall be read. |





**Returns:** The number of bytes read or an error code.



**Since:** BeOS R3


Reimplemented from [BPositionIO](../support_kit/classBPositionIO.md#abce66c314f7cbd5ab6de0e6480bd7a00).

---

### `ReadAt()`

```cpp
ssize_t BFile::ReadAt(off_t location, void * buffer, size_t size)
```

Reads a number of bytes from a certain position within the file into a buffer. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `location` | The position (in bytes) within the file from which the data shall be read. |
| `buffer` | The buffer the data from the file shall be written to. |
| `size` | The number of bytes that shall be read. |





**Returns:** The number of bytes read or an error code.



**Since:** BeOS R3


Implements [BPositionIO](../support_kit/classBPositionIO.md#a6eb7aff1d69bf3049b2b421da52fdf8f).

---

### `Seek()`

```cpp
off_t BFile::Seek(off_t offset, uint32 seekMode)
```

Seeks to another read/write position within the file. 


It is allowed to seek past the end of the file. A subsequent call to [Write()](classBFile.md#afcf216fde234f4fd0754409617bedc55) will pad the file with undefined data. Seeking before the beginning of the file will fail and the behavior of subsequent [Read()](classBFile.md#a84879555b0c3bee54e36abdeeb2cb559) or [Write()](classBFile.md#afcf216fde234f4fd0754409617bedc55) invocations will be undefined.


Parameters

| Parameter | Description |
| :--- | :--- |
| `offset` | New read/write position, depending on *seekMode* relative to the beginning or the end of the file or the current position. |
| `seekMode` | * `SEEK_SET:` move relative to the beginning of the file.  * `SEEK_CUR:` move relative to the current position.  * `SEEK_END:` move relative to the end of the file. |





**Returns:** The new read/write position relative to the beginning of the file or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_ERROR | Trying to seek before the beginning of the file. |
| B_FILE_ERROR | The file is not properly initialized. |





**Since:** BeOS R3


Implements [BPositionIO](../support_kit/classBPositionIO.md#af8296875d9711dd498b0fbcace028abc).

---

### `SetSize()`

```cpp
status_t BFile::SetSize(off_t size)
```

Sets the size of the file. 


If the file is shorter than *size* bytes it will be padded with unspecified data to the requested size. If it is larger, it will be truncated.



> [!NOTE]
> There's no problem with setting the size of a [BFile](classBFile.md) opened in `B_READ_ONLY` mode, unless the file resides on a read only volume.


Parameters

| Parameter | Description |
| :--- | :--- |
| `size` | The new file size. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NOT_ALLOWED | Trying to set the size of a file on a read only volume. |
| B_DEVICE_FULL | There's not enough space left on the volume. |





**Since:** BeOS R3


Reimplemented from [BPositionIO](../support_kit/classBPositionIO.md#a35613c7ee06c7c9583ca2505e1fdff28).

---

### `SetTo()`

```cpp
status_t BFile::SetTo(const BDirectory * dir, const char * path, uint32 openMode)
```

Re-initializes the [BFile](classBFile.md) to the file referred to by the supplied path name relative to the specified [BDirectory](classBDirectory.md) and according to the specified open mode. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The [BDirectory](classBDirectory.md), relative to which the file's path name is given. |
| `path` | The file's path name relative to *dir*. |
| `openMode` | The mode in which the file should be opened. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *dir* or *path* or bad *openMode*. |
| B_ENTRY_NOT_FOUND | File not found or failed to create file. |
| B_FILE_EXISTS | File exists and `B_FAIL_IF_EXISTS` was passed. |
| B_PERMISSION_DENIED | File permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BFile::SetTo(const BEntry * entry, uint32 openMode)
```

Re-initializes the [BFile](classBFile.md) to the file referred to by the supplied [BEntry](classBEntry.md) and according to the specified open mode. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | the [BEntry](classBEntry.md) referring to the file |
| `openMode` | the mode in which the file should be opened |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *entry* or bad *openMode*. |
| B_ENTRY_NOT_FOUND | File not found or failed to create file. |
| B_FILE_EXISTS | File exists and `B_FAIL_IF_EXISTS` was passed. |
| B_PERMISSION_DENIED | File permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BFile::SetTo(const char * path, uint32 openMode)
```

Re-initializes the [BFile](classBFile.md) to the file referred to by the supplied path name and according to the specified open mode. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The file's path name. |
| `openMode` | The mode in which the file should be opened. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *path* or bad *openMode*. |
| B_ENTRY_NOT_FOUND | File not found or failed to create file. |
| B_FILE_EXISTS | File exists and `B_FAIL_IF_EXISTS` was passed. |
| B_PERMISSION_DENIED | File permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BFile::SetTo(const entry_ref * ref, uint32 openMode)
```

Re-initializes the [BFile](classBFile.md) to the file referred to by the supplied [entry_ref](structentry__ref.md) and according to the specified open mode. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The [entry_ref](structentry__ref.md) referring to the file. |
| `openMode` | The mode in which the file should be opened *openMode* must be a bitwise or of exactly one of the flags. * `B_READ_ONLY:` The file is opened read only.  * `B_WRITE_ONLY:` The file is opened write only.  * `B_READ_WRITE:` The file is opened for random read/write access. and any number of the flags  * `B_CREATE_FILE:` A new file will be created, if it does not already exist.  * `B_FAIL_IF_EXISTS:` If the file does already exist and `B_CREATE_FILE` is set, [SetTo()](classBFile.md#a2897b1f33eea3c75f16311b37e6ee57a) fails.  * `B_ERASE_FILE:` An already existing file is truncated to zero size.  * `B_OPEN_AT_END:` [Seek()](classBFile.md#a396e6721a72e8fbed4056e37741dcb8a) to the end of the file after opening. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *ref* or bad *openMode*. |
| B_ENTRY_NOT_FOUND | File not found or failed to create file. |
| B_FILE_EXISTS | File exists and `B_FAIL_IF_EXISTS` was passed. |
| B_PERMISSION_DENIED | File permissions didn't allow operation. |
| B_NO_MEMORY | Insufficient memory for operation. |
| B_LINK_LIMIT | Indicates a cyclic loop within the file system. |
| B_BUSY | A node was busy. |
| B_FILE_ERROR | A general file error. |
| B_NO_MORE_FDS | The application has run out of file descriptors. |





**Since:** BeOS R3

---

### `Write()`

```cpp
ssize_t BFile::Write(const void * buffer, size_t size)
```

Writes a number of bytes from a buffer into the file. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | The buffer containing the data to be written to the file. |
| `size` | The number of bytes that shall be written. |





**Returns:** The number of bytes actually written or an error code.



**Since:** BeOS R3


Reimplemented from [BPositionIO](../support_kit/classBPositionIO.md#a50ec7f6b834893a153d46c0f3c0e09c4).

---

### `WriteAt()`

```cpp
ssize_t BFile::WriteAt(off_t location, const void * buffer, size_t size)
```

Writes a number of bytes from a buffer at a certain position into the file. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `location` | The position (in bytes) within the file at which the data shall be written. |
| `buffer` | The buffer containing the data to be written to the file. |
| `size` | The number of bytes that shall be written. |





**Returns:** The number of bytes actually written or an error code.



**Since:** BeOS R3


Implements [BPositionIO](../support_kit/classBPositionIO.md#a0efce1a07d1d6509e8ec00598244ace1).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBFile.html).
