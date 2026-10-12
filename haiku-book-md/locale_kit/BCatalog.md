---
name: BCatalog
type: class
kit: locale_kit
brief: "String localization handling"
source: haiku-book
---

# BCatalog Class
**Kit/Group:** [Locale Kit](../locale_kit/group__locale.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

String localization handling. 


[BCatalog](classBCatalog.md) is the class that allows you to perform string localization. This means you give it a string in english, and it automatically returns the translation of this string in the user's specified language, if available.


Most of the time, you don't have to deal with [BCatalog](classBCatalog.md) directly. You use the translation macros instead. However, there are some cases where you will have to use catalogs directly. These include :


* Tools for managing catalogs : if you want to add, remove or edit entries in a catalog, you need to do it using the [BCatalog](classBCatalog.md) class.

* Accessing catalogs other than your own : the macros only grant you access to the catalog linked with your application. To access other catalogs (for example if you create a script interpreter and want to localize the scripts), you will have to open a catalog associated with your script.




Using the macros
You don't have to do much in your program to handle catalogs. You must first set the B_TRANSLATION_CONTEXT define to a string that identifies which part of the application the strings you will translate are in. This allows the translators to keep track of the strings in the catalog more easily, and find where they are visible in the application. then, all you have to do, is enclose any string you want to make translatable in the B_TRANSLATE() macro. This macro has two uses, it will allow your text to be replaced at run-time by the proper localized one, but it will also allow to build the base catalog, the one that you will send to the translator team, from your sourcecode.


Note that each image (application, library or add-on) using these macros must be linked with liblocalestub.a. This allows the Locale Kit to identify it and locate the matching string catalogs for translation.



Chaining of catalogs
The catalogs you get from the locale kit are designed to use a fallback system so that the user get strings in the language he's the most fluent with, depending on what catalogs are available.


For example, if the user sets his language preferences as French(France), spanish, english, when an application loads a catalog, the following rules are used:


* Try to load a French(France) catalog. If it is found, this catalog will automatically include strings from the generic french catalog.

* Try to load a generic french catalog.

* Try to load a generic spanish catalog.

* Try to load a generic english catalog.

* If all of them failed, use the strings that are in the source code.



Note that French(France) will failback to French, but then directly to the language in the source code. This avoids mixing 3 or more languages in the same application if the catalogs are incomplete and avoids confusion.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BCatalog](#a45b0bd772e3aee626a65aba2e9e88a6e) () — Construct an empty BCatalog object.
* [BCatalog](#a95fcfcd9674c4a1c6875ea0ca318ded2) (const char *signature, const char *language=NULL) — Construct a BCatalog object for the given application signature.
* [BCatalog](#a338e2e4c785310844ded2fe5840f5c32) (const entry_ref &catalogOwner, const char *language=NULL, uint32 fingerprint=0) — Construct a BCatalog object for the given catalogOwner.
* `virtual` [~BCatalog](#a7ca1efd6e50d05caabcc24d294da25a5) () — Destroys the BCatalog object freeing memory used by it.
* `int32` [CountItems](#a418f04da03164887a5e3eba2f61e6bc2) () const — Gets the number of items in the catalog.
* `status_t` [GetData](#a8b9181119a2971a214473dcc482a3415) (const char *name, BMessage *msg) — Get custom data from the catalog.
* `status_t` [GetData](#ac5c03e634c4b07f14ae374e6ff3d67f4) (uint32 id, BMessage *msg) — Get custom data from the catalog.
* `status_t` [GetFingerprint](#a19269c5a3a23e28de3ccf5d96bcdbf90) (uint32 *fingerprint) — Get the catalog fingerprint.
* `status_t` [GetLanguage](#af8ecfe730a02fe7dd03eb086545521ec) (BString *language) — Get the catalog language.
* `status_t` [GetSignature](#aaa4c2bf292dbd2dad5938177eafffced) (BString *signature) — Get the catalog mime-signature.
* `const char *` [GetString](#a151e295bda9c5411fa0e2781f9f0653a) (const char *string, const char *context=NULL, const char *comment=NULL) — Get a string from the catalog.
* `const char *` [GetString](#ac6caaefe60ec06d0aa901e0dcc46fb37) (uint32 id) — Get a string by id from the catalog.
* `status_t` [InitCheck](#a6cab9f7d71eec3cee2c19ba4a4153761) () const — Check if the catalog is in a valid and usable state.
* `status_t` [SetTo](#a1736341fa377b305e27ff4ea0f77c139) (const char *signature, const char *language=NULL) — Reload the string data.
* `status_t` [SetTo](#a029e8144be7b24bb4dce96e4b4a283fc) (const entry_ref &catalogOwner, const char *language=NULL, uint32 fingerprint=0) — Reload the string data.

## Detailed Member Documentation

### `BCatalog()`

```cpp
BCatalog::BCatalog()
```

Construct an empty [BCatalog](classBCatalog.md) object. 


Should be followed by [SetTo()](classBCatalog.md#a029e8144be7b24bb4dce96e4b4a283fc) method to set the catalog.



**Since:** Haiku R1

---

### `BCatalog()`

```cpp
BCatalog::BCatalog(const entry_ref & catalogOwner, const char * language = NULL, uint32 fingerprint = 0)
```

Construct a [BCatalog](classBCatalog.md) object for the given *catalogOwner*. 


If you don't specify a language, the system default list will be used. The language is passed here as a 2 letter ISO code.


The fingerprint is a way to check that the catalog that will be loaded matches the current version of the application. A catalog made for a different version of the application can be loaded if you set the fingerprint to `0`. This is usually not a problem, it only means that some strings may not be translated properly. But if you want to provide different versions of your application, it may be useful to separate their catalogs.


Parameters

| Parameter | Description |
| :--- | :--- |
| `catalogOwner` | [entry_ref](../storage_kit/structentry__ref.md) or application, add-on or library for which to load a catalog. |
| `language` | The language of the catalog to load. If `NULL`, the user settings will be used. |
| `fingerprint` | The fingerprint version-info for the catalog to load. If `0`, the fingerprint will not be checked,and any version of the catalog will be loaded. |





**Since:** Haiku R1

---

### `BCatalog()`

```cpp
BCatalog::BCatalog(const char * signature, const char * language = NULL)
```

Construct a [BCatalog](classBCatalog.md) object for the given application *signature*. 


If you don't specify a language, the system default list will be used. The language is passed here as a 2 letter ISO code.


This constructor is used to load catalogs that are not related to an executable or library file (so there is no [entry_ref](../storage_kit/structentry__ref.md) usable to identify the catalog). As it uses only the MIME signature, it cannot load catalogs from application resources or a catalog file located next to the application. Only the catalogs in the standard system directories (data/locale/catalogs) are checked. Moreover, only the default catalog format is available, not custom formats from catalog add-ons.


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | MIME signature for which to load a catalog. |
| `language` | The language of the catalog to load. If `NULL`, the user settings will be used. |





**Since:** Haiku R1

---

### `~BCatalog()`

```cpp
BCatalog::~BCatalog()
```

Destroys the [BCatalog](classBCatalog.md) object freeing memory used by it. 



**Since:** Haiku R1

---

### `CountItems()`

```cpp
int32 BCatalog::CountItems()const
```

Gets the number of items in the catalog. 



**Returns:** the number of strings in the catalog or 0 on error.



**Since:** Haiku R1

---

### `GetData()`

```cpp
status_t BCatalog::GetData(const char * name, BMessage * msg)
```

Get custom data from the catalog. 


This method allows you to localize something else than raw text. This may include pictures, sounds, videos, or anything else. Note there is no support for generating a catalog with such data inside, and the current format may not support it. If you need to localize data that is not text, it is advised to handle it by yourself.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the data to retrieve. |
| `msg` | The [BMessage](../application_kit/classBMessage.md) to fill in with the data. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ERROR | Unable to get an exclusive lock on data. |
| B_NO_INIT | Catalog is `NULL`. |
| B_NAME_NOT_FOUND | catalog with the specified *name* could not be found. |





**Since:** Haiku R1

---

### `GetData()`

```cpp
status_t BCatalog::GetData(uint32 id, BMessage * msg)
```

Get custom data from the catalog. 


As for GetString, the id-based version may be subject to hash-collisions, but is faster.


Note the current catalog format doesn't allow storing custom data in catalogs, so the only way to use this method is providing your own catalog add-on for storing the data.



**Since:** Haiku R1

---

### `GetFingerprint()`

```cpp
status_t BCatalog::GetFingerprint(uint32 * fp)
```

Get the catalog fingerprint. 


This method setsfp to the fingerprint of the catalog. This allows you to check which version of the sourcecode this catalog was generated from.


Parameters

| Parameter | Description |
| :--- | :--- |
| `fp` | The integer to set to the fingerprint value. |





**Returns:** An error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went as expected. |
| B_ERROR | Could not get exclusive lock on catalog. |
| B_BAD_VALUE | *fp* is `NULL`. |
| B_NO_INIT | Catalog data is `NULL`. |





**Since:** Haiku R1

---

### `GetLanguage()`

```cpp
status_t BCatalog::GetLanguage(BString * lang)
```

Get the catalog language. 


This method fills the lang string with the language name for the catalog.


Parameters

| Parameter | Description |
| :--- | :--- |
| `lang` | The string where to copy the language. |





**Returns:** An error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went as expected. |
| B_ERROR | Could not get exclusive lock on catalog. |
| B_BAD_VALUE | *lang* is `NULL`. |
| B_NO_INIT | Catalog data is `NULL`. |





**Since:** Haiku R1

---

### `GetSignature()`

```cpp
status_t BCatalog::GetSignature(BString * sig)
```

Get the catalog mime-signature. 


This method fills the sig string with the mime-signature associated to the catalog.


Parameters

| Parameter | Description |
| :--- | :--- |
| `sig` | The string where to copy the signature. |





**Returns:** An error code.



**Since:** Haiku R1

---

### `GetString()`

```cpp
const char * BCatalog::GetString(const char * string, const char * context = NULL, const char * comment = NULL)
```

Get a string from the catalog. 


This method access the data of the catalog and returns you the translated version of the string. You must pass it the context where the string is, as the same string may appear somewhere else and need a different translation. The comment is optional. It is meant as an help to translators, when the string alone is not helpful enough or there are special things to note. The comment is also used as a way to uniquely identify a string, so if two identical strings share the same context, it is still possible to provide different translations.


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to translate. |
| `context` | The context where the string is located. |
| `comment` | Supplementary comment for translators. |





**Returns:** The translated string, or the one passed as a parameter if no translation was found.



**Since:** Haiku R1

---

### `GetString()`

```cpp
const char * BCatalog::GetString(uint32 id)
```

Get a string by id from the catalog. 


The id based version of this method is slightly faster, as it doesn't have to compute the hash from the 3 parameters. However, it will fail if there is an hash collision, so you should still fallback to the first one in case of problems. Also note that the hash value may be different from one catalog to another, depending on the file format they are stored in, so you shouldn't rely on this method unless you are sure you can keep all the catalog files under control.


Parameters

| Parameter | Description |
| :--- | :--- |
| `id` | The identifier of the string. |





**Returns:** The translated string if found, or an empty string.



**Since:** Haiku R1

---

### `InitCheck()`

```cpp
status_t BCatalog::InitCheck()const
```

Check if the catalog is in a valid and usable state. 



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The catalog is initialized properly. |
| B_ERROR | Could not get exclusive lock on catalog. |
| B_NO_INIT | Catalog data is `NULL`. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BCatalog::SetTo(const char * signature, const char * language = NULL)
```

Reload the string data. 


This method reloads the data for the given signature and language.


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | The MIME signature identifying the catalog to load. |
| `language` | The language of the catalog to load. If `NULL`, the user settings will be used. |





**Returns:** A status code, `B_OK` on success, `B_ERROR` on error.



**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BCatalog::SetTo(const entry_ref & catalogOwner, const char * language = NULL, uint32 fingerprint = 0)
```

Reload the string data. 


This method reloads the data for the given file, language and fingerprint.


Parameters

| Parameter | Description |
| :--- | :--- |
| `catalogOwner` | The `entry_ref` of the application, add-on or library for which you want to load a catalog. |
| `language` | The language of the catalog to load. If `NULL`, the user settings will be used. |
| `fingerprint` | The fingerprint of the catalog you want to load. |





**Returns:** A status code, `B_OK` on success, `B_ERROR` on error.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBCatalog.html).
