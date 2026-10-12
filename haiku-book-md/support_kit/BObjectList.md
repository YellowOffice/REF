---
name: BObjectList< T, Owning > Template Reference
type: class
kit: support_kit
brief: "BObjectList is a wrapper around BList that adds type safety, optional object ownership, search, and insert operations"
source: haiku-book
---

# BObjectList< T, Owning > Class Template Reference
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

template<class T, bool Owning>

class BObjectList< T, Owning >[BObjectList](classBObjectList.md) is a wrapper around [BList](classBList.md) that adds type safety, optional object ownership, search, and insert operations. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BObjectList](#ab187f06381c5aad02866025658b87f15) (const BObjectList &list) — Creates a new BObjectList as a copy of another list.
* [BObjectList](#a8af6e5f632040dca6ee517bbb3c60210) (int32 itemsPerBlock=20) — Creates a new BObjectList.
* `virtual` [~BObjectList](#a2eaf169fa07c0a5fb75c324fb7bca66c) () — Deletes the list.
* `BObjectList &` [operator=](#afa70527e3d1a319bc9e61b67752df9f1) (const BObjectList &list) — Creates a new BObjectList as a copy of another list by overloading the = operator.
* `bool` [AddItem](#acf86b51a49cbb8095ad99228555a5e87) (T *) — Append the item to the end of the list.
* `bool` [AddItem](#ac357255e0552b1004e05c80eb863fdc2) (T *, int32) — Add item at the specified index.
* `bool` [AddList](#a66930b1bb06b6f855ddbc0b9a1b6adbf) (BObjectList *) — Append a list of items to this list.
* `bool` [AddList](#a6a18e822d4d5b6cba7397904277bdca9) (BObjectList *, int32) — Add a list of items to this list at the specified index.
* `bool` [RemoveItem](#aabb34570449e80cc508e661e5ac881d9) (T *, bool deleteIfOwning=true) — Remove item from the list.
* `T *` [RemoveItemAt](#a4d18abf9d53d064d96c59f7449a19d0e) (int32) — Remove the item at index from the list.
* `void` [MakeEmpty](#ab6446b2ac0e41f889690950aecacc7e3) (bool deleteIfOwning=true) — Clear all the items from the list.
* `T *` [ItemAt](#a252d9a2b2409b1721fcdfaf19c498191) (int32) const — Return a pointer to the item at the given index.
* `bool` [ReplaceItem](#a41f899fe44cb6c95293a308f67308f3d) (int32 index, T *) — Replace an item with another one.
* `T *` [SwapWithItem](#ad3291d16e4cc1afc9d251424d01f82d3) (int32 index, T *newItem) — Swap the item with the item at index.
* `bool` [MoveItem](#a795478db539f0b246cc0a7f997f24f4c) (int32 from, int32 to) — Move the item at from to the position of to.
* `void` [SortItems](#a89c5547512be874db5abf2423889d915) (CompareFunction) — Sort the items with the use of a supplied comparison function.
* `void` [SortItems](#ab2a42ba860f9977651f8656ce790c53a) (CompareFunctionWithState, void *state) — Sort the items with the use of a supplied comparison function and addtional state.
* `void` [HSortItems](#ad01d48e10b3c96fbf54ec57c3b100cd5) (CompareFunction) — Sort the items with the use of a supplied comparison function.
* `T *` [FirstItem](#a1ffba0029aee494767df6de974435173) () const — Return a pointer to the first item in the list.
* `T *` [LastItem](#abfdbfba1d233d9d28c7198e97f3d4de5) () const — Return a pointer to the last item in the list.
* `int32` [IndexOf](#a65d68fcae07503414a061b49a85f7f2a) (const T *) const — Return the index of item.
* `bool` [HasItem](#aac8e8470d40c8decdbf0d6c53581aafd) (const T *) const — Return whether or not item is in the list.
* `bool` [IsEmpty](#ae5bff72f39b6869a88e69aaf56221bf2) () const — Return whether or not there are items in the list.
* `int32` [CountItems](#ad081aa49d6dd5b2a3eb40de8b5ed738e) () const — Returns the number of items in the list.
* `T *` [EachElement](#a62640f3534d328214859ca91b0a67e34) (EachFunction, void *) — Perform an action on each item in the list.
* `const T *` [EachElement](#a6faa20d6b2568f944d01f7354769dcef) (ConstEachFunction, void *) const — Perform an action on each item in the list.
* `const T *` [FindIf](#a094941dc725da1fd5e0dacbaf941b656) (const UnaryPredicate< T > &) const — Find items that match predicate.
* `T *` [FindIf](#ab8e2bd0e5ed493bbb20b06c5a039448b) (const UnaryPredicate< T > &) — Find items that match predicate.
* `T *` [BinarySearch](#a5c72feac688386f1ff1169640af25d5c) (const T &, CompareFunction) const — Search for key in the list of items using the supplied comparison function via a binary search algorithm.
* `T *` [BinarySearch](#a4cb06c477e0f87d79eae4f6e97580355) (const T &, CompareFunctionWithState, void *state) const — Search for key in the list of items using the supplied comparison function via a binary search algorithm.

## Detailed Member Documentation

### `BObjectList()`

```cpp
BObjectList< T, Owning >::BObjectList(int32 itemsPerBlock = 20)
```

Creates a new [BObjectList](classBObjectList.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `itemsPerBlock` | The number of items per block to allocate. |




Template Parameters

| Col 1 | Col 2 |
| :--- | :--- |
| owning | Whether or not the [BObjectList](classBObjectList.md) deletes its items when it is emptied or deleted. |





**Since:** Haiku R1

---

### `BObjectList()`

```cpp
template< class T, bool owning > BObjectList< T, Owning >::BObjectList(const BObjectList< T, Owning > & list)
```

Creates a new [BObjectList](classBObjectList.md) as a copy of another *list*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `list` | The *list* to copy from. |





**Since:** Haiku R1

---

### `~BObjectList()`

```cpp
BObjectList< T, Owning >::~BObjectList
```

Deletes the list. 


If the list owns its items they are deleted too.



**Since:** Haiku R1

---

### `AddItem()`

```cpp
bool BObjectList< T, O >::AddItem(T * item)
```

Append the *item* to the end of the list. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The *item* to append. |





**Returns:** Whether or not the *item* was appended.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The *item* was appended. |
| false | *item* was not appended, since resizing the [BObjectList](classBObjectList.md) failed. |





**Since:** Haiku R1


References [BList::AddItem()](classBList.md#ab827c4118ba2a46eae24f5a41eb9bdb6).

---

### `AddItem()`

```cpp
bool BObjectList< T, O >::AddItem(T * item, int32 index)
```

Add *item* at the specified *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The *item* to add. |
| `index` | The place in the list to add the *item*. |





**Returns:** Whether or not the item was added.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The item was added. |
| false | Item was not added. Either the index is negative or invalid, or resizing the [BObjectList](classBObjectList.md) failed. |





**Since:** Haiku R1


References [BList::AddItem()](classBList.md#ab827c4118ba2a46eae24f5a41eb9bdb6).

---

### `AddList()`

```cpp
template< class T, bool owning > bool BObjectList< T, Owning >::AddList(BObjectList< T, Owning > * list)
```

Append a *list* of items to this list. 


The original list is not altered.


Parameters

| Parameter | Description |
| :--- | :--- |
| `list` | The *list* to be added. |





**Returns:** Whether or not the *list* was added.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The *list* was added. |
| false | Failed to append the list, resizing failed. |





**Since:** Haiku R1

---

### `AddList()`

```cpp
template< class T, bool owning > bool BObjectList< T, Owning >::AddList(BObjectList< T, Owning > * list, int32 index)
```

Add a *list* of items to this list at the specified *index*. 


The original list is not altered.


Parameters

| Parameter | Description |
| :--- | :--- |
| `list` | The *list* to be added. |
| `index` | The position in the current *list* where the new item(s) are added. |





**Returns:** Whether or not the *list* was added.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The *list* was added. |
| false | Failed to insert the *list* resizing failed. |





**Since:** Haiku R1

---

### `BinarySearch()`

```cpp
T * BObjectList< T, O >::BinarySearch(const T & key, CompareFunction func)const
```

Search for *key* in the list of items using the supplied comparison function via a binary search algorithm. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `key` | The *key* to search for. |
| `func` | The comparison function to use. |





**Returns:** A pointer to T.



**Since:** Haiku R1

---

### `BinarySearch()`

```cpp
T * BObjectList< T, O >::BinarySearch(const T & key, CompareFunctionWithState func, void * state)const
```

Search for *key* in the list of items using the supplied comparison function via a binary search algorithm. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `key` | The *key* to search for. |
| `func` | The comparison function to use. |
| `state` | Additional information used to search for the item. |





**Returns:** A pointer to T.



**Since:** Haiku R1

---

### `CountItems()`

```cpp
int32 BObjectList< T, O >::CountItems
```

Returns the number of items in the list. 



**Returns:** The number of items in the list as an int32.



**Since:** Haiku R1


References [BList::CountItems()](classBList.md#a9934f3617c27ae2276607efd0de858f0).


Referenced by [BObjectList< T, Owning >::operator=()](classBObjectList.md#afa70527e3d1a319bc9e61b67752df9f1).

---

### `EachElement()`

```cpp
const T * BObjectList< T, O >::EachElement(ConstEachFunction func, void * params)const
```

Perform an action on each item in the list. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `func` | A function that takes a `void*` argument and returns a boolean. |
| `params` | parameters for *func*. |





**Returns:** A pointer to the item.



**Since:** Haiku R1

---

### `EachElement()`

```cpp
T * BObjectList< T, O >::EachElement(EachFunction func, void * params)
```

Perform an action on each item in the list. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `func` | A function that takes a `void*` argument and returns a boolean. |
| `params` | parameters for *func*. |





**Returns:** A pointer to the item.



**Since:** Haiku R1

---

### `FindIf()`

```cpp
T * BObjectList< T, O >::FindIf(const UnaryPredicate< T > & predicate)
```

Find items that match *predicate*. 



**Returns:** A pointer to T.



**Since:** Haiku R1

---

### `FindIf()`

```cpp
const T * BObjectList< T, O >::FindIf(const UnaryPredicate< T > & predicate)const
```

Find items that match *predicate*. 



**Returns:** A const pointer to T.



**Since:** Haiku R1

---

### `FirstItem()`

```cpp
T * BObjectList< T, O >::FirstItem
```

Return a pointer to the first item in the list. 



**Returns:** A pointer to the first item or `NULL` if the list is empty.



**See also:** [BObjectList<T>::LastItem() const](classBObjectList.md#abfdbfba1d233d9d28c7198e97f3d4de5)



**Since:** Haiku R1


References [BList::FirstItem()](classBList.md#a0f942e4b3c56a1a5b4b6685eda799d65).

---

### `HasItem()`

```cpp
bool BObjectList< T, O >::HasItem(const T * item)const
```

Return whether or not *item* is in the list. 



**Returns:** `true` if the *item* was in the list, `false` otherwise.



**Since:** Haiku R1


References [BList::HasItem()](classBList.md#a52eba743d386b339fcc092781a25ba81).

---

### `HSortItems()`

```cpp
void BObjectList< T, O >::HSortItems(CompareFunction function)
```

Sort the items with the use of a supplied comparison *function*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `function` | The *function* used to sort the items. |





**Since:** Haiku R1

---

### `IndexOf()`

```cpp
int32 BObjectList< T, O >::IndexOf(const T * item)const
```

Return the index of *item*. 



**Returns:** The index of the item, or -1 when the item is not in the list.



**Since:** Haiku R1


References [BList::IndexOf()](classBList.md#aa66edf99e4c395006964e665805a9f84).

---

### `IsEmpty()`

```cpp
bool BObjectList< T, O >::IsEmpty
```

Return whether or not there are items in the list. 



**Returns:** `true` if the list was empty, `false` otherwise.



**Since:** Haiku R1


References [BList::IsEmpty()](classBList.md#a8fe0fa7c73e17ce27e543f4de22751ad).

---

### `ItemAt()`

```cpp
T * BObjectList< T, O >::ItemAt(int32 index)const
```

Return a pointer to the item at the given *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The item to retrieve. |





**Returns:** A pointer to the item in that position, or `NULL` if the *index* is out of bounds.



**Since:** Haiku R1


References [BList::ItemAt()](classBList.md#a8dd0ea855550a6923294ceff045a82b0).


Referenced by [BObjectList< T, Owning >::operator=()](classBObjectList.md#afa70527e3d1a319bc9e61b67752df9f1).

---

### `LastItem()`

```cpp
T * BObjectList< T, O >::LastItem
```

Return a pointer to the last item in the list. 



**Returns:** A pointer to the last item or `NULL` if the list is empty.



**See also:** [BObjectList<T>::FirstItem() const](classBObjectList.md#a1ffba0029aee494767df6de974435173)



**Since:** Haiku R1


References [BList::LastItem()](classBList.md#a38e516f6bf9f058b970793f877c4d41f).

---

### `MakeEmpty()`

```cpp
void BObjectList< T, Owning >::MakeEmpty(bool deleteIfOwning = true)
```

Clear all the items from the list. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `deleteIfOwning` | Also deletes items if owned. |





**Since:** Haiku R1


References [BList::MakeEmpty()](classBList.md#ad7529a3817b21cd33f34802f1efa26bd).

---

### `MoveItem()`

```cpp
bool BObjectList< T, O >::MoveItem(int32 from, int32 to)
```

Move the item at *from* to the position of *to*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `from` | The index to move the item *from*. |
| `to` | The index to move the item *to*. |





**Returns:** Whether or not the items were moved.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The items were moved. |
| false | The *from* or *to* index was invalid. |





**See also:** [BList::MoveItem()](classBList.md#a9a90328dd4eb4f86160b2acc1ea90cee)



**Since:** Haiku R1

---

### `operator=()`

```cpp
BObjectList< T, Owning > & BObjectList< T, Owning >::operator=(const BObjectList< T, Owning > & list)
```

Creates a new [BObjectList](classBObjectList.md) as a copy of another *list* by overloading the = operator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `list` | The *list* to copy from. |





**Since:** Haiku R1


References [BObjectList< T, Owning >::CountItems()](classBObjectList.md#ad081aa49d6dd5b2a3eb40de8b5ed738e), and [BObjectList< T, Owning >::ItemAt()](classBObjectList.md#a252d9a2b2409b1721fcdfaf19c498191).

---

### `RemoveItem()`

```cpp
bool BObjectList< T, Owning >::RemoveItem(T * item, bool deleteIfOwning = true)
```

Remove *item* from the list. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The *item* to be removed. |
| `deleteIfOwning` | Also delete the *item* if owned. |





**Returns:** Whether or not the *item* was removed.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The *item* was found and removed. |
| false | The *item* was not in this list and thus not removed. |





**Since:** Haiku R1


References [BList::RemoveItem()](classBList.md#abea827f5275c57b89fe463e1ad191088).

---

### `RemoveItemAt()`

```cpp
T * BObjectList< T, O >::RemoveItemAt(int32 index)
```

Remove the item at *index* from the list. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The *index* of the item to be removed. |





**Returns:** The pointer to the item that was removed, or `NULL` if the *index* was invalid.



**Since:** Haiku R1


References [BList::RemoveItem()](classBList.md#abea827f5275c57b89fe463e1ad191088).

---

### `ReplaceItem()`

```cpp
bool BObjectList< T, Owning >::ReplaceItem(int32 index, T * item)
```

Replace an item with another one. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The offset in the list where to put the *item*. |
| `item` | The new *item* to put in the list. |





**Returns:** Whether or not the item was replaced.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The item was replaced. |
| false | The *index* was invalid. |





**Since:** Haiku R1

---

### `SortItems()`

```cpp
void BObjectList< T, O >::SortItems(CompareFunction function)
```

Sort the items with the use of a supplied comparison *function*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `function` | The *function* used to sort the items. |





**Since:** Haiku R1


References [BList::SortItems()](classBList.md#abe55aa005c16d47128365775b7aee021).

---

### `SortItems()`

```cpp
void BObjectList< T, O >::SortItems(CompareFunctionWithState function, void * state)
```

Sort the items with the use of a supplied comparison *function* and addtional *state*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `function` | The *function* used to sort the items. |
| `state` | Additional information used to sort the items. |





**Since:** Haiku R1


References [BList::SortItems()](classBList.md#abe55aa005c16d47128365775b7aee021).

---

### `SwapWithItem()`

```cpp
T * BObjectList< T, O >::SwapWithItem(int32 index, T * item)
```

Swap the *item* with the item at *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The offset in the list where to put the *item*. |
| `item` | The new *item* to put in the list. |





**Returns:** A pointer to the item in that position, or `NULL` if the *index* is out of bounds.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBObjectList.html).
