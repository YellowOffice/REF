---
name: BCursor
type: class
kit: application_kit
brief: "BCursor describes a view-wide or application-wide cursor"
source: haiku-book
---

# BCursor Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

[BCursor](classBCursor.md) describes a view-wide or application-wide cursor. 



> [!NOTE]
> As BeOS only supports 16x16 monochrome cursors, to see a nice shadowed one we will need to extend this.



**Since:** BeOS R5

## Member List

### Public Member Functions

* [BCursor](#a9efcd878c804b2560bd8d390a0cce271) (BCursorID id) — Initializes a new cursor object from a predefined cursor id.
* [BCursor](#aecc135bb1461a1efd78f533fc6ede17c) (BMessage *data) — Initializes a new cursor object from a message archive.
* [BCursor](#afa8336bae1b43af072e1c855960fd5fe) (const BBitmap *bitmap, const BPoint &hotspot) — Initializes a new cursor object from a bitmap object and a point object.
* [BCursor](#a99346e06fb84879d585128434ef054f2) (const BCursor &other) — Initializes a new cursor object from another cursor object.
* [BCursor](#acb25a7b77241256c875e0e5ee035d75a) (const void *cursorData) — Initializes a new cursor object.
* `virtual` [~BCursor](#a951045e9f31f6bb4f399a4dfed2ab431) () — Destroy the cursor and free its memory.
* `virtual status_t` [Archive](#acae76743745b2ed1fd08de01edab9279) (BMessage *archive, bool deep=true) const — Archive the cursor. Not implemented.
* `status_t` [InitCheck](#ae6e4bf15d00a7e6a1c9c89fc2350335a) () const — Returns the initialization status.
* `bool` [operator!=](#a85b3eeae79027ff31368e11187a54bbe) (const BCursor &other) const — Compare a cursor object to another and return if they are not equal.
* `BCursor &` [operator=](#abddb994e8702bec22faf730e833786b5) (const BCursor &other) — Set the cursor to another cursor object.
* `bool` [operator==](#a9cdc3210c31eea70f7f949a8fd85ebc4) (const BCursor &other) const — Compare a cursor object to another and return if they are equal.

### Static Public Member Functions

* `static BArchivable *` [Instantiate](#a1484d01de98c4d4e2e1b900b48cd47f7) (BMessage *archive) — Instantiate the cursor from a message. Not implemented.

## Detailed Member Documentation

### `BCursor()`

```cpp
BCursor::BCursor(const void * cursorData)
```

Initializes a new cursor object. 


If the *cursorData* parameter is not `NULL` then the cursor is initialized with the cursor data.


Parameters

| Parameter | Description |
| :--- | :--- |
| `cursorData` | The cursor data. |





**Since:** BeOS R5

---

### `BCursor()`

```cpp
BCursor::BCursor(const BCursor & other)
```

Initializes a new cursor object from another cursor object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The cursor object to initialize from. |





**Since:** BeOS R5

---

### `BCursor()`

```cpp
BCursor::BCursor(BCursorID id)
```

Initializes a new cursor object from a predefined cursor *id*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `id` | The predefined *id* to initialize to. |





**Since:** BeOS R5

---

### `BCursor()`

```cpp
BCursor::BCursor(BMessage * data)
```

Initializes a new cursor object from a message archive. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The message data to initialize from. |





**Since:** BeOS R5

---

### `BCursor()`

```cpp
BCursor::BCursor(const BBitmap * bitmap, const BPoint & hotspot)
```

Initializes a new cursor object from a bitmap object and a point object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The bitmap object to initialize from. |
| `hotspot` | The cursor hotspot. |





**Since:** Haiku R1

---

### `~BCursor()`

```cpp
BCursor::~BCursor()
```

Destroy the cursor and free its memory. 



**Since:** BeOS R5

---

### `Archive()`

```cpp
status_t BCursor::Archive(BMessage * into, bool deep = true)const
```

Archive the cursor. Not implemented. 



**Since:** BeOS R5


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44).

---

### `InitCheck()`

```cpp
status_t BCursor::InitCheck()const
```

Returns the initialization status. 



**Returns:** `B_OK` if the object was properly initialized or an error code otherwise.



**Since:** Haiku R1

---

### `Instantiate()`

```cpp
BArchivable * BCursor::Instantiate(BMessage * archive)
```

Instantiate the cursor from a message. Not implemented. 



**Since:** BeOS R5

---

### `operator!=()`

```cpp
bool BCursor::operator!=(const BCursor & other)const
```

Compare a cursor object to another and return if they are not equal. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The cursor object to compare to. |





**Returns:** `true` if the cursor objects are not equal, `false` if the cursor objects are equal.



**Since:** BeOS R5

---

### `operator=()`

```cpp
BCursor & BCursor::operator=(const BCursor & other)
```

Set the cursor to another cursor object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The cursor object to copy from. |





**Returns:** the new cursor object.



**Since:** BeOS R5

---

### `operator==()`

```cpp
bool BCursor::operator==(const BCursor & other)const
```

Compare a cursor object to another and return if they are equal. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The cursor object to compare to. |





**Returns:** `true` if the cursor objects are equal, `false` if the cursor objects are not equal.



**Since:** BeOS R5

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBCursor.html).
