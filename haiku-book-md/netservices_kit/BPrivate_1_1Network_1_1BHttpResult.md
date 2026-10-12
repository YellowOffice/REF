---
name: BPrivate::Network::BHttpResult
type: class
kit: netservices_kit
brief: "Unique object to wait for and access a HTTP response data"
source: haiku-book
---

# BPrivate::Network::BHttpResult Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Unique object to wait for and access a HTTP response data. 


Once you have scheduled a HTTP request in a HTTP session, you will get an object of this type as a return value. This object allows you to track the progress of receiving the response, and to inspect the status, the headers and the data as the response is received from the server.


The object is a future type, meaning that eventually it will contain the data or an error. The [Status()](classBPrivate_1_1Network_1_1BHttpResult.md#a67e061b8e1c60b6b195c8a24f728c392), [Fields()](classBPrivate_1_1Network_1_1BHttpResult.md#a0193d68aed1470532a62d63476477972) and [Body()](classBPrivate_1_1Network_1_1BHttpResult.md#adeef8669a4d6f0fcbbbc2766072a8519) methods will yield the respective data. If it is not yet received, they will block until it is available. You can also use the non-blocking methods to check if data is available yet.


The result can either be a partial or completed HTTP Response, or an error. The partial aspect is represented by the fact that the status line, the fields and the body are loaded progressively and can be accessed as soon as they have been received. The meaning of a HTTP response is defined by the HTTP standards. For example, a GET request can return a response with a 200 status code, a set of headers and a body. But it can also return a 404 response, indicating that the resource was not found at the location. It is important to note that both responses are valid HTTP responses within the context of this API. This means that you can still use the access methods of this class to access data from the 404 response without raising an exception.


When there are errors during the request that lead to the situation where there is no valid response according to the HTTP specification, then this object goes into an error state. This means that the access methods of this object will throw an exception of the [BNetworkRequestError](classBPrivate_1_1Network_1_1BNetworkRequestError.md) type.


A special property of this object is that it is unique. This means it cannot be copied, only moved. Objects that have moved from, are in an invalid state, and will always raise a [BRuntimeError](classBPrivate_1_1Network_1_1BRuntimeError.md) exception when they are used.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BHttpResult](#ae7511645ad5e24dd69a857a95305d0a1) (const BHttpResult &other)=delete — Copy constructor is disabled.
* [BHttpResult](#abd0f5b0598998a80adb51a8b1a75699a) (BHttpResult &&other) noexcept — Move constructor.
* [~BHttpResult](#a872c3098ebe80c9e8f9f14bae954d840) () — Destructor.
* `BHttpResult &` [operator=](#a86e358e0586bab389c5bf1558a508b68) (const BHttpResult &other)=delete — Copy assignment is disabled.
* `BHttpResult &` [operator=](#ab7e4087ac2ff36f9d805e10bb1da51fd) (BHttpResult &&other) noexcept — Move operator.
* `const BHttpStatus &` [Status](#a67e061b8e1c60b6b195c8a24f728c392) () const — Retrieve the status line of the HTTP response.
* `const BHttpFields &` [Fields](#a0193d68aed1470532a62d63476477972) () const — Retrieve the header fields of the HTTP response.
* `BHttpBody &` [Body](#adeef8669a4d6f0fcbbbc2766072a8519) () const — Retrieve the body of the HTTP response.
* `bool` [HasStatus](#ae31cede2d4456b59a826d34960a6c536) () const — Check if the status is available.
* `bool` [HasFields](#ab5714b0675051500751ed2edad4445d6) () const — Check if the header fields are available.
* `bool` [HasBody](#a7a12921bb7c5f99de05e7d3819fcd05a) () const — Check if the body is available.
* `bool` [IsCompleted](#a258156ef5ffab1367eb616b2438c470d) () const — Check if the request is completed.
* `int32` [Identity](#a2136f32fa9d3efdd78ff6cc40e8c5821) () const — Unique identifier for the response.

## Detailed Member Documentation

### `BHttpResult()`

```cpp
BPrivate::Network::BHttpResult::BHttpResult(const BHttpResult & other)
```

Copy constructor is disabled. 


These objects cannot be copied.



**Since:** Haiku R1

---

### `BHttpResult()`

```cpp
BPrivate::Network::BHttpResult::BHttpResult(BHttpResult && other)
```

Move constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The object to move from. The *other* object will be in an invalid state and will always throw exceptions when it is used. |





**Since:** Haiku R1

---

### `~BHttpResult()`

```cpp
BPrivate::Network::BHttpResult::~BHttpResult()
```

Destructor. 



**Since:** Haiku R1

---

### `Body()`

```cpp
BHttpBody & BPrivate::Network::BHttpResult::Body()const
```

Retrieve the body of the HTTP response. 


If the body is not yet available, then this method call will block until it is. You can use the [HasBody()](classBPrivate_1_1Network_1_1BHttpResult.md#a7a12921bb7c5f99de05e7d3819fcd05a) method to do a non-blocking check if the status is available.


The lifetime of the body is tied to the lifetime of this response result object. If you want to keep the body beyond that time, you can copy or move the data from the [BHttpBody](structBPrivate_1_1Network_1_1BHttpBody.md) object.



**Returns:** A reference to the [BHttpBody](structBPrivate_1_1Network_1_1BHttpBody.md) object that contains the body.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| BRuntimeException | This exception is raised when the object has been moved from and is thus no longer valid. |
| [BNetworkRequestError](classBPrivate_1_1Network_1_1BNetworkRequestError.md) | This exception is raised when there was an error that prevented completely retrieving and parsing the HTTP response. |





**Since:** Haiku R1

---

### `Fields()`

```cpp
const BHttpFields & BPrivate::Network::BHttpResult::Fields()const
```

Retrieve the header fields of the HTTP response. 


If the header fields are not yet available, then this method call will block until it is. You can use the [HasFields()](classBPrivate_1_1Network_1_1BHttpResult.md#ab5714b0675051500751ed2edad4445d6) method to do a non-blocking check if the fields are available.



**Returns:** A const reference to the [BHttpFields](classBPrivate_1_1Network_1_1BHttpFields.md) object that describes the header fields of the response.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| BRuntimeException | This exception is raised when the object has been moved from and is thus no longer valid. |
| [BNetworkRequestError](classBPrivate_1_1Network_1_1BNetworkRequestError.md) | This exception is raised when there was an error that prevented completely retrieving and parsing the HTTP response. |





**Since:** Haiku R1

---

### `HasBody()`

```cpp
bool BPrivate::Network::BHttpResult::HasBody()const
```

Check if the body is available. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The body of the response is available using the [Body()](classBPrivate_1_1Network_1_1BHttpResult.md#adeef8669a4d6f0fcbbbc2766072a8519) method. |
| false | The body is not yet available. Any call to [Body()](classBPrivate_1_1Network_1_1BHttpResult.md#adeef8669a4d6f0fcbbbc2766072a8519) will block. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| BRuntimeException | This exception is raised when the object has been moved from and is thus no longer valid. |





**Since:** Haiku R1

---

### `HasFields()`

```cpp
bool BPrivate::Network::BHttpResult::HasFields()const
```

Check if the header fields are available. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The header fields of the response is available using the [Fields()](classBPrivate_1_1Network_1_1BHttpResult.md#a0193d68aed1470532a62d63476477972) method. |
| false | They are not yet available. Any call to [Fields()](classBPrivate_1_1Network_1_1BHttpResult.md#a0193d68aed1470532a62d63476477972) will block. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| BRuntimeException | This exception is raised when the object has been moved from and is thus no longer valid. |





**Since:** Haiku R1

---

### `HasStatus()`

```cpp
bool BPrivate::Network::BHttpResult::HasStatus()const
```

Check if the status is available. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The status line of the response is available using the [Status()](classBPrivate_1_1Network_1_1BHttpResult.md#a67e061b8e1c60b6b195c8a24f728c392) method. |
| false | The line is not yet available. Any call to [Status()](classBPrivate_1_1Network_1_1BHttpResult.md#a67e061b8e1c60b6b195c8a24f728c392) will block. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| BRuntimeException | This exception is raised when the object has been moved from and is thus no longer valid. |





**Since:** Haiku R1

---

### `Identity()`

```cpp
int32 BPrivate::Network::BHttpResult::Identity()const
```

Unique identifier for the response. 


The identifier can be used to cancel requests in a [BHttpSession](classBPrivate_1_1Network_1_1BHttpSession.md). It can also be uses to check incoming asynchronous event messages against the response.



**Returns:** A unique identifier that associates this response with an active or completed request.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| BRuntimeException | This exception is raised when the object has been moved from and is thus no longer valid. |





**Since:** Haiku R1

---

### `IsCompleted()`

```cpp
bool BPrivate::Network::BHttpResult::IsCompleted()const
```

Check if the request is completed. 


A request is completed when the status, headers and body have been received, or an error was raised while receiving the data.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| BRuntimeException | This exception is raised when the object has been moved from and is thus no longer valid. |





**Since:** Haiku R1

---

### `operator=()`

```cpp
BHttpResult & BPrivate::Network::BHttpResult::operator=(BHttpResult && other)
```

Move operator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The object to move from. The *other* object will be in an invalid state and will always throw exceptions when it is used. |





**Since:** Haiku R1

---

### `operator=()`

```cpp
BHttpResult & BPrivate::Network::BHttpResult::operator=(const BHttpResult & other)
```

Copy assignment is disabled. 


These objects cannot be copied.



**Since:** Haiku R1

---

### `Status()`

```cpp
const BHttpStatus & BPrivate::Network::BHttpResult::Status()const
```

Retrieve the status line of the HTTP response. 


If the status line is not yet available, then this method call will block until it is. You can use the [HasStatus()](classBPrivate_1_1Network_1_1BHttpResult.md#ae31cede2d4456b59a826d34960a6c536) method to do a non-blocking check if the status is available.



**Returns:** A const reference to the [BHttpStatus](structBPrivate_1_1Network_1_1BHttpStatus.md) object that describes the status of the response.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| BRuntimeException | This exception is raised when the object has been moved from and is thus no longer valid. |
| [BNetworkRequestError](classBPrivate_1_1Network_1_1BNetworkRequestError.md) | This exception is raised when there was an error that prevented completely retrieving and parsing the HTTP response. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BHttpResult.html).
