---
name: BPasswordKey
type: class
kit: application_kit
brief: "Class that represents a password for or from the Haiku key store"
source: haiku-book
---

# BPasswordKey Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Class that represents a password for or from the Haiku key store. 


This is a specialized version of the [BKey](classBKey.md) class, which represents a key of the BKeyType::B_KEY_TYPE_PASSWORD.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BPasswordKey](#aa667369ca41b313313374cfbf556c797) () — Constructor for an empty password key.
* [BPasswordKey](#a97d1797a04fae33d6ce5c87a0dd6c6e0) (BPasswordKey &other) — Copy constructor that makes a copy of an other BPasswordKey.
* [BPasswordKey](#abfd39eba0b2d9295af356dd591854e10) (const char *password, BKeyPurpose purpose, const char *identifier, const char *secondaryIdentifier=NULL) — Constructor for a password key with the provided data.
* `virtual` [~BPasswordKey](#af21b7ed6f6546491459478d7a56a23d2) () — Free all resources associated with this key.
* `const char *` [Password](#ad554ead88f376d5b86a35e19e63b346c) () const — Get the password for the key.
* `virtual void` [PrintToStream](#a64ff92b5e0fde95eef53112a99f868dc) () — Dump the contents of the key to standard output.
* `status_t` [SetPassword](#a2f68636af50e84b753a646c68fb17c2d) (const char *password) — Set the password for this key.
* `status_t` [SetTo](#a1beb95e09102cd23d24b10a97a566f34) (const char *password, BKeyPurpose purpose, const char *identifier, const char *secondaryIdentifier=NULL) — Set the key to specific values.
* `virtual BKeyType` [Type](#a8c53e208ace43023a7ed026bdf0938b6) () const — Returns BKeyType::B_KEY_TYPE_PASSWORD.
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

### `BPasswordKey()`

```cpp
BPasswordKey::BPasswordKey()
```

Constructor for an empty password key. 


An empty key has no data associated with it, other than that it has a generic purpose and a password key type.



**Since:** Haiku R1

---

### `BPasswordKey()`

```cpp
BPasswordKey::BPasswordKey(const char * password, BKeyPurpose purpose, const char * identifier, const char * secondaryIdentifier = NULL)
```

Constructor for a password key with the provided data. 


See the [BKey](classBKey.md) introduction for more information about the properties of a key. As you can see, the only required parameters are the *purpose* and the *identifier*. Any data you provide will be copied into the [BKey](classBKey.md) object.


Parameters

| Parameter | Description |
| :--- | :--- |
| `password` | A null-terminated string that contains the password |
| `purpose` | The purpose of this key |
| `identifier` | A unique identifier for this key |
| `secondaryIdentifier` | An (optional) secondary identifier for this key |





**Since:** Haiku R1

---

### `BPasswordKey()`

```cpp
BPasswordKey::BPasswordKey(BPasswordKey & other)
```

Copy constructor that makes a copy of an *other* [BPasswordKey](classBPasswordKey.md). 



**Since:** Haiku R1

---

### `~BPasswordKey()`

```cpp
BPasswordKey::~BPasswordKey()
```

Free all resources associated with this key. 



**Since:** Haiku R1

---

### `Password()`

```cpp
const char * BPasswordKey::Password()const
```

Get the password for the key. 



**Since:** Haiku R1

---

### `PrintToStream()`

```cpp
void BPasswordKey::PrintToStream()
```

Dump the contents of the key to standard output. 


This is a debug function that helps you read the contents of the key. All properties, including the actual **password**, will be printed to `stdout`.



**Since:** Haiku R1


Reimplemented from [BKey](classBKey.md#ac7cd25324b948b012a6e0cf16f940658).

---

### `SetPassword()`

```cpp
status_t BPasswordKey::SetPassword(const char * password)
```

Set the *password* for this key. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `password` | A null-terminated string that contains the password. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BPasswordKey::SetTo(const char * password, BKeyPurpose purpose, const char * identifier, const char * secondaryIdentifier = NULL)
```

Set the key to specific values. 


All properties of the key will be set to the parameters. If the key had a creation time set, it will be cleared. If there was an owner set, this piece of information will *not* be cleared.


Parameters

| Parameter | Description |
| :--- | :--- |
| `password` | A null-terminated string that contains the password |
| `purpose` | The purpose of this key |
| `identifier` | A unique identifier for this key |
| `secondaryIdentifier` | An (optional) secondary identifier for this key |





**Returns:** * `B_OK` if the changes were successful.

* `B_NO_MEMORY` in case it fails to allocate memory.



**Since:** Haiku R1

---

### `Type()`

```cpp
BKeyType BPasswordKey::Type()const
```

Returns BKeyType::B_KEY_TYPE_PASSWORD. 



**Since:** Haiku R1


Reimplemented from [BKey](classBKey.md#a7971f210c7d6805a415ec19dbae3038d).


References [B_KEY_TYPE_PASSWORD](Key_8h.md#ab6fe8f56a119810db6dd4146fcece444aed0cd6ae9d3daf69a44facdf0852836a).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPasswordKey.html).
