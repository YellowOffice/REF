---
name: BPrivate::Network::BHttpRequest::Body
type: struct
kit: netservices_kit
brief: "Describe the body for a network request"
source: haiku-book
---

# BPrivate::Network::BHttpRequest::Body Struct
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Describe the body for a network request. 



**Since:** Haiku R1

## Member List

### Public Attributes

* `std::unique_ptr< BDataIO >` [input](#a070222a623bb49a83d151c04bffdd69a) — The BDataIO object that holds the contents of the body.
* `BString` [mimeType](#a892ebd04b690d10ab98a8628ac31e3b3) — The mimetype of the body.
* `std::optional< off_t >` [size](#aacf2167880a0f395fcd9fae30313fa0c) — The size of the content, if known.
* `std::optional< off_t >` [startPosition](#a30b76dbccb1b45a7004976f3c652ee9e) — If the input is a BPositionIO, this is the current position when the body was set.

## Detailed Member Documentation

### `input`

```cpp
std::unique_ptr< BDataIO > BPrivate::Network::BHttpRequest::Body::input
```

The [BDataIO](../support_kit/classBDataIO.md) object that holds the contents of the body. 



**Since:** Haiku R1

---

### `mimeType`

```cpp
BString BPrivate::Network::BHttpRequest::Body::mimeType
```

The mimetype of the body. 


The `Content-Type` header field of the request is set to this value.



**Since:** Haiku R1

---

### `size`

```cpp
std::optional< off_t > BPrivate::Network::BHttpRequest::Body::size
```

The size of the content, if known. 



**Since:** Haiku R1

---

### `startPosition`

```cpp
std::optional< off_t > BPrivate::Network::BHttpRequest::Body::startPosition
```

If the input is a [BPositionIO](../support_kit/classBPositionIO.md), this is the current position when the body was set. 


This value is used to rewind the input when it needs to be resubmitted, for example in the case of a redirection.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structBPrivate_1_1Network_1_1BHttpRequest_1_1Body.html).
