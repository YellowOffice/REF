---
name: BTranslatorRoster
type: class
kit: translation_kit
brief: "Class that serves as an interface between applications and translators"
source: haiku-book
---

# BTranslatorRoster Class
**Kit/Group:** [Translation Kit](../translation_kit/group__translation.md) | [Translation Kit library (libtranslation.so)](group__libtranslation.md)

## Description

Class that serves as an interface between applications and translators. 


[BTranslatorRoster](classBTranslatorRoster.md) gives applications access to the translation kit. Applications can request translations and [BTranslatorRoster](classBTranslatorRoster.md) will automatically search for a matching translator and have it perfrom the translation.



> [!WARNING]
> [BTranslatorRoster](classBTranslatorRoster.md) does not perform chaining of any sort. Only translations that can be made by invoking a single translator are supported.



> [!NOTE]
> BTranslationUtils provides some helper methods that perform the interaction with [BTranslatorRoster](classBTranslatorRoster.md) for you.


BTranslationRoster acts as a container. While in most cases the default roster is used, it is possible to create a roster that interacts with a custom set of translators.

## Member List

### Public Member Functions

* `status_t` [AddTranslators](#ab0123b5bdbf2edd8e451383dc17f68c4) (const char *loadPath=NULL) — Adds translators from a directory to the roster.
* `status_t` [AddTranslator](#a3a594e4e4c9cb34a959e70b5760816e4) (BTranslator *translator) — Adds a single BTranslator to the roster.
* `virtual status_t` [Identify](#abc19c6daf3381256da9f11140c030401) (BPositionIO *source, BMessage *ioExtension, translator_info *_info, uint32 hintType=0, const char *hintMIME=NULL, uint32 wantType=0) — Determines the best translator in the roster to perform a certain conversion.
* `virtual status_t` [Translate](#afdbf0925f7f4425d39893f2f8ff6338a) (BPositionIO *source, const translator_info *info, BMessage *ioExtension, BPositionIO *destination, uint32 wantOutType, uint32 hintType=0, const char *hintMIME=NULL) — Finds and invokes the best translator for a conversion.
* `virtual status_t` [Translate](#ad93df9a0a73f5bfb2b50d0144586f39e) (translator_id translatorID, BPositionIO *source, BMessage *ioExtension, BPositionIO *destination, uint32 wantOutType) — Uses a specified translator from the roster to perform a conversion.
* `virtual status_t` [GetTranslators](#a57a59b5623c1909aaaa34ae02428ad2f) (BPositionIO *source, BMessage *ioExtension, translator_info **_info, int32 *_numInfo, uint32 hintType=0, const char *hintMIME=NULL, uint32 wantType=0) — Collects information about all translators that are able to perform a certain conversion in an array.
* `virtual status_t` [GetAllTranslators](#a4243683e52936ddf802c47d79a081436) (translator_id **_list, int32 *_count) — Collects the IDs of all translators in the roster in an array.
* `virtual status_t` [GetTranslatorInfo](#a2e38aed81b23a399fe2c83cf5a017ba6) (translator_id translatorID, const char **_name, const char **_info, int32 *_version) — Looks up general information of the translator with a given ID.
* `virtual status_t` [GetInputFormats](#a46b37086a22347d8e9b8a01413bd8f0c) (translator_id translatorID, const translation_format **_formats, int32 *_numFormats) — Looks up the input formats of the translator with a given ID.
* `virtual status_t` [GetOutputFormats](#a039dbcf8967418f988f370459cb82d0a) (translator_id translatorID, const translation_format **_formats, int32 *_numFormats) — Looks up the output formats of the translator with a given ID.
* `virtual status_t` [MakeConfigurationView](#a8c0ac933442510d1e1dcadea850580db) (translator_id translatorID, BMessage *ioExtension, BView **_view, BRect *_extent) — Creates the configuration view of a specified translator from the roster.
* `virtual status_t` [GetConfigurationMessage](#a545782121c88e69708c5679706c7166f) (translator_id translatorID, BMessage *ioExtension) — Populates a BMessage with the settings of the specified translator.
* `status_t` [GetRefFor](#abdb8e6c9742b1764fa4529791c74b1ff) (translator_id translatorID, entry_ref *ref) — Returns the entry_ref of the specified translator.
* `bool` [IsTranslator](#a6524c2e8e3d5eb693bdac714f3301174) (entry_ref *ref) — Determines whether the specified add-on contains at least one translator.
* `status_t` [StartWatching](#ad389aed357b37c8bf7c6b6a6828355f8) (BMessenger target) — Register a messenger to be notified when the roster changes.
* `status_t` [StopWatching](#a56dffa645a8cd40ff084441d71e129aa) (BMessenger target) — Unregister a messenger from the notification list.
* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).

### Constructors and Destructor

* [BTranslatorRoster](#af83b21d0ef78199fee09dd6036e8a59a) () — Constructs an empty BTranslatorRoster.
* [BTranslatorRoster](#af89f82b5a2d066a05474a45d17fd5340) (BMessage *model) — Constructs a BTranslatorRoster and fills it.
* `virtual` [~BTranslatorRoster](#a29f95c13d3bc13aaea57f17766a0d91d) () — Deletes this BTranslatorRoster.
* `static BTranslatorRoster *` [Default](#a60e78b682be3b46d4dd283f9f4ae09b6) () — Gets the default BTranslatorRoster.

### Archiving

* `virtual status_t` [Archive](#a3da914e839d12c865bfc1f7a89d902e9) (BMessage *into, bool deep=true) const — Archive this BTranslatorRoster into a BMessage.
* `static BArchivable *` [Instantiate](#a9b9638d2fa6763193e62495b098f0b54) (BMessage *from) — Creates a new BTranslatorRoster from a message.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BTranslatorRoster()`

```cpp
BTranslatorRoster::BTranslatorRoster()
```

Constructs an empty [BTranslatorRoster](classBTranslatorRoster.md). 



> [!WARNING]
> Only call the contructor if you want to use a custom collection of translators. Use [Default()](classBTranslatorRoster.md#a60e78b682be3b46d4dd283f9f4ae09b6) if you don't.

---

### `BTranslatorRoster()`

```cpp
BTranslatorRoster::BTranslatorRoster(BMessage * model)
```

Constructs a [BTranslatorRoster](classBTranslatorRoster.md) and fills it. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `model` | A message that contains information about a [BTranslatorRoster](classBTranslatorRoster.md). |




After initialization, *model* is searched for strings with the name `"be:translator_path"`. The translators that are located at each path are added to the roster. If multiple paths point to translators with the same name, the translator at the path with the lowest index within the message will be kept.



> [!WARNING]
> Use [Instantiate()](classBTranslatorRoster.md#a9b9638d2fa6763193e62495b098f0b54) instead of this constructor if *model* was created using [Archive()](classBTranslatorRoster.md#a3da914e839d12c865bfc1f7a89d902e9).

---

### `~BTranslatorRoster()`

```cpp
BTranslatorRoster::~BTranslatorRoster()
```

Deletes this [BTranslatorRoster](classBTranslatorRoster.md). 


If the [BTranslatorRoster](classBTranslatorRoster.md) that is deleted is the default roster, a new default roster will be created when [BTranslatorRoster::Default()](classBTranslatorRoster.md#a60e78b682be3b46d4dd283f9f4ae09b6) is called for the next time.


Release() is called on all translators in the roster.

---

### `AddTranslator()`

```cpp
status_t BTranslatorRoster::AddTranslator(BTranslator * translator)
```

Adds a single [BTranslator](classBTranslator.md) to the roster. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `translator` | The translator that should be added. |




Remarks[AddTranslator()](classBTranslatorRoster.md#a3a594e4e4c9cb34a959e70b5760816e4) calls Acquire() on the translator, so it is safe to release it if you had acquired it before.
Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The translator was successfully added to the roster. |
| B_NO_MEMORY | There was no memory to enlarge the roster. |
| B_BAD_VALUE | *translator* was `NULL`. |

---

### `AddTranslators()`

```cpp
status_t BTranslatorRoster::AddTranslators(const char * loadPath = NULL)
```

Adds translators from a directory to the roster. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `loadPath` | A colon-separated list of directories to search for translators in. |




The following method is used to determine which translators to add:


If *loadPath* is not `NULL`, the roster will be populated with all translators that are present in the directores denoted by *loadPath*. The paths are separated by a colon (`:`). If multiple paths contain a translator with the same name, the translator that is located in the path that appears earliest in *loadPath* will be kept.


If *loadPath* is `NULL` and the environment variable `TRANSLATORS` is set, it will be populated with all translators that are present in the directories denoted by `TRANSLATORS`. The paths are separated by a colon (`:`). If multiple paths contain a translator with the same name, the translator that is located in the path that appears earliest in `TRANSLATORS` will be kept.


If *loadPath* is `NULL` and `TRANSLATORS` is unset, the user non-packaged add-ons directory, the user add-ons directory, the system non-packaged add-ons directory and the system add-ons directory will be used. If those directories do not contain a subdirectory `Translators`, it will be created. The subdirectories are then added in the above order. If multiple directories contain a translator with the same name, the translator that is located in the path that appears earliest in the above list will be kept.



**Returns:** `B_OK` if everything went well, an error code specific to the operation that failed otherwise.

---

### `Archive()`

```cpp
status_t BTranslatorRoster::Archive(BMessage * into, bool deep = true)const
```

Archive this [BTranslatorRoster](classBTranslatorRoster.md) into a [BMessage](../application_kit/classBMessage.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `into` | Where the [BTranslatorRoster](classBTranslatorRoster.md) will be stored. |
| `deep` | Unused. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation was successful. |
| B_BAD_VALUE | *into* was NULL. |
| B_ERROR | The operation failed. |




Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44).

---

### `Default()`

```cpp
static BTranslatorRoster * BTranslatorRoster::Default()
```

Gets the default [BTranslatorRoster](classBTranslatorRoster.md). 


At any point, there is only one default roster. It is created when this method is called for the first time (possibly after being deleted) and is populated according to the following rules:


If the environment variable `TRANSLATORS` is set, the default roster will be populated with all translators that are present in the directories denoted by `TRANSLATORS`. The paths are separated by a colon (`:`). If multiple paths contain a translator with the same name, the translator that is located in the path that appears earliest in `TRANSLATORS` will be kept.


If `TRANSLATORS` is not set, the user non-packaged add-ons directory, the user add-ons directory, the system non-packaged add-ons directory and the system add-ons directory will be used. If those directories do not contain a subdirectory `Translators`, it will be created. The subdirectories are then added in the above order. If multiple directories contain a translator with the same name, the translator that is located in the path that appears earliest in the above list will be kept.

---

### `GetAllTranslators()`

```cpp
status_t BTranslatorRoster::GetAllTranslators(translator_id ** _list, int32 * _count)
```

Collects the IDs of all translators in the roster in an array. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `_list` | Where the resulting array will be stored. |
| `_count` | Where the number of elements in the resulting array will be stored. |




If this function returns `B_OK` the caller has to call `delete`[] when they are done using *_info*.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | *_list* and *_count* were populated successfully. |
| B_NO_MEMORY | Could not allocate the memory for the array. |

---

### `GetConfigurationMessage()`

```cpp
status_t BTranslatorRoster::GetConfigurationMessage(translator_id translatorID, BMessage * ioExtension)
```

Populates a [BMessage](../application_kit/classBMessage.md) with the settings of the specified translator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `translatorID` | The ID of the translator whose settings *ioExtension* should be populated with. |
| `ioExtension` | The message that should be populated. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | *ioExtension* was populated successfully. |
| B_NO_TRANSLATOR | The roster does not contain any translator with the ID *translatorID*. |
| B_BAD_VALUE | *ioExtension* was `NULL`. |
| B_ERROR | An error occurred or the translator chose not to provide this functionality. |

---

### `GetInputFormats()`

```cpp
status_t BTranslatorRoster::GetInputFormats(translator_id translatorID, const translation_format ** _formats, int32 * _numFormats)
```

Looks up the input formats of the translator with a given ID. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `translatorID` | The ID of the translator whose input formats are requested. |
| `_formats` | Where the array of input formats will be stored. |
| `_numFormats` | Where the number of elements in the array of input formats will be stored. |




Do not free any of the returned data.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | *_formats* and *_numFormats* were successfully set. |
| B_BAD_VALUE | *_formats* or *_numFormats* was `NULL`. |
| B_NO_TRANSLATOR | The roster does not contain any translator with the ID *translatorID*. |

---

### `GetOutputFormats()`

```cpp
status_t BTranslatorRoster::GetOutputFormats(translator_id translatorID, const translation_format ** _formats, int32 * _numFormats)
```

Looks up the output formats of the translator with a given ID. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `translatorID` | The ID of the translator whose output formats are requested. |
| `_formats` | Where the array of output formats will be stored. |
| `_numFormats` | Where the number of elements in the array of output formats will be stored. |




Do not free any of the returned data.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | *_formats* and *_numFormats* were successfully set. |
| B_BAD_VALUE | *_formats* or *_numFormats* was `NULL`. |
| B_NO_TRANSLATOR | The roster does not contain any translator with the ID *translatorID*. |

---

### `GetRefFor()`

```cpp
status_t BTranslatorRoster::GetRefFor(translator_id translatorID, entry_ref * ref)
```

Returns the [entry_ref](../storage_kit/structentry__ref.md) of the specified translator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `translatorID` | The ID of the translator whose [entry_ref](../storage_kit/structentry__ref.md) is to be found. |
| `ref` | Where the [entry_ref](../storage_kit/structentry__ref.md) will be written. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went well. |
| B_BAD_VALUE | *ref* was `NULL`. |
| B_NO_TRANSLATOR | The roster does not contain any translator with the ID *translatorID*. |
| B_ERROR | An error occurred. |

---

### `GetTranslatorInfo()`

```cpp
status_t BTranslatorRoster::GetTranslatorInfo(translator_id translatorID, const char ** _name, const char ** _info, int32 * _version)
```

Looks up general information of the translator with a given ID. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `translatorID` | The ID of the translator whose information is requested. |
| `_name` | Where the name of the translator will be stored. |
| `_info` | Where the description of the translator will be stored. |
| `_version` | Where the version of the translator will be stored. |




Do not free any returned data. If any of *_name*, *_info* and *_version* are `NULL`, the non-null pointers will still be written to.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | All non-null pointers were written to successfully. |
| B_BAD_VALUE | All three pointers were `NULL`. |
| B_NO_TRANSLATOR | The roster does not contain any translator with the ID *translatorID*. |

---

### `GetTranslators()`

```cpp
status_t BTranslatorRoster::GetTranslators(BPositionIO * source, BMessage * ioExtension, translator_info ** _info, int32 * _numInfo, uint32 hintType = 0, const char * hintMIME = NULL, uint32 wantType = 0)
```

Collects information about all translators that are able to perform a certain conversion in an array. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `source` | Read and seek interface to the data to be examinded. |
| `ioExtension` | A message containing configuration information for the translators. |
| `_info` | Where the resulting array will be stored. |
| `_numInfo` | Where the number of elements in the resulting array will be stored. |
| `hintType` | A hint about the data format in *source*. `0` represents an unknown type. |
| `hintMIME` | A hint about the MIME type of *source*. `NULL` represents an unknown type. |
| `wantType` | The format that *source* needs to be translated into. `0` permits any output type. |




If this function returns `B_OK` the caller has to call `delete`[] when they are done using *_info*.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | *_info* and *_numInfo* were successfully populated. |
| B_NO_TRANSLATOR | No suitable translator was found. |
| B_BAD_VALUE | *source*, *_info* or *_numInfo* was `NULL`. |
| B_IO_ERROR | There was an error interacting with *source*. |
| B_NO_MEMORY | Could not allocate enough memory for the array. |

---

### `Identify()`

```cpp
status_t BTranslatorRoster::Identify(BPositionIO * source, BMessage * ioExtension, translator_info * _info, uint32 hintType = 0, const char * hintMIME = NULL, uint32 wantType = 0)
```

Determines the best translator in the roster to perform a certain conversion. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `source` | Read and seek interface to the data to be examined. |
| `ioExtension` | A message containing configuration infortmation for the translators. |
| `_info` | Where information about the best translator will be written. |
| `hintType` | A hint about the data format in *source*. `0` represents an unknown type. |
| `hintMIME` | A hint about the MIME type of *source*. `NULL` represents an unknown type. |
| `wantType` | The format that *source* needs to be translated into. `0` permits any output type. |




To determine the best translator, for all translators that report that they are able to perform the translation, the values they return for quality and capability are multiplied. The translator with the highest value gets returned. Note that quality and capability for the output format are not taken into consideration.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Identification was successful. Information about the chosen translator was written to *_info*. |
| B_NO_TRANSLATOR | No suitable translator was found. |
| B_BAD_VALUE | *source* or *_info* was `NULL`. |
| B_IO_ERROR | There was an error interacting with *source*. |

---

### `Instantiate()`

```cpp
static BArchivable * BTranslatorRoster::Instantiate(BMessage * from)
```

Creates a new [BTranslatorRoster](classBTranslatorRoster.md) from a message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `from` | The message that contains information about a [BTranslatorRoster](classBTranslatorRoster.md). |





**Returns:** `NULL` if *from* was `NULL`, contained invalid archive data or archive data of a class that is not [BTranslatorRoster](classBTranslatorRoster.md). A pointer to a new [BTranslatorRoster](classBTranslatorRoster.md) containing the information from *from* otherwise.

---

### `IsTranslator()`

```cpp
bool BTranslatorRoster::IsTranslator(entry_ref * ref)
```

Determines whether the specified add-on contains at least one translator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The [entry_ref](../storage_kit/structentry__ref.md) to be tested. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The add-on exposes translators. |
| false | The add-on exposes no translators or an error occurred. |

---

### `MakeConfigurationView()`

```cpp
status_t BTranslatorRoster::MakeConfigurationView(translator_id translatorID, BMessage * ioExtension, BView ** _view, BRect * _extent)
```

Creates the configuration view of a specified translator from the roster. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `translatorID` | The ID of the translator whose configuration view should be created. |
| `ioExtension` | A message containing configuration information for the translator. |
| `_view` | Where a pointer to the newly created configuration view will be stored. |
| `_extent` | Where the size of of the newly created configuration view will be stored. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went well. |
| B_BAD_VALUE | *_view* or *_extent* were `NULL` or *ioExtension* was `NULL` or contained bad data. |
| B_NO_TRANSLATOR | The roster does not contain any translator with the ID *translatorID*. |
| B_ERROR | An error occurred or the translator chose not to supply a configuration view. |

---

### `StartWatching()`

```cpp
status_t BTranslatorRoster::StartWatching(BMessenger target)
```

Register a messenger to be notified when the roster changes. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | The [BMessenger](../application_kit/classBMessenger.md) to be registered. |




Whenever a translator is added to or removed from the roster, all messengers that were registered through this method are sent a message. `message->what` will be `B_TRANSLATOR_ADDED` or `B_TRANSLATOR_REMOVED` (as defined in AppDefs.h) respectively.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | *target* was successfully registered. |
| B_NO_MEMORY | Unable to allocate more memory for the list of targets. |

---

### `StopWatching()`

```cpp
status_t BTranslatorRoster::StopWatching(BMessenger target)
```

Unregister a messenger from the notification list. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | The [BMessenger](../application_kit/classBMessenger.md) to be removed. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | *target* was successfully unsubscribed. |
| B_BAD_VALUE | *target* could not be found on the notification list. |





**See also:** [StartWatching(BMessenger target)](classBTranslatorRoster.md#ad389aed357b37c8bf7c6b6a6828355f8)

---

### `Translate()`

```cpp
status_t BTranslatorRoster::Translate(BPositionIO * source, const translator_info * info, BMessage * ioExtension, BPositionIO * destination, uint32 wantOutType, uint32 hintType = 0, const char * hintMIME = NULL)
```

Finds and invokes the best translator for a conversion. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `source` | Read and seek interface to the input data. |
| `info` | Information about wich translator should be used. If *info* is `NULL`, [Identify()](classBTranslatorRoster.md#abc19c6daf3381256da9f11140c030401) will be used to find a suitable translator. |
| `ioExtension` | A message containing configuration information for the translator. |
| `destination` | Write interface to the output location. |
| `wantOutType` | The desired output format. If this is `0`, any type is permitted. |
| `hintType` | A hint about the type of the data in *source*. |
| `hintMIME` | A hint about the MIME type of the data in *source*. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The translated data was successfully written to *destination*. |
| B_NO_TRANSLATOR | When *info* was non-null, it did not match to any translator in the roster. If *info* was `NULL`, then no suitable translator was found. |
| B_ERROR | An error occurred. |
| B_BAD_VALUE | *source* or *destination* was `NULL` or *ioExtension* was `NULL` or contained bad data. |
| B_IO_ERROR | An error occurred accessing *source* or *destination*. |

---

### `Translate()`

```cpp
status_t BTranslatorRoster::Translate(translator_id translatorID, BPositionIO * source, BMessage * ioExtension, BPositionIO * destination, uint32 wantOutType)
```

Uses a specified translator from the roster to perform a conversion. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `translatorID` | The ID of the translator that should be used. |
| `source` | Read and seek interface to the input data. |
| `ioExtension` | A message containing configuration information for the translator. |
| `destination` | Write interface to the output location. |
| `wantOutType` | The desired output format. If this is `0`, any type is permitted. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The translated data was successfully written to *destination*. |
| B_NO_TRANSLATOR | The specified translator cannot handle the data in *source*. |
| B_ERROR | An error occurred. |
| B_BAD_VALUE | *source* or *destination* was `NULL` or *ioExtension* was `NULL` or contained bad data. |
| B_IO_ERROR | An error occurred accessing *source* or *destination*. |

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBTranslatorRoster.html).
