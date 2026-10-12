---
name: BPrivate::Network::BHttpMethod::InvalidMethod
type: class
kit: netservices_kit
brief: "Error that represents when a custom method does not conform to the HTTP standard"
source: haiku-book
---

# BPrivate::Network::BHttpMethod::InvalidMethod Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Error that represents when a custom method does not conform to the HTTP standard. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [InvalidMethod](#afc0bc1a17c8dcd2c67e280b709566cda) (const char *origin, BString input) — Constructor that sets the origin and the invalid input.
* `virtual BString` [DebugMessage](#a7f52e4d68de0f5735b223e78f3ac4b67) () const override — Retrieve a debug message that contains all info in this error.
* `virtual const char *` [Message](#a397e87c6134ba1a25488ad781519016e) () const noexcept override — Access the string representation of the message.
* [BError](#a227208ede157ae501ea3acee188e46b7) (BError &&error) noexcept — Move constructor.
* [BError](#abbf80a044f5af02aac87a65a6aba703a) (BString origin) — Constructor that sets the origin.
* [BError](#abf7e40af168fdcf53eb7a86e42c9141c) (const BError &error) — Copy constructor.
* [BError](#a98953038abdab68796b3bf373ead0540) (const char *origin) — Constructor that sets the origin.
* `virtual` [~BError](#a0ffdd9cc030c188df03dd95e1de82bf4) () noexcept — Standard destructor.
* `virtual BString` [DebugMessage](#a93a2260671aad699aa8787fd74061f98) () const — Retrieve a debug message that contains all info in this error.
* `virtual const char *` [Message](#a2c1b049e967387a289b1b0b8694eca28) () const noexcept=0 — Access the string representation of the message.
* `BError &` [operator=](#ab80467e8f9af8142d4d7cfa311f04c68) (BError &&error) noexcept — Move assignment operator.
* `BError &` [operator=](#af4a889a39e9530458aeb649d2ba12d45) (const BError &error) — Copy assignment operator.
* `virtual const char *` [Origin](#a63dedfb711a141621fa266fb25bff2d8) () const noexcept — Access the string representation of the origin of the error.
* `size_t` [WriteToOutput](#a69a0b83a56c08e510e16aaba841f25e5) (BDataIO *output) const — Write the error description to an output.
* `void` [WriteToStream](#a2c7538bd21c2844cd1ee0c8ee0ba74ef) (std::ostream &stream) const — Write the error description to an output stream.

### Public Attributes

* `BString` [input](#aecc3243315602e5ab9c7095f47827108) — The input that contains the invalid contents.

## Detailed Member Documentation

### `InvalidMethod()`

```cpp
BPrivate::Network::BHttpMethod::InvalidMethod::InvalidMethod(const char * origin, BString input)
```

Constructor that sets the *origin* and the invalid *input*. 



**Since:** Haiku R1

---

### `DebugMessage()`

```cpp
virtual BString BPrivate::Network::BHttpMethod::InvalidMethod::DebugMessage()const
```

Retrieve a debug message that contains all info in this error. 



```cpp
[Origin] Message of error
```

Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | In the future this method may throw this exception when the memory for the debug message cannot be allocated. |





**Returns:** A [BString](../support_kit/classBString.md) object that contains the debug message.



**Since:** Haiku R1


Reimplemented from [BPrivate::Network::BError](classBPrivate_1_1Network_1_1BError.md#a93a2260671aad699aa8787fd74061f98).

---

### `Message()`

```cpp
virtual const char * BPrivate::Network::BHttpMethod::InvalidMethod::Message()const
```

Access the string representation of the message. 


Implementations should return a meaningful description of the error that occured. The primary target audience of these messages are developers, who (hopefully) see them during development, testing or in bug reports. However, if it makes sense to have the error messages be instructive to users too, then do not hesitate to do so.


Implementations of this function should never return `NULL`.



**Since:** Haiku R1


Implements [BPrivate::Network::BError](classBPrivate_1_1Network_1_1BError.md#a2c1b049e967387a289b1b0b8694eca28).

---

### `input`

```cpp
BString BPrivate::Network::BHttpMethod::InvalidMethod::input
```

The input that contains the invalid contents. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BHttpMethod_1_1InvalidMethod.html).
