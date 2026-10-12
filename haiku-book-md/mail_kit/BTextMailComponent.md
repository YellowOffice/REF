---
name: BTextMailComponent
type: class
kit: mail_kit
brief: "A component that stores plain text"
source: haiku-book
---

# BTextMailComponent Class
**Kit/Group:** [Mail Kit](../mail_kit/group__mail.md) | [Mail Kit library (libmail.so)](group__libmail.md)

## Description

A component that stores plain text. 


It uses UTF8 text as its canonical format and reads and writes [RFC-2047](https://www.ietf.org/rfc/rfc2047.txt) style text. As such, it handles accents and other 8 bit characters with ease. If you want to send text, this is the way to go.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BTextMailComponent](#a8c7e9bd07148239b5ca0983a813e0a56) (const char *text=NULL, uint32 defaultCharSet=B_MAIL_NULL_CONVERSION) — Initializes the component and sets its content to text.
* `virtual` ~BTextMailComponent () — Destructor.
* `void` [AppendText](#af1fcacbff91a2827e3a5eceda0781729) (const char *text) — Appends the UTF8 string text to the current contents of this component.
* `BString *` [BStringText](#a0ea6307ce7d0de47c5d2c4c6c5c1f8a0) () — Returns the internal UTF8 format BString used by this component.
* `virtual status_t` [GetDecodedData](#aa09e051b9ccb894e537277ed33b60dfc) (BPositionIO *data) — Retrieves the data contained in this component as a UTF8 string into data.
* `void` [Quote](#a1ee6268d87e5282176b495f352c7e56d) (const char *message=NULL, const char *quote_style="> ") — Quotes the contents of this component.
* `virtual status_t` [RenderToRFC822](#a141a7071157c94d9c3569ef14e9b554c) (BPositionIO *render_to) — Renders the component into RFC-822 format.
* `virtual status_t` [SetDecodedData](#a5bf619e5270526a2a622422d1a627115) (BPositionIO *data) — Sets the contents of this component to the UTF8 format data.
* `void` [SetEncoding](#a285a450dedc975fac8a97c1a6176d8d4) (mail_encoding encoding, int32 charset) — Sets the encoding and charset used by Render().
* `void` [SetText](#a6dac24681b519c152ab2a1b4956e58bc) (const char *text) — Sets the contents of this component to the UTF8 string text.
* `virtual status_t` [SetToRFC822](#a1833a51f2062dc6acf41c7927f786d39) (BPositionIO *data, size_t length, bool parse_now=false) — Sets this object from a component in RFC-822 format.
* `const char *` [Text](#a2ab6f3f39c0789d958ed82ff44bc9d34) () — Returns the contents of this component as a UTF8 string.
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

### `BTextMailComponent()`

```cpp
BTextMailComponent::BTextMailComponent(const char * text = NULL, uint32 defaultCharSet = B_MAIL_NULL_CONVERSION)
```

Initializes the component and sets its content to *text*. 


*text* can be `NULL`. The argument is a UTF-8 null-terminated string. Encoding defaults to quoted_printable with the ISO-15 charset.



**Since:** Haiku R1

---

### `AppendText()`

```cpp
void BTextMailComponent::AppendText(const char * text)
```

Appends the UTF8 string *text* to the current contents of this component. 



**Since:** Haiku R1

---

### `BStringText()`

```cpp
BString * BTextMailComponent::BStringText()
```

Returns the internal UTF8 format [BString](../support_kit/classBString.md) used by this component. 


As such, you can do raw text operations on the content of the message. The use of this function is not reccomended.



**Since:** Haiku R1

---

### `GetDecodedData()`

```cpp
status_t BTextMailComponent::GetDecodedData(BPositionIO * data)
```

Retrieves the data contained in this component as a UTF8 string into *data*. 



**Since:** Haiku R1


Reimplemented from [BMailComponent](classBMailComponent.md#a46e65753239d6efe7856aafe02a7cc27).

---

### `Quote()`

```cpp
void BTextMailComponent::Quote(const char * message = NULL, const char * quote_style = "> ")
```

Quotes the contents of this component. 


Inserts *quote_style* at the start of every line, and prefaces the content with *message*, if it is not `NULL`. *message* should be something like `"On September 30, 2001, John Smith said:"`, or something in that vein. Note that the new line after *message* is supplied for you, so you do not need to add it.



**Since:** Haiku R1

---

### `RenderToRFC822()`

```cpp
status_t BTextMailComponent::RenderToRFC822(BPositionIO * render_to)
```

Renders the component into RFC-822 format. 


It places the result in data, starting at data->Position(). Encodes and translates charsets according to the arguments passed to [SetEncoding()](classBTextMailComponent.md#a285a450dedc975fac8a97c1a6176d8d4), or the defaults set in [BTextMailComponent::BTextMailComponent()](classBTextMailComponent.md#a8c7e9bd07148239b5ca0983a813e0a56) otherwise.



**Since:** Haiku R1


Reimplemented from [BMailComponent](classBMailComponent.md#a1b38a761364e8cc7bcab62f921db1ee3).

---

### `SetDecodedData()`

```cpp
status_t BTextMailComponent::SetDecodedData(BPositionIO * data)
```

Sets the contents of this component to the UTF8 format *data*. 



**Since:** Haiku R1


Reimplemented from [BMailComponent](classBMailComponent.md#aba4b4e0d158e5c6c66cfd37b2fc38dd4).

---

### `SetEncoding()`

```cpp
void BTextMailComponent::SetEncoding(mail_encoding encoding, int32 charset)
```

Sets the *encoding* and *charset* used by Render(). 


Use the conversion constants from UTF8.h for *charset*. We strongly reccomend that you always use the defaults (and strongly recommend against using base64) for the reasons outlined in RFC 2047.



**Since:** Haiku R1

---

### `SetText()`

```cpp
void BTextMailComponent::SetText(const char * text)
```

Sets the contents of this component to the UTF8 string *text*. 



**Since:** Haiku R1

---

### `SetToRFC822()`

```cpp
status_t BTextMailComponent::SetToRFC822(BPositionIO * data, size_t length, bool parse_now = false)
```

Sets this object from a component in RFC-822 format. 


Initializes this component to the RFC 822 format data in *data*, starting at `data->Position()`, for up to *length* bytes. Handles encoded data according to RFC 2047.


If *parse_now* is `false`, then the *data* will not be parsed until RenderToRFC822 is called.



**Since:** Haiku R1


Reimplemented from [BMailComponent](classBMailComponent.md#a95a1764eb1e70b410be3bf7e3137d855).

---

### `Text()`

```cpp
const char * BTextMailComponent::Text()
```

Returns the contents of this component as a UTF8 string. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBTextMailComponent.html).
