---
name: escapement_delta
type: struct
kit: interface_kit
brief: "A struct that allows you to specify extra horizontal space to surround each character with"
source: haiku-book
---

# escapement_delta Struct
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A struct that allows you to specify extra horizontal space to surround each character with. 


Escapements need to be multiplied by the font size to get the correct value for the font.



**See also:** [BFont::GetEscapements()](classBFont.md#aca49530c494a52f06fd5ea88d66a0f31)



**Since:** BeOS R3

## Member List

### Public Attributes

* `float` [nonspace](#aee2d82396e67a1309184e3c05928f418)
* `float` [space](#a339344ba07a97dc559528907ce6b8b04)

## Detailed Member Documentation

### `nonspace`

```cpp
escapement_delta::nonspace
```

The amount of horizontal space to surround a visible glyph character with.



**Since:** BeOS R3

---

### `space`

```cpp
escapement_delta::space
```

The amount of horizontal space to surround a whitespace character with, for example `B_TAB` or `B_SPACE`.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structescapement__delta.html).
