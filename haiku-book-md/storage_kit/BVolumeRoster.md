---
name: BVolumeRoster
type: class
kit: storage_kit
brief: "Provides an interface for iterating through available volumes and watching for mounting/unmounting"
source: haiku-book
---

# BVolumeRoster Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Provides an interface for iterating through available volumes and watching for mounting/unmounting. 


This class wraps the next_dev() function for iterating through the list of available volumes and [watch_node()](NodeMonitor_8h.md#aa47570f615a5e07a38f452a47f9a8f48)/stop_watching() for watching volumes.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BVolumeRoster](#ac3d5de1081dff8e5d3acdb7de76f61e3) () — Creates a BVolumeRoster object. The object is ready to be used.
* `virtual` [~BVolumeRoster](#abaf24db5614655d7b1c10dc266bffd38) () — Deletes the volume roster and frees all associated resources.
* `status_t` [GetBootVolume](#a1df1b33f20f83ede40149d17555c7a9e) (BVolume *volume) — Fills out the passed in BVolume object with the boot volume.
* `status_t` [GetNextVolume](#a8f8fbd0e558c214536d97e74026ac183) (BVolume *volume) — Fills out the passed in BVolume object with the next available volume.
* `BMessenger` [Messenger](#a347c10c05554e3a96a33da78b6ac7657) () const — Returns the messenger currently watching the volume list.
* `void` [Rewind](#aab13bb090dab13062b708b03a1534172) () — Rewinds the list of available volumes back to the first item.
* `status_t` [StartWatching](#ab437b00c523ed563d5456f46ad8a89b2) (BMessenger messenger=be_app_messenger) — Starts watching the available volumes for changes.
* `void` [StopWatching](#a17aad18f747c04a89ea99325f55af158) () — Stops watching volumes initiated by StartWatching().

## Detailed Member Documentation

### `BVolumeRoster()`

```cpp
BVolumeRoster::BVolumeRoster()
```

Creates a [BVolumeRoster](classBVolumeRoster.md) object. The object is ready to be used. 



**Since:** BeOS R3

---

### `~BVolumeRoster()`

```cpp
BVolumeRoster::~BVolumeRoster()
```

Deletes the volume roster and frees all associated resources. 


If a watch was activated (by [StartWatching()](classBVolumeRoster.md#ab437b00c523ed563d5456f46ad8a89b2)), it is deactivated.



**Since:** BeOS R3

---

### `GetBootVolume()`

```cpp
status_t BVolumeRoster::GetBootVolume(BVolume * volume)
```

Fills out the passed in [BVolume](classBVolume.md) object with the boot volume. 


Currently, this method looks for the volume that is mounted at "/boot". The only way to fool the system into thinking that there is not a boot volume is to rename "/boot" – but, please refrain from doing this.


Parameters

| Parameter | Description |
| :--- | :--- |
| `volume` | A pointer to a pre-allocated [BVolume](classBVolume.md) to be initialized to refer to the boot volume. |





**Returns:** A status code, `B_OK` if everything went fine or an error code otherwise.



**Since:** BeOS R3

---

### `GetNextVolume()`

```cpp
status_t BVolumeRoster::GetNextVolume(BVolume * volume)
```

Fills out the passed in [BVolume](classBVolume.md) object with the next available volume. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `volume` | A pointer to a pre-allocated [BVolume](classBVolume.md) object to be initialized to the next available volume. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | The last volume in the list was already returned. |





**Since:** BeOS R3

---

### `Messenger()`

```cpp
BMessenger BVolumeRoster::Messenger()const
```

Returns the messenger currently watching the volume list. 



**Returns:** A messenger to the target currently watching the volume list, or an invalid messenger if not watching.



**Since:** BeOS R3

---

### `Rewind()`

```cpp
void BVolumeRoster::Rewind()
```

Rewinds the list of available volumes back to the first item. 


The next call to [GetNextVolume()](classBVolumeRoster.md#a8f8fbd0e558c214536d97e74026ac183) will return the first available volume.



**Since:** BeOS R3

---

### `StartWatching()`

```cpp
status_t BVolumeRoster::StartWatching(BMessenger messenger = be_app_messenger)
```

Starts watching the available volumes for changes. 


Notifications are sent to the specified target whenever a volume is mounted or unmounted. The format of the notification messages is described under [watch_node()](NodeMonitor_8h.md#aa47570f615a5e07a38f452a47f9a8f48). Actually [BVolumeRoster](classBVolumeRoster.md) just provides a more convenient interface for it.


If [StartWatching()](classBVolumeRoster.md#ab437b00c523ed563d5456f46ad8a89b2) has been called before with another target and no [StopWatching()](classBVolumeRoster.md#a17aad18f747c04a89ea99325f55af158) since, [StopWatching()](classBVolumeRoster.md#a17aad18f747c04a89ea99325f55af158) is called first, so that the former target won't receive any notifications anymore.


When the object is destroyed all watching ends as well.


Parameters

| Parameter | Description |
| :--- | :--- |
| `messenger` | The target which the notification messages are sent. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | The supplied [BMessenger](../application_kit/classBMessenger.md) was invalid. |
| B_NO_MEMORY | There was insufficient memory to carry out this operation. |





**See also:** [watch_node()](NodeMonitor_8h.md#aa47570f615a5e07a38f452a47f9a8f48)



**Since:** BeOS R3

---

### `StopWatching()`

```cpp
void BVolumeRoster::StopWatching()
```

Stops watching volumes initiated by [StartWatching()](classBVolumeRoster.md#ab437b00c523ed563d5456f46ad8a89b2). 



**See also:** [stop_watching()](NodeMonitor_8h.md#a0f58e29c5793f34222c9779ab7aa4f60)



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBVolumeRoster.html).
