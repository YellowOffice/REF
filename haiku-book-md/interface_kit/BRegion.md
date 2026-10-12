---
name: BRegion
type: class
kit: interface_kit
brief: "An area composed of rectangles"
source: haiku-book
---

# BRegion Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

An area composed of rectangles. 


The rectangles do not need to overlap. This class is useful for creating clipping masks.



> [!WARNING]
> [BRegion](classBRegion.md) is designed to be used with integral coordinates only.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BRegion](#a7e2dbbec42e8891a69d4ba663aaa80e9) () — Initializes an empty region. The region contains no rectangles, and its bounds are invalid.
* [BRegion](#a2a66bf43339ff0dcf20d51e494b5fd2c) (const BRect rect) — Initializes a region to contain a rect.
* [BRegion](#af595eadeb97cc1fb7a027a6a34b5010e) (const BRegion &other) — Initializes a region as a copy of other.
* `virtual` [~BRegion](#a63437394f71585ab815bcc409db0a748) () — Destroys the BRegion freeing any memory allocated by it.
* `bool` [Contains](#ac5ec6b249865caa8da950fe6752585f2) (BPoint point) const — Returns whether or not if the region contains the given point.
* `bool` [Contains](#a5250e6954c464d7715bbdb55cd813347) (int32 x, int32 y) — Returns whether or not the region contains the given coordinates.
* `bool` [Contains](#af03b71a7cc5140f88221abb5145ce2dd) (int32 x, int32 y) const — Return whether or not the region contains the given coordinates.
* `int32` [CountRects](#ae1bf831e6482828a2ec47118806dff96) () — Returns the number of rectangles contained in the region.
* `int32` [CountRects](#a54a4a57f4d638e50b8cc83a854d7edab) () const — Returns the number of rectangles contained in the region.
* `void` [Exclude](#a9bd228331fe056ac7c6e320e561c5d43) (BRect rect) — Modifies the region excluding the area of the given rect.
* `void` [Exclude](#a94ac7e39ced930992a055f49a1d9d8ac) (clipping_rect clipping) — Modifies the region excluding the area of the given clipping rectangle.
* `void` [Exclude](#a82519f0df83c965841589567e2c89af0) (const BRegion *region) — Modifies the region excluding the area contained by the given region.
* `void` [ExclusiveInclude](#ae581bbadfb610cdaf9c019505976565b) (const BRegion *region) — Modifies the region so that it contains only the area which the BRegion and region do NOT have in common.
* `BRect` [Frame](#ad7f1cba70c1fce88291b70b4ff1fb455) () const — Returns a rectangle that encloses the BRegion.
* `clipping_rect` [FrameInt](#a159da8dc4f9756d60e18a6d0be467c2a) () const — Returns the bounds of the region as a clipping_rect (which has integer coordinates).
* `void` [Include](#a9dff47818a7d5aa679316ce15395a4df) (BRect rect) — Modifies the region so that it includes the given rect.
* `void` [Include](#ad28b6747c731733f8e4849aed4b80f05) (clipping_rect clipping) — Modifies the region so that it includes the given clipping rectangle.
* `void` [Include](#accebfca3556d27adf1bea45c5726104d) (const BRegion *region) — Modifies the region to include the area of the given region.
* `bool` [Intersects](#a72d7028553a319a07cad042500b1fedc) (BRect rect) const — Returns whether or not the region has any area in common with rect.
* `bool` [Intersects](#a3968004110456b591b5d57088667b16a) (clipping_rect clipping) const — Returns whether or not the region has any area in common with clipping.
* `void` [IntersectWith](#acb9334810e022225f2dde3387113ba1d) (const BRegion *region) — Modifies the region, so that it will contain only the area in common with region.
* `void` [MakeEmpty](#a80c4adc8af0be406eb93ac3be6b9c974) () — Empties the region so that it doesn't containt any rects, and invalidates its bounds.
* `void` [OffsetBy](#ac67b9f13dd014b8d878777f84e6707be) (const BPoint &point) — Applies the given offsets given by the x and y coordinates of point to each rectangle contained in the region and recalculates the region's bounds.
* `void` [OffsetBy](#a9834ddaf5c57a59336f73be8a59359ff) (int32 x, int32 y) — Applies the given x and y offsets to each rectangle contained in the region and recalculates the region's bounds.
* `void` [PrintToStream](#a7a03684ac6222a879520756f1f055e86) () const — Prints each rect in the the BRegion to standard output.
* `BRect` [RectAt](#ab6dac50d37813cc2040647aa31c6c272) (int32 index) — Returns the rectangle contained in the region at the given index.
* `BRect` [RectAt](#a286dadbfd8551f17f0f5daebce1e5e38) (int32 index) const — Returns the rectangle contained in the region at the given index.
* `clipping_rect` [RectAtInt](#aa7a2c1714034f92aab812245b68ed3e7) (int32 index) — Returns the clipping_rect contained in the region at the given index.
* `clipping_rect` [RectAtInt](#a0af40dc7dc7b76172ba5b75056b935b6) (int32 index) const — Returns the clipping_rect contained in the region at the given index.
* `void` [ScaleBy](#ada9797eac56d69d41d46570701cf3f6a) (BSize scale) — Resize each of the contained rectangles by the given factor and recalculates the region's bounds.
* `void` [ScaleBy](#a4a49d3cc8249eb64d953353955f44f50) (float x, float y) — Resize each of the contained rectangles by the given factors and recalculates the region's bounds.
* `void` [Set](#a43e6180761175f1398885d8828385182) (BRect rect) — Set the region to bounds of newBounds.
* `void` [Set](#af645a90814cfeb2b13345fa59f049f95) (clipping_rect clipping) — Set the region to the bounds of clipping_rect.
* `BRegion &` [operator=](#add50fc8573429395207c289fbc44e6c3) (const BRegion &other) — Modifies the BRegion to be a copy of other.
* `bool` [operator==](#a12e4ebc4f6f2d52a81b525242541ed39) (const BRegion &other) const — Compares this region to other by value.

## Detailed Member Documentation

### `BRegion()`

```cpp
BRegion::BRegion()
```

Initializes an empty region. The region contains no rectangles, and its bounds are invalid. 



**Since:** BeOS R3

---

### `BRegion()`

```cpp
BRegion::BRegion(const BRegion & other)
```

Initializes a region as a copy of *other*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The region to copy. |





**Since:** BeOS R3

---

### `BRegion()`

```cpp
BRegion::BRegion(const BRect rect)
```

Initializes a region to contain a *rect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The [BRect](classBRect.md) to add to the region. |





**Since:** BeOS R5

---

### `~BRegion()`

```cpp
BRegion::~BRegion()
```

Destroys the [BRegion](classBRegion.md) freeing any memory allocated by it. 



**Since:** BeOS R3

---

### `Contains()`

```cpp
bool BRegion::Contains(BPoint point)const
```

Returns whether or not if the region contains the given *point*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The *point* to check. |





**Returns:** `true` if the region contains the *point*, `false` if not.



**Since:** BeOS R3

---

### `Contains()`

```cpp
bool BRegion::Contains(int32 x, int32 y)
```

Returns whether or not the region contains the given coordinates. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | The `x` coordinate of the point to check. |
| `y` | The `y` coordinate of the point to check. |





**Returns:** `true` if the region contains the point, `false` if not.



**Since:** Haiku R1

---

### `Contains()`

```cpp
bool BRegion::Contains(int32 x, int32 y)const
```

Return whether or not the region contains the given coordinates. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | The `x` coordinate of the point to check. |
| `y` | The `y` coordinate of the point to check. |





**Returns:** `true` if the region contains the point, `false` if not.



**Since:** Haiku R1

---

### `CountRects()`

```cpp
int32 BRegion::CountRects()
```

Returns the number of rectangles contained in the region. 



**Returns:** The number of rectangles in the region as an int32.



**Since:** BeOS R3

---

### `CountRects()`

```cpp
int32 BRegion::CountRects()const
```

Returns the number of rectangles contained in the region. 



**Returns:** The number of rectangles in the region as an int32.



**Since:** Haiku R1

---

### `Exclude()`

```cpp
void BRegion::Exclude(BRect rect)
```

Modifies the region excluding the area of the given *rect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The [BRect](classBRect.md) to be excluded. |





**Since:** BeOS R3

---

### `Exclude()`

```cpp
void BRegion::Exclude(clipping_rect clipping)
```

Modifies the region excluding the area of the given *clipping* rectangle. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `clipping` | The clipping_rect to be excluded. |





**Since:** Haiku R1

---

### `Exclude()`

```cpp
void BRegion::Exclude(const BRegion * region)
```

Modifies the region excluding the area contained by the given *region*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `region` | The [BRegion](classBRegion.md) to be excluded. |





**Since:** BeOS R3

---

### `ExclusiveInclude()`

```cpp
void BRegion::ExclusiveInclude(const BRegion * region)
```

Modifies the region so that it contains only the area which the [BRegion](classBRegion.md) and *region* do NOT have in common. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `region` | the [BRegion](classBRegion.md) to exclusively include. |





**Since:** Haiku R1

---

### `Frame()`

```cpp
BRect BRegion::Frame()const
```

Returns a rectangle that encloses the [BRegion](classBRegion.md). 



**Returns:** A [BRect](classBRect.md) that encloses the [BRegion](classBRegion.md).



**Since:** BeOS R3

---

### `FrameInt()`

```cpp
clipping_rect BRegion::FrameInt()const
```

Returns the bounds of the region as a clipping_rect (which has integer coordinates). 



**Returns:** The clipping_rect which represents the region's bounds.



**Since:** Haiku R1

---

### `Include()`

```cpp
void BRegion::Include(BRect rect)
```

Modifies the region so that it includes the given *rect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The [BRect](classBRect.md) to include in the region. |





**Since:** BeOS R3

---

### `Include()`

```cpp
void BRegion::Include(clipping_rect clipping)
```

Modifies the region so that it includes the given *clipping* rectangle. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `clipping` | The clipping_rect to include in the region. |





**Since:** Haiku R1

---

### `Include()`

```cpp
void BRegion::Include(const BRegion * region)
```

Modifies the region to include the area of the given *region*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `region` | The *region* to be included. |





**Since:** BeOS R3

---

### `Intersects()`

```cpp
bool BRegion::Intersects(BRect rect)const
```

Returns whether or not the region has any area in common with *rect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The [BRect](classBRect.md) to check the region against. |





**Returns:** `true` if the region has any area in common with the [BRect](classBRect.md), `false` if not.



**Since:** BeOS R3

---

### `Intersects()`

```cpp
bool BRegion::Intersects(clipping_rect clipping)const
```

Returns whether or not the region has any area in common with *clipping*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `clipping` | The clipping_rect to check the region against. |





**Returns:** `true` if the region has any area in common with the clipping_rect, `false` if not.



**Since:** Haiku R1

---

### `IntersectWith()`

```cpp
void BRegion::IntersectWith(const BRegion * region)
```

Modifies the region, so that it will contain only the area in common with *region*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `region` | the [BRegion](classBRegion.md) to intersect with. |





**Since:** BeOS R3

---

### `MakeEmpty()`

```cpp
void BRegion::MakeEmpty()
```

Empties the region so that it doesn't containt any rects, and invalidates its bounds. 



**Since:** BeOS R3

---

### `OffsetBy()`

```cpp
void BRegion::OffsetBy(const BPoint & point)
```

Applies the given offsets given by the x and y coordinates of *point* to each rectangle contained in the region and recalculates the region's bounds. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The point to get the coordinates to offset by. |





**Since:** Haiku R1

---

### `OffsetBy()`

```cpp
void BRegion::OffsetBy(int32 x, int32 y)
```

Applies the given *x* and *y* offsets to each rectangle contained in the region and recalculates the region's bounds. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | The horizontal offset. |
| `y` | The vertical offset. |





**Since:** BeOS R3

---

### `operator=()`

```cpp
BRegion & BRegion::operator=(const BRegion & other)
```

Modifies the [BRegion](classBRegion.md) to be a copy of *other*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | the [BRegion](classBRegion.md) to copy. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R3

---

### `operator==()`

```cpp
bool BRegion::operator==(const BRegion & other)const
```

Compares this region to *other* by value. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | the [BRegion](classBRegion.md) to compare to. |





**Returns:** `true` if the regions are the same, `false` otherwise.



**Since:** BeOS R3

---

### `PrintToStream()`

```cpp
void BRegion::PrintToStream()const
```

Prints each rect in the the [BRegion](classBRegion.md) to standard output. 



**Since:** BeOS R3

---

### `RectAt()`

```cpp
BRect BRegion::RectAt(int32 index)
```

Returns the rectangle contained in the region at the given *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index of the [BRect](classBRect.md) to retreive. |





**Returns:** If the given index is valid, it returns the [BRect](classBRect.md) at that index, otherwise, it returns an invalid [BRect](classBRect.md).



**Since:** BeOS R3

---

### `RectAt()`

```cpp
BRect BRegion::RectAt(int32 index)const
```

Returns the rectangle contained in the region at the given *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index of the [BRect](classBRect.md) to retreive. (zero based) |





**Returns:** If the given index is valid, it returns the [BRect](classBRect.md) at that index, otherwise, it returns an invalid [BRect](classBRect.md).



**Since:** Haiku R1

---

### `RectAtInt()`

```cpp
clipping_rect BRegion::RectAtInt(int32 index)
```

Returns the clipping_rect contained in the region at the given *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index of the clipping_rect to retrieve. (zero based) |





**Returns:** If the given index is valid, it returns the clipping_rect at that index, otherwise, it returns an invalid clipping_rect.



**Since:** Haiku R1

---

### `RectAtInt()`

```cpp
clipping_rect BRegion::RectAtInt(int32 index)const
```

Returns the clipping_rect contained in the region at the given *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index of the clipping_rect to retrieve. (zero based) |





**Returns:** If the given index is valid, it returns the clipping_rect at that index, otherwise, it returns an invalid clipping_rect.



**Since:** Haiku R1

---

### `ScaleBy()`

```cpp
void BRegion::ScaleBy(BSize scale)
```

Resize each of the contained rectangles by the given factor and recalculates the region's bounds. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `scale` | The scale factor |





**Since:** Haiku R1

---

### `ScaleBy()`

```cpp
void BRegion::ScaleBy(float x, float y)
```

Resize each of the contained rectangles by the given factors and recalculates the region's bounds. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | The horizontal scale. |
| `y` | The vertical scale. |





**Since:** Haiku R1

---

### `Set()`

```cpp
void BRegion::Set(BRect rect)
```

Set the region to bounds of *newBounds*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The [BRect](classBRect.md) to set the bounds to. |





**Since:** BeOS R3

---

### `Set()`

```cpp
void BRegion::Set(clipping_rect clipping)
```

Set the region to the bounds of *clipping_rect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `clipping` | The clipping_rect to set the bounds to. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBRegion.html).
