---
name: BScreen
type: class
kit: interface_kit
brief: "The BScreen class provides methods to retrieve and change display settings"
source: haiku-book
---

# BScreen Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

The [BScreen](classBScreen.md) class provides methods to retrieve and change display settings. 


Each [BScreen](classBScreen.md) object describes one display connected to the computer. Multiple [BScreen](classBScreen.md) objects can represent the same physical display.



> [!IMPORTANT]
> Haiku currently supports only a single display. The main screen with id `B_MAIN_SCREEN_ID` contains the origin in its top left corner. Additional displays, when they become supported, will extend the coordinates of the main screen.


Some utility methods provided by this class are [ColorSpace()](classBScreen.md#a56340c50b7488bd3bed1b44afa62ce4f) to get the color space of the screen, [Frame()](classBScreen.md#ad0846a4958e4287cdb891e2ca7f8cb98) to get the frame rectangle, and [ID()](classBScreen.md#ab67837ac2adc413602d326af8151f255) to get the identifier of the screen.


Methods to convert between 8-bit and 32-bit colors are provided by [IndexForColor()](classBScreen.md#a4ceb2e5c169cc77e0aedaf4af14254d9) and [ColorForIndex()](classBScreen.md#ad3c982989b0668a024d22bb8488597d7).


You can also use this class to take a screenshot of the entire screen or a particular portion of it. To take a screenshot use either the [GetBitmap()](classBScreen.md#a103f21878d503134ca7b71c4e8db278b) or [ReadBitmap()](classBScreen.md#a1f05b947376c3322f6dcf9fcfc18d02c) method.


Furthermore, you can use this class get and set the background color of a workspace. To get the background color call [DesktopColor()](classBScreen.md#ae6df75ca8af53688e88e195c6dafdadc) or to set the background color use [SetDesktopColor()](classBScreen.md#a241bcdde894d7cb0255c5ec7dbb15043).


This class provides methods to get and set the resolution, pixel depth, and color map of a display. To get a list of the display modes supported by the graphics card use the [GetModeList()](classBScreen.md#a1d86da3d8a8ab2bcce1781a3b429252b) method. You can get and set the screen resolution by calling the [GetMode()](classBScreen.md#afa032aafc0efa58e666bc673f3d3b0d3) and [SetMode()](classBScreen.md#a7c22338581a5c5e75835d30de2019bfd) methods. The color map of the display can be retrieved by calling the [ColorMap()](classBScreen.md#abb25fe0aabfc7505fd0265cff4044f90) method.


You can use this class to get information about the graphics card and monitor connected to the computer by calling the [GetDeviceInfo()](classBScreen.md#a2b34d215fa6f9d98e6e04098cc30a7dd) and [GetMonitorInfo()](classBScreen.md#a399e41f3885803dcc7fa54d00c7f7561) methods.


VESA Display Power Management Signaling support allow you to put the monitor into a low-power mode. Call [DPMSCapabilites()](classBScreen.md#a348ad8b92849ab8ea9c84d8f99118375) to check what modes are supported by your monitor. [DPMSState()](classBScreen.md#aba78689135ae0af5cf9f4b07a8719833) tells you what state your monitor is currently in and [SetDPMS()](classBScreen.md#a1af45eaea5ee9539ab481f9f68ad630c) allows you to change it.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BScreen](#a98f6d2890b1f380d8e66b3ae33c34500) (BWindow *window) — Creates a BScreen object which represents the display that contains window.
* [BScreen](#a855bab18a9fde11d87c3344611c4f2a1) (screen_id id=B_MAIN_SCREEN_ID) — Creates a BScreen object which represents the display connected to the computer with the given screen_id.
* [~BScreen](#a3dec0c06b06665c37c5c493230823c7f) () — Frees the resources used by the BScreen object and unlocks the screen.
* `bool` [IsValid](#a9e3b631d389bbcedc046d301e9de8d4a) () — Checks that the BScreen object represents a real display that is connected to the computer.
* `status_t` [SetToNext](#a666a5d576a26688d2c59c11f27e559e9) () — Sets the BScreen object to the next display in the screen list.
* `color_space` [ColorSpace](#a56340c50b7488bd3bed1b44afa62ce4f) () — Returns the color_space of the display.
* `BRect` [Frame](#ad0846a4958e4287cdb891e2ca7f8cb98) () — Gets the frame of the screen in the screen's coordinate system.
* `screen_id` [ID](#ab67837ac2adc413602d326af8151f255) () — Gets the identifier of the display.
* `status_t` [WaitForRetrace](#a29a521bd71459cd20fec8287b9cf678f) () — Blocks until the monitor has finished its current vertical retrace.
* `status_t` [WaitForRetrace](#ac47812cdef0f0b65b40b3b79af3db4b5) (bigtime_t timeout) — Blocks until the monitor has finished its current vertical retrace or until timeout has expired.
* `uint8` [IndexForColor](#a4ceb2e5c169cc77e0aedaf4af14254d9) (rgb_color color) — Returns the 8-bit color index that most closely matches a 32-bit color.
* `uint8` [IndexForColor](#a9235d186f8470fdc8e7b3e5edeb8cd18) (uint8 red, uint8 green, uint8 blue, uint8 alpha=255) — Returns the 8-bit color index that most closely matches a set of red, green, blue, and alpha values.
* `rgb_color` [ColorForIndex](#ad3c982989b0668a024d22bb8488597d7) (uint8 index) — Gets the 32-bit color representation of an 8-bit color index.
* `uint8` [InvertIndex](#ad04dc4456c0544172a29647e35ed44aa) (uint8 index) — Gets the "Inversion" of an 8-bit color index.
* `const color_map *` [ColorMap](#abb25fe0aabfc7505fd0265cff4044f90) () — Gets the color_map of the BScreen.
* `status_t` [GetBitmap](#a103f21878d503134ca7b71c4e8db278b) (BBitmap **_bitmap, bool drawCursor=true, BRect *frame=NULL) — Allocates a BBitmap and copies the contents of the screen into it.
* `status_t` [ReadBitmap](#a1f05b947376c3322f6dcf9fcfc18d02c) (BBitmap *bitmap, bool drawCursor=true, BRect *frame=NULL) — Copies the contents of the screen into a BBitmap.
* `rgb_color` [DesktopColor](#ae6df75ca8af53688e88e195c6dafdadc) () — Gets the background color of the current workspace.
* `rgb_color` [DesktopColor](#a1595a0dbc8f453892e7fd371470be4af) (uint32 workspace) — Gets the background color of the specified workspace.
* `void` [SetDesktopColor](#a241bcdde894d7cb0255c5ec7dbb15043) (rgb_color color, bool stick=true) — Set the background color of the current workspace.
* `void` [SetDesktopColor](#a740c6dd4b7ec9e982624b86c73de7ee3) (rgb_color color, uint32 workspace, bool stick=true) — Set the background color of the specified workspace.
* `status_t` [ProposeMode](#ac23d8d6d04333b84ecacf47e0bb4a3b2) (display_mode *target, const display_mode *low, const display_mode *high) — Adjust the target mode to make it a supported mode.
* `status_t` [GetModeList](#a1d86da3d8a8ab2bcce1781a3b429252b) (display_mode **_modeList, uint32 *_count) — Allocates and returns a list of the display modes supported by the graphics card into _modeList.
* `status_t` [GetMode](#afa032aafc0efa58e666bc673f3d3b0d3) (display_mode *mode) — Fills out the display_mode struct from the current workspace.
* `status_t` [GetMode](#adbaecd70d8b670d9de171f84da3a905b) (uint32 workspace, display_mode *mode) — Fills out the display_mode struct from the specified workspace.
* `status_t` [SetMode](#a7c22338581a5c5e75835d30de2019bfd) (display_mode *mode, bool makeDefault=false) — Sets the screen in the current workspace to the given mode.
* `status_t` [SetMode](#ae26f68f38d02e57825188a5336e2f759) (uint32 workspace, display_mode *mode, bool makeDefault=false) — Set the screen in the specified workspace to the given mode.
* `status_t` [GetDeviceInfo](#a2b34d215fa6f9d98e6e04098cc30a7dd) (accelerant_device_info *info) — Fills out the info struct with information about a graphics card.
* `status_t` [GetMonitorInfo](#a399e41f3885803dcc7fa54d00c7f7561) (monitor_info *info) — Fills out the info struct with information about a monitor.
* `status_t` [GetPixelClockLimits](#afbb89f5b53c0fddccaaee09fe75b4cff) (display_mode *mode, uint32 *_low, uint32 *_high) — Gets the minimum and maximum pixel clock rates that are possible for the specified mode.
* `status_t` [GetTimingConstraints](#a142936ded6c6c30e357b8f00ea8efd4d) (display_timing_constraints *timingConstraints) — Fills out the constraints structure with the timing constraints of the current display mode.
* `status_t` [SetDPMS](#a1af45eaea5ee9539ab481f9f68ad630c) (uint32 state) — Sets the VESA Display Power Management Signaling (DPMS) state for the display.
* `uint32` [DPMSState](#aba78689135ae0af5cf9f4b07a8719833) () — Gets the current VESA Display Power Management Signaling (DPMS) state of the screen.
* `uint32` [DPMSCapabilites](#a348ad8b92849ab8ea9c84d8f99118375) () — Gets the VESA Display Power Management Signaling (DPMS) modes that the display supports as a bit mask.

## Detailed Member Documentation

### `BScreen()`

```cpp
BScreen::BScreen(screen_id id = B_MAIN_SCREEN_ID)
```

Creates a [BScreen](classBScreen.md) object which represents the display connected to the computer with the given screen_id. 


In the current implementation, there is only one display (`B_MAIN_SCREEN_ID`). To be sure that the object was constructed correctly, call [IsValid()](classBScreen.md#a9e3b631d389bbcedc046d301e9de8d4a).


Parameters

| Parameter | Description |
| :--- | :--- |
| `id` | The screen_id of the screen to create a [BScreen](classBScreen.md) object from. |





**Since:** BeOS R3

---

### `BScreen()`

```cpp
BScreen::BScreen(BWindow * window)
```

Creates a [BScreen](classBScreen.md) object which represents the display that contains *window*. 


In the current implementation, there is only one display (`B_MAIN_SCREEN_ID`). To be sure that the object was constructed correctly, call [IsValid()](classBScreen.md#a9e3b631d389bbcedc046d301e9de8d4a).


Parameters

| Parameter | Description |
| :--- | :--- |
| `window` | A [BWindow](classBWindow.md) object. |





**Since:** BeOS R3

---

### `~BScreen()`

```cpp
BScreen::~BScreen()
```

Frees the resources used by the [BScreen](classBScreen.md) object and unlocks the screen. 



> [!NOTE]
> The main screen object will never go away, even if you disconnect all monitors.



**Since:** BeOS R3

---

### `ColorForIndex()`

```cpp
rgb_color BScreen::ColorForIndex(uint8 index)
```

Gets the 32-bit color representation of an 8-bit color *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The 8-bit color *index* to convert to a 32-bit color. |





**Returns:** A 32-bit [rgb_color](structrgb__color.md) structure.



**Since:** BeOS R3

---

### `ColorMap()`

```cpp
const color_map * BScreen::ColorMap()
```

Gets the color_map of the [BScreen](classBScreen.md). 



**Returns:** A pointer to the [BScreen](classBScreen.md) object's color_map.



**Since:** BeOS R3

---

### `ColorSpace()`

```cpp
color_space BScreen::ColorSpace()
```

Returns the color_space of the display. 



**Returns:** `B_CMAP8`, `B_RGB15`, `B_RGB32`, or `B_NO_COLOR_SPACE` if the [BScreen](classBScreen.md) object is invalid.



**Since:** BeOS R3

---

### `DesktopColor()`

```cpp
rgb_color BScreen::DesktopColor()
```

Gets the background color of the current workspace. 



**Returns:** A 32-bit [rgb_color](structrgb__color.md) structure containing the background color of the current workspace.



**Since:** BeOS R3

---

### `DesktopColor()`

```cpp
rgb_color BScreen::DesktopColor(uint32 workspace)
```

Gets the background color of the specified *workspace*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `workspace` | The *workspace* index to get the desktop background color of. |





**Returns:** An 32-bit [rgb_color](structrgb__color.md) structure containing the background color of the specified *workspace*.



**Since:** Haiku R1

---

### `DPMSCapabilites()`

```cpp
uint32 BScreen::DPMSCapabilites()
```

Gets the VESA Display Power Management Signaling (DPMS) modes that the display supports as a bit mask. 



* `B_DPMS_ON` is worth 1

* `B_DPMS_STAND_BY` is worth 2

* `B_DPMS_SUSPEND` is worth 4

* `B_DPMS_OFF` is worth 8




**Returns:** A bit mask of the VESA Display Power Management Signaling (DPMS) modes that the display supports or 0 in the case of an error.



**Since:** BeOS R5

---

### `DPMSState()`

```cpp
uint32 BScreen::DPMSState()
```

Gets the current VESA Display Power Management Signaling (DPMS) state of the screen. 



**Returns:** The current VESA Display Power Management Signaling (DPMS) state of the display or 0 in the case of an error.



**Since:** BeOS R5

---

### `Frame()`

```cpp
BRect BScreen::Frame()
```

Gets the frame of the screen in the screen's coordinate system. 


For example if the [BScreen](classBScreen.md) object points to the main screen with a resolution of 1,366x768 then this method returns [BRect](classBRect.md)(0.0, 0.0, 1365.0, 767.0). If the [BScreen](classBScreen.md) object is invalid then this method returns an empty rectangle i.e. [BRect](classBRect.md)(0.0, 0.0, 0.0, 0.0)


You can set the frame programmatically by calling the [SetMode()](classBScreen.md#a7c22338581a5c5e75835d30de2019bfd) method.



**Returns:** a [BRect](classBRect.md) frame of the screen in the screen's coordinate system.



**Since:** BeOS R3

---

### `GetBitmap()`

```cpp
status_t BScreen::GetBitmap(BBitmap ** _bitmap, bool drawCursor = true, BRect * bounds = NULL)
```

Allocates a [BBitmap](classBBitmap.md) and copies the contents of the screen into it. 



> [!NOTE]
> [GetBitmap()](classBScreen.md#a103f21878d503134ca7b71c4e8db278b) will allocate a [BBitmap](classBBitmap.md) object for you while [ReadBitmap()](classBScreen.md#a1f05b947376c3322f6dcf9fcfc18d02c) requires you to pre-allocate a [BBitmap](classBBitmap.md) object first.


Parameters

| Parameter | Description |
| :--- | :--- |
| `_bitmap` | A pointer to a [BBitmap](classBBitmap.md) pointer where this method will store the contents of the display. |
| `drawCursor` | Specifies whether or not to draw the cursor. |
| `bounds` | Specifies the screen area that you want copied. If *bounds* is `NULL` then the entire screen is copied. |





**Returns:** `B_OK` if the operation was successful, `B_ERROR` otherwise.



**Since:** BeOS R4

---

### `GetDeviceInfo()`

```cpp
status_t BScreen::GetDeviceInfo(accelerant_device_info * info)
```

Fills out the *info* struct with information about a graphics card. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `info` | An accelerant_device_info struct to store the device *info*. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | if the operation was successful. |
| B_BAD_VALUE | if *info* is invalid. |
| B_ERROR | for all other errors. |





**Since:** BeOS R5

---

### `GetMode()`

```cpp
status_t BScreen::GetMode(display_mode * mode)
```

Fills out the display_mode struct from the current workspace. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `mode` | A pointer to a display_mode struct to copy into. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | if the operation was successful. |
| B_BAD_VALUE | if *mode* is invalid. |
| B_ERROR | for all other errors. |





**Since:** BeOS R5

---

### `GetMode()`

```cpp
status_t BScreen::GetMode(uint32 workspace, display_mode * mode)
```

Fills out the display_mode struct from the specified *workspace*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `workspace` | The index of the *workspace* to query. |
| `mode` | A pointer to a display_mode structure to copy into. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | if the operation was successful |
| B_BAD_VALUE | if *mode* is invalid. |
| B_ERROR | for all other errors. |





**Since:** Haiku R1

---

### `GetModeList()`

```cpp
status_t BScreen::GetModeList(display_mode ** _modeList, uint32 * _count)
```

Allocates and returns a list of the display modes supported by the graphics card into *_modeList*. 



> [!WARNING]
> The monitor may not be able to display all of the modes that [GetModeList()](classBScreen.md#a1d86da3d8a8ab2bcce1781a3b429252b) retrieves.



> [!NOTE]
> The caller is responsible for freeing the display_mode object.


Parameters

| Parameter | Description |
| :--- | :--- |
| `_modeList` | A pointer to a display_mode pointer, where the function will allocate an array of display_mode structures. |
| `_count` | A pointer to an integer used to store the count of available display modes. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | if the operation was successful. |
| B_ERROR | for all other errors. |





**Since:** BeOS R5

---

### `GetMonitorInfo()`

```cpp
status_t BScreen::GetMonitorInfo(monitor_info * info)
```

Fills out the *info* struct with information about a monitor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `info` | A monitor_info struct to store the monitor *info*. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | if the operation was successful. |
| B_BAD_VALUE | if *info* is invalid. |
| B_ERROR | for all other errors. |





**Since:** Haiku R1

---

### `GetPixelClockLimits()`

```cpp
status_t BScreen::GetPixelClockLimits(display_mode * mode, uint32 * _low, uint32 * _high)
```

Gets the minimum and maximum pixel clock rates that are possible for the specified *mode*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `mode` | A pointer to a display_mode structure. |
| `_low` | A pointer to a uint32 where the method stores the lowest available pixel clock. |
| `_high` | A pointer to a uint32 where the method stores the highest available pixel clock. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | if the operation was successful. |
| B_BAD_VALUE | if *mode*, *low*, or *high* is invalid. |
| B_ERROR | for all other errors. |





**Since:** BeOS R5

---

### `GetTimingConstraints()`

```cpp
status_t BScreen::GetTimingConstraints(display_timing_constraints * constraints)
```

Fills out the *constraints* structure with the timing constraints of the current display mode. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `constraints` | A pointer to a display_timing_constraints structure to store the timing constraints. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | if the operation was successful. |
| B_BAD_VALUE | if *constraints* is invalid. |
| B_ERROR | for all other errors. |





**Since:** BeOS R5

---

### `ID()`

```cpp
screen_id BScreen::ID()
```

Gets the identifier of the display. 


In the current implementation this method returns `B_MAIN_SCREEN_ID` even if the object is invalid.



**Returns:** A screen_id that identifies the screen.



**Since:** BeOS R3

---

### `IndexForColor()`

```cpp
uint8 BScreen::IndexForColor(rgb_color color)
```

Returns the 8-bit color index that most closely matches a 32-bit *color*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `color` | The 32-bit *color* to get the 8-bit index of. |





**Returns:** An 8-bit color index in the screen's color_map.



**Since:** BeOS R3


References [rgb_color::alpha](structrgb__color.md#a089265e492dbf6743a6eaaa23fa94699), [rgb_color::blue](structrgb__color.md#adbc9af28f1ec74ac8e7cc8f7fc1e6ce3), [rgb_color::green](structrgb__color.md#ac0259068653969121d72739ad8509979), [IndexForColor()](classBScreen.md#a4ceb2e5c169cc77e0aedaf4af14254d9), and [rgb_color::red](structrgb__color.md#ad8f118f509b77a245d9e38829336f0ec).


Referenced by [IndexForColor()](classBScreen.md#a4ceb2e5c169cc77e0aedaf4af14254d9).

---

### `IndexForColor()`

```cpp
uint8 BScreen::IndexForColor(uint8 red, uint8 green, uint8 blue, uint8 alpha = 255)
```

Returns the 8-bit color index that most closely matches a set of *red*, *green*, *blue*, and *alpha* values. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `red` | The *red* value. |
| `green` | The *green* value. |
| `blue` | The *blue* value. |
| `alpha` | The *alpha* value. |





**Returns:** An 8-bit color index in the screen's color_map.



**Since:** BeOS R3

---

### `InvertIndex()`

```cpp
uint8 BScreen::InvertIndex(uint8 index)
```

Gets the "Inversion" of an 8-bit color *index*. 


Inverted colors are useful for highlighting.


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The 8-bit color *index*. |





**Returns:** An 8-bit color *index* that represents the "Inversion" of the given color in the screen's color_map.



**Since:** BeOS R3

---

### `IsValid()`

```cpp
bool BScreen::IsValid()
```

Checks that the [BScreen](classBScreen.md) object represents a real display that is connected to the computer. 



**Returns:** `true` if the [BScreen](classBScreen.md) object is valid, `false` otherwise.



**Since:** BeOS R3

---

### `ProposeMode()`

```cpp
status_t BScreen::ProposeMode(display_mode * target, const display_mode * low, const display_mode * high)
```

Adjust the *target* mode to make it a supported mode. 


The list of supported modes for the graphics card is supplied by the [GetModeList()](classBScreen.md#a1d86da3d8a8ab2bcce1781a3b429252b) method.


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | The mode you want adjust. |
| `low` | The lower display mode limit. |
| `high` | The higher display mode limit. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | if *target* is supported and falls within the *low* and *high* limits. |
| B_BAD_VALUE | if *target* is supported but does not fall within the *low* and *high* limits. |
| B_ERROR | if the target mode isn't supported. |





**Since:** BeOS R5

---

### `ReadBitmap()`

```cpp
status_t BScreen::ReadBitmap(BBitmap * bitmap, bool drawCursor = true, BRect * bounds = NULL)
```

Copies the contents of the screen into a [BBitmap](classBBitmap.md). 



> [!NOTE]
> [ReadBitmap()](classBScreen.md#a1f05b947376c3322f6dcf9fcfc18d02c) requires you to pre-allocate a [BBitmap](classBBitmap.md) object first, while [GetBitmap()](classBScreen.md#a103f21878d503134ca7b71c4e8db278b) will allocate a [BBitmap](classBBitmap.md) object for you.


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | A pointer to a pre-allocated [BBitmap](classBBitmap.md) where this method will store the contents of the display. |
| `drawCursor` | Specifies whether or not to draw the cursor. |
| `bounds` | Specifies the screen area that you want copied. If *bounds* is `NULL` then the entire screen is copied. |





**Returns:** `B_OK` if the operation was successful, `B_ERROR` otherwise.



**Since:** BeOS R4

---

### `SetDesktopColor()`

```cpp
void BScreen::SetDesktopColor(rgb_color color, bool stick = true)
```

Set the background *color* of the current workspace. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `color` | The 32-bit *color* to paint the desktop background. |
| `stick` | Whether or not the *color* will stay after a reboot. |





**Since:** BeOS R3

---

### `SetDesktopColor()`

```cpp
void BScreen::SetDesktopColor(rgb_color color, uint32 workspace, bool stick = true)
```

Set the background *color* of the specified *workspace*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `color` | The 32-bit *color* to paint the desktop background. |
| `workspace` | The *workspace* index to update. |
| `stick` | Whether or not the *color* will stay after a reboot. |





**Since:** Haiku R1

---

### `SetDPMS()`

```cpp
status_t BScreen::SetDPMS(uint32 dpmsState)
```

Sets the VESA Display Power Management Signaling (DPMS) state for the display. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dpmsState` | The DPMS state to set, valid values are: * `B_DPMS_ON`  * `B_DPMS_STAND_BY`  * `B_DPMS_SUSPEND`  * `B_DPMS_OFF` |





**Returns:** `B_OK` if the operation was successful, otherwise an error code.



**Since:** BeOS R5

---

### `SetMode()`

```cpp
status_t BScreen::SetMode(display_mode * mode, bool makeDefault = false)
```

Sets the screen in the current workspace to the given *mode*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `mode` | A pointer to a display_mode struct. |
| `makeDefault` | Whether or not *mode* is set as the default. |





**Returns:** `B_OK` if the operation was successful, `B_ERROR` otherwise.



**Since:** BeOS R5

---

### `SetMode()`

```cpp
status_t BScreen::SetMode(uint32 workspace, display_mode * mode, bool makeDefault = false)
```

Set the screen in the specified *workspace* to the given *mode*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `workspace` | The index of the workspace to set the *mode* of. |
| `mode` | A pointer to a display_mode struct. |
| `makeDefault` | Whether or not the *mode* is set as the default for the specified *workspace*. |





**Returns:** `B_OK` if the operation was successful, `B_ERROR` otherwise.



**Since:** Haiku R1

---

### `SetToNext()`

```cpp
status_t BScreen::SetToNext()
```

Sets the [BScreen](classBScreen.md) object to the next display in the screen list. 



**Returns:** `B_OK` if successful, otherwise `B_ERROR`.



**Since:** BeOS R5

---

### `WaitForRetrace()`

```cpp
status_t BScreen::WaitForRetrace()
```

Blocks until the monitor has finished its current vertical retrace. 



**Returns:** `B_OK` or `B_ERROR` if the screen object is invalid.



**Since:** BeOS R3

---

### `WaitForRetrace()`

```cpp
status_t BScreen::WaitForRetrace(bigtime_t timeout)
```

Blocks until the monitor has finished its current vertical retrace or until *timeout* has expired. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `timeout` | The amount of time to wait before returning. |





**Returns:** `B_OK` if the monitor has retraced in the given *timeout* duration, `B_ERROR` otherwise.



**Since:** BeOS R5

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBScreen.html).
