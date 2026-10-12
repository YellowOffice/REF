---
name: BUSBDevice
type: class
kit: device_kit
brief: "Represents an interface to a USB device"
source: haiku-book
---

# BUSBDevice Class
**Kit/Group:** [Device Kit](../device_kit/group__device.md) | [Device Kit library (libdevice.so)](group__libdevice.md)

## Description

Represents an interface to a USB device. 


You can either get it through the [BUSBRoster](classBUSBRoster.md) or by creating one yourself and setting it to a valid raw usb device (with a path of `"/dev/bus/usb/x"`).


The device class provides direct accessors for descriptor fields as well as convenience functions to directly get string representations of fields. The [BUSBDevice](classBUSBDevice.md) also provides access for the [BUSBConfiguration](classBUSBConfiguration.md) objects of a device. These objects and all of their child objects depend on the parent device and will be deleted as soon as the device object is destroyed.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BUSBDevice](#a91d4447cba26b952d39a173a903373da) (const char *path=NULL) — Initializes the USB device with path.
* `virtual` [~BUSBDevice](#a7364f8894c994850c19f47a560c4f063) () — Releases all the allocated resources by this object.
* `virtual status_t` [InitCheck](#af7f495edd7857a1d01ae71b0bd5deb21) () — Checks the object initialization status.
* `bool` [IsHub](#a79f30405bab3c37dfc23828c1a40f85e) () const — Returns true if the device is a USB hub or false otherwise.
* `const char *` [Location](#abf96fec50ac20108856e00938ce8bcbf) () const — Returns the location on the bus represented as hub/device sequence.
* `status_t` [SetTo](#adebb01501404c73a103b0251861cb6e1) (const char *path) — (Re)initializes the object to the device with path.
* `void` [Unset](#a3b1865a4c99a7001ecb0bc81d7a24322) () — Uninitializes the object.
* `uint16` [USBVersion](#a5e9e0eebf404375a1fbfe9046b1378af) () const — Returns the minimum USB version supported by the device.
* `uint8` [Class](#a2b1c58c595a5be6a3cd43f7c07f60a6d) () const — Returns the USB device class.
* `uint8` [Subclass](#acfd31bdfb0b1e91fe90490692314cebe) () const — Returns the USB device subclass.
* `uint8` [Protocol](#a8bea595ec4fb1c38fe5fea3ada46d811) () const — Returns the device protocol.
* `uint8` [MaxEndpoint0PacketSize](#ad7b2ee9ac5d7973a6886df84d6636ccd) () const — Returns the max packet size for the endpoint 0.
* `uint16` [VendorID](#abb01d25b798600b8a9f368995fce1764) () const — Returns the vendor identifier.
* `uint16` [ProductID](#a6e0579d38520fff97bfa597189ce7ccf) () const — Returns the product identifier.
* `uint16` [Version](#a1e379388a9d795a4bf388567c0f8be5f) () const — Returns the device version.
* `const char *` [ManufacturerString](#aafebead610e2fef88dfbc99c44063f72) () const — Returns a string of the manufacturer name.
* `const char *` [ProductString](#a0f3070eec634fce56f682fe2280df829) () const — Returns a string of the product name.
* `const char *` [SerialNumberString](#a4ca64ae0b65453c3eec354b05d8101a4) () const — Returns a string of the serial number.
* `const usb_device_descriptor *` [Descriptor](#ac9aa6594d05516d4c8df77df658ef99e) () const — Returns a pointer to the device descriptor.
* `size_t` [GetStringDescriptor](#a0b57b558ac433d8930965106c8411723) (uint32 index, usb_string_descriptor *descriptor, size_t length) const — Retrieves the raw usb_string_descriptor at the given index.
* `char *` [DecodeStringDescriptor](#a9b0a31fee10ad1b9a7ff73a1ddbdef42) (uint32 index) const — Convenience method to get a null terminated C string for the given string index.
* `size_t` [GetDescriptor](#a8b7b5f5794c3ee044ac1d4b63ff77aa5) (uint8 type, uint8 index, uint16 languageID, void *data, size_t length) const — Gets the descriptor with type and languageID at index.
* `uint32` [CountConfigurations](#a982f97f1c568e3c73cc9041ebd88d9fa) () const — Returns the number of configurations that the device contains.
* `const BUSBConfiguration *` [ConfigurationAt](#ad3991b7b9dfe2ae71ed7aa8c7a592432) (uint32 index) const — Returns the device configuration at the given index.
* `const BUSBConfiguration *` [ActiveConfiguration](#a0db6e3b9a35de944b31f70576be09de9) () const — Returns the active device configuration.
* `status_t` [SetConfiguration](#a6de00cba988d27099d20a07845d58c42) (const BUSBConfiguration *configuration) — Activates a device configuration in the USB device.
* `ssize_t` [ControlTransfer](#a247d15c7765f82c1cd6c156ee50a739a) (uint8 requestType, uint8 request, uint16 value, uint16 index, uint16 length, void *data) const — Sends a request to the device using the default pipe.

## Detailed Member Documentation

### `BUSBDevice()`

```cpp
BUSBDevice::BUSBDevice(const char * path = NULL)
```

Initializes the USB device with *path*. 


You should check if the object was initialized successfully by calling [InitCheck()](classBUSBDevice.md#af7f495edd7857a1d01ae71b0bd5deb21).


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The path of the USB device. |





**See also:** [SetTo()](classBUSBDevice.md#adebb01501404c73a103b0251861cb6e1)



**Since:** Haiku R1

---

### `~BUSBDevice()`

```cpp
BUSBDevice::~BUSBDevice()
```

Releases all the allocated resources by this object. 



**Since:** Haiku R1

---

### `ActiveConfiguration()`

```cpp
const BUSBConfiguration * BUSBDevice::ActiveConfiguration()const
```

Returns the active device configuration. 



**Returns:** A read-only pointer to the current configuration or `NULL` if there are no configurations.



**Since:** Haiku R1

---

### `Class()`

```cpp
uint8 BUSBDevice::Class()const
```

Returns the USB device class. 



**Since:** Haiku R1

---

### `ConfigurationAt()`

```cpp
const BUSBConfiguration * BUSBDevice::ConfigurationAt(uint32 index)const
```

Returns the device configuration at the given *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index of the configuration. |





**Returns:** A read-only pointer to the configuration at *index* or `NULL` if the index number is invalid or there are no configurations.



**Since:** Haiku R1

---

### `ControlTransfer()`

```cpp
ssize_t BUSBDevice::ControlTransfer(uint8 requestType, uint8 request, uint16 value, uint16 index, uint16 length, void * data)const
```

Sends a request to the device using the default pipe. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `requestType` | The request type. |
| `request` | The request you want to perform. |
| `value` | The value of the request. |
| `index` | The index of the request. |
| `length` | The size of the *data* buffer. |
| `data` | The buffer where to write the result in. |





**Returns:** The amount of data written or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | *data* is `NULL`. |
| B_ERROR | The operation request failed. |





**Since:** Haiku R1

---

### `CountConfigurations()`

```cpp
uint32 BUSBDevice::CountConfigurations()const
```

Returns the number of configurations that the device contains. 



**Since:** Haiku R1

---

### `DecodeStringDescriptor()`

```cpp
char * BUSBDevice::DecodeStringDescriptor(uint32 index)const
```

Convenience method to get a null terminated C string for the given string *index*. 


Notice that this will allocate memory on the heap for the returned string. The caller needs to delete it to release the memory.


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index of the string. |





**Since:** Haiku R1

---

### `Descriptor()`

```cpp
const usb_device_descriptor * BUSBDevice::Descriptor()const
```

Returns a pointer to the device descriptor. 



**Since:** Haiku R1

---

### `GetDescriptor()`

```cpp
size_t BUSBDevice::GetDescriptor(uint8 type, uint8 index, uint16 languageID, void * data, size_t length)const
```

Gets the descriptor with *type* and *languageID* at *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The descriptor type. |
| `index` | The index of the descriptor to get. |
| `languageID` | The language identifier of the descriptor. |
| `data` | A pre-allocated buffer where to write the descriptor into. |
| `length` | The *data* buffer size. |





**Returns:** The amount of data written or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| 0 | The operation could not be performed. |
| B_BAD_VALUE | *data* is `NULL`. |





**Since:** Haiku R1

---

### `GetStringDescriptor()`

```cpp
size_t BUSBDevice::GetStringDescriptor(uint32 index, usb_string_descriptor * descriptor, size_t length)const
```

Retrieves the raw usb_string_descriptor at the given *index*. 


The string contained is usually two-byte unicode encoded.


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index of the string. |
| `descriptor` | A pointer to a pre-allocated usb_string_descriptor instance to write the data into. |
| `length` | The length of *descriptor*. |





**Returns:** The length of the string or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| 0 | The string descriptor could not be retrieved. |
| B_BAD_VALUE | *descriptor* is `NULL`. |





**Since:** Haiku R1

---

### `InitCheck()`

```cpp
status_t BUSBDevice::InitCheck()
```

Checks the object initialization status. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object was initialized to the given device path. |
| B_ERROR | The object is not initialized properly or the path of the device does not exist. |





**Since:** Haiku R1

---

### `IsHub()`

```cpp
bool BUSBDevice::IsHub()const
```

Returns `true` if the device is a USB hub or `false` otherwise. 



**Since:** Haiku R1

---

### `Location()`

```cpp
const char * BUSBDevice::Location()const
```

Returns the location on the bus represented as hub/device sequence. 



**Since:** Haiku R1

---

### `ManufacturerString()`

```cpp
const char * BUSBDevice::ManufacturerString()const
```

Returns a string of the manufacturer name. 


If a string for the manufacturer is not available in the descriptor data, an empty string is returned.



**Since:** Haiku R1

---

### `MaxEndpoint0PacketSize()`

```cpp
uint8 BUSBDevice::MaxEndpoint0PacketSize()const
```

Returns the max packet size for the endpoint 0. 



**Since:** Haiku R1

---

### `ProductID()`

```cpp
uint16 BUSBDevice::ProductID()const
```

Returns the product identifier. 



**Since:** Haiku R1

---

### `ProductString()`

```cpp
const char * BUSBDevice::ProductString()const
```

Returns a string of the product name. 


If a string for the product name is not available in the descriptor data, an empty string is returned.



**Since:** Haiku R1

---

### `Protocol()`

```cpp
uint8 BUSBDevice::Protocol()const
```

Returns the device protocol. 



**Since:** Haiku R1

---

### `SerialNumberString()`

```cpp
const char * BUSBDevice::SerialNumberString()const
```

Returns a string of the serial number. 


If a string for the serial number is not available in the descriptor data, an empty string is returned.



**Since:** Haiku R1

---

### `SetConfiguration()`

```cpp
status_t BUSBDevice::SetConfiguration(const BUSBConfiguration * configuration)
```

Activates a device configuration in the USB device. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `configuration` | A pointer to a [BUSBConfiguration](classBUSBConfiguration.md) with the configuration data. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The configuration was activated successfully. It has become the active configuration. |
| B_BAD_VALUE | `configuration` is NULL, or the index value of it is out of range (see [CountConfigurations()](classBUSBDevice.md#a982f97f1c568e3c73cc9041ebd88d9fa)). |
| B_ERROR | There was an error trying to activate the configuration. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BUSBDevice::SetTo(const char * path)
```

(Re)initializes the object to the device with *path*. 


If it was opened successfully, this will load the device descriptor and the associated device configurations.


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The path of the USB device. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Initialization successful and device opened. |
| B_BAD_VALUE | The device *path* is `NULL`. |
| B_ERROR | The device *path* could not be opened, or the USB version or descriptor for the device could not be retrieved. |
| B_NO_MEMORY | Internal memory error trying to get device configurations. |





**Since:** Haiku R1

---

### `Subclass()`

```cpp
uint8 BUSBDevice::Subclass()const
```

Returns the USB device subclass. 



**Since:** Haiku R1

---

### `Unset()`

```cpp
void BUSBDevice::Unset()
```

Uninitializes the object. 



**Since:** Haiku R1

---

### `USBVersion()`

```cpp
uint16 BUSBDevice::USBVersion()const
```

Returns the minimum USB version supported by the device. 



**Since:** Haiku R1

---

### `VendorID()`

```cpp
uint16 BUSBDevice::VendorID()const
```

Returns the vendor identifier. 



**Since:** Haiku R1

---

### `Version()`

```cpp
uint16 BUSBDevice::Version()const
```

Returns the device version. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBUSBDevice.html).
