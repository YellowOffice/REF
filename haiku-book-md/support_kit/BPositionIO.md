---
name: BPositionIO
type: class
kit: support_kit
brief: "Abstract interface that provides advanced read, write and seek access to data"
source: haiku-book
---

# BPositionIO Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Abstract interface that provides advanced read, write and seek access to data. 


The interface of this object applies to objects or data that allows position-aware reading and writing of data. Classes that derive from this class should at least re-implement [ReadAt()](classBPositionIO.md#a6eb7aff1d69bf3049b2b421da52fdf8f), [WriteAt()](classBPositionIO.md#a0efce1a07d1d6509e8ec00598244ace1), [Seek()](classBPositionIO.md#af8296875d9711dd498b0fbcace028abc), [Position()](classBPositionIO.md#a4ebc2cd7a7493767e79fa6d88657a84a), [SetSize()](classBPositionIO.md#a35613c7ee06c7c9583ca2505e1fdff28) and [GetSize()](classBPositionIO.md#a5be704340522f36f80697c6bc883a00d) methods.


A good example of a form of data that can derive from this object, are files. The [BFile](../storage_kit/classBFile.md) class derives from [BPositionIO](classBPositionIO.md) and provides this interface to files. If your object or data only supports linear reading and writing, consider deriving from the base-class [BDataIO](classBDataIO.md).


A final note, from [BDataIO](classBDataIO.md) this class inherits [Read()](classBPositionIO.md#abce66c314f7cbd5ab6de0e6480bd7a00) and [Write()](classBPositionIO.md#a50ec7f6b834893a153d46c0f3c0e09c4). The default implementation is to read or write the data at the current position indicated by [Position()](classBPositionIO.md#a4ebc2cd7a7493767e79fa6d88657a84a). Re-implement the methods if you require a different behavior.



**Since:** Haiku R1

## Member List

### Public Member Functions

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

### `BPositionIO()`

```cpp
BPositionIO::BPositionIO()
```

This constructor does nothing. 



**Since:** Haiku R1

---

### `~BPositionIO()`

```cpp
BPositionIO::~BPositionIO()
```

This destructor does nothing. 



**Since:** Haiku R1

---

### `GetSize()`

```cpp
status_t BPositionIO::GetSize(off_t * size)const
```

Get the size of the object or data. 


The default implementation uses [Seek()](classBPositionIO.md#af8296875d9711dd498b0fbcace028abc) with the `SEEK_END` flag to determine the size of the buffer. If your data or object has a different way of determining size, reimplement this method.


Please check that NULL is not passed into `size` if you reimplement it in your class.


Parameters

| Parameter | Description |
| :--- | :--- |
| `size` | The size of the object is put into this parameter. |





**Returns:** This method returns `B_OK` on success or an error code on error.



**See also:** [SetSize()](classBPositionIO.md#a35613c7ee06c7c9583ca2505e1fdff28)



**Since:** BeOS R3


Reimplemented in [BFile](../storage_kit/classBFile.md#a9438a3e18c34008d98fbb56cae890645).

---

### `Position()`

```cpp
off_t BPositionIO::Position()const
```

Pure virtual to return the current position of the cursor. 



**Returns:** Your implementation should return the current position of the cursor.



**Since:** BeOS R3


Implemented in [BFile](../storage_kit/classBFile.md#aef5499cdc105ac4817f669bad3ca05b8), [BBufferIO](classBBufferIO.md#a83acd23044df368781a9069191492cf7), [BMemoryIO](classBMemoryIO.md#ac1dbae182c93e030cd9bf1cfc49596a5), [BMallocIO](classBMallocIO.md#af007bb9933ffa65b337ed49cdf5dd42e), and [BBitmapStream](../translation_kit/classBBitmapStream.md#aa172a68e7325680c9d3210714e5330c4).

---

### `Read()`

```cpp
ssize_t BPositionIO::Read(void * buffer, size_t size)
```

Read data from current position. 


This method is derived from [BDataIO](classBDataIO.md). The default implementation reads data from the current position of the cursor, pointed at by [Position()](classBPositionIO.md#a4ebc2cd7a7493767e79fa6d88657a84a). If you require different behaviour, please look at [BDataIO::Read()](classBDataIO.md#a847ec8576c368bf9aada412e92aed623) for what is expected of this method.



**Since:** BeOS R3


Reimplemented from [BDataIO](classBDataIO.md#a847ec8576c368bf9aada412e92aed623).


Reimplemented in [BFile](../storage_kit/classBFile.md#a84879555b0c3bee54e36abdeeb2cb559).

---

### `ReadAt()`

```cpp
ssize_t BPositionIO::ReadAt(off_t position, void * buffer, size_t size)
```

Pure virtual to read data from a certain position. 


Your implementation should copy data from the position indicated by *position* into the *buffer* with the maximum size of *size*.



**Returns:** The amount of bytes actually read, or an error code.



**Since:** BeOS R3


Implemented in [BFile](../storage_kit/classBFile.md#aa66cbdba802924c4b5fbeac6a2765805), [BBitmapStream](../translation_kit/classBBitmapStream.md#a22bc134d272bac2f1979951f6d00140a), [BBufferIO](classBBufferIO.md#a7887fde998d8629c6a4063ba5c3e41aa), [BMemoryIO](classBMemoryIO.md#a48959adcf4da35b53b965dcae570e5b7), and [BMallocIO](classBMallocIO.md#ab32620f9be85989e04da5f77f93db604).

---

### `ReadAtExactly()`

```cpp
status_t BPositionIO::ReadAtExactly(off_t position, void * buffer, size_t size, size_t * _bytesRead = NULL)
```

Reads an exact amount of data from the object at the specified position into a buffer. 


This is a convenience wrapper method for [ReadAt()](classBPositionIO.md#a6eb7aff1d69bf3049b2b421da52fdf8f) for code that expects the exact number of bytes requested to be read. This method calls [ReadAt()](classBPositionIO.md#a6eb7aff1d69bf3049b2b421da52fdf8f) in a loop to read the data. It fails when [ReadAt()](classBPositionIO.md#a6eb7aff1d69bf3049b2b421da52fdf8f) returns an error or fails to read any more data (i.e. returns 0).


Parameters

| Parameter | Description |
| :--- | :--- |
| `position` | The object position at which to read the data. |
| `buffer` | Pointer to pre-allocated storage of at least *size* bytes into which the data shall be read. Won't be dereferenced, when *size* is 0. |
| `size` | The number of bytes to be read. |
| `_bytesRead` | Optional pointer to a pre-allocated size_t into which the number of bytes actually read will be written. When the method returns `B_OK` this will always be *size*. Can be `NULL`. |





**Returns:** An error code indicating whether or not the method succeeded.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | All data have been read. |
| B_PARTIAL_READ | [ReadAt()](classBPositionIO.md#a6eb7aff1d69bf3049b2b421da52fdf8f) didn't fail, but couldn't provide as many bytes as requested. |





**Since:** Haiku R1

---

### `Seek()`

```cpp
off_t BPositionIO::Seek(off_t position, uint32 seekMode)
```

Pure virtual to move the cursor to a certain position. 


Your implementation should move the position of the cursor to the provided point. What this actually means, depends on your object or data.


Parameters

| Parameter | Description |
| :--- | :--- |
| `position` | An integer that defines a position. |
| `seekMode` | You will get one of the following values: * `SEEK_SET` Set the cursor to the position indicated by `position`.  * `SEEK_END` Set the cursor to the end of the buffer, and go `position` beyond that.  * `SEEK_CUR` Set the cursor the the current position plus `position`. |





**Returns:** The new position.



**Since:** BeOS R3


Implemented in [BFile](../storage_kit/classBFile.md#a396e6721a72e8fbed4056e37741dcb8a), [BBufferIO](classBBufferIO.md#a7ba7f66e172e2d7ad87a114069028876), [BMemoryIO](classBMemoryIO.md#a49898b4f0b195b025c896e8163d625b7), [BMallocIO](classBMallocIO.md#af15fd592a792fce67693c4181daf7a30), and [BBitmapStream](../translation_kit/classBBitmapStream.md#af17115c38e1f19e8bbfbba3880850223).

---

### `SetSize()`

```cpp
status_t BPositionIO::SetSize(off_t size)
```

Set the size of the object or data. 


The default implementation returns `B_ERROR`. If your object or data allows the size to be changed, reimplement this method.



**Returns:** Return `B_OK` if everything succeeded, else return the appropriate error code.



**Since:** BeOS R3


Reimplemented in [BFile](../storage_kit/classBFile.md#a5b8f0932cff0d50b6e0c7aea169a74ef), [BBufferIO](classBBufferIO.md#aed5125f4b157b0e5208cd39aa0af0d77), [BMemoryIO](classBMemoryIO.md#a422e492427167bc7d779d2a8fa92072b), [BMallocIO](classBMallocIO.md#ad0d175f05abea98db9fbf3754e7d5e51), and [BBitmapStream](../translation_kit/classBBitmapStream.md#a47ce4b957cbde849427f8aa937d0f716).

---

### `Write()`

```cpp
ssize_t BPositionIO::Write(const void * buffer, size_t size)
```

Write data to the current position. 


This method is derived from [BDataIO](classBDataIO.md). The default implementation writes data to the current position of the cursor, pointed at by [Position()](classBPositionIO.md#a4ebc2cd7a7493767e79fa6d88657a84a). If you require different behaviour, please look at [BDataIO::Write()](classBDataIO.md#a01692303eba7601c6a7cfa72c06d6afb) for what is expected of this method.



**Since:** BeOS R3


Reimplemented from [BDataIO](classBDataIO.md#a01692303eba7601c6a7cfa72c06d6afb).


Reimplemented in [BFile](../storage_kit/classBFile.md#afcf216fde234f4fd0754409617bedc55).

---

### `WriteAt()`

```cpp
ssize_t BPositionIO::WriteAt(off_t position, const void * buffer, size_t size)
```

Pure virtual to write data to a certain position. 


Your implementation should copy data from *buffer* to the position indicated by *buffer* with the maximum size of *size*.



**Returns:** The amount of bytes actually written, or an error code.



**Since:** BeOS R3


Implemented in [BFile](../storage_kit/classBFile.md#a43a09d7441f9fda29cc90c1f3612021c), [BBitmapStream](../translation_kit/classBBitmapStream.md#af48762a7326aebc52aed25315e04ef6d), [BBufferIO](classBBufferIO.md#a949b030b3fd3dc93be06d39f627f2bce), [BMemoryIO](classBMemoryIO.md#ace4180382856baecafa545fc92aabd85), and [BMallocIO](classBMallocIO.md#aa168631c8995ac5f325b2501e222fef8).

---

### `WriteAtExactly()`

```cpp
status_t BPositionIO::WriteAtExactly(off_t position, const void * buffer, size_t size, size_t * _bytesWritten = NULL)
```

Writes an exact amount of data from a buffer to the object at the specified position. 


This is a convenience wrapper method for [WriteAt()](classBPositionIO.md#a0efce1a07d1d6509e8ec00598244ace1) for code that expects the exact number of bytes given to be written. This method calls [WriteAt()](classBPositionIO.md#a0efce1a07d1d6509e8ec00598244ace1) in a loop to write the data. It fails when [WriteAt()](classBPositionIO.md#a0efce1a07d1d6509e8ec00598244ace1) returns an error or fails to write any more data (i.e. returns 0).


Parameters

| Parameter | Description |
| :--- | :--- |
| `position` | The object position at which to write the data. |
| `buffer` | Pointer to a buffer of at least *size* bytes containing the data to be written. Won't be dereferenced, when *size* is 0. |
| `size` | The number of bytes to be written. |
| `_bytesWritten` | Optional pointer to a pre-allocated size_t into which the number of bytes actually written will be written. When the method returns `B_OK` this will always be *size*. Can be `NULL`. |





**Returns:** An error code indicated whether the method succeeded.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | All data have been written. |
| B_PARTIAL_READ | [WriteAt()](classBPositionIO.md#a0efce1a07d1d6509e8ec00598244ace1) didn't fail, but couldn't write as many bytes as provided. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPositionIO.html).
