---
name: BLocker
type: class
kit: support_kit
brief: "Semaphore-type class for thread safety"
source: haiku-book
---

# BLocker Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Semaphore-type class for thread safety. 


The [BLocker](classBLocker.md) interface is not merely a wrapper around a semaphore, but it also has two advantages. First of all, it implements a benaphore. A benaphore is in some ways more speed efficient, because before it uses the internal semaphore, it first checks against a variable that is only operated on with atomic operations. Setting a variable is a lot more efficient than acquiring a semaphore, thus this type of locking is much preferred.


It basically works as follows. Whenever you newly created [BLocker](classBLocker.md) object receives a locking request, it atomically sets the benaphore variable to `1`. Then only additional calls from different threads will utilize the semaphore. You can imagine that in many cases where you protect of data that *might* be accessed by two or more concurrent threads, but the chances of it happening being very small, the benaphore benefits the most from its speed.


The other feature of [BLocker](classBLocker.md) that improves basic semaphore handling is that it allows for recursive locks. The following piece of code works with a [BLocker](classBLocker.md), but block inevitably with a semaphore. Let's pretend I call `Water()`:



```cpp
status_t
Flower::Grow(int length)
{
 if (fLock->Lock()) {
        fLength += length;
        fLock->Unlock();
 return B_OK;
    } else
 return B_ERROR;
}
 
status_t
Flower::Water(int amount)
{
 if (fLock->Lock()) {
 status_t status = Grow(amount * 2);
        fLock->Unlock();
 return status;
    } else
 return B_ERROR;
}
```

