---
name: direct_buffer_info
type: struct
kit: game_kit
brief: "Direct butter info struct"
source: haiku-book
---

# direct_buffer_info Struct
**Kit/Group:** [Game Kit](../game_kit/group__game.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Direct butter info struct



**Since:** BeOS R3

## Member List

### Public Attributes

* `addr_t` [_reserved](#a924c2e0709b1d0e1459cdec18cb9a4d8)
* `void *` [bits](#a9d32e4c10fbf74f3ae06950cc2574778)
* `uint32` [bits_per_pixel](#aa57a0f955dc80b9769e5e679f959b238)
* `direct_buffer_state` [buffer_state](#a2e71385b7557555ffb7971732cf2c89d)
* `int32` [bytes_per_row](#a7844d9d98266d508cbe8de30dc8146b6)
* `clipping_rect` [clip_bounds](#acadae6b1044925025788fde20ba67c6f)
* `clipping_rect` [clip_list](#a67902e64f90dc357612e097158f0c720) [1]
* `uint32` [clip_list_count](#adaa1333beb80fa27e8de3cdd2d0f9480)
* `direct_driver_state` [driver_state](#acb1169f13e69e876120cd86a8219b660)
* `buffer_layout` [layout](#a00d98d664a4321c0fdf7087db6fb73de)
* `buffer_orientation` [orientation](#a58749870fd051e59c00e6ddeaa1c634b)
* `color_space` [pixel_format](#ae08e199e035ec0743cbf25c7b39b167c)
* `clipping_rect` [window_bounds](#a99b51d73067b030e8f8f0ac20266c01e)

## Detailed Member Documentation

### `_reserved`

```cpp
direct_buffer_info::_reserved[9]
```

Reserved for future use.



**Since:** BeOS R3

---

### `bits`

```cpp
direct_buffer_info::bits
```

Pointer to the frame buffer in your team's memory space.



**Since:** BeOS R3

---

### `bits_per_pixel`

```cpp
direct_buffer_info::bits_per_pixel
```

Number of bits actually used to store a single pixel, including reserved, unused, or alpha channel bits. This value is usually a multiple of eight.



**Since:** BeOS R3

---

### `buffer_state`

```cpp
direct_buffer_info::buffer_state
```

State of the direct buffer access privileges. It can have one of the following values:


* `B_DIRECT_MODE_MASK`

* `B_DIRECT_START`

* `B_DIRECT_MODIFY`

* `B_DIRECT_STOP`

* `B_BUFFER_MOVED`

* `B_BUFFER_RESET`

* `B_BUFFER_RESIZED`

* `B_CLIPPING_MODIFIED`




**Since:** BeOS R3

---

### `bytes_per_row`

```cpp
direct_buffer_info::bytes_per_row
```

Number of bytes used to represent a single row of pixels in the frame buffer.



**Since:** BeOS R3

---

### `clip_bounds`

```cpp
direct_buffer_info::clip_bounds
```

Bounding rectangle of the visible part of the content area of the window in screen coordinates.



**Since:** BeOS R3

---

### `clip_list`

```cpp
direct_buffer_info::clip_list
```

List of rectangles that together define the visible region of the content area of the window in screen coordinates.



**Since:** BeOS R3

---

### `clip_list_count`

```cpp
direct_buffer_info::clip_list_count
```

Number of rectangles in `clip_list`.



**Since:** BeOS R3

---

### `driver_state`

```cpp
direct_buffer_info::driver_state
```

State of the graphics card on which your direct window is displayed. There are two possible values:


* `B_MODE_CHANGED` The resolution or color depth has changed.

* `B_DRIVER_CHANGED` The window was moved onto another monitor.




**Since:** BeOS R3

---

### `layout`

```cpp
direct_buffer_info::layout
```

Reserved for future use.



**Since:** BeOS R3

---

### `orientation`

```cpp
direct_buffer_info::orientation
```

Reserved for future use.



**Since:** BeOS R3

---

### `pixel_format`

```cpp
direct_buffer_info::pixel_format
```

The format used to encode a pixel as defined by the `color_space` type.



**Since:** BeOS R3

---

### `window_bounds`

```cpp
direct_buffer_info::window_bounds
```

Rectangle that defines the full content area of the window in screen coordinates.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structdirect__buffer__info.html).
