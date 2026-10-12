---
name: BShelf
type: class
kit: interface_kit
brief: "A container attached to a BView that accepts BDragger objects (replicants)"
source: haiku-book
---

# BShelf Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A container attached to a [BView](classBView.md) that accepts [BDragger](classBDragger.md) objects (replicants). 


A [BShelf](classBShelf.md) object creates a container where to store [BDragger](classBDragger.md) objects, also known as "replicants". When the user drops a replicant on the shelf, or a shelf is loaded from an archived message, it will load and display it as a child object. Once created, it could either save the replicant's data in a filesystem entry or in a [BDataIO](../support_kit/classBDataIO.md) data stream and retrieve the data from either source to display the replicant.


During the construction, or afterwards with [SetAllowsDragging()](classBShelf.md#ac577daed252c534e44c3a4dbe0460d9f), it can be configured to allow or disallow to accept the replicants dropped by the user onto the shelf. This behavior can be queried by calling the method [AllowsDragging()](classBShelf.md#ae00815117907e08475191b5dadaadb64).


The *shelfType* parameter from the constructors allows the shelf to have a filter-like system. This is reflected in the archived field `shelf_type`. In this way, the shelf could reject any replicant whose shelf type does not match shelf's type, or the other way around. But the shelf accepts by default the replicants without a type (and a shelf without a type could also accept any kind of replicants, as long as they do not reject it). However, this behavior can be disabled by using the type enforcement with [SetTypeEnforced()](classBShelf.md#a0a26218791d9b717a5c72c3bbc2822dc), allowing the shelf to reject any replicant strictly without the same type of the shelf. The state of this behavior can be queried with [IsTypeEnforced()](classBShelf.md#a2256b0c3adf369aa53780158c4772046).


When a replicant was unable to be loaded, a "zombie view" could be deployed instead. "Zombie views" are placeholder views that are deployed in place of a replicant whose application of origin cannot be found. This behavior can be modified to disable the generation of zombie views with [SetAllowsZombies()](classBShelf.md#a472104e37d047cbbb365856bc44788c1), or to hide them with SetDisplayZombies(). [AllowsZombies()](classBShelf.md#ad0020b6fed020286127b484c27be0cc1) and [DisplaysZombies()](classBShelf.md#a8569175f0202bef15c43c0bf66cfca55) queries the state of any of those behaviors.


This class supports the standard scripting protocol.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BShelf](#a74c3eb1e7df394c9c25fb1be3c683bbb) (BDataIO *stream, BView *view, bool allowDrags=true, const char *shelfType=NULL) — Creates a BShelf object that is attached to a view, and sets stream as the data stream source from where to load the archived BDragger objects and where to save them.
* [BShelf](#a5819ea6f90b64994e04de74bee634659) (BMessage *archive) — Unimplemented.
* [BShelf](#a8eee6effe455b73dd773d820811bd9ab) (BView *view, bool allowDrags=true, const char *shelfType=NULL) — Creates a BShelf object that is attached to a view.
* [BShelf](#a3a05367b7bce98a20e1d8a69c2878f7f) (const entry_ref *ref, BView *view, bool allowDrags=true, const char *shelfType=NULL) — Creates a BShelf object that is attached to a view, and sets ref as the source from where to load the archived BDragger objects and where to save them.
* `virtual` [~BShelf](#a9773dceb19fe546c1223e0ece4954b07) () — The destructor calls Save(), frees the data sources and replicant data of the replicants and detaches itself from the container BView.
* `status_t` [AddReplicant](#a751b89386476573ea9e3067cdb442bf1) (BMessage *archive, BPoint location) — Adds a replicant whose data is in archive to the shelf in location.
* `bool` [AllowsDragging](#ae00815117907e08475191b5dadaadb64) () const — Check if the user is able to drag replicants to the shelf.
* `bool` [AllowsZombies](#ad0020b6fed020286127b484c27be0cc1) () const — Checks if zombie views are allowed in the shelf.
* `int32` [CountReplicants](#a0a81ddb72c0e453e8689cba81b5123f4) () const — Tells the number of replicants currently contained by the shelf.
* `status_t` [DeleteReplicant](#a4c33ff81d1a13b16518f8714170fdf5c) (BMessage *archive) — Removes the replicant identified by the archive replicant message.
* `status_t` [DeleteReplicant](#afa3694905532f3bb6ced4f73c1a978e2) (BView *replicant) — Removes the replicant referred by the replicant BView.
* `status_t` [DeleteReplicant](#a72affe5085013d0e9565a7c1b693a339) (int32 index) — Removes the replicant identified by index.
* `bool` [DisplaysZombies](#a8569175f0202bef15c43c0bf66cfca55) () const — Checks if zombie views are displayed on the shelf.
* `virtual status_t` [GetSupportedSuites](#a5b14d8c9f67cdec075beab9bfefa281d) (BMessage *data) — Report the suites of messages this control understands.
* `int32` [IndexOf](#a26d148ce316b615a00e9213f099e8774) (const BMessage *archive) const — Returns the index of a replicant identified by its archive replicant message.
* `int32` [IndexOf](#a5db2ee9c4562b8397199eeeede027077) (const BView *replicantView) const — Returns the index of a replicant identified by its replicantView view.
* `int32` [IndexOf](#a569af2235a1766e8f2a3b23880c4ba72) (uint32 id) const — Returns the index of a replicant identified by its unique identifier id.
* `bool` [IsDirty](#a65ffd970a534f772463bc08116184f32) () const — Retrieves the "dirty" flag status of the shelf.
* `bool` [IsTypeEnforced](#a2256b0c3adf369aa53780158c4772046) () const — Checks if the shelf enforces the type or not.
* `virtual void` [MessageReceived](#a6355e985c4a15187a523035c983f3063) (BMessage *message) — Handle message received by the associated looper.
* `virtual status_t` [Perform](#afbf73f485603cf3a50ff1bd4c99d9a6a) (perform_code code, void *data) — Perform some action (Internal method defined for binary compatibility purposes).
* `BMessage *` [ReplicantAt](#a114924415a66d6a845f7f69c8ce2b9a3) (int32 index, BView **view=NULL, uint32 *uid=NULL, status_t *perr=NULL) const — Retrieves the replicant data referenced by its index.
* `virtual BHandler *` [ResolveSpecifier](#af4294354dfabd65838909b174990db8c) (BMessage *message, int32 index, BMessage *specifier, int32 form, const char *property) — Determine the proper handler for a scripting message.
* `status_t` [Save](#a20251e6d69474eb00623dea8eec3d322) () — Saves the BShelf contents as an archived BMessage into a filesystem entry or BDataIO stream if any of them were specified with the constructor.
* `BDataIO *` [SaveLocation](#ad7951ea246adefa9476dec231e67f105) (entry_ref *ref) const — Retrieves the save location for the shelf data.
* `void` [SetAllowsDragging](#ac577daed252c534e44c3a4dbe0460d9f) (bool state) — Allows or disallows the shelf to accept the replicants dragged into it by the user.
* `void` [SetAllowsZombies](#a472104e37d047cbbb365856bc44788c1) (bool state) — Sets the shelf to allow zombie views or not.
* `virtual void` [SetDirty](#a93f73b1550a81012915321cdc84bc02f) (bool state) — Sets the "dirty" state flag. This flag is used by the application and is also automatically applied when the save location is changed.
* `void` [SetDisplaysZombies](#a95cf8fdb466da32beebec49a01224451) (bool state) — Sets the shelf to display zombie views or not.
* `status_t` [SetSaveLocation](#ab7ff52e4037c424be4839f4c94c11447) (BDataIO *stream) — Configures the save location of the shelf data to stream.
* `status_t` [SetSaveLocation](#a5e800097dfe777998927303153868eeb) (const entry_ref *ref) — Configures the save location of the shelf data to ref.
* `void` [SetTypeEnforced](#a0a26218791d9b717a5c72c3bbc2822dc) (bool state) — Sets the type enforcement flag.
* [BHandler](#a2142e21fe781b24f914ec2086e5f05b7) (const char *name=NULL) — Construct a new handler with a name.
* `virtual` [~BHandler](#a928254034959d19ef588b7898a6f8194) () — Free the filters of this handler, as well as the list of observers.
* `virtual status_t` [Perform](#a4e6ebc7ebcb72855a1f0fee7bde99766) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).
* [BHandler](#add8fa081a7bb8633581e78777b215d0b) (BMessage *data) — Construct a handler from an archived message.
* `BLooper *` [Looper](#ac8e949959b12e602e3b0c4f023c60e6c) () const — Return a pointer to the looper that this handler is associated with.
* `void` [SetName](#abf861126df4b6e71b9261a99da4ad0eb) (const char *name) — Set or change the name of this handler.
* `const char *` [Name](#a40b246ac272e09b2f641d1290be21200) () const — Return the name of this handler.
* `virtual void` [SetNextHandler](#a02f78779c8141987d6030e73c22e734a) (BHandler *handler) — Set the next handler in the chain that the message is passed on to if this handler cannot process it.
* `BHandler *` [NextHandler](#a92855d8f88f6072e7225bde292feaa38) () const — Return the next hander in the chain to which the message is passed on.
* `virtual void` [AddFilter](#a862bea548363faac6f883b348cbed838) (BMessageFilter *filter) — Add filter as a prerequisite to this handler.
* `virtual bool` [RemoveFilter](#a2b608135b27f283802648e7c6f8cdc83) (BMessageFilter *filter) — Remove filter from the filter list.
* `virtual void` [SetFilterList](#a503344dc801858e1f5f419be3919e9cf) (BList *filters) — Set the internal list of filters to filters.
* `BList *` [FilterList](#a909662a049856f6863a934cf18161554) () — Return a pointer to the list of filters.
* `bool` [LockLooper](#a9d64bf66b4914918e24390d117e83477) () — Lock the looper associated with this handler.
* `status_t` [LockLooperWithTimeout](#afa0099ff6defcb6d64e3ee1c2fb47afe) (bigtime_t timeout) — Lock the looper associated with this handler, with a time out value.
* `void` [UnlockLooper](#ab131af7eb7aa2b9eea3a11ac1bfd4c03) () — Unlock the looper.
* `status_t` [StartWatching](#af7d600e33a0586af7444d9abc8500504) (BMessenger target, uint32 what) — Subscribe this handler to watch a specific state change of a target.
* `status_t` [StartWatchingAll](#a58d7c8d30e47fbb7590f10dea1f21166) (BMessenger target) — Subscribe this handler to watch a target for all events.
* `status_t` [StopWatching](#a9d1f0d55b3dc7337058aba769b4e4f93) (BMessenger target, uint32 what) — Unsubscribe this handler from watching a specific state.
* `status_t` [StopWatchingAll](#a199c167e0dcee95aa65d09435804b3d9) (BMessenger target) — Unsubscribe this handler from watching all states.
* `status_t` [StartWatching](#a20713ff6ee9df49a014f391374eaf689) (BHandler *observer, uint32 what) — Subscribe an observer for a specific state change of this handler.
* `status_t` [StartWatchingAll](#a31927c51d89e0e3b3bf609a786ee6c3b) (BHandler *observer) — Subscribe an observer for a all state changes.
* `status_t` [StopWatching](#ad3544be491270f856a0af8d36ce02d78) (BHandler *observer, uint32 what) — Unsubscribe an observer from watching a specific state.
* `status_t` [StopWatchingAll](#a8b9a424ce63f5932666094b6eadf10cf) (BHandler *observer) — Unsubscribe an observer from watching all states.
* `virtual void` [SendNotices](#a71bf72dc17a64bcd42656722271a9e0c) (uint32 what, const BMessage *notice=NULL) — Emit a state change to the observers.
* `bool` [IsWatched](#a581b84f0f067afa88768ce6a0c07f59f) () const — Check if there are any observers watching this handler.
* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).

### Protected Member Functions

* `virtual BPoint` [AdjustReplicantBy](#a154d4f97e6364fac71b824b295f39669) (BRect, BMessage *) const — Adjusts the replicant's location to fit the rect in the shelf.
* `virtual bool` [CanAcceptReplicantMessage](#a196170a463b4b90152c64b1d844bfd44) (BMessage *archive) const — Determines if the archive message where the replicant should be contained is formatted as expected.
* `virtual bool` [CanAcceptReplicantView](#afea898a78005207f83e731473aea39ec) (BRect, BView *, BMessage *) const — Determines whether the replicant's view is accepted or rejected.
* `virtual void` [ReplicantDeleted](#a0e2452823ea8a0f401c129fee46b6368) (int32 index, const BMessage *archive, const BView *replicant) — Unimplemented.

### Archiving

* `virtual status_t` [Archive](#a098c2a557715a3a4fa91a66125653f0e) (BMessage *archive, bool deep=true) const — Unimplemented.
* `static BArchivable *` [Instantiate](#ab340bc823609ffb04ae5117e38ed0585) (BMessage *archive) — Unimplemented.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#a0c23aeb48d578525f81ba6d47f968528) (BMessage *data) — Static method to instantiate a handler from an archived message.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BShelf()`

```cpp
BShelf::BShelf(BView * view, bool allowDrags = true, const char * shelfType = NULL)
```

Creates a [BShelf](classBShelf.md) object that is attached to a view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `view` | The container [BView](classBView.md). |
| `allowDrags` | Specifies if the shelf accepts replicants dragged to it by the user or not. |
| `shelfType` | Specifies a filter-like name for the object's underlying [BHandler](../application_kit/classBHandler.md). This can be used to reject [BDragger](classBDragger.md) objects whose names does not match shelfType. |





**Since:** BeOS R3

---

### `BShelf()`

```cpp
BShelf::BShelf(const entry_ref * ref, BView * view, bool allowDrags = true, const char * shelfType = NULL)
```

Creates a [BShelf](classBShelf.md) object that is attached to a view, and sets *ref* as the source from where to load the archived [BDragger](classBDragger.md) objects and where to save them. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The filesystem entry from where the archived [BDragger](classBDragger.md) objects will be loaded during the initialization and saved. |
| `view` | The container [BView](classBView.md). |
| `allowDrags` | Specifies if the shelf accepts replicants dragged to it by the user or not. |
| `shelfType` | Specifies a filter-like name for the object's underlying [BHandler](../application_kit/classBHandler.md). This can be used to reject [BDragger](classBDragger.md) objects whose names does not match shelfType. |





**Since:** BeOS R3

---

### `BShelf()`

```cpp
BShelf::BShelf(BDataIO * stream, BView * view, bool allowDrags = true, const char * shelfType = NULL)
```

Creates a [BShelf](classBShelf.md) object that is attached to a view, and sets *stream* as the data stream source from where to load the archived [BDragger](classBDragger.md) objects and where to save them. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `stream` | The data stream from where the archived [BDragger](classBDragger.md) objects will be loaded during the initialization and saved. |
| `view` | The container [BView](classBView.md). |
| `allowDrags` | Specifies if the shelf accepts replicants dragged to it by the user or not. |
| `shelfType` | Specifies a filter-like name for the object's underlying [BHandler](../application_kit/classBHandler.md). This can be used to reject [BDragger](classBDragger.md) objects whose names does not match shelfType. |





**Since:** BeOS R3

---

### `BShelf()`

```cpp
BShelf::BShelf(BMessage * archive)
```

Unimplemented. 



**Since:** BeOS R3

---

### `~BShelf()`

```cpp
BShelf::~BShelf()
```

The destructor calls [Save()](classBShelf.md#a20251e6d69474eb00623dea8eec3d322), frees the data sources and replicant data of the replicants and detaches itself from the container [BView](classBView.md). 



**Since:** BeOS R3

---

### `AddReplicant()`

```cpp
status_t BShelf::AddReplicant(BMessage * archive, BPoint location)
```

Adds a replicant whose data is in *archive* to the shelf in *location*. 


This method is automatically called when a replicant is dropped on the shelf.


If type enforcement is enabled, the replicant must have the same type, otherwise it will be rejected.


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The archive data from where the replicant information is retrieved. |
| `location` | The place where the replicant was dropped on the shelf. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_ERROR | One of these happened:   - the replicant's type and shelf's type does not match;   - the replicant data was rejected by [CanAcceptReplicantMessage()](classBShelf.md#a196170a463b4b90152c64b1d844bfd44);   - the replicant only allows a unique instance and there is already an instance of the replicant on the shelf;   - the object could not be instantiated and the archive did not contain an instantiated [BView](classBView.md);   - the replicant could not be loaded, and the creation of a zombie view was disabled. |
| B_OK | The replicant was added successfully. |





**Since:** BeOS R3

---

### `AdjustReplicantBy()`

```cpp
BPoint BShelf::AdjustReplicantBy(BRect rect, BMessage * archive)const
```

Adjusts the replicant's location to fit the rect in the shelf. 


Called upon a replicant was dropped on the shelf.



**Since:** BeOS R3

---

### `AllowsDragging()`

```cpp
bool BShelf::AllowsDragging()const
```

Check if the user is able to drag replicants to the shelf. 



**Returns:** `true` if the shelf accepts the replicants dragged into it, or `false` otherwise.



**Since:** BeOS R3

---

### `AllowsZombies()`

```cpp
bool BShelf::AllowsZombies()const
```

Checks if zombie views are allowed in the shelf. 



**Returns:** `true` if the shelf allows zombie views, or `false` otherwise.



**Since:** BeOS R3

---

### `Archive()`

```cpp
status_t BShelf::Archive(BMessage * archive, bool deep = true)const
```

Unimplemented. 



**Since:** BeOS R3


Reimplemented from [BHandler](../application_kit/classBHandler.md#ac2711ccff5e7f711244c88a5642c83db).

---

### `CanAcceptReplicantMessage()`

```cpp
bool BShelf::CanAcceptReplicantMessage(BMessage * archive)const
```

Determines if the *archive* message where the replicant should be contained is formatted as expected. 


It is called during the execution of [AddReplicant()](classBShelf.md#a751b89386476573ea9e3067cdb442bf1).


An undesired format of the message makes it to return to false and discard it.


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The replicant's message. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The replicant was accepted. |
| false | The replicant was rejected. |





**Since:** BeOS R3

---

### `CanAcceptReplicantView()`

```cpp
bool BShelf::CanAcceptReplicantView(BRect rect, BView * view, BMessage * archive)const
```

Determines whether the replicant's view is accepted or rejected. 


It is called during the execution of [AddReplicant()](classBShelf.md#a751b89386476573ea9e3067cdb442bf1).


If the view has not been accepted, the replicant will be rejected.


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The rect that the replicant will occupy on the shelf. |
| `view` | The replicant's view. |
| `archive` | The replicant's archived message. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The replicant was accepted. |
| false | The replicant was rejected. |





**Since:** BeOS R3

---

### `CountReplicants()`

```cpp
int32 BShelf::CountReplicants()const
```

Tells the number of replicants currently contained by the shelf. 



**Returns:** The number of attached replicants.



**Since:** BeOS R3

---

### `DeleteReplicant()`

```cpp
status_t BShelf::DeleteReplicant(BMessage * archive)
```

Removes the replicant identified by the *archive* replicant message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The replicant's data archive of reference. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The replicant was removed successfully. |
| B_BAD_VALUE | There is no replicant identified by such message. |





**Since:** BeOS R3

---

### `DeleteReplicant()`

```cpp
status_t BShelf::DeleteReplicant(BView * replicant)
```

Removes the replicant referred by the *replicant* [BView](classBView.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replicant` | The view identified by the *replicant* [BView](classBView.md). |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The replicant was removed successfully. |
| B_BAD_VALUE | There is no replicant identified by such [BView](classBView.md). |





**Since:** BeOS R3

---

### `DeleteReplicant()`

```cpp
status_t BShelf::DeleteReplicant(int32 index)
```

Removes the replicant identified by *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The replicant's index number. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The replicant was removed successfully. |
| B_BAD_INDEX | There is no replicant identified by such index. |





**Since:** BeOS R3

---

### `DisplaysZombies()`

```cpp
bool BShelf::DisplaysZombies()const
```

Checks if zombie views are displayed on the shelf. 



**Returns:** `true` if the shelf displays zombie views, or `false` otherwise.



**Since:** BeOS R3

---

### `GetSupportedSuites()`

```cpp
status_t BShelf::GetSupportedSuites(BMessage * data)
```

Report the suites of messages this control understands. 


Adds the string "suite/vnd.Be-shelf" to the message.



**See also:** [BHandler::GetSupportedSuites()](../application_kit/classBHandler.md#acf34435dada239f411e8e034e0ea36b5)



**Since:** BeOS R3


Reimplemented from [BHandler](../application_kit/classBHandler.md#acf34435dada239f411e8e034e0ea36b5).

---

### `IndexOf()`

```cpp
int32 BShelf::IndexOf(const BMessage * archive)const
```

Returns the index of a replicant identified by its *archive* replicant message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The replicant's message archive. |





**Returns:** The index of the specified replicant, or `-1` if it does not exist.



**Since:** BeOS R3

---

### `IndexOf()`

```cpp
int32 BShelf::IndexOf(const BView * replicantView)const
```

Returns the index of a replicant identified by its *replicantView* view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replicantView` | The replicant's [BView](classBView.md). |





**Returns:** The index of the specified replicant, or `-1` if it does not exist.



**Since:** BeOS R3

---

### `IndexOf()`

```cpp
int32 BShelf::IndexOf(uint32 id)const
```

Returns the index of a replicant identified by its unique identifier *id*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `id` | The replicant's unique identifier. |





**Returns:** The index of the specified replicant, or `-1` if it does not exist.



**Since:** BeOS R3

---

### `Instantiate()`

```cpp
BArchivable * BShelf::Instantiate(BMessage * archive)
```

Unimplemented. 



**Since:** BeOS R3

---

### `IsDirty()`

```cpp
bool BShelf::IsDirty()const
```

Retrieves the "dirty" flag status of the shelf. 



**Returns:** `true` if the shelf is "dirty", or `false` otherwise.



**See also:** [SetDirty(bool)](classBShelf.md#a93f73b1550a81012915321cdc84bc02f)



**Since:** BeOS R3

---

### `IsTypeEnforced()`

```cpp
bool BShelf::IsTypeEnforced()const
```

Checks if the shelf enforces the type or not. 



**Returns:** `true` if the shelf enforces the type filtering, or `false` otherwise.



**Since:** BeOS R3

---

### `MessageReceived()`

```cpp
void BShelf::MessageReceived(BMessage * message)
```

Handle *message* received by the associated looper. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The *message* received by the associated looper. |





**See also:** [BHandler::MessageReceived()](../application_kit/classBHandler.md#aeecda5017e0081db617f23bbff71fb53)



**Since:** BeOS R3


Reimplemented from [BHandler](../application_kit/classBHandler.md#aeecda5017e0081db617f23bbff71fb53).

---

### `Perform()`

```cpp
virtual status_t BShelf::Perform(perform_code d, void * arg)
```

Perform some action (Internal method defined for binary compatibility purposes). 


Reimplemented from [BHandler](../application_kit/classBHandler.md#a4e6ebc7ebcb72855a1f0fee7bde99766).

---

### `ReplicantAt()`

```cpp
BMessage * BShelf::ReplicantAt(int32 index, BView ** view = NULL, uint32 * uid = NULL, status_t * perr = NULL)const
```

Retrieves the replicant data referenced by its *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The replicant index. |
| `view` | If not `NULL`, returns the respective [BView](classBView.md) of the replicant at *index*, or `NULL` otherwise. |
| `uid` | If not `NULL`, returns the unique identifier of the replicant at *index*, or  ```cpp ~(uint32)0 ```   (maximum value of an unsigned integer) otherwise. |
| `perr` | If not `NULL`, returns the replicant's current status code (usually B_OK if everything is OK), or `B_BAD_INDEX` otherwise. |





**Returns:** A replicant's data message, or NULL if there is not a replicant at such *index*.



**Since:** BeOS R3

---

### `ReplicantDeleted()`

```cpp
void BShelf::ReplicantDeleted(int32 index, const BMessage * archive, const BView * replicant)
```

Unimplemented. 



**Since:** BeOS R3

---

### `ResolveSpecifier()`

```cpp
virtual BHandler * BShelf::ResolveSpecifier(BMessage * message, int32 index, BMessage * specifier, int32 what, const char * property)
```

Determine the proper handler for a scripting message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The scripting message to determine the handler. |
| `index` | The index of the specifier. |
| `specifier` | The message which contains the specifier. |
| `what` | The 'what' field of the specifier message. |
| `property` | The name of the target property. |





**Returns:** A pointer to the proper [BHandler](../application_kit/classBHandler.md) for the given scripting message.



**Since:** BeOS R3


Reimplemented from [BHandler](../application_kit/classBHandler.md#a76439ffaf84e65232698d2a4a3317d22).

---

### `Save()`

```cpp
status_t BShelf::Save()
```

Saves the [BShelf](classBShelf.md) contents as an archived [BMessage](../application_kit/classBMessage.md) into a filesystem entry or [BDataIO](../support_kit/classBDataIO.md) stream if any of them were specified with the constructor. 


In case there was not a data destination specified with the constructor, it can be set with [SetSaveLocation()](classBShelf.md#ab7ff52e4037c424be4839f4c94c11447).



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation was performed successfully. |
| B_ERROR | The archiving operation failed, or there was not any data destination specified. |





**Since:** BeOS R3

---

### `SaveLocation()`

```cpp
BDataIO * BShelf::SaveLocation(entry_ref * ref)const
```

Retrieves the save location for the shelf data. 


If *ref* is not `NULL`, there it will be saved an [entry_ref](../storage_kit/structentry__ref.md) of the saving location.



**Returns:** A [BDataIO](../support_kit/classBDataIO.md) stream where the shelf data is saved, or `NULL` if the saving location does not translate into a [BDataIO](../support_kit/classBDataIO.md).



**Since:** BeOS R3

---

### `SetAllowsDragging()`

```cpp
void BShelf::SetAllowsDragging(bool state)
```

Allows or disallows the shelf to accept the replicants dragged into it by the user. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `state` | `true` to allow dragging, or `false` to disallow it. |





**Since:** BeOS R3

---

### `SetAllowsZombies()`

```cpp
void BShelf::SetAllowsZombies(bool state)
```

Sets the shelf to allow zombie views or not. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `state` | `true` if zombie views are allowed, or `false` otherwise. |





**Since:** BeOS R3

---

### `SetDirty()`

```cpp
void BShelf::SetDirty(bool state)
```

Sets the "dirty" state flag. This flag is used by the application and is also automatically applied when the save location is changed. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `state` | `true` to set it as "dirty", or `false` to remove the flag. |





**See also:** [IsDirty()](classBShelf.md#a65ffd970a534f772463bc08116184f32)



**Since:** BeOS R3

---

### `SetDisplaysZombies()`

```cpp
void BShelf::SetDisplaysZombies(bool state)
```

Sets the shelf to display zombie views or not. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `state` | `true` if zombie views are displayed, or `false` otherwise. |





**Since:** BeOS R3

---

### `SetSaveLocation()`

```cpp
status_t BShelf::SetSaveLocation(BDataIO * stream)
```

Configures the save location of the shelf data to *stream*. 


It also sets the "dirty" flag.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The save location was set to *stream*. |





**Since:** BeOS R3

---

### `SetSaveLocation()`

```cpp
status_t BShelf::SetSaveLocation(const entry_ref * ref)
```

Configures the save location of the shelf data to *ref*. 


It also sets the "dirty" flag.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The save location was set to *ref*. |





**Since:** BeOS R3

---

### `SetTypeEnforced()`

```cpp
void BShelf::SetTypeEnforced(bool state)
```

Sets the type enforcement flag. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `state` | `true` to enforce the type and reject replicants without the same type, or `false` to disable the enforcement. |





**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBShelf.html).
