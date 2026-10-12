---
name: BNetworkRoute
type: class
kit: network_kit
brief: "BNetworkRoute class represents a network route, a path for traffic across one or multiple networks"
source: haiku-book
---

# BNetworkRoute Class
**Kit/Group:** [Network Kit](../network_kit/group__network.md)

## Description

[BNetworkRoute](classBNetworkRoute.md) class represents a network route, a path for traffic across one or multiple networks. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BNetworkRoute](#a8a2c3577527d90e638571ef2f8ad397f) () — Creates an uninitialized BNetworkRoute object.
* [~BNetworkRoute](#ae8ac421de4f6f76a0eb9881bc482194b) () — Releases all the allocated resources.
* `int` [AddressFamily](#aa3b3273c70a8dc1cee1199377d40e13e) () const — Returns the route's address family.
* `void` [Adopt](#a4afac38d940880fe89fd7e18a1c02aa9) (BNetworkRoute &other) — Moves other to this instance.
* `const sockaddr *` [Destination](#a5de16a467e50d653abdd5e4188359328) () const — Returns the destination address.
* `uint32` [Flags](#a4752a0c562b71db1f97958d711ddebfb) () const — Returns the route's flags mask.
* `const sockaddr *` [Gateway](#a8cdba30c96a5308f57c0a83ea56b9d6d) () const — Returns the gateway address.
* `const sockaddr *` [Mask](#af0bd1123d16bd70dc301496de992a6ce) () const — Returns the subnet mask address.
* `uint32` [MTU](#a71e6676334a0ac81d121f4db35d955f1) () const — Returns the maximum transmission unit size of the route.
* `const route_entry &` [RouteEntry](#a7c6ab519083d566ea3bf95f0495c92da) () const — Returns a copy of the route_entry with routing information of this object.
* `status_t` [SetDestination](#ae5bda255a99a927537cc9e6d55d1b323) (const sockaddr &destination) — Sets the destination address.
* `void` [SetFlags](#a25bc3f13c9c62e74ddc7cc08503baf19) (uint32 flags) — Sets the route's flags mask.
* `status_t` [SetGateway](#ab91386fe496161da8218c4c4df628fed) (const sockaddr &gateway) — Sets the gateway address.
* `status_t` [SetMask](#ae8bdbf271077c5cef90b108fe8f9a5f5) (const sockaddr &mask) — Sets the subnet mask address.
* `void` [SetMTU](#a66f9913555f04cbb466f66d86418a760) (uint32 mtu) — Sets the maximum transmission unit size of the route.
* `status_t` [SetSource](#aedabfdeafb5c9891dcd008d49fa7493c) (const sockaddr &source) — Sets the source address.
* `status_t` [SetTo](#a245b7e361a94e27173cd0d862de8fd0a) (const BNetworkRoute &other) — Initializes this object from other BNetworkRoute object.
* `status_t` [SetTo](#a2ca7c1d490f93a53ec5c79f175c24f3d) (const route_entry &routeEntry) — Initializes this object from a route_entry instance.
* `const sockaddr *` [Source](#a44e1c70de3e0ca8b85013b252bc61222) () const — Returns the source address.
* `void` [UnsetDestination](#a829a78cf4853880fbed9aa9e1bbfe05a) () — Uninitializes the destination address.
* `void` [UnsetGateway](#a4096e0d935b16a0dcca5be1c25d737c8) () — Uninitializes the gateway address.
* `void` [UnsetMask](#a0cd1094fe957fdb0bb9faa306419f28e) () — Uninitializes the subnet mask address.
* `void` [UnsetSource](#a702862c9ea0c98ca1beafa2eb2209829) () — Uninitializes the source address.

### Static Public Member Functions

* `static status_t` [GetDefaultGateway](#a104e1e6725204628fc73e087e1cef997) (int family, const char *interfaceName, sockaddr &gateway) — Gets the default gateway.
* `static status_t` [GetDefaultRoute](#a3ed6c7d0ceb740668f550244ed04bd14) (int family, const char *interfaceName, BNetworkRoute &route) — Gets the default route.
* `static status_t` [GetRoutes](#a424b485f934d439e4c14c2177c5927e7) (int family, BObjectList< BNetworkRoute, true > &routes) — Returns the routes of family type into routes.
* `static status_t` [GetRoutes](#a97926fc0f11b59f6736e6a53ad9b45ef) (int family, const char *interfaceName, BObjectList< BNetworkRoute, true > &routes) — Returns the routes of family type in interfaceName into routes.
* `static status_t` [GetRoutes](#a31ccc5899031d13bb376298a96ee2860) (int family, const char *interfaceName, uint32 filterFlags, BObjectList< BNetworkRoute, true > &routes) — Returns the routes of family type in interfaceName that are not filtered by filterFlags into routes.

## Detailed Member Documentation

### `BNetworkRoute()`

```cpp
BNetworkRoute::BNetworkRoute()
```

Creates an uninitialized [BNetworkRoute](classBNetworkRoute.md) object. 



**Since:** Haiku R1

---

### `~BNetworkRoute()`

```cpp
BNetworkRoute::~BNetworkRoute()
```

Releases all the allocated resources. 



**Since:** Haiku R1

---

### `AddressFamily()`

```cpp
int BNetworkRoute::AddressFamily()const
```

Returns the route's address family. 


If this object is uninitialized, it returns `AF_UNSPEC`.



**Since:** Haiku R1

---

### `Adopt()`

```cpp
void BNetworkRoute::Adopt(BNetworkRoute & other)
```

Moves *other* to this instance. 


*other* is left uninitialized.


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The other [BNetworkRoute](classBNetworkRoute.md) object. |





**Since:** Haiku R1

---

### `Destination()`

```cpp
const sockaddr * BNetworkRoute::Destination()const
```

Returns the destination address. 



**Since:** Haiku R1

---

### `Flags()`

```cpp
uint32 BNetworkRoute::Flags()const
```

Returns the route's flags mask. 



**Since:** Haiku R1

---

### `Gateway()`

```cpp
const sockaddr * BNetworkRoute::Gateway()const
```

Returns the gateway address. 



**Since:** Haiku R1

---

### `GetDefaultGateway()`

```cpp
static status_t BNetworkRoute::GetDefaultGateway(int family, const char * interfaceName, sockaddr & gateway)
```

Gets the default gateway. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `family` | The address family. See the POSIX header file sys/socket.h for the address families. |
| `interfaceName` | The network interface name. |
| `gateway` | A sockaddr instance where to write the default gateway. |





**Returns:** `B_OK` on success, or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The default gateway was successfully retrieved. |
| B_ENTRY_NOT_FOUND | There is not a default route or a default gateway configured. |





**Since:** Haiku R1

---

### `GetDefaultRoute()`

```cpp
static status_t BNetworkRoute::GetDefaultRoute(int family, const char * interfaceName, BNetworkRoute & route)
```

Gets the default route. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `family` | The address family. See the POSIX header file sys/socket.h for the address families. |
| `interfaceName` | The network interface name. |
| `route` | A [BNetworkRoute](classBNetworkRoute.md) where to write the default route. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The default route was successfully retrieved. |
| B_ENTRY_NOT_FOUND | There is not a default route configured. |





**Since:** Haiku R1

---

### `GetRoutes()`

```cpp
static status_t BNetworkRoute::GetRoutes(int family, BObjectList< BNetworkRoute, true > & routes)
```

Returns the routes of *family* type into *routes*. 



**See also:** [BNetworkRoute::GetRoutes(int, const char*,
	uint32, BObjectList<BNetworkRoute, true>&)](classBNetworkRoute.md#a31ccc5899031d13bb376298a96ee2860)



**Since:** Haiku R1

---

### `GetRoutes()`

```cpp
static status_t BNetworkRoute::GetRoutes(int family, const char * interfaceName, BObjectList< BNetworkRoute, true > & routes)
```

Returns the routes of *family* type in *interfaceName* into *routes*. 



**See also:** [BNetworkRoute::GetRoutes(int, const char*,
	uint32, BObjectList<BNetworkRoute, true>&)](classBNetworkRoute.md#a31ccc5899031d13bb376298a96ee2860)



**Since:** Haiku R1

---

### `GetRoutes()`

```cpp
static status_t BNetworkRoute::GetRoutes(int family, const char * interfaceName, uint32 filterFlags, BObjectList< BNetworkRoute, true > & routes)
```

Returns the routes of *family* type in *interfaceName* that are not filtered by *filterFlags* into *routes*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `family` | The address family. See the POSIX header file sys/socket.h for the address families. |
| `interfaceName` | The network interface name. |
| `filterFlags` | Flag mask to filter out routes. See the POSIX header file net/route.h for the valid route flags. |
| `routes` | A [BObjectList](../support_kit/classBObjectList.md) of [BNetworkRoute](classBNetworkRoute.md) to store the found routes. |





**Since:** Haiku R1

---

### `Mask()`

```cpp
const sockaddr * BNetworkRoute::Mask()const
```

Returns the subnet mask address. 



**Since:** Haiku R1

---

### `MTU()`

```cpp
uint32 BNetworkRoute::MTU()const
```

Returns the maximum transmission unit size of the route. 



**Since:** Haiku R1

---

### `RouteEntry()`

```cpp
const route_entry & BNetworkRoute::RouteEntry()const
```

Returns a copy of the route_entry with routing information of this object. 



**Since:** Haiku R1

---

### `SetDestination()`

```cpp
status_t BNetworkRoute::SetDestination(const sockaddr & destination)
```

Sets the destination address. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `destination` | A sockaddr struct instance with the destination information. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The destination has been modified successfully. |
| B_BAD_VALUE | The length in *destination.sa_len* is higher than the size of sockaddr_storage struct. |
| B_NO_MEMORY | Internal memory allocation error. |





**Since:** Haiku R1

---

### `SetFlags()`

```cpp
void BNetworkRoute::SetFlags(uint32 flags)
```

Sets the route's flags mask. 



**Since:** Haiku R1

---

### `SetGateway()`

```cpp
status_t BNetworkRoute::SetGateway(const sockaddr & gateway)
```

Sets the gateway address. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `gateway` | A sockaddr struct instance with the gateway information. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The gateway has been modified successfully. |
| B_BAD_VALUE | The length in *gateway.sa_len* is higher than the size of sockaddr_storage struct. |
| B_NO_MEMORY | Internal memory allocation error. |





**Since:** Haiku R1

---

### `SetMask()`

```cpp
status_t BNetworkRoute::SetMask(const sockaddr & mask)
```

Sets the subnet mask address. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `mask` | A sockaddr struct instance with the mask information. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The mask has been modified successfully. |
| B_BAD_VALUE | The length in *mask.sa_len* is higher than the size of sockaddr_storage struct. |
| B_NO_MEMORY | Internal memory allocation error. |





**Since:** Haiku R1

---

### `SetMTU()`

```cpp
void BNetworkRoute::SetMTU(uint32 mtu)
```

Sets the maximum transmission unit size of the route. 



**Since:** Haiku R1

---

### `SetSource()`

```cpp
status_t BNetworkRoute::SetSource(const sockaddr & source)
```

Sets the source address. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `source` | A sockaddr struct instance with the source address information. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The source address has been modified successfully. |
| B_BAD_VALUE | The length in *source.sa_len* is higher than the size of sockaddr_storage struct. |
| B_NO_MEMORY | Internal memory allocation error. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BNetworkRoute::SetTo(const BNetworkRoute & other)
```

Initializes this object from *other* [BNetworkRoute](classBNetworkRoute.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BNetworkRoute](classBNetworkRoute.md) instance from where to initialize this object. |





**Returns:** `B_OK` if the object was initialized or an error code.



**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BNetworkRoute::SetTo(const route_entry & routeEntry)
```

Initializes this object from a route_entry instance. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `routeEntry` | A route_entry object with the routing information. |





**Returns:** `B_OK` if the object was initialized or an error code.



**Since:** Haiku R1

---

### `Source()`

```cpp
const sockaddr * BNetworkRoute::Source()const
```

Returns the source address. 



**Since:** Haiku R1

---

### `UnsetDestination()`

```cpp
void BNetworkRoute::UnsetDestination()
```

Uninitializes the destination address. 



**Since:** Haiku R1

---

### `UnsetGateway()`

```cpp
void BNetworkRoute::UnsetGateway()
```

Uninitializes the gateway address. 



**Since:** Haiku R1

---

### `UnsetMask()`

```cpp
void BNetworkRoute::UnsetMask()
```

Uninitializes the subnet mask address. 



**Since:** Haiku R1

---

### `UnsetSource()`

```cpp
void BNetworkRoute::UnsetSource()
```

Uninitializes the source address. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBNetworkRoute.html).
