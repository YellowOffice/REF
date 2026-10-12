---
name: BBitmapStream
type: class
kit: translation_kit
brief: "Provides for the conversion of a Translation Kit bitmap object to a BBitmap"
source: haiku-book
---

# BBitmapStream Class
**Kit/Group:** [Translation Kit](../translation_kit/group__translation.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Provides for the conversion of a Translation Kit bitmap object to a [BBitmap](../interface_kit/classBBitmap.md). 


[BBitmapStream](classBBitmapStream.md) is limited subclass of [BPositionIO](../support_kit/classBPositionIO.md) that is good at reading and writing Translation Kit bitmaps. The [DetachBitmap()](classBBitmapStream.md#aa42001694aef557857f3dc1879a1869c) method is the main method of this class as it returns the contents of the Translation Kit bitmap object into a [BBitmap](../interface_kit/classBBitmap.md).


In most cases you shouldn't have to use this class directly as BTranslationUtils contains methods to load images from files and resources.

## Member List

### Public Member Functions

* [BBitmapStream](#a2ff1f2f2d88371f96d8cb118acd63707) (BBitmap *bitmap=NULL) — Initializes this object to either use the BBitmap passed to it as the object to read/write to or to create a BBitmap when data is written to this object.
* `virtual` ~BBitmapStream () — Destroys the object and the BBitmap object if attached.
* `status_t` [DetachBitmap](#aa42001694aef557857f3dc1879a1869c) (BBitmap **_bitmap) — Sets _bitmap to point to the internal bitmap object.
* `virtual off_t` [Position](#aa172a68e7325680c9d3210714e5330c4) () const — Gets the current stream position.
* `virtual ssize_t` [ReadAt](#a22bc134d272bac2f1979951f6d00140a) (off_t offset, void *buffer, size_t size) — Reads data from the stream into buffer at a specific position and size.
* `virtual off_t` [Seek](#af17115c38e1f19e8bbfbba3880850223) (off_t position, uint32 seekMode) — Changes the current stream position.
* `virtual status_t` [SetSize](#a47ce4b957cbde849427f8aa937d0f716) (off_t size) — Sets the size of the data.
* `virtual off_t` [Size](#a68025a63cbfbb87eaa1dda7edf188589) () const — Gets the current stream size.
* `virtual ssize_t` [WriteAt](#af48762a7326aebc52aed25315e04ef6d) (off_t offset, const void *buffer, size_t size) — Writes data to the bitmap starting at a specific position and size.
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

### Protected Member Functions

* `void` [SwapHeader](#a1787243e990879d262c26dca64535a40) (const TranslatorBitmap *source, TranslatorBitmap *destination) — Swaps the byte order of source, no matter the byte order, and copies the result to destination.

## Detailed Member Documentation

### `BBitmapStream()`

```cpp
BBitmapStream::BBitmapStream(BBitmap * bitmap = NULL)
```

Initializes this object to either use the [BBitmap](../interface_kit/classBBitmap.md) passed to it as the object to read/write to or to create a [BBitmap](../interface_kit/classBBitmap.md) when data is written to this object. 


If *bitmap* is `NULL`, a new [BBitmap](../interface_kit/classBBitmap.md) object is created when this object is written to.


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The bitmap object to read from/write to. |

---

### `DetachBitmap()`

```cpp
status_t BBitmapStream::DetachBitmap(BBitmap ** _bitmap)
```

Sets *_bitmap* to point to the internal bitmap object. 


The bitmap is not deleted when the [BBitmapStream](classBBitmapStream.md) is deleted. After the bitmap has been detached it is still used by the stream, but it is never deleted by the stream.


Once you have called [DetachBitmap()](classBBitmapStream.md#aa42001694aef557857f3dc1879a1869c) no further operations should be performed on the [BBitmapStream](classBBitmapStream.md) except to destroy the object.


Parameters

| Parameter | Description |
| :--- | :--- |
| `_bitmap` | A [BBitmap](../interface_kit/classBBitmap.md) pointer that will be set to point to the internal bitmap object. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The bitmap was detached. |
| B_BAD_VALUE | _bitmap is `NULL`. |
| B_ERROR | The internal bitmap object is `NULL` or has already been detached. |

---

### `Position()`

```cpp
off_t BBitmapStream::Position()const
```

Gets the current stream position. 



**Returns:** The current stream position.


Implements [BPositionIO](../support_kit/classBPositionIO.md#a4ebc2cd7a7493767e79fa6d88657a84a).

---

### `ReadAt()`

```cpp
ssize_t BBitmapStream::ReadAt(off_t pos, void * buffer, size_t size)
```

Reads data from the stream into *buffer* at a specific position and size. 


The first sizeof(TranslatorBitmap) bytes are the bitmap header. The header is always written out and read in as big endian byte order.


Parameters

| Parameter | Description |
| :--- | :--- |
| `pos` | The position in the stream to read from. |
| `buffer` | Where the data will be read into |
| `size` | The amount of data to be read. |





**Returns:** The amount of data written if the result is >= 0 or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | *buffer* is `NULL` or *pos* is invalid or the amount read if the result >= 0 |
| B_NO_INIT | There is no bitmap stored by the stream. |




Implements [BPositionIO](../support_kit/classBPositionIO.md#a6eb7aff1d69bf3049b2b421da52fdf8f).

---

### `Seek()`

```cpp
off_t BBitmapStream::Seek(off_t position, uint32 seekMode)
```

Changes the current stream position. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `position` | The position offset. |
| `seekMode` | Decides how the position offset is used: * `SEEK_CUR` Position is added to current stream position.  * `SEEK_END` Position is added to the end stream position.  * `SEEK_SET` The stream position is set to position. |





**Returns:** The new position offset if the result >= 0.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | *position* was bad. |




Implements [BPositionIO](../support_kit/classBPositionIO.md#af8296875d9711dd498b0fbcace028abc).

---

### `SetSize()`

```cpp
status_t BBitmapStream::SetSize(off_t size)
```

Sets the size of the data. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `size` | The size to set the stream size to. |





**Returns:** A status code, `B_NO_ERROR` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_NO_ERROR | (or `B_OK`) Size is a valid value. |
| B_BAD_VALUE | *size* is NOT a valid value. |




Reimplemented from [BPositionIO](../support_kit/classBPositionIO.md#a35613c7ee06c7c9583ca2505e1fdff28).

---

### `Size()`

```cpp
off_t BBitmapStream::Size()const
```

Gets the current stream size. 



**Returns:** The current stream size.

---

### `SwapHeader()`

```cpp
void BBitmapStream::SwapHeader(const TranslatorBitmap * source, TranslatorBitmap * destination)
```

Swaps the byte order of *source*, no matter the byte order, and copies the result to *destination*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `source` | Data to be swapped. |
| `destination` | Where the swapped data will be copied to. |

---

### `WriteAt()`

```cpp
ssize_t BBitmapStream::WriteAt(off_t pos, const void * data, size_t size)
```

Writes data to the bitmap starting at a specific position and size. 


The first sizeof(TranslatorBitmap) bytes of data must be the TranslatorBitmap header in big endian byte order or the data will not be written.


Parameters

| Parameter | Description |
| :--- | :--- |
| `pos` | The position in the stream to write to *data*. |
| `data` | The data to write to the stream. |
| `size` | The size of the data to write to the stream. |





**Returns:** The amount of data written if the result is >= 0 or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | Size is bad or data is `NULL` or *pos* is invalid. |
| B_MISMATCHED_VALUES | The bitmap header is bad. |
| B_ERROR | Error allocating memory or setting up big endian header, |




Implements [BPositionIO](../support_kit/classBPositionIO.md#a0efce1a07d1d6509e8ec00598244ace1).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBBitmapStream.html).
