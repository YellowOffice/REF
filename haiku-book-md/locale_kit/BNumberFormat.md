---
name: BNumberFormat
type: class
kit: locale_kit
brief: "Formatter for numbers and monetary values"
source: haiku-book
---

# BNumberFormat Class
**Kit/Group:** [Locale Kit](../locale_kit/group__locale.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Formatter for numbers and monetary values. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [~BNumberFormat](#afaa7b4585648a11f1dd865abc65d7a17) () — Destructor.
* `status_t` [Format](#a396a60cc6ef6504abdae0e8ed64b3ac2) (BString &string, const double value) — Format the double value as a string and put the result into string in the current locale.
* `status_t` [Format](#a70187c85b58c1769a4286f942991d056) (BString &string, const int32 value) — Format the int32 value as a string and put the result into string in the current locale.
* `ssize_t` [Format](#a3b6ae24878908e80ba3a173521c5d8f1) (char *string, size_t maxSize, const double value) — Format the double value as a string and put the result into string up to maxSize bytes in the current locale.
* `ssize_t` [Format](#ae6f77207e74d982b38c58b6937486b4b) (char *string, size_t maxSize, const int32 value) — Format the int32 value as a string and put the result into string up to maxSize bytes in the current locale.
* `status_t` [FormatMonetary](#aa692e59beaf7a961601cba3a23b87099) (BString &string, const double value) — Format the double value as a monetary string and put the result into string in the current locale.
* `ssize_t` [FormatMonetary](#ad3124227366747f9fffed18584a2b3fd) (char *string, size_t maxSize, const double value) — Format the double value as a monetary string and put the result into string up to maxSize bytes in the current locale.

## Detailed Member Documentation

### `~BNumberFormat()`

```cpp
BNumberFormat::~BNumberFormat()
```

Destructor. 



**Since:** Haiku R1

---

### `Format()`

```cpp
status_t BNumberFormat::Format(BString & string, const double value)
```

Format the `double` *value* as a string and put the result into *string* in the current locale. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to put the formatted number into. |
| `value` | The number that you want to get a formatted version of. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ERROR | Unable to lock the [BNumberFormat](classBNumberFormat.md). |
| B_NO_MEMORY | Ran out of memory while creating the NumberFormat object. |
| B_BAD_VALUE | There was not enough space to store the result. |





**See also:** BNumberFormat::Format(BString* string, int32 value) const



**Since:** Haiku R1

---

### `Format()`

```cpp
status_t BNumberFormat::Format(BString & string, const int32 value)
```

Format the `int32` *value* as a string and put the result into *string* in the current locale. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to put the formatted number into. |
| `value` | The number that you want to get a formatted version of. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ERROR | Unable to lock the [BNumberFormat](classBNumberFormat.md). |
| B_NO_MEMORY | Ran out of memory while creating the NumberFormat object. |
| B_BAD_VALUE | There was not enough space to store the result. |





**See also:** BNumberFormat::Format(BString* string, double value) const



**Since:** Haiku R1

---

### `Format()`

```cpp
ssize_t BNumberFormat::Format(char * string, size_t maxSize, const double value)
```

Format the `double` *value* as a string and put the result into *string* up to *maxSize* bytes in the current locale. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to put the formatted number into. |
| `maxSize` | The maximum of bytes to copy into *string*. |
| `value` | The number that you want to get a formatted version of. |





**Returns:** The length of the string created or an error status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_ERROR | Unable to lock the [BNumberFormat](classBNumberFormat.md). |
| B_NO_MEMORY | Ran out of memory while creating the NumberFormat object. |
| B_BAD_VALUE | There was not enough space to store the result. |





**See also:** BNumberFormat::Format(char* string, size_t maxSize,
	int32 value) const



**Since:** Haiku R1

---

### `Format()`

```cpp
ssize_t BNumberFormat::Format(char * string, size_t maxSize, const int32 value)
```

Format the `int32` *value* as a string and put the result into *string* up to *maxSize* bytes in the current locale. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to put the formatted number into. |
| `maxSize` | The maximum of bytes to copy into *string*. |
| `value` | The number that you want to get a formatted version of. |





**Returns:** The length of the string created or an error status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_ERROR | Unable to lock the [BNumberFormat](classBNumberFormat.md). |
| B_NO_MEMORY | Ran out of memory while creating the NumberFormat object. |
| B_BAD_VALUE | There was not enough space to store the result. |





**See also:** BNumberFormat::Format(char* string, size_t maxSize,
	double value) const



**Since:** Haiku R1

---

### `FormatMonetary()`

```cpp
status_t BNumberFormat::FormatMonetary(BString & string, const double value)
```

Format the `double` *value* as a monetary string and put the result into *string* in the current locale. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to put the monetary formatted number into. |
| `value` | The number to format as a monetary *value*. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ERROR | Unable to lock the [BNumberFormat](classBNumberFormat.md). |
| B_NO_MEMORY | Ran out of memory while creating the NumberFormat object. |
| B_BAD_VALUE | There was not enough space to store the result. |





**See also:** BNumberFormat::Format(BString* string, double value) const



**Since:** Haiku R1

---

### `FormatMonetary()`

```cpp
ssize_t BNumberFormat::FormatMonetary(char * string, size_t maxSize, const double value)
```

Format the `double` *value* as a monetary string and put the result into *string* up to *maxSize* bytes in the current locale. 


It uses the money symbol set by the Locale (€, $, ...) or the generic money symbol (¤) if the locale is not country-specific.


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to put the monetary formatted number into. |
| `maxSize` | The maximum of bytes to copy into *string*. |
| `value` | The number to format as a monetary *value*. |





**Returns:** The length of the string created or an error status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_ERROR | Unable to lock the [BNumberFormat](classBNumberFormat.md). |
| B_NO_MEMORY | Ran out of memory while creating the NumberFormat object. |
| B_BAD_VALUE | There was not enough space to store the result. |





**See also:** BNumberFormat::Format(char* string, size_t maxSize, double value) const



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBNumberFormat.html).
