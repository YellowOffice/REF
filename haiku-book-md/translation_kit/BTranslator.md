---
name: BTranslator
type: class
kit: translation_kit
brief: "Abstract class that defines the necessary functionality of a translator"
source: haiku-book
---

# BTranslator Class
**Kit/Group:** [Translation Kit](../translation_kit/group__translation.md) | [Translation Kit library (libtranslation.so)](group__libtranslation.md)

## Description

Abstract class that defines the necessary functionality of a translator. 


[BTranslator](classBTranslator.md) is the core class of the translation kit. Every translator defines input and output data types it can work with. A [BTranslator](classBTranslator.md) uses [BPositionIO](../support_kit/classBPositionIO.md) as an abstraction for the data it operates on. It is able to decide wether incoming data is of any of its known input types and, upon successful identification, translate it to any of its output formats. It may also provide a config view that appears in the DataTranslations preference app.


Usually, a translator is very specific. It only offers translations between the format it was created for and the basic format for that media type. As an example, the translator for GIF images only translates between GIF images and bitmaps, the baseline format for images.


The function `make_nth_translator` enables add-ons to expose translators. Communication between applications and BTranslators is carried out by the [BTranslatorRoster](classBTranslatorRoster.md) class.



> [!NOTE]
> Another option to create a translator is using a BFuncTranslator.


RemarksIn most cases it is easier to derive from BaseTranslator instead of [BTranslator](classBTranslator.md). BaseTranslator provides a lot of functionality that is common for most translators as well as a unified method to save settings and routines for handling bitmaps.

**Since:** BeOS R3

## Member List

### Public Member Functions

