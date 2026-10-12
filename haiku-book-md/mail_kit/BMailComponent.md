---
name: BMailComponent
type: class
kit: mail_kit
brief: "The base class for most of the Mail Kit"
source: haiku-book
---

# BMailComponent Class
**Kit/Group:** [Mail Kit](../mail_kit/group__mail.md) | [Mail Kit library (libmail.so)](group__libmail.md)

## Description

The base class for most of the Mail Kit. 


Note that [BMailComponent](classBMailComponent.md) is not abstract, and is useful by itself. A [BMailComponent](classBMailComponent.md) has the important quality of being able to read the headers of a message or component without instantiating whatever massive quantity of data might lie therein. This is useful primarily to determine the kind of data you are dealing with, so that the user can make a decision as to whether it should be shown.



**Since:** Haiku R1

## Member List

### Public Member Functions

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

### `BMailComponent()`

```cpp
BMailComponent::BMailComponent(uint32 defaultCharSet = B_MAIL_NULL_CONVERSION)
```

Initializes a new [BMailComponent](classBMailComponent.md) with the specified character set. 



**Since:** Haiku R1

---

### `ComponentType()`

```cpp
uint32 BMailComponent::ComponentType()
```

Returns the `component_type` of this object. 



**Since:** Haiku R1

---

### `GetDecodedData()`

```cpp
status_t BMailComponent::GetDecodedData(BPositionIO * data)
```

Retrieves the data contained in this component in canonical format and places it into *data*. 


The various attachments subclasses implement this function to return decoded data, and [BTextMailComponent](classBTextMailComponent.md) returns UTF8 text. `BMailComponent` implements this function to do nothing and return `B_OK`.



**Since:** Haiku R1


