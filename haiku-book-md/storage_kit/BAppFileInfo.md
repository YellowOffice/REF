---
name: BAppFileInfo
type: class
kit: storage_kit
brief: "Provides access to the metadata associated with executables, libraries and add-ons"
source: haiku-book
---

# BAppFileInfo Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Provides access to the metadata associated with executables, libraries and add-ons. 


The [BAppFileInfo](classBAppFileInfo.md) class allows for information about an executable or add-on to be accessed or set. Information about an executable that can be accessed include the signature, catalog entry, supported MIME types, application flags, icon(s), and version info.


You should initialize the [BAppFileInfo](classBAppFileInfo.md) with a [BFile](classBFile.md) object that represents the executable or add-on that you want to access. If you only want to read metadata from the file you do not have to open it for reading. However, if you also want to write metadata then you should open the [BFile](classBFile.md) for writing.


To associate a [BFile](classBFile.md) with a [BAppFileInfo](classBAppFileInfo.md) object you can either pass the [BFile](classBFile.md) object into the constructor or you can use the empty constructor and then use the [SetTo()](classBAppFileInfo.md#a4bd4d27aa93d92cce91f2cb10e3852e9) method to set the [BFile](classBFile.md) to the [BAppFileInfo](classBAppFileInfo.md) object.


When accessing information from a BFileInfo object it will first look in the attributes of the [BFile](classBFile.md). If the information is not found then the BFileInfo object will next look at the resource of the [BFile](classBFile.md). You can tell the BFileInfo object to look only in the attributes or resources with the [SetInfoLocation()](classBAppFileInfo.md#a4e01cba2089d250f6d7e4c4d73d4495d) method.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BAppFileInfo](#a14518c82d65e51cf21fef2abe9e1e5f2) () — Creates an uninitialized BAppFileInfo object.
* [BAppFileInfo](#adfd620140120aad88d314001f7ea6a84) (BFile *file) — Creates an BAppFileInfo object and initializes it to the supplied file.
* `virtual` [~BAppFileInfo](#a831286d13b3c8290b7ccac8e56613c7c) () — Frees all resources associated with this object.
* `status_t` [SetTo](#a4bd4d27aa93d92cce91f2cb10e3852e9) (BFile *file) — Initializes the BAppFileInfo to the supplied file.
* `virtual status_t` [GetType](#aef1969cb93211a9edafb4b34219c0ec8) (char *type) const — Gets the MIME type of the associated file.
* `virtual status_t` [SetType](#a6fc65b958f2652f0a910ac2190252ff8) (const char *type) — Sets the MIME type of the associated file.
* `status_t` [GetSignature](#ae68c6df1b47ef4add615030c743afdb7) (char *signature) const — Gets the application signature of the associated file.
* `status_t` [SetSignature](#afca5bdac998eff41aa0135955950a747) (const char *signature) — Sets the application signature of the associated file.
* `status_t` [GetCatalogEntry](#ad914a37f1b242347c1d471ada964461d) (char *catalogEntry) const — Gets the catalog entry of the associated file used for localization.
* `status_t` [SetCatalogEntry](#aea19df97f084ffd5335ba740273c930c) (const char *catalogEntry) — Sets the catalog entry of the associated file used for localization.
* `status_t` [GetAppFlags](#aadbed49f3eaedbd25463128b079c33df) (uint32 *flags) const — Gets the application flags of the associated file.
* `status_t` [SetAppFlags](#ad2c49b8678e85372e9e1338eb5367976) (uint32 flags) — Sets the application flags of the associated file.
* `status_t` [RemoveAppFlags](#a54479f28ec210a8710e0b126c2e4bde5) () — Removes the application flags from the associated file.
* `status_t` [GetSupportedTypes](#a42552464f2758ed6b7d9a69c8e1d0a5a) (BMessage *types) const — Gets the MIME types supported by the application.
* `status_t` [SetSupportedTypes](#ab80c89a3832a379e02e88354ab58b902) (const BMessage *types, bool updateMimeDB, bool syncAll) — Sets the MIME types that are supported by the application and allows you to specify whether or not the supported types in the MIME DB shall be updated as well.
* `status_t` [SetSupportedTypes](#a74f609c8c49d842946b92c9bcba6eccb) (const BMessage *types, bool syncAll) — Sets the MIME types that are supported by the application and allows you to specify whether or not the no longer supported types shall be updated as well.
* `status_t` [SetSupportedTypes](#a973d1ea97db339dc65ee621c05ef39fe) (const BMessage *types) — Sets the MIME types supported by the application.
* `bool` [IsSupportedType](#a4b54d96d31373b701ab810d41085a356) (const char *type) const — Returns whether the application supports the supplied MIME type.
* `bool` [Supports](#a0429ee4e052178f3d78d9e3d25797d57) (BMimeType *type) const — Returns whether the application supports the supplied MIME type explicitly.
* `virtual status_t` [GetIcon](#a923c307844f5c97781adeb05df3fdf63) (BBitmap *icon, icon_size which) const — Gets the icon of the associated file and puts it into a pre-allocated BBitmap.
* `status_t` [SetIcon](#a103efc4ed5c28d31a1720e03627db7a8) (const BBitmap *icon, icon_size which, bool updateMimeDB) — Sets the icon of the associated file from a BBitmap.
* `virtual status_t` [SetIcon](#a08664bc229f29bb15648ff8d6fce4569) (const BBitmap *icon, icon_size which) — Sets the icon of the associated file from a BBitmap.
* `status_t` [GetIcon](#af68a89c04ed513c1408b4234ac4209fe) (uint8 **data, size_t *size) const — Gets the icon of the associated file and puts it into a buffer.
* `status_t` [SetIcon](#a2db8cf52b3a56077342135ff7b8fb947) (const uint8 *data, size_t size, bool updateMimeDB) — Sets the icon of the associated file from a buffer.
* `status_t` [SetIcon](#ade849cafa939e192ce3afa7e6b43b4d5) (const uint8 *data, size_t size) — Sets the icon of the associated file from a buffer.
* `status_t` [GetIconForType](#ac724955a16d777e199d8eb3732e54319) (const char *type, BBitmap *icon, icon_size which) const — Gets the icon the application provides for a given MIME type and puts it into a BBitmap.
* `status_t` [GetIconForType](#aef9303de1c959944f9d4a0162699499c) (const char *type, uint8 **data, size_t *size) const — Gets the icon the application provides for a given MIME type and puts it into a buffer.
* `status_t` [SetIconForType](#ad590932ba096ebc583f4b42eb51395cd) (const char *type, const BBitmap *icon, icon_size which, bool updateMimeDB) — Sets the icon the application provides for a given MIME type from a BBitmap.
* `status_t` [SetIconForType](#aafac860cede3142d214c0f095d8d4411) (const char *type, const BBitmap *icon, icon_size which) — Sets the icon the application provides for a given MIME type from a BBitmap.
* `status_t` [SetIconForType](#a8fad38770a480931855ce6c3e7fe22da) (const char *type, const uint8 *data, size_t size, bool updateMimeDB) — Sets the icon the application provides for a given MIME type from a buffer.
* `status_t` [SetIconForType](#a7b6f4737af83799ee6d9f623cfb98e9a) (const char *type, const uint8 *data, size_t size) — Sets the icon the application provides for a given MIME type from a buffer.
* `status_t` [GetVersionInfo](#a3cbced16e0fcc255cf3d526536dcc27b) (version_info *info, version_kind kind) const — Gets the version info of the associated file.
* `status_t` [SetVersionInfo](#a4178864a920b20753cd24469e5a27ddd) (const version_info *info, version_kind kind) — Sets the version info of the associated file.
* `void` [SetInfoLocation](#a4e01cba2089d250f6d7e4c4d73d4495d) (info_location location) — Specifies the location where the metadata shall be stored.
* `bool` [IsUsingAttributes](#af51c19a647c8d4955bc3a752cc3966e7) () const — Returns whether the object (also) stores the metadata in the attributes of the associated file.
* `bool` [IsUsingResources](#a25595984795ba90584d05e920f0ce399) () const — Returns whether the object (also) stores the metadata in the resources of the associated file.
* [BNodeInfo](#ad752fd7c10a42b1f11ae35d910aa645c) () — Creates an uninitialized BNodeInfo object.
* [BNodeInfo](#a98100e447a6fa36f7f77ee69acccd61e) (BNode *node) — Creates a BNodeInfo object and initializes it to the supplied node.
* `virtual` [~BNodeInfo](#a02c3e3aa4ffa005913a4ad32861d1f99) () — Frees the object and associated resources.
* `status_t` [SetTo](#ac565dcc8ed1e34571e35a51b4f09ea39) (BNode *node) — Initializes the BNodeInfo to the supplied node.
* `status_t` [InitCheck](#a362e684a08d62ec3aa95c75395f3698e) () const — Checks whether or not the object has been properly initialized.
* `status_t` [GetPreferredApp](#a7efa86ade48aec51d4a4b7ff4762c163) (char *signature, app_verb verb=B_OPEN) const — Gets the preferred application of the node.
* `status_t` [SetPreferredApp](#ae02314008ca406a34f3391ee2e2f2326) (const char *signature, app_verb verb=B_OPEN) — Sets the preferred application of the node. If signature is NULL, the BEOS:PREF_APP attribute is removed instead.
* `status_t` [GetAppHint](#a3ab221c59085959fa85387359a7afbee) (entry_ref *ref) const — Fills out ref with a pointer to a hint about the application that will open this node.
* `status_t` [SetAppHint](#af5efb90d7a21c84b73e80be96644a882) (const entry_ref *ref) — Sets the application that will open the file type of the node. If ref is NULL, the BEOS:PPATH attribute is removed instead.
* `status_t` [GetIcon](#a0d2207fd5cd79534cc2ae1a5c2a7b489) (uint8 **data, size_t *size, type_code *type) const — Gets the icon of the node.
* `status_t` [SetIcon](#a5b659144815814b289e4fbab020777d2) (const uint8 *data, size_t size) — Sets the node icon of the node. If data is NULL or size is 0, the BEOS:ICON attribute is removed instead.
* `status_t` [GetTrackerIcon](#a2259ab1207533b6deb8c06e39086b980) (BBitmap *icon, icon_size which=B_LARGE_ICON) const — Gets the icon displayed by Tracker for the icon.

### Additional Inherited Members

* `static status_t` [GetTrackerIcon](#a7f0bfd78768ed5ce96cba288487c781b) (const entry_ref *ref, BBitmap *icon, icon_size which=B_LARGE_ICON) — Gets the icon displayed by Tracker for the node referred to by ref.

## Detailed Member Documentation

### `BAppFileInfo()`

```cpp
BAppFileInfo::BAppFileInfo()
```

Creates an uninitialized [BAppFileInfo](classBAppFileInfo.md) object. 



**Since:** BeOS R3

---

### `BAppFileInfo()`

```cpp
BAppFileInfo::BAppFileInfo(BFile * file)
```

Creates an [BAppFileInfo](classBAppFileInfo.md) object and initializes it to the supplied file. 


The caller retains ownership of the supplied [BFile](classBFile.md) object. It must not be deleted during the life time of the [BAppFileInfo](classBAppFileInfo.md). It is not deleted when the [BAppFileInfo](classBAppFileInfo.md) is destroyed.


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | The [BFile](classBFile.md) object that the [BAppFileInfo](classBAppFileInfo.md) object shall be initialized to. |





**Since:** BeOS R3

---

### `~BAppFileInfo()`

```cpp
BAppFileInfo::~BAppFileInfo()
```

Frees all resources associated with this object. 


The supplied [BFile](classBFile.md) object is not deleted if one is specified.



**Since:** BeOS R3

---

### `GetAppFlags()`

```cpp
status_t BAppFileInfo::GetAppFlags(uint32 * flags)const
```

Gets the application *flags* of the associated file. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `flags` | A pointer to a pre-allocated `uint32` into which the application flags of the file are written. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | `NULL` *flags*. |
| B_BAD_TYPE | The attribute/resources the flags are stored in have the wrong type. |
| B_ENTRY_NOT_FOUND | No application flags are set on the file. |





**Since:** BeOS R3

---

### `GetCatalogEntry()`

```cpp
status_t BAppFileInfo::GetCatalogEntry(char * catalogEntry)const
```

Gets the catalog entry of the associated file used for localization. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `catalogEntry` | A pointer to a pre-allocated character buffer of size `B_MIME_TYPE_LENGTH` * 3 or larger into which the catalog entry of the file will be written. |





**Returns:** a status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | `NULL` *catalogEntry* or the entry stored in the attribute/resources is longer than `B_MIME_TYPE_LENGTH` * 3. |
| B_BAD_TYPE | The attribute/resources the entry is stored in have the wrong type. |
| B_ENTRY_NOT_FOUND | No catalog entry is set on the file. |





**Since:** Haiku R1

---

### `GetIcon()`

```cpp
status_t BAppFileInfo::GetIcon(BBitmap * icon, icon_size which)const
```

Gets the icon of the associated file and puts it into a pre-allocated [BBitmap](../interface_kit/classBBitmap.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `icon` | A pointer to a pre-allocated [BBitmap](../interface_kit/classBBitmap.md) of the correct dimension to store the requested icon (16x16 for the `B_MINI_ICON` and 32x32 for the `B_LARGE_ICON`). |
| `which` | Specifies the size of the icon to be retrieved: `B_MINI_ICON` for the mini and `B_LARGE_ICON` for the large icon. For HVIF icons this parameter has no effect. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | `NULL` *icon*, unsupported icon size *which* or bitmap dimensions (*icon*) and icon size (*which*) do not match. |





**Since:** BeOS R3


Reimplemented from [BNodeInfo](classBNodeInfo.md#a68b1e0645325e3ef8251cd505fe9c854).

---

### `GetIcon()`

```cpp
status_t BAppFileInfo::GetIcon(uint8 ** data, size_t * size)const
```

Gets the icon of the associated file and puts it into a buffer. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The pointer in which the flat icon data will be returned. |
| `size` | The pointer in which the size of the data found will be returned. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | `NULL` *data* or `NULL` size. |





**Since:** BeOS R3

---

### `GetIconForType()`

```cpp
status_t BAppFileInfo::GetIconForType(const char * type, BBitmap * icon, icon_size size)const
```

Gets the icon the application provides for a given MIME type and puts it into a [BBitmap](../interface_kit/classBBitmap.md). 



> [!NOTE]
> If *type* is `NULL`, the application's icon is retrieved.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The MIME type in question. May be `NULL`. |
| `icon` | A pointer to a pre-allocated [BBitmap](../interface_kit/classBBitmap.md) of the correct dimension to store the requested icon (16x16 for the mini and 32x32 for the large icon). |
| `size` | Specifies the size of the icon to be retrieved: `B_MINI_ICON` for the mini and `B_LARGE_ICON` for the large icon. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | `NULL` *icon*, unsupported icon size *which* or bitmap dimensions (*icon*) and icon size (*which*) do not match. |





**Since:** BeOS R3

---

### `GetIconForType()`

```cpp
status_t BAppFileInfo::GetIconForType(const char * type, uint8 ** data, size_t * size)const
```

Gets the icon the application provides for a given MIME type and puts it into a buffer. 



> [!NOTE]
> If *type* is set to `NULL` the the application's icon is retrieved.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The MIME type in question. May be `NULL`. |
| `data` | A pointer in which the icon data will be returned. When you are done with the data, you should use free() to deallocate it. |
| `size` | A pointer in which the size of the retrieved data is returned. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | `NULL` *data* and/or *size*. Or the supplied *type* is not a valid MIME type. |





**Since:** Haiku R1

---

### `GetSignature()`

```cpp
status_t BAppFileInfo::GetSignature(char * signature)const
```

Gets the application signature of the associated file. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | A pointer to a pre-allocated character buffer of size `B_MIME_TYPE_LENGTH` or larger into which the application signature of the file will be written. |





**Returns:** a status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | `NULL` *signature* or the signature stored in the attribute/resources is longer than `B_MIME_TYPE_LENGTH`. |
| B_BAD_TYPE | The attribute/resources the signature is stored in have the wrong type. |
| B_ENTRY_NOT_FOUND | No signature is set on the file. |





**Since:** BeOS R3

---

### `GetSupportedTypes()`

```cpp
status_t BAppFileInfo::GetSupportedTypes(BMessage * types)const
```

Gets the MIME types supported by the application. 


The supported MIME types are added to a field "types" of type `B_STRING_TYPE` in *types*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `types` | A pointer to a pre-allocated [BMessage](../application_kit/classBMessage.md) into which the MIME types supported by the application will be written. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | `NULL` *types*. |
| B_BAD_TYPE | The attribute/resources that the supported types are stored in have the wrong type. |
| B_ENTRY_NOT_FOUND | No supported types are set on the file. |





**Since:** BeOS R3

---

### `GetType()`

```cpp
status_t BAppFileInfo::GetType(char * type)const
```

Gets the MIME type of the associated file. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | A pointer to a pre-allocated character buffer of size `B_MIME_TYPE_LENGTH` or larger into which the MIME type of the file will be written. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | `NULL` *type* or the type string stored in the attribute/resources is longer than `B_MIME_TYPE_LENGTH`. |
| B_BAD_TYPE | The attribute/resources the type string is stored in has the wrong type. |
| B_ENTRY_NOT_FOUND | No type is set on the file. |





**Since:** BeOS R3


Reimplemented from [BNodeInfo](classBNodeInfo.md#a9bfd75065d98e817d078c968d02228e4).

---

### `GetVersionInfo()`

```cpp
status_t BAppFileInfo::GetVersionInfo(version_info * info, version_kind kind)const
```

Gets the version info of the associated file. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `info` | A pointer to a pre-allocated version_info structure into which the version info should be written. |
| `kind` | Specifies the kind of the version info to be retrieved: * `B_APP_VERSION_KIND` for the application's version info and  * `B_SYSTEM_VERSION_KIND` for the suite's info the application belongs to. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | `NULL` *info*. |





**Since:** BeOS R3

---

### `IsSupportedType()`

```cpp
bool BAppFileInfo::IsSupportedType(const char * type)const
```

Returns whether the application supports the supplied MIME type. 


If the application supports the wildcard type "application/octet-stream" then this method returns `true` for any MIME type.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The MIME type in question. |





**Returns:** `true` if *type* is a valid MIME type and it is supported by the application, `false` otherwise.



**Since:** BeOS R3

---

### `IsUsingAttributes()`

```cpp
bool BAppFileInfo::IsUsingAttributes()const
```

Returns whether the object (also) stores the metadata in the attributes of the associated file. 



**Returns:** `true` if the metadata are (also) stored in the file's attributes, `false` otherwise.



**Since:** BeOS R3

---

### `IsUsingResources()`

```cpp
bool BAppFileInfo::IsUsingResources()const
```

Returns whether the object (also) stores the metadata in the resources of the associated file. 



**Returns:** `true` if the metadata are (also) stored in the file's resources, `false` otherwise.



**Since:** BeOS R3

---

### `RemoveAppFlags()`

```cpp
status_t BAppFileInfo::RemoveAppFlags()
```

Removes the application flags from the associated file. 



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object was not properly initialized. |





**Since:** Haiku R1

---

### `SetAppFlags()`

```cpp
status_t BAppFileInfo::SetAppFlags(uint32 flags)
```

Sets the application *flags* of the associated file. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `flags` | The application *flags* to be assigned to the file. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object was not properly initialized. |





**Since:** BeOS R3

---

### `SetCatalogEntry()`

```cpp
status_t BAppFileInfo::SetCatalogEntry(const char * catalogEntry)
```

Sets the catalog entry of the associated file used for localization. 


If *catalogEntry* is `NULL` the file's catalog entry is unset.


Parameters

| Parameter | Description |
| :--- | :--- |
| `catalogEntry` | The catalog entry to be assigned to the file. Of the form "x-vnd.Haiku-app:context:name". Must not be longer than `B_MIME_TYPE_LENGTH` * 3 (including the terminating \0). The *catalogEntry* may be `NULL`. |





**Returns:** a status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | *catalogEntry* is longer than `B_MIME_TYPE_LENGTH` * 3. |





**Since:** Haiku R1

---

### `SetIcon()`

```cpp
status_t BAppFileInfo::SetIcon(const BBitmap * icon, icon_size which)
```

Sets the icon of the associated file from a [BBitmap](../interface_kit/classBBitmap.md). 


If *icon* is `NULL` then the icon of the file is unset.


Also sets the application's icon in the MIME DB, if the file has a valid application signature.


Parameters

| Parameter | Description |
| :--- | :--- |
| `icon` | A pointer to the [BBitmap](../interface_kit/classBBitmap.md) containing the icon to be set. May be `NULL` to specify no icon. |
| `which` | Specifies the size of the icon to be set: `B_MINI_ICON` for 16x16 mini icon and `B_LARGE_ICON` for the 32x32 large icon. For HVIF icons this parameter has no effect. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | Unknown icon size *which* or bitmap dimensions (*icon*) and icon size (*which*) do not match. |





**Since:** BeOS R3


Reimplemented from [BNodeInfo](classBNodeInfo.md#a8ddb7be63e9a48ff851d61ab13f0a997).

---

### `SetIcon()`

```cpp
status_t BAppFileInfo::SetIcon(const BBitmap * icon, icon_size which, bool updateMimeDB)
```

Sets the icon of the associated file from a [BBitmap](../interface_kit/classBBitmap.md). 


If *icon* is `NULL` then the icon of the file is unset.


Parameters

| Parameter | Description |
| :--- | :--- |
| `icon` | A pointer to the [BBitmap](../interface_kit/classBBitmap.md) containing the icon to be set. May be `NULL` to specify no icon. |
| `which` | Specifies the size of the icon to be set: `B_MINI_ICON` for 16x16 mini icon and `B_LARGE_ICON` for the 32x32 large icon. For HVIF icons this parameter has no effect. |
| `updateMimeDB` | `true` to also set the icon for the application in the MIME DB. `false` otherwise. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | Unknown icon size *which* or bitmap dimensions (*icon*) and icon size (*which*) do not match. |





**Since:** Haiku R1

---

### `SetIcon()`

```cpp
status_t BAppFileInfo::SetIcon(const uint8 * data, size_t size)
```

Sets the icon of the associated file from a buffer. 


If *data* is `NULL` then the icon of the file is unset.


Also sets the application's icon in the MIME DB, if the file has a valid application signature.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A pointer to the data buffer containing the vector icon to be set. May be `NULL`. |
| `size` | Specifies the size of buffer pointed to by *data*. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | `NULL` data. |





**Since:** Haiku R1

---

### `SetIcon()`

```cpp
status_t BAppFileInfo::SetIcon(const uint8 * data, size_t size, bool updateMimeDB)
```

Sets the icon of the associated file from a buffer. 


If *data* is `NULL` then the icon of the file is unset.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A pointer to the data buffer containing the vector icon to be set. May be `NULL`. |
| `size` | Specifies the size of buffer pointed to by *data*. |
| `updateMimeDB` | `true` to also set the icon for the application in the MIME DB. `false` otherwise. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | `NULL` data. |





**Since:** Haiku R1

---

### `SetIconForType()`

```cpp
status_t BAppFileInfo::SetIconForType(const char * type, const BBitmap * icon, icon_size which)
```

Sets the icon the application provides for a given MIME type from a [BBitmap](../interface_kit/classBBitmap.md). 



> [!NOTE]
> If *type* is `NULL` then the icon is set.


If the file has a signature, then the icon is also set on the MIME type. If the type for the signature has not been installed yet, it is installed before.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The MIME type in question. May be `NULL`. |
| `icon` | A pointer to the [BBitmap](../interface_kit/classBBitmap.md) containing the icon to be set. May be `NULL`. |
| `which` | Specifies the size of the icon to be set: `B_MINI_ICON` for the mini and `B_LARGE_ICON` for the large icon. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | Either the icon size *which* is unknown, the bitmap dimensions (*icon*) and icon size (*which*) do not match, or the provided *type* is not a valid MIME type. |





**Since:** BeOS R3

---

### `SetIconForType()`

```cpp
status_t BAppFileInfo::SetIconForType(const char * type, const BBitmap * icon, icon_size which, bool updateMimeDB)
```

Sets the icon the application provides for a given MIME type from a [BBitmap](../interface_kit/classBBitmap.md). 



> [!NOTE]
> If *type* is `NULL` then the icon is set.


If *updateMimeDB* is `true` and if the file has a signature, then the icon is also set on the MIME type. If the type for the signature has not been installed yet, it is installed before.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The MIME type in question. May be `NULL`. |
| `icon` | A pointer to the [BBitmap](../interface_kit/classBBitmap.md) containing the icon to be set. May be `NULL`. |
| `which` | Specifies the size of the icon to be set: `B_MINI_ICON` for the mini and `B_LARGE_ICON` for the large icon. |
| `updateMimeDB` | `true` to also set the icon for the type in the MIME DB. `false` otherwise. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | Either the icon size *which* is unknown, the bitmap dimensions (*icon*) and icon size (*which*) do not match, or the provided *type* is not a valid MIME type. |





**Since:** Haiku R1

---

### `SetIconForType()`

```cpp
status_t BAppFileInfo::SetIconForType(const char * type, const uint8 * data, size_t size)
```

Sets the icon the application provides for a given MIME type from a buffer. 



> [!NOTE]
> If *type* is `NULL` then the icon is set.


If the file has a signature, then the icon is also set on the MIME type. If the type for the signature has not been installed yet, it is installed before.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The MIME type in question. May be `NULL`. |
| `data` | A pointer to the data containing the icon to be set. May be `NULL`. |
| `size` | Specifies the size of buffer provided in *data*. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | The provided *type* is not a valid MIME type. |





**Since:** Haiku R1

---

### `SetIconForType()`

```cpp
status_t BAppFileInfo::SetIconForType(const char * type, const uint8 * data, size_t size, bool updateMimeDB)
```

Sets the icon the application provides for a given MIME type from a buffer. 



> [!NOTE]
> If *type* is `NULL` then the icon is set.


If *updateMimeDB* is `true` and if the file has a signature, then the icon is also set on the MIME type. If the type for the signature has not been installed yet, it is installed before.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The MIME type in question. May be `NULL`. |
| `data` | A pointer to the data containing the icon to be set. May be `NULL`. |
| `size` | Specifies the size of buffer provided in *data*. |
| `updateMimeDB` | `true` to also set the icon for the type in the MIME DB. `false` otherwise. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | The provided *type* is not a valid MIME type. |





**Since:** Haiku R1

---

### `SetInfoLocation()`

```cpp
void BAppFileInfo::SetInfoLocation(info_location location)
```

Specifies the location where the metadata shall be stored. 


The options for *location* are:


* `B_USE_ATTRIBUTES:` Store the data in the attributes.

* `B_USE_RESOURCES:` Store the data in the resources.

* `B_USE_BOTH_LOCATIONS:` Store the data in attributes and resources.



Parameters

| Parameter | Description |
| :--- | :--- |
| `location` | The location where the metadata shall be stored. |





**Since:** BeOS R3

---

### `SetSignature()`

```cpp
status_t BAppFileInfo::SetSignature(const char * signature)
```

Sets the application signature of the associated file. 


If *signature* is `NULL` the file's application signature is unset.


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | The application signature to be assigned to the file. Must not be longer than `B_MIME_TYPE_LENGTH` (including the terminating \0). The *signature* may be `NULL`. |





**Returns:** a status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | *signature* is longer than `B_MIME_TYPE_LENGTH`. |





**Since:** BeOS R3

---

### `SetSupportedTypes()`

```cpp
status_t BAppFileInfo::SetSupportedTypes(const BMessage * types)
```

Sets the MIME types supported by the application. 


This method is a short-hand for SetSupportedTypes(types, false). 


**See also:** SetSupportedType(const BMessage*, bool) for detailed information.


Parameters

| Parameter | Description |
| :--- | :--- |
| `types` | The supported types to be assigned to the file. May be `NULL`. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |





**Since:** BeOS R3

---

### `SetSupportedTypes()`

```cpp
status_t BAppFileInfo::SetSupportedTypes(const BMessage * types, bool syncAll)
```

Sets the MIME types that are supported by the application and allows you to specify whether or not the no longer supported types shall be updated as well. 


If *types* is `NULL` then the application's supported types are unset.


The supported MIME types must be stored in a field "types" of type `B_STRING_TYPE` in *types*.


The method informs the registrar about this news. For each supported type the result of [BMimeType::GetSupportingApps()](classBMimeType.md#a32e1d909b97c84d943ac50467e56fc3d) will afterwards include the signature of this application. That is, the application file needs to have a signature set.


*syncAll* specifies whether the no longer supported types shall be updated as well, i.e. whether or not this application shall be removed from the list of supporting applications.


Parameters

| Parameter | Description |
| :--- | :--- |
| `types` | The supported types to be assigned to the file. May be `NULL`. |
| `syncAll` | `true` to also synchronize the no-longer supported types, `false` otherwise. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |





**Since:** BeOS R3

---

### `SetSupportedTypes()`

```cpp
status_t BAppFileInfo::SetSupportedTypes(const BMessage * types, bool updateMimeDB, bool syncAll)
```

Sets the MIME types that are supported by the application and allows you to specify whether or not the supported types in the MIME DB shall be updated as well. 


If *types* is `NULL` then the application's supported types are unset.


The supported MIME types must be stored in a field "types" of type `B_STRING_TYPE` in *types*.


If *updateMimeDB* is `true`, the method will inform the registrar about this news. In this case for each supported type the result of [BMimeType::GetSupportingApps()](classBMimeType.md#a32e1d909b97c84d943ac50467e56fc3d) will afterward include the signature of this application. That is, the application file needs to have a signature set.


*syncAll* specifies whether the no longer supported types shall be updated as well, i.e. whether or not this application shall be removed from the list of supporting applications. Only relevant when *updateMimeDB* is `true`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `types` | The supported types to be assigned to the file. May be `NULL`. |
| `updateMimeDB` | `true` to update the supported types in the MIME DB, `false` otherwise. |
| `syncAll` | `true` to also synchronize the no-longer supported types, `false` otherwise. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BAppFileInfo::SetTo(BFile * file)
```

Initializes the [BAppFileInfo](classBAppFileInfo.md) to the supplied file. 


The caller retains ownership of the supplied [BFile](classBFile.md) object. It must not be deleted during the life time of the [BAppFileInfo](classBAppFileInfo.md). The [BFile](classBFile.md) object is not deleted when the [BAppFileInfo](classBAppFileInfo.md) is destroyed.


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | The [BFile](classBFile.md) object that the [BAppFileInfo](classBAppFileInfo.md) object shall be initialized to. |





**Returns:** an status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *file* or *file* is not properly initialized. |





**Since:** BeOS R3

---

### `SetType()`

```cpp
status_t BAppFileInfo::SetType(const char * type)
```

Sets the MIME type of the associated file. 


If *type* is `NULL` if the file's MIME type is unset.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The MIME type to be assigned to the file. It must not be longer than `B_MIME_TYPE_LENGTH` (including the terminating \0). The MIME type may be `NULL`. |





**Returns:** a status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |
| B_BAD_VALUE | *type* is longer than `B_MIME_TYPE_LENGTH`. |





**Since:** BeOS R3


Reimplemented from [BNodeInfo](classBNodeInfo.md#a27843b992dd5f5f9b5755073e7c6b310).

---

### `SetVersionInfo()`

```cpp
status_t BAppFileInfo::SetVersionInfo(const version_info * info, version_kind kind)
```

Sets the version info of the associated file. 



> [!NOTE]
> If *info* is set to `NULL` then the file's version info is unset.


Parameters

| Parameter | Description |
| :--- | :--- |
| `info` | The version info to be set. May be `NULL`. |
| `kind` | Specifies kind of version info to be set: * `B_APP_VERSION_KIND` for the application's version info and  * `B_SYSTEM_VERSION_KIND` for the suite's info the application belongs to. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object is not properly initialized. |





**Since:** BeOS R3

---

### `Supports()`

```cpp
bool BAppFileInfo::Supports(BMimeType * type)const
```

Returns whether the application supports the supplied MIME type explicitly. 


Unlike [IsSupportedType()](classBAppFileInfo.md#a4b54d96d31373b701ab810d41085a356), this method returns `true`, only if the type is explicitly supported, regardless of whether it supports "application/octet-stream".


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The MIME type in question. |





**Returns:** `true` if *type* is a valid MIME type and it is explicitly supported by the application, `false` otherwise.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBAppFileInfo.html).
