---
name: BDateTimeFormat
type: class
kit: locale_kit
brief: "Formatter for datetimes"
source: haiku-book
---

# BDateTimeFormat Class
**Kit/Group:** [Locale Kit](../locale_kit/group__locale.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Formatter for datetimes. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BDateTimeFormat](#a02517326f1349c7359f9e5ce805f2c16) (const BDateTimeFormat &other) — Copy Constructor.
* [BDateTimeFormat](#a65336a0cecd02488de60264b175bfc86) (const BLanguage &language, const BFormattingConventions &conventions) — Language and formatting convention constructor.
* [BDateTimeFormat](#a7dbb44126ed962bd709513fe1c5da4d6) (const BLocale *locale=NULL) — Locale constructor.
* `virtual` [~BDateTimeFormat](#a02298aa64117cd2e98c8b3523d4abefa) () — Destructor.
* `status_t` [Format](#a9f6db975646cfaca1afcc6550a7965b5) (BString &buffer, const time_t time, BDateFormatStyle dateStyle, BTimeFormatStyle timeStyle, const BTimeZone *timeZone=NULL) const — Fills in string with a formatted datetime for the given time, timeStyle, and timeZone for the locale.
* `ssize_t` [Format](#a91a1ce4df7e34dcdc6963a61b9322417) (char *target, const size_t maxSize, const time_t time, BDateFormatStyle dateStyle, BTimeFormatStyle timeStyle) const — Fills in string with a formatted datetime up to maxSize bytes for the given time and style for the locale.

## Detailed Member Documentation

### `BDateTimeFormat()`

```cpp
BDateTimeFormat::BDateTimeFormat(const BLocale * locale = NULL)
```

Locale constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `locale` | The locale to use, can be `NULL` for the default locale. |

---

### `BDateTimeFormat()`

```cpp
BDateTimeFormat::BDateTimeFormat(const BLanguage & language, const BFormattingConventions & format)
```

Language and formatting convention constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `language` | The *language* to use. |
| `format` | The formatting convention to use. |

---

### `BDateTimeFormat()`

```cpp
BDateTimeFormat::BDateTimeFormat(const BDateTimeFormat & other)
```

Copy Constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BDateTimeFormat](classBDateTimeFormat.md) object to copy from. |





**Since:** Haiku R1

---

### `~BDateTimeFormat()`

```cpp
BDateTimeFormat::~BDateTimeFormat()
```

Destructor. 



**Since:** Haiku R1

---

### `Format()`

```cpp
status_t BDateTimeFormat::Format(BString & buffer, const time_t time, BDateFormatStyle dateStyle, BTimeFormatStyle timeStyle, const BTimeZone * timeZone = NULL)const
```

Fills in *string* with a formatted datetime for the given *time*, *timeStyle*, and *timeZone* for the locale. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | The string buffer to fill with the formatted date. |
| `time` | The time (in seconds since epoch) to format |
| `dateStyle` | Specifies the long format or the short format of the date. |
| `timeStyle` | Specifies the long format or the short format of the time. |
| `timeZone` | Specifies the time zone to use, if `NULL`, use the system default time zone (usually UTC). |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ERROR | Unable to lock the [BLocale](classBLocale.md). |
| B_NO_MEMORY | Ran out of memory while creating the object. |





**Since:** Haiku R1

---

### `Format()`

```cpp
ssize_t BDateTimeFormat::Format(char * target, const size_t maxSize, const time_t time, BDateFormatStyle dateStyle, BTimeFormatStyle timeStyle)const
```

Fills in *string* with a formatted datetime up to *maxSize* bytes for the given *time* and *style* for the locale. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | The string buffer to fill with the formatted datetime. |
| `maxSize` | The size of the buffer. |
| `time` | The time (in seconds since epoch) to format |
| `dateStyle` | Specify the long format or the short format of the date. |
| `timeStyle` | Specify the long format or the short format of the time. |





**Returns:** The number of bytes written during the datetime formatting.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_ERROR | Unable to lock the [BLocale](classBLocale.md). |
| B_NO_MEMORY | Ran out of memory while creating the object. |
| B_BAD_VALUE | There was not enough space to store the result. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBDateTimeFormat.html).
