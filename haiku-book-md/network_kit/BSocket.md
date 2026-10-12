---
name: BSocket
type: class
kit: network_kit
brief: "BSocket is a class used to perform stream-based socket connections"
source: haiku-book
---

# BSocket Class
**Kit/Group:** [Network Kit](../network_kit/group__network.md)

## Description

[BSocket](classBSocket.md) is a class used to perform stream-based socket connections. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BSocket](#a2718874f83284dc0bf891c20efe1e8dd) () — Creates an uninitialized socket in disconnected and unbound state.
* [BSocket](#a710ce9d9e7480a84c4d81b2a4d4bdad5) (const BNetworkAddress &peer, bigtime_t timeout=B_INFINITE_TIMEOUT) — Creates a socket to peer and tries to connect to that endpoint until timeout is reached.
* [BSocket](#ad5c5728ffbb1b9cfc95ee7543cd58728) (const BSocket &other) — Copy constructor.
* `virtual` [~BSocket](#af0bdcc8c65418ea20ff836661b4bcc8c) () — Destructor.
* `virtual status_t` [Accept](#afb1513c9a99aa332890c93b16bcc5904) (BAbstractSocket *&_socket) — Accepts an incoming connection to this socket and initializes _socket to that remote endpoint.
* `virtual status_t` [Bind](#a75a596c2013198459411ca7470a7fe28) (const BNetworkAddress &peer, bool reuseAddr=true) — Assigns a local address peer to this socket.
* `virtual status_t` [Connect](#aef3f13db01648873c08be592b7551e72) (const BNetworkAddress &peer, bigtime_t timeout=B_INFINITE_TIMEOUT) — Connects the socket to the given peer.
* `virtual ssize_t` [Read](#a25f8738613bd62e582ca7cb83e6d1035) (void *buffer, size_t size) — Receives from the socket's peer and stores it in buffer.
* `virtual ssize_t` [Write](#a872e78ba97c25377c7804c72f2c0e396) (const void *buffer, size_t size) — Sends data from the socket to its peer.
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

### Additional Inherited Members

* `status_t` [Bind](#a1b4ea12b64505e5dbbc33628f8aa8ca1) (const BNetworkAddress &local, bool reuseAddr, int type) — binds the socket to the given address
* `status_t` [Connect](#a20f10d2f72c427132973bf813ec18092) (const BNetworkAddress &peer, int type, bigtime_t timeout=B_INFINITE_TIMEOUT) — Connect the socket to the given peer.

## Detailed Member Documentation

### `BSocket()`

```cpp
BSocket::BSocket()
```

Creates an uninitialized socket in disconnected and unbound state. 



**Since:** Haiku R1

---

### `BSocket()`

```cpp
BSocket::BSocket(const BNetworkAddress & peer, bigtime_t timeout = B_INFINITE_TIMEOUT)
```

Creates a socket to *peer* and tries to connect to that endpoint until *timeout* is reached. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `peer` | A network address. |
| `timeout` | The timeout in microseconds or `B_INFINITE_TIMEOUT`. This is used for subsequent reads and writes as well. |





**Since:** Haiku R1

---

### `BSocket()`

```cpp
BSocket::BSocket(const BSocket & other)
```

Copy constructor. 


The copied object accesses the same underlying socket.


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The other [BSocket](classBSocket.md) object. |





**Since:** Haiku R1

---

### `~BSocket()`

```cpp
BSocket::~BSocket()
```

Destructor. 


Disconnects the socket.



**Since:** Haiku R1

---

### `Accept()`

```cpp
status_t BSocket::Accept(BAbstractSocket *& _socket)
```

Accepts an incoming connection to this socket and initializes *_socket* to that remote endpoint. 


This method extracts the first connection from the pending incoming connections' queue and fills *_socket* with the peer's information.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The connection was accepted and the other object was initialized with the peer's information. |
| B_NO_MEMORY | Not enough memory to allocate for the other socket object. |
| -1 | Failure to accept the incoming connection. |





**Since:** Haiku R1


Implements [BAbstractSocket](classBAbstractSocket.md).


Reimplemented in [BSecureSocket](classBSecureSocket.md#ab6c1d05a192d08620771c85a8919f978).

---

### `Bind()`

```cpp
status_t BSocket::Bind(const BNetworkAddress & peer, bool reuseAddr = true)
```

Assigns a local address *peer* to this socket. 


If *reuseAddr* is `true`, it should allow the reuse of the local address.


If the binding is successful, the object is left in a bound state.


Parameters

| Parameter | Description |
| :--- | :--- |
| `peer` | The local address to be bound to this socket object. |
| `reuseAddr` | Whether the reuse of local addresses should be allowed in non-zero requests. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Binding was successful. |
| EADDRINUSE | The specified address is already in use and *reuseAddr* is false. |
| EADDRNOTAVAIL | The specified address is not available from the local machine. |
| EAFNOSUPPORT | The specified address is not of a family address accepted by the socket. |





**Since:** Haiku R1


Implements [BAbstractSocket](classBAbstractSocket.md).

---

### `Connect()`

```cpp
status_t BSocket::Connect(const BNetworkAddress & peer, bigtime_t timeout = B_INFINITE_TIMEOUT)
```

Connects the socket to the given *peer*. 


The socket is disconnected from any previous connections.


Parameters

| Parameter | Description |
| :--- | :--- |
| `peer` | The peer's address to connect to. |
| `timeout` | The timeout in microseconds or `B_INFINITE_TIMEOUT`. This is used for subsequent reads and writes as well. |





**Returns:** B_OK if the connection was performed successfully or an error code otherwise.



**Since:** Haiku R1


Implements [BAbstractSocket](classBAbstractSocket.md).


Reimplemented in [BProxySecureSocket](classBProxySecureSocket.md#a5b8e1f2e175cbb2c201a1fa922d45757), and [BSecureSocket](classBSecureSocket.md#a2c8a9ed54bce033660b7451f08c48617).

---

### `Read()`

```cpp
ssize_t BSocket::Read(void * buffer, size_t size)
```

Receives from the socket's peer and stores it in *buffer*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | A buffer where the data should be stored. |
| `size` | The length in bytes of the buffer. |





**Returns:** The length of bytes received, or an error code.



**Since:** Haiku R1


Reimplemented from [BDataIO](../support_kit/classBDataIO.md#a847ec8576c368bf9aada412e92aed623).


Reimplemented in [BSecureSocket](classBSecureSocket.md#a637c9bf1d12151a5541f9c7c1e4ea423).

---

### `Write()`

```cpp
ssize_t BSocket::Write(const void * buffer, size_t size)
```

Sends data from the socket to its peer. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | The data to be sent. |
| `size` | The length in bytes of the data. |





**Returns:** The length of bytes sent, or an error code.



**Since:** Haiku R1


Reimplemented from [BDataIO](../support_kit/classBDataIO.md#a01692303eba7601c6a7cfa72c06d6afb).


Reimplemented in [BSecureSocket](classBSecureSocket.md#a032f89a5521cdb79bdf002447d5f64ba).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBSocket.html).
