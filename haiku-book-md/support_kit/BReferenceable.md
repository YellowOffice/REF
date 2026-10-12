---
name: BReferenceable
type: class
kit: support_kit
brief: "Implementation of reference-counted memory management"
source: haiku-book
---

# BReferenceable Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Implementation of reference-counted memory management. 


The C++ language provides two main ways of allocating objects: on the stack, and on the heap. Objects created on the heap must be managed by the application and deleted when they are not needed. Objects allocated on the stack have a lifetime limited to the execution of the block they are declared in.


This approach is simple, but in some cases it can become quite difficult to track ownership and lifetime of objects. The [BReferenceable](classBReferenceable.md) class allows to implement reference counting, which allows a partially automated memory management and some safety checks. It can also be used to implement pools of reusable objects.


As the name implies, reference counting consists of keeping track, inside an object, of how much references there are to it in the running application. When the object is not referenced anymore, it can't be reached or used from other parts of the application, so it is safe to delete or recycle the object.


To use reference counting for a particular class, you make it inherit [BReferenceable](classBReferenceable.md). This provides all the support for reference counting. Objects are created as usual, on the stack or using the new operator.


The object can then be referenced from other places. Each time a reference to it is kept, the owner of the reference should call AcquireReference. When the reference is not needed, it should call ReleaseReference.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BReferenceable](#aef45178f24465974be5d385b204176e3) () — Initialize the object with a reference count of 1.
* `virtual` [~BReferenceable](#aed77fa81682764305085f8c8480b2b19) () — Destructor.
* `int32` [AcquireReference](#ac98c8b1801978166c2a7e6c994fb689a) () — Acquire a reference to the object.
* `int32` [CountReferences](#a2ffe8211f9390cb6b83f0fc86824a3a1) () const — Return the number of references to the object.
* `int32` [ReleaseReference](#a699a804cd2650e9f9078c49958aa431b) () — Release a reference to the object.

### Protected Member Functions

* `virtual void` [FirstReferenceAcquired](#aa9e2bd2354b0985827a2868b8aa15f47) () — Called when the first reference to the object is reacquired.
* `virtual void` [LastReferenceReleased](#a86ae8a45fa2fce4f5db3bdecac6a0a5e) () — Called when the last reference to the object is released.

## Detailed Member Documentation

### `BReferenceable()`

```cpp
BReferenceable::BReferenceable()
```

Initialize the object with a reference count of 1. 


The creator of the object is assumed to owns the first reference to it.

---

### `~BReferenceable()`

```cpp
BReferenceable::~BReferenceable()
```

Destructor. 


The destructor should not be called directly, as the object is destructed automatically when the last reference is released. This destructor is public because you may still need to destroy the objects in the case where LastReferenceReleased is overriden and you handle object destruction in some other way.


In debug mode, the destructor checks that no references to the object are still held. If the object was allocated on the stack, it allows exactly one reference to be kept, which makes it possible to allocate [BReferenceable](classBReferenceable.md) on the stack without needing to release the single reference to it.

---

### `AcquireReference()`

```cpp
int32 BReferenceable::AcquireReference()
```

Acquire a reference to the object. 



**Returns:** the previous reference count


If the reference count was previously 0, this will call FirstReferenceAcquired.

---

### `CountReferences()`

```cpp
int32 BReferenceable::CountReferences()const
```

Return the number of references to the object. 



**Returns:** the reference count.


References [atomic_get()](group__support__globals.md#ga61648da3ddc2f3df3c0b08b14b5dd09e).

---

### `FirstReferenceAcquired()`

```cpp
void BReferenceable::FirstReferenceAcquired()
```

Called when the first reference to the object is reacquired. 


The default implementation does nothing. This method can be overriden to implement reinitialization of the object, when using [BReferenceable](classBReferenceable.md) to keep track of a pool of reusable objects.


In this use case, the objects are created (at initialization or lazily on an as-needed basis) and stored in a pool. When an object is needed, if there is an unused one waiting in the pool, it is reused instead of creating a new one. Once a reference to it is acquired, this method is called and the object can initialize itself to a clean state.



> [!WARNING]
> This is currently not called when the object is first created, but only on subsequent reuses.

---

### `LastReferenceReleased()`

```cpp
void BReferenceable::LastReferenceReleased()
```

Called when the last reference to the object is released. 


This function is called when the object is not referenced anymore. The default implementation deletes the object using the delete operator.


This behavior can be overriden. For example, to implement an object pool, this method would not delete the object, but instead put it back in the free object pool, ready for reuse at a later point.

---

### `ReleaseReference()`

```cpp
int32 BReferenceable::ReleaseReference()
```

Release a reference to the object. 



**Returns:** the previous reference count


If the reference count was previously 1 (and is now 0), this will call LastReferenceReleased.

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBReferenceable.html).
