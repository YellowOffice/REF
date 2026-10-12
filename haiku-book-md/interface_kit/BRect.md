---
name: BRect
type: class
kit: interface_kit
brief: "Defines a rectangular area aligned along pixel dimensions"
source: haiku-book
---

# BRect Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Defines a rectangular area aligned along pixel dimensions. 


[BRect](classBRect.md)'s are used throughout the Interface Kit to define the frames of windows, views, and bitmaps. [BRect](classBRect.md)'s are always oriented with completely vertical and horizontal lines, they cannot be rotated.


A [BRect](classBRect.md) must have a non-negative width and height to be valid, that is the left value must be greater than or equal to the right value and the bottom edge value be greater than or equal to the top value. You can test whether or not a [BRect](classBRect.md) is valid by calling [IsValid()](classBRect.md#af3e701c7a92ea7379943ce2cc1d66a79). Nothing prevents you from creating an invalid [BRect](classBRect.md), but, using one to define an area can produce unpredictable results.


A gotcha of using [BRect](classBRect.md)'s is that the starting point is 0, not 1, so in order to create a [BRect](classBRect.md) with a 32x32 pixel area you write:



```cpp
BRect(0, 0, 31, 31);
```

or if you have the width and height stored in a variable you subtract 1 like this:



```cpp
BRect(0, 0, width - 1, height -1);
```


**Since:** BeOS R3

## Member List

### Public Member Functions

* [BRect](#aec45286d0efd6227e3fa09e04b7a3baf) () — Creates an empty BRect object with dimensions (0, 0, -1, -1).
* [BRect](#a2351732f3198e9465eac7a69e60d04f2) (BPoint leftTop, BPoint rightBottom) — Creates a new BRect object with its dimensions defined by the leftTop and rightBottom points.
* [BRect](#a45d54a02a30734acf967f28d0c267508) (BPoint leftTop, BSize size) — Creates a new BRect object with its dimensions defined by the leftTop point and size.
* [BRect](#a0fdf1eb31002961b98f3d577dc4346a7) (const BRect &other) — Creates a new BRect object as a copy of other.
* [BRect](#a2049dc161cc78c7955a6302304faae66) (float left, float top, float right, float bottom) — Creates a new BRect object with the given dimensions.
* [BRect](#a4c40d50693fc042a4e3036bb7fd863e7) (float side) — Creates a new BRect object setting the left and top dimensions to 0 and setting the right and bottom dimensions to side - 1.
* `bool` [Contains](#a6f5c37ccc41d49131df112d5a74d5200) (BPoint point) const — Returns whether or not the BRect contains point.
* `bool` [Contains](#a7e5268e764cdcd03ef7177780338c658) (BRect rect) const — Returns whether or not the BRect wholly contains rect.
* `float` [Height](#aca81521a6170bdc66bf1cefa79ad3609) () const — Returns the height of the rectangle.
* `int32` [IntegerHeight](#a9b163b3d07d27dd23130781bde483bd9) () const — Returns The height of the rectangle rounded using ceil(bottom - top).
* `int32` [IntegerWidth](#ae52162fc1adc048605ec958c298417cd) () const — Returns The width of the rectangle rounded using ceil(right - left).
* `bool` [Intersects](#a5f0bd9533e3a9b3aa73674e2f74cb7e3) (BRect rect) const — Returns whether or not the BRect and rect intersect.
* `bool` [IsValid](#af3e701c7a92ea7379943ce2cc1d66a79) () const — Returns whether or not the BRect is valid.
* `BPoint` [LeftBottom](#aeea8c62fa651880f159793ae7da5054a) () const — Returns the left bottom point of the BRect.
* `BPoint` [LeftTop](#a39cb030731bbc8b0e82e04ed563d4340) () const — Returns the left top point of the BRect.
* `void` [PrintToStream](#ad2e5f6b30e591969f620a2e5cb8d3785) () const — Prints the BRect dimensions to standard output.
* `BPoint` [RightBottom](#a7e52511bb18f8e22d1bdd7d9c01b6a39) () const — Returns the right bottom point of the BRect.
* `BPoint` [RightTop](#af66a48189605a69edf987720ad5fa635) () const — Returns the right top point of the BRect.
* `void` [Set](#a7ad2bdde464155de1bdf38db91bceca3) (float left, float top, float right, float bottom) — Sets the dimensions of a BRect.
* `void` [SetLeftBottom](#a8c2558f788131c37db92a0be041a46ec) (const BPoint point) — Sets the left bottom point of the BRect.
* `void` [SetLeftTop](#a304bd292bba6a3fa54c0aa7b54220290) (const BPoint point) — Sets the left top point of the BRect.
* `void` [SetRightBottom](#ae5c5c2389dab41f899217e9b81af7aad) (const BPoint point) — Sets the right bottom point of the BRect.
* `void` [SetRightTop](#a4f1f445beee1e7048fe0dd7a4fd40d7c) (const BPoint point) — Sets the right top point of the BRect.
* `BSize` [Size](#a903279542b3a58bf10fd6d8b259f725b) () const — Returns the dimensions of the BRect.
* `float` [Width](#aaa68bc8c6101c25b021dcae20c01960a) () const — Returns the width of the rectangle.
* `BRect &` [operator=](#a18e7aca7fd299b5767b1468f3089b3fa) (const BRect &other) — Creates a new BRect object as a copy of other by overloading the = operator.
* `bool` [operator==](#a52ee98faa60ee7229409ba7637dde267) (BRect other) const — Returns whether or not two rectangles coincide exactly.
* `bool` [operator!=](#a30ec89be4be0b1de75f347fe03b917dd) (BRect other) const — Returns whether or not two rectangles do NOT coincide exactly.
* `BRect` [operator&](#ab7c07d135312a89bc41794969d608a7a) (BRect other) const — Creates and returns a new BRect that is the intersection of the BRect and other.
* `BRect` [operator|](#a12a843c53ea0ef93a6bf11a5bc4c59d6) (BRect other) const — Returns a new BRect that is the union of the BRect and other.
* `void` [InsetBy](#ad3b069e34687b65d0e6b4b083c47b59c) (BPoint inset) — Inset the BRect by the x and y coordinates of point.
* `void` [InsetBy](#a343783f899a8501669458172f6949b35) (float dx, float dy) — Inset the BRect by dx units in the horizontal direction and dy units in the vertical direction.
* `BRect &` [InsetBySelf](#a83c551c7c3ea2682103bdacf950045bd) (BPoint inset) — Like BRect::InsetBy() but returns the transformed BRect.
* `BRect &` [InsetBySelf](#a6377eafe20d2d0e872082dac30eafbe4) (float dx, float dy) — Like BRect::InsetBy() but returns the transformed BRect.
* `BRect` [InsetByCopy](#a41ff92a5d0b62a5ba4543ce841b83f22) (BPoint inset) const — Like BRect::InsetBy() but returns a copy of the transformed BRect leaving the original unmodified.
* `BRect` [InsetByCopy](#a509115fe2690096e857068dae20f09f0) (float dx, float dy) const — Like BRect::InsetBy() but returns a copy of the transformed BRect leaving the original unmodified.
* `void` [OffsetBy](#a9a8b7148025f839c387085535048fae2) (BPoint delta) — Moves the BRect horizontally by the x value of point and vertically by y value of point without changing the size of the rectangle.
* `void` [OffsetBy](#aee260dabc7f5d10f117b916f11168429) (float dx, float dy) — Moves the BRect horizontally by dx units and vertically by dy units point without changing the size of the rectangle.
* `void` [OffsetTo](#a1ca9ed8ce028d98c8a124295ecea41fe) (BPoint offset) — Move the BRect to the location specified by point.
* `void` [OffsetTo](#afd443e9c51d991d386bd11b372e1fa69) (float x, float y) — Move the BRect to the point specified by the given x and y coordinates.
* `BRect &` [OffsetBySelf](#a7fa352a96bb16046f0d5b0801ed91ba1) (BPoint offset) — Like BRect::OffsetBy() but returns the translated BRect.
* `BRect &` [OffsetBySelf](#a77f057d3ab457b177ef70ff726bda59d) (float dx, float dy) — Like BRect::OffsetBy() but returns the translated BRect.
* `BRect` [OffsetByCopy](#aa3c2f35396060f90675701f16ffc7c45) (BPoint offset) const — Like BRect::OffsetBy() but returns a copy of the translated BRect leaving the original unmodified.
* `BRect` [OffsetByCopy](#ae5ab87965986017c658fc906fed1a388) (float dx, float dy) const — Like BRect::OffsetBy() but returns a copy of the translated BRect leaving the original unmodified.
* `BRect &` [OffsetToSelf](#a2b8fa1ec48096e16de1c0a94efc6816e) (BPoint offset) — Like BRect::OffsetTo() but returns the translated BRect.
* `BRect &` [OffsetToSelf](#ace358552bc769a21db704b00b11f9400) (float x, float y) — Like BRect::OffsetTo() but returns the translated BRect.
* `BRect` [OffsetToCopy](#ac1b3a5eab5aac9a852df175a406927c8) (BPoint offset) const — Like BRect::OffsetTo() but returns a copy of the translated BRect leaving the original unmodified.
* `BRect` [OffsetToCopy](#a9df225c7be4a68fffc865e19b2f10080) (float x, float y) const — Like BRect::OffsetTo() but returns a copy of the translated BRect leaving the original unmodified.

### Public Attributes

* `float` [bottom](#a58dffee4bce99e849468e97fa926cfce) — The value of the rectangle's bottom edge.
* `float` [left](#a177c8a67d9ebe9af16620a4eaa7915cf) — The value of the rectangle's left edge.
* `float` [right](#aa9d294e406cc08595d4eb012b2ce5e5a) — The value of the rectangle's right edge.
* `float` [top](#ac5b5e678515645c6f4becf57448120ab) — The value of the rectangle's top edge.

## Detailed Member Documentation

### `BRect()`

```cpp
BRect::BRect()
```

Creates an empty [BRect](classBRect.md) object with dimensions (0, 0, -1, -1). 


These dimensions are invalid, use [Set()](classBRect.md#a7ad2bdde464155de1bdf38db91bceca3) to provide valid dimensions.



**See also:** [BRect::Set()](classBRect.md#a7ad2bdde464155de1bdf38db91bceca3)



**Since:** BeOS R3

---

### `BRect()`

```cpp
BRect::BRect(const BRect & other)
```

Creates a new [BRect](classBRect.md) object as a copy of *other*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BRect](classBRect.md) object to copy. |





**Since:** BeOS R3

---

### `BRect()`

```cpp
BRect::BRect(float left, float top, float right, float bottom)
```

Creates a new [BRect](classBRect.md) object with the given dimensions. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `left` | The left dimension. |
| `top` | The top dimension. |
| `right` | The right dimension. |
| `bottom` | The bottom dimension. |





**Since:** BeOS R3

---

### `BRect()`

```cpp
BRect::BRect(BPoint leftTop, BPoint rightBottom)
```

Creates a new [BRect](classBRect.md) object with its dimensions defined by the *leftTop* and *rightBottom* points. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `leftTop` | The position to set the left top corner to. |
| `rightBottom` | The position to set the bottom right corner to. |





**Since:** BeOS R3

---

### `BRect()`

```cpp
BRect::BRect(BPoint leftTop, BSize size)
```

Creates a new [BRect](classBRect.md) object with its dimensions defined by the *leftTop* point and *size*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `leftTop` | The position of the left top corner. |
| `size` | The *size* of the rect defining its width and height. |





**Since:** Haiku R1

---

### `BRect()`

```cpp
BRect::BRect(float side)
```

Creates a new [BRect](classBRect.md) object setting the left and top dimensions to 0 and setting the right and bottom dimensions to *side* - 1. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `side` | The dimension to set the right and bottom sides. |





**Since:** Haiku R1

---

### `Contains()`

```cpp
bool BRect::Contains(BPoint point)const
```

Returns whether or not the [BRect](classBRect.md) contains *point*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The point to test. |





**Returns:** `true` if the [BRect](classBRect.md) contains *point*, `false` otherwise.



**Since:** BeOS R3

---

### `Contains()`

```cpp
bool BRect::Contains(BRect rect)const
```

Returns whether or not the [BRect](classBRect.md) wholly contains *rect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The rectangle to test. |





**Returns:** `true` if the [BRect](classBRect.md) contains *rect*, `false` otherwise.



**Since:** BeOS R3

---

### `Height()`

```cpp
float BRect::Height()const
```

Returns the height of the rectangle. 



**Returns:** The height of the rectangle as a float.



**Since:** BeOS R3


References [bottom](classBRect.md#a58dffee4bce99e849468e97fa926cfce), and [top](classBRect.md#ac5b5e678515645c6f4becf57448120ab).

---

### `InsetBy()`

```cpp
void BRect::InsetBy(BPoint point)
```

Inset the [BRect](classBRect.md) by the x and y coordinates of *point*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The *point* to use to inset the [BRect](classBRect.md). |





**Since:** BeOS R3

---

### `InsetBy()`

```cpp
void BRect::InsetBy(float dx, float dy)
```

Inset the [BRect](classBRect.md) by *dx* units in the horizontal direction and *dy* units in the vertical direction. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dx` | The horizontal distance to inset the [BRect](classBRect.md) by. |
| `dy` | The vertical distance to inset the [BRect](classBRect.md) by. |





**Since:** BeOS R3

---

### `InsetByCopy()`

```cpp
BRect BRect::InsetByCopy(BPoint point)const
```

Like [BRect::InsetBy()](classBRect.md#ad3b069e34687b65d0e6b4b083c47b59c) but returns a copy of the transformed [BRect](classBRect.md) leaving the original unmodified. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The *point* to use to inset the [BRect](classBRect.md). |





**Returns:** A copy of the [BRect](classBRect.md) after it has been transformed.



**See also:** [BRect::InsetBy(BPoint point)](classBRect.md#ad3b069e34687b65d0e6b4b083c47b59c)



**Since:** BeOS R5

---

### `InsetByCopy()`

```cpp
BRect BRect::InsetByCopy(float dx, float dy)const
```

Like [BRect::InsetBy()](classBRect.md#ad3b069e34687b65d0e6b4b083c47b59c) but returns a copy of the transformed [BRect](classBRect.md) leaving the original unmodified. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dx` | The horizontal distance to inset the [BRect](classBRect.md) by. |
| `dy` | The vertical distance to inset the [BRect](classBRect.md) by. |





**Returns:** A copy of the [BRect](classBRect.md) after it has been transformed.



**See also:** [BRect::InsetBy(float dx, float dy)](classBRect.md#a343783f899a8501669458172f6949b35)



**Since:** BeOS R5

---

### `InsetBySelf()`

```cpp
BRect & BRect::InsetBySelf(BPoint point)
```

Like [BRect::InsetBy()](classBRect.md#ad3b069e34687b65d0e6b4b083c47b59c) but returns the transformed [BRect](classBRect.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The *point* to use to inset the [BRect](classBRect.md). |





**Returns:** The transformed [BRect](classBRect.md).



**See also:** [BRect::InsetBy(BPoint point)](classBRect.md#ad3b069e34687b65d0e6b4b083c47b59c)



**Since:** BeOS R5

---

### `InsetBySelf()`

```cpp
BRect & BRect::InsetBySelf(float dx, float dy)
```

Like [BRect::InsetBy()](classBRect.md#ad3b069e34687b65d0e6b4b083c47b59c) but returns the transformed [BRect](classBRect.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dx` | The horizontal distance to inset the [BRect](classBRect.md) by. |
| `dy` | The vertical distance to inset the [BRect](classBRect.md) by. |





**Returns:** The transformed [BRect](classBRect.md).



**See also:** [BRect::InsetBy(float dx, float dy)](classBRect.md#a343783f899a8501669458172f6949b35)



**Since:** BeOS R5

---

### `IntegerHeight()`

```cpp
int32 BRect::IntegerHeight()const
```

Returns The height of the rectangle rounded using ceil(*bottom* - *top*). 



**Returns:** The height of the rectangle as an int32.



**Since:** BeOS R3


References [bottom](classBRect.md#a58dffee4bce99e849468e97fa926cfce), and [top](classBRect.md#ac5b5e678515645c6f4becf57448120ab).

---

### `IntegerWidth()`

```cpp
int32 BRect::IntegerWidth()const
```

Returns The width of the rectangle rounded using ceil(*right* - *left*). 



**Returns:** The width of the rectangle as an int32.



**Since:** BeOS R3


References [left](classBRect.md#a177c8a67d9ebe9af16620a4eaa7915cf), and [right](classBRect.md#aa9d294e406cc08595d4eb012b2ce5e5a).

---

### `Intersects()`

```cpp
bool BRect::Intersects(BRect rect)const
```

Returns whether or not the [BRect](classBRect.md) and *rect* intersect. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The [BRect](classBRect.md) to use to test for intersection. |





**Returns:** `true` if the rectangles intersect, *false* otherwise.



**Since:** BeOS R3

---

### `IsValid()`

```cpp
bool BRect::IsValid()const
```

Returns whether or not the [BRect](classBRect.md) is valid. 


A [BRect](classBRect.md) is valid if its width and height are non-negative, that is its right value is greater than or equal to its left value and its bottom value is greater than or equal to its top value.



**Returns:** `true` if the [BRect](classBRect.md) is valid, `false` if the [BRect](classBRect.md) is invalid.



**Since:** BeOS R3


References [bottom](classBRect.md#a58dffee4bce99e849468e97fa926cfce), [left](classBRect.md#a177c8a67d9ebe9af16620a4eaa7915cf), [right](classBRect.md#aa9d294e406cc08595d4eb012b2ce5e5a), and [top](classBRect.md#ac5b5e678515645c6f4becf57448120ab).

---

### `LeftBottom()`

```cpp
BPoint BRect::LeftBottom()const
```

Returns the left bottom point of the [BRect](classBRect.md). 



**Returns:** The left bottom point as a [BPoint](classBPoint.md).



**Since:** BeOS R3


References [bottom](classBRect.md#a58dffee4bce99e849468e97fa926cfce), and [left](classBRect.md#a177c8a67d9ebe9af16620a4eaa7915cf).

---

### `LeftTop()`

```cpp
BPoint BRect::LeftTop()const
```

Returns the left top point of the [BRect](classBRect.md). 



**Returns:** The left top point as a [BPoint](classBPoint.md).



**Since:** BeOS R3


References [left](classBRect.md#a177c8a67d9ebe9af16620a4eaa7915cf).

---

### `OffsetBy()`

```cpp
void BRect::OffsetBy(BPoint point)
```

Moves the [BRect](classBRect.md) horizontally by the x value of *point* and vertically by y value of *point* without changing the size of the rectangle. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The *point* to use to move the rectangle. |





**Since:** BeOS R3

---

### `OffsetBy()`

```cpp
void BRect::OffsetBy(float dx, float dy)
```

Moves the [BRect](classBRect.md) horizontally by *dx* units and vertically by *dy* units point without changing the size of the rectangle. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dx` | The number of units the move the rectangle vertically. |
| `dy` | The number of units the move the rectangle horizontally. |





**Since:** BeOS R3

---

### `OffsetByCopy()`

```cpp
BRect BRect::OffsetByCopy(BPoint point)const
```

Like [BRect::OffsetBy()](classBRect.md#a9a8b7148025f839c387085535048fae2) but returns a copy of the translated [BRect](classBRect.md) leaving the original unmodified. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The *point* to use to move the rectangle. |





**Returns:** A copy of the [BRect](classBRect.md) after it has been translated.



**See also:** [BRect::OffsetBy(BPoint point)](classBRect.md#a9a8b7148025f839c387085535048fae2)



**Since:** BeOS R5

---

### `OffsetByCopy()`

```cpp
BRect BRect::OffsetByCopy(float dx, float dy)const
```

Like [BRect::OffsetBy()](classBRect.md#a9a8b7148025f839c387085535048fae2) but returns a copy of the translated [BRect](classBRect.md) leaving the original unmodified. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dx` | The number of units the move the rectangle vertically. |
| `dy` | The number of units the move the rectangle horizontally. |





**Returns:** A copy of the [BRect](classBRect.md) after it has been translated.



**See also:** [BRect::OffsetBy(float dx, float dy)](classBRect.md#aee260dabc7f5d10f117b916f11168429)



**Since:** BeOS R5

---

### `OffsetBySelf()`

```cpp
BRect & BRect::OffsetBySelf(BPoint point)
```

Like [BRect::OffsetBy()](classBRect.md#a9a8b7148025f839c387085535048fae2) but returns the translated [BRect](classBRect.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The *point* to use to move the rectangle. |





**See also:** [BRect::OffsetBy(BPoint point)](classBRect.md#a9a8b7148025f839c387085535048fae2)



**Since:** BeOS R5

---

### `OffsetBySelf()`

```cpp
BRect & BRect::OffsetBySelf(float dx, float dy)
```

Like [BRect::OffsetBy()](classBRect.md#a9a8b7148025f839c387085535048fae2) but returns the translated [BRect](classBRect.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dx` | The number of units the move the rectangle vertically. |
| `dy` | The number of units the move the rectangle horizontally. |





**Returns:** The translated [BRect](classBRect.md).



**See also:** [BRect::OffsetBy(float dx, float dy)](classBRect.md#aee260dabc7f5d10f117b916f11168429)



**Since:** BeOS R5

---

### `OffsetTo()`

```cpp
void BRect::OffsetTo(BPoint point)
```

Move the [BRect](classBRect.md) to the location specified by *point*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The location to move the [BRect](classBRect.md) to. |





**Since:** BeOS R3

---

### `OffsetTo()`

```cpp
void BRect::OffsetTo(float x, float y)
```

Move the [BRect](classBRect.md) to the point specified by the given *x* and *y* coordinates. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | The vertical coordinate of the point to move the [BRect](classBRect.md) to. |
| `y` | The horizontal coordinate of the point to move the [BRect](classBRect.md) to. |





**Since:** BeOS R3

---

### `OffsetToCopy()`

```cpp
BRect BRect::OffsetToCopy(BPoint point)const
```

Like [BRect::OffsetTo()](classBRect.md#a1ca9ed8ce028d98c8a124295ecea41fe) but returns a copy of the translated [BRect](classBRect.md) leaving the original unmodified. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The *point* to use to move the rectangle. |





**Returns:** A copy of the [BRect](classBRect.md) after it has been translated.



**See also:** [BRect::OffsetTo(BPoint point)](classBRect.md#a1ca9ed8ce028d98c8a124295ecea41fe)



**Since:** BeOS R5

---

### `OffsetToCopy()`

```cpp
BRect BRect::OffsetToCopy(float x, float y)const
```

Like [BRect::OffsetTo()](classBRect.md#a1ca9ed8ce028d98c8a124295ecea41fe) but returns a copy of the translated [BRect](classBRect.md) leaving the original unmodified. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | The number of units the move the rectangle vertically. |
| `y` | The number of units the move the rectangle horizontally. |





**Returns:** A copy of the [BRect](classBRect.md) after it has been translated.



**See also:** [BRect::OffsetTo(float x, float y)](classBRect.md#afd443e9c51d991d386bd11b372e1fa69)



**Since:** BeOS R5

---

### `OffsetToSelf()`

```cpp
BRect & BRect::OffsetToSelf(BPoint point)
```

Like [BRect::OffsetTo()](classBRect.md#a1ca9ed8ce028d98c8a124295ecea41fe) but returns the translated [BRect](classBRect.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The *point* to use to move the rectangle. |





**Returns:** The translated [BRect](classBRect.md).



**See also:** [BRect::OffsetTo(BPoint point)](classBRect.md#a1ca9ed8ce028d98c8a124295ecea41fe)



**Since:** BeOS R5

---

### `OffsetToSelf()`

```cpp
BRect & BRect::OffsetToSelf(float x, float y)
```

Like [BRect::OffsetTo()](classBRect.md#a1ca9ed8ce028d98c8a124295ecea41fe) but returns the translated [BRect](classBRect.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | The vertical coordinate of the point to move the [BRect](classBRect.md) to. |
| `y` | The horizontal coordinate of the point to move the [BRect](classBRect.md) to. |





**Returns:** The translated [BRect](classBRect.md).



**See also:** [BRect::OffsetTo(float x, float y)](classBRect.md#afd443e9c51d991d386bd11b372e1fa69)



**Since:** BeOS R5

---

### `operator!=()`

```cpp
bool BRect::operator!=(BRect other)const
```

Returns whether or not two rectangles do NOT coincide exactly. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BRect](classBRect.md) to compare with. |





**Returns:** `true` if the rectangles do NOT coincide, `false` otherwise.



**Since:** BeOS R3

---

### `operator&()`

```cpp
BRect BRect::operator&(BRect other)const
```

Creates and returns a new [BRect](classBRect.md) that is the intersection of the [BRect](classBRect.md) and *other*. 


The intersection of two rectangles is the area that they both share.


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BRect](classBRect.md) to take the intersection of. |





**Returns:** A new [BRect](classBRect.md) that is the intersection of the [BRect](classBRect.md) and *other*.



**Since:** BeOS R3

---

### `operator=()`

```cpp
BRect & BRect::operator=(const BRect & other)
```

Creates a new [BRect](classBRect.md) object as a copy of *other* by overloading the = operator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BRect](classBRect.md) object to copy. |





**Returns:** The newly created [BRect](classBRect.md) object.



**Since:** BeOS R3


References [bottom](classBRect.md#a58dffee4bce99e849468e97fa926cfce), [left](classBRect.md#a177c8a67d9ebe9af16620a4eaa7915cf), [right](classBRect.md#aa9d294e406cc08595d4eb012b2ce5e5a), and [top](classBRect.md#ac5b5e678515645c6f4becf57448120ab).

---

### `operator==()`

```cpp
bool BRect::operator==(BRect other)const
```

Returns whether or not two rectangles coincide exactly. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BRect](classBRect.md) to compare with. |





**Returns:** `true` if the rectangles coincide, `false` otherwise.



**Since:** BeOS R3

---

### `operator|()`

```cpp
BRect BRect::operator|(BRect other)const
```

Returns a new [BRect](classBRect.md) that is the union of the [BRect](classBRect.md) and *other*. 


The union of two rectangles is the area that encloses both rectangles.


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BRect](classBRect.md) to take the union of. |





**Returns:** A new [BRect](classBRect.md) that is the union of the [BRect](classBRect.md) and *other*.



**Since:** BeOS R3

---

### `PrintToStream()`

```cpp
void BRect::PrintToStream()const
```

Prints the [BRect](classBRect.md) dimensions to standard output. 


The format of the output looks like this: 

	BRect(l:%.1f, t:%.1f, r:%.1f, b:%.1f).

**Since:** BeOS R3

---

### `RightBottom()`

```cpp
BPoint BRect::RightBottom()const
```

Returns the right bottom point of the [BRect](classBRect.md). 



**Returns:** The right bottom point as a [BPoint](classBPoint.md).



**Since:** BeOS R3


References [right](classBRect.md#aa9d294e406cc08595d4eb012b2ce5e5a).

---

### `RightTop()`

```cpp
BPoint BRect::RightTop()const
```

Returns the right top point of the [BRect](classBRect.md). 



**Returns:** The left right point as a [BPoint](classBPoint.md).



**Since:** BeOS R3


References [right](classBRect.md#aa9d294e406cc08595d4eb012b2ce5e5a), and [top](classBRect.md#ac5b5e678515645c6f4becf57448120ab).

---

### `Set()`

```cpp
void BRect::Set(float left, float top, float right, float bottom)
```

Sets the dimensions of a [BRect](classBRect.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `left` | The *left* dimension to set. |
| `top` | The *top* dimension to set. |
| `right` | The *right* dimension to set. |
| `bottom` | The *bottom* dimension to set. |





**Since:** BeOS R3


References [bottom](classBRect.md#a58dffee4bce99e849468e97fa926cfce), [left](classBRect.md#a177c8a67d9ebe9af16620a4eaa7915cf), [right](classBRect.md#aa9d294e406cc08595d4eb012b2ce5e5a), and [top](classBRect.md#ac5b5e678515645c6f4becf57448120ab).

---

### `SetLeftBottom()`

```cpp
void BRect::SetLeftBottom(const BPoint point)
```

Sets the left bottom *point* of the [BRect](classBRect.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The *point* to set. |





**Since:** BeOS R3

---

### `SetLeftTop()`

```cpp
void BRect::SetLeftTop(const BPoint point)
```

Sets the left top *point* of the [BRect](classBRect.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The *point* to set. |





**Since:** BeOS R3

---

### `SetRightBottom()`

```cpp
void BRect::SetRightBottom(const BPoint point)
```

Sets the right bottom *point* of the [BRect](classBRect.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The *point* to set. |





**Since:** BeOS R3

---

### `SetRightTop()`

```cpp
void BRect::SetRightTop(const BPoint point)
```

Sets the right top *point* of the [BRect](classBRect.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The *point* to set. |





**Since:** BeOS R3

---

### `Size()`

```cpp
BSize BRect::Size()const
```

Returns the dimensions of the [BRect](classBRect.md). 



**Returns:** The dimensions of the [BRect](classBRect.md) as a [BSize](classBSize.md).



**Since:** Haiku R1


References [bottom](classBRect.md#a58dffee4bce99e849468e97fa926cfce), [left](classBRect.md#a177c8a67d9ebe9af16620a4eaa7915cf), [right](classBRect.md#aa9d294e406cc08595d4eb012b2ce5e5a), and [top](classBRect.md#ac5b5e678515645c6f4becf57448120ab).

---

### `Width()`

```cpp
float BRect::Width()const
```

Returns the width of the rectangle. 



**Returns:** The width of the rectangle as a float.


References [left](classBRect.md#a177c8a67d9ebe9af16620a4eaa7915cf), and [right](classBRect.md#aa9d294e406cc08595d4eb012b2ce5e5a).

---

### `bottom`

```cpp
BRect::bottom
```

The value of the rectangle's bottom edge. 



**Since:** BeOS R3


Referenced by [Height()](classBRect.md#aca81521a6170bdc66bf1cefa79ad3609), [IntegerHeight()](classBRect.md#a9b163b3d07d27dd23130781bde483bd9), [IsValid()](classBRect.md#af3e701c7a92ea7379943ce2cc1d66a79), [LeftBottom()](classBRect.md#aeea8c62fa651880f159793ae7da5054a), [operator=()](classBRect.md#a18e7aca7fd299b5767b1468f3089b3fa), [Set()](classBRect.md#a7ad2bdde464155de1bdf38db91bceca3), and [Size()](classBRect.md#a903279542b3a58bf10fd6d8b259f725b).

---

### `left`

```cpp
BRect::left
```

The value of the rectangle's left edge. 



**Since:** BeOS R3


Referenced by [IntegerWidth()](classBRect.md#ae52162fc1adc048605ec958c298417cd), [IsValid()](classBRect.md#af3e701c7a92ea7379943ce2cc1d66a79), [LeftBottom()](classBRect.md#aeea8c62fa651880f159793ae7da5054a), [LeftTop()](classBRect.md#a39cb030731bbc8b0e82e04ed563d4340), [operator=()](classBRect.md#a18e7aca7fd299b5767b1468f3089b3fa), [Set()](classBRect.md#a7ad2bdde464155de1bdf38db91bceca3), [Size()](classBRect.md#a903279542b3a58bf10fd6d8b259f725b), and [Width()](classBRect.md#aaa68bc8c6101c25b021dcae20c01960a).

---

### `right`

```cpp
BRect::right
```

The value of the rectangle's right edge. 



**Since:** BeOS R3


Referenced by [IntegerWidth()](classBRect.md#ae52162fc1adc048605ec958c298417cd), [IsValid()](classBRect.md#af3e701c7a92ea7379943ce2cc1d66a79), [operator=()](classBRect.md#a18e7aca7fd299b5767b1468f3089b3fa), [RightBottom()](classBRect.md#a7e52511bb18f8e22d1bdd7d9c01b6a39), [RightTop()](classBRect.md#af66a48189605a69edf987720ad5fa635), [Set()](classBRect.md#a7ad2bdde464155de1bdf38db91bceca3), [Size()](classBRect.md#a903279542b3a58bf10fd6d8b259f725b), and [Width()](classBRect.md#aaa68bc8c6101c25b021dcae20c01960a).

---

### `top`

```cpp
BRect::top
```

The value of the rectangle's top edge. 



**Since:** BeOS R3


Referenced by [Height()](classBRect.md#aca81521a6170bdc66bf1cefa79ad3609), [IntegerHeight()](classBRect.md#a9b163b3d07d27dd23130781bde483bd9), [IsValid()](classBRect.md#af3e701c7a92ea7379943ce2cc1d66a79), [operator=()](classBRect.md#a18e7aca7fd299b5767b1468f3089b3fa), [RightTop()](classBRect.md#af66a48189605a69edf987720ad5fa635), [Set()](classBRect.md#a7ad2bdde464155de1bdf38db91bceca3), and [Size()](classBRect.md#a903279542b3a58bf10fd6d8b259f725b).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBRect.html).
