---
name: BUnicodeChar
type: class
kit: locale_kit
brief: "Management of all information about characters"
source: haiku-book
---

# BUnicodeChar Class
**Kit/Group:** [Locale Kit](../locale_kit/group__locale.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Management of all information about characters. 


This class provide a set of tools for managing the whole set of characters defined by unicode. This include information about special sets of characters such as if the character is whitespace, or alphanumeric. It also provides the uppercase equivalent of a character and determines whether a character can be ornamented with accents.


This class consists entirely of static methods, so you do not have to instantiate it. You can call one of the methods passing in the character that you want to be examined.


Note all the function work with chars encoded in UTF-32. This is not the most usual way to handle characters, but it is the fastest. To convert an UTF-8 string to an UTF-32 character use the [FromUTF8()](classBUnicodeChar.md#afc8fda9ba1759ecae751d92cea4dac0a) method.



**Since:** Haiku R1

## Member List

### Static Public Member Functions

* `static int32` [DigitValue](#a67bb2e55a6df3edfd7e8cbed5c0895f4) (uint32 c) — Gets the numeric value c.
* `static uint32` [FromUTF8](#afc8fda9ba1759ecae751d92cea4dac0a) (const char **in) — Transform a UTF-8 string to an UTF-32 character.
* `static bool` [IsAlNum](#a4f2527179e7166f757d8a96daa3b8b77) (uint32 c) — Determine if c is alphanumeric.
* `static bool` [IsAlpha](#a5742a6696309783267a3402fac001961) (uint32 c) — Determine if c is alphabetic.
* `static bool` [IsBase](#aeb5bb45061d6aba81f79b824eea3f280) (uint32 c) — Determine if c can be used with a diacritic.
* `static bool` [IsControl](#aaae54f38cc91cbb2227e48d86583f2b4) (uint32 c) — Determine if c is a control character.
* `static bool` [IsDefined](#ae5250d53b709291a61a66279d0ccc061) (uint32 c) — Determine if c is defined.
* `static bool` [IsDigit](#af839a05c7079c29dd5131c10e95dbc3e) (uint32 c) — Determine if c is numeric.
* `static bool` [IsHexDigit](#aebff7cb08394bcf1a7ed0fb7880d2ff7) (uint32 c) — Determine if c is a hexadecimal digit.
* `static bool` [IsLower](#aa6c837f19a90696fa20bf75f07a466a4) (uint32 c) — Determine if c is lowercase.
* `static bool` [IsPrintable](#a1d938ac2279485c3a8a09c5ae7406275) (uint32 c) — Determine if c is printable.
* `static bool` [IsPunctuation](#a3eae5f1aceb4bda319ad3228b6d4d7e1) (uint32 c) — Determine if c is punctuation character.
* `static bool` [IsSpace](#a73440dcc192f995a423694f7150afad5) (uint32 c) — Determine if c is a space.
* `static bool` [IsTitle](#aaa46b9e4e672588a077cda7d55acbd72) (uint32 c) — Determine if c is title case.
* `static bool` [IsUpper](#adbbd94d47f0c5cd850aeca194ed8cca3) (uint32 c) — Determine if c is uppercase.
* `static bool` [IsWhitespace](#a10120c029b7157d97cfae72c9b254f64) (uint32 c) — Determine if c is whitespace.
* `static uint32` [ToLower](#a565af2e2c1bea1f8268b92c98a8576fa) (uint32 c) — Transforms c to lowercase.
* `static uint32` [ToTitle](#ae241f694ac02fbae4b88da234101a3e7) (uint32 c) — Transforms c to title case.
* `static uint32` [ToUpper](#a60941ccc1f91411200cce679d7ecb962) (uint32 c) — Transforms c to uppercase.
* `static void` [ToUTF8](#a357fcf22fa1cf39303ce104e0172435e) (uint32 c, char **out) — Transform a character to UTF-8 encoding.
* `static int8` [Type](#adf54317eca46b1d2da67ed46a3c4b0ca) (uint32 c) — Gets the type of a character.
* `static size_t` [UTF8StringLength](#af0ba5d552b7c76a46bcaa524907adff2) (const char *string) — Counts the characters in the given NUL terminated string.
* `static size_t` [UTF8StringLength](#a2d04840a4ff3327bb341d3f1c366523f) (const char *string, size_t maxLength) — Counts the characters in the given string up to maxLength characters.

## Detailed Member Documentation

### `DigitValue()`

```cpp
int32 BUnicodeChar::DigitValue(uint32 c)
```

Gets the numeric value *c*. 



**Returns:** The numeric version of the specified unicode character.



**Since:** Haiku R1

---

### `FromUTF8()`

```cpp
uint32 BUnicodeChar::FromUTF8(const char ** in)
```

Transform a UTF-8 string to an UTF-32 character. 


If the string contains multiple characters, only the fist one is used. This function updates the in pointer so that it points on the next character for the following call.



**Returns:** The UTF-32 encoded version of *in*.



**Since:** Haiku R1

---

### `IsAlNum()`

```cpp
static bool BUnicodeChar::IsAlNum(uint32 c)
```

Determine if *c* is alphanumeric. 



**Returns:** `true` if the specified unicode character is a alphabetic or numeric character.



**Since:** Haiku R1

---

### `IsAlpha()`

```cpp
static bool BUnicodeChar::IsAlpha(uint32 c)
```

Determine if *c* is alphabetic. 



**Returns:** `true` if the specified unicode character is an alphabetic character.



**Since:** Haiku R1

---

### `IsBase()`

```cpp
static bool BUnicodeChar::IsBase(uint32 c)
```

Determine if *c* can be used with a diacritic. 



> [!NOTE]
> [IsBase()](classBUnicodeChar.md#aeb5bb45061d6aba81f79b824eea3f280) does not determine if a unicode character is distinct.



**Returns:** `true` if the specified unicode character is a base form character that can be used with a diacritic.



**Since:** Haiku R1

---

### `IsControl()`

```cpp
static bool BUnicodeChar::IsControl(uint32 c)
```

Determine if *c* is a control character. 


Example control characters are the non-printable ASCII characters from 0x0 to 0x1F.



**Returns:** `true` if the specified unicode character is a control character.



**See also:** [IsPrintable()](classBUnicodeChar.md#a1d938ac2279485c3a8a09c5ae7406275)



**Since:** Haiku R1

---

### `IsDefined()`

```cpp
static bool BUnicodeChar::IsDefined(uint32 c)
```

Determine if *c* is defined. 


In unicode some codes are not valid or not attributed yet. For these codes this method will return `false`.



**Returns:** `true` if the specified unicode character is defined.



**Since:** Haiku R1

---

### `IsDigit()`

```cpp
static bool BUnicodeChar::IsDigit(uint32 c)
```

Determine if *c* is numeric. 



**Returns:** `true` if the specified unicode character is a number character.



**Since:** Haiku R1

---

### `IsHexDigit()`

```cpp
static bool BUnicodeChar::IsHexDigit(uint32 c)
```

Determine if *c* is a hexadecimal digit. 



**Returns:** `true` if the specified unicode character is a hexadecimal number character.



**Since:** Haiku R1

---

### `IsLower()`

```cpp
static bool BUnicodeChar::IsLower(uint32 c)
```

Determine if *c* is lowercase. 



**Returns:** `true` if the specified unicode character is a lowercase character.



**Since:** Haiku R1

---

### `IsPrintable()`

```cpp
static bool BUnicodeChar::IsPrintable(uint32 c)
```

Determine if *c* is printable. 


Printable characters are not control characters.



**Returns:** `true` if the specified unicode character is a printable character.



**See also:** [IsControl()](classBUnicodeChar.md#aaae54f38cc91cbb2227e48d86583f2b4)



**Since:** Haiku R1

---

### `IsPunctuation()`

```cpp
static bool BUnicodeChar::IsPunctuation(uint32 c)
```

Determine if *c* is punctuation character. 



**Returns:** `true` if the specified unicode character is a punctuation character.



**Since:** Haiku R1

---

### `IsSpace()`

```cpp
static bool BUnicodeChar::IsSpace(uint32 c)
```

Determine if *c* is a space. 


Unlike [IsWhitespace()](classBUnicodeChar.md#a10120c029b7157d97cfae72c9b254f64) this function will return `true` for non-breakable spaces. This method is useful for determining if the character will render as an empty space which can be stretched on-screen.



**Returns:** `true` if the specified unicode character is some kind of a space character.



**See also:** [IsWhitespace()](classBUnicodeChar.md#a10120c029b7157d97cfae72c9b254f64)



**Since:** Haiku R1

---

### `IsTitle()`

```cpp
static bool BUnicodeChar::IsTitle(uint32 c)
```

Determine if *c* is title case. 


Title case characters are a smaller version of normal uppercase letters.



**Returns:** `true` if the specified unicode character is a title case character.



**Since:** Haiku R1

---

### `IsUpper()`

```cpp
static bool BUnicodeChar::IsUpper(uint32 c)
```

Determine if *c* is uppercase. 



**Returns:** `true` if the specified unicode character is an uppercase character.



**Since:** Haiku R1

---

### `IsWhitespace()`

```cpp
static bool BUnicodeChar::IsWhitespace(uint32 c)
```

Determine if *c* is whitespace. 


This method is essentially the same as [IsSpace()](classBUnicodeChar.md#a73440dcc192f995a423694f7150afad5), but excludes all non-breakable spaces.



**Returns:** `true` if the specified unicode character is a whitespace character.



**See also:** [IsSpace()](classBUnicodeChar.md#a73440dcc192f995a423694f7150afad5)



**Since:** Haiku R1

---

### `ToLower()`

```cpp
uint32 BUnicodeChar::ToLower(uint32 c)
```

Transforms *c* to lowercase. 



**Returns:** The lowercase version of the specified unicode character.



**Since:** Haiku R1

---

### `ToTitle()`

```cpp
uint32 BUnicodeChar::ToTitle(uint32 c)
```

Transforms *c* to title case. 



**Returns:** The title case version of the specified unicode character.



**Since:** Haiku R1

---

### `ToUpper()`

```cpp
uint32 BUnicodeChar::ToUpper(uint32 c)
```

Transforms *c* to uppercase. 



**Returns:** The uppercase version of the specified unicode character.



**Since:** Haiku R1

---

### `ToUTF8()`

```cpp
void BUnicodeChar::ToUTF8(uint32 c, char ** out)
```

Transform a character to UTF-8 encoding. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `out` | Set to the UTF-8 encoding of the specified unicode character. |





**Since:** Haiku R1

---

### `Type()`

```cpp
static int8 BUnicodeChar::Type(uint32 c)
```

Gets the type of a character. 



**Returns:** A member of the `unicode_char_category` enum.



**Since:** Haiku R1

---

### `UTF8StringLength()`

```cpp
size_t BUnicodeChar::UTF8StringLength(const char * string)
```

Counts the characters in the given `NUL` terminated string. 



**Returns:** the number of UTF-8 characters in the `NUL` terminated string.



**See also:** [BString::CountChars()](../support_kit/classBString.md#ab7324c44bfcbd8c8b590b257eafc7886)



**Since:** Haiku R1

---

### `UTF8StringLength()`

```cpp
size_t BUnicodeChar::UTF8StringLength(const char * string, size_t maxLength)
```

Counts the characters in the given string up to *maxLength* characters. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | does not need to be `NUL` terminated if you specify a *maxLength* that is shorter than the maximum length of the string. |
| `maxLength` | The maximum length of the string in bytes. |





**Returns:** the number of UTF-8 characters in the `NUL` terminated string up to *maxLength* characters.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBUnicodeChar.html).
