---
name: BBufferedDataIO
type: class
kit: support_kit
brief: "Undocumented class"
source: haiku-book
---

# BBufferedDataIO Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Undocumented class. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BBufferedDataIO](#a14247dfc82837620926ea27a4b366a87) (BDataIO &stream, size_t bufferSize=65536L, bool ownsStream=true, bool partialReads=false) — Undocumented public method.
* `virtual` [~BBufferedDataIO](#ab4f07b2711e0e6a3aa3314543aad2e75) () — Undocumented public method.
* `size_t` [BufferSize](#a86486fc86db946101955e9434ced9e73) () const — Undocumented public method.
* `status_t` [Flush](#a7a1cd3147b96744c2e3646db4cb6c995) () — Undocumented public method.
* `status_t` [InitCheck](#afce2817f7fefa830225ba2977f79ba67) () const — Undocumented public method.
* `bool` [OwnsStream](#a86daec9e1251fcd8be5a49bf4e80e908) () const — Undocumented public method.
* `virtual ssize_t` [Read](#aef91ed925bd2f40a4332dff9a7cbdb28) (void *buffer, size_t size) — Undocumented public method.
* `void` [SetOwnsStream](#a4ab727d95a58d68cd1d8be3b3e3c4e8e) (bool ownsStream) — Undocumented public method.
* `BDataIO *` [Stream](#abe2fa74234dd379edab62ed06b4cf398) () const — Undocumented public method.
* `virtual ssize_t` [Write](#a6396fe1a4a153f1a70ef28e358cac037) (const void *buffer, size_t size) — Undocumented public method.
* [BDataIO](#a67891b7afe78d6a77845dd0352218801) () — This constructor does nothing.
* `virtual` [~BDataIO](#a45daa9db670dd2e5b83efcefcf8dbaed) () — This destructor does nothing.
* `virtual status_t` [Flush](#a38a8df63b367585fe5e6b6a85c406d05) () — Writes pending data to underlying storage.
* `virtual ssize_t` [Read](#a847ec8576c368bf9aada412e92aed623) (void *buffer, size_t size) — Reads data from the object into a buffer.
* `status_t` [ReadExactly](#a3a0b0fc36232531a1d8c1144a7d75741) (void *buffer, size_t size, size_t *_bytesRead=NULL) — Reads an exact amount of data from the object into a buffer.
* `virtual ssize_t` [Write](#a01692303eba7601c6a7cfa72c06d6afb) (const void *buffer, size_t size) — Writes data from a buffer to the object.
* `status_t` [WriteExactly](#a0095cfffa454a82eac3dedda2e187ab7) (const void *buffer, size_t size, size_t *_bytesWritten=NULL) — Writes an exact amount of data from a buffer to the object.

## Detailed Member Documentation

### `BBufferedDataIO()`

```cpp
BBufferedDataIO::BBufferedDataIO(BDataIO & stream, size_t bufferSize = 65536L, bool ownsStream = true, bool partialReads = false)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `stream` | Undocumented |
| `bufferSize` | Undocumented |
| `ownsStream` | Undocumented |
| `partialReads` | Undocumented |





**Since:** Haiku R1

---

### `~BBufferedDataIO()`

```cpp
BBufferedDataIO::~BBufferedDataIO()
```

Undocumented public method. 



**Since:** Haiku R1

---

### `BufferSize()`

```cpp
size_t BBufferedDataIO::BufferSize()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Flush()`

```cpp
status_t BBufferedDataIO::Flush()
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Reimplemented from [BDataIO](classBDataIO.md#a38a8df63b367585fe5e6b6a85c406d05).

---

### `InitCheck()`

```cpp
status_t BBufferedDataIO::InitCheck()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `OwnsStream()`

```cpp
bool BBufferedDataIO::OwnsStream()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Read()`

```cpp
ssize_t BBufferedDataIO::Read(void * buffer, size_t size)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | Undocumented |
| `size` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Reimplemented from [BDataIO](classBDataIO.md#a847ec8576c368bf9aada412e92aed623).

---

### `SetOwnsStream()`

```cpp
void BBufferedDataIO::SetOwnsStream(bool ownsStream)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ownsStream` | Undocumented |





**Since:** Haiku R1

---

### `Stream()`

```cpp
BDataIO * BBufferedDataIO::Stream()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Write()`

```cpp
ssize_t BBufferedDataIO::Write(const void * buffer, size_t size)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | Undocumented |
| `size` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Reimplemented from [BDataIO](classBDataIO.md#a01692303eba7601c6a7cfa72c06d6afb).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBBufferedDataIO.html).
