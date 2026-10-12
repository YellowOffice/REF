---
name: BAttributedMailAttachment
type: class
kit: mail_kit
brief: "Represents an mail attachment compatible with Be File System attributes"
source: haiku-book
---

# BAttributedMailAttachment Class
**Kit/Group:** [Mail Kit](../mail_kit/group__mail.md) | [Mail Kit library (libmail.so)](group__libmail.md)

## Description

Represents an mail attachment compatible with Be File System attributes. 


This class builds a multipart container where the attached file is copied alongside its Be File System attributes, allowing to send or receive files without losing those filesystem attributes.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BAttributedMailAttachment](#a3d7128e1e2f8db9e92a4a252229ac904) () — Creates an uninitialized BAttributedMailAttachment object.
* [BAttributedMailAttachment](#a52d3f19929a1fdf6461f1eb0aecf68ce) (BFile *file, bool delete_when_done) — Creates and initializes an attachment object from a file.
* [BAttributedMailAttachment](#aab12ef3a27d1ed30621e518f03d97a77) (entry_ref *ref) — Creates and initializes an attachment object from a filesystem entry.
* `virtual` [~BAttributedMailAttachment](#aeef80ea7c5e63697c7b7bb1a94ebce61) () — Frees all resources associated with this object.
* `virtual status_t` [InitCheck](#a22f272c7af57056b5df675df6898b8a6) () — Checks whether the object has been properly initialized or not.
* `virtual status_t` [MIMEType](#a9f00a42aa935ff5ff8e272c86137a8cb) (BMimeType *mime) — Places the MIME type of the data into mime.
* `virtual status_t` [RenderToRFC822](#a632eea4d8e4b743b9e759e3935c7a5ff) (BPositionIO *render_to) — Renders the component into RFC-822 format.
* `void` [SaveToDisk](#a59a7fca1d6210c3a0c49035493a9eeb5) (BEntry *entry) — Stores the attachment's decoded data in a temporary file on disk.
* `virtual status_t` [SetTo](#aa57e7405d84466119418e2ddcb2980c5) (BFile *file, bool delete_file_when_done=false) — Initializes the object to the specified file.
* `virtual status_t` [SetTo](#a360820343eb6d9263d581f4ad3f86d5a) (entry_ref *ref) — Initializes the object to the specified entry_ref.
* `virtual status_t` [SetToRFC822](#a9aad3eb693e7cbae8212a4bb90eb2423) (BPositionIO *data, size_t length, bool parse_now=false) — Sets this object from a data stream in a RFC-822 compliant format.
* `void` [SetEncoding](#a6d73d7697989b72fdfb025fa0b277bb8) (mail_encoding encoding) — Sets the Content-Transfer-Encoding header to encoding.
* `mail_encoding` [Encoding](#a89e489576b9f05c482c7d352cc101c85) () — Returns the current Content-Transfer-Encoding header value.
* `virtual status_t` [FileName](#a528b97b02936a07f5382686c73ab45c0) (char *name) — Returns the attachment's filename.
* `virtual void` [SetFileName](#a089fa84bc5b55ae20ac3c28cea77e18c) (const char *name) — Changes the attachment's filename.
* `virtual status_t` [GetDecodedData](#a4e25615f55b2d5af9f960bf63d45b4b5) (BPositionIO *data) — Retrieves the attachment's decoded data with its attributes and writes them into data.
* `virtual status_t` [SetDecodedData](#ac687282eb7e6ecfb5522122401b4a3c9) (BPositionIO *data) — Sets the attachment's attributes and data to data.
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

### `BAttributedMailAttachment()`

```cpp
BAttributedMailAttachment::BAttributedMailAttachment(BFile * file, bool delete_when_done)
```

Creates and initializes an attachment object from a file. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | A file to be used for the attachment. |
| `delete_when_done` | Tells if the file has to be deleted when this object is destroyed. |





**See also:** [SetTo(BFile*, bool)](classBAttributedMailAttachment.md#aa57e7405d84466119418e2ddcb2980c5)



**Since:** Haiku R1

---

### `BAttributedMailAttachment()`

```cpp
BAttributedMailAttachment::BAttributedMailAttachment(entry_ref * ref)
```

Creates and initializes an attachment object from a filesystem entry. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The filesystem entry from where to retrieve the attachment's data. |





**See also:** [SetTo(entry_ref*)](classBAttributedMailAttachment.md#a360820343eb6d9263d581f4ad3f86d5a)



**Since:** Haiku R1

---

### `BAttributedMailAttachment()`

```cpp
BAttributedMailAttachment::BAttributedMailAttachment()
```

Creates an uninitialized [BAttributedMailAttachment](classBAttributedMailAttachment.md) object. 


It can be later be initialized with either [SetTo(BFile*, bool)](classBAttributedMailAttachment.md#aa57e7405d84466119418e2ddcb2980c5) or [SetTo(entry_ref *)](classBAttributedMailAttachment.md#a360820343eb6d9263d581f4ad3f86d5a).



**Since:** Haiku R1

---

### `~BAttributedMailAttachment()`

```cpp
BAttributedMailAttachment::~BAttributedMailAttachment()
```

Frees all resources associated with this object. 



**Since:** Haiku R1

---

### `Encoding()`

```cpp
mail_encoding BAttributedMailAttachment::Encoding()
```

Returns the current Content-Transfer-Encoding header value. 



**Since:** Haiku R1

---

### `FileName()`

```cpp
status_t BAttributedMailAttachment::FileName(char * name)
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
status_t BAttributedMailAttachment::GetDecodedData(BPositionIO * data)
```

Retrieves the attachment's decoded data with its attributes and writes them into *data*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A [BPositionIO](../support_kit/classBPositionIO.md) based data stream where to write the output data. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The decoded data and attributes were retrieved successfully. |
| B_IO_ERROR | There is internally no data associated with this attachment. |
| B_BAD_VALUE | *data* is invalid. |





**Since:** Haiku R1


Reimplemented from [BMailComponent](classBMailComponent.md#a46e65753239d6efe7856aafe02a7cc27).

---

### `InitCheck()`

```cpp
status_t BAttributedMailAttachment::InitCheck()
```

Checks whether the object has been properly initialized or not. 



**Returns:** `B_OK` if the object has been properly initialized, or `B_NO_INIT` otherwise.



**Since:** Haiku R1


Implements [BMailAttachment](classBMailAttachment.md#aaf83d1814571300858fbb53894a028c4).

---

### `MIMEType()`

```cpp
status_t BAttributedMailAttachment::MIMEType(BMimeType * mime)
```

Places the MIME type of the data into *mime*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `mime` | A pre-allocated [BMimeType](../storage_kit/classBMimeType.md) variable where to write the mimetype. |





**Since:** Haiku R1


Reimplemented from [BMailComponent](classBMailComponent.md#a59da0d548d0bd23a29c7e9e043843377).

---

### `RenderToRFC822()`

```cpp
status_t BAttributedMailAttachment::RenderToRFC822(BPositionIO * render_to)
```

Renders the component into RFC-822 format. 



**Returns:** `B_OK` if everything was performed successfully, or an error code otherwise.



**Since:** Haiku R1


Reimplemented from [BMailComponent](classBMailComponent.md#a1b38a761364e8cc7bcab62f921db1ee3).

---

### `SaveToDisk()`

```cpp
void BAttributedMailAttachment::SaveToDisk(BEntry * entry)
```

Stores the attachment's decoded data in a temporary file on disk. 


The file path will be saved to *entry*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | A pre-allocated [BEntry](../storage_kit/classBEntry.md) where to write the temporary file path. |





**Since:** Haiku R1

---

### `SetDecodedData()`

```cpp
status_t BAttributedMailAttachment::SetDecodedData(BPositionIO * data)
```

Sets the attachment's attributes and data to *data*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The data stream from where the data and the attributes will be copied. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | No error. |





**Since:** Haiku R1


Reimplemented from [BMailComponent](classBMailComponent.md#aba4b4e0d158e5c6c66cfd37b2fc38dd4).

---

### `SetEncoding()`

```cpp
void BAttributedMailAttachment::SetEncoding(mail_encoding encoding)
```

Sets the Content-Transfer-Encoding header to *encoding*. 



**Since:** Haiku R1

---

### `SetFileName()`

```cpp
void BAttributedMailAttachment::SetFileName(const char * name)
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
status_t BAttributedMailAttachment::SetTo(BFile * file, bool delete_file_when_done = false)
```

Initializes the object to the specified *file*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | A file to be used for the attachment. |
| `delete_file_when_done` | Tells if the file has to be deleted when this object is destroyed. |





**Returns:** `B_OK` on success or an error code otherwise.



**Since:** Haiku R1


Implements [BMailAttachment](classBMailAttachment.md#aef8e92f96085efae9a65d18d2a2c3529).

---

### `SetTo()`

```cpp
status_t BAttributedMailAttachment::SetTo(entry_ref * ref)
```

Initializes the object to the specified [entry_ref](../storage_kit/structentry__ref.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | An [entry_ref](../storage_kit/structentry__ref.md) for the attachment's data. |





**Returns:** `B_OK` on success or an error code otherwise.



**Since:** Haiku R1


Implements [BMailAttachment](classBMailAttachment.md#a4d5fb5473f7a90a44b844b3bc58bf4f0).

---

### `SetToRFC822()`

```cpp
status_t BAttributedMailAttachment::SetToRFC822(BPositionIO * data, size_t length, bool parse_now = false)
```

Sets this object from a *data* stream in a [RFC-822](https://www.ietf.org/rfc/rfc822.txt) compliant format. 


Initializes this component to the RFC 822 format data in *data*, starting at `data->Position()`, for up to *length* bytes.


If *parse_now* is `false`, then the data will not be parsed until [RenderToRFC822()](classBAttributedMailAttachment.md#a632eea4d8e4b743b9e759e3935c7a5ff) is called.


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
| B_BAD_TYPE | The underlying multipart container mimetype is invalid. |
| B_BAD_VALUE | The data and attributes are `NULL`. |
| B_NO_MEMORY | Not enough memory to decode the attachment's attributes. |
| B_IO_ERROR | Input/output error retrieving the attributes' data. |





**Since:** Haiku R1


Reimplemented from [BMailComponent](classBMailComponent.md#a95a1764eb1e70b410be3bf7e3137d855).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBAttributedMailAttachment.html).
