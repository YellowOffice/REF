---
name: BSize
type: class
kit: interface_kit
brief: "A two-dimensional size"
source: haiku-book
---

# BSize Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A two-dimensional size. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BSize](#a0b5ebd8b8b5f4c0b5c761a4a373b0190) () — Initializes a BSize object with both dimensions set to B_SIZE_UNSET.
* [BSize](#aebd79552dc1dfc26306d1672c21c98fc) (const BSize &other) — Initializes a BSize object from another BSize.
* [BSize](#a8508a9b19f7ed6e7c7885d635a9002e1) (float width, float height) — Initializes a BSize object with the specified width and height values.
* `float` [Height](#aa93b0d4c9957e9133b67b8e23759db64) () const — Gets the height of the BSize object.
* `int32` [IntegerHeight](#a6437f6b0f008a2cdb620de4f992c309c) () const — Returns the height value of a BSize object as an int32.
* `int32` [IntegerWidth](#aaaafde7965ffc89603d63ea615667b0f) () const — Returns the width value of a BSize object as an int32.
* `bool` [IsHeightSet](#a5ad873454dda2b3f33046297e1d74172) () const — Checks if the BSize::height is not B_SIZE_UNSET.
* `bool` [IsWidthSet](#a453861866d677ae6d3bf2e9ccc436179) () const — Checks if the BSize::width is not B_SIZE_UNSET.
* `void` [Set](#ac5c881bb77144a1bb06c035298870c99) (float width, float height) — Sets the width and height values of a BSize object.
* `void` [SetHeight](#a33da506f5759c9651a61af61a766221c) (float height) — Sets the height value of a BSize object.
* `void` [SetWidth](#a7272b3bdb3e42642bf437f6c7621fc3b) (float width) — Sets the width value of a BSize object.
* `float` [Width](#a0539c980fd88ea95a3405ec1185653f8) () const — Gets the width of the BSize object.
* `bool` [operator==](#ae8aafd08046f848dd8fa5681db9aeb95) (const BSize &other) const — Returns whether or not the width and height values of the BSize objects are equal.
* `bool` [operator!=](#af10fa4c2c80541888c3b2408cf8b6fda) (const BSize &other) const — Returns whether or not the width and height values of the BSize objects differ.
* `BSize &` [operator=](#a47f7f6185bf36370d514c86a8670481e) (const BSize &other) — Initializes a BSize object from another BSize by overloading the = operator.

### Public Attributes

* `float` [height](#a518f29c07d95774fdc18c7cc88c1b562) — The vertical dimension.
* `float` [width](#a4c78fadd3cc44c3460e88842cb90bd67) — The horizontal dimension.

## Detailed Member Documentation

### `BSize()`

```cpp
BSize::BSize()
```

Initializes a [BSize](classBSize.md) object with both dimensions set to `B_SIZE_UNSET`. 



**See also:** [BSize::Set()](classBSize.md#ac5c881bb77144a1bb06c035298870c99)



**Since:** Haiku R1

---

### `BSize()`

```cpp
BSize::BSize(const BSize & other)
```

Initializes a [BSize](classBSize.md) object from another [BSize](classBSize.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BSize](classBSize.md) object to copy from. |





**Since:** Haiku R1

---

### `BSize()`

```cpp
BSize::BSize(float width, float height)
```

Initializes a [BSize](classBSize.md) object with the specified *width* and *height* values. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `width` | The *width* value to set. |
| `height` | The *height* value to set. |





**Since:** Haiku R1

---

### `Height()`

```cpp
float BSize::Height()const
```

Gets the *height* of the [BSize](classBSize.md) object. 



**Returns:** [BSize::height](classBSize.md#a518f29c07d95774fdc18c7cc88c1b562)



**Since:** Haiku R1


References [height](classBSize.md#a518f29c07d95774fdc18c7cc88c1b562).

---

### `IntegerHeight()`

```cpp
int32 BSize::IntegerHeight()const
```

Returns the *height* value of a [BSize](classBSize.md) object as an *int32*. 



**Returns:** [BSize::height](classBSize.md#a518f29c07d95774fdc18c7cc88c1b562), cast to an *int32*.



> [!WARNING]
> This may lose precision!



**Since:** Haiku R1


References [height](classBSize.md#a518f29c07d95774fdc18c7cc88c1b562).

---

### `IntegerWidth()`

```cpp
int32 BSize::IntegerWidth()const
```

Returns the *width* value of a [BSize](classBSize.md) object as an *int32*. 



**Returns:** [BSize::width](classBSize.md#a4c78fadd3cc44c3460e88842cb90bd67), cast to an *int32*.



> [!WARNING]
> This may lose precision!



**Since:** Haiku R1


References [width](classBSize.md#a4c78fadd3cc44c3460e88842cb90bd67).

---

### `IsHeightSet()`

```cpp
bool BSize::IsHeightSet()const
```

Checks if the [BSize::height](classBSize.md#a518f29c07d95774fdc18c7cc88c1b562) is not `B_SIZE_UNSET`. 



**Returns:** `true` if the height is set, `false` otherwise.



**Since:** Haiku R1


References [B_SIZE_UNSET](Size_8h.md#a1dc099c8754c10733691596df97c47c1), and [height](classBSize.md#a518f29c07d95774fdc18c7cc88c1b562).

---

### `IsWidthSet()`

```cpp
bool BSize::IsWidthSet()const
```

Checks if the [BSize::width](classBSize.md#a4c78fadd3cc44c3460e88842cb90bd67) is not `B_SIZE_UNSET`. 



**Returns:** `true` if the width is set, `false` otherwise.



**Since:** Haiku R1


References [B_SIZE_UNSET](Size_8h.md#a1dc099c8754c10733691596df97c47c1), and [width](classBSize.md#a4c78fadd3cc44c3460e88842cb90bd67).

---

### `operator!=()`

```cpp
bool BSize::operator!=(const BSize & other)const
```

Returns whether or not the width and height values of the [BSize](classBSize.md) objects differ. 



**Returns:** `true` if the width or height values differ, `false` otherwise.



**Since:** Haiku R1

---

### `operator=()`

```cpp
BSize & BSize::operator=(const BSize & other)
```

Initializes a [BSize](classBSize.md) object from another [BSize](classBSize.md) by overloading the = operator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BSize](classBSize.md) object to copy from. |





**Since:** Haiku R1


References [height](classBSize.md#a518f29c07d95774fdc18c7cc88c1b562), and [width](classBSize.md#a4c78fadd3cc44c3460e88842cb90bd67).

---

### `operator==()`

```cpp
bool BSize::operator==(const BSize & other)const
```

Returns whether or not the width and height values of the [BSize](classBSize.md) objects are equal. 



**Returns:** `true` if the width and height values are equal, `false` otherwise.



**Since:** Haiku R1


References [height](classBSize.md#a518f29c07d95774fdc18c7cc88c1b562), and [width](classBSize.md#a4c78fadd3cc44c3460e88842cb90bd67).

---

### `Set()`

```cpp
void BSize::Set(float width, float height)
```

Sets the *width* and *height* values of a [BSize](classBSize.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `width` | The *width* value to set. |
| `height` | The *height* value to set. |





**Since:** Haiku R1


References [height](classBSize.md#a518f29c07d95774fdc18c7cc88c1b562), and [width](classBSize.md#a4c78fadd3cc44c3460e88842cb90bd67).

---

### `SetHeight()`

```cpp
void BSize::SetHeight(float height)
```

Sets the *height* value of a [BSize](classBSize.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `height` | The *height* value to set. |





**Since:** Haiku R1


References [height](classBSize.md#a518f29c07d95774fdc18c7cc88c1b562).

---

### `SetWidth()`

```cpp
void BSize::SetWidth(float width)
```

Sets the *width* value of a [BSize](classBSize.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `width` | The *width* value to set. |





**Since:** Haiku R1


References [width](classBSize.md#a4c78fadd3cc44c3460e88842cb90bd67).

---

### `Width()`

```cpp
float BSize::Width()const
```

Gets the *width* of the [BSize](classBSize.md) object. 



**Returns:** [BSize::width](classBSize.md#a4c78fadd3cc44c3460e88842cb90bd67)



**Since:** Haiku R1


References [width](classBSize.md#a4c78fadd3cc44c3460e88842cb90bd67).

---

### `height`

```cpp
BSize::height
```

The vertical dimension. 



**Since:** Haiku R1


Referenced by [Height()](classBSize.md#aa93b0d4c9957e9133b67b8e23759db64), [IntegerHeight()](classBSize.md#a6437f6b0f008a2cdb620de4f992c309c), [IsHeightSet()](classBSize.md#a5ad873454dda2b3f33046297e1d74172), [operator=()](classBSize.md#a47f7f6185bf36370d514c86a8670481e), [operator==()](classBSize.md#ae8aafd08046f848dd8fa5681db9aeb95), [Set()](classBSize.md#ac5c881bb77144a1bb06c035298870c99), and [SetHeight()](classBSize.md#a33da506f5759c9651a61af61a766221c).

---

### `width`

```cpp
BSize::width
```

The horizontal dimension. 



**Since:** Haiku R1


Referenced by [IntegerWidth()](classBSize.md#aaaafde7965ffc89603d63ea615667b0f), [IsWidthSet()](classBSize.md#a453861866d677ae6d3bf2e9ccc436179), [operator=()](classBSize.md#a47f7f6185bf36370d514c86a8670481e), [operator==()](classBSize.md#ae8aafd08046f848dd8fa5681db9aeb95), [Set()](classBSize.md#ac5c881bb77144a1bb06c035298870c99), [SetWidth()](classBSize.md#a7272b3bdb3e42642bf437f6c7621fc3b), and [Width()](classBSize.md#a0539c980fd88ea95a3405ec1185653f8).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBSize.html).
