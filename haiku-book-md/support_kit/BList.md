---
name: BList
type: class
kit: support_kit
brief: "An ordered container that is designed to hold generic void* objects"
source: haiku-book
---

# BList Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

An ordered container that is designed to hold generic `void*` objects. 


This class is designed to be used for a variety of tasks. Unlike similar implementations in other libraries, this class is not based on templates and as such is inherently not typed. So it will be the job of the programmer to make sure proper data is entered since the compiler cannot check this by itself.


[BList](classBList.md) contains a list of items that will grow and shrink depending on how many items are in it. So you will not have to do any of the memory management nor any ordering. These properties makes it useful in a whole range of situations such as the interface kit within the [BListView](../interface_kit/classBListView.md) class.


A note on the ownership of the objects might come in handy. [BList](classBList.md) never assumes ownership of the objects. As such, removing items from the list will only remove the entries from the list; it will not delete the items themselves. Similarly, you should also make sure that before you might delete an object that is in a list, you will have to remove it from the list first.



> [!WARNING]
> This class is not thread-safe.


The class implements methods to add, remove, reorder, retrieve, and query items as well as some advanced methods which let you perform a task on all the items in the list.



**See also:** [BObjectList](classBObjectList.md) for a templated version of [BList](classBList.md) that adds type safety, optional object ownership, search, and insert operations.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BList](#a38ee57f24e4f987679e169ce09beeed4) (const BList &other) — Copy constructor. Copy a complete list into this one.
* [BList](#a00052b2d527609ed9879dbbb268c4696) (int32 blockSize=20) — Create a new list with a number of empty slots.
* `virtual` [~BList](#af08f58e63380be9bb720a2918afe3113) () — Destroy the list.
* `BList &` [operator=](#af7da7ecbaaa1963074ca17302adb6099) (const BList &other) — Copy another list into this object.
* `bool` [operator==](#aaec14d70fda5ee21b0bfb26702b6640e) (const BList &other) const — Returns whether or not the BList and other are equal.
* `bool` [operator!=](#abbaf2188cd4f4f1588399b4dd7be5c7b) (const BList &other) const — Returns whether or not the BList and other are NOT equal.
* `bool` [AddItem](#ab827c4118ba2a46eae24f5a41eb9bdb6) (void *item, int32 index) — Add item at the specified index.
* `bool` [AddItem](#a466d0c711d3736a185ca243749120ad3) (void *item) — Append the item to the end of the list.
* `bool` [AddList](#ad6d19427b9f9f6accf0ab5ab5df7f219) (const BList *list, int32 index) — Add a list of items to this list at the specified index.
* `bool` [AddList](#a285e109e612c8e2c18fd09436e9afd6d) (const BList *list) — Append a list of items to this list.
* `bool` [RemoveItem](#abea827f5275c57b89fe463e1ad191088) (void *item) — Remove item from the list.
* `void *` [RemoveItem](#a4ce0e34daae40f74ff024773a5f799b2) (int32 index) — Remove the item at index from the list.
* `bool` [RemoveItems](#a401542cd9d61fe480bcfd61e7caf9f3d) (int32 index, int32 count) — Remove a number of items starting at a certain position.
* `bool` [ReplaceItem](#a043d798461212144c1388f3ee6059cda) (int32 index, void *item) — Replace an item with another one.
* `void` [MakeEmpty](#ad7529a3817b21cd33f34802f1efa26bd) () — Clear all the items from the list.
* `void` [SortItems](#abe55aa005c16d47128365775b7aee021) (int(*compareFunc)(const void *, const void *)) — Sort the items with the use of a supplied comparison function.
* `bool` [SwapItems](#a1e0f5e82f57fe98ed9b76228e2df43d5) (int32 indexA, int32 indexB) — Swap the items at indexA and indexB.
* `bool` [MoveItem](#a9a90328dd4eb4f86160b2acc1ea90cee) (int32 from, int32 to) — Move the item at fromIndex to the position of toIndex.
* `void *` [ItemAt](#a8dd0ea855550a6923294ceff045a82b0) (int32 index) const — Return a pointer to the item at the given index.
* `void *` [FirstItem](#a0f942e4b3c56a1a5b4b6685eda799d65) () const — Return a pointer to the first item in the list.
* `void *` [ItemAtFast](#a7d6db1ced8d620bdfc6cfaf6d9383162) (int32 index) const — Return a pointer to the item at index.
* `void *` [LastItem](#a38e516f6bf9f058b970793f877c4d41f) () const — Return a pointer to the last item in the list.
* `void *` [Items](#a3af18a435a926a1200ac44671a01f2a8) () const — Return the internal list of objects.
* `bool` [HasItem](#a52eba743d386b339fcc092781a25ba81) (void *item) const — Return whether or not item is in the list.
* `bool` [HasItem](#a9046dd4910aa56e436eb97146984c050) (const void *item) const — Return whether or not item is in the list.
* `int32` [IndexOf](#aa66edf99e4c395006964e665805a9f84) (void *item) const — Return the index of item.
* `int32` [IndexOf](#a17f9954ac3b3b8af9a2054f9caa0a63b) (const void *item) const — Return the index of item.
* `int32` [CountItems](#a9934f3617c27ae2276607efd0de858f0) () const — Returns the number of items in the list.
* `bool` [IsEmpty](#a8fe0fa7c73e17ce27e543f4de22751ad) () const — Return whether or not there are items in the list.
* `void` [DoForEach](#af6c57e27f1c15a8779f1c7e4002d593c) (bool(*func)(void *item)) — Perform an action on every item in the list.
* `void` [DoForEach](#aa00ded2072c9c604bcbbabb8f1a70a6a) (bool(*func)(void *item, void *arg2), void *arg2) — Perform an action on every item in the list with an argument.

## Detailed Member Documentation

### `BList()`

```cpp
BList::BList(int32 count = 20)
```

Create a new list with a number of empty slots. 


The memory management of this class allocates new memory per block. The `count` parameter can be tweaked to determine the size of these blocks. In general, if you know your list is only going to contain a certain number of items at most, you can pass that value. If you expect your list to have very few items, it is safe to choose a low number. This is to prevent the list from taking up unneeded memory. If you expect the list to contain a large number of items, choose a higher value. Every time the memory is full, all the items have to be copied into a new piece of allocated memory, which is an expensive operation.


If you are unsure, you do not have to worry too much. Just make sure you do not use a lot of lists, and as long as the list is not used in one of the performance critical parts of the code, you are safe to go with the default values.


Parameters

| Parameter | Description |
| :--- | :--- |
| `count` | The size of the blocks allocated in memory. |





**Since:** BeOS R3

---

### `BList()`

```cpp
BList::BList(const BList & other)
```

Copy constructor. Copy a complete list into this one. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The list to copy from. |





**Since:** BeOS R3

---

### `~BList()`

```cpp
BList::~BList()
```

Destroy the list. 


Please note that as [BList](classBList.md) does not assume ownership of the objects, only the list will be freed, not the objects that are held in it.



**Since:** BeOS R3

---

### `AddItem()`

```cpp
bool BList::AddItem(void * item)
```

Append the *item* to the end of the list. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The item to append. |





**Returns:** Whether or not the *item* was appended.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The *item* was appended. |
| false | *item* was not appended, since resizing the [BList](classBList.md) failed. |





**See also:** [AddItem(void*, int32)](classBList.md#ab827c4118ba2a46eae24f5a41eb9bdb6)



**Since:** BeOS R3

---

### `AddItem()`

```cpp
bool BList::AddItem(void * item, int32 index)
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
| false | Item was not added. Either the index is negative or invalid, or resizing the list failed. |





**See also:** [AddItem(void*)](classBList.md#a466d0c711d3736a185ca243749120ad3)



**Since:** BeOS R3


Referenced by [BObjectList< T, Owning >::AddItem()](classBObjectList.md#acf86b51a49cbb8095ad99228555a5e87).

---

### `AddList()`

```cpp
bool BList::AddList(const BList * list)
```

Append a *list* of items to this list. 


Note that the *list* parameter is a `const`, so the original list will not be altered.


Parameters

| Parameter | Description |
| :--- | :--- |
| `list` | The *list* to be added. |





**Returns:** Whether or not the *list* was added.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The *list* was appended. |
| false | Failed to append the list, resizing failed. |





**See also:** [AddList(const BList*, int32)](classBList.md#ad6d19427b9f9f6accf0ab5ab5df7f219)



**Since:** BeOS R3

---

### `AddList()`

```cpp
bool BList::AddList(const BList * list, int32 index)
```

Add a *list* of items to this list at the specified *index*. 


Note that the *list* parameter is `const`, so the original list will not be altered.


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





**See also:** [AddList(const BList*)](classBList.md#a285e109e612c8e2c18fd09436e9afd6d)



**Since:** BeOS R3

---

### `CountItems()`

```cpp
int32 BList::CountItems()const
```

Returns the number of items in the list. 



**Returns:** The number of items in the list as an int32.



**Since:** BeOS R3


Referenced by [BObjectList< T, Owning >::CountItems()](classBObjectList.md#ad081aa49d6dd5b2a3eb40de8b5ed738e).

---

### `DoForEach()`

```cpp
void BList::DoForEach(bool(*)(void *item)func)
```

Perform an action on every item in the list. 


Iterates over all items in the list, and calls the *func* function on each of them, until the function returns `true`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `func` | A pointer to a function that takes a `void*` list item, and returns a bool indicating if the iteration should stop. |





**See also:** [DoForEach](classBList.md#af6c57e27f1c15a8779f1c7e4002d593c)(bool (*func)(void*, void*), void*)



**Since:** BeOS R3

---

### `DoForEach()`

```cpp
void BList::DoForEach(bool(*)(void *item, void *arg2)func, void * arg2)
```

Perform an action on every item in the list with an argument. 


The iteration stops when the *func* function returns `true`. This can be used to implement a linear search of the list, for example:



```cpp
bool compareFunc(void* _item, void* arg2) {
    Item* item = (Item*)_item;
    Args* args = (Args*)arg2;
 if (item->Matches(args->pattern)) {
        args->result = item;
 return true;
    }
 return false;
}
 
Args args = {0};
list.DoForEach(compareFunc, &args);
if (args->result != NULL) {
 // Found it!
}
```

Parameters

| Parameter | Description |
| :--- | :--- |
| `func` | A function with the first `void*` argument being the item and the second `void*` being the argument that you supply. |
| `arg2` | An argument to supply to *func*. |





**See also:** [DoForEach](classBList.md#af6c57e27f1c15a8779f1c7e4002d593c)(bool (*func)(void*))



**Since:** BeOS R3

---

### `FirstItem()`

```cpp
void * BList::FirstItem()const
```

Return a pointer to the first item in the list. 



**Returns:** A pointer to the first item or `NULL` if the list is empty.



**See also:** [LastItem() const](classBList.md#a38e516f6bf9f058b970793f877c4d41f)



**Since:** BeOS R3


Referenced by [BObjectList< T, Owning >::FirstItem()](classBObjectList.md#a1ffba0029aee494767df6de974435173).

---

### `HasItem()`

```cpp
bool BList::HasItem(const void * item)const
```

Return whether or not *item* is in the list. 



**Returns:** `true` if the *item* was in the list, `false` otherwise.



**Since:** Haiku R1

---

### `HasItem()`

```cpp
bool BList::HasItem(void * item)const
```

Return whether or not *item* is in the list. 



**Returns:** `true` if the *item* was in the list, `false` otherwise.



**Since:** BeOS R3


Referenced by [BObjectList< T, Owning >::HasItem()](classBObjectList.md#aac8e8470d40c8decdbf0d6c53581aafd).

---

### `IndexOf()`

```cpp
int32 BList::IndexOf(const void * item)const
```

Return the index of *item*. 



**Returns:** The index of the item, or -1 when the item is not in the list.



**Since:** Haiku R1

---

### `IndexOf()`

```cpp
int32 BList::IndexOf(void * item)const
```

Return the index of *item*. 



**Returns:** The index of the item, or -1 when the item is not in the list.



**Since:** BeOS R3


Referenced by [BObjectList< T, Owning >::IndexOf()](classBObjectList.md#a65d68fcae07503414a061b49a85f7f2a).

---

### `IsEmpty()`

```cpp
bool BList::IsEmpty()const
```

Return whether or not there are items in the list. 



**Returns:** `true` if the list was empty, `false` otherwise.



**Since:** BeOS R3


Referenced by [BObjectList< T, Owning >::IsEmpty()](classBObjectList.md#ae5bff72f39b6869a88e69aaf56221bf2).

---

### `ItemAt()`

```cpp
void * BList::ItemAt(int32 index)const
```

Return a pointer to the item at the given *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The item to retrieve. |





**Returns:** A pointer to the item in that position, or `NULL` if the *index* is out of bounds.



**See also:** [ItemAtFast(int32 index) const](classBList.md#a7d6db1ced8d620bdfc6cfaf6d9383162)



**Since:** BeOS R3


Referenced by [BObjectList< T, Owning >::ItemAt()](classBObjectList.md#a252d9a2b2409b1721fcdfaf19c498191).

---

### `ItemAtFast()`

```cpp
void * BList::ItemAtFast(int32 index)const
```

Return a pointer to the item at *index*. 


This method does not perform any boundary checks when it retrieves an item. Use this method in a performance critical area of your program where you are sure you will not get an invalid item.



**Returns:** A pointer to the item.



**Since:** Haiku R1

---

### `Items()`

```cpp
void * BList::Items()const
```

Return the internal list of objects. 


This method will return a pointer to the internal pointer list. This means that you should be careful what you are doing, since you are working with the internals of the class directly.


It is not a good idea to make any changes to the list, since that will mess up the internal consistency.



> [!WARNING]
> If there is anything you want, for which you need the list of objects, please realize that that probably means that what you want to do is a bad idea to begin with and that you should avoid this method. The list of objects does not belong to you.



**Returns:** The internal list of pointers.



**See also:** [DoForEach()](classBList.md#af6c57e27f1c15a8779f1c7e4002d593c) for an alternate method.



**Since:** BeOS R3

---

### `LastItem()`

```cpp
void * BList::LastItem()const
```

Return a pointer to the last item in the list. 



**Returns:** A pointer to the last item or `NULL` if the list is empty.



**See also:** [FirstItem() const](classBList.md#a0f942e4b3c56a1a5b4b6685eda799d65)



**Since:** BeOS R3


Referenced by [BObjectList< T, Owning >::LastItem()](classBObjectList.md#abfdbfba1d233d9d28c7198e97f3d4de5).

---

### `MakeEmpty()`

```cpp
void BList::MakeEmpty()
```

Clear all the items from the list. 



> [!NOTE]
> This does not free the items.



**Since:** BeOS R3


Referenced by [BObjectList< T, Owning >::MakeEmpty()](classBObjectList.md#ab6446b2ac0e41f889690950aecacc7e3).

---

### `MoveItem()`

```cpp
bool BList::MoveItem(int32 fromIndex, int32 toIndex)
```

Move the item at *fromIndex* to the position of *toIndex*. 


This moves a list item from position A to position B, moving the appropriate block of list elements to make up for the move. For example, in the array: 

A B C D E F G H I J
Moving 1(B)->6(G) would result in this: 

A C D E F G B H I J
Parameters

| Parameter | Description |
| :--- | :--- |
| `fromIndex` | The original location. |
| `toIndex` | The new location. |





**Returns:** Whether or not the items were moved.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | Move succeeded. |
| false | Move failed due to the indexes being invalid. |





**Since:** Haiku R1

---

### `operator!=()`

```cpp
bool BList::operator!=(const BList & other)const
```

Returns whether or not the [BList](classBList.md) and *other* are NOT equal. 



**Returns:** `true` if the lists are NOT equal, `false` if they are equal.



**Since:** Haiku R1

---

### `operator=()`

```cpp
BList & BList::operator=(const BList & other)
```

Copy another list into this object. 



**Since:** BeOS R3

---

### `operator==()`

```cpp
bool BList::operator==(const BList & other)const
```

Returns whether or not the [BList](classBList.md) and *other* are equal. 


Equal means that they are the same object or their contents are the same.



**Returns:** `true` if the lists are equal, `false` if they are NOT equal.



**Since:** Haiku R1

---

### `RemoveItem()`

```cpp
void * BList::RemoveItem(int32 index)
```

Remove the item at *index* from the list. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The *index* of the item to be removed. |





**Returns:** The pointer to the item that was removed, or `NULL` if the *index* was invalid.



**See also:** [RemoveItem(void*)](classBList.md#abea827f5275c57b89fe463e1ad191088)



**Since:** BeOS R3

---

### `RemoveItem()`

```cpp
bool BList::RemoveItem(void * item)
```

Remove *item* from the list. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The *item* to be removed. |





**Returns:** Whether or not the *item* was removed.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The *item* was found and removed. |
| false | The *item* was not in this list and thus not removed. |





**See also:** [RemoveItem(int32)](classBList.md#a4ce0e34daae40f74ff024773a5f799b2)



**Since:** BeOS R3


Referenced by [BObjectList< T, Owning >::RemoveItem()](classBObjectList.md#aabb34570449e80cc508e661e5ac881d9), and [BObjectList< T, Owning >::RemoveItemAt()](classBObjectList.md#a4d18abf9d53d064d96c59f7449a19d0e).

---

### `RemoveItems()`

```cpp
bool BList::RemoveItems(int32 index, int32 count)
```

Remove a number of items starting at a certain position. 


If the count parameter is larger than the number of items in the list, all the items from the offset to the end will be removed.


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The offset in the list where removal should start. |
| `count` | The number of items to remove. |





**Returns:** Whether or not the items were removed.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | Removal succeeded. |
| false | Failed to remove the items because the index was invalid. |





**Since:** BeOS R3

---

### `ReplaceItem()`

```cpp
bool BList::ReplaceItem(int32 index, void * item)
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
void BList::SortItems(int(*)(const void *, const void *)compareFunc)
```

Sort the items with the use of a supplied comparison function. 


The function should take two `const` pointers as arguments and should return an integer.


For an example, see the [Compare(const BString *, const BString *)](group__support__globals.md#gaa845691f971dbf61ff57ba6d86aa2df1) function.



**Since:** BeOS R3


Referenced by [BObjectList< T, Owning >::SortItems()](classBObjectList.md#a89c5547512be874db5abf2423889d915).

---

### `SwapItems()`

```cpp
bool BList::SwapItems(int32 indexA, int32 indexB)
```

Swap the items at *indexA* and *indexB*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `indexA` | The first item. |
| `indexB` | The second item. |





**Returns:** Whether or not the items were swapped.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | Swap succeeded. |
| false | Swap failed because one of the indexes was invalid. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBList.html).
