---
name: BUSBRoster
type: class
kit: device_kit
brief: "Abstract class to implement to watch for devices that get attached or removed from the USB bus"
source: haiku-book
---

# BUSBRoster Class
**Kit/Group:** [Device Kit](../device_kit/group__device.md) | [Device Kit library (libdevice.so)](group__libdevice.md)

## Description

Abstract class to implement to watch for devices that get attached or removed from the USB bus. 


The roster subclass must implement the pure virtual hooks [DeviceAdded()](classBUSBRoster.md#a445d30ecc7199d8e84c9017421fa48a0) and [DeviceRemoved()](classBUSBRoster.md#a014511be7507f188f02e11af90d67a73).



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BUSBRoster](#a67226526a45ec74f2b590ee18f89c407) () — Default constructor.
* `virtual` [~BUSBRoster](#acc40922acf89b7224c785fb9be5bf626) () — Stops the USB roster looper and releases the allocated resources.
* `virtual status_t` [DeviceAdded](#a445d30ecc7199d8e84c9017421fa48a0) (BUSBDevice *device)=0 — Hook method called when a new device gets attached to the USB bus.
* `virtual void` [DeviceRemoved](#a014511be7507f188f02e11af90d67a73) (BUSBDevice *device)=0 — Hook method called when a device gets detached from the USB bus.
* `void` [Start](#ac86819f1f5d8d6e5332178403c055f58) () — Starts the USB roster looper to monitor for attachment or detachment events.
* `void` [Stop](#a5cad5c2d95c126ba01edd718a3a35357) () — Stops the USB roster looper and releases its resources.

## Detailed Member Documentation

### `BUSBRoster()`

```cpp
BUSBRoster::BUSBRoster()
```

Default constructor. 



**Since:** Haiku R1

---

### `~BUSBRoster()`

```cpp
BUSBRoster::~BUSBRoster()
```

Stops the USB roster looper and releases the allocated resources. 



**Since:** Haiku R1

---

### `DeviceAdded()`

```cpp
status_t BUSBRoster::DeviceAdded(BUSBDevice * device)
```

Hook method called when a new device gets attached to the USB bus. 


The hook is called with an initialized [BUSBDevice](classBUSBDevice.md) object. If you return `B_OK` from your hook the object will stay valid and the [DeviceRemoved()](classBUSBRoster.md#a014511be7507f188f02e11af90d67a73) hook will be called for it. Otherwise the object is deleted and [DeviceRemoved()](classBUSBRoster.md#a014511be7507f188f02e11af90d67a73) is not called.


Parameters

| Parameter | Description |
| :--- | :--- |
| `device` | A [BUSBDevice](classBUSBDevice.md) instance of the device attached. |





**Since:** Haiku R1

---

### `DeviceRemoved()`

```cpp
void BUSBRoster::DeviceRemoved(BUSBDevice * device)
```

Hook method called when a device gets detached from the USB bus. 


The device object gets invalid and will be deleted as soon as you return from the hook so be sure to remove all references to it.


Parameters

| Parameter | Description |
| :--- | :--- |
| `device` | A [BUSBDevice](classBUSBDevice.md) instance of the device removed. |





**Since:** Haiku R1

---

### `Start()`

```cpp
void BUSBRoster::Start()
```

Starts the USB roster looper to monitor for attachment or detachment events. 



**Since:** Haiku R1

---

### `Stop()`

```cpp
void BUSBRoster::Stop()
```

Stops the USB roster looper and releases its resources. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBUSBRoster.html).
