---
name: BUnarchiver
type: class
kit: support_kit
brief: "A class that simplifies the unarchiving of complicated BArchivable hierarchies"
source: haiku-book
---

# BUnarchiver Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A class that simplifies the unarchiving of complicated [BArchivable](classBArchivable.md) hierarchies. 


The [BUnarchiver](classBUnarchiver.md) class is a small class used to recover [BArchivable](classBArchivable.md) objects that have been archived with the [BArchiver](classBArchiver.md) class. It also provides ownership semantics, so that memory leaks can be avoided during the unarchival process. When retrieving an object (either via [GetObject()](classBUnarchiver.md#a60bc2e909dbdc0b9a786e073dc56e9d7) or [FindObject()](classBUnarchiver.md#ad64f70e03bc7b9c202eec4d5d07d075e)), you can specify a [BUnarchiver::ownership_policy](classBUnarchiver.md#ac1a5a14b2ae797c7f051dc44e725d640). If you specify [BUnarchiver::B_ASSUME_OWNERSHIP](classBUnarchiver.md#ac1a5a14b2ae797c7f051dc44e725d640a915cee940a254f586f0fc83402dcd4d4), you will become responsible for deleting the retrieved item. If you specify [BUnarchiver::B_DONT_ASSUME_OWNERSHIP](classBUnarchiver.md#ac1a5a14b2ae797c7f051dc44e725d640a4cc389b871e531d4f05c9d72e641b7e3), you will not become responsible. You cannot take ownership of the same object twice. After the unarchival process finishes, any unclaimed objects, excluding the root object (the object being instantiated via [instantiate_object()](group__support__globals.md#gac98d3af4a84cd0880d8a853f7c526764) or [BUnarchiver::InstantiateObject()](classBUnarchiver.md#a3bf0c1cbca1644015d17850424d0c374)), will be deleted.


If you are updating a class that previously did not use the [BArchiver](classBArchiver.md) and [BUnarchiver](classBUnarchiver.md) helper classes, and want to maintain backwards compatibility with old archive, this can be done using the [IsArchiveManaged()](classBUnarchiver.md#af5a80d3440ee8d7b1ce7055157fef814) method.



> [!WARNING]
> Calling methods on your [BUnarchiver](classBUnarchiver.md) with a legacy archive (one that was not managed by a [BArchiver](classBArchiver.md) during archival) will result in a call to debugger().



**Since:** Haiku R1

## Member List

### Public Types

* `enum` [ownership_policy](#ac1a5a14b2ae797c7f051dc44e725d640) { 
  B_ASSUME_OWNERSHIP
, 
  B_DONT_ASSUME_OWNERSHIP

 } — Options for the ownership policy of objects retrieved from BUnarchiver.

### Public Member Functions

* [BUnarchiver](#ac01e05c6da11e90d27808dcd30cf9120) (const BMessage *archive) — Constructs a BUnarchiver object to manage archive.
* [~BUnarchiver](#a3476736967aaed6de3cd21cb00a91496) () — Destroys a BUnarchiver object.
* `const BMessage *` [ArchiveMessage](#a9ac2b68a35e07a5e831a9fe4714c2f9c) () const — Returns the BMessage* used to construct this BUnarchiver.
* `void` [AssumeOwnership](#aeac457088aaae9dabced13103b8c4205) (BArchivable *archivable) — Become the owner of archivable.
* `status_t` [EnsureUnarchived](#af2a3f90c5405356b8f9588dcec99d61e) (const char *name, int32 index=0) — Ensure the object archived under name at index is unarchived and instantiated.
* `status_t` [EnsureUnarchived](#a265dcb1cfd3cb185deb80c0fb0836613) (int32 token) — Ensure the object represented by token is unarchived and instantiated.
* 
*  — Recover an object that had previously been archived using the BArchiver::AddArchivable() method.
* 
*  — Recover and take ownership of an object that had previously been archived using the BArchiver::AddArchivable() method.
* 
*  — Recover an object at index 0 that had previously been archived using the BArchiver::AddArchivable() method.
* 
*  — Recover and take ownership of an object at index 0 that had previously been archived using the BArchiver::AddArchivable() method.
* `status_t` [Finish](#a7640fa5d84dc6dca19d7513326d2bba2) (status_t err=B_OK) — Report any unarchiving errors and possibly complete the archiving session.
* 
*  — Recover an object by token that was archived by a BArchiver object. If the object has not yet been instantiated, and this request is not coming from an AllUnarchived() implementation, the object will be instantiated now.
* 
*  — Recover and take ownership of an object represented by token.
* `bool` [IsInstantiated](#ad497bb9f706e1147c197827b66e914ac) (const char *name, int32 index=0) — Checks whether the object archived under name at index has been instantiated in this session.
* `bool` [IsInstantiated](#a952bf7fa844b79b7e5a503945a6df7cd) (int32 token) — Checks whether the object represented by token has been instantiated in this session.
* `void` [RelinquishOwnership](#aa14b4974578f4a6587ce29d7408f722e) (BArchivable *archivable) — Relinquish ownership of archivable. If archivable remains unclaimed at the end of the unarchiving session, it will be deleted (unless it is the root object).

### Static Public Member Functions

* 
*  — Attempt to instantiate an object of type T from BMessage* from.
* `static bool` [IsArchiveManaged](#af5a80d3440ee8d7b1ce7055157fef814) (const BMessage *archive) — Checks whether archive was managed by a BArchiver object.
* `static BMessage *` [PrepareArchive](#acdd712bd85312bc7d36896e20b71b6b9) (BMessage *&archive) — Prepares archive for use by a BUnarchiver.

## Detailed Member Documentation

### `ownership_policy`

```cpp
enum BUnarchiver::ownership_policy
```

Options for the ownership policy of objects retrieved from [BUnarchiver](classBUnarchiver.md). 



**Since:** Haiku R1



| Enumerator |
| :--- |
| B_ASSUME_OWNERSHIP | Ownership of unarchived objects will be transferred to the caller.     **Since:** Haiku R1 |
| B_DONT_ASSUME_OWNERSHIP | The unarchived objects will be borrowed to the caller.     **Since:** Haiku R1 |

---

### `BUnarchiver()`

```cpp
BUnarchiver::BUnarchiver(const BMessage * archive)
```

Constructs a [BUnarchiver](classBUnarchiver.md) object to manage `archive`. 



> [!NOTE]
> To guarantee that your AllUnarchived() method will be called during archival, you must create a [BUnarchiver](classBUnarchiver.md) object in your archive constructor. It is necessary to do this even if you won't use the [BUnarchiver](classBUnarchiver.md) object in your archive constructor.



> [!WARNING]
> Do not construct a [BUnarchiver](classBUnarchiver.md) object without first calling [BUnarchiver::PrepareArchive()](classBUnarchiver.md#acdd712bd85312bc7d36896e20b71b6b9) on `archive`. It is only safe to build a [BUnarchiver](classBUnarchiver.md) without this call in your AllUnarchived() implementation.



**See also:** [BUnarchiver::PrepareArchive()](classBUnarchiver.md#acdd712bd85312bc7d36896e20b71b6b9)



**Since:** Haiku R1

---

### `~BUnarchiver()`

```cpp
BUnarchiver::~BUnarchiver()
```

Destroys a [BUnarchiver](classBUnarchiver.md) object. 


Calls this objects [Finish()](classBUnarchiver.md#a7640fa5d84dc6dca19d7513326d2bba2) method, if it has not yet been called.



**Since:** Haiku R1

---

### `ArchiveMessage()`

```cpp
const BMessage * BUnarchiver::ArchiveMessage()const
```

Returns the BMessage* used to construct this [BUnarchiver](classBUnarchiver.md). 


This is the archive that [FindObject()](classBUnarchiver.md#ad64f70e03bc7b9c202eec4d5d07d075e) uses.

---

### `AssumeOwnership()`

```cpp
void BUnarchiver::AssumeOwnership(BArchivable * archivable)
```

Become the owner of *archivable*. 


After calling this method you are responsible for deleting the *archivable*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `archivable` | The *archivable* object. |





**Since:** Haiku R1

---

### `EnsureUnarchived()`

```cpp
status_t BUnarchiver::EnsureUnarchived(const char * name, int32 index = 0)
```

Ensure the object archived under *name* at *index* is unarchived and instantiated. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The archive *name*. |
| `index` | The archive *index*. |





**Returns:** A status code.



**Since:** Haiku R1


References [B_DONT_ASSUME_OWNERSHIP](classBUnarchiver.md#ac1a5a14b2ae797c7f051dc44e725d640a4cc389b871e531d4f05c9d72e641b7e3), and [FindObject()](classBUnarchiver.md#ad64f70e03bc7b9c202eec4d5d07d075e).

---

### `EnsureUnarchived()`

```cpp
status_t BUnarchiver::EnsureUnarchived(int32 token)
```

Ensure the object represented by *token* is unarchived and instantiated. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `token` | the object *token* |





**Returns:** A status code.



**Since:** Haiku R1


References [B_DONT_ASSUME_OWNERSHIP](classBUnarchiver.md#ac1a5a14b2ae797c7f051dc44e725d640a4cc389b871e531d4f05c9d72e641b7e3), and [GetObject()](classBUnarchiver.md#a60bc2e909dbdc0b9a786e073dc56e9d7).

---

### `FindObject()`

```cpp
status_t BUnarchiver::FindObject(const char * name, int32 index, ownership_policy owning, T *& object)
```

Recover an object that had previously been archived using the [BArchiver::AddArchivable()](classBArchiver.md#a237a50590efba0121bf12249c5b6cb7f) method. 


If the object has not yet been instantiated, and this request is not coming from an AllUnarchived() implementation, the object will be instantiated now.


If the retrieved object is not of the type T, then this method will fail. If this method fails, you will not receive ownership of the object, no matter what you specified in `owning`.


Template Parameters

| Col 1 | Col 2 |
| :--- | :--- |
| T | The type of object you wish to find. |




Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name that was passed to [BArchiver::AddArchivable()](classBArchiver.md#a237a50590efba0121bf12249c5b6cb7f) when adding this object. |
| `index` | The index of the object you wish to recover (`0-based`, like [BMessage::FindData()](../application_kit/classBMessage.md#a1e896648ee668dd5d6c8a4311d6cfa94). |
| `owning` | Dictates whether or not you wish to take ownership of the retrieved object. |
| `object` | Return parameter for the retrieved object of type T. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object retrieved was of type T. |
| B_BAD_TYPE | The object retrieved was not of type T. |





**Since:** Haiku R1


References [B_ASSUME_OWNERSHIP](classBUnarchiver.md#ac1a5a14b2ae797c7f051dc44e725d640a915cee940a254f586f0fc83402dcd4d4), [FindObject()](classBUnarchiver.md#ad64f70e03bc7b9c202eec4d5d07d075e), [NULL](SupportDefs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), and [RelinquishOwnership()](classBUnarchiver.md#aa14b4974578f4a6587ce29d7408f722e).

---

### `FindObject()`

```cpp
status_t BUnarchiver::FindObject(const char * name, int32 index, T *& object)
```

Recover and take ownership of an object that had previously been archived using the [BArchiver::AddArchivable()](classBArchiver.md#a237a50590efba0121bf12249c5b6cb7f) method. 


Template Parameters

| Col 1 | Col 2 |
| :--- | :--- |
| T | The type of object you wish to find. |




Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name that was passed to [BArchiver::AddArchivable()](classBArchiver.md#a237a50590efba0121bf12249c5b6cb7f) when adding this object. |
| `index` | The index of the object you wish to recover (`0-based`, like [BMessage::FindData()](../application_kit/classBMessage.md#a1e896648ee668dd5d6c8a4311d6cfa94). |
| `object` | Return parameter for the retrieved object of type T. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object retrieved was of type T. |
| B_BAD_TYPE | The object retrieved was not of type T. |





**Since:** Haiku R1


References [B_ASSUME_OWNERSHIP](classBUnarchiver.md#ac1a5a14b2ae797c7f051dc44e725d640a915cee940a254f586f0fc83402dcd4d4), and [FindObject()](classBUnarchiver.md#ad64f70e03bc7b9c202eec4d5d07d075e).

---

### `FindObject()`

```cpp
status_t BUnarchiver::FindObject(const char * name, ownership_policy owning, T *& object)
```

Recover an object at index `0` that had previously been archived using the [BArchiver::AddArchivable()](classBArchiver.md#a237a50590efba0121bf12249c5b6cb7f) method. 


Equivalent to calling FindObject(name, `0`, owning, object).


Template Parameters

| Col 1 | Col 2 |
| :--- | :--- |
| T | The type of *object* you wish to find. |




Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name that was passed to [BArchiver::AddArchivable()](classBArchiver.md#a237a50590efba0121bf12249c5b6cb7f) when adding this object. |
| `owning` | Dictates whether or not you wish to take ownership of the retrieved object. |
| `object` | Return parameter for the retrieved object of type T. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object retrieved was of type T. |
| B_BAD_TYPE | The object retrieved was not of type T. |





**Since:** Haiku R1


References [FindObject()](classBUnarchiver.md#ad64f70e03bc7b9c202eec4d5d07d075e).

---

### `FindObject()`

```cpp
status_t BUnarchiver::FindObject(const char * name, T *& object)
```

Recover and take ownership of an object at index `0` that had previously been archived using the [BArchiver::AddArchivable()](classBArchiver.md#a237a50590efba0121bf12249c5b6cb7f) method. 


Equivalent to calling FindObject(name, `0`, [BUnarchiver::B_ASSUME_OWNERSHIP](classBUnarchiver.md#ac1a5a14b2ae797c7f051dc44e725d640a915cee940a254f586f0fc83402dcd4d4), object).


Template Parameters

| Col 1 | Col 2 |
| :--- | :--- |
| T | The type of *object* you wish to find. |




Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name that was passed to [BArchiver::AddArchivable()](classBArchiver.md#a237a50590efba0121bf12249c5b6cb7f) when adding this object. |
| `object` | Return parameter for the retrieved *object* of type T. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The *object* retrieved was of type T. |
| B_BAD_TYPE | The *object* retrieved was not of type T. |





**Since:** Haiku R1


References [B_ASSUME_OWNERSHIP](classBUnarchiver.md#ac1a5a14b2ae797c7f051dc44e725d640a915cee940a254f586f0fc83402dcd4d4).


Referenced by [EnsureUnarchived()](classBUnarchiver.md#af2a3f90c5405356b8f9588dcec99d61e), and [FindObject()](classBUnarchiver.md#a65b5036350c00bb31cff5f484287071a).

---

### `Finish()`

```cpp
status_t BUnarchiver::Finish(status_t err = B_OK)
```

Report any unarchiving errors and possibly complete the archiving session. 


This method may finish an unarchiving session (triggering the call of all instantiated objects' AllUnarchived() methods) if the following conditions are true:



* No errors have been reported to this or any other [BUnarchiver](classBUnarchiver.md) object within this session.

* This is the last remaining [BUnarchiver](classBUnarchiver.md) that has not had its [Finish()](classBUnarchiver.md#a7640fa5d84dc6dca19d7513326d2bba2) method invoked.



If you call this method with an error code not equal to B_OK, then this unarchiving session has failed, instantiated objects will not have their AllUnarchived() methods called, and any subsequent calls to this method on any [BUnarchiver](classBUnarchiver.md) objects in this session will return your error code. Furthermore, any objects that have been instantiated, but have not had their ownership assumed by another object will now be deleted (excluding the root object).



**Returns:** The first error reported in this unarchiving session, or `B_OK`.



**Since:** Haiku R1

---

### `GetObject()`

```cpp
status_t BUnarchiver::GetObject(int32 token, ownership_policy owning, T *& object)
```

Recover an object by token that was archived by a [BArchiver](classBArchiver.md) object. If the object has not yet been instantiated, and this request is not coming from an AllUnarchived() implementation, the object will be instantiated now. 


If the retrieved object is not of the type T, then this method will fail. If this method fails, you will not receive ownership of the object, no matter what you specified in `owning`.


Template Parameters

| Col 1 | Col 2 |
| :--- | :--- |
| T | The type of *object* you wish to find. |




Parameters

| Parameter | Description |
| :--- | :--- |
| `token` | The *token* you got for this object from [BArchiver::GetTokenForArchivable()](classBArchiver.md#a787a6a7972a6c4624829c5c8d8d16e55) during archival. |
| `owning` | Whether or not you wish to take ownership of the retrieved object. |
| `object` | Return parameter for the retrieved object of type T. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object retrieved was of type T. |
| B_BAD_TYPE | The object retrieved was not of type T. |





**Since:** Haiku R1


References [B_ASSUME_OWNERSHIP](classBUnarchiver.md#ac1a5a14b2ae797c7f051dc44e725d640a915cee940a254f586f0fc83402dcd4d4), [GetObject()](classBUnarchiver.md#a60bc2e909dbdc0b9a786e073dc56e9d7), [NULL](SupportDefs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), and [RelinquishOwnership()](classBUnarchiver.md#aa14b4974578f4a6587ce29d7408f722e).

---

### `GetObject()`

```cpp
status_t BUnarchiver::GetObject(int32 token, T *& object)
```

Recover and take ownership of an object represented by *token*. 


Equivalent to calling GetObject(token, `B_ASSUME_OWNERSHIP`, object)


Template Parameters

| Col 1 | Col 2 |
| :--- | :--- |
| T | The type of *object* you wish to find. |




Parameters

| Parameter | Description |
| :--- | :--- |
| `token` | The *token* you got for this object from [BArchiver::GetTokenForArchivable()](classBArchiver.md#a787a6a7972a6c4624829c5c8d8d16e55) during archival. |
| `object` | The return parameter for the retrieved object of type T. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object retrieved was of type T. |
| B_BAD_TYPE | The object retrieved was not of type T. |





**Since:** Haiku R1


References [B_ASSUME_OWNERSHIP](classBUnarchiver.md#ac1a5a14b2ae797c7f051dc44e725d640a915cee940a254f586f0fc83402dcd4d4).


Referenced by [EnsureUnarchived()](classBUnarchiver.md#a265dcb1cfd3cb185deb80c0fb0836613), and [GetObject()](classBUnarchiver.md#a939359c608ad87dee82b073d0ac79517).

---

### `InstantiateObject()`

```cpp
status_t BUnarchiver::InstantiateObject(BMessage * from, T *& object)
```

Attempt to instantiate an object of type T from BMessage* *from*. 


If the instantiated object is not of type T, then it will be deleted, and this method will return `B_BAD_TYPE`. This method is similar to the [instantiate_object()](group__support__globals.md#gac98d3af4a84cd0880d8a853f7c526764) function, but provides error reporting and protection from memory leaks.


Parameters

| Parameter | Description |
| :--- | :--- |
| `from` | The [BMessage](../application_kit/classBMessage.md) to instantiate from. |
| `object` | Return parameter for the retrieved object of type T. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object retrieved was of type T. |
| B_BAD_TYPE | The object retrieved was not of type T. |





**Since:** Haiku R1


References [InstantiateObject()](classBUnarchiver.md#a3bf0c1cbca1644015d17850424d0c374), and [NULL](SupportDefs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4).


Referenced by [InstantiateObject()](classBUnarchiver.md#a3bf0c1cbca1644015d17850424d0c374).

---

### `IsArchiveManaged()`

```cpp
static bool BUnarchiver::IsArchiveManaged(const BMessage * archive)
```

Checks whether *archive* was managed by a [BArchiver](classBArchiver.md) object. 


This method can be used to maintain archive backwards-compatibility for a class that has been updated to use the [BArchiver](classBArchiver.md) class. If there is a possibility that you are may dealing with a legacy archive, you can use this method to find out before calling any methods on your [BUnarchiver](classBUnarchiver.md) object.


Here is an example of how you might use this method. Note that you must still call PrepareArchive(archive) either way.



```cpp
MyArchivableClas::MyArchivableClass(BMessage* archive)
    :
 BArchivable(BUnarchiver::PrepareArchive(archive))
{
 BUnarchiver unarchiver(archive);
 
 if (BUnarchiver::IsArchiveManaged(archive)) {
 // ... calls to FindObject() or GetObject() here ...
    } else {
 // ... calls to BMessage::FindMessage() here ...
    }
}
```


**Returns:** Whether *archive* was managed by a [BArchiver](classBArchiver.md) object.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | if *archive* was managed by a [BArchiver](classBArchiver.md) object. |
| false | otherwise. |





**Since:** Haiku R1

---

### `IsInstantiated()`

```cpp
bool BUnarchiver::IsInstantiated(const char * name, int32 index = 0)
```

Checks whether the object archived under *name* at *index* has been instantiated in this session. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The archive *name*. |
| `index` | The arcive *token*. |





**Returns:** `true` if instantiated, `false` otherwise.



**Since:** Haiku R1

---

### `IsInstantiated()`

```cpp
bool BUnarchiver::IsInstantiated(int32 token)
```

Checks whether the object represented by `token` has been instantiated in this session. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `token` | The object *token*. |





**Returns:** `true` if instantiated, `false` otherwise



**Since:** Haiku R1

---

### `PrepareArchive()`

```cpp
static BMessage * BUnarchiver::PrepareArchive(BMessage *& archive)
```

Prepares `archive` for use by a [BUnarchiver](classBUnarchiver.md). 


This method must be called if you plan to use a [BUnarchiver](classBUnarchiver.md) on an archive. It must be called once for each class an object inherits from that will use a [BUnarchiver](classBUnarchiver.md).



> [!WARNING]
> This method **must** be called **before** a call to the archive constructor of your parent class.


Notice the use of this method in the example provided below. 


```cpp
MyArchivableClas::MyArchivableClas(BMessage* archive)
    :
 BArchivable(BUnarchiver::PrepareArchive(archive))
{
 // ...
}
```

Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The archive you wish to have prepared. |





**Returns:** The same [BMessage](../application_kit/classBMessage.md) as is passed in.



**Since:** Haiku R1

---

### `RelinquishOwnership()`

```cpp
void BUnarchiver::RelinquishOwnership(BArchivable * archivable)
```

Relinquish ownership of *archivable*. If *archivable* remains unclaimed at the end of the unarchiving session, it will be deleted (unless it is the root object). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archivable` | The *archivable* object. |





**Since:** Haiku R1


Referenced by [FindObject()](classBUnarchiver.md#a65b5036350c00bb31cff5f484287071a), and [GetObject()](classBUnarchiver.md#a939359c608ad87dee82b073d0ac79517).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBUnarchiver.html).
