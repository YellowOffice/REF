---
name: BBuffer
type: class
kit: media_kit
brief: "A reference to a chunk of memory useful for sharing media data between applications and nodes"
source: haiku-book
---

# BBuffer Class
**Kit/Group:** [Media Kit](../media_kit/group__media.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A reference to a chunk of memory useful for sharing media data between applications and nodes.

## Member List

### Public Member Functions

* `media_audio_header *` [AudioHeader](#acd2a32e5f8230de5b7c2ee7fedb8c593) () — Gets a pointer to the header of the audio buffer.
* `buffer_clone_info` [CloneInfo](#a0cba66df5a17f4621c32546e679980ce) () const — Gets the buffer_clone_info struct that describes the buffer.
* `void *` [Data](#a0f46ae6790a79ec6a20b8ef3934c14a4) () — Gets a pointer to the data of the buffer.
* `uint32` [Flags](#a0431f6e78452ff5009d10cda57dd4f98) () — Gets the flags of the buffer.
* `media_header *` [Header](#a27e31a7322ff1ccc65742952467bd317) () — Gets a pointer to the header of the buffer.
* `media_buffer_id` [ID](#aafc2c2aa5d008a06efbcfc33a3fe9c12) () — Gets the ID of the buffer according to the App Server.
* `void` Recycle () — Recycles the buffer so that it can be reused.
* `void` [SetSizeUsed](#aea0ea88878c68f7e79cb262f72dcacc4) (size_t used) — Sets the size of the buffer that is used in bytes.
* `size_t` [Size](#aad70a9423ff721c57cf4209e8b8a28cd) () — Gets the size of the buffer in bytes.
* `size_t` [SizeAvailable](#a2559ff70225558ef1bc75d166e238e6d) () — Gets the size of the buffer in bytes. Alias for Size().
* `size_t` [SizeUsed](#af284b6bf16f97588588d4c9e6b5beaff) () — Gets the size of the portion of the buffer that is currently in use in bytes.
* `media_type` [Type](#a409a98b5c569d14519cc6aea462214d0) () — Gets the media type of the data in the buffer.
* `media_video_header *` [VideoHeader](#a17ad998b75258cc7a8de859ad22a03ce) () — Gets a pointer to a header of the video buffer.

## Detailed Member Documentation

### `AudioHeader()`

```cpp
media_audio_header * BBuffer::AudioHeader()
```

Gets a pointer to the header of the audio buffer. 



**Returns:** A pointer to the header of the audio buffer.

---

### `CloneInfo()`

```cpp
buffer_clone_info BBuffer::CloneInfo()const
```

Gets the `buffer_clone_info` struct that describes the buffer. 



**Returns:** The a clone of the `buffer_clone_info` struct.

---

### `Data()`

```cpp
void * BBuffer::Data()
```

Gets a pointer to the data of the buffer. 



**Returns:** A void* pointer to the data.

---

### `Flags()`

```cpp
uint32 BBuffer::Flags()
```

Gets the flags of the buffer. 



**Returns:** The buffer flags.

---

### `Header()`

```cpp
media_header * BBuffer::Header()
```

Gets a pointer to the header of the buffer. 



**Returns:** A pointer to the header of the buffer.

---

### `ID()`

```cpp
media_buffer_id BBuffer::ID()
```

Gets the ID of the buffer according to the App Server. 



**Returns:** The App Server's ID of the buffer.

---

### `SetSizeUsed()`

```cpp
void BBuffer::SetSizeUsed(size_t size_used)
```

Sets the size of the buffer that is used in bytes. 


This method should be called after writing data to the buffer.

---

### `Size()`

```cpp
size_t BBuffer::Size()
```

Gets the size of the buffer in bytes. 


Alias for [SizeAvailable()](classBBuffer.md#a2559ff70225558ef1bc75d166e238e6d).



**Returns:** The size of the buffer in bytes.

---

### `SizeAvailable()`

```cpp
size_t BBuffer::SizeAvailable()
```

Gets the size of the buffer in bytes. Alias for [Size()](classBBuffer.md#aad70a9423ff721c57cf4209e8b8a28cd). 



**Returns:** The buffer size in bytes

---

### `SizeUsed()`

```cpp
size_t BBuffer::SizeUsed()
```

Gets the size of the portion of the buffer that is currently in use in bytes. 



**Returns:** The currently used portion of the buffer size in bytes.

---

### `Type()`

```cpp
media_type BBuffer::Type()
```

Gets the media type of the data in the buffer. 



**Returns:** The media type of the data in the buffer.

---

### `VideoHeader()`

```cpp
media_video_header * BBuffer::VideoHeader()
```

Gets a pointer to a header of the video buffer. 



**Returns:** A pointer to a header of the video buffer.

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBBuffer.html).
