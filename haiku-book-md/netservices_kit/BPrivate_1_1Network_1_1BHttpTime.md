---
name: BPrivate::Network::BHttpTime
type: class
kit: netservices_kit
brief: "Utility class that can parse and format HTTP Date strings"
source: haiku-book
---

# BPrivate::Network::BHttpTime Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Utility class that can parse and format HTTP Date strings. 


See the description of the module in [HttpTime.h](HttpTime_8h.md) for more information about HTTP timestamps.


Note that for quick conversions of a BDateTime into a [BString](../support_kit/classBString.md) and vice versa, you can also use the [format_http_time()](namespaceBPrivate_1_1Network.md#adf43cae73e73f416b4ec05923e81a772) and [parse_http_time()](namespaceBPrivate_1_1Network.md#a564db27874e23e8e080df76f21d39ed8) utilities.



**Since:** Haiku R1

## Member List

### Classes

* `class` [InvalidInput](#InvalidInput) — Error that indicates that a string cannot be parsed as a valid HTTP timestamp.

### Public Member Functions

* [BHttpTime](#a828931a80f511cc15b98c8e930dde2a0) () noexcept — Constructs a new object and sets the timestamp to the current time.
* [BHttpTime](#af7b0356a07fc11bbef1079a4e07d23fa) (BDateTime date) — Constructs a new object and sets the timestamp to date.
* [BHttpTime](#a4c8625d39a63bca0f677e39d50d26ba3) (const BString &dateString) — Constructs a new object and parses the timestamp from dateString.
* `BDateTime` [DateTime](#a288063850b49d6aad2554178303f02aa) () const noexcept — Get the current timestamp.
* `BHttpTimeFormat` [DateTimeFormat](#a57c8a3c869c450814a0ee5f7ce003f5d) () const noexcept — Get the format that the current timestamp parsed from.
* `void` [SetTo](#a2c9b2c4cf24f24a0ec7962332659a69f) (BDateTime date) — Set the current timestamp to date.
* `void` [SetTo](#a5fa42216d0c23cad9437a883445487aa) (const BString &string) — Set the current timestamp by parsing string.
* `BString` [ToString](#a10ee3127792f468ac943ef70c7e5c380) (BHttpTimeFormat outputFormat=BHttpTimeFormat::RFC1123) const — Formats the timestamp to a string.

## Detailed Member Documentation

### `BHttpTime()`

```cpp
BPrivate::Network::BHttpTime::BHttpTime()
```

Constructs a new object and sets the timestamp to the current time. 



**Since:** Haiku R1

---

### `BHttpTime()`

```cpp
BPrivate::Network::BHttpTime::BHttpTime(BDateTime date)
```

Constructs a new object and sets the timestamp to *date*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `date` | A valid BDateTime object for the desired timestamp. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| [BHttpTime::InvalidInput](classBPrivate_1_1Network_1_1BHttpTime_1_1InvalidInput.md) | The *date* does not contain a valid timestamp. |





**Since:** Haiku R1

---

### `BHttpTime()`

```cpp
BPrivate::Network::BHttpTime::BHttpTime(const BString & dateString)
```

Constructs a new object and parses the timestamp from *dateString*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dateString` | A string that contains a valid HTTP timestamp. The *dateString* must not contain any characters, other than the timestamp. It is up to the caller to sanitize any input, including trimming whitespace at the beginning and end of the string. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| [BHttpTime::InvalidInput](classBPrivate_1_1Network_1_1BHttpTime_1_1InvalidInput.md) | The *dateString* cannot be parsed as a valid timestamp. |





**Since:** Haiku R1

---

### `DateTime()`

```cpp
BDateTime BPrivate::Network::BHttpTime::DateTime()const
```

Get the current timestamp. 



**Returns:** A valid BDateTime object that contains the timestamp that this object is currently set to.



**Since:** Haiku R1

---

### `DateTimeFormat()`

```cpp
BHttpTimeFormat BPrivate::Network::BHttpTime::DateTimeFormat()const
```

Get the format that the current timestamp parsed from. 


If the timestamp was parsed from a string, this method supplies a bit of information about what format the original string was in. Note that for both the RFC 1132 and RFC 850 formats, the parsing is slightly less strict than the RFC prescribes. This may mean that if you parse a non-canonical string, and then format it back using the same format specifier, the two strings may differ in content.


If the timestamp was set by setting it to a BDateTime object, then this will always return `BHttpTimeFormat::RFC1123`.



**Returns:** The [BHttpTimeFormat](namespaceBPrivate_1_1Network.md#a9b49062e24f11190deacce6b0ab82a5e) that describes the format the input string was in, or `BHttpTimeFormat::RFC1123` if the timestamp was set by a BDateTime.



**Since:** Haiku R1

---

### `SetTo()`

```cpp
void BPrivate::Network::BHttpTime::SetTo(BDateTime date)
```

Set the current timestamp to *date*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `date` | A valid BDateTime object for the desired timestamp. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| [BHttpTime::InvalidInput](classBPrivate_1_1Network_1_1BHttpTime_1_1InvalidInput.md) | The *date* does not contain a valid timestamp. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
void BPrivate::Network::BHttpTime::SetTo(const BString & string)
```

Set the current timestamp by parsing *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | A string that contains a valid HTTP timestamp. The *dateString* must not contain any characters, other than the timestamp. It is up to the caller to sanitize any input, including trimming whitespace at the beginning and end of the string. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| [BHttpTime::InvalidInput](classBPrivate_1_1Network_1_1BHttpTime_1_1InvalidInput.md) | The *dateString* cannot be parsed as a valid timestamp. |





**Since:** Haiku R1

---

### `ToString()`

```cpp
BString BPrivate::Network::BHttpTime::ToString(BHttpTimeFormat outputFormat = BHttpTimeFormat::RFC1123)const
```

Formats the timestamp to a string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `outputFormat` | The requested outputformat. The default is the recommended RFC 1123 format. |





**Returns:** A string that contains the formatted timestamp.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | In the future this method may throw this exception when the memory for the output string cannot be allocated. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BHttpTime.html).
