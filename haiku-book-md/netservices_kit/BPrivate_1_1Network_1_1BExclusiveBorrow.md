---
name: BPrivate::Network::BExclusiveBorrow< T > Template Reference
type: class
kit: netservices_kit
brief: "Smart pointer that allows shared ownership of an object with exclusive access"
source: haiku-book
---

# BPrivate::Network::BExclusiveBorrow< T > Class Template Reference
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

template<typename T>

class BPrivate::Network::BExclusiveBorrow< T >Smart pointer that allows shared ownership of an object with exclusive access. 


This smart pointer was designed to support the particular pattern where a non-threadsafe or non-lockable needs to be shared between two threads, where only one can have access to the underlying object at the time.


When creating a new object, the underlying object can be accessed using the dereference operator overloads as if with any other smart pointer. This ownership can then be borrowed by creating a [BBorrow](classBPrivate_1_1Network_1_1BBorrow.md) object. At that stage, the original owner can no longer access the underlying object, until the borrow is returned. The borrow can access the object as long as they retain the borrow. The borrow is returned by the borrow object going out of scope, or by the borrow object being assigned a `nullptr` object. At that stage, the original owner regains access.



```cpp
// Create a newly owned string object.
BExclusiveBorrow<BString> owner = make_exclusive_borrow<BString>("Initial value");
 
// Access the exclusively accessibe object and set it to a different value
owner->SetTo("New value set by owner");
 
// Create a borrow.
BBorrow<BString> borrow = BBorrow<BString>(owner);
 
try {
    owner->SetTo("Another value set by owner");
} catch (const BorrowError& e) {
 // This error will be thrown because the `owner` cannot access the object while borrowed.
}
 
try {
    BBorrow<BString> secondBorrow = BBorrow<BString>(owner);
} catch (const BorrowError& e) {
 // This error will be thrown because there cannot be more than one borrow at a time.
}
 
// The `borrow` has exclusive access to the underlying BString object
borrow->SetTo("A value set by the borrower");
 
// The borrow is returned by explicitly setting it to `nullptr` or by having the object go out
// of scope.
borrow = nullptr;
 
// The owner can access the object again
assert(*owner == "A value set by the borrower");
```

