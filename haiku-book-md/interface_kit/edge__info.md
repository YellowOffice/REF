---
name: edge_info
type: struct
kit: interface_kit
brief: "The distance that a character outline is inset from its escapement boundaries"
source: haiku-book
---

# edge_info Struct
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

The distance that a character outline is inset from its escapement boundaries. 


Edge values, like escapements, need to be multiplied by the font size to get the correct value for the font.



**See also:** [BFont::GetEdges()](classBFont.md#aa08a3467e1720dd4431fb7264a242c45)



**Since:** BeOS R3

## Member List

### Public Attributes

* `float` [left](#ae8f1d94bf201c8dfc5ffbd6f1e70e4a9)
* `float` [right](#a0875f3a277a3713808e0938a09d24fce)

## Detailed Member Documentation

### `left`

```cpp
edge_info::left
```

The distance that the character outline is inset from the left escapement boundary.



**Since:** BeOS R3

---

### `right`

```cpp
edge_info::right
```

The distance that the character outline is inset from the right escapement boundary.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structedge__info.html).
