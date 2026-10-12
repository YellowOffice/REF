---
name: BNetworkDevice
type: class
kit: network_kit
brief: "BNetworkDevice class represents a network device"
source: haiku-book
---

# BNetworkDevice Class
**Kit/Group:** [Network Kit](../network_kit/group__network.md)

## Description

[BNetworkDevice](classBNetworkDevice.md) class represents a network device. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BNetworkDevice](#a302740aab8c98ea74dc1330d22740fc5) () — Creates a BNetworkDevice object in an uninitialized state.
* [BNetworkDevice](#ae75aa92b8f59f8de62e7c49827525cb7) (const char *name) — Creates and initializes a BNetworkDevice object identified by name.
* `status_t` [Control](#abdbee44fe61dba73ef37e9a02fe62d94) (int option, void *request) — Sends an ioctl request to the device.
* `bool` [Exists](#a19a8b61deb084ad7547a9dea8273be2e) () const — Checks if the network device identified as Name() exists in the system.
* `uint32` [Flags](#a4e806826c18ccf26920d4455498a2ec8) () const — Returns a bit mask of the flags associated with the device.
* `status_t` [GetHardwareAddress](#acee63258691cdf7d28ca59ac25f0e7c3) (BNetworkAddress &address) — Gets the MAC address of the device.
* `status_t` [GetNetwork](#aea42de6bbd9f5229f09f1265d6c85e0a) (const BNetworkAddress &address, wireless_network &network) — Returns a wireless_network object of the network described in address.
* `status_t` [GetNetwork](#a80e442e414f32d326eac916fe8d1db61) (const char *name, wireless_network &network) — Returns a wireless_network object of the network identified as name.
* `status_t` [GetNetworks](#ad6829a4e6bf21d2285264635f18cc469) (wireless_network *&networks, uint32 &count) — Gets all the detected wireless networks from a previous scan.
* `status_t` [GetNextAssociatedNetwork](#a9e7b907b8e4015db469f21f9fbb35f71) (uint32 &cookie, BNetworkAddress &address) — Iterates through the associated networks and saves the address of next one in address.
* `status_t` [GetNextAssociatedNetwork](#ae3ae9acc3777bc373762f71e0c62b4d7) (uint32 &cookie, wireless_network &network) — Iterates through the associated networks and saves the next one in network.
* `bool` [HasLink](#aed2944bcfd727d14487dad458e8fd8db) () const — Checks if the device has an active connection with another interface.
* `uint32` [Index](#a9def8d92b0402a4a1d480c51f458d6c7) () const — Returns the index of the device in the list of network devices.
* `bool` [IsEthernet](#a3a448f921b65c16f7323e0aeb98b046e) () — Checks if the device media type is ethernet.
* `bool` [IsWireless](#a3b0dfc7f230746c0056b77a58804fadf) () — Checks if the device media type is IEEE 802.11 (WLAN) or wireless.
* `status_t` [JoinNetwork](#aa690aa8ca5192cae910c62f5f702005f) (const BNetworkAddress &address, const char *password=NULL) — Connects to the network in address.
* `status_t` [JoinNetwork](#a3158219268f4e2b75c990089953ea315) (const char *name, const char *password=NULL) — Connects to the network identified as name.
* `status_t` [JoinNetwork](#adb46628fa3b234d92cea261c82ca37ec) (const wireless_network &network, const char *password=NULL) — Connects to the network described in network.
* `status_t` [LeaveNetwork](#ae89086c5ae6e8ba27c3c5bd30138dc0f) (const BNetworkAddress &address) — Disconnects from the wireless network in address.
* `status_t` [LeaveNetwork](#aea9defc65a03bcc9fdbae0a6430983fb) (const char *name) — Disconnects from the wireless network name.
* `status_t` [LeaveNetwork](#aa2b63e4b2b7ca9e5820f9c6695514d12) (const wireless_network &network) — Disconnects from the wireless network.
* `int32` [Media](#a6195a75d3942148efb4c4dd4a194605d) () const — Returns a bit mask of the device's media options.
* `const char *` [Name](#a739d0eb0fd3e79bb5b938bf890752cb3) () const — Returns the device name.
* `status_t` [Scan](#a961291e1ab2cb218c673e2cc40724e86) (bool wait=true, bool forceRescan=true) — Scans for a wireless network.
* `status_t` [SetMedia](#ad1f5f189c3f0f1e002646187da848f8f) (int32 media) — Configures the media options of the device.
* `void` [SetTo](#a8740a432c3ecd9b3ccee2902ff5623dd) (const char *name) — (Re)initializes the BNetworkDevice object to work with the device in name.
* `void` [Unset](#ab7ad677ccc7ac832fc18ca965b62d7e6) () — Returns the object to an uninitialized state.

## Detailed Member Documentation

### `BNetworkDevice()`

```cpp
BNetworkDevice::BNetworkDevice()
```

Creates a [BNetworkDevice](classBNetworkDevice.md) object in an uninitialized state. 



**See also:** [SetTo()](classBNetworkDevice.md#a8740a432c3ecd9b3ccee2902ff5623dd)



**Since:** Haiku R1

---

### `BNetworkDevice()`

```cpp
BNetworkDevice::BNetworkDevice(const char * name)
```

Creates and initializes a [BNetworkDevice](classBNetworkDevice.md) object identified by *name*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The device name. |





**See also:** [SetTo()](classBNetworkDevice.md#a8740a432c3ecd9b3ccee2902ff5623dd)



**Since:** Haiku R1

---

### `Control()`

```cpp
status_t BNetworkDevice::Control(int option, void * request)
```

Sends an ioctl request to the device. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `option` | The kind of operation. |
| `request` | The request data. |





**Returns:** `B_OK` on success, or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Command sent and processed successfully. |
| B_ERROR | Something went wrong, or performing ioctl calls is not supported for the device's media type. |





**Since:** Haiku R1

---

### `Exists()`

```cpp
bool BNetworkDevice::Exists()const
```

Checks if the network device identified as [Name()](classBNetworkDevice.md#a739d0eb0fd3e79bb5b938bf890752cb3) exists in the system. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The device exists. |
| false | The device does not exist or the [BNetworkDevice](classBNetworkDevice.md) object is not initialized. |





**Since:** Haiku R1

---

### `Flags()`

```cpp
uint32 BNetworkDevice::Flags()const
```

Returns a bit mask of the flags associated with the device. 


Possible flags are those defined in the POSIX header `net/if.h`.



**Since:** Haiku R1

---

### `GetHardwareAddress()`

```cpp
status_t BNetworkDevice::GetHardwareAddress(BNetworkAddress & address)
```

Gets the MAC address of the device. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | A [BNetworkAddress](classBNetworkAddress.md) object where to write the address. |





**Returns:** `B_OK` on success, or an error code.



**Since:** Haiku R1

---

### `GetNetwork()`

```cpp
status_t BNetworkDevice::GetNetwork(const BNetworkAddress & address, wireless_network & network)
```

Returns a [wireless_network](structwireless__network.md) object of the network described in *address*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | A [BNetworkAddress](classBNetworkAddress.md) object of the wireless network. |
| `network` | A [wireless_network](structwireless__network.md) object where the network information will be written to. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_BAD_VALUE | *address'* family is not `AF_LINK`. |
| B_NO_MEMORY | Internal memory allocation error. |
| B_ENTRY_NOT_FOUND | There is no network called *name*. |





**Since:** Haiku R1

---

### `GetNetwork()`

```cpp
status_t BNetworkDevice::GetNetwork(const char * name, wireless_network & network)
```

Returns a [wireless_network](structwireless__network.md) object of the network identified as *name*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The wireless network name. |
| `network` | A [wireless_network](structwireless__network.md) object where the network information will be written to. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_BAD_VALUE | *name* is `NULL`. |
| B_NO_MEMORY | Internal memory allocation error. |
| B_ENTRY_NOT_FOUND | There is no network called *name*. |





**Since:** Haiku R1

---

### `GetNetworks()`

```cpp
status_t BNetworkDevice::GetNetworks(wireless_network *& networks, uint32 & count)
```

Gets all the detected wireless networks from a previous scan. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `networks` | A `NULL` pointer where an array of [wireless_network](structwireless__network.md) will be written to. |
| `count` | How many items there are in *networks*. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_BAD_VALUE | *networks* is not `NULL`. |
| B_NO_MEMORY | Internal memory allocation error. |





**Since:** Haiku R1

---

### `GetNextAssociatedNetwork()`

```cpp
status_t BNetworkDevice::GetNextAssociatedNetwork(uint32 & cookie, BNetworkAddress & address)
```

Iterates through the associated networks and saves the address of next one in *address*. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_ENTRY_NOT_FOUND | There are no more associated networks. |





**Since:** Haiku R1

---

### `GetNextAssociatedNetwork()`

```cpp
status_t BNetworkDevice::GetNextAssociatedNetwork(uint32 & cookie, wireless_network & network)
```

Iterates through the associated networks and saves the next one in *network*. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_ENTRY_NOT_FOUND | There are no more associated networks. |





**Since:** Haiku R1

---

### `HasLink()`

```cpp
bool BNetworkDevice::HasLink()const
```

Checks if the device has an active connection with another interface. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The device has a link. |
| false | The device does not have a link. |





**Since:** Haiku R1

---

### `Index()`

```cpp
uint32 BNetworkDevice::Index()const
```

Returns the index of the device in the list of network devices. 


If the device was not found or this object is not initialized, it returns `0`.



**Since:** Haiku R1

---

### `IsEthernet()`

```cpp
bool BNetworkDevice::IsEthernet()
```

Checks if the device media type is ethernet. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The device is an ethernet device. |
| false | The device is not an ethernet device. |





**Since:** Haiku R1

---

### `IsWireless()`

```cpp
bool BNetworkDevice::IsWireless()
```

Checks if the device media type is IEEE 802.11 (WLAN) or wireless. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The device is a wireless device. |
| false | The device is not a wireless device. |





**Since:** Haiku R1

---

### `JoinNetwork()`

```cpp
status_t BNetworkDevice::JoinNetwork(const BNetworkAddress & address, const char * password = NULL)
```

Connects to the network in *address*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `address` | The network address. |
| `password` | The network password. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_BAD_VALUE | *address* is not properly initialized. |





**Since:** Haiku R1

---

### `JoinNetwork()`

```cpp
status_t BNetworkDevice::JoinNetwork(const char * name, const char * password = NULL)
```

Connects to the network identified as *name*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The network name. |
| `password` | The network password. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_BAD_VALUE | *name* is `NULL`. |





**Since:** Haiku R1

---

### `JoinNetwork()`

```cpp
status_t BNetworkDevice::JoinNetwork(const wireless_network & network, const char * password = NULL)
```

Connects to the network described in *network*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `network` | A [wireless_network](structwireless__network.md) object with the network information. |
| `password` | The network password. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_BAD_VALUE | The name in *network* is `NULL`. |





**Since:** Haiku R1

---

### `LeaveNetwork()`

```cpp
status_t BNetworkDevice::LeaveNetwork(const BNetworkAddress & address)
```

Disconnects from the wireless network in *address*. 



**Returns:** `B_OK` if it could leave the network or an error code.



**Since:** Haiku R1

---

### `LeaveNetwork()`

```cpp
status_t BNetworkDevice::LeaveNetwork(const char * name)
```

Disconnects from the wireless network *name*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The network name. |





**Returns:** `B_OK` if it could leave the network or an error code.



**Since:** Haiku R1

---

### `LeaveNetwork()`

```cpp
status_t BNetworkDevice::LeaveNetwork(const wireless_network & network)
```

Disconnects from the wireless *network*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `network` | A [wireless_network](structwireless__network.md) object with the network name. |





**Returns:** `B_OK` if it could leave the network or an error code.



**Since:** Haiku R1

---

### `Media()`

```cpp
int32 BNetworkDevice::Media()const
```

Returns a bit mask of the device's media options. 


Possible flags are those defined in the header `net/if_media.h`.



**Since:** Haiku R1

---

### `Name()`

```cpp
const char * BNetworkDevice::Name()const
```

Returns the device name. 



**Since:** Haiku R1

---

### `Scan()`

```cpp
status_t BNetworkDevice::Scan(bool wait = true, bool forceRescan = true)
```

Scans for a wireless network. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `wait` | Tells the object to wait for any WLAN change before starting to scan. |
| `forceRescan` | Flush any previous scan result. |





**Returns:** B_OK if the operation was performed successfully or an error code otherwise.



**Since:** Haiku R1

---

### `SetMedia()`

```cpp
status_t BNetworkDevice::SetMedia(int32 media)
```

Configures the media options of the device. 



**Returns:** B_OK on success, or an error code.



**Since:** Haiku R1

---

### `SetTo()`

```cpp
void BNetworkDevice::SetTo(const char * name)
```

(Re)initializes the [BNetworkDevice](classBNetworkDevice.md) object to work with the device in *name*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The device name. |





**See also:** [Unset()](classBNetworkDevice.md#ab7ad677ccc7ac832fc18ca965b62d7e6)



**Since:** Haiku R1

---

### `Unset()`

```cpp
void BNetworkDevice::Unset()
```

Returns the object to an uninitialized state. 



**See also:** [SetTo()](classBNetworkDevice.md#a8740a432c3ecd9b3ccee2902ff5623dd)



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBNetworkDevice.html).
