---
name: BMemoryRingIO
type: class
kit: support_kit
brief: "An implementation of a ring buffer with a BDataIO interface"
source: haiku-book
---

# BMemoryRingIO Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Experimental functions and classes](group__libshared.md)

## Description

An implementation of a ring buffer with a [BDataIO](classBDataIO.md) interface. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BMemoryRingIO](#ada0280b3dc869fccfc82062d20fce63c) (size_t size) — Creates a new BMemoryRingIO object with the given buffer size.
* `virtual` [~BMemoryRingIO](#a555551964fdcdedb75f0ee8b54ac3f12) () — Free up resources held by the object.
* `size_t` [BufferSize](#a5b7e271192ebe8a506201c53766489ae) () — Get the total capacity of the object.
* `size_t` [BytesAvailable](#a06183c418cfe254f11d7258ca9bf8001) () — Get the amount of data stored in the object.
* `void` [Clear](#a79bcf6bc65f25e5c542352193bbf64d6) () — Discard all data in the object.
* `status_t` [InitCheck](#a27e69b901fb20fe9fc4606202d113365) () const — Whether the object has been initialized correctly.
* `virtual ssize_t` [Read](#a3818ee42f7273efbafc38e1c559c87cd) (void *buffer, size_t size) — Reads data from the object into a buffer.
* `status_t` [SetSize](#a01fad99fdaaa66e70cd25e0b5a785099) (size_t size) — Change the ring buffer capacity.
* `void` [SetWriteDisabled](#ac513ffdbce33a9095a41a1c69afc367a) (bool disabled) — Set whether writes to the ring buffer is disabled.
* `size_t` [SpaceAvailable](#a46bee59062d566023b9c8e43f6e3b96d) () — Get the amount of space left in the object.
* `status_t` [WaitForRead](#afb8157e42f9ddd0a682900d2fc44a0ae) (bigtime_t timeout=B_INFINITE_TIMEOUT) — Wait for data to be available for reading.
* `status_t` [WaitForWrite](#a24f6aa233c34af8ff8ee570aab5209b1) (bigtime_t timeout=B_INFINITE_TIMEOUT) — Wait for space to be available for writing.
* `virtual ssize_t` [Write](#a10a76c9e67013c9439f57d14b6e43812) (const void *buffer, size_t size) — Writes data from a buffer to the object.
* `bool` [WriteDisabled](#a70803d41888b75dfacdfdd3da032b7ab) () — Indicates whether writes to the ring buffer is disabled.
* [BDataIO](#a67891b7afe78d6a77845dd0352218801) () — This constructor does nothing.
* `virtual` [~BDataIO](#a45daa9db670dd2e5b83efcefcf8dbaed) () — This destructor does nothing.
* `virtual status_t` [Flush](#a38a8df63b367585fe5e6b6a85c406d05) () — Writes pending data to underlying storage.
* `virtual ssize_t` [Read](#a847ec8576c368bf9aada412e92aed623) (void *buffer, size_t size) — Reads data from the object into a buffer.
* `status_t` [ReadExactly](#a3a0b0fc36232531a1d8c1144a7d75741) (void *buffer, size_t size, size_t *_bytesRead=NULL) — Reads an exact amount of data from the object into a buffer.
* `virtual ssize_t` [Write](#a01692303eba7601c6a7cfa72c06d6afb) (const void *buffer, size_t size) — Writes data from a buffer to the object.
* `status_t` [WriteExactly](#a0095cfffa454a82eac3dedda2e187ab7) (const void *buffer, size_t size, size_t *_bytesWritten=NULL) — Writes an exact amount of data from a buffer to the object.

## Detailed Member Documentation

### `BMemoryRingIO()`

```cpp
BMemoryRingIO::BMemoryRingIO(size_t size)
```

Creates a new [BMemoryRingIO](classBMemoryRingIO.md) object with the given buffer size. 


Call [InitCheck()](classBMemoryRingIO.md#a27e69b901fb20fe9fc4606202d113365) to verify that the buffer has been successfully created.


Parameters

| Parameter | Description |
| :--- | :--- |
| `size` | The initial size of the buffer. |





**Since:** Haiku R1



**See also:** [SetSize()](classBMemoryRingIO.md#a01fad99fdaaa66e70cd25e0b5a785099)

---

### `~BMemoryRingIO()`

```cpp
BMemoryRingIO::~BMemoryRingIO()
```

Free up resources held by the object. 



**Since:** Haiku R1

---

### `BufferSize()`

```cpp
size_t BMemoryRingIO::BufferSize()
```

Get the total capacity of the object. 



**Returns:** The total capacity of the object in bytes.



**Since:** Haiku R1



**See also:** [SpaceAvailable()](classBMemoryRingIO.md#a46bee59062d566023b9c8e43f6e3b96d) for the amount of space left for writing in the object.

---

### `BytesAvailable()`

```cpp
size_t BMemoryRingIO::BytesAvailable()
```

Get the amount of data stored in the object. 



**Returns:** The amount of bytes ready to be read from the object.



**Since:** Haiku R1



**See also:** [BufferSize()](classBMemoryRingIO.md#a5b7e271192ebe8a506201c53766489ae) for the total buffer size.

---

### `Clear()`

```cpp
void BMemoryRingIO::Clear()
```

Discard all data in the object. 


This method will discard all data within the buffer. However it does not free the memory held by the buffer. If this is desired, use in combination with [SetSize()](classBMemoryRingIO.md#a01fad99fdaaa66e70cd25e0b5a785099) with `0` as the new capacity.



**Since:** Haiku R1



**See also:** [SetSize()](classBMemoryRingIO.md#a01fad99fdaaa66e70cd25e0b5a785099) for freeing memory held by the buffer, or for growing the buffer's size.

---

### `InitCheck()`

```cpp
status_t BMemoryRingIO::InitCheck()const
```

Whether the object has been initialized correctly. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything is initialized. |
| B_NO_INIT | The internal buffer couldn't be created or the buffer capacity is `0`. |





**Since:** Haiku R1

---

### `Read()`

```cpp
ssize_t BMemoryRingIO::Read(void * buffer, size_t size)
```

Reads data from the object into a buffer. 


If the ring buffer is empty, this method blocks until some data is made available. `0` is returned if `size` is `0` or the buffer is empty and was set to have write disabled.



**Returns:** The amount of bytes read.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | `buffer` is `NULL` |





**Since:** Haiku R1



**See also:** [SetWriteDisabled()](classBMemoryRingIO.md#ac513ffdbce33a9095a41a1c69afc367a)


Reimplemented from [BDataIO](classBDataIO.md#a847ec8576c368bf9aada412e92aed623).

---

### `SetSize()`

```cpp
status_t BMemoryRingIO::SetSize(size_t size)
```

Change the ring buffer capacity. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `size` | The new capacity for the ring buffer. This value will be rounded up to the nearest power of two. The new capacity must be larger or equal to [BytesAvailable()](classBMemoryRingIO.md#a06183c418cfe254f11d7258ca9bf8001). If set to `0` when there are no the bytes available to be read, the buffer will be freed. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation was successful. |
| B_BAD_VALUE | The new capacity is smaller than [BytesAvailable()](classBMemoryRingIO.md#a06183c418cfe254f11d7258ca9bf8001). |
| B_NO_MEMORY | Memory couldn't be allocated to grow/create the buffer. The buffer remains unchanged. |





**Since:** Haiku R1



**See also:** [BytesAvailable()](classBMemoryRingIO.md#a06183c418cfe254f11d7258ca9bf8001) for the amount of data to be read.

---

### `SetWriteDisabled()`

```cpp
void BMemoryRingIO::SetWriteDisabled(bool disabled)
```

Set whether writes to the ring buffer is disabled. 


This method controls whether further writes to the ring buffer is allowed. If writing is disabled, any further writes will error with `B_READ_ONLY_DEVICE`, and read will no longer block on an empty buffer and instead return `0`. In addition, [WaitForRead()](classBMemoryRingIO.md#afb8157e42f9ddd0a682900d2fc44a0ae) and [WaitForWrite()](classBMemoryRingIO.md#a24f6aa233c34af8ff8ee570aab5209b1) will return `B_READ_ONLY_DEVICE`.


This method is usually used to notify the writer/reader of the pipe to not write more and/or to wait for more data.


Parameters

| Parameter | Description |
| :--- | :--- |
| `disabled` | Whether writes should be disabled. |





**See also:** [WriteDisabled()](classBMemoryRingIO.md#a70803d41888b75dfacdfdd3da032b7ab) to see whether writes to the ring buffer is currently disabled.

---

### `SpaceAvailable()`

```cpp
size_t BMemoryRingIO::SpaceAvailable()
```

Get the amount of space left in the object. 



**Returns:** The remaining storage capacity of the object in bytes.



**Since:** Haiku R1



**See also:** [BufferSize()](classBMemoryRingIO.md#a5b7e271192ebe8a506201c53766489ae) for the total buffer size.

---

### `WaitForRead()`

```cpp
status_t BMemoryRingIO::WaitForRead(bigtime_t timeout = B_INFINITE_TIMEOUT)
```

Wait for data to be available for reading. 


This method will block the current thread until there's data ready to be [Read()](classBMemoryRingIO.md#a3818ee42f7273efbafc38e1c559c87cd) from the object or until timeout has been reached.


Parameters

| Parameter | Description |
| :--- | :--- |
| `timeout` | The minimum amount of time to wait in microseconds. If the value is `B_INFINITE_TIMEOUT`, this method will not return until data can be read from the object. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | There's data ready to be read. |
| B_TIMED_OUT | Timeout reached but no data has been made available. |
| B_READ_ONLY_DEVICE | The buffer has write disabled. |





**See also:** [Read()](classBMemoryRingIO.md#a3818ee42f7273efbafc38e1c559c87cd)

---

### `WaitForWrite()`

```cpp
status_t BMemoryRingIO::WaitForWrite(bigtime_t timeout = B_INFINITE_TIMEOUT)
```

Wait for space to be available for writing. 


This method will block the current thread until there are storage space available for a [Write()](classBMemoryRingIO.md#a10a76c9e67013c9439f57d14b6e43812) operation or until timeout has been reached.


Parameters

| Parameter | Description |
| :--- | :--- |
| `timeout` | The minimum amount of time to wait in microseconds. If the value is `B_INFINITE_TIMEOUT`, this method will not return until data can be written into the object. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | There's storage space to write to. |
| B_TIMED_OUT | Timeout reached but no additional storage space has been made available. |
| B_READ_ONLY_DEVICE | The buffer has write disabled. |





**See also:** [Write()](classBMemoryRingIO.md#a10a76c9e67013c9439f57d14b6e43812)

---

### `Write()`

```cpp
ssize_t BMemoryRingIO::Write(const void * buffer, size_t size)
```

Writes data from a buffer to the object. 


If the ring buffer is full, this method blocks until some space is made available.



**Returns:** The amount of bytes written. If the ring buffer is filled or `size` is `0`, `0` will be returned.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | `buffer` is `NULL` |
| B_READ_ONLY_DEVICE | Writes to the buffer has been disabled. |





**Since:** Haiku R1



**See also:** [SetWriteDisabled()](classBMemoryRingIO.md#ac513ffdbce33a9095a41a1c69afc367a)


Reimplemented from [BDataIO](classBDataIO.md#a01692303eba7601c6a7cfa72c06d6afb).

---

### `WriteDisabled()`

```cpp
bool BMemoryRingIO::WriteDisabled()
```

Indicates whether writes to the ring buffer is disabled. 


This method indicates whether further writes to the ring buffer is allowed. See [SetWriteDisabled()](classBMemoryRingIO.md#ac513ffdbce33a9095a41a1c69afc367a) for more information.



**See also:** [SetWriteDisabled()](classBMemoryRingIO.md#ac513ffdbce33a9095a41a1c69afc367a) to control whether writes to the ring buffer is disabled.



**Returns:** `true` if writes to the ring buffer is disabled, `false` if not.

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMemoryRingIO.html).
