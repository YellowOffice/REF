---
name: BInputDevice
type: class
kit: interface_kit
brief: "Undocumented class"
source: haiku-book
---

# BInputDevice Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Undocumented class. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [~BInputDevice](#a5fab53eb62c44c320bf75e9699db55f8) () — Undocumented public method.
* `status_t` [Control](#ac54ce720535576f9dc25a6d9a58cb242) (uint32 code, BMessage *message) — Undocumented public method.
* `bool` [IsRunning](#aee8c08a47edd90c505ac8e680bb483e6) () const — Undocumented public method.
* `const char *` [Name](#a4eb90075b94dba72d2a3f25fb211675a) () const — Undocumented public method.
* `status_t` [Start](#ac210aedf4d8d24326f66b621eef010b8) () — Undocumented public method.
* `status_t` [Stop](#afeae379bc06356bae81f8a0fbd8f236a) () — Undocumented public method.
* `input_device_type` [Type](#ac394723350e4b8b5ab5de91a7fa06528) () const — Undocumented public method.

### Static Public Member Functions

* `static status_t` [Control](#ac1dee9c535b35284440f8c6109173e3a) (input_device_type type, uint32 code, BMessage *message) — Undocumented public method.
* `static status_t` [Start](#ad46c11be169a35f5b52adb0667b78e2c) (input_device_type type) — Undocumented public method.
* `static status_t` [Stop](#aec43473b17e80b88602fa0ca1aa30045) (input_device_type type) — Undocumented public method.

## Detailed Member Documentation

### `~BInputDevice()`

```cpp
BInputDevice::~BInputDevice()
```

Undocumented public method. 



**Since:** Haiku R1

---

### `Control()`

```cpp
static static status_t BInputDevice::Control(input_device_type type, uint32 code, BMessage * message)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | Undocumented |
| `code` | Undocumented |
| `message` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Control()`

```cpp
status_t BInputDevice::Control(uint32 code, BMessage * message)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `code` | Undocumented |
| `message` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `IsRunning()`

```cpp
bool BInputDevice::IsRunning()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Name()`

```cpp
const char * BInputDevice::Name()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Start()`

```cpp
status_t BInputDevice::Start()
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Start()`

```cpp
static static status_t BInputDevice::Start(input_device_type type)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Stop()`

```cpp
status_t BInputDevice::Stop()
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Stop()`

```cpp
static static status_t BInputDevice::Stop(input_device_type type)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Type()`

```cpp
input_device_type BInputDevice::Type()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBInputDevice.html).
