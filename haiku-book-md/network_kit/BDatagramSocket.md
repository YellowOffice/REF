---
name: BDatagramSocket
type: class
kit: network_kit
brief: "BAbstractSocket implementation for datagram connections"
source: haiku-book
---

# BDatagramSocket Class
**Kit/Group:** [Network Kit](../network_kit/group__network.md)

## Description

[BAbstractSocket](classBAbstractSocket.md) implementation for datagram connections. 


Datagrams are atomic messages. There is no notion of sequence and the data sent in a sequence of write calls may not get to the other end of the connections in the same order. There is no flow control, so some of them may not even make it to the peer. The most well known datagram protocol is UDP, which also happens to be the only one that Haiku currently supports.


The main uses for datagram sockets are when performance is more important than safety (the lack of acknowledge mechanism allows to send a lot of datagram packets at once, whereas TCP is limited by its sliding window mechanism), when the application wants to manage flow control and acknowledges itself (ie. when you want to implement your own protocol on top of UDP), and when lost packets don't matter (for example, in a video stream, there is no use for receiving late video frames if they were already skipped to play the following ones).


Since UDP is a connectionless protocol, in order to specify the target, or to be able to know from where you got a packet, this class provides you with the extra methods [SendTo()](classBDatagramSocket.md#abbab81c244f9e6fe3078e960750a13c7) and [ReceiveFrom()](classBDatagramSocket.md#ab63539aacc97082f7e036f135354ea96).

## Member List

### Public Member Functions

* [BDatagramSocket](#aff103fc27ec7e5e6c297834f51c22647) () — Default constructor.
* [BDatagramSocket](#BDatagramSocket) (const BDatagramSocket &other) — Copy constructor.
* [BDatagramSocket](#a4b0de32f12b5b4792351891c1efad563) (const BNetworkAddress &peer, bigtime_t timeout=-1) — Create and connect a datagram socket.
* `virtual` [~BDatagramSocket](#acd83cd922179997e11eeea350595abc3) () — Destructor.
* `virtual size_t` [MaxTransmissionSize](#a14121c4a20ea7583b5b29bcef28aeb26) () const
* `virtual ssize_t` [Read](#ac8d954e7e11eb2ef59d55b80a89e286c) (void *buffer, size_t size) — Receive a datagram from any sender.
* `virtual ssize_t` [ReceiveFrom](#ab63539aacc97082f7e036f135354ea96) (void *buffer, size_t bufferSize, BNetworkAddress &from) — receive a single datagram from a given host
* `virtual ssize_t` [SendTo](#abbab81c244f9e6fe3078e960750a13c7) (const BNetworkAddress &address, const void *buffer, size_t size) — Send a single datagram to the given address.
* `status_t` [SetBroadcast](#a66af2ddaeda1631dd384e1c677c3233a) (bool broadcast) — enables or disable broadcast mode
* `void` [SetPeer](#a9ffccacba93217a50f57772c7c9f755f) (const BNetworkAddress &peer) — Change the remote host for this connections.
* `virtual ssize_t` [Write](#a166e043d7e578825b4b36f069309d1df) (const void *buffer, size_t size) — Send a datagram to the default target.
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

### `BDatagramSocket()`

```cpp
BDatagramSocket::BDatagramSocket()
```

Default constructor. 


Does nothing. Call Bind() or Connect() to actually start network communications.



**See also:** [BAbstractSocket::BAbstractSocket()](classBAbstractSocket.md#aa0eff1ec277cbae66613975c3bb67da7).

---

### `BDatagramSocket()`

```cpp
BDatagramSocket::BDatagramSocket(const BNetworkAddress & peer, bigtime_t timeout = -1)
```

Create and connect a datagram socket. 


The socket is immediately connected to the given peer. Use [InitCheck()](classBAbstractSocket.md#af9d46dffaf8377e7235680873e82d66f) to make sure the connection was successful.


Parameters

| Parameter | Description |
| :--- | :--- |
| `peer` | host to connect to |
| `timeout` | connection timeout, in microsecond. |

---

### `~BDatagramSocket()`

```cpp
BDatagramSocket::~BDatagramSocket()
```

Destructor. 


The socket is disconnected.

---

### `MaxTransmissionSize()`

```cpp
size_t BDatagramSocket::MaxTransmissionSize()const
```

The maximum size for datagram sockets is 32768 bytes.



**Returns:** 32768


Reimplemented from [BAbstractSocket](classBAbstractSocket.md#aeb86b990a759fae1d7f15cb150510e2a).

---

### `Read()`

```cpp
ssize_t BDatagramSocket::Read(void * buffer, size_t size)
```

Receive a datagram from any sender. 


This is similar to [ReceiveFrom()](classBDatagramSocket.md#ab63539aacc97082f7e036f135354ea96), but there is no way to know who sent the message.


If the buffer is too small, the remaining part of the datagram is lost.


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | memory to store the datagram in |
| `size` | the size of the buffer |





**Returns:** the number of bytes actually written, or a negative error code.


Reimplemented from [BDataIO](../support_kit/classBDataIO.md#a847ec8576c368bf9aada412e92aed623).

---

### `ReceiveFrom()`

```cpp
ssize_t BDatagramSocket::ReceiveFrom(void * buffer, size_t bufferSize, BNetworkAddress & from)
```

receive a single datagram from a given host 


Receives a datagram, and fills the *from* address with the host that sent it. If the buffer is too small, extra bytes from the datagram will be lost.


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | the buffer to store the datagram in |
| `bufferSize` | size of the buffer |
| `from` | the datagram sender address |

---

### `SendTo()`

```cpp
ssize_t BDatagramSocket::SendTo(const BNetworkAddress & address, const void * buffer, size_t size)
```

Send a single datagram to the given address. 


Unlike the [Write()](classBDatagramSocket.md#a166e043d7e578825b4b36f069309d1df) method, which always sends to the same peer, this method can be used to send messages to different destinations.


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | the host to send the datagram to |
| `buffer` | datagram contents |
| `size` | size of the buffer |





**Returns:** the number of bytes sent, which may be less than requested, or a negative error code.

---

### `SetBroadcast()`

```cpp
BDatagramSocket::SetBroadcast(bool broadcast)
```

enables or disable broadcast mode 


In broadcast mode, datagrams can be sent to multiple peers at once. Calling this method is not enough, you must also set your peer address to be `INADDR_BROADCAST` to effectively send a broadcast message.


Note that broadcast messages usually don't propagate on Internet as they would generate too much traffic. Their use is thus restricted to local networks.


Parameters

| Parameter | Description |
| :--- | :--- |
| `broadcast` | the requested state for broadcast permissions. |





**Returns:** `B_OK` on success, or other error codes on failure.

---

### `SetPeer()`

```cpp
void BDatagramSocket::SetPeer(const BNetworkAddress & peer)
```

Change the remote host for this connections. 


Datagram connections are not statically bound to a remote address, so it is possible to change the destination of packets at runtime.


Note that packets coming to the right local address, no matter where they come from, will always be accepted.


Parameters

| Parameter | Description |
| :--- | :--- |
| `peer` | the address to which following Write calls will send datagrams |

---

### `Write()`

```cpp
ssize_t BDatagramSocket::Write(const void * buffer, size_t size)
```

Send a datagram to the default target. 


If the socket is connected, send a datagram to the connected host. If it's not, send to the peer given to the [SetPeer()](classBDatagramSocket.md#a9ffccacba93217a50f57772c7c9f755f) function.


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | the datagram to send |
| `size` | the size of the message |





**Returns:** the number of bytes written, which may be less than requested, or a negative error code.


Reimplemented from [BDataIO](../support_kit/classBDataIO.md#a01692303eba7601c6a7cfa72c06d6afb).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBDatagramSocket.html).
