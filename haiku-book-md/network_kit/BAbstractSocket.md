---
name: BAbstractSocket
type: class
kit: network_kit
brief: "Abstract interface for all socket connections"
source: haiku-book
---

# BAbstractSocket Class
**Kit/Group:** [Network Kit](../network_kit/group__network.md)

## Description

Abstract interface for all socket connections. 


[BAbstractSocket](classBAbstractSocket.md) provides a common interface for all socket-based communication streams. These include [BDatagramSocket](classBDatagramSocket.md), [BSocket](classBSocket.md), [BSecureSocket](classBSecureSocket.md) and [BProxySecureSocket](classBProxySecureSocket.md).


[BAbstractSocket](classBAbstractSocket.md) implements common behavior between these different socket types. This includes management of a BSD socket integer handle, knowledge of the local and remote network addresses, as well as the connection state.

## Member List

### Public Member Functions

* [BAbstractSocket](#aa0eff1ec277cbae66613975c3bb67da7) () — Default constructor.
* [BAbstractSocket](#adad46cb8129dad3066d464e34320211f) (const BAbstractSocket &other) — Copy constructor.
* `virtual` [~BAbstractSocket](#a8813b61b49c1a409fc64d85e155f77fc) () — Destructor.
* `virtual void` [Disconnect](#aa10aba8e260b4051c1ed381aee6f0fb9) () — Close the connection.
* `status_t` [InitCheck](#af9d46dffaf8377e7235680873e82d66f) () const — Check connection status.
* `virtual bool` [IsBound](#ac645bece7a4d03ea21988243ba169c02) () const
* `virtual bool` [IsConnected](#adc36a9456fed2b132630b2411b58e81b) () const
* `virtual const BNetworkAddress &` [Local](#a958ca85bdfcfe2b4414ef1e03efa86ce) () const — gets the local address for this socket
* `virtual size_t` [MaxTransmissionSize](#aeb86b990a759fae1d7f15cb150510e2a) () const — Return the maximal size of a transmission on this socket.
* `virtual const BNetworkAddress &` [Peer](#a26c3225da767963450b74be2b46d515c) () const — gets the peer address
* `virtual status_t` [SetTimeout](#aadd29c12de2b666f398d8605b7b72c8e) (bigtime_t timeout) — sets the read and write timeout
* `int` [Socket](#a6994fc974cf477aaff8728931302e395) () const — get the underlying socket descriptor
* `virtual bigtime_t` [Timeout](#a5f014ac80e2457bcb931c9b5a20dae05) () const — gets the socket timeout
* `virtual status_t` [WaitForReadable](#a174391627c31e9789ebe9f74719b837a) (bigtime_t timeout=B_INFINITE_TIMEOUT) const — wait for incoming data
* `virtual status_t` [WaitForWritable](#a66a1117d00833276e19ac9f8e5950c30) (bigtime_t timeout=B_INFINITE_TIMEOUT) const — wait until writing is possible
* [BDataIO](#a67891b7afe78d6a77845dd0352218801) () — This constructor does nothing.
* `virtual` [~BDataIO](#a45daa9db670dd2e5b83efcefcf8dbaed) () — This destructor does nothing.
* `virtual status_t` [Flush](#a38a8df63b367585fe5e6b6a85c406d05) () — Writes pending data to underlying storage.
* `virtual ssize_t` [Read](#a847ec8576c368bf9aada412e92aed623) (void *buffer, size_t size) — Reads data from the object into a buffer.
* `status_t` [ReadExactly](#a3a0b0fc36232531a1d8c1144a7d75741) (void *buffer, size_t size, size_t *_bytesRead=NULL) — Reads an exact amount of data from the object into a buffer.
* `virtual ssize_t` [Write](#a01692303eba7601c6a7cfa72c06d6afb) (const void *buffer, size_t size) — Writes data from a buffer to the object.
* `status_t` [WriteExactly](#a0095cfffa454a82eac3dedda2e187ab7) (const void *buffer, size_t size, size_t *_bytesWritten=NULL) — Writes an exact amount of data from a buffer to the object.

### Protected Member Functions

* `status_t` [Bind](#a1b4ea12b64505e5dbbc33628f8aa8ca1) (const BNetworkAddress &local, bool reuseAddr, int type) — binds the socket to the given address
* `status_t` [Connect](#a20f10d2f72c427132973bf813ec18092) (const BNetworkAddress &peer, int type, bigtime_t timeout=B_INFINITE_TIMEOUT) — Connect the socket to the given peer.

## Detailed Member Documentation

### `BAbstractSocket()`

```cpp
BAbstractSocket::BAbstractSocket()
```

Default constructor. 


Creates an uninitialized socket in disconnected and unbound state.

---

### `BAbstractSocket()`

```cpp
BAbstractSocket::BAbstractSocket(const BAbstractSocket & other)
```

Copy constructor. 


The copied object accesses the same underlying socket.

---

### `~BAbstractSocket()`

```cpp
BAbstractSocket::~BAbstractSocket()
```

Destructor.

---

### `Bind()`

```cpp
status_t BAbstractSocket::Bind(const BNetworkAddress & local, bool reuseAddr, int type)
```

binds the socket to the given address 


If the socket was already bound, the previous binding is removed.


Parameters

| Parameter | Description |
| :--- | :--- |
| `local` | the local address to bind |
| `reuseAddr` | if `true`, non-zero requests reuse *local* address |
| `type` | the socket type |





**Returns:** B_OK on success, other error codes on error.

---

### `Connect()`

```cpp
status_t BAbstractSocket::Connect(const BNetworkAddress & peer, int type, bigtime_t timeout = B_INFINITE_TIMEOUT)
```

Connect the socket to the given peer. 


The socket is disconnected from any previous connections.


Parameters

| Parameter | Description |
| :--- | :--- |
| `peer` | the peer to connect to |
| `type` | the socket type |
| `timeout` | The timeout in microseconds or B_INFINITE_TIMEOUT. This is used for subsequent reads and writes as well. |

---

### `Disconnect()`

```cpp
void BAbstractSocket::Disconnect()
```

Close the connection. 


The socket becomes disconnected and unbound. You can Connect or Bind it again, either to the same or another peer. 


Reimplemented in [BSecureSocket](classBSecureSocket.md#aa19904aaffa4f465d3431004b420d901).

---

### `InitCheck()`

```cpp
status_t BAbstractSocket::InitCheck()const
```

Check connection status. 



**Returns:** B_OK if the connection is working, or an error code if something went wrong.

---

### `IsBound()`

```cpp
bool BAbstractSocket::IsBound()const
```

A socket becomes bound when Bind succeeds, and stops being bound when Disconnect is called.



**Returns:** wether the socket is currently bound

---

### `IsConnected()`

```cpp
bool BAbstractSocket::IsConnected()const
```

A socket becomes connected when Connect succeeds, and disconnected when Disconnect is called.



**Returns:** wether the socket is currently connected

---

### `Local()`

```cpp
const BNetworkAddress & BAbstractSocket::Local()const
```

gets the local address for this socket 


This gives useful results only if the socket is either connected or bound. Otherwise, an uninitialized address is returned.

---

### `MaxTransmissionSize()`

```cpp
size_t BAbstractSocket::MaxTransmissionSize()const
```

Return the maximal size of a transmission on this socket. 


The default implementation always returns SSIZE_MAX, but subclasses may restrict this to a smaller size. 


Reimplemented in [BDatagramSocket](classBDatagramSocket.md#a14121c4a20ea7583b5b29bcef28aeb26).

---

### `Peer()`

```cpp
const BNetworkAddress & BAbstractSocket::Peer()const
```

gets the peer address 


This gives useful results only if the socket is either connected or bound. Otherwise, an uninitialized address is returned.

---

### `SetTimeout()`

```cpp
status_t BAbstractSocket::SetTimeout(bigtime_t timeout)
```

sets the read and write timeout 


A negative value disables timeouts, so the Read and Write calls will wait until data is available or can be sent.


Parameters

| Parameter | Description |
| :--- | :--- |
| `timeout` | The timeout in microseconds, or B_INFINITE_TIMEOUT. |

---

### `Socket()`

```cpp
int BAbstractSocket::Socket()const
```

get the underlying socket descriptor 


The BSD socket descriptor can be used to modify advanced connection paramters using the POSIX socket API.



**Returns:** the socket descriptor

---

### `Timeout()`

```cpp
bigtime_t BAbstractSocket::Timeout()const
```

gets the socket timeout 



**Returns:** the timeout in microseconds, or B_INFINITE_TIMEOUT

---

### `WaitForReadable()`

```cpp
status_t BAbstractSocket::WaitForReadable(bigtime_t timeout = B_INFINITE_TIMEOUT)const
```

wait for incoming data 


Wait until data comes in, or the timeout expires. After this function returns B_OK, Read can be called without blocking.


Parameters

| Parameter | Description |
| :--- | :--- |
| `timeout` | the timeout in microseconds, or B_INFINITE_TIMEOUT |





**Returns:** B_OK when data is available, B_TIMED_OUT when the timeout expires, or B_WOULD_BLOCK when the wait was interrupted for other reasons.


Reimplemented in [BSecureSocket](classBSecureSocket.md#aace1524545debf62b3d60c2f9edd1493).

---

### `WaitForWritable()`

```cpp
status_t BAbstractSocket::WaitForWritable(bigtime_t timeout = B_INFINITE_TIMEOUT)const
```

wait until writing is possible 


Wait until the socket becomes ready for writing, or the timeout expires. After this function returns B_OK, Write can be called without blocking.


Parameters

| Parameter | Description |
| :--- | :--- |
| `timeout` | the timeout in microseconds, or B_INFINITE_TIMEOUT |





**Returns:** B_OK when the socket is ready to accept writes, B_TIMED_OUT when the timeout expires, or B_WOULD_BLOCK when the wait was interrupted for another reason.

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBAbstractSocket.html).