Object Lifetime ManagementThe [BExclusiveBorrow](classBPrivate_1_1Network_1_1BExclusiveBorrow.md) and [BBorrow](classBPrivate_1_1Network_1_1BBorrow.md) pair manage the lifetime of the underlying object, meaning the memory will be freed when the object is no longer referenced by either the owner or the borrower. It is possible to get the ownership of the underlying object through the [BExclusiveBorrow::Release()](classBPrivate_1_1Network_1_1BExclusiveBorrow.md#a5a7fc48f8c2892988f9adc2d86b2e78f) method. This returns a `unique_ptr`.
Creating New ObjectsWhen creating a [BExclusiveBorrow](classBPrivate_1_1Network_1_1BExclusiveBorrow.md) object, you can use the [BExclusiveBorrow(T* object)](classBPrivate_1_1Network_1_1BExclusiveBorrow.md#a3774e0c2fcb68201e285b07f4329aa4f) constructor to create a new smart pointer that takes an *existing* underlying object. Note that the smart pointer will assume ownership, meaning that you should also have ownership of that object. If you want to create a [BExclusiveBorrow](classBPrivate_1_1Network_1_1BExclusiveBorrow.md) object for a new object, then you can use the [make_exclusive_borrow()](group__netservices.md#ga9d2f443c775ed1dff92d0cd6196adf93) function to create a new object.
Move Semantics and Empty ObjectsThe template class is designed around having an underlying object value, and in most cases will have an underlying object. However, there may be cases where a BExclusiveOwner or [BBorrow](classBPrivate_1_1Network_1_1BBorrow.md) object will not have an internal value. This either happens when it is explicitly assigned an empty value, or after the object has been moved. You can check whether the object has a value through the [HasValue()](classBPrivate_1_1Network_1_1BExclusiveBorrow.md#a3a95bdba411f5f861d2e43170d45b34d) method. Trying to access an empty object will throw a [BBorrowError](classBPrivate_1_1Network_1_1BBorrowError.md).
Checked AccessThe semantics of the exclusive ownership are enforced by this class. The rules are:
* There can only be one owner. The object cannot be copied, only moved.

* There can only be one borrower at a time. The borrow object cannot be copied, only moved.

* If one tries to create an additional borrow, an exception is thrown.

* If an object is borrowed, accessing it through the owner will throw exceptions.




Casting Pointers between Owner and BorrowerFor some design patterns, you may want to be able to cast the type of the owner to a related type for the borrower. For example, the [Network](namespaceBPrivate_1_1Network.md) Services kit accepts a `BBorrow<BDataIO>` type in order to allow the user to specify where to write the content of a network request to. The [BDataIO](../support_kit/classBDataIO.md) itself is an abstract interface to read and write data from an object. A user will most likely use a [BFile](../storage_kit/classBFile.md) or [BMallocIO](../support_kit/classBMallocIO.md) as underlying objects, both of which have [BDataIO](../support_kit/classBDataIO.md) as their base class.
Due to the specialized constructor of [BBorrow](classBPrivate_1_1Network_1_1BBorrow.md), it is possible to cast between compatible pointer types, without loosing the advantages of properly cleaning up the object when the borrow and the owner go out of scope. In the internals of the template, a type erasure technique similar to that of `std::shared_ptr` is used.

```cpp
// Create a new BFile object, which inherits the BDataIO class.
BExclusiveBorrow<BFile> owner = make_exclusive_borrow<BFile>("path/to/file", B_READ_WRITE);
// The following succeeds because a BFile pointer can be assigned to a BDataIO pointer.
BBorrow<BDataIO> borrow = BBorrow<BDataIO>(owner);
```

Multithread Safety, and Performance CostThis smart object uses atomics to synchronize the ownership and borrows of the object, and to enforce all the checks that were mentioned previously. The atomics guarantee that when you want to access the object in [BExclusiveBorrow](classBPrivate_1_1Network_1_1BExclusiveBorrow.md), that this only succeeds after any outstanding borrow is completed, otherwise an exception is thrown. While atomics can be used as a method of synchronization, this templace class is *not* designed for that and it does not have the tools to help doing that. If you need to synchronize object access between through threads, you should use semaphores or thread joins instead.
Template Parameters

| Col 1 | Col 2 |
| :--- | :--- |
| T | The type of object for this smart pointer. |





**Since:** Haiku R1

## Member List

### Public Member Functions

* [BExclusiveBorrow](#af5b72c221574d182b29f27a1a4eb4518) () noexcept — Create a new smart pointer with no value.
* [BExclusiveBorrow](#a4d2fd4fe4985838dfee5b3a83ff6fe14) (BExclusiveBorrow &&other) noexcept — Move constructor.
* [BExclusiveBorrow](#a0c6d71369f832a7feb455a6f50c2f68c) (nullptr_t) noexcept — Special constructor that creates a new smart pointer with no value.
* [BExclusiveBorrow](#a3774e0c2fcb68201e285b07f4329aa4f) (T *object) — Create a new smart pointer that takes ownership of the object.
* [~BExclusiveBorrow](#a5404867eb8a34dacbcd9f3c645a4c2d5) () — Destructor.
* `bool` [HasValue](#a3a95bdba411f5f861d2e43170d45b34d) () const noexcept — Check if the object has a value or is empty.
* `T &` [operator*](#a63fe5db991ceabf8ce079587fdcd2892) () const — Dereferences the pointer.
* `T *` [operator->](#a14339cc646350e12061f0601be87ede1) () const — Dereferences the pointer.
* `BExclusiveBorrow &` [operator=](#aef3712f61fe6543f81444bd4f2cb9ed4) (BExclusiveBorrow &&other) noexcept — Move assignment.
* `std::unique_ptr< T >` [Release](#a5a7fc48f8c2892988f9adc2d86b2e78f) () — Returns a unique_ptr of the inner object and releases the ownership.

## Detailed Member Documentation

### `BExclusiveBorrow()`

```cpp
BPrivate::Network::BExclusiveBorrow< T >::BExclusiveBorrow()
```

Create a new smart pointer with no value. 



**Since:** Haiku R1

---

### `BExclusiveBorrow()`

```cpp
BPrivate::Network::BExclusiveBorrow< T >::BExclusiveBorrow(nullptr_t)
```

Special constructor that creates a new smart pointer with no value. 



**Since:** Haiku R1

---

### `BExclusiveBorrow()`

```cpp
BPrivate::Network::BExclusiveBorrow< T >::BExclusiveBorrow(T * object)
```

Create a new smart pointer that takes ownership of the *object*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `object` | The object to wrap inside this smart pointer. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | In case there are issues allocating memory for the internals of the smart pointer. |





**Since:** Haiku R1

---

### `~BExclusiveBorrow()`

```cpp
BPrivate::Network::BExclusiveBorrow< T >::~BExclusiveBorrow()
```

Destructor. 


If the smart pointer is not empty, the underlying object will be deleted if there no longer is a borrow accessing it.



**Since:** Haiku R1

---

### `BExclusiveBorrow()`

```cpp
BPrivate::Network::BExclusiveBorrow< T >::BExclusiveBorrow(BExclusiveBorrow< T > && other)
```

Move constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The object to move from. It will be left empty after the move. |





**Since:** Haiku R1

---

### `HasValue()`

```cpp
bool BPrivate::Network::BExclusiveBorrow< T >::HasValue()const
```

Check if the object has a value or is empty. 



**Since:** Haiku R1

---

### `operator*()`

```cpp
T & BPrivate::Network::BExclusiveBorrow< T >::operator*()const
```

Dereferences the pointer. 


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| [BBorrowError](classBPrivate_1_1Network_1_1BBorrowError.md) | This exception is raised if the object is borrowed, or if it is empty. |





**Since:** Haiku R1

---

### `operator->()`

```cpp
T * BPrivate::Network::BExclusiveBorrow< T >::operator->()const
```

Dereferences the pointer. 


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| [BBorrowError](classBPrivate_1_1Network_1_1BBorrowError.md) | This exception is raised if the object is borrowed, or if it is empty. |





**Since:** Haiku R1

---

### `operator=()`

```cpp
BExclusiveBorrow & BPrivate::Network::BExclusiveBorrow< T >::operator=(BExclusiveBorrow< T > && other)
```

Move assignment. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The object to move from. It will be left empty after the move. |





**Since:** Haiku R1

---

### `Release()`

```cpp
std::unique_ptr< T > BPrivate::Network::BExclusiveBorrow< T >::Release()
```

Returns a unique_ptr of the inner object and releases the ownership. 


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| [BBorrowError](classBPrivate_1_1Network_1_1BBorrowError.md) | This exception is raised if the object is borrowed, or if it is empty. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BExclusiveBorrow.html).
