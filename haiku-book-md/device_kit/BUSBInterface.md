---
name: BUSBInterface
type: class
kit: device_kit
brief: "Represents an interface of a configuration in a USB device"
source: haiku-book
---

# BUSBInterface Class
**Kit/Group:** [Device Kit](../device_kit/group__device.md) | [Device Kit library (libdevice.so)](group__libdevice.md)

## Description

Represents an interface of a configuration in a USB device. 


This class can be used to access the descriptor fields of an underlying USB interface. In addition, it can be used to iterate over and retrieve [BUSBEndpoint](classBUSBEndpoint.md) objects that can be used to transfer data over the bus.



**Since:** Haiku R1

## Member List

### Public Member Functions

* `uint32` [Index](#ad7d1d98c7d09afbfd35f65d2cc12dd50) () const — Returns the index in the interfaces list of the parent configuration.
* `uint32` [AlternateIndex](#a274d0f1523d1f50dd92db3de854c239c) () const — Returns the alternate interface index.
* `const BUSBConfiguration *` [Configuration](#abde551a78be3041d8aaa3bf3fafdb6b3) () const — Returns a pointer to the parent configuration of this interface.
* `const BUSBDevice *` [Device](#a3412620265d014d3d0e443eb2dfe8c1c) () const — Convenience method to directly return the parent device of this interface.
* `uint8` [Class](#a77f4adbdc47dd9800172ce998cddb347) () const — Returns the class of the interface.
* `uint8` [Subclass](#a9987a7d76f5c23e8da66a233ce8936f8) () const — Returns the subclass of the interface.
* `uint8` [Protocol](#a5c944a3914f1ca11120657d623ca1be8) () const — Returns the protocol of the interface.
* `const char *` [InterfaceString](#ad94f2b967ea95f1cdaafd6eb925c4532) () const — Returns a descriptive string for the interface.
* `const usb_interface_descriptor *` [Descriptor](#a7ec356f59353b09e111790f959ef1541) () const — Returns a pointer to a usb_interface_descriptor with the descriptor of this interface.
* `status_t` [OtherDescriptorAt](#a829049fcac8ee483e0a70dcfd7b777b5) (uint32 index, usb_descriptor *descriptor, size_t length) const — Gets generic descriptors for an interface.
* `uint32` [CountEndpoints](#a2b2caffccacd16c1d12e2b26bbbe41d2) () const — Returns the number of endpoints available in this interface.
* `const BUSBEndpoint *` [EndpointAt](#ad82786bc4f6566ee263f1a0ac63d7dc1) (uint32 index) const — Returns a pointer to the endpoint at the given index.
* `uint32` [CountAlternates](#a823bb409d0963a29f146a215eda2f88f) () const — Returns the number of alternate interfaces for this interface.
* `uint32` [ActiveAlternateIndex](#a4ff8c7e51a478cb406cd1952be456540) () const — Returns the index of the currently active alternate interface.
* `const BUSBInterface *` [AlternateAt](#ae0684734eb5b9edb1ec8193c76a645ea) (uint32 alternateIndex) const — Returns the interface descriptor of the alternate interface with the specified index.
* `status_t` [SetAlternate](#a09557503689826563dc9a22667f225c4) (uint32 alternateIndex) — Switches this object to the alternate interface at alternateIndex.

## Detailed Member Documentation

### `ActiveAlternateIndex()`

```cpp
uint32 BUSBInterface::ActiveAlternateIndex()const
```

Returns the index of the currently active alternate interface. 



**Since:** Haiku R1

---

### `AlternateAt()`

```cpp
const BUSBInterface * BUSBInterface::AlternateAt(uint32 alternateIndex)const
```

Returns the interface descriptor of the alternate interface with the specified index. 


This allows to peek at the attributes of that alternate (including endpoints) without having to switch to this alternate interface.


Note that you cannot use any endpoint you retrieve through an interface you get through [AlternateAt()](classBUSBInterface.md#ae0684734eb5b9edb1ec8193c76a645ea). Even if you switch to that alternate later on, you cannot use an interface returned by [AlternateAt()](classBUSBInterface.md#ae0684734eb5b9edb1ec8193c76a645ea). Instead switch to that alternate using the interface you got from the configuration and then use this switched interface to enumerate the endpoints.


Parameters

| Parameter | Description |
| :--- | :--- |
| `alternateIndex` | The index of the alternate interface. |





**Since:** Haiku R1

---

### `AlternateIndex()`

```cpp
uint32 BUSBInterface::AlternateIndex()const
```

Returns the alternate interface index. 



**Since:** Haiku R1

---

### `Class()`

```cpp
uint8 BUSBInterface::Class()const
```

Returns the class of the interface. 



**Since:** Haiku R1

---

### `Configuration()`

```cpp
const BUSBConfiguration * BUSBInterface::Configuration()const
```

Returns a pointer to the parent configuration of this interface. 



**Since:** Haiku R1

---

### `CountAlternates()`

```cpp
uint32 BUSBInterface::CountAlternates()const
```

Returns the number of alternate interfaces for this interface. 


Note that this interface itself counts as an alternate so an alternate count of one really means that you are currently using the sole interface present.



**Since:** Haiku R1

---

### `CountEndpoints()`

```cpp
uint32 BUSBInterface::CountEndpoints()const
```

Returns the number of endpoints available in this interface. 



**Since:** Haiku R1

---

### `Descriptor()`

```cpp
const usb_interface_descriptor * BUSBInterface::Descriptor()const
```

Returns a pointer to a usb_interface_descriptor with the descriptor of this interface. 



**Since:** Haiku R1

---

### `Device()`

```cpp
const BUSBDevice * BUSBInterface::Device()const
```

Convenience method to directly return the parent device of this interface. 



**Since:** Haiku R1

---

### `EndpointAt()`

```cpp
const BUSBEndpoint * BUSBInterface::EndpointAt(uint32 index)const
```

Returns a pointer to the endpoint at the given *index*. 


This is the only valid way to get [BUSBEndpoint](classBUSBEndpoint.md) object.


Note that these objects will get invalid and deleted as soon as the parent interface is deleted.


If *index* is invalid or there are no endpoints, this will return `NULL`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index of the endpoint. |





**Since:** Haiku R1

---

### `Index()`

```cpp
uint32 BUSBInterface::Index()const
```

Returns the index in the interfaces list of the parent configuration. 



**Since:** Haiku R1

---

### `InterfaceString()`

```cpp
const char * BUSBInterface::InterfaceString()const
```

Returns a descriptive string for the interface. 


If there is no string available it returns an empty string.



**Since:** Haiku R1

---

### `OtherDescriptorAt()`

```cpp
status_t BUSBInterface::OtherDescriptorAt(uint32 index, usb_descriptor * descriptor, size_t length)const
```

Gets generic descriptors for an interface. 


These are usually device/interface class specific or they may represent vendor specific extensions.


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index of the generic descriptor. |
| `descriptor` | A pointer to a pre-allocated usb_descriptor instance where to write the data. |
| `length` | The size of *descriptor*. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Operation performed successfully. |
| B_BAD_VALUE | *descriptor* is `NULL` or *length* is invalid (less than or equal to zero). |
| B_ERROR | The descriptor could not be fetched. |





**Since:** Haiku R1

---

### `Protocol()`

```cpp
uint8 BUSBInterface::Protocol()const
```

Returns the protocol of the interface. 



**Since:** Haiku R1

---

### `SetAlternate()`

```cpp
status_t BUSBInterface::SetAlternate(uint32 alternateIndex)
```

Switches this object to the alternate interface at *alternateIndex*. 


Note that all endpoints retrieved through [EndpointAt()](classBUSBInterface.md#ad82786bc4f6566ee263f1a0ac63d7dc1) will become invalid and will be deleted as soon as you set an alternate interface (even if the resulting interface is the same you were using before).


Parameters

| Parameter | Description |
| :--- | :--- |
| `alternateIndex` | The index of the alternate interface to switch into. |





**Since:** Haiku R1

---

### `Subclass()`

```cpp
uint8 BUSBInterface::Subclass()const
```

Returns the subclass of the interface. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBUSBInterface.html).
