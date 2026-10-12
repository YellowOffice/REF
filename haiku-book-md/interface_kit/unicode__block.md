---
name: unicode_block
type: class
kit: interface_kit
brief: "Describes the blocks of Unicode characters supported by a font"
source: haiku-book
---

# unicode_block Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Describes the blocks of Unicode characters supported by a font. 



**See also:** [BFont::Blocks()](classBFont.md#a8151aa73d7f435cd9c4115a8b92f62cc)



**Since:** BeOS R4

## Member List

### Public Member Functions

* [unicode_block](#ab71df865eed4a1744130f9863fa31cbd) () — Construct a unicode_block and set block data to 0.
* [unicode_block](#a97bb20127c06e6f815e46a08af7f0d6f) (uint64 block2, uint64 block1) — Construct a unicode_block object and initialize it with the supplied Unicode block range.
* `bool` [Includes](#a7df05e1625e331254b2b7fbe368b0b76) (const unicode_block &block) const — Determines if block is a subset of the unicode_block object.
* `unicode_block` [operator&](#ad0d8df788d12f8fa31ced85dcd958079) (const unicode_block &block) const — Creates and returns a new unicode_block object that is the intersection of block and the unicode_block object.
* `unicode_block` [operator|](#aabab32d560e1459c6334ae3170395528) (const unicode_block &block) const — Creates and returns a new unicode_block object that is the union of block and the unicode_block object.
* `unicode_block &` [operator=](#a28f6a0ebc61ae63a20cf48e37f829467) (const unicode_block &block) — Copies block data into the left-hand side object.
* `bool` [operator==](#aad1dde41862d7971c713d0fc08bd7f30) (const unicode_block &block) const — Determines if the block object are exactly equal.
* `bool` [operator!=](#afd5b5b4264e233118b671d882282ecd7) (const unicode_block &block) const — Determines if the block object are not equal.

## Detailed Member Documentation

### `unicode_block()`

```cpp
unicode_block::unicode_block()
```

Construct a `unicode_block` and set block data to 0. 


You must initialize the block data before before using this object.



**Since:** BeOS R4

---

### `unicode_block()`

```cpp
unicode_block::unicode_block(uint64 block2, uint64 block1)
```

Construct a `unicode_block` object and initialize it with the supplied Unicode block range. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `block2` | End block. |
| `block1` | Begin block. |





**Since:** BeOS R4

---

### `Includes()`

```cpp
bool unicode_block::Includes(const unicode_block & block)const
```

Determines if *block* is a subset of the `unicode_block` object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `block` | The Unicode block to check. |





**Returns:** Whether or not *block* is a subset of the `unicode_block` object.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | *block* is a subset of the current `unicode_block`. |
| false | *block* is NOT a subset of the current `unicode_block`. |





**Since:** BeOS R4

---

### `operator!=()`

```cpp
bool unicode_block::operator!=(const unicode_block & block)const
```

Determines if the block object are not equal. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `block` | The unicode block to compare against. |





**Returns:** `true` if the block object are NOT equal, `false` if the block objects are exactly equal.



**Since:** BeOS R4

---

### `operator&()`

```cpp
unicode_block unicode_block::operator&(const unicode_block & block)const
```

Creates and returns a new `unicode_block` object that is the intersection of *block* and the `unicode_block` object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `block` | The Unicode block to intersect with. |





**Returns:** The intersection of *block* and the `unicode_block` object.



**Since:** BeOS R4

---

### `operator=()`

```cpp
unicode_block & unicode_block::operator=(const unicode_block & block)
```

Copies *block* data into the left-hand side object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `block` | The unicode block to copy from. |





**Returns:** A copy of *block*.



**Since:** BeOS R4

---

### `operator==()`

```cpp
bool unicode_block::operator==(const unicode_block & block)const
```

Determines if the block object are exactly equal. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `block` | The unicode block to compare against. |





**Returns:** `true` if the block object are exactly equal, `false` otherwise.



**Since:** BeOS R4

---

### `operator|()`

```cpp
unicode_block unicode_block::operator|(const unicode_block & block)const
```

Creates and returns a new `unicode_block` object that is the union of *block* and the `unicode_block` object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `block` | The Unicode block to form a union with. |





**Returns:** The union of *block* and the `unicode_block` object.



**Since:** BeOS R4

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classunicode__block.html).
