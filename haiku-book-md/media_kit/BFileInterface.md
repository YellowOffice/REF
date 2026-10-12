---
name: BFileInterface
type: class
kit: media_kit
brief: "A node that can read and write data to a file on disk"
source: haiku-book
---

# BFileInterface Class
**Kit/Group:** [Media Kit](../media_kit/group__media.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A node that can read and write data to a file on disk. 


You should derive your subclass from [BFileInterface](classBFileInterface.md) so that your application may specify the file that the node will reference. The Media Server will then call upon the node to try to identify and work with files that are hereunto unknown to it.


Your node must also derive from BBufferConsumer or BBufferProducer, in addition to [BFileInterface](classBFileInterface.md).

## Member List

### Protected Member Functions

* BFileInterface () — Constructor.
* `virtual` ~BFileInterface () — Destructor.
* `virtual void` [DisposeFileFormatCookie](#a99d5c4dfe9b028110fb3693bf97fcc1a) (int32 cookie)=0 — Implement this method to dispose of a file format supported by your node indexed by cookie.
* `virtual status_t` [GetDuration](#af16daa3210ffc3399cf8aa749895523f) (bigtime_t *_time)=0 — Implement this method to fill out the duration in microseconds of the media data contained in the currently referenced file in _time.
* `virtual status_t` [GetNextFileFormat](#a5cc3b4a49d5ade8a1357c4163a62c2e5) (int32 *cookie, media_file_format *_format)=0 — Implement this method to fill out information about a file format indexed by cookie.
* `virtual status_t` [GetRef](#a7544c7072ce649af46863a872f31d9b3) (entry_ref *_ref, char *_mimeType)=0 — Implement to set the entry_ref and the MIME type of the file referenced by the current node.
* `virtual status_t` [HandleMessage](#ab69c5000ffe084e34af54d1f2ad641e7) (int32 message, const void *data, size_t size) — Dispatches a message to the appropriate BMediaNode hook method given a message received on the control port. Implement this method to handle messages that arrive on your control port.
* `virtual status_t` [SetRef](#a95b3bf9e479102fe094c007cfdb8d7cd) (const entry_ref &file, bool create, bigtime_t *_time)=0 — Used when an application wants your node to use a specific file.
* `virtual status_t` [SniffRef](#a98d7947526061d8ee32474ecba68bc90) (const entry_ref &file, char *_mimeType, float *_quality)=0 — Implement this method to allow the Media Roster to identify a file format associated with this node.

## Detailed Member Documentation

### `DisposeFileFormatCookie()`

```cpp
void BFileInterface::DisposeFileFormatCookie(int32 cookie)
```

Implement this method to dispose of a file format supported by your node indexed by *cookie*. 


You are responsible for freeing any data blocks associated with this *cookie* before returning.


Parameters

| Parameter | Description |
| :--- | :--- |
| `cookie` | Index of the cookie you wish to dispose of. |

---

### `GetDuration()`

```cpp
status_t BFileInterface::GetDuration(bigtime_t * _time)
```

Implement this method to fill out the duration in microseconds of the media data contained in the currently referenced file in *_time*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `_time` | The duration parameter to fill out. |





**Returns:** A status code, typically `B_OK` on success and `B_ERROR` or another error code on error.

---

### `GetNextFileFormat()`

```cpp
status_t BFileInterface::GetNextFileFormat(int32 * cookie, media_file_format * _format)
```

Implement this method to fill out information about a file format indexed by *cookie*. 


The first time this method is called *cookie* will be set to 0. In your implementation you should set information about the first file format you support in *_format* and set *cookie* to some meaningful non-zero value to track your positing in the list of supported formats, then return `B_OK`.


On successive calls return successive file format information and update *cookie* to track your position in the list. Each time you return new information about a file format return `B_OK`.


Once you run out of formats return `B_ERROR`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `cookie` | Index of file format to fill out. |
| `_format` | Pointer to a preallocated `media_file_format` object to fill out. |





**Returns:** `B_OK` if a file format was filled out for *cookie*, `B_ERROR` or an appropriate error code otherwise.

---

### `GetRef()`

```cpp
status_t BFileInterface::GetRef(entry_ref * _ref, char * _mimeType)
```

Implement to set the `entry_ref` and the MIME type of the file referenced by the current node. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `_ref` | Set to the `entry_ref` of the file. |
| `_mimeType` | Set to the MIME type of the current file. |





**Returns:** `B_OK` on success or an appropriate error code such as `B_ERROR` on error.

---

### `HandleMessage()`

```cpp
status_t BFileInterface::HandleMessage(int32 message, const void * data, size_t size)
```

Dispatches a message to the appropriate [BMediaNode](classBMediaNode.md) hook method given a message received on the control port. Implement this method to handle messages that arrive on your control port. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The message identifier. |
| `data` | The message data. |
| `size` | The size of the message data in bytes. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Message was dispatched. |
| B_ERROR | There was an error dispatching the message, possibly because it doesn't correspond to a hook function. |





**See also:** BMediaNode::HandleMessage() for details.


Reimplemented from [BMediaNode](classBMediaNode.md).

---

### `SetRef()`

```cpp
status_t BFileInterface::SetRef(const entry_ref & file, bool create, bigtime_t * _time)
```

Used when an application wants your node to use a specific file. 


The file specified by *file* may or may not exist.


If create is `false` you should try to open the existing file, and if successful you should write the running time of the file into *_time*. If you the file does not exist you should return `B_ENTRY_NOT_FOUND`.


If *create* is `true` you should create a new file, initialize the file for writing, and store 0 in *_time*. You should overwrite the file if it already exists.



**Returns:** `B_OK` on success or an appropriate error code such as `B_ERROR` or `B_ENTRY_NOT_FOUND` on error.

---

### `SniffRef()`

```cpp
status_t BFileInterface::SniffRef(const entry_ref & file, char * _mimeType, float * _quality)
```

Implement this method to allow the Media Roster to identify a file format associated with this node. 


If you can handle the format, set *_mimeType* to the MIME type of the file format and set *_quality* to indicate how well you can process the file.


A *_quality* of 0.0 means that you can't handle the file format at all and an *_quality* of 1.0 means you have total control over the file format.


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | The file being sniffed. |
| `_mimeType` | Fill this out with the appropriate MIME type. |
| `_quality` | How well you are able to handle the file format from 0.0 to 1.0. |





**Returns:** `B_OK` if you can identify the file's contents, otherwise return an appropriate error code. If you can't handle the file format at all, you should return `B_MEDIA_NO_HANDLER`.

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBFileInterface.html).
