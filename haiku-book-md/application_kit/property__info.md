---
name: property_info
type: struct
kit: application_kit
brief: "Property info struct containing lists of commands and specifiers"
source: haiku-book
---

# property_info Struct
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Property info struct containing lists of commands and specifiers. 



**Since:** BeOS R3

## Member List

### Public Attributes

* `uint32` [_reserved](#a491f2e59f2e305476ca56ab4477893c2) [10] — Reserved for future expansion, do not use.
* `uint32` [commands](#aeffd1070c7bf94abc3ebfc68aae81d33) [10] — Zero-terminated array of commands understood by the property e.g. B_GET_PROPERTY.
* `compound_type` [ctypes](#afa83cfbf23f28dfe07d19d7880a4aa60) [3] — Type chunks?
* `uint32` [extra_data](#a4268fb27674968e0ca7858becc171040) — Place to specify freeform data, it is not used by the OS.
* `const char *` [name](#a1abf3398482826a406059861448d041b) — The name of the property.
* `uint32` [specifiers](#a03a26dcadc3a8ca737d38dce899666ed) [10] — Zero-terminated array of the specifiers understood by the property e.g. B_DIRECT_SPECIFIER.
* `uint32` [types](#a3b0a900c9c8bd7918a3f60db84a88d75) [10] — Type chunks?
* `const char *` [usage](#a419267a1e4650efcc45dde1d72832315) — Human-readable string describing the property and its supported commands and specifiers.

## Detailed Member Documentation

### `_reserved`

```cpp
property_info::_reserved
```

Reserved for future expansion, do not use. 



**Since:** BeOS R5

---

### `commands`

```cpp
property_info::commands
```

Zero-terminated array of commands understood by the property e.g. `B_GET_PROPERTY`. 


If the first element is 0 it is treated as a wildcard matching all supported commands.



**Since:** BeOS R3

---

### `ctypes`

```cpp
property_info::ctypes
```

Type chunks? 



**Since:** BeOS R4

---

### `extra_data`

```cpp
property_info::extra_data
```

Place to specify freeform data, it is not used by the OS. 



**Since:** BeOS R3

---

### `name`

```cpp
property_info::name
```

The name of the property. 



**Since:** BeOS R3

---

### `specifiers`

```cpp
property_info::specifiers
```

Zero-terminated array of the specifiers understood by the property e.g. `B_DIRECT_SPECIFIER`. 


If the first element is 0 it is treated as a wildcard matching all supported specifiers.



**Since:** BeOS R3

---

### `types`

```cpp
property_info::types
```

Type chunks? 



**Since:** BeOS R4

---

### `usage`

```cpp
property_info::usage
```

Human-readable string describing the property and its supported commands and specifiers. 



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structproperty__info.html).
