---
name: BPrivate::Network::BBorrow< T > Template Reference
type: class
kit: netservices_kit
brief: "Smart pointer that borrows an object from a BExclusiveBorrow owner"
source: haiku-book
---

# BPrivate::Network::BBorrow< T > Class Template Reference
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

template<typename T>

class BPrivate::Network::BBorrow< T >Smart pointer that borrows an object from a [BExclusiveBorrow](classBPrivate_1_1Network_1_1BExclusiveBorrow.md) owner. 


The [BBorrow](classBPrivate_1_1Network_1_1BBorrow.md) smart pointer is the accompanyment to the [BExclusiveBorrow](classBPrivate_1_1Network_1_1BExclusiveBorrow.md) owner object. See the documentation on that template class on how to use the smart pointer pairs to express and enforce exclusive ownership between the owner and the borrower.


Like a [BExclusiveBorrow](classBPrivate_1_1Network_1_1BExclusiveBorrow.md) object, a [BBorrow](classBPrivate_1_1Network_1_1BBorrow.md) object can either have a borrow or be empty. When it is empty, it means the current object is not borrowing anything at that moment. Any calls to access the underlying data will fail in that case.


Template Parameters

| Col 1 | Col 2 |
| :--- | :--- |
| T | The type of object that is owned by this smart pointer. |





**Since:** Haiku R1

## Member List

### Public Member Functions

* [BBorrow](#ad903e9f280f48a5ddd03dc284be82c4b) () noexcept — Create a new smart pointer with no value.
* [BBorrow](#a8878a4629154e7165fc076acf865e912) (BBorrow &&other) noexcept — Move constructor.
* 
*  — Construct a borrowed object from the owner.
* [BBorrow](#a62395d4a3ebae71cb8c8d7a85028ca1b) (nullptr_t) noexcept — Special constructor that builds an empty borrow object.
* [~BBorrow](#a77b10a579d6982a30422c5040eb16bb1) () — Destructor that returns the object to the original owner.
* `bool` [HasValue](#a82878adbd2c0e40296e6481c4c314590) () const noexcept — Check if the object has a value or is empty.
* `T &` [operator*](#a8e8cec6c2312d7e8fe2aecabb3cde875) () const — Dereference operator.
* `T *` [operator->](#a0f3c63dd00d7e10a94f698d343b9068d) () const — Dereference operator.
* `BBorrow &` [operator=](#a4d60b54217d8da6de0ff4b61219aa7a8) (BBorrow &&other) noexcept — Move assignment.
* `void` [Return](#af3c89452b889097865f1a48511cdd81b) () noexcept — Return object to the owner.

## Detailed Member Documentation

### `BBorrow()`

```cpp
BPrivate::Network::BBorrow< T >::BBorrow()
```

Create a new smart pointer with no value. 



**Since:** Haiku R1

---

### `BBorrow()`

```cpp
BPrivate::Network::BBorrow< T >::BBorrow(nullptr_t)
```

Special constructor that builds an empty borrow object. 



**Since:** Haiku R1

---

### `BBorrow()`

```cpp
BPrivate::Network::BBorrow< T >::BBorrow(BExclusiveBorrow< P > & owner)
```

Construct a borrowed object from the *owner*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `owner` | The owner to borrow from. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| [BBorrowError](classBPrivate_1_1Network_1_1BBorrowError.md) | In case the *owner* already borrowed their object, or in case the *owner* is an empty object, as you cannot borrow something that is not there. |




Template Parameters

| Col 1 | Col 2 |
| :--- | :--- |
| T | The type of object for this [BBorrow](classBPrivate_1_1Network_1_1BBorrow.md) object. |
| P | The type of objedt for the [BExclusiveBorrow](classBPrivate_1_1Network_1_1BExclusiveBorrow.md) object. This allows you to have different types between the owner and the borrower, with the requirement that a pointer to type P can be cast to a pointer of type T without issue. |





**Since:** Haiku R1

---

### `BBorrow()`

```cpp
BPrivate::Network::BBorrow< T >::BBorrow(BBorrow< T > && other)
```

Move constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The object to move from. It will be left empty after the move. |





**Since:** Haiku R1

---

### `~BBorrow()`

```cpp
BPrivate::Network::BBorrow< T >::~BBorrow()
```

Destructor that returns the object to the original owner. 


If the original owner no longer exists, the underlying object will be deleted.



**Since:** Haiku R1

---

### `HasValue()`

```cpp
bool BPrivate::Network::BBorrow< T >::HasValue()const
```

Check if the object has a value or is empty. 



**Since:** Haiku R1

---

### `operator*()`

```cpp
T & BPrivate::Network::BBorrow< T >::operator*()const
```

Dereference operator. 


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| [BBorrowError](classBPrivate_1_1Network_1_1BBorrowError.md) | When the smart pointer is empty and there is no object to access. |





**Since:** Haiku R1

---

### `operator->()`

```cpp
T * BPrivate::Network::BBorrow< T >::operator->()const
```

Dereference operator. 


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| [BBorrowError](classBPrivate_1_1Network_1_1BBorrowError.md) | When the smart pointer is empty and there is no object to access. |





**Since:** Haiku R1

---

### `operator=()`

```cpp
BBorrow & BPrivate::Network::BBorrow< T >::operator=(BBorrow< T > && other)
```

Move assignment. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The object to move from. It will be left empty after the move. |





**Since:** Haiku R1


References [BPrivate::Network::BBorrow< T >::Return()](classBPrivate_1_1Network_1_1BBorrow.md#af3c89452b889097865f1a48511cdd81b).

---

### `Return()`

```cpp
void BPrivate::Network::BBorrow< T >::Return()
```

Return object to the owner. 


The current object will be set to be an empty object after this call. If the object is already empty, this call will not do anything. If the owner no longer exists, the object will be disposed off.



**Since:** Haiku R1


Referenced by [BPrivate::Network::BBorrow< T >::operator=()](classBPrivate_1_1Network_1_1BBorrow.md#a4d60b54217d8da6de0ff4b61219aa7a8).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BBorrow.html).
