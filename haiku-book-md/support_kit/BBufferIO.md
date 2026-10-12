---
name: BBufferIO
type: class
kit: support_kit
brief: "A buffered adapter for BPositionIO objects"
source: haiku-book
---

# BBufferIO Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A buffered adapter for [BPositionIO](classBPositionIO.md) objects. 


This class differs from other classes derived from [BPositionIO](classBPositionIO.md) in a sense that it does not actually provide an actual entity to be read or written to, but rather acts like a "frontend" to a stream. This class especially comes in handy when working with files that are constantly written and rewritten and where you want do this writing buffered so that the hard disk or the network will not have to be accessed so frequently.


This class works as follows. After constructing a [BPositionIO](classBPositionIO.md) object that you want to be buffered, you can create this object. The constructor takes a *stream* parameter that points to the object to be buffered.


You then use this object as a proxy to the resource you want to read of or write to. As soon as you use [ReadAt()](classBBufferIO.md#a7887fde998d8629c6a4063ba5c3e41aa), the buffer will be initialized to the contents of the original stream, and subsequent calls to the positions within the buffer will not be routed to the original stream. In the same way [WriteAt()](classBBufferIO.md#a949b030b3fd3dc93be06d39f627f2bce) will change the data in the buffer, but not in the actual stream. In order to flush the changes to the original stream, use the [Flush()](classBBufferIO.md#a6c51066fea50d99b1b87228651c689f3) method. Deleting the object when you are done with it will also flush the stream and update the original stream.



> [!NOTE]
> This class is not meant to be used in cases where the original stream requires to be in a consistent state. Neither should this class be used as a way to perform 'atomic' writes, because the object might need to do partial writes if it needs to 'move' the buffer. This happens for instance if the original stream is bigger than the buffer.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BBufferIO](#a48fbdf7ea0d409c492addc9636ec8d0e) (BPositionIO *stream, size_t bufferSize=65536L, bool ownsStream=true) — Initialize a BBufferIO object.
* `virtual` [~BBufferIO](#a3318cecf9a1780b332fe157656113006) () — Free the resources allocated by the object.
* `size_t` [BufferSize](#a847813fab6391b1a21fad19bd1e41dae) () const — Return the size of the internal buffer.
* `virtual status_t` [Flush](#a6c51066fea50d99b1b87228651c689f3) () — Write pending modifications to the stream.
* `bool` [OwnsStream](#a830fee2824d387c64ae8855c13ba872a) () const — Return whether or not the BBufferIO object "owns" the stream.
* `virtual off_t` [Position](#a83acd23044df368781a9069191492cf7) () const — Return the current position in the stream.
* `void` [PrintToStream](#aa6c5bb0b0a3c2fba56b2faced6044ef3) () const — Print the object to standard output.
* `virtual ssize_t` [ReadAt](#a7887fde998d8629c6a4063ba5c3e41aa) (off_t pos, void *buffer, size_t size) — Read the specified amount of bytes at the given position.
* `virtual off_t` [Seek](#a7ba7f66e172e2d7ad87a114069028876) (off_t position, uint32 seekMode) — Set the position in the stream.
* `void` [SetOwnsStream](#ab47ac843be8304193fa1e99c720703e1) (bool ownsStream) — Set the owns_stream property of the object.
* `virtual status_t` [SetSize](#aed5125f4b157b0e5208cd39aa0af0d77) (off_t size) — Call the SetSize() function of the assigned BPositionIO stream.
* `BPositionIO *` [Stream](#a2a50815b961ccd527b7e1b10e7dc7281) () const — Return a pointer to the stream specified on construction.
* `virtual ssize_t` [WriteAt](#a949b030b3fd3dc93be06d39f627f2bce) (off_t pos, const void *buffer, size_t size) — Write the specified amount of bytes at the given position.
* [BPositionIO](#a08051e865cd2623fab56c3733ecbf099) () — This constructor does nothing.
* `virtual` [~BPositionIO](#a505defae83a1a6937c77b9acac2aaafe) () — This destructor does nothing.
* `virtual status_t` [GetSize](#a5be704340522f36f80697c6bc883a00d) (off_t *size) const — Get the size of the object or data.
* `virtual off_t` [Position](#a4ebc2cd7a7493767e79fa6d88657a84a) () const =0 — Pure virtual to return the current position of the cursor.
* `virtual ssize_t` [Read](#abce66c314f7cbd5ab6de0e6480bd7a00) (void *buffer, size_t size) — Read data from current position.
* `virtual ssize_t` [ReadAt](#a6eb7aff1d69bf3049b2b421da52fdf8f) (off_t position, void *buffer, size_t size)=0 — Pure virtual to read data from a certain position.
* `status_t` [ReadAtExactly](#a91bab7ae60926dbe3726bc73734318b6) (off_t position, void *buffer, size_t size, size_t *_bytesRead=NULL) — Reads an exact amount of data from the object at the specified position into a buffer.
* `virtual off_t` [Seek](#af8296875d9711dd498b0fbcace028abc) (off_t position, uint32 seekMode)=0 — Pure virtual to move the cursor to a certain position.
* `virtual status_t` [SetSize](#a35613c7ee06c7c9583ca2505e1fdff28) (off_t size) — Set the size of the object or data.
* `virtual ssize_t` [Write](#a50ec7f6b834893a153d46c0f3c0e09c4) (const void *buffer, size_t size) — Write data to the current position.
* `virtual ssize_t` [WriteAt](#a0efce1a07d1d6509e8ec00598244ace1) (off_t position, const void *buffer, size_t size)=0 — Pure virtual to write data to a certain position.
* `status_t` [WriteAtExactly](#a18100db340087226321c332182816d27) (off_t position, const void *buffer, size_t size, size_t *_bytesWritten=NULL) — Writes an exact amount of data from a buffer to the object at the specified position.
* [BDataIO](#a67891b7afe78d6a77845dd0352218801) () — This constructor does nothing.
* `virtual` [~BDataIO](#a45daa9db670dd2e5b83efcefcf8dbaed) () — This destructor does nothing.
* `virtual status_t` [Flush](#a38a8df63b367585fe5e6b6a85c406d05) () — Writes pending data to underlying storage.
* `virtual ssize_t` [Read](#a847ec8576c368bf9aada412e92aed623) (void *buffer, size_t size) — Reads data from the object into a buffer.
* `status_t` [ReadExactly](#a3a0b0fc36232531a1d8c1144a7d75741) (void *buffer, size_t size, size_t *_bytesRead=NULL) — Reads an exact amount of data from the object into a buffer.
* `virtual ssize_t` [Write](#a01692303eba7601c6a7cfa72c06d6afb) (const void *buffer, size_t size) — Writes data from a buffer to the object.
* `status_t` [WriteExactly](#a0095cfffa454a82eac3dedda2e187ab7) (const void *buffer, size_t size, size_t *_bytesWritten=NULL) — Writes an exact amount of data from a buffer to the object.

## Detailed Member Documentation

### `BBufferIO()`

```cpp
BBufferIO::BBufferIO(BPositionIO * stream, size_t bufferSize = 65536L, bool ownsStream = true)
```

Initialize a [BBufferIO](classBBufferIO.md) object. 


The constructor will create a buffer of the given size and associate the object with the given [BPositionIO](classBPositionIO.md) stream.


Parameters

| Parameter | Description |
| :--- | :--- |
| `stream` | A pointer to a [BPositionIO](classBPositionIO.md) object. |
| `bufferSize` | The size of the buffer that the object will allocate and use. |
| `ownsStream` | Specifies if the object will delete the stream on destruction. |





**Since:** Haiku R1

---

### `~BBufferIO()`

```cpp
BBufferIO::~BBufferIO()
```

Free the resources allocated by the object. 


Flush pending changes to the stream and free the allocated memory. If the `owns_stream` property is `true`, the destructor also deletes the stream associated with the [BBufferIO](classBBufferIO.md) object.



**Since:** Haiku R1

---

### `BufferSize()`

```cpp
size_t BBufferIO::BufferSize()const
```

Return the size of the internal buffer. 



**Returns:** The size of the buffer allocated by the object.



**Since:** Haiku R1

---

### `Flush()`

```cpp
status_t BBufferIO::Flush()
```

Write pending modifications to the stream. 



**Returns:** The amount of bytes written, or if it failed it will return an error code.



**Since:** Haiku R1


Reimplemented from [BDataIO](classBDataIO.md#a38a8df63b367585fe5e6b6a85c406d05).

---

### `OwnsStream()`

```cpp
bool BBufferIO::OwnsStream()const
```

Return whether or not the [BBufferIO](classBBufferIO.md) object "owns" the stream. 



**Returns:** Whether or not the [BBufferIO](classBBufferIO.md) object "owns" the stream.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The object "owns" the stream and will destroy it upon destruction. |
| false | The object does not own the stream. |





**See also:** [SetOwnsStream()](classBBufferIO.md#ab47ac843be8304193fa1e99c720703e1)



**Since:** Haiku R1

---

### `Position()`

```cpp
off_t BBufferIO::Position()const
```

Return the current position in the stream. 



**Returns:** The current position as an offset in bytes from the beginning of the stream.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_NO_INIT | The object is not associated with a valid [BPositionIO](classBPositionIO.md) stream. |





**Since:** Haiku R1


Implements [BPositionIO](classBPositionIO.md#a4ebc2cd7a7493767e79fa6d88657a84a).

---

### `PrintToStream()`

```cpp
void BBufferIO::PrintToStream()const
```

Print the object to standard output. 



**Since:** Haiku R1

---

### `ReadAt()`

```cpp
ssize_t BBufferIO::ReadAt(off_t pos, void * buffer, size_t size)
```

Read the specified amount of bytes at the given position. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `pos` | The offset into the stream where to read. |
| `buffer` | A pointer to a buffer where to copy the read data. |
| `size` | The amount of bytes to read. |





**Returns:** The amount of bytes actually read, or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_NO_INIT | The object is not associated with a valid [BPositionIO](classBPositionIO.md) stream. |
| B_BAD_VALUE | The `buffer` parameter is not valid. |





**Since:** Haiku R1


Implements [BPositionIO](classBPositionIO.md#a6eb7aff1d69bf3049b2b421da52fdf8f).

---

### `Seek()`

```cpp
off_t BBufferIO::Seek(off_t position, uint32 seekMode)
```

Set the position in the stream. 


Set the position in the stream where the [Read()](classBPositionIO.md#abce66c314f7cbd5ab6de0e6480bd7a00) and [Write()](classBPositionIO.md#a50ec7f6b834893a153d46c0f3c0e09c4) functions (inherited from [BPositionIO](classBPositionIO.md)) begin reading and writing. How the position argument is understood depends on the seek_mode flag.


Parameters

| Parameter | Description |
| :--- | :--- |
| `position` | The position where you want to seek. |
| `seekMode` | Can have three values: * `SEEK_SET` The position passed is an offset from the beginning of the stream; in other words, the current position is set to position. For this mode, position should be a positive value.  * `SEEK_CUR` The position argument is an offset from the current position; the value of the argument is added to the current position.  * `SEEK_END`. The position argument is an offset from the end of the stream. In this mode the position argument should be negative (or zero). |





**Returns:** The current position as an offset in bytes from the beginning of the stream.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_NO_INIT | The object is not associated with a valid [BPositionIO](classBPositionIO.md) stream. |





**Since:** Haiku R1


Implements [BPositionIO](classBPositionIO.md#af8296875d9711dd498b0fbcace028abc).

---

### `SetOwnsStream()`

```cpp
void BBufferIO::SetOwnsStream(bool owns_stream)
```

Set the `owns_stream` property of the object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `owns_stream` | If you pass `true`, the object will delete the stream upon destruction, if you pass `false` it will not. |





**Since:** Haiku R1

---

### `SetSize()`

```cpp
status_t BBufferIO::SetSize(off_t size)
```

Call the [SetSize()](classBBufferIO.md#aed5125f4b157b0e5208cd39aa0af0d77) function of the assigned [BPositionIO](classBPositionIO.md) stream. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `size` | The new size of the [BPositionIO](classBPositionIO.md) object. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The stream is resized. |
| B_NO_INIT | The object is not associated with a valid [BPositionIO](classBPositionIO.md) stream. |





**Since:** Haiku R1


Reimplemented from [BPositionIO](classBPositionIO.md#a35613c7ee06c7c9583ca2505e1fdff28).

---

### `Stream()`

```cpp
BPositionIO * BBufferIO::Stream()const
```

Return a pointer to the stream specified on construction. 



**Returns:** A pointer to the [BPositionIO](classBPositionIO.md) stream specified on construction.



**Since:** Haiku R1

---

### `WriteAt()`

```cpp
ssize_t BBufferIO::WriteAt(off_t pos, const void * buffer, size_t size)
```

Write the specified amount of bytes at the given position. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `pos` | The offset into the stream where to write. |
| `buffer` | A pointer to a buffer which contains the data to write. |
| `size` | The amount of bytes to write. |





**Returns:** The amount of bytes actually written, or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_NO_INIT | The object is not associated with a valid [BPositionIO](classBPositionIO.md) stream. |
| B_BAD_VALUE | The `buffer` parameter is not valid. |





**Since:** Haiku R1


Implements [BPositionIO](classBPositionIO.md#a0efce1a07d1d6509e8ec00598244ace1).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBBufferIO.html).
