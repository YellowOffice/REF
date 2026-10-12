---
name: BPrivate::Network::BSystemError
type: class
kit: netservices_kit
brief: "Advanced error object that wrap low-level system errors"
source: haiku-book
---

# BPrivate::Network::BSystemError Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Advanced error object that wrap low-level system errors. 


A [BSystemError](classBPrivate_1_1Network_1_1BSystemError.md) is a concrete advanced error object that is used to wrap tradition errors that are usually returned as a `status_t`. This type takes the system error, and adds an *origin* specifier.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BSystemError](#a1a853245bf93930f04ce77558dbaab02) (BString origin, status_t error)
* [BSystemError](#a9b8aa2aca2b7611a6604a92e78590530) (BSystemError &&other) noexcept — Move constructor.
* [BSystemError](#a7c5ee29ff40fd1fb4ff6920123a938a5) (const BSystemError &other) — Copy constructor.
* [BSystemError](#acced9d1ba62658f42b75ad859821dba8) (const char *origin, status_t error) — Create an object for error code with a specified origin.
* `virtual BString` [DebugMessage](#a5ee62b6ae8191453274a93c3e9d00b36) () const override — Retrieve a debug message that contains all info in this error.
* `status_t` [Error](#aebbcce59d40e011f63c3373eda58c308) () noexcept — Get the error code for this error.
* `virtual const char *` [Message](#ad4c1783170eebdd85479aaca28519565) () const noexcept override — Access the string representation of the message.
* `BSystemError &` [operator=](#afbea1db67adc272ed7aec51f7894bd1a) (BSystemError &&other) noexcept — Move assignment operator.
* `BSystemError &` [operator=](#a8b049f6e3e0683e0658f295a5176c604) (const BSystemError &other) — Copy assignment.
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

### `BSystemError()`

```cpp
BPrivate::Network::BSystemError::BSystemError(const char * origin, status_t error)
```

Create an object for *error* code with a specified *origin*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `origin` | A string representing where this error occured. As this object usually wraps around a lower level API call, this should usually be the call that the error code originated from. |
| `error` | The error code. |





**Since:** Haiku R1

---

### `BSystemError()`

```cpp
BPrivate::Network::BSystemError::BSystemError(BString origin, status_t error)
```

Create an object for *error* code with a specified *origin*.  


Parameters

| Parameter | Description |
| :--- | :--- |
| `origin` | A string representing where this error occured. As this object usually wraps around a lower level API call, this should usually be the call that the error code originated from. |
| `error` | The error code. |





**Since:** Haiku R1

---

### `BSystemError()`

```cpp
BPrivate::Network::BSystemError::BSystemError(const BSystemError & other)
```

Copy constructor. 



**Since:** Haiku R1

---

### `BSystemError()`

```cpp
BPrivate::Network::BSystemError::BSystemError(BSystemError && other)
```

Move constructor. 



**Since:** Haiku R1

---

### `DebugMessage()`

```cpp
BString BPrivate::Network::BSystemError::DebugMessage()const
```

Retrieve a debug message that contains all info in this error. 



```cpp
[Origin] Message of error (error code)
```

Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | In the future this method may throw this exception when the memory for the debug message cannot be allocated. |





**Returns:** A [BString](../support_kit/classBString.md) object that contains the debug message.



**Since:** Haiku R1


Reimplemented from [BPrivate::Network::BError](classBPrivate_1_1Network_1_1BError.md#a93a2260671aad699aa8787fd74061f98).

---

### `Error()`

```cpp
status_t BPrivate::Network::BSystemError::Error()
```

Get the error code for this error. 



**Since:** Haiku R1

---

### `Message()`

```cpp
const char * BPrivate::Network::BSystemError::Message()const
```

Access the string representation of the message. 


This returns the value of `strerror()` for the error code.



**Since:** Haiku R1


Implements [BPrivate::Network::BError](classBPrivate_1_1Network_1_1BError.md#a2c1b049e967387a289b1b0b8694eca28).

---

### `operator=()`

```cpp
BSystemError & BPrivate::Network::BSystemError::operator=(BSystemError && other)
```

Move assignment operator. 



**Since:** Haiku R1

---

### `operator=()`

```cpp
BSystemError & BPrivate::Network::BSystemError::operator=(const BSystemError & other)
```

Copy assignment. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BSystemError.html).
