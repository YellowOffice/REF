---
name: BCardLayout
type: class
kit: interface_kit
brief: "The BCardLayout class is a simple BLayout subclass that arranges the items as a stack of cards with only one card being on top and visible to the user"
source: haiku-book
---

# BCardLayout Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Layout API](group__layout.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

The [BCardLayout](classBCardLayout.md) class is a simple [BLayout](classBLayout.md) subclass that arranges the items as a stack of cards with only one card being on top and visible to the user. 


Once you have set up the items in the container, you can select which one is visible using the [SetVisibleItem()](classBCardLayout.md#ac95bfc498c345988fba42857ce9c2c69) methods on this class. When there is no item on top, the system's default grey background is shown.


This view is useful when you have a number of pre-loaded UI elements, and you want to be able to swap between them quickly, while retaining the underlying state. The container itself will retain a fixed size, so from a visual perspective, it is imperative that the items in the stack have comparable dimensions.


An example usage is for a configuration wizard, where the user will need to complete a number of steps to perform an action. Because you want to the user to experience all these steps as a smooth flow within one window, you can set up the individual pages as views, and add these as cards to the card layout. Then you tie the *Next* and *Previous* buttons to switch between the visible cards using the [BCardLayout::SetVisible()](classBAbstractLayout.md#ae40de089e697c7ecb8466ec3e8bd87e8) methods.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BCardLayout](#a01d825ad601014b72e35fd6651deb5ca) () — Create a new card layout.
* [BCardLayout](#ade15ab13e63ab6b624813c74593d8c02) (BMessage *from) — Constructs a BCardLayout from an archive message.
* `virtual` [~BCardLayout](#a53d3608894935fe26ead5deb18428d91) () — Destructor.
* `virtual status_t` [Archive](#a0cfce7f1c906b28d8e3abaca74bcda56) (BMessage *into, bool deep=true) const — Archive this layout into a BMessage.
* `virtual BAlignment` [BaseAlignment](#aaeca998a3a94cdd7026df33390d9aa07) () — Overridden hook method from BAbstractLayout.
* `virtual BSize` [BaseMaxSize](#a8a081d05a58a6dec0e00859ee9bbfc63) () — Overridden hook method from BAbstractLayout.
* `virtual BSize` [BaseMinSize](#aedec5db8dfdb7dbc8035308cdc38d5bf) () — Overridden hook method from BAbstractLayout.
* `virtual BSize` [BasePreferredSize](#a80ade79f9bfda23a54dcac1cff06e5b2) () — Overridden hook method from BAbstractLayout.
* `virtual void` [GetHeightForWidth](#a5686748cc63ce7aa9879b19ab777fb44) (float width, float *min, float *max, float *preferred) — Overridden hook method from BAbstractLayout.
* `virtual bool` [HasHeightForWidth](#a259483ea3d7732b211155b00cef22be8) () — Overridden hook method from BAbstractLayout.
* `virtual status_t` [Perform](#a7b75708b091f51e8dce826477f28e33a) (perform_code d, void *arg) — Overridden hook method from BAbstractLayout.
* `void` [SetVisibleItem](#a0568aa153555bf7501c8fa61d65c1399) (BLayoutItem *item) — Set the current visible item to item.
* `void` [SetVisibleItem](#ac95bfc498c345988fba42857ce9c2c69) (int32 index) — Set the current visible item to the item at index.
* `int32` [VisibleIndex](#a71b48b12bf6f03240d21db69d4dce75a) () const — Get the index of the currently visible item.
* `BLayoutItem *` [VisibleItem](#ad326a97ba7e690e145f7d429c44bb8f2) () const — Get a pointer to the currently visible item.
* `virtual BAlignment` [Alignment](#a218c3772949ac855126f461162fc1ee9) ()
* `virtual status_t` [Archive](#a76c6e663adb27a10972dafe22c898bf7) (BMessage *into, bool deep=true) const — Archives this layout into archive. If deep is true, also archives the items in this layout, calling ItemArchived() for each one.
* `virtual BRect` [Frame](#a931bce77912316857d2e8d2a557e4241) () — Return the bounding frame of this item.
* `virtual bool` [IsVisible](#aac40eebbdd9c0fa7e594e5d1d9201a87) () — Return the current local visibility of this item. If an item is not visible, it will not be given space by the BLayout it resides in.
* `virtual BSize` [MaxSize](#ad1ea5d04a5c8028f8295efde7106a66c) ()
* `virtual BSize` [MinSize](#a3f692cb3306ce726e3cc6d2771824cd5) ()
* `virtual status_t` [Perform](#aa4d7d592de1e566f73f440576d1c2cac) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).
* `virtual BSize` [PreferredSize](#af5f21d9900c85ca053dba3938bef3fd3) ()
* `virtual void` [SetExplicitAlignment](#a3e7f4071b63452d77210f852cb92604d) (BAlignment alignment) — Set this item's explicit alignment, to be used in Alignment().
* `virtual void` [SetExplicitMaxSize](#aeb41b2e1e0b6414d0de4eeb4e5fb93e4) (BSize size) — Set this item's explicit max size, to be used in MaxSize().
* `virtual void` [SetExplicitMinSize](#af63e5777fabfb9be1f29286bf6931fe6) (BSize size) — Set this item's explicit min size, to be used in MinSize().
* `virtual void` [SetExplicitPreferredSize](#a577b9839ac8e726bbecc7f3e40bb01a3) (BSize size) — Set this item's explicit preferred size, to be used in PreferredSize().
* `virtual void` [SetFrame](#a879dd41748f05cab421789930e7bd7af) (BRect frame) — Set the bounding frame of this item.
* `virtual void` [SetVisible](#ae40de089e697c7ecb8466ec3e8bd87e8) (bool visible) — Set the local visibility of this item.
* [BAbstractLayout](#ac31ae4b204f6731fec17f7af2ed25859) () — Construct a BAbstractLayout.
* [BAbstractLayout](#ae7eea1f1b57d19981c210085953cae76) (BMessage *from) — Archive constructor.
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
* `bool` [AncestorsVisible](#a4f2ff9362ef1e84d7c886c58881d2be9) () const — Get the visibility of the ancestors of this layout.
* `BRect` [LayoutArea](#a25735d4b3149817ab91b2f4cff0a2fed) () — Returns the on-screen area this layout has received to lay out its items in.
* `virtual void` [InvalidateLayout](#a2b775de411ef6e9ecb4f7c412a26bf31) (bool children=false) — Invalidate this layout and any cached data this layout has relating to positioning and sizing of its items.
* `void` [RequireLayout](#a1983a8770e7cd89c3f1afc4d961230d5) () — Flag this layout as stale, i.e. any cached data may still be valid, but the items need to be repositioned or resized.
* `bool` [IsValid](#a9b5b6b764433dee59ed4d1f01aaada04) () — Returns whether this layout has been invalidated (via BLayout::InvalidateLayout()) and has not yet been validated (by doing a layout, or by its ResetLayoutInvalidation() method.
* `void` [EnableLayoutInvalidation](#a7f369cb77173c3922dddbb38db893a6c) () — Re-enable layout invalidation after a call to DisableLayoutInvalidation().
* `void` [DisableLayoutInvalidation](#a509ff18ffa060bd9aab042c4ee6af245) () — Disable layout invalidation notifications, i.e. calls to this object's InvalidateLayout() method.
* [BLayoutItem](#ac639d9cfa9b8124106ef2d8bc5badb2e) (BMessage *from) — Archive constructor.
* `virtual status_t` [Archive](#af2c2593e6179ee367ef26eff7ab7409f) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `BLayout *` [Layout](#ab760ea9f0eb6bb25063b5bac7a52ec3d) () const — Returns the BLayout this BLayoutItem resides in.
* `virtual status_t` [Perform](#a38b237fb8bbd1d0054e3a2b4cbc1fd15) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).
* `bool` [RemoveSelf](#af4059e73a30336f0ae6bbbc04c70dd6a) () — Remove this layout item from the BLayout it is a part of.
* `virtual BView *` [View](#a4a053fcf62bc431028355efbd59873fc) () — Return the BView this item is representing, or NULL if it does not represent any view.
* `void` [SetExplicitSize](#ac630c7ab0e98d5da0225792e31f596f1) (BSize size) — Set the explicity size to size.
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

### Static Public Member Functions

* `static BArchivable *` [Instantiate](#a93849be2d8eaa1ec5470d1e190ae875c) (BMessage *from) — Instantiate a BCardLayout object from message from.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

### Protected Member Functions

* `virtual status_t` [AllArchived](#ac561655882cd31e4f8a8b214de846fb6) (BMessage *archive) const — Hook method overridden from BArchivable.
* `virtual status_t` [AllUnarchived](#a30c68436cd5efd9708c1cfd75655647a) (const BMessage *from) — Hook method overridden from BArchivable.
* `virtual void` [DoLayout](#adb91400ccc94cdbbba90efe8158c933f) () — Hook method overridden from BAbstractLayout.
* `virtual bool` [ItemAdded](#a44ea0d7a577626d6992e292bd93556bc) (BLayoutItem *item, int32 atIndex) — Hook method overridden from BAbstractLayout.
* `virtual status_t` [ItemArchived](#a8190101471e608007ca0b1864056512c) (BMessage *into, BLayoutItem *item, int32 index) const — Hook method overridden from BArchivable.
* `virtual void` [ItemRemoved](#ab1b92790589cc18c25c9c5ec9521fd62) (BLayoutItem *item, int32 fromIndex) — Hook method overridden from BAbstractLayout.
* `virtual status_t` [ItemUnarchived](#a54cbd1654003320469e93c258091f840) (const BMessage *from, BLayoutItem *item, int32 index) — Hook method overridden from BArchivable.
* `virtual void` [LayoutInvalidated](#a98304460f6a41f4e3aa387d914310cf8) (bool children=false) — Hook method overridden from BAbstractLayout.
* `virtual status_t` [AllArchived](#a73b50e5ee03b980b4e8f08c875528162) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2664ac14ab5dbe33a18cee88d420aa22) (const BMessage *from) — Unarchives the BLayoutItem's for this layout, calling ItemUnarchived() for each one.
* `virtual void` [AncestorVisibilityChanged](#a5e36e0a2cb89ef4f45905c20159ef371) (bool shown) — Hook method inherited from BLayoutItem, classes derived from BLayout must include the BLayout version of this method in their implementation.
* `virtual void` [AttachedToLayout](#a0eb40b1488e9b5f524cbc263106e7f3b) () — Hook method inherited from BLayoutItem, classes derived from BLayout must include the BLayout version of this method in their implementation.
* `virtual void` [DetachedFromLayout](#a4535f6de7c5193ba20038b891944864b) (BLayout *layout) — Hook method inherited from BLayoutItem, classes derived from BLayout must include the BLayout version of this method in their implementation.
* `virtual bool` [ItemAdded](#a842b424b62039753db229d3deafd0d10) (BLayoutItem *item, int32 atIndex) — Hook method called when item is added to this layout.
* `virtual status_t` [ItemArchived](#a8f3461939aac1452b9e34ff707b38684) (BMessage *into, BLayoutItem *item, int32 index) const — Hook for derived classes to add data specific to item to the into BMessage. item resides at index.
* `virtual void` [ItemRemoved](#a4df45f148af285d521bc5d6a491dac7b) (BLayoutItem *item, int32 fromIndex) — Hook method called when item is removed from this layout.
* `virtual status_t` [ItemUnarchived](#a9c3fd4aa60076e9869fa937d37f55ad3) (const BMessage *from, BLayoutItem *item, int32 index) — Hook for derived classes to retrieve data specific to item from the from BMessage. item resides at index.
* `virtual void` [LayoutInvalidated](#aa8d37f3c77c4fa240c0c18f800e7c64a) (bool children)
* `virtual void` [OwnerChanged](#a3aca5334eed301df4013fb2a3fdfd5ac) (BView *was) — Hook method called when this layout is attached to a BView.
* `virtual status_t` [AllArchived](#ab9747436e251333693d54d29d472e2f9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `void` [VisibilityChanged](#a7df37ec98c2d29dca5ce4f2246c5665a) (bool show) — Method to be called by derived classes in their SetVisible() implementation. Calls AncestorVisibilityChanged() on the items in this BLayout.
* `void` [ResetLayoutInvalidation](#aacf1392bbef13efc20277e15595bb329) () — Reset layout invalidation, causing InvalidateLayout calls to proceed again. This method should be called once any cached data has been validated, or updated to valid values.
* `virtual status_t` [AllArchived](#a13ec3faa075b23b3073f97531365102c) (BMessage *into) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#af78b72941cf1532299c2396cfeb7f9ed) (const BMessage *from) — Method relating to the use of BUnarchiver.

## Detailed Member Documentation

### `BCardLayout()`

```cpp
BCardLayout::BCardLayout()
```

Create a new card layout. 



**Since:** Haiku R1

---

### `BCardLayout()`

```cpp
BCardLayout::BCardLayout(BMessage * from)
```

Constructs a [BCardLayout](classBCardLayout.md) *from* an archive message. 


This method is usually not called directly, if you want to build a card layout from an archived message you should call [Instantiate()](classBCardLayout.md#a93849be2d8eaa1ec5470d1e190ae875c) instead because it can handle errors properly.


Parameters

| Parameter | Description |
| :--- | :--- |
| `from` | The [BMessage](../application_kit/classBMessage.md) that contains the card layout. |





**Since:** Haiku R1

---

### `~BCardLayout()`

```cpp
BCardLayout::~BCardLayout()
```

Destructor. 



**Since:** Haiku R1

---

### `AllArchived()`

```cpp
status_t BCardLayout::AllArchived(BMessage * archive)const
```

Hook method overridden from [BArchivable](../support_kit/classBArchivable.md). 



**Since:** Haiku R1


Reimplemented from [BAbstractLayout](classBAbstractLayout.md#a73b50e5ee03b980b4e8f08c875528162).

---

### `AllUnarchived()`

```cpp
status_t BCardLayout::AllUnarchived(const BMessage * from)
```

Hook method overridden from [BArchivable](../support_kit/classBArchivable.md). 



**Since:** Haiku R1


Reimplemented from [BAbstractLayout](classBAbstractLayout.md#a2664ac14ab5dbe33a18cee88d420aa22).

---

### `Archive()`

```cpp
status_t BCardLayout::Archive(BMessage * into, bool deep = true)const
```

Archive this layout *into* a [BMessage](../application_kit/classBMessage.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `into` | The message to which to archive into. |
| `deep` | When `true`, the children of this layout will also be added. |





**Since:** Haiku R1


Reimplemented from [BAbstractLayout](classBAbstractLayout.md#a76c6e663adb27a10972dafe22c898bf7).

---

### `BaseAlignment()`

```cpp
BAlignment BCardLayout::BaseAlignment()
```

Overridden hook method from [BAbstractLayout](classBAbstractLayout.md). 



**Since:** Haiku R1


Reimplemented from [BAbstractLayout](classBAbstractLayout.md#a4f637a263f6b087334d946bf97e307ca).

---

### `BaseMaxSize()`

```cpp
BSize BCardLayout::BaseMaxSize()
```

Overridden hook method from [BAbstractLayout](classBAbstractLayout.md). 



**Since:** Haiku R1


Reimplemented from [BAbstractLayout](classBAbstractLayout.md#a7e6be2609135ea8b87a370bbc49d454c).

---

### `BaseMinSize()`

```cpp
BSize BCardLayout::BaseMinSize()
```

Overridden hook method from [BAbstractLayout](classBAbstractLayout.md). 



**Since:** Haiku R1


Reimplemented from [BAbstractLayout](classBAbstractLayout.md#a71018d789f5374ecf4b5acc82ea0d9a6).

---

### `BasePreferredSize()`

```cpp
BSize BCardLayout::BasePreferredSize()
```

Overridden hook method from [BAbstractLayout](classBAbstractLayout.md). 



**Since:** Haiku R1


Reimplemented from [BAbstractLayout](classBAbstractLayout.md#afdc5353db27d60c86c2e723a846446a4).

---

### `DoLayout()`

```cpp
void BCardLayout::DoLayout()
```

Hook method overridden from [BAbstractLayout](classBAbstractLayout.md). 



**Since:** Haiku R1


Implements [BLayout](classBLayout.md#a972a7f273fc24f7665f5918e99989658).

---

### `GetHeightForWidth()`

```cpp
void BCardLayout::GetHeightForWidth(float width, float * min, float * max, float * preferred)
```

Overridden hook method from [BAbstractLayout](classBAbstractLayout.md). 



**Since:** Haiku R1


Reimplemented from [BLayoutItem](classBLayoutItem.md#addd90adf76c9caad200f6f465c06e0bf).

---

### `HasHeightForWidth()`

```cpp
bool BCardLayout::HasHeightForWidth()
```

Overridden hook method from [BAbstractLayout](classBAbstractLayout.md). 



**Since:** Haiku R1


Reimplemented from [BLayoutItem](classBLayoutItem.md#a3186c8eec495915c5b074fe7d10dc94c).

---

### `Instantiate()`

```cpp
static BArchivable * BCardLayout::Instantiate(BMessage * from)
```

Instantiate a [BCardLayout](classBCardLayout.md) object from message *from*. 



**Since:** Haiku R1

---

### `ItemAdded()`

```cpp
bool BCardLayout::ItemAdded(BLayoutItem * item, int32 atIndex)
```

Hook method overridden from [BAbstractLayout](classBAbstractLayout.md). 



**Since:** Haiku R1


Reimplemented from [BAbstractLayout](classBAbstractLayout.md#a842b424b62039753db229d3deafd0d10).

---

### `ItemArchived()`

```cpp
status_t BCardLayout::ItemArchived(BMessage * into, BLayoutItem * item, int32 index)const
```

Hook method overridden from [BArchivable](../support_kit/classBArchivable.md). 



**Since:** Haiku R1


Reimplemented from [BAbstractLayout](classBAbstractLayout.md#a8f3461939aac1452b9e34ff707b38684).

---

### `ItemRemoved()`

```cpp
void BCardLayout::ItemRemoved(BLayoutItem * item, int32 fromIndex)
```

Hook method overridden from [BAbstractLayout](classBAbstractLayout.md). 



**Since:** Haiku R1


Reimplemented from [BAbstractLayout](classBAbstractLayout.md#a4df45f148af285d521bc5d6a491dac7b).

---

### `ItemUnarchived()`

```cpp
status_t BCardLayout::ItemUnarchived(const BMessage * from, BLayoutItem * item, int32 index)
```

Hook method overridden from [BArchivable](../support_kit/classBArchivable.md). 



**Since:** Haiku R1


Reimplemented from [BAbstractLayout](classBAbstractLayout.md#a9c3fd4aa60076e9869fa937d37f55ad3).

---

### `LayoutInvalidated()`

```cpp
void BCardLayout::LayoutInvalidated(bool children = false)
```

Hook method overridden from [BAbstractLayout](classBAbstractLayout.md). 



**Since:** Haiku R1


Reimplemented from [BAbstractLayout](classBAbstractLayout.md#aa8d37f3c77c4fa240c0c18f800e7c64a).

---

### `Perform()`

```cpp
status_t BCardLayout::Perform(perform_code d, void * arg)
```

Overridden hook method from [BAbstractLayout](classBAbstractLayout.md). 



**Since:** Haiku R1


Reimplemented from [BAbstractLayout](classBAbstractLayout.md#aa4d7d592de1e566f73f440576d1c2cac).

---

### `SetVisibleItem()`

```cpp
void BCardLayout::SetVisibleItem(BLayoutItem * item)
```

Set the current visible item to *item*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | A pointer to an item that is already added to this layout. When a reference to an item not on the stack, or `NULL` is passed, then no item will be displayed and the view will reset to the default grey background. |





**Since:** Haiku R1

---

### `SetVisibleItem()`

```cpp
void BCardLayout::SetVisibleItem(int32 index)
```

Set the current visible item to the item at *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | This is a zero-based index for the item you want to display. If the item does not exist (it is lower than 0 or it is higher than the number of items), no item will be displayed and the view will reset to the default grey background. |





**Since:** Haiku R1

---

### `VisibleIndex()`

```cpp
int32 BCardLayout::VisibleIndex()const
```

Get the index of the currently visible item. 



**Returns:** Returns the zero-based index, or -1 if there is no item visible.



**Since:** Haiku R1

---

### `VisibleItem()`

```cpp
BLayoutItem * BCardLayout::VisibleItem()const
```

Get a pointer to the currently visible item. 



**Returns:** This method returns a pointer to the currently visible layout item, or `NULL` if there is no card visible.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBCardLayout.html).
