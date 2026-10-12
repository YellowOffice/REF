---
name: BPrivate::Network::BHttpFields::FieldName
type: class
kit: netservices_kit
brief: "Representation of a HTTP header name"
source: haiku-book
---

# BPrivate::Network::BHttpFields::FieldName Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Representation of a HTTP header name. 


As per the HTTP specification, header fields have a name. There are limitations to which characters are supported. As per the specification, header field names are case insensitive. This means that the `content-encoding` is equal to `Content-Encoding` or even `COnTenT-ENcOdING`.


A header field name can never be empty.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [operator std::string_view](#afee5149fbeac4c6a50345fab7b65cb07) () const — Return a std::string_view over the header name.
* `bool` [operator==](#a865c2a5b932f83a770f5e0124cddc2f2) (const BString &other) const noexcept — Compare the header name to a string.
* `bool` [operator==](#ae1e738b4c759a35a0daa89c58511f70a) (const FieldName &other) const noexcept
* `bool` [operator==](#a57627124710224a270205430bd397b0a) (const std::string_view &other) const noexcept

## Detailed Member Documentation

### `operator std::string_view()`

```cpp
BPrivate::Network::BHttpFields::FieldName::operator std::string_view()const
```

Return a `std::string_view` over the header name. 



**Returns:** A `std::string_view` object over the header name.



**Since:** Haiku R1

---

### `operator==()`

```cpp
bool BPrivate::Network::BHttpFields::FieldName::operator==(const BString & other)const
```

Compare the header name to a string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The `other` string to compare it to. |




The comparison is case-insensitive. So if this header name is set to `Content-Encoding`, comparing it to `content-encoding` will return `true`.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The current header name is equal to the *other* name. |
| false | The current header name is different from the *other* name. |





**Since:** Haiku R1

---

### `operator==()`

```cpp
bool BPrivate::Network::BHttpFields::FieldName::operator==(const FieldName & other)const
```

Compare the header name to a string.   noexcept


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The `other` string to compare it to. |




The comparison is case-insensitive. So if this header name is set to `Content-Encoding`, comparing it to `content-encoding` will return `true`.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The current header name is equal to the *other* name. |
| false | The current header name is different from the *other* name. |





**Since:** Haiku R1   noexcept

---

### `operator==()`

```cpp
bool BPrivate::Network::BHttpFields::FieldName::operator==(const std::string_view & other)const
```

Compare the header name to a string.   noexcept


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The `other` string to compare it to. |




The comparison is case-insensitive. So if this header name is set to `Content-Encoding`, comparing it to `content-encoding` will return `true`.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The current header name is equal to the *other* name. |
| false | The current header name is different from the *other* name. |





**Since:** Haiku R1   noexcept

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BHttpFields_1_1FieldName.html).
