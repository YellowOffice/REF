---
name: BMimeType
type: class
kit: storage_kit
brief: "A class that represents a MIME (Multi-purpose Internet Mail Extensions) type string"
source: haiku-book
---

# BMimeType Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A class that represents a MIME (Multi-purpose Internet Mail Extensions) type string. 


MIME types use, has grown beyond describing the content of email to describe the content types of applications and file formats.


MIME types consist of a supertype and a subtype.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BMimeType](#a1fdf3459c8af726c9846770d7aea5e09) () — Creates an uninitialized BMimeType object.
* [BMimeType](#a9a0f254e32643872f7c2379bb20b634a) (const char *mimeType) — Creates a BMimeType object and initializes it to the supplied MIME type.
* `virtual` [~BMimeType](#a6a3cc1a25aa82d1bad7e10b25f169991) () — Frees all resources associated with this object.
* `bool` [Contains](#a1f5de6e7f1349432a061664e4764a101) (const BMimeType *type) const — Returns whether this MIME type is a supertype of or equals the supplied one.
* `status_t` [Delete](#a928153d3227956971ee5e0d7ad23bbfd) () — Removes the MIME type from the MIME database.
* `status_t` [GetAppHint](#ab2768b8a9e6254791cd6628a58675115) (entry_ref *ref) const — Fetches an entry_ref that serves as a hint as to where the MIME type's preferred application might live.
* `status_t` [GetAttrInfo](#a9018ca198dd5ca710326f6601fc58fb4) (BMessage *info) const — Fetches from the MIME database a BMessage describing the attributes typically associated with files of the given MIME type.
* `status_t` [GetFileExtensions](#a353aea2c7e048f66912b67e1c29a852d) (BMessage *extensions) const — Fetches the MIME type's associated filename extensions from the MIME database.
* `status_t` [GetIcon](#af549bda9abf4470f838333a4c99d541c) (BBitmap *icon, icon_size size) const — Fetches the large or mini icon associated with the MIME type.
* `status_t` [GetIcon](#a3e787905dd154ab589f80f805ed01ef1) (uint8 **_data, size_t *_size) const — Fetches the vector icon associated with the MIME type The icon data is returned in data.
* `status_t` [GetIconForType](#ad1f67fec0e6ca8c244c10c0ab41e9d34) (const char *type, BBitmap *icon, icon_size which) const — Fetches the large or mini icon used by an application of this type for files of the given type.
* `status_t` [GetIconForType](#aa10038e1db9d8669320c2d8690db8cad) (const char *type, uint8 **_data, size_t *_size) const — Fetches the vector icon used by an application of this type for files of the given type.
* `status_t` [GetLongDescription](#a8f0f647361c5f2873e8d4b474a96cf62) (char *description) const — Fetches the MIME type's long description from the MIME database.
* `status_t` [GetPreferredApp](#ac2b36e26d733f92749823a78c800a416) (char *signature, app_verb verb=B_OPEN) const — Fetches the signature of the preferred application from the MIME database.
* `status_t` [GetShortDescription](#a35f404ae1c8942d91ef901c81f5d3392) (char *description) const — Fetches the MIME type's short description from the MIME database.
* `status_t` [GetSnifferRule](#ad6294a567022c4fb4b22f797d3fae6aa) (BString *result) const — Retrieves the MIME type's sniffer rule.
* `status_t` [GetSupertype](#aae9ee70db2704a737a05ff073d97a850) (BMimeType *supertype) const — Gets the supertype of the MIME type represented by this object.
* `status_t` [GetSupportingApps](#a32e1d909b97c84d943ac50467e56fc3d) (BMessage *signatures) const — Fetches a BMessage containing a list of MIME signatures of applications that are able to handle files of this MIME type.
* `status_t` [InitCheck](#a5a1c59c7ad858324d50a3f419bc285d5) () const — Returns the result of the most recent constructor or SetTo() call.
* `status_t` [Install](#a79f20914ab176d2b7a6b3e41a3387dc4) () — Adds the MIME type to the MIME database.
* `bool` [IsInstalled](#aa6988f049900d2c19c333da3a9fb0428) () const — Returns whether or not this type is currently installed in the MIME database.
* `bool` [IsSupertypeOnly](#aa952ebae10a18465f89bdf22a6b32762) () const — Returns whether this objects represents a supertype.
* `bool` [IsValid](#a12c9b6d8c40c1f505d0d7c04a299914b) () const — Returns whether the object represents a valid MIME type.
* `bool` [operator==](#a670f3b9ab71f46c85315c83fe3e2aa78) (const BMimeType &type) const — Returns whether this and the supplied MIME type are equal.
* `bool` [operator==](#a303623e252ecf9932ae2c735d6774add) (const char *type) const — Returns whether this and the supplied MIME type are equal.
* `status_t` [SetAppHint](#a3308b9ea259de72cc79d5a3a84c9aa13) (const entry_ref *ref) — Sets the app hint field for the MIME type.
* `status_t` [SetAttrInfo](#ac95cc9cea6b036d9b7baec668cf32822) (const BMessage *info) — Sets the description of the attributes typically associated with files of the given MIME type.
* `status_t` [SetFileExtensions](#a0a4dc7205fa52a36a84b9c0b6ed1d904) (const BMessage *extensions) — Sets the list of filename extensions associated with the MIME type.
* `status_t` [SetIcon](#a44b252859ffae8b70bf9c8e70b0d9d48) (const BBitmap *icon, icon_size size) — Sets the large or mini icon for the MIME type.
* `status_t` [SetIcon](#a9f75552ced0097078921f6be0730787d) (const uint8 *data, size_t size) — Sets the vector icon for the MIME type.
* `status_t` [SetIconForType](#af4f299f8d833c42c693e5650c18c46b8) (const char *type, const BBitmap *icon, icon_size which) — Sets the large or mini icon used by an application of this type for files of the given type.
* `status_t` [SetIconForType](#a7101fe71a0c72127edd4b80ccce9f4c4) (const char *type, const uint8 *data, size_t size) — Sets the icon used by an application of this type for files of the given type.
* `status_t` [SetLongDescription](#ad976818e62d2f12542f05fc6ca49b49d) (const char *description) — Sets the long description field for the MIME type.
* `status_t` [SetPreferredApp](#aa4ec5c9f0e4bd29872bd525b7ce5dbd0) (const char *signature, app_verb verb=B_OPEN) — Sets the preferred application for the MIME type.
* `status_t` [SetShortDescription](#a5d46d51dd1665d49f2c91e46721c6bb4) (const char *description) — Sets the short description field for the MIME type.
* `status_t` [SetSnifferRule](#ab9da3155010b5f6d1a0868ca202b1ab9) (const char *) — Sets the MIME type's sniffer rule.
* `status_t` [SetTo](#ab4eb64b2e47f111b796e641ffa624046) (const char *mimeType) — Initializes this object to the supplied MIME type.
* `status_t` [SetType](#a17ac52bb752f00d9fb190d06f44d1145) (const char *mimeType) _DEPRECATED — Initializes this object to the supplied MIME type.
* `const char *` [Type](#a9b1e232d61a088a8197fdee7db580071) () const — Returns the MIME string represented by this object.
* `void` [Unset](#a24cc52aecc8310fdc109b7afa827040b) () — Returns the object to an uninitialized state.

### Static Public Member Functions

* `static status_t` [CheckSnifferRule](#a7e1d370ef1e52b167ac7cee93ca1410e) (const char *rule, BString *parseError) — Checks whether a MIME sniffer rule is valid or not.
* `static status_t` [GetInstalledSupertypes](#a3e829715b115ef4c9ffdcd244655f637) (BMessage *supertypes) — Fetches a BMessage listing all the MIME supertypes currently installed in the MIME database.
* `static status_t` [GetInstalledTypes](#ab7c36a18387907085d2135960af41551) (BMessage *types) — Fetches a BMessage listing all the MIME types currently installed in the MIME database.
* `static status_t` [GetInstalledTypes](#a6d6c8d8478e87d16965e52c5776f13ca) (const char *supertype, BMessage *subtypes) — Fetches a BMessage listing all the MIME subtypes of the given supertype currently installed in the MIME database.
* `static status_t` [GetWildcardApps](#a21419efb577f0a7bdae84c1b700bf12f) (BMessage *wildcardApps) — Fetches a BMessage containing a list of MIME signatures of applications that are able to handle files of any type.
* `static status_t` [GuessMimeType](#a9c7f383db42b7418577986aaca98490d) (const char *filename, BMimeType *type) — Guesses a MIME type for the given filename.
* `static status_t` [GuessMimeType](#a014ae51a0763796a1c9ed57c942fd46e) (const entry_ref *file, BMimeType *type) — Guesses a MIME type for the entry referred to by the given entry_ref.
* `static status_t` [GuessMimeType](#aac732b4c4943f51fb682e6edeea3c9ca) (const void *buffer, int32 length, BMimeType *type) — Guesses a MIME type for the supplied chunk of data.
* `static bool` [IsValid](#abd581b5da6138967bbf028371e03181d) (const char *mimeType) — Returns whether the given string represents a valid MIME type.
* `static status_t` [StartWatching](#a503a2f6daed253b2bb5f7a9469e9c2f7) (BMessenger target) — Starts monitoring the MIME database for a given target.
* `static status_t` [StopWatching](#a3d48acac5d9fb081c55729c2b7045a6f) (BMessenger target) — Stops monitoring the MIME database for a given target (previously started via StartWatching()).

## Detailed Member Documentation

### `BMimeType()`

```cpp
BMimeType::BMimeType()
```

Creates an uninitialized [BMimeType](classBMimeType.md) object. 



**Since:** BeOS R3

---

### `BMimeType()`

```cpp
BMimeType::BMimeType(const char * mimeType)
```

Creates a [BMimeType](classBMimeType.md) object and initializes it to the supplied MIME type. 


The supplied string must specify a valid MIME type or supertype.


Parameters

| Parameter | Description |
| :--- | :--- |
| `mimeType` | The MIME string. |





**See also:** [SetTo()](classBMimeType.md#ab4eb64b2e47f111b796e641ffa624046) for further information.



**Since:** BeOS R3

---

### `~BMimeType()`

```cpp
BMimeType::~BMimeType()
```

Frees all resources associated with this object. 



**Since:** BeOS R3

---

### `CheckSnifferRule()`

```cpp
status_t BMimeType::CheckSnifferRule(const char * rule, BString * parseError)
```

Checks whether a MIME sniffer rule is valid or not. 


A MIME sniffer rule is valid, if it is well-formed with respect to the following grammar and fulfills some further conditions listed thereafter:


	Rule			::= LWS Priority LWS ExprList LWS
	ExprList		::= Expression (LWS Expression)*
	Expression		::= "(" LWS (PatternList | RPatternList) LWS ")"
						| Range LWS "(" LWS PatternList LWS ")"
	RPatternList	::= RPattern (LWS "|" LWS RPattern)*
	PatternList		::= Pattern (LWS "|" LWS Pattern)*
	RPattern		::= Range LWS Pattern
	Pattern			::= PString [ LWS "&" LWS Mask ]
	Range			::=	"[" LWS SDecimal [LWS ":" LWS SDecimal] LWS "]"

	Priority		::= Float
	Mask			::= PString
	PString			::= HexString | QuotedString | Octal [UnquotedString]
						EscapedChar [UnquotedString]
	HexString		::= "0x" HexPair HexPair*
	HexPair			::= HexChar HexChar
	QuotedString	::= '"' QChar QChar* '"' | "'" QChar QChar* "'"
	Octal			::= "\" OctChar [OctChar [OctChar]]
	SDecimal		::= ["+" | "-"] Decimal
	Decimal			::= DecChar DecChar*
	Float			::= Fixed [("E" | "e") Decimal]
	Fixed			::= SDecimal ["." [Decimal]] | [SDecimal] "." Decimal
	UnquotedString	::= UChar UChar*
	LWS				::= LWSChar*

	LWSChar			::= LF | " " | TAB
	OctChar			::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7"
	DecChar			::= OctChar | "8" | "9"
	HexChar			::= DecChar | "a" | "b" | "c" | "d" | "e" | "A" | "B" | "C"
						| "D" | "E"
	Char			:: <any character>
	QChar			::= <Char except "\", "&", "'" and '"'> | EscapedChar
	EscapedChar		::= "\" Char
	UChar			::= <QChar except LWSChar>

	Conditions:
	(checked)
	- If a mask is specified for a pattern, this mask must have the same
	  length as the pattern string.
	(not checked)
	- 0 <= Priority <= 1
	- 0 <= Range begin <= Range end
	- Rules of the form "() | () | ..." are invalid.

	Examples:
	- 1.0 ('ABCD')
	  The file must start with the string "ABCD". The priority of the rule
	  is 1.0 (maximal).
	- 0.8 [0:3] ('ABCD' | 'abcd')
	  The file must contain the string "ABCD" or "abcd" starting somewhere in
	  the first four bytes. The rule priority is 0.8.
	- 0.5 ([0:3] 'ABCD' | [0:3] 'abcd' | [13] 'EFGH')
	  The file must contain the string "ABCD" or "abcd" starting somewhere in
	  the first four bytes or the string "EFGH" at position 13. The rule
	  priority is 0.5.
	- 0.8 [0:3] ('ABCD' & 0xff00ffff | 'abcd' & 0xffff00ff)
	  The file must contain the string "A.CD" or "ab.d" (whereas "." is an
	  arbitrary character) starting somewhere in the first four bytes. The
	  rule priority is 0.8.

	Real examples:
	- 0.20 ([0]"//" | [0]"/\*" | [0:32]"#include" | [0:32]"#ifndef"
	        | [0:32]"#ifdef")
	  text/x-source-code
	- 0.70 ("8BPS  \000\000\000\000" & 0xffffffff0000ffffffff )
	  image/x-photoshop
Parameters

| Parameter | Description |
| :--- | :--- |
| `rule` | The rule string. |
| `parseError` | A pointer to a pre-allocated [BString](../support_kit/classBString.md) into which a description of the parse error is written (if any), may be `NULL`. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The supplied sniffer rule is valid. |
| B_BAD_VALUE | `NULL` *rule*. |
| B_BAD_MIME_SNIFFER_RULE | The supplied sniffer rule is not valid. A description of the error is written to *parseError*, if supplied. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |





**Since:** Haiku R1

---

### `Contains()`

```cpp
bool BMimeType::Contains(const BMimeType * type)const
```

Returns whether this MIME type is a supertype of or equals the supplied one. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The MIME type. |





**Returns:** `true`, if this MIME type is a supertype of or equals the supplied one, `false` otherwise.



**Since:** BeOS R3

---

### `Delete()`

```cpp
status_t BMimeType::Delete()
```

Removes the MIME type from the MIME database. 


To check if the MIME type is already installed, call `IsInstalled()`. To add the MIME type to the database, call `Install()`.



> [!NOTE]
> Calling `BMimeType::Delete()` does not uninitialize or otherwise deallocate the `BMimeType` object; it simply removes the type from the database.



**Returns:** `B_OK` on success or another error code on failure.



**Since:** BeOS R3

---

### `GetAppHint()`

```cpp
status_t BMimeType::GetAppHint(entry_ref * ref)const
```

Fetches an `entry_ref` that serves as a hint as to where the MIME type's preferred application might live. 


The app hint is a path that identifies the executable that should be used when launching an application that has this signature. For example, when Tracker needs to launch an app of type `"application/YourAppHere"`, it asks the database for the application hint. This hint is converted to an `entry_ref` before it is passed to the caller. Of course, the path may not point to an application, or it might point to an application with the wrong signature (and so on); that's why this is merely a hint.


The `entry_ref` pointed to by `ref` must be pre-allocated.


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | Pointer to a pre-allocated `entry_ref` into which the location of the app hint is copied. If the function fails, the contents of the `entry_ref` are undefined. |





**Returns:** A status code, B_OK on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The ref was retrieved successfully. |
| B_ENTRY_NOT_FOUND | No app hint existed for the given *ref*. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |





**Since:** BeOS R3

---

### `GetAttrInfo()`

```cpp
status_t BMimeType::GetAttrInfo(BMessage * info)const
```

Fetches from the MIME database a [BMessage](../application_kit/classBMessage.md) describing the attributes typically associated with files of the given MIME type. 


The attribute information is returned in a pre-allocated [BMessage](../application_kit/classBMessage.md) pointed to by the `info` parameter (note that the any prior contents of the message will be destroyed). If the method succeeds, the format of the [BMessage](../application_kit/classBMessage.md) pointed to by `info` will be the following:



| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| **field name** | **type** | **element[0..n]** |
| "attr:name" | `B_STRING_TYPE` | The name of each attribute |
| "attr:public_name" | `B_STRING_TYPE` | The human-readable name of each attribute |
| "attr:type" | `B_INT32_TYPE` | The type code for each attribute |
| "attr:viewable" | `B_BOOL_TYPE` | For each attribute: `true` if the attribute is public, `false` if it's private |
| "attr:editable" | `B_BOOL_TYPE` | For each attribute: `true` if the attribute should be user editable, `false` if not |


The `BMessage::what` value is set to decimal `233`, but is otherwise meaningless.


Parameters

| Parameter | Description |
| :--- | :--- |
| `info` | Pointer to a pre-allocated [BMessage](../application_kit/classBMessage.md) into which information about the MIME type's associated file attributes is stored. |





**Returns:** `B_OK` on success or another error code on failure.



**See also:** [SetAttrInfo()](classBMimeType.md#ac95cc9cea6b036d9b7baec668cf32822)



**Since:** BeOS R3

---

### `GetFileExtensions()`

```cpp
status_t BMimeType::GetFileExtensions(BMessage * extensions)const
```

Fetches the MIME type's associated filename extensions from the MIME database. 


The MIME database associates a list of filename extensions (a character string following the rightmost dot, `"."`, character in the filename) with each type. These extensions can then be used to help determine the type of any untyped files that may be encountered.


The list of extensions is returned in a pre-allocated [BMessage](../application_kit/classBMessage.md) pointed to by the `extensions` parameter (note that the any prior contents of the message will be destroyed). If the method succeeds, the format of the [BMessage](../application_kit/classBMessage.md) pointed to by `extensions` will be the following:



* The message's `"extensions"` field will contain an indexed array of strings, one for each extension. The extensions are given without the preceding `"."` character by convention.

* The message's `"type"` field will be a string containing the MIME type whose associated file extensions you are fetching.

* The `what` member of the [BMessage](../application_kit/classBMessage.md) will be set to `234`, but is otherwise irrelevant.



Note that any other fields present in the [BMessage](../application_kit/classBMessage.md) passed to the most recent `SetFileExtensions()` call will also be returned.


Parameters

| Parameter | Description |
| :--- | :--- |
| `extensions` | Pointer to a pre-allocated [BMessage](../application_kit/classBMessage.md) into which the MIME type's associated file extensions will be stored. |





**Returns:** `B_OK` on success or another error code on failure.



**See also:** [SetFileExtensions()](classBMimeType.md#a0a4dc7205fa52a36a84b9c0b6ed1d904)



**Since:** BeOS R3

---

### `GetIcon()`

```cpp
status_t BMimeType::GetIcon(BBitmap * icon, icon_size size)const
```

Fetches the large or mini icon associated with the MIME type. 


The icon is copied into the `BBitmap` pointed to by `icon`. The bitmap must be the proper size: `32x32` for the large icon, `16x16` for the mini icon. Additionally, the bitmap must be in the `B_CMAP8` color space (8-bit color).


Parameters

| Parameter | Description |
| :--- | :--- |
| `icon` | Pointer to a pre-allocated `BBitmap` of proper size and colorspace into which the icon is copied. |
| `size` | Value that specifies which icon to return. Currently `B_LARGE_ICON` and `B_MINI_ICON` are supported. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ENTRY_NOT_FOUND | No icon of the given size exists for the given type. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |





**Since:** BeOS R3

---

### `GetIcon()`

```cpp
status_t BMimeType::GetIcon(uint8 ** data, size_t * size)const
```

Fetches the vector icon associated with the MIME type The icon data is returned in `data`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | Pointer in which the allocated icon data is returned. You need to delete the buffer when you are done with it. |
| `size` | Pointer in which the size of the allocated icon data is returned. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ENTRY_NOT_FOUND | No icon of the given size found for the given type. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |





**Since:** BeOS R3

---

### `GetIconForType()`

```cpp
status_t BMimeType::GetIconForType(const char * type, BBitmap * icon, icon_size which)const
```

Fetches the large or mini icon used by an application of this type for files of the given type. 


This can be confusing, so here's how this function is intended to be used:


* The actual `BMimeType` object should be set to the MIME signature of an application for whom you want to look up custom icons for custom MIME types.

* The `type` parameter specifies the file type whose custom icon you are fetching.



The type of the `BMimeType` object is not required to actually be a subtype of `"application/"`; that is the intended use however, and calling `GetIconForType()` on a non-application type will likely return `B_ENTRY_NOT_FOUND`.


The icon is copied into the `BBitmap` pointed to by `icon`. The bitmap must be the proper size: `32x32` for the large icon, `16x16` for the mini icon. Additionally, the bitmap must be in the `B_CMAP8` color space (8-bit color).


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | Pointer to a pre-allocated string containing the MIME type whose custom icon you wish to fetch. |
| `icon` | Pointer to a pre-allocated `BBitmap` of proper size and colorspace into which the icon is copied. |
| `which` | Value that specifies which icon to return. Currently `B_LARGE_ICON` and `B_MINI_ICON` are supported. |





**Returns:** A status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Success |
| B_ENTRY_NOT_FOUND | No icon of the given size exists for the given type. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |





**Since:** BeOS R3

---

### `GetIconForType()`

```cpp
status_t BMimeType::GetIconForType(const char * type, uint8 ** _data, size_t * _size)const
```

Fetches the vector icon used by an application of this type for files of the given type. 


The icon data is returned in `data`. See the other [GetIconForType()](classBMimeType.md#ad1f67fec0e6ca8c244c10c0ab41e9d34) for more information.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | Pointer to a pre-allocated string containing the MIME type whose custom icon you wish to fetch. |
| `_data` | Pointer in which the allocated icon data is returned. You need to delete the buffer when you are done with it. |
| `_size` | Pointer in which the size of the allocated icon data is filled out. |





**Returns:** A status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Success. |
| B_ENTRY_NOT_FOUND | No icon of the given size exists for the given type. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |





**Since:** Haiku R1

---

### `GetInstalledSupertypes()`

```cpp
status_t BMimeType::GetInstalledSupertypes(BMessage * supertypes)
```

Fetches a [BMessage](../application_kit/classBMessage.md) listing all the MIME *supertypes* currently installed in the MIME database. 


The types are copied into the `"super_types"` field of the passed-in `BMessage`. The `BMessage` must be pre-allocated.


Parameters

| Parameter | Description |
| :--- | :--- |
| `supertypes` | Pointer to a pre-allocated `BMessage` into which the MIME *supertypes* will be copied. |





**Returns:** `B_OK` on success or another error code on failure.



**Since:** BeOS R3

---

### `GetInstalledTypes()`

```cpp
status_t BMimeType::GetInstalledTypes(BMessage * types)
```

Fetches a [BMessage](../application_kit/classBMessage.md) listing all the MIME types currently installed in the MIME database. 


The types are copied into the `"types"` field of the passed-in `BMessage`. The `BMessage` must be pre-allocated.


Parameters

| Parameter | Description |
| :--- | :--- |
| `types` | Pointer to a pre-allocated `BMessage` into which the MIME types will be copied. |





**Returns:** `B_OK` on success or another error code on failure.



**Since:** BeOS R3

---

### `GetInstalledTypes()`

```cpp
status_t BMimeType::GetInstalledTypes(const char * supertype, BMessage * types)
```

Fetches a [BMessage](../application_kit/classBMessage.md) listing all the MIME subtypes of the given *supertype* currently installed in the MIME database. 


The types are copied into the `"types"` field of the passed-in `BMessage`. The `BMessage` must be pre-allocated.


Parameters

| Parameter | Description |
| :--- | :--- |
| `supertype` | Pointer to a string containing the MIME *supertype* whose subtypes you wish to retrieve. |
| `types` | Pointer to a pre-allocated `BMessage` into which the appropriate MIME subtypes will be copied. |





**Returns:** `B_OK` on success or another error code on failure.



**Since:** BeOS R3

---

### `GetLongDescription()`

```cpp
status_t BMimeType::GetLongDescription(char * description)const
```

Fetches the MIME type's long description from the MIME database. 


The string pointed to by `description` must be long enough to hold the long description; a length of `B_MIME_TYPE_LENGTH` is recommended.


Parameters

| Parameter | Description |
| :--- | :--- |
| `description` | Pointer to a pre-allocated string into which the long description is copied. If the function fails, the contents of the string are undefined. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Success |
| B_ENTRY_NOT_FOUND | No long description exists for the given type. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |





**See also:** [SetLongDescription()](classBMimeType.md#ad976818e62d2f12542f05fc6ca49b49d)



**Since:** BeOS R3

---

### `GetPreferredApp()`

```cpp
status_t BMimeType::GetPreferredApp(char * signature, app_verb verb = B_OPEN)const
```

Fetches the signature of the preferred application from the MIME database. 


The preferred app is the application that's used to access a file when, for example, the user double-clicks the file in a Tracker window. Unless the file identifies in its attributes a "custom" preferred app, Tracker will ask the file type database for the preferred app that's associated with the file's type.


The string pointed to by `signature` must be long enough to hold the preferred applications signature; a length of `B_MIME_TYPE_LENGTH` is recommended.


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | Pointer to a pre-allocated string into which the signature of the preferred app is copied. If the function fails, the contents of the string are undefined. |
| `verb` | `app_verb` value that specifies the type of access for which you are requesting the preferred app. Currently, the only supported app verb is `B_OPEN`. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Success |
| B_ENTRY_NOT_FOUND | No preferred app exists for the given type and app_verb. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |





**See also:** [SetPreferredApp()](classBMimeType.md#aa4ec5c9f0e4bd29872bd525b7ce5dbd0)



**Since:** BeOS R3

---

### `GetShortDescription()`

```cpp
status_t BMimeType::GetShortDescription(char * description)const
```

Fetches the MIME type's short description from the MIME database. 


The string pointed to by `description` must be long enough to hold the short description; a length of `B_MIME_TYPE_LENGTH` is recommended.


Parameters

| Parameter | Description |
| :--- | :--- |
| `description` | Pointer to a pre-allocated string into which the long description is copied. If the function fails, the contents of the string are undefined. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Success |
| B_ENTRY_NOT_FOUND | No short description exists for the given type. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |





**See also:** [SetShortDescription()](classBMimeType.md#a5d46d51dd1665d49f2c91e46721c6bb4)



**Since:** BeOS R3

---

### `GetSnifferRule()`

```cpp
status_t BMimeType::GetSnifferRule(BString * result)const
```

Retrieves the MIME type's sniffer rule. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `result` | Pointer to a pre-allocated [BString](../support_kit/classBString.md) into which the value is copied. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *result* or uninitialized [BMimeType](classBMimeType.md). |
| B_ENTRY_NOT_FOUND | The MIME type is not installed. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |





**See also:** [SetSnifferRule()](classBMimeType.md#ab9da3155010b5f6d1a0868ca202b1ab9)



**Since:** Haiku R1

---

### `GetSupertype()`

```cpp
status_t BMimeType::GetSupertype(BMimeType * supertype)const
```

Gets the *supertype* of the MIME type represented by this object. 


The supplied object is initialized to this object's *supertype*. If this [BMimeType](classBMimeType.md) is not properly initialized, the supplied object will be [Unset()](classBMimeType.md#a24cc52aecc8310fdc109b7afa827040b).


Parameters

| Parameter | Description |
| :--- | :--- |
| `supertype` | A pointer to the [BMimeType](classBMimeType.md) object that shall be initialized to this object's *supertype*. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *superType*, this object is not initialized, or this object is a supertype only. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |





**Since:** BeOS R3

---

### `GetSupportingApps()`

```cpp
status_t BMimeType::GetSupportingApps(BMessage * signatures)const
```

Fetches a `BMessage` containing a list of MIME signatures of applications that are able to handle files of this MIME type. 


If successful, the [BMessage](../application_kit/classBMessage.md) containing the MIME signatures will be of the following format:



| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| **field name** | **type** | **contains** |
| "applications" | `B_STRING_TYPE`[] | An array of MIME signatures. The first * n * signatures (where * n * is the value in the `"be:sub"` field of the message) are able to handle the full type (supertype * and * subtype). The remaining signatures are of applications that handle the supertype only. |
| "be:sub" | `B_INT32_TYPE` | The number of applications in the `"applications"` array that can handle the object's full MIME type. These applications are listed first in the array. This field is omitted if the object represents a supertype only. |
| "be:super" | `B_INT32_TYPE` | The number of applications in the "applications" array that can handle the object's supertype (not counting those that can handle the full type). These applications are listed after the full-MIME-type supporters. By definition, the `GetWildcardApps()` function never returns supertype-only apps. |


The `BMessage::what` value is meaningless and should be ignored.


Parameters

| Parameter | Description |
| :--- | :--- |
| `signatures` | Pointer to a pre-allocated [BMessage](../application_kit/classBMessage.md) into which the signatures of the supporting applications will be copied. |





**Returns:** `B_OK` on success or an error code on failure.



**See also:** SetSupportingApps()



**Since:** BeOS R3

---

### `GetWildcardApps()`

```cpp
status_t BMimeType::GetWildcardApps(BMessage * wild_ones)
```

Fetches a `BMessage` containing a list of MIME signatures of applications that are able to handle files of any type. 


This function is the same as calling `GetSupportingApps()` on a `BMimeType` object initialized to a MIME type of] `"application/octet-stream"`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `wild_ones` | Pointer to a pre-allocated [BMessage](../application_kit/classBMessage.md) into which signatures of applications supporting files of any type are copied. |





**Returns:** `B_OK` on success or another error code on failure.



**See also:** [GetSupportingApps()](classBMimeType.md#a32e1d909b97c84d943ac50467e56fc3d) for details on the format of the data returned in the `BMessage` pointed to by `wild_ones`.



**Since:** BeOS R3

---

### `GuessMimeType()`

```cpp
status_t BMimeType::GuessMimeType(const char * filename, BMimeType * type)
```

Guesses a MIME type for the given filename. 


Only the filename itself is taken into consideration (in particular its name extension), not the entry it refers to. I.e. an entry with that name doesn't need to exist at all.


Parameters

| Parameter | Description |
| :--- | :--- |
| `filename` | The filename. |
| `type` | Pointer to a pre-allocated [BMimeType](classBMimeType.md) which is set to the resulting MIME type. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *ref* or *result*. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |





**Since:** Haiku R1

---

### `GuessMimeType()`

```cpp
status_t BMimeType::GuessMimeType(const entry_ref * file, BMimeType * type)
```

Guesses a MIME type for the entry referred to by the given [entry_ref](structentry__ref.md). 


This version of [GuessMimeType()](classBMimeType.md#a014ae51a0763796a1c9ed57c942fd46e) combines the features of the other versions: First the data of the given file are checked (sniffed). Only if the result of this operation is inconclusive, i.e. "application/octet-stream", the filename is examined for extensions.


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | Pointer to the [entry_ref](structentry__ref.md) referring to the entry. |
| `type` | Pointer to a pre-allocated [BMimeType](classBMimeType.md) which is set to the resulting MIME type. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *ref* or *result*. |
| B_NAME_NOT_FOUND | *ref* refers to an abstract entry. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |





**Since:** Haiku R1

---

### `GuessMimeType()`

```cpp
status_t BMimeType::GuessMimeType(const void * buffer, int32 length, BMimeType * type)
```

Guesses a MIME type for the supplied chunk of data. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | Pointer to the data buffer. |
| `length` | Size of the buffer in bytes. |
| `type` | Pointer to a pre-allocated [BMimeType](classBMimeType.md) which is set to the resulting MIME type. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *buffer* or *result*. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |





**Since:** Haiku R1

---

### `InitCheck()`

```cpp
status_t BMimeType::InitCheck()const
```

Returns the result of the most recent constructor or [SetTo()](classBMimeType.md#ab4eb64b2e47f111b796e641ffa624046) call. 



**Returns:** `B_OK` If the object is properly initialized, a specific error code otherwise.



**Since:** BeOS R3

---

### `Install()`

```cpp
status_t BMimeType::Install()
```

Adds the MIME type to the MIME database. 


To check if the MIME type is already installed, call `IsInstalled()`. To remove the MIME type from the database, call `Delete()`.



> [!NOTE]
> The R5 implementation returns random values if the type is already installed, so be sure to check `IsInstalled()` first.



**Returns:** `B_OK` on success or another error code on failure.



**See also:** [Delete()](classBMimeType.md#a928153d3227956971ee5e0d7ad23bbfd)



**Since:** BeOS R3

---

### `IsInstalled()`

```cpp
bool BMimeType::IsInstalled()const
```

Returns whether or not this type is currently installed in the MIME database. 


To add the MIME type to the database, call `Install()`. To remove the MIME type from the database, call `Delete()`.



**Returns:** A `bool` indicating whether or not this type is currently installed in the MIME database.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The MIME type is currently installed in the database. |
| false | The MIME type is not currently installed in the database. |





**Since:** BeOS R3

---

### `IsSupertypeOnly()`

```cpp
bool BMimeType::IsSupertypeOnly()const
```

Returns whether this objects represents a supertype. 



**Returns:** `true`, if the object is properly initialized and represents a supertype, `false` otherwise.



**Since:** BeOS R3

---

### `IsValid()`

```cpp
bool BMimeType::IsValid()const
```

Returns whether the object represents a valid MIME type. 



**Returns:** `true`, if the object is properly initialized, `false` otherwise.



**See also:** [SetTo()](classBMimeType.md#ab4eb64b2e47f111b796e641ffa624046) for further information.



**Since:** BeOS R3

---

### `IsValid()`

```cpp
bool BMimeType::IsValid(const char * string)
```

Returns whether the given string represents a valid MIME type. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The MIME type string. |





**Returns:** `true`, if the given string represents a valid MIME type.



**See also:** [SetTo()](classBMimeType.md#ab4eb64b2e47f111b796e641ffa624046) for further information.



**Since:** BeOS R3

---

### `operator==()`

```cpp
bool BMimeType::operator==(const BMimeType & type)const
```

Returns whether this and the supplied MIME type are equal. 


Two [BMimeType](classBMimeType.md) objects are said to be equal if they represent the same MIME string, ignoring case, or if both are not initialized.



> [!WARNING]
> In BeOS R5 two uninitialized [BMimeType](classBMimeType.md) objects were not considered to be equal, in Haiku they are.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The [BMimeType](classBMimeType.md) to be compared with. |





**Returns:** `true`, if the objects are equal, `false` otherwise.



**Since:** BeOS R3

---

### `operator==()`

```cpp
bool BMimeType::operator==(const char * type)const
```

Returns whether this and the supplied MIME type are equal. 


A [BMimeType](classBMimeType.md) objects equals a MIME string, if its MIME string equals the latter one, ignoring case, or if it is uninitialized and the MIME string is `NULL`.



> [!WARNING]
> In BeOS R5 an uninitialized [BMimeType](classBMimeType.md) object was not considered to be equal to `NULL`, in Haiku it is.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The MIME string to be compared with. |





**Returns:** `true`, if the MIME types are equal, `false` otherwise.



**Since:** BeOS R4

---

### `SetAppHint()`

```cpp
status_t BMimeType::SetAppHint(const entry_ref * ref)
```

Sets the app hint field for the MIME type. 


The app hint is a path that identifies the executable that should be used when launching an application that has this signature. For example, when Tracker needs to launch an app of type `"application/YourAppHere"`, it asks the database for the application hint. This hint is converted to an `entry_ref` before it is passed to the caller. Of course, the path may not point to an application, or it might point to an application with the wrong signature (and so on); that's why this is merely a hint.


The `entry_ref` pointed to by `ref` must be pre-allocated. It must be a valid `entry_ref` (i.e. `entry_ref(-1, -1, "some_file")` will trigger an error), but it need not point to an existing file, nor need it actually point to an application. That's not to say that it shouldn't; such an `entry_ref` would render the app hint useless.


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | Pointer to a pre-allocated `entry_ref` containting the location of the new app hint |





**Returns:** `B_OK` on success or another error code on failure.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The ref was retrieved successfully. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |
| B_BAD_VALUE | *ref* was `NULL`. |





**Since:** BeOS R3

---

### `SetAttrInfo()`

```cpp
since BeOS R3 *status_t BMimeType::SetAttrInfo(const BMessage * info)
```

Sets the description of the attributes typically associated with files of the given MIME type. 


The attribute information is technically arbitrary, but the expected format of the [BMessage](../application_kit/classBMessage.md) pointed to by the `info` parameter is as follows:



| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| **field name** | **type** | **element[0..n]** |
| "attr:name" | `B_STRING_TYPE` | The name of each attribute |
| "attr:public_name" | `B_STRING_TYPE` | The human-readable name of each attribute |
| "attr:type" | `B_INT32_TYPE` | The type code for each attribute |
| "attr:viewable" | `B_BOOL_TYPE` | For each attribute: `true` if the attribute is public, `false` if it's private |
| "attr:editable" | `B_BOOL_TYPE` | For each attribute: `true` if the attribute should be user editable, `false` if not |


The `BMessage::what` value is ignored.


Parameters

| Parameter | Description |
| :--- | :--- |
| `info` | Pointer to a pre-allocated and properly formatted [BMessage](../application_kit/classBMessage.md) containing information about the file attributes typically associated with the MIME type. |





**Returns:** `B_OK` on success or another error code on failure.



**Since:** BeOS R3

---

### `SetFileExtensions()`

```cpp
status_t BMimeType::SetFileExtensions(const BMessage * extensions)
```

Sets the list of filename extensions associated with the MIME type. 


The MIME database associates a list of filename extensions (a character string following the rightmost dot, `"."`, character in the filename) with each type. These extensions can then be used to help determine the type of any untyped files that may be encountered.


The list of extensions is given in a pre-allocated [BMessage](../application_kit/classBMessage.md) pointed to by the `extensions` parameter. The format of the message should be as follows:


* The message's `"extensions"` field should contain an indexed array of strings, one for each extension. The extensions are to be given without the preceding `"."` character (i.e. `"html"` or `"mp3"`, not `".html"` or `".mp3"` ).

* The `what` member of the [BMessage](../application_kit/classBMessage.md) is ignored.




> [!NOTE]
> Any other fields present in the `BMessage` will currently be retained and returned by calls to `GetFileExtensions()`; however, this may change in the future, so it is recommended that you not rely on this behavior, and that no other fields be present. Also, note that no checking is performed to verify the `BMessage` is properly formatted; it's up to you to do things right.


Finally, bear in mind that `SetFileExtensions()` clobbers the existing set of extensions. If you want to augment a type's extensions, you should retrieve the existing set, add the new ones, and then call `SetFileExtensions()`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `extensions` | Pointer to a pre-allocated, properly formatted [BMessage](../application_kit/classBMessage.md) containing the new list of file extensions to associate with this MIME type. |





**Returns:** `B_OK` on success or another error code on failure.



**Since:** BeOS R3

---

### `SetIcon()`

```cpp
status_t BMimeType::SetIcon(const BBitmap * icon, icon_size which)
```

Sets the large or mini icon for the MIME type. 


The icon is copied from the `BBitmap` pointed to by `icon`. The bitmap must be the proper size: `32x32` for the large icon, `16x16` for the mini icon. Additionally, the bitmap must be in the `B_CMAP8` color space (8-bit color).


If you want to erase the current icon, pass `NULL` as the `icon` argument.


Parameters

| Parameter | Description |
| :--- | :--- |
| `icon` | Pointer to a pre-allocated `BBitmap` of proper size and colorspace containing the new icon, or `NULL` to clear the current icon. |
| `which` | Value that specifies which icon to update. Currently `B_LARGE_ICON` and `B_MINI_ICON` are supported. |





**Returns:** `B_OK` on success or another error code on failure.



**Since:** BeOS R3

---

### `SetIcon()`

```cpp
status_t BMimeType::SetIcon(const uint8 * data, size_t size)
```

Sets the vector icon for the MIME type. 


The icon is copied from the provided *data* which must contain *size* bytes.


If you want to erase the current icon, pass `NULL` as the *data* argument.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | Pointer to a buffer containing the new icon, or `NULL` to clear the current icon. |
| `size` | Size of the provided buffer. |





**Returns:** `B_OK` on success or another error code on failure.



**Since:** Haiku R1

---

### `SetIconForType()`

```cpp
status_t BMimeType::SetIconForType(const char * type, const BBitmap * icon, icon_size which)
```

Sets the large or mini icon used by an application of this type for files of the given *type*. 


This can be confusing, so here's how this function is intended to be used:


* The actual `BMimeType` object should be set to the MIME signature of an application to whom you want to assign custom icons for custom MIME types.

* The `type` parameter specifies the file type whose custom icon you are setting.



The type of the `BMimeType` object is not required to actually be a subtype of `"application/"`; that is the intended use however, and application-specific icons are not expected to be present for non-application types.


The icon is copied from the `BBitmap` pointed to by `icon`. The bitmap must be the proper size: `32x32` for the large icon, `16x16` for the mini icon.


If you want to erase the current icon, pass `NULL` as the `icon` argument.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | Pointer to a pre-allocated string containing the MIME type whose custom icon you wish to set. |
| `icon` | Pointer to a pre-allocated `BBitmap` of proper size and colorspace containing the new icon, or `NULL` to clear the current icon. |
| `which` | Value that specifies which icon to update. Currently `B_LARGE_ICON` and `B_MINI_ICON` are supported. |





**Returns:** `B_OK` on success or another error code on failure.



**Since:** BeOS R3

---

### `SetIconForType()`

```cpp
status_t BMimeType::SetIconForType(const char * type, const uint8 * data, size_t dataSize)
```

Sets the icon used by an application of this type for files of the given *type*. 


This can be confusing, so here's how this function is intended to be used:


* The actual `BMimeType` object should be set to the MIME signature of an application to whom you want to assign custom icons for custom MIME types.

* The `type` parameter specifies the file type whose custom icon you are setting.



The type of the `BMimeType` object is not required to actually be a subtype of `"application/"`; that is the intended use however, and application-specific icons are not expected to be present for non-application types.


The icon is copied from the `BBitmap` pointed to by `icon`. The bitmap must be the proper size: `32x32` for the large icon, `16x16` for the mini icon.


If you want to erase the current icon, pass `NULL` as the `icon` argument.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | Pointer to a pre-allocated string containing the MIME type whose custom icon you wish to set. |
| `data` | Pointer to a pre-allocated uint8 array of the proper size to contain the new icon, or `NULL` to clear the current icon. |
| `dataSize` | The size of *data* in bytes. |





**Returns:** `B_OK` on success or another error code on failure.



**Since:** Haiku R1

---

### `SetLongDescription()`

```cpp
status_t BMimeType::SetLongDescription(const char * description)
```

Sets the long description field for the MIME type. 


The string pointed to by `description` must be of length less than `B_MIME_TYPE_LENGTH` characters.



> [!NOTE]
> If the MIME type is not installed, it will first be installed, and then the long description will be set.


Parameters

| Parameter | Description |
| :--- | :--- |
| `description` | Pointer to a pre-allocated string containing the new long description |





**Returns:** `B_OK` on success or another error code on failure.



**Since:** BeOS R3

---

### `SetPreferredApp()`

```cpp
status_t BMimeType::SetPreferredApp(const char * signature, app_verb verb = B_OPEN)
```

Sets the preferred application for the MIME type. 


The preferred app is the application that's used to access a file when, for example, the user double-clicks the file in a Tracker window. Unless the file identifies in its attributes a "custom" preferred app, Tracker will ask the file type database for the preferred app that's associated with the file's type.


The string pointed to by `signature` must be of length less than `B_MIME_TYPE_LENGTH` characters.



> [!NOTE]
> If the MIME type is not installed, it will first be installed, and then the preferred app will be set.


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | Pointer to a pre-allocated string containing the signature of the new preferred app. |
| `verb` | `app_verb` value that specifies the type of access for which you are setting the preferred app. Currently, the only supported app verb is `B_OPEN`. |





**Returns:** `B_OK` on success or another error code on failure.

---

### `SetShortDescription()`

```cpp
status_t BMimeType::SetShortDescription(const char * description)
```

Sets the short description field for the MIME type. 


The string pointed to by `description` must be of length less than `B_MIME_TYPE_LENGTH` characters.



> [!NOTE]
> If the MIME type is not installed, it will first be installed, and then the short description will be set.


Parameters

| Parameter | Description |
| :--- | :--- |
| `description` | Pointer to a pre-allocated string containing the new short description. |





**Returns:** `B_OK` on success or another error code on failure.



**Since:** BeOS R3

---

### `SetSnifferRule()`

```cpp
status_t BMimeType::SetSnifferRule(const char * rule)
```

Sets the MIME type's sniffer rule. 


If the supplied *rule* is `NULL`, the MIME type's sniffer rule is unset.


[SetSnifferRule()](classBMimeType.md#ab9da3155010b5f6d1a0868ca202b1ab9) does also return `B_OK`, if the type is not installed, but the call will have no effect in this case.


Parameters

| Parameter | Description |
| :--- | :--- |
| `rule` | The rule string, may be `NULL`. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | Uninitialized [BMimeType](classBMimeType.md). |
| B_BAD_MIME_SNIFFER_RULE | The supplied sniffer rule is invalid. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |





**See also:** [CheckSnifferRule()](classBMimeType.md#a7e1d370ef1e52b167ac7cee93ca1410e)



**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BMimeType::SetTo(const char * mimeType)
```

Initializes this object to the supplied MIME type. 


The supplied string must specify a valid MIME type or supertype. Valid MIME types are given by the following grammar:


MIMEType ::= Supertype "/" [ Subtype ] Supertype ::= "application" | "audio" | "image" | "message" | "multipart" | "text" | "video" Subtype ::= MIMEChar MIMEChar* MIMEChar ::= any character except white spaces, CTLs and '/', '<', '>', '@',, ',', ';', ':', '"', '(', ')', '[', ']', '?', '=', '\' (Note: RFC1341 also forbits '.', but it is allowed here.)


Currently the supertype is not restricted to one of the seven types given, but can be an arbitrary string (obeying the same rule as the subtype). Nevertheless it is a very bad idea to use another supertype. The supplied MIME string is copied; the caller retains the ownership.


Parameters

| Parameter | Description |
| :--- | :--- |
| `mimeType` | The MIME string. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | Invalid *mimeType* string. |
| B_NO_INIT | [BMimeType](classBMimeType.md) was uninitialized. |
| B_NO_MEMORY | Insufficient memory to copy the MIME string. |





**Since:** BeOS R3

---

### `SetType()`

```cpp
status_t BMimeType::SetType(const char * mimeType)
```

Initializes this object to the supplied MIME type. 



**Since:** BeOS R3

---

### `StartWatching()`

```cpp
status_t BMimeType::StartWatching(BMessenger target)
```

Starts monitoring the MIME database for a given target. 


Until [StopWatching()](classBMimeType.md#a3d48acac5d9fb081c55729c2b7045a6f) is called for the target, an update message is sent to it whenever the MIME database changes.


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | A [BMessenger](../application_kit/classBMessenger.md) identifying the target for the update messages. |





**Returns:** `B_OK` on success or another error code on failure.



**Since:** BeOS R4

---

### `StopWatching()`

```cpp
status_t BMimeType::StopWatching(BMessenger target)
```

Stops monitoring the MIME database for a given target (previously started via [StartWatching()](classBMimeType.md#a503a2f6daed253b2bb5f7a9469e9c2f7)). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | A [BMessenger](../application_kit/classBMessenger.md) identifying the target for the update messages. |





**Returns:** `B_OK` on success or another error code on failure.



**Since:** BeOS R4

---

### `Type()`

```cpp
const char * BMimeType::Type()const
```

Returns the MIME string represented by this object. 



**Returns:** The MIME string, if the object is properly initialized, `NULL` otherwise.



**Since:** BeOS R3

---

### `Unset()`

```cpp
void BMimeType::Unset()
```

Returns the object to an uninitialized state. 



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMimeType.html).
