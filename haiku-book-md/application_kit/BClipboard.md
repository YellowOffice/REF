---
name: BClipboard
type: class
kit: application_kit
brief: "Used for short-term data storage between documents and applications via copy and paste operations"
source: haiku-book
---

# BClipboard Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Used for short-term data storage between documents and applications via copy and paste operations. 


Clipboards are differentiated by their name. In order for two applications to share a clipboard they simply have to create a [BClipboard](classBClipboard.md) object with the same name. However, it is rarely necessary to create your own clipboard, instead you can use the `be_clipboard` system clipboard object.


RemarksTo access the system clipboard without a [BApplication](classBApplication.md) object, create a [BClipboard](classBClipboard.md) object with the name "system". You should avoid creating a custom clipboard with the name "system" for your own use.
To access the clipboard data call the [Data()](classBClipboard.md#a8725f40981256bce5e63ef7b5c70f9b4) method. The [BMessage](classBMessage.md) object returned by the [Data()](classBClipboard.md#a8725f40981256bce5e63ef7b5c70f9b4) method has the following properties:


* The `what` value is unused.

* The clipboard data is stored in a message field typed as `B_MIME_TYPE`.

* The MIME type of the data is used as the name of the field that holds the data.

* Each field in the data message contains the same data with a different format.



To read and write to the clipboard you must first lock the [BClipboard](classBClipboard.md) object. If you fail to lock the [BClipboard](classBClipboard.md) object then the [Data()](classBClipboard.md#a8725f40981256bce5e63ef7b5c70f9b4) method will return `NULL` instead of a pointer to a [BMessage](classBMessage.md) object.


Below is an example of reading a string from the system clipboard. 


```cpp
const char *string;
int32 stringLen;
if (be_clipboard->Lock()) {
 // Get the clipboard BMessage
 BMessage *clip = be_clipboard->Data();
 
 // Read the string from the clipboard data message
    clip->FindData("text/plain", B_MIME_TYPE, (const void **)&string,
        &stringLen);
 
 be_clipboard->Unlock();
} else
    fprintf(stderr, "could not lock clipboard.\n");
```

Below is an example of writing a string to the system clipboard. 


```cpp
const char* string = "Some clipboard data";
 
if (be_clipboard->Lock()) {
 // Clear the clipboard data
 be_clipboard->Clear();
 
 // Get the clipboard data message
 BMessage *clip = be_clipboard->Data();
 
 // Write string data to the clipboard data message
    clip->AddData("text/plain", B_MIME_TYPE, string, strlen(string));
 
 // Commit the data to the clipboard
    status = be_clipboard->Commit();
 if (status != B_OK)
        fprintf(stderr, "could not commit data to clipboard.\n");
 
 be_clipboard->Unlock();
} else
    fprintf(stderr, "could not lock clipboard.\n");
```


**Since:** BeOS R3

## Member List

### Public Member Functions

* [BClipboard](#aad708b905729146ba078a4e64ea6b0b4) (const char *name, bool transient=false) — Create a BClipboard object with the given name.
* `virtual` [~BClipboard](#a61c6c94d8bbcb9853615c97e3ace0d2f) () — Destroys the BClipboard object. The clipboard data is not destroyed.
* `const char *` [Name](#ac65770020e3178d6af8788a2bb196e81) () const — Returns the name of the BClipboard object.
* `uint32` [LocalCount](#a3ebf50bcad5524840398ef5c3aa67af2) () const — Returns the (locally cached) number of commits to the clipboard.
* `uint32` [SystemCount](#ad338ae61edc9c6d1df73be89cd903afa) () const — Returns the number of commits to the clipboard.
* `status_t` [StartWatching](#a8edb82d5df9abb96a2273ea969e69e4c) (BMessenger target) — Start watching the BClipboard object for changes.
* `status_t` [StopWatching](#a52dfd633666d0de9e8180e94277209da) (BMessenger target) — Stop watching the BClipboard object for changes.
* `bool` [Lock](#af6739195b86ae73b7f8c16bb17ebb66c) () — Locks the clipboard so that no other tread can read from it or write to it.
* `void` [Unlock](#afb846e47951f042740d81d0acdd3d078) () — Unlocks the clipboard.
* `bool` [IsLocked](#a1397fc057cff4f3bb7abd1f99970ae22) () const — Returns whether or not the clipboard is locked.
* `status_t` [Clear](#ab761d1164ce410618671312d2f9d6e70) () — Clears out all data from the clipboard.
* `status_t` [Commit](#a987a3b6c6e9bc68e3d1b471fb71457fc) () — Commits the clipboard data to the BClipboard object.
* `status_t` [Commit](#adb941a4d7b920486c96faa7491c8cab1) (bool failIfChanged) — Commits the clipboard data to the BClipboard object with the option to fail if there is a change to the clipboard data.
* `status_t` [Revert](#a5393effd0c6f1eb5b6794a4bc9d9768f) () — Reverts the clipboard data.
* `BMessenger` [DataSource](#ad52756e9ae1b1ea7e59425c591b25703) () const — Gets a BMessenger object targeting the application that last modified the clipboard.
* `BMessage *` [Data](#a8725f40981256bce5e63ef7b5c70f9b4) () const — Gets a pointer to the BMessage object that holds the clipboard data.

## Detailed Member Documentation

### `BClipboard()`

```cpp
BClipboard::BClipboard(const char * name, bool transient = false)
```

Create a [BClipboard](classBClipboard.md) object with the given *name*. 


If the *name* parameter is `NULL` then the "system" [BClipboard](classBClipboard.md) object is constructed instead.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The *name* of the clipboard. |
| `transient` | If `true`, lose data after a reboot (currently unused). |





**Since:** BeOS R3

---

### `~BClipboard()`

```cpp
BClipboard::~BClipboard()
```

Destroys the [BClipboard](classBClipboard.md) object. The clipboard data is not destroyed. 



**Since:** BeOS R3

---

### `Clear()`

```cpp
status_t BClipboard::Clear()
```

Clears out all data from the clipboard. 


You should call [Clear()](classBClipboard.md#ab761d1164ce410618671312d2f9d6e70) before adding new data to the [BClipboard](classBClipboard.md) object.



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went find. |
| B_NOT_ALLOWED | The clipboard is not locked. |
| B_NO_MEMORY | Ran out of memory initializing the data message. |
| B_ERROR | Another error occurred. |





**Since:** BeOS R3

---

### `Commit()`

```cpp
status_t BClipboard::Commit()
```

Commits the clipboard data to the [BClipboard](classBClipboard.md) object. 



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went find. |
| B_NOT_ALLOWED | The clipboard is not locked. |
| B_ERROR | Another error occurred. |





**Since:** BeOS R3

---

### `Commit()`

```cpp
status_t BClipboard::Commit(bool failIfChanged)
```

Commits the clipboard data to the [BClipboard](classBClipboard.md) object with the option to fail if there is a change to the clipboard data. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `failIfChanged` | Whether or not to fail to commit the changes if there is a change in the clipboard data. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went find. |
| B_NOT_ALLOWED | The clipboard is not locked. |
| B_ERROR | Another error occurred. |





**Since:** BeOS R5

---

### `Data()`

```cpp
BMessage * BClipboard::Data()const
```

Gets a pointer to the [BMessage](classBMessage.md) object that holds the clipboard data. 


If the [BClipboard](classBClipboard.md) object is not locked this method returns `NULL`.



**Returns:** A pointer to the [BMessage](classBMessage.md) object that holds the clipboard data or `NULL` if the clipboard is not locked.



**Since:** BeOS R3

---

### `DataSource()`

```cpp
BMessenger BClipboard::DataSource()const
```

Gets a [BMessenger](classBMessenger.md) object targeting the application that last modified the clipboard. 


The clipboard object does not need to be locked to call this method.



**Returns:** A [BMessenger](classBMessenger.md) object that targets the application that last modified the clipboard.



**Since:** BeOS R3

---

### `IsLocked()`

```cpp
bool BClipboard::IsLocked()const
```

Returns whether or not the clipboard is locked. 



**Returns:** `true` if the clipboard is locked, `false` if it is unlocked.



**Since:** BeOS R5

---

### `LocalCount()`

```cpp
uint32 BClipboard::LocalCount()const
```

Returns the (locally cached) number of commits to the clipboard. 


The returned value is the number of successful [Commit()](classBClipboard.md#a987a3b6c6e9bc68e3d1b471fb71457fc) invocations for the clipboard represented by this object, either invoked on this object or another (even from another application). This method returns a locally cached value, which might already be obsolete. For an up-to-date value use [SystemCount()](classBClipboard.md#ad338ae61edc9c6d1df73be89cd903afa).



**Returns:** The number of commits to the clipboard.



**See also:** [SystemCount()](classBClipboard.md#ad338ae61edc9c6d1df73be89cd903afa)



**Since:** BeOS R5

---

### `Lock()`

```cpp
bool BClipboard::Lock()
```

Locks the clipboard so that no other tread can read from it or write to it. 


You should call [Lock()](classBClipboard.md#af6739195b86ae73b7f8c16bb17ebb66c) before reading or writing to the clipboard.



**Returns:** `true` if the clipboard was locked, `false` otherwise.



**See also:** [Unlock()](classBClipboard.md#afb846e47951f042740d81d0acdd3d078)



**Since:** BeOS R3

---

### `Name()`

```cpp
const char * BClipboard::Name()const
```

Returns the name of the [BClipboard](classBClipboard.md) object. 



**Returns:** The name of the clipboard.



**Since:** BeOS R3

---

### `Revert()`

```cpp
status_t BClipboard::Revert()
```

Reverts the clipboard data. 


The method should be used in the case that you have made a change to the clipboard data message and then decide to revert the change instead of committing it.



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went find. |
| B_NOT_ALLOWED | The clipboard is not locked. |
| B_NO_MEMORY | Ran out of memory initializing the data message. |
| B_ERROR | Another error occurred. |





**Since:** BeOS R5

---

### `StartWatching()`

```cpp
status_t BClipboard::StartWatching(BMessenger target)
```

Start watching the [BClipboard](classBClipboard.md) object for changes. 


When a change in the clipboard occurs, most like as the result of a cut or copy action, a *B_CLIPBOARD_CHANGED* message is sent to *target*.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *target* is invalid. |
| B_ERROR | An error occured. |





**See also:** [StopWatching()](classBClipboard.md#a52dfd633666d0de9e8180e94277209da)



**Since:** BeOS R5

---

### `StopWatching()`

```cpp
status_t BClipboard::StopWatching(BMessenger target)
```

Stop watching the [BClipboard](classBClipboard.md) object for changes. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *target* is invalid. |
| B_ERROR | An error occurred. |





**See also:** [StartWatching()](classBClipboard.md#a8edb82d5df9abb96a2273ea969e69e4c)



**Since:** BeOS R5

---

### `SystemCount()`

```cpp
uint32 BClipboard::SystemCount()const
```

Returns the number of commits to the clipboard. 


The returned value is the number of successful [Commit()](classBClipboard.md#a987a3b6c6e9bc68e3d1b471fb71457fc) invocations for the clipboard represented by this object, either invoked on this object or another (even from another application). This method retrieves the value directly from the system service managing the clipboards, so it is more expensive, but more up-to-date than [LocalCount()](classBClipboard.md#a3ebf50bcad5524840398ef5c3aa67af2), which returns a locally cached value.



**Returns:** The number of commits to the clipboard.



**See also:** [LocalCount()](classBClipboard.md#a3ebf50bcad5524840398ef5c3aa67af2)



**Since:** BeOS R5

---

### `Unlock()`

```cpp
void BClipboard::Unlock()
```

Unlocks the clipboard. 



**See also:** [Lock()](classBClipboard.md#af6739195b86ae73b7f8c16bb17ebb66c)



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBClipboard.html).
