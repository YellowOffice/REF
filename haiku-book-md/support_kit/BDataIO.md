---
name: BDataIO
type: class
kit: support_kit
brief: "Abstract interface for objects that provide read and write access to data"
source: haiku-book
---

# BDataIO Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Abstract interface for objects that provide read and write access to data. 


The interface provided by this class applies to objects or data that are limited to reading and writing data. Classes derived from this class should re-implement the [Read()](classBDataIO.md#a847ec8576c368bf9aada412e92aed623) or the [Write()](classBDataIO.md#a01692303eba7601c6a7cfa72c06d6afb) method from this class or both.


Candidates of types of data or objects that should be derived from this class are probably broadcasting media streams (which don't support reading at a certain point in the data) or network streams that output data continuously. Objects and data that support more advanced operations like seeking or reading at writing at defined positions should derive their classes from [BPositionIO](classBPositionIO.md), which inherits this class.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BDataIO](#a67891b7afe78d6a77845dd0352218801) () — This constructor does nothing.
* `virtual` [~BDataIO](#a45daa9db670dd2e5b83efcefcf8dbaed) () — This destructor does nothing.
* `virtual status_t` [Flush](#a38a8df63b367585fe5e6b6a85c406d05) () — Writes pending data to underlying storage.
* `virtual ssize_t` [Read](#a847ec8576c368bf9aada412e92aed623) (void *buffer, size_t size) — Reads data from the object into a buffer.
* `status_t` [ReadExactly](#a3a0b0fc36232531a1d8c1144a7d75741) (void *buffer, size_t size, size_t *_bytesRead=NULL) — Reads an exact amount of data from the object into a buffer.
* `virtual ssize_t` [Write](#a01692303eba7601c6a7cfa72c06d6afb) (const void *buffer, size_t size) — Writes data from a buffer to the object.
* `status_t` [WriteExactly](#a0095cfffa454a82eac3dedda2e187ab7) (const void *buffer, size_t size, size_t *_bytesWritten=NULL) — Writes an exact amount of data from a buffer to the object.

## Detailed Member Documentation

### `BDataIO()`

```cpp
BDataIO::BDataIO()
```

This constructor does nothing. 



**Since:** BeOS R3

---

### `~BDataIO()`

```cpp
BDataIO::~BDataIO()
```

This destructor does nothing. 



**Since:** BeOS R3

---

### `Flush()`

```cpp
status_t BDataIO::Flush()
```

Writes pending data to underlying storage. 


This method is relevant for [BDataIO](classBDataIO.md) implementations that buffer data passed to [Write()](classBDataIO.md#a01692303eba7601c6a7cfa72c06d6afb). The [Flush()](classBDataIO.md#a38a8df63b367585fe5e6b6a85c406d05) implementation should make sure that all such data are written to the underlying storage.


The default implementation is a no-op returning `B_OK`.



**Returns:** An error code indicating whether flushing the buffered data succeeded.



**Since:** Haiku R1


Reimplemented in [BBufferedDataIO](classBBufferedDataIO.md#a7a1cd3147b96744c2e3646db4cb6c995), and [BBufferIO](classBBufferIO.md#a6c51066fea50d99b1b87228651c689f3).

---

### `Read()`

```cpp
ssize_t BDataIO::Read(void * buffer, size_t size)
```

Reads data from the object into a buffer. 


Your implementation should copy data into `buffer`, with the maximum size of `size`.


The default implementation is a no-op returning `B_NOT_SUPPORTED`.



**Returns:** You should return the amount of bytes actually read, or an error code in case of failure.



**Since:** BeOS R3


Reimplemented in [BDatagramSocket](../network_kit/classBDatagramSocket.md#ac8d954e7e11eb2ef59d55b80a89e286c), [BSecureSocket](../network_kit/classBSecureSocket.md#a637c9bf1d12151a5541f9c7c1e4ea423), [BSocket](../network_kit/classBSocket.md#a25f8738613bd62e582ca7cb83e6d1035), [BFile](../storage_kit/classBFile.md#a84879555b0c3bee54e36abdeeb2cb559), [BBufferedDataIO](classBBufferedDataIO.md#aef91ed925bd2f40a4332dff9a7cbdb28), [BPositionIO](classBPositionIO.md#abce66c314f7cbd5ab6de0e6480bd7a00), and [BMemoryRingIO](classBMemoryRingIO.md#a3818ee42f7273efbafc38e1c559c87cd).

---

### `ReadExactly()`

```cpp
status_t BDataIO::ReadExactly(void * buffer, size_t size, size_t * _bytesRead = NULL)
```

Reads an exact amount of data from the object into a buffer. 


This is a convenience wrapper method for [Read()](classBDataIO.md#a847ec8576c368bf9aada412e92aed623) for code that expects the exact number of bytes requested to be read. This method calls [Read()](classBDataIO.md#a847ec8576c368bf9aada412e92aed623) in a loop to read the data. It fails when [Read()](classBDataIO.md#a847ec8576c368bf9aada412e92aed623) returns an error or fails to read any more data (i.e. returns 0).


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | Pointer to pre-allocated storage of at least *size* bytes into which the data shall be read. Won't be dereferenced, when *size* is 0. |
| `size` | The number of bytes to be read. |
| `_bytesRead` | Optional pointer to a pre-allocated size_t into which the number of bytes actually read will be written. When the method returns `B_OK` this will always be *size*. Can be `NULL`. |





**Returns:** An error code indicating whether or not the method succeeded.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | All data have been read. |
| B_PARTIAL_READ | [Read()](classBDataIO.md#a847ec8576c368bf9aada412e92aed623) didn't fail, but couldn't provide as many bytes as requested. |





**Since:** Haiku R1

---

### `Write()`

```cpp
ssize_t BDataIO::Write(const void * buffer, size_t size)
```

Writes data from a buffer to the object. 


Your implementation should copy data from `buffer`, with the maximum size of `size`.


The default implementation is a no-op returning `B_NOT_SUPPORTED`.



**Returns:** You should return the amount of bytes actually written, or an error code in case of failure.



**Since:** BeOS R3


Reimplemented in [BDatagramSocket](../network_kit/classBDatagramSocket.md#a166e043d7e578825b4b36f069309d1df), [BSecureSocket](../network_kit/classBSecureSocket.md#a032f89a5521cdb79bdf002447d5f64ba), [BSocket](../network_kit/classBSocket.md#a872e78ba97c25377c7804c72f2c0e396), [BFile](../storage_kit/classBFile.md#afcf216fde234f4fd0754409617bedc55), [BBufferedDataIO](classBBufferedDataIO.md#a6396fe1a4a153f1a70ef28e358cac037), [BPositionIO](classBPositionIO.md#a50ec7f6b834893a153d46c0f3c0e09c4), and [BMemoryRingIO](classBMemoryRingIO.md#a10a76c9e67013c9439f57d14b6e43812).

---

### `WriteExactly()`

```cpp
status_t BDataIO::WriteExactly(const void * buffer, size_t size, size_t * _bytesWritten = NULL)
```

Writes an exact amount of data from a buffer to the object. 


This is a convenience wrapper method for [Write()](classBDataIO.md#a01692303eba7601c6a7cfa72c06d6afb) for code that expects the exact number of bytes given to be written. This method calls [Write()](classBDataIO.md#a01692303eba7601c6a7cfa72c06d6afb) in a loop to write the data. It fails when [Write()](classBDataIO.md#a01692303eba7601c6a7cfa72c06d6afb) returns an error or fails to write any more data (i.e. returns 0).


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | Pointer to a buffer of at least *size* bytes containing the data to be written. Won't be dereferenced, when *size* is 0. |
| `size` | The number of bytes to be written. |
| `_bytesWritten` | Optional pointer to a pre-allocated size_t into which the number of bytes actually written will be written. When the method returns `B_OK` this will always be *size*. Can be `NULL`. |





**Returns:** An error code indicated whether the method succeeded.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | All data have been written. |
| B_PARTIAL_READ | [Write()](classBDataIO.md#a01692303eba7601c6a7cfa72c06d6afb) didn't fail, but couldn't write as many bytes as provided. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBDataIO.html).
