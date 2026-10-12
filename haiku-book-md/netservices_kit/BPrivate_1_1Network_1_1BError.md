---
name: BPrivate::Network::BError
type: class
kit: netservices_kit
brief: "Abstract base class for advanced error objects"
source: haiku-book
---

# BPrivate::Network::BError Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Abstract base class for advanced error objects. 


This class defines the minimum interface for advanced error objects in modern parts of the Haiku API.


The minimum definition of an error is that it contains an *origin* and a *message*. The origin should contain a string that helps a developer identify the origin of the error. Common practise is to pass the `__PRETTY_FUNCTION__` from the place where the error is constructed, but subclasses can have their own definitions for the origin.


The message is a freeform message that describes the exact error condition. While it is not meant as a user-facing message, when creating custom error objects, take into account that a user may be confronted with a message in situations where an application presents it to a user as a final resort.



> [!NOTE]
> The advanced error objects are not used in the existing legacy Haiku Kits. They are being tested for use in the modern parts of the API and are therefore included in the network services kit.



**Since:** Haiku R1

## Member List

### Public Member Functions

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

### `BError()`

```cpp
BPrivate::Network::BError::BError(const char * error)
```

Constructor that sets the *origin*. 



**Since:** Haiku R1

---

### `BError()`

```cpp
BPrivate::Network::BError::BError(BString origin)
```

Constructor that sets the *origin*. 



**Since:** Haiku R1

---

### `~BError()`

```cpp
BPrivate::Network::BError::~BError()
```

Standard destructor. 



**Since:** Haiku R1

---

### `BError()`

```cpp
BPrivate::Network::BError::BError(const BError & other)
```

Copy constructor. 



**Since:** Haiku R1

---

### `BError()`

```cpp
BPrivate::Network::BError::BError(BError && other)
```

Move constructor. 



**Since:** Haiku R1

---

### `DebugMessage()`

```cpp
virtual BString BPrivate::Network::BError::DebugMessage()const
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


Reimplemented in [BPrivate::Network::BSystemError](classBPrivate_1_1Network_1_1BSystemError.md#a5ee62b6ae8191453274a93c3e9d00b36), [BPrivate::Network::BHttpFields::InvalidInput](classBPrivate_1_1Network_1_1BHttpFields_1_1InvalidInput.md#afb2156182ef6be328515b94733ec4bf2), [BPrivate::Network::BHttpMethod::InvalidMethod](classBPrivate_1_1Network_1_1BHttpMethod_1_1InvalidMethod.md#a7f52e4d68de0f5735b223e78f3ac4b67), [BPrivate::Network::BHttpTime::InvalidInput](classBPrivate_1_1Network_1_1BHttpTime_1_1InvalidInput.md#a39203d08c6694acce04af2a6cfc5726e), and [BPrivate::Network::BNetworkRequestError](classBPrivate_1_1Network_1_1BNetworkRequestError.md#a038e30d1d5fcaac6a48c6b8281b5b110).

---

### `Message()`

```cpp
const char * BPrivate::Network::BError::Message()const
```

Access the string representation of the message. 


Implementations should return a meaningful description of the error that occured. The primary target audience of these messages are developers, who (hopefully) see them during development, testing or in bug reports. However, if it makes sense to have the error messages be instructive to users too, then do not hesitate to do so.


Implementations of this function should never return `NULL`.



**Since:** Haiku R1


Implemented in [BPrivate::Network::BRuntimeError](classBPrivate_1_1Network_1_1BRuntimeError.md#a6a164c6533818d2bb23d099e45dfc837), [BPrivate::Network::BSystemError](classBPrivate_1_1Network_1_1BSystemError.md#ad4c1783170eebdd85479aaca28519565), [BPrivate::Network::BBorrowError](classBPrivate_1_1Network_1_1BBorrowError.md#ac73f39c13681c993028f9c92ba654ffd), [BPrivate::Network::BHttpFields::InvalidInput](classBPrivate_1_1Network_1_1BHttpFields_1_1InvalidInput.md#a35b8bd69f9464a25407e1f1e5346db6a), [BPrivate::Network::BHttpMethod::InvalidMethod](classBPrivate_1_1Network_1_1BHttpMethod_1_1InvalidMethod.md#a397e87c6134ba1a25488ad781519016e), [BPrivate::Network::BHttpTime::InvalidInput](classBPrivate_1_1Network_1_1BHttpTime_1_1InvalidInput.md#a9b89f597f4628bf70778d61d524549d2), [BPrivate::Network::BUnsupportedProtocol](classBPrivate_1_1Network_1_1BUnsupportedProtocol.md#ac332e120fd1aeab5cb44cf3704ba4841), [BPrivate::Network::BInvalidUrl](classBPrivate_1_1Network_1_1BInvalidUrl.md#a68f2c421e5cfca9d7102257459602e23), and [BPrivate::Network::BNetworkRequestError](classBPrivate_1_1Network_1_1BNetworkRequestError.md#aca0ab9afcc80043409a087da5a784508).

---

### `operator=()`

```cpp
BError & BPrivate::Network::BError::operator=(BError && other)
```

Move assignment operator. 



**Since:** Haiku R1

---

### `operator=()`

```cpp
BError & BPrivate::Network::BError::operator=(const BError & other)
```

Copy assignment operator. 



**Since:** Haiku R1

---

### `Origin()`

```cpp
const char * BPrivate::Network::BError::Origin()const
```

Access the string representation of the origin of the error. 


The default implementation returns a pointer to the string that was set as the origin when this object was constructed.


Implementations of this function should never return `NULL`.



**Since:** Haiku R1

---

### `WriteToOutput()`

```cpp
size_t BPrivate::Network::BError::WriteToOutput(BDataIO * output)const
```

Write the error description to an output. 


The default implementation will use the output from [DebugMessage()](classBPrivate_1_1Network_1_1BError.md#a93a2260671aad699aa8787fd74061f98) and write it to the *output*, including a newline and the NUL that terminates the string.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| [BSystemError](classBPrivate_1_1Network_1_1BSystemError.md) | For any error that occurs when calling [BDataIO::Write()](../support_kit/classBDataIO.md#a01692303eba7601c6a7cfa72c06d6afb) |





**Returns:** The number of bytes that was written to *output*.



**Since:** Haiku R1

---

### `WriteToStream()`

```cpp
void BPrivate::Network::BError::WriteToStream(std::ostream & stream)const
```

Write the error description to an output stream. 


The default implementation will write the output of the [DebugMessage()](classBPrivate_1_1Network_1_1BError.md#a93a2260671aad699aa8787fd74061f98) method, and append a newline.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::ios_base::failure | Any error that is forwarded when writing to the *stream*. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BError.html).
