---
name: BNodeInfo
type: class
kit: storage_kit
brief: "Provides access to file type meta data on a node"
source: haiku-book
---

# BNodeInfo Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Provides access to file type meta data on a node. 


[BNodeInfo](classBNodeInfo.md) provides a nice wrapper to all sorts of useful meta data such as the MIME-type, the file's icon and the application that will open the file.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BNodeInfo](#ad752fd7c10a42b1f11ae35d910aa645c) () — Creates an uninitialized BNodeInfo object.
* [BNodeInfo](#a98100e447a6fa36f7f77ee69acccd61e) (BNode *node) — Creates a BNodeInfo object and initializes it to the supplied node.
* `virtual` [~BNodeInfo](#a02c3e3aa4ffa005913a4ad32861d1f99) () — Frees the object and associated resources.
* `status_t` [SetTo](#ac565dcc8ed1e34571e35a51b4f09ea39) (BNode *node) — Initializes the BNodeInfo to the supplied node.
* `status_t` [InitCheck](#a362e684a08d62ec3aa95c75395f3698e) () const — Checks whether or not the object has been properly initialized.
* `virtual status_t` [GetType](#a9bfd75065d98e817d078c968d02228e4) (char *type) const — Writes the MIME-type of the node into type.
* `virtual status_t` [SetType](#a27843b992dd5f5f9b5755073e7c6b310) (const char *type) — Sets the MIME-type of the node. If type is NULL the BEOS:TYPE attribute is removed instead.
* `status_t` [GetPreferredApp](#a7efa86ade48aec51d4a4b7ff4762c163) (char *signature, app_verb verb=B_OPEN) const — Gets the preferred application of the node.
* `status_t` [SetPreferredApp](#ae02314008ca406a34f3391ee2e2f2326) (const char *signature, app_verb verb=B_OPEN) — Sets the preferred application of the node. If signature is NULL, the BEOS:PREF_APP attribute is removed instead.
* `status_t` [GetAppHint](#a3ab221c59085959fa85387359a7afbee) (entry_ref *ref) const — Fills out ref with a pointer to a hint about the application that will open this node.
* `status_t` [SetAppHint](#af5efb90d7a21c84b73e80be96644a882) (const entry_ref *ref) — Sets the application that will open the file type of the node. If ref is NULL, the BEOS:PPATH attribute is removed instead.

### Icon

* `virtual status_t` [GetIcon](#a68b1e0645325e3ef8251cd505fe9c854) (BBitmap *icon, icon_size which=B_LARGE_ICON) const — Gets the icon of the node.
* `virtual status_t` [SetIcon](#a8ddb7be63e9a48ff851d61ab13f0a997) (const BBitmap *icon, icon_size which=B_LARGE_ICON) — Sets the icon of the node. If icon is NULL, the attribute is removed instead.
* `status_t` [GetIcon](#a0d2207fd5cd79534cc2ae1a5c2a7b489) (uint8 **data, size_t *size, type_code *type) const — Gets the icon of the node.
* `status_t` [SetIcon](#a5b659144815814b289e4fbab020777d2) (const uint8 *data, size_t size) — Sets the node icon of the node. If data is NULL or size is 0, the BEOS:ICON attribute is removed instead.
* `status_t` [GetTrackerIcon](#a2259ab1207533b6deb8c06e39086b980) (BBitmap *icon, icon_size which=B_LARGE_ICON) const — Gets the icon displayed by Tracker for the icon.
* `static status_t` [GetTrackerIcon](#a7f0bfd78768ed5ce96cba288487c781b) (const entry_ref *ref, BBitmap *icon, icon_size which=B_LARGE_ICON) — Gets the icon displayed by Tracker for the node referred to by ref.

## Detailed Member Documentation

### `BNodeInfo()`

```cpp
BNodeInfo::BNodeInfo()
```

Creates an uninitialized [BNodeInfo](classBNodeInfo.md) object. 


After created a [BNodeInfo](classBNodeInfo.md) with this, you should call [SetTo()](classBNodeInfo.md#ac565dcc8ed1e34571e35a51b4f09ea39).



**See also:** [SetTo(BNode* node)](classBNodeInfo.md#ac565dcc8ed1e34571e35a51b4f09ea39)



**Since:** BeOS R3

---

### `BNodeInfo()`

```cpp
BNodeInfo::BNodeInfo(BNode * node)
```

Creates a [BNodeInfo](classBNodeInfo.md) object and initializes it to the supplied *node*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `node` | The *node* to initialize to and gather information. |





**Since:** BeOS R3

---

### `~BNodeInfo()`

```cpp
BNodeInfo::~BNodeInfo()
```

Frees the object and associated resources. 


The internal [BNode](classBNode.md) object is not deleted.



**Since:** BeOS R3

---

### `GetAppHint()`

```cpp
status_t BNodeInfo::GetAppHint(entry_ref * ref)const
```

Fills out *ref* with a pointer to a hint about the application that will open this node. 


The path contained in the `BEOS:PPATH` attribute of the node is converted into an [entry_ref](structentry__ref.md) and returned. *ref* should be pre-allocated before being passed into this method.


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | A pointer to a pre-allocated [entry_ref](structentry__ref.md) into which the app hint is written. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_DATA | Attribute size greater than `B_PATH_NAME_LENGTH`. |
| B_BAD_TYPE | The stored type string attribute has the wrong type. |
| B_BAD_VALUE | The *ref* object passed in was `NULL`. |
| B_ERROR | Unable to read `BEOS:PPATH` attribute. |
| B_NO_INIT | The object was not properly initialized. |

---

### `GetIcon()`

```cpp
status_t BNodeInfo::GetIcon(BBitmap * icon, icon_size which = B_LARGE_ICON)const
```

Gets the icon of the node. 


The icon stored in the `BEOS:L:STD_ICON` attribute (large) or `BEOS:M:STD_ICON` attribute (mini) is retrieved.


Parameters

| Parameter | Description |
| :--- | :--- |
| `icon` | A pointer to a pre-allocated [BBitmap](../interface_kit/classBBitmap.md) object of the correct dimension to store the requested icon: 16x16 for the mini or 32x32 for the large icon. |
| `which` | The size of the icon to be retrieved: `B_MINI_ICON` for a 16x16 icon and `B_LARGE_ICON` for a 32x32 icon. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object was not properly initialized. |
| B_BAD_VALUE | `NULL` *icon*, unsupported icon size *k* or bitmap dimensions (*icon*) and icon size (*k*) do not match. |





**Since:** BeOS R3


Reimplemented in [BAppFileInfo](classBAppFileInfo.md#a923c307844f5c97781adeb05df3fdf63).

---

### `GetIcon()`

```cpp
status_t BNodeInfo::GetIcon(uint8 ** data, size_t * size, type_code * type)const
```

Gets the icon of the node. 


The icon stored in the `BEOS:ICON` attribute of the node is retrieved. The caller is responsible to `delete[]` the data if the icon was retrieved.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A pointer in which a pointer to the icon data will be filled in. |
| `size` | A pointer in which the size of the found icon data will be filled in. |
| `type` | A pointer in which the type of the found icon data will be filled in. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object was not properly initialized. |
| B_BAD_VALUE | `NULL` *data*, `NULL` *size* or `NULL` *type*. |
| B_NO_MEMORY | No memory to allocate the *data* buffer. |





**Since:** Haiku R1

---

### `GetPreferredApp()`

```cpp
status_t BNodeInfo::GetPreferredApp(char * signature, app_verb verb = B_OPEN)const
```

Gets the preferred application of the node. 


Writes the contents of the `BEOS:PREF_APP` attribute into the *signature* buffer. The preferred application can be identified by its signature. *signature* should be at least `B_MIME_TYPE_LENGTH` or longer and pre-allocated before it is passed into this method.


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | A pointer to a pre-allocated character buffer of size `B_MIME_TYPE_LENGTH` or larger into which the MIME-type of the preferred application is written. |
| `verb` | The type of access the preferred application is requested. Currently `B_OPEN` is the only meaningful option. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object was not properly initialized. |
| B_BAD_VALUE | `NULL` *signature* or bad app_verb. |

---

### `GetTrackerIcon()`

```cpp
status_t BNodeInfo::GetTrackerIcon(BBitmap * icon, icon_size which = B_LARGE_ICON)const
```

Gets the icon displayed by Tracker for the icon. 


This method tries really hard to find an icon for the node:


* If the node has no type this method returns the icon for `B_FILE_MIME_TYPE` if it's a regular file or `B_DIRECTORY_MIME_TYPE` if it's a directory, even if the node has its own icon!

* Next it will ask [GetIcon()](classBNodeInfo.md#a68b1e0645325e3ef8251cd505fe9c854) for an icon.

* If this fails it will get the preferred application and ask the MIME database if the application has an icon for the file type of the node.

* Next it will ask the MIME database whether there is an icon for the file type of the node.

* Then it will ask the MIME database for the preferred application for the file type of the node and whether this application has a special icon for the type.

* Finally it will return a generic icon for whatever type of file type (file/dir/etc.) the node is from the MIME database.



The first action that provides an icon is used. In the case that none of them yield an icon this method fails, this is very unlikely though.


RemarksYou can set *which* to get a scaled icon instead of using a predefined icon_size constant, pass in an integer casted to icon_size. For example to get a 64x64 icon pass in: 
```cpp
(icon_size)64
```


Parameters

| Parameter | Description |
| :--- | :--- |
| `icon` | A pointer to a pre-allocated [BBitmap](../interface_kit/classBBitmap.md) of the correct dimension to store the requested icon (16x16 for the mini and 32x32 for the large icon). |
| `which` | The size of the icon to be retrieved: `B_MINI_ICON` for a 16x16 icon or `B_LARGE_ICON` for a 32x32 icon. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object was not properly initialized. |
| B_BAD_VALUE | `NULL` *icon*, unsupported icon size *which* or bitmap dimensions (*icon*) and icon size (*which*) do not match. |





**Since:** BeOS R3

---

### `GetTrackerIcon()`

```cpp
status_t BNodeInfo::GetTrackerIcon(const entry_ref * ref, BBitmap * icon, icon_size which = B_LARGE_ICON)
```

Gets the icon displayed by Tracker for the node referred to by *ref*. 


This methods works similarly to the non-static version but *ref* identifies the node. *icon* must be pre-allocated to the size requested using *which* before being passed to this method.


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | An [entry_ref](structentry__ref.md) referring to the node for which the icon is retrieved. |
| `icon` | A pointer to a pre-allocated [BBitmap](../interface_kit/classBBitmap.md) object of the correct dimension to store the requested icon (16x16 for the mini and 32x32 for the large icon). |
| `which` | The size of the icon to be retrieved: `B_MINI_ICON` for a 16x16 icon or `B_LARGE_ICON` for a 32x32 icon. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | `NULL` ref or *icon*, unsupported icon size *which* or bitmap dimensions (*icon*) and icon size (*which*) do not match. |





**Since:** BeOS R3

---

### `GetType()`

```cpp
status_t BNodeInfo::GetType(char * type)const
```

Writes the MIME-type of the node into *type*. 


The source of the type information is the `BEOS:TYPE` attribute of the node. The *type* buffer should be pre-allocated before it is passed into [GetType()](classBNodeInfo.md#a9bfd75065d98e817d078c968d02228e4), it should be at least `B_MIME_TYPE_LENGTH` in length.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | A pointer to a pre-allocated char buffer of at least `B_MIME_TYPE_LENGTH` length into which the MIME-type of the node is written. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | `NULL` *type* or the type string stored in the attribute is longer than `B_MIME_TYPE_LENGTH`. |
| B_BAD_TYPE | The stored type string attribute has the wrong type. |
| B_ENTRY_NOT_FOUND | No type is set on the node. |





**Since:** BeOS R3


Reimplemented in [BAppFileInfo](classBAppFileInfo.md#aef1969cb93211a9edafb4b34219c0ec8).

---

### `InitCheck()`

```cpp
status_t BNodeInfo::InitCheck()const
```

Checks whether or not the object has been properly initialized. 



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object was properly initialized. |
| B_BAD_VALUE | The object was **not** properly initialized. |





**Since:** BeOS R3

---

### `SetAppHint()`

```cpp
status_t BNodeInfo::SetAppHint(const entry_ref * ref)
```

Sets the application that will open the file type of the node. If *ref* is `NULL`, the `BEOS:PPATH` attribute is removed instead. 


*ref* is converted into a path and stored in the `BEOS:PPATH` attribute of the node. If *ref* is NULL `BEOS:PPATH` is removed instead.


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | A pointer to an [entry_ref](structentry__ref.md) referring to the application. May be `NULL`. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | The *ref* object passed in was `NULL`. |
| B_ENTRY_NOT_FOUND | `BEOS:PPATH` attribute not found. |
| B_ERROR | Unable to write `BEOS:PPATH` attribute. |
| B_NO_INIT | The object was not properly initialized. |

---

### `SetIcon()`

```cpp
status_t BNodeInfo::SetIcon(const BBitmap * icon, icon_size which = B_LARGE_ICON)
```

Sets the icon of the node. If *icon* is `NULL`, the attribute is removed instead. 


The icon is stored in the `BEOS:L:STD_ICON` attribute (large) or `BEOS:M:STD_ICON` attribute (mini). If *icon* is `NULL` the respective attribute is removed instead.


Parameters

| Parameter | Description |
| :--- | :--- |
| `icon` | A pointer to a [BBitmap](../interface_kit/classBBitmap.md) object containing the icon to be set. May be `NULL`. |
| `which` | The size of the icon to be set: `B_MINI_ICON` for the mini or `B_LARGE_ICON` for the large icon. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | Unknown icon size *k* or bitmap dimensions (*icon*) and icon size (*k*) do not match. |





**Since:** BeOS R3


Reimplemented in [BAppFileInfo](classBAppFileInfo.md#a08664bc229f29bb15648ff8d6fce4569).

---

### `SetIcon()`

```cpp
status_t BNodeInfo::SetIcon(const uint8 * data, size_t size)
```

Sets the node icon of the node. If *data* is `NULL` or *size* is 0, the `BEOS:ICON` attribute is removed instead. 


The icon is stored in the `BEOS:ICON` attribute of the node.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A pointer to valid icon data. May be `NULL`. |
| `size` | The size of the provided data buffer. May be 0. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object was not properly initialized. |





**Since:** Haiku R1

---

### `SetPreferredApp()`

```cpp
status_t BNodeInfo::SetPreferredApp(const char * signature, app_verb verb = B_OPEN)
```

Sets the preferred application of the node. If *signature* is `NULL`, the `BEOS:PREF_APP` attribute is removed instead. 


The supplied string is written into the `BEOS:PREF_APP` attribute of the node. If *signature* is `NULL`, the respective attribute is removed instead. *signature* must not be longer than `B_MIME_TYPE_LENGTH` (including the terminating `NUL`).


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | The signature of the preferred application to be set. May be `NULL`. |
| `verb` | The type of access set to the preferred application. Currently only `B_OPEN` is meaningful. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | `NULL` *signature*, *signature* is longer than `B_MIME_TYPE_LENGTH` or bad app_verb. |

---

### `SetTo()`

```cpp
status_t BNodeInfo::SetTo(BNode * node)
```

Initializes the [BNodeInfo](classBNodeInfo.md) to the supplied *node*. 


The [BNodeInfo](classBNodeInfo.md) object does not copy the supplied *node* object, it uses it directly instead. You must not delete the supply *node* while the [BNodeInfo](classBNodeInfo.md) object exists. The [BNodeInfo](classBNodeInfo.md) does not take over ownership of the *node* and it doesn't delete it on destruction either.


Parameters

| Parameter | Description |
| :--- | :--- |
| `node` | The *node* to gather information on. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | The node was not properly initialized. |





**Since:** BeOS R3

---

### `SetType()`

```cpp
status_t BNodeInfo::SetType(const char * type)
```

Sets the MIME-type of the node. If *type* is `NULL` the `BEOS:TYPE` attribute is removed instead. 


The *type* string is written into the `BEOS:TYPE` attribute of the node. If *type* is `NULL`, the `BEOS:TYPE` attribute is removed instead. The *type* parameter may not by longer than `B_MIME_TYPE_LENGTH` in length including the terminating \0 character.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The MIME-type to be assigned to the *node*. Must not be longer than `B_MIME_TYPE_LENGTH` (including the terminating `NUL`). May be `NULL` to remove the attribute. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object was not properly initialized. |
| B_BAD_VALUE | *type* is longer than `B_MIME_TYPE_LENGTH`. |





**Since:** BeOS R3


Reimplemented in [BAppFileInfo](classBAppFileInfo.md#a6fc65b958f2652f0a910ac2190252ff8).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBNodeInfo.html).
