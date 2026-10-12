---
name: BPrivate::Network::BHttpBody
type: struct
kit: netservices_kit
brief: "Represents a HTTP response body"
source: haiku-book
---

# BPrivate::Network::BHttpBody Struct
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Represents a HTTP response body. 


The HTTP response body is captured in this object. The body is either stored into a target, or into a [text](structBPrivate_1_1Network_1_1BHttpBody.md#a2c22caaff871835ac25ecafe3789c4d3) variable, depending on how you called the [BHttpSession::Execute()](classBPrivate_1_1Network_1_1BHttpSession.md#ae14a7c52aaddfd69e22be4a8aeff727f) method.


You will usually get a reference to this object through the [BHttpResult::Body()](classBPrivate_1_1Network_1_1BHttpResult.md#adeef8669a4d6f0fcbbbc2766072a8519) method. If you want to keep the contents of the body beyond the lifetime of the [BHttpResult](classBPrivate_1_1Network_1_1BHttpResult.md) object, you should move the data into owned objects of your own.



**Since:** Haiku R1

## Member List

### Public Attributes

* `std::optional< BString >` [text](#a2c22caaff871835ac25ecafe3789c4d3) — A string containing the body of the HTTP request.

## Detailed Member Documentation

### `text`

```cpp
std::optional< BString > BPrivate::Network::BHttpBody::text
```

A string containing the body of the HTTP request. 


The value of this class variable is set to `std::nullopt` if the target body was written to a specified target. Otherwise, the response body is stored in this string. If the response body was empty, then this will be an empty string.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structBPrivate_1_1Network_1_1BHttpBody.html).
