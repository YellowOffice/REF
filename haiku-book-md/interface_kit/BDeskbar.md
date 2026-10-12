---
name: BDeskbar
type: class
kit: interface_kit
brief: "Undocumented class"
source: haiku-book
---

# BDeskbar Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Undocumented class. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BDeskbar](#accf8f56f13e055a0731fda3273c0e1b1) () — Undocumented public method.
* [~BDeskbar](#ab7e2d9d3e7ae6a9a9135067110ffb8f1) () — Undocumented public method.
* `status_t` [AddItem](#a7cbb95ec5aa64eae7837a459d1cee612) (BView *archivableView, int32 *_id=NULL) — Undocumented public method.
* `status_t` [AddItem](#a64b7ccd996410b467974730fdfc2ca00) (entry_ref *addOn, int32 *_id=NULL) — Undocumented public method.
* `uint32` [CountItems](#a7453778f4d7fda742380de1f2543a5f1) () const — Undocumented public method.
* `status_t` [Expand](#a6ac06ba0753dbd89971971d4612704f3) (bool expand) — Undocumented public method.
* `BRect` [Frame](#a3167b8fa927ed84a3d432eaeda434fb8) () const — Undocumented public method.
* `status_t` [GetItemInfo](#a6acae26302449a61ce11aa8f9343fa98) (const char *name, int32 *_id) const — Undocumented public method.
* `status_t` [GetItemInfo](#a12a639ac5ba6d1ab839205bed1ed8843) (int32 id, const char **_name) const — Undocumented public method.
* `bool` [HasItem](#a6e16dc7ffd84b2dbaeb3346ba51f7b7c) (const char *name) const — Undocumented public method.
* `bool` [HasItem](#ab2fa890995267e6403bd34ebbf02bb35) (int32 id) const — Undocumented public method.
* `bool` [IsAlwaysOnTop](#ac806c34f99d8ddb2f48c51c7a7d52ef8) () const — Undocumented public method.
* `bool` [IsAutoHide](#a8ba2cdfdf7a001777c470ace069950e5) () const — Undocumented public method.
* `bool` [IsAutoRaise](#acbe4f90ff1732b0d931eb9c99f7968a6) () const — Undocumented public method.
* `bool` [IsExpanded](#ae3661ba6d68d5a9550d47f0b218d2807) () const — Undocumented public method.
* `bool` [IsRunning](#ae596bcca9c71130d558e900aff7d5c84) () const — Undocumented public method.
* `deskbar_location` [Location](#a72e4660e00f5d328f4e1d44a5c065100) (bool *_isExpanded=NULL) const — Undocumented public method.
* `float` [MaxItemHeight](#ab236b67935143956e9207d1f8a633dc6) () const — Undocumented public method.
* `float` [MaxItemWidth](#acb19e5a65a3de0e815fd3b81fc871cdb) () const — Undocumented public method.
* `status_t` [RemoveItem](#ae99b258f63f46e61103cc9abef8b9755) (const char *name) — Undocumented public method.
* `status_t` [RemoveItem](#a8d043bae10399c0948db88a61d4acee4) (int32 id) — Undocumented public method.
* `status_t` [SetAlwaysOnTop](#ad40c21ffbe88b5124f8d03215a6ce9a1) (bool alwaysOnTop) — Undocumented public method.
* `status_t` [SetAutoHide](#ac2cd5c003cb4b9425047a64c12758468) (bool autoHide) — Undocumented public method.
* `status_t` [SetAutoRaise](#a337a2a121bf3be628d38ca72c4ab7059) (bool autoRaise) — Undocumented public method.
* `status_t` [SetLocation](#a8a9890d6b225c2ecf155ab7792cd53b4) (deskbar_location location, bool expanded=false) — Undocumented public method.

## Detailed Member Documentation

### `BDeskbar()`

```cpp
BDeskbar::BDeskbar()
```

Undocumented public method. 



**Since:** Haiku R1

---

### `~BDeskbar()`

```cpp
BDeskbar::~BDeskbar()
```

Undocumented public method. 



**Since:** Haiku R1

---

### `AddItem()`

```cpp
status_t BDeskbar::AddItem(BView * archivableView, int32 * _id = NULL)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archivableView` | Undocumented |
| `_id` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `AddItem()`

```cpp
status_t BDeskbar::AddItem(entry_ref * addOn, int32 * _id = NULL)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `addOn` | Undocumented |
| `_id` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `CountItems()`

```cpp
uint32 BDeskbar::CountItems()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Expand()`

```cpp
status_t BDeskbar::Expand(bool expand)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `expand` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Frame()`

```cpp
BRect BDeskbar::Frame()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `GetItemInfo()`

```cpp
status_t BDeskbar::GetItemInfo(const char * name, int32 * _id)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | Undocumented |
| `_id` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `GetItemInfo()`

```cpp
status_t BDeskbar::GetItemInfo(int32 id, const char ** _name)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `id` | Undocumented |
| `_name` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `HasItem()`

```cpp
bool BDeskbar::HasItem(const char * name)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `HasItem()`

```cpp
bool BDeskbar::HasItem(int32 id)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `id` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `IsAlwaysOnTop()`

```cpp
bool BDeskbar::IsAlwaysOnTop()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `IsAutoHide()`

```cpp
bool BDeskbar::IsAutoHide()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `IsAutoRaise()`

```cpp
bool BDeskbar::IsAutoRaise()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `IsExpanded()`

```cpp
bool BDeskbar::IsExpanded()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `IsRunning()`

```cpp
bool BDeskbar::IsRunning()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Location()`

```cpp
deskbar_location BDeskbar::Location(bool * _isExpanded = NULL)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `_isExpanded` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `MaxItemHeight()`

```cpp
float BDeskbar::MaxItemHeight()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `MaxItemWidth()`

```cpp
float BDeskbar::MaxItemWidth()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `RemoveItem()`

```cpp
status_t BDeskbar::RemoveItem(const char * name)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `RemoveItem()`

```cpp
status_t BDeskbar::RemoveItem(int32 id)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `id` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `SetAlwaysOnTop()`

```cpp
status_t BDeskbar::SetAlwaysOnTop(bool alwaysOnTop)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `alwaysOnTop` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `SetAutoHide()`

```cpp
status_t BDeskbar::SetAutoHide(bool autoHide)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `autoHide` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `SetAutoRaise()`

```cpp
status_t BDeskbar::SetAutoRaise(bool autoRaise)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `autoRaise` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `SetLocation()`

```cpp
status_t BDeskbar::SetLocation(deskbar_location location, bool expanded = false)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `location` | Undocumented |
| `expanded` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBDeskbar.html).
