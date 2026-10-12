---
name: BPath
type: class
kit: storage_kit
brief: "A class representing a file system path"
source: haiku-book
---

# BPath Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A class representing a file system path. 



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BPath](#afd5d004c1cb0622546a18f316a68c807) () — Creates an uninitialized BPath object.
* [BPath](#a5ecced69773ff2c9941a4f015f627f9d) (const BDirectory *dir, const char *leaf=NULL, bool normalize=false) — Creates a BPath object and initializes it to the specified directory and filename combination.
* [BPath](#a053ee656e6da94e7226bbf7e343db5bb) (const BEntry *entry) — Creates a BPath object and initializes it to the filesystem entry specified by the passed in BEntry object.
* [BPath](#a4e6b40dd0cee0996a63ba9b88b3d0b00) (const BPath &path) — Creates a copy of the given BPath object.
* [BPath](#a7d44e82248c6540b020fc2433533e572) (const char *dir, const char *leaf=NULL, bool normalize=false) — Creates a BPath object and initializes it to the specified path or path and filename combination.
* [BPath](#a1d37b9b75d5b7ff24ad40266b7b9dd9f) (const entry_ref *ref) — Creates a BPath object and initializes it to the filesystem entry specified by the passed in entry_ref struct.
* `virtual` [~BPath](#a0ec9767088fad845ed3c71014bd4d789) () — Destroys the BPath object and frees any associated resources.
* `status_t` [InitCheck](#a16c60cbaab02bb25cf8f690ebad2c48b) () const — Checks whether or not the object was properly initialized.
* `status_t` [SetTo](#a88b5935bf1bd2fe2c64c41baaaf6a6d7) (const entry_ref *ref) — Reinitializes the object to the filesystem entry specified by the passed in entry_ref struct.
* `status_t` [SetTo](#a17c725dfdc0f250b4ad95b567b6c1d2a) (const BEntry *entry) — Reinitializes the object to the specified filesystem entry.
* `status_t` [SetTo](#a206afd69b062fc5c52be5459d386f9ae) (const char *path, const char *leaf=NULL, bool normalize=false) — Reinitializes the object to the passed in path or path and leaf combination.
* `status_t` [SetTo](#ac03159e0d8b645a24b5bb08bb46bd11b) (const BDirectory *dir, const char *leaf=NULL, bool normalize=false) — Reinitializes the object to the passed in dir and relative path combination.
* `void` [Unset](#ac9f197dd6bfe7f02c35beb9810ca15a8) () — Returns the object to an uninitialized state.
* `status_t` [Append](#abe6828b73e063e9c9ee8f25082a3e670) (const char *path, bool normalize=false) — Appends the passed in relative path to the end of the current path.
* `const char *` [Path](#aa8aba68bed27b256de14222fe6df227b) () const — Gets the entire path of the object.
* `const char *` [Leaf](#aadae8a538bb405ea3850e32fb33b05f9) () const — Gets the leaf portion of the path.
* `status_t` [GetParent](#a096cdfcd70db54b3c30fe76743ac4f1b) (BPath *path) const — Initializes path with the parent directory of the BPath object.
* `bool` [IsAbsolute](#a456d6f1419fe00f376d1434d55d2432d) () const — Gets whether or not the path is absolute or relative.
* `bool` [operator==](#a3df539180ce332bebd6aa5b657b76254) (const BPath &item) const — Performs a simple (string-wise) comparison of paths for equality.
* `bool` [operator==](#ac50f789504a61cb9f90be71120d66508) (const char *path) const — Performs a simple (string-wise) comparison of paths for equality.
* `bool` [operator!=](#a76995b964f1751539c60703eedfa3a85) (const BPath &item) const — Performs a simple (string-wise) comparison of paths for inequality.
* `bool` [operator!=](#a02ac6810e4881f905703ce030af683fd) (const char *path) const — Performs a simple (string-wise) comparison of paths for inequality.
* `BPath &` [operator=](#a528ea14902d638e6a434f70177880a78) (const BPath &item) — Initializes the object as a copy of item.
* `BPath &` [operator=](#aed09ac7562d7a7f67c25f3ef1a8a562f) (const char *path) — Initializes the object with the passed in path.
* `virtual bool` [IsFixedSize](#ac43f61c0280de191eef4adcf6a642437) () const — Implements BFlattenable::IsFixedSize(). Always returns false.
* `virtual type_code` [TypeCode](#a05dc54fed4718135a3f55f476816f1cb) () const — Implements BFlattenable::TypeCode(). Always returns B_REF_TYPE.
* `virtual ssize_t` [FlattenedSize](#a5c77e3e9fb829249e9d1b6366f6d5520) () const — Implements BFlattenable::FlattenedSize(). Gets the size of the flattened entry_ref struct that represents the path in bytes.
* `virtual status_t` [Flatten](#a2866faf2cacac53e9d583f9a3dbd903c) (void *buffer, ssize_t size) const — Implements BFlattenable::Flatten(). Converts the path of the object to an entry_ref and writes it into buffer.
* `virtual bool` [AllowsTypeCode](#aef48a6f6cf10836b412df6b6e060c4c2) (type_code code) const — Implements BFlattenable::AllowsTypeCode(). Checks if type code is equal to B_REF_TYPE.
* `virtual status_t` [Unflatten](#a437333127ec6d2e1037e72dd822afeca) (type_code code, const void *buffer, ssize_t size) — Implements BFlattenable::Unflatten(). Initializes the object with the flattened entry_ref data from the passed in buffer.
* `virtual` [~BFlattenable](#a884e130a5d27acc15b1e4e4c505157ff) () — Destructor. Does nothing.
* `virtual bool` [AllowsTypeCode](#a30165696bba76fed10e37508cc4f6925) (type_code code) const — Get whether or not the supplied type_code is supported.
* `virtual status_t` [Flatten](#ab934b64a8b218a4f9078ded191be6fbb) (void *buffer, ssize_t size) const =0 — Pure virtual that should flatten the object into the supplied buffer.
* `virtual ssize_t` [FlattenedSize](#a9b5885d4454326ca448438960ecff466) () const =0 — Pure virtual that should return the size of the flattened object in bytes.
* `virtual bool` [IsFixedSize](#ac019f502749a0cc78082f5ec7c8f5b56) () const =0 — Pure virtual that should return whether or not flattened objects of this type always have a fixed size.
* `virtual type_code` [TypeCode](#a819507fa1b0906f14299db15f6e990d1) () const =0 — Pure virtual that returns the type_code this class flattens to.
* `virtual status_t` [Unflatten](#a41e7168574912690be159991d2b07a97) (type_code code, const void *buffer, ssize_t size)=0 — Pure virtual that should unflatten the buffer and put the contents into the current object.

## Detailed Member Documentation

### `BPath()`

```cpp
BPath::BPath()
```

Creates an uninitialized [BPath](classBPath.md) object. 



**See also:** [SetTo()](classBPath.md#a88b5935bf1bd2fe2c64c41baaaf6a6d7)

---

### `BPath()`

```cpp
BPath::BPath(const BPath & path)
```

Creates a copy of the given [BPath](classBPath.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | the object to be copied. |





**Since:** BeOS R3

---

### `BPath()`

```cpp
BPath::BPath(const entry_ref * ref)
```

Creates a [BPath](classBPath.md) object and initializes it to the filesystem entry specified by the passed in [entry_ref](structentry__ref.md) struct. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | the [entry_ref](structentry__ref.md) to initialize from. |





**Since:** BeOS R5

---

### `BPath()`

```cpp
BPath::BPath(const BEntry * entry)
```

Creates a [BPath](classBPath.md) object and initializes it to the filesystem entry specified by the passed in [BEntry](classBEntry.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | the [BEntry](classBEntry.md) object to initialize from. |





**Since:** BeOS R4

---

### `BPath()`

```cpp
BPath::BPath(const char * dir, const char * leaf = NULL, bool normalize = false)
```

Creates a [BPath](classBPath.md) object and initializes it to the specified path or path and filename combination. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The base component of the pathname. May be absolute or relative. If relative, it is based off the current working directory. |
| `leaf` | The (optional) leaf component of the pathname. Must be relative. The value of *leaf* is concatenated to the end of *dir* (a "/" will be added as a separator, if necessary). |
| `normalize` | boolean flag used to force normalization; normalization may sometimes occur even if `false`. The following items require normalization: * Relative pathnames (after concatenation; e.g. "boot/ltj")  * The presence of "." or ".." ("/boot/ltj/../ltj/./gwar")  * Redundant slashes ("/boot//ltj")  * A trailing slash ("/boot/ltj/") |





**Since:** BeOS R3

---

### `BPath()`

```cpp
BPath::BPath(const BDirectory * dir, const char * leaf = NULL, bool normalize = false)
```

Creates a [BPath](classBPath.md) object and initializes it to the specified directory and filename combination. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The directory that provides the base component of the pathname. |
| `leaf` | The (optional) leaf component of the pathname. Must be relative. The value of *leaf* is concatenated to the end of *dir* (a "/" will be added as a separator, if necessary). |
| `normalize` | boolean flag used to force normalization; normalization may sometimes occur even if `false`. The following items require normalization: * Relative pathnames (after concatenation; e.g. "boot/ltj")  * The presence of "." or ".." ("/boot/ltj/../ltj/./gwar")  * Redundant slashes ("/boot//ltj")  * A trailing slash ("/boot/ltj/") |





**Since:** BeOS R3

---

### `~BPath()`

```cpp
BPath::~BPath()
```

Destroys the [BPath](classBPath.md) object and frees any associated resources. 



**Since:** BeOS R3

---

### `AllowsTypeCode()`

```cpp
bool BPath::AllowsTypeCode(type_code code)const
```

Implements [BFlattenable::AllowsTypeCode()](../support_kit/classBFlattenable.md#a30165696bba76fed10e37508cc4f6925). Checks if type code is equal to `B_REF_TYPE`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `code` | The type code to test. |





**Returns:** `true` if code is `B_REF_TYPE`, `false` otherwise.



**Since:** BeOS R3


Reimplemented from [BFlattenable](../support_kit/classBFlattenable.md#a30165696bba76fed10e37508cc4f6925).

---

### `Append()`

```cpp
status_t BPath::Append(const char * path, bool normalize = false)
```

Appends the passed in relative path to the end of the current path. 


This method fails if the path is absolute or the [BPath](classBPath.md) object is uninitialized.


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | Relative pathname to append to current path (may be `NULL`). |
| `normalize` | Boolean flag used to force normalization; normalization may sometimes occur even if `false`. The following items require normalization: * Relative pathnames (after concatenation; e.g. "boot/ltj")  * The presence of "." or ".." ("/boot/ltj/../ltj/./gwar")  * Redundant slashes ("/boot//ltj")  * A trailing slash ("/boot/ltj/") |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Initialization was successful. |
| B_BAD_VALUE | *ref* was `NULL`. |
| B_NAME_TOO_LONG | The pathname was longer than `B_PATH_NAME_LENGTH`. |





**Since:** BeOS R3

---

### `Flatten()`

```cpp
status_t BPath::Flatten(void * buffer, ssize_t size)const
```

Implements [BFlattenable::Flatten()](../support_kit/classBFlattenable.md#ab934b64a8b218a4f9078ded191be6fbb). Converts the path of the object to an [entry_ref](structentry__ref.md) and writes it into *buffer*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | The buffer that the data is to be stored in. |
| `size` | Size of *buffer*. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *buffer* was `NULL` or of insufficient size. |





**Since:** BeOS R3


Implements [BFlattenable](../support_kit/classBFlattenable.md#ab934b64a8b218a4f9078ded191be6fbb).

---

### `FlattenedSize()`

```cpp
ssize_t BPath::FlattenedSize()const
```

Implements [BFlattenable::FlattenedSize()](../support_kit/classBFlattenable.md#a9b5885d4454326ca448438960ecff466). Gets the size of the flattened [entry_ref](structentry__ref.md) struct that represents the path in bytes. 



**Returns:** The size of the flattened [entry_ref](structentry__ref.md) struct that represents the path in bytes.



**Since:** BeOS R3


Implements [BFlattenable](../support_kit/classBFlattenable.md#a9b5885d4454326ca448438960ecff466).

---

### `GetParent()`

```cpp
status_t BPath::GetParent(BPath * path)const
```

Initializes *path* with the parent directory of the [BPath](classBPath.md) object. 


No normalization is performed on the path.


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The [BPath](classBPath.md) object to be initialized to the parent directory. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *path* was `NULL`. |
| B_ENTRY_NOT_FOUND | The [BPath](classBPath.md) object represents the root path and thus has no parent. |

---

### `InitCheck()`

```cpp
status_t BPath::InitCheck()const
```

Checks whether or not the object was properly initialized. 



**Returns:** `B_OK`, if the [BPath](classBPath.md) object was properly initialized, an error code otherwise.



**Since:** BeOS R3

---

### `IsAbsolute()`

```cpp
bool BPath::IsAbsolute()const
```

Gets whether or not the path is absolute or relative. 



> [!WARNING]
> This method returns `false` if the object is initialized.



**Returns:** `true` if the path is absolute, `false` if relative or if the object is uninitialized.

---

### `IsFixedSize()`

```cpp
bool BPath::IsFixedSize()const
```

Implements [BFlattenable::IsFixedSize()](../support_kit/classBFlattenable.md#ac019f502749a0cc78082f5ec7c8f5b56). Always returns `false`. 



**Returns:** `false`



**Since:** BeOS R3


Implements [BFlattenable](../support_kit/classBFlattenable.md#ac019f502749a0cc78082f5ec7c8f5b56).

---

### `Leaf()`

```cpp
const char * BPath::Leaf()const
```

Gets the leaf portion of the path. 


The leaf portion of the path is defined to be the string after the last `'/'`. For the root path (`"/"`) it is an empty string (`""`).



**Returns:** The leaf portion of the path or `NULL` if it is not properly initialized.



**Since:** BeOS R3

---

### `operator!=()`

```cpp
bool BPath::operator!=(const BPath & item)const
```

Performs a simple (string-wise) comparison of paths for inequality. 



> [!WARNING]
> No normalization takes place, two uninitialized [BPath](classBPath.md) objects are considered equal.


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | the [BPath](classBPath.md) object to compare. |





**Returns:** `true`, if the path names are **not** equal, `false` otherwise.



**Since:** BeOS R3

---

### `operator!=()`

```cpp
bool BPath::operator!=(const char * path)const
```

Performs a simple (string-wise) comparison of paths for inequality. 



> [!WARNING]
> No normalization takes place.


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The path to compare. |





**Returns:** `true`, if the path names are **not** equal, `false` otherwise.



**Since:** BeOS R3

---

### `operator=()`

```cpp
BPath & BPath::operator=(const BPath & item)
```

Initializes the object as a copy of *item*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The [BPath](classBPath.md) object to copy |





**Returns:** A pointer to the newly initialized [BPath](classBPath.md) object.



**Since:** BeOS R3

---

### `operator=()`

```cpp
BPath & BPath::operator=(const char * path)
```

Initializes the object with the passed in *path*. 


Has the same effect as 


```cpp
SetTo(path)
```

Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | the path to be assign to this object. |





**Returns:** A pointer to the newly initialized [BPath](classBPath.md) object.



**Since:** BeOS R3

---

### `operator==()`

```cpp
bool BPath::operator==(const BPath & item)const
```

Performs a simple (string-wise) comparison of paths for equality. 



> [!WARNING]
> No normalization takes place, two uninitialized [BPath](classBPath.md) objects are considered equal.


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | the [BPath](classBPath.md) object to compare. |





**Returns:** `true`, if the paths are equal, `false` otherwise.



**Since:** BeOS R3

---

### `operator==()`

```cpp
bool BPath::operator==(const char * path)const
```

Performs a simple (string-wise) comparison of paths for equality. 



> [!WARNING]
> No normalization takes place.


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The path to compare. |





**Returns:** `true`, if the path names are equal, `false` otherwise.



**Since:** BeOS R3

---

### `Path()`

```cpp
const char * BPath::Path()const
```

Gets the entire path of the object. 



**Returns:** The path name of the object, or `NULL` if it is not properly initialized.



**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BPath::SetTo(const BDirectory * dir, const char * path = NULL, bool normalize = false)
```

Reinitializes the object to the passed in *dir* and relative *path* combination. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The directory that provides the base component of the pathname. |
| `path` | the relative *path* name (may be `NULL`). |
| `normalize` | boolean flag used to force normalization; normalization may sometimes occur even if `false`. The following items require normalization: * Relative pathnames (after concatenation; e.g. "boot/ltj")  * The presence of "." or ".." ("/boot/ltj/../ltj/./gwar")  * Redundant slashes ("/boot//ltj")  * A trailing slash ("/boot/ltj/") |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Initialization was successful. |
| B_BAD_VALUE | *ref* was `NULL`. |
| B_NAME_TOO_LONG | The pathname was longer than `B_PATH_NAME_LENGTH`. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BPath::SetTo(const BEntry * entry)
```

Reinitializes the object to the specified filesystem entry. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | The [BEntry](classBEntry.md) to reinitialize the entry from. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Initialization was successful. |
| B_BAD_VALUE | *ref* was `NULL`. |
| B_NAME_TOO_LONG | The pathname was longer than `B_PATH_NAME_LENGTH`. |





**Since:** BeOS R4

---

### `SetTo()`

```cpp
status_t BPath::SetTo(const char * path, const char * leaf = NULL, bool normalize = false)
```

Reinitializes the object to the passed in *path* or *path* and *leaf* combination. 


RemarksThe following pseudocode is safe: 
```cpp
path.SetTo(path.Path(), "new leaf")
```


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The *path* name to use. |
| `leaf` | The *leaf* name to use (may be `NULL`). |
| `normalize` | Boolean flag used to force normalization; normalization may sometimes occur even if `false`. The following items require normalization: * Relative pathnames (after concatenation; e.g. "boot/ltj")  * The presence of "." or ".." ("/boot/ltj/../ltj/./gwar")  * Redundant slashes ("/boot//ltj")  * A trailing slash ("/boot/ltj/") |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Initialization was successful. |
| B_BAD_VALUE | *ref* was `NULL`. |
| B_NAME_TOO_LONG | The pathname was longer than `B_PATH_NAME_LENGTH`. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BPath::SetTo(const entry_ref * ref)
```

Reinitializes the object to the filesystem entry specified by the passed in [entry_ref](structentry__ref.md) struct. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The [entry_ref](structentry__ref.md) to reinitialize the entry from. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Initialization was successful. |
| B_BAD_VALUE | *ref* was `NULL`. |
| B_NAME_TOO_LONG | The pathname was longer than `B_PATH_NAME_LENGTH`. |





**Since:** BeOS R5

---

### `TypeCode()`

```cpp
type_code BPath::TypeCode()const
```

Implements [BFlattenable::TypeCode()](../support_kit/classBFlattenable.md#a819507fa1b0906f14299db15f6e990d1). Always returns `B_REF_TYPE`. 



**Returns:** `B_REF_TYPE`



**Since:** BeOS R3


Implements [BFlattenable](../support_kit/classBFlattenable.md#a819507fa1b0906f14299db15f6e990d1).

---

### `Unflatten()`

```cpp
status_t BPath::Unflatten(type_code code, const void * buffer, ssize_t size)
```

Implements [BFlattenable::Unflatten()](../support_kit/classBFlattenable.md#a41e7168574912690be159991d2b07a97). Initializes the object with the flattened [entry_ref](structentry__ref.md) data from the passed in buffer. 


The type code must be set to `B_REF_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `code` | The type code of the flattened data, must be `B_REF_TYPE`. |
| `buffer` | A pointer to a buffer containing the flattened data. |
| `size` | The size of *buffer* in bytes. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *buffer* was `NULL` or didn't contain an [entry_ref](structentry__ref.md). |





**Since:** BeOS R3


Implements [BFlattenable](../support_kit/classBFlattenable.md#a41e7168574912690be159991d2b07a97).

---

### `Unset()`

```cpp
void BPath::Unset()
```

Returns the object to an uninitialized state. 


Frees any resources it allocated and marks the object as uninitialized.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPath.html).
