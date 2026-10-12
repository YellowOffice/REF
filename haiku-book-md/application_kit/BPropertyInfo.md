---
name: BPropertyInfo
type: class
kit: application_kit
brief: "Class used to manage scripting"
source: haiku-book
---

# BPropertyInfo Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Class used to manage scripting. 



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BPropertyInfo](#ac125ac852be44e17bc30c60d62323ab0) (property_info *prop=NULL, value_info *value=NULL, bool freeOnDelete=false) — Initializes the object with the specified NULL-terminated arrays propertyInfo and valueInfo.
* `virtual` [~BPropertyInfo](#aa551f86d3802a646b2facd070bb6eb66) () — Destructor method.
* `virtual bool` [AllowsTypeCode](#a52ef3962ccae6efe91780df25c2c043a) (type_code code) const — Returns true if code is B_PROPERTY_INFO_TYPE, false otherwise.
* `int32` [CountProperties](#a656448b6f78eb446875a6bf597369215) () const — Returns The number of properties specified as an int32.
* `int32` [CountValues](#a5b2742b582dacf23dd4557c2ad48ba68) () const — Returns The number of values specified as an int32.
* `virtual int32` [FindMatch](#aeceb1f3e070b4b4604d0ec02af1bba23) (BMessage *msg, int32 index, BMessage *specifier, int32 form, const char *prop, void *data=NULL) const
* `virtual status_t` [Flatten](#a141a4d054c98424d677af1aecdb8e176) (void *buffer, ssize_t size) const
* `virtual ssize_t` [FlattenedSize](#a326574fe08e91224d95e1c4943396bb6) () const — Returns the size of the flattened object in bytes.
* `virtual bool` [IsFixedSize](#a33f147be78c14a2a0da3a45d21391bf2) () const — Always returns false.
* `void` [PrintToStream](#acc46b72a11086c54337b6231d758cae0) () const — Prints each property, command, type, and specifier to standard output.
* `const property_info *` [Properties](#ac08ebb5e8faefa538c19f6fdcf745d97) () const — Returns the properties as a property_info pointer.
* `virtual type_code` [TypeCode](#a9217a74cb2653b6f63472166c4373196) () const — Always returns B_PROPERTY_INFO_TYPE.
* `virtual status_t` [Unflatten](#af4ae06ccc8b9f93ab74ffdde0d1f93ce) (type_code code, const void *buffer, ssize_t size)
* `const value_info *` [Values](#a0f259398818fe100acd80c05a091ae81) () const — Returns the values as a value_info pointer.
* `virtual` [~BFlattenable](#a884e130a5d27acc15b1e4e4c505157ff) () — Destructor. Does nothing.
* `virtual bool` [AllowsTypeCode](#a30165696bba76fed10e37508cc4f6925) (type_code code) const — Get whether or not the supplied type_code is supported.
* `virtual status_t` [Flatten](#ab934b64a8b218a4f9078ded191be6fbb) (void *buffer, ssize_t size) const =0 — Pure virtual that should flatten the object into the supplied buffer.
* `virtual ssize_t` [FlattenedSize](#a9b5885d4454326ca448438960ecff466) () const =0 — Pure virtual that should return the size of the flattened object in bytes.
* `virtual bool` [IsFixedSize](#ac019f502749a0cc78082f5ec7c8f5b56) () const =0 — Pure virtual that should return whether or not flattened objects of this type always have a fixed size.
* `virtual type_code` [TypeCode](#a819507fa1b0906f14299db15f6e990d1) () const =0 — Pure virtual that returns the type_code this class flattens to.
* `virtual status_t` [Unflatten](#a41e7168574912690be159991d2b07a97) (type_code code, const void *buffer, ssize_t size)=0 — Pure virtual that should unflatten the buffer and put the contents into the current object.

### Static Protected Member Functions

* `static bool` [FindCommand](#a3dc32742ee4247ad4720de2314171e0f) (uint32 what, int32 index, property_info *info) — Find the command inside of propertyInfo matching what and index.
* `static bool` [FindSpecifier](#a4492fda22fe56b9ba2a8e30b6cce14d0) (uint32 form, property_info *info) — Find the specifier inside of propertyInfo matching form.

## Detailed Member Documentation

### `BPropertyInfo()`

```cpp
BPropertyInfo::BPropertyInfo(property_info * propertyInfo = NULL, value_info * valueInfo = NULL, bool freeOnDelete = false)
```

Initializes the object with the specified NULL-terminated arrays *propertyInfo* and *valueInfo*. 


The arrays are not copied so do not modify or delete the arrays while they are in use by [BPropertyInfo](classBPropertyInfo.md).


Parameters

| Parameter | Description |
| :--- | :--- |
| `propertyInfo` | The NULL-terminated properties array. |
| `valueInfo` | The NULL-terminated values array. |
| `freeOnDelete` | if `true`, free the memory associated with *propertyInfo* and *valueInfo* when the object is destroyed. |





**Since:** BeOS R4

---

### `~BPropertyInfo()`

```cpp
BPropertyInfo::~BPropertyInfo()
```

Destructor method. 


If *freeOnDelete* is set to `true` in the constructor this method frees all memory associated with *propertyInfo* and *valueInfo*.



**Since:** BeOS R3

---

### `AllowsTypeCode()`

```cpp
bool BPropertyInfo::AllowsTypeCode(type_code code)const
```

Returns `true` if *code* is B_PROPERTY_INFO_TYPE, `false` otherwise. 



**See also:** [BFlattenable::AllowsTypeCode()](../support_kit/classBFlattenable.md#a30165696bba76fed10e37508cc4f6925)



**Since:** BeOS R4


Reimplemented from [BFlattenable](../support_kit/classBFlattenable.md#a30165696bba76fed10e37508cc4f6925).

---

### `CountProperties()`

```cpp
int32 BPropertyInfo::CountProperties()const
```

Returns The number of properties specified as an int32. 



**Since:** BeOS R4

---

### `CountValues()`

```cpp
int32 BPropertyInfo::CountValues()const
```

Returns The number of values specified as an int32. 



**Since:** BeOS R4

---

### `FindCommand()`

```cpp
bool BPropertyInfo::FindCommand(uint32 what, int32 index, property_info * propertyInfo)
```

Find the command inside of *propertyInfo* matching *what* and *index*. 


You may want to override this method in derived classes.



**Returns:** `true` if the command was found, `false` otherwise.



**Since:** BeOS R4

---

### `FindMatch()`

```cpp
int32 BPropertyInfo::FindMatch(BMessage * message, int32 index, BMessage * specifier, int32 form, const char * property, void * data = NULL)const
```

**Since:** BeOS R3

---

### `FindSpecifier()`

```cpp
bool BPropertyInfo::FindSpecifier(uint32 form, property_info * propertyInfo)
```

Find the specifier inside of *propertyInfo* matching *form*. 


You may want to override this method in derived classes.



**Returns:** `true` if the specifier was found, `false` otherwise.



**Since:** BeOS R4

---

### `Flatten()`

```cpp
status_t BPropertyInfo::Flatten(void * buffer, ssize_t numBytes)const
```

**See also:** [BFlattenable::Flatten()](../support_kit/classBFlattenable.md#ab934b64a8b218a4f9078ded191be6fbb)



**Since:** BeOS R4


Implements [BFlattenable](../support_kit/classBFlattenable.md#ab934b64a8b218a4f9078ded191be6fbb).

---

### `FlattenedSize()`

```cpp
ssize_t BPropertyInfo::FlattenedSize()const
```

Returns the size of the flattened object in bytes. 



**See also:** [BFlattenable::FlattenedSize()](../support_kit/classBFlattenable.md#a9b5885d4454326ca448438960ecff466)



**Since:** BeOS R4


Implements [BFlattenable](../support_kit/classBFlattenable.md#a9b5885d4454326ca448438960ecff466).

---

### `IsFixedSize()`

```cpp
bool BPropertyInfo::IsFixedSize()const
```

Always returns `false`. 



**See also:** [BFlattenable::IsFixedSize()](../support_kit/classBFlattenable.md#ac019f502749a0cc78082f5ec7c8f5b56)



**Since:** BeOS R4


Implements [BFlattenable](../support_kit/classBFlattenable.md#ac019f502749a0cc78082f5ec7c8f5b56).

---

### `PrintToStream()`

```cpp
void BPropertyInfo::PrintToStream()const
```

Prints each property, command, type, and specifier to standard output. 



**Since:** BeOS R4

---

### `Properties()`

```cpp
const property_info * BPropertyInfo::Properties()const
```

Returns the properties as a `property_info` pointer. 


Returns the pointer directly, does not make copy.


Called PropertyInfo() in the BeBook.



**Since:** BeOS R4

---

### `TypeCode()`

```cpp
type_code BPropertyInfo::TypeCode()const
```

Always returns `B_PROPERTY_INFO_TYPE`. 



**See also:** [BFlattenable::TypeCode()](../support_kit/classBFlattenable.md#a819507fa1b0906f14299db15f6e990d1)



**Since:** BeOS R4


Implements [BFlattenable](../support_kit/classBFlattenable.md#a819507fa1b0906f14299db15f6e990d1).

---

### `Unflatten()`

```cpp
status_t BPropertyInfo::Unflatten(type_code code, const void * buffer, ssize_t numBytes)
```

**See also:** [BFlattenable::Unflatten()](../support_kit/classBFlattenable.md#a41e7168574912690be159991d2b07a97)



**Since:** BeOS R4


Implements [BFlattenable](../support_kit/classBFlattenable.md#a41e7168574912690be159991d2b07a97).

---

### `Values()`

```cpp
const value_info * BPropertyInfo::Values()const
```

Returns the values as a `value_info` pointer. 


Returns the pointer directly, does not make copy.



**Since:** BeOS R4

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPropertyInfo.html).
