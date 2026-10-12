---
name: node_ref
type: struct
kit: storage_kit
brief: "Reference structure to a particular vnode on a device"
source: haiku-book
---

# node_ref Struct
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Reference structure to a particular vnode on a device. 



**Since:** BeOS R3

## Member List

### Public Member Functions

* [node_ref](#a2b097557fa33781260d4a566c19d907c) () — Creates an uninitialized node_ref object.
* [node_ref](#a94c3c6a2b3277965a85d9f7ed5c07ef9) (const node_ref &other) — Creates a copy of the given node_ref object.
* `bool` [operator==](#a01f8d43a61ba910af3390f1eb6f52d26) (const node_ref &other) const — Tests whether this node_ref and the supplied one are equal.
* `bool` [operator!=](#ad4dab79b91781c05e998b767b874b0aa) (const node_ref &other) const — Tests whether this node_ref and the supplied one are NOT equal.
* `bool` [operator<](#aa116637e70bb5c74bc2eb8bd882cc8fe) (const node_ref &other) const — Tests whether this node_ref is less than the supplied one.
* `node_ref &` [operator=](#ac11068e1e602560147bbfd69883bc0d9) (const node_ref &other) — Makes this node ref a copy of the supplied one.

### Public Attributes

* `dev_t` [device](#a9c22ea29daa9253ca04088117808e3c1) — The device number on which the node is located.
* `ino_t` [node](#a374a1e7f07677c0dd2ac949b4441d642) — The node's inode number.

## Detailed Member Documentation

### `node_ref()`

```cpp
node_ref::node_ref()
```

Creates an uninitialized [node_ref](structnode__ref.md) object. 



**Since:** BeOS R3

---

### `node_ref()`

```cpp
node_ref::node_ref(const node_ref & other)
```

Creates a copy of the given [node_ref](structnode__ref.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | the [node_ref](structnode__ref.md) to be copied. |





**Since:** BeOS R3

---

### `operator!=()`

```cpp
bool node_ref::operator!=(const node_ref & other)const
```

Tests whether this [node_ref](structnode__ref.md) and the supplied one are NOT equal. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [node_ref](structnode__ref.md) to be compared against. |





**Returns:** `true`, if the objects are **NOT** equal, `false` otherwise.



**Since:** BeOS R3

---

### `operator<()`

```cpp
bool node_ref::operator<(const node_ref & other)const
```

Tests whether this [node_ref](structnode__ref.md) is less than the supplied one. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [node_ref](structnode__ref.md) to be compared against. |





**Returns:** `true`, if this [node_ref](structnode__ref.md) is less than *other*, `false` otherwise.



**Since:** Haiku R1

---

### `operator=()`

```cpp
node_ref & node_ref::operator=(const node_ref & other)
```

Makes this node ref a copy of the supplied one. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [node_ref](structnode__ref.md) to be copied. |





**Returns:** A reference to this object.



**Since:** BeOS R3

---

### `operator==()`

```cpp
bool node_ref::operator==(const node_ref & other)const
```

Tests whether this [node_ref](structnode__ref.md) and the supplied one are equal. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [node_ref](structnode__ref.md) to be compared against. |





**Returns:** `true`, if the objects are equal, `false` otherwise.



**Since:** BeOS R3

---

### `device`

```cpp
node_ref::device
```

The device number on which the node is located. 



**Since:** BeOS R3

---

### `node`

```cpp
node_ref::node
```

The node's inode number. 



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structnode__ref.html).
