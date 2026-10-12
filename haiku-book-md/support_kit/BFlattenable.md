---
name: BFlattenable
type: class
kit: support_kit
brief: "Interface for classes that can flatten and unflatten themselves to a stream of bytes"
source: haiku-book
---

# BFlattenable Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Interface for classes that can flatten and unflatten themselves to a stream of bytes. 


It is convenient that objects can be stored as a flat stream of bytes. In this way, they can be written to disk, exchanged between applications or send over networks. This ability, known as marshaling in many other programming languages, is not native to C++. The Haiku API has created a universal interface that classes have if they are able to be flattened. This class defines the interface. This class does nothing on its own, and therefore contains pure virtual functions. By inheriting this class and implementing the methods in your own class, you will be able to use your objects as flattenable objects throughout the Haiku API.


Flattened objects can be used for example when sending messages within an application or between applications. The [BMessage](../application_kit/classBMessage.md) class uses the interface to store and transmit custom classes.


If you want to be able to flatten your objects, you will need to implement various methods. [Flatten()](classBFlattenable.md#ab934b64a8b218a4f9078ded191be6fbb) and [Unflatten()](classBFlattenable.md#a41e7168574912690be159991d2b07a97) are where the magic happen. These methods handle the actual flattening and unflattening. To identify flattened data in for example [BMessage](../application_kit/classBMessage.md), the object has a type_code. Type codes are four byte long integers. You can choose to flatten to one of the existing types, if you are certain that you are compatible to those, but you'll usually define your own type. Your best option is by using a multicharacter constant, such as 'STRI'. Implement [TypeCode()](classBFlattenable.md#a819507fa1b0906f14299db15f6e990d1) to return the type you support. Implement [FlattenedSize()](classBFlattenable.md#a9b5885d4454326ca448438960ecff466) to make sure that other objects can provide the right buffers. Implement [IsFixedSize()](classBFlattenable.md#ac019f502749a0cc78082f5ec7c8f5b56) to return whether your objects always store to a fixed size.


See the following example: 


```cpp
type_code CUSTOM_STRING_TYPE = 'CUST';
 
class CustomString : public BFlattenable {
public:
 char data[100];
 
 // from BFlattenable
 bool IsFixedSize() const { return false; };
 type_code TypeCode() const { return CUSTOM_STRING_TYPE; };
    ssize_t FlattenedSize() const { return strlen(data); };
 
 status_t Flatten(void* buffer, ssize_t size) const
 {
 if ((strlen(data) + 1) < size)
 return B_BAD_VALUE;
 
        memcpy(buffer, data, size);
 
 return B_OK;
    };
 
 status_t Unflatten(type_code code, const void* buffer, ssize_t size)
    {
 if (code != CUSTOM_STRING_TYPE)
 return B_BAD_TYPE;
 
 if (size > 100)
 return B_NO_MEMORY;
 
        memcpy(data, buffer, size);
 
 return B_OK;
    };
};
```

Have a look at [TypeConstants.h](TypeConstants_8h.md) for a list of all the types that the Haiku API defines.


The Haiku API has a second interface for storing objects, which is with [BArchivable](classBArchivable.md). [BArchivable](classBArchivable.md) is for more complex cases. Instead of one flat datastream, it stores an object in a [BMessage](../application_kit/classBMessage.md). In that way you can reflect internals of a class better. It also provides an interface for instantiating objects, that is, for objects to restore themselves from a [BMessage](../application_kit/classBMessage.md). In essence, [BArchivable](classBArchivable.md) is more suitable for objects that are alive. In short [BFlattenable](classBFlattenable.md) is for data objects, [BArchivable](classBArchivable.md) is for 'live' objects.


Other classes in the API that support flattening and unflattening are for example [BMessage](../application_kit/classBMessage.md), which enables you to conveniently write flattened data to disk. Another example is [BPath](../storage_kit/classBPath.md). Because of that you can store paths and send them over via messages. Throughout the Haiku API you will find classes that provide the flattening interface.



**Since:** BeOS R3

## Member List

### Public Member Functions

* `virtual` [~BFlattenable](#a884e130a5d27acc15b1e4e4c505157ff) () — Destructor. Does nothing.
* `virtual bool` [AllowsTypeCode](#a30165696bba76fed10e37508cc4f6925) (type_code code) const — Get whether or not the supplied type_code is supported.
* `virtual status_t` [Flatten](#ab934b64a8b218a4f9078ded191be6fbb) (void *buffer, ssize_t size) const =0 — Pure virtual that should flatten the object into the supplied buffer.
* `virtual ssize_t` [FlattenedSize](#a9b5885d4454326ca448438960ecff466) () const =0 — Pure virtual that should return the size of the flattened object in bytes.
* `virtual bool` [IsFixedSize](#ac019f502749a0cc78082f5ec7c8f5b56) () const =0 — Pure virtual that should return whether or not flattened objects of this type always have a fixed size.
* `virtual type_code` [TypeCode](#a819507fa1b0906f14299db15f6e990d1) () const =0 — Pure virtual that returns the type_code this class flattens to.
* `virtual status_t` [Unflatten](#a41e7168574912690be159991d2b07a97) (type_code code, const void *buffer, ssize_t size)=0 — Pure virtual that should unflatten the buffer and put the contents into the current object.

## Detailed Member Documentation

### `~BFlattenable()`

```cpp
BFlattenable::~BFlattenable()
```

Destructor. Does nothing. 



**Since:** Haiku R1

---

### `AllowsTypeCode()`

```cpp
bool BFlattenable::AllowsTypeCode(type_code code)const
```

Get whether or not the supplied type_code is supported. 


This default implementation checks the *code* argument against the type_code returned by [TypeCode()](classBFlattenable.md#a819507fa1b0906f14299db15f6e990d1).


Parameters

| Parameter | Description |
| :--- | :--- |
| `code` | The type_code constant you want to check for. |





**Returns:** Whether or not the supplied type_code is supported.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The type_code is supported. |
| false | The type_code is not supported. |





**Since:** BeOS R3


Reimplemented in [BPropertyInfo](../application_kit/classBPropertyInfo.md#a52ef3962ccae6efe91780df25c2c043a), [BPath](../storage_kit/classBPath.md#aef48a6f6cf10836b412df6b6e060c4c2), and [BStringList](classBStringList.md#ada0bef2ce78540984803c8cfa3967a6a).

---

### `Flatten()`

```cpp
status_t BFlattenable::Flatten(void * buffer, ssize_t size)const
```

Pure virtual that should flatten the object into the supplied *buffer*. 


Please make sure that you check that the supplied buffer is not a `NULL` pointer. Also make sure that the size of the flattened object does isn't larger than the size of the buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | The buffer to flatten in. |
| `size` | The size of the buffer. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object was flattened. |
| B_NO_MEMORY | The buffer was smaller than required. |
| B_BAD_VALUE | The buffer was a `NULL` pointer. |





**Since:** BeOS R3


Implemented in [BPropertyInfo](../application_kit/classBPropertyInfo.md#a141a4d054c98424d677af1aecdb8e176), [BAffineTransform](../interface_kit/classBAffineTransform.md#a8e9004914c3d7ac7ddb16d866cab918e), [BNetworkAddress](../network_kit/classBNetworkAddress.md#a83691ef631ad8a0dd4d047c00c00c61a), [BPath](../storage_kit/classBPath.md#a2866faf2cacac53e9d583f9a3dbd903c), and [BStringList](classBStringList.md#a2950d106932743b78d006740557074fe).

---

### `FlattenedSize()`

```cpp
ssize_t BFlattenable::FlattenedSize()const
```

Pure virtual that should return the size of the flattened object in bytes. 



**Since:** BeOS R3


Implemented in [BPropertyInfo](../application_kit/classBPropertyInfo.md#a326574fe08e91224d95e1c4943396bb6), [BAffineTransform](../interface_kit/classBAffineTransform.md#a5ee0a422598727d1653c06d6769a26f9), [BNetworkAddress](../network_kit/classBNetworkAddress.md#ae7b6ebe7b9ac4eec5302fa7cb2892c8b), [BPath](../storage_kit/classBPath.md#a5c77e3e9fb829249e9d1b6366f6d5520), and [BStringList](classBStringList.md#a58b7d9d1f5581d6e05537fb24abbb241).

---

### `IsFixedSize()`

```cpp
bool BFlattenable::IsFixedSize()const
```

Pure virtual that should return whether or not flattened objects of this type always have a fixed size. 



**Returns:** Should return whether or not the flattened objects of this type always have a fixed size.



**Since:** BeOS R3


Implemented in [BPropertyInfo](../application_kit/classBPropertyInfo.md#a33f147be78c14a2a0da3a45d21391bf2), [BAffineTransform](../interface_kit/classBAffineTransform.md#ac4b8ff09ab94c925d2f6e068b945bf4b), [BNetworkAddress](../network_kit/classBNetworkAddress.md#acce52cf6caec21d846d9d188210d5f59), [BPath](../storage_kit/classBPath.md#ac43f61c0280de191eef4adcf6a642437), and [BStringList](classBStringList.md#a27f621354797cf96fd55327d0dafdc2e).

---

### `TypeCode()`

```cpp
type_code BFlattenable::TypeCode()const
```

Pure virtual that returns the type_code this class flattens to. 



**Returns:** Either one of the existing typecodes found in [TypeConstants.h](TypeConstants_8h.md) if your class actually is compatible to those formats, or a custom four-byte integer constant if not.



**Since:** BeOS R3


Implemented in [BPropertyInfo](../application_kit/classBPropertyInfo.md#a9217a74cb2653b6f63472166c4373196), [BAffineTransform](../interface_kit/classBAffineTransform.md#a8b6a0f6bc9f1999f1f4a4e5a17610958), [BNetworkAddress](../network_kit/classBNetworkAddress.md#ad541b8571ed046f74556b23427867e7f), [BPath](../storage_kit/classBPath.md#a05dc54fed4718135a3f55f476816f1cb), and [BStringList](classBStringList.md#aebe54b1791b65f0ea349f4fce771f0b9).

---

### `Unflatten()`

```cpp
status_t BFlattenable::Unflatten(type_code code, const void * buffer, ssize_t size)
```

Pure virtual that should unflatten the buffer and put the contents into the current object. 


Make sure that the supplied buffer is not `NULL` and that you actually support the typecode.


Parameters

| Parameter | Description |
| :--- | :--- |
| `code` | The type_code this data is. |
| `buffer` | The buffer to unflatten the data from. |
| `size` | The size of the data. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object is unflattened. |
| B_BAD_VALUE | The *buffer* pointer is `NULL` or the data is invalid. |
| B_BAD_TYPE | You don't support data with this *code*. |





**Since:** BeOS R3


Implemented in [BPropertyInfo](../application_kit/classBPropertyInfo.md#af4ae06ccc8b9f93ab74ffdde0d1f93ce), [BAffineTransform](../interface_kit/classBAffineTransform.md#a00b1c34cc0b696e14fb233f3ad74212f), [BNetworkAddress](../network_kit/classBNetworkAddress.md#a2430483749ce8c64600e8f5a6929f477), [BPath](../storage_kit/classBPath.md#a437333127ec6d2e1037e72dd822afeca), and [BStringList](classBStringList.md#aaba64379fbd1a9fa334137c712a5e073).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBFlattenable.html).