* [BTranslator](#a2f62f219cbc88c68e24b190c7815f49a) () — Creates a new BTranslator and sets its reference count to 1.
* `BTranslator *` [Acquire](#a1a385cacf95b85e7988d41437a00cf64) () — Increments the reference count by 1 and returns a pointer to itself.
* `BTranslator *` [Release](#a5edb71d50a84af82d6c25979d38c385b) () — Decrements the reference count by 1. If the reference count is decreased to zero, the object is deleted.
* `int32` [ReferenceCount](#ac6db049c2e18559761528e9b304acba8) () — Gets the current reference count.
* `virtual const char *` [TranslatorName](#a780b894e10d20a443aa68ff18d98fa9a) () const =0 — Pure virtual. Returns the name of the translator.
* `virtual const char *` [TranslatorInfo](#ae893bfad197cfc77ad06fa8edcd974f6) () const =0 — Pure virtual. Returns a brief description of the translator.
* `virtual int32` [TranslatorVersion](#ab1367814e1344d6d41679f3e33d6fa16) () const =0 — Pure virtual. Returns the version of the translator.
* `virtual const translation_format *` [InputFormats](#a7730d0bd8774b558e41f2e19b4362b46) (int32 *_count) const =0 — Pure virtual. Returns an array containing information about all input formats the translator can handle.
* `virtual const translation_format *` [OutputFormats](#a8513e71cfe17d1915613401996af8eb8) (int32 *_count) const =0 — Pure virtual. Returns an array containing information about all output formats the translator can produce.
* `virtual status_t` [Identify](#afeeb58dd769f1fdf5ba29da69d9fff25) (BPositionIO *source, const translation_format *format, BMessage *extension, translator_info *info, uint32 outType)=0 — Pure virtual. Analyzes source and decides whether this translator can work with the provided format.
* `virtual status_t` [Translate](#aceccae4a5041677afcb71cd4e739416c) (BPositionIO *source, const translator_info *info, BMessage *extension, uint32 outType, BPositionIO *destination)=0 — Pure virtual. Reads the provided data and tries to translate it to a given format.
* `virtual status_t` [MakeConfigurationView](#a04604cd147897713783a936feb6b28e7) (BMessage *extension, BView **_view, BRect *_extent) — Virtual. Creates a BView that contains information and configuration options for the translator.
* `virtual status_t` [GetConfigurationMessage](#aba382f2b2672c6732dd6905875d2fb3b) (BMessage *extension) — Populates a BMessage with the settings of the translator.
* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BTranslator()`

```cpp
BTranslator::BTranslator()
```

Creates a new [BTranslator](classBTranslator.md) and sets its reference count to 1. 



**Since:** BeOS R3

---

### `Acquire()`

```cpp
BTranslator * BTranslator::Acquire()
```

Increments the reference count by 1 and returns a pointer to itself. 



**Returns:** `this`.



**Since:** BeOS R3

---

### `GetConfigurationMessage()`

```cpp
status_t BTranslator::GetConfigurationMessage(BMessage * extension)
```

Populates a [BMessage](../application_kit/classBMessage.md) with the settings of the translator. 


A standard set of possible fields is defined in [TranslatorFormats.h](TranslatorFormats_8h.md). This method is optional. If the translator chose not to implement it, `B_ERROR` will be returned.


Parameters

| Parameter | Description |
| :--- | :--- |
| `extension` | The [BMessage](../application_kit/classBMessage.md) that is populated. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went well. |
| B_ERROR | An error occurred or the method was not overriden by the translator. |
| B_BAD_VALUE | *extension* was `NULL`. |





**Since:** BeOS R3

---

### `Identify()`

```cpp
status_t BTranslator::Identify(BPositionIO * source, const translation_format * format, BMessage * extension, translator_info * info, uint32 outType)
```

Pure virtual. Analyzes *source* and decides whether this translator can work with the provided format. 


The translator examines the data in source and tries to identify its format (for instance by checking for magic numbers). It may use the hints provided by *format*. If it is successful, and it is able to translate the data at hand to *outType*, it populates *info* with information about the input format and returns `B_OK`. If it is unable to identify the data or cannot translate it to *outType*, it returns `B_NO_TRANSLATOR`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `source` | Read and seek interface to the input data. |
| `format` | Hints about the incoming data. |
| `extension` | A message containing configuration information for the translator. A standard set of possible fields is defined in [TranslatorFormats.h](TranslatorFormats_8h.md). |
| `info` | Where the translator will write information about the determined input format in case identification is successful. |
| `outType` | If *outType* is non-zero, identification will only be successful if the translator can transform the data in source to the format denoted by *outType*. |





> [!WARNING]
> When creating a translator, be prepared for the information in *format* to be inaccurate or wrong.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The translator has identified the data in *source*, has verified its ability to translate it to *outType* and has written information describing it to *info*. |
| B_NO_TRANSLATOR | The translator does not know how to handle the data in *source* or cannot translate it to *outType*. |
| B_BAD_VALUE | *extension* was `NULL` or contained bad data. |
| B_ERROR | An error occurred. |





**Since:** BeOS R3

---

### `InputFormats()`

```cpp
const translation_format * BTranslator::InputFormats(int32 * _count)const
```

Pure virtual. Returns an array containing information about all input formats the translator can handle. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `_count` | Where the number of input formats that are returned will be written. |





**Returns:** A pointer to the first element of the array of input formats.



**Since:** BeOS R3

---

### `MakeConfigurationView()`

```cpp
status_t BTranslator::MakeConfigurationView(BMessage * extension, BView ** _view, BRect * _extent)
```

Virtual. Creates a [BView](../interface_kit/classBView.md) that contains information and configuration options for the translator. 


This method is optional. If the translator chose not to implement it, `B_ERROR` will be returned.


Parameters

| Parameter | Description |
| :--- | :--- |
| `extension` | A message containing configuration information for the translator. A standard set of possible fields is defined in [TranslatorFormats.h](TranslatorFormats_8h.md). |
| `_view` | Where a pointer to the newly created configuration view will be stored. |
| `_extent` | Where the size of the newly created configuration view will be stored. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went well. |
| B_ERROR | An error occurred or the method was not overriden by the translator. |
| B_BAD_VALUE | *_view* or *_extent* were `NULL` or *extension* was `NULL` or contained bad data. |





**Since:** BeOS R3

---

### `OutputFormats()`

```cpp
const translation_format * BTranslator::OutputFormats(int32 * _count)const
```

Pure virtual. Returns an array containing information about all output formats the translator can produce. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `_count` | Where the number of output formats that are returned will be written. |





**Returns:** A pointer to the first element of the array of output formats.



**Since:** BeOS R3

---

### `ReferenceCount()`

```cpp
int32 BTranslator::ReferenceCount()
```

Gets the current reference count. 



**Returns:** The current reference count.



**Since:** BeOS R3

---

### `Release()`

```cpp
BTranslator * BTranslator::Release()
```

Decrements the reference count by 1. If the reference count is decreased to zero, the object is deleted. 



**Returns:** `this` if the object was not destroyed, `NULL` if it was.



**Since:** BeOS R3

---

### `Translate()`

```cpp
status_t BTranslator::Translate(BPositionIO * source, const translator_info * info, BMessage * extension, uint32 outType, BPositionIO * destination)
```

Pure virtual. Reads the provided data and tries to translate it to a given format. 


The translator attempts to translate the data in *source*, which may or may not have the format represented by *info*, to *outType* and then write the result to destination. Upon success, it returns `B_OK`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `source` | Read and seek interface to the input data. |
| `info` | Hints about the incoming data. |
| `extension` | A message containing configuration information for the translator. A standard set of possible fields is defined in [TranslatorFormats.h](TranslatorFormats_8h.md). |
| `outType` | The identifier of the desired output format. An *outType* of 0 is equivalent to the defualt format for the media type if the translator. |
| `destination` | Write interface for the destination of the data. |





> [!WARNING]
> When creating a translator, be prepared for the information in *format* to be inaccurate or wrong.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The translated data was successfully written to destination. |
| B_ERROR | An error occurred during memory allocation or the conversion itself. |
| B_BAD_VALUE | *extension* was `NULL` or contained bad data. |
| B_NO_TRANSLATOR | The translator cannot handle the input. |





**Since:** BeOS R3

---

### `TranslatorInfo()`

```cpp
const char * BTranslator::TranslatorInfo()const
```

Pure virtual. Returns a brief description of the translator. 



**Returns:** A brief description of the translator.



**Since:** BeOS R3

---

### `TranslatorName()`

```cpp
const char * BTranslator::TranslatorName()const
```

Pure virtual. Returns the name of the translator. 


Amongst other uses, the name is used to populate Save as-dropdowns and for the preference window.



**Returns:** The name of the translator.



**Since:** BeOS R3

---

### `TranslatorVersion()`

```cpp
int32 BTranslator::TranslatorVersion()const
```

Pure virtual. Returns the version of the translator. 


The correct way to format the version is using the `B_TRANSLATION_MAKE_VERSION` macro from [TranslationDefs.h](TranslationDefs_8h.md).



**Returns:** The version of the translator.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBTranslator.html).
