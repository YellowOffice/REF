---
name: Global functions
type: topic
kit: support_kit
source: haiku-book
---

# Global functions
**Kit/Group:** [Support Kit](../support_kit/group__support.md)

## Member List

### Typedefs

* `typedef BArchivable *(*` [instantiation_func](#gac69340ddd30c80ddaf1878c84491cc86)) (BMessage *) — Internal definition of a function that can instantiate objects that have been created with the BArchivable API.

### Functions

* `status_t` [add_system_beep_event](#gab1527bdd01873399ce1cab5257deb523) (const char *eventName, uint32 flags=0) — Adds an event to the media server.
* `int32` [atomic_add](#ga8a7c9722b2dcc2d6a92da0d8e6809390) (int32 *value, int32 addValue) — Atomically add the value of addValue to value.
* `int64` [atomic_add64](#ga3cc98e39c62b37089aa6ce270244f636) (int64 *value, int64 addValue) — Atomically add the value of addValue to value.
* `int32` [atomic_and](#gac0f5dbcaa491161a6ab6f16ac1c1bca3) (int32 *value, int32 andValue) — Atomically perform a bitwise AND operation of andValue to the variable andValue.
* `int64` [atomic_and64](#ga2ffe7f5af9390fa80744a35be7796177) (int64 *value, int64 andValue) — Atomically perform a bitwise AND operation of andValue to the variable andValue.
* `int32` [atomic_get](#ga61648da3ddc2f3df3c0b08b14b5dd09e) (int32 *value) — Atomically return the value of value.
* `int64` [atomic_get64](#gae15a75fb3937e2497baf8989cf6206af) (int64 *value) — Atomically return the value of value.
* `int32` [atomic_get_and_set](#ga07b69379f20df5cfc6a7506a69364d80) (int32 *value, int32 newValue) — Atomically set the variable value to newvalue and return the old value.
* `int64` [atomic_get_and_set64](#gaa28eab35df67e1b51685340a00c61484) (int64 *value, int64 newValue) — Atomically set the variable value to newvalue and return the old value.
* `int32` [atomic_or](#ga7ea6205f09f65652dd5b35987e570a20) (int32 *value, int32 orValue) — Atomically perform a bitwise OR operation of orValue to the variable andValue.
* `int64` [atomic_or64](#ga58bc6786c1eab83a64b31bdb44db5634) (int64 *value, int64 orValue) — Atomically perform a bitwise OR operation of orValue to the variable andValue.
* `void` [atomic_set](#gad6d9cc999081f5f54afe500b8ab22a31) (int32 *value, int32 newValue) — Atomically set the variable value to newvalue.
* `void` [atomic_set64](#ga90492800f50ed0520d6b82408436b551) (int64 *value, int64 newValue) — Atomically set the variable value to newvalue.
* `int32` [atomic_test_and_set](#gad5e8491539af69445d3eaea7818166e4) (int32 *value, int32 newValue, int32 testAgainst) — Atomically set the variable value to newValue if the current value is testAgainst.
* `int64` [atomic_test_and_set64](#ga18987c30eda4e56c0111528af4dd8d9c) (int64 *value, int64 newValue, int64 testAgainst) — Atomically set the variable value to newValue if the current value is testAgainst.
* `status_t` [beep](#gac178267cc77532b134ff7ee34c99d6e1) () — Invoke the standard system beep to alert users.
* `int` [Compare](#ga4ed93281e1f1459821c6f41dbc81499c) (const BString &a, const BString &b) — Lexicographically compare two strings.
* `int` [Compare](#gaa845691f971dbf61ff57ba6d86aa2df1) (const BString *a, const BString *b) — Lexicographically compare two strings.
* `instantiation_func` [find_instantiation_func](#ga43c75713eb3ac57b46018dab24ed1a11) (BMessage *archive) — Internal function that searches for the instantiation func that works on the specified archive. Use instantiate_object() instead.
* `instantiation_func` [find_instantiation_func](#gae4cdf523a00d2b6ca0f3e8bc5f28ef51) (const char *className) — Internal function that searches for the instantiation func of a specific class. Use instantiate_object() instead.
* `instantiation_func` [find_instantiation_func](#ga222db6ff576bd53ba4f54d356992d621) (const char *className, const char *signature) — Internal function that searches for the instantiation func with a specific signature. Use instantiate_object() instead.
* `int` [ICompare](#ga7e131707bf6c4a0481647e5a84b6e4a0) (const BString &a, const BString &b) — Lexicographically compare two strings case-insensitively.
* `int` [ICompare](#ga00dfffa0c89a6c24dedd0176782e53bf) (const BString *a, const BString *b) — Lexicographically compare two strings case-insensitively.
* `BArchivable *` [instantiate_object](#ga1ad60dbee75973620a85b2559e02d62d) (BMessage *from) — Instantiate an archived object.
* `BArchivable *` [instantiate_object](#gac98d3af4a84cd0880d8a853f7c526764) (BMessage *from, image_id *id) — Instantiate an archived object with the object being defined in a different application or library.
* `bool` [operator!=](#gad38636cf059e2166e653b1ff257526ba) (const char *a, const BString &b) — Lexicographically compare if a is not equal to given BString b.
* `bool` [operator<](#gaf9da661b62e03cf779fcf99831bde205) (const char *a, const BString &b) — Lexicographically compare if a is less than the given BString b.
* `bool` [operator<=](#gabc5ffd2bede5b8fb0f41ad273b10485b) (const char *a, const BString &b) — Lexicographically compare if a is less than or equal to a given BString b.
* `bool` [operator==](#gafc658fa3946745858aad13c8589c7065) (const char *a, const BString &b) — Lexicographically compare if a is equal to a given BString b.
* `bool` [operator>](#ga79515be2058ee0aade9eb39fe8114dde) (const char *a, const BString &b) — Lexicographically compare if a is greater than a given BString b.
* `bool` [operator>=](#ga7840009be7074a1fbff9e1c89742bf3a) (const char *a, const BString &b) — Lexicographically compare if a is greater than or equal to a given BString b.
* `status_t` [system_beep](#gadd6488e3357ba3dfb3a8217db6cfc67d) (const char *eventName) — Invokes the sound for event eventName.
* `bool` [validate_instantiation](#gae5dd9c83f4d3ab639edd84deb6bfd1c5) (BMessage *from, const char *className) — Internal function that checks if the className is the same as the one stored in the from message.

## Detailed Member Documentation

### `instantiation_func`

```cpp
typedef BArchivable *(* instantiation_func)(BMessage *)
```

Internal definition of a function that can instantiate objects that have been created with the [BArchivable](classBArchivable.md) API. 



**Since:** BeOS R3

---

### `add_system_beep_event()`

```cpp
status_t add_system_beep_event(const char * eventName, uint32 flags = 0)
```

Adds an event to the media server. 


Call this method to add a specific event to the media server. From [Beep.h](Beep_8h.md) and in libbe.so.


Parameters

| Parameter | Description |
| :--- | :--- |
| `eventName` | The name of the event. |
| `flags` | Currently unused. Pass `0`. |





**Since:** BeOS R5

---

### `atomic_add()`

```cpp
int32 atomic_add(int32 * value, int32 addValue)
```

Atomically add the value of *addValue* to *value*. 


This is a thread-safe way of performing the `*value` `+=` `addValue` operation. You should use these function when two or more threads might access the variable simultaneously. You don't have to use a semaphore or a mutex in this case.



**Returns:** The original value of `value`.



**See also:** [atomic_add64()](group__support__globals.md#ga3cc98e39c62b37089aa6ce270244f636) for a version that works on `long` `long`.



**Since:** BeOS R3

---

### `atomic_add64()`

```cpp
int64 atomic_add64(int64 * value, int64 addValue)
```

Atomically add the value of *addValue* to *value*. 


This is a thread-safe way of performing the `*value` `+=` `addValue` operation. You should use these function when two or more threads might access the variable simultaneously. You don't have to use a semaphore or a mutex in this case.



**Returns:** The original value of `value`.



**See also:** [atomic_add()](group__support__globals.md#ga8a7c9722b2dcc2d6a92da0d8e6809390) for a version that works on an `int32`.



**Since:** Haiku R1

---

### `atomic_and()`

```cpp
int32 atomic_and(int32 * value, int32 andValue)
```

Atomically perform a bitwise AND operation of *andValue* to the variable *andValue*. 


This is a thread-safe way of performing the `*value` `&=` `andValue` operation. You should use these function when two or more threads might access the variable simultaneously. You don't have to use a semaphore or a mutex in this case.



**Returns:** The original value of `value`.



**See also:** [atomic_and64()](group__support__globals.md#ga2ffe7f5af9390fa80744a35be7796177) for a version that works on `long` `long`.



**Since:** BeOS R3

---

### `atomic_and64()`

```cpp
int64 atomic_and64(int64 * value, int64 andValue)
```

Atomically perform a bitwise AND operation of *andValue* to the variable *andValue*. 


This is a thread-safe way of performing the `*value` `&=` `andValue` operation. You should use these function when two or more threads might access the variable simultaneously. You don't have to use a semaphore or a mutex in this case.



**Returns:** The original value of `value`.



**See also:** [atomic_and()](group__support__globals.md#gac0f5dbcaa491161a6ab6f16ac1c1bca3) for a version that works on an `int32`.



**Since:** Haiku R1

---

### `atomic_get()`

```cpp
int32 atomic_get(int32 * value)
```

Atomically return the value of `value`. 


This is a thread-safe way of reading the contents of the `value` operation. You should use these function when two or more threads might access the variable simultaneously. You don't have to use a semaphore or a mutex in this case. The variable must be naturally aligned.



**Returns:** The original value of `value`.



**See also:** [atomic_get64()](group__support__globals.md#gae15a75fb3937e2497baf8989cf6206af) for a version that works on `long` `long`.



**Since:** Haiku R1


Referenced by [BReferenceable::CountReferences()](classBReferenceable.md#a2ffe8211f9390cb6b83f0fc86824a3a1), and [ConditionVariable::EntriesCount()](../unknown_kit/structConditionVariable.md#a8f9e5c13b0735859d76eec224ef8061e).

---

### `atomic_get64()`

```cpp
int64 atomic_get64(int64 * value)
```

Atomically return the value of `value`. 


This is a thread-safe way of reading the contents of the `value` operation. You should use these function when two or more threads might access the variable simultaneously. You don't have to use a semaphore or a mutex in this case. The variable must be naturally aligned.



**Returns:** The original value of `value`.



**See also:** [atomic_get()](group__support__globals.md#ga61648da3ddc2f3df3c0b08b14b5dd09e) for a version that works on an `int32`.



**Since:** Haiku R1

---

### `atomic_get_and_set()`

```cpp
int32 atomic_get_and_set(int32 * value, int32 newValue)
```

Atomically set the variable *value* to *newvalue* and return the old value. 


This is a thread-safe way of performing the `*value` `=` `newValue` operation. You should use these function when two or more threads might access the variable simultaneously. You don't have to use a semaphore or a mutex in this case.



**Returns:** The original value of `value`.



**See also:** [atomic_get_and_set64()](group__support__globals.md#gaa28eab35df67e1b51685340a00c61484) for a version that works on `long` `long`.



**Since:** Haiku R1

---

### `atomic_get_and_set64()`

```cpp
int64 atomic_get_and_set64(int64 * value, int64 newValue)
```

Atomically set the variable *value* to *newvalue* and return the old value. 


This is a thread-safe way of performing the `*value` `=` `newValue` operation. You should use these function when two or more threads might access the variable simultaneously. You don't have to use a semaphore or a mutex in this case.



**Returns:** The original value of `value`.



**See also:** [atomic_get_and_set()](group__support__globals.md#ga07b69379f20df5cfc6a7506a69364d80) for a version that works on an `int32`.



**Since:** Haiku R1

---

### `atomic_or()`

```cpp
int32 atomic_or(int32 * value, int32 orValue)
```

Atomically perform a bitwise OR operation of *orValue* to the variable *andValue*. 


This is a thread-safe way of performing the `*value` ``|= `orValue` operation. You should use these function when two or more threads might access the variable simultaneously. You don't have to use a semaphore or a mutex in this case.



**Returns:** The original value of `value`.



**See also:** [atomic_or64()](group__support__globals.md#ga58bc6786c1eab83a64b31bdb44db5634) for a version that works on `long` `long`.



**Since:** BeOS R3

---

### `atomic_or64()`

```cpp
int64 atomic_or64(int64 * value, int64 orValue)
```

Atomically perform a bitwise OR operation of *orValue* to the variable *andValue*. 


This is a thread-safe way of performing the `*value` ``|= `orValue` operation. You should use these function when two or more threads might access the variable simultaneously. You don't have to use a semaphore or a mutex in this case.



**Returns:** The original value of `value`.



**See also:** [atomic_or()](group__support__globals.md#ga7ea6205f09f65652dd5b35987e570a20) for a version that works on an `int32`.



**Since:** Haiku R1

---

### `atomic_set()`

```cpp
void atomic_set(int32 * value, int32 newValue)
```

Atomically set the variable *value* to *newvalue*. 


This is a thread-safe way of performing the `*value` `=` `newValue` operation. You should use these function when two or more threads might access the variable simultaneously. You don't have to use a semaphore or a mutex in this case. The variable must be naturally aligned.



**See also:** [atomic_set64()](group__support__globals.md#ga90492800f50ed0520d6b82408436b551) for a version that works on `long` `long`.



**Since:** Haiku R1

---

### `atomic_set64()`

```cpp
void atomic_set64(int64 * value, int64 newValue)
```

Atomically set the variable *value* to *newvalue*. 


This is a thread-safe way of performing the `*value` `=` `newValue` operation. You should use these function when two or more threads might access the variable simultaneously. You don't have to use a semaphore or a mutex in this case. The variable must be naturally aligned.



**See also:** [atomic_set()](group__support__globals.md#gad6d9cc999081f5f54afe500b8ab22a31) for a version that works on an `int32`.



**Since:** Haiku R1

---

### `atomic_test_and_set()`

```cpp
int32 atomic_test_and_set(int32 * value, int32 newValue, int32 testAgainst)
```

Atomically set the variable *value* to *newValue* if the current value is *testAgainst*. 


This is a thread-safe way of conditionally performing the `*value` `+=` `newValue` operation. You should use these function when two or more threads might access the variable simultaneously. You don't have to use a semaphore or a mutex in this case.



**Returns:** The original value of `value`.



**See also:** [atomic_test_and_set64()](group__support__globals.md#ga18987c30eda4e56c0111528af4dd8d9c) for a version that works on `long` `long`.



**Since:** Haiku R1

---

### `atomic_test_and_set64()`

```cpp
int64 atomic_test_and_set64(int64 * value, int64 newValue, int64 testAgainst)
```

Atomically set the variable *value* to *newValue* if the current value is *testAgainst*. 


This is a thread-safe way of conditionally performing the `*value` `+=` `newValue` operation. You should use these function when two or more threads might access the variable simultaneously. You don't have to use a semaphore or a mutex in this case.



**Returns:** The original value of `value`.



**See also:** [atomic_test_and_set()](group__support__globals.md#gad5e8491539af69445d3eaea7818166e4) for a version that works on an `int32`.



**Since:** Haiku R1

---

### `beep()`

```cpp
status_t beep()
```

Invoke the standard system beep to alert users. 


From [Beep.h](Beep_8h.md) and in libbe.so.



**See also:** [system_beep()](group__support__globals.md#gadd6488e3357ba3dfb3a8217db6cfc67d) and [add_system_beep_event()](group__support__globals.md#gab1527bdd01873399ce1cab5257deb523)



**Since:** BeOS R3

---

### `Compare()`

```cpp
int Compare(const BString & a, const BString & b)
```

Lexicographically compare two strings. 


This function is useful if you need a global compare function to feed to [BList::SortItems()](classBList.md#abe55aa005c16d47128365775b7aee021).


Parameters

| Parameter | Description |
| :--- | :--- |
| `a` | The first string to compare. |
| `b` | The second string to compare. |




From [String.h](String_8h.md) and in libbe.so.



**Returns:** An int representing the strings relationship to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| >0 | *a* sorts lexicographically after *b*. |
| =0 | *a* is equal to *b*. |
| <0 | *a* sorts lexicographically before *b*. |





**See also:** [BString::Compare(const BString&) const](classBString.md#a58a9b35feb85f415771c9270d01c1951)



**Since:** BeOS R5

---

### `Compare()`

```cpp
int Compare(const BString * a, const BString * b)
```

Lexicographically compare two strings. 


This function is useful if you need a global compare function to feed to [BList::SortItems()](classBList.md#abe55aa005c16d47128365775b7aee021).


From [String.h](String_8h.md) and in libbe.so.


Parameters

| Parameter | Description |
| :--- | :--- |
| `a` | The first string to compare. |
| `b` | The second string to compare. |





**Returns:** An int representing the strings relationship to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| >0 | *a* sorts lexicographically after *b*. |
| =0 | *a* is equal to *b*. |
| <0 | *a* sorts lexicographically before *b*. |





**See also:** [BString::Compare(const BString&) const](classBString.md#a58a9b35feb85f415771c9270d01c1951)



**Since:** BeOS R5

---

### `find_instantiation_func()`

```cpp
instantiation_func find_instantiation_func(BMessage * archive)
```

Internal function that searches for the instantiation func that works on the specified *archive*. Use [instantiate_object()](group__support__globals.md#gac98d3af4a84cd0880d8a853f7c526764) instead. 



**Since:** BeOS R3

---

### `find_instantiation_func()`

```cpp
instantiation_func find_instantiation_func(const char * className)
```

Internal function that searches for the instantiation func of a specific class. Use [instantiate_object()](group__support__globals.md#gac98d3af4a84cd0880d8a853f7c526764) instead. 



**Since:** BeOS R3

---

### `find_instantiation_func()`

```cpp
instantiation_func find_instantiation_func(const char * className, const char * signature)
```

Internal function that searches for the instantiation func with a specific signature. Use [instantiate_object()](group__support__globals.md#gac98d3af4a84cd0880d8a853f7c526764) instead. 



**Since:** Haiku R1

---

### `ICompare()`

```cpp
int ICompare(const BString & a, const BString & b)
```

Lexicographically compare two strings case-insensitively. 


This function is useful if you need a global compare function to feed to [BList::SortItems()](classBList.md#abe55aa005c16d47128365775b7aee021).


From [String.h](String_8h.md) and in libbe.so.


Parameters

| Parameter | Description |
| :--- | :--- |
| `a` | The first string to compare. |
| `b` | The second string to compare. |





**Returns:** An int representing the strings relationship to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| >0 | *a* sorts lexicographically after *b*. |
| =0 | *a* is equal to *b*. |
| <0 | *a* sorts lexicographically before *b*. |





**See also:** [BString::Compare(const BString&) const](classBString.md#a58a9b35feb85f415771c9270d01c1951)



**Since:** BeOS R5

---

### `ICompare()`

```cpp
int ICompare(const BString * a, const BString * b)
```

Lexicographically compare two strings case-insensitively. 


This function is useful if you need a global compare function to feed to [BList::SortItems()](classBList.md#abe55aa005c16d47128365775b7aee021).


From [String.h](String_8h.md) and in libbe.so.


Parameters

| Parameter | Description |
| :--- | :--- |
| `a` | The first string to compare. |
| `b` | The second string to compare. |





**Returns:** An int representing the strings relationship to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| >0 | *a* sorts lexicographically after *b*. |
| =0 | *a* is equal to *b*. |
| <0 | *a* sorts lexicographically before *b*. |





**See also:** [BString::Compare(const BString&) const](classBString.md#a58a9b35feb85f415771c9270d01c1951)



**Since:** BeOS R5

---

### `instantiate_object()`

```cpp
BArchivable * instantiate_object(BMessage * from)
```

Instantiate an archived object. 


This global function will determine the base class, based on the *from* argument, and it will call the Instantiate() function of that object to restore it.


Parameters

| Parameter | Description |
| :--- | :--- |
| `from` | The archived object. |





**Returns:** The object returns a pointer to the instantiated object, or `NULL` if the instantiation failed. The global `errno` variable will contain the reason why it failed.



**See also:** [instantiate_object(BMessage *from, image_id *id)](group__support__globals.md#gac98d3af4a84cd0880d8a853f7c526764)



**Since:** BeOS R3

---

### `instantiate_object()`

```cpp
BArchivable * instantiate_object(BMessage * from, image_id * id)
```

Instantiate an archived object with the object being defined in a different application or library. 


This function is similar to [instantiate_object(BMessage *from)](group__support__globals.md#ga1ad60dbee75973620a85b2559e02d62d), except that it takes the *id* argument referring to an image where the object might be stored.



> [!NOTE]
> Images are names for executable files. Image id's refer to these executable files that have been loaded by your application. Have a look at the kernel API for further information.



**Since:** BeOS R3

---

### `operator!=()`

```cpp
bool operator!=(const char * a, const BString & b)
```

Lexicographically compare if `a` is not equal to given [BString](classBString.md) *b*. 


From [String.h](String_8h.md) and in libbe.so.


Parameters

| Parameter | Description |
| :--- | :--- |
| `a` | The first string to compare. |
| `b` | The second string to compare. |





**Returns:** `true` if *a* is NOT equal to *b*, `false` otherwise.



**See also:** [BString::operator!=(const char*) const](classBString.md#a68a2d28b93ee8348163a320bb1054b22)



**Since:** BeOS R5

---

### `operator<()`

```cpp
bool operator<(const char * a, const BString & b)
```

Lexicographically compare if `a` is less than the given [BString](classBString.md) *b*. 


From [String.h](String_8h.md) and in libbe.so.


Parameters

| Parameter | Description |
| :--- | :--- |
| `a` | The first string to compare. |
| `b` | The second string to compare. |





**Returns:** `true` if *a* is less than *b*, `false` otherwise.



**See also:** [BString::operator<(const char*) const](classBString.md#aa6886f45135f335ed05f002bd19f842d)



**Since:** BeOS R5

---

### `operator<=()`

```cpp
bool operator<=(const char * a, const BString & b)
```

Lexicographically compare if `a` is less than or equal to a given [BString](classBString.md) *b*. 


From [String.h](String_8h.md) and in libbe.so.


Parameters

| Parameter | Description |
| :--- | :--- |
| `a` | The first string to compare. |
| `b` | The second string to compare. |





**Returns:** `true` if *a* is less than or equal to *b*, `false` otherwise.



**See also:** [BString::operator<=(const char*) const](classBString.md#a7c660e1dd749f068967cfb0f900bd96d)



**Since:** BeOS R5

---

### `operator==()`

```cpp
bool operator==(const char * a, const BString & b)
```

Lexicographically compare if `a` is equal to a given [BString](classBString.md) *b*. 


From [String.h](String_8h.md) and in libbe.so.


Parameters

| Parameter | Description |
| :--- | :--- |
| `a` | The first string to compare. |
| `b` | The second string to compare. |





**See also:** [BString::operator==(const char*) const](classBString.md#a67138abea38871ddb5dfc8646a1676f3)



**Returns:** `true` if *a* is equal to *b*, `false` otherwise.



**Since:** BeOS R5

---

### `operator>()`

```cpp
bool operator>(const char * a, const BString & b)
```

Lexicographically compare if `a` is greater than a given [BString](classBString.md) *b*. 


From [String.h](String_8h.md) and in libbe.so.


Parameters

| Parameter | Description |
| :--- | :--- |
| `a` | The first string to compare. |
| `b` | The second string to compare. |





**See also:** [BString::operator>(const char*) const](classBString.md#af7bb77100b7103935c0b325b7666e3fa)



**Returns:** `true` if *a* is greater than *b*, `false` otherwise.



**Since:** BeOS R5

---

### `operator>=()`

```cpp
bool operator>=(const char * a, const BString & b)
```

Lexicographically compare if `a` is greater than or equal to a given [BString](classBString.md) *b*. 


From [String.h](String_8h.md) and in libbe.so.


Parameters

| Parameter | Description |
| :--- | :--- |
| `a` | The first string to compare. |
| `b` | The second string to compare. |





**Returns:** `true` if *a* is greater than or equal to *b*, `false` otherwise.



**See also:** [BString::operator>=(const char*) const](classBString.md#acc3c2882848a1bcd43c37fb1a44e7665)



**Since:** BeOS R5

---

### `system_beep()`

```cpp
status_t system_beep(const char * eventName)
```

Invokes the sound for event *eventName*. 


You can add the events using [add_system_beep_event()](group__support__globals.md#gab1527bdd01873399ce1cab5257deb523). From [Beep.h](Beep_8h.md) and in libbe.so.



**Since:** BeOS R5

---

### `validate_instantiation()`

```cpp
bool validate_instantiation(BMessage * from, const char * className)
```

Internal function that checks if the *className* is the same as the one stored in the *from* message. 



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/group__support__globals.html).
