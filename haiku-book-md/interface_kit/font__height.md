---
name: font_height
type: struct
kit: interface_kit
brief: "The amount of vertical space surrounding a character"
source: haiku-book
---

# font_height Struct
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

The amount of vertical space surrounding a character. 



**See also:** [BFont::GetHeight()](classBFont.md#a9748877645b9e3ab98a3a43a5375f392)



**Since:** BeOS R3

## Member List

### Public Attributes

* `float` [ascent](#ae5be38f63066837661faddd9d37d42b3)
* `float` [descent](#a622b531cac9f22e9bf3756571bcbb768)
* `float` [leading](#a4d8f4dde404154b62d937d3871e350e1)

## Detailed Member Documentation

### `ascent`

```cpp
font_height::ascent
```

The distance characters can ascend above the baseline.



**Since:** BeOS R3

---

### `descent`

```cpp
font_height::descent
```

The distance characters can descend below the baseline.



**Since:** BeOS R3

---

### `leading`

```cpp
font_height::leading
```

The distance between lines, descent above to ascent below.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structfont__height.html).
