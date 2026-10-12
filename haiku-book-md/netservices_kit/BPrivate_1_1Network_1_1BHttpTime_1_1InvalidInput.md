---
name: BPrivate::Network::BHttpTime::InvalidInput
type: class
kit: netservices_kit
brief: "Error that indicates that a string cannot be parsed as a valid HTTP timestamp"
source: haiku-book
---

# BPrivate::Network::BHttpTime::InvalidInput Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Error that indicates that a string cannot be parsed as a valid HTTP timestamp. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [InvalidInput](#ae2940286e9e179ffe4b03d2a613a64af) (const char *origin, BString input) — Constructor that sets the origin and the invalid input.
* `virtual BString` [DebugMessage](#a39203d08c6694acce04af2a6cfc5726e) () const override — Retrieve a debug message that contains all info in this error.
* `virtual const char *` [Message](#a9b89f597f4628bf70778d61d524549d2) () const noexcept override — Access the string representation of the message.
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

* `BString` [input](#a01107e56bc8583b21e5860e731dab451) — Copy of the original timestamp that could not be parsed.

## Detailed Member Documentation

### `InvalidInput()`

```cpp
BPrivate::Network::BHttpTime::InvalidInput::InvalidInput(const char * origin, BString input)
```

Constructor that sets the *origin* and the invalid *input*. 



**Since:** Haiku R1

---

### `DebugMessage()`

```cpp
virtual BString BPrivate::Network::BHttpTime::InvalidInput::DebugMessage()const
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
virtual const char * BPrivate::Network::BHttpTime::InvalidInput::Message()const
```

Access the string representation of the message. 


Implementations should return a meaningful description of the error that occured. The primary target audience of these messages are developers, who (hopefully) see them during development, testing or in bug reports. However, if it makes sense to have the error messages be instructive to users too, then do not hesitate to do so.


Implementations of this function should never return `NULL`.



**Since:** Haiku R1


Implements [BPrivate::Network::BError](classBPrivate_1_1Network_1_1BError.md#a2c1b049e967387a289b1b0b8694eca28).

---

### `input`

```cpp
BString BPrivate::Network::BHttpTime::InvalidInput::input
```

Copy of the original timestamp that could not be parsed. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BHttpTime_1_1InvalidInput.html).
