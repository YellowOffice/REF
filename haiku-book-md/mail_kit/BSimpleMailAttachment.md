---
name: BSimpleMailAttachment
type: class
kit: mail_kit
brief: "Represents a basic mail attachment"
source: haiku-book
---

# BSimpleMailAttachment Class
**Kit/Group:** [Mail Kit](../mail_kit/group__mail.md) | [Mail Kit library (libmail.so)](group__libmail.md)

## Description

Represents a basic mail attachment. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BSimpleMailAttachment](#a6190bea1534b3cfcbd696fef7c22ff6b) () — Creates an uninitialized BSimpleMailAttachment object.
* [BSimpleMailAttachment](#a7fa7b86c9081b6ecaa35f3efcb6f9eeb) (BFile *file, bool delete_when_done) — Creates and initializes an attachment object from a file.
* [BSimpleMailAttachment](#a6292c61b6ff6f741e32615e05c3a88fb) (BPositionIO *dataToAttach, mail_encoding encoding=base64) — Creates and initializes an attachment object from a BPositionIO based data stream.
* [BSimpleMailAttachment](#abfeb754b39bbe7033b755321166c8a32) (const void *dataToAttach, size_t lengthOfData, mail_encoding encoding=base64) — Creates and initializes an attachment object from a buffer.
* [BSimpleMailAttachment](#a597e2f23dbbfa34640150ba8cc5ead1a) (entry_ref *ref) — Creates and initializes an attachment object from a filesystem entry.
* `virtual` [~BSimpleMailAttachment](#a01222310d1e787fe438003882b6429e0) () — Frees all resources associated with this object.
* `virtual status_t` [InitCheck](#a7b67c462a0d8e5bc8e0f6dd9f581a6d7) () — Checks whether the object has been properly initialized or not.
* `virtual status_t` [RenderToRFC822](#a03f21854f1ca9ccfee0181b7c8757c03) (BPositionIO *render_to) — Renders the component into RFC-822 format.
* `virtual status_t` [SetTo](#a78d1e28d48870204b91b0b23325ef3a2) (BFile *file, bool delete_file_when_done=false) — Initializes the object to the specified file.
* `virtual status_t` [SetTo](#afb31324d4f65fb776a4575e31b0378a5) (entry_ref *ref) — Initializes the object to the specified entry_ref.
* `virtual status_t` [SetToRFC822](#a7a6ba96c4c777f33ac6944e7f6fc3508) (BPositionIO *data, size_t length, bool parse_now=false) — Sets this object from a data stream in a RFC-822 compliant format.
* `virtual void` [SetFileName](#aa5438a0a66e15b9f74225cad4f2011a5) (const char *name) — Changes the attachment's filename.
* `virtual status_t` [FileName](#a5725088ae0779b833e0e53888e066168) (char *name) — Returns the attachment's filename.
* `virtual status_t` [GetDecodedData](#a6617ef80822c8f1dcddc0d513d5f8f9e) (BPositionIO *data) — Converts the attachment's encoded data back to its unencoded form and writes the result into data.
* `virtual status_t` [SetDecodedData](#a24c937455f8c43081f987dd16f93ecab) (BPositionIO *data) — Sets the attachment's content to data.
* `virtual BPositionIO *` [GetDecodedData](#a041765ef148664d4e85c4a1a58b3cdfd) () — Decodes the attachment's encoded data and returns the result to a BPositionIO based data stream.
* `virtual status_t` [SetDecodedData](#a739b1970f087efdfcad3bd0039c5b1be) (const void *data, size_t length) — Sets the attachment's content to the contents in the data generic buffer of length.
* `virtual status_t` [SetDecodedDataAndDeleteWhenDone](#acc40e93e5dfd37efa977ab42d631ca1d) (BPositionIO *data) — Sets the attachment's content to the contents contained in data.
* `void` [SetEncoding](#aa28fd047f74ecbe9a6f3f0ca51a9c7d5) (mail_encoding encoding=base64) — Sets the Content-Transfer-Encoding header to encoding.
* `mail_encoding` [Encoding](#ad5d0cc3908675efa09615cb952a6a048) () — Returns the current Content-Transfer-Encoding header value.
* `virtual status_t` [InitCheck](#aaf83d1814571300858fbb53894a028c4) ()=0 — Pure virtual to check if the object was successfully initialized.
* `virtual status_t` [SetTo](#aef8e92f96085efae9a65d18d2a2c3529) (BFile *file, bool deleteFileWhenDone=false)=0 — Pure virtual to initialize the object's attached file.
* `virtual status_t` [SetTo](#a4d5fb5473f7a90a44b844b3bc58bf4f0) (entry_ref *ref)=0 — Pure virtual to initialize the object's attached file.
* [BMailComponent](#a896e3d00ea10a8e0a606e892a68006cc) (uint32 defaultCharSet=B_MAIL_NULL_CONVERSION) — Initializes a new BMailComponent with the specified character set.
* `virtual` ~BMailComponent () — Destructor.
* `uint32` [ComponentType](#a31efb4b32fb435918e9ada3afd2dc424) () — Returns the component_type of this object.
* `virtual status_t` [GetDecodedData](#a46e65753239d6efe7856aafe02a7cc27) (BPositionIO *data) — Retrieves the data contained in this component in canonical format and places it into data.
* `const char *` [HeaderAt](#a06cb67bf4ec90ca225ed5cf4c8cf115b) (int32 index) const — Returns the key of the header at index.
* `status_t` [HeaderField](#ac83168c9e94be178a111402eb4ac6484) (const char *key, BMessage *structured_header, int32 index=0) const — Returns the header key.
* `const char *` [HeaderField](#abc5f64496ba534360d0b1e9dcc0f17e4) (const char *key, int32 index=0) const — Returns the header key.
* `bool` [IsAttachment](#ab66ce045c8b608e7064bc091868d8953) () — Employs simple heuristics such as the MIME type and the Content-Disposition: header to determine whether this component is an attachment.
* `virtual status_t` [MIMEType](#a59da0d548d0bd23a29c7e9e043843377) (BMimeType *mime) — Places the MIME type of the data into mime.
* `status_t` [RemoveHeader](#a58bbcaedf4bb7d71e765835f4f4b92f5) (const char *key) — Removes all headers with the key key.
* `virtual status_t` [RenderToRFC822](#a1b38a761364e8cc7bcab62f921db1ee3) (BPositionIO *render_to) — Renders the component into RFC-822 format.
* `virtual status_t` [SetDecodedData](#aba4b4e0d158e5c6c66cfd37b2fc38dd4) (BPositionIO *data) — Sets the content of this component to the canonical format data contained in data.
* `void` [SetHeaderField](#ac918b8e513ea48fc9df181e96d88e22d) (const char *key, BMessage *structured_header, bool replace_existing=true) — Adds a structured header of type key to the component.
* `void` [SetHeaderField](#acdb63a023d53293efda55180466dd14f) (const char *key, const char *value, uint32 charset=B_MAIL_NULL_CONVERSION, mail_encoding encoding=null_encoding, bool replace_existing=true) — Adds the specified header of type key and with the value to the component.
* `virtual status_t` [SetToRFC822](#a95a1764eb1e70b410be3bf7e3137d855) (BPositionIO *data, size_t length, bool parse_now=false) — Sets this object from a component in RFC-822 format.
* `BMailComponent *` [WhatIsThis](#ab7986c49344a2f9b14ede9974788a03a) () — Employs simple heuristics such as the MIME type to present you with an instance of a useful subclass.

## Detailed Member Documentation

### `BSimpleMailAttachment()`

```cpp
BSimpleMailAttachment::BSimpleMailAttachment(BPositionIO * dataToAttach, mail_encoding encoding = base64)
```

Creates and initializes an attachment object from a [BPositionIO](../support_kit/classBPositionIO.md) based data stream. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dataToAttach` | The data to attach. |
| `encoding` | The encoding format to use in the attachment object. |





**Since:** Haiku R1

---

### `BSimpleMailAttachment()`

```cpp
BSimpleMailAttachment::BSimpleMailAttachment(const void * dataToAttach, size_t lengthOfData, mail_encoding encoding = base64)
```

Creates and initializes an attachment object from a buffer. 


This constructor takes ownership of the data. This means that the data is deleted upon new calls of [SetDecodedData()](classBSimpleMailAttachment.md#a24c937455f8c43081f987dd16f93ecab) and when the object is destroyed as well.


Parameters

| Parameter | Description |
| :--- | :--- |
| `dataToAttach` | A buffer for the attachment data. |
| `lengthOfData` | The buffer length. |
| `encoding` | The encoding format to use in the attachment object. |





**Since:** Haiku R1

---

### `BSimpleMailAttachment()`

```cpp
BSimpleMailAttachment::BSimpleMailAttachment(BFile * file, bool delete_when_done)
```

Creates and initializes an attachment object from a file. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | A file for the attachment. |
| `delete_when_done` | Tells if the file has to be deleted when this object is destroyed. |





**See also:** [SetTo(BFile*, bool)](classBSimpleMailAttachment.md#a78d1e28d48870204b91b0b23325ef3a2)



**Since:** Haiku R1

---

### `BSimpleMailAttachment()`

```cpp
BSimpleMailAttachment::BSimpleMailAttachment(entry_ref * ref)
```

Creates and initializes an attachment object from a filesystem entry. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The filesystem entry from where to retrieve the attachment's data. |





**See also:** [SetTo(entry_ref*)](classBSimpleMailAttachment.md#afb31324d4f65fb776a4575e31b0378a5)



**Since:** Haiku R1

---

### `BSimpleMailAttachment()`

```cpp
BSimpleMailAttachment::BSimpleMailAttachment()
```

Creates an uninitialized [BSimpleMailAttachment](classBSimpleMailAttachment.md) object. 


It can be later be initialized with either [SetTo(BFile*, bool)](classBSimpleMailAttachment.md#a78d1e28d48870204b91b0b23325ef3a2) or [SetTo(entry_ref *)](classBSimpleMailAttachment.md#afb31324d4f65fb776a4575e31b0378a5).



**Since:** Haiku R1

---

### `~BSimpleMailAttachment()`

```cpp
BSimpleMailAttachment::~BSimpleMailAttachment()
```

Frees all resources associated with this object. 



**Since:** Haiku R1

---

### `Encoding()`

```cpp
mail_encoding BSimpleMailAttachment::Encoding()
```

Returns the current Content-Transfer-Encoding header value. 



**Since:** Haiku R1

---

### `FileName()`

```cpp
status_t BSimpleMailAttachment::FileName(char * name)
```

Returns the attachment's filename. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | A pre-allocated variable of `B_FILE_NAME_LENGTH` length where to write the filename. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The filename was retrieved successfully. |
| B_NAME_NOT_FOUND | The filename could not be found. |





**Since:** Haiku R1


Implements [BMailAttachment](classBMailAttachment.md#a813029bf32c5052125b6ddb2b432160d).

---

### `GetDecodedData()`

```cpp
BPositionIO * BSimpleMailAttachment::GetDecodedData()
```

Decodes the attachment's encoded data and returns the result to a [BPositionIO](../support_kit/classBPositionIO.md) based data stream. 



**Since:** Haiku R1

---

### `GetDecodedData()`

```cpp
status_t BSimpleMailAttachment::GetDecodedData(BPositionIO * data)
```

Converts the attachment's encoded data back to its unencoded form and writes the result into *data*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A [BPositionIO](../support_kit/classBPositionIO.md) based data stream where to write the output data. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The attachment's data was written into *data* successfully. |
| B_IO_ERROR | There is internally no data associated with this attachment. |
| B_BAD_VALUE | *data* is invalid. |





**Since:** Haiku R1


Reimplemented from [BMailComponent](classBMailComponent.md#a46e65753239d6efe7856aafe02a7cc27).

---

### `InitCheck()`

```cpp
status_t BSimpleMailAttachment::InitCheck()
```

Checks whether the object has been properly initialized or not. 



**Returns:** `B_OK` if the object has been properly initialized, or `B_NO_INIT` otherwise.



**Since:** Haiku R1


Implements [BMailAttachment](classBMailAttachment.md#aaf83d1814571300858fbb53894a028c4).

---

### `RenderToRFC822()`

```cpp
status_t BSimpleMailAttachment::RenderToRFC822(BPositionIO * render_to)
```

Renders the component into RFC-822 format. 



**Returns:** `B_OK` if everything was performed successfully, or an error code otherwise.



**Since:** Haiku R1


Reimplemented from [BMailComponent](classBMailComponent.md#a1b38a761364e8cc7bcab62f921db1ee3).

---

### `SetDecodedData()`

```cpp
status_t BSimpleMailAttachment::SetDecodedData(BPositionIO * data)
```

Sets the attachment's content to *data*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The data stream from where the data will be copied. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | No error. |





**Since:** Haiku R1


Reimplemented from [BMailComponent](classBMailComponent.md#aba4b4e0d158e5c6c66cfd37b2fc38dd4).

---

### `SetDecodedData()`

```cpp
status_t BSimpleMailAttachment::SetDecodedData(const void * data, size_t length)
```

Sets the attachment's content to the contents in the *data* generic buffer of *length*. 


This overloaded version takes ownership of the data buffer, so the data is deleted upon new calls of [SetDecodedData()](classBSimpleMailAttachment.md#a24c937455f8c43081f987dd16f93ecab) and when the object is destroyed as well.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The buffer from where obtain the new contents of the attachment. |
| `length` | The buffer's length. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | No error. |





**Since:** Haiku R1

---

### `SetDecodedDataAndDeleteWhenDone()`

```cpp
status_t BSimpleMailAttachment::SetDecodedDataAndDeleteWhenDone(BPositionIO * data)
```

Sets the attachment's content to the contents contained in *data*. 


This method takes ownership of the data buffer, so the data is deleted upon new calls of [SetDecodedData()](classBSimpleMailAttachment.md#a24c937455f8c43081f987dd16f93ecab) and when the object is destroyed as well.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The source from where obtain the new contents of the attachment. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | No error. |





**Since:** Haiku R1

---

### `SetEncoding()`

```cpp
void BSimpleMailAttachment::SetEncoding(mail_encoding encoding = base64)
```

Sets the Content-Transfer-Encoding header to *encoding*. 



**Since:** Haiku R1

---

### `SetFileName()`

```cpp
void BSimpleMailAttachment::SetFileName(const char * name)
```

Changes the attachment's filename. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The new filename string for the attachment. |





**Since:** Haiku R1


Implements [BMailAttachment](classBMailAttachment.md#a6cc715e62b04b35a85e0fdce0d4d5ff6).

---

### `SetTo()`

```cpp
status_t BSimpleMailAttachment::SetTo(BFile * file, bool delete_file_when_done = false)
```

Initializes the object to the specified *file*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | A file for the attachment. |
| `delete_file_when_done` | Tells if the file has to be deleted when this object is destroyed. |





**Returns:** `B_OK` on success or an error code otherwise.



**Since:** Haiku R1


Implements [BMailAttachment](classBMailAttachment.md#aef8e92f96085efae9a65d18d2a2c3529).

---

### `SetTo()`

```cpp
status_t BSimpleMailAttachment::SetTo(entry_ref * ref)
```

Initializes the object to the specified [entry_ref](../storage_kit/structentry__ref.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The [entry_ref](../storage_kit/structentry__ref.md) for the attachment's data. |





**Returns:** `B_OK` on success or an error code otherwise.



**Since:** Haiku R1


Implements [BMailAttachment](classBMailAttachment.md#a4d5fb5473f7a90a44b844b3bc58bf4f0).

---

### `SetToRFC822()`

```cpp
status_t BSimpleMailAttachment::SetToRFC822(BPositionIO * data, size_t length, bool parse_now = false)
```

Sets this object from a *data* stream in a [RFC-822](https://www.ietf.org/rfc/rfc822.txt) compliant format. 


Initializes this component to the RFC 822 format data in *data*, starting at `data->Position()`, for up to *length* bytes.


If *parse_now* is `false`, then the data will not be parsed (encoded) until [RenderToRFC822()](classBSimpleMailAttachment.md#a03f21854f1ca9ccfee0181b7c8757c03) is called.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The data source. |
| `length` | The data's length. |
| `parse_now` | Whether the data will be parsed now or not. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation was performed successfully. |
| B_ERROR | Error in MIME headers' length. |





**Since:** Haiku R1


Reimplemented from [BMailComponent](classBMailComponent.md#a95a1764eb1e70b410be3bf7e3137d855).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBSimpleMailAttachment.html).
