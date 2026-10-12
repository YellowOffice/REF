---
name: BPolygon
type: class
kit: interface_kit
brief: "A closed, many-sided figure which defines an area in a two-dimensional Cartesian coordinate system"
source: haiku-book
---

# BPolygon Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A closed, many-sided figure which defines an area in a two-dimensional Cartesian coordinate system. 


A [BPolygon](classBPolygon.md) is defined as a set of [BPoint](classBPoint.md) objects, each [BPoint](classBPoint.md) represents a vertex of the polygon. Unlike a [BRect](classBRect.md), a [BPolygon](classBPolygon.md) can can have any number of sides and the sides don't have to be aligned on coordinate axes.


[BPolygon](classBPolygon.md) objects are most commonly used for drawing. [BView::StrokePolygon()](classBView.md#ae871d03592c1bba5d6be3d5d982ea747) and [BView::FillPolygon()](classBView.md#ae72733cae8a1fc2da8feb47c0c2149fa) allow you to draw a polygon in a [BView](classBView.md) by taking a [BPolygon](classBPolygon.md) object as an argument.



**See also:** [BView::StrokePolygon()](classBView.md#ae871d03592c1bba5d6be3d5d982ea747)



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BPolygon](#a1999696becac03b18ee5b788219f9e72) () — Initializes an empty polygon without any points.
* [BPolygon](#afa50735acb1d1b7bbcbdf286a30d87d0) (const BPoint *points, int32 count) — Initializes a new BPolygon object from an array of points.
* [BPolygon](#a5d001b01ce94f98fee127715ef2e8399) (const BPolygon &other) — Initializes a new BPolygon object from another BPolygon and copies the list of BPoint objects from other.
* [BPolygon](#ac4f1a99f37a2ab9aeb1978aa7170eb47) (const BPolygon *other) — Initializes a new BPolygon object from a pointer to another BPolygon and copies the list of BPoint objects from other.
* `virtual` [~BPolygon](#a0736e9f6a4a7831671b6460429e8deba) () — Destroys the object and frees the memory used by the associated BPoint objects.
* `void` [AddPoints](#a385666513c5f239e5d48b32d3365a01a) (const BPoint *points, int32 count) — Adds an array of BPoint objects.
* `int32` [CountPoints](#a56c8c5a268f1d12986f3a5bd7584e545) () const — Returns the number of points associated with the polygon.
* `BRect` [Frame](#adcba7cd85d9ccb6d5da915c19e56c21f) () const — Returns the frame rectangle that encloses the BPolygon object.
* `void` [MapTo](#ab7b196c1ddc62166cb8ed56d03d896ce) (BRect source, BRect destination) — Modifies each BPoint in the BPolygon so that the shape fits inside the destination rectangle.
* `BPolygon &` [operator=](#a4e2c7547f8bc0c76e0d5f566ca0f457d) (const BPolygon &other) — Initializes a new BPolygon object and copies the list of BPoint objects from other.
* `void` [PrintToStream](#a04fcd873a28cdad4a81cefc1012dc556) () const — Prints each of the points of the BPolygon to standard output.

## Detailed Member Documentation

### `BPolygon()`

```cpp
BPolygon::BPolygon(const BPoint * points, int32 count)
```

Initializes a new [BPolygon](classBPolygon.md) object from an array of *points*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `points` | The array of [BPoint](classBPoint.md) objects to add. |
| `count` | The number of [BPoint](classBPoint.md) objects in the array. |





**Since:** BeOS R3

---

### `BPolygon()`

```cpp
BPolygon::BPolygon(const BPolygon & other)
```

Initializes a new [BPolygon](classBPolygon.md) object from another [BPolygon](classBPolygon.md) and copies the list of [BPoint](classBPoint.md) objects from *other*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BPolygon](classBPolygon.md) object to copy from. |





**Since:** Haiku R1

---

### `BPolygon()`

```cpp
BPolygon::BPolygon(const BPolygon * other)
```

Initializes a new [BPolygon](classBPolygon.md) object from a pointer to another [BPolygon](classBPolygon.md) and copies the list of [BPoint](classBPoint.md) objects from *other*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | A pointer to a [BPolygon](classBPolygon.md) object to copy from. |





**Since:** BeOS R3

---

### `BPolygon()`

```cpp
BPolygon::BPolygon()
```

Initializes an empty polygon without any points. 



**See also:** [BPolygon::AddPoints()](classBPolygon.md#a385666513c5f239e5d48b32d3365a01a) to add points to the [BPolygon](classBPolygon.md).



**Since:** BeOS R3

---

### `~BPolygon()`

```cpp
BPolygon::~BPolygon()
```

Destroys the object and frees the memory used by the associated [BPoint](classBPoint.md) objects. 



**Since:** BeOS R3

---

### `AddPoints()`

```cpp
void BPolygon::AddPoints(const BPoint * points, int32 count)
```

Adds an array of [BPoint](classBPoint.md) objects. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `points` | The array of [BPoint](classBPoint.md) objects to add. |
| `count` | The number of [BPoint](classBPoint.md) objects in the array. |





**Since:** BeOS R3

---

### `CountPoints()`

```cpp
int32 BPolygon::CountPoints()const
```

Returns the number of points associated with the polygon. 



**Since:** BeOS R3

---

### `Frame()`

```cpp
BRect BPolygon::Frame()const
```

Returns the frame rectangle that encloses the [BPolygon](classBPolygon.md) object. 



**Since:** BeOS R3

---

### `MapTo()`

```cpp
void BPolygon::MapTo(BRect source, BRect destination)
```

Modifies each [BPoint](classBPoint.md) in the [BPolygon](classBPolygon.md) so that the shape fits inside the *destination* rectangle. 


The *source* rectangle is used so that the points are mapped proportionally. To modify a polygon so that it is inscribed in the *destination* rectangle exactly, pass the frame rectangle as the *source*.



**Since:** BeOS R3

---

### `operator=()`

```cpp
BPolygon & BPolygon::operator=(const BPolygon & other)
```

Initializes a new [BPolygon](classBPolygon.md) object and copies the list of [BPoint](classBPoint.md) objects from *other*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BPolygon](classBPolygon.md) object to copy from. |





**Since:** BeOS R3

---

### `PrintToStream()`

```cpp
void BPolygon::PrintToStream()const
```

Prints each of the points of the [BPolygon](classBPolygon.md) to standard output. 



**See also:** [BPoint::PrintToStream()](classBPoint.md#a18a683442d46d96f940caf72989c139e)



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPolygon.html).