This code would work because [BLocker](classBLocker.md) keeps track of the amount of lock requests from the same thread. A normal semaphore would block in `Grow()` because the semaphore would be acquired already. Please do make sure you pair every [Lock()](classBLocker.md#a42596788c0e5dca043987b2efad244bd) with an [Unlock()](classBLocker.md#a0ebddc8ec0db8f51e57d6bff0f5ac2bf) though, or you'll create a deadlock.



**See also:** [BAutolock](classBAutolock.md)



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BLocker](#ad63fe8ee004e52497dfd0b75a57c0e69) () — Create a new BLocker with the default name "some BLocker" and benaphore-style locking.
* [BLocker](#a47a9333ac5c2b773b459cfab055ad793) (bool benaphoreStyle) — Creates a BLocker with the default name "some BLocker" and the given locking style.
* [BLocker](#ab347e240218606aced8e3ca8778e4465) (const char *name) — Creates a new BLocker with the given name and benaphore-style locking.
* [BLocker](#a94ccf392b8571f70827134ea007b1385) (const char *name, bool benaphoreStyle) — Creates a new BLocker with the given name and locking style.
* `virtual` [~BLocker](#a9926584a2ceb1fef875042f849d0d7f6) () — Destructor.
* `int32` [CountLockRequests](#a2919e1b6bdd50acb4318eed4b96026c3) () const — Return the number of threads with a pending lock request.
* `int32` [CountLocks](#ac2d2a9a6f1a33aafdf1014adf0e3767e) () const — Return the number of recursive locks that are currently held.
* `status_t` [InitCheck](#a14f387a1cbd1849238cef0c33ee26617) () const — Check whether the locker has properly initialized.
* `bool` [IsLocked](#a0a2e0aff83a6d31c0b0f2a228ccc9bec) () const — Check if the calling thread is actually holding the lock.
* `bool` [Lock](#a42596788c0e5dca043987b2efad244bd) () — Add a lock request and block on it until we get it.
* `thread_id` [LockingThread](#a5c586d25058fa71c5f279532e5401109) () const — Return the thread_id of the thread that's currently holding the lock.
* `status_t` [LockWithTimeout](#a6da24e86f4acab13f674889b7bf8226e) (bigtime_t timeout) — Add a lock request and block until we get it or until it times out.
* `sem_id` [Sem](#a4ed8883d53e7888cabb01eda8065b1c0) () const — Return the sem_id of the semaphore this object holds.
* `void` [Unlock](#a0ebddc8ec0db8f51e57d6bff0f5ac2bf) () — Release the lock that's currently held.

## Detailed Member Documentation

### `BLocker()`

```cpp
BLocker::BLocker()
```

Create a new [BLocker](classBLocker.md) with the default name "some BLocker" and benaphore-style locking. 


This [BLocker](classBLocker.md) will use the benaphore-style locking.



> [!NOTE]
> For debugging purposes, it's extremely convenient to actually give a name to the object. In case of a deadlock, it's easier to track down which [BLocker](classBLocker.md) object might have caused the problems.



**See also:** [BLocker(const char*, bool)](classBLocker.md#a94ccf392b8571f70827134ea007b1385) for all the options.



**Since:** BeOS R3

---

### `BLocker()`

```cpp
BLocker::BLocker(const char * name)
```

Creates a new [BLocker](classBLocker.md) with the given *name* and benaphore-style locking. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | A NULL-terminated string that contains the name of the semaphore. Note that the length of the names are limited to `B_OS_NAME_LENGTH` constant, which includes the `\0` character. |





**See also:** [BLocker(const char* name, bool benaphoreStyle)](classBLocker.md#a94ccf392b8571f70827134ea007b1385) for all the options.



**Since:** BeOS R3

---

### `BLocker()`

```cpp
BLocker::BLocker(bool benaphoreStyle)
```

Creates a [BLocker](classBLocker.md) with the default name "some BLocker" and the given locking style. 



> [!NOTE]
> For debugging purposes, it's extremely convenient to actually give a name to the object. In case of a deadlock, it's easier to track down which [BLocker](classBLocker.md) object might have caused the problems.


Parameters

| Parameter | Description |
| :--- | :--- |
| `benaphoreStyle` | If you pass `true`, the locker will be in benaphore style (which is the default option for other constructors). If you pass `false`, the object will completely rely on semaphores for its functioning. |





**See also:** [BLocker(const char* name, bool benaphoreStyle)](classBLocker.md#a94ccf392b8571f70827134ea007b1385) if you also want to set a name.



**Since:** BeOS R4

---

### `BLocker()`

```cpp
BLocker::BLocker(const char * name, bool benaphoreStyle)
```

Creates a new [BLocker](classBLocker.md) with the given *name* and locking style. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | A NULL-terminated string that contains the name of the semaphore. Note that the length of the names are limited to `B_OS_NAME_LENGTH` constant, which includes the `\0` character. |
| `benaphoreStyle` | If you pass `true`, the locker will be in benaphore style (which is the default option for other constructors). If you pass `false`, the object will completely rely on semaphores for its functioning. |





**Since:** BeOS R4

---

### `~BLocker()`

```cpp
BLocker::~BLocker()
```

Destructor. 


Release the internal semaphore. Because of this, any pending [Lock()](classBLocker.md#a42596788c0e5dca043987b2efad244bd) calls from other threads be cancelled. The return code will be `false` for those calls.



**Since:** BeOS R3

---

### `CountLockRequests()`

```cpp
int32 BLocker::CountLockRequests(void)const
```

Return the number of threads with a pending lock request. 



**Returns:** The number of threads with a pending lock request as an int32.



**Since:** BeOS R3

---

### `CountLocks()`

```cpp
int32 BLocker::CountLocks(void)const
```

Return the number of recursive locks that are currently held. 



**Returns:** the number of currently held recursive locks as an int32.



**Since:** BeOS R3

---

### `InitCheck()`

```cpp
status_t BLocker::InitCheck()const
```

Check whether the locker has properly initialized. 



**Returns:** A status code, `B_OK` if the semaphore has been properly initialized or any other error (negative) value related to semaphore initialization.



**Since:** Haiku R1

---

### `IsLocked()`

```cpp
bool BLocker::IsLocked(void)const
```

Check if the calling thread is actually holding the lock. 



**Returns:** Whether or not the calling thread is holding the lock.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The thread from which this method is called from is currently holding the lock. |
| false | The object is unlocked or the lock is held by another thread. |





**Since:** BeOS R3

---

### `Lock()`

```cpp
bool BLocker::Lock()
```

Add a lock request and block on it until we get it. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | Lock acquired successfully. |
| false | Failed to acquire the lock. Most probable cause is that the object is deleted. This frees the semaphore and releases the pending [Lock()](classBLocker.md#a42596788c0e5dca043987b2efad244bd) requests. |





**See also:** [LockWithTimeout(bigtime_t timeout)](classBLocker.md#a6da24e86f4acab13f674889b7bf8226e), [Unlock()](classBLocker.md#a0ebddc8ec0db8f51e57d6bff0f5ac2bf)



**Since:** BeOS R3


Referenced by [BAutolock::Lock()](classBAutolock.md#a5808a41f3c76294ed35deef3864c9a7c).

---

### `LockingThread()`

```cpp
thread_id BLocker::LockingThread(void)const
```

Return the `thread_id` of the thread that's currently holding the lock. 



**Since:** BeOS R3

---

### `LockWithTimeout()`

```cpp
status_t BLocker::LockWithTimeout(bigtime_t timeout)
```

Add a lock request and block until we get it or until it times out. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `timeout` | This is a timeout in microseconds (one millionth of a second) relative to now. |





**See also:** [Lock()](classBLocker.md#a42596788c0e5dca043987b2efad244bd), [Unlock()](classBLocker.md#a0ebddc8ec0db8f51e57d6bff0f5ac2bf)



**Since:** BeOS R3

---

### `Sem()`

```cpp
sem_id BLocker::Sem(void)const
```

Return the sem_id of the semaphore this object holds. 



> [!WARNING]
> Like any other internal objects that the Haiku API might expose, this semaphore id should in general be left alone. You should not use any of the public low-level semaphore functions on this semaphore, because it will harm the internal consistency of the object.



**Returns:** The sem_id of the semaphore this object holds.



**Since:** BeOS R3

---

### `Unlock()`

```cpp
void BLocker::Unlock(void)
```

Release the lock that's currently held. 



**Since:** BeOS R3


Referenced by [BAutolock::Unlock()](classBAutolock.md#a62e220b72b39ffa459b51dae1ca50332).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBLocker.html).
