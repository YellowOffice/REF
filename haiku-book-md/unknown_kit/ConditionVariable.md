---
name: ConditionVariable
type: struct
kit: unknown_kit
brief: "Condition variable for thread and interrupt synchronization"
source: haiku-book
---

# ConditionVariable Struct
**Kit/Group:** [Kernel Kit](group__kernel.md)

## Description

Condition variable for thread and interrupt synchronization. 


Condition variables implement the wait/notify pattern. They are usually associated with an "object" (for the condition variable's own purposes, that is just an opaque pointer).


One thread will use the Wait functions or a [ConditionVariableEntry](structConditionVariableEntry.md) to wait on the condition variable. When another thread or an interrupt needs to wake up one such thread, it does so by notifying the condition variable.


Condition variables are usually used in combination with a mutex, recursive_lock, or some other direct use of the [ConditionVariableEntry](structConditionVariableEntry.md) struct with its two-step interface ([Add()](structConditionVariable.md#abb351282edc4d0ca542e0046e978e16a) then [Wait()](structConditionVariable.md#aab03cdbac51ea2d61172763904151e6a)) allows usage of any other locking design, or even with no locking at all if the order of operations is already guaranteed by the code structure.


There are no restrictions on the destruction order: a condition variable may be destructed while there are condition variable entries waiting on it, or the condition variable entries may be destructed before they are notified.

## Member List

### Public Member Functions

* `void` Add ([ConditionVariableEntry](#ConditionVariableEntry) *entry) — Add a ConditionVariableEntry to the waiting list for this condition variable.
* `int32` [EntriesCount](#a8f9e5c13b0735859d76eec224ef8061e) () — Return the number of ConditionVariableEntries that are currently in the ConditionVariable.
* `void` [Init](#a215fe6d8fbb6372b16e64e65980a3830) (const void *object, const char *objectType) — Initialize an anonymous (unpublished) condition variable.
* `int32` [NotifyAll](#a90209157b046b62a1edad4d7098e1929) (status_t result=B_OK) — Notify all the threads waiting on the condition variable.
* `int32` [NotifyOne](#aca8f6069de730feea6e8d7760a8c727a) (status_t result=B_OK) — Notify one of the threads waiting on the condition variable.
* `void` [Publish](#a443b52824050747ee72ed951c6e45a46) (const void *object, const char *objectType) — Initialize and publish a condition variable associated with an object.
* `void` Unpublish () — Unpublish a previously published condition variable.
* `status_t` [Wait](#aecfab06bac2084489d901f16ab6d9b23) (mutex *lock, uint32 flags=0, bigtime_t timeout=0) — Convenience method for atomically unlocking a mutex and waiting on a condition variable.
* `status_t` [Wait](#a5549eb777fcb787fed7bd5d7d1e08ba8) (recursive_lock *lock, uint32 flags=0, bigtime_t timeout=0) — Convenience method for atomically unlocking a recursive_lock and waiting on a condition variable.
* `status_t` [Wait](#aab03cdbac51ea2d61172763904151e6a) (uint32 flags=0, bigtime_t timeout=0) — Convenience method for waiting without an explicit ConditionVariableEntry.

### Static Public Member Functions

* `static int32` [NotifyAll](#ad834424526f5283bf7ebff159b44430c) (const void *object, status_t result) — Notify all threads waiting on the published condition variable for object.
* `static int32` [NotifyOne](#ac4757171e06a574e7160758dee6a3f18) (const void *object, status_t result) — Notify one thread waiting on the published condition variable for object.

## Detailed Member Documentation

### `EntriesCount()`

```cpp
int32 ConditionVariable::EntriesCount()
```

Return the number of ConditionVariableEntries that are currently in the [ConditionVariable](structConditionVariable.md). 


The threads associated with such entries may already be waiting, or still executing other code between their Add and Wait steps. 


References [atomic_get()](../support_kit/group__support__globals.md#ga61648da3ddc2f3df3c0b08b14b5dd09e).

---

### `Init()`

```cpp
void ConditionVariable::Init(const void * object, const char * objectType)
```

Initialize an anonymous (unpublished) condition variable. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `object` | Object that the condition variable is associated with. |
| `objectType` | String describing the associated object, for debugging purposes. |




Anonymous condition variables cannot be used with [ConditionVariableEntry::Add()](structConditionVariableEntry.md#a8f98a277ac9e0f0f888d39dd2465173e) and will not appear in the kernel debugger list of condition variables (it can still be examined by the dump command if you have a pointer to it). The other methods can be used without restrictions.

---

### `NotifyAll()`

```cpp
static int32 ConditionVariable::NotifyAll(const void * object, status_t result)
```

Notify all threads waiting on the published condition variable for *object*. 



**Returns:** The number of threads that were notified

---

### `NotifyAll()`

```cpp
int32 ConditionVariable::NotifyAll(status_t result = B_OK)
```

Notify all the threads waiting on the condition variable. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `result` | Result value that will be returned by the Wait call in the notified thread. |





**Returns:** Number of threads that will the result value

---

### `NotifyOne()`

```cpp
static int32 ConditionVariable::NotifyOne(const void * object, status_t result)
```

Notify one thread waiting on the published condition variable for *object*. 



**Returns:** The number of threads that were notified (0 or 1)

---

### `NotifyOne()`

```cpp
int32 ConditionVariable::NotifyOne(status_t result = B_OK)
```

Notify one of the threads waiting on the condition variable. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `result` | Result value that will be returned by the Wait call in the notified thread. |





**Returns:** Number of threads that will receive the result value (0 if no [ConditionVariableEntry](structConditionVariableEntry.md) was attached, or 1 if there were)


If the thread was already blocked by calling Wait, its execution is resumed.


If the thread had added a [ConditionVariableEntry](structConditionVariableEntry.md) to the condition variable but is not yet waiting on it, the call to Wait will not block, and will immediately return the *result* value.

---

### `Publish()`

```cpp
void ConditionVariable::Publish(const void * object, const char * objectType)
```

Initialize and publish a condition variable associated with an *object*. 


The condition variable is published: [ConditionVariableEntry::Add()](structConditionVariableEntry.md#a8f98a277ac9e0f0f888d39dd2465173e) can be used on the associated object, and the condition variable will be present in the kernel debugger's condition variables list.


Publication allows to associate a condition variable with another object that is accessed from multiple drivers or kernel modules. For example, this can be used to notify some events from low level drivers to higher level ones (interrupts, hot-pluggable device being removed, ...) by publishing condition variables associated to device tree nodes.

---

### `Wait()`

```cpp
status_t ConditionVariable::Wait(mutex * lock, uint32 flags = 0, bigtime_t timeout = 0)
```

Convenience method for atomically unlocking a mutex and waiting on a condition variable. 


Create and add a temporary [ConditionVariableEntry](structConditionVariableEntry.md) to the condition variable, unlock the mutex, wait on the condition variable, and re-acquire the mutex.


This allows to use the condition variable safely for inter-thread synchronization with mutex.

---

### `Wait()`

```cpp
status_t ConditionVariable::Wait(recursive_lock * lock, uint32 flags = 0, bigtime_t timeout = 0)
```

Convenience method for atomically unlocking a recursive_lock and waiting on a condition variable. 


Create and add a temporary [ConditionVariableEntry](structConditionVariableEntry.md) to the condition variable, unlock the recursive_lock, wait on the condition variable, and re-acquire the recursive_lock.


The recursion count of the recursive lock is preserved.


This allows to use the condition variable safely for inter-thread synchronization with a recursive_lock.

---

### `Wait()`

```cpp
status_t ConditionVariable::Wait(uint32 flags = 0, bigtime_t timeout = 0)
```

Convenience method for waiting without an explicit [ConditionVariableEntry](structConditionVariableEntry.md). 


Create and add a temporary [ConditionVariableEntry](structConditionVariableEntry.md) to the condition variable, then wait on it.

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structConditionVariable.html).
