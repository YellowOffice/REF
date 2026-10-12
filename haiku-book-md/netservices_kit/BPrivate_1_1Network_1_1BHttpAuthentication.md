---
name: BPrivate::Network::BHttpAuthentication
type: struct
kit: netservices_kit
brief: "Describe username and password for basic authentication for the request"
source: haiku-book
---

# BPrivate::Network::BHttpAuthentication Struct
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Describe username and password for basic authentication for the request. 



**See also:** These options are used by [BHttpRequest::Authentication()](classBPrivate_1_1Network_1_1BHttpRequest.md#ac837488d86d25ef1f52e1f0631b84eee) and [BHttpRequest::SetAuthentication()](classBPrivate_1_1Network_1_1BHttpRequest.md#ae334ac3d1f5408479d75814f7a28af26)



**Since:** Haiku R1

## Member List

### Public Attributes

* `BString` [password](#a11d4062064a16f26415ef7889a0f7651) — The password for the request.
* `BString` [username](#a6798279afc08c4a97c53d84fcfd28d73) — The username for the request.

## Detailed Member Documentation

### `password`

```cpp
BString BPrivate::Network::BHttpAuthentication::password
```

The password for the request. 



**Since:** Haiku R1

---

### `username`

```cpp
BString BPrivate::Network::BHttpAuthentication::username
```

The username for the request. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structBPrivate_1_1Network_1_1BHttpAuthentication.html).