Reimplemented in [BSimpleMailAttachment](classBSimpleMailAttachment.md#a6617ef80822c8f1dcddc0d513d5f8f9e), [BAttributedMailAttachment](classBAttributedMailAttachment.md#a4e25615f55b2d5af9f960bf63d45b4b5), and [BTextMailComponent](classBTextMailComponent.md#aa09e051b9ccb894e537277ed33b60dfc).

---

### `HeaderAt()`

```cpp
const char * BMailComponent::HeaderAt(int32 index)const
```

Returns the key of the `header` at index. 


Useful for iterating through all the headers. If index is out of range, [HeaderAt()](classBMailComponent.md#a06cb67bf4ec90ca225ed5cf4c8cf115b) returns NULL.



**Since:** Haiku R1

---

### `HeaderField()`

```cpp
status_t BMailComponent::HeaderField(const char * key, BMessage * structured_header, int32 index = 0)const
```

Returns the header *key*. 


Decodes whatever structured header may exist in *key* and places it in *structured_header* according to the format laid out in [SetHeaderField()](classBMailComponent.md#acdb63a023d53293efda55180466dd14f). Returns `B_NAME_NOT_FOUND` if the header key does not exist. If it does exist, but is not structured, no error is returned; the entire contents of the header are placed in `unlabeled`.



**Since:** Haiku R1

---

### `HeaderField()`

```cpp
const char * BMailComponent::HeaderField(const char * key, int32 index = 0)const
```

Returns the header *key*. 


If there is more than one header key, use *index* to iterate through them. In the event that the specified header does not exist, [HeaderField()](classBMailComponent.md#abc5f64496ba534360d0b1e9dcc0f17e4) returns `NULL`. Thus, to retrieve the contents of the `Subject:` field, you would do this:



```cpp
const char *subject = component->HeaderField("Subject");
```


**Since:** Haiku R1

---

### `IsAttachment()`

```cpp
bool BMailComponent::IsAttachment()
```

Employs simple heuristics such as the MIME type and the Content-Disposition: header to determine whether this component is an attachment. 



**Returns:** true if it is an attachment, false if not.



**Since:** Haiku R1

---

### `MIMEType()`

```cpp
status_t BMailComponent::MIMEType(BMimeType * mime)
```

Places the MIME type of the data into mime. 



**Since:** Haiku R1


Reimplemented in [BAttributedMailAttachment](classBAttributedMailAttachment.md#a9f00a42aa935ff5ff8e272c86137a8cb).

---

### `RemoveHeader()`

```cpp
status_t BMailComponent::RemoveHeader(const char * key)
```

Removes all headers with the key *key*. 



**Since:** Haiku R1

---

### `RenderToRFC822()`

```cpp
status_t BMailComponent::RenderToRFC822(BPositionIO * data)
```

Renders the component into RFC-822 format. 


It places the result in data, starting at data->Position().



**Since:** Haiku R1


Reimplemented in [BSimpleMailAttachment](classBSimpleMailAttachment.md#a03f21854f1ca9ccfee0181b7c8757c03), [BAttributedMailAttachment](classBAttributedMailAttachment.md#a632eea4d8e4b743b9e759e3935c7a5ff), and [BTextMailComponent](classBTextMailComponent.md#a141a7071157c94d9c3569ef14e9b554c).

---

### `SetDecodedData()`

```cpp
status_t BMailComponent::SetDecodedData(BPositionIO * data)
```

Sets the content of this component to the canonical format data contained in data. 


Thus, an attachment subclass would accept a file here and encode it into the specified encoding. [BMailComponent](classBMailComponent.md) implements this function to do nothing and return `B_OK`.



**Since:** Haiku R1


Reimplemented in [BSimpleMailAttachment](classBSimpleMailAttachment.md#a24c937455f8c43081f987dd16f93ecab), [BAttributedMailAttachment](classBAttributedMailAttachment.md#ac687282eb7e6ecfb5522122401b4a3c9), and [BTextMailComponent](classBTextMailComponent.md#a5bf619e5270526a2a622422d1a627115).

---

### `SetHeaderField()`

```cpp
void BMailComponent::SetHeaderField(const char * key, BMessage * structured_header, bool replace_existing = true)
```

Adds a structured header of type *key* to the component. 


Structured headers are in the format unlabeled; key=value; key=value. The most common instance of this is the Content-Type header, where the MIME type is unlabeled, and various other information, such as character set, is specified in the key/value pairs. The format for structured_header is relatively simple: simply use BMessage::AddString(key,value) for each key/value pair. The only exception to this rule is the unlabeled data. For this, simply use the key unlabeled. Please note that the charset and encoding arguments defined for the text version of SetHeaderField is not provided here because structured headers cannot be encoded.


Thus, a relatively standard Content-Type header would be specified as follows:



```cpp
BMessage structured;
structured.AddString("unlabeled","text/plain");
structured.AddString("charset","iso-8859-1");
component->SetHeaderField("To",&structured);
```


**Since:** Haiku R1

---

### `SetHeaderField()`

```cpp
void BMailComponent::SetHeaderField(const char * key, const char * value, uint32 charset = B_MAIL_NULL_CONVERSION, mail_encoding encoding = null_encoding, bool replace_existing = true)
```

Adds the specified header of type *key* and with the *value* to the component. 


Converts any 8 bit-data in *value* to *charset* and encodes it into 7-bit data using *encoding*. If *replace_existing* is true, replaces any existing header of this type with this one, otherwise adds a second one.


Thus, to set the header To: of some [BMailComponent](classBMailComponent.md) *component* to [foo@e.nosp@m.xamp.nosp@m.le.co.nosp@m.m](#), we would do this:



```cpp
component->SetHeaderField("To","foo@example.com");
```

If you want to delete a header, pass in a zero length or NULL string for the value field, or use [BMailComponent::RemoveHeader](classBMailComponent.md#a58bbcaedf4bb7d71e765835f4f4b92f5).



**Since:** Haiku R1

---

### `SetToRFC822()`

```cpp
status_t BMailComponent::SetToRFC822(BPositionIO * data, size_t length, bool parse_now = false)
```

Sets this object from a component in RFC-822 format. 



**Since:** Haiku R1


Reimplemented in [BSimpleMailAttachment](classBSimpleMailAttachment.md#a7a6ba96c4c777f33ac6944e7f6fc3508), [BAttributedMailAttachment](classBAttributedMailAttachment.md#a9aad3eb693e7cbae8212a4bb90eb2423), and [BTextMailComponent](classBTextMailComponent.md#a1833a51f2062dc6acf41c7927f786d39).

---

### `WhatIsThis()`

```cpp
BMailComponent * BMailComponent::WhatIsThis()
```

Employs simple heuristics such as the MIME type to present you with an instance of a useful subclass. 


You can then use any of [BMailComponent](classBMailComponent.md)'s hook functions or RTTI calls to get more information. Bear in mind that the returned component is not set to any data. You must still Instantiate() it from whatever data this object was instantiated from.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMailComponent.html).
