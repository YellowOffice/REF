---
name: BStringItem
type: class
kit: interface_kit
brief: "A list item of a text string used as a member of a BListView or BOutlineListView"
source: haiku-book
---

# BStringItem Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A list item of a text string used as a member of a [BListView](classBListView.md) or [BOutlineListView](classBOutlineListView.md). 



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BStringItem](#a86adf0aa661f0be1cb4947f9673ab97b) (BMessage *archive) — Archive constructor.
* [BStringItem](#ab72e888919ddf89d63b58f674a642874) (const char *text, uint32 outlineLevel=0, bool expanded=true) — Creates a new BStringItem object which displays the text string.
* `virtual` [~BStringItem](#a0d967342d5d9b19da19f8cd4b2ced318) () — Destructor, frees the memory used by the string.
* `virtual void` [DrawItem](#a06cd7b53357037f2dd98bdac8f025ae0) (BView *owner, BRect frame, bool complete=false) — Hook method called when the string item is drawn.
* `virtual status_t` [Perform](#a68a5af5b0d0c958fa9528090c1ec6bcf) (perform_code code, void *arg) — Performs an action give a perform_code and arg. (Internal Method)
* `virtual void` [SetText](#a04e4422119aceb7fd32e666f35d646fb) (const char *text) — Sets the text string displayed by the item. The memory used by the old string is freed.
* `const char *` [Text](#a95282c6e093ebab8450ddc3734446e47) () const
* `virtual void` [Update](#aea6bc71b073a62c57f857c2b6d0bd9e3) (BView *owner, const BFont *font) — Hook method that's called when the owner changes.
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
* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).

### Protected Member Functions

* `float` [BaselineOffset](#addebb3bdce798fd2bb247b0aa722ed56) () const — Returns the offset from the top of the frame to the base line of the text.

### Archiving

* `virtual status_t` [Archive](#acf33097176356dbfbe1229d40ca4453a) (BMessage *archive, bool deep=true) const — Archives the the BStringItem object into the archive message.
* `static BArchivable *` [Instantiate](#a331044aec521bf2f0213ee7aeb668504) (BMessage *archive) — Creates a new BStringItem object from an archive message.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BStringItem()`

```cpp
BStringItem::BStringItem(const char * text, uint32 level = 0, bool expanded = true)
```

Creates a new [BStringItem](classBStringItem.md) object which displays the *text* string. 


The *level* and *expanded* parameters only apply to string items attached to a [BOutlineListView](classBOutlineListView.md) and are passed unchanged to the [BListItem](classBListItem.md) constructor.


Parameters

| Parameter | Description |
| :--- | :--- |
| `text` | The *text* to display. |
| `level` | The *level* of the item in a [BOutlineListView](classBOutlineListView.md). |
| `expanded` | Whether or not the item is *expanded* in a [BOutlineListView](classBOutlineListView.md). |





**Since:** BeOS R3

---

### `BStringItem()`

```cpp
BStringItem::BStringItem(BMessage * archive)
```

Archive constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The message *archive* to construct the string item from. |





**Since:** BeOS R3

---

### `~BStringItem()`

```cpp
BStringItem::~BStringItem()
```

Destructor, frees the memory used by the string. 



**Since:** BeOS R3

---

### `Archive()`

```cpp
status_t BStringItem::Archive(BMessage * archive, bool deep = true)const
```

Archives the the [BStringItem](classBStringItem.md) object into the *archive* message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | A pointer to the [BMessage](../application_kit/classBMessage.md) to archive the object into. |
| `deep` | This parameter has no effect for this class. |





**Returns:** A status code, `B_OK` if everything went well or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object was archived successfully. |
| B_NO_MEMORY | Ran out of memory while archiving the object. |





**Since:** BeOS R3


Reimplemented from [BListItem](classBListItem.md#a3fa7ca1250e123e3cf1488b1d88901d3).

---

### `BaselineOffset()`

```cpp
float BStringItem::BaselineOffset()const
```

Returns the offset from the top of the frame to the base line of the text. 


The baseline is the line upon which the letters "sit" and below which descenders extend. This value is set in the [Update()](classBStringItem.md#aea6bc71b073a62c57f857c2b6d0bd9e3) method.


This may be overridden by derived classes to set the base line offset.



**Returns:** The offset to the baseline of the text as a float.



**Since:** Haiku R1

---

### `DrawItem()`

```cpp
void BStringItem::DrawItem(BView * owner, BRect frame, bool complete = false)
```

Hook method called when the string item is drawn. 


The background is drawn either `B_LIST_BACKGROUND_COLOR` or `B_LIST_SELECTED_BACKGROUND_COLOR` depending on whether the item is selected or not.


Similarly, the text is drawn either `B_LIST_ITEM_TEXT_COLOR` or `B_LIST_SELECTED_ITEM_TEXT_COLOR`.


The text is drawn in a lighter color if the item is disabled to indicate that it may not be selected. A darker color is used instead if `B_LIST_BACKGROUND_COLOR` is set to a dark color.


Parameters

| Parameter | Description |
| :--- | :--- |
| `owner` | The string item's parent. |
| `frame` | The frame to draw in. |
| `complete` | Whether or not to draw the background in addition to the item's contents. |





**See also:** [IsSelected()](classBListItem.md#aeb958ab6a26b936f4c0169c5ff7c40a9)



**Since:** BeOS R3


Implements [BListItem](classBListItem.md#ac63fc6a6467a7130a174c643adf53c52).

---

### `Instantiate()`

```cpp
BArchivable * BStringItem::Instantiate(BMessage * archive)
```

Creates a new [BStringItem](classBStringItem.md) object from an *archive* message. 



**Returns:** A newly created [BStringItem](classBStringItem.md) object or `NULL` if the message doesn't contain an archived [BStringItem](classBStringItem.md).



**Since:** BeOS R3

---

### `Perform()`

```cpp
virtual status_t BStringItem::Perform(perform_code d, void * arg)
```

Performs an action give a perform_code and arg. (Internal Method) 


Parameters

| Parameter | Description |
| :--- | :--- |
| `d` | The perform code. |
| `arg` | A pointer to some data to perform on. |





**Returns:** A status code.



**Since:** Haiku R1


Reimplemented from [BListItem](classBListItem.md#a4b764176db576c63b8bedda260c76f91).

---

### `SetText()`

```cpp
void BStringItem::SetText(const char * text)
```

Sets the *text* string displayed by the item. The memory used by the old string is freed. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `text` | The *text* string to set in a C-string. |





**Since:** BeOS R3

---

### `Text()`

```cpp
const char * BStringItem::Text()const
```

**Returns:** The text set to the item.



**Since:** BeOS R3

---

### `Update()`

```cpp
virtual void BStringItem::Update(BView * owner, const BFont * font)
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


Reimplemented from [BListItem](classBListItem.md#a81b5b7fa5cbd942917ce7d3b5d1fe1e0).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBStringItem.html).
