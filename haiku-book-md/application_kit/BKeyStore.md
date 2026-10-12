---
name: BKeyStore
type: class
kit: application_kit
brief: "The BKeyStore lets you query, retrieve and store keys in the system's key store"
source: haiku-book
---

# BKeyStore Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

The [BKeyStore](classBKeyStore.md) lets you query, retrieve and store keys in the system's key store. 


Instances of this object give you an easy API to interact with the system's `keystore_server`. This is the central service that manages storing and retrieving keys, as well as managing the authorizations that a user grants to individual applications.


It is important to note that all calls on this object operate **synchronously**. This means that it should not be used during the event loop of a visible [BWindow](../interface_kit/classBWindow.md), as this may cause drawing and interaction issues.


All operations are performed in the context of a keyring. All systems have at least the **Master** **keyring**. Many of the methods take the name of the keyring as its first argument. Most of the methods in this class have an overloaded variant that operate on the Master keyring. If you want to access this keyring through the normal methods, pass an empty string as the identifier to the method.


See the [overview to the Password and Key Storage API](app_keystore.md) for an introduction to the API.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BKeyStore](#af8f574a3730645d3127e7adbc78bc757) () — Create a new BKeyStore object that you can use to query, retrieve and store keys in the system's key store.
* `virtual` [~BKeyStore](#a43442117cd22e25371191eec17c0973a) () — Free all resources.
* `status_t` [GetKey](#a1512f697b5398543f7668cd5358f4fb4) (BKeyType type, const char *identifier, BKey &key) — Query the Master keyring for for specific key.
* `status_t` [GetKey](#a09219e0fefeff7f875717eb980aaa6c3) (BKeyType type, const char *identifier, const char *secondaryIdentifier, BKey &key) — Query the Master keyring for for specific key.
* `status_t` [GetKey](#a00f53c4eec45515821cb2e362c258909) (BKeyType type, const char *identifier, const char *secondaryIdentifier, bool secondaryIdentifierOptional, BKey &key) — Query the Master keyring for for specific key.
* `status_t` [GetKey](#a56cf7a18c18a5af9b29f04c3dc6c426b) (const char *keyring, BKeyType type, const char *identifier, BKey &key) — Query a certain keyring for for specific key.
* `status_t` [GetKey](#a860415deade3c8192e1790d6971b5b71) (const char *keyring, BKeyType type, const char *identifier, const char *secondaryIdentifier, BKey &key) — Query a certain keyring for for specific key.
* `status_t` [GetKey](#afd7ab0096a5cb8877930523ed5ab9b3a) (const char *keyring, BKeyType type, const char *identifier, const char *secondaryIdentifier, bool secondaryIdentifierOptional, BKey &key) — Query a certain keyring for for specific key.
* `status_t` [AddKey](#a758592b27bbd551b3c67452eb73f7f61) (const BKey &key) — Add a key to the Master keyring.
* `status_t` [AddKey](#aaa80a2acbb55d9e6a65454b407dd4188) (const char *keyring, const BKey &key) — Add a key to a keyring.
* `status_t` [RemoveKey](#af509aae99028fc2c828b25df258fe17d) (const BKey &key) — Remove a key from the Master keyring.
* `status_t` [RemoveKey](#a2fae39a5ac3ccb3caff10563abb3ba26) (const char *keyring, const BKey &key) — Remove a key from a keyring.
* `status_t` [GetNextKey](#a2b19dd024340ae18fdcbdc2e9feb69ce) (uint32 &cookie, BKey &key) — Iterate through the keys of the Master keyring.
* `status_t` [GetNextKey](#a0ec659c6898e11801c98882de90641c6) (BKeyType type, BKeyPurpose purpose, uint32 &cookie, BKey &key) — Iterate through the keys of the Master keyring.
* `status_t` [GetNextKey](#a32d03049f56892650d33118d0de97012) (const char *keyring, uint32 &cookie, BKey &key) — Iterate through the keys of a keyring.
* `status_t` [GetNextKey](#a5c3667e7021aa20fa2455b8d39c8463f) (const char *keyring, BKeyType type, BKeyPurpose purpose, uint32 &cookie, BKey &key) — Iterate through keys of a keyring.
* `status_t` [AddKeyring](#a21196565a98779d7f453b34a83defffc) (const char *keyring) — Create a new keyring.
* `status_t` [RemoveKeyring](#adcbf50f1b4407c419ddf3df895f7c454) (const char *keyring) — Remove a keyring.
* `status_t` [GetNextKeyring](#a6e383f92d6b016acc46ea3d7a7dbee94) (uint32 &cookie, BString &keyring) — Iterate through the keyrings.
* `status_t` [SetUnlockKey](#aafe09eb784e5ef120ab40bf62663197b) (const char *keyring, const BKey &key) — Not implemented.
* `status_t` [RemoveUnlockKey](#a8afb38ec314d18af3c51036d97b053b9) (const char *keyring) — Not implemented.
* `status_t` [SetMasterUnlockKey](#a44b7f9f78c28c16502e586556c497560) (const BKey &key) — Not implemented.
* `status_t` [RemoveMasterUnlockKey](#a7829451ada875e5ec8997326fe40fb6c) () — Not implemented.
* `status_t` [AddKeyringToMaster](#a14c38ee17ef5154b586eb4d868163a2d) (const char *keyring) — Not implemented.
* `status_t` [RemoveKeyringFromMaster](#aefa08ee4b2b53cecdab266c6799cd404) (const char *keyring) — Not implemented.
* `status_t` [GetNextMasterKeyring](#a18518e740545ba785f62d30ef1c8db0d) (uint32 &cookie, BString &keyring) — Not implemented.
* `bool` [IsKeyringUnlocked](#a2304e4edab4b11d81d33722abef33905) (const char *keyring) — Not implemented.
* `status_t` [LockKeyring](#a1c2bab7d0a7f71e73e35ff394049034f) (const char *keyring) — Not implemented.
* `status_t` [LockMasterKeyring](#aa8236dcace3de6a2c9591c34c7471543) () — Not implemented.
* `status_t` [GetNextApplication](#afc5dcda17cd81a5655c4fb53c17f355b) (uint32 &cookie, BString &signature) const — Iterate through applications that currently have been granted access to the Master keyring.
* `status_t` [GetNextApplication](#aa25e51e43046e1182d7da255b87e8c84) (const char *keyring, uint32 &cookie, BString &signature) const — Iterate through applications that currently have been granted access to the specified keyring.
* `status_t` [RemoveApplication](#a3a366f827bc86231c5980b35235f4005) (const char *signature) — Remove access for an application to the Master keyring.
* `status_t` [RemoveApplication](#a6b597f86b5ada490cf18e621ee8bb7d4) (const char *keyring, const char *signature) — Remove access for an application to a keyring.
* `status_t` [GeneratePassword](#a42d144264431359d4c866e49d1a59e43) (BPasswordKey &password, size_t length, uint32 flags) — Unimplemented.
* `float` [PasswordStrength](#a3b48121eec2387ca02f6d744d30bbbb7) (const char *password) — Unimplemented.

## Detailed Member Documentation

### `BKeyStore()`

```cpp
BKeyStore::BKeyStore()
```

Create a new [BKeyStore](classBKeyStore.md) object that you can use to query, retrieve and store keys in the system's key store. 


This is a cheap object to make, as it has no data associated with it. The recommended use is to create an instance on the stack whenever you want to interact with the API.



**Since:** Haiku R1

---

### `~BKeyStore()`

```cpp
BKeyStore::~BKeyStore()
```

Free all resources. 



**Since:** Haiku R1

---

### `AddKey()`

```cpp
status_t BKeyStore::AddKey(const BKey & key)
```

Add a *key* to the Master keyring. 


This is a convenience method that calls [AddKey(const char *, const BKey&)](classBKeyStore.md#aaa80a2acbb55d9e6a65454b407dd4188) for the `Master` keyring.



**Since:** Haiku R1

---

### `AddKey()`

```cpp
status_t BKeyStore::AddKey(const char * keyring, const BKey & key)
```

Add a *key* to a *keyring*. 


This method will send the key to the `keystore_server` and request it to be stored in the database.


A key needs to have a unique primary and secondary identifier within the Master keyring.


Parameters

| Parameter | Description |
| :--- | :--- |
| `keyring` | A string that identifies the keyring you want to add the key to. |
| `key` | The key you want to add. |





**Returns:** * `B_OK` in case the *key* was succesfully added.

* `B_BAD_VALUE` in case the *keyring* does not exist.

* `B_NOT_ALLOWED` in case the user did not grant you access right to this *keyring*.

* `B_NAME_IN_USE` in case there already is another key with the same primary and secondary identifiers.

* Any other error that indicates that there was a problem communicating with the `keystore_server`.



**Since:** Haiku R1

---

### `AddKeyring()`

```cpp
status_t BKeyStore::AddKeyring(const char * keyring)
```

Create a new *keyring*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `keyring` | An UTF-8 string that identifies the keyring you want to create. |





**Returns:** * `B_OK` if the keyring was succesfully added.

* `B_NAME_IN_USE` if the *keyring* already exists.

* Any other error in case there was an unknown error in the `keystore_server`, or while communicating to it.



**Since:** Haiku R1

---

### `AddKeyringToMaster()`

```cpp
status_t BKeyStore::AddKeyringToMaster(const char * keyring)
```

Not implemented. 


This feature is not available in the current release of Haiku.



**See also:** [AddKeyring(const char* keyring)](classBKeyStore.md#a21196565a98779d7f453b34a83defffc)

---

### `GeneratePassword()`

```cpp
status_t BKeyStore::GeneratePassword(BPasswordKey & password, size_t length, uint32 flags)
```

Unimplemented. 


This method is currently not implemented.

---

### `GetKey()`

```cpp
status_t BKeyStore::GetKey(BKeyType type, const char * identifier, BKey & key)
```

Query the Master keyring for for specific key. 


This is a convenience method that calls [GetKey(const char* keyring, BKeyType type, const char* identifier, const char* secondaryIdentifier, bool secondaryIdentifierOptional, BKey& key)](classBKeyStore.md#afd7ab0096a5cb8877930523ed5ab9b3a).


It works on the Master *keyring*, and assumes an empty *secondaryIdentifier*, *secondaryIdentifierOptional* set to `false`.



**Since:** Haiku R1

---

### `GetKey()`

```cpp
status_t BKeyStore::GetKey(BKeyType type, const char * identifier, const char * secondaryIdentifier, BKey & key)
```

Query the Master keyring for for specific key. 


This is a convenience method that calls [GetKey(const char* keyring, BKeyType type, const char* identifier, const char* secondaryIdentifier, bool secondaryIdentifierOptional, BKey& key)](classBKeyStore.md#afd7ab0096a5cb8877930523ed5ab9b3a).


It works on the Master *keyring*, it sets *secondaryIdentifierOptional* to `false`, meaning it both identifiers are required to match.



**Since:** Haiku R1

---

### `GetKey()`

```cpp
status_t BKeyStore::GetKey(BKeyType type, const char * identifier, const char * secondaryIdentifier, bool secondaryIdentifierOptional, BKey & key)
```

Query the Master keyring for for specific key. 


This is a convenience method that calls [GetKey(const char* keyring, BKeyType type, const char* identifier, const char* secondaryIdentifier, bool secondaryIdentifierOptional, BKey& key)](classBKeyStore.md#afd7ab0096a5cb8877930523ed5ab9b3a).


It works on the Master *keyring*.



**Since:** Haiku R1

---

### `GetKey()`

```cpp
status_t BKeyStore::GetKey(const char * keyring, BKeyType type, const char * identifier, BKey & key)
```

Query a certain *keyring* for for specific key. 


This is a convenience method that calls [GetKey(const char* keyring, BKeyType type, const char* identifier, const char* secondaryIdentifier, bool secondaryIdentifierOptional, BKey& key)](classBKeyStore.md#afd7ab0096a5cb8877930523ed5ab9b3a).


The call assumes an empty *secondaryIdentifier*, and sets *secondaryIdentifierOptional* to `false`.



**Since:** Haiku R1

---

### `GetKey()`

```cpp
status_t BKeyStore::GetKey(const char * keyring, BKeyType type, const char * identifier, const char * secondaryIdentifier, BKey & key)
```

Query a certain *keyring* for for specific key. 


This is a convenience method that calls [GetKey(const char* keyring, BKeyType type, const char* identifier, const char* secondaryIdentifier, bool secondaryIdentifierOptional, BKey& key)](classBKeyStore.md#afd7ab0096a5cb8877930523ed5ab9b3a).


It sets *secondaryIdentifierOptional* to `false`, meaning it both identifiers are required to match.



**Since:** Haiku R1

---

### `GetKey()`

```cpp
status_t BKeyStore::GetKey(const char * keyring, BKeyType type, const char * identifier, const char * secondaryIdentifier, bool secondaryIdentifierOptional, BKey & key)
```

Query a certain *keyring* for for specific key. 


This variation of the query function is useful when you know that a key has a secondary identifier, but you may not know it, or care about what it is.


Parameters

| Parameter | Description |
| :--- | :--- |
| `keyring` | A string that identifies the keyring get the key from. |
| `type` | The type of key to match. The type parameter is currently ignored and therefore does not need to match the actual type of the key that is stored. |
| `identifier` | The string with the primary identifier of the key that you are looking for. |
| `secondaryIdentifier` | The string with the secondary identifier of the key that you are looking for. |
| `secondaryIdentifierOptional` | Use this query parameter to indicate if the secondary identifier has to match. When set to *true*, a result will be returned, even if the *secondaryIdentifier* does not match. |
| `key` | A [BKey](classBKey.md) object to copy the found data to. Any existing data in the key will be overwritten in case there is a match. |





**Returns:** * `B_OK` in case the key was found and stored in *key*.

* `B_BAD_VALUE` in case the *keyring* does not exist.

* `B_NOT_ALLOWED` in case the user did not grant you access right to this *keyring*.

* `B_ENTRY_NOT_FOUND` in case there is no key that matches the given identifier(s).

* Any other error that indicates that there was a problem communicating with the `keystore_server`.



**Since:** Haiku R1

---

### `GetNextApplication()`

```cpp
status_t BKeyStore::GetNextApplication(const char * keyring, uint32 & cookie, BString & signature)const
```

Iterate through applications that currently have been granted access to the specified *keyring*. 


This method allows you to iterate through all applications that the user has granted access to the *keyring*, whether it is temporarily, or on a more permanent basis.


Parameters

| Parameter | Description |
| :--- | :--- |
| `keyring` | A UTF-8 string that identifies the keyring that you want to inspect granted access to. |
| `cookie` | A cookie that the `keystore_server` uses to keep track of where you are in the list of keys. When you start the query, set the initial value to `0`. After that, pass the cookie to each subsequent call to progress the iterator. |
| `signature` | If a next application is found, the signature will be stored in this parameter. Any existing string will be overwritten. |





**Returns:** * `B_OK` if the next signature was found succesfully.

* `B_BAD_VALUE` if the keyring does not exist.

* `B_NOT_ALLOWED` in case the user did not grant you access right to this *keyring*.

* `B_ENTRY_NOT_FOUND` if there are no more applications to iterate through.

* Any other error in case there was an unknown error in the `keystore_server`, or while communicating to it.



**Since:** Haiku R1

---

### `GetNextApplication()`

```cpp
status_t BKeyStore::GetNextApplication(uint32 & cookie, BString & signature)const
```

Iterate through applications that currently have been granted access to the Master keyring. 


This is a convenience method that calls GetNextApplication(const char* keyring, uint32& cookie,
BString& signature) for the Master *keyring*.



**Since:** Haiku R1

---

### `GetNextKey()`

```cpp
status_t BKeyStore::GetNextKey(BKeyType type, BKeyPurpose purpose, uint32 & cookie, BKey & key)
```

Iterate through the keys of the Master keyring. 


This convenience method calls [GetNextKey(const char*, BKeyType, BKeyPurpose, uint32&, BKey&)](classBKeyStore.md#a5c3667e7021aa20fa2455b8d39c8463f) for the Master keyring.



**Since:** Haiku R1

---

### `GetNextKey()`

```cpp
status_t BKeyStore::GetNextKey(const char * keyring, BKeyType type, BKeyPurpose purpose, uint32 & cookie, BKey & key)
```

Iterate through keys of a *keyring*. 


This method allows you to query through the key store, and iterate through a list of results of keys that match your query.


Parameters

| Parameter | Description |
| :--- | :--- |
| `keyring` | An UTF-8 string that identifies the keyring |
| `type` | The BKeyType that identifies the type of key you are looking for. This may be BKeyType::B_KEY_TYPE_ANY if it may be a key of any type. |
| `purpose` | The BKeyPurpose that indicates the purpose of the key. This may be BKeyPurpose::B_KEY_PURPOSE_ANY if it may be a key with any purpose. |
| `cookie` | A cookie that the `keystore_server` uses to keep track of where you are in the list of keys. When you start the query, set the initial value to `0`. After that, pass the cookie to each subsequent call to progress the iterator. |
| `key` | The key that holds the data. Any existing data in the key will be overwritten, when a key is found that matches the criteria. |





**Returns:** * `B_OK` in case the next *key* was found.

* `B_BAD_VALUE` in case the *keyring* does not exist.

* `B_NOT_ALLOWED` in case the user did not grant you access right to this *keyring*.

* `B_ENTRY_NOT_FOUND` in case there is no key that matches the given identifier(s), or if you retrieved the last key.

* Any other error that indicates that there was a problem communicating with the `keystore_server`.



**Since:** Haiku R1

---

### `GetNextKey()`

```cpp
status_t BKeyStore::GetNextKey(const char * keyring, uint32 & cookie, BKey & key)
```

Iterate through the keys of a *keyring*. 


This convenience method calls [GetNextKey(const char*, BKeyType, BKeyPurpose, uint32&, BKey&)](classBKeyStore.md#a5c3667e7021aa20fa2455b8d39c8463f) with the arguments BKeyType::B_KEY_TYPE_ANY for the type and BKeyPurpose::B_KEY_PURPOSE_ANY for the purpose.



**Since:** Haiku R1

---

### `GetNextKey()`

```cpp
status_t BKeyStore::GetNextKey(uint32 & cookie, BKey & key)
```

Iterate through the keys of the Master keyring. 


This convenience method that calls [GetNextKey(const char*, BKeyType, BKeyPurpose, uint32&, BKey&)](classBKeyStore.md#a5c3667e7021aa20fa2455b8d39c8463f) for the Master keyring, with the arguments BKeyType::B_KEY_TYPE_ANY for the type and BKeyPurpose::B_KEY_PURPOSE_ANY for the purpose.



**Since:** Haiku R1

---

### `GetNextKeyring()`

```cpp
status_t BKeyStore::GetNextKeyring(uint32 & cookie, BString & keyring)
```

Iterate through the keyrings. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `cookie` | A cookie that the `keystore_server` uses to keep track of where you are in the list of keyrings. When you start the query, set the initial value to `0`. After that, pass the cookie to each subsequent call to progress the iterator. |
| `keyring` | A [BString](../support_kit/classBString.md) that holds the current name of the keyring. For each succesful iteration, the existing contents is overwritten. |





**Returns:** * `B_OK` if the iteration was succesful.

* `B_ENTRY_NOT_FOUND` if there are no more keyrings left to iterate

* Any other error in case there was an unknown error in the `keystore_server`, or while communicating to it.



**Since:** Haiku R1

---

### `GetNextMasterKeyring()`

```cpp
status_t BKeyStore::GetNextMasterKeyring(uint32 & cookie, BString & keyring)
```

Not implemented. 


This feature is not available in the current release of Haiku.



**See also:** [GetNextKeyring(uint32& cookie, BString& keyring)](classBKeyStore.md#a6e383f92d6b016acc46ea3d7a7dbee94)

---

### `IsKeyringUnlocked()`

```cpp
bool BKeyStore::IsKeyringUnlocked(const char * keyring)
```

Not implemented. 


This feature is not available in the current release of Haiku.

---

### `LockKeyring()`

```cpp
status_t BKeyStore::LockKeyring(const char * keyring)
```

Not implemented. 


This feature is not available in the current release of Haiku.

---

### `LockMasterKeyring()`

```cpp
status_t BKeyStore::LockMasterKeyring()
```

Not implemented. 


This feature is not available in the current release of Haiku.

---

### `PasswordStrength()`

```cpp
float BKeyStore::PasswordStrength(const char * password)
```

Unimplemented. 


This method is currently not implemented

---

### `RemoveApplication()`

```cpp
status_t BKeyStore::RemoveApplication(const char * keyring, const char * signature)
```

Remove access for an application to a *keyring*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `keyring` | A UTF-8 string that identifies the keyring that you want to inspect granted access to. |
| `signature` | The signature of the application that you want to revoke permissions to access the keyring. |





**Returns:** * `B_OK` if the application's access has been revoked.

* `B_NOT_ALLOWED` in case the user did not grant you access right to this *keyring*.

* `B_ENTRY_NOT_FOUND` if the application did not have access to this keyring.

* Any other error in case there was an unknown error in the `keystore_server`, or while communicating to it.



**Since:** Haiku R1

---

### `RemoveApplication()`

```cpp
status_t BKeyStore::RemoveApplication(const char * signature)
```

Remove access for an application to the Master keyring. 


This is a convenience method that calls [RemoveApplication(const char *, const char*)](classBKeyStore.md#a6b597f86b5ada490cf18e621ee8bb7d4) for the Master *keyring*.



**Since:** Haiku R1

---

### `RemoveKey()`

```cpp
status_t BKeyStore::RemoveKey(const BKey & key)
```

Remove a *key* from the Master keyring. 


This is a convenience method that calls [RemoveKey(const char *, const BKey&)](classBKeyStore.md#a2fae39a5ac3ccb3caff10563abb3ba26) for the `Master` keyring.



**Since:** Haiku R1

---

### `RemoveKey()`

```cpp
status_t BKeyStore::RemoveKey(const char * keyring, const BKey & key)
```

Remove a *key* from a *keyring*. 


This method will remove a *key* from a *keyring*. The *key* needs to match exactly with the key that is in the database of `keystore_server`. The easiest way to guarantee this, is to use the exact key you find using [GetKey()](classBKeyStore.md#a1512f697b5398543f7668cd5358f4fb4) without making any alterations.


Parameters

| Parameter | Description |
| :--- | :--- |
| `keyring` | A string that identifies the keyring you want to remove the key from. |
| `key` | The key you want to remove. |





**Returns:** * `B_OK` in case the *key* was succesfully removed.

* `B_BAD_VALUE` in case the *keyring* does not exist.

* `B_NOT_ALLOWED` in case the user did not grant you access right to this *keyring*.

* `B_ENTRY_NOT_FOUND` in case there is no key that matches the given identifier(s).

* Any other error that indicates that there was a problem communicating with the `keystore_server`.



**Since:** Haiku R1

---

### `RemoveKeyring()`

```cpp
status_t BKeyStore::RemoveKeyring(const char * keyring)
```

Remove a *keyring*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `keyring` | An UTF-8 string that identifies the keyring you want to remove. |





**Returns:** * `B_OK` if the keyring was sucessfully removed.

* `B_ENTRY_NOT_FOUND` if the keyring does not exist

* `B_NOT_ALLOWED` when you try to remove the Master keyring.

* Any other error in case there was an unknown error in the `keystore_server`, or while communicating to it.



**Since:** Haiku R1

---

### `RemoveKeyringFromMaster()`

```cpp
status_t BKeyStore::RemoveKeyringFromMaster(const char * keyring)
```

Not implemented. 


This feature is not available in the current release of Haiku.



**See also:** [RemoveKeyring(const char* keyring)](classBKeyStore.md#adcbf50f1b4407c419ddf3df895f7c454)

---

### `RemoveMasterUnlockKey()`

```cpp
status_t BKeyStore::RemoveMasterUnlockKey()
```

Not implemented. 


This feature is not available in the current release of Haiku.

---

### `RemoveUnlockKey()`

```cpp
status_t BKeyStore::RemoveUnlockKey(const char * keyring)
```

Not implemented. 


This feature is not available in the current release of Haiku.

---

### `SetMasterUnlockKey()`

```cpp
status_t BKeyStore::SetMasterUnlockKey(const BKey & key)
```

Not implemented. 


This feature is not available in the current release of Haiku.

---

### `SetUnlockKey()`

```cpp
status_t BKeyStore::SetUnlockKey(const char * keyring, const BKey & key)
```

Not implemented. 


This feature is not available in the current release of Haiku.

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBKeyStore.html).
