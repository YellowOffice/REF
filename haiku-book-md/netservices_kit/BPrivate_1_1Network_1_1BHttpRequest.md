---
name: BPrivate::Network::BHttpRequest
type: class
kit: netservices_kit
brief: "Represent a HTTP request"
source: haiku-book
---

# BPrivate::Network::BHttpRequest Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Represent a HTTP request. 


This class can be used to construct HTTP requests that can be executed by the [Network](namespaceBPrivate_1_1Network.md) Services Kit. A request has two states, either it is is a valid request, or it is an empty request. The criterium is whether or not the request has a URL. This class has all kinds of convenience methods set and retrieve particular options. Most options are wrapped in specialized container classes that do some form of validation.


The default options are: 


| Getter | Setter | Description | Default |
| :--- | :--- | :--- | :--- |
| [Url()](classBPrivate_1_1Network_1_1BHttpRequest.md#a4ab0b01f3f6dbd94dedcddb2a0daf72c) | [SetUrl()](classBPrivate_1_1Network_1_1BHttpRequest.md#a6c095622eb7be3bec6d5a58b3de76b47) | The URL. This must start with http or https. | Defaults to an empty [BUrl](../support_kit/classBUrl.md) |
| [Fields()](classBPrivate_1_1Network_1_1BHttpRequest.md#aa2b4c16a1e5e8c59052b4f310f63dfb4) | [SetFields()](classBPrivate_1_1Network_1_1BHttpRequest.md#abb42d55a1b9296ee317091694852ba28) | Additional fields set in the request header. | Defaults with no additional fields |
| [Method()](classBPrivate_1_1Network_1_1BHttpRequest.md#a15ec1596ab365755cce3a93ef26f1cf5) | [SetMethod()](classBPrivate_1_1Network_1_1BHttpRequest.md#a0b749d41f92f0102e279607f031055ad) | The HTTP method for the request | Defaults to [BHttpMethod::Get](classBPrivate_1_1Network_1_1BHttpMethod.md#ga16eddbfe1a87e0c5c233416f2358e55eae16d94bfc1bdba38523d7d09648f314f) |
| [MaxRedirections()](classBPrivate_1_1Network_1_1BHttpRequest.md#a171280deecf9e9222b42244b1a892e03) | [SetMaxRedirections()](classBPrivate_1_1Network_1_1BHttpRequest.md#afcc97e60fdf1b05592908e592e83665f) | How many redirections should be followed. Set to 0 to disable. | Defaults to 8 redirections per request |
| [RequestBody()](classBPrivate_1_1Network_1_1BHttpRequest.md#a65dbf7dc1fa5e5ea26578c9c613b53d1) | [SetRequestBody()](classBPrivate_1_1Network_1_1BHttpRequest.md#a20ba3bb6bd91224a7207d56208add672) | [Body](structBPrivate_1_1Network_1_1BHttpRequest_1_1Body.md) contents that is sent with the request. | Defaults to an empty body |
| [StopOnError()](classBPrivate_1_1Network_1_1BHttpRequest.md#a156aa59838ce4b782f18aef1a85525dc) | [SetStopOnError()](classBPrivate_1_1Network_1_1BHttpRequest.md#ac1b3d4ad8820991191ef12a3e9850ca7) | Stop parsing the server response when there is a client or server error. | Defaults to *false* |
| [Timeout()](classBPrivate_1_1Network_1_1BHttpRequest.md#a90a392bb5093f33dc7825c5d227cdf01) | [SetTimeout()](classBPrivate_1_1Network_1_1BHttpRequest.md#a2d86edf07d6e9458493e8c274ab760ff) | The timeout determines how long is waited for the server to respond | `B_INFINITE_TIMEOUT` |



**Since:** Haiku R1

## Member List

### Classes

* `struct` [Body](#Body) — Describe the body for a network request.

### Public Member Functions

* [BHttpRequest](#a32e3059501cecb9c77e92c89c2f7674e) () — Construct an empty HTTP request.
* [BHttpRequest](#aa7773d8d1165f4f05c1a5265e60d24c4) (const BUrl &url) — Construct a HTTP request for an url.
* [BHttpRequest](#a55afcc4906f83a75370bc2f963047e9b) (const BHttpRequest &other)=delete — Copying is not allowed.
* [BHttpRequest](#a7e6af5e282a64319c35e5baf1f817ef6) (BHttpRequest &&other) noexcept — Move constructor.
* [~BHttpRequest](#a26e9ac3a43fe05eec0e8ac1b863012a7) () — Destructor.
* `BHttpRequest &` [operator=](#ae791ddb4bc341aa2439733563e4bf774) (const BHttpRequest &other)=delete — Copy assignment is not allowed.
* `BHttpRequest &` [operator=](#a4cca69e9a02ab1db1b7a34a667b044e5) (BHttpRequest &&) noexcept — Move assignment.
* `bool` [IsEmpty](#a5b0464e2f3417b904bce245cf5faff3b) () const noexcept — Check if the request is valid or empty.
* `const BHttpAuthentication *` [Authentication](#ac837488d86d25ef1f52e1f0631b84eee) () const noexcept — Get the credentials for the authentication for the request.
* `const BHttpFields &` [Fields](#aa2b4c16a1e5e8c59052b4f310f63dfb4) () const noexcept — Get the additional header fields set for the request.
* `uint8` [MaxRedirections](#a171280deecf9e9222b42244b1a892e03) () const noexcept — Get the current redirection options for this request.
* `const BHttpMethod &` [Method](#a15ec1596ab365755cce3a93ef26f1cf5) () const noexcept — Get the current method for the request.
* `const Body *` [RequestBody](#a65dbf7dc1fa5e5ea26578c9c613b53d1) () const noexcept — Get the details of the custom body set for the request.
* `bool` [StopOnError](#a156aa59838ce4b782f18aef1a85525dc) () const noexcept — Is the request set to parse the full response on error.
* `bigtime_t` [Timeout](#a90a392bb5093f33dc7825c5d227cdf01) () const noexcept — Get the current timeout for the server to respond.
* `const BUrl &` [Url](#a4ab0b01f3f6dbd94dedcddb2a0daf72c) () const noexcept — Get the current Url for the request.
* `void` [SetAuthentication](#ae334ac3d1f5408479d75814f7a28af26) (const BHttpAuthentication &authentication) — Set the credentials to enable basic authentication for the request.
* `void` [SetFields](#abb42d55a1b9296ee317091694852ba28) (const BHttpFields &fields) — Set additional header fields for this request.
* `void` [SetMaxRedirections](#afcc97e60fdf1b05592908e592e83665f) (uint8 maxRedirections) — Set the redirection options for this request.
* `void` [SetMethod](#a0b749d41f92f0102e279607f031055ad) (const BHttpMethod &method) — Set the method for this request.
* `void` [SetRequestBody](#a20ba3bb6bd91224a7207d56208add672) (std::unique_ptr< BDataIO > input, BString mimeType, std::optional< off_t > size) — Set a body for this request.
* `void` [SetStopOnError](#ac1b3d4ad8820991191ef12a3e9850ca7) (bool stopOnError) — Set whether the entire response will be parsed on a client or server error.
* `void` [SetTimeout](#a2d86edf07d6e9458493e8c274ab760ff) (bigtime_t timeout) — Set the maximum time waiting for the server to respond.
* `void` [SetUrl](#a6c095622eb7be3bec6d5a58b3de76b47) (const BUrl &url) — Set the url for this request.
* `void` [ClearAuthentication](#a4d93841151f1214139608df29013c66c) () noexcept — Clear any authentication details previously set with SetAuthentication().
* `std::unique_ptr< BDataIO >` [ClearRequestBody](#a929a032b44ef5222877661aceeefe468) () noexcept — Clear any request body previously set with SetRequestBody().
* `BString` [HeaderToString](#a99c6af9d109665f433c8270502d9aebf) () const — Serialize the HTTP Header of this request to a string.

## Detailed Member Documentation

### `BHttpRequest()`

```cpp
BPrivate::Network::BHttpRequest::BHttpRequest()
```

Construct an empty HTTP request. 


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | This exception may be raised if it is impossible to allocate memory. |





**Since:** Haiku R1

---

### `BHttpRequest()`

```cpp
BPrivate::Network::BHttpRequest::BHttpRequest(const BUrl & url)
```

Construct a HTTP request for an *url*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `url` | A valid URL with the `http` or `https` protocol. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | This exception may be raised if it is impossible to allocate memory. |
| [BUnsupportedProtocol](classBPrivate_1_1Network_1_1BUnsupportedProtocol.md) | This exception is raised when the protocol of the URL cannot be handled. |
| [BInvalidUrl](classBPrivate_1_1Network_1_1BInvalidUrl.md) | This exception is raised when the *url* is invalid. |





**Since:** Haiku R1

---

### `BHttpRequest()`

```cpp
BPrivate::Network::BHttpRequest::BHttpRequest(const BHttpRequest & other)
```

Copying is not allowed. 



**Since:** Haiku R1

---

### `BHttpRequest()`

```cpp
BPrivate::Network::BHttpRequest::BHttpRequest(BHttpRequest && other)
```

Move constructor. 


After a move, the *other* object is left in an empty state.


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The request to move data from. |





**Since:** Haiku R1

---

### `~BHttpRequest()`

```cpp
BPrivate::Network::BHttpRequest::~BHttpRequest()
```

Destructor. 



**Since:** Haiku R1

---

### `Authentication()`

```cpp
const BHttpAuthentication * BPrivate::Network::BHttpRequest::Authentication()const
```

Get the credentials for the authentication for the request. 



**Returns:** When no credentials are set for this request, the method returns a `nullptr`. Otherwise, it will return a pointer to the current [BHttpAuthentication](structBPrivate_1_1Network_1_1BHttpAuthentication.md) data set for this request.



**Since:** Haiku R1

---

### `ClearAuthentication()`

```cpp
void BPrivate::Network::BHttpRequest::ClearAuthentication()
```

Clear any authentication details previously set with [SetAuthentication()](classBPrivate_1_1Network_1_1BHttpRequest.md#ae334ac3d1f5408479d75814f7a28af26). 


If there is no authentication data set, this method does nothing.



**Since:** Haiku R1

---

### `ClearRequestBody()`

```cpp
std::unique_ptr< BDataIO > BPrivate::Network::BHttpRequest::ClearRequestBody()
```

Clear any request body previously set with [SetRequestBody()](classBPrivate_1_1Network_1_1BHttpRequest.md#a20ba3bb6bd91224a7207d56208add672). 



**Returns:** Returns the previously set input [BDataIO](../support_kit/classBDataIO.md) object. If there is no request body set, this method returns `nullptr`.



**Since:** Haiku R1

---

### `Fields()`

```cpp
const BHttpFields & BPrivate::Network::BHttpRequest::Fields()const
```

Get the additional header fields set for the request. 


The returned header fields may be empty if no additional header fields were set.



**Since:** Haiku R1

---

### `HeaderToString()`

```cpp
BString BPrivate::Network::BHttpRequest::HeaderToString()const
```

Serialize the HTTP Header of this request to a string. 


The HTTP header consists of the request line, and the fields, serialized as text according to the HTTP specification.


This method can be used to debug requests.



**Returns:** A new string that represents the HTTP request.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | In case it is not possible to allocate memory for the output string. |





**Since:** Haiku R1

---

### `IsEmpty()`

```cpp
bool BPrivate::Network::BHttpRequest::IsEmpty()const
```

Check if the request is valid or empty. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The request is empty. |
| false | The request is valid. |





**Since:** Haiku R1

---

### `MaxRedirections()`

```cpp
uint8 BPrivate::Network::BHttpRequest::MaxRedirections()const
```

Get the current redirection options for this request. 



**See also:** [BHttpRequest::SetMaxRedirections()](classBPrivate_1_1Network_1_1BHttpRequest.md#afcc97e60fdf1b05592908e592e83665f) for details on the options.



**Since:** Haiku R1

---

### `Method()`

```cpp
const BHttpMethod & BPrivate::Network::BHttpRequest::Method()const
```

Get the current method for the request. 


This will either return the custom value set for this request, or the default as is listed in the overview documentation of this class.



**Since:** Haiku R1

---

### `operator=()`

```cpp
BHttpRequest & BPrivate::Network::BHttpRequest::operator=(BHttpRequest && other)
```

Move assignment. 


After a move, the *other* object is left in an empty state.


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The request to move data from. |





**Since:** Haiku R1

---

### `operator=()`

```cpp
BHttpRequest & BPrivate::Network::BHttpRequest::operator=(const BHttpRequest & other)
```

Copy assignment is not allowed. 



**Since:** Haiku R1

---

### `RequestBody()`

```cpp
const BHttpRequest::Body * BPrivate::Network::BHttpRequest::RequestBody()const
```

Get the details of the custom body set for the request. 



**Returns:** When no body is set for this request, the method returns a `nullptr`. Otherwise, it will return a pointer to a struct that describes the current body.



**Since:** Haiku R1

---

### `SetAuthentication()`

```cpp
void BPrivate::Network::BHttpRequest::SetAuthentication(const BHttpAuthentication & authentication)
```

Set the credentials to enable basic authentication for the request. 


The Basic authorization line is added to the request upon setting the request details. There is no support for other authentication schemes, like digest authentication.


Parameters

| Parameter | Description |
| :--- | :--- |
| `authentication` | The credentials to apply to the request. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | This exception may be raised if it is impossible to allocate memory. |





**Since:** Haiku R1

---

### `SetFields()`

```cpp
void BPrivate::Network::BHttpRequest::SetFields(const BHttpFields & fields)
```

Set additional header *fields* for this request. 


There are a few reserved fields, which cannot be set as optional fields. These currently are: `Host` `Accept-Encoding` `Connection` `Content-Type` `Content-Length` 


Parameters

| Parameter | Description |
| :--- | :--- |
| `fields` | Additional fields for the header of the request. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | This exception may be raised if it is impossible to allocate memory. |
| BHttpFields::InvalidData | This exception is raised when the *fields* contain reserved fields. |





**Since:** Haiku R1

---

### `SetMaxRedirections()`

```cpp
void BPrivate::Network::BHttpRequest::SetMaxRedirections(uint8 maxRedirections)
```

Set the redirection options for this request. 


The HTTP protocol allows the server to redirect requests if the resources have moved to a new location. For your convenience, you can instruct the network services kit to follow these redirections. You can set how many redirects should be followed. The maximum value is that of an unsigned 8 bit int, so maximum is 256 redirects. This prevents the request from staying stuck in a redirection loop.


If redirects are set to 0, or the maximum number of redirects have been processed, then the response will be set to the actual (last) received redirection response.


Parameters

| Parameter | Description |
| :--- | :--- |
| `maxRedirections` | The number of redirections to follow. Set to 0 to disable. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | This exception may be raised if it is impossible to allocate memory. |





**Since:** Haiku R1

---

### `SetMethod()`

```cpp
void BPrivate::Network::BHttpRequest::SetMethod(const BHttpMethod & method)
```

Set the *method* for this request. 


Note that there currently is no additional validation done on any semantical incompatibilities. This means that it is currently allowed to do a `GET` or `HEAD` request with data, while that is forbidden by the standard.


Parameters

| Parameter | Description |
| :--- | :--- |
| `method` | The method to use for the request. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | This exception may be raised if it is impossible to allocate memory. |





**Since:** Haiku R1

---

### `SetRequestBody()`

```cpp
void BPrivate::Network::BHttpRequest::SetRequestBody(std::unique_ptr< BDataIO > input, BString mimeType, std::optional< off_t > size)
```

Set a body for this request. 


When the requests needs a body, this method can be used to set the contents of that body.


Parameters

| Parameter | Description |
| :--- | :--- |
| `input` | The input is an owned pointer to an input. The lifetime of the input is guaranteed up to the point that the request is sent for execution. |
| `mimeType` | A valid mimetype, with a class and a subtype. For example `text/plain` is a valid mime type. |
| `size` | When the content size is set, the request will have a `Content-Length` header field. If the *input* has less data in the buffer, this will cause the request to error out. However, if the input has more data, it is only read up to size. If the actual size of the data is unknown, this can be made optional. The request body will then be sent as a so-called chunked transfer, sending data until the input is at the end. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | This exception may be raised if it is impossible to allocate memory. |
| std::invalid_argument | This exception is raised when the *mimeType* is invalid or when *input* is a `nullptr`. |





**Since:** Haiku R1

---

### `SetStopOnError()`

```cpp
void BPrivate::Network::BHttpRequest::SetStopOnError(bool stopOnError)
```

Set whether the entire response will be parsed on a client or server error. 


When the server encounters an error processing a request, it may respond with an error code. Error responses can be either an error with the request, like the 404 Not Found error, or errors on the server side, like a 500 Internal Server Error. Error responses may still have header fields and bodies.


If your application is not interested in the rest of the response in case a client error or a server error occurs, you can set this option to stop parsing. This will allow you to use the [BHttpResult](classBPrivate_1_1Network_1_1BHttpResult.md) object as normal, but the response fields will be empty, and there will be no body data.


Parameters

| Parameter | Description |
| :--- | :--- |
| `stopOnError` | Set to `true` to stop parsing the HTTP response when a client error or server error occurs. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | This exception may be raised if it is impossible to allocate memory. |





**Since:** Haiku R1

---

### `SetTimeout()`

```cpp
void BPrivate::Network::BHttpRequest::SetTimeout(bigtime_t timeout)
```

Set the maximum time waiting for the server to respond. 


If the request times out, then the response will hold the [BNetworkRequestError](classBPrivate_1_1Network_1_1BNetworkRequestError.md) of the `NetworkError` type. By default, the request does not time out.


Parameters

| Parameter | Description |
| :--- | :--- |
| `timeout` | The timeout in milliseconds. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | This exception may be raised if it is impossible to allocate memory. |





**Since:** Haiku R1

---

### `SetUrl()`

```cpp
void BPrivate::Network::BHttpRequest::SetUrl(const BUrl & url)
```

Set the *url* for this request. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `url` | A valid URL with the `http` or `https` protocol. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | This exception may be raised if it is impossible to allocate memory. |
| [BUnsupportedProtocol](classBPrivate_1_1Network_1_1BUnsupportedProtocol.md) | This exception is raised when the protocol of the URL cannot be handled. |
| [BInvalidUrl](classBPrivate_1_1Network_1_1BInvalidUrl.md) | This exception is raised when the *url* is invalid. |





**Since:** Haiku R1

---

### `StopOnError()`

```cpp
bool BPrivate::Network::BHttpRequest::StopOnError()const
```

Is the request set to parse the full response on error. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | When encountering a HTTP status of the client error class (4xx) or server error class (5xx), then the response will not be parsed. |
| false | The full response will be parsed, even with an error status code. |





**Since:** Haiku R1

---

### `Timeout()`

```cpp
bigtime_t BPrivate::Network::BHttpRequest::Timeout()const
```

Get the current timeout for the server to respond. 



**Since:** Haiku R1

---

### `Url()`

```cpp
const BUrl & BPrivate::Network::BHttpRequest::Url()const
```

Get the current Url for the request. 


This will either return the custom value set for this request, or the default as is listed in the overview documentation of this class.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BHttpRequest.html).
