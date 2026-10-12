---
name: BDateFormat
type: class
kit: locale_kit
brief: "Formatter for dates"
source: haiku-book
---

# BDateFormat Class
**Kit/Group:** [Locale Kit](../locale_kit/group__locale.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Formatter for dates. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BDateFormat](#a34192a2dd6c0fddf349f4bf8a6cea819) (const BDateFormat &other) — Copy Constructor.
* [BDateFormat](#a1ae923cd57baac144afaeb9ec730bed3) (const BLanguage &language, const BFormattingConventions &format) — Language and formatting convention constructor.
* [BDateFormat](#a73f4f100f3f6d4909cbff0ad940fda08) (const BLocale *locale=NULL) — Locale constructor.
* `virtual` [~BDateFormat](#a4e1fd346005ccd2ffd4ee51da087b35b) () — Destructor.
* `status_t` [Format](#aa240a7355abcf2f69e5f7c40223033d7) (BString &string, const time_t time, const BDateFormatStyle style, const BTimeZone *timeZone=NULL) const — Fills in string with a formatted date for the given time, style, and timeZone for the locale.
* `status_t` [Format](#af74b53bd1f3653dabdb7803d51ffda04) (BString &string, int *&fieldPositions, int &fieldCount, const time_t time, const BDateFormatStyle style) const — Fills in string with a custom formatted date according to the given parameters for the locale and fills out an array of fieldPositions which must be freed by the caller and a fieldCount which contains the number of positions.
* `ssize_t` [Format](#a080f552db87ba9240bb8a13b1f236c29) (char *string, const size_t maxSize, const time_t time, const BDateFormatStyle style) const — Fills in string with a formatted date up to maxSize bytes for the given time and style for the locale.
* `status_t` [GetFields](#a8d147bfab995cd48604a211732afe30c) (BDateElement *&fields, int &fieldCount, BDateFormatStyle style) const — Get the type of each field in the date format of the locale.
* `status_t` [GetStartOfWeek](#a27a5359c2a3e28cb9bca2058d402f57e) (BWeekday *weekday) const — Returns the day used as the start of week in this locale.

## Detailed Member Documentation

### `BDateFormat()`

```cpp
BDateFormat::BDateFormat(const BLocale * locale = NULL)
```

Locale constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `locale` | The locale to use, can be `NULL` for the default locale. |





**Since:** Haiku R1

---

### `BDateFormat()`

```cpp
BDateFormat::BDateFormat(const BLanguage & language, const BFormattingConventions & format)
```

Language and formatting convention constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `language` | The *language* to use. |
| `format` | The formatting convention to use. |





**Since:** Haiku R1

---

### `BDateFormat()`

```cpp
BDateFormat::BDateFormat(const BDateFormat & other)
```

Copy Constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BDateFormat](classBDateFormat.md) object to copy from. |





**Since:** Haiku R1

---

### `~BDateFormat()`

```cpp
BDateFormat::~BDateFormat()
```

Destructor. 



**Since:** Haiku R1

---

### `Format()`

```cpp
status_t BDateFormat::Format(BString & string, const time_t time, const BDateFormatStyle style, const BTimeZone * timeZone = NULL)const
```

Fills in *string* with a formatted date for the given *time*, *style*, and *timeZone* for the locale. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string buffer to fill with the formatted date. |
| `time` | The time (in seconds since epoch) to format |
| `style` | Specify the long format (with day name, full month name) or the short format, 08/12/2010 or similar. |
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
status_t BDateFormat::Format(BString & string, int *& fieldPositions, int & fieldCount, const time_t time, const BDateFormatStyle style)const
```

Fills in *string* with a custom formatted date according to the given parameters for the locale and fills out an array of *fieldPositions* which must be freed by the caller and a *fieldCount* which contains the number of positions. 


The positions are offsets in the string at which each element of the date (day, month, year, etc) and the separator starting positions. These can be used, for example, to split the string into parts to use in a locale-aware set of BMenuFields to edit the date in the local format.


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string buffer to fill with the formatted date. |
| `fieldPositions` | An array of date field positions to be filled out. |
| `fieldCount` | The number of *fields* in *fieldPositions* to be filled out. |
| `time` | The time (in seconds since epoch) to format |
| `style` | Specify the long format (with day name, full month name) or the short format, 08/12/2010 or similar. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ERROR | Unable to lock the [BLocale](classBLocale.md). |
| B_NO_MEMORY | Ran out of memory while creating the *string* buffer or *fieldPositions* array. |
| B_BAD_VALUE | There was not enough space to store the result. |





**Since:** Haiku R1

---

### `Format()`

```cpp
ssize_t BDateFormat::Format(char * string, const size_t maxSize, const time_t time, const BDateFormatStyle style)const
```

Fills in *string* with a formatted date up to *maxSize* bytes for the given *time* and *style* for the locale. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string buffer to fill with the formatted date. |
| `maxSize` | The size of the buffer. |
| `time` | The time (in seconds since epoch) to format |
| `style` | Specify the long format (with day name, full month name) or the short format, 08/12/2010 or similar. |





**Returns:** The number of bytes written during the date formatting.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_ERROR | Unable to lock the [BLocale](classBLocale.md). |
| B_NO_MEMORY | Ran out of memory while creating the object. |
| B_BAD_VALUE | There was not enough space to store the result. |





**Since:** Haiku R1

---

### `GetFields()`

```cpp
status_t BDateFormat::GetFields(BDateElement *& fields, int & fieldCount, BDateFormatStyle style)const
```

Get the type of each field in the date format of the locale. 


This method is most often used in combination with the version of [Format()](classBDateFormat.md#a080f552db87ba9240bb8a13b1f236c29) that takes a fieldPositions parameter. [Format()](classBDateFormat.md#a080f552db87ba9240bb8a13b1f236c29) gives you the offset of each field in a formatted string, and [GetFields()](classBDateFormat.md#a8d147bfab995cd48604a211732afe30c) gives you the type of the field at a given offset. With these informations, you can handle the formatted date string as a list of fields that you can split and alter at will.


Parameters

| Parameter | Description |
| :--- | :--- |
| `fields` | Pointer to the array of BDateElement objects. |
| `fieldCount` | The number of fields in *fields*. |
| `style` | Specify the long format (with day name, full month name) or the short format, "08/12/2010" or similar. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ERROR | Unable to lock the [BLocale](classBLocale.md). |
| B_NO_MEMORY | Ran out of memory while creating the object. |
| B_BAD_VALUE | Bad or invalid *fields* data. |





**See also:** BDateFormat::GetFields(BDateElement*&, int&, BTimeFormatStyle) const



**Since:** Haiku R1

---

### `GetStartOfWeek()`

```cpp
status_t BDateFormat::GetStartOfWeek(BWeekday * startOfWeek)const
```

Returns the day used as the start of week in this locale. 


Possible values for *startOfWeek* include:


* `B_WEEKDAY_SUNDAY`

* `B_WEEKDAY_MONDAY`

* `B_WEEKDAY_TUESDAY`

* `B_WEEKDAY_WEDNESDAY`

* `B_WEEKDAY_THURSDAY`

* `B_WEEKDAY_FRIDAY`

* `B_WEEKDAY_SATURDAY`




**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *startOfWeek* is `NULL`. |
| B_ERROR | Unable to lock the [BLocale](classBLocale.md) or another error occurred. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBDateFormat.html).
