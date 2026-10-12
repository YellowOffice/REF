---
name: BJoystick
type: class
kit: device_kit
brief: "Class that provides an interface to joysticks and game controllers"
source: haiku-book
---

# BJoystick Class
**Kit/Group:** [Device Kit](../device_kit/group__device.md) | [Device Kit library (libdevice.so)](group__libdevice.md)

## Description

Class that provides an interface to joysticks and game controllers. 


This class allows application to access the data from game controllers of any type (joysticks, gamepads, racing wheels, etc). It provides discovery of the button configuration and axis layout and reports the status of the buttons and position of the axis. There is also support for enumerating the available controllers.


Joysticks can be accessed in two modes called standard and enhanced. The standard mode is for compatibility with the BeBox joysticks and is not implemented in Haiku. New applications should use the enhanced mode.

## Member List

### Public Member Functions

* `int32` [CountDevices](#acc54ce01e639035b9a428877dcdeca57) () — Count the number of joysticks connected.
* `status_t` [Open](#a474a4b77443c9202caf82aec0a590762) (const char *portName, bool enhanced) — Open a specific game port.

## Detailed Member Documentation

### `CountDevices()`

```cpp
int32 BJoystick::CountDevices()
```

Count the number of joysticks connected. 



**Returns:** The number of joystick devices connected to the computer.

---

### `Open()`

```cpp
status_t BJoystick::Open(const char * portname, bool enhanced)
```

Open a specific game port. 


This method can be used to open the game port specified by the parameter `portname` amd also allows you to specify whether to use enhanced mode or not. The port name can be either an absolute path to the game port device, or only the device file name.


Enhanced mode adds support for more than 32 buttons per joystick, and an unlimited number of axes and thumb controls. To support this, several functions allow to get information about the device, such as the button count, the name of each button, and the number and name of the axis.


Parameters

| Parameter | Description |
| :--- | :--- |
| `portname` | The name of the game port to be opened. |
| `enhanced` | Specifies whether to use enhanced mode while opening the port. |





**Returns:** B_BAD_VALUE if portname is null.

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBJoystick.html).
