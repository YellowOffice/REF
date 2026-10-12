---
name: BPicture
type: class
kit: interface_kit
brief: "Records a series of drawing instructions that can be \"replayed\" later"
source: haiku-book
---

# BPicture Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Records a series of drawing instructions that can be "replayed" later. 


A [BPicture](classBPicture.md), unlike a [BBitmap](classBBitmap.md), is independent of the display resolution as it contains drawing instructions rather than image data.


To begin drawing you first create a new [BPicture](classBPicture.md) object and pass it to [BView::BeginPicture()](classBView.md#a14155192773aad22ebe47a9975afac5f). All subsequent drawing instructions are drawn into the [BPicture](classBPicture.md) object instead of the [BView](classBView.md). When you are done recording call [BView::EndPicture()](classBView.md#ae01506892a9b2d39f6df13726be9d0af) which stops drawing into the [BPicture](classBPicture.md) object and passes a pointer to it back to the caller.


For example: 


```cpp
BPicture* picture;
view->BeginPicture(new BPicture);
// drawing instructions go here
picture = view->EndPicture();
```

Only drawing instructions performed directly on the view, not its child views are sent to the [BPicture](classBPicture.md) object and [BPicture](classBPicture.md) captures only primitive graphics operations. The view must be attached to a window for the drawing instruction to be recorded. Drawing instructions are recorded even if the view is hidden or resides outside the clipping region or the window is off-screen.


The [BPicture](classBPicture.md) object data is erased when passed to [BView::BeginPicture()](classBView.md#a14155192773aad22ebe47a9975afac5f). If you'd like to append data to a [BPicture](classBPicture.md) object instead use [BView::AppendToPicture()](classBView.md#a2d73d2f2b0b35390929cf54fbfa5ecff). Both [BView::BeginPicture()](classBView.md#a14155192773aad22ebe47a9975afac5f) and [BView::AppendToPicture()](classBView.md#a2d73d2f2b0b35390929cf54fbfa5ecff) must be followed by a call to [BView::EndPicture()](classBView.md#ae01506892a9b2d39f6df13726be9d0af) to finish recording.



**See also:** [BView::AppendToPicture()](classBView.md#a2d73d2f2b0b35390929cf54fbfa5ecff)



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BPicture](#ad3e5dca72d104acdfeb0145f24bd634d) () — Initializes an empty BPicture object.
* [BPicture](#a8ec07c636d394d68bfba82706fb3231d) (BMessage *data) — Initializes an BPicture object copying the data from from the passed in data archive.
* [BPicture](#a17506ec76a02406ae4c568bf0b07bae6) (const BPicture &other) — Initializes an BPicture object copying the data from otherPicture.
* `virtual` [~BPicture](#a709258d8bf01b57f44bc0935dbf02e33) () — Destroys the BPicture object and deletes all associated data.
* `status_t` [Flatten](#af773a67253f860f33f71e68289c45ab6) (BDataIO *stream) — Flattens the contents of the BPicture object into stream.
* `virtual status_t` [Perform](#acb9a2bdcbad655692e126a3dc2be3166) (perform_code code, void *arg) — Perform some action (internal method defined for binary compatibility purposes).
* `status_t` [Play](#a97a2ca69d6eb3902d66a2940fbcae9bb) (void **callBackTable, int32 tableEntries, void *userData) — Plays back a picture using the passed in call back functions.
* `status_t` [Unflatten](#a84f37addb7b9d536cdc5d0413646d5a5) (BDataIO *stream) — Unflattens the contents from the stream into the BPicture object.
* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).

### Archiving

* `virtual status_t` [Archive](#a9854a69b51d30728a20fd8688ce7a0f0) (BMessage *data, bool deep=true) const — Archives the BPicture object into the data message.
* `static BArchivable *` [Instantiate](#a5dddcb1b146250d2ca15da3d48c4d7dd) (BMessage *data) — Returns a pointer to a new BPicture object created from the BPicture data archived in data.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BPicture()`

```cpp
BPicture::BPicture()
```

Initializes an empty [BPicture](classBPicture.md) object. 



**Since:** BeOS R3

---

### `BPicture()`

```cpp
BPicture::BPicture(const BPicture & otherPicture)
```

Initializes an [BPicture](classBPicture.md) object copying the data from *otherPicture*. 



**Since:** BeOS R3

---

### `BPicture()`

```cpp
BPicture::BPicture(BMessage * data)
```

Initializes an [BPicture](classBPicture.md) object copying the data from from the passed in *data* archive. 



**Since:** BeOS R3

---

### `~BPicture()`

```cpp
BPicture::~BPicture()
```

Destroys the [BPicture](classBPicture.md) object and deletes all associated data. 



**Since:** BeOS R3

---

### `Archive()`

```cpp
status_t BPicture::Archive(BMessage * data, bool deep = true)const
```

Archives the [BPicture](classBPicture.md) object into the *data* message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A pointer to the [BMessage](../application_kit/classBMessage.md) object to archive into. |
| `deep` | The parameter has no effect to this method. |





**Returns:** A status code, `B_OK` if everything went well or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object was archived successfully. |
| B_NO_MEMORY | Ran out of memory while archiving the object. |





**See also:** [BArchivable::Archive()](../support_kit/classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44)



**Since:** BeOS R3


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44).

---

### `Flatten()`

```cpp
status_t BPicture::Flatten(BDataIO * stream)
```

Flattens the contents of the [BPicture](classBPicture.md) object into *stream*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `stream` | The stream to write to. |





**Returns:** A status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The [BPicture](classBPicture.md) object was flattened successfully. |
| B_BAD_VALUE | The *stream* pointer was `NULL` or the data was invalid. |
| B_IO_ERROR | The number of bytes written does not equal the size of the contents of the [BPicture](classBPicture.md) object. |





**Since:** Haiku R1

---

### `Instantiate()`

```cpp
BArchivable * BPicture::Instantiate(BMessage * data)
```

Returns a pointer to a new [BPicture](classBPicture.md) object created from the [BPicture](classBPicture.md) data archived in *data*. 



**Returns:** A newly created [BPicture](classBPicture.md) object or `NULL` if the message doesn't contain an archived [BPicture](classBPicture.md).



**See also:** [BArchivable::Instantiate()](../support_kit/classBArchivable.md#a04efcb17fa2a64a776923cc12303efcd)



**Since:** BeOS R3

---

### `Perform()`

```cpp
status_t BPicture::Perform(perform_code code, void * arg)
```

Perform some action (internal method defined for binary compatibility purposes). 



**Since:** Haiku R1


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a827fa92febcf925f07545aa9777df9de).

---

### `Play()`

```cpp
status_t BPicture::Play(void ** callBackTable, int32 tableEntries, void * user)
```

Plays back a picture using the passed in call back functions. 


See [http://haiku-os.org/legacy-docs/bebook/BPicture.html#BPicture_Play](http://haiku-os.org/legacy-docs/bebook/BPicture.html#BPicture_Play) for details.


Parameters

| Parameter | Description |
| :--- | :--- |
| `callBackTable` | An array of pointers to pointers of call back functions. |
| `tableEntries` | Specifies the number of function pointers found in *callBackTable*. |
| `user` | A hook to pass additional data to each call back function. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The [BPicture](classBPicture.md) object was played back successfully. |
| B_ERROR | [BPicture](classBPicture.md) data is `NULL`. |





**Since:** BeOS R3

---

### `Unflatten()`

```cpp
status_t BPicture::Unflatten(BDataIO * stream)
```

Unflattens the contents from the *stream* into the [BPicture](classBPicture.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `stream` | The stream to read from. |





**Returns:** A status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object was unflattened successfully. |
| B_BAD_VALUE | The *stream* pointer was `NULL` or the data was invalid. |
| B_IO_ERROR | The number of bytes read does not equal the size of the contents of the [BPicture](classBPicture.md) object. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPicture.html).
