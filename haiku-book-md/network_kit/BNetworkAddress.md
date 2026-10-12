---
name: BNetworkAddress
type: class
kit: network_kit
brief: "BNetworkAddress class represents a network address"
source: haiku-book
---

# BNetworkAddress Class
**Kit/Group:** [Network Kit](../network_kit/group__network.md)

## Description

[BNetworkAddress](classBNetworkAddress.md) class represents a network address. 


There are several ways to initialize a [BNetworkAddress](classBNetworkAddress.md) object, from any of the constructors with parameters or the [SetTo()](classBNetworkAddress.md#ac861599f4f3f0a3913382628384e59b8) methods. Depending on the overloaded version, the parameters could be:



* The *address*, that is the representation of a host's IP address (such as `"127.0.0.1"` or `"::1"`) or hostname (such as `"www.haiku-os.org"`).

* The *port*, a number representing the communication endpoint in the address, that identifies a specific process or application.

* The *service*, a string with a service name such as *"http"*, *"ftp"*, etc., that can be mapped to a port number and a protocol.

* The *family*, the address family identifier. A list of possible values is defined in POSIX header sys/socket.h.

* *flags* to pass to the address resolver: `0` (default value), `B_NO_ADDRESS_RESOLUTION` or `B_UNCONFIGURED_ADDRESS_FAMILIES`.



A [BNetworkAddress](classBNetworkAddress.md) object can also be initialized from a socket storage object (sockaddr, sockaddr_storage, sockaddr_in, sockaddr_in6 or sockaddr_dl), or from a raw IP address (in_addr_t for IPv4 or in6_addr for IPv6).



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BNetworkAddress](#a677e21546ba4116df28be6739029a332) () — Creates an uninitialized BNetworkAddress object.
* [BNetworkAddress](#a6b32b021b81f0d09dc7fe8f485c59c7d) (const BNetworkAddress &other) — Copy constructor.
* [BNetworkAddress](#a91ec0a3fa4d53e1bd09fc1892a91c2b9) (const char *address, const char *service, uint32 flags=0) — Creates and initializes a BNetworkAddress object using a network address and a service.
* [BNetworkAddress](#a49966752a8c140799bce549fcac2fa84) (const char *address, uint16 port=0, uint32 flags=0) — Creates and initializes a BNetworkAddress object using a network address and a port.
* [BNetworkAddress](#a14edd3911772415a84da21aac6d4cb6c) (const in6_addr &address, uint16 port=0) — Creates and initializes a BNetworkAddress object to a raw IPv6 address and a port.
* [BNetworkAddress](#a28de9a2e845f1477055bdfe6b2358c00) (const sockaddr &address) — Creates and initializes a BNetworkAddress object from a generic socket address storage object.
* [BNetworkAddress](#a9fe89dd05031365e5d3b79959e2decf0) (const sockaddr_dl &address) — Creates and initializes a BNetworkAddress object from a link level socket address storage object.
* [BNetworkAddress](#a302aad38827c81931dec88d8aed21457) (const sockaddr_in &address) — Creates and initializes a BNetworkAddress object from a IPv4 socket address storage object.
* [BNetworkAddress](#a80e9accca4aa2afca9fc1558f1859f35) (const sockaddr_in6 &address) — Creates and initializes a BNetworkAddress object from a IPv6 socket address storage object.
* [BNetworkAddress](#a0ea25f8c26181da9c8587e793fcf3493) (const sockaddr_storage &address) — Creates and initializes a BNetworkAddress object from a generic socket address storage object.
* [BNetworkAddress](#ac1f873e46aeb92c3ad1d8caccc23046f) (in_addr_t address, uint16 port=0) — Creates and initializes a BNetworkAddress object to a raw IPv4 address and a port.
* [BNetworkAddress](#a9fbee11f091fbaf6704a28bb670031c3) (int family, const char *address, const char *service, uint32 flags=0) — Creates and initializes a BNetworkAddress object using a network family, address and a service.
* [BNetworkAddress](#a5f14fd302a3d5cf2f15d2524251c69e1) (int family, const char *address, uint16 port=0, uint32 flags=0) — Creates and initializes a BNetworkAddress object using a network family, address and a port.
* `virtual` [~BNetworkAddress](#a87bad5ed0a854b32b5de92456c66a925) () — Default destructor.
* `status_t` [InitCheck](#a78844d3c7128a868c8710223728f3369) () const — Returns the initialization status of this object.
* `void` [Unset](#ab04b8cc643aea2e5747678a7ae387c2d) () — Uninitializes the BNetworkAddress object.
* `status_t` [SetTo](#ac861599f4f3f0a3913382628384e59b8) (const char *address, uint16 port=0, uint32 flags=0) — (Re)initializes the object using a network address and a port.
* `status_t` [SetTo](#a2e70e588a13839bd54aad2df14f1fa5e) (const char *address, const char *service, uint32 flags=0) — (Re)initializes the object using a network address and a service.
* `status_t` [SetTo](#aa18e9a3274605b4c4f81799c3b7e7d18) (int family, const char *address, uint16 port=0, uint32 flags=0) — (Re)initializes the object using a network family, address and a port.
* `status_t` [SetTo](#a74b1d350d1bc2348e9c7d34d7f6b1a7f) (int family, const char *address, const char *service, uint32 flags=0) — (Re)initializes the object using a network family, address and a service.
* `void` [SetTo](#a152a0c1abcf7f39c6bdb24f958b3de20) (const sockaddr &address) — (Re)initializes the object from a generic socket address storage object.
* `void` [SetTo](#ae29e30af20f1017a5463617cb9121c3e) (const sockaddr &address, size_t length) — (Re)initializes the object from a generic socket address storage object.
* `void` [SetTo](#ae05be3a797fea49b9ace69acfeee421b) (const sockaddr_storage &address) — (Re)initializes the object from a generic socket address storage object.
* `void` [SetTo](#a54b6f9bda609662f1176bc5821d22425) (const sockaddr_in &address) — (Re)initializes the object from a IPv4 socket address storage object.
* `void` [SetTo](#a6d1bcd2d603d3015257133979baf23dd) (const sockaddr_in6 &address) — (Re)initializes the object from a IPv6 socket address storage object.
* `void` [SetTo](#a9fb923a6a7ce478a5c36c38fae7b9a6e) (const sockaddr_dl &address) — (Re)initializes the object from a link level socket address storage object.
* `void` [SetTo](#ab651b97e1b549fddc28a9ffe3d18ac3a) (in_addr_t address, uint16 port=0) — (Re)initializes the object to a raw IPv4 address and a port.
* `void` [SetTo](#ace184eb512d89d1b833fdd04552bc3fd) (const in6_addr &address, uint16 port=0) — (Re)initializes the object to a raw IPv6 address and a port.
* `void` [SetTo](#a239592725aa308c2beac1e58cbdea302) (const BNetworkAddress &other) — (Re)initializes the object from other instance.
* `status_t` [SetToBroadcast](#ae2db03a01331c0cbc31c11820a8401c6) (int family, uint16 port=0) — (Re)initializes the object to the broadcast address.
* `status_t` [SetToLocal](#a28d6d88ea3dfc02d85c669623ff935a8) (int family=AF_UNSPEC, uint16 port=0) — Unimplemented.
* `status_t` [SetToLoopback](#ab04429f542391adc1a60b5a1c92d7f91) (int family=AF_UNSPEC, uint16 port=0) — (Re)initializes the object to the loopback address.
* `status_t` [SetToMask](#a7c8e4b3d06d509e94dd4b51c7eea165c) (int family, uint32 prefixLength) — (Re)initializes the object to a mask address depending on the address family loopback address, and prefixLength for the address prefix.
* `status_t` [SetToWildcard](#ab7fe7f4f5e7751c57cce99b2c846eb9b) (int family, uint16 port=0) — (Re)initializes the object to the wildcard address.
* `status_t` [SetAddress](#aeb026e23a7e907773396eb0848ff912b) (in_addr_t address) — Sets the address to a IPv4 address.
* `status_t` [SetAddress](#a370cbcf21aa8543774387619e3af86f7) (const in6_addr &address) — Sets the address to a IPv6 address.
* `void` [SetPort](#a30cb4d3dc21bdaf0088feb7b4a341f75) (uint16 port) — Changes the port number.
* `status_t` [SetPort](#a6d7d327179eb80a2cd13e042b3dd7849) (const char *service) — Unimplemented.
* `void` [SetToLinkLevel](#a34b2effbeafca42031f15e5b3554f1ed) (const uint8 *address, size_t length) — Sets the address to a link local address.
* `void` [SetToLinkLevel](#a76260c050113901377146d3e9f5676e7) (const char *name) — Sets the address to a link local address.
* `void` [SetToLinkLevel](#a0d1891112fd0db714b99a283a7603068) (uint32 index) — Sets the address to a link local address.
* `void` [SetLinkLevelIndex](#a46a9235763a584c9d610c7d9b10b5e05) (uint32 index) — Sets the link local address at index.
* `void` [SetLinkLevelType](#a18fc418803a34e14eb7b79c9448fb39a) (uint8 type) — Sets the link local address type.
* `void` [SetLinkLevelFrameType](#a17b6b52a85b4bdc2ddd78b2d1af2ede2) (uint16 frameType) — Sets the link local address frameType.
* `BNetworkAddress &` [operator=](#a51f26d22d0a64df15adcb9d27ca9af32) (const BNetworkAddress &other) — Copies other address onto this address object.
* `int` [Family](#a3b94d8011fc1d095f673eecdc4c14059) () const — Returns the address family.
* `uint16` [Port](#a04499b62dcf21444e4f025b4e15e49c7) () const — Returns the address port.
* `size_t` [Length](#acacd3674c541e36b1bb54817182ec986) () const — Returns the address length.
* `bool` [IsEmpty](#a00b27c4d19bcf713ba2566a984792c9c) () const — Returns whether the address is empty or not.
* `bool` [IsWildcard](#a531d18bd384b91ac46302bd03a74d80e) () const — Returns whether the address is a wildcard address or not.
* `bool` [IsBroadcast](#ae0e7512dabda3eb39967646450cf7371) () const — Returns whether the address is a broadcast address or not.
* `bool` [IsMulticast](#a3e362d289c9f89cf2b4a754280dd0719) () const — Returns whether the address is a multicast address or not.
* `bool` [IsMulticastGlobal](#a227f647041bb9dcb1e34dcbe69273dc8) () const — Returns whether the IPv6 multicast address is of global scope or not.
* `bool` [IsMulticastNodeLocal](#aa30da114b00db10ec89d6a722e91b4ae) () const — Returns whether the IPv6 multicast address is node local or not.
* `bool` [IsMulticastLinkLocal](#a32a84bd20a666a98389cba68504dfa71) () const — Returns whether the IPv6 multicast address is link local or not.
* `bool` [IsMulticastSiteLocal](#a9b3096542fde1c295120f404271f36f4) () const — Returns whether the IPv6 multicast address is site local or not.
* `bool` [IsMulticastOrgLocal](#ab02f43e288019390fa7539c6a7b49c2e) () const — Returns whether the IPv6 multicast address is organization local or not.
* `bool` [IsLinkLocal](#ab24fe010ad0123ebf544c2389d370bd0) () const — Returns whether the address is link local or not.
* `bool` [IsSiteLocal](#aa4952cfbbef26dd98c5d0e6382435061) () const — Returns whether the address is site local or not.
* `bool` [IsLocal](#a418351bfaa8eb232883af564260bae02) () const — Returns whether the address is local or not.
* `ssize_t` [PrefixLength](#af4aca1b46b2da7d6734e46f495d9878b) () const — Returns the prefix length for the subnet mask.
* `uint32` [LinkLevelIndex](#a421ecbe53fbcf0fcb4c631962827f3b7) () const — Returns the index of the network interface that the link local address belongs to.
* `BString` [LinkLevelInterface](#aaeee326c41bbeb6fd63e3579eeb838ea) () const — Returns the link local address' interface name.
* `uint8` [LinkLevelType](#a614fd37d7e6f8031bf3e1a9183b9bcee) () const — Returns the link local address' interface type.
* `uint16` [LinkLevelFrameType](#aed63975a7f1150a7abe92c0d8c8f5fb5) () const — Returns the link local address' frame type.
* `uint8 *` [LinkLevelAddress](#a4575081c326c1f7c867e13be76f7569e) () const — Returns a pointer to the link local address.
* `size_t` [LinkLevelAddressLength](#a54e8473dd9f65af56d804473217a43a3) () const — Returns the link local address length.
* `BString` [ToString](#abf4be3bde6a07194c2942b4bc9e19706) (bool includePort=true) const — Returns the network address in a stringified form.
* `BString` [HostName](#a31ec57cb84ab477f2fcb90e793a1e785) () const — Returns the host name for the network address.
* `BString` [ServiceName](#ac444f437717500f0756a2155d7d7364b) () const — Returns the port number for the current address.
* `const sockaddr &` [SockAddr](#aa3efd210bfb156db099e304cdcfca770) () const — Returns a read only reference to the underlying socket address.
* `sockaddr &` [SockAddr](#ae0f455424feb618cb61ea8d70076e2de) () — Returns a mutable reference to the underlying socket address.
* [operator const sockaddr *](#a2d67e079eccf2ecf28777dabae05a6e9) () const — Returns a read only pointer to the underlying socket address.
* [operator const sockaddr &](#a2804d9e1ed848a259fd5de607273e40e) () const — Returns a read only reference to the underlying socket address.
* [operator const sockaddr *](#ae76673f4f35bc5d95ca034c3d9c3d06e) () — Returns a read only pointer to the underlying socket address.
* [operator sockaddr *](#ae48a0e5347fb08a119095fb7fa33f847) () — Returns a mutable pointer to the underlying socket address.
* [operator const sockaddr &](#a828dbd7a9ec5613156cbd30096adbde4) () — Returns a read only reference to the underlying socket address.
* [operator sockaddr &](#aa23e5b89404e3b21106e693bc4c6936b) () — Returns a mutable reference to the underlying socket address.
* `status_t` [ResolveForDestination](#a45fc7c65f42d16a7cf816506d61bbb62) (const BNetworkAddress &destination) — For the given destination resolves the source address in the route and sets this object address to that source address.
* `status_t` [ResolveTo](#a7e0c7411e72c1ae2081a88b91138d9b8) (const BNetworkAddress &address) — Sets this object to address.
* `bool` [Equals](#a927a6e7539d1502048cab54f426dfd98) (const BNetworkAddress &other, bool includePort=true) const — Compares if this address is equal to other address.
* `bool` [operator==](#a93b39baca8aa5f28561e8ce18dc78380) (const BNetworkAddress &other) const — Compares if this address is equal to other address.
* `bool` [operator!=](#a957893152e452aae4df4cbfa5fc362ea) (const BNetworkAddress &other) const — Compares if this address is not equal to other address.
* `bool` [operator<](#a7ebbdf9d3a2738efb67881e534a1e4ea) (const BNetworkAddress &other) const — Compares if this address is less than other address.
* `virtual bool` [IsFixedSize](#acce52cf6caec21d846d9d188210d5f59) () const — Returnd whether or not BNetworkAddress flattened objects always have a fixed size.
* `virtual type_code` [TypeCode](#ad541b8571ed046f74556b23427867e7f) () const — Returns the type_code this class flattens to.
* `virtual ssize_t` [FlattenedSize](#ae7b6ebe7b9ac4eec5302fa7cb2892c8b) () const — Returns the size of the flattened object in bytes.
* `virtual status_t` [Flatten](#a83691ef631ad8a0dd4d047c00c00c61a) (void *buffer, ssize_t size) const — Flattens the object into the supplied buffer.
* `virtual status_t` [Unflatten](#a2430483749ce8c64600e8f5a6929f477) (type_code code, const void *buffer, ssize_t size) — Unflattens the buffer and puts the contents into the current object.
* `virtual` [~BFlattenable](#a884e130a5d27acc15b1e4e4c505157ff) () — Destructor. Does nothing.
* `virtual bool` [AllowsTypeCode](#a30165696bba76fed10e37508cc4f6925) (type_code code) const — Get whether or not the supplied type_code is supported.
* `virtual status_t` [Flatten](#ab934b64a8b218a4f9078ded191be6fbb) (void *buffer, ssize_t size) const =0 — Pure virtual that should flatten the object into the supplied buffer.
* `virtual ssize_t` [FlattenedSize](#a9b5885d4454326ca448438960ecff466) () const =0 — Pure virtual that should return the size of the flattened object in bytes.
* `virtual bool` [IsFixedSize](#ac019f502749a0cc78082f5ec7c8f5b56) () const =0 — Pure virtual that should return whether or not flattened objects of this type always have a fixed size.
* `virtual type_code` [TypeCode](#a819507fa1b0906f14299db15f6e990d1) () const =0 — Pure virtual that returns the type_code this class flattens to.
* `virtual status_t` [Unflatten](#a41e7168574912690be159991d2b07a97) (type_code code, const void *buffer, ssize_t size)=0 — Pure virtual that should unflatten the buffer and put the contents into the current object.

## Detailed Member Documentation

### `BNetworkAddress()`

```cpp
BNetworkAddress::BNetworkAddress()
```

Creates an uninitialized [BNetworkAddress](classBNetworkAddress.md) object. 


It can be later initialized with any of the [SetTo()](classBNetworkAddress.md#ac861599f4f3f0a3913382628384e59b8) functions.



**Since:** Haiku R1

---

### `BNetworkAddress()`

```cpp
BNetworkAddress::BNetworkAddress(const char * address, uint16 port = 0, uint32 flags = 0)
```

Creates and initializes a [BNetworkAddress](classBNetworkAddress.md) object using a network *address* and a *port*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | A network address. |
| `port` | The port in *address*. |
| `flags` | Configuration flags to pass to the address resolver. |





**See also:** [SetTo(const char*, uint16, uint32)](classBNetworkAddress.md#ac861599f4f3f0a3913382628384e59b8)



**Since:** Haiku R1

---

### `BNetworkAddress()`

```cpp
BNetworkAddress::BNetworkAddress(const char * address, const char * service, uint32 flags = 0)
```

Creates and initializes a [BNetworkAddress](classBNetworkAddress.md) object using a network *address* and a *service*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | A network address. |
| `service` | The service to be used. |
| `flags` | Configuration flags to pass to the address resolver. |





**See also:** [SetTo(const char*, const char*, uint32)](classBNetworkAddress.md#a2e70e588a13839bd54aad2df14f1fa5e)



**Since:** Haiku R1

---

### `BNetworkAddress()`

```cpp
BNetworkAddress::BNetworkAddress(int family, const char * address, uint16 port = 0, uint32 flags = 0)
```

Creates and initializes a [BNetworkAddress](classBNetworkAddress.md) object using a network *family*, *address* and a *port*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `family` | The address family identifier. |
| `address` | A network address. |
| `port` | The port in *address*. |
| `flags` | Configuration flags to pass to the address resolver. |





**See also:** [SetTo(int, const char*, uint16, uint32)](classBNetworkAddress.md#aa18e9a3274605b4c4f81799c3b7e7d18)



**Since:** Haiku R1

---

### `BNetworkAddress()`

```cpp
BNetworkAddress::BNetworkAddress(int family, const char * address, const char * service, uint32 flags = 0)
```

Creates and initializes a [BNetworkAddress](classBNetworkAddress.md) object using a network *family*, *address* and a *service*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `family` | The address family identifier. |
| `address` | A network address. |
| `service` | The service to be used. |
| `flags` | Configuration flags to pass to the address resolver. |





**See also:** [SetTo(int, const char*, const char*, uint32)](classBNetworkAddress.md#a74b1d350d1bc2348e9c7d34d7f6b1a7f)



**Since:** Haiku R1

---

### `BNetworkAddress()`

```cpp
BNetworkAddress::BNetworkAddress(const sockaddr & address)
```

Creates and initializes a [BNetworkAddress](classBNetworkAddress.md) object from a generic socket address storage object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | The sockaddr instance containing the socket address information. |





**See also:** [SetTo(const sockaddr&)](classBNetworkAddress.md#a152a0c1abcf7f39c6bdb24f958b3de20)



**Since:** Haiku R1

---

### `BNetworkAddress()`

```cpp
BNetworkAddress::BNetworkAddress(const sockaddr_storage & address)
```

Creates and initializes a [BNetworkAddress](classBNetworkAddress.md) object from a generic socket address storage object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | The sockaddr_storage instance containing the socket address information. |





**See also:** [SetTo(const sockaddr_storage&)](classBNetworkAddress.md#ae05be3a797fea49b9ace69acfeee421b)



**Since:** Haiku R1

---

### `BNetworkAddress()`

```cpp
BNetworkAddress::BNetworkAddress(const sockaddr_in & address)
```

Creates and initializes a [BNetworkAddress](classBNetworkAddress.md) object from a IPv4 socket address storage object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | The sockaddr_in instance containing the socket address information. |





**See also:** [SetTo(const sockaddr_in&)](classBNetworkAddress.md#a54b6f9bda609662f1176bc5821d22425)



**Since:** Haiku R1

---

### `BNetworkAddress()`

```cpp
BNetworkAddress::BNetworkAddress(const sockaddr_in6 & address)
```

Creates and initializes a [BNetworkAddress](classBNetworkAddress.md) object from a IPv6 socket address storage object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | The sockaddr_in6 instance containing the socket address information. |





**See also:** [SetTo(const sockaddr_in6&)](classBNetworkAddress.md#a6d1bcd2d603d3015257133979baf23dd)



**Since:** Haiku R1

---

### `BNetworkAddress()`

```cpp
BNetworkAddress::BNetworkAddress(const sockaddr_dl & address)
```

Creates and initializes a [BNetworkAddress](classBNetworkAddress.md) object from a link level socket address storage object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | The sockaddr_dl instance containing the socket address information. |





**See also:** [SetTo(const sockaddr_dl&)](classBNetworkAddress.md#a9fb923a6a7ce478a5c36c38fae7b9a6e)



**Since:** Haiku R1

---

### `BNetworkAddress()`

```cpp
BNetworkAddress::BNetworkAddress(in_addr_t address, uint16 port = 0)
```

Creates and initializes a [BNetworkAddress](classBNetworkAddress.md) object to a raw IPv4 *address* and a *port*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | A IPv4 address in 32-bit binary form. |
| `port` | The port number. |





**See also:** [SetTo(in_addr_t, uint16)](classBNetworkAddress.md#ab651b97e1b549fddc28a9ffe3d18ac3a)



**Since:** Haiku R1

---

### `BNetworkAddress()`

```cpp
BNetworkAddress::BNetworkAddress(const in6_addr & address, uint16 port = 0)
```

Creates and initializes a [BNetworkAddress](classBNetworkAddress.md) object to a raw IPv6 *address* and a *port*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | A IPv6 address in 128-bit binary form. |
| `port` | The port number. |





**See also:** [SetTo(const in6_addr&, uint16)](classBNetworkAddress.md#ace184eb512d89d1b833fdd04552bc3fd)



**Since:** Haiku R1

---

### `BNetworkAddress()`

```cpp
BNetworkAddress::BNetworkAddress(const BNetworkAddress & other)
```

Copy constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Another [BNetworkAddress](classBNetworkAddress.md) instance from where to initialize. |





**See also:** [SetTo(const BNetworkAddress&)](classBNetworkAddress.md#a239592725aa308c2beac1e58cbdea302)



**Since:** Haiku R1

---

### `~BNetworkAddress()`

```cpp
BNetworkAddress::~BNetworkAddress()
```

Default destructor. 



**Since:** Haiku R1

---

### `Equals()`

```cpp
bool BNetworkAddress::Equals(const BNetworkAddress & other, bool includePort = true)const
```

Compares if *this* address is equal to *other* address. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | *this* address is equal to *other* address. |
| false | *this* address is not equal to *other* address. |





**Since:** Haiku R1

---

### `Family()`

```cpp
int BNetworkAddress::Family()const
```

Returns the address family. 



**Since:** Haiku R1

---

### `Flatten()`

```cpp
status_t BNetworkAddress::Flatten(void * buffer, ssize_t size)const
```

Flattens the object into the supplied *buffer*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | The buffer to flatten in. |
| `size` | The size of the buffer. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object was flattened. |
| B_BAD_VALUE | The supplied buffer is `NULL` or the size is lesser than the required size in [FlattenedSize()](classBNetworkAddress.md#ae7b6ebe7b9ac4eec5302fa7cb2892c8b). |





**Since:** Haiku R1


Implements [BFlattenable](../support_kit/classBFlattenable.md#ab934b64a8b218a4f9078ded191be6fbb).

---

### `FlattenedSize()`

```cpp
ssize_t BNetworkAddress::FlattenedSize()const
```

Returns the size of the flattened object in bytes. 



**Since:** Haiku R1


Implements [BFlattenable](../support_kit/classBFlattenable.md#a9b5885d4454326ca448438960ecff466).

---

### `HostName()`

```cpp
BString BNetworkAddress::HostName()const
```

Returns the host name for the network address. 



**Since:** Haiku R1

---

### `InitCheck()`

```cpp
status_t BNetworkAddress::InitCheck()const
```

Returns the initialization status of this object. 


If [Unset()](classBNetworkAddress.md#ab04b8cc643aea2e5747678a7ae387c2d) is used, the initialization status turns into `B_OK`.



**Since:** Haiku R1

---

### `IsBroadcast()`

```cpp
bool BNetworkAddress::IsBroadcast()const
```

Returns whether the address is a broadcast address or not. 


This is valid only for `AF_INET` or `AF_INET6` address families. For other families it always returns `false`.


The broadcast address is `INADDR_BROADCAST` (`255.255.255.255`).



**Since:** Haiku R1

---

### `IsEmpty()`

```cpp
bool BNetworkAddress::IsEmpty()const
```

Returns whether the address is empty or not. 


If the address family is `AF_UNSPEC`, it is considered empty.



**Since:** Haiku R1

---

### `IsFixedSize()`

```cpp
bool BNetworkAddress::IsFixedSize()const
```

Returnd whether or not [BNetworkAddress](classBNetworkAddress.md) flattened objects always have a fixed size. 



**Returns:** It always returns `false`.



**Since:** Haiku R1


Implements [BFlattenable](../support_kit/classBFlattenable.md#ac019f502749a0cc78082f5ec7c8f5b56).

---

### `IsLinkLocal()`

```cpp
bool BNetworkAddress::IsLinkLocal()const
```

Returns whether the address is link local or not. 



**Since:** Haiku R1

---

### `IsLocal()`

```cpp
bool BNetworkAddress::IsLocal()const
```

Returns whether the address is local or not. 



**Since:** Haiku R1

---

### `IsMulticast()`

```cpp
bool BNetworkAddress::IsMulticast()const
```

Returns whether the address is a multicast address or not. 


This is valid only for `AF_INET` or `AF_INET6` address families. For other families it always returns `false`.



**Since:** Haiku R1

---

### `IsMulticastGlobal()`

```cpp
bool BNetworkAddress::IsMulticastGlobal()const
```

Returns whether the IPv6 multicast address is of global scope or not. 



**Since:** Haiku R1

---

### `IsMulticastLinkLocal()`

```cpp
bool BNetworkAddress::IsMulticastLinkLocal()const
```

Returns whether the IPv6 multicast address is link local or not. 



**Since:** Haiku R1

---

### `IsMulticastNodeLocal()`

```cpp
bool BNetworkAddress::IsMulticastNodeLocal()const
```

Returns whether the IPv6 multicast address is node local or not. 



**Since:** Haiku R1

---

### `IsMulticastOrgLocal()`

```cpp
bool BNetworkAddress::IsMulticastOrgLocal()const
```

Returns whether the IPv6 multicast address is organization local or not. 



**Since:** Haiku R1

---

### `IsMulticastSiteLocal()`

```cpp
bool BNetworkAddress::IsMulticastSiteLocal()const
```

Returns whether the IPv6 multicast address is site local or not. 



**Since:** Haiku R1

---

### `IsSiteLocal()`

```cpp
bool BNetworkAddress::IsSiteLocal()const
```

Returns whether the address is site local or not. 



**Since:** Haiku R1

---

### `IsWildcard()`

```cpp
bool BNetworkAddress::IsWildcard()const
```

Returns whether the address is a wildcard address or not. 


This is valid only for `AF_INET` or `AF_INET6` address families. For other families it always returns `false`.


For IPv4 addresses, the wildcard address is `INADDR_ANY` (`0.0.0.0`), and for IPv6 addresses is *in6addr_any* (`::`).



**Since:** Haiku R1

---

### `Length()`

```cpp
size_t BNetworkAddress::Length()const
```

Returns the address length. 



**Since:** Haiku R1

---

### `LinkLevelAddress()`

```cpp
uint8 * BNetworkAddress::LinkLevelAddress()const
```

Returns a pointer to the link local address. 



**Since:** Haiku R1

---

### `LinkLevelAddressLength()`

```cpp
size_t BNetworkAddress::LinkLevelAddressLength()const
```

Returns the link local address length. 



**Since:** Haiku R1

---

### `LinkLevelFrameType()`

```cpp
uint16 BNetworkAddress::LinkLevelFrameType()const
```

Returns the link local address' frame type. 



**Since:** Haiku R1

---

### `LinkLevelIndex()`

```cpp
uint32 BNetworkAddress::LinkLevelIndex()const
```

Returns the index of the network interface that the link local address belongs to. 



**Since:** Haiku R1

---

### `LinkLevelInterface()`

```cpp
BString BNetworkAddress::LinkLevelInterface()const
```

Returns the link local address' interface name. 



**Since:** Haiku R1

---

### `LinkLevelType()`

```cpp
uint8 BNetworkAddress::LinkLevelType()const
```

Returns the link local address' interface type. 



**Since:** Haiku R1

---

### `operator const sockaddr &()`

```cpp
BNetworkAddress::operator const sockaddr &()
```

Returns a read only reference to the underlying socket address. 



**Since:** Haiku R1

---

### `operator const sockaddr &()`

```cpp
BNetworkAddress::operator const sockaddr &()const
```

Returns a read only reference to the underlying socket address. 



**Since:** Haiku R1

---

### `operator const sockaddr *()`

```cpp
BNetworkAddress::operator const sockaddr *()
```

Returns a read only pointer to the underlying socket address. 



**Since:** Haiku R1

---

### `operator const sockaddr *()`

```cpp
BNetworkAddress::operator const sockaddr *()const
```

Returns a read only pointer to the underlying socket address. 



**Since:** Haiku R1

---

### `operator sockaddr &()`

```cpp
BNetworkAddress::operator sockaddr &()
```

Returns a mutable reference to the underlying socket address. 



**Since:** Haiku R1

---

### `operator sockaddr *()`

```cpp
BNetworkAddress::operator sockaddr *()
```

Returns a mutable pointer to the underlying socket address. 



**Since:** Haiku R1

---

### `operator!=()`

```cpp
bool BNetworkAddress::operator!=(const BNetworkAddress & other)const
```

Compares if *this* address is not equal to *other* address. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | *this* address is not equal to *other* address. |
| false | *this* address is equal to *other* address. |





**Since:** Haiku R1

---

### `operator<()`

```cpp
bool BNetworkAddress::operator<(const BNetworkAddress & other)const
```

Compares if *this* address is less than *other* address. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | *this* address is less than *other* address. |
| false | *this* address is equal to or greater than *other* address. |





**Since:** Haiku R1

---

### `operator=()`

```cpp
BNetworkAddress & BNetworkAddress::operator=(const BNetworkAddress & other)
```

Copies *other* address onto *this* address object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The other [BNetworkAddress](classBNetworkAddress.md) object from where to copy the data. |





**Since:** Haiku R1

---

### `operator==()`

```cpp
bool BNetworkAddress::operator==(const BNetworkAddress & other)const
```

Compares if *this* address is equal to *other* address. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | *this* address is equal to *other* address. |
| false | *this* address is not equal to *other* address. |





**Since:** Haiku R1

---

### `Port()`

```cpp
uint16 BNetworkAddress::Port()const
```

Returns the address port. 



**Since:** Haiku R1

---

### `PrefixLength()`

```cpp
ssize_t BNetworkAddress::PrefixLength()const
```

Returns the prefix length for the subnet mask. 



**Since:** Haiku R1

---

### `ResolveForDestination()`

```cpp
status_t BNetworkAddress::ResolveForDestination(const BNetworkAddress & destination)
```

For the given *destination* resolves the source address in the route and sets *this* object address to that source address. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `destination` | The destination address from where to resolve the source address. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Source address was resolved successfully. |
| B_BAD_VALUE | The destination address family is not the same as this address family. |





**Since:** Haiku R1

---

### `ResolveTo()`

```cpp
status_t BNetworkAddress::ResolveTo(const BNetworkAddress & address)
```

Sets this object to *address*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | The addres to be resolved. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_BAD_VALUE | The address family of *address* is not the same as this object's address family. |





**Since:** Haiku R1

---

### `ServiceName()`

```cpp
BString BNetworkAddress::ServiceName()const
```

Returns the port number for the current address. 



**Since:** Haiku R1

---

### `SetAddress()`

```cpp
status_t BNetworkAddress::SetAddress(const in6_addr & address)
```

Sets the address to a IPv6 *address*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | A IPv6 network address in 128-bit form. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_BAD_VALUE | The address family is not `AF_INET6`. |





**Since:** Haiku R1

---

### `SetAddress()`

```cpp
status_t BNetworkAddress::SetAddress(in_addr_t address)
```

Sets the address to a IPv4 *address*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | A IPv4 network address in 32-bit form. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_BAD_VALUE | The address family is not `AF_INET`. |





**Since:** Haiku R1

---

### `SetLinkLevelFrameType()`

```cpp
void BNetworkAddress::SetLinkLevelFrameType(uint16 frameType)
```

Sets the link local address *frameType*. 



**Since:** Haiku R1

---

### `SetLinkLevelIndex()`

```cpp
void BNetworkAddress::SetLinkLevelIndex(uint32 index)
```

Sets the link local address at *index*. 



**Since:** Haiku R1

---

### `SetLinkLevelType()`

```cpp
void BNetworkAddress::SetLinkLevelType(uint8 type)
```

Sets the link local address *type*. 



**Since:** Haiku R1

---

### `SetPort()`

```cpp
status_t BNetworkAddress::SetPort(const char * service)
```

Unimplemented. 



**Since:** Haiku R1

---

### `SetPort()`

```cpp
void BNetworkAddress::SetPort(uint16 port)
```

Changes the port number. 


This works only if the address family is `AF_INET` or `AF_INET6`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `port` | The port number. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
void BNetworkAddress::SetTo(const BNetworkAddress & other)
```

(Re)initializes the object from *other* instance. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Another [BNetworkAddress](classBNetworkAddress.md) instance from where to initialize. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BNetworkAddress::SetTo(const char * address, const char * service, uint32 flags = 0)
```

(Re)initializes the object using a network *address* and a *service*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | A network address. |
| `service` | The service to be used. |
| `flags` | Configuration flags to pass to the address resolver. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Initialization was successful. |
| B_ERROR | Unknown error. |
| B_NO_MEMORY | Internal memory allocation error. |
| B_BAD_VALUE | Address family not supported, unknown host or service, bad port number or socket type not supported. |
| B_TIMED_OUT | Temporary failure in name resolution. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BNetworkAddress::SetTo(const char * address, uint16 port = 0, uint32 flags = 0)
```

(Re)initializes the object using a network *address* and a *port*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | A network address. |
| `port` | The port in *address*. |
| `flags` | Configuration flags to pass to the address resolver. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Initialization was successful. |
| B_ERROR | Unknown error. |
| B_NO_MEMORY | Internal memory allocation error. |
| B_BAD_VALUE | Address family not supported, unknown host or service, bad port number or socket type not supported. |
| B_TIMED_OUT | Temporary failure in name resolution. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
void BNetworkAddress::SetTo(const in6_addr & address, uint16 port = 0)
```

(Re)initializes the object to a raw IPv6 *address* and a *port*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | The IPv6 address represented in binary form. |
| `port` | The port number. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
void BNetworkAddress::SetTo(const sockaddr & address)
```

(Re)initializes the object from a generic socket address storage object. 


It automatically casts the kind of socket according to the address family.


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | The sockaddr instance containing the socket address information. |





**See also:** [SetTo(const sockaddr&, size_t)](classBNetworkAddress.md#ae29e30af20f1017a5463617cb9121c3e)



**Since:** Haiku R1

---

### `SetTo()`

```cpp
void BNetworkAddress::SetTo(const sockaddr & address, size_t length)
```

(Re)initializes the object from a generic socket address storage object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | The sockaddr instance containing the socket address information. |
| `length` | The data length of *address*. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
void BNetworkAddress::SetTo(const sockaddr_dl & address)
```

(Re)initializes the object from a link level socket address storage object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | The sockaddr_dl instance containing the socket address information. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
void BNetworkAddress::SetTo(const sockaddr_in & address)
```

(Re)initializes the object from a IPv4 socket address storage object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | The sockaddr_in instance containing the socket address information. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
void BNetworkAddress::SetTo(const sockaddr_in6 & address)
```

(Re)initializes the object from a IPv6 socket address storage object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | The sockaddr_in6 instance containing the socket address information. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
void BNetworkAddress::SetTo(const sockaddr_storage & address)
```

(Re)initializes the object from a generic socket address storage object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | The sockaddr_storage instance containing the socket address information. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
void BNetworkAddress::SetTo(in_addr_t address, uint16 port = 0)
```

(Re)initializes the object to a raw IPv4 *address* and a *port*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | The IPv4 address represented with a 32-bit integer. |
| `port` | The port number. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BNetworkAddress::SetTo(int family, const char * address, const char * service, uint32 flags = 0)
```

(Re)initializes the object using a network *family*, *address* and a *service*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `family` | The address family identifier. |
| `address` | A network address. |
| `service` | The service to be used. |
| `flags` | Configuration flags to pass to the address resolver. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Initialization was successful. |
| B_ERROR | Unknown error. |
| B_NO_MEMORY | Internal memory allocation error. |
| B_BAD_VALUE | Address family not supported, unknown host or service, bad port number or socket type not supported. |
| B_TIMED_OUT | Temporary failure in name resolution. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BNetworkAddress::SetTo(int family, const char * address, uint16 port = 0, uint32 flags = 0)
```

(Re)initializes the object using a network *family*, *address* and a *port*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `family` | The address family identifier. |
| `address` | A network address. |
| `port` | The port in *address*. |
| `flags` | Configuration flags to pass to the address resolver. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Initialization was successful. |
| B_ERROR | Unknown error. |
| B_NO_MEMORY | Internal memory allocation error. |
| B_BAD_VALUE | Address family not supported, unknown host or service, bad port number or socket type not supported. |
| B_TIMED_OUT | Temporary failure in name resolution. |





**Since:** Haiku R1

---

### `SetToBroadcast()`

```cpp
status_t BNetworkAddress::SetToBroadcast(int family, uint16 port = 0)
```

(Re)initializes the object to the broadcast address. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `family` | The address family. |
| `port` | The port number. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_NOT_SUPPORTED | The address family is not `AF_INET`. |





**See also:** IsBroadCast()



**Since:** Haiku R1

---

### `SetToLinkLevel()`

```cpp
void BNetworkAddress::SetToLinkLevel(const char * name)
```

Sets the address to a link local address. 



**Since:** Haiku R1

---

### `SetToLinkLevel()`

```cpp
void BNetworkAddress::SetToLinkLevel(const uint8 * address, size_t length)
```

Sets the address to a link local address. 



**Since:** Haiku R1

---

### `SetToLinkLevel()`

```cpp
void BNetworkAddress::SetToLinkLevel(uint32 index)
```

Sets the address to a link local address. 



**Since:** Haiku R1

---

### `SetToLocal()`

```cpp
status_t BNetworkAddress::SetToLocal(int family = AF_UNSPEC, uint16 port = 0)
```

Unimplemented. 



**Since:** Haiku R1

---

### `SetToLoopback()`

```cpp
status_t BNetworkAddress::SetToLoopback(int family = AF_UNSPEC, uint16 port = 0)
```

(Re)initializes the object to the loopback address. 


The loopback address is `INADDR_LOOPBACK` (`127.0.0.1`) for the family `AF_INET`, or in6addr_loopback (`::1`) for the family `AF_INET6`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `family` | The address family. |
| `port` | The port number. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_NOT_SUPPORTED | The address family does not support loopback address. |





**Since:** Haiku R1

---

### `SetToMask()`

```cpp
status_t BNetworkAddress::SetToMask(int family, uint32 prefixLength)
```

(Re)initializes the object to a mask address depending on the address *family* loopback address, and *prefixLength* for the address prefix. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `family` | The address family. |
| `prefixLength` | The subnet prefix length. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_BAD_VALUE | *prefixLength* is greater than `32` if *family* is `AF_INET`, or greater than `128` if *family* is `AF_INET6`. |
| B_NOT_SUPPORTED | The address *family* does not support subnet masks (is not `AF_INET` nor `AF_INET6`). |





**Since:** Haiku R1

---

### `SetToWildcard()`

```cpp
status_t BNetworkAddress::SetToWildcard(int family, uint16 port = 0)
```

(Re)initializes the object to the wildcard address. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `family` | The family address. |
| `port` | The port number. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_NOT_SUPPORTED | The address *family* does not support wildcard addresses. |





**See also:** [IsWildcard()](classBNetworkAddress.md#a531d18bd384b91ac46302bd03a74d80e)



**Since:** Haiku R1

---

### `SockAddr()`

```cpp
sockaddr & BNetworkAddress::SockAddr()
```

Returns a mutable reference to the underlying socket address. 



**Since:** Haiku R1

---

### `SockAddr()`

```cpp
const sockaddr & BNetworkAddress::SockAddr()const
```

Returns a read only reference to the underlying socket address. 



**Since:** Haiku R1

---

### `ToString()`

```cpp
BString BNetworkAddress::ToString(bool includePort = true)const
```

Returns the network address in a stringified form. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `includePort` | If `true`, includes the port number in the output string. |





**Since:** Haiku R1

---

### `TypeCode()`

```cpp
type_code BNetworkAddress::TypeCode()const
```

Returns the type_code this class flattens to. 



**Returns:** The type code of this class `B_NETWORK_ADDRESS_TYPE`.



**Since:** Haiku R1


Implements [BFlattenable](../support_kit/classBFlattenable.md#a819507fa1b0906f14299db15f6e990d1).

---

### `Unflatten()`

```cpp
status_t BNetworkAddress::Unflatten(type_code code, const void * buffer, ssize_t size)
```

Unflattens the buffer and puts the contents into the current object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `code` | The type code of the data. |
| `buffer` | The buffer to unflatten the data from. |
| `size` | The size of the data. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The data was unflattened into this object. |
| B_BAD_TYPE | This class does not support the type *code*. |
| B_BAD_VALUE | The buffer is `NULL` or too small, or it contains an invalid address. |





**Since:** Haiku R1


Implements [BFlattenable](../support_kit/classBFlattenable.md#a41e7168574912690be159991d2b07a97).

---

### `Unset()`

```cpp
void BNetworkAddress::Unset()
```

Uninitializes the [BNetworkAddress](classBNetworkAddress.md) object. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBNetworkAddress.html).
