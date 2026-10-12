---
name: BStringList
type: class
kit: support_kit
brief: "Undocumented class"
source: haiku-book
---

# BStringList Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Undocumented class. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BStringList](#a593dd3de7ab47baf6a06cc8a89b5b329) (const BStringList &other) — Undocumented public method.
* [BStringList](#a48e26a3eccda1dfaae86dfaf3918a46e) (int32 count=20) — Undocumented public method.
* `virtual` [~BStringList](#a248c9e06a87653aeb71f6b730cd63a15) () — Undocumented public method.
* `bool` [Add](#a6c8a2181c728e71019b7c076682eab4a) (const BString &string) — Undocumented public method.
* `bool` [Add](#aa0dcb67710fa09cbeeb9b8ed3235177b) (const BString &string, int32 index) — Undocumented public method.
* `bool` [Add](#a19e2aa6ab510e3e4eb57921e2e251a4b) (const BStringList &list) — Undocumented public method.
* `bool` [Add](#a93cf78d854b172a330b0d9a01673c786) (const BStringList &list, int32 index) — Undocumented public method.
* `virtual bool` [AllowsTypeCode](#ada0bef2ce78540984803c8cfa3967a6a) (type_code code) const — Undocumented public method.
* `int32` [CountStrings](#a8a8817f8eab19d3ca8d7ed55de806e76) () const — Undocumented public method.
* `void` [DoForEach](#aaa8a2ed6a1c660addd3015651286c51c) (bool(*func)(const BString &string)) — Undocumented public method.
* `void` [DoForEach](#aae0656773b8c991ae8095c01a731d530) (bool(*func)(const BString &string, void *arg2), void *arg2) — Undocumented public method.
* `BString` [First](#a46e61a1998607b89ee0916427dabb20f) () const — Undocumented public method.
* `virtual status_t` [Flatten](#a2950d106932743b78d006740557074fe) (void *buffer, ssize_t size) const — Undocumented public method.
* `virtual ssize_t` [FlattenedSize](#a58b7d9d1f5581d6e05537fb24abbb241) () const — Undocumented public method.
* `bool` [HasString](#a833ab51442b6bce8f9dd325fa944daa2) (const BString &string, bool ignoreCase=false) const — Undocumented public method.
* `int32` [IndexOf](#aab7a1be149515d5d4effde72973d1a9c) (const BString &string, bool ignoreCase=false) const — Undocumented public method.
* `bool` [IsEmpty](#a7128e31d57e788905c0cd65d4575a310) () const — Undocumented public method.
* `virtual bool` [IsFixedSize](#a27f621354797cf96fd55327d0dafdc2e) () const — Undocumented public method.
* `BString` [Join](#a445e5f698181a655e7c7a14d59266725) (const char *separator, int32 length=-1) const — Undocumented public method.
* `BString` [Last](#a0554ef82b22b339eb23b08a31ef31f5d) () const — Undocumented public method.
* `void` [MakeEmpty](#a44cc43cf1e78b0046c90e723005ce64c) () — Undocumented public method.
* `bool` [Move](#a04135c584e4b521679c3c380ac0bc6da) (int32 fromIndex, int32 toIndex) — Undocumented public method.
* `bool` [operator!=](#a0bc4fa7b7e5024c0918c0d3b26c4e86a) (const BStringList &other) const — Undocumented public method.
* `BStringList &` [operator=](#a80f5fb8ca605b3f10b605c8ed0a82bba) (const BStringList &other) — Undocumented public method.
* `bool` [operator==](#a6965c38ea06e1289105538e738802f0b) (const BStringList &other) const — Undocumented public method.
* `bool` [Remove](#a752dc1228eab9956b79f9f28425b2f93) (const BString &string, bool ignoreCase=false) — Undocumented public method.
* `bool` [Remove](#a0710481f1a753e5c3a90c4785b4e6d80) (const BStringList &list, bool ignoreCase=false) — Undocumented public method.
* `BString` [Remove](#a0249d816aaef64d5bdda32036b2f08da) (int32 index) — Undocumented public method.
* `bool` [Remove](#aeb9330c10fdeff2852de6df8b0856063) (int32 index, int32 count) — Undocumented public method.
* `bool` [Replace](#a11d0472fe2dbf1e833c5a94f0feab32c) (int32 index, const BString &string) — Undocumented public method.
* `void` [Sort](#a7e8e2ae78bd3e6b81e7e1eceb35b8deb) (bool ignoreCase=false) — Undocumented public method.
* `BString` [StringAt](#a4881b430738322707fc7ad8e95fbb1eb) (int32 index) const — Undocumented public method.
* `bool` [Swap](#a10497950b6769249ad23dc534173f934) (int32 indexA, int32 indexB) — Undocumented public method.
* `virtual type_code` [TypeCode](#aebe54b1791b65f0ea349f4fce771f0b9) () const — Undocumented public method.
* `virtual status_t` [Unflatten](#aaba64379fbd1a9fa334137c712a5e073) (type_code code, const void *buffer, ssize_t size) — Undocumented public method.
* `virtual` [~BFlattenable](#a884e130a5d27acc15b1e4e4c505157ff) () — Destructor. Does nothing.
* `virtual bool` [AllowsTypeCode](#a30165696bba76fed10e37508cc4f6925) (type_code code) const — Get whether or not the supplied type_code is supported.
* `virtual status_t` [Flatten](#ab934b64a8b218a4f9078ded191be6fbb) (void *buffer, ssize_t size) const =0 — Pure virtual that should flatten the object into the supplied buffer.
* `virtual ssize_t` [FlattenedSize](#a9b5885d4454326ca448438960ecff466) () const =0 — Pure virtual that should return the size of the flattened object in bytes.
* `virtual bool` [IsFixedSize](#ac019f502749a0cc78082f5ec7c8f5b56) () const =0 — Pure virtual that should return whether or not flattened objects of this type always have a fixed size.
* `virtual type_code` [TypeCode](#a819507fa1b0906f14299db15f6e990d1) () const =0 — Pure virtual that returns the type_code this class flattens to.
* `virtual status_t` [Unflatten](#a41e7168574912690be159991d2b07a97) (type_code code, const void *buffer, ssize_t size)=0 — Pure virtual that should unflatten the buffer and put the contents into the current object.

## Detailed Member Documentation

### `BStringList()`

```cpp
BStringList::BStringList(int32 count = 20)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `count` | Undocumented |





**Since:** Haiku R1

---

### `BStringList()`

```cpp
BStringList::BStringList(const BStringList & other)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Since:** Haiku R1

---

### `~BStringList()`

```cpp
BStringList::~BStringList()
```

Undocumented public method. 



**Since:** Haiku R1

---

### `Add()`

```cpp
bool BStringList::Add(const BString & string)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Add()`

```cpp
bool BStringList::Add(const BString & string, int32 index)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | Undocumented |
| `index` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Add()`

```cpp
bool BStringList::Add(const BStringList & list)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `list` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Add()`

```cpp
bool BStringList::Add(const BStringList & list, int32 index)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `list` | Undocumented |
| `index` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `AllowsTypeCode()`

```cpp
bool BStringList::AllowsTypeCode(type_code code)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `code` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Reimplemented from [BFlattenable](classBFlattenable.md#a30165696bba76fed10e37508cc4f6925).

---

### `CountStrings()`

```cpp
int32 BStringList::CountStrings()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `DoForEach()`

```cpp
void BStringList::DoForEach(bool(*)(const BString &string)func)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `func` | Undocumented |





**Since:** Haiku R1

---

### `DoForEach()`

```cpp
void BStringList::DoForEach(bool(*)(const BString &string, void *arg2)func, void * arg2)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `func` | Undocumented |
| `arg2` | Undocumented |





**Since:** Haiku R1

---

### `First()`

```cpp
BString BStringList::First()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Flatten()`

```cpp
status_t BStringList::Flatten(void * buffer, ssize_t size)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | Undocumented |
| `size` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Implements [BFlattenable](classBFlattenable.md#ab934b64a8b218a4f9078ded191be6fbb).

---

### `FlattenedSize()`

```cpp
ssize_t BStringList::FlattenedSize()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Implements [BFlattenable](classBFlattenable.md#a9b5885d4454326ca448438960ecff466).

---

### `HasString()`

```cpp
bool BStringList::HasString(const BString & string, bool ignoreCase = false)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | Undocumented |
| `ignoreCase` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [IndexOf()](classBStringList.md#aab7a1be149515d5d4effde72973d1a9c).

---

### `IndexOf()`

```cpp
int32 BStringList::IndexOf(const BString & string, bool ignoreCase = false)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | Undocumented |
| `ignoreCase` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Referenced by [HasString()](classBStringList.md#a833ab51442b6bce8f9dd325fa944daa2).

---

### `IsEmpty()`

```cpp
bool BStringList::IsEmpty()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `IsFixedSize()`

```cpp
bool BStringList::IsFixedSize()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Implements [BFlattenable](classBFlattenable.md#ac019f502749a0cc78082f5ec7c8f5b56).

---

### `Join()`

```cpp
BString BStringList::Join(const char * separator, int32 length = -1)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `separator` | Undocumented |
| `length` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Last()`

```cpp
BString BStringList::Last()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `MakeEmpty()`

```cpp
void BStringList::MakeEmpty()
```

Undocumented public method. 



**Since:** Haiku R1

---

### `Move()`

```cpp
bool BStringList::Move(int32 fromIndex, int32 toIndex)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `fromIndex` | Undocumented |
| `toIndex` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `operator!=()`

```cpp
bool BStringList::operator!=(const BStringList & other)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `operator=()`

```cpp
BStringList & BStringList::operator=(const BStringList & other)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `operator==()`

```cpp
bool BStringList::operator==(const BStringList & other)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Remove()`

```cpp
bool BStringList::Remove(const BString & string, bool ignoreCase = false)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | Undocumented |
| `ignoreCase` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Remove()`

```cpp
bool BStringList::Remove(const BStringList & list, bool ignoreCase = false)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `list` | Undocumented |
| `ignoreCase` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Remove()`

```cpp
BString BStringList::Remove(int32 index)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Remove()`

```cpp
bool BStringList::Remove(int32 index, int32 count)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | Undocumented |
| `count` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Replace()`

```cpp
bool BStringList::Replace(int32 index, const BString & string)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | Undocumented |
| `string` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Sort()`

```cpp
void BStringList::Sort(bool ignoreCase = false)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ignoreCase` | Undocumented |





**Since:** Haiku R1

---

### `StringAt()`

```cpp
BString BStringList::StringAt(int32 index)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Swap()`

```cpp
bool BStringList::Swap(int32 indexA, int32 indexB)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `indexA` | Undocumented |
| `indexB` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `TypeCode()`

```cpp
type_code BStringList::TypeCode()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Implements [BFlattenable](classBFlattenable.md#a819507fa1b0906f14299db15f6e990d1).

---

### `Unflatten()`

```cpp
status_t BStringList::Unflatten(type_code code, const void * buffer, ssize_t size)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `code` | Undocumented |
| `buffer` | Undocumented |
| `size` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Implements [BFlattenable](classBFlattenable.md#a41e7168574912690be159991d2b07a97).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBStringList.html).
