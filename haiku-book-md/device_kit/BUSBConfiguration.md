---
name: BUSBConfiguration
type: class
kit: device_kit
brief: "Represents one of possibly multiple configurations a device might have"
source: haiku-book
---

# BUSBConfiguration Class
**Kit/Group:** [Device Kit](../device_kit/group__device.md) | [Device Kit library (libdevice.so)](group__libdevice.md)

## Description

Represents one of possibly multiple configurations a device might have. 


The only way to get a valid object is through [BUSBDevice::ConfigurationAt()](classBUSBDevice.md#ad3991b7b9dfe2ae71ed7aa8c7a592432) or [BUSBDevice::ActiveConfiguration()](classBUSBDevice.md#a0db6e3b9a35de944b31f70576be09de9).


[BUSBConfiguration](classBUSBConfiguration.md) provides further access into the configuration by providing [CountInterfaces()](classBUSBConfiguration.md#a78750b0a3e032c0dff4312d4fee2aa7d) and [InterfaceAt()](classBUSBConfiguration.md#a8696e3c3dc6af83408dcf48b7041679b) to retrieve [BUSBInterface](classBUSBInterface.md) objects.



**Since:** Haiku R1

## Member List

### Public Member Functions

* `const char *` [ConfigurationString](#a6718b48a303fbfbf57920e08be454d72) () const — Gets a descriptive string for this configuration.
* `uint32` [CountInterfaces](#a78750b0a3e032c0dff4312d4fee2aa7d) () const — Returns the number of child interfaces within this configuration.
* `const usb_configuration_descriptor *` [Descriptor](#a01982e6886751523aa0a3a50c038334a) () const — Returns a pointer to a usb_configuration_descriptor instace with the descriptor of this configuration.
* `const BUSBDevice *` [Device](#a14d34b9ba012050068d614a3e5342e87) () const — Returns the parent device of this configuration.
* `uint32` [Index](#a4110a76a415ed94791134f7f49bf5982) () const — Returns the index of this configuration within the configurations list in Device().
* `const BUSBInterface *` [InterfaceAt](#a8696e3c3dc6af83408dcf48b7041679b) (uint32 index) const — Returns the child interface of this configuration at the given index.

## Detailed Member Documentation

### `ConfigurationString()`

```cpp
const char * BUSBConfiguration::ConfigurationString()const
```

Gets a descriptive string for this configuration. 


If it is not available, an empty string is returned.



**Since:** Haiku R1

---

### `CountInterfaces()`

```cpp
uint32 BUSBConfiguration::CountInterfaces()const
```

Returns the number of child interfaces within this configuration. 



**Since:** Haiku R1

---

### `Descriptor()`

```cpp
const usb_configuration_descriptor * BUSBConfiguration::Descriptor()const
```

Returns a pointer to a usb_configuration_descriptor instace with the descriptor of this configuration. 



**Since:** Haiku R1

---

### `Device()`

```cpp
const BUSBDevice * BUSBConfiguration::Device()const
```

Returns the parent device of this configuration. 



**Since:** Haiku R1

---

### `Index()`

```cpp
uint32 BUSBConfiguration::Index()const
```

Returns the index of this configuration within the configurations list in [Device()](classBUSBConfiguration.md#a14d34b9ba012050068d614a3e5342e87). 



**Since:** Haiku R1

---

### `InterfaceAt()`

```cpp
const BUSBInterface * BUSBConfiguration::InterfaceAt(uint32 index)const
```

Returns the child interface of this configuration at the given *index*. 


If the *index* is invalid (see [CountInterfaces()](classBUSBConfiguration.md#a78750b0a3e032c0dff4312d4fee2aa7d)) or there are no child interfaces, it returns `NULL`.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBUSBConfiguration.html).
