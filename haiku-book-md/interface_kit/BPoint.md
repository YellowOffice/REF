---
name: BPoint
type: class
kit: interface_kit
brief: "A point on a two-dimensional Cartesian coordinate system"
source: haiku-book
---

# BPoint Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A point on a two-dimensional Cartesian coordinate system. 



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BPoint](#a00db170ab9b36aa841dd8a99efeb8e20) () — Initializes a BPoint object at the origin, (0, 0).
* [BPoint](#acd4b14896346e476bcf7d3e905001edd) (const BPoint &p) — Initializes a BPoint object from another BPoint.
* [BPoint](#a4dc55682abc94f59f13faddb51518397) (float x, float y) — Initializes a BPoint object at the specified x and y coordinates.
* `void` [ConstrainTo](#a81254fef5bb205f952e252cf5f07ab59) (BRect rect) — Moves the BPoint so that it is contained within rect.
* `void` [PrintToStream](#a18a683442d46d96f940caf72989c139e) () const — Print the x and y coordinates to standard output.
* `void` [Set](#a2c74b3de1e07a3e015d8aff2201f0d93) (float x, float y) — Sets the x and y coordinates of a BPoint object.
* `BPoint &` [operator=](#a09bdb140927d4fe8bf41064995de3d73) (const BPoint &other) — Initializes a BPoint object from another BPoint by overloading the = operator.
* `BPoint` [operator-](#a9fc2679f8a8b35158ed13e4bf2fc0744) () const — Returns a BPoint object with the x and y coordinates negated.
* `BPoint` [operator+](#a895ffea834de0a6cc36e8f1382521acb) (const BPoint &other) const — Returns a BPoint where the x-coordinate is the sum of the x values and the y-coordinate is the sum of the y values.
* `BPoint` [operator-](#a4061051950412275ef5f4502079d0d19) (const BPoint &other) const — Returns a BPoint where the x-coordinate is the difference of the x values and the y-coordinate is the difference of the y values.
* `BPoint &` [operator+=](#aa66d7811e0fb28039e6f0945220b5714) (const BPoint &other) — Uses the BPoint as an accumulator storing the sum of the x values and the sum of the y values.
* `BPoint &` [operator-=](#a129b464172b365046e2a802e5c56c3ab) (const BPoint &other) — Uses the BPoint as an accumulator storing the difference of the x values and the difference of the y values.
* `bool` [operator!=](#ae68f985f367819c790bece3179813d15) (const BPoint &other) const — Returns whether or not the x and y coordinates of the BPoint objects differ.
* `bool` [operator==](#a49e648398da89761103928bb125c3165) (const BPoint &other) const — Returns whether or not the x and y coordinates of the BPoint objects are equal.

### Public Attributes

* `float` [x](#ae8e68c02284caf91f82efb3410fd6708) — The horizontal coordinate.
* `float` [y](#a5ffb358a63973977830a85489829c737) — The vertical coordinate.

## Detailed Member Documentation

### `BPoint()`

```cpp
BPoint::BPoint()
```

Initializes a [BPoint](classBPoint.md) object at the origin, (0, 0). 



**See also:** [BPoint::Set()](classBPoint.md#a2c74b3de1e07a3e015d8aff2201f0d93)



**Since:** BeOS R3

---

### `BPoint()`

```cpp
BPoint::BPoint(float x, float y)
```

Initializes a [BPoint](classBPoint.md) object at the specified *x* and *y* coordinates. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | The *x* coordinate. |
| `y` | The *y* coordinate. |





**Since:** BeOS R3

---

### `BPoint()`

```cpp
BPoint::BPoint(const BPoint & other)
```

Initializes a [BPoint](classBPoint.md) object from another [BPoint](classBPoint.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BPoint](classBPoint.md) object to copy from. |





**Since:** BeOS R3

---

### `ConstrainTo()`

```cpp
void BPoint::ConstrainTo(BRect rect)
```

Moves the [BPoint](classBPoint.md) so that it is contained within *rect*. 


If the [BPoint](classBPoint.md) is already contained within *rect* this method has no effect.


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The [BRect](classBRect.md) to constrain the [BPoint](classBPoint.md) within. |





**Since:** BeOS R3

---

### `operator!=()`

```cpp
bool BPoint::operator!=(const BPoint & other)const
```

Returns whether or not the x and y coordinates of the [BPoint](classBPoint.md) objects differ. 



**Returns:** `true` if the x or y coordinates differ, `false` otherwise.



**Since:** BeOS R3

---

### `operator+()`

```cpp
BPoint BPoint::operator+(const BPoint & other)const
```

Returns a [BPoint](classBPoint.md) where the x-coordinate is the sum of the x values and the y-coordinate is the sum of the y values. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BPoint](classBPoint.md) object to use in the addition. |





**Returns:** A new [BPoint](classBPoint.md) object.



**Since:** BeOS R3

---

### `operator+=()`

```cpp
BPoint & BPoint::operator+=(const BPoint & other)
```

Uses the [BPoint](classBPoint.md) as an accumulator storing the sum of the x values and the sum of the y values. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BPoint](classBPoint.md) object to use in the addition. |





**Returns:** The address of the [BPoint](classBPoint.md) object.



**Since:** BeOS R3

---

### `operator-()`

```cpp
BPoint BPoint::operator-()const
```

Returns a [BPoint](classBPoint.md) object with the x and y coordinates negated. 



**Returns:** A new [BPoint](classBPoint.md) object.



**Since:** BeOS R3

---

### `operator-()`

```cpp
BPoint BPoint::operator-(const BPoint & other)const
```

Returns a [BPoint](classBPoint.md) where the x-coordinate is the difference of the x values and the y-coordinate is the difference of the y values. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BPoint](classBPoint.md) object to use in the subtraction. |





**Returns:** A new [BPoint](classBPoint.md) object.



**Since:** BeOS R3

---

### `operator-=()`

```cpp
BPoint & BPoint::operator-=(const BPoint & other)
```

Uses the [BPoint](classBPoint.md) as an accumulator storing the difference of the x values and the difference of the y values. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BPoint](classBPoint.md) object to use in the subtraction. |





**Returns:** The address of the [BPoint](classBPoint.md) object.



**Since:** BeOS R3

---

### `operator=()`

```cpp
BPoint & BPoint::operator=(const BPoint & other)
```

Initializes a [BPoint](classBPoint.md) object from another [BPoint](classBPoint.md) by overloading the = operator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BPoint](classBPoint.md) object to copy from. |





**Since:** BeOS R3


References [x](classBPoint.md#ae8e68c02284caf91f82efb3410fd6708), and [y](classBPoint.md#a5ffb358a63973977830a85489829c737).

---

### `operator==()`

```cpp
bool BPoint::operator==(const BPoint & other)const
```

Returns whether or not the x and y coordinates of the [BPoint](classBPoint.md) objects are equal. 



**Returns:** `true` if the x and y coordinates are equal, `false` otherwise.



**Since:** BeOS R3

---

### `PrintToStream()`

```cpp
void BPoint::PrintToStream()const
```

Print the x and y coordinates to standard output. 


Prints in the following format:


BPoint(x:%.0f, y:%.0f)

**Since:** BeOS R3

---

### `Set()`

```cpp
void BPoint::Set(float x, float y)
```

Sets the *x* and *y* coordinates of a [BPoint](classBPoint.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | The *x* coordinate to set. |
| `y` | The *y* coordinate to set. |





**Since:** BeOS R3


References [x](classBPoint.md#ae8e68c02284caf91f82efb3410fd6708), and [y](classBPoint.md#a5ffb358a63973977830a85489829c737).

---

### `x`

```cpp
BPoint::x
```

The horizontal coordinate. 



**Since:** BeOS R3


Referenced by [operator=()](classBPoint.md#a09bdb140927d4fe8bf41064995de3d73), and [Set()](classBPoint.md#a2c74b3de1e07a3e015d8aff2201f0d93).

---

### `y`

```cpp
BPoint::y
```

The vertical coordinate. 



**Since:** BeOS R3


Referenced by [operator=()](classBPoint.md#a09bdb140927d4fe8bf41064995de3d73), and [Set()](classBPoint.md#a2c74b3de1e07a3e015d8aff2201f0d93).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPoint.html).
