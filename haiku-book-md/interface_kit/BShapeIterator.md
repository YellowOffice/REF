---
name: BShapeIterator
type: class
kit: interface_kit
brief: "Allows you to iterate through BShape operations"
source: haiku-book
---

# BShapeIterator Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Allows you to iterate through [BShape](classBShape.md) operations. 


You should override this class and implement the [IterateMoveTo()](classBShapeIterator.md#a7d6f517a72417e91e5d071e01166826c), [IterateLineTo()](classBShapeIterator.md#aadfce4825458bfcaa3255c22423e02d4), [IterateBezierTo()](classBShapeIterator.md#aec88187a4c636b8515dccef965c3b25b), [IterateClose()](classBShapeIterator.md#abd832aedee4ce794d4b6e8676b15ec3e), and [IterateArcTo()](classBShapeIterator.md#afeaf8241a4fa83028d09640ab959fd92) methods which correspond to [BShape::MoveTo()](classBShape.md#a1c09ecefdcf97647be144a296768d3a8), [BShape::LineTo()](classBShape.md#ad4d566bb4953c3c3861a2d3d9d13deda), [BShape::BezierTo()](classBShape.md#a7cb0066ad12c01792af8db55d0e63d29), [BShape::Close()](classBShape.md#aac2250db6c8e504433b4a7665623640b) and [BShape::ArcTo()](classBShape.md#ac6c84ff1042d4896a9a2a06fe06a3281) respectively.



**See also:** [BShape](classBShape.md)



**Since:** BeOS R4

## Member List

### Public Member Functions

* [BShapeIterator](#af75e4b21ce367ff43dbc4f5280ad4adc) () — Constructor, does nothing.
* `virtual` [~BShapeIterator](#acf898961872f144f8b8a1a8fa96c1d02) () — Destructor, does nothing.
* `status_t` [Iterate](#a21d75abfba3c3a8d7735ab0c865aec92) (BShape *shape) — Iterates over each operation that make up the BShape calling IterateMoveTo(), IterateLineTo(), IterateBezierTo(), IterateClose() or IterateArcTo() depending on the operation.
* `virtual status_t` [IterateArcTo](#afeaf8241a4fa83028d09640ab959fd92) (float &rx, float &ry, float &angle, bool largeArc, bool counterClockWise, BPoint &point) — Called by Iterate() to act on an arc.
* `virtual status_t` [IterateBezierTo](#aec88187a4c636b8515dccef965c3b25b) (int32 bezierCount, BPoint *bezierPoints) — Called by Iterate() to act on bezierCount Bézier curves comprised of the points specified by bezierPoints.
* `virtual status_t` [IterateClose](#abd832aedee4ce794d4b6e8676b15ec3e) () — Called by Iterate() to close the BShape.
* `virtual status_t` [IterateLineTo](#aadfce4825458bfcaa3255c22423e02d4) (int32 lineCount, BPoint *linePoints) — Called by Iterate() to act on lineCount lines comprised of the points specified by linePoints.
* `virtual status_t` [IterateMoveTo](#a7d6f517a72417e91e5d071e01166826c) (BPoint *point) — Called by Iterate() to act on point.

## Detailed Member Documentation

### `BShapeIterator()`

```cpp
BShapeIterator::BShapeIterator()
```

Constructor, does nothing. 


This method does nothing and should be implemented by derived classes.



**Since:** BeOS R4

---

### `~BShapeIterator()`

```cpp
BShapeIterator::~BShapeIterator()
```

Destructor, does nothing. 


This method does nothing and should be implemented by derived classes.



**Since:** BeOS R4

---

### `Iterate()`

```cpp
status_t BShapeIterator::Iterate(BShape * shape)
```

Iterates over each operation that make up the [BShape](classBShape.md) calling [IterateMoveTo()](classBShapeIterator.md#a7d6f517a72417e91e5d071e01166826c), [IterateLineTo()](classBShapeIterator.md#aadfce4825458bfcaa3255c22423e02d4), [IterateBezierTo()](classBShapeIterator.md#aec88187a4c636b8515dccef965c3b25b), [IterateClose()](classBShapeIterator.md#abd832aedee4ce794d4b6e8676b15ec3e) or [IterateArcTo()](classBShapeIterator.md#afeaf8241a4fa83028d09640ab959fd92) depending on the operation. 


shape The [BShape](classBShape.md) object to iterate through.



**Returns:** Always returns `B_OK`. You should override this method to return an appropriate status code.



**Since:** BeOS R4

---

### `IterateArcTo()`

```cpp
status_t BShapeIterator::IterateArcTo(float & rx, float & ry, float & angle, bool largeArc, bool counterClockWise, BPoint & point)
```

Called by [Iterate()](classBShapeIterator.md#a21d75abfba3c3a8d7735ab0c865aec92) to act on an arc. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rx` | The horizontal radius of the arc to act on. |
| `ry` | The vertical radius of the arc to act on. |
| `angle` | The starting angle of the arc in degrees to act on. |
| `largeArc` | Whether or not to draw a large arc. |
| `counterClockWise` | `true` if the arc is drawn counter-clockwise, `false` if the arc is drawn clockwise. |
| `point` | The center point of the arc to act on. |




This method does nothing and should be implemented by derived classes.



**Returns:** Always returns `B_OK`. You should override this method to return an appropriate status code.



**Since:** Haiku R1

---

### `IterateBezierTo()`

```cpp
status_t BShapeIterator::IterateBezierTo(int32 bezierCount, BPoint * bezierPoints)
```

Called by [Iterate()](classBShapeIterator.md#a21d75abfba3c3a8d7735ab0c865aec92) to act on *bezierCount* Bézier curves comprised of the points specified by *bezierPoints*. 


This method does nothing and should be implemented by derived classes.


Parameters

| Parameter | Description |
| :--- | :--- |
| `bezierCount` | The number of points in *bezierPoints*. |
| `bezierPoints` | The list of Bézier curve points to act on. |





**Returns:** Always returns `B_OK`. You should override this method to return an appropriate status code.



**Since:** BeOS R4

---

### `IterateClose()`

```cpp
status_t BShapeIterator::IterateClose()
```

Called by [Iterate()](classBShapeIterator.md#a21d75abfba3c3a8d7735ab0c865aec92) to close the [BShape](classBShape.md). 


This method does nothing and should be implemented by derived classes.



**Returns:** Always returns `B_OK`. You should override this method to return an appropriate status code.



**Since:** BeOS R4

---

### `IterateLineTo()`

```cpp
status_t BShapeIterator::IterateLineTo(int32 lineCount, BPoint * linePoints)
```

Called by [Iterate()](classBShapeIterator.md#a21d75abfba3c3a8d7735ab0c865aec92) to act on *lineCount* lines comprised of the points specified by *linePoints*. 


This method does nothing and should be implemented by derived classes.


Parameters

| Parameter | Description |
| :--- | :--- |
| `lineCount` | The number of points in *linePoints*. |
| `linePoints` | The list of points of lines to act on. |





**Returns:** Always returns `B_OK`. You should override this method to return an appropriate status code.



**Since:** BeOS R4

---

### `IterateMoveTo()`

```cpp
status_t BShapeIterator::IterateMoveTo(BPoint * point)
```

Called by [Iterate()](classBShapeIterator.md#a21d75abfba3c3a8d7735ab0c865aec92) to act on *point*. 


This method does nothing and should be implemented by derived classes.


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The point to act on. |





**Returns:** Always returns `B_OK`. You should override this method to return an appropriate status code.



**Since:** BeOS R4

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBShapeIterator.html).
