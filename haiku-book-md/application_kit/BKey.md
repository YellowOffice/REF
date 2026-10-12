---
name: BKey
type: class
kit: application_kit
brief: "Class that represents a generic key for or from the Haiku key store"
source: haiku-book
---

# BKey Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Class that represents a generic key for or from the Haiku key store. 


A key has the following properties:


* A key **type** of [BKeyType](Key_8h.md#ab6fe8f56a119810db6dd4146fcece444), which identifies the type. For a generic key (like this key), it will be set to BKeyType::B_KEY_TYPE_GENERIC.

* A key **purpose** of [BKeyPurpose](Key_8h.md#a9518f864f4ad0bbd2fc5056a51f9ed5d), which identifies the purpose of the key. This is a hint for your (or other) applications on how and where the key may be used.

* A **primary** **identifier** that identifies a specific key. As an example, for WPA passwords, this is set to the network name. This should be a valid UTF-8 string.

* A **secondary** **identifier** that can be used as additional metadata.

* The **data**, the actual value of the key (such as a password or a certificate). This should be a valid UTF-8 string.

* Not in use: the **owner** identifies who created and/or owns the key. This feature is not yet enabled. It will always be set to an empty string.

* Not in use: the **creation** **time** will indicate when a key was stored in the central database. This feature is not yet enabled, and the value will always be 0.




**Since:** Haiku R1

## Member List

### Public Member Functions

* [BKey](#a77809839d879a1c07eddd64d8ff88b1a) () — Constructor for an empty generic key.
* [BKey](#ab797b11dcd56baefc46b298fc0b8a718) (BKey &other) — Copy constructor that makes a copy of an other BKey.
* [BKey](#a25764fe6ea6418ea5a3f10d903f80aa4) (BKeyPurpose purpose, const char *identifier, const char *secondaryIdentifier=NULL, const uint8 *data=NULL, size_t length=0) — Constructor for a generic key with the provided data.
* `virtual` [~BKey](#a2dfdbc566ae1f2643db4c46bbd4942c0) () — Free all resources associated with this key.
* `bigtime_t` [CreationTime](#af14a6300c8eccb77040c3d06fa7c9933) () const — Get the creation time of the key.
* `const uint8 *` [Data](#a55f2daba99a80eacfae784ec5b681c65) () const — Get a pointer to the data of the key.
* `size_t` [DataLength](#a8691803a6b74f8e27ae9cbc89ab6eb21) () const — Get the size of the key in bytes.
* `virtual status_t` [Flatten](#a054a1fea3c3a71393589ff6f45d873f2) (BMessage &message) const — Flatten the key into a message.
* `status_t` [GetData](#ae129138c6f94b3e6b796122c07c80f94) (uint8 *buffer, size_t bufferSize) const — Copy the key into the buffer.
* `const char *` [Identifier](#a519fb286f9b9bf340c45ab42ade87257) () const — Get the identifier of the key.
* `bool` [operator!=](#ae67824b7f83adf295a47b9cb31edac81) (const BKey &other) const — Compare this key to an other key.
* `BKey &` [operator=](#a9ffb98b62e2f1d1f2bbadbc9e917ee69) (const BKey &other) — Copy the data from the other key into this key.
* `bool` [operator==](#abec7406e9dbf876d9102ee08642f663d) (const BKey &other) const — Compare this key to an other key.
* `const char *` [Owner](#aea174803d7f63f94dd9de82bdf7b70b4) () const — Get the owner of the key.
* `virtual void` [PrintToStream](#ac7cd25324b948b012a6e0cf16f940658) () — Dump the contents of the key to standard output.
* `BKeyPurpose` [Purpose](#a3545ab4336657b23ce9f062e4d2eb831) () const — Get the purpose of the key.
* `const char *` [SecondaryIdentifier](#a8f31e4a4b0eb8ccce2e4a9214d7651a6) () const — Get the secondary identifier of the key.
* `status_t` [SetData](#adaf416afe5767fcc27bd79caa990e488) (const uint8 *data, size_t length) — Set the data for the key.
* `void` [SetIdentifier](#aaf927007ee39004f99acebd9741ba621) (const char *identifier) — Set the identifier of the key.
* `void` [SetPurpose](#adba48733f398dd45a12c5ac15a4ce938) (BKeyPurpose purpose) — Set the purpose of the key.
* `void` [SetSecondaryIdentifier](#a7d7f282241d38ba79da68cc2aa2c5785) (const char *identifier) — Set the secondary identifier of the key.
* `status_t` [SetTo](#a753f3fd6c65c9abf4fe7957a653d9685) (BKeyPurpose purpose, const char *identifier, const char *secondaryIdentifier=NULL, const uint8 *data=NULL, size_t length=0) — Set the key to the specified values.
* `virtual BKeyType` [Type](#a7971f210c7d6805a415ec19dbae3038d) () const — Returns the type of key.
* `virtual status_t` [Unflatten](#a0a59826da2f3a2da218f846e1e2aa216) (const BMessage &message) — Unflatten the key from a message.
* `void` [Unset](#a7c001778a01edb880e215b5851c7254b) () — Reset the values of the key.

## Detailed Member Documentation

### `BKey()`

```cpp
BKey::BKey()
```

Constructor for an empty generic key. 


An empty key has no data associated with it, other than that it has a generic purpose and a generic key type.



**Since:** Haiku R1

---

### `BKey()`

```cpp
BKey::BKey(BKeyPurpose purpose, const char * identifier, const char * secondaryIdentifier = NULL, const uint8 * data = NULL, size_t length = 0)
```

Constructor for a generic key with the provided data. 


See the class introduction for more information about the properties of a key. As you can see, the only required parameters are the *purpose* and the *identifier*. Any data you provide will be copied into the [BKey](classBKey.md) object.


Parameters

| Parameter | Description |
| :--- | :--- |
| `purpose` | The purpose of this key |
| `identifier` | A unique identifier for this key |
| `secondaryIdentifier` | An (optional) secondary identifier for this key |
| `data` | A pointer to a buffer that contains the value of the key, such as the password or the certificate data. |
| `length` | The length of the data in bytes that should be copied. |





**Since:** Haiku R1

---

### `BKey()`

```cpp
BKey::BKey(BKey & other)
```

Copy constructor that makes a copy of an *other* [BKey](classBKey.md). 



**Since:** Haiku R1

---

### `~BKey()`

```cpp
BKey::~BKey()
```

Free all resources associated with this key. 



**Since:** Haiku R1

---

### `CreationTime()`

```cpp
bigtime_t BKey::CreationTime()const
```

Get the creation time of the key. 



**Since:** Haiku R1

---

### `Data()`

```cpp
const uint8 * BKey::Data()const
```

Get a pointer to the data of the key. 



**Since:** Haiku R1

---

### `DataLength()`

```cpp
size_t BKey::DataLength()const
```

Get the size of the key in bytes. 



**Since:** Haiku R1

---

### `Flatten()`

```cpp
status_t BKey::Flatten(BMessage & message)const
```

Flatten the key into a *message*. 



**Since:** Haiku R1

---

### `GetData()`

```cpp
status_t BKey::GetData(uint8 * buffer, size_t bufferSize)const
```

Copy the key into the *buffer*. 


It is up to you to make sure the size of the buffer is the actual size of the key's data. If the provided buffer is smaller, only the *bufferSize* will be copied. If the buffer is larger, the key is copied, but the rest of the buffer will not be touched.


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | The buffer to copy the key to. |
| `bufferSize` | The size of the provided *buffer*. |





**Returns:** * `B_OK` if the data is sucessfully copied.

* An other error code if there was an issue copying the data.



**Since:** Haiku R1

---

### `Identifier()`

```cpp
const char * BKey::Identifier()const
```

Get the identifier of the key. 



**Since:** Haiku R1

---

### `operator!=()`

```cpp
bool BKey::operator!=(const BKey & other)const
```

Compare this key to an *other* key. 



**Returns:** `true` if any of the properties in this key differ from *other*.



**Since:** Haiku R1

---

### `operator=()`

```cpp
BKey & BKey::operator=(const BKey & other)
```

Copy the data from the *other* key into this key. 



**Since:** Haiku R1

---

### `operator==()`

```cpp
bool BKey::operator==(const BKey & other)const
```

Compare this key to an *other* key. 



**Returns:** `true` if all the properties in both keys are identical.



**Since:** Haiku R1

---

### `Owner()`

```cpp
const char * BKey::Owner()const
```

Get the owner of the key. 



**Since:** Haiku R1

---

### `PrintToStream()`

```cpp
void BKey::PrintToStream()
```

Dump the contents of the key to standard output. 


This is a debug function that helps you read the contents of the key. All properties, except for the actual `data` of the key, will be printed to `stdout`.



**Since:** Haiku R1


Reimplemented in [BPasswordKey](classBPasswordKey.md#a64ff92b5e0fde95eef53112a99f868dc).

---

### `Purpose()`

```cpp
BKeyPurpose BKey::Purpose()const
```

Get the purpose of the key. 



**Since:** Haiku R1

---

### `SecondaryIdentifier()`

```cpp
const char * BKey::SecondaryIdentifier()const
```

Get the secondary identifier of the key. 



**Since:** Haiku R1

---

### `SetData()`

```cpp
status_t BKey::SetData(const uint8 * data, size_t length)
```

Set the data for the key. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A pointer to the buffer that contains the data of the key. |
| `length` | The length in bytes of the data. |





**Returns:** * `B_OK` if the key data was updated.

* `B_NO_MEMORY` in case it fails to allocate memory.



**Since:** Haiku R1

---

### `SetIdentifier()`

```cpp
void BKey::SetIdentifier(const char * identifier)
```

Set the identifier of the key. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `identifier` | A pointer to a valid UTF-8 string. |





**Since:** Haiku R1

---

### `SetPurpose()`

```cpp
void BKey::SetPurpose(BKeyPurpose purpose)
```

Set the purpose of the key. 



**Since:** Haiku R1

---

### `SetSecondaryIdentifier()`

```cpp
void BKey::SetSecondaryIdentifier(const char * identifier)
```

Set the secondary identifier of the key. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `identifier` | A pointer to a valid UTF-8 string. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BKey::SetTo(BKeyPurpose purpose, const char * identifier, const char * secondaryIdentifier = NULL, const uint8 * data = NULL, size_t length = 0)
```

Set the key to the specified values. 


All properties of the key will be set to the parameters. If the key had a creation time set, it will be cleared. If there was an owner set, this piece of information will *not* be cleared.


Parameters

| Parameter | Description |
| :--- | :--- |
| `purpose` | The purpose of this key |
| `identifier` | A unique identifier for this key |
| `secondaryIdentifier` | An (optional) secondary identifier for this key |
| `data` | A pointer to a buffer that contains the value of the key, such as the password or the certificate data. |
| `length` | The length of the data in bytes that should be copied. |





**Returns:** * `B_OK` if the changes were successful.

* `B_NO_MEMORY` in case it fails to allocate memory.



**Since:** Haiku R1

---

### `Type()`

```cpp
virtual BKeyType BKey::Type()const
```

Returns the type of key. 


For a generic [BKey](classBKey.md), this will always be BKeyType::B_KEY_TYPE_GENERIC



**Since:** Haiku R1


Reimplemented in [BPasswordKey](classBPasswordKey.md#a8c53e208ace43023a7ed026bdf0938b6).


References [B_KEY_TYPE_GENERIC](Key_8h.md#ab6fe8f56a119810db6dd4146fcece444abda8bc3c6de747daab1b1b8468c4690e).

---

### `Unflatten()`

```cpp
status_t BKey::Unflatten(const BMessage & message)
```

Unflatten the key from a *message*. 



**Since:** Haiku R1

---

### `Unset()`

```cpp
void BKey::Unset()
```

Reset the values of the key. 


All properties of the key will be reset, except for the identifying owner.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBKey.html).
