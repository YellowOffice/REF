---
name: BListItem
type: class
kit: interface_kit
brief: "A list item, a member of a BListView or BOutlineListView"
source: haiku-book
---

# BListItem Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A list item, a member of a [BListView](classBListView.md) or [BOutlineListView](classBOutlineListView.md). 



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BListItem](#a73aeb0d40d0d41a8e3119d2aa9c81f76) (BMessage *archive) — Create a new list item from archived message.
* [BListItem](#af5b74e8991410be39e7dfa6960e6bd3a) (uint32 outlineLevel=0, bool expanded=true) — Create a new list item with the specified level.
* `virtual` [~BListItem](#a21ea0c88196a4a383485e73787da1a74) () — Destroy the list item freeing any memory used.
* `void` [Deselect](#aebcef421495d32b4048a29ef92ae2fd3) () — Unselect the list item.
* `float` [Height](#ac5ac9d274d9f8cacf7606e8c564299eb) () const — Return the height of the list item.
* `bool` [IsEnabled](#aac7de254077fe53441c4a8e110aabfca) () const — Returns whether or not the list item is currently enabled.
* `bool` [IsExpanded](#a6947bea2aff6fc64fceb6d724fd4e126) () const — Returns whether or not the list item is currently expanded.
* `bool` [IsSelected](#aeb958ab6a26b936f4c0169c5ff7c40a9) () const — Return whether or not the list item is currently selected.
* `uint32` [OutlineLevel](#aeeddbeae37ddef9b77c69a7a0f8d8b79) () const — Returns the current outline level of the list item. This only makes sense if the list item is part of a BOutlineListView.
* `virtual status_t` [Perform](#a4b764176db576c63b8bedda260c76f91) (perform_code code, void *arg) — Performs an action give a perform_code and arg. (Internal Method)
* `void` [Select](#ae15dad05ee58f72ba3334a72817103c1) () — Select the list item.
* `virtual void` [SetEnabled](#a06b78f86ce25d6420f0459be9aed4125) (bool enabled) — Enable or disable the list item.
* `void` [SetExpanded](#a527cc7876a66ba4047bf916e80e62aa4) (bool expanded) — Set the expanded state of the list item. This only makes sense if the list item is part of a BOutlineListView.
* `void` [SetHeight](#a637ad01974e7a9c44439fb88f2052f67) (float height) — Set the height of the list item to height.
* `void` [SetOutlineLevel](#a51af2b0dfc7694570de05f7aace2c474) (uint32 level) — Set the outline level of the list item.
* `void` [SetWidth](#a7c16ae3dff1e05749bd1fd5a2e2ca7d9) (float width) — Set the width of the list item to width.
* `virtual void` [Update](#a81b5b7fa5cbd942917ce7d3b5d1fe1e0) (BView *owner, const BFont *font) — Hook method that's called when the owner changes.
* `float` [Width](#a34b8798b40fb01aa1b45661f058123ef) () const — Return the width of the list item.
* `virtual status_t` [Archive](#a3fa7ca1250e123e3cf1488b1d88901d3) (BMessage *archive, bool deep=true) const — Archive the list item to a message.
* `virtual void` [DrawItem](#ac63fc6a6467a7130a174c643adf53c52) (BView *owner, BRect frame, bool complete=false)=0 — Hook method called when the item is drawn.
* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BListItem()`

```cpp
BListItem::BListItem(uint32 level = 0, bool expanded = true)
```

Create a new list item with the specified *level*. 


The *level* and *expanded* arguments are only used if the item is added to a [BOutlineListView](classBOutlineListView.md).


Parameters

| Parameter | Description |
| :--- | :--- |
| `level` | The level to create the list item on, default level is 0. |
| `expanded` | Whether or not the item is expanded. |





**See also:** [BOutlineListView::AddItem()](classBOutlineListView.md#abc985b1be1870818dd6d1b243204b999)



**Since:** BeOS R3

---

### `BListItem()`

```cpp
BListItem::BListItem(BMessage * data)
```

Create a new list item from archived message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The message to create the list item from. |





**Since:** BeOS R3

---

### `~BListItem()`

```cpp
BListItem::~BListItem()
```

Destroy the list item freeing any memory used. 


The default destructor is empty.



**Since:** BeOS R3

---

### `Archive()`

```cpp
status_t BListItem::Archive(BMessage * archive, bool deep = true)const
```

Archive the list item to a message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The message to archive the list item to. |
| `deep` | If `true` also archive child views. |





**Since:** BeOS R3


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44).


Reimplemented in [BStringItem](classBStringItem.md#acf33097176356dbfbe1229d40ca4453a).

---

### `Deselect()`

```cpp
void BListItem::Deselect()
```

Unselect the list item. 



**Since:** BeOS R3

---

### `DrawItem()`

```cpp
void BListItem::DrawItem(BView * owner, BRect frame, bool complete = false)
```

Hook method called when the item is drawn. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `owner` | The view that the list item is a child of. |
| `frame` | The frame of the item. |
| `complete` | Whether or not to draw the background in addition to the item's contents. |





**Since:** BeOS R3


Implemented in [BStringItem](classBStringItem.md#a06cd7b53357037f2dd98bdac8f025ae0).

---

### `Height()`

```cpp
float BListItem::Height()const
```

Return the height of the list item. 



**Returns:** The height of the list item as a float.



**Since:** BeOS R3

---

### `IsEnabled()`

```cpp
bool BListItem::IsEnabled()const
```

Returns whether or not the list item is currently enabled. 



**Returns:** `true` if the list item is enabled, `false` if it is disabled.



**Since:** BeOS R3

---

### `IsExpanded()`

```cpp
bool BListItem::IsExpanded()const
```

Returns whether or not the list item is currently expanded. 



**Returns:** `true` if the list item is expanded, `false` if it is not expanded.



**Since:** BeOS R3

---

### `IsSelected()`

```cpp
bool BListItem::IsSelected()const
```

Return whether or not the list item is currently selected. 



**Returns:** `true` if the list item is selected, `false` otherwise.



**Since:** BeOS R3

---

### `OutlineLevel()`

```cpp
uint32 BListItem::OutlineLevel()const
```

Returns the current outline level of the list item. This only makes sense if the list item is part of a [BOutlineListView](classBOutlineListView.md). 



**Returns:** The current outline level of the list item.



**Since:** BeOS R3

---

### `Perform()`

```cpp
status_t BListItem::Perform(perform_code d, void * arg)
```

Performs an action give a perform_code and arg. (Internal Method) 


Parameters

| Parameter | Description |
| :--- | :--- |
| `d` | The perform code. |
| `arg` | A pointer to some data to perform on. |





**Returns:** A status code.



**Since:** Haiku R1


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a827fa92febcf925f07545aa9777df9de).


Reimplemented in [BStringItem](classBStringItem.md#a68a5af5b0d0c958fa9528090c1ec6bcf).

---

### `Select()`

```cpp
void BListItem::Select()
```

Select the list item. 



**Since:** BeOS R3

---

### `SetEnabled()`

```cpp
void BListItem::SetEnabled(bool on)
```

Enable or disable the list item. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `on` | Set `true` to enable, `false` to disable the list item. |





**Since:** BeOS R3

---

### `SetExpanded()`

```cpp
void BListItem::SetExpanded(bool expanded)
```

Set the expanded state of the list item. This only makes sense if the list item is part of a [BOutlineListView](classBOutlineListView.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `expanded` | `true` to expand the list item, `false` to un-expand the list item. |





**Since:** BeOS R3

---

### `SetHeight()`

```cpp
void BListItem::SetHeight(float height)
```

Set the height of the list item to *height*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `height` | The height to set the list item to. |





> [!NOTE]
> Unlike BeOS, if you change the height then you need to force the [BListView](classBListView.md) to recalculate the cached tops of the item selection boxes, otherwise selection highlights will be drawn in the wrong places and mouse clicks will be misinterpreted. You can do this by adding and removing a dummy [BListItem](classBListItem.md) at the top of the list, or after hrev50780 by calling [BListView::FrameResized()](classBListView.md#af4fdd5e524c68a7aa318179c8a5acadd) with the current Frame rectangle (though the FrameResized() method will additionally call [BListItem::Update()](classBListItem.md#a81b5b7fa5cbd942917ce7d3b5d1fe1e0) for all items).



**Since:** BeOS R3

---

### `SetOutlineLevel()`

```cpp
void BListItem::SetOutlineLevel(uint32 level)
```

Set the outline level of the list item. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `level` | The outline level to set the list item to. |





**Since:** BeOS R3

---

### `SetWidth()`

```cpp
void BListItem::SetWidth(float width)
```

Set the width of the list item to *width*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `width` | The width to set the list item to. |





**Since:** BeOS R3

---

### `Update()`

```cpp
void BListItem::Update(BView * owner, const BFont * font)
```

Hook method that's called when the *owner* changes. 


This method gets called when the list item is added to the list view.


The default implementation sets the width of the list item to the width of *owner* and sets the height to fit *font*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `owner` | The list item's new *owner*. |
| `font` | The font set to the list item's current *owner*. |





**Since:** BeOS R3


Reimplemented in [BStringItem](classBStringItem.md#aea6bc71b073a62c57f857c2b6d0bd9e3).

---

### `Width()`

```cpp
float BListItem::Width()const
```

Return the width of the list item. 



**Returns:** The width of the list item as a float.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBListItem.html).
