---
name: BAutolock
type: class
kit: support_kit
brief: "Convenient utility to make parts of your code thread-safe easily"
source: haiku-book
---

# BAutolock Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Convenient utility to make parts of your code thread-safe easily. 


The autolocker uses a [BLooper](../application_kit/classBLooper.md) or a [BLocker](classBLocker.md) in order to protect a part of your code. This class is usually used in combination with a [BLocker](classBLocker.md) that protects a certain part of your code and data that are being accessed by multiple threads. While [BAutolock](classBAutolock.md) does not add any features to locking, it provides a mechanism to easily lock and protect a part of your code.


Normally, when you need to protect data, you would have to make sure that all your locks are paired with unlocks. Below is a simple example, but you can imagine that there are more complex situations where you might spend a lot of time debugging a hang because you didn't pair all the [Lock()](classBAutolock.md#a5808a41f3c76294ed35deef3864c9a7c)s with an [Unlock()](classBAutolock.md#a62e220b72b39ffa459b51dae1ca50332). See the example:



```cpp
status_t
Receiver::HandleCall(Call *call)
{
    ... work on call data ...
 
    fDataLocker->Lock()
 
    ... perform changes ...
 
 if (!success) {
      fDataLocker->Unlock();
 return B_ERROR;
    }
 
    fDataLocker->Unlock()
 
 return B_OK;
}
```

 With the [BAutolock](classBAutolock.md) this example can be rewritten as follows:



```cpp
status_t
Receiver::HandleCall(Call *call)
{
    ... work on call data ...
 
 BAutolock autolock(fDataLocker);
 
    ... perform changes ...
 
 if (!success)
 return B_ERROR;
 
 return B_OK;
}
```

Since the object is created on stack, it is destroyed as soon as we leave the function. Because the destruction of the object causes it to unlock the [BLocker](classBLocker.md) or [BLooper](../application_kit/classBLooper.md), you don't have to manually make sure that every exit from the function is properly unlocked.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BAutolock](#a28e4047538936e011cde19d4815756e5) (BLocker &locker) — Create an object and lock the BLocker.
* [BAutolock](#a3a64bb8f598284952f9c07c5f551b914) (BLocker *locker) — Create an object and lock the BLocker.
* [BAutolock](#a233e8c62e49a70b4b3708c2327d2bc16) (BLooper *looper) — Create an object and lock the BLooper.
* [~BAutolock](#a85fc5fd8722878d78f35eee797143e69) () — Destroy the object and unlock the associated BLocker or BLooper.
* `bool` [IsLocked](#a271307ad7bf96be725f315d62a8739cb) () — Verify whether the associated BLocker or BLooper are actually locked.
* `bool` [Lock](#a5808a41f3c76294ed35deef3864c9a7c) () — Lock the BAutolock if it has not already happened.
* `void` [Unlock](#a62e220b72b39ffa459b51dae1ca50332) () — Unlock the BAutolock if the lock is being held.

## Detailed Member Documentation

### `BAutolock()`

```cpp
BAutolock::BAutolock(BLooper * looper)
```

Create an object and lock the [BLooper](../application_kit/classBLooper.md). 



**Since:** BeOS R3

---

### `BAutolock()`

```cpp
BAutolock::BAutolock(BLocker * locker)
```

Create an object and lock the [BLocker](classBLocker.md). 



**Since:** BeOS R3

---

### `BAutolock()`

```cpp
BAutolock::BAutolock(BLocker & locker)
```

Create an object and lock the [BLocker](classBLocker.md). 



**Since:** BeOS R3

---

### `~BAutolock()`

```cpp
BAutolock::~BAutolock()
```

Destroy the object and unlock the associated [BLocker](classBLocker.md) or [BLooper](../application_kit/classBLooper.md). 



**Since:** BeOS R3


References [Unlock()](classBAutolock.md#a62e220b72b39ffa459b51dae1ca50332).

---

### `IsLocked()`

```cpp
bool BAutolock::IsLocked()
```

Verify whether the associated [BLocker](classBLocker.md) or [BLooper](../application_kit/classBLooper.md) are actually locked. 


Basically you may assume that when the object is created, you are almost always sure the actual locking succeeds. It might fail if the [BLocker](classBLocker.md) or [BLooper](../application_kit/classBLooper.md) are destroyed though. The semaphore will be released and the [Lock()](classBAutolock.md#a5808a41f3c76294ed35deef3864c9a7c) call will fail.


If you expect this to happen, you can use this method to help you protect yourself from any harm.



**Returns:** Whether or not the [BLocker](classBLocker.md) or [BLooper](../application_kit/classBLooper.md) is locked.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The lock was acquired. |
| false | Failed to acquire the lock. |





**Since:** BeOS R3

---

### `Lock()`

```cpp
bool BAutolock::Lock()
```

Lock the [BAutolock](classBAutolock.md) if it has not already happened. 


Note that unlike [BLocker](classBLocker.md), the object is not locked with lock count. That means that if the lock is already taken, this method returns `true` without any action.



**Returns:** Whether or not the [BLocker](classBLocker.md) or [BLooper](../application_kit/classBLooper.md) was locked.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The lock was acquired (or had already been acquired). |
| false | Failed to acquire the lock. |





**Since:** Haiku R1


References [BLooper::Lock()](../application_kit/classBLooper.md#a757a3e406ea3b7bb9a1ad16d04689b1d), [BLocker::Lock()](classBLocker.md#a42596788c0e5dca043987b2efad244bd), and [NULL](SupportDefs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4).

---

### `Unlock()`

```cpp
void BAutolock::Unlock()
```

Unlock the [BAutolock](classBAutolock.md) if the lock is being held. 


If the lock is not held, the method does nothing.



**Since:** Haiku R1


References [NULL](SupportDefs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), [BLooper::Unlock()](../application_kit/classBLooper.md#ac84ea15405640082b9fda58f6672467c), and [BLocker::Unlock()](classBLocker.md#a0ebddc8ec0db8f51e57d6bff0f5ac2bf).


Referenced by [~BAutolock()](classBAutolock.md#a85fc5fd8722878d78f35eee797143e69).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBAutolock.html).
