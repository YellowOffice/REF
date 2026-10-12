---
name: BUrl
type: class
kit: support_kit
brief: "Represents and manipulates an URL (Uniform Resource Locator)"
source: haiku-book
---

# BUrl Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Represents and manipulates an URL (Uniform Resource Locator). 



**Since:** Haiku R1


An "Uniform Resource Locator" identifies a place where a resource can be found. It specifies both a location and a mechanism to retrieve the data. For example, [http://www.example.com/index.html](http://www.example.com/index.html) indicates a protocol (http), a hostname (www.example.com), and a file name (index.html).


Every URL consists of a sequence of up to five components: protocol, authority (consisting of login and password, hostname and port) path, request and fragment.


The format is provided in RFC3986 (URI generic syntax), Appendix B as a regular expression: ^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?


This regular expression makes it possible to parse any string as an URL (if there are no special characters to spearate the fields, everything will end up in the path compopent). However, some characters are not allowed: space, newlines, tabs, <, > and ". If any of these is present in the URL string, the parsing results in an empty URL.


The protocols (http, https, ftp, irc, etc) identifies which way the resource can be accessed.


Authority consists of userinfo such as username and password, a host subcomponent consisting of IP address or hostname and a port subcomponent.


The path component locates the resource inside the authority's hierarchy, and can have different formats (for example, directory names separated by slashes) depending on the protocol in use.


The request component (preceeded by a question mark) contains a query string of non-hierarchial data.


The fragment contains a fragment identifier providing direction to a secondary resource, usually an identifier for a specific element into the resource such as a paragraph in a text.

## Member List

### Public Member Functions

* `virtual status_t` [Archive](#a7a31ffee9b9a2a2c0ed5e1469926b0fa) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `bool` [HasPreferredApplication](#ac9246cefd84a7982f6f2c50c2b6542df) () const — Undocumented public method.
* `status_t` [IDNAToAscii](#abca014a8cc3914752f705b7d54d0fd5f) () — Undocumented public method.
* `status_t` [IDNAToUnicode](#afcc5d2782f5dc66adfc551ac91fda03b) () — Undocumented public method.
* `status_t` [OpenWithPreferredApplication](#a09f6715479da11c9144097fd14108ea3) (bool onProblemAskUser=true) const — Undocumented public method.
* [operator const char *](#a3e90fb68ff042f3466b07fd50f18000f) () const — Undocumented public method.
* `bool` [operator!=](#ab19ee40437564a6973655e99b520ae38) (BUrl &other) const — Undocumented public method.
* `const BUrl &` [operator=](#a38bc20169ae0167ece8b6db3a1e387bd) (const BString &string) — Undocumented public method.
* `const BUrl &` [operator=](#a0c014664d9af6d2922ced7f1c7d32f9c) (const BUrl &other) — Undocumented public method.
* `const BUrl &` [operator=](#a6eec777fcd47f02fdd9227f9c774a3d1) (const char *string) — Undocumented public method.
* `bool` [operator==](#a8d540dc63f937690a33affe3ab202a6c) (BUrl &other) const — Undocumented public method.
* `BString` [PreferredApplication](#abe2a65d6ac098771d30cc906cb78c13e) () const — Undocumented public method.
* [BUrl](#a1df61481f2881af6c5b2849400db35a3) (const char *url, bool encode=true) — Constructs a BUrl and fills it.
* [BUrl](#a5293b708cdf87492893d60653412169d) (BMessage *archive) — Restore an URL from archived data.
* [BUrl](#ae807d2bcb5472e5c7dac4a5232411a9a) (const BUrl &other) — Copy constructor.
* [BUrl](#a60259de36be5fe073c5c3ad98c011645) (const BUrl &base, const BString &relative) — Construct a BUrl using a known base and a string representing a relative URL.
* [BUrl](#af1ff7c9a2d6a3db235dbefb7f39ddd8f) (const BPath &path) — Constructs a BUrl identifying a local file.
* BUrl () — Constructs an empty BUrl.
* `virtual` ~BUrl () — Destructor for BUrl.
* `BUrl &` [SetUrlString](#a7ba7686cc8e16427b435baeea4e7e408) (const BString &url, bool encode=true) — Parse a string and set the URL accordingly.
* `BUrl &` [SetProtocol](#a197682695d429bb6ac00aad83f1763d4) (const BString &scheme) — Set the protocol.
* `BUrl &` [SetUserName](#a97ac2ce47db4214c813bb54804bf6817) (const BString &user) — Set the username in the authority component.
* `BUrl &` [SetPassword](#ad08b29132b24147d450d91f4cb9555b0) (const BString &password) — Set the password in the authority component.
* `void` [SetAuthority](#a118c3ce21032d81625b26318f9813c9e) (const BString &authority) — Replace the complete authority component.
* `BUrl &` [SetHost](#aaa5b4f8a1f155de6344971ebd099029f) (const BString &host) — Sets the host part of the authority component.
* `BUrl &` [SetPort](#abad7861de9d16c1199d658c5844bb14e) (int port) — Set the port of the authority component.
* `BUrl &` [SetPath](#a76be6277ba21086f775c974bc182ce4c) (const BString &path) — Set the path of the URL.
* `BUrl &` [SetRequest](#a1450afbf8c6359872cd8f4df9ce54ee3) (const BString &request) — Set the request part of the URL.
* `BUrl &` [SetFragment](#a97388e065d4863faf20093866510a7c5) (const BString &fragment) — Set the fragment part of the URL.
* `const BString &` [UrlString](#abe7146fe16a9177a5eb3d0eda8df01fa) () const — Returns the string representation of the URL.
* `const BString &` [Protocol](#a5fe451dcb0024678f5e34188391b5496) () const — Returns the protocol used in the url.
* `const BString &` [UserName](#a6a79c0ca3d8eb190ef855e92c3800593) () const — Returns the username.
* `const BString &` [Password](#a3a0b93ae1312526a97bcea3eb4ec327c) () const — Returns the password.
* `const BString &` [UserInfo](#ac381182fc92fd3b314312dd566c0cd07) () const — Returns the user information (username:password)
* `const BString &` [Host](#a3bedb52143857d30495789c09f258134) () const — Returns the URL host component.
* `int` [Port](#a7178e9456097294f5a7a454371898410) () const — Returns the URL port number.
* `const BString &` [Authority](#aa772e3c1c34c9f318a59249e122ffbbd) () const — Returns the authority url as a string.
* `const BString &` [Path](#adf781a52fc4369605b9fab4d60c263e1) () const — Returns the url path.
* `const BString &` [Request](#afce69e43da0253fce49a4591ac98a329) () const — Returns the url-request.
* `const BString &` [Fragment](#a5247243f9c25d56e3af0b4bb13599c92) () const — Returns the fragment of the url.
* `bool` [IsValid](#ac000b758475efde79295319800c4b94b) () const — Check if the URL is valid.
* `bool` [HasProtocol](#a4b884454b70e103c201961eac0650f82) () const — Check wether the URL has a protocol.
* `bool` [HasUserName](#a857be1340cf7af43e810126394ad9dad) () const — Check wether the URL has an username.
* `bool` [HasPassword](#a3961a8f49869c3cad79bc8a1b04e4491) () const — Check wether the URL has a password.
* `bool` [HasUserInfo](#a34c3b86756ac910df9fbcde6d49fd158) () const — Check wether the URL has user information.
* `bool` [HasHost](#a405d684c631e583b49474e2c23e318ba) () const — Check wether the URL has an host.
* `bool` [HasPort](#a6a377ec8b922efe03773ff751afc9e14) () const — Check wether the URL has a port.
* `bool` [HasAuthority](#a703193b440ab8ff190d4ce2cd72e88f0) () const — Check if the URL has an host or port.
* `bool` [HasPath](#a0f92337b33cb90ea69ff0a8d13994e0a) () const — Check wether the URL has a path.
* `bool` [HasRequest](#a5ddadbf707dcfcf06dd0f84c72da89be) () const — Check wether the URL has a request.
* `bool` [HasFragment](#a3f7abc38df2ca8439acdda75ffb76c2c) () const — Check wether the URL has a fragment.
* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).

### Static Public Member Functions

* `static BArchivable *` [Instantiate](#ab44ebd044cb54077712694ac3b625bc7) (BMessage *archive) — Undocumented public method.
* `static BString` [UrlDecode](#a9975cd2f6b18d067246da734816bd66c) (const BString &url, bool strict=false) — URL-decode a string containing an URL or URL component.
* `static BString` [UrlEncode](#a36dee6b88cc2454848cc9790fdd2f7d5) (const BString &url, bool strict=false, bool directory=false) — URL-encode a string containing an URL or URL component.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BUrl()`

```cpp
BUrl::BUrl(const char * url, bool encode = true)
```

Constructs a [BUrl](classBUrl.md) and fills it. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `url` | A string to parse and populate the URL fields from. |
| `encode` | Wether to urlencode the string. |




The URL fields are extracted from the passed string and encoded. If you are constructing an URL from a string that is already URL-encoded, set encode to false.


Call InitCheck() to verify that the string was succesfully parsed and resulted in a valid URL.

---

### `BUrl()`

```cpp
BUrl::BUrl(BMessage * archive)
```

Restore an URL from archived data. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | An archived [BUrl](classBUrl.md) (using BArchive()). |




Usually, archived messages are restored using BArchivable::Unarchive() which will automatically instanciate the correct class.

---

### `BUrl()`

```cpp
BUrl::BUrl(const BUrl & other)
```

Copy constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | A [BUrl](classBUrl.md) object to copy. |

---

### `BUrl()`

```cpp
BUrl::BUrl(const BUrl & base, const BString & relative)
```

Construct a [BUrl](classBUrl.md) using a known base and a string representing a relative URL. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `base` | A [BUrl](classBUrl.md) object that holds base URL. |
| `relative` | A path relative to the base URL. |




URLs can sometimes be represented in relative form. For example, links in a webpage may refer to only a path, assuming the same protocol and authority are the same as the current page. This constructor applies the required resolution process to construct a complete, standalone URL from such a string.


For example, the following:


[BUrl](classBUrl.md) base("http://example.org/path/page.html"); [BUrl](classBUrl.md) relative(base, "sudirectory/otherpage.html");


results in:


"http://example.org/path/subdirectory/otherpage.hhtml"


The relative URL can override any of the fields from the original one. The algorithm for resolution is documented in RFC3986 section 5.

---

### `BUrl()`

```cpp
BUrl::BUrl(const BPath & path)
```

Constructs a [BUrl](classBUrl.md) identifying a local file. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The path to convert into an URL |




The generated URL uses the file protocol, and its path component is the path given as a parameter.

---

### `Archive()`

```cpp
virtual status_t BUrl::Archive(BMessage * into, bool deep = true)const
```

Archive the object into a [BMessage](../application_kit/classBMessage.md). 


You should call this method from your derived implementation as it adds the data needed to instantiate your object to the message.


Parameters

| Parameter | Description |
| :--- | :--- |
| `into` | The message you store your object in. |
| `deep` | If `true`, all children of this object should be archived as well. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The archive operation was successful. |
| B_BAD_VALUE | `NULL` *archive* message. |
| B_ERROR | The archive operation failed. |





**Since:** BeOS R3


Reimplemented from [BArchivable](classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44).

---

### `Authority()`

```cpp
const BString & BUrl::Authority()const
```

Returns the authority url as a string. 



**Returns:** The authority url as a string.


The authority is of the form username:password@host:port.

---

### `Fragment()`

```cpp
const BString & BUrl::Fragment()const
```

Returns the fragment of the url. 



**Returns:** The fragment of the url as a string.

---

### `HasAuthority()`

```cpp
bool BUrl::HasAuthority()const
```

Check if the URL has an host or port. 



**Returns:** True if the URL has an host or port.

---

### `HasFragment()`

```cpp
bool BUrl::HasFragment()const
```

Check wether the URL has a fragment. 



**Returns:** True if the URL has a fragment.

---

### `HasHost()`

```cpp
bool BUrl::HasHost()const
```

Check wether the URL has an host. 



**Returns:** True if the URL has an host.

---

### `HasPassword()`

```cpp
bool BUrl::HasPassword()const
```

Check wether the URL has a password. 



**Returns:** True if the URL has a password.

---

### `HasPath()`

```cpp
bool BUrl::HasPath()const
```

Check wether the URL has a path. 



**Returns:** True if the URL has a path.

---

### `HasPort()`

```cpp
bool BUrl::HasPort()const
```

Check wether the URL has a port. 



**Returns:** True if the URL has a port.

---

### `HasPreferredApplication()`

```cpp
bool BUrl::HasPreferredApplication()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `HasProtocol()`

```cpp
bool BUrl::HasProtocol()const
```

Check wether the URL has a protocol. 



**Returns:** True if the URL has a protocol.

---

### `HasRequest()`

```cpp
bool BUrl::HasRequest()const
```

Check wether the URL has a request. 



**Returns:** True if the URL has a request.

---

### `HasUserInfo()`

```cpp
bool BUrl::HasUserInfo()const
```

Check wether the URL has user information. 



**Returns:** True if the URL has an username or password.

---

### `HasUserName()`

```cpp
bool BUrl::HasUserName()const
```

Check wether the URL has an username. 



**Returns:** True if the URL has an username.

---

### `Host()`

```cpp
const BString & BUrl::Host()const
```

Returns the URL host component. 



**Returns:** The URL host.

---

### `IDNAToAscii()`

```cpp
status_t BUrl::IDNAToAscii()
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `IDNAToUnicode()`

```cpp
status_t BUrl::IDNAToUnicode()
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Instantiate()`

```cpp
static static BArchivable * BUrl::Instantiate(BMessage * archive)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `IsValid()`

```cpp
bool BUrl::IsValid()const
```

Check if the URL is valid. 



**Returns:** true if the URL is valid.


This function verifies that the mandatory fields are present and perform some other sanity checks on the URL.


An URL is valid if:


* It has a protocol, starting with an alphabetic character and folowed by alphanumeric or +, -, or . characters exclusively,

* If the protocol requires one, there is a valid host,

* If the protocol requires one, there is a path.

* If there is a host, it is either an IPv4 address or valid DNS name, or an IPv6 address enclosed in brackets



An invalid URL can still be modified using the various setters to turn it into a valid one.

---

### `OpenWithPreferredApplication()`

```cpp
status_t BUrl::OpenWithPreferredApplication(bool onProblemAskUser = true)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `onProblemAskUser` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `operator const char *()`

```cpp
BUrl::operator const char *()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `operator!=()`

```cpp
bool BUrl::operator!=(BUrl & other)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `operator=()`

```cpp
const BUrl & BUrl::operator=(const BString & string)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `operator=()`

```cpp
const BUrl & BUrl::operator=(const BUrl & other)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `operator=()`

```cpp
const BUrl & BUrl::operator=(const char * string)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `operator==()`

```cpp
bool BUrl::operator==(BUrl & other)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Password()`

```cpp
const BString & BUrl::Password()const
```

Returns the password. 



**Returns:** The password.

---

### `Path()`

```cpp
const BString & BUrl::Path()const
```

Returns the url path. 



**Returns:** The url-path.

---

### `Port()`

```cpp
int BUrl::Port()const
```

Returns the URL port number. 



**Returns:** The URL port number.


-1 is returned if no port is set.

---

### `PreferredApplication()`

```cpp
BString BUrl::PreferredApplication()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Protocol()`

```cpp
const BString & BUrl::Protocol()const
```

Returns the protocol used in the url. 



**Returns:** The URL protocol.

---

### `Request()`

```cpp
const BString & BUrl::Request()const
```

Returns the url-request. 



**Returns:** The url-request as a string.

---

### `SetAuthority()`

```cpp
void BUrl::SetAuthority(const BString & authority)
```

Replace the complete authority component. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `authority` | The authority component. |




The username, password, host and port fields are replaced. The authority can be of the form username:password@host:port

---

### `SetFragment()`

```cpp
BUrl & BUrl::SetFragment(const BString & fragment)
```

Set the fragment part of the URL. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `fragment` | The fragment to use. |

---

### `SetHost()`

```cpp
BUrl & BUrl::SetHost(const BString & host)
```

Sets the host part of the authority component. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `host` | The hostname or address to use. |

---

### `SetPassword()`

```cpp
BUrl & BUrl::SetPassword(const BString & password)
```

Set the password in the authority component. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `password` | The password. |

---

### `SetPath()`

```cpp
BUrl & BUrl::SetPath(const BString & path)
```

Set the path of the URL. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | Set the path to use. |

---

### `SetPort()`

```cpp
BUrl & BUrl::SetPort(int port)
```

Set the port of the authority component. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `port` | The port number to use (usually a TCP or UDP port). |

---

### `SetProtocol()`

```cpp
BUrl & BUrl::SetProtocol(const BString & scheme)
```

Set the protocol. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `scheme` | The protocol to use. |

---

### `SetRequest()`

```cpp
BUrl & BUrl::SetRequest(const BString & request)
```

Set the request part of the URL. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `request` | The request string. |

---

### `SetUrlString()`

```cpp
BUrl & BUrl::SetUrlString(const BString & url, bool encode = true)
```

Parse a string and set the URL accordingly. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `url` | A string to parse as an absolute URL. |
| `encode` | Wether to URL-encode the string. |




Set encode to false if the URL string is already URL-encoded.

---

### `SetUserName()`

```cpp
BUrl & BUrl::SetUserName(const BString & user)
```

Set the username in the authority component. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `user` | The username. |

---

### `UrlDecode()`

```cpp
static BString BUrl::UrlDecode(const BString & url, bool strict = false)
```

URL-decode a string containing an URL or URL component. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `strict` | Use strict mode. |





**Returns:** The decoded URL string



**Since:** Haiku R1

---

### `UrlEncode()`

```cpp
static BString BUrl::UrlEncode(const BString & url, bool strict = false, bool directory = false)
```

URL-encode a string containing an URL or URL component. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `strict` | Use strict mode |
| `directory` | Use directory mode |




In strict mode, space are replaced by %20. In non-strict mode they are replaced by a + character.


In directory mode, / and \ characters are not encoded. In the other fields they are percent-encoded.



**Returns:** The encoded URL string



**Since:** Haiku R1

---

### `UrlString()`

```cpp
const BString & BUrl::UrlString()const
```

Returns the string representation of the URL. 



**Returns:** the string representation of the URL.


A complete URL string is of the form protocol://username:passord@host:port/path?request::fragment . All the fields are optional, for example a file URL will have only a protocol and a path.

---

### `UserInfo()`

```cpp
const BString & BUrl::UserInfo()const
```

Returns the user information (username:password) 



**Returns:** The username and password.


If there is no password, the username alone is returned. If there is no username, a string of the form ":password" is returned.

---

### `UserName()`

```cpp
const BString & BUrl::UserName()const
```

Returns the username. 



**Returns:** The username.

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBUrl.html).
