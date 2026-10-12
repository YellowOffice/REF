---
name: BRefFilter
type: class
kit: storage_kit
brief: "Allows you to filter the items displayed in a file panel"
source: haiku-book
---

# BRefFilter Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Tracker Kit](group__libtracker.md)

## Description

Allows you to filter the items displayed in a file panel. 



**Since:** BeOS R3

## Member List

### Public Member Functions

* `virtual bool` [Filter](#ab6cd680428bb5d60a747a8b033795a7d) (const entry_ref *ref, BNode *node, struct stat_beos *stat, const char *mimeType)=0 — Hook method that's called on each file in the target directory displayed by a file panel.

## Detailed Member Documentation

### `Filter()`

```cpp
bool BRefFilter::Filter(const entry_ref * ref, BNode * node, struct stat_beos * stat, const char * mimeType)
```

Hook method that's called on each file in the target directory displayed by a file panel. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The file currently under consideration. |
| `node` | The node currently under consideration. |
| `stat` | The stat information of the file. |
| `mimeType` | The MIME type of the file. |





**Returns:** Whether or not the entry is a valid candidate for an open/save dialog.



**See also:** [BFilePanel::SetRefFilter()](classBFilePanel.md#a573e40a3e16a18392e6c728581ab149e)



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBRefFilter.html).
