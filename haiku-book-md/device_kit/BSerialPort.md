---
name: BSerialPort
type: class
kit: device_kit
brief: "BSerialPort provides an interface for communicating with devices connected through a serial port"
source: haiku-book
---

# BSerialPort Class
**Kit/Group:** [Device Kit](../device_kit/group__device.md) | [Device Kit library (libdevice.so)](group__libdevice.md)

## Description

[BSerialPort](classBSerialPort.md) provides an interface for communicating with devices connected through a serial port. 


To start a connection with a serial port:


* Create a [BSerialPort](classBSerialPort.md) object

* Use [Open()](classBSerialPort.md#a80fc7eafd3b57f4888df6a6074447fae) to open a specific serial port

* If the port is successfully open, use [Read()](classBSerialPort.md#aba570b16b6080f86695b171eefe8d99b) and [Write()](classBSerialPort.md#a5d19c23626f6be250264f0e7c6f1d3f4) to communicate.



For example: 


```cpp
status_t
SendDataToSerialPort(const char* port, const void* data, size_t length)
{
 // Creates an object and configures it.
 // At this point the object is not yet connected to any serial port
 BSerialPort serialPort;
    serialPort.SetDataRate(B_57600_BPS);
    serialPort.SetFlowControl(B_SOFTWARE_CONTROL);
 
 // Opens the serial port
 if (serialPort.Open(port) <= 0)
 return B_ERROR;
 
 // Performs any operations...
    ssize_t writtenBytes = serialPort.Write(data, length);
 
 // ...
 
    serialPort.Close();
 return (writtenBytes >= 0) ? B_OK : B_IO_ERROR;
}
```

To know which serial ports are available to the system, the methods [CountDevices()](classBSerialPort.md#a0b8d0e706fc45d858d97646eaabda44f) and [GetDeviceName()](classBSerialPort.md#ab8005aa62457c0f0ff1e748d0bb8be0a) allow to retrieve a list of them:



```cpp
void
GetSerialPortsNames(BStringList& outPortList)
{
 BSerialPort serialPort;
 char portName[B_OS_NAME_LENGTH]; // Ports paths temporary storage
 
    outPortList.MakeEmpty();
 
 for (int32 i = 0; i < serialPort.CountDevices(); i++) {
 // For each found port...
 if (serialPort.GetDeviceName(i, portName) == B_OK) {
 // try to open it to know if it is available to us
 if (serialPort.Open(portName) > 0) {
 // Add it to the list because we can access it,
 // and close it so we can test the next
                outPortList.Add(portName);
                serialPort.Close();
            }
        }
    }
}
```


**Since:** BeOS R3

## Member List

### Public Member Functions

* [BSerialPort](#a37931d33e8d644735b7e5bf401c36785) () — Creates and initializes a BSerialPort object.
* `virtual` [~BSerialPort](#a567fa36f2d1ec69e3fc5ead87a52d084) () — Frees the resources associated with the object.
* `void` [ClearInput](#a258eb7e0b2fc93794920dc75ae1194eb) () — Clears the input buffer. This discards the data received but not read by Read().
* `void` [ClearOutput](#aa9dba99b5a072a46eaa058858c4a5acd) () — Clears the output buffer. This discards the data written to the output buffer with Write() but not yet transmitted to the other endpoint.
* `void` [Close](#a351d27d69efbf7952776dae99323b683) () — Closes the port.
* `int32` [CountDevices](#a0b8d0e706fc45d858d97646eaabda44f) () — Counts the number of available serial ports.
* `data_bits` [DataBits](#a2803472667f85735953d7d5c6e2f68a8) () — Gets the current data bits.
* `data_rate` [DataRate](#ac1af51293f4f7349f8ccf5debdfe108e) () — Gets the current baud rate.
* `uint32` [FlowControl](#ab4903e944fb8d087eaab18e84bd79da3) () — Returns the selected flow control.
* `status_t` [GetDeviceName](#ab8005aa62457c0f0ff1e748d0bb8be0a) (int32 index, char *name, size_t bufSize=B_OS_NAME_LENGTH) — Gets the device name by the given index.
* `bool` [IsCTS](#a2afac55951f91a84a14cc3df383682c7) () — Checks if the Clear To Send (CTS) pin is asserted (in an active state).
* `bool` [IsDCD](#a14976b72bb302f43c89b6c01e1a3359c) () — Checks if the Data Carrier Detect (DCD) pin is asserted (in an active state).
* `bool` [IsDSR](#a4368a32509b7b7b77c14688955417386) () — Checks if the Data Set Ready (DSR) pin is asserted (in an active state).
* `bool` [IsRI](#a346ff107b5108bafbb70a3e155cfb0f8) () — Checks if the Ring Indicator (RI) pin is asserted (in an active state).
* `status_t` [NumCharsAvailable](#aabf1b491ec2a10d79e03c2f8689732eb) (int32 *waitThisMany) — Unimplemented.
* `status_t` [Open](#a80fc7eafd3b57f4888df6a6074447fae) (const char *portName) — Opens a serial port represented by portName.
* `parity_mode` [ParityMode](#ae4e24ff2aa599a283886fb1337f3afe6) () — Gets the parity mode.
* `ssize_t` [Read](#aba570b16b6080f86695b171eefe8d99b) (void *buf, size_t count) — Reads some bytes from the serial port.
* `void` [SetBlocking](#ae0bec0386c30dbd6b6b587699cbf7ad4) (bool blocking) — Sets the blocking mode.
* `void` [SetDataBits](#aed0d5a7e0bf182c146b4b147bd82f26b) (data_bits numBits) — Sets the data bits.
* `status_t` [SetDataRate](#ad404a2c9f62c419e8b6b527d5523401c) (data_rate bitsPerSecond) — Sets the baud rate for the port.
* `status_t` [SetDTR](#a151f9e163914a728e871100561e22a66) (bool asserted) — Sets the Data Terminal Ready (DTR) pin active if asserted is true, or inactive if it is false.
* `void` [SetFlowControl](#a4f0336ec0ed3f45b52155830e8a52649) (uint32 method) — Sets the flow control.
* `void` [SetParityMode](#ae3510987436c10b6a3a2a6d116c047ae) (parity_mode which) — Sets the parity mode.
* `status_t` [SetRTS](#a762354fefea8ef6561017c9d481f9164) (bool asserted) — Sets the Request To Send (RTS) pin active if asserted is true, or inactive if it is false.
* `void` [SetStopBits](#af41210945a951619018ac16a939fffa8) (stop_bits numBits) — Sets the stop bits.
* `status_t` [SetTimeout](#ae9ed661337c7aa33cadb225f666f6fea) (bigtime_t microSeconds) — Sets the timeout period for how long Read() and WaitForInput() will wait for the data to arrive to the port's input buffer before returning.
* `stop_bits` [StopBits](#a22bbb23e861cf6d95113f57f52db6862) () — Gets the current stop bits.
* `ssize_t` [WaitForInput](#ae8a14f3889f8133377920d040f0fb21d) () — Waits until there is something to read from the serial port.
* `ssize_t` [Write](#a5d19c23626f6be250264f0e7c6f1d3f4) (const void *buf, size_t count) — Writes some bytes to the serial port.

## Detailed Member Documentation

### `BSerialPort()`

```cpp
BSerialPort::BSerialPort()
```

Creates and initializes a [BSerialPort](classBSerialPort.md) object. 


Queries the driver, and builds a list of the available serial ports. The [BSerialPort](classBSerialPort.md) object is initialized to these values:


* `B_19200_BPS`

* `B_DATA_BITS_8`

* `B_STOP_BIT_1`

* `B_NO_PARITY`

* `B_HARDWARE_CONTROL`

* `B_INFINITE_TIMEOUT`

* Blocking mode enabled



At this point the object does not have any specific serial port selected. To connect and work with a serial port it has to be opened using [Open()](classBSerialPort.md#a80fc7eafd3b57f4888df6a6074447fae).



**Since:** BeOS R3

---

### `~BSerialPort()`

```cpp
BSerialPort::~BSerialPort()
```

Frees the resources associated with the object. 


Closes the port, if it is open, and deletes the devices list.



**Since:** BeOS R3

---

### `ClearInput()`

```cpp
void BSerialPort::ClearInput()
```

Clears the input buffer. This discards the data received but not read by [Read()](classBSerialPort.md#aba570b16b6080f86695b171eefe8d99b). 



**Since:** BeOS R3

---

### `ClearOutput()`

```cpp
void BSerialPort::ClearOutput()
```

Clears the output buffer. This discards the data written to the output buffer with [Write()](classBSerialPort.md#a5d19c23626f6be250264f0e7c6f1d3f4) but not yet transmitted to the other endpoint. 



**Since:** BeOS R3

---

### `Close()`

```cpp
void BSerialPort::Close()
```

Closes the port. 



**See also:** [Open()](classBSerialPort.md#a80fc7eafd3b57f4888df6a6074447fae)



**Since:** BeOS R3

---

### `CountDevices()`

```cpp
int32 BSerialPort::CountDevices()
```

Counts the number of available serial ports. 



**Returns:** An integer which represents the number of available serial ports.



**See also:** [GetDeviceName()](classBSerialPort.md#ab8005aa62457c0f0ff1e748d0bb8be0a)



**Since:** BeOS R3

---

### `DataBits()`

```cpp
data_bits BSerialPort::DataBits()
```

Gets the current data bits. 



**Returns:** The current data bits.



**See also:** [SetDataBits()](classBSerialPort.md#aed0d5a7e0bf182c146b4b147bd82f26b)



**Since:** BeOS R3

---

### `DataRate()`

```cpp
data_rate BSerialPort::DataRate()
```

Gets the current baud rate. 



**Returns:** The current baud rate.



**See also:** [SetDataRate()](classBSerialPort.md#ad404a2c9f62c419e8b6b527d5523401c)



**Since:** BeOS R3

---

### `FlowControl()`

```cpp
uint32 BSerialPort::FlowControl()
```

Returns the selected flow control. 



**Returns:** The flow control for the current open port.



**See also:** [SetFlowControl()](classBSerialPort.md#a4f0336ec0ed3f45b52155830e8a52649)



**Since:** BeOS R3

---

### `GetDeviceName()`

```cpp
status_t BSerialPort::GetDeviceName(int32 index, char * name, size_t bufSize = B_OS_NAME_LENGTH)
```

Gets the device name by the given *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | Index number of the device to know the name of. |
| `name` | The buffer where to store the name. |
| `bufSize` | The size of the buffer. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The device name of the device at *index* was copied successfully. |
| B_ERROR | No device was found at *index*. |





**See also:** [CountDevices()](classBSerialPort.md#a0b8d0e706fc45d858d97646eaabda44f)



**Since:** BeOS R3

---

### `IsCTS()`

```cpp
bool BSerialPort::IsCTS()
```

Checks if the Clear To Send (CTS) pin is asserted (in an active state). 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | CTS is asserted. |
| false | CTS is not asserted. |





**Since:** BeOS R3

---

### `IsDCD()`

```cpp
bool BSerialPort::IsDCD()
```

Checks if the Data Carrier Detect (DCD) pin is asserted (in an active state). 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | DCD is asserted. |
| false | DCD is not asserted. |





**Since:** BeOS R3

---

### `IsDSR()`

```cpp
bool BSerialPort::IsDSR()
```

Checks if the Data Set Ready (DSR) pin is asserted (in an active state). 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | DSR is asserted. |
| false | DSR is not asserted. |





**Since:** BeOS R3

---

### `IsRI()`

```cpp
bool BSerialPort::IsRI()
```

Checks if the Ring Indicator (RI) pin is asserted (in an active state). 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | RI is asserted. |
| false | RI is not asserted. |





**Since:** BeOS R3

---

### `NumCharsAvailable()`

```cpp
status_t BSerialPort::NumCharsAvailable(int32 * waitThisMany)
```

Unimplemented. 



**Since:** BeOS R3

---

### `Open()`

```cpp
status_t BSerialPort::Open(const char * portName)
```

Opens a serial port represented by *portName*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `portName` | A valid port name (i.e. `"/dev/ports/serial2"`). |





**Returns:** A positive number (a file descriptor) if the serial port has been succesfully opened or an error code (negative integer) if an error has occurred.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_BALUE | *portName* is `NULL`. |





**See also:** [Close()](classBSerialPort.md#a351d27d69efbf7952776dae99323b683)



**Since:** BeOS R3

---

### `ParityMode()`

```cpp
parity_mode BSerialPort::ParityMode()
```

Gets the parity mode. 



**Returns:** The current parity mode.



**See also:** [SetParityMode()](classBSerialPort.md#ae3510987436c10b6a3a2a6d116c047ae)



**Since:** BeOS R3

---

### `Read()`

```cpp
ssize_t BSerialPort::Read(void * buf, size_t count)
```

Reads some bytes from the serial port. 


If blocking mode is enabled, [Read()](classBSerialPort.md#aba570b16b6080f86695b171eefe8d99b) will block, returning either after the whole *count* bytes arrive or the time limit set with [SetTimeout()](classBSerialPort.md#ae9ed661337c7aa33cadb225f666f6fea) is not infinite and reaches zero. If the timeout is `B_INFINITE_TIMEOUT` it will keep blocking forever.


With blocking mode disabled, it takes as much bytes as there are in the port's input buffer up to *count* bytes, if any, and returns immediately.


Parameters

| Parameter | Description |
| :--- | :--- |
| `buf` | The buffer where to copy the data. |
| `count` | The maximum amount of bytes to read. |





**Returns:** The amount of data read or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_FILE_ERROR | The serial port is not available or it was closed. |
| B_WOULD_BLOCK | The operation cannot be performed immediately and the request must not block. |
| B_TIMED_OUT | Blocking mode is enabled and the timeout period has ended before the *count* amount of data arrived at the serial port. |
| B_INTERRUPTED | The operation was interrupted by a signal. |





**Since:** BeOS R3

---

### `SetBlocking()`

```cpp
void BSerialPort::SetBlocking(bool blocking)
```

Sets the blocking mode. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `blocking` | If `true`, enables the blocking mode. If `false`, disables it. |





**Since:** BeOS R3

---

### `SetDataBits()`

```cpp
void BSerialPort::SetDataBits(data_bits numBits)
```

Sets the data bits. 


This operation will fail silently if the driver does not support the requested number of data bits. To make sure the setting was applied it is required to check [DataBits()](classBSerialPort.md#a2803472667f85735953d7d5c6e2f68a8).


Parameters

| Parameter | Description |
| :--- | :--- |
| `numBits` | The number of data bits. |





**See also:** [DataBits()](classBSerialPort.md#a2803472667f85735953d7d5c6e2f68a8)



**Since:** BeOS R3

---

### `SetDataRate()`

```cpp
status_t BSerialPort::SetDataRate(data_rate bitsPerSecond)
```

Sets the baud rate for the port. 


To set a custom data rate not defined in the data_rate enumeration you can pass the number of bits per second directly in *bitsPerSecond*, but the value has to be above 50.


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitsPerSecond` | The baud rate. |





**Returns:** `B_OK` if successful, or an error code if something went wrong.



**See also:** [DataRate()](classBSerialPort.md#ac1af51293f4f7349f8ccf5debdfe108e)



**Since:** BeOS R3

---

### `SetDTR()`

```cpp
status_t BSerialPort::SetDTR(bool asserted)
```

Sets the Data Terminal Ready (DTR) pin active if *asserted* is `true`, or inactive if it is `false`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `asserted` | The DTR status wanted. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | DTR pin state was changed. |
| B_ERROR | DTR pin state could not be changed or an error has occurred. |





**Since:** BeOS R3

---

### `SetFlowControl()`

```cpp
void BSerialPort::SetFlowControl(uint32 method)
```

Sets the flow control. 


Valid values for *method* are:


* `B_NOFLOW_CONTROL` to not perform flow control.

* `B_HARDWARE_CONTROL` to perform flow control via hardware.

* `B_SOFTWARE_CONTROL` to perform flow control via software.

* `B_HARDWARE_CONTROL` | `B_SOFTWARE_CONTROL` to perform flow control via both hardware and software.



Parameters

| Parameter | Description |
| :--- | :--- |
| `method` | The type of flow control. |





**See also:** [FlowControl()](classBSerialPort.md#ab4903e944fb8d087eaab18e84bd79da3)



**Since:** BeOS R3

---

### `SetParityMode()`

```cpp
void BSerialPort::SetParityMode(parity_mode which)
```

Sets the parity mode. 


Valid values for *which* are:


* [B_NO_PARITY](SerialPort_8h.md#a99478acbedd26edb50291fe85d4a7d14aaaa9549b95985a1a5df2ca2611c83c35) to not send a parity bit.

* [B_ODD_PARITY](SerialPort_8h.md#a99478acbedd26edb50291fe85d4a7d14a275972f75a3b3516373e58c22c0b65d9) to send a parity bit and set it to have an odd number of "1" bits in the transmission.

* [B_EVEN_PARITY](SerialPort_8h.md#a99478acbedd26edb50291fe85d4a7d14ad8d9e5fe1603db6d17f071020490e510) to send a parity bit and set it to have an even number of "1" bits in the transmission.



Parameters

| Parameter | Description |
| :--- | :--- |
| `which` | The parity mode to set. |





**See also:** [ParityMode()](classBSerialPort.md#ae4e24ff2aa599a283886fb1337f3afe6)



**Since:** BeOS R3

---

### `SetRTS()`

```cpp
status_t BSerialPort::SetRTS(bool asserted)
```

Sets the Request To Send (RTS) pin active if *asserted* is `true`, or inactive if it is `false`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `asserted` | The RTS status wanted. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | RTS pin state was changed. |
| B_ERROR | RTS pin state could not be changed or an error has occurred. |





**Since:** BeOS R3

---

### `SetStopBits()`

```cpp
void BSerialPort::SetStopBits(stop_bits numBits)
```

Sets the stop bits. 


This operation will fail silently if the driver does not support the requested number of stop bits. To make sure the setting was applied it is required to check [StopBits()](classBSerialPort.md#a22bbb23e861cf6d95113f57f52db6862).


Parameters

| Parameter | Description |
| :--- | :--- |
| `numBits` | The number of stop bits. |





**See also:** [StopBits()](classBSerialPort.md#a22bbb23e861cf6d95113f57f52db6862)



**Since:** BeOS R3

---

### `SetTimeout()`

```cpp
status_t BSerialPort::SetTimeout(bigtime_t microSeconds)
```

Sets the timeout period for how long [Read()](classBSerialPort.md#aba570b16b6080f86695b171eefe8d99b) and [WaitForInput()](classBSerialPort.md#ae8a14f3889f8133377920d040f0fb21d) will wait for the data to arrive to the port's input buffer before returning. 


The timeout period only applies when in blocking mode. In non-blocking mode it takes no effect.


Parameters

| Parameter | Description |
| :--- | :--- |
| `microSeconds` | The timeout for the port. Valid values are: * `B_INFINITE_TIMEOUT` to wait forever  * Any value between 0 and 25000000 microseconds. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Timeout changed successfully. |
| B_BAD_VALUE | The timeout value provided by *microSeconds* was invalid. |





**Since:** BeOS R3

---

### `StopBits()`

```cpp
stop_bits BSerialPort::StopBits()
```

Gets the current stop bits. 



**Returns:** The current stop bits.



**See also:** [SetStopBits()](classBSerialPort.md#af41210945a951619018ac16a939fffa8)



**Since:** BeOS R3

---

### `WaitForInput()`

```cpp
ssize_t BSerialPort::WaitForInput()
```

Waits until there is something to read from the serial port. 


If no data is ready, it will always block, ignoring the value of [SetBlocking()](classBSerialPort.md#ae0bec0386c30dbd6b6b587699cbf7ad4); however, it respects the timeout set by [SetTimeout()](classBSerialPort.md#ae9ed661337c7aa33cadb225f666f6fea).



**Returns:** The number of bytes available to be read or an error code.



**Since:** BeOS R3

---

### `Write()`

```cpp
ssize_t BSerialPort::Write(const void * buf, size_t count)
```

Writes some bytes to the serial port. 


In blocking mode, [Write()](classBSerialPort.md#a5d19c23626f6be250264f0e7c6f1d3f4) will write exactly the full contents of *buf*, even if this makes it to wait.


In non-blocking mode, it will write as many bytes as it can, which may not be the complete buffer, and then returns immediately.


Parameters

| Parameter | Description |
| :--- | :--- |
| `buf` | The buffer from where to copy the data. |
| `count` | The amount of bytes to write. |





**Returns:** The amount of data written or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_FILE_ERROR | The serial port is not available or it was closed. |
| B_WOULD_BLOCK | The operation cannot be performed immediately and the request must not block. |
| B_INTERRUPTED | The operation was interrupted by a signal. |





**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBSerialPort.html).
