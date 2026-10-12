---
name: BArchiver
type: class
kit: support_kit
brief: "A class that simplifies the archiving of complicated BArchivable hierarchies"
source: haiku-book
---

# BArchiver Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A class that simplifies the archiving of complicated [BArchivable](classBArchivable.md) hierarchies. 


The [BArchiver](classBArchiver.md) class is a small class that is used for archiving of complicated [BArchivable](classBArchivable.md) hierarchies. Such a hierarchy may include multiple [BArchivable](classBArchivable.md) objects, each of which might be referenced by many [BArchivable](classBArchivable.md) objects. With the [BArchiver](classBArchiver.md) class, you can be certain that each [BArchivable](classBArchivable.md) object is archived only once with very little work. When used in conjuction with the [BArchivable::AllArchived()](classBArchivable.md#a4075315c407443a3b0dbb3d7551b53c9) and [BArchivable::AllUnarchived()](classBArchivable.md#a2b1d74c147ea18e4b4bfacd42f11e0d2) methods, it is simple to rebuild your system of references upon unarchival so that they are equivalent to those that were present in your original hierarchy.


The objects you archive can be retrieved using a [BUnarchiver](classBUnarchiver.md) object.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BArchiver](#a77816a77b0589a0e136d8b44b440715b) (BMessage *archive) — Constructs a BArchiver object that manages archive.
* [~BArchiver](#a9eb0e393cc86926246d0662bf74db79b) () — Destroys a BArchiver object. If the BArchiver object has not had its Finish() method called, this will be done now.
* `status_t` [AddArchivable](#a237a50590efba0121bf12249c5b6cb7f) (const char *name, BArchivable *archivable, bool deep=true) — Adds a reference to archivable to the archive used to construct this BArchiver. May call archivable's Archive() method.
* `BMessage *` [ArchiveMessage](#a355bbcf04d61e561a2d304c035fe4052) () const — Returns the BMessage* used to construct this BArchiver. This is the archive that AddArchivable() modifies.
* `status_t` [Finish](#a7c82dbc0fb42795c575ac2c6a5405297) (status_t err=B_OK) — Report any archiving errors and possibly complete the archiving session.
* `status_t` [GetTokenForArchivable](#aa2e8cfc3e02979ab597ec08e0b99a3b1) (BArchivable *archivable, bool deep, int32 &_token) — Get a token representing a BArchivable object for this archiving session.
* `status_t` [GetTokenForArchivable](#a787a6a7972a6c4624829c5c8d8d16e55) (BArchivable *archivable, int32 &_token) — Equivalent to calling the expanded GetTokenForArchivable(
       BArchivable*, bool, int32&), with the deep parameter equal to true.
* `bool` [IsArchived](#a77f099b123416c719be2cd78eb999d19) (BArchivable *archivable) — Returns whether archivable has already been archived in this session.

## Detailed Member Documentation

### `BArchiver()`

```cpp
BArchiver::BArchiver(BMessage * archive)
```

Constructs a [BArchiver](classBArchiver.md) object that manages `archive`. 



**Since:** Haiku R1

---

### `~BArchiver()`

```cpp
BArchiver::~BArchiver()
```

Destroys a [BArchiver](classBArchiver.md) object. If the [BArchiver](classBArchiver.md) object has not had its [Finish()](classBArchiver.md#a7c82dbc0fb42795c575ac2c6a5405297) method called, this will be done now. 



**Since:** Haiku R1

---

### `AddArchivable()`

```cpp
status_t BArchiver::AddArchivable(const char * name, BArchivable * archivable, bool deep = true)
```

Adds a reference to `archivable` to the archive used to construct this [BArchiver](classBArchiver.md). May call `archivable's` Archive() method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | Where this reference will be stored in the archive. |
| `archivable` | The BArchivable* object that to reference. |
| `deep` | Passed to `archivable->Archive()` if `archivable` must be archived. |




Adds a reference to `archivable` to your archive. If `archivable` has not yet been archived, then its Archive() method is called. [BArchiver](classBArchiver.md) can only track [BArchivable](classBArchivable.md) objects that have been archived through this method or the [GetTokenForArchivable()](classBArchiver.md#a787a6a7972a6c4624829c5c8d8d16e55) methods.



> [!WARNING]
> If you manually archive an object, and then pass it to [AddArchivable()](classBArchiver.md#a237a50590efba0121bf12249c5b6cb7f) or [GetTokenForArchivable()](classBArchiver.md#a787a6a7972a6c4624829c5c8d8d16e55), it will be archived again, and when unarchived you will end up with two different [BArchivable](classBArchivable.md) objects.



**Since:** Haiku R1

---

### `ArchiveMessage()`

```cpp
const BMessage * BArchiver::ArchiveMessage()const
```

Returns the BMessage* used to construct this [BArchiver](classBArchiver.md). This is the archive that [AddArchivable()](classBArchiver.md#a237a50590efba0121bf12249c5b6cb7f) modifies. 



**Since:** Haiku R1

---

### `Finish()`

```cpp
status_t BArchiver::Finish(status_t err = B_OK)
```

Report any archiving errors and possibly complete the archiving session. 


This method may finish an archiving session (triggering the call of all archived objects' AllArchived() methods) if the following conditions are true:


* No errors have been reported to this or any other [BArchiver](classBArchiver.md) object within this session.

* This is the last remaining [BArchiver](classBArchiver.md) that has not had its [Finish()](classBArchiver.md#a7c82dbc0fb42795c575ac2c6a5405297) method invoked.



If you call this method with an error code not equal to B_OK, then this archiving session has failed, archived objects will not have their AllArchived() methods called, and any subsequent calls to this method on any [BArchiver](classBArchiver.md) objects in this session will return your error code.



**Returns:** The first error reported in this archiving session, or `B_OK`.



**Since:** Haiku R1

---

### `GetTokenForArchivable()`

```cpp
status_t BArchiver::GetTokenForArchivable(BArchivable * archivable, bool deep, int32 & _token)
```

Get a token representing a [BArchivable](classBArchivable.md) object for this archiving session. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archivable` | The [BArchivable](classBArchivable.md) object for which you wish to get a token. |
| `deep` | Controls how `archivable` will be archived, if it has not yet been archived in this session. |
| `_token` | The token representing `archivable` is stored here. |




Retrieves or creates a token to represent `archivable` in this archiving session. If `archivable` has not yet been archived, it will be now. If `archivable` gets archived, the `deep` parameter will be passed to its Archive() method.



> [!WARNING]
> If you manually archive an object, and then pass it to [GetTokenForArchivable()](classBArchiver.md#a787a6a7972a6c4624829c5c8d8d16e55), it will be archived again, and when unarchived you will end up with two different [BArchivable](classBArchivable.md) objects.



**Since:** Haiku R1

---

### `GetTokenForArchivable()`

```cpp
status_t BArchiver::GetTokenForArchivable(BArchivable * archivable, int32 & _token)
```

Equivalent to calling the expanded [GetTokenForArchivable(
       BArchivable*, bool, int32&)](classBArchiver.md#aa2e8cfc3e02979ab597ec08e0b99a3b1), with the deep parameter equal to `true`. 



**See also:** [GetTokenForArchivable(BArchivable*, bool, int32&)](classBArchiver.md#aa2e8cfc3e02979ab597ec08e0b99a3b1)



**Since:** Haiku R1


References [GetTokenForArchivable()](classBArchiver.md#a787a6a7972a6c4624829c5c8d8d16e55).


Referenced by [GetTokenForArchivable()](classBArchiver.md#a787a6a7972a6c4624829c5c8d8d16e55).

---

### `IsArchived()`

```cpp
bool BArchiver::IsArchived(BArchivable * archivable)
```

Returns whether `archivable` has already been archived in this session. 



**Returns:** Whether or not the object has already been archived.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | `archivable` has been archived in this archiving session. |
| false | `archivable` has not been archived in this archiving session. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBArchiver.html).
