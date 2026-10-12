---
name: BPrivate::Network::BHttpFields::InvalidInput
type: class
kit: netservices_kit
brief: "Error that represents when a string input contains characters that are incompatible with the HTTP specification"
source: haiku-book
---

# BPrivate::Network::BHttpFields::InvalidInput Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Error that represents when a string input contains characters that are incompatible with the HTTP specification. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [InvalidInput](#a2d084b070375ae89f538ec5f8c08b0ea) (const char *origin, BString input) — Constructor that sets the origin and the invalid input.
* `virtual BString` [DebugMessage](#afb2156182ef6be328515b94733ec4bf2) () const override — Retrieve a debug message that contains all info in this error.
* `virtual const char *` [Message](#a35b8bd69f9464a25407e1f1e5346db6a) () const noexcept override — Get a pointer to the message describing the error.
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

* `BString` [input](#a1100da56c1211cb526fb82fdfb8e8e97) — The input that contains the invalid contents.

## Detailed Member Documentation

### `InvalidInput()`

```cpp
BPrivate::Network::BHttpFields::InvalidInput::InvalidInput(const char * origin, BString input)
```

Constructor that sets the *origin* and the invalid *input*. 



**Since:** Haiku R1

---

### `DebugMessage()`

```cpp
BString BPrivate::Network::BHttpFields::InvalidInput::DebugMessage()const
```

Retrieve a debug message that contains all info in this error. 


The output will be along the lines of: 


```cpp
[Origin] Invalid format or unsupported characters in input    [input]
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
const char * BPrivate::Network::BHttpFields::InvalidInput::Message()const
```

Get a pointer to the message describing the error. 



**Since:** Haiku R1


Implements [BPrivate::Network::BError](classBPrivate_1_1Network_1_1BError.md#a2c1b049e967387a289b1b0b8694eca28).

---

### `input`

```cpp
BString BPrivate::Network::BHttpFields::InvalidInput::input
```

The input that contains the invalid contents. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BHttpFields_1_1InvalidInput.html).
