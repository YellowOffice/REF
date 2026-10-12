---
name: BBlockCache
type: class
kit: support_kit
brief: "A class that creates and maintains a pool of memory blocks"
source: haiku-book
---

# BBlockCache Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A class that creates and maintains a pool of memory blocks. 


In some performance critical code there might come a time where you require a lot of little blocks of memory that you want to access and dispose of continuously. Since allocating and freeing memory are 'expensive' operations, it is better to have a pool of memory blocks at your disposal. Luckily, the Haiku API provides a class that will act as the administrator of your memory pool, so you will not have to reinvent the wheel every time.


The principle is easy. The constructor takes the number of blocks you want to create beforehand, the size of the blocks, and the method of allocation. This can either be [B_OBJECT_CACHE](BlockCache_8h.md#a26e1124d33b4acdb532c49f6498df549a9dcad77c9fcf0f4be8332af2a541d004) or [B_MALLOC_CACHE](BlockCache_8h.md#a26e1124d33b4acdb532c49f6498df549a5785baf710ae44d11020aa00eadc1bca). The first one uses C++ operators `new`[] and `delete`[], while the second one uses `malloc()` and `free()`. Unless you have specific demands on performance or you want to take care of freeing the objects yourself, either way works fine.


As soon as you have the memory pool, you can [Get()](classBBlockCache.md#ad3029dc7884e862338e0b20dfdf77f18) blocks. If the pre-allocated memory blocks run out, [BBlockCache](classBBlockCache.md) will allocate new ones, so you will not have to worry about availability. As soon as you are done you can [Save()](classBBlockCache.md#a9a4b1d9199fcd8107b08f9b8b736921c) the memory back into the pool. [BBlockCache](classBBlockCache.md) will make sure that no more blocks will be saved than the initial number you requested when you created the object, so be aware of that.


As soon as you got a pointer from the [Get()](classBBlockCache.md#ad3029dc7884e862338e0b20dfdf77f18) method, you own that block of memory; this means that you have the liberty to dispose of it yourself. It also means that when you delete your [BBlockCache](classBBlockCache.md) instance, any blocks of memory that are checked out will not be destroyed. In case you might want to delete your objects yourself, make sure you free the memory the right way. If you created the object as [B_OBJECT_CACHE](BlockCache_8h.md#a26e1124d33b4acdb532c49f6498df549a9dcad77c9fcf0f4be8332af2a541d004), use `delete`[] to free your object. If you created the object as [B_MALLOC_CACHE](BlockCache_8h.md#a26e1124d33b4acdb532c49f6498df549a5785baf710ae44d11020aa00eadc1bca), use `free()`. Please note that it defeats the purpose of this class if your are going to free all the objects yourself since it basically means that when the pool runs out, [Get()](classBBlockCache.md#ad3029dc7884e862338e0b20dfdf77f18) will be allocating the objects by itself.



> [!NOTE]
> [BBlockCache](classBBlockCache.md) is thread-safe.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BBlockCache](#a03b66b65aaabf96bf08eca5f0e46f945) (uint32 blockCount, size_t blockSize, uint32 allocationType) — Allocate a new memory pool.
* `virtual` [~BBlockCache](#ae9b912af354a845798644df023639195) () — Destroy the empty blocks in the free list.
* `void *` [Get](#ad3029dc7884e862338e0b20dfdf77f18) (size_t blockSize) — Get a block from the pool of free blocks.
* `void` [Save](#a9a4b1d9199fcd8107b08f9b8b736921c) (void *pointer, size_t blockSize) — Save a block of memory to the memory pool.

## Detailed Member Documentation

### `BBlockCache()`

```cpp
BBlockCache::BBlockCache(uint32 blockCount, size_t blockSize, uint32 allocationType)
```

Allocate a new memory pool. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `blockCount` | The number of free memory blocks you want to allocate initially. This number is also used as the maximum number of free blocks that will be kept. |
| `blockSize` | The size of the blocks. |
| `allocationType` | Either [B_OBJECT_CACHE](BlockCache_8h.md#a26e1124d33b4acdb532c49f6498df549a9dcad77c9fcf0f4be8332af2a541d004) for using `new`[] and `delete`[] or [B_MALLOC_CACHE](BlockCache_8h.md#a26e1124d33b4acdb532c49f6498df549a5785baf710ae44d11020aa00eadc1bca) for `malloc()` and `free()`. |





**Since:** BeOS R3

---

### `~BBlockCache()`

```cpp
BBlockCache::~BBlockCache()
```

Destroy the empty blocks in the free list. 


Note that the blocks you checked out with [Get()](classBBlockCache.md#ad3029dc7884e862338e0b20dfdf77f18) and not checked back in with [Save()](classBBlockCache.md#a9a4b1d9199fcd8107b08f9b8b736921c) will not be freed, since ownership belongs to you. Make sure you clean up after yourself.



**Since:** BeOS R3

---

### `Get()`

```cpp
void * BBlockCache::Get(size_t blockSize)
```

Get a block from the pool of free blocks. 


If the pool runs out of free blocks, a new one will be allocated. Please note that if the size given in the `blockSize` parameter is different from the size given in the constructor, a new block of memory will be created. Only sizes that match the blocks in the memory pool will come from the pool.


Parameters

| Parameter | Description |
| :--- | :--- |
| `blockSize` | The required size of the memory block. |





**Returns:** Returns a pointer to a memory block, or `NULL` if locking the object failed.



**Since:** BeOS R3

---

### `Save()`

```cpp
void BBlockCache::Save(void * pointer, size_t blockSize)
```

Save a block of memory to the memory pool. 


The block of memory will only be added to the pool if the `blockSize` is equal to the size the object was created with and if the maximum number of free blocks in the list will not be exceeded. If not, the memory will be freed.


Note that it is perfectly valid to pass objects other than those you got from [Get()](classBBlockCache.md#ad3029dc7884e862338e0b20dfdf77f18), but please note that the way it was created conforms to the way memory is allocated and freed in this pool. Therefore, only feed blocks that were created with `new`[] if the allocation type is [B_OBJECT_CACHE](BlockCache_8h.md#a26e1124d33b4acdb532c49f6498df549a9dcad77c9fcf0f4be8332af2a541d004). Likewise, you should only use objects allocated with `malloc()` when the allocation type is [B_MALLOC_CACHE](BlockCache_8h.md#a26e1124d33b4acdb532c49f6498df549a5785baf710ae44d11020aa00eadc1bca).



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBBlockCache.html).
