---
name: BMemoryIO
type: class
kit: support_kit
brief: "A BPositionIO derived class that works on memory buffers"
source: haiku-book
---

# BMemoryIO Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A [BPositionIO](classBPositionIO.md) derived class that works on memory buffers. 


This class is used if you require access that confirms to the [BPositionIO](classBPositionIO.md) interface on memory buffers that you created. If you would like to use that interface on new buffers, have a look at [BMallocIO](classBMallocIO.md).


This class is particularly useful if you would like to use a class or method that are written to make use of the [BPositionIO](classBPositionIO.md) interface. It might also be used for 'secure' reading and writing from buffers, since this class automatically checks the bounds of anything you might want to do.


This class reimplements the [Read()](classBPositionIO.md#abce66c314f7cbd5ab6de0e6480bd7a00), [Write()](classBPositionIO.md#a50ec7f6b834893a153d46c0f3c0e09c4), [ReadAt()](classBMemoryIO.md#a48959adcf4da35b53b965dcae570e5b7), Writeat(), [Seek()](classBMemoryIO.md#a49898b4f0b195b025c896e8163d625b7) and [Position()](classBMemoryIO.md#ac1dbae182c93e030cd9bf1cfc49596a5) interface from [BPositionIO](classBPositionIO.md).



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BMemoryIO](#ad5d3157a3f83902f7e81a2c7b61750a6) (const void *data, size_t length) — Create a read-only object.
* [BMemoryIO](#a278fa4cfbac1a04bf4c99bb2a16d2dc6) (void *data, size_t length) — Create a read/write object.
* `virtual` [~BMemoryIO](#a4fb9a9e955c9cb4d9235f447f64876cd) () — The destructor does nothing.
* `virtual off_t` [Position](#ac1dbae182c93e030cd9bf1cfc49596a5) () const — Return the current position.
* `virtual ssize_t` [ReadAt](#a48959adcf4da35b53b965dcae570e5b7) (off_t position, void *buffer, size_t size) — Read from a given position.
* `virtual off_t` [Seek](#a49898b4f0b195b025c896e8163d625b7) (off_t position, uint32 seekMode) — Move the cursor to a given position.
* `virtual status_t` [SetSize](#a422e492427167bc7d779d2a8fa92072b) (off_t size) — Resize the buffer.
* `virtual ssize_t` [WriteAt](#ace4180382856baecafa545fc92aabd85) (off_t position, const void *buffer, size_t size) — Write at a given position.
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

### `BMemoryIO()`

```cpp
BMemoryIO::BMemoryIO(void * data, size_t length)
```

Create a read/write object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A pointer to the buffer to adopt. |
| `length` | The size of the buffer. |





**See also:** [BMemoryIO(const void *buffer, size_t length)](classBMemoryIO.md#ad5d3157a3f83902f7e81a2c7b61750a6) for a read-only implementation.



**Since:** BeOS R3

---

### `BMemoryIO()`

```cpp
BMemoryIO::BMemoryIO(const void * buffer, size_t length)
```

Create a read-only object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | A pointer to the `const` (read-only) buffer to adopt. |
| `length` | The size of the buffer. |





**See also:** [BMemoryIO(void *buffer, size_t length)](classBMemoryIO.md#a278fa4cfbac1a04bf4c99bb2a16d2dc6) for a read-write implementation.



**Since:** BeOS R3

---

### `~BMemoryIO()`

```cpp
BMemoryIO::~BMemoryIO()
```

The destructor does nothing. 



**Since:** BeOS R3

---

### `Position()`

```cpp
off_t BMemoryIO::Position()const
```

Return the current position. 



**Returns:** The current position as an off_t.



**Since:** BeOS R3


Implements [BPositionIO](classBPositionIO.md#a4ebc2cd7a7493767e79fa6d88657a84a).

---

### `ReadAt()`

```cpp
ssize_t BMemoryIO::ReadAt(off_t pos, void * buffer, size_t size)
```

Read from a given position. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `pos` | The offset where to start reading data. |
| `buffer` | The buffer to copy the read bytes into. |
| `size` | The size of the *buffer*. |





**Returns:** The amount of read bytes or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | The position is less than zero or the buffer given on construction is invalid. |





**Since:** BeOS R3


Implements [BPositionIO](classBPositionIO.md#a6eb7aff1d69bf3049b2b421da52fdf8f).

---

### `Seek()`

```cpp
off_t BMemoryIO::Seek(off_t position, uint32 seek_mode)
```

Move the cursor to a given position. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `position` | The position to move the cursor to. |
| `seek_mode` | The mode determines where the cursor is placed. Possibilities include: * `SEEK_SET` The cursor is set to *position*.  * `SEEK_CUR` The *position* is added to the current position of the cursor.  * `SEEK_END` The cursor is put at the end of the data, plus *position* added to it. |





**Returns:** The new position.



**Since:** BeOS R3


Implements [BPositionIO](classBPositionIO.md#af8296875d9711dd498b0fbcace028abc).

---

### `SetSize()`

```cpp
status_t BMemoryIO::SetSize(off_t size)
```

Resize the buffer. 


This method does not actually resize the buffer. If the new size is greater than the size of the buffer, resizing will fail. It will only succeed if the new size is less than the size of the buffer. The buffer itself will not be resized though.


This method might be useful in some cases. If the buffer is larger than the data it holds, changing the size will enable you to use the [Seek()](classBMemoryIO.md#a49898b4f0b195b025c896e8163d625b7) method with the flag `SEEK_END` and not get an error if you read or write from that position, since you actually have a buffer at the end.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The buffer is resized. |
| B_NOT_ALLOWED | The buffer is read-only. |
| B_ERROR | The `size` is larger than the size of the buffer. |





**Since:** BeOS R3


Reimplemented from [BPositionIO](classBPositionIO.md#a35613c7ee06c7c9583ca2505e1fdff28).

---

### `WriteAt()`

```cpp
ssize_t BMemoryIO::WriteAt(off_t pos, const void * buffer, size_t size)
```

Write at a given position. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `pos` | The offset to write to. |
| `buffer` | The buffer to copy the bytes from. |
| `size` | The number of bytes to write. |





**Returns:** The amount of bytes written or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_NOT_ALLOWED | The object is constructed as a read-only object. |
| B_BAD_VALUE | The position is less than zero or the buffer given on construction is invalid. |





**Since:** BeOS R3


Implements [BPositionIO](classBPositionIO.md#a0efce1a07d1d6509e8ec00598244ace1).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMemoryIO.html).
