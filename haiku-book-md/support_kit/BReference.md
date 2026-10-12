---
name: BReference< Type > Template Reference
type: class
kit: support_kit
brief: "A reference to a BReferenceable object"
source: haiku-book
---

# BReference< Type > Class Template Reference
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

template<typename Type = BReferenceable>

class BReference< Type >A reference to a [BReferenceable](classBReferenceable.md) object. 


[BReference](classBReference.md) simplifies the use of [BReferenceable](classBReferenceable.md) and makes it more transparent. It automatically acquires and release references to the pointed objects. It provides an API similar to a standard C++ pointer, allowing use of assignment and comparison operators and direct access to the object with -> and *.

## Member List

### Public Member Functions

* [BReference](#a97124246c768e66fc49dc0c7357f4bc7) () — Creates a reference without initializing it.
* [BReference](#ad694af934be34d8be54c709c7f8351cf) (const BReference< Type > &other) — Copy constructor.
* [BReference](#aefbc75bee079adf7f1b160d6191dd684) (Type *object, bool alreadyHasReference=false) — Creates and initialize a reference.
* [~BReference](#a872adc6879d3a5b48b899c88f5409e79) () — Destructor.
* `Type *` [Detach](#ab865062e02bcb965de786bea7123c2ce) () — Detach the pointed object from the reference.
* `Type *` [Get](#ab33183b2a96745b1395f8fdaf54012f6) () const — Get the target object.
* `void` [SetTo](#a1b58b8859fed0fe6553bef4127cf40c5) (Type *object, bool alreadyHasReference=false) — Sets a new target for the reference.
* `void` [Unset](#ae38aa2951c99b148715fbbc0d4e7c81f) () — Unsets the reference.

## Detailed Member Documentation

### `BReference()`

```cpp
BReference< Type >::BReference()
```

Creates a reference without initializing it. 


An uninitialized references behaves similarly to a NULL pointer.

---

### `BReference()`

```cpp
BReference< Type >::BReference(Type * object, bool alreadyHasReference = false)
```

Creates and initialize a reference. 


The reference is set to the pointed object. If the parameter is set to true, the reference count is not incremented, this should only be used when referencing a freshly constructed object. 


References [BReference< Type >::SetTo()](classBReference.md#a1b58b8859fed0fe6553bef4127cf40c5).

---

### `BReference()`

```cpp
BReference< Type >::BReference(const BReference< Type > & other)
```

Copy constructor. 


The reference is set to the same object as the source. The reference count of the target object is incremented. 


References [BReference< Type >::Get()](classBReference.md#ab33183b2a96745b1395f8fdaf54012f6), and [BReference< Type >::SetTo()](classBReference.md#a1b58b8859fed0fe6553bef4127cf40c5).

---

### `~BReference()`

```cpp
BReference< Type >::~BReference()
```

Destructor. 


The reference count of the target object is decremented. 


References [BReference< Type >::Unset()](classBReference.md#ae38aa2951c99b148715fbbc0d4e7c81f).

---

### `Detach()`

```cpp
ConstType * BReference< Type >::Detach()
```

Detach the pointed object from the reference. 



**Returns:** a raw pointer to the target object.


This returns the pointed object and unsets the reference, without decrementing the object reference count. It is used to transfer ownership of the reference to something else. 


References [NULL](SupportDefs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4).

---

### `Get()`

```cpp
ConstType * BReference< Type >::Get()const
```

Get the target object. 



**Returns:** a raw pointer to the target object.


Referenced by [BReference< Type >::BReference()](classBReference.md#ad694af934be34d8be54c709c7f8351cf).

---

### `SetTo()`

```cpp
void BReference< Type >::SetTo(Type * object, bool alreadyHasReference = false)
```

Sets a new target for the reference. 


The reference to the previously targetted object is released. A reference to the new object is acquired only if `alreadyHasReference` is false. 


References [NULL](SupportDefs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), and [BReference< Type >::Unset()](classBReference.md#ae38aa2951c99b148715fbbc0d4e7c81f).


Referenced by [BReference< Type >::BReference()](classBReference.md#aefbc75bee079adf7f1b160d6191dd684).

---

### `Unset()`

```cpp
void BReference< Type >::Unset()
```

Unsets the reference. 


The targetted object is released. The reference is unset and can't be used to access it anymore. 


References [NULL](SupportDefs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4).


Referenced by [BReference< Type >::~BReference()](classBReference.md#a872adc6879d3a5b48b899c88f5409e79), and [BReference< Type >::SetTo()](classBReference.md#a1b58b8859fed0fe6553bef4127cf40c5).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBReference.html).
