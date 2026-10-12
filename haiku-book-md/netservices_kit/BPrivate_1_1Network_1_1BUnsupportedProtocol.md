---
name: BPrivate::Network::BUnsupportedProtocol
type: class
kit: netservices_kit
brief: "Error that indicates that the protocol is not supported"
source: haiku-book
---

# BPrivate::Network::BUnsupportedProtocol Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Error that indicates that the protocol is not supported. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BUnsupportedProtocol](#af055285c0d0b05fe7c7cfa02831bd8d4) (BString origin, BUrl url, BStringList supportedProtocols)
* [BUnsupportedProtocol](#a0b532cb0a8b5ebc0ebef95a0c94c7762) (const char *origin, BUrl url, BStringList supportedProtocols) — Create a new unsupported protocol error.
* `virtual const char *` [Message](#ac332e120fd1aeab5cb44cf3704ba4841) () const noexcept override — Access the string representation of the message.
* `const BStringList &` [SupportedProtocols](#accf395baf5f143fb50f4412fe8b4f5a6) () const — A list of protocols that are supported.
* `const BUrl &` [Url](#a32b12a8c91140c3b031fc44fe64d2f9f) () const — The URL that caused the issue.
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

### `BUnsupportedProtocol()`

```cpp
BPrivate::Network::BUnsupportedProtocol::BUnsupportedProtocol(const char * origin, BUrl url, BStringList supportedProtocols)
```

Create a new unsupported protocol error. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `origin` | A string representing where this error occured. It is advised to initialize it to `__PRETTY_FUNCTION__` by default. |
| `url` | The URL object with the unsupported protocol. |
| `supportedProtocols` | A list with the supported protocols. |





**Since:** Haiku R1

---

### `BUnsupportedProtocol()`

```cpp
BPrivate::Network::BUnsupportedProtocol::BUnsupportedProtocol(BString origin, BUrl url, BStringList supportedProtocols)
```

Create a new unsupported protocol error.  


Parameters

| Parameter | Description |
| :--- | :--- |
| `origin` | A string representing where this error occured. It is advised to initialize it to `__PRETTY_FUNCTION__` by default. |
| `url` | The URL object with the unsupported protocol. |
| `supportedProtocols` | A list with the supported protocols. |





**Since:** Haiku R1

---

### `Message()`

```cpp
const char * BPrivate::Network::BUnsupportedProtocol::Message()const
```

Access the string representation of the message. 



**Since:** Haiku R1


Implements [BPrivate::Network::BError](classBPrivate_1_1Network_1_1BError.md#a2c1b049e967387a289b1b0b8694eca28).

---

### `SupportedProtocols()`

```cpp
const BStringList & BPrivate::Network::BUnsupportedProtocol::SupportedProtocols()const
```

A list of protocols that are supported. 



**Since:** Haiku R1

---

### `Url()`

```cpp
const BUrl & BPrivate::Network::BUnsupportedProtocol::Url()const
```

The URL that caused the issue. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BUnsupportedProtocol.html).
