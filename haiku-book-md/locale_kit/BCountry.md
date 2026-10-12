---
name: BCountry
type: class
kit: locale_kit
brief: "Class representing a country"
source: haiku-book
---

# BCountry Class
**Kit/Group:** [Locale Kit](../locale_kit/group__locale.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Class representing a country. 


[BCountry](classBCountry.md) provides information about a particular country including the countries flag (as an HVIF icon), the localized name of the country, and the ISO country code.


Date, time, and number formatting also depends to some extent on the language used so they are found in the [BLocale](classBLocale.md) class instead.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BCountry](#a1cc78037ab1ac3f7c7fc294666a60b67) (const BCountry &other) — Initialize a BCountry from another BCountry object.
* [BCountry](#a290207a5b58c8160bf1f4d7dc767cefb) (const char *countryCode=NULL) — Initialize a BCountry from a country code.
* [~BCountry](#a2a01929a0ca287b74463ff981e228a44) () — Destructor method.
* `const char *` [Code](#a9c13a56f8ff4b13eae2cb9eb667fda32) () const — Gets the ISO country code for the country.
* `status_t` [GetIcon](#a56bf64fc40d482e07b7a882b1cadb318) (BBitmap *result) const — Render the country's flag to the given BBitmap.
* `status_t` [GetName](#a3c3c64cd01d7371e1be172eea7a72a85) (BString &name, const BLanguage *displayLanguage=NULL) const — Writes the country's name into the supplied BString.
* `status_t` [GetPreferredLanguage](#a63a919b79114ab9e50afc2a3bf168951) (BLanguage &) const — Get the most likely language to use in that country.
* `status_t` [InitCheck](#aeb619b42fa62733dcca1e4e58697c506) () const — Check validity of the BCountry object.
* `BCountry &` [operator=](#a3f5228d4016eaed9465b61843a3d628a) (const BCountry &other) — Initialize a BCountry from another BCountry object by overloading the = operator.
* `status_t` [SetTo](#ac682ea0490fe9d3171e040cd570b1b90) (const char *countryCode) — Initialize a BCountry from a country code.

## Detailed Member Documentation

### `BCountry()`

```cpp
BCountry::BCountry(const char * countryCode = NULL)
```

Initialize a [BCountry](classBCountry.md) from a country code. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `countryCode` | The country code to initialize from. |





**Since:** Haiku R1

---

### `BCountry()`

```cpp
BCountry::BCountry(const BCountry & other)
```

Initialize a [BCountry](classBCountry.md) from another [BCountry](classBCountry.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BCountry](classBCountry.md) object to initialize from. |





**Since:** Haiku R1

---

### `~BCountry()`

```cpp
BCountry::~BCountry()
```

Destructor method. 



**Since:** Haiku R1

---

### `Code()`

```cpp
const char * BCountry::Code()const
```

Gets the ISO country code for the country. 



**Returns:** The ISO country code for the country.



**Since:** Haiku R1

---

### `GetIcon()`

```cpp
status_t BCountry::GetIcon(BBitmap * result)const
```

Render the country's flag to the given [BBitmap](../interface_kit/classBBitmap.md). 


This function renders the country's flag to the given [BBitmap](../interface_kit/classBBitmap.md). The bitmap should already be set to the pixel format and size you want to use.


The flag is stored in HVIF format so it can be rendered at any size and color depth.


Parameters

| Parameter | Description |
| :--- | :--- |
| `result` | The [BBitmap](../interface_kit/classBBitmap.md) object to draw the flag into. |





**Returns:** `B_OK` if the drawing was successful.



**Since:** Haiku R1

---

### `GetName()`

```cpp
status_t BCountry::GetName(BString & name, const BLanguage * displayLanguage = NULL)const
```

Writes the country's name into the supplied [BString](../support_kit/classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | A reference to a [BString](../support_kit/classBString.md) to write the country name to. |
| `displayLanguage` | The language to use when writing the name. Can be `NULL` to use the language set by the user's locale. |





**Returns:** A status code, B_OK if everything went fine, or an error code otherwise.



**Since:** Haiku R1

---

### `GetPreferredLanguage()`

```cpp
status_t BCountry::GetPreferredLanguage(BLanguage & language)const
```

Get the most likely language to use in that country. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `language` | A reference to a BLanguage to set to the preferred language. |





**Returns:** A status code, B_OK if everything went fine, or an error code otherwise.



**Since:** Haiku R1

---

### `InitCheck()`

```cpp
status_t BCountry::InitCheck()const
```

Check validity of the [BCountry](classBCountry.md) object. 



**Returns:** B_OK if everything went fine, B_BAD_DATA if the specified country code is not valid, B_NO_MEMORY if the object could not be allocated properly.



**Since:** Haiku R1

---

### `operator=()`

```cpp
BCountry & BCountry::operator=(const BCountry & other)
```

Initialize a [BCountry](classBCountry.md) from another [BCountry](classBCountry.md) object by overloading the = operator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BCountry](classBCountry.md) object to initialize from. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BCountry::SetTo(const char * countryCode)
```

Initialize a [BCountry](classBCountry.md) from a country code. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `countryCode` | The country code to initialize from. |





**Returns:** Same value as InitCheck.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBCountry.html).
