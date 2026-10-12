---
name: menu_info
type: struct
kit: interface_kit
brief: "Information about a menu such as font size and family, background color, and flags"
source: haiku-book
---

# menu_info Struct
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Information about a menu such as font size and family, background color, and flags. 



**Since:** BeOS R3

## Member List

### Public Attributes

* `rgb_color` [background_color](#a3093ed6ac19914c3d36026e46783cc09)
* `bool` [click_to_open](#a5e943f22532ed0841dae40f548200e9c)
* `font_family` [f_family](#a1c63ea3b3dd3ad3e5dc6b28a0c100876)
* `font_style` [f_style](#a1fa0c40ae6617f5b0d2b2e09846231fb)
* `float` [font_size](#a8a9cd0123734d553bf9a3a1d0751b43d)
* `int32` [separator](#af8a447c33fd70f283b52cc9f4a51d5f5)
* `bool` [triggers_always_shown](#a9dec783b348ac00ebbd6315d8469a7fb)

## Detailed Member Documentation

### `background_color`

```cpp
menu_info::background_color
```

The menu's background color.



**Since:** BeOS R3

---

### `click_to_open`

```cpp
menu_info::click_to_open
```

Whether or not the menu opens on click. The default value is `true`.



**Since:** BeOS R3

---

### `f_family`

```cpp
menu_info::f_family
```

The font family used to draw menu items.



**Since:** BeOS R3

---

### `f_style`

```cpp
menu_info::f_style
```

The font style used to draw menu items.



**Since:** BeOS R3

---

### `font_size`

```cpp
menu_info::font_size
```

The font size to draw menu items with.



**Since:** BeOS R3

---

### `separator`

```cpp
menu_info::separator
```

The style of horizontal line to use to separates groups of items in a menu.



**Since:** BeOS R3

---

### `triggers_always_shown`

```cpp
menu_info::triggers_always_shown
```

Whether or not trigger underlines should always be shown. The default value is `false`.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structmenu__info.html).
