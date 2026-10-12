---
name: BPrivate::Network::BNetworkRequestError
type: class
kit: netservices_kit
brief: "Error that indicates there was an issue executing the network request"
source: haiku-book
---

# BPrivate::Network::BNetworkRequestError Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Error that indicates there was an issue executing the network request. 



**Since:** Haiku R1

## Member List

### Public Types

* `enum` [ErrorType](#ga03cb239064102cab8aaecb6a730ff736) { 
  HostnameError
, 
  NetworkError
, 
  ProtocolError
, 
  SystemError
, 
  Canceled

 } — A list of errors that can occur while executing a network request.

### Public Member Functions

* [BNetworkRequestError](#a90f16a87c95785dfdf2944c0f0a607b9) (const char *origin, ErrorType type, const BString &customMessage=BString()) — Create a new network request error.
* [BNetworkRequestError](#a148d5c6515b415f0ed6d8734af96210f) (const char *origin, ErrorType type, status_t errorCode, const BString &customMessage=BString()) — Create a new network request error.
* `const char *` [CustomMessage](#a1b11eec92e14ff4ad4a1fe434245e9c5) () const noexcept — Get the custom error message.
* `virtual BString` [DebugMessage](#a038e30d1d5fcaac6a48c6b8281b5b110) () const override — Retrieve a debug message that contains all info in this error.
* `status_t` [ErrorCode](#ab16d8aa51743e78602ff42f37149d94b) () const noexcept — Get the underlying system error code.
* `virtual const char *` [Message](#aca0ab9afcc80043409a087da5a784508) () const noexcept override — Access the string representation of the message.
* `ErrorType` [Type](#aa2d064311bd62e50719c267bdf53661c) () const noexcept — Get the error type.
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

### `BNetworkRequestError()`

```cpp
BPrivate::Network::BNetworkRequestError::BNetworkRequestError(const char * origin, ErrorType type, status_t errorCode, const BString & customMessage = BString())
```

Create a new network request error. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `origin` | A string representing where this error occured. It is advised to initialize it to `__PRETTY_FUNCTION__` by default. |
| `type` | The error type that describes what the issue was that prevented the completion of the request. |
| `errorCode` | The underlying system error. See the [BNetworkRequestError::ErrorType](group__netservices.md#ga03cb239064102cab8aaecb6a730ff736) documentation on which error types expect a system error. |
| `customMessage` | Optional custom message describing the reason or cause for the error. |





**Since:** Haiku R1

---

### `BNetworkRequestError()`

```cpp
BPrivate::Network::BNetworkRequestError::BNetworkRequestError(const char * origin, ErrorType type, const BString & customMessage = BString())
```

Create a new network request error. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `origin` | A string representing where this error occured. It is advised to initialize it to `__PRETTY_FUNCTION__` by default. |
| `type` | The error type that describes what the issue was that prevented the completion of the request. |
| `customMessage` | Optional custom message describing the reason or cause for the error. |





**Since:** Haiku R1

---

### `CustomMessage()`

```cpp
const char * BPrivate::Network::BNetworkRequestError::CustomMessage()const
```

Get the custom error message. 



**Returns:** Get the custom error message. This may be an empty string if it was not set.



**Since:** Haiku R1

---

### `DebugMessage()`

```cpp
virtual BString BPrivate::Network::BNetworkRequestError::DebugMessage()const
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

### `ErrorCode()`

```cpp
status_t BPrivate::Network::BNetworkRequestError::ErrorCode()const
```

Get the underlying system error code. 



**Returns:** A `status_t` error code when the associated [BNetworkRequestError::ErrorType](group__netservices.md#ga03cb239064102cab8aaecb6a730ff736) sets the system error, or `B_OK` if there is no additional error code available.



**Since:** Haiku R1

---

### `Message()`

```cpp
virtual const char * BPrivate::Network::BNetworkRequestError::Message()const
```

Access the string representation of the message. 


Implementations should return a meaningful description of the error that occured. The primary target audience of these messages are developers, who (hopefully) see them during development, testing or in bug reports. However, if it makes sense to have the error messages be instructive to users too, then do not hesitate to do so.


Implementations of this function should never return `NULL`.



**Since:** Haiku R1


Implements [BPrivate::Network::BError](classBPrivate_1_1Network_1_1BError.md#a2c1b049e967387a289b1b0b8694eca28).

---

### `Type()`

```cpp
ErrorType BPrivate::Network::BNetworkRequestError::Type()const
```

Get the error type. 



**Returns:** Get the [BNetworkRequestError::ErrorType](group__netservices.md#ga03cb239064102cab8aaecb6a730ff736) that describes the cause for the request to fail.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BNetworkRequestError.html).
