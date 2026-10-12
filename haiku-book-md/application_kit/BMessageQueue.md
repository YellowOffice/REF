---
name: BMessageQueue
type: class
kit: application_kit
brief: "A container that maintains a queue of messages"
source: haiku-book
---

# BMessageQueue Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A container that maintains a queue of messages. 


This class is used by [BLooper](classBLooper.md) to maintain a queue of messages that need to be processed. This class has been designed as a first in, first out container.


The default message handling of a [BLooper](classBLooper.md) probably suffices for most uses, but if you want more control, you can perform operations using the methods of this class. Use [BLooper::MessageQueue()](classBLooper.md#ad0643973ceda5cca540c4684a9f670ac) to retrieve the specific [BMessageQueue](classBMessageQueue.md) instance.


Note that you are encouraged to make sure that whichever operation you perform, that you only do this after the object has been locked (see [Lock()](classBMessageQueue.md#af02862de04f304f2ca1d0665dbc555f4)). The most important method, [NextMessage()](classBMessageQueue.md#ac43250227a2d7ebe25287e8bb7e2f4de) will fail if you have not complied with this requirement.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BMessageQueue](#ab65ad5a2fad4b4574e490a0b65282b1c) () — Constructs an empty message queue.
* `virtual` [~BMessageQueue](#a6cc31296ddac5ef7fc19cdd40c4ef314) () — Destruct the BMessageQueue. It iterates over any messages left on the queue and deletes them.
* `void` [AddMessage](#a2dfdb322775026c6d3e50da3d53c760a) (BMessage *message) — Add a message to the end of the queue.
* `int32` [CountMessages](#a5b03b046c4e4e631ee48b9b9effb00e2) () const — Return the number of messages waiting in the queue.
* `BMessage *` [FindMessage](#a7f849a0a1a1478e2a91a529d1b318b38) (int32 index) const — Retrieve the message at the index of this queue.
* `BMessage *` [FindMessage](#a28d39fce8b2672f10ceb36fc54ae88fa) (uint32 what, int32 index=0) const — Retrieve the message at the index of this queue, but only if it has a specific what constant.
* `bool` [IsEmpty](#ac01e4e0b8491f96bb02aae2bb9cbd2e2) () const — Check if there are messages waiting in the queue.
* `bool` [IsLocked](#a06f96a090475ea4064bd6cf99789299a) () const — Check if the queue is locked.
* `bool` [IsNextMessage](#a2d420852de788cc07f17d53a8dbb2a32) (const BMessage *message) const — Check if the pointer to a message points at the next message on the queue.
* `bool` [Lock](#af02862de04f304f2ca1d0665dbc555f4) () — Lock the queue so no other thread can perform operations on it.
* `BMessage *` [NextMessage](#ac43250227a2d7ebe25287e8bb7e2f4de) () — Remove the first BMessage on the queue and return it to the caller.
* `void` [RemoveMessage](#a9871427c7af17f88cd6a931afb740a57) (BMessage *message) — Remove a message from the queue.
* `void` [Unlock](#afffb5a231a21f8f70e2b17e8857eb5d6) () — Unlock the queue after a Lock() request.

## Detailed Member Documentation

### `BMessageQueue()`

```cpp
BMessageQueue::BMessageQueue()
```

Constructs an empty message queue. 



**Since:** BeOS R3

---

### `~BMessageQueue()`

```cpp
BMessageQueue::~BMessageQueue()
```

Destruct the [BMessageQueue](classBMessageQueue.md). It iterates over any messages left on the queue and deletes them. 


The implementation is careful not to release the lock when the [BMessageQueue](classBMessageQueue.md) is deconstructed. If the lock is released, it is possible another thread will start an [AddMessage()](classBMessageQueue.md#a2dfdb322775026c6d3e50da3d53c760a) operation before the [BLocker](../support_kit/classBLocker.md) is deleted. The safe thing to do is not to unlock the [BLocker](../support_kit/classBLocker.md) from the destructor once it is acquired. That way, any thread waiting to do a [AddMessage()](classBMessageQueue.md#a2dfdb322775026c6d3e50da3d53c760a) will fail to acquire the lock since the [BLocker](../support_kit/classBLocker.md) will be deleted before they can acquire it.



**Since:** BeOS R3

---

### `AddMessage()`

```cpp
void BMessageQueue::AddMessage(BMessage * message)
```

Add a *message* to the end of the queue. 


The message has to be allocated on the heap with `new`, because the queue claims ownership of the message. Messages that were constructed on the stack will corrupt the queue.


Because a [BMessageQueue](classBMessageQueue.md) claims ownership of the *message*, it is important that the message does not belong to another [BMessageQueue](classBMessageQueue.md).



**Since:** BeOS R3

---

### `CountMessages()`

```cpp
int32 BMessageQueue::CountMessages()const
```

Return the number of messages waiting in the queue. 



**Since:** BeOS R3

---

### `FindMessage()`

```cpp
BMessage * BMessageQueue::FindMessage(int32 index)const
```

Retrieve the message at the *index* of this queue. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | A zero-based index of the message you want to retrieve. |





**Returns:** A pointer to a message, or `NULL` if the *index* is out of bounds.



**See also:** FindMessage(uint32, int32) for a variant that takes a specific `what` identifier.



**Since:** BeOS R3

---

### `FindMessage()`

```cpp
BMessage * BMessageQueue::FindMessage(uint32 what, int32 index = 0)const
```

Retrieve the message at the *index* of this queue, but only if it has a specific *what* constant. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | A zero-based index of the message you want to retrieve. |
| `what` | The *what* code of the message. |





**Returns:** A pointer to a message, or `NULL` if there is no message at the *index* with that *what* constant, or if the *index* is out of bounds.



**Since:** BeOS R3

---

### `IsEmpty()`

```cpp
bool BMessageQueue::IsEmpty()const
```

Check if there are messages waiting in the queue. 



**Since:** BeOS R3

---

### `IsLocked()`

```cpp
bool BMessageQueue::IsLocked()const
```

Check if the queue is locked. 



**See also:** [Lock()](classBMessageQueue.md#af02862de04f304f2ca1d0665dbc555f4)



**Since:** Haiku R1

---

### `IsNextMessage()`

```cpp
bool BMessageQueue::IsNextMessage(const BMessage * message)const
```

Check if the pointer to a *message* points at the next message on the queue. 



**Since:** Haiku R1

---

### `Lock()`

```cpp
bool BMessageQueue::Lock()
```

Lock the queue so no other thread can perform operations on it. 



**See also:** [Unlock()](classBMessageQueue.md#afffb5a231a21f8f70e2b17e8857eb5d6)



**Since:** BeOS R3

---

### `NextMessage()`

```cpp
BMessage * BMessageQueue::NextMessage()
```

Remove the first [BMessage](classBMessage.md) on the queue and return it to the caller. 


After calling this method, you get the ownership of the message, so make sure it is deleted after you are done.



**Returns:** A pointer to a message, or `NULL` if the queue is empty, or the object has not been properly locked.



**See also:** [Lock()](classBMessageQueue.md#af02862de04f304f2ca1d0665dbc555f4)



**Since:** BeOS R3

---

### `RemoveMessage()`

```cpp
void BMessageQueue::RemoveMessage(BMessage * message)
```

Remove a *message* from the queue. 


If the *message* is indeed associated with this queue, it is removed from it. This effectively means that you regain ownership of the message.



**Since:** BeOS R3

---

### `Unlock()`

```cpp
void BMessageQueue::Unlock()
```

Unlock the queue after a [Lock()](classBMessageQueue.md#af02862de04f304f2ca1d0665dbc555f4) request. 



**See also:** [Lock()](classBMessageQueue.md#af02862de04f304f2ca1d0665dbc555f4)



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMessageQueue.html).
