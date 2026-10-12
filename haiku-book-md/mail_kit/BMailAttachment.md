---
name: BMailAttachment
type: class
kit: mail_kit
brief: "Abstract interface for objects that handle mail attachments"
source: haiku-book
---

# BMailAttachment Class
**Kit/Group:** [Mail Kit](../mail_kit/group__mail.md) | [Mail Kit library (libmail.so)](group__libmail.md)

## Description

Abstract interface for objects that handle mail attachments. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* `virtual status_t` [InitCheck](#aaf83d1814571300858fbb53894a028c4) ()=0 — Pure virtual to check if the object was successfully initialized.
* `virtual status_t` [SetTo](#aef8e92f96085efae9a65d18d2a2c3529) (BFile *file, bool deleteFileWhenDone=false)=0 — Pure virtual to initialize the object's attached file.
* `virtual status_t` [SetTo](#a4d5fb5473f7a90a44b844b3bc58bf4f0) (entry_ref *ref)=0 — Pure virtual to initialize the object's attached file.
* `virtual void` [SetFileName](#a6cc715e62b04b35a85e0fdce0d4d5ff6) (const char *name)=0 — Pure virtual to change the filename of the attachment.
* `virtual status_t` [FileName](#a813029bf32c5052125b6ddb2b432160d) (char *name)=0 — Pure virtual to return the filename of the attachment.
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

### `FileName()`

```cpp
status_t BMailAttachment::FileName(char * name)
```

Pure virtual to return the filename of the attachment. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | A pre-allocated variable of `B_FILE_NAME_LENGTH` length where to write the filename. |





**Returns:** A status code.



**Since:** Haiku R1


Implemented in [BSimpleMailAttachment](classBSimpleMailAttachment.md#a5725088ae0779b833e0e53888e066168), and [BAttributedMailAttachment](classBAttributedMailAttachment.md#a528b97b02936a07f5382686c73ab45c0).

---

### `InitCheck()`

```cpp
status_t BMailAttachment::InitCheck()
```

Pure virtual to check if the object was successfully initialized. 



**Returns:** A status code.



**Since:** Haiku R1


Implemented in [BSimpleMailAttachment](classBSimpleMailAttachment.md#a7b67c462a0d8e5bc8e0f6dd9f581a6d7), and [BAttributedMailAttachment](classBAttributedMailAttachment.md#a22f272c7af57056b5df675df6898b8a6).

---

### `SetFileName()`

```cpp
void BMailAttachment::SetFileName(const char * name)
```

Pure virtual to change the filename of the attachment. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The new filename string. |





**Since:** Haiku R1


Implemented in [BSimpleMailAttachment](classBSimpleMailAttachment.md#aa5438a0a66e15b9f74225cad4f2011a5), and [BAttributedMailAttachment](classBAttributedMailAttachment.md#a089fa84bc5b55ae20ac3c28cea77e18c).

---

### `SetTo()`

```cpp
status_t BMailAttachment::SetTo(BFile * file, bool deleteFileWhenDone = false)
```

Pure virtual to initialize the object's attached file. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | A file for the attachment's data. |
| `deleteFileWhenDone` | Tells if the file has to be deleted when this object is destroyed. |





**Returns:** A status code.



**Since:** Haiku R1


Implemented in [BSimpleMailAttachment](classBSimpleMailAttachment.md#a78d1e28d48870204b91b0b23325ef3a2), and [BAttributedMailAttachment](classBAttributedMailAttachment.md#aa57e7405d84466119418e2ddcb2980c5).

---

### `SetTo()`

```cpp
status_t BMailAttachment::SetTo(entry_ref * ref)
```

Pure virtual to initialize the object's attached file. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | An [entry_ref](../storage_kit/structentry__ref.md) for the attachment's data. |





**Returns:** A status code.



**Since:** Haiku R1


Implemented in [BSimpleMailAttachment](classBSimpleMailAttachment.md#afb31324d4f65fb776a4575e31b0378a5), and [BAttributedMailAttachment](classBAttributedMailAttachment.md#a360820343eb6d9263d581f4ad3f86d5a).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMailAttachment.html).
