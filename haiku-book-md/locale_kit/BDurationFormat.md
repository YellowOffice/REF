---
name: BDurationFormat
type: class
kit: locale_kit
brief: "Formatter for time intervals"
source: haiku-book
---

# BDurationFormat Class
**Kit/Group:** [Locale Kit](../locale_kit/group__locale.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Formatter for time intervals. 


[BDurationFormat](classBDurationFormat.md) is a formatter for time intervals. A time interval is defined by its start and end values, and the result is a string such as "1 hour, 2 minutes, 28 seconds".



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BDurationFormat](#a46c91429cf0cbaf27a5a2037ec29ca9f) (const BDurationFormat &other) — Copy Constructor.
* [BDurationFormat](#a0c9d97b5f31d56b7979ea2133cf030e4) (const BLanguage &language, const BFormattingConventions &conventions, const BString &separator=", ", const time_unit_style style=B_TIME_UNIT_FULL) — Constructor.
* [BDurationFormat](#aef36eb90b2ed8b63afa4634714d15164) (const BString &separator=", ", const time_unit_style style=B_TIME_UNIT_FULL) — Constructor.
* `virtual` [~BDurationFormat](#a642042b63fa1d99c6f5fd6f4207bb333) () — Destructor.
* `status_t` [Format](#aed797e2a366459e29fd0d3f78182e8d8) (BString &buffer, const bigtime_t startValue, const bigtime_t stopValue) const — Formats a duration defined by its start and end values.
* `void` [SetSeparator](#a0d10a0407170ddb8079a92c86f68d4dd) (const BString &separator) — Replace the separator for this formatter.
* `status_t` [SetTimeZone](#afd6f13d7956d363c506b2069f18a875c) (const BTimeZone *timeZone) — Sets the timezone for this formatter.

## Detailed Member Documentation

### `BDurationFormat()`

```cpp
BDurationFormat::BDurationFormat(const BLanguage & language, const BFormattingConventions & conventions, const BString & separator = ", ", const time_unit_style style = B_TIME_UNIT_FULL)
```

Constructor. 



> [!WARNING]
> Creating a [BDurationFormat](classBDurationFormat.md) is a costly operation. Most of the time want to use the default one through the [BLocale](classBLocale.md) class.


Parameters

| Parameter | Description |
| :--- | :--- |
| `language` | The language to use. |
| `conventions` | The formatting conventions to use. |
| `separator` | String appended between the duration elements. |
| `style` | The time unit style to use. |





**Since:** Haiku R1

---

### `BDurationFormat()`

```cpp
BDurationFormat::BDurationFormat(const BString & separator = ", ", const time_unit_style style = B_TIME_UNIT_FULL)
```

Constructor. 



> [!WARNING]
> Creating a [BDurationFormat](classBDurationFormat.md) is a costly operation. Most of the time want to use the default one through the [BLocale](classBLocale.md) class.


Parameters

| Parameter | Description |
| :--- | :--- |
| `separator` | String appended between the duration elements. |
| `style` | The time unit style to use. |





**Since:** Haiku R1

---

### `BDurationFormat()`

```cpp
BDurationFormat::BDurationFormat(const BDurationFormat & other)
```

Copy Constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BDurationFormat](classBDurationFormat.md) object to copy from. |





**Since:** Haiku R1

---

### `~BDurationFormat()`

```cpp
BDurationFormat::~BDurationFormat()
```

Destructor. 



**Since:** Haiku R1

---

### `Format()`

```cpp
status_t BDurationFormat::Format(BString & buffer, const bigtime_t startValue, const bigtime_t stopValue)const
```

Formats a duration defined by its start and end values. 


The start and end values are in milliseconds. The result is appended to the buffer. The full time style uses full words (hours, minutes, seconds), while the short one uses units (h, m, s).


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | The buffer to fill out. |
| `startValue` | The start value in milliseconds. |
| `stopValue` | The stop value in milliseconds. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *buffer* was `NULL` or invalid. |
| B_ERROR | Formatting error. |





**Since:** Haiku R1

---

### `SetSeparator()`

```cpp
void BDurationFormat::SetSeparator(const BString & separator)
```

Replace the separator for this formatter. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `separator` | The separator string to set. |





**Since:** Haiku R1

---

### `SetTimeZone()`

```cpp
status_t BDurationFormat::SetTimeZone(const BTimeZone * timeZone)
```

Sets the timezone for this formatter. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `timeZone` | The [BTimeZone](classBTimeZone.md) object to set. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | Format object is `NULL`. |
| B_ERROR | Other errors. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBDurationFormat.html).
