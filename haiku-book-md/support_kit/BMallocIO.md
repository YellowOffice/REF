---
name: BMallocIO
type: class
kit: support_kit
brief: "A BPositionIO derived class that creates a memory buffer"
source: haiku-book
---

# BMallocIO Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A [BPositionIO](classBPositionIO.md) derived class that creates a memory buffer. 


This class creates a memory buffer and provides a [BPositionIO](classBPositionIO.md) interface to work on it. The memory buffer grows and shrinks automatically. This is especially useful if you want to use a method or function that works on an object derived from [BPositionIO](classBPositionIO.md) and you want to do something with the resulting data, or it could be useful if you want to read and write to memory in a safe way, since this class has boundary checking.


[BMallocIO](classBMallocIO.md) allocates a buffer based on a certain block size. This provides a mechanism that will prevent it from needing to allocate new memory too often. The default block size is 256 bytes, you can change it with [SetBlockSize()](classBMallocIO.md#aebc7cca39f8e57f540be76c6b937061f). If you are sure you are going to use a bigger buffer, change the block size so that you won't have to allocate more memory too often, especially if you use this class in performance-critical code.


If you require a [BPositionIO](classBPositionIO.md) derived object that works on buffers you provide, have a look at [BMemoryIO](classBMemoryIO.md).



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BMallocIO](#aaa22efd3d5e51d7029ab52986ae1f71d) () — Create a new memory buffer with block size 256.
* `virtual` [~BMallocIO](#aa4a6f48404f4ffb4587c81ac26fa36e0) () — Destroy the object and free the internal buffer.
* `const void *` [Buffer](#a9b8a31c564374d8289b7581d76bf2b73) () const — Return a pointer to the internal buffer.
* `size_t` [BufferLength](#aaa31f36dc078f9f873679b7c4bab8167) () const — Return the number of bytes in the buffer.
* `virtual off_t` [Position](#af007bb9933ffa65b337ed49cdf5dd42e) () const — Return the position of the cursor.
* `virtual ssize_t` [ReadAt](#ab32620f9be85989e04da5f77f93db604) (off_t position, void *buffer, size_t size) — Read data at a certain position.
* `virtual off_t` [Seek](#af15fd592a792fce67693c4181daf7a30) (off_t position, uint32 seekMode) — Move the cursor to a given position.
* `void` [SetBlockSize](#aebc7cca39f8e57f540be76c6b937061f) (size_t blockSize) — Change the block size to a certain value.
* `virtual status_t` [SetSize](#ad0d175f05abea98db9fbf3754e7d5e51) (off_t size) — Change the size of the buffer.
* `virtual ssize_t` [WriteAt](#aa168631c8995ac5f325b2501e222fef8) (off_t position, const void *buffer, size_t size) — Write data to a certain position.
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

### `BMallocIO()`

```cpp
BMallocIO::BMallocIO()
```

Create a new memory buffer with block size 256. 



**See also:** [SetBlockSize()](classBMallocIO.md#aebc7cca39f8e57f540be76c6b937061f)



**Since:** BeOS R3

---

### `~BMallocIO()`

```cpp
BMallocIO::~BMallocIO()
```

Destroy the object and free the internal buffer. 



**Since:** BeOS R3

---

### `Buffer()`

```cpp
const void * BMallocIO::Buffer()const
```

Return a pointer to the internal buffer. 


As with any pointer to internal buffers the Haiku API exposes, make sure you don't change anything since it doesn't belong to you.



**Since:** BeOS R3

---

### `BufferLength()`

```cpp
size_t BMallocIO::BufferLength()const
```

Return the number of bytes in the buffer. 


This number doesn't have to be the same size as the buffer is. Because memory is allocated in blocks the actual size of the buffer may be greater, but this method only returns the number of bytes that are actually used.



**Since:** BeOS R3

---

### `Position()`

```cpp
off_t BMallocIO::Position()const
```

Return the position of the cursor. 



**Since:** BeOS R3


Implements [BPositionIO](classBPositionIO.md#a4ebc2cd7a7493767e79fa6d88657a84a).

---

### `ReadAt()`

```cpp
ssize_t BMallocIO::ReadAt(off_t pos, void * buffer, size_t size)
```

Read data at a certain position. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `pos` | Offset into the data where to read from. |
| `buffer` | The buffer to copy the read bytes in. |
| `size` | Size of the buffer. |





**Returns:** The number of read bytes, or `B_BAD_VALUE` if the provided *buffer* is invalid.



**Since:** BeOS R3


Implements [BPositionIO](classBPositionIO.md#a6eb7aff1d69bf3049b2b421da52fdf8f).

---

### `Seek()`

```cpp
off_t BMallocIO::Seek(off_t position, uint32 seekMode)
```

Move the cursor to a given position. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `position` | The position to move the cursor to. |
| `seekMode` | The mode determines where the cursor is placed. Possibilities: * `SEEK_SET` The cursor is set to *position*.  * `SEEK_CUR` The `position` is added to the current position of the cursor.  * `SEEK_END` The cursor is put at the end of the data, plus *position* added to it. |





**Returns:** The new position as an off_t.



**Since:** BeOS R3


Implements [BPositionIO](classBPositionIO.md#af8296875d9711dd498b0fbcace028abc).

---

### `SetBlockSize()`

```cpp
void BMallocIO::SetBlockSize(size_t blockSize)
```

Change the block size to a certain value. 


This class allocates memory in blocks. If you are in performance-critical code you might want to tweak this setting to create a better performance in case you know you are going to allocate more than the default block size of 256.


Parameters

| Parameter | Description |
| :--- | :--- |
| `blockSize` | The new block size. |





**Since:** BeOS R3

---

### `SetSize()`

```cpp
status_t BMallocIO::SetSize(off_t size)
```

Change the size of the buffer. 


This method changes the size of the current buffer. If *size* is smaller than the current size, the data will be cleared.


Parameters

| Parameter | Description |
| :--- | :--- |
| `size` | The new size of the buffer. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Resizing the data succeeded. |
| B_NO_MEMORY | Failed to allocate the necessary memory. |





**Since:** BeOS R3


Reimplemented from [BPositionIO](classBPositionIO.md#a35613c7ee06c7c9583ca2505e1fdff28).

---

### `WriteAt()`

```cpp
ssize_t BMallocIO::WriteAt(off_t pos, const void * buffer, size_t size)
```

Write data to a certain position. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `pos` | Offset into the data where to write to. |
| `buffer` | The buffer to copy from. |
| `size` | The size of the buffer. |





**Returns:** The number of bytes written or `B_BAD_VALUE` if the provided. *buffer* is invalid.



**Since:** BeOS R3


Implements [BPositionIO](classBPositionIO.md#a0efce1a07d1d6509e8ec00598244ace1).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMallocIO.html).
