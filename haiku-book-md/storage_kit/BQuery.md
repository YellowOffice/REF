---
name: BQuery
type: class
kit: storage_kit
brief: "Provides an interface for creating file system queries and implements BEntryList methods for iterating through the results"
source: haiku-book
---

# BQuery Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Provides an interface for creating file system queries and implements [BEntryList](classBEntryList.md) methods for iterating through the results. 



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BQuery](#a1314925aad6b0a1663e5c73196aac5f9) () — Creates an uninitialized BQuery object.
* `virtual` [~BQuery](#ac7d7b1e4fb011605eaa5ed2dfcc7165e) () — Destroys the BQuery object and frees any associated resources.
* `status_t` [Clear](#af6c12ffd1d1c74c451ae1a03ee33c7d0) () — Resets the object to a uninitialized state.
* `status_t` [Fetch](#aa2a6473e999bf602cb5684e1477ecc3b) () — Start fetching entries satisfying the predicate.
* `status_t` [PushAttr](#a486babcb3938a19035aa820c85c10088) (const char *attrName) — Pushes an attribute name onto the predicate stack.
* `status_t` [PushOp](#a17f934eed4967e0df7a67a41336f88da) (query_op op) — Pushes an operator onto the predicate stack.
* `status_t` [PushUInt32](#a1cb827689d0485df5151661474f5c450) (uint32 value) — Pushes a uint32 onto the predicate stack.
* `status_t` [PushInt32](#a635dcf559feb1a07bb5910fab3a84b13) (int32 value) — Pushes an int32 onto the predicate stack.
* `status_t` [PushUInt64](#a21c56cfb7bbf927d702dab55ae333481) (uint64 value) — Pushes a uint64 onto the predicate stack.
* `status_t` [PushInt64](#a581f2eec46eb664088d76d027b510612) (int64 value) — Pushes an int64 onto the predicate stack.
* `status_t` [PushFloat](#a67e418693af55811941975b4da275b1d) (float value) — Pushes a float onto the predicate stack.
* `status_t` [PushDouble](#a7e654307d914dd003f7dc5dfe38af22f) (double value) — Pushes a double onto the predicate stack.
* `status_t` [PushString](#aa5c9d0d2558cda8b127d705f9abfde54) (const char *value, bool caseInsensitive=false) — Pushes a string onto the predicate stack.
* `status_t` [PushDate](#a0c01d4a0c19b3af80d1c861ca8ec3e6c) (const char *date) — Pushes a date string onto the predicate stack.
* `status_t` [SetVolume](#aa49ccd947942b5eca16c52a56a9a13db) (const BVolume *volume) — Assigns volume to the BQuery object.
* `status_t` [SetPredicate](#a8dc3c9a0aa6fb7c991a88a5731fc6cae) (const char *expression) — Assigns the passed-in predicate expression.
* `status_t` [SetTarget](#aca4694dedfd74796a38992ca256bc260) (BMessenger messenger) — Assigns the target messenger and makes the query live.
* `status_t` [SetFlags](#ae497989322ff5f7ceffbbcf1036813cc) (uint32 flags) — Sets the flags the query will be opened with.
* `bool` [IsLive](#a9a6755cdc56b04b07feceacdc1051b04) () const — Gets whether the query associated with this object is live.
* `size_t` [PredicateLength](#a0566fa5220d288eaf9aece48a0d0d5d9) () — Gets the length of the predicate string.
* `dev_t` [TargetDevice](#ab5d775120b8a329d94da275466c06880) () const — Gets the device ID identifying the volume of the BQuery object.
* `status_t` [GetPredicate](#a0735d502fefe1bfa6b9fd514f584658c) (char *buffer, size_t length) — Fills out buffer with the predicate string assigned to the BQuery object.
* `status_t` [GetPredicate](#a4964d96bf0349c95ff912c532f9326a8) (BString *predicate) — Fills out the passed-in BString object with the predicate string assigned to the BQuery object.
* `virtual status_t` [GetNextEntry](#ab30c05e8425a5c39dd35bd5fe5b05748) (BEntry *entry, bool traverse=false) — Fills out entry with the next entry traversing symlinks if traverse is true.
* `virtual status_t` [GetNextRef](#a40b44c5c8e047d005572334dd681bd37) (entry_ref *ref) — Fills out ref with the next entry as an entry_ref.
* `virtual int32` [GetNextDirents](#af5a9ba3e24f68c59b1247b7181433d23) (struct dirent *buffer, size_t length, int32 count=INT_MAX) — Fill out up to count entries into the array of dirent structs pointed to by buffer.
* `virtual status_t` [Rewind](#a42e73f8b1328e0a0bf42610a87a97e4a) () — Rewinds the entry list back to the first entry.
* `virtual int32` [CountEntries](#ab57f2b6d7a84c557f77a77d3baaca421) () — Unimplemented.
* [BEntryList](#adf5344c4229922691642b6e07c29bcaa) () — Creates a BEntryList object.
* `virtual` [~BEntryList](#ac239f4229be2d0a1c9a58c83f503be4c) () — Frees all resources associated with the BEntryList object.
* `virtual int32` [CountEntries](#a290b792f7b12265c10ba589aa969b862) ()=0 — Returns the number of entries in the list.
* `virtual int32` [GetNextDirents](#a2f8498249c876866d5f53a8b89044871) (struct dirent *direntBuffer, size_t bufferSize, int32 maxEntries=INT_MAX)=0 — Returns the BEntryList's next entries as dirent structures.
* `virtual status_t` [GetNextEntry](#a52e6c79344a6e511e7890f008e7281d1) (BEntry *entry, bool traverse=false)=0 — Returns the BEntryList's next entry as a BEntry.
* `virtual status_t` [GetNextRef](#a908ff7149239ab66683b12b27be917ee) (entry_ref *ref)=0 — Returns the BEntryList's next entry as an entry_ref.
* `virtual status_t` [Rewind](#a6cbcd041425e5a1225a762c72a4eb8af) ()=0 — Rewinds the list pointer to the beginning of the list.

## Detailed Member Documentation

### `BQuery()`

```cpp
BQuery::BQuery()
```

Creates an uninitialized [BQuery](classBQuery.md) object. 



**See also:** [SetPredicate()](classBQuery.md#a8dc3c9a0aa6fb7c991a88a5731fc6cae)



**Since:** BeOS R3

---

### `~BQuery()`

```cpp
BQuery::~BQuery()
```

Destroys the [BQuery](classBQuery.md) object and frees any associated resources. 



**Since:** BeOS R3

---

### `Clear()`

```cpp
status_t BQuery::Clear()
```

Resets the object to a uninitialized state. 



**Returns:** `B_OK`



**Since:** BeOS R3

---

### `CountEntries()`

```cpp
int32 BQuery::CountEntries()
```

Unimplemented. 



**Returns:** `B_ERROR`.



**Since:** BeOS R3


Implements [BEntryList](classBEntryList.md#a290b792f7b12265c10ba589aa969b862).

---

### `Fetch()`

```cpp
status_t BQuery::Fetch()
```

Start fetching entries satisfying the predicate. 


After [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b) has been called [GetNextEntry()](classBQuery.md#ab30c05e8425a5c39dd35bd5fe5b05748), [GetNextRef()](classBQuery.md#a40b44c5c8e047d005572334dd681bd37) and [GetNextDirents()](classBQuery.md#af5a9ba3e24f68c59b1247b7181433d23) can be used to retrieve the entities. Live query updates may be sent immediately after this method has been called.


[Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b) fails if it has already been called. To reuse the [BQuery](classBQuery.md) object it must first be reset with the [Clear()](classBQuery.md#af6c12ffd1d1c74c451ae1a03ee33c7d0) method.



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The object predicate or the volume wasn't set. |
| B_BAD_VALUE | The object predicate was invalid. |
| B_NOT_ALLOWED | [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b) already called. |





**Since:** BeOS R3

---

### `GetNextDirents()`

```cpp
int32 BQuery::GetNextDirents(struct dirent * buffer, size_t length, int32 count = INT_MAX)
```

Fill out up to *count* entries into the array of dirent structs pointed to by *buffer*. 


Reads as many but no more than *count* entries, as many entries as remain, or as many entries as will fit into the array at *buffer* with the given *length* (in bytes), whichever is smallest.


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | A pointer to a buffer filled out with dirent structures of the entries. |
| `length` | The length of *buffer*. |
| `count` | The maximum number of entries to be read. |





**Returns:** The number of dirent structures stored in the buffer, 0 when there are no more entries to be read, or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | The predicate included unindexed attributes. |
| B_FILE_ERROR | [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b) was not previously called on the object. |





**Since:** BeOS R3


Implements [BEntryList](classBEntryList.md#a2f8498249c876866d5f53a8b89044871).

---

### `GetNextEntry()`

```cpp
status_t BQuery::GetNextEntry(BEntry * entry, bool traverse = false)
```

Fills out *entry* with the next entry traversing symlinks if *traverse* is `true`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | A pointer to a [BEntry](classBEntry.md) object initialized with the entry. |
| `traverse` | Whether or not to follow symbolic links. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ENTRY_NOT_FOUND | At end of list. |
| B_BAD_VALUE | The predicate included unindexed attributes. |
| B_NOT_ALLOWED | [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b) was not previously called on the object. |





**Since:** BeOS R3


Implements [BEntryList](classBEntryList.md#a52e6c79344a6e511e7890f008e7281d1).

---

### `GetNextRef()`

```cpp
status_t BQuery::GetNextRef(entry_ref * ref)
```

Fills out *ref* with the next entry as an [entry_ref](structentry__ref.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | A pointer to an [entry_ref](structentry__ref.md) object filled out with the entry's data. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ENTRY_NOT_FOUND | At end of list. |
| B_BAD_VALUE | The predicate included unindexed attributes. |
| B_NOT_ALLOWED | [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b) was not previously called on the object. |





**Since:** BeOS R3


Implements [BEntryList](classBEntryList.md#a908ff7149239ab66683b12b27be917ee).

---

### `GetPredicate()`

```cpp
status_t BQuery::GetPredicate(BString * predicate)
```

Fills out the passed-in [BString](../support_kit/classBString.md) object with the predicate string assigned to the [BQuery](classBQuery.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `predicate` | A pointer to a [BString](../support_kit/classBString.md) object that gets filled out with the predicate string. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The predicate of the [BQuery](classBQuery.md) object wasn't set. |
| B_BAD_VALUE | *predicate* was `NULL`. |





**Since:** Haiku R1

---

### `GetPredicate()`

```cpp
status_t BQuery::GetPredicate(char * buffer, size_t length)
```

Fills out *buffer* with the predicate string assigned to the [BQuery](classBQuery.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | A pointer to a buffer which the predicate is written to. |
| `length` | the size of *buffer*. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The predicate of the [BQuery](classBQuery.md) object wasn't set. |
| B_BAD_VALUE | *buffer* was `NULL` or too short. |





**Since:** BeOS R3

---

### `IsLive()`

```cpp
bool BQuery::IsLive()const
```

Gets whether the query associated with this object is live. 



**Returns:** `true`, if the query is live, `false` otherwise.



**See also:** [SetTarget()](classBQuery.md#aca4694dedfd74796a38992ca256bc260)



**Since:** BeOS R3

---

### `PredicateLength()`

```cpp
size_t BQuery::PredicateLength()
```

Gets the length of the predicate string. 


This method returns the length of the string representation of the predicate (including the terminating `NUL`) regardless of whether the predicate has been constructed using the predicate stack or set via [SetPredicate()](classBQuery.md#a8dc3c9a0aa6fb7c991a88a5731fc6cae).



**Returns:** The length of the predicate string or 0 if an error occurred.



**See also:** [SetPredicate()](classBQuery.md#a8dc3c9a0aa6fb7c991a88a5731fc6cae)



**Since:** BeOS R3

---

### `PushAttr()`

```cpp
status_t BQuery::PushAttr(const char * attrName)
```

Pushes an attribute name onto the predicate stack. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `attrName` | The name of the attribute to push on the stack. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_MEMORY | Not enough memory. |
| B_NOT_ALLOWED | PushAttribute() was called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). |





**Since:** BeOS R3

---

### `PushDate()`

```cpp
status_t BQuery::PushDate(const char * date)
```

Pushes a date string onto the predicate stack. 


The supplied date can be any string understood by [parsedate()](parsedate_8h.md#ac9c3a59c9a7eb77650ef5ae5838cdd0b).


Parameters

| Parameter | Description |
| :--- | :--- |
| `date` | The date string to push onto the stack. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_MEMORY | Not enough memory. |
| B_NOT_ALLOWED | [PushDate()](classBQuery.md#a0c01d4a0c19b3af80d1c861ca8ec3e6c) was called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). |





**See also:** [parsedate()](parsedate_8h.md#ac9c3a59c9a7eb77650ef5ae5838cdd0b)



**Since:** Haiku R1

---

### `PushDouble()`

```cpp
status_t BQuery::PushDouble(double value)
```

Pushes a `double` onto the predicate stack. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The `double` to push onto the stack. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_MEMORY | Not enough memory. |
| B_NOT_ALLOWED | [PushDouble()](classBQuery.md#a7e654307d914dd003f7dc5dfe38af22f) was called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). |





**Since:** BeOS R3

---

### `PushFloat()`

```cpp
status_t BQuery::PushFloat(float value)
```

Pushes a `float` onto the predicate stack. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The `float` to push onto the stack. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_MEMORY | Not enough memory. |
| B_NOT_ALLOWED | [PushFloat()](classBQuery.md#a67e418693af55811941975b4da275b1d) was called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). |





**Since:** BeOS R3

---

### `PushInt32()`

```cpp
status_t BQuery::PushInt32(int32 value)
```

Pushes an `int32` onto the predicate stack. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The `int32` to push onto the stack. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_MEMORY | Not enough memory. |
| B_NOT_ALLOWED | [PushInt32()](classBQuery.md#a635dcf559feb1a07bb5910fab3a84b13) was called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). |





**Since:** BeOS R3

---

### `PushInt64()`

```cpp
status_t BQuery::PushInt64(int64 value)
```

Pushes an int64 onto the predicate stack. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The `int64` to push onto the stack. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_MEMORY | Not enough memory. |
| B_NOT_ALLOWED | [PushInt64()](classBQuery.md#a581f2eec46eb664088d76d027b510612) was called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). |





**Since:** BeOS R3

---

### `PushOp()`

```cpp
status_t BQuery::PushOp(query_op op)
```

Pushes an operator onto the predicate stack. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `op` | The operator code to push onto the stack. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_MEMORY | Not enough memory. |
| B_NOT_ALLOWED | [PushOp()](classBQuery.md#a17f934eed4967e0df7a67a41336f88da) was called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). |





**Since:** BeOS R3

---

### `PushString()`

```cpp
status_t BQuery::PushString(const char * value, bool caseInsensitive = false)
```

Pushes a string onto the predicate stack. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The string to push onto the stack. |
| `caseInsensitive` | Whether or not the case of *value* should be ignored in the resulting query. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_MEMORY | Not enough memory. |
| B_NOT_ALLOWED | [PushString()](classBQuery.md#aa5c9d0d2558cda8b127d705f9abfde54) was called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). |





**Since:** BeOS R3

---

### `PushUInt32()`

```cpp
status_t BQuery::PushUInt32(uint32 value)
```

Pushes a `uint32` onto the predicate stack. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The `uint32` to push onto the stack. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_MEMORY | Not enough memory. |
| B_NOT_ALLOWED | [PushUInt32()](classBQuery.md#a1cb827689d0485df5151661474f5c450) was called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). |





**Since:** BeOS R3

---

### `PushUInt64()`

```cpp
status_t BQuery::PushUInt64(uint64 value)
```

Pushes a `uint64` onto the predicate stack. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The `uint64` to push onto the stack. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_MEMORY | Not enough memory. |
| B_NOT_ALLOWED | [PushUInt64()](classBQuery.md#a21c56cfb7bbf927d702dab55ae333481) was called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). |





**Since:** BeOS R3

---

### `Rewind()`

```cpp
status_t BQuery::Rewind()
```

Rewinds the entry list back to the first entry. 



> [!NOTE]
> BeOS R5 does not implement this method for [BQuery](classBQuery.md).



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_FILE_ERROR | [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b) was not previously called on the object. |





**Since:** BeOS R3


Implements [BEntryList](classBEntryList.md#a6cbcd041425e5a1225a762c72a4eb8af).

---

### `SetFlags()`

```cpp
status_t BQuery::SetFlags(uint32 flags)
```

Sets the flags the query will be opened with. 


The possible flags to set are defined in `fs_query.h`.


This methods fails if called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). To reuse the [BQuery](classBQuery.md) object it must first be reset via [Clear()](classBQuery.md#af6c12ffd1d1c74c451ae1a03ee33c7d0).



> [!NOTE]
> The `B_LIVE_QUERY` flag will be ignored; [BQuery](classBQuery.md) always sets it automatically if necessary.


Parameters

| Parameter | Description |
| :--- | :--- |
| `flags` | The flags to set. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NOT_ALLOWED | [SetFlags()](classBQuery.md#ae497989322ff5f7ceffbbcf1036813cc) was called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). |





**Since:** Haiku R1

---

### `SetPredicate()`

```cpp
status_t BQuery::SetPredicate(const char * expression)
```

Assigns the passed-in predicate *expression*. 


A predicate can be set either using this method or by constructing one on the predicate stack, however, the two methods can not be mixed. The predicate stack takes precedence over this method.


The method fails if called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). To reuse the [BQuery](classBQuery.md) object it must first be reset using the [Clear()](classBQuery.md#af6c12ffd1d1c74c451ae1a03ee33c7d0) method.


Parameters

| Parameter | Description |
| :--- | :--- |
| `expression` | The predicate *expression* to set. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_MEMORY | Not enough memory. |
| B_NOT_ALLOWED | [SetPredicate()](classBQuery.md#a8dc3c9a0aa6fb7c991a88a5731fc6cae) was called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). |





**Since:** BeOS R3

---

### `SetTarget()`

```cpp
status_t BQuery::SetTarget(BMessenger messenger)
```

Assigns the target *messenger* and makes the query live. 


The query update messages are sent to the specified target. They might roll in immediately after calling [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b).


This methods fails if called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). To reuse the [BQuery](classBQuery.md) object it must first be reset via [Clear()](classBQuery.md#af6c12ffd1d1c74c451ae1a03ee33c7d0).


Parameters

| Parameter | Description |
| :--- | :--- |
| `messenger` | The target *messenger* to set. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_MEMORY | Not enough memory. |
| B_NOT_ALLOWED | [SetTarget()](classBQuery.md#aca4694dedfd74796a38992ca256bc260) was called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). |





**Since:** BeOS R3

---

### `SetVolume()`

```cpp
status_t BQuery::SetVolume(const BVolume * volume)
```

Assigns *volume* to the [BQuery](classBQuery.md) object. 


A query may only be assigned to one volume.


The method fails if called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). To reuse the [BQuery](classBQuery.md) object it must first be reset using the [Clear()](classBQuery.md#af6c12ffd1d1c74c451ae1a03ee33c7d0) method.


Parameters

| Parameter | Description |
| :--- | :--- |
| `volume` | The *volume* to set. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NOT_ALLOWED | [SetVolume()](classBQuery.md#aa49ccd947942b5eca16c52a56a9a13db) was called after [Fetch()](classBQuery.md#aa2a6473e999bf602cb5684e1477ecc3b). |





**Since:** BeOS R3

---

### `TargetDevice()`

```cpp
dev_t BQuery::TargetDevice()const
```

Gets the device ID identifying the volume of the [BQuery](classBQuery.md) object. 



**Returns:** The device ID of the volume or `B_NO_INIT` if the volume wasn't set.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBQuery.html).
