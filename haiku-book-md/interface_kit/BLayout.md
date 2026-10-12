---
name: BLayout
type: class
kit: interface_kit
brief: "The BLayout class provides an interface, and some basic implementation to manage the positioning and sizing of BLayoutItem s"
source: haiku-book
---

# BLayout Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Layout API](group__layout.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

The [BLayout](classBLayout.md) class provides an interface, and some basic implementation to manage the positioning and sizing of [BLayoutItem](classBLayoutItem.md) s. 


BLayouts can be attached to a [BView](classBView.md), managing the [BLayoutItem](classBLayoutItem.md)'s and [BView](classBView.md)'s that reside in that view, or can be nested within another [BLayout](classBLayout.md) as a [BLayoutItem](classBLayoutItem.md).


Before adding a [BLayoutItem](classBLayoutItem.md) to a [BLayout](classBLayout.md), that layout must have a target view. When a [BLayout](classBLayout.md) is attached directly to a [BView](classBView.md) via [BView::SetLayout()](classBView.md#acac1ebbba8c76e543e1b06e84dffab02) then that [BView](classBView.md) becomes the target of the layout. When a [BLayout](classBLayout.md) is nested in another [BLayout](classBLayout.md) (via [BLayout::AddItem()](classBLayout.md#a61bab6592bb26173d12488526b203ead)) the nested [BLayout](classBLayout.md) inherits the target of the layout its nested in, if it does not have a target already. You can retrieve the target view for a layout with the [TargetView()](classBLayout.md#a14639db95758a7b1b9604473e8f3a7c9) method. When adding a [BLayoutItem](classBLayoutItem.md) to a [BLayout](classBLayout.md), the item's view (as returned by [BLayoutItem::View()](classBLayoutItem.md#a4a053fcf62bc431028355efbd59873fc)) is added to the [BLayout](classBLayout.md)'s target view.



```cpp
BView* topView = new BGroupView();
BLayout* topLayout = topView->GetLayout();
 
BLayout* nestedLayout = new BGroupLayout(B_HORIZONTAL);
topLayout->AddItem(nestedLayout);
 
BLayout* veryNestedLayout = new BGroupLayout(B_VERTICAL);
nestedLayout->AddItem(veryNestedLayout);
```

After executing this code, `veryNestedLayout`, `nestedLayout`, and `topLayout` all have the same target view: `topView`.


Continuing with the same objects...



```cpp
BLayout* nestedLayoutWithView = (new BGroupView())->GetLayout();
topLayout->AddItem(nestedLayoutWithView);
```

`nestedLayoutWithView` does have a target view of `topView`. This is because `nestedLayoutWithView` is attached directly to a [BView](classBView.md).



> [!WARNING]
> This class is not yet finalized, if you use it in your software assume that it will break some time in the future.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BLayout](#a95bf53912a8c34a70e63f74b155b42cb) () — Default constructor.
* [BLayout](#a972a6ece042bd46710f6b945d9d87763) (BMessage *archive) — Archive constructor.
* `virtual` [~BLayout](#aa3250586083f6cbd106051efaa6982d9) () — Destructor, deletes all BLayoutItem's that this layout manages, and detaches from this BLayout's owner view if there is one.
* `virtual status_t` [Perform](#adb8e95073f7626f04fe78337ca7114f8) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).
* `BView *` [Owner](#adb34c16c239813c45d8159d3f18d96d9) () const — Returns the Owner of this layout, i.e. the view this layout manages.
* `BView *` [TargetView](#a14639db95758a7b1b9604473e8f3a7c9) () const — Returns the target view of this layout.
* `virtual BView *` [View](#aefd7bf5546d6b69d1561e7baebf15387) () — Returns the same BView* as BLayout::Owner(), this method is inherited from BLayoutItem.
* `virtual BLayoutItem *` [AddView](#a83f286f504a1a735f07304c7647ba7f9) (BView *child) — Creates a BLayoutItem to represent a BView, and adds that item to this layout.
* `virtual BLayoutItem *` [AddView](#ad7ff945dc53e94a34954da6eaf9e2268) (int32 index, BView *child) — Creates a BLayoutItem to represent child, and adds that item at index to this layout. child is added to this BLayout's target view.
* `virtual bool` [AddItem](#a61bab6592bb26173d12488526b203ead) (BLayoutItem *item) — Adds a BLayoutItem to this layout, and adds the BView it represents to this BLayout's target view.
* `virtual bool` [AddItem](#a1b9a50f6a573a777afc2b27bac65c7f6) (int32 index, BLayoutItem *item) — Adds item to this layout, and adds the BView item represents to this BLayout's target view.
* `virtual bool` [RemoveView](#a3120e95dc34ab57ab276c324ec94654c) (BView *child) — Removes and deletes all BLayoutItem representing a BView from this layout.
* `virtual bool` [RemoveItem](#abf0b19d4203e1a41292137fd8a2038d0) (BLayoutItem *item) — Removes a BLayoutItem from this layout, and also removes the view it represents from this BLayout's target view.
* `virtual BLayoutItem *` [RemoveItem](#a34a299447961069bdd54d19ae7a5176a) (int32 index) — Remove the BLayoutItem at index.
* `BLayoutItem *` [ItemAt](#ad47d881e6008578d2f8cc0e3c6ea467a) (int32 index) const — Get the BLayoutItem at index. Returns NULL if index is out of bounds.
* `int32` [CountItems](#ab7d1b881e91213047412abdcb10eae4f) () const — Get the number of BLayoutItem s in this layout.
* `int32` [IndexOfItem](#a1d3746cfb977dce44b052e7d58bd481c) (const BLayoutItem *item) const — Get the index of a BLayoutItem in this layout.
* `int32` [IndexOfView](#ade2afbfa0bd50c01a1ce3db6654eaa0c) (BView *child) const — Get the index of child in this layout.
* `virtual void` [Relayout](#a2a168d993feaf8fc58b53ded8243e7b7) (bool immediate=false) — Request this BLayout to reposition and resize its items as required.
* `void` [LayoutItems](#a683aba3445c345b47c7fa38a2b6c3c1a) (bool force=false) — If there is no layout currently ongoing, and force is false, creates a new BLayoutContext and calls the DoLayout() method of this BLayout and any BLayout's nested in this BLayout.
* `BLayoutContext *` [LayoutContext](#a7d2db371223df3a53cd7a1c5f19f309a) () const — Returns the BLayoutContext this BLayout is currently operating in, or NULL.
* [BLayoutItem](#ac639d9cfa9b8124106ef2d8bc5badb2e) (BMessage *from) — Archive constructor.
* `virtual status_t` [Archive](#af2c2593e6179ee367ef26eff7ab7409f) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `BLayout *` [Layout](#ab760ea9f0eb6bb25063b5bac7a52ec3d) () const — Returns the BLayout this BLayoutItem resides in.
* `virtual status_t` [Perform](#a38b237fb8bbd1d0054e3a2b4cbc1fd15) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).
* `bool` [RemoveSelf](#af4059e73a30336f0ae6bbbc04c70dd6a) () — Remove this layout item from the BLayout it is a part of.
* `virtual BView *` [View](#a4a053fcf62bc431028355efbd59873fc) () — Return the BView this item is representing, or NULL if it does not represent any view.
* `virtual BSize` [MinSize](#aa6b24064b472cf72f98dbfd11198f067) ()=0 — Returns the minimum desirable size for this item.
* `virtual BSize` [MaxSize](#ac8279364e37b84f2b152fd052200f158) ()=0 — Returns the maximum desirable size for this item.
* `virtual BSize` [PreferredSize](#a7311fd45380396ae3840179f9b63fae3) ()=0 — Returns the preferred size for this item.
* `virtual BAlignment` [Alignment](#a3f34ad935970e7d941dafe7ca5290d26) ()=0 — Returns the requested alignment for this item.
* `virtual bool` [HasHeightForWidth](#a3186c8eec495915c5b074fe7d10dc94c) () — Returns whether or not this BLayoutItem's height constraints are dependent on its width.
* `virtual void` [GetHeightForWidth](#addd90adf76c9caad200f6f465c06e0bf) (float width, float *min, float *max, float *preferred) — Get this BLayoutItem's height constraints for a given width.
* `virtual void` [SetExplicitMinSize](#ab5bfb3d6541b1e3097c77577be279346) (BSize size)=0 — Set this item's explicit min size, to be used in MinSize().
* `virtual void` [SetExplicitMaxSize](#ad91aa5d8c83270f33ec4503dbc8e438e) (BSize size)=0 — Set this item's explicit max size, to be used in MaxSize().
* `virtual void` [SetExplicitPreferredSize](#afa1c729ac363fc0296c9aca68eca4ddc) (BSize size)=0 — Set this item's explicit preferred size, to be used in PreferredSize().
* `void` [SetExplicitSize](#ac630c7ab0e98d5da0225792e31f596f1) (BSize size) — Set the explicity size to size.
* `virtual void` [SetExplicitAlignment](#a78604c5055ac0aca561f196d879d762d) (BAlignment alignment)=0 — Set this item's explicit alignment, to be used in Alignment().
* `virtual bool` [IsVisible](#ad83886b5bef773a870e6668dd008a88a) ()=0 — Return the current local visibility of this item. If an item is not visible, it will not be given space by the BLayout it resides in.
* `virtual void` [SetVisible](#a51d14ca920b9f302662a619fa8b79957) (bool visible)=0 — Set the local visibility of this item.
* `virtual BRect` [Frame](#a6bc751e914fc3b31dfaa072674972124) ()=0 — Return the bounding frame of this item.
* `virtual void` [SetFrame](#ad6e6d52145cb3007e54b5eafe454caed) (BRect frame)=0 — Set the bounding frame of this item.
* `void` [AlignInFrame](#a3b5b23daa375b3333fc58c9c22ce62fa) (BRect frame) — Position this BLayoutItem within frame, given the value returned by Alignment(), and the size constraints for this item.
* `void *` [LayoutData](#a82ba24d424129d989855b74eb3a86627) () const — Retrieve arbitrary data attached to this BLayoutItem.
* `void` [SetLayoutData](#abffd9c09f9951f25b4a752a06e4040c3) (void *data) — Attach arbitrary data to this BLayoutItem.
* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).

### Protected Member Functions

* `virtual status_t` [AllArchived](#ab9747436e251333693d54d29d472e2f9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual bool` [ItemAdded](#a139763bba67c7e68cf0311eb6fd5a19d) (BLayoutItem *item, int32 atIndex) — Hook method called when item is added to this layout.
* `virtual void` [ItemRemoved](#af17a219d364b091425a28759a4d684f8) (BLayoutItem *item, int32 fromIndex) — Hook method called when item is removed from this layout.
* `virtual void` [LayoutInvalidated](#a76c0a3aee65267a10187e4081b6d240d) (bool children)
* `virtual void` [DoLayout](#a972a7f273fc24f7665f5918e99989658) ()=0 — Implemented by derived classes to position and resize the items in this layout.
* `virtual void` [OwnerChanged](#a58f983930686b554fd70e7aacafe1817) (BView *was) — Hook method called when this layout is attached to a BView.
* `virtual void` [AttachedToLayout](#a18f9f855b86a1a517249288672adf680) () — Hook method inherited from BLayoutItem, classes derived from BLayout must include the BLayout version of this method in their implementation.
* `virtual void` [DetachedFromLayout](#a1339f65fb6907b6944d24b2f37e6f738) (BLayout *layout) — Hook method inherited from BLayoutItem, classes derived from BLayout must include the BLayout version of this method in their implementation.
* `virtual void` [AncestorVisibilityChanged](#a9fe7eaa534d51bbfc807b9aca444176f) (bool shown) — Hook method inherited from BLayoutItem, classes derived from BLayout must include the BLayout version of this method in their implementation.
* `virtual status_t` [AllArchived](#a13ec3faa075b23b3073f97531365102c) (BMessage *into) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#af78b72941cf1532299c2396cfeb7f9ed) (const BMessage *from) — Method relating to the use of BUnarchiver.

### Subclass Helpers

* `bool` [AncestorsVisible](#a4f2ff9362ef1e84d7c886c58881d2be9) () const — Get the visibility of the ancestors of this layout.
* `BRect` [LayoutArea](#a25735d4b3149817ab91b2f4cff0a2fed) () — Returns the on-screen area this layout has received to lay out its items in.
* `void` [VisibilityChanged](#a7df37ec98c2d29dca5ce4f2246c5665a) (bool show) — Method to be called by derived classes in their SetVisible() implementation. Calls AncestorVisibilityChanged() on the items in this BLayout.

### Invalidation and State Mutators and Accessors

* `virtual void` [InvalidateLayout](#a2b775de411ef6e9ecb4f7c412a26bf31) (bool children=false) — Invalidate this layout and any cached data this layout has relating to positioning and sizing of its items.
* `void` [RequireLayout](#a1983a8770e7cd89c3f1afc4d961230d5) () — Flag this layout as stale, i.e. any cached data may still be valid, but the items need to be repositioned or resized.
* `bool` [IsValid](#a9b5b6b764433dee59ed4d1f01aaada04) () — Returns whether this layout has been invalidated (via BLayout::InvalidateLayout()) and has not yet been validated (by doing a layout, or by its ResetLayoutInvalidation() method.
* `void` [EnableLayoutInvalidation](#a7f369cb77173c3922dddbb38db893a6c) () — Re-enable layout invalidation after a call to DisableLayoutInvalidation().
* `void` [DisableLayoutInvalidation](#a509ff18ffa060bd9aab042c4ee6af245) () — Disable layout invalidation notifications, i.e. calls to this object's InvalidateLayout() method.
* `void` [ResetLayoutInvalidation](#aacf1392bbef13efc20277e15595bb329) () — Reset layout invalidation, causing InvalidateLayout calls to proceed again. This method should be called once any cached data has been validated, or updated to valid values.

### Archiving

* `virtual status_t` [Archive](#a0d5f0b0a3ca81f5f7d54dae6ab7a099f) (BMessage *into, bool deep=true) const — Archives this layout into archive. If deep is true, also archives the items in this layout, calling ItemArchived() for each one.
* `virtual status_t` [AllUnarchived](#a3517e73d524672645425f80ebd4f53c7) (const BMessage *from) — Unarchives the BLayoutItem's for this layout, calling ItemUnarchived() for each one.
* `virtual status_t` [ItemArchived](#a7b342780ed464d0074a63fe8fac67003) (BMessage *into, BLayoutItem *item, int32 index) const — Hook for derived classes to add data specific to item to the into BMessage. item resides at index.
* `virtual status_t` [ItemUnarchived](#a6cf3d79228879f9a6e2c29d238a2a1cf) (const BMessage *from, BLayoutItem *item, int32 index) — Hook for derived classes to retrieve data specific to item from the from BMessage. item resides at index.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BLayout()`

```cpp
BLayout::BLayout()
```

Default constructor. 


After this constructor has finished, this [BLayout](classBLayout.md) holds no [BLayoutItem](classBLayoutItem.md)'s and does not have a target [BView](classBView.md).



> [!WARNING]
> Because a new [BLayout](classBLayout.md) does not have a target [BView](classBView.md), calls to the [AddItem()](classBLayout.md#a61bab6592bb26173d12488526b203ead) and [AddView()](classBLayout.md#a83f286f504a1a735f07304c7647ba7f9) methods will fail.



**Since:** Haiku R1

---

### `BLayout()`

```cpp
BLayout::BLayout(BMessage * archive)
```

Archive constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The archive message. |





**Since:** Haiku R1

---

### `~BLayout()`

```cpp
BLayout::~BLayout()
```

Destructor, deletes all [BLayoutItem](classBLayoutItem.md)'s that this layout manages, and detaches from this [BLayout](classBLayout.md)'s owner view if there is one. 


Destructor method.


Each [BLayoutItem](classBLayoutItem.md)'s [BView](classBView.md) (as returned by [BLayoutItem::View()](classBLayoutItem.md#a4a053fcf62bc431028355efbd59873fc)) is also removed from their parent.



> [!NOTE]
> Because nested [BLayout](classBLayout.md)'s are treated as [BLayoutItem](classBLayoutItem.md)'s, any layouts nested in this [BLayout](classBLayout.md) will be deleted.



**Since:** Haiku R1


Standard Destructor.



**Since:** Haiku R1

---

### `AddItem()`

```cpp
bool BLayout::AddItem(BLayoutItem * item)
```

Adds a [BLayoutItem](classBLayoutItem.md) to this layout, and adds the [BView](classBView.md) it represents to this [BLayout](classBLayout.md)'s target view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The [BLayoutItem](classBLayoutItem.md) to be added. |





**Returns:** `true` if the item was added, `false` otherwise.



**Since:** Haiku R1


Reimplemented in [BGridLayout](classBGridLayout.md#a2428b80791df9c5d01c5c88a62455d7e), and [BGroupLayout](classBGroupLayout.md#a7d53490ec7fe0b7fff6c2df5cc084493).

---

### `AddItem()`

```cpp
bool BLayout::AddItem(int32 index, BLayoutItem * item)
```

Adds *item* to this layout, and adds the [BView](classBView.md) *item* represents to this [BLayout](classBLayout.md)'s target view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The [BLayoutItem](classBLayoutItem.md) to be added. |
| `index` | The index at which to add `item`. |




If *index* is out of bounds, *item* will be added at the end. If *index* is somewhere between the first and last indices, then items from *index* to the end will be shuffled over by one.



**Returns:** `true` if the item was added, `false` otherwise.



**Since:** Haiku R1


Reimplemented in [BGridLayout](classBGridLayout.md#a016186a888ad44a8807d7686c00f2d84), and [BGroupLayout](classBGroupLayout.md#abe585d5630ede5df6602b43421fe8ebc).

---

### `AddView()`

```cpp
BLayoutItem * BLayout::AddView(BView * child)
```

Creates a [BLayoutItem](classBLayoutItem.md) to represent a [BView](classBView.md), and adds that item to this layout. 


*child* is added to this [BLayout](classBLayout.md)'s target view.



**Returns:** The [BLayoutItem](classBLayoutItem.md) created to represent *child*, or `NULL` if there was an error.


Parameters

| Parameter | Description |
| :--- | :--- |
| `child` | The [BView](classBView.md) to be added to this [BLayout](classBLayout.md). |





**Since:** Haiku R1


Reimplemented in [BGridLayout](classBGridLayout.md#a226fb320cbb2f5028fe4b537d9922fb3), and [BGroupLayout](classBGroupLayout.md#ac732947ea67a015a1d2babe82f60fd90).

---

### `AddView()`

```cpp
BLayoutItem * BLayout::AddView(int32 index, BView * child)
```

Creates a [BLayoutItem](classBLayoutItem.md) to represent *child*, and adds that item at *index* to this layout. *child* is added to this [BLayout](classBLayout.md)'s target view. 



**Since:** Haiku R1


Reimplemented in [BGridLayout](classBGridLayout.md#a98676374bc080f6070686362409b4378), and [BGroupLayout](classBGroupLayout.md#a7fce65b286ae16105cb6b91661e24b55).

---

### `AllArchived()`

```cpp
virtual status_t BLayout::AllArchived(BMessage * into)const
```

Method relating to the use of `BArchiver`. 


This hook function is called once the first [BArchiver](../support_kit/classBArchiver.md) that was created in an archiving session is either destroyed, or has its Finish() method called. Implementations of this method can be used, in conjunction with [BArchiver::IsArchived()](../support_kit/classBArchiver.md#a77f099b123416c719be2cd78eb999d19), to reference objects in your archive that you do not own, depending on whether or not those objects were archived by their owners. Implementations of this method should call the implementation of their parent class, the same as for the [Archive()](classBLayout.md#a0d5f0b0a3ca81f5f7d54dae6ab7a099f) method.



> [!WARNING]
> To guarantee that your [AllArchived()](classBLayout.md#ab9747436e251333693d54d29d472e2f9) method will be called during archival, you must create a [BArchiver](../support_kit/classBArchiver.md) object in your [Archive()](classBLayout.md#a0d5f0b0a3ca81f5f7d54dae6ab7a099f) implementation.



**See also:** [BArchiver](../support_kit/classBArchiver.md) [BArchiver::Finish()](../support_kit/classBArchiver.md#a7c82dbc0fb42795c575ac2c6a5405297)



**Since:** Haiku R1


Reimplemented from [BLayoutItem](classBLayoutItem.md#a13ec3faa075b23b3073f97531365102c).


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a73b50e5ee03b980b4e8f08c875528162), [BCardLayout](classBCardLayout.md#ac561655882cd31e4f8a8b214de846fb6), [BGridLayout](classBGridLayout.md#adddbabf3f060e0e3d20af12cf3f3dab1), [BGroupLayout](classBGroupLayout.md#a62670753e05e05601592d49f0b5f438f), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#adb001699008fe0cb2eff51661da175e6).

---

### `AllUnarchived()`

```cpp
status_t BLayout::AllUnarchived(const BMessage * from)
```

Unarchives the [BLayoutItem](classBLayoutItem.md)'s for this layout, calling [ItemUnarchived()](classBLayout.md#a6cf3d79228879f9a6e2c29d238a2a1cf) for each one. 



**Since:** Haiku R1


Reimplemented from [BLayoutItem](classBLayoutItem.md#af78b72941cf1532299c2396cfeb7f9ed).


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a2664ac14ab5dbe33a18cee88d420aa22), [BCardLayout](classBCardLayout.md#a30c68436cd5efd9708c1cfd75655647a), [BGridLayout](classBGridLayout.md#a2cd9bd9915c14ac32c0081234e12a5fb), [BGroupLayout](classBGroupLayout.md#a25bd4f838e672aa3eb611a616c5ec5e0), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#a67ba660a95e7cf8647be8835184b6cc3).

---

### `AncestorsVisible()`

```cpp
bool BLayout::AncestorsVisible()const
```

Get the visibility of the ancestors of this layout. 


If a [BLayout](classBLayout.md) is connected to a [BView](classBView.md), this will always return `true`. If a [BLayout](classBLayout.md) is nested in another layout (it was passed to [AddItem()](classBLayout.md#a61bab6592bb26173d12488526b203ead)), then this will reflect the visibility of this [BLayout](classBLayout.md)'s parent layout. If any layout is hidden (by [BLayout::SetVisible()](classBLayoutItem.md#a51d14ca920b9f302662a619fa8b79957)) between this layout and its target [BView](classBView.md)'s layout, then this method will return `false`.



**Since:** Haiku R1

---

### `AncestorVisibilityChanged()`

```cpp
void BLayout::AncestorVisibilityChanged(bool shown)
```

Hook method inherited from [BLayoutItem](classBLayoutItem.md), classes derived from [BLayout](classBLayout.md) must include the [BLayout](classBLayout.md) version of this method in their implementation. 



**Since:** Haiku R1


Reimplemented from [BLayoutItem](classBLayoutItem.md#a46e148b6608b3b21b1442fbc3aa9f404).


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a5e36e0a2cb89ef4f45905c20159ef371).

---

### `Archive()`

```cpp
status_t BLayout::Archive(BMessage * archive, bool deep = true)const
```

Archives this layout into *archive*. If deep is true, also archives the items in this layout, calling [ItemArchived()](classBLayout.md#a7b342780ed464d0074a63fe8fac67003) for each one. 



**Since:** Haiku R1


Reimplemented from [BLayoutItem](classBLayoutItem.md#af2c2593e6179ee367ef26eff7ab7409f).


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a76c6e663adb27a10972dafe22c898bf7), [BCardLayout](classBCardLayout.md#a0cfce7f1c906b28d8e3abaca74bcda56), [BGridLayout](classBGridLayout.md#aab5e2df95091bb76bb93628dcd01013e), [BGroupLayout](classBGroupLayout.md#aae43bdb3a725755664e55f13a054b510), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#a405b207a3fa1770d5349de6d66705390).

---

### `AttachedToLayout()`

```cpp
void BLayout::AttachedToLayout()
```

Hook method inherited from [BLayoutItem](classBLayoutItem.md), classes derived from [BLayout](classBLayout.md) must include the [BLayout](classBLayout.md) version of this method in their implementation. 



**Since:** Haiku R1


Reimplemented from [BLayoutItem](classBLayoutItem.md#a4798b0eb99c785b1d61dc2c169fb7df0).


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a0eb40b1488e9b5f524cbc263106e7f3b).

---

### `CountItems()`

```cpp
int32 BLayout::CountItems()const
```

Get the number of [BLayoutItem](classBLayoutItem.md) s in this layout. 



**Since:** Haiku R1

---

### `DetachedFromLayout()`

```cpp
void BLayout::DetachedFromLayout(BLayout * layout)
```

Hook method inherited from [BLayoutItem](classBLayoutItem.md), classes derived from [BLayout](classBLayout.md) must include the [BLayout](classBLayout.md) version of this method in their implementation. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `layout` | The [BLayout](classBLayout.md) that this [BLayout](classBLayout.md) was detached from. |





**Since:** Haiku R1


Reimplemented from [BLayoutItem](classBLayoutItem.md#ad829ab9d9a38acffb39f0183e77acee8).


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a4535f6de7c5193ba20038b891944864b).

---

### `DisableLayoutInvalidation()`

```cpp
void BLayout::DisableLayoutInvalidation()
```

Disable layout invalidation notifications, i.e. calls to this object's [InvalidateLayout()](classBLayout.md#a2b775de411ef6e9ecb4f7c412a26bf31) method. 



**Since:** Haiku R1

---

### `DoLayout()`

```cpp
void BLayout::DoLayout()
```

Implemented by derived classes to position and resize the items in this layout. 



**Since:** Haiku R1


Implemented in [BCardLayout](classBCardLayout.md#adb91400ccc94cdbbba90efe8158c933f), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#a18eeeb1d0b5fa7b4b57d8a2a9dc3824b).

---

### `EnableLayoutInvalidation()`

```cpp
void BLayout::EnableLayoutInvalidation()
```

Re-enable layout invalidation after a call to [DisableLayoutInvalidation()](classBLayout.md#a509ff18ffa060bd9aab042c4ee6af245). 



**Since:** Haiku R1

---

### `IndexOfItem()`

```cpp
int32 BLayout::IndexOfItem(const BLayoutItem * item)const
```

Get the index of a [BLayoutItem](classBLayoutItem.md) in this layout. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The [BLayoutItem](classBLayoutItem.md) whose index you want. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| -1 | *item* was not found in this [BLayout](classBLayout.md). |





**Since:** Haiku R1

---

### `IndexOfView()`

```cpp
int32 BLayout::IndexOfView(BView * child)const
```

Get the index of *child* in this layout. 



> [!NOTE]
> This finds the index of views added through [BLayout::AddView()](classBLayout.md#a83f286f504a1a735f07304c7647ba7f9), not the index of an item which represents *child* that was added through [BLayout::AddItem()](classBLayout.md#a61bab6592bb26173d12488526b203ead).



**Since:** Haiku R1

---

### `InvalidateLayout()`

```cpp
void BLayout::InvalidateLayout(bool children = false)
```

Invalidate this layout and any cached data this layout has relating to positioning and sizing of its items. 


Invalidating a [BLayout](classBLayout.md) also invalidates the view it is connected to (if there is one) and the [BLayout](classBLayout.md) this layout (or this [BLayout](classBLayout.md)'s view) resides in.


Although this method is virtual, you should not override it, override the [BLayout::LayoutInvalidated()](classBLayout.md#a76c0a3aee65267a10187e4081b6d240d) hook instead.


This method should be called whenever the layout becomes invalid. This might happen if the size constraints of an item in this layout change, this layout is given more or less space than it previously had, or an object in this layout has had its [InvalidateLayout()](classBLayout.md#a2b775de411ef6e9ecb4f7c412a26bf31) method called.



**See also:** [BView::InvalidateLayout()](classBView.md#a4a711316094e43076a3f5478d937accf), [BLayoutItem::InvalidateLayout()](classBLayoutItem.md#a9afedf1de602c6b277e8eb6eb3ff928d), [BLayout::LayoutInvalidated()](classBLayout.md#a76c0a3aee65267a10187e4081b6d240d)



**Since:** Haiku R1


Reimplemented from [BLayoutItem](classBLayoutItem.md#a9afedf1de602c6b277e8eb6eb3ff928d).

---

### `IsValid()`

```cpp
bool BLayout::IsValid()
```

Returns whether this layout has been invalidated (via [BLayout::InvalidateLayout()](classBLayout.md#a2b775de411ef6e9ecb4f7c412a26bf31)) and has not yet been validated (by doing a layout, or by its [ResetLayoutInvalidation()](classBLayout.md#aacf1392bbef13efc20277e15595bb329) method. 



**Since:** Haiku R1

---

### `ItemAdded()`

```cpp
bool BLayout::ItemAdded(BLayoutItem * item, int32 atIndex)
```

Hook method called when *item* is added to this layout. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The [BLayoutItem](classBLayoutItem.md) that is being added. |
| `atIndex` | The index of the [BLayoutItem](classBLayoutItem.md). |





**Returns:** `true` on succcess, false if *item* will not be added.



> [!NOTE]
> This is a good time to allocate data for a [BLayoutItem](classBLayoutItem.md) and attach it to *item* via [BLayoutItem::SetLayoutData()](classBLayoutItem.md#abffd9c09f9951f25b4a752a06e4040c3).



**Since:** Haiku R1


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a842b424b62039753db229d3deafd0d10), [BCardLayout](classBCardLayout.md#a44ea0d7a577626d6992e292bd93556bc), [BGridLayout](classBGridLayout.md#a5edc94b8a647debd21f7303a225c0bfe), and [BGroupLayout](classBGroupLayout.md#ab7222b8afc2e96f1396d226117fbbc34).

---

### `ItemArchived()`

```cpp
status_t BLayout::ItemArchived(BMessage * into, BLayoutItem * item, int32 index)const
```

Hook for derived classes to add data specific to *item* to the *into* [BMessage](../application_kit/classBMessage.md). *item* resides at *index*. 



> [!NOTE]
> The same archive is passed to [BLayout::ItemArchived()](classBLayout.md#a7b342780ed464d0074a63fe8fac67003) for all items, so any data added for each item will be stored in an array.



**Since:** Haiku R1


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a8f3461939aac1452b9e34ff707b38684), [BCardLayout](classBCardLayout.md#a8190101471e608007ca0b1864056512c), [BGridLayout](classBGridLayout.md#aa78c81cd57baacbdb8890b0de281f720), [BGroupLayout](classBGroupLayout.md#ab7a1143b436b800e42c76de98534dbc7), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#af70e3bd455f4dafa684ac6352223fcc4).

---

### `ItemAt()`

```cpp
BLayoutItem * BLayout::ItemAt(int32 index)const
```

Get the [BLayoutItem](classBLayoutItem.md) at *index*. Returns `NULL` if *index* is out of bounds. 



**Since:** Haiku R1

---

### `ItemRemoved()`

```cpp
void BLayout::ItemRemoved(BLayoutItem * item, int32 fromIndex)
```

Hook method called when *item* is removed from this layout. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The [BLayoutItem](classBLayoutItem.md) being removed. |
| `fromIndex` | The index where *item* used to reside. |




When this hook is called, *item* is not yet completely removed. It can no longer be accessed with LayoutItemAt(), nor does it contribute to the value of [CountItems()](classBLayout.md#ab7d1b881e91213047412abdcb10eae4f), but the item has not yet had its ItemDetached() hook called.



> [!NOTE]
> This is a good time to delete the data you've attached to *item* via [BLayoutItem::SetLayoutData()](classBLayoutItem.md#abffd9c09f9951f25b4a752a06e4040c3).



**Since:** Haiku R1


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a4df45f148af285d521bc5d6a491dac7b), [BCardLayout](classBCardLayout.md#ab1b92790589cc18c25c9c5ec9521fd62), [BGridLayout](classBGridLayout.md#a69ef1fdfffae399d06a09fe99b72fda0), and [BGroupLayout](classBGroupLayout.md#ac347c539f60e59dee72e7038bcb83ff6).

---

### `ItemUnarchived()`

```cpp
status_t BLayout::ItemUnarchived(const BMessage * from, BLayoutItem * item, int32 index)
```

Hook for derived classes to retrieve data specific to *item* from the *from* [BMessage](../application_kit/classBMessage.md). *item* resides at *index*. 



> [!NOTE]
> The same archive is passed to [BLayout::ItemArchived()](classBLayout.md#a7b342780ed464d0074a63fe8fac67003) for all items, so any data added for each item will be stored in an array. You should pass *index* to the [BMessage](../application_kit/classBMessage.md) methods you will be using in this method.



**Since:** Haiku R1


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a9c3fd4aa60076e9869fa937d37f55ad3), [BCardLayout](classBCardLayout.md#a54cbd1654003320469e93c258091f840), [BGridLayout](classBGridLayout.md#ad7bda5e11e67558de88b0ccaeccd3949), [BGroupLayout](classBGroupLayout.md#a3fee09f7df25a5d730a888fc88360f09), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#a7e98a6fb9b41e0856e353f6c0baaee12).

---

### `LayoutArea()`

```cpp
BRect BLayout::LayoutArea()
```

Returns the on-screen area this layout has received to lay out its items in. 


The return value is in the coordinate space of this [BLayout](classBLayout.md)'s target view. If this [BLayout](classBLayout.md) is attached directly to a [BView](classBView.md), then ` LayoutArea().LeftTop() == B_ORIGIN `.



**Since:** Haiku R1

---

### `LayoutContext()`

```cpp
BLayoutContext * BLayout::LayoutContext()const
```

Returns the BLayoutContext this [BLayout](classBLayout.md) is currently operating in, or `NULL`. 



**Since:** Haiku R1

---

### `LayoutInvalidated()`

```cpp
void BLayout::LayoutInvalidated(bool children)
```

Hook method called when this layout becomes invalid. This is a good place to clear any caches your object might hold.


Parameters

| Parameter | Description |
| :--- | :--- |
| `children` | Whether or not child layouts have also been invalidated. |





**Since:** Haiku R1


Reimplemented from [BLayoutItem](classBLayoutItem.md#a69da4cf2822d9add9dbd6760e30eabfb).


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#aa8d37f3c77c4fa240c0c18f800e7c64a), [BCardLayout](classBCardLayout.md#a98304460f6a41f4e3aa387d914310cf8), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#a213da2d0c283091e48562e8fbb448c5f).

---

### `LayoutItems()`

```cpp
void BLayout::LayoutItems(bool force = false)
```

If there is no layout currently ongoing, and *force* is `false`, creates a new BLayoutContext and calls the [DoLayout()](classBLayout.md#a972a7f273fc24f7665f5918e99989658) method of this [BLayout](classBLayout.md) and any [BLayout](classBLayout.md)'s nested in this [BLayout](classBLayout.md). 


This method also guarantees that the owner view of this layout (as returned by [BLayout::Owner()](classBLayout.md#adb34c16c239813c45d8159d3f18d96d9)) performs a layout as well (if it is suitable to do so).


Parameters

| Parameter | Description |
| :--- | :--- |
| `force` | Force the LayoutItems. |





**Since:** Haiku R1

---

### `Owner()`

```cpp
BView * BLayout::Owner()const
```

Returns the Owner of this layout, i.e. the view this layout manages. 



**Since:** Haiku R1


Referenced by [BLayoutBuilder::Cards< ParentBuilder >::Cards()](classBLayoutBuilder_1_1Cards.md#a08329883aebee0490f3faf96d86f1108), [BLayoutBuilder::Grid< ParentBuilder >::Grid()](classBLayoutBuilder_1_1Grid.md#ad7bd68789548063830f46a0bb279e17a), and [BLayoutBuilder::Group< ParentBuilder >::Group()](classBLayoutBuilder_1_1Group.md#adebaf628afb53fdd86d6b153d60cf0ea).

---

### `OwnerChanged()`

```cpp
void BLayout::OwnerChanged(BView * was)
```

Hook method called when this layout is attached to a [BView](classBView.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `was` | The previous owner of this [BLayout](classBLayout.md), for new [BLayout](classBLayout.md) s, this will be `NULL`. |





**Since:** Haiku R1


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a3aca5334eed301df4013fb2a3fdfd5ac).

---

### `Perform()`

```cpp
virtual status_t BLayout::Perform(perform_code d, void * arg)
```

Perform some action (Internal method defined for binary compatibility purposes). 


Reimplemented from [BLayoutItem](classBLayoutItem.md#a38b237fb8bbd1d0054e3a2b4cbc1fd15).


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#aa4d7d592de1e566f73f440576d1c2cac), [BCardLayout](classBCardLayout.md#a7b75708b091f51e8dce826477f28e33a), [BGridLayout](classBGridLayout.md#a0ab603b381b9ba4d7efb3efbeae4940f), [BGroupLayout](classBGroupLayout.md#a31d82f6cd2fdecdc0a04d60d6e3943f7), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#aac851d9c86397296d0e7e69716c01926).

---

### `Relayout()`

```cpp
void BLayout::Relayout(bool immediate = false)
```

Request this [BLayout](classBLayout.md) to reposition and resize its items as required. 


If *immediate* is `false`, and there is already a request to have the window this layout resides in re-laid-out, then the layout will happen at that time. If *immediate* is `true`, and there is no such pending request, nor is this [BLayout](classBLayout.md)'s parent layout in the process of laying out its items, then this [BLayout](classBLayout.md) will now layout its items.


Parameters

| Parameter | Description |
| :--- | :--- |
| `immediate` | Whether or not to Relayout immediately or wait for pending requests first. |





**Since:** Haiku R1


Reimplemented from [BLayoutItem](classBLayoutItem.md#afddc9eb49deca3121887f0b923da6a0b).

---

### `RemoveItem()`

```cpp
bool BLayout::RemoveItem(BLayoutItem * item)
```

Removes a [BLayoutItem](classBLayoutItem.md) from this layout, and also removes the view it represents from this [BLayout](classBLayout.md)'s target view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The [BLayoutItem](classBLayoutItem.md) to be removed |





> [!WARNING]
> *item* is not deleted, you must delete it manually, or add it to another [BLayout](classBLayout.md).



**Returns:** `true` if the item was removed, `false` otherwise.



**Since:** Haiku R1

---

### `RemoveItem()`

```cpp
BLayoutItem * BLayout::RemoveItem(int32 index)
```

Remove the [BLayoutItem](classBLayoutItem.md) at *index*. 



**See also:** [RemoveItem(BLayoutItem*)](classBLayout.md#abf0b19d4203e1a41292137fd8a2038d0)



**Returns:** The [BLayoutItem](classBLayoutItem.md) that was removed.



**Since:** Haiku R1

---

### `RemoveView()`

```cpp
bool BLayout::RemoveView(BView * child)
```

Removes and deletes all [BLayoutItem](classBLayoutItem.md) representing a [BView](classBView.md) from this layout. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `child` | The [BView](classBView.md) to be removed. |





**Returns:** `true` if the item was removed, `false` otherwise.



**Since:** Haiku R1

---

### `RequireLayout()`

```cpp
void BLayout::RequireLayout()
```

Flag this layout as stale, i.e. any cached data may still be valid, but the items need to be repositioned or resized. 



**Since:** Haiku R1

---

### `ResetLayoutInvalidation()`

```cpp
void BLayout::ResetLayoutInvalidation()
```

Reset layout invalidation, causing InvalidateLayout calls to proceed again. This method should be called once any cached data has been validated, or updated to valid values. 



**Since:** Haiku R1

---

### `TargetView()`

```cpp
BView * BLayout::TargetView()const
```

Returns the target view of this layout. 


The target view of a layout becomes the parent of any [BView](classBView.md)'s in this layout, as well as the [BView](classBView.md)'s returned by [BLayoutItem::View()](classBLayoutItem.md#a4a053fcf62bc431028355efbd59873fc) for each [BLayoutItem](classBLayoutItem.md) in this layout.



**Since:** Haiku R1

---

### `View()`

```cpp
BView * BLayout::View()
```

Returns the same BView* as [BLayout::Owner()](classBLayout.md#adb34c16c239813c45d8159d3f18d96d9), this method is inherited from [BLayoutItem](classBLayoutItem.md). 



**Since:** Haiku R1


Reimplemented from [BLayoutItem](classBLayoutItem.md#a4a053fcf62bc431028355efbd59873fc).

---

### `VisibilityChanged()`

```cpp
void BLayout::VisibilityChanged(bool show)
```

Method to be called by derived classes in their [SetVisible()](classBLayoutItem.md#a51d14ca920b9f302662a619fa8b79957) implementation. Calls [AncestorVisibilityChanged()](classBLayout.md#a9fe7eaa534d51bbfc807b9aca444176f) on the items in this [BLayout](classBLayout.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `show` | `true` to show, `false` to hide. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBLayout.html).
