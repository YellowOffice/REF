---
name: BPrivate::Network::BHttpStatus
type: struct
kit: netservices_kit
brief: "Represents the HTTP status code and status text of an incoming response"
source: haiku-book
---

# BPrivate::Network::BHttpStatus Struct
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Represents the HTTP status code and status text of an incoming response. 


The HTTP Standard specifies that each response should include a [three digit status code](https://datatracker.ietf.org/doc/html/rfc7230#section-3.1.2) and a phrase that describes the status code. When processing the response status, you should ignore the textual representation and only look at the status code.


Instances of this class provide a representation of the actual status information in the response. There is no additional validation done, other than that the structure of the status line is in compliance with the HTTP specification.



**Since:** Haiku R1

## Member List

### Public Member Functions

* `BHttpStatusClass` [StatusClass](#aee040081cc92117a553cef8b4a399334) () const noexcept — Map the code value to a BHttpStatusClass value.
* `BHttpStatusCode` [StatusCode](#af2897a3a9446c64935e1263a598aad4b) () const noexcept — Map the code value to a BHttpStatusCode value.

### Public Attributes

* `int16` [code](#a1607a1c572652414b8bc51e521b3745e) = 0 — The three digit status code.
* `BString` [text](#a470208315b4ea46b23ebe708db235c2d) — A textual representation of the result status.

## Detailed Member Documentation

### `StatusClass()`

```cpp
BHttpStatusClass BPrivate::Network::BHttpStatus::StatusClass()const
```

Map the [code](structBPrivate_1_1Network_1_1BHttpStatus.md#a1607a1c572652414b8bc51e521b3745e) value to a [BHttpStatusClass](namespaceBPrivate_1_1Network.md#a10223862da6f30a38b3fccf10054ccf9) value. 



**Returns:** One of the valid values of [BHttpStatusClass](namespaceBPrivate_1_1Network.md#a10223862da6f30a38b3fccf10054ccf9), or `BHttpStatusClass::Invalid` if the return code cannot be maped.



**Since:** Haiku R1

---

### `StatusCode()`

```cpp
BHttpStatusCode BPrivate::Network::BHttpStatus::StatusCode()const
```

Map the [code](structBPrivate_1_1Network_1_1BHttpStatus.md#a1607a1c572652414b8bc51e521b3745e) value to a [BHttpStatusCode](namespaceBPrivate_1_1Network.md#a7fc5fcbcd12571685bad319d48fef5ce) value. 



**Returns:** One of the valid values of [BHttpStatusCode](namespaceBPrivate_1_1Network.md#a7fc5fcbcd12571685bad319d48fef5ce), or `BHttpStatusCode::Unknown` if the return code cannot be maped.



**Since:** Haiku R1

---

### `code`

```cpp
int16 BPrivate::Network::BHttpStatus::code = 0
```

The three digit status code. 


This code represents the result of how the server is processing or has processed a request. Common codes are `200` indicating success, or `404` indicating that the requested resource is not found.


See [RFC7231 and its references](https://datatracker.ietf.org/doc/html/rfc7231#page-48) for more information.



**Since:** Haiku R1

---

### `text`

```cpp
BString BPrivate::Network::BHttpStatus::text
```

A textual representation of the result status. 


As defined in the [specification](https://datatracker.ietf.org/doc/html/rfc7230#section-3.1.2), the status text should only be taken as informative. Only the [BHttpStatus::code](structBPrivate_1_1Network_1_1BHttpStatus.md#a1607a1c572652414b8bc51e521b3745e) should be used for further processing.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structBPrivate_1_1Network_1_1BHttpStatus.html).
