---
name: ConditionVariableEntry
type: struct
kit: unknown_kit
brief: "Waiting on a condition variable"
source: haiku-book
---

# ConditionVariableEntry Struct
**Kit/Group:** [Kernel Kit](group__kernel.md)

## Description

Waiting on a condition variable. 


Waiting on a condition variable is implemented by creating a [ConditionVariableEntry](structConditionVariableEntry.md), associating it to a condition variable (using either [Add(const void*)](structConditionVariableEntry.md#a8f98a277ac9e0f0f888d39dd2465173e) or [ConditionVariable::Add(ConditionVariableEntry*)](structConditionVariable.md#abb351282edc4d0ca542e0046e978e16a) ), and then waiting for the condition variable to be notified using [Wait(uint32, bigtime_t)](structConditionVariableEntry.md#a7abc3796cf6aa4deb72a4744e305530b).

## Member List

### Public Member Functions

* `bool` [Add](#a8f98a277ac9e0f0f888d39dd2465173e) (const void *object) — Watch the published condition variable associated with the object.
* `ConditionVariable *` [Variable](#a50eb3287d6614d3c917940031e2dfa50) () const — Get a pointer to the added condition variable object.
* `status_t` [Wait](#ac2143a90ba001edb6dd4896b28be4df3) (const void *object, uint32 flags=0, bigtime_t timeout=0) — Convenience method to add a condition variable and immediately wait on it.
* `status_t` [Wait](#a7abc3796cf6aa4deb72a4744e305530b) (uint32 flags=0, bigtime_t timeout=0) — Wait for the condition variable to be notified.

## Detailed Member Documentation

### `Add()`

```cpp
bool ConditionVariableEntry::Add(const void * object)
```

Watch the published condition variable associated with the *object*. 


This method is used to watch a condition variable previously published using ConditionVariable::Publish(const cvoid*, const char*). The condition variable corresponding to the object will be located and the condition variable entry will be added to it.


A [ConditionVariableEntry](structConditionVariableEntry.md) can only be added to one single [ConditionVariable](structConditionVariable.md).


It is safe to delete a [ConditionVariableEntry](structConditionVariableEntry.md) without having waited for the corresponding event.



**Returns:** false if the entry could not be added. In that case, calling [Wait()](structConditionVariableEntry.md#a7abc3796cf6aa4deb72a4744e305530b) will immediately fail and return the corresponding error code B_ENTRY_NOT_FOUND.

---

### `Variable()`

```cpp
ConditionVariable * ConditionVariableEntry::Variable()const
```

Get a pointer to the added condition variable object. 


This allows to access the [ConditionVariable](structConditionVariable.md) object previously added to the condition variable. It is especially useful if you need to access a published condition variable, which you cannot access directly until adding it to a [ConditionVariableEntry](structConditionVariableEntry.md).


This returns NULL if the condition variable entry is not attached attached to any condition variable, including when the condition variable has already notified the entry.

---

### `Wait()`

```cpp
status_t ConditionVariableEntry::Wait(const void * object, uint32 flags = 0, bigtime_t timeout = 0)
```

Convenience method to add a condition variable and immediately wait on it. 


This combines the effect of the Add and Wait methods. You can use this if you are waiting on a published condition variable, and do not need to perform any other work between adding and waiting (such as releasing other locks to perform a "lock switch").

---

### `Wait()`

```cpp
status_t ConditionVariableEntry::Wait(uint32 flags = 0, bigtime_t timeout = 0)
```

Wait for the condition variable to be notified. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `flags` | timeout and semaphore flags to use |
| `timeout` | in microseconds if enabled by flags |





**Returns:** The status code passed to Notify to wake up the thread


Wait for the previously added condition variable to be notified. The thread is blocked until then, or until a timeout occurs. The entry is then removed from the condition variable waiting list. It can be reused by adding it to the same or another condition variable.


If the condition variable was already notified since this entry was added to it, the function returns immediately and does not block the thread.


The *flags* can be used to:


* Limit the wait to a timeout using B_RELATIVE_TIMEOUT or B_ABSOLUTE_TIMEOUT

* Control semaphore behavior (B_CAN_INTERRUPT, B_KILL_CAN_INTERRUPT)

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structConditionVariableEntry.html).
