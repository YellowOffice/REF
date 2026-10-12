---
name: BTab
type: class
kit: interface_kit
brief: "A tab that goes in a BTabView"
source: haiku-book
---

# BTab Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A tab that goes in a [BTabView](classBTabView.md). 



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BTab](#a0bf106f8dc2ea9f92372ddd128012a55) (BMessage *archive) — Archive Constructor.
* [BTab](#a04eeacfb469eba435e4d0778e15b5871) (BView *contentsView=NULL) — Initializes a new BTab object as part of a tabView.
* `virtual` ~BTab () — Destructor.
* `virtual status_t` [Archive](#aac9d5205065158ab4079c2b8913c495d) (BMessage *data, bool deep=true) const — Archives the object into the data message.
* `virtual void` [Deselect](#acd30148ad1e9071d167c50ec6ebf75ec) () — Called by the BTabView when the tab is de-selected.
* `virtual void` [DrawFocusMark](#ad15c17720fb1794da9261d612673d02d) (BView *owner, BRect frame) — Draws the mark indicating that the BTab object is in focus.
* `virtual void` [DrawLabel](#a338e11022b6305af859d680635ae78f2) (BView *owner, BRect frame) — Draws the tab's title.
* `virtual void` [DrawTab](#aa563ba3f1d37d86c81510281ea45694d) (BView *owner, BRect frame, tab_position position, bool full=true) — Draws the tab and label according to position and full.
* `bool` IsEnabled () const — Returns whether or not the tab is enabled.
* `bool` IsFocus () const — Returns whether or not the tab is the window's focus view.
* `bool` [IsSelected](#a62ec71ce9a64b267b5a17f46459a0898) () const — Returns whether or not the tab is selected.
* `const char *` [Label](#a43f2f6b75818c4ce301860bfa62fe7f9) () const — Returns the tab's label (the target view's name).
* `void` [MakeFocus](#acd46898f0069953226a05fc1131c344c) (bool focus=true) — Makes the tab the window's focus view or removes it.
* `virtual status_t` [Perform](#a4db961b6bd5104b4c9d76b6136bd6856) (uint32 d, void *arg) — Perform some action. (Internal Method)
* `virtual void` [Select](#a7f0670c4a57d07265e8e7ea59304d4b2) (BView *owner) — Called by the BTabView when the tab is selected.
* `virtual void` [SetEnabled](#ad97f4b0c53a1d9698d1c8938c48ff9a2) (bool enable) — Enables or disables the tab.
* `virtual void` [SetLabel](#a0771a3e4d36f32685712b14f16250b2e) (const char *label) — Sets the tab label.
* `virtual void` [SetView](#acdb2c4b1cbf280d515e1259e856f75f9) (BView *view) — Sets the view to be displayed for this tab.
* `BView *` View () const — Returns a pointer to the view to be displayed for this tab.
* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).

### Static Public Member Functions

* `static BArchivable *` [Instantiate](#aa3f3f900a862c967238dfae0cb22556c) (BMessage *archive) — Instantiates a BTab object from the passed in archive.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BTab()`

```cpp
BTab::BTab(BView * contentsView = NULL)
```

Initializes a new [BTab](classBTab.md) object as part of a *tabView*. 


The [BTab](classBTab.md) is enabled, but not selected nor the current focus. *contentsView* is set as the tab's target view – when the tab is selected, its target view is activated.



**Since:** BeOS R3

---

### `BTab()`

```cpp
BTab::BTab(BMessage * archive)
```

Archive Constructor. 



**Since:** BeOS R3

---

### `Archive()`

```cpp
status_t BTab::Archive(BMessage * data, bool deep = true)const
```

Archives the object into the *data* message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A pointer to the [BMessage](../application_kit/classBMessage.md) object to archive the object into. |
| `deep` | Whether or not to archive child views as well. |





**Returns:** A status code, `B_OK` if everything went well or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object was archived. |
| B_NO_MEMORY | Ran out of memory while archiving the object. |





**Since:** BeOS R3


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44).

---

### `Deselect()`

```cpp
void BTab::Deselect()
```

Called by the [BTabView](classBTabView.md) when the tab is de-selected. 



**Since:** BeOS R3

---

### `DrawFocusMark()`

```cpp
void BTab::DrawFocusMark(BView * owner, BRect frame)
```

Draws the mark indicating that the [BTab](classBTab.md) object is in focus. 


This consists of a blue line drawn across the bottom of the tab frame by default.



**Since:** BeOS R3

---

### `DrawLabel()`

```cpp
void BTab::DrawLabel(BView * owner, BRect frame)
```

Draws the tab's title. 



**Since:** BeOS R3

---

### `DrawTab()`

```cpp
void BTab::DrawTab(BView * owner, BRect frame, tab_position position, bool full = true)
```

Draws the tab and label according to *position* and *full*. 


This method draws the tab, then draws the tab's title by calling [DrawLabel()](classBTab.md#a338e11022b6305af859d680635ae78f2). The *position* of the tab may affect how the tab is rendered – for example the first tab may have a different appearance than the other tabs. You may override this method to draw tabs differently in your [BTab](classBTab.md) subclass.


Parameters

| Parameter | Description |
| :--- | :--- |
| `owner` | The view that owns the tab. |
| `frame` | The frame rectangle to draw in. |
| `position` | May affect how the tab is rendered. Choices include: * `B_TAB_FIRST` The first tab  * `B_TAB_FRONT` The selected or active tab  * `B_TAB_ANY` Tab that is not first or front |
| `full` | Whether or not to completely draw the tab. All tabs were full except for the tab before the selected tab on BeOS R5. |





> [!WARNING]
> The *position* and *full* parameters should no longer be used. This information can be gathered from [BTabView](classBTabView.md) by calling the [BTabView::IndexOf()](classBTabView.md#a7bb1dd022ca51fc1f4c4a1724ebd024b), [BTabView::Selection()](classBTabView.md#a375938ffbd6f7331691aa407298e4ae0), and [BTabView::CountTabs()](classBTabView.md#a83dff446e7ba13d9d2e8881acad5b46f) methods.



**Since:** BeOS R3

---

### `Instantiate()`

```cpp
BArchivable * BTab::Instantiate(BMessage * archive)
```

Instantiates a [BTab](classBTab.md) object from the passed in *archive*. 



**Since:** BeOS R3

---

### `IsSelected()`

```cpp
bool BTab::IsSelected()const
```

Returns whether or not the tab is selected. 



**Since:** BeOS R3

---

### `Label()`

```cpp
const char * BTab::Label()const
```

Returns the tab's label (the target view's name). 



> [!WARNING]
> In BeOS, the tab label is determined from the view name. In Haiku, they can be different if [SetLabel()](classBTab.md#a0771a3e4d36f32685712b14f16250b2e) was used.



**Since:** BeOS R3

---

### `MakeFocus()`

```cpp
void BTab::MakeFocus(bool focus = true)
```

Makes the tab the window's focus view or removes it. 



**Since:** BeOS R3

---

### `Perform()`

```cpp
status_t BTab::Perform(uint32 d, void * arg)
```

Perform some action. (Internal Method) 



**Since:** BeOS R3


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a827fa92febcf925f07545aa9777df9de).

---

### `Select()`

```cpp
void BTab::Select(BView * owner)
```

Called by the [BTabView](classBTabView.md) when the tab is selected. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `owner` | The view that the tab's view should be owned by. |





**Since:** BeOS R3

---

### `SetEnabled()`

```cpp
void BTab::SetEnabled(bool enable)
```

Enables or disables the tab. 



**Since:** BeOS R3

---

### `SetLabel()`

```cpp
void BTab::SetLabel(const char * label)
```

Sets the tab label. 



> [!WARNING]
> In BeOS, setting the tab label also renamed the view attached to the tab. In Haiku, this is not the case anymore, the label and view name are independant.



**Since:** BeOS R3

---

### `SetView()`

```cpp
void BTab::SetView(BView * view)
```

Sets the view to be displayed for this tab. 


This also resets the tab label to match the view name (to preserve BeOS behavior). If you need to use a different label, SetLabel must be called after SetView.

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBTab.html).
