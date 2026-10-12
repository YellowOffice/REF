---
name: BResources
type: class
kit: storage_kit
brief: "Provides an interface for accessing and manipulating file resources"
source: haiku-book
---

# BResources Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Provides an interface for accessing and manipulating file resources. 


[BResources](classBResources.md) delegates most of the work to ResourcesContainer and ResourceFile. The former manages a collections of ResourceItem objects's (the actual resources) whereas the latter provides the file I/O functionality.


An [InitCheck()](classBResources.md#aea04304030d7b1996a37a3a00c3aa977) method is not needed, since a [BResources](classBResources.md) object will never be invalid. It always serves as a resources container, even if it is not associated with a file. It is always possible to [WriteTo()](classBResources.md#a01aafeeadafe79f583fe7e83df3d063c) the resources [BResources](classBResources.md) contains to a file (a valid one of course).



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BResources](#ad1e463f5bdc164e205a882b872cf58ef) () — Creates an uninitialized BResources object.
* [BResources](#a5d744f91e84857bd91ba54a21c082653) (const BFile *file, bool clobber=false) — Creates a BResources object that represents the resources of the supplied file.
* [BResources](#a09b282c868b7e9bdf339bece74c1bceb) (const char *path, bool clobber=false) — Creates a BResources object that represents the resources of the file referenced by the supplied path.
* [BResources](#ace28cb708db56d032ae51fc3b7eac41f) (const entry_ref *ref, bool clobber=false) — Creates a BResources object that represents the resources of the file referenced by the supplied ref.
* `virtual` [~BResources](#a0b612db75a3c10ecc6f17fd27c1432f8) () — Destroys the BResources object and frees any associated resources.
* `status_t` [AddResource](#a4a470900257d43bc3c110c2b58e87bc4) (type_code type, int32 id, const void *data, size_t length, const char *name=NULL) — Adds a new resource to the file.
* `const BFile &` [File](#aa3bfbfac9750deeccbdeb0c0e2f01013) () const — Gets a reference to the internal BFile object.
* `bool` [GetResourceInfo](#a4d5e969ae90214873d6ada21ac3715e3) (const void *byPointer, type_code *typeFound, int32 *idFound, size_t *lengthFound, const char **nameFound) — Gets information about a resource identified by byPointer.
* `bool` [GetResourceInfo](#abe6ff3ccaf5f71d229f765c934362ec2) (int32 byIndex, type_code *typeFound, int32 *idFound, const char **nameFound, size_t *lengthFound) — Gets information about a resource identified by byindex.
* `bool` [GetResourceInfo](#a234d4ab82091cb9637c3f94b8e2c0e45) (type_code byType, const char *andName, int32 *idFound, size_t *lengthFound) — Gets information about a resource identified by byType and andName.
* `bool` [GetResourceInfo](#a099ed545021dc84983657347245e5ee5) (type_code byType, int32 andID, const char **nameFound, size_t *lengthFound) — Gets information about a resource identified by byType and andID.
* `bool` [GetResourceInfo](#a66efbde2f4656ecd88cba77acbf8293a) (type_code byType, int32 andIndex, int32 *idFound, const char **nameFound, size_t *lengthFound) — Gets information about a resource identified by byType and andIndex.
* `bool` [HasResource](#a64280e5289fcf1f9308f1f962c6fb56b) (type_code type, const char *name) — Returns whether the file contains a resource with the specified type and name.
* `bool` [HasResource](#a38d2f0f9fb67f2633c43730d05d541d6) (type_code type, int32 id) — Returns whether the file contains a resource with the specified type and id.
* `status_t` [MergeFrom](#a81e0bb83cae30eed1f9657a982fc02aa) (BFile *fromFile) — Adds the resources of fromFile to the internal file of the BResources object.
* `status_t` [RemoveResource](#a2c4b0aa9e7e0cad840af9f47f7c452ae) (const void *resource) — Removes a resource identified by resource.
* `status_t` [RemoveResource](#a810e6f6ed02581763e887cbf83592cc3) (type_code type, int32 id) — Removes a resource identified by type and id.
* `status_t` [Sync](#a040b5cfd22da43472571bcf5c2f99fd4) () — Writes all changes to the resources to the file.
* `status_t` [WriteTo](#a01aafeeadafe79f583fe7e83df3d063c) (BFile *file) — Writes the resources to a new file.
* `status_t` [SetTo](#a7c59913cefb4f22ac9ae6f2976b21d57) (const BFile *file, bool clobber=false) — Initializes the BResources object to represent the resources of the supplied file.
* `status_t` [SetTo](#af5871eccccce9020623345cf145f298e) (const char *path, bool clobber=false) — Initialized the BResources object to represent the resources of the file referred to by the supplied path.
* `status_t` [SetTo](#a4bc5dcfcb1b0058db9552a320daf5e7d) (const entry_ref *ref, bool clobber=false) — Initialized the BResources object to represent the resources of the file referenced by the supplied ref.
* `status_t` [SetToImage](#a7134ad1f4514b6b5546957aade7ca77a) (image_id image, bool clobber=false) — Initialized the BResources object to represent the resources of the file from which the specified image has been loaded.
* `status_t` [SetToImage](#aaa710351d1391401e946877f579167b6) (const void *codeOrDataPointer, bool clobber=false) — Initialized the BResources object to represent the resources of the file from which the specified pointer has been loaded.
* `void` [Unset](#a4c840520fffd3c019ee6e910fb1088d9) () — Returns the BResources object to an uninitialized state.
* `status_t` [InitCheck](#aea04304030d7b1996a37a3a00c3aa977) () const — Gets the initialization status of the object.
* `const void *` [LoadResource](#aa215bc39f8373df2aa9c12aaf55c760c) (type_code type, int32 id, size_t *_size) — Loads a resource identified by type and id into memory.
* `const void *` [LoadResource](#a311ef2ea74c914403316dca0477b90c3) (type_code type, const char *name, size_t *_size) — Loads a resource identified by type and name into memory.
* `status_t` [PreloadResourceType](#ad9ba84db4f28b6e32a155e1713ecc1ac) (type_code type=0) — Loads all resources of the specified type into memory.
* `status_t` [WriteResource](#ae78de70e805234e12a25db9e88342a82) (type_code type, int32 id, const void *data, off_t offset, size_t length) _DEPRECATED — Writes data into an existing resource. (deprecated, use AddResource() instead)
* `status_t` [ReadResource](#a300e1947c6ef386580d072c6d60e28be) (type_code type, int32 id, void *data, off_t offset, size_t length) _DEPRECATED — Reads data from an existing resource. (deprecated, use LoadResource() instead)
* `void *` [FindResource](#a63e5d607705b2375bc164ac6474f5ccc) (type_code type, int32 id, size_t *lengthFound) _DEPRECATED — Finds a resource by type and id and returns a pointer to a copy of its data. (deprecated, use LoadResource() instead)
* `void *` [FindResource](#aa9f3f9b5b4e0f213f3de3c6b25f46b69) (type_code type, const char *name, size_t *lengthFound) _DEPRECATED — Finds a resource by type and name and returns a pointer to a copy of its data. (deprecated, use LoadResource() instead)

## Detailed Member Documentation

### `BResources()`

```cpp
BResources::BResources()
```

Creates an uninitialized [BResources](classBResources.md) object. 



**See also:** [SetTo()](classBResources.md#a7c59913cefb4f22ac9ae6f2976b21d57)



**Since:** BeOS R3

---

### `BResources()`

```cpp
BResources::BResources(const BFile * file, bool clobber = false)
```

Creates a [BResources](classBResources.md) object that represents the resources of the supplied *file*. 


If the *clobber* argument is `true`, the data of the file are erased and it is turned into an empty resource file. Otherwise *file* must refer either to a resource file or to an executable (ELF or PEF binary). If the file has been opened `B_READ_ONLY`, only read access to its resources is possible.


The [BResources](classBResources.md) object makes a copy of *file*, that is the caller remains owner of the [BFile](classBFile.md) object.


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | The file to create a BResource object from. |
| `clobber` | If `true`, the data of the file are erased. |





**Since:** BeOS R3

---

### `BResources()`

```cpp
BResources::BResources(const char * path, bool clobber = false)
```

Creates a [BResources](classBResources.md) object that represents the resources of the file referenced by the supplied *path*. 


If the *clobber* argument is `true`, the data of the file are erased and it is turned into an empty resource file. Otherwise *path* must refer either to a resource file or to an executable (ELF or PEF binary).


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | A path referring to the file to create a BResource object from. |
| `clobber` | If `true`, the data of the file are erased. |





**Since:** Haiku R1

---

### `BResources()`

```cpp
BResources::BResources(const entry_ref * ref, bool clobber = false)
```

Creates a [BResources](classBResources.md) object that represents the resources of the file referenced by the supplied *ref*. 


If the *clobber* argument is `true`, the data of the file are erased and it is turned into an empty resource file. Otherwise *ref* must refer either to a resource file or to an executable (ELF or PEF binary).


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | An [entry_ref](structentry__ref.md) referring to the file to create a BResource object from. |
| `clobber` | If `true`, the data of the file are erased. |





**Since:** Haiku R1

---

### `~BResources()`

```cpp
BResources::~BResources()
```

Destroys the [BResources](classBResources.md) object and frees any associated resources. 


[Sync()](classBResources.md#a040b5cfd22da43472571bcf5c2f99fd4) is first called to make sure that the changes are written back to the file.



**Since:** BeOS R3

---

### `AddResource()`

```cpp
status_t BResources::AddResource(type_code type, int32 id, const void * data, size_t length, const char * name = NULL)
```

Adds a new resource to the file. 


If a resource already exists with the same *type* and *id* it is replaced. The caller keeps the ownership of the supplied chunk of memory containing the resource data.


Supplying an empty *name* (`""`) is equivalent to supplying a `NULL` *name*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The type of the resource. |
| `id` | The ID of the resource. |
| `data` | The resource data. |
| `length` | The size of the data in bytes. |
| `name` | The name of the resource (may be empty or `NULL`). |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *data* was `NULL`. |
| B_FILE_ERROR | A file error occurred. |
| B_NO_MEMORY | Not enough memory for the operation. |
| B_NOT_ALLOWED | The file was opened read only. |





**Since:** BeOS R3

---

### `File()`

```cpp
const BFile & BResources::File()const
```

Gets a reference to the internal [BFile](classBFile.md) object. 



**Returns:** A reference to the internal [BFile](classBFile.md) object.



**Since:** BeOS R4

---

### `FindResource()`

```cpp
void * BResources::FindResource(type_code type, const char * name, size_t * lengthFound)
```

Finds a resource by *type* and *name* and returns a pointer to a copy of its data. (deprecated, use [LoadResource()](classBResources.md#aa215bc39f8373df2aa9c12aaf55c760c) instead) 



> [!WARNING]
> The caller is responsible for calling free() to release the memory used by the returned data.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The type of the resource to find. |
| `name` | The name of the resource to find. |
| `lengthFound` | A pointer to a variable into which the size of the resource data shall be written. |





**Returns:** A pointer to the resource data if everything went fine or `NULL` if an error occurred.



**Since:** BeOS R3

---

### `FindResource()`

```cpp
void * BResources::FindResource(type_code type, int32 id, size_t * lengthFound)
```

Finds a resource by *type* and *id* and returns a pointer to a copy of its data. (deprecated, use [LoadResource()](classBResources.md#aa215bc39f8373df2aa9c12aaf55c760c) instead) 



> [!WARNING]
> The caller is responsible for calling free() to release the memory used by the returned data.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The type of the resource to find. |
| `id` | The ID of the resource to find. |
| `lengthFound` | A pointer to a variable into which the size of the resource data shall be written. |





**Returns:** A pointer to the resource data if everything went fine or `NULL` if an error occurred.



**Since:** BeOS R3

---

### `GetResourceInfo()`

```cpp
bool BResources::GetResourceInfo(const void * byPointer, type_code * typeFound, int32 * idFound, size_t * lengthFound, const char ** nameFound)
```

Gets information about a resource identified by *byPointer*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `byPointer` | The pointer to the resource data (formerly returned by [LoadResource()](classBResources.md#aa215bc39f8373df2aa9c12aaf55c760c)). |
| `typeFound` | A pointer to a variable the type of the found resource shall be written into. |
| `idFound` | A pointer to a variable the ID of the found resource shall be written into. |
| `lengthFound` | A pointer to a variable the data size of the found resource shall be written into. |
| `nameFound` | A pointer to a variable the name pointer of the found resource shall be written into. |





**Returns:** `true`, if a matching resource could be found, `false` otherwise.



**Since:** BeOS R4

---

### `GetResourceInfo()`

```cpp
bool BResources::GetResourceInfo(int32 byIndex, type_code * typeFound, int32 * idFound, const char ** nameFound, size_t * lengthFound)
```

Gets information about a resource identified by *byindex*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `byIndex` | The index of the resource in the file. |
| `typeFound` | A pointer to a variable the type of the found resource shall be written into. |
| `idFound` | A pointer to a variable the ID of the found resource shall be written into. |
| `nameFound` | A pointer to a variable the name pointer of the found resource shall be written into. |
| `lengthFound` | A pointer to a variable the data size of the found resource shall be written into. |





**Returns:** `true`, if a matching resource could be found, `false` otherwise.



**Since:** BeOS R3

---

### `GetResourceInfo()`

```cpp
bool BResources::GetResourceInfo(type_code byType, const char * andName, int32 * idFound, size_t * lengthFound)
```

Gets information about a resource identified by *byType* and *andName*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `byType` | The resource type. |
| `andName` | The resource name. |
| `idFound` | A pointer to a variable the ID of the found resource shall be written into. |
| `lengthFound` | A pointer to a variable the data size of the found resource shall be written into. |





**Returns:** `true`, if a matching resource could be found, `false` otherwise.



**Since:** BeOS R3

---

### `GetResourceInfo()`

```cpp
bool BResources::GetResourceInfo(type_code byType, int32 andID, const char ** nameFound, size_t * lengthFound)
```

Gets information about a resource identified by *byType* and *andID*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `byType` | The resource type. |
| `andID` | The resource ID. |
| `nameFound` | A pointer to a variable the name pointer of the found resource shall be written into. |
| `lengthFound` | A pointer to a variable the data size of the found resource shall be written into. |





**Returns:** `true`, if a matching resource could be found, `false` otherwise.



**Since:** BeOS R3

---

### `GetResourceInfo()`

```cpp
bool BResources::GetResourceInfo(type_code byType, int32 andIndex, int32 * idFound, const char ** nameFound, size_t * lengthFound)
```

Gets information about a resource identified by *byType* and *andIndex*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `byType` | The resource type. |
| `andIndex` | The index into a array of resources of type *byType*. |
| `idFound` | A pointer to a variable the ID of the found resource shall be written into. |
| `nameFound` | A pointer to a variable the name pointer of the found resource shall be written into. |
| `lengthFound` | A pointer to a variable the data size of the found resource shall be written into. |





**Returns:** `true`, if a matching resource could be found, `false` otherwise.



**Since:** BeOS R3

---

### `HasResource()`

```cpp
bool BResources::HasResource(type_code type, const char * name)
```

Returns whether the file contains a resource with the specified *type* and *name*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The resource type to check. |
| `name` | The name of the resource to check. |





**Returns:** `true`, if the file contains a matching resource, `false` otherwise.



**Since:** BeOS R3

---

### `HasResource()`

```cpp
bool BResources::HasResource(type_code type, int32 id)
```

Returns whether the file contains a resource with the specified *type* and *id*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The resource type to check. |
| `id` | The ID of the resource to check. |





**Returns:** `true` if the file contains a matching resource, `false` otherwise.



**Since:** BeOS R3

---

### `InitCheck()`

```cpp
status_t BResources::InitCheck()const
```

Gets the initialization status of the object. 


Unlike other Storage Kit classes a [BResources](classBResources.md) object is always properly initialized, unless it couldn't allocate memory for some important internal structures. Thus even after a call to [SetTo()](classBResources.md#a7c59913cefb4f22ac9ae6f2976b21d57) that reported an error, [InitCheck()](classBResources.md#aea04304030d7b1996a37a3a00c3aa977) is likely to return `B_OK`.



> [!NOTE]
> This method is not found in BeOS R5.



**Returns:** `B_OK` if the objects is properly initialized, `B_NO_MEMORY` otherwise.



**Since:** Haiku R1

---

### `LoadResource()`

```cpp
const void * BResources::LoadResource(type_code type, const char * name, size_t * _size)
```

Loads a resource identified by *type* and *name* into memory. 



> [!NOTE]
> Since a type and name pair may not identify a resource uniquely, this method always returns the first resource that matches the parameters, that is the one with the smallest index.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The type of the resource to be loaded. |
| `name` | The name of the resource to be loaded. |
| `_size` | A pointer to a variable into which the size of the resource shall be written. |





**Returns:** A pointer to the resource data if everything went fine, or `NULL` if the file does not have a resource that matches the parameters or an error occurred.



**Since:** BeOS R4

---

### `LoadResource()`

```cpp
const void * BResources::LoadResource(type_code type, int32 id, size_t * _size)
```

Loads a resource identified by *type* and *id* into memory. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The type of the resource to be loaded. |
| `id` | The ID of the resource to be loaded. |
| `_size` | A pointer to a variable into which the size of the resource shall be written. |





**Returns:** A pointer to the resource data if everything went fine, or `NULL` if the file does not have a resource that matches the parameters or an error occurred.



**Since:** BeOS R4

---

### `MergeFrom()`

```cpp
status_t BResources::MergeFrom(BFile * fromFile)
```

Adds the resources of *fromFile* to the internal file of the [BResources](classBResources.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `fromFile` | The file whose resources are to be be copied from. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_FILE | The resource map is empty??? |
| B_BAD_VALUE | *fromFile* was `NULL`. |
| B_FILE_ERROR | A file error occurred. |
| B_IO_ERROR | An error occurred while writing the resources. |





**Since:** BeOS R4

---

### `PreloadResourceType()`

```cpp
status_t BResources::PreloadResourceType(type_code type = 0)
```

Loads all resources of the specified *type* into memory. 


If *type* is 0, all resources are loaded. This might be useful for performance reasons.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The type of resources to be loaded. |





**Returns:** One of the following status codes or the negation of the number of errors that occurred.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_FILE | The resource map is empty??? |





**Since:** BeOS R4

---

### `ReadResource()`

```cpp
status_t BResources::ReadResource(type_code type, int32 id, void * data, off_t offset, size_t length)
```

Reads data from an existing resource. (deprecated, use [LoadResource()](classBResources.md#aa215bc39f8373df2aa9c12aaf55c760c) instead) 


If more data than existing are requested, this method does not fail. It will then read only the existing data. As a consequence an offset past the end of the resource will not cause the method to fail, but no data will be read at all.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The type of the resource to be read. |
| `id` | The ID of the resource to be read. |
| `data` | A pointer to a buffer into which the data shall be read |
| `offset` | The byte offset relative to the beginning of the resource from which the data shall be read. |
| `length` | The size of the data to be read. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *data* was `NULL` or *type* and *id* did not identify an existing resource. |
| B_ERROR | Error reading data. |
| B_NO_MEMORY | Not enough memory for this operation. |





**Since:** BeOS R3

---

### `RemoveResource()`

```cpp
status_t BResources::RemoveResource(const void * resource)
```

Removes a resource identified by *resource*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `resource` | The pointer to the resource data (formerly returned by [LoadResource()](classBResources.md#aa215bc39f8373df2aa9c12aaf55c760c)). |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *resource* was `NULL` or invalid (didn't point to any resource data of this file). |
| B_ERROR | An error occurred while removing the resource. |
| B_FILE_ERROR | A file error occurred. |
| B_NOT_ALLOWED | The file was opened read only. |





**Since:** BeOS R4

---

### `RemoveResource()`

```cpp
status_t BResources::RemoveResource(type_code type, int32 id)
```

Removes a resource identified by *type* and *id*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The type of the resource to remove. |
| `id` | The ID of the resource to remove. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | No such resource was found. |
| B_ERROR | An error occurred while removing the resource. |
| B_FILE_ERROR | A file error occurred. |
| B_NOT_ALLOWED | The file was opened read only. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BResources::SetTo(const BFile * file, bool clobber = false)
```

Initializes the [BResources](classBResources.md) object to represent the resources of the supplied file. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | The file to initialize the [BResources](classBResources.md) object from. |
| `clobber` | If `true`, the data of the file are erased. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *file* was `NULL` or uninitialized. |
| B_ERROR | Failed to initialize the object. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BResources::SetTo(const char * path, bool clobber = false)
```

Initialized the [BResources](classBResources.md) object to represent the resources of the file referred to by the supplied *path*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | A path referring to the file to create a BResource object from. |
| `clobber` | If `true`, the data of the file are erased. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *path* was `NULL`. |
| B_ENTRY_NOT_FOUND | The file referenced by *path* couldn't be found. |
| B_ERROR | Failed to initialize the object. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BResources::SetTo(const entry_ref * ref, bool clobber = false)
```

Initialized the [BResources](classBResources.md) object to represent the resources of the file referenced by the supplied *ref*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | An [entry_ref](structentry__ref.md) referring to the file to create a BResource object from. |
| `clobber` | If `true`, the data of the file are erased. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *ref* was `NULL`. |
| B_ENTRY_NOT_FOUND | The file referenced by *ref* couldn't be found. |
| B_ERROR | Failed to initialize the object. |





**Since:** Haiku R1

---

### `SetToImage()`

```cpp
status_t BResources::SetToImage(const void * codeOrDataPointer, bool clobber = false)
```

Initialized the [BResources](classBResources.md) object to represent the resources of the file from which the specified pointer has been loaded. 


The image belongs to the current team and is identified by a pointer into it's code (aka text) or data segment, i.e. any pointer to a function or a static (or global) variable will do.


If *clobber* is `true`, the file's resources are removed.


Parameters

| Parameter | Description |
| :--- | :--- |
| `codeOrDataPointer` | Pointer to the text or data segment of the image. |
| `clobber` | If `true`, the data of the file are erased. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *codeOrDataPointer* was `NULL`. |
| B_ENTRY_NOT_FOUND | The image or the file couldn't be found. |
| B_ERROR | Failed to initialize the object. |





**Since:** Haiku R1

---

### `SetToImage()`

```cpp
status_t BResources::SetToImage(image_id image, bool clobber = false)
```

Initialized the [BResources](classBResources.md) object to represent the resources of the file from which the specified *image* has been loaded. 


If *clobber* is `true`, the file's resources are removed.


Parameters

| Parameter | Description |
| :--- | :--- |
| `image` | ID of a loaded image. |
| `clobber` | If `true`, the data of the file are erased. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ENTRY_NOT_FOUND | The file referenced by *image* couldn't be found. |
| B_ERROR | Failed to initialize the object. |





**Since:** Haiku R1

---

### `Sync()`

```cpp
status_t BResources::Sync()
```

Writes all changes to the resources to the file. 


Since [AddResource()](classBResources.md#a4a470900257d43bc3c110c2b58e87bc4) and [RemoveResource()](classBResources.md#a2c4b0aa9e7e0cad840af9f47f7c452ae) may change the resources only in memory, this method can be used to make sure, that all changes are actually written to the file.


The [BResources](classBResources.md) object's destructor calls [Sync()](classBResources.md#a040b5cfd22da43472571bcf5c2f99fd4) before cleaning up.



> [!NOTE]
> When a resource is written to the file its data is converted to the endianness of the file. When reading a resource the data is converted to the endianness of the host. This of course only works for known types, i.e. those that swap_data() is able to understand.



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_FILE | The resource map is empty??? |
| B_FILE_ERROR | A file error occurred. |
| B_IO_ERROR | An error occurred while writing the resources. |
| B_NOT_ALLOWED | The file was opened read only. |





**Since:** BeOS R4

---

### `Unset()`

```cpp
void BResources::Unset()
```

Returns the [BResources](classBResources.md) object to an uninitialized state. 


If the object represented resources that had been modified, the data are written back to the file.



> [!NOTE]
> This method is not found in BeOS R5.



**Since:** Haiku R1

---

### `WriteResource()`

```cpp
status_t BResources::WriteResource(type_code type, int32 id, const void * data, off_t offset, size_t length)
```

Writes data into an existing resource. (deprecated, use [AddResource()](classBResources.md#a4a470900257d43bc3c110c2b58e87bc4) instead) 


If writing the data would exceed the bounds of the resource, it is enlarged respectively. If *offset* is past the end of the resource, padding with unspecified data is inserted.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The type of the resource to write data to. |
| `id` | The ID of the resource to write data to. |
| `data` | The data to be written. |
| `offset` | The byte offset relative to the beginning of the resource at which the data shall be written. |
| `length` | The size of the data to be written. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *data* was `NULL` or *type* and *id* did not identify an existing resource. |
| B_ERROR | Error writing data. |
| B_NO_MEMORY | Not enough memory for this operation. |





**Since:** BeOS R3

---

### `WriteTo()`

```cpp
status_t BResources::WriteTo(BFile * file)
```

Writes the resources to a new file. 


The resources formerly contained in the target file (if any) are erased. When the method returns, the [BResources](classBResources.md) object refers to the new file.



> [!WARNING]
> If the resources have been modified, but [Sync()](classBResources.md#a040b5cfd22da43472571bcf5c2f99fd4) has not been called, the old file remains unmodified.


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | The file that the resources shall be written to. |





**Returns:** `B_OK` if everything went fine or an error code otherwise.



**Since:** BeOS R4

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBResources.html).
