---
name: BPrivate::Network::BHttpFields
type: class
kit: netservices_kit
brief: "Represents the field section of a HTTP header"
source: haiku-book
---

# BPrivate::Network::BHttpFields Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Represents the field section of a HTTP header. 


The HTTP protocol (RFC 7230) specifies that each HTTP request and response has a header. Part of that header is a list of fields, which are name and value pairs. The high level protocol defines what valid field names and field values look like. When adding or modifying field data, the members of this class enforce those constraints.


When you are processing a HTTP response, this object gives you the methods to query the headers in that response. When you are creating a HTTP request, this object gives you methods to add and modify header fields on your request. When retrieving data from the header fields, this data is often returned as an `std::string_view`. Please note that this object will only point to valid data for the lifetime of this object, which in case of a HTTP response, will be bound to the lifetime of the object that contains the HTTP response.


When adding headers, the fields are stored in the order in which they were added. You can use [AddField()](classBPrivate_1_1Network_1_1BHttpFields.md#af5d450e33dba0b759f27ac61624575d2) to add more than one field with the same key.


The HTTP protocol does not prohibit multiple fields with the same name, but it does note that semantically this is only allowed for a limited set of explicitly named headers, like the 'Set-Cookie' field (see RFC 7230 section 3.2.2). Because most header fields will only exist once, the interface of this class is optimized for each header field existing only once. The onus is on the user to take additional steps when dealing with header fields that they know can occur more than once.



**Since:** Haiku R1

## Member List

### Classes

* `class` [Field](#Field) — Represents a HTTP header field.
* `class` [FieldName](#FieldName) — Representation of a HTTP header name.
* `class` [InvalidInput](#InvalidInput) — Error that represents when a string input contains characters that are incompatible with the HTTP specification.

### Public Types

* `using` [ConstIterator](#aace9e798caa59506b3fa1f763c055a8f) = std::list< Field >::const_iterator — Define a constant iterator to iterate through the list of header fields.

### Public Member Functions

* [BHttpFields](#a97dab78d985884bf1a98cbb99b0e9eaa) () — Construct an empty list of HTTP header fields.
* [BHttpFields](#a87984a2703edbe514ac18162800f6e95) (std::initializer_list< Field > fields) — Initialize the object with a list of fields.
* [BHttpFields](#a8c22cef3f56f8e86d94d84f8930efd92) (const BHttpFields &other) — Copy constructor.
* [BHttpFields](#a042678f30d9ebd62b0d8886658a2596a) (BHttpFields &&other) — Move constructor.
* [~BHttpFields](#a84d6349162ab618171094fc6c8ce95ce) () noexcept — Destructor.
* `BHttpFields &` [operator=](#a102e16df1dbd3e2a354cb80d83a1d12b) (const BHttpFields &) — Copy assignment operator.
* `BHttpFields &` [operator=](#a8a6da5ad61f5b2da5c913a85a3b2768f) (BHttpFields &&) noexcept — Move assignment operator.
* `const Field &` [operator[]](#a7db3f3143adc608e1aa32496837d9a23) (size_t index) const — Get the item at an index.
* `void` [AddField](#af5d450e33dba0b759f27ac61624575d2) (const std::string_view &name, const std::string_view &value) — Append a field with name and a value to the list of headers.
* `void` [AddField](#a907539c02ecf4fd477cd452b131e2f20) (BString &field) — Append a field from the raw field line.
* `void` [AddFields](#a074c575ebfa84c49b19140605346932d) (std::initializer_list< Field > fields) — Add a list of fields.
* `void` [RemoveField](#a1dde58dbec6a291046ea3329960378fb) (const std::string_view &name) noexcept — Remove all fields with the name.
* `void` [RemoveField](#ace0b24d647ff93ac673c3351bcf742ec) (ConstIterator it) noexcept — Remove the specific field at the location of an iterator.
* `void` [MakeEmpty](#a98e63d61dd4fd26b452101dafb90bffd) () noexcept — Clear all fields from this header.
* `ConstIterator` [FindField](#a6dc1750db7e303f87d025812920541bd) (const std::string_view &name) const noexcept — Find a field with name.
* `size_t` [CountFields](#a43e0109e4958caec53aea425625f4d70) () const noexcept — Get the number of fields.
* `size_t` [CountFields](#a2943b6398fe8a80d2172a9eadca9dd9e) (const std::string_view &name) const noexcept — Cound the number of fields that have this name.
* `ConstIterator` [begin](#aea54668280d09020d17d8f1dbbba1047) () const noexcept — Return an iterator to the first field.
* `ConstIterator` [end](#a763fea9be7bdc49f11cc045aaafbeee9) () const noexcept — Return an iterator to the end of the fields.

## Detailed Member Documentation

### `ConstIterator`

```cpp
BPrivate::Network::BHttpFields::ConstIterator
```

Define a constant iterator to iterate through the list of header fields. 


This iterator has the same semantics as other constant iterators in the C++ standard library.



**Since:** Haiku R1

---

### `BHttpFields()`

```cpp
BPrivate::Network::BHttpFields::BHttpFields()
```

Construct an empty list of HTTP header fields. 


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | Error in case memory cannot be allocated. |





**Since:** Haiku R1

---

### `BHttpFields()`

```cpp
BPrivate::Network::BHttpFields::BHttpFields(std::initializer_list< Field > fields)
```

Initialize the object with a list of fields. 


This enables you to initialize the fields with a list of [BHttpFields::Field](classBPrivate_1_1Network_1_1BHttpFields_1_1Field.md) objects. Any empty fields will be skipped. Like [AddField()](classBPrivate_1_1Network_1_1BHttpFields.md#af5d450e33dba0b759f27ac61624575d2), this constructor keeps the fields in the original order.


The example below will create an object with four fields, even though five fields have been passed in the initializer. The two `Accept-Encoding` will be added in this order, even though the HTTP specification does not explicitly allow this.



```cpp
const BHttpFields defaultFields = {
    {"Host"sv, "haiku-os.org"sv},
    {"Accept-Encoding"sv, "gzip"sv}
    {"Accept"sv, "*\/*"sv},
    {},
    {"Accept-Encoding"sv, "bzip2"sv}
};
```

Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | Error in case memory cannot be allocated. |
| [BHttpFields::InvalidInput](classBPrivate_1_1Network_1_1BHttpFields_1_1InvalidInput.md) | This error indicates that some of the names or values in the list do not adhere to the HTTP specification. |





**Since:** Haiku R1

---

### `BHttpFields()`

```cpp
BPrivate::Network::BHttpFields::BHttpFields(const BHttpFields & other)
```

Copy constructor. 


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | Error in case memory cannot be allocated. |





**Since:** Haiku R1

---

### `BHttpFields()`

```cpp
BPrivate::Network::BHttpFields::BHttpFields(BHttpFields && other)
```

Move constructor. 


The name and value from the *other* fields object will be moved to this object. The *other* object will be empty, meaning it no longer has any fields.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | Error in case memory cannot be allocated. |





**Since:** Haiku R1

---

### `~BHttpFields()`

```cpp
BPrivate::Network::BHttpFields::~BHttpFields()
```

Destructor. 



**Since:** Haiku R1

---

### `AddField()`

```cpp
void BPrivate::Network::BHttpFields::AddField(BString & field)
```

Append a field from the raw *field* line. 


The raw header field is checked to determine whether it corresponds to the the HTTP specification. Note that the raw field should not include any newline characters at the end of the string.


If succesful, the string is moved into the fields object, and the original input value will be empty.


Parameters

| Parameter | Description |
| :--- | :--- |
| `field` | The raw header field to move into the list of headers. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | Error in case memory cannot be allocated. |
| [BHttpFields::InvalidInput](classBPrivate_1_1Network_1_1BHttpFields_1_1InvalidInput.md) | This error indicates that the *name* or the *value* is empty or contains invalid characters. |





**Since:** Haiku R1

---

### `AddField()`

```cpp
void BPrivate::Network::BHttpFields::AddField(const std::string_view & name, const std::string_view & value)
```

Append a field with *name* and a *value* to the list of headers. 


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
| [BHttpFields::InvalidInput](classBPrivate_1_1Network_1_1BHttpFields_1_1InvalidInput.md) | This error indicates that the *name* or the *value* contains invalid characters. |





**Since:** Haiku R1

---

### `AddFields()`

```cpp
void BPrivate::Network::BHttpFields::AddFields(std::initializer_list< Field > fields)
```

Add a list of fields. 


This enables you to add a list of [BHttpFields::Field](classBPrivate_1_1Network_1_1BHttpFields_1_1Field.md) objects. Like [AddField()](classBPrivate_1_1Network_1_1BHttpFields.md#af5d450e33dba0b759f27ac61624575d2), the fields are added in the the original order.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | Error in case memory cannot be allocated. |
| [BHttpFields::InvalidInput](classBPrivate_1_1Network_1_1BHttpFields_1_1InvalidInput.md) | This error indicates that some of the names or values in the list do not adhere to the HTTP specification. |





**Since:** Haiku R1

---

### `begin()`

```cpp
ConstIterator BPrivate::Network::BHttpFields::begin()const
```

Return an iterator to the first field. 



**Since:** Haiku R1

---

### `CountFields()`

```cpp
size_t BPrivate::Network::BHttpFields::CountFields()const
```

Get the number of fields. 



**Returns:** The number of fields in this container. If multiple fields have the same name, they will be counted individually.



**Since:** Haiku R1

---

### `CountFields()`

```cpp
size_t BPrivate::Network::BHttpFields::CountFields(const std::string_view & name)const
```

Cound the number of fields that have this *name*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the field you are looking for. Name matching will be done case insensitively. |





**Returns:** The number of field with the *name*.



**Since:** Haiku R1

---

### `end()`

```cpp
ConstIterator BPrivate::Network::BHttpFields::end()const
```

Return an iterator to the end of the fields. 



**Since:** Haiku R1

---

### `FindField()`

```cpp
ConstIterator BPrivate::Network::BHttpFields::FindField(const std::string_view & name)const
```

Find a field with *name*. 


In case there are more than one fields with the same name, you cannot use this method to find all instances, and you should iterate through the fields instead.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the field to be found. |





**Returns:** Returns a valid iterator to the first field with *name* in this container, or [BHttpFields::end()](classBPrivate_1_1Network_1_1BHttpFields.md#a763fea9be7bdc49f11cc045aaafbeee9) in case the name is not found.



**Since:** Haiku R1

---

### `MakeEmpty()`

```cpp
void BPrivate::Network::BHttpFields::MakeEmpty()
```

Clear all fields from this header. 


Removes all fields from the container.



**Since:** Haiku R1

---

### `operator=()`

```cpp
BHttpFields & BPrivate::Network::BHttpFields::operator=(BHttpFields && other)
```

Move assignment operator. 


The name and value from the *other* fields object will be moved to this object. The *other* object will be empty, meaning it no longer has any fields.



**Since:** Haiku R1

---

### `operator=()`

```cpp
BHttpFields & BPrivate::Network::BHttpFields::operator=(const BHttpFields & other)
```

Copy assignment operator. 


Make a new fields object with a copy of the fields of the *other* header.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | Error in case memory cannot be allocated. |





**Since:** Haiku R1

---

### `operator[]()`

```cpp
const Field & BPrivate::Network::BHttpFields::operator[](size_t index)const
```

Get the item at an *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The zero-based index of the item in the list of fields. |





**Returns:** A const reference to the the field.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| [BRuntimeError](classBPrivate_1_1Network_1_1BRuntimeError.md) | Error in case the index is out of bounds. |





**Since:** Haiku R1

---

### `RemoveField()`

```cpp
void BPrivate::Network::BHttpFields::RemoveField(const std::string_view & name)
```

Remove all fields with the *name*. 


If there are no fields with this name, this method does nothing. Like all operations that involve a field name, the name matching is case insensitive.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the field to remove. |





**Since:** Haiku R1

---

### `RemoveField()`

```cpp
void BPrivate::Network::BHttpFields::RemoveField(ConstIterator it)
```

Remove the specific field at the location of an iterator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `it` | A valid iterator to the item that must be removed. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BHttpFields.html).
