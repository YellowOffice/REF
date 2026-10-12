---
name: BUSBEndpoint
type: class
kit: device_kit
brief: "Represents a device endpoint that can be used to send or receive data"
source: haiku-book
---

# BUSBEndpoint Class
**Kit/Group:** [Device Kit](../device_kit/group__device.md) | [Device Kit library (libdevice.so)](group__libdevice.md)

## Description

Represents a device endpoint that can be used to send or receive data. 


It also allows to query endpoint characteristics like endpoint type or direction.



**Since:** Haiku R1

## Member List

### Public Member Functions

* `uint32` [Index](#a0b55519b6eb62b12e8739aeec76e5492) () const — Returns the index of the endpoint in the list of endpoints of the parent interface.
* `const BUSBInterface *` [Interface](#a2bc98e5373e4351ed70ce5561e3349a6) () const — Returns the parent interface of this endpoint.
* `const BUSBConfiguration *` [Configuration](#acba1e1dceb6bbef560ccae1ec9440371) () const — Convenience method to directly reach the parent configuration of this endpoint.
* `const BUSBDevice *` [Device](#a539deffb90492383a4d50a23d8f4e086) () const — Convenience method to directly reach the parent device of this endpoint.
* `bool` [IsBulk](#a9e7ab7a83961198a0a0673947bb4607d) () const — Returns if the transfer type is bulk.
* `bool` [IsInterrupt](#a52b18ef7d0d644d8c2e228aa1d960c35) () const — Returns if the transfer type is interrupt.
* `bool` [IsIsochronous](#a651ff49160c7154dc4a00da3c316693d) () const — Returns if the transfer type is isochronous.
* `bool` [IsControl](#a5adc33b0a0251a44b127bdea297d295a) () const — Returns if the transfer type is control.
* `bool` [IsInput](#abdd5538fc7508f1c048b9319dc14b72f) () const — Returns if the address direction is input.
* `bool` [IsOutput](#a31412d44b1c6a42b21445be43f3ee200) () const — Returns if the address direction is output.
* `uint16` [MaxPacketSize](#a7a49e932b278366e065ca95a1cd9377d) () const — Returns the maximum packet size that this endpoint is able to receive or send.
* `uint8` [Interval](#a65666c24b48bfcced34c3744afab4794) () const — Returns the polling interval of this endpoint for data transfers.
* `const usb_endpoint_descriptor *` [Descriptor](#aff7176716c09690096d5804ab92ad193) () const — Returns a pointer to a usb_endpoint_descriptor instance with the descriptor of this endpoint.
* `ssize_t` [ControlTransfer](#a50d194b81da76c362f68e5b8397cc675) (uint8 requestType, uint8 request, uint16 value, uint16 index, uint16 length, void *data) const — Perform a control transfer operation.
* `ssize_t` [InterruptTransfer](#a50452144484ee652fd246e667aa7e537) (void *data, size_t length) const — Perform an interrupt transfer operation.
* `ssize_t` [BulkTransfer](#a9e5583742bfb59deeefad55db19db0db) (void *data, size_t length) const — Perform a bulk transfer operation.
* `ssize_t` [IsochronousTransfer](#ae5c0ec58cbbc0e8ec3dfcad0840595a6) (void *data, size_t length, usb_iso_packet_descriptor *packetDescriptors, uint32 packetCount) const — Perform an isochronous transfer operation.
* `bool` [IsStalled](#ab7a93ee695c563c84dc3ed9e8481be63) () const — Gets the halt state of the endpoint.
* `status_t` [ClearStall](#ae1e1764968edc18d64d4229cc09e5c8d) () const — Clears the halt state of the endpoint.

## Detailed Member Documentation

### `BulkTransfer()`

```cpp
ssize_t BUSBEndpoint::BulkTransfer(void * data, size_t length)const
```

Perform a bulk transfer operation. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The data buffer you want to pass. |
| `length` | The size of the data buffer. |





**Returns:** The actual number of bytes written or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | *data* is `NULL` |
| B_ERROR | The request failed. |





**Since:** Haiku R1

---

### `ClearStall()`

```cpp
status_t BUSBEndpoint::ClearStall()const
```

Clears the halt state of the endpoint. 



**Since:** Haiku R1

---

### `Configuration()`

```cpp
const BUSBConfiguration * BUSBEndpoint::Configuration()const
```

Convenience method to directly reach the parent configuration of this endpoint. 



**Since:** Haiku R1

---

### `ControlTransfer()`

```cpp
ssize_t BUSBEndpoint::ControlTransfer(uint8 requestType, uint8 request, uint16 value, uint16 index, uint16 length, void * data)const
```

Perform a control transfer operation. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `requestType` | The request type. |
| `request` | The request you want to perform. |
| `value` | The value of the request. |
| `index` | The index of the request. |
| `length` | The size of the buffer pointed by *data*. |
| `data` | The buffer where to write the result. |





**Returns:** The actual number of bytes written or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | *data* is `NULL` |
| B_ERROR | The request failed. |





**Since:** Haiku R1

---

### `Descriptor()`

```cpp
const usb_endpoint_descriptor * BUSBEndpoint::Descriptor()const
```

Returns a pointer to a usb_endpoint_descriptor instance with the descriptor of this endpoint. 



**Since:** Haiku R1

---

### `Device()`

```cpp
const BUSBDevice * BUSBEndpoint::Device()const
```

Convenience method to directly reach the parent device of this endpoint. 



**Since:** Haiku R1

---

### `Index()`

```cpp
uint32 BUSBEndpoint::Index()const
```

Returns the index of the endpoint in the list of endpoints of the parent interface. 



**Since:** Haiku R1

---

### `Interface()`

```cpp
const BUSBInterface * BUSBEndpoint::Interface()const
```

Returns the parent interface of this endpoint. 



**Since:** Haiku R1

---

### `InterruptTransfer()`

```cpp
ssize_t BUSBEndpoint::InterruptTransfer(void * data, size_t length)const
```

Perform an interrupt transfer operation. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The data buffer you want to pass. |
| `length` | The size of the data buffer. |





**Returns:** The actual number of bytes written or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | *data* is `NULL` |
| B_ERROR | The request failed. |





**Since:** Haiku R1

---

### `Interval()`

```cpp
uint8 BUSBEndpoint::Interval()const
```

Returns the polling interval of this endpoint for data transfers. 



**Since:** Haiku R1

---

### `IsBulk()`

```cpp
bool BUSBEndpoint::IsBulk()const
```

Returns if the transfer type is bulk. 



**Since:** Haiku R1

---

### `IsControl()`

```cpp
bool BUSBEndpoint::IsControl()const
```

Returns if the transfer type is control. 



**Since:** Haiku R1

---

### `IsInput()`

```cpp
bool BUSBEndpoint::IsInput()const
```

Returns if the address direction is input. 



**Since:** Haiku R1

---

### `IsInterrupt()`

```cpp
bool BUSBEndpoint::IsInterrupt()const
```

Returns if the transfer type is interrupt. 



**Since:** Haiku R1

---

### `IsIsochronous()`

```cpp
bool BUSBEndpoint::IsIsochronous()const
```

Returns if the transfer type is isochronous. 



**Since:** Haiku R1

---

### `IsochronousTransfer()`

```cpp
ssize_t BUSBEndpoint::IsochronousTransfer(void * data, size_t length, usb_iso_packet_descriptor * packetDescriptors, uint32 packetCount)const
```

Perform an isochronous transfer operation. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The data buffer you want to pass. |
| `length` | The size of the data buffer. |
| `packetDescriptors` | Packet descriptors for the isochronous request. |
| `packetCount` | The number of entries in *packetDescriptors*. |





**Returns:** The actual number of bytes written or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | *data* is `NULL` |
| B_ERROR | The request failed. |





**Since:** Haiku R1

---

### `IsOutput()`

```cpp
bool BUSBEndpoint::IsOutput()const
```

Returns if the address direction is output. 



**Since:** Haiku R1

---

### `IsStalled()`

```cpp
bool BUSBEndpoint::IsStalled()const
```

Gets the halt state of the endpoint. 



**Since:** Haiku R1

---

### `MaxPacketSize()`

```cpp
uint16 BUSBEndpoint::MaxPacketSize()const
```

Returns the maximum packet size that this endpoint is able to receive or send. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBUSBEndpoint.html).
