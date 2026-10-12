---
name: BShape
type: class
kit: interface_kit
brief: "Encapsulates a Postscript-style \"path\""
source: haiku-book
---

# BShape Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Encapsulates a Postscript-style "path". 


You can obtain the outlines of characters from a string as [BShape](classBShape.md) objects by calling [BFont::GetGlyphShapes()](classBFont.md#ac51729d5adbaabf69520f9d2342af1b1).



**Since:** BeOS R4

## Member List

### Public Member Functions

* [BShape](#abae1c1db14831afc4577871db976e77b) () — Creates an empty BShape object.
* [BShape](#a965f545110247b705c908415c47d43c5) (BMessage *archive) — Creates a new BShape message from an archive message.
* [BShape](#a08f57601a9d0bb9ef9a7f8a431c4c8aa) (const BShape &other) — Creates a new BShape object as a copy of other.
* `virtual` [~BShape](#afda42343ddb445d38691d91b8d284695) () — Destructor, deletes all associated data.
* `status_t` [AddShape](#a68e1fee470acccc5bec36605d2da3a10) (const BShape *other) — Adds the lines and curves of otherShape to BShape.
* `BRect` [Bounds](#a181832ed7c8e5f5913e4701b8a74c3e9) () const — Returns a BRect that encloses all points in the BShape.
* `void` [Clear](#a016b65b4f53273192d69952ab13df5bd) () — Deletes all data returning the BShape to an empty state.
* `BPoint` [CurrentPosition](#a774165c79f57ff3212680b8b761758be) () const — Returns the current end point of the path.
* `BShape &` [operator=](#afc519b158bc6600c4962980b49860b61) (const BShape &other) — Constructs a BShape object as a copy of other by overloading the = operator.
* `bool` [operator==](#aa7d10d99628a942c62be4863ef2422f3) (const BShape &other) const — Returns whether or not the contents of this BShape and other contain the same data.
* `bool` [operator!=](#a12875c68c295fd6e35eb551ba61ab7e8) (const BShape &other) const — Returns whether or not the contents of this BShape and other do NOT contain the same data.
* `status_t` [MoveTo](#a1c09ecefdcf97647be144a296768d3a8) (BPoint point) — Adds a "move to" operation to the BShape.
* `status_t` [LineTo](#ad4d566bb4953c3c3861a2d3d9d13deda) (BPoint linePoint) — Adds a "draw line" operation to the BShape.
* `status_t` [BezierTo](#a7cb0066ad12c01792af8db55d0e63d29) (BPoint controlPoints[3]) — Adds a "draw Bézier curve" operation to the BShape.
* `status_t` [BezierTo](#a2f9bbdaaf8c373f99f75e62933b165b1) (const BPoint &control1, const BPoint &control2, const BPoint &endPoint) — Adds a "draw Bézier curve" operation to the BShape.
* `status_t` [ArcTo](#ac6c84ff1042d4896a9a2a06fe06a3281) (float rx, float ry, float angle, bool largeArc, bool counterClockWise, const BPoint &point) — Adds a "draw arc" operation to the BShape.
* `status_t` [Close](#aac2250db6c8e504433b4a7665623640b) () — Adds an operation to close the BShape once it is fully constructed.
* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).

### Archiving

* `virtual status_t` [Archive](#ae132d554f4df208974b5019436ad1b36) (BMessage *archive, bool deep=true) const — Archives the BShape object to a BMessage.
* `static BArchivable *` [Instantiate](#a012debe8f24b7b5d69712f57a863923f) (BMessage *archive) — Creates a new BShape object from an archive message.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BShape()`

```cpp
BShape::BShape()
```

Creates an empty [BShape](classBShape.md) object. 



**Since:** BeOS R4

---

### `BShape()`

```cpp
BShape::BShape(const BShape & other)
```

Creates a new [BShape](classBShape.md) object as a copy of *other*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BShape](classBShape.md) object to copy from. |





**Since:** BeOS R4

---

### `BShape()`

```cpp
BShape::BShape(BMessage * archive)
```

Creates a new [BShape](classBShape.md) message from an *archive* message. 


You should call [Instantiate()](classBShape.md#a012debe8f24b7b5d69712f57a863923f) instead as it will validate whether or not the object was created successfully.


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The [BMessage](../application_kit/classBMessage.md) object to construct the data from. |





**Since:** BeOS R4

---

### `~BShape()`

```cpp
BShape::~BShape()
```

Destructor, deletes all associated data. 



**Since:** BeOS R4

---

### `AddShape()`

```cpp
status_t BShape::AddShape(const BShape * otherShape)
```

Adds the lines and curves of *otherShape* to [BShape](classBShape.md). 



**Returns:** Always returns `B_OK`.



**Since:** BeOS R4

---

### `Archive()`

```cpp
status_t BShape::Archive(BMessage * archive, bool deep = true)const
```

Archives the [BShape](classBShape.md) object to a [BMessage](../application_kit/classBMessage.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The [BMessage](../application_kit/classBMessage.md) object to archive the [BShape](classBShape.md) data to. |
| `deep` | Currently unused. |





**Returns:** A status code, `B_OK` on scucess or an error code otherwise.



**Since:** BeOS R4


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44).

---

### `ArcTo()`

```cpp
status_t BShape::ArcTo(float rx, float ry, float angle, bool largeArc, bool counterClockWise, const BPoint & point)
```

Adds a "draw arc" operation to the [BShape](classBShape.md). 


An arc is draw that begins at the current point and is specified by the parameters to this method.


Parameters

| Parameter | Description |
| :--- | :--- |
| `rx` | The horizontal radius of the arc. |
| `ry` | The vertical radius of the arc. |
| `angle` | The starting angle of the arc in degrees. |
| `largeArc` | Whether or not to draw a large arc. |
| `counterClockWise` | `true` to draw the arc counter-clockwise, `false` to draw the arc clockwise. |
| `point` | The center point of the arc. |





**Returns:** Returns a status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation was added successfully. |
| B_NO_MEMORY | Ran out of memory while trying to add the operation. |





**Since:** Haiku R1

---

### `BezierTo()`

```cpp
status_t BShape::BezierTo(BPoint controlPoints[3])
```

Adds a "draw Bézier curve" operation to the [BShape](classBShape.md). 


A Bézier curve is drawn that begins at the current point and is made up of the specified *controlPoints*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `controlPoints` | The points that make up the Bézier curve. |





**Returns:** Returns a status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation was added successfully. |
| B_NO_MEMORY | Ran out of memory while trying to add the operation. |





**Since:** BeOS R4

---

### `BezierTo()`

```cpp
status_t BShape::BezierTo(const BPoint & control1, const BPoint & control2, const BPoint & endPoint)
```

Adds a "draw Bézier curve" operation to the [BShape](classBShape.md). 


A Bézier curve is drawn that begins at the current point and is made up of the specified points.


Parameters

| Parameter | Description |
| :--- | :--- |
| `control1` | The first control point of the Bézier curve. |
| `control2` | The second control point of the Bézier curve. |
| `endPoint` | The end point of the Bézier curve. |





**Returns:** Returns a status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation was added successfully. |
| B_NO_MEMORY | Ran out of memory while trying to add the operation. |





**Since:** Haiku R1

---

### `Bounds()`

```cpp
BRect BShape::Bounds()const
```

Returns a [BRect](classBRect.md) that encloses all points in the [BShape](classBShape.md). 



> [!WARNING]
> This implementation doesn't take into account curves at all.



**Since:** BeOS R4

---

### `Clear()`

```cpp
void BShape::Clear()
```

Deletes all data returning the [BShape](classBShape.md) to an empty state. 



**Since:** BeOS R4

---

### `Close()`

```cpp
status_t BShape::Close()
```

Adds an operation to close the [BShape](classBShape.md) once it is fully constructed. 



**Returns:** Returns a status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation was added successfully. |
| B_NO_MEMORY | Ran out of memory while trying to add the operation. |





**Since:** BeOS R4

---

### `CurrentPosition()`

```cpp
BPoint BShape::CurrentPosition()const
```

Returns the current end point of the path. 



**Returns:** The current end point of the path or `B_ORIGIN` if no points have been added yet.



**Since:** Haiku R1

---

### `Instantiate()`

```cpp
BArchivable * BShape::Instantiate(BMessage * archive)
```

Creates a new [BShape](classBShape.md) object from an *archive* message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The [BMessage](../application_kit/classBMessage.md) object to construct the [BShape](classBShape.md) data from. |





**Returns:** A new [BShape](classBShape.md) object or `NULL` if *archive* was invalid.



**Since:** BeOS R4

---

### `LineTo()`

```cpp
status_t BShape::LineTo(BPoint point)
```

Adds a "draw line" operation to the [BShape](classBShape.md). 


A line will be drawn from the previous point to the *point* specified.


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The point to draw a line to starting at the previous location. |





**Returns:** Returns a status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation was added successfully. |
| B_NO_MEMORY | Ran out of memory while trying to add the operation. |





**Since:** BeOS R4

---

### `MoveTo()`

```cpp
status_t BShape::MoveTo(BPoint point)
```

Adds a "move to" operation to the [BShape](classBShape.md). 


The next [LineTo()](classBShape.md#ad4d566bb4953c3c3861a2d3d9d13deda) or [BezierTo()](classBShape.md#a7cb0066ad12c01792af8db55d0e63d29) will begin at *point* allowing you to create noncontiguous shapes.


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The point to start the next [LineTo()](classBShape.md#ad4d566bb4953c3c3861a2d3d9d13deda) or [BezierTo()](classBShape.md#a7cb0066ad12c01792af8db55d0e63d29) at. |





**Returns:** Returns a status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation was added successfully. |
| B_NO_MEMORY | Ran out of memory while trying to add the operation. |





**Since:** BeOS R4

---

### `operator!=()`

```cpp
bool BShape::operator!=(const BShape & other)const
```

Returns whether or not the contents of this [BShape](classBShape.md) and *other* do NOT contain the same data. 



**Returns:** `true` if the contents are NOT equal, `false` otherwise.



**Since:** Haiku R1

---

### `operator=()`

```cpp
BShape & BShape::operator=(const BShape & other)
```

Constructs a [BShape](classBShape.md) object as a copy of *other* by overloading the = operator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BShape](classBShape.md) object to copy from. |




Always returns *this.



**Since:** Haiku R1

---

### `operator==()`

```cpp
bool BShape::operator==(const BShape & other)const
```

Returns whether or not the contents of this [BShape](classBShape.md) and *other* contain the same data. 



**Returns:** `true` if the contents are equal, `false` otherwise.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBShape.html).
