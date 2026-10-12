---
name: BPrivate::Network::BBorrowError
type: class
kit: netservices_kit
brief: "Error while handling a BExclusiveBorrow or BBorrow object"
source: haiku-book
---

# BPrivate::Network::BBorrowError Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Error while handling a [BExclusiveBorrow](classBPrivate_1_1Network_1_1BExclusiveBorrow.md) or [BBorrow](classBPrivate_1_1Network_1_1BBorrow.md) object. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BBorrowError](#a6665ec7cb127940b181dcb21aed49cc5) (const char *origin) — Constructor that sets the origin.
* `virtual const char *` [Message](#ac73f39c13681c993028f9c92ba654ffd) () const noexcept override — Get a pointer to the message describing the borrow error.
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

## Detailed Member Documentation

### `BBorrowError()`

```cpp
BPrivate::Network::BBorrowError::BBorrowError(const char * origin)
```

Constructor that sets the *origin*. 



**Since:** Haiku R1

---

### `Message()`

```cpp
const char * BPrivate::Network::BBorrowError::Message()const
```

Get a pointer to the message describing the borrow error. 



**Since:** Haiku R1


Implements [BPrivate::Network::BError](classBPrivate_1_1Network_1_1BError.md#a2c1b049e967387a289b1b0b8694eca28).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BBorrowError.html).
