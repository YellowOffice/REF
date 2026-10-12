---
name: BLayoutItem
type: class
kit: interface_kit
brief: "Abstract class representing things that are positionable and resizable by objects of the BLayout class"
source: haiku-book
---

# BLayoutItem Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Layout API](group__layout.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Abstract class representing things that are positionable and resizable by objects of the [BLayout](classBLayout.md) class. 


The [BLayoutItem](classBLayoutItem.md) class provides an interface that is meant to be used almost exclusively by objects of the [BLayout](classBLayout.md) class. Despite this, there are some methods that are provided for other users of the class.



> [!WARNING]
> This class is not yet finalized, if you use it in your software assume that it will break some time in the future.



**Since:** Haiku R1

## Member List

### Public Member Functions

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
* `virtual void` [InvalidateLayout](#a9afedf1de602c6b277e8eb6eb3ff928d) (bool children=false) — Invalidate the layout of this item, or the object it represents.
* `virtual void` [Relayout](#afddc9eb49deca3121887f0b923da6a0b) (bool immediate=false) — Relayout any children or onscreen data this item contains. Often this request is forwarded to another object.
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

* `virtual status_t` [AllArchived](#a13ec3faa075b23b3073f97531365102c) (BMessage *into) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#af78b72941cf1532299c2396cfeb7f9ed) (const BMessage *from) — Method relating to the use of BUnarchiver.
* `virtual void` [LayoutInvalidated](#a69da4cf2822d9add9dbd6760e30eabfb) (bool children) — Hook called from InvalidateLayout().
* `virtual void` [AttachedToLayout](#a4798b0eb99c785b1d61dc2c169fb7df0) () — Hook called when this object is attached to a BLayout (via BLayout::AddItem())
* `virtual void` [DetachedFromLayout](#ad829ab9d9a38acffb39f0183e77acee8) (BLayout *layout) — Hook called when this object is attached to a BLayout (via BLayout::RemoveItem())
* `virtual void` [AncestorVisibilityChanged](#a46e148b6608b3b21b1442fbc3aa9f404) (bool shown) — Hook called when this BLayoutItem's ancestors change visibility, effectively hiding or showing this item.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BLayoutItem()`

```cpp
BLayoutItem::BLayoutItem(BMessage * archive)
```

Archive constructor. 


Creates a [BLayoutItem](classBLayoutItem.md) from the *archive* message.



**Since:** Haiku R1

---

### `AlignInFrame()`

```cpp
void BLayoutItem::AlignInFrame(BRect frame)
```

Position this [BLayoutItem](classBLayoutItem.md) within *frame*, given the value returned by [Alignment()](classBLayoutItem.md#a3f34ad935970e7d941dafe7ca5290d26), and the size constraints for this item. 



**Since:** Haiku R1

---

### `Alignment()`

```cpp
BAlignment BLayoutItem::Alignment()
```

Returns the requested alignment for this item. 


The value returned from this method is used in [BLayoutItem::AlignInFrame()](classBLayoutItem.md#a3b5b23daa375b3333fc58c9c22ce62fa), which BLayouts use to position and resize items. In a vertical [BGroupLayout](classBGroupLayout.md), for example, although each item recieves the same horizontal area, each item can use that area differently, aligning to the left, right or center for example.



**Since:** Haiku R1


Implemented in [BAbstractLayout](classBAbstractLayout.md#a218c3772949ac855126f461162fc1ee9), and [BSpaceLayoutItem](classBSpaceLayoutItem.md#ad97ec22e92e72a0b37a197d1a6f762b7).

---

### `AllArchived()`

```cpp
virtual status_t BLayoutItem::AllArchived(BMessage * into)const
```

Method relating to the use of `BArchiver`. 


This hook function is called once the first [BArchiver](../support_kit/classBArchiver.md) that was created in an archiving session is either destroyed, or has its Finish() method called. Implementations of this method can be used, in conjunction with [BArchiver::IsArchived()](../support_kit/classBArchiver.md#a77f099b123416c719be2cd78eb999d19), to reference objects in your archive that you do not own, depending on whether or not those objects were archived by their owners. Implementations of this method should call the implementation of their parent class, the same as for the [Archive()](classBLayoutItem.md#af2c2593e6179ee367ef26eff7ab7409f) method.



> [!WARNING]
> To guarantee that your [AllArchived()](classBLayoutItem.md#a13ec3faa075b23b3073f97531365102c) method will be called during archival, you must create a [BArchiver](../support_kit/classBArchiver.md) object in your [Archive()](classBLayoutItem.md#af2c2593e6179ee367ef26eff7ab7409f) implementation.



**See also:** [BArchiver](../support_kit/classBArchiver.md) [BArchiver::Finish()](../support_kit/classBArchiver.md#a7c82dbc0fb42795c575ac2c6a5405297)



**Since:** Haiku R1


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a4075315c407443a3b0dbb3d7551b53c9).


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a73b50e5ee03b980b4e8f08c875528162), [BCardLayout](classBCardLayout.md#ac561655882cd31e4f8a8b214de846fb6), [BLayout](classBLayout.md#ab9747436e251333693d54d29d472e2f9), [BGridLayout](classBGridLayout.md#adddbabf3f060e0e3d20af12cf3f3dab1), [BGroupLayout](classBGroupLayout.md#a62670753e05e05601592d49f0b5f438f), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#adb001699008fe0cb2eff51661da175e6).

---

### `AllUnarchived()`

```cpp
virtual status_t BLayoutItem::AllUnarchived(const BMessage * archive)
```

Method relating to the use of `BUnarchiver`. 


This hook function is called triggered in the [BUnarchiver::Finish()](../support_kit/classBUnarchiver.md#a7640fa5d84dc6dca19d7513326d2bba2) method. In this method, you can rebuild references to objects that may be direct children of your object, or may be children of other objects. Implementations of this method should call the implementation of their parent class, the same as for the [Archive()](classBLayoutItem.md#af2c2593e6179ee367ef26eff7ab7409f) method.



> [!WARNING]
> To guarantee that your [AllUnarchived()](classBLayoutItem.md#af78b72941cf1532299c2396cfeb7f9ed) method will be called during unarchival, you must create a [BUnarchiver](../support_kit/classBUnarchiver.md) object in your archive constructor.



**See also:** [BUnarchiver](../support_kit/classBUnarchiver.md), [BUnarchiver::Finish()](../support_kit/classBUnarchiver.md#a7640fa5d84dc6dca19d7513326d2bba2)



**Since:** Haiku R1


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a2b1d74c147ea18e4b4bfacd42f11e0d2).


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a2664ac14ab5dbe33a18cee88d420aa22), [BCardLayout](classBCardLayout.md#a30c68436cd5efd9708c1cfd75655647a), [BGridLayout](classBGridLayout.md#a2cd9bd9915c14ac32c0081234e12a5fb), [BGroupLayout](classBGroupLayout.md#a25bd4f838e672aa3eb611a616c5ec5e0), [BLayout](classBLayout.md#a3517e73d524672645425f80ebd4f53c7), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#a67ba660a95e7cf8647be8835184b6cc3).

---

### `AncestorVisibilityChanged()`

```cpp
void BLayoutItem::AncestorVisibilityChanged(bool shown)
```

Hook called when this [BLayoutItem](classBLayoutItem.md)'s ancestors change visibility, effectively hiding or showing this item. 


Implementations of this method should alter the onscreen visibility of this item. I.E. if *shown* is `false`, nothing should be drawn to represent this item.



> [!NOTE]
> This method should not effect the value returned by this object's [IsVisible()](classBLayoutItem.md#ad83886b5bef773a870e6668dd008a88a) method.


Parameters

| Parameter | Description |
| :--- | :--- |
| `shown` | `true` to show, `false` to hide. |





**Since:** Haiku R1


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a5e36e0a2cb89ef4f45905c20159ef371), and [BLayout](classBLayout.md#a9fe7eaa534d51bbfc807b9aca444176f).

---

### `Archive()`

```cpp
virtual status_t BLayoutItem::Archive(BMessage * into, bool deep = true)const
```

Archive the object into a [BMessage](../application_kit/classBMessage.md). 


You should call this method from your derived implementation as it adds the data needed to instantiate your object to the message.


Parameters

| Parameter | Description |
| :--- | :--- |
| `into` | The message you store your object in. |
| `deep` | If `true`, all children of this object should be archived as well. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The archive operation was successful. |
| B_BAD_VALUE | `NULL` *archive* message. |
| B_ERROR | The archive operation failed. |





**Since:** BeOS R3


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44).


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a76c6e663adb27a10972dafe22c898bf7), [BCardLayout](classBCardLayout.md#a0cfce7f1c906b28d8e3abaca74bcda56), [BGridLayout](classBGridLayout.md#aab5e2df95091bb76bb93628dcd01013e), [BGroupLayout](classBGroupLayout.md#aae43bdb3a725755664e55f13a054b510), [BLayout](classBLayout.md#a0d5f0b0a3ca81f5f7d54dae6ab7a099f), [BSpaceLayoutItem](classBSpaceLayoutItem.md#a27a757bd5903c14dce5a54af00177d4a), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#a405b207a3fa1770d5349de6d66705390).

---

### `AttachedToLayout()`

```cpp
void BLayoutItem::AttachedToLayout()
```

Hook called when this object is attached to a [BLayout](classBLayout.md) (via [BLayout::AddItem()](classBLayout.md#a61bab6592bb26173d12488526b203ead)) 



> [!NOTE]
> You can find the [BLayout](classBLayout.md) you've been attached to with the [Layout()](classBLayoutItem.md#ab760ea9f0eb6bb25063b5bac7a52ec3d) method.



**Since:** Haiku R1


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a0eb40b1488e9b5f524cbc263106e7f3b), and [BLayout](classBLayout.md#a18f9f855b86a1a517249288672adf680).

---

### `DetachedFromLayout()`

```cpp
void BLayoutItem::DetachedFromLayout(BLayout * layout)
```

Hook called when this object is attached to a [BLayout](classBLayout.md) (via [BLayout::RemoveItem()](classBLayout.md#abf0b19d4203e1a41292137fd8a2038d0)) 



> [!WARNING]
> You should not use this hook to reattach `this` to *[BLayout](classBLayout.md)*, doing so will cause undefined behaviour (probably a crash).


Parameters

| Parameter | Description |
| :--- | :--- |
| `layout` | The [BLayout](classBLayout.md) you were previously attached to. |





**Since:** Haiku R1


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a4535f6de7c5193ba20038b891944864b), and [BLayout](classBLayout.md#a1339f65fb6907b6944d24b2f37e6f738).

---

### `Frame()`

```cpp
BRect BLayoutItem::Frame()
```

Return the bounding frame of this item. 


The returned [BRect](classBRect.md) is in the coordinate system of the target view of the [BLayout](classBLayout.md) this item belongs to.



**Since:** Haiku R1


Implemented in [BAbstractLayout](classBAbstractLayout.md#a931bce77912316857d2e8d2a557e4241), and [BSpaceLayoutItem](classBSpaceLayoutItem.md#a019b39fdc8e3d14056a74a46333f57d6).

---

### `GetHeightForWidth()`

```cpp
void BLayoutItem::GetHeightForWidth(float width, float * min, float * max, float * preferred)
```

Get this [BLayoutItem](classBLayoutItem.md)'s height constraints for a given *width*. 


If a [BLayoutItem](classBLayoutItem.md) does not have height for width constraints ([HasHeightForWidth()](classBLayoutItem.md#a3186c8eec495915c5b074fe7d10dc94c) returns `false`) it does not need to implement this method.



> [!NOTE]
> It is prudent to compare *min*, *max*, *preferred* to `NULL` before dereferencing them.



**Since:** Haiku R1


Reimplemented in [BCardLayout](classBCardLayout.md#a5686748cc63ce7aa9879b19ab777fb44), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#a360c3c27eb293edea81b8cf8742d3913).

---

### `HasHeightForWidth()`

```cpp
bool BLayoutItem::HasHeightForWidth()
```

Returns whether or not this [BLayoutItem](classBLayoutItem.md)'s height constraints are dependent on its width. 



> [!NOTE]
> By default, this method returns `false`.



**Since:** Haiku R1


Reimplemented in [BCardLayout](classBCardLayout.md#a259483ea3d7732b211155b00cef22be8), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#a8b14614c8b378412107043b1e8e24ead).

---

### `InvalidateLayout()`

```cpp
void BLayoutItem::InvalidateLayout(bool children = false)
```

Invalidate the layout of this item, or the object it represents. 


Although this method is virtual, you should not override it in your classes, override [LayoutInvalidated()](classBLayoutItem.md#a69da4cf2822d9add9dbd6760e30eabfb) instead. This method will take care of calling the [InvalidateLayout()](classBLayoutItem.md#a9afedf1de602c6b277e8eb6eb3ff928d) methods of affected views/layouts/items. However, if there is an object that is somehow connected to this one by means other than the standard mechanisms provided by the Haiku API, you should use the [LayoutInvalidated()](classBLayoutItem.md#a69da4cf2822d9add9dbd6760e30eabfb) hook to do this.


Parameters

| Parameter | Description |
| :--- | :--- |
| `children` | Whether or not to invalidate children of this object. |





**Since:** Haiku R1


Reimplemented in [BLayout](classBLayout.md#a2b775de411ef6e9ecb4f7c412a26bf31).

---

### `IsVisible()`

```cpp
bool BLayoutItem::IsVisible()
```

Return the current local visibility of this item. If an item is not visible, it will not be given space by the [BLayout](classBLayout.md) it resides in. 


A simple implementation would return the last thing passed to [SetVisible()](classBLayoutItem.md#a51d14ca920b9f302662a619fa8b79957). A more complex implementation may deal with a [BView](classBView.md) that could be hidden in any number of ways.



**Since:** Haiku R1


Implemented in [BAbstractLayout](classBAbstractLayout.md#aac40eebbdd9c0fa7e594e5d1d9201a87), and [BSpaceLayoutItem](classBSpaceLayoutItem.md#a4a260f90fe800e6feb36e5ec4bfa83ff).

---

### `Layout()`

```cpp
BLayout * BLayoutItem::Layout()const
```

Returns the [BLayout](classBLayout.md) this [BLayoutItem](classBLayoutItem.md) resides in. 



**Since:** Haiku R1

---

### `LayoutData()`

```cpp
void * BLayoutItem::LayoutData()const
```

Retrieve arbitrary data attached to this [BLayoutItem](classBLayoutItem.md). 



> [!NOTE]
> This method should only be called by a [BLayout](classBLayout.md) subclass.



**Since:** Haiku R1

---

### `LayoutInvalidated()`

```cpp
void BLayoutItem::LayoutInvalidated(bool children)
```

Hook called from [InvalidateLayout()](classBLayoutItem.md#a9afedf1de602c6b277e8eb6eb3ff928d). 


Override this method to clean out an cached layout info. It is good practice to recreate such info only on demand, eg when [MinSize()](classBLayoutItem.md#aa6b24064b472cf72f98dbfd11198f067) or friends are called.


If *children* is `true`, then you should invalidate any information on child objects as well, and propagate the invalidation to them.



**Since:** Haiku R1


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#aa8d37f3c77c4fa240c0c18f800e7c64a), [BLayout](classBLayout.md#a76c0a3aee65267a10187e4081b6d240d), [BCardLayout](classBCardLayout.md#a98304460f6a41f4e3aa387d914310cf8), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#a213da2d0c283091e48562e8fbb448c5f).

---

### `MaxSize()`

```cpp
BSize BLayoutItem::MaxSize()
```

Returns the maximum desirable size for this item. 



**Since:** Haiku R1


Implemented in [BAbstractLayout](classBAbstractLayout.md#ad1ea5d04a5c8028f8295efde7106a66c), and [BSpaceLayoutItem](classBSpaceLayoutItem.md#ab6bd78081d23d6b3d0f7c337fd0a2930).

---

### `MinSize()`

```cpp
BSize BLayoutItem::MinSize()
```

Returns the minimum desirable size for this item. 



**Since:** Haiku R1


Implemented in [BAbstractLayout](classBAbstractLayout.md#a3f692cb3306ce726e3cc6d2771824cd5), and [BSpaceLayoutItem](classBSpaceLayoutItem.md#a999c87d6aeea8d8cf17787bcd71d4c3f).

---

### `Perform()`

```cpp
virtual status_t BLayoutItem::Perform(perform_code d, void * arg)
```

Perform some action (Internal method defined for binary compatibility purposes). 


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a827fa92febcf925f07545aa9777df9de).


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#aa4d7d592de1e566f73f440576d1c2cac), [BCardLayout](classBCardLayout.md#a7b75708b091f51e8dce826477f28e33a), [BGridLayout](classBGridLayout.md#a0ab603b381b9ba4d7efb3efbeae4940f), [BGroupLayout](classBGroupLayout.md#a31d82f6cd2fdecdc0a04d60d6e3943f7), [BLayout](classBLayout.md#adb8e95073f7626f04fe78337ca7114f8), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#aac851d9c86397296d0e7e69716c01926).

---

### `PreferredSize()`

```cpp
BSize BLayoutItem::PreferredSize()
```

Returns the preferred size for this item. 



**Since:** Haiku R1


Implemented in [BAbstractLayout](classBAbstractLayout.md#af5f21d9900c85ca053dba3938bef3fd3), and [BSpaceLayoutItem](classBSpaceLayoutItem.md#a03fdd0cc28dd13c93cd20e85f93b2945).

---

### `Relayout()`

```cpp
void BLayoutItem::Relayout(bool immediate = false)
```

Relayout any children or onscreen data this item contains. Often this request is forwarded to another object. 


The default implementation of this method will likely be sufficient in most cases. Assuming `this->View()` doesn't return `NULL`, the default implementation calls [Relayout()](classBLayoutItem.md#afddc9eb49deca3121887f0b923da6a0b) or [Layout()](classBLayoutItem.md#ab760ea9f0eb6bb25063b5bac7a52ec3d) on the value returned by [View()](classBLayoutItem.md#a4a053fcf62bc431028355efbd59873fc).



**Since:** Haiku R1


Reimplemented in [BLayout](classBLayout.md#a2a168d993feaf8fc58b53ded8243e7b7).

---

### `RemoveSelf()`

```cpp
bool BLayoutItem::RemoveSelf()
```

Remove this layout item from the [BLayout](classBLayout.md) it is a part of. 


This method works analoguous to [BView::RemoveSelf()](classBView.md#a87e0848b1760a9f28aad4516467a03ed), that is it removes itself from the parent layout and returns whether or not this was succesful.



**Returns:** `true` if the item was removed from the layout, or `false` if item was not part of a layout, or removal was succesful.



**Since:** Haiku R1

---

### `SetExplicitAlignment()`

```cpp
void BLayoutItem::SetExplicitAlignment(BAlignment alignment)
```

Set this item's explicit alignment, to be used in [Alignment()](classBLayoutItem.md#a3f34ad935970e7d941dafe7ca5290d26). 



**Since:** Haiku R1


Implemented in [BAbstractLayout](classBAbstractLayout.md#a3e7f4071b63452d77210f852cb92604d), and [BSpaceLayoutItem](classBSpaceLayoutItem.md#adfe30d9d69c35f667e7c9caae9956e67).


Referenced by [BLayoutBuilder::Grid< ParentBuilder >::AddMenuField()](classBLayoutBuilder_1_1Grid.md#aa626e7f8d7743e13be8dcbac5bed4b25), and [BLayoutBuilder::Grid< ParentBuilder >::AddTextControl()](classBLayoutBuilder_1_1Grid.md#adbf89ec8422af8181a1b4c88b23c99b7).

---

### `SetExplicitMaxSize()`

```cpp
void BLayoutItem::SetExplicitMaxSize(BSize size)
```

Set this item's explicit max size, to be used in [MaxSize()](classBLayoutItem.md#ac8279364e37b84f2b152fd052200f158). 



**Since:** Haiku R1


Implemented in [BAbstractLayout](classBAbstractLayout.md#aeb41b2e1e0b6414d0de4eeb4e5fb93e4), and [BSpaceLayoutItem](classBSpaceLayoutItem.md#aaeccb3f364ee28497f509f44ae097fdb).

---

### `SetExplicitMinSize()`

```cpp
void BLayoutItem::SetExplicitMinSize(BSize size)
```

Set this item's explicit min size, to be used in [MinSize()](classBLayoutItem.md#aa6b24064b472cf72f98dbfd11198f067). 


This forces the minimal size for the item and overrides any constraints that would normally be used to compute it. Most importantly, the minimal size of children is ignored, so setting this can lead to the children not fitting the view.



**Since:** Haiku R1


Implemented in [BAbstractLayout](classBAbstractLayout.md#af63e5777fabfb9be1f29286bf6931fe6), and [BSpaceLayoutItem](classBSpaceLayoutItem.md#a8085527e5311e748e83948116c23ab35).

---

### `SetExplicitPreferredSize()`

```cpp
void BLayoutItem::SetExplicitPreferredSize(BSize size)
```

Set this item's explicit preferred size, to be used in [PreferredSize()](classBLayoutItem.md#a7311fd45380396ae3840179f9b63fae3). 



**Since:** Haiku R1


Implemented in [BAbstractLayout](classBAbstractLayout.md#a577b9839ac8e726bbecc7f3e40bb01a3), and [BSpaceLayoutItem](classBSpaceLayoutItem.md#abc5a03d24165cb317858aefc998ca3b8).

---

### `SetExplicitSize()`

```cpp
void BLayoutItem::SetExplicitSize(BSize size)
```

Set the explicity size to *size*. 


This method is a convenience method that sets the minimum size, maximum size and preferred size to *size*, as to force this layout item to have a specific size.


Parameters

| Parameter | Description |
| :--- | :--- |
| `size` | The specific (non-zero) size for this layout item. |





**Since:** Haiku R1

---

### `SetFrame()`

```cpp
void BLayoutItem::SetFrame(BRect frame)
```

Set the bounding frame of this item. 


*frame* is in the coordinate system of the target view of the [BLayout](classBLayout.md) that this item belongs to.



**Since:** Haiku R1


Implemented in [BAbstractLayout](classBAbstractLayout.md#a879dd41748f05cab421789930e7bd7af), [BSpaceLayoutItem](classBSpaceLayoutItem.md#a8fe4a4566215f74842e7dc6e4b89269e), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#a8a4f4e152b4f6106cbc88fc0bb1f32d8).

---

### `SetLayoutData()`

```cpp
void BLayoutItem::SetLayoutData(void * data)
```

Attach arbitrary data to this [BLayoutItem](classBLayoutItem.md). 



> [!NOTE]
> This method should only be called by a [BLayout](classBLayout.md) subclass.



**Since:** Haiku R1

---

### `SetVisible()`

```cpp
void BLayoutItem::SetVisible(bool visible)
```

Set the local visibility of this item. 



**Since:** Haiku R1


Implemented in [BAbstractLayout](classBAbstractLayout.md#ae40de089e697c7ecb8466ec3e8bd87e8), and [BSpaceLayoutItem](classBSpaceLayoutItem.md#a31bfa01d4b25c761ee565436c5d29a9a).

---

### `View()`

```cpp
BView * BLayoutItem::View()
```

Return the [BView](classBView.md) this item is representing, or `NULL` if it does not represent any view. 


When a [BLayoutItem](classBLayoutItem.md) is added to a [BLayout](classBLayout.md), this method is called, and the returned [BView](classBView.md) will be added to the [BLayout](classBLayout.md)'s target view.



**Since:** Haiku R1


Reimplemented in [BLayout](classBLayout.md#aefd7bf5546d6b69d1561e7baebf15387).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBLayoutItem.html).
