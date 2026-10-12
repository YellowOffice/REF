---
name: BPathFinder
type: class
kit: storage_kit
brief: "Helper class to retrieve paths in the file system layout"
source: haiku-book
---

# BPathFinder Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Helper class to retrieve paths in the file system layout. 


The [BPathFinder](classBPathFinder.md) provides two sets of methods for retrieving paths: [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) for getting a single path in an installation location specified via a constructor or a [SetTo()](classBPathFinder.md#a852db3b34c79cbe2e8d2bf2b9d651d53) invocation, and the static [FindPaths()](classBPathFinder.md#a7e0b20cb3f8378a2a7d3763821eb2558) for getting a list of paths for all installation locations.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BPathFinder](#a5bf296f6e46ac468209dac444f8f114b) (const BResolvableExpression &expression, const char *dependency=NULL) — Creates an object referring to an installation location based on the path of a package satisfying the given resolvable expression.
* [BPathFinder](#a93c4e093bbe3e99758a8222abf548a5c) (const char *path, const char *dependency=NULL) — Creates an object referring to an installation location based on a given path.
* [BPathFinder](#a24a6178102ad509becb312a467cebb89) (const entry_ref &ref, const char *dependency=NULL) — Creates an object referring to an installation location based on a given entry_ref.
* [BPathFinder](#a3c7a42103ed1d0a87c60d488ed3181d2) (const void *codePointer=NULL, const char *dependency=NULL) — Creates an object referring to an installation location based on a loaded image file.
* `status_t` [FindPath](#a6430c47700b38075404d427f48b37868) (const char *architecture, path_base_directory baseDirectory, const char *subPath, uint32 flags, BPath &_path) — Retrieves a path in the file system layout based.
* `status_t` [FindPath](#a769fed5369dfe5ca73cc14dc321afef1) (path_base_directory baseDirectory, BPath &_path) — Retrieves a path in the file system layout based.
* `status_t` [FindPath](#a9e0e6558f8070334dc56632bac6058ca) (path_base_directory baseDirectory, const char *subPath, BPath &_path) — Retrieves a path in the file system layout based.
* `status_t` [FindPath](#aae646784db3ec1c29844b6312d857250) (path_base_directory baseDirectory, const char *subPath, uint32 flags, BPath &_path) — Retrieves a path in the file system layout based.
* `status_t` [SetTo](#af6afaf9aae2355b57978e660338bd642) (const BResolvableExpression &expression, const char *dependency=NULL) — Reinitializes the object to refer to an installation location based on a given resolvable expression.
* `status_t` [SetTo](#a6a97b207ffcc8212c74f994fb6e16f66) (const char *path, const char *dependency=NULL) — Reinitializes the object to refer to an installation location based on a given path.
* `status_t` [SetTo](#afa658250375811e03bf8a53094bd9422) (const entry_ref &ref, const char *dependency=NULL) — Reinitializes the object to refer to an installation location based on a given entry_ref.
* `status_t` [SetTo](#a852db3b34c79cbe2e8d2bf2b9d651d53) (const void *codePointer=NULL, const char *dependency=NULL) — Reinitializes the object to refer to an installation location based on a loaded image file.

### Static Public Member Functions

* `static status_t` [FindPaths](#a7e0b20cb3f8378a2a7d3763821eb2558) (const char *architecture, path_base_directory baseDirectory, const char *subPath, uint32 flags, BStringList &_paths) — Retrieves a list of paths in the file system layout.
* `static status_t` [FindPaths](#ad34869d7e9b0a36a0a324fc5cced8ed0) (path_base_directory baseDirectory, BStringList &_paths) — Retrieves a list of paths in the file system layout.
* `static status_t` [FindPaths](#aa4aa3e6d65a193f92cd83f303d3f8ac7) (path_base_directory baseDirectory, const char *subPath, BStringList &_paths) — Retrieves a list of paths in the file system layout.
* `static status_t` [FindPaths](#afc36200c68bf618a0d6e6dad99c91e2e) (path_base_directory baseDirectory, const char *subPath, uint32 flags, BStringList &_paths) — Retrieves a list of paths in the file system layout.

## Detailed Member Documentation

### `BPathFinder()`

```cpp
BPathFinder::BPathFinder(const void * codePointer = NULL, const char * dependency = NULL)
```

Creates an object referring to an installation location based on a loaded image file. 


When initialized with this constructor a [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) method called afterward determines the path of the image (i.e. executable, library, or add-on) file associated with *codePointer*, a pointer to a location in the code or static data of an image loaded in the caller's team. Based on that path the path constant passed to [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) will be evaluated. In most cases that means first determining the path of the installation location from the path.


If *dependency* is specified, instead of determining the installation location path from the image path, the installation location path of the dependency *dependency* of the package containing the image file is used.


If the initialization fails, e.g. due to insufficient memory or invalid arguments, subsequent calls to [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) will return an error.


Parameters

| Parameter | Description |
| :--- | :--- |
| `codePointer` | A pointer to code or static data belonging to the image based on which [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) shall compute the path. The special value `B_APP_IMAGE_SYMBOL` (the default) can be used to refer to the program image, and `B_CURRENT_IMAGE_SYMBOL` for the caller's image. |
| `dependency` | The name of the package's "requires" entry to be used for resolving the installation location. Can be `NULL` (the default). |





**Since:** Haiku R1

---

### `BPathFinder()`

```cpp
BPathFinder::BPathFinder(const char * path, const char * dependency = NULL)
```

Creates an object referring to an installation location based on a given *path*. 


When initialized with this constructor a [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) method called afterward evaluates the path constant passed to it based on *path*. In most cases that means first determining the path of the installation location from the given *path*.


If *dependency* is specified, instead of determining the installation location path from the given path, the installation location path of the dependency *dependency* of the package containing the file referred to by *path* is used.


If the initialization fails, e.g. due to insufficient memory or invalid arguments, subsequent calls to [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) will return an error.


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | A path based on which [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) shall compute the path. |
| `dependency` | The name of the package's "requires" entry to be used for resolving the installation location. Can be `NULL`. |





**Since:** Haiku R1

---

### `BPathFinder()`

```cpp
BPathFinder::BPathFinder(const entry_ref & ref, const char * dependency = NULL)
```

Creates an object referring to an installation location based on a given [entry_ref](structentry__ref.md). 


The constructor converts the given [entry_ref](structentry__ref.md) *ref* to a path and then initializes the object like [BPathFinder::BPathFinder(const char*, const char*)](classBPathFinder.md#a93c4e093bbe3e99758a8222abf548a5c).


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | A reference to be resolved to a path based on which [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) shall compute the path. |
| `dependency` | The name of the package's "requires" entry to be used for resolving the installation location. Can be `NULL`. |





**See also:** [BPathFinder::BPathFinder(const char*, const char*)](classBPathFinder.md#a93c4e093bbe3e99758a8222abf548a5c)



**Since:** Haiku R1

---

### `BPathFinder()`

```cpp
BPathFinder::BPathFinder(const BResolvableExpression & expression, const char * dependency = NULL)
```

Creates an object referring to an installation location based on the path of a package satisfying the given resolvable expression. 


The constructor finds the latest package that satisfies the resolvable expression *expression* and then uses its path to initialize the object like [BPathFinder::BPathFinder(const char*, const char*)](classBPathFinder.md#a93c4e093bbe3e99758a8222abf548a5c).



> [!NOTE]
> When using this constructor linking against libpackage.so is required.


Parameters

| Parameter | Description |
| :--- | :--- |
| `expression` | A resolvable expression to be resolved to the path of the latest package satisfying it, based on which [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) shall compute the path. |
| `dependency` | The name of the package's "requires" entry to be used for resolving the installation location. Can be `NULL`. |





**See also:** [BPathFinder::BPathFinder(const char*, const char*)](classBPathFinder.md#a93c4e093bbe3e99758a8222abf548a5c)



**Since:** Haiku R1

---

### `FindPath()`

```cpp
status_t BPathFinder::FindPath(const char * architecture, path_base_directory baseDirectory, const char * subPath, uint32 flags, BPath & _path)
```

Retrieves a path in the file system layout based. 


Depending on how the object was initialized this method starts with a path (from an image file or as given) and based on it evaluates *baseDirectory*. In most cases that means first determining the path of the installation location from the path, then appending the relative path corresponding to the given *baseDirectory* constant, and finally appending *subPath*, if given.


If a dependency string was passed to the previous constructor or [SetTo()](classBPathFinder.md#a852db3b34c79cbe2e8d2bf2b9d651d53) method, instead of determining the installation location path from the initial path, the installation location path of the dependency of the package containing the file the initial path refers to is used.


If *baseDirectory* specifies a path that is architecture dependent, *architecture* is used for constructing the path. If *architecture* is `NULL`, the architecture associated with the initial path (as returned by [guess_architecture_for_path()](Architecture_8h.md#af6527c1353b821375656e9720d033a1e)) is used. Note that if an image was specified, this is the same as the caller's architecture (as returned by [get_architecture()](Architecture_8h.md#a9d717f29f2e0b8d913b8d5be020a8bb3)).


If `B_FIND_PATH_IMAGE_PATH` or `B_FIND_PATH_PACKAGE_PATH` are specified, *subPath* is ignored. In the former case, which is only valid, if an image was specified for initialization, *dependency* is ignored as well and the path of the image file is returned. In the latter case the path of the package containing the file the initial path refers to, respectively, if *dependency* was specified, that of the package *dependency* was resolved to is returned.


Parameters

| Parameter | Description |
| :--- | :--- |
| `architecture` | The name of the architecture to be used for resolving *architecture* dependent paths. Can be `NULL`, in which case the *architecture* associated with the initial path is used. |
| `baseDirectory` | Constant indicating which path to retrieve. |
| `subPath` | Relative subpath that shall be appended. Can be `NULL`. |
| `flags` | Bitwise OR of any of the following flags: * `B_FIND_PATH_CREATE_DIRECTORY:` If the resulting path doesn't exist, create it as a directory (including all missing ancestors).  * `B_FIND_PATH_CREATE_PARENT_DIRECTORY:` If the resulting path's parent doesn't exist, create the parent directory (including all missing ancestors).  * `B_FIND_PATH_EXISTING_ONLY:` If the resulting path doesn't exist, fail with `B_ENTRY_NOT_FOUND`. |
| `_path` | The variable to be set to the resulting path on success. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ENTRY_NOT_FOUND | A file system entry required for retrieving the path didn't exist, e.g. `B_FIND_PATH_PACKAGE_PATH` was specified and the image file didn't belong to a package, or `dependency` was specified, but wasn't a "requires" entry of the package, or `B_FIND_PATH_EXISTING_ONLY` was specified and the resulting path didn't exist. |





**Since:** Haiku R1

---

### `FindPath()`

```cpp
status_t BPathFinder::FindPath(path_base_directory baseDirectory, BPath & _path)
```

Retrieves a path in the file system layout based. 


Equivalent to a call to [BPathFinder::FindPath(const char*,
path_base_directory, const char*, uint32, BPath&)](classBPathFinder.md#a6430c47700b38075404d427f48b37868) with a `NULL` architecture, 0 flags, and `NULL` subpath.


Parameters

| Parameter | Description |
| :--- | :--- |
| `baseDirectory` | Constant indicating which path to retrieve. |
| `_path` | The variable to be set to the resulting path on success. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ENTRY_NOT_FOUND | A file system entry required for retrieving the path didn't exist, e.g. `B_FIND_PATH_PACKAGE_PATH` was specified and the image file didn't belong to a package, or `dependency` was specified, but wasn't a "requires" entry of the package. |





**Since:** Haiku R1

---

### `FindPath()`

```cpp
status_t BPathFinder::FindPath(path_base_directory baseDirectory, const char * subPath, BPath & _path)
```

Retrieves a path in the file system layout based. 


Equivalent to a call to [BPathFinder::FindPath(const char*,
path_base_directory, const char*, uint32, BPath&)](classBPathFinder.md#a6430c47700b38075404d427f48b37868) with a `NULL` architecture and 0 flags.


Parameters

| Parameter | Description |
| :--- | :--- |
| `baseDirectory` | Constant indicating which path to retrieve. |
| `subPath` | Relative subpath that shall be appended. Can be `NULL`. |
| `_path` | The variable to be set to the resulting path on success. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ENTRY_NOT_FOUND | A file system entry required for retrieving the path didn't exist, e.g. `B_FIND_PATH_PACKAGE_PATH` was specified and the image file didn't belong to a package, or `dependency` was specified, but wasn't a "requires" entry of the package. |

---

### `FindPath()`

```cpp
status_t BPathFinder::FindPath(path_base_directory baseDirectory, const char * subPath, uint32 flags, BPath & _path)
```

Retrieves a path in the file system layout based. 


Equivalent to a call to [BPathFinder::FindPath(const char*,
path_base_directory, const char*, uint32, BPath&)](classBPathFinder.md#a6430c47700b38075404d427f48b37868) with a `NULL` architecture.


Parameters

| Parameter | Description |
| :--- | :--- |
| `baseDirectory` | Constant indicating which path to retrieve. |
| `subPath` | Relative subpath that shall be appended. Can be `NULL`. |
| `flags` | Bitwise OR of any of the following flags: * `B_FIND_PATH_CREATE_DIRECTORY:` If the resulting path doesn't exist, create it as a directory (including all missing ancestors).  * `B_FIND_PATH_CREATE_PARENT_DIRECTORY:` If the resulting path's parent doesn't exist, create the parent directory (including all missing ancestors).  * `B_FIND_PATH_EXISTING_ONLY:` If the resulting path doesn't exist, fail with `B_ENTRY_NOT_FOUND`. |
| `_path` | The variable to be set to the resulting path on success. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ENTRY_NOT_FOUND | A file system entry required for retrieving the path didn't exist, e.g. `B_FIND_PATH_PACKAGE_PATH` was specified and the image file didn't belong to a package, or `dependency` was specified, but wasn't a "requires" entry of the package, or `B_FIND_PATH_EXISTING_ONLY` was specified and the resulting path didn't exist. |





**Since:** Haiku R1

---

### `FindPaths()`

```cpp
status_t BPathFinder::FindPaths(const char * architecture, path_base_directory baseDirectory, const char * subPath, uint32 flags, BStringList & _paths)
```

Retrieves a list of paths in the file system layout. 


For each installation location – in the order most specific to most generic, non-packaged before packaged – the function evaluates *baseDirectory* to a path and appends *subPath*, if given.


If *baseDirectory* specifies a path that is architecture dependent, *architecture* is used for constructing each path. If *architecture* is `NULL`, the caller's architecture (as returned by [get_architecture()](Architecture_8h.md#a9d717f29f2e0b8d913b8d5be020a8bb3)) is used.


`B_FIND_PATH_PACKAGE_PATH` and `B_FIND_PATH_IMAGE_PATH` are not valid arguments for this function.


Parameters

| Parameter | Description |
| :--- | :--- |
| `architecture` | The name of the architecture to be used for resolving *architecture* dependent paths. Can be `NULL`, in which case the caller's *architecture* is used. |
| `baseDirectory` | Constant indicating which paths to retrieve. |
| `subPath` | Relative subpath that shall be appended. Can be `NULL`. |
| `flags` | Bitwise OR of any of the following flags: * `B_FIND_PATH_CREATE_DIRECTORY:` If a resulting path doesn't exist, create it as a directory (including all missing ancestors).  * `B_FIND_PATH_CREATE_PARENT_DIRECTORY:` If a resulting path's parent doesn't exist, create the parent directory (including all missing ancestors).  * `B_FIND_PATH_EXISTING_ONLY:` If a resulting path doesn't exist, skip it. If none of the paths exist, fail with `B_ENTRY_NOT_FOUND`. |
| `_paths` | The [BStringList](../support_kit/classBStringList.md) variable where the retrieved paths shall be stored. The list is emptied before adding the paths. It is also emptied on error. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ENTRY_NOT_FOUND | A file system entry required for retrieving the paths didn't exist, e.g. `B_FIND_PATH_EXISTING_ONLY` was specified and none of the resulting paths existed. |





**Since:** Haiku R1

---

### `FindPaths()`

```cpp
status_t BPathFinder::FindPaths(path_base_directory baseDirectory, BStringList & _paths)
```

Retrieves a list of paths in the file system layout. 


Equivalent to a call to [BPathFinder::FindPaths(const char*,
path_base_directory, const char*, uint32, BStringList&)](classBPathFinder.md#a7e0b20cb3f8378a2a7d3763821eb2558) with a `NULL` architecture, 0 flags, and `NULL` subpath.


Parameters

| Parameter | Description |
| :--- | :--- |
| `baseDirectory` | Constant indicating which paths to retrieve. |
| `_paths` | The [BStringList](../support_kit/classBStringList.md) variable where the retrieved paths shall be stored. The list is emptied before adding the paths. It is also emptied on error. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ENTRY_NOT_FOUND | A file system entry required for retrieving the paths didn't exist, e.g. `B_FIND_PATH_EXISTING_ONLY` was specified and none of the resulting paths existed. |





**Since:** Haiku R1

---

### `FindPaths()`

```cpp
status_t BPathFinder::FindPaths(path_base_directory baseDirectory, const char * subPath, BStringList & _paths)
```

Retrieves a list of paths in the file system layout. 


Equivalent to a call to [BPathFinder::FindPaths(const char*,
path_base_directory, const char*, uint32, BStringList&)](classBPathFinder.md#a7e0b20cb3f8378a2a7d3763821eb2558) with a `NULL` architecture and 0 flags.


Parameters

| Parameter | Description |
| :--- | :--- |
| `baseDirectory` | Constant indicating which paths to retrieve. |
| `subPath` | Relative subpath that shall be appended. Can be `NULL`. |
| `_paths` | The [BStringList](../support_kit/classBStringList.md) variable where the retrieved paths shall be stored. The list is emptied before adding the paths. It is also emptied on error. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ENTRY_NOT_FOUND | A file system entry required for retrieving the paths didn't exist, e.g. `B_FIND_PATH_EXISTING_ONLY` was specified and none of the resulting paths existed. |





**Since:** Haiku R1

---

### `FindPaths()`

```cpp
status_t BPathFinder::FindPaths(path_base_directory baseDirectory, const char * subPath, uint32 flags, BStringList & _paths)
```

Retrieves a list of paths in the file system layout. 


Equivalent to a call to [BPathFinder::FindPaths(const char*,
path_base_directory, const char*, uint32, BStringList&)](classBPathFinder.md#a7e0b20cb3f8378a2a7d3763821eb2558) with a `NULL` architecture.


Parameters

| Parameter | Description |
| :--- | :--- |
| `baseDirectory` | Constant indicating which paths to retrieve. |
| `subPath` | Relative subpath that shall be appended. Can be `NULL`. |
| `flags` | Bitwise OR of any of the following flags: * `B_FIND_PATH_CREATE_DIRECTORY:` If a resulting path doesn't exist, create it as a directory (including all missing ancestors).  * `B_FIND_PATH_CREATE_PARENT_DIRECTORY:` If a resulting path's parent doesn't exist, create the parent directory (including all missing ancestors).  * `B_FIND_PATH_EXISTING_ONLY:` If a resulting path doesn't exist, skip it. If none of the paths exist, fail with `B_ENTRY_NOT_FOUND`. |
| `_paths` | The [BStringList](../support_kit/classBStringList.md) variable where the retrieved paths shall be stored. The list is emptied before adding the paths. It is also emptied on error. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ENTRY_NOT_FOUND | A file system entry required for retrieving the paths didn't exist, e.g. `B_FIND_PATH_EXISTING_ONLY` was specified and none of the resulting paths existed. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BPathFinder::SetTo(const BResolvableExpression & expression, const char * dependency = NULL)
```

Reinitializes the object to refer to an installation location based on a given resolvable expression. 


This method finds the latest package that satisfies the resolvable expression *expression* and then passes its path to [BPathFinder::SetTo(const char*, const char*)](classBPathFinder.md#a6a97b207ffcc8212c74f994fb6e16f66).



> [!NOTE]
> When using this method linking against libpackage.so is required.


Parameters

| Parameter | Description |
| :--- | :--- |
| `expression` | A resolvable expression to be resolved to the path of the latest package satisfying it, based on which [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) shall compute the path. |
| `dependency` | The name of the package's "requires" entry to be used for resolving the installation location. Can be `NULL`. |





**See also:** [status_t](SupportDefs_8h.md#ab6735558965995709a53691ae913c81b) [BPathFinder::SetTo(const char*, const char*)](classBPathFinder.md#a6a97b207ffcc8212c74f994fb6e16f66)



**Returns:** `B_OK` Everything if went fine or an error code otherwise.



**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BPathFinder::SetTo(const char * path, const char * dependency = NULL)
```

Reinitializes the object to refer to an installation location based on a given *path*. 


When reinitialized with this method a [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) method called afterward evaluates the path constant passed to it based on *path*. In most cases that means first determining the path of the installation location from the given *path*.


If *dependency* is specified, instead of determining the installation location path from the given path, the installation location path of the dependency *dependency* of the package containing the file referred to by *path* is used.


If the initialization fails, e.g. due to insufficient memory or invalid arguments, this method and subsequent calls to [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) will return an error.


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | A path based on which [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) shall compute the path. |
| `dependency` | The name of the package's "requires" entry to be used for resolving the installation location. Can be `NULL`. |





**Returns:** `B_OK` Everything if went fine or an error code otherwise.



**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BPathFinder::SetTo(const entry_ref & ref, const char * dependency = NULL)
```

Reinitializes the object to refer to an installation location based on a given [entry_ref](structentry__ref.md). 


This method converts the given [entry_ref](structentry__ref.md) *ref* to a path and then calls calls [BPathFinder::SetTo(const char*, const char*)](classBPathFinder.md#a6a97b207ffcc8212c74f994fb6e16f66).


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | A reference to be resolved to a path based on which [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) shall compute the path. |
| `dependency` | The name of the package's "requires" entry to be used for resolving the installation location. Can be `NULL`. |





**See also:** [status_t](SupportDefs_8h.md#ab6735558965995709a53691ae913c81b) [BPathFinder::SetTo(const char*, const char*)](classBPathFinder.md#a6a97b207ffcc8212c74f994fb6e16f66)



**Returns:** `B_OK` Everything if went fine or an error code otherwise.



**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BPathFinder::SetTo(const void * codePointer = NULL, const char * dependency = NULL)
```

Reinitializes the object to refer to an installation location based on a loaded image file. 


When reinitialized with this method a [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) method called afterward determines the path of the image (i.e. executable, library, or add-on) file associated with *codePointer*, a pointer to a location in the code or static data of an image loaded in the caller's team. Based on that path the path constant passed to [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) will be evaluated. In most cases that means first determining the path of the installation location from the path.


If *dependency* is specified, instead of determining the installation location path from the image path, the installation location path of the dependency *dependency* of the package containing the image file is used.


If the initialization fails, e.g. due to insufficient memory or invalid arguments, this method and subsequent calls to [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) will return an error.


Parameters

| Parameter | Description |
| :--- | :--- |
| `codePointer` | A pointer to code or static data belonging to the image based on which [FindPath()](classBPathFinder.md#a6430c47700b38075404d427f48b37868) shall compute the path. The special value `B_APP_IMAGE_SYMBOL` (the default) can be used to refer to the program image, and `B_CURRENT_IMAGE_SYMBOL` for the caller's image. |
| `dependency` | The name of the package's "requires" entry to be used for resolving the installation location. Can be `NULL` (the default). |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPathFinder.html).
