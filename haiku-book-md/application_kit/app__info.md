---
name: app_info
type: struct
kit: application_kit
brief: "Provides info for a running app"
source: haiku-book
---

# app_info Struct
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Provides info for a running app. 



**Since:** BeOS R3

## Member List

### Public Member Functions

* [app_info](#afde0f2b2b1d183bfc66241fd4e76b8b1) () — Creates an uninitialized app_info.
* [~app_info](#af78aefcb1e8931519035712f745a0662) () — Does nothing.

### Public Attributes

* `uint32` [flags](#ad9fb2ef08478dd943647df6c90c9bf7e) — Mask of flags that determine the behavior of the application.
* `port_id` [port](#a7ee43d42f9ef4055d0efb9e79faffbe7) — The main thread port, or -1 if the application isn't running.
* `entry_ref` [ref](#af8255d396dd76b981666223df2f2106a) — A file ref that was executed to run the application.
* `char` signature [B_MIME_TYPE_LENGTH] — The signature that uniquely identifies the application.
* `team_id` [team](#a5a09b8a902a64bd909f93ed32d3edb68) — The team id or -1 if the application isn't running.
* `thread_id` [thread](#a2d3c41d83021944aadbb43c3c88dc4fe) — The main thread id or -1 if the application isn't running.

## Detailed Member Documentation

### `app_info()`

```cpp
app_info::app_info()
```

Creates an uninitialized [app_info](structapp__info.md). 



**Since:** BeOS R3

---

### `~app_info()`

```cpp
app_info::~app_info()
```

Does nothing. 



**Since:** BeOS R3

---

### `flags`

```cpp
app_info::flags
```

Mask of flags that determine the behavior of the application. 



**Since:** BeOS R3

---

### `port`

```cpp
app_info::port
```

The main thread port, or -1 if the application isn't running. 



**Since:** BeOS R3

---

### `ref`

```cpp
app_info::ref
```

A file ref that was executed to run the application. 



**Since:** BeOS R3

---

### `team`

```cpp
app_info::team
```

The team id or -1 if the application isn't running. 



**Since:** BeOS R3

---

### `thread`

```cpp
app_info::thread
```

The main thread id or -1 if the application isn't running. 



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structapp__info.html).
