---
name: BPrivate::Network::BHttpSession
type: class
kit: netservices_kit
brief: "Schedule, execute and manage HTTP requests"
source: haiku-book
---

# BPrivate::Network::BHttpSession Class
**Kit/Group:** [Experimental Network Services Support](../netservices_kit/group__netservices.md)

## Description

Schedule, execute and manage HTTP requests. 


All requests start from a `BHttpSession`. This class has the following jobs:


* Store data used between various HTTP calls
* Proxies

* Cookies

* Additional SSL certificates

* Authentication Data

* Manage the scheduling and execution of HTTP requests.



Objects of the `BHttpSession` class can be shared between different parts of the application. They should be copied, rather than shared using pointers. This is because they have an inner state that is shared between the various objects.



```cpp
// Creating and sharing a session
auto session = BHttpSession();
 
// A copy is passed to window1 and window2, which share the same session data
auto window1 = new WindowWithSession(session);
auto window2 = new WindowWithSession(session);
 
// Add a cookie to the session, this cookie will be used in window1 and window2
BNetworkCookie cookie("key", "value", BUrl("https://example.com/"));
session.AddCookie(std::move(cookie));
 
// The session data persists, even if the original session goes out of scope
```

There are specific scenarios for having more than one session, most notably if an application provides services over HTTP whereby a user is identified by cookies, and the application wants to support more than one user account. But in most cases, there will be one instance of the [BHttpSession](classBPrivate_1_1Network_1_1BHttpSession.md) that is shared between various segments of the application.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BHttpSession](#a3985a2419f61d848d76cc091414f72da) () — Construct a new object.
* [BHttpSession](#afefa20d6a6b0ef89dc9bd091ad3c02c8) (BHttpSession &&) noexcept=delete — Move is disabled.
* [BHttpSession](#ac0e71239d098a1088b7362b705918f81) (const BHttpSession &) noexcept — Create a new BHttpSession object that shares a state with another.
* [~BHttpSession](#a7b11bb0aa92564bdea568757395ccbbf) () noexcept — Destructor.
* `void` [Cancel](#a4eff1630ceb2d7f22654dd8bbe9a5c10) (const BHttpResult &request) — Cancel a running request.
* `void` [Cancel](#accde0fa55308b63b41e661df47b423da) (int32 identifier) — Cancel a running request.
* `BHttpResult` [Execute](#ae14a7c52aaddfd69e22be4a8aeff727f) (BHttpRequest &&request, BBorrow< BDataIO > target=nullptr, BMessenger observer=BMessenger()) — Schedule and execute a request.
* `BHttpSession &` [operator=](#a9b44dbc7966ed58ad903768e13b37c55) (BHttpSession &&) noexcept=delete — Move is disabled.
* `BHttpSession &` [operator=](#a096712cf5ee1b7b4f3d752030d9bfd42) (const BHttpSession &) noexcept — Copy and use the shared state from another session.
* `void` [SetMaxConnectionsPerHost](#a24751671e7b5665d62241d3f968f9098) (size_t maxConnections) — Set the maximum number of connections per host.
* `void` [SetMaxHosts](#a46fbd98c452c1d3b97db93b8ddff81f6) (size_t maxConnections) — Set the maximum number of concurrent hosts that can be connected to.

## Detailed Member Documentation

### `BHttpSession()`

```cpp
BPrivate::Network::BHttpSession::BHttpSession()
```

Construct a new object. 


Each newly constructed object will have their own queue for HTTP requests, as well as their own cookies and certificate store.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | Unable to allocate resources for the object. |
| [BRuntimeError](classBPrivate_1_1Network_1_1BRuntimeError.md) | Unable to create semaphores or threads. |





**Since:** Haiku R1

---

### `BHttpSession()`

```cpp
BPrivate::Network::BHttpSession::BHttpSession(const BHttpSession &)
```

Create a new [BHttpSession](classBPrivate_1_1Network_1_1BHttpSession.md) object that shares a state with another. 


The internal HTTP queue and context can be shared among multiple objects. You can use the copy constructor to create a new object.



**Since:** Haiku R1

---

### `BHttpSession()`

```cpp
BPrivate::Network::BHttpSession::BHttpSession(BHttpSession &&)
```

Move is disabled. 


[BHttpSession](classBPrivate_1_1Network_1_1BHttpSession.md) objects cannot be moved. Because it has a shared internal state, making copies is cheap and it is the only supported method of creating multiple scoped objects with a shared lifetime.



**Since:** Haiku R1

---

### `~BHttpSession()`

```cpp
BPrivate::Network::BHttpSession::~BHttpSession()
```

Destructor. 


The destructor releases the shared internal state of the session object. If there are no more sessions using the shared state, the state is cleaned up.



**Since:** Haiku R1

---

### `Cancel()`

```cpp
void BPrivate::Network::BHttpSession::Cancel(const BHttpResult & request)
```

Cancel a running *request*. 


See the [BHttpSession::Cancel(int32 identifier)](classBPrivate_1_1Network_1_1BHttpSession.md#accde0fa55308b63b41e661df47b423da) method for more details on how this method works.


Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | Error in case memory cannot be allocated. |





**Since:** Haiku R1

---

### `Cancel()`

```cpp
void BPrivate::Network::BHttpSession::Cancel(int32 identifier)
```

Cancel a running request. 


When a request that is scheduled or running is cancelled, its [BHttpResult](classBPrivate_1_1Network_1_1BHttpResult.md) object will be set to the [BNetworkRequestError](classBPrivate_1_1Network_1_1BNetworkRequestError.md) exception with the `Cancelled` type.


There are three possible outcomes: 1. If the request is not yet scheduled, then it will never start. The result will be set to the cancelled error state. 2. If the request was started, then processing it will be terminated. The result will be set to the cancelled error state. 3. If the request was already finished, then nothing happens. The result will keep the value it had assigned. The same if the request identifier is invalid.


Parameters

| Parameter | Description |
| :--- | :--- |
| `identifier` | The identifier for the request to cancel. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| std::bad_alloc | Error in case memory cannot be allocated. |





**Since:** Haiku R1

---

### `Execute()`

```cpp
BHttpResult BPrivate::Network::BHttpSession::Execute(BHttpRequest && request, BBorrow< BDataIO > target = nullptr, BMessenger observer = BMessenger())
```

Schedule and execute a *request*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `request` | The (valid) request to move from. |
| `target` | An optional data buffer to write the incoming body of the request to. This can be `nullptr` if you want to use the default internal storage. If you provide a buffer, it must be wrapped in a [BBorrow](classBPrivate_1_1Network_1_1BBorrow.md) object. This means that you exclusively borrow the target to this session object. After the request is finished, you can regain usage of the object through the matching [BExclusiveBorrow](classBPrivate_1_1Network_1_1BExclusiveBorrow.md) object. Use the [BHttpResult::Body()](classBPrivate_1_1Network_1_1BHttpResult.md#adeef8669a4d6f0fcbbbc2766072a8519) method to synchronize when the target is available again. |
| `observer` | An optional observer that will receive the progress and status messages for this request. |





**Returns:** The [BHttpResult](classBPrivate_1_1Network_1_1BHttpResult.md) object that corresponds to this request, and that can be used to monitor the progress.



**Since:** Haiku R1

---

### `operator=()`

```cpp
BHttpSession & BPrivate::Network::BHttpSession::operator=(BHttpSession &&)
```

Move is disabled. 


[BHttpSession](classBPrivate_1_1Network_1_1BHttpSession.md) objects cannot be moved. Because it has a shared internal state, making copies is cheap and it is the only supported method of creating multiple scoped objects with a shared lifetime.



**Since:** Haiku R1

---

### `operator=()`

```cpp
BHttpSession & BPrivate::Network::BHttpSession::operator=(const BHttpSession &)
```

Copy and use the shared state from another session. 


The internal HTTP queue and context can be shared among multiple objects. You can use the copy constructor to create a new copy.


This copy assignment operator should be used in very specific instances only, where there is a particular reason to replace an existing session internal session with another. It should not be used in the following case:



```cpp
// Bad example
BHttpSession session1 = BHttpSession();
 // Creates a new session, including an entirely new (expensive) state
BHttpSession session2 = BHttpSession();
 // Creates another new session, including internal state
session2 = session1;
 // At this stage, the internal state of session2 would
 // have to be cleaned up just after it was created.
 
// Instead do this
BHttpSession session1 = BHttpSession();
BHttpSession session2(session1);
 // Now session2 directly shares the state with session 1
```


**Since:** Haiku R1

---

### `SetMaxConnectionsPerHost()`

```cpp
void BPrivate::Network::BHttpSession::SetMaxConnectionsPerHost(size_t maxConnections)
```

Set the maximum number of connections per host. 


A host is identified by the domain name and the port. You can limit the number of concurrent connections to a host by tweaking this value.


The default value is 2 connections per host.


If the value is decreased, any requests that already started will not be affected. The new value will only be applied when any new requests are added.


Parameters

| Parameter | Description |
| :--- | :--- |
| `maxConnections` | The maximum number of connections per host. This value must between 1 and `INT32_MAX`. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| [BRuntimeError](classBPrivate_1_1Network_1_1BRuntimeError.md) | In case the *maxConnections* is invalid. |





**Since:** Haiku R1

---

### `SetMaxHosts()`

```cpp
void BPrivate::Network::BHttpSession::SetMaxHosts(size_t maxConnections)
```

Set the maximum number of concurrent hosts that can be connected to. 


A host is identified by the domain name and the port. You can limit the number of concurrent hosts by tweaking this value.


The default value is 10 concurrent hosts.


If the value is decreased, any requests that already started will not be affected. The new value will only be applied when any new requests are added.


Parameters

| Parameter | Description |
| :--- | :--- |
| `maxConnections` | The maximum number of hosts. The value must be at least 1. |




Exceptions

| Col 1 | Col 2 |
| :--- | :--- |
| [BRuntimeError](classBPrivate_1_1Network_1_1BRuntimeError.md) | In case the *maxConnections* is 0. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBPrivate_1_1Network_1_1BHttpSession.html).
