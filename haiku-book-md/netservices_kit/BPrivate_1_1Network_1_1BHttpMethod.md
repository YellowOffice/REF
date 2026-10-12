---
name: BPrivate::Network::BHttpMethod
type: class
kit: netservices_kit
brief: "Represent a HTTP method"
source: haiku-book
---

# BPrivate::Network::BHttpMethod Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Represent a HTTP method. 


The [HTTP standard](https://datatracker.ietf.org/doc/html/rfc7231#section-4.1) specifies that HTTP requests have a method. Common methods are `GET` and `HEAD` methods. Standardized and common methods are in the form of *verbs* and are in capitalized letters from the ASCII token set, though any valid token can be used.


It is most likely that you will not use the methods of this class directly, instead you will use the implicit constructors while interacting with the [BHttpRequest](classBPrivate_1_1Network_1_1BHttpRequest.md) class.



```cpp
auto url = BUrl("https://www.haiku-os.org/");
// implicitly construct a standard get request
auto standard = BHttpRequest(url, BHttpMethod::Get);
// implicitly construct a nonstandard patch request
auto custom = BHttpRequest(url, "PATCH"sv);
```


> [!NOTE]
> When you are using the standard list of verbs, there will never be an exception when creating objects of this type. When you create a custom method, exceptions may be raised when the system runs out of memory, or when your custom method contains invalid characters. In almost all cases, you can probably safely assume you will not run into these exceptions, except for cases where you use user input to create methods or you are very defensive about memory management.



**Since:** Haiku R1

## Member List

### Classes

* `class` [InvalidMethod](#InvalidMethod) — Error that represents when a custom method does not conform to the HTTP standard.

### Public Types

* `enum` [Verb](#ga16eddbfe1a87e0c5c233416f2358e55e) { 
  Get
, 
  Head
, 
  Post
, 
  Put
, 
  Delete
, 
  Connect
, 
  Options
, 
  Trace

 } — A list of standard HTTP methods.

### Public Member Functions

* [BHttpMethod](#a1dde8f2e72bd791376a5ac52c366df6e) (BHttpMethod &&other) noexcept — Move constructor.
* [BHttpMethod](#aab95cc2c8bb0b0a454458b765e5d7c75) (const BHttpMethod &other) — Copy constructor.
* [BHttpMethod](#a4657c7a2181f6a77d981455c06f24dcf) (const std::string_view &method) — Construct a custom method.
* [BHttpMethod](#afad640b36abdaa3ce9ab2aa973745073) (Verb verb) noexcept — Construct a standard method.
* [~BHttpMethod](#a0a01b80dc314bf8802c2f80b5a5bd1f5) () — Destructor.
* `const std::string_view` [Method](#a4f8bc5715db0def42e5241b6b7618f30) () const noexcept — Get a string representation of the method.
* `bool` [operator!=](#a11140387e4a692f1656fecbaf15f7b99) (const Verb &other) const noexcept — Comparison operator.
* `BHttpMethod &` [operator=](#a69b49f84e78f00e7b8532dca8b02cac1) (BHttpMethod &&other) noexcept — Move assignment. Moves the data from the other to this object. The other object will be set to BHttpMethod::Get.
* `BHttpMethod &` [operator=](#a1a5554c8211b2cd6d730a359f6a700d6) (const BHttpMethod &other) — Copy assignment.
* `bool` [operator==](#aeebfa89b7e5f85ef5995cdc730ce40cd) (const Verb &other) const noexcept — Comparison operator.

## Detailed Member Documentation

### `BHttpMethod()`

```cpp
BPrivate::Network::BHttpMethod::BHttpMethod(Verb verb)
```

Construct a standard method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `verb` | The chosen method. |





**Since:** Haiku R1

---

### `BHttpMethod()`

```cpp
BPrivate::Network::BHttpMethod::BHttpMethod(const std::string_view & method)
```

Construct a custom method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `method` | The verb for the method. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | In case it is not possible to allocate memory for the custom string. |
| [BHttpMethod::InvalidMethod](classBPrivate_1_1Network_1_1BHttpMethod_1_1InvalidMethod.md) | In case the *method* is empty or contains invalid characters. |





**Since:** Haiku R1

---

### `BHttpMethod()`

```cpp
BPrivate::Network::BHttpMethod::BHttpMethod(const BHttpMethod & other)
```

Copy constructor. 


Copy data from an *other* object.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | When the *other* object contains a custom verb, this exception will be raised if it is impossible to allocate memory. |





**Since:** Haiku R1

---

### `BHttpMethod()`

```cpp
BPrivate::Network::BHttpMethod::BHttpMethod(BHttpMethod && other)
```

Move constructor. 


Moves the data from the *other* to this object. The *other* object will be set to [BHttpMethod::Get](classBPrivate_1_1Network_1_1BHttpMethod.md#ga16eddbfe1a87e0c5c233416f2358e55eae16d94bfc1bdba38523d7d09648f314f).



**Since:** Haiku R1

---

### `~BHttpMethod()`

```cpp
BPrivate::Network::BHttpMethod::~BHttpMethod()
```

Destructor. 



**Since:** Haiku R1

---

### `Method()`

```cpp
const std::string_view BPrivate::Network::BHttpMethod::Method()const
```

Get a string representation of the method. 



**Returns:** A `std::string_view` that is a string representation of the standard or custom method in this object. The lifetime of the string view is bound to the lifetime of this method.



**Since:** Haiku R1

---

### `operator!=()`

```cpp
bool BPrivate::Network::BHttpMethod::operator!=(const Verb & other)const
```

Comparison operator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The verb to compare to. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | This method is different from *other*. |
| false | This method is equal to *other*. |





**Since:** Haiku R1

---

### `operator=()`

```cpp
BHttpMethod & BPrivate::Network::BHttpMethod::operator=(BHttpMethod && other)
```

Move assignment. Moves the data from the *other* to this object. The *other* object will be set to [BHttpMethod::Get](classBPrivate_1_1Network_1_1BHttpMethod.md#ga16eddbfe1a87e0c5c233416f2358e55eae16d94bfc1bdba38523d7d09648f314f). 



**Since:** Haiku R1

---

### `operator=()`

```cpp
BHttpMethod & BPrivate::Network::BHttpMethod::operator=(const BHttpMethod & other)
```

Copy assignment. 


Copy data from an *other* object.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | When the *other* object contains a custom verb, this exception will be raised if it is impossible to allocate memory. |





**Since:** Haiku R1

---

### `operator==()`

```cpp
bool BPrivate::Network::BHttpMethod::operator==(const Verb & other)const
```

Comparison operator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The verb to compare to. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | This method is equal to *other*. |
| false | This method is different from *other*. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BHttpMethod.html).
