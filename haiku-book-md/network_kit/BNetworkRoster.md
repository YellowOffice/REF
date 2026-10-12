---
name: BNetworkRoster
type: class
kit: network_kit
brief: "BNetworkRoster class allows to manage network interfaces as well as persistent (wireless) networks"
source: haiku-book
---

# BNetworkRoster Class
**Kit/Group:** [Network Kit](../network_kit/group__network.md)

## Description

[BNetworkRoster](classBNetworkRoster.md) class allows to manage network interfaces as well as persistent (wireless) networks. 


To use this class you have to call the default instance:



```cpp
BNetworkRoster& roster = BNetworkRoster::Default();
```

Once done, you can manage network interfaces using [AddInterface()](classBNetworkRoster.md#a1c15c9a8037c3c08455629e61c872551) and [RemoveInterface()](classBNetworkRoster.md#aca6368b02813f3a05ca45dece5c21154), or enumerate them using [CountInterfaces()](classBNetworkRoster.md#a771884895ae09663a2002ae620c6509f) and [GetNextInterface()](classBNetworkRoster.md#acb73dbc46ce2f621cbd89823ba71480c).


You can also manage persistent networks using [AddPersistentNetwork()](classBNetworkRoster.md#a16a381f2657a540f32bfcdf83c5879bd) and [RemovePersistentNetwork()](classBNetworkRoster.md#af43e7fb8822579c76823f361d11a3b60), as well as enumerate them using [CountPersistentNetworks()](classBNetworkRoster.md#aeeb24a013e3d0630e30a353e157cdfab) and [GetNextPersistentNetwork()](classBNetworkRoster.md#ae09e8c3b4b186a3cdb0f099b2a95447b).


In addition, you can have access to the network notifications API using [StartWatching()](classBNetworkRoster.md#ae27e0e17ecb94f446096087060c4109c) and [StopWatching()](classBNetworkRoster.md#a3ad8607dda2843161e39a7a2c33db0ba), attaching to it a [BMessenger](../application_kit/classBMessenger.md) instance as a parameter to start or stop monitoring for network related events.



**Since:** Haiku R1

## Member List

### Public Member Functions

* `size_t` [CountInterfaces](#a771884895ae09663a2002ae620c6509f) () const — Returns the number of network interfaces in the system.
* `status_t` [GetNextInterface](#acb73dbc46ce2f621cbd89823ba71480c) (uint32 *cookie, BNetworkInterface &interface) const — Iterate through the network interfaces.
* `status_t` [AddInterface](#a1c15c9a8037c3c08455629e61c872551) (const char *name) — Add a network interface identified by name.
* `status_t` [AddInterface](#ad529c189843b266ea372a4f3b924df9f) (const BNetworkInterface &interface) — Add a network interface from a BNetworkInterface object.
* `status_t` [RemoveInterface](#aca6368b02813f3a05ca45dece5c21154) (const char *name) — Remove the network interface identified by name.
* `status_t` [RemoveInterface](#a9e4e22cfc6c269752b5d093238c624a6) (const BNetworkInterface &interface) — Remove the network interface matching a BNetworkInterface object.
* `int32` [CountPersistentNetworks](#aeeb24a013e3d0630e30a353e157cdfab) () const — Returns the number of saved persistent networks.
* `status_t` [GetNextPersistentNetwork](#ae09e8c3b4b186a3cdb0f099b2a95447b) (uint32 *cookie, wireless_network &network) const — Iterate through the saved persistent networks.
* `status_t` [AddPersistentNetwork](#a16a381f2657a540f32bfcdf83c5879bd) (const wireless_network &network) — Add network to the list of persistent networks.
* `status_t` [RemovePersistentNetwork](#af43e7fb8822579c76823f361d11a3b60) (const char *name) — Remove the persistent network identified as name.
* `status_t` [StartWatching](#ae27e0e17ecb94f446096087060c4109c) (const BMessenger &target, uint32 eventMask) — Subscribes target to receive network events' notifications described in eventMask.
* `void` [StopWatching](#a3ad8607dda2843161e39a7a2c33db0ba) (const BMessenger &target) — Unsubscribes target from receiving network messages.

### Static Public Member Functions

* `static BNetworkRoster &` [Default](#ad57086b0701e4c15b25fb4f4e768c55e) () — Returns the default network roster.

## Detailed Member Documentation

### `AddInterface()`

```cpp
status_t BNetworkRoster::AddInterface(const BNetworkInterface & interface)
```

Add a network interface from a BNetworkInterface object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `interface` | A BNetworkInterface object from where to create the interface. |





**Returns:** B_OK if the interface was added, or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |





**Since:** Haiku R1

---

### `AddInterface()`

```cpp
status_t BNetworkRoster::AddInterface(const char * name)
```

Add a network interface identified by *name*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the interface. |





**Returns:** B_OK if the interface was added, or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |





**Since:** Haiku R1

---

### `AddPersistentNetwork()`

```cpp
status_t BNetworkRoster::AddPersistentNetwork(const wireless_network & network)
```

Add *network* to the list of persistent networks. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `network` | The [wireless_network](structwireless__network.md) instance containing the network information. |





**Returns:** `B_OK` on success, or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The network was added to the persistent network list. |
| B_BAD_VALUE | [wireless_network::name](structwireless__network.md#a1d2d44774df8c730fc8fdcffdf38fd1a) is NULL or its length is equal to `0`. |





**Since:** Haiku R1

---

### `CountInterfaces()`

```cpp
size_t BNetworkRoster::CountInterfaces()const
```

Returns the number of network interfaces in the system. 



**Since:** Haiku R1

---

### `CountPersistentNetworks()`

```cpp
int32 BNetworkRoster::CountPersistentNetworks()const
```

Returns the number of saved persistent networks. 



**Since:** Haiku R1

---

### `Default()`

```cpp
static BNetworkRoster & BNetworkRoster::Default()
```

Returns the default network roster. 



**Since:** Haiku R1

---

### `GetNextInterface()`

```cpp
status_t BNetworkRoster::GetNextInterface(uint32 * cookie, BNetworkInterface & interface)const
```

Iterate through the network interfaces. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `cookie` | A cookie used to keep track of where you are in the list of network interfaces. Before doing the first query, it has to be initialized to `0`. After that, pass the cookie to each subsequent call to progress the iterator. |
| `interface` | A pre-allocated BNetworkInterface where to write the network interface information. For each successful iteration, the existing contents is overwritten. |





**Returns:** `B_OK` if the iteration was successful, or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The iteration was successful and the current interface information was written to *interface*. |
| B_BAD_VALUE | *cookie* is `NULL`, or no more interfaces were found. |
| B_NO_MEMORY | Internal memory allocation error. |





**Since:** Haiku R1

---

### `GetNextPersistentNetwork()`

```cpp
status_t BNetworkRoster::GetNextPersistentNetwork(uint32 * cookie, wireless_network & network)const
```

Iterate through the saved persistent networks. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `cookie` | A cookie used to keep track of where you are in the list of persistent networks. Before doing the first query, it has to be initialized to `0`. After that, pass the cookie to each subsequent call to progress the iterator. |
| `network` | A pre-allocated [wireless_network](structwireless__network.md) object where to write the network information. For each successful iteration, the existing contents is overwritten. |





**Returns:** `B_OK` if the iteration was successful, or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The iteration was successful and the current persistent network was written to *network*. |
| B_ERROR | There was an error receiving the reply from the net server, the end of the persistent networks was reached, or the network name could not be retrieved. |





**Since:** Haiku R1

---

### `RemoveInterface()`

```cpp
status_t BNetworkRoster::RemoveInterface(const BNetworkInterface & interface)
```

Remove the network interface matching a BNetworkInterface object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `interface` | A BNetworkInterface object from where to get the interface name to remove. |





**Returns:** B_OK if the interface was removed, or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |





**Since:** Haiku R1

---

### `RemoveInterface()`

```cpp
status_t BNetworkRoster::RemoveInterface(const char * name)
```

Remove the network interface identified by *name*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the interface. |





**Returns:** B_OK if the interface was removed, or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |





**Since:** Haiku R1

---

### `RemovePersistentNetwork()`

```cpp
status_t BNetworkRoster::RemovePersistentNetwork(const char * name)
```

Remove the persistent network identified as *name*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The network name. |





**Returns:** `B_OK` on success, or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The network was removed successfully. |
| B_BAD_VALUE | *name* is NULL or its length is equal to `0`. |
| B_ENTRY_NOT_FOUND | A network *name* could not be found in the persistent networks list. |





**Since:** Haiku R1

---

### `StartWatching()`

```cpp
status_t BNetworkRoster::StartWatching(const BMessenger & target, uint32 eventMask)
```

Subscribes *target* to receive network events' notifications described in *eventMask*. 


Valid values for *eventMask* are any combination of the following:


* `B_WATCH_NETWORK_INTERFACE_CHANGES`

* `B_WATCH_NETWORK_LINK_CHANGES`

* `B_WATCH_NETWORK_WLAN_CHANGES`



For `B_WATCH_NETWORK_INTERFACE_CHANGES`, the following notifications will be sent to *target* if such events happen:


* `B_NETWORK_INTERFACE_ADDED`

* `B_NETWORK_INTERFACE_REMOVED`

* `B_NETWORK_INTERFACE_CHANGED`



For `B_WATCH_NETWORK_LINK_CHANGES`, the following notification will be sent to *target* if such event happens:


* `B_NETWORK_DEVICE_LINK_CHANGED`



For `B_WATCH_NETWORK_WLAN_CHANGES`, the following notifications will be sent to *target* if such events happen:


* `B_NETWORK_WLAN_JOINED`

* `B_NETWORK_WLAN_LEFT`

* `B_NETWORK_WLAN_SCANNED`

* `B_NETWORK_WLAN_MESSAGE_INTEGRITY_FAILED`



If *eventMask* is `0`, it will stop sending notifications to *target*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | A [BMessenger](../application_kit/classBMessenger.md) object to where the notification messages will be delivered. |
| `eventMask` | A flags mask for the events to watch. Setting it to `0` will stop watching for network events (the same as calling [StopWatching()](classBNetworkRoster.md#a3ad8607dda2843161e39a7a2c33db0ba)). |





**Returns:** `B_OK` on success or an error code.



**Since:** Haiku R1

---

### `StopWatching()`

```cpp
void BNetworkRoster::StopWatching(const BMessenger & target)
```

Unsubscribes *target* from receiving network messages. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | A [BMessenger](../application_kit/classBMessenger.md) object that will not be sent any more messages. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBNetworkRoster.html).
