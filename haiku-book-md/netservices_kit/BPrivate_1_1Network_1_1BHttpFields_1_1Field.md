---
name: BPrivate::Network::BHttpFields::Field
type: class
kit: netservices_kit
brief: "Represents a HTTP header field"
source: haiku-book
---

# BPrivate::Network::BHttpFields::Field Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Represents a HTTP header field. 


This type represents a combination of a field name and a field value. In order to be used in a HTTP header, each object must contain data that is in compliance with the HTTP specification (RFC 7230).


Some official HTTP specifications give additional guidelines for how to interpret specific fields. This class, however, does not supply any additional parsing for those specializations.


Manipulation of the contents of a HTTP field will in most cases be done through the interface of the [BHttpFields](classBPrivate_1_1Network_1_1BHttpFields.md) object that owns this field.


This type has a special 'empty' state. This means that they do not have a key and value. Empty objects only come into existence when explicitly instantiated with the constructor with no arguments, or after the contents has been moved to another object. Empty objects cannot be added to [BHttpFields](classBPrivate_1_1Network_1_1BHttpFields.md) objets. You do not have to check for empty fields when working with fields coming from [BHttpFields](classBPrivate_1_1Network_1_1BHttpFields.md) objects.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [Field](#abc673300d40154b52ba357c84feee066) () noexcept — Construct empty field.
* [Field](#a5708e4773bf198e6a5ae4880959df9ec) (BString &field) — Construct a field from the raw field value.
* [Field](#a93f8f1a7356364e8e82270d21e186b34) (const Field &other) — Copy constructor.
* [Field](#a868062bb06799fc560b4369e52dcb45d) (const std::string_view &name, const std::string_view &value) — Construct a field with a name and a value.
* [Field](#aadec28092fdd68929d84df8d5eed8279) (Field &&) noexcept — Move constructor.
* `bool` [IsEmpty](#ae601531fc2ce05efb96bda88d4b10368) () const noexcept — Check if the field is empty or has valid data.
* `const FieldName &` [Name](#af15525b6622bb20ec9042d3f0819a0b2) () const noexcept — Get a const reference to the field name.
* `Field &` [operator=](#abf1b3bd840a943d2c4488cd66058ccc6) (const Field &other) — Copy assignment.
* `Field &` [operator=](#aba528215b4a166ecba57bf574626352d) (Field &&other) noexcept — Move assignment.
* `std::string_view` [RawField](#a735bfb608950414690e81876347ff9dc) () const noexcept — Get a view to the field value.
* `std::string_view` [Value](#a9235f0ccfa2db5a085a8db532c33a022) () const noexcept — Get a const reference to the field value.

## Detailed Member Documentation

### `Field()`

```cpp
BPrivate::Network::BHttpFields::Field::Field()
```

Construct empty field. 


This constructs an empty field. Because empty fields cannot be used in combination with a [BHttpFields](classBPrivate_1_1Network_1_1BHttpFields.md) object, it is unlikely that you will construct these empty fields yourself.



**Since:** Haiku R1

---

### `Field()`

```cpp
BPrivate::Network::BHttpFields::Field::Field(const std::string_view & name, const std::string_view & value)
```

Construct a field with a *name* and a *value*. 


The parameters are checked whether they only contain characters that are allowed by the HTTP specification.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the header field. |
| `value` | The value of the header field. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | Error in case memory cannot be allocated. |
| [BHttpFields::InvalidInput](classBPrivate_1_1Network_1_1BHttpFields_1_1InvalidInput.md) | This error indicates that the *name* or the *value* is empty or contains invalid characters. |





**Since:** Haiku R1

---

### `Field()`

```cpp
BPrivate::Network::BHttpFields::Field::Field(BString & field)
```

Construct a field from the raw *field* value. 


The raw header field is checked to determine whether it corresponds to the the HTTP specification. Note that the raw field should not include any newline characters at the end of the string.


If succesful, the string is moved into the fields object, and the original input value will be empty.


Parameters

| Parameter | Description |
| :--- | :--- |
| `field` | The raw header field to move into the list of headers |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | Error in case memory cannot be allocated. |
| [BHttpFields::InvalidInput](classBPrivate_1_1Network_1_1BHttpFields_1_1InvalidInput.md) | This error indicates that the *name* or the *value* is empty or contains invalid characters. |





**Since:** Haiku R1

---

### `Field()`

```cpp
BPrivate::Network::BHttpFields::Field::Field(const Field & other)
```

Copy constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The other field to copy data from. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | Error in case memory cannot be allocated. |





**Since:** Haiku R1

---

### `Field()`

```cpp
BPrivate::Network::BHttpFields::Field::Field(Field && other)
```

Move constructor. 


After moving, the *other* field object will be an empty field.



**Since:** Haiku R1

---

### `IsEmpty()`

```cpp
bool BPrivate::Network::BHttpFields::Field::IsEmpty()const
```

Check if the field is empty or has valid data. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | This field is empty. |
| false | This field contains a valid name and value. |





**Since:** Haiku R1

---

### `Name()`

```cpp
const FieldName & BPrivate::Network::BHttpFields::Field::Name()const
```

Get a const reference to the field name. 



**Returns:** The name of the field as a [BHttpFields::FieldName](classBPrivate_1_1Network_1_1BHttpFields_1_1FieldName.md).



**Since:** Haiku R1

---

### `operator=()`

```cpp
Field & BPrivate::Network::BHttpFields::Field::operator=(const Field & other)
```

Copy assignment. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The other field to copy data from. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | Error in case memory cannot be allocated. |





**Since:** Haiku R1

---

### `operator=()`

```cpp
Field & BPrivate::Network::BHttpFields::Field::operator=(Field && other)
```

Move assignment. 


After moving, the *other* field object will be an empty field.



**Since:** Haiku R1

---

### `RawField()`

```cpp
std::string_view BPrivate::Network::BHttpFields::Field::RawField()const
```

Get a view to the field value. 



**Returns:** The raw field value as a `string_view`. The raw value does not include the line ending (\r\n).



**Since:** Haiku R1

---

### `Value()`

```cpp
std::string_view BPrivate::Network::BHttpFields::Field::Value()const
```

Get a const reference to the field value. 



**Returns:** The contents of the field value as a `std::string_view`.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BHttpFields_1_1Field.html).
