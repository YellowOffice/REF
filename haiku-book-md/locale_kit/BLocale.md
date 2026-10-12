---
name: BLocale
type: class
kit: locale_kit
brief: "Class for representing a locale and its settings"
source: haiku-book
---

# BLocale Class
**Kit/Group:** [Locale Kit](../locale_kit/group__locale.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Class for representing a locale and its settings. 


A locale is defined by the combination of a country and a language. Using these two informations, it is possible to determine the format to use for date, time, and number formatting. The [BLocale](classBLocale.md) class also provide collators, which allows you to sort a list of strings properly depending on a set of rules about accented chars and other special cases that vary over the different locales.


[BLocale](classBLocale.md) is also the class to use when you want to perform formatting or parsing of dates, times, and numbers, in the natural language of the user.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BLocale](#ab8f1c9cb3c16b8eef0e16dcd94f4163b) (const BLanguage *language=NULL, const BFormattingConventions *conventions=NULL) — Initializes a BLocale object corresponding to the passed in language and conventions.
* [BLocale](#ad38c7098a382708b4e65c27df9f1183c) (const BLocale &other) — Initializes a BLocale object as a copy of other.
* [~BLocale](#a9c9d3df81a9381e7fa5f1aff70878122) () — Destructor method.
* `status_t` [GetCollator](#add9b62e1276138a8a2853b634aa92adc) (BCollator *collator) const — Sets collator object to the default collator for the BLocale.
* `status_t` [GetFormattingConventions](#a8cc776da97fbe6d1b01b7ee5bfb64760) (BFormattingConventions *conventions) const — Fills out conventions with the default formatting conventions for the BLocale.
* `status_t` [GetLanguage](#a5ecf38b372ec866475c116639f7e0242) (BLanguage *language) const — Sets language object to the default language for the BLocale.
* `const char *` [GetString](#a40a6f3f39d711ed0e2efa41d4d859e6c) (uint32 id) const — Gets the language string for the locale.
* `BLocale &` [operator=](#ae1aaeedea30ad7f8df586e9bc9eef7d7) (const BLocale &other) — Gets the collator associated to this locale.
* `void` [SetCollator](#af3cb42bdb2b55c864971fe4aad9af6bd) (const BCollator &newCollator) — Set the collator for this locale.
* `void` [SetFormattingConventions](#a0acf391e1c2c7669c83cb398ce11cdef) (const BFormattingConventions &conventions) — Sets the formatting convention for this locale.
* `void` [SetLanguage](#a87ba312e6bf9fb5c70724cc30377073d) (const BLanguage &newLanguage) — Set the language for this locale.

## Detailed Member Documentation

### `BLocale()`

```cpp
BLocale::BLocale(const BLanguage * language = NULL, const BFormattingConventions * conventions = NULL)
```

Initializes a [BLocale](classBLocale.md) object corresponding to the passed in *language* and *conventions*. 



**Since:** Haiku R1

---

### `BLocale()`

```cpp
BLocale::BLocale(const BLocale & other)
```

Initializes a [BLocale](classBLocale.md) object as a copy of *other*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BLocale](classBLocale.md) object to initialize from. |





**Since:** Haiku R1

---

### `~BLocale()`

```cpp
BLocale::~BLocale()
```

Destructor method. 



**Since:** Haiku R1

---

### `GetCollator()`

```cpp
status_t BLocale::GetCollator(BCollator * collator)const
```

Sets *collator* object to the default collator for the [BLocale](classBLocale.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `collator` | A pointer to a [BCollator](classBCollator.md) object to fill out. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went well. |
| B_BAD_VALUE | `NULL` *collator* object passed in. |
| B_ERROR | Unable to lock the [BLocale](classBLocale.md). |





**Since:** Haiku R1

---

### `GetFormattingConventions()`

```cpp
status_t BLocale::GetFormattingConventions(BFormattingConventions * conventions)const
```

Fills out *conventions* with the default formatting conventions for the [BLocale](classBLocale.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `conventions` | A pointer to a BFormattingConventions object to fill out. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went well. |
| B_BAD_VALUE | `NULL` *conventions* object passed in. |
| B_ERROR | Unable to lock the [BLocale](classBLocale.md). |





**Since:** Haiku R1

---

### `GetLanguage()`

```cpp
status_t BLocale::GetLanguage(BLanguage * language)const
```

Sets *language* object to the default language for the [BLocale](classBLocale.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `language` | A pointer to a BLanguage object to fill out. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went well. |
| B_BAD_VALUE | `NULL` *language* object passed in. |
| B_ERROR | Unable to lock the [BLocale](classBLocale.md). |





**Since:** Haiku R1

---

### `GetString()`

```cpp
const char * BLocale::GetString(uint32 id)const
```

Gets the language string for the locale. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `id` | The locale *id* to get the language of. |

---

### `operator=()`

```cpp
BLocale & BLocale::operator=(const BLocale & other)
```

Gets the collator associated to this locale. 


status_t [BLocale::GetCollator(BCollator* collator) const](classBLocale.md#add9b62e1276138a8a2853b634aa92adc) 


Returns the collator in use for this locale, allowing you to use it to sort a set of strings.



**Since:** Haiku R1


Initializes a [BLocale](classBLocale.md) object as a copy of *other* by overloading the = operator.


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BLocale](classBLocale.md) object to initialize from. |





**Since:** Haiku R1

---

### `SetCollator()`

```cpp
void BLocale::SetCollator(const BCollator & newCollator)
```

Set the collator for this locale. 


If unable to lock the [BLocale](classBLocale.md) *newCollator* is left untouched.


Parameters

| Parameter | Description |
| :--- | :--- |
| `newCollator` | The collator to set. |





**Since:** Haiku R1

---

### `SetFormattingConventions()`

```cpp
void BLocale::SetFormattingConventions(const BFormattingConventions & conventions)
```

Sets the formatting convention for this locale. 


If unable to lock the [BLocale](classBLocale.md) *conventions* is left untouched.


Parameters

| Parameter | Description |
| :--- | :--- |
| `conventions` | The formatting convention to set. |





**Since:** Haiku R1

---

### `SetLanguage()`

```cpp
void BLocale::SetLanguage(const BLanguage & newLanguage)
```

Set the language for this locale. 


If unable to lock the [BLocale](classBLocale.md) *newLanguage* is left untouched.


Parameters

| Parameter | Description |
| :--- | :--- |
| `newLanguage` | The code of the language to set to locale to. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBLocale.html).
