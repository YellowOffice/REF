---
name: rgb_color
type: struct
kit: interface_kit
brief: "Structure representing a 32 bit RGBA color"
source: haiku-book
---

# rgb_color Struct
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Structure representing a 32 bit RGBA color. 



**Since:** BeOS R3

## Member List

### RGB Colors

* `uint8` [red](#ad8f118f509b77a245d9e38829336f0ec) — Red value for the color.
* `uint8` [green](#ac0259068653969121d72739ad8509979) — Green value for the color.
* `uint8` [blue](#adbc9af28f1ec74ac8e7cc8f7fc1e6ce3) — Blue value for the color.
* `uint8` [alpha](#a089265e492dbf6743a6eaaa23fa94699) — Alpha value for the color.
* `rgb_color &` [set_to](#a8d76eb4b2489f7d18c10b8d6774cefe3) (uint8 r, uint8 g, uint8 b, uint8 a=255) — Helper method to set all values of the color.
* `int32` [Brightness](#abb088e4bd6e263afc739fa24b7401198) () const — Calculates a value representing the brightness of this color.
* `bool` [IsDark](#a7a1170ad5306cd97cf83901b190ae739) () const — Determines if the color is dark.
* `bool` [IsLight](#a960f4c9cce47c250fa2d677567f82b3d) () const — Determines if the color is light.
* `bool` [operator==](#a9cbd0265aa3640ca58145b7f79665497) (const rgb_color &other) const — Comparison operator.
* `bool` [operator!=](#a36765297538d947c2dc29eb076e3d731) (const rgb_color &other) const — Comparison operator.
* `rgb_color &` [operator=](#ab2556f45cf157bbba7c668f3822c6d5d) (const rgb_color &other) — Assign values from another color object.
* `static int32` [Contrast](#a2d32a190bd0de04aacc157bbc9ad86cc) (rgb_color colorA, rgb_color colorB) — Calculates the contrast between two colors.

## Detailed Member Documentation

### `Brightness()`

```cpp
int32 rgb_color::Brightness()const
```

Calculates a value representing the brightness of this color. 


This method calculates the perceptual brightness of a color.



**Returns:** A value representing the brightness. (0-255)



**Since:** Haiku R1


Referenced by [Contrast()](structrgb__color.md#a2d32a190bd0de04aacc157bbc9ad86cc), [IsDark()](structrgb__color.md#a7a1170ad5306cd97cf83901b190ae739), and [IsLight()](structrgb__color.md#a960f4c9cce47c250fa2d677567f82b3d).

---

### `Contrast()`

```cpp
static int32 rgb_color::Contrast(rgb_color colorA, rgb_color colorB)
```

Calculates the contrast between two colors. 


This method compares the Brightness of colorA and colorB and returns the Contrast that is between them.


For example this can used to make sure a color combination is legible on a specifc background.



**Returns:** A value representing the Contrast. (0-255)



**Since:** Haiku R1


References [Brightness()](structrgb__color.md#abb088e4bd6e263afc739fa24b7401198).

---

### `IsDark()`

```cpp
bool rgb_color::IsDark()const
```

Determines if the color is dark. 


A color is considered 'dark' if its [Brightness()](structrgb__color.md#abb088e4bd6e263afc739fa24b7401198) is <= 127.



**Since:** Haiku R1


References [Brightness()](structrgb__color.md#abb088e4bd6e263afc739fa24b7401198).

---

### `IsLight()`

```cpp
bool rgb_color::IsLight()const
```

Determines if the color is light. 


A color is considered 'light' if its [Brightness()](structrgb__color.md#abb088e4bd6e263afc739fa24b7401198) is > 127.



**Since:** Haiku R1


References [Brightness()](structrgb__color.md#abb088e4bd6e263afc739fa24b7401198).

---

### `operator!=()`

```cpp
bool rgb_color::operator!=(const rgb_color & other)const
```

Comparison operator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The other color to compare to. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The colors are different. |
| false | The colors match. |





**Since:** Haiku R1

---

### `operator=()`

```cpp
rgb_color & rgb_color::operator=(const rgb_color & other)
```

Assign values from another color object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The other color to copy. |





**Returns:** A reference to this object.



**Since:** Haiku R1


References [alpha](structrgb__color.md#a089265e492dbf6743a6eaaa23fa94699), [blue](structrgb__color.md#adbc9af28f1ec74ac8e7cc8f7fc1e6ce3), [green](structrgb__color.md#ac0259068653969121d72739ad8509979), [red](structrgb__color.md#ad8f118f509b77a245d9e38829336f0ec), and [set_to()](structrgb__color.md#a8d76eb4b2489f7d18c10b8d6774cefe3).

---

### `operator==()`

```cpp
bool rgb_color::operator==(const rgb_color & other)const
```

Comparison operator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The other color to compare to. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The colors match. |
| false | The colors are different. |





**Since:** Haiku R1

---

### `set_to()`

```cpp
rgb_color & rgb_color::set_to(uint8 r, uint8 g, uint8 b, uint8 a = 255)
```

Helper method to set all values of the color. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `r` | Red value. |
| `g` | Green value. |
| `b` | Blue value. |
| `a` | Alpha value. |





**Returns:** A reference to this object.



**Since:** Haiku R1


References [alpha](structrgb__color.md#a089265e492dbf6743a6eaaa23fa94699), [blue](structrgb__color.md#adbc9af28f1ec74ac8e7cc8f7fc1e6ce3), [green](structrgb__color.md#ac0259068653969121d72739ad8509979), and [red](structrgb__color.md#ad8f118f509b77a245d9e38829336f0ec).


Referenced by [operator=()](structrgb__color.md#ab2556f45cf157bbba7c668f3822c6d5d).

---

### `alpha`

```cpp
uint8 rgb_color::alpha
```

Alpha value for the color. 



**Since:** BeOS R3


Referenced by [BScreen::IndexForColor()](classBScreen.md#a4ceb2e5c169cc77e0aedaf4af14254d9), [operator=()](structrgb__color.md#ab2556f45cf157bbba7c668f3822c6d5d), [set_to()](structrgb__color.md#a8d76eb4b2489f7d18c10b8d6774cefe3), [BView::SetHighColor()](classBView.md#aff9e1ab5e88f33027e72b39874868e9b), [BView::SetLowColor()](classBView.md#a929fb1ca47a00220c355ae55a0ea6077), and [BView::SetViewColor()](classBView.md#a7dace2963c85b5ce55b7d8e96946625c).

---

### `blue`

```cpp
uint8 rgb_color::blue
```

Blue value for the color. 



**Since:** BeOS R3


Referenced by [BScreen::IndexForColor()](classBScreen.md#a4ceb2e5c169cc77e0aedaf4af14254d9), [operator=()](structrgb__color.md#ab2556f45cf157bbba7c668f3822c6d5d), [set_to()](structrgb__color.md#a8d76eb4b2489f7d18c10b8d6774cefe3), [BView::SetHighColor()](classBView.md#aff9e1ab5e88f33027e72b39874868e9b), [BView::SetLowColor()](classBView.md#a929fb1ca47a00220c355ae55a0ea6077), [BColorControl::SetValue()](classBColorControl.md#a31a875017105a55681f12848043f0d67), and [BView::SetViewColor()](classBView.md#a7dace2963c85b5ce55b7d8e96946625c).

---

### `green`

```cpp
uint8 rgb_color::green
```

Green value for the color. 



**Since:** BeOS R3


Referenced by [BScreen::IndexForColor()](classBScreen.md#a4ceb2e5c169cc77e0aedaf4af14254d9), [operator=()](structrgb__color.md#ab2556f45cf157bbba7c668f3822c6d5d), [set_to()](structrgb__color.md#a8d76eb4b2489f7d18c10b8d6774cefe3), [BView::SetHighColor()](classBView.md#aff9e1ab5e88f33027e72b39874868e9b), [BView::SetLowColor()](classBView.md#a929fb1ca47a00220c355ae55a0ea6077), [BColorControl::SetValue()](classBColorControl.md#a31a875017105a55681f12848043f0d67), and [BView::SetViewColor()](classBView.md#a7dace2963c85b5ce55b7d8e96946625c).

---

### `red`

```cpp
uint8 rgb_color::red
```

Red value for the color. 



**Since:** BeOS R3


Referenced by [BScreen::IndexForColor()](classBScreen.md#a4ceb2e5c169cc77e0aedaf4af14254d9), [operator=()](structrgb__color.md#ab2556f45cf157bbba7c668f3822c6d5d), [set_to()](structrgb__color.md#a8d76eb4b2489f7d18c10b8d6774cefe3), [BView::SetHighColor()](classBView.md#aff9e1ab5e88f33027e72b39874868e9b), [BView::SetLowColor()](classBView.md#a929fb1ca47a00220c355ae55a0ea6077), [BColorControl::SetValue()](classBColorControl.md#a31a875017105a55681f12848043f0d67), and [BView::SetViewColor()](classBView.md#a7dace2963c85b5ce55b7d8e96946625c).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structrgb__color.html).
