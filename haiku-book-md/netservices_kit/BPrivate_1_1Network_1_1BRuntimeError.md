---
name: BPrivate::Network::BRuntimeError
type: class
kit: netservices_kit
brief: "Advanced error object for runtime errors"
source: haiku-book
---

# BPrivate::Network::BRuntimeError Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Advanced error object for runtime errors. 


A [BRuntimeError](classBPrivate_1_1Network_1_1BRuntimeError.md) is a concrete advanced error object that is used for errors that happen during a program's execution and that by their nature are outside of the scope of the control of the program.


Objects of this class store strings to the *origin* and the error *message*. This class can be used as an error class or as a base to create more specialized error types.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BRuntimeError](#a0fb42ac934cabe487399beb583c6dda1) (BRuntimeError &&other) noexcept — Move constructor.
* [BRuntimeError](#aa96f0c937cf2c67a2af1a499417f291b) (BString origin, BString message)
* [BRuntimeError](#a734f2754b7e03820228d3959a34fea8c) (const BRuntimeError &other) — Copy constructor.
* [BRuntimeError](#a2d766268402d65132627542cfc82182c) (const char *origin, BString message)
* [BRuntimeError](#a5e8f67a995fc117575f0876c51f01690) (const char *origin, const char *message) — Constructor for a new error object.
* `virtual const char *` Message () const noexcept override — Get a pointer to the message describing the runtime error.
* `BRuntimeError &` [operator=](#a37e3896ad28932f9695949ca50998492) (BRuntimeError &&other) noexcept — Move assignment operator.
* `BRuntimeError &` [operator=](#aaa8e285b59f980e309ca4b0b13b94462) (const BRuntimeError &other) — Copy assignment operator.
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

### `BRuntimeError()`

```cpp
BPrivate::Network::BRuntimeError::BRuntimeError(const char * origin, const char * message)
```

Constructor for a new error object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `origin` | A string representing where this error occured. It is advised to initialize it to `__PRETTY_FUNCTION__` by default. |
| `message` | A string explaining the contents for the error. While it is generally geared towards the developer, it may be useful to make the error understandable by a user, as they may sometimes see it. |





**Since:** Haiku R1

---

### `BRuntimeError()`

```cpp
BPrivate::Network::BRuntimeError::BRuntimeError(const char * origin, BString message)
```

Constructor for a new error object.  


Parameters

| Parameter | Description |
| :--- | :--- |
| `origin` | A string representing where this error occured. It is advised to initialize it to `__PRETTY_FUNCTION__` by default. |
| `message` | A string explaining the contents for the error. While it is generally geared towards the developer, it may be useful to make the error understandable by a user, as they may sometimes see it. |





**Since:** Haiku R1

---

### `BRuntimeError()`

```cpp
BPrivate::Network::BRuntimeError::BRuntimeError(BString origin, BString message)
```

Constructor for a new error object.  


Parameters

| Parameter | Description |
| :--- | :--- |
| `origin` | A string representing where this error occured. It is advised to initialize it to `__PRETTY_FUNCTION__` by default. |
| `message` | A string explaining the contents for the error. While it is generally geared towards the developer, it may be useful to make the error understandable by a user, as they may sometimes see it. |





**Since:** Haiku R1

---

### `BRuntimeError()`

```cpp
BPrivate::Network::BRuntimeError::BRuntimeError(const BRuntimeError & other)
```

Copy constructor. 



**Since:** Haiku R1

---

### `BRuntimeError()`

```cpp
BPrivate::Network::BRuntimeError::BRuntimeError(BRuntimeError && other)
```

Move constructor. 



**Since:** Haiku R1

---

### `operator=()`

```cpp
BRuntimeError & BPrivate::Network::BRuntimeError::operator=(BRuntimeError && other)
```

Move assignment operator. 



**Since:** Haiku R1

---

### `operator=()`

```cpp
BRuntimeError & BPrivate::Network::BRuntimeError::operator=(const BRuntimeError & other)
```

Copy assignment operator. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BRuntimeError.html).
