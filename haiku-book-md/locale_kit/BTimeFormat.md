---
name: BTimeFormat
type: class
kit: locale_kit
brief: "Formatter for times"
source: haiku-book
---

# BTimeFormat Class
**Kit/Group:** [Locale Kit](../locale_kit/group__locale.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Formatter for times. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BTimeFormat](#a2b50630d755536ac5d9b635cb6f824ac) () — Default Constructor. The current system locale is used.
* [BTimeFormat](#aae2dfce6b3269db342864211651efd65) (const BLanguage &language, const BFormattingConventions &conventions) — Language and formatting convention constructor.
* [BTimeFormat](#a3c2ceba93c851ea52a78d0db84ce618a) (const BTimeFormat &other) — Copy Constructor.
* `virtual` [~BTimeFormat](#a68c679ef13de01dcbb3366770b33c4d2) () — Destructor.
* `status_t` [Format](#a207ec36e9853557aa616b18c2d3abbd9) (BString &string, const time_t time, const BTimeFormatStyle style, const BTimeZone *timeZone=NULL) const — Fills in string with a formatted time for the given time, style, and timeZone for the locale.
* `status_t` [Format](#a094e6458a42f53167a440f57d8072572) (BString &string, int *&fieldPositions, int &fieldCount, time_t time, BTimeFormatStyle style) const — Fills in string with a custom formatted date according to the given parameters for the locale and fills out an array of fieldPositions which must be freed by the caller and a fieldCount which contains the number of positions.
* `ssize_t` [Format](#aa3b37bfb1fdce83c5740263628649719) (char *string, size_t maxSize, time_t time, BTimeFormatStyle style) const — Fills in string with a formatted time up to maxSize bytes for the given time and style for the locale.
* `status_t` [GetTimeFields](#a47658ac0d566e56db7edd798cc51ffd6) (BDateElement *&fields, int &fieldCount, BTimeFormatStyle style) const — Get the type of each field in the time format of the locale.

## Detailed Member Documentation

### `BTimeFormat()`

```cpp
BTimeFormat::BTimeFormat()
```

Default Constructor. The current system locale is used. 



**Since:** Haiku R1

---

### `BTimeFormat()`

```cpp
BTimeFormat::BTimeFormat(const BLanguage & language, const BFormattingConventions & format)
```

Language and formatting convention constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `language` | The *language* to use. |
| `format` | The formatting convention to use. |





**Since:** Haiku R1

---

### `BTimeFormat()`

```cpp
BTimeFormat::BTimeFormat(const BTimeFormat & other)
```

Copy Constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BTimeFormat](classBTimeFormat.md) object to copy from. |





**Since:** Haiku R1

---

### `~BTimeFormat()`

```cpp
BTimeFormat::~BTimeFormat()
```

Destructor. 



**Since:** Haiku R1

---

### `Format()`

```cpp
status_t BTimeFormat::Format(BString & string, const time_t time, const BTimeFormatStyle style, const BTimeZone * timeZone = NULL)const
```

Fills in *string* with a formatted time for the given *time*, *style*, and *timeZone* for the locale. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string buffer to fill with the formatted time. |
| `time` | The time (in seconds since epoch) to format. |
| `style` | Specifies whether to use the long format or short format. |
| `timeZone` | Specifies the time zone to use, if `NULL`, use the system default time zone (usually UTC). |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ERROR | Unable to lock the [BLocale](classBLocale.md). |
| B_NO_MEMORY | Ran out of memory while creating the object. |
| B_BAD_VALUE | There was not enough space to store the result. |





**Since:** Haiku R1

---

### `Format()`

```cpp
status_t BTimeFormat::Format(BString & string, int *& fieldPositions, int & fieldCount, time_t time, BTimeFormatStyle style)const
```

Fills in *string* with a custom formatted date according to the given parameters for the locale and fills out an array of *fieldPositions* which must be freed by the caller and a *fieldCount* which contains the number of positions. 


The positions are offsets in the string at which each element of the time (hour, minute, second, etc) and the separator starting positions. These can be used, for example, to split the string in parts to use in a locale-aware set of BMenuFields to edit the time in the local format.


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string buffer to fill with the formatted time. |
| `fieldPositions` | An array of time field positions to be filled out. |
| `fieldCount` | The number of *fields* in *fieldPositions* to be filled out. |
| `time` | The time (in seconds since epoch) to format. |
| `style` | Specify the long format (with day name, full month name) or the short format, 08/12/2010 or similar. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ERROR | Unable to lock the [BLocale](classBLocale.md). |
| B_NO_MEMORY | Ran out of memory while creating the object. |
| B_BAD_VALUE | There was not enough space to store the result. |





**Since:** Haiku R1

---

### `Format()`

```cpp
ssize_t BTimeFormat::Format(char * string, size_t maxSize, time_t time, BTimeFormatStyle style)const
```

Fills in *string* with a formatted time up to *maxSize* bytes for the given *time* and *style* for the locale. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string buffer to fill with the formatted time. |
| `maxSize` | The size of the buffer. |
| `time` | The time (in seconds since midnight) to format. |
| `style` | Specify the long format or the short format. |





**Returns:** The number of bytes written during the time formatting.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_ERROR | Unable to lock the [BLocale](classBLocale.md). |
| B_NO_MEMORY | Ran out of memory while creating the object. |
| B_BAD_VALUE | There was not enough space to store the result. |





**Since:** Haiku R1

---

### `GetTimeFields()`

```cpp
status_t BTimeFormat::GetTimeFields(BDateElement *& fields, int & fieldCount, BTimeFormatStyle style)const
```

Get the type of each field in the time format of the locale. 


This method is used most often in combination with FormatTime(). FormatTime() gives you the offset of each field in a formatted string, and [GetTimeFields()](classBTimeFormat.md#a47658ac0d566e56db7edd798cc51ffd6) gives you the type of the field at a given offset. With this information you can handle the formatted time string as a list of fields that you can split and alter at will.


Parameters

| Parameter | Description |
| :--- | :--- |
| `fields` | Pointer to the fields object. |
| `fieldCount` | The number of fields. |
| `style` | Specify the long format or the short format. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ERROR | Unable to lock the [BLocale](classBLocale.md). |
| B_NO_MEMORY | Ran out of memory while creating the object. |
| B_BAD_VALUE | Bad or invalid *fields* data. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBTimeFormat.html).
