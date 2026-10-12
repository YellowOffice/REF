---
name: BFilePanel
type: class
kit: storage_kit
brief: "Displays a standard Open/Save dialog"
source: haiku-book
---

# BFilePanel Class
**Kit/Group:** [Storage Kit](../storage_kit/group__storage.md) | [Tracker Kit](group__libtracker.md)

## Description

Displays a standard Open/Save dialog. 


A save panel looks like this:





An open dialog looks similar but doesn't have a text box for the file name.


You generally construct a [BFilePanel](classBFilePanel.md) object in response to a user action for example the user clicks on a "Open" or "Save"/"Save As" menu item. Constructing an open or save panel is easy:



```cpp
BFilePanel* openPanel = new BFilePanel(B_OPEN_PANEL);
BFilePanel* savePanel = new BFilePanel(B_SAVE_PANEL);
```

You can then call methods to indicate what directory to display, whether or not multiple selections are allowed, whether or not the user is allowed to open a directory, what target view to send send notifications, and more. See the constructor for details.


You can modify the look of your [BFilePanel](classBFilePanel.md) object by calling the [SetButtonLabel()](classBFilePanel.md#ad7ca9a1c60b2945075d73649fdfb348b) and [SetSaveText()](classBFilePanel.md#a948e0e67e7d0831b8f4ba3696672503a) methods. If you want to change the look even more radically you can get alter the panel's [BWindow](../interface_kit/classBWindow.md) and [BView](../interface_kit/classBView.md) objects. You get the window by calling the [Window()](classBFilePanel.md#ae08c1a26cbeea8beaeabcab2a41579c6) method. With a pointer to the panel's [BWindow](../interface_kit/classBWindow.md) object you can drill down to the various views contained therein.


Once you have constructed and customized your [BFilePanel](classBFilePanel.md) object you should call the [Show()](classBFilePanel.md#a9a11515a7d9989d86d6bedc94017b23b) method to display the panel to the user.


When the user confirms or cancels a [BMessage](../application_kit/classBMessage.md) object is constructed and sent to the target of the [BFilePanel](classBFilePanel.md) object. You can specify a different target in the constructor or by calling the [SetTarget()](classBFilePanel.md#a6523bd53af73c514d9fafec0c6384417) method.


**Open Notifications**


For open notifications the default target is `be_app_messenger` and is caught by the RefsReceived() method The `what` field is set to `B_REFS_RECEIVED`. You can set your own message by calling the [SetMessage()](classBFilePanel.md#a6c150d4f445e57e090b9e4b4234e16f5) method; in this case the message will be sent to the target's MessageReceived() method instead.


The `refs` field of the message contains an `entry_ref` structure for each entry that the user has selected. The `refs` field is of type `B_REF_TYPE`. If the selected entry is a symlink to a file you'll need to dereference the file yourself. You can do this more easily by turning the `ref` into a [BEntry](classBEntry.md) passing `true` into the `traverse` argument like this:



```cpp
BEntry entry(ref, true);
```

**Save Notifications**


Save notifications are always sent to the target's MessageReceived() method unlike open notifications. The `what` field of the message is set to `B_SAVE_REQUESTED`. The `directory` field contain a single `entry_ref` structure that points to the directory that the entry is saved to. The text that the user typed in the save panel's text view is put in the `name` field and is of type `B_STRING_TYPE`.


**Cancel Notifications**


Cancel notifications are sent when the panel is hidden whether by the user clicking the cancel button, closing the dialog, or confirming the action (assuming hide-when-done is turned on).


Cancel notifications can be caught by the MessageReceived() method of the target. The `what` field is set to `B_CANCEL`. The `old_what` field is set to the previous what value which is useful if you have overridden the default message. The `what` field of the message you sent is put in the `old_what` field.


The `source` field is a pointer of `B_POINTER_TYPE` to the closed [BFilePanel](classBFilePanel.md) object. When the [BFilePanel](classBFilePanel.md) object is closed it is not destroyed, it is hidden instead. You can then delete the [BFilePanel](classBFilePanel.md) object or leave it be and simply call [Show()](classBFilePanel.md#a9a11515a7d9989d86d6bedc94017b23b) to use the panel next time you need it.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BFilePanel](#a439f0ac01edd3d0dd8f4a4b07b7f034b) (file_panel_mode mode=B_OPEN_PANEL, BMessenger *target=NULL, const entry_ref *directory=NULL, uint32 nodeFlavors=0, bool allowMultipleSelection=true, BMessage *message=NULL, BRefFilter *refFilter=NULL, bool modal=false, bool hideWhenDone=true) — Creates and initializes a BFilePanel object.
* `virtual` [~BFilePanel](#a4ee47f070fe2f25b57305b408430ab19) () — Destroys the file panel object.
* `status_t` [GetNextSelectedRef](#a8b3351d8b9663c1e8fb3a60f8cee1c83) (entry_ref *ref) — Sets the ref pointer to the next entry in the directory.
* `void` [GetPanelDirectory](#a252fefadcb045dca2a0f84ff13f9cca8) (entry_ref *ref) const — Gets the entry ref of the panel and sets ref to point to it.
* `void` [Hide](#acd03421c7c41f16ef98748511bf93892) () — Hides the file panel.
* `bool` [HidesWhenDone](#ae1f607e61d456dd2f3cf2558af96a89f) () const — Gets whether or not the panel should hide on confirm or cancel.
* `bool` [IsShowing](#a744ca07473066cd3c8de391135d0e473) () const — Determines whether or not the file panel is shown.
* `BMessenger` [Messenger](#aaa95bdc5b6367691a47d594eadf66d6e) () const — Gets the panel's target messenger object.
* `file_panel_mode` [PanelMode](#a92779bd92a8f645e24e5e01d22e978b6) () const — Gets the panel mode, either B_OPEN_PANEL or B_SAVE_PANEL.
* `BRefFilter *` [RefFilter](#a48c4355f7b8c96ee8d30702c5a22c84b) () const — Gets the BRefFilter object associated with the panel.
* `void` [Refresh](#ab7c7351d8b387e6824939e7f3cccf2c4) () — Refresh the directory or the panel causing the entries to be re-run through the BRefFilter::Filter() method.
* `void` [Rewind](#a9180700dffb4009583e7f40f16e5b91a) () — Sets the entry ref back to the top of the list.
* `virtual void` [SendMessage](#a9f9dea8a4668c6c8f7582750fe7e8c30) (const BMessenger *target, BMessage *message) — Sends the message to the target BHandler messenger.
* `void` [SetButtonLabel](#ad7ca9a1c60b2945075d73649fdfb348b) (file_panel_button button, const char *label) — Set the button label specified by button to text.
* `void` [SetHideWhenDone](#a0c83fafc916144019c15653be8cbf13b) (bool hideWhenDone) — Sets whether or not the panel should hide on confirm or cancel.
* `void` [SetMessage](#a6c150d4f445e57e090b9e4b4234e16f5) (BMessage *message) — Sets the target messenge.
* `void` [SetPanelDirectory](#aa68fd9531e74e8cb123c3005a189d8ec) (const BDirectory *newDirectory) — Sets the entry ref of the panel to the directory referenced by dir.
* `void` [SetPanelDirectory](#a9ba8c35c592a9ba0bee622e124f439a1) (const BEntry *newDirectory) — Sets the entry ref of the panel to the directory referenced by entry.
* `void` [SetPanelDirectory](#a3793e34c75a1e2a13ca1610ff803e742) (const char *newDirectory) — Sets the entry ref of the panel to the directory referenced by path.
* `void` [SetPanelDirectory](#a6f78ddfb53546fdda9f5eb9883feb12b) (const entry_ref *newDirectory) — Sets the entry ref of the panel to the directory contained by ref.
* `void` [SetRefFilter](#a573e40a3e16a18392e6c728581ab149e) (BRefFilter *filter) — Sets the BRefFilter used by the panel to filter entries.
* `void` [SetSaveText](#a948e0e67e7d0831b8f4ba3696672503a) (const char *text) — Set some save text to display in the save dialog.
* `void` [SetTarget](#a6523bd53af73c514d9fafec0c6384417) (BMessenger target) — Sets the target messenger.
* `void` [Show](#a9a11515a7d9989d86d6bedc94017b23b) () — Displays the file panel on screen.
* `BWindow *` [Window](#ae08c1a26cbeea8beaeabcab2a41579c6) () const — Gets a pointer to the BWindow object used by the file panel.
* `virtual void` [WasHidden](#a9fcdbb4061db0553ac931caee266c567) () — Hook method that gets called when the file panel is hidden due to a user action.
* `virtual void` [SelectionChanged](#afc73710e12dc128609f391334917fc20) () — Hook method that gets called when the entry ref references by the file panel changes.

## Detailed Member Documentation

### `BFilePanel()`

```cpp
BFilePanel::BFilePanel(file_panel_mode mode = B_OPEN_PANEL, BMessenger * target = NULL, const entry_ref * ref = NULL, uint32 nodeFlavors = 0, bool multipleSelection = true, BMessage * message = NULL, BRefFilter * filter = NULL, bool modal = false, bool hideWhenDone = true)
```

Creates and initializes a [BFilePanel](classBFilePanel.md) object. 


The constructor has many parameters but they may generally be set after the object has been constructed. The only parameters that must be set during construction are the *mode*, *nodeFlavors*, *multipleSelection*, and *modal* parameters. The rest may be set after the object has been constructed by the [SetTarget()](classBFilePanel.md#a6523bd53af73c514d9fafec0c6384417), [SetPanelDirectory()](classBFilePanel.md#a9ba8c35c592a9ba0bee622e124f439a1), [SetMessage()](classBFilePanel.md#a6c150d4f445e57e090b9e4b4234e16f5), [SetRefFilter()](classBFilePanel.md#a573e40a3e16a18392e6c728581ab149e), and [SetHideWhenDone()](classBFilePanel.md#a0c83fafc916144019c15653be8cbf13b) methods.


Parameters

| Parameter | Description |
| :--- | :--- |
| `mode` | Set to `B_OPEN_PANEL` for an open panal or `B_SAVE_PANEL` for a save panel. Default is `B_OPEN_PANEL`. |
| `target` | The [BMessenger](../application_kit/classBMessenger.md) object that sends messages to the [BLooper](../application_kit/classBLooper.md) or [BHandler](../application_kit/classBHandler.md) controlled by the file panel. |
| `ref` | The directory to display, by default the current working directory. |
| `nodeFlavors` | One or more option flags, this applies to open panels only. * `B_FILE_NODE` Can select files and symlinks to files.  * `B_DIRECTORY_NODE` Can select directories and symlinks to directories.  * `B_SYMLINK_NODE` Can select symlinks only. |
| `multipleSelection` | Whether or not the user is allowed to select more than one item to open. Save panels should always set this to `false`. |
| `message` | Message sent by the file panel on confirms or cancels. |
| `filter` | Hook method to call. |
| `modal` | Whether or not the panel is modal, defaults to `false`. |
| `hideWhenDone` | Set to `false` to keep the panel even after the user confirms or cancels. The close button will hide the panel regardless. |





**Since:** BeOS R3

---

### `~BFilePanel()`

```cpp
BFilePanel::~BFilePanel()
```

Destroys the file panel object. 


If file panel is currently being displayed it is closed. The [BRefFilter](classBRefFilter.md) object references by this panel is not destroyed by this method.



**Since:** BeOS R3

---

### `GetNextSelectedRef()`

```cpp
status_t BFilePanel::GetNextSelectedRef(entry_ref * ref)
```

Sets the *ref* pointer to the next entry in the directory. 



**Returns:** a status message.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_ERROR | Couldn't attain a lock on the window. |
| B_ENTRY_NOT_FOUND | End of the entry list. |





**See also:** [Rewind()](classBFilePanel.md#a9180700dffb4009583e7f40f16e5b91a)



**Since:** BeOS R3

---

### `GetPanelDirectory()`

```cpp
void BFilePanel::GetPanelDirectory(entry_ref * ref)const
```

Gets the entry ref of the panel and sets *ref* to point to it. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The `entry_ref` pointer you want set. |





**Since:** BeOS R3

---

### `Hide()`

```cpp
void BFilePanel::Hide()
```

Hides the file panel. 



**Since:** BeOS R3

---

### `HidesWhenDone()`

```cpp
bool BFilePanel::HidesWhenDone(void)const
```

Gets whether or not the panel should hide on confirm or cancel. 


Panel always hides if the user clicks the window's close button.



**Returns:** `true` if panel will hide, `false` if panel will not hide.



**See also:** [SetHideWhenDone()](classBFilePanel.md#a0c83fafc916144019c15653be8cbf13b)



**Since:** BeOS R3

---

### `IsShowing()`

```cpp
bool BFilePanel::IsShowing()const
```

Determines whether or not the file panel is shown. 



**Returns:** `true` if visible, `false` if hidden.



**See also:** [Show()](classBFilePanel.md#a9a11515a7d9989d86d6bedc94017b23b)



**Since:** BeOS R3

---

### `Messenger()`

```cpp
BMessenger BFilePanel::Messenger()const
```

Gets the panel's target messenger object. 



**Returns:** The [BMessenger](../application_kit/classBMessenger.md) object that sends messages for this panel.



**Since:** BeOS R3

---

### `PanelMode()`

```cpp
file_panel_mode BFilePanel::PanelMode()const
```

Gets the panel mode, either `B_OPEN_PANEL` or `B_SAVE_PANEL`. 



**Returns:** `B_OPEN_PANEL` if the panel is an open panel, or `B_SAVE_PANEL` if the panel is a save panel.



**Since:** BeOS R3

---

### `RefFilter()`

```cpp
BRefFilter * BFilePanel::RefFilter()const
```

Gets the [BRefFilter](classBRefFilter.md) object associated with the panel. 



**Returns:** The [BRefFilter](classBRefFilter.md) set to the panel.



**See also:** [BRefFilter::Filter()](classBRefFilter.md#ab6cd680428bb5d60a747a8b033795a7d)



**Since:** BeOS R3

---

### `Refresh()`

```cpp
void BFilePanel::Refresh()
```

Refresh the directory or the panel causing the entries to be re-run through the [BRefFilter::Filter()](classBRefFilter.md#ab6cd680428bb5d60a747a8b033795a7d) method. 



**Since:** BeOS R3

---

### `Rewind()`

```cpp
void BFilePanel::Rewind()
```

Sets the entry ref back to the top of the list. 



**See also:** [SelectionChanged()](classBFilePanel.md#afc73710e12dc128609f391334917fc20)



**Since:** BeOS R3

---

### `SelectionChanged()`

```cpp
void BFilePanel::SelectionChanged()
```

Hook method that gets called when the entry ref references by the file panel changes. 



**See also:** [GetNextSelectedRef()](classBFilePanel.md#a8b3351d8b9663c1e8fb3a60f8cee1c83)



**Since:** BeOS R3

---

### `SendMessage()`

```cpp
void BFilePanel::SendMessage(const BMessenger * messenger, BMessage * message)
```

Sends the *message* to the target [BHandler](../application_kit/classBHandler.md) *messenger*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `messenger` | The target [BHandler](../application_kit/classBHandler.md) to send the message to. |
| `message` | The message to send. |





**See also:** [BMessenger::SendMessage()](../application_kit/classBMessenger.md#aebe5aba546fa4a4696988b1bf6028f3c)



**Since:** BeOS R3

---

### `SetButtonLabel()`

```cpp
void BFilePanel::SetButtonLabel(file_panel_button button, const char * text)
```

Set the button label specified by *button* to *text*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `button` | The button to set the label of. |
| `text` | The text to set the button label to. |





**Since:** BeOS R3

---

### `SetHideWhenDone()`

```cpp
void BFilePanel::SetHideWhenDone(bool on)
```

Sets whether or not the panel should hide on confirm or cancel. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `on` | `true` to hide, `false` to not hide when done. |





**Since:** BeOS R3

---

### `SetMessage()`

```cpp
void BFilePanel::SetMessage(BMessage * message)
```

Sets the target messenge. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The [BMessage](../application_kit/classBMessage.md) object to send on confirm. |





**Since:** BeOS R3

---

### `SetPanelDirectory()`

```cpp
void BFilePanel::SetPanelDirectory(const BDirectory * dir)
```

Sets the entry ref of the panel to the directory referenced by *dir*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `dir` | The [BDirectory](classBDirectory.md) object pointing to the desired directory. |





**Since:** BeOS R3

---

### `SetPanelDirectory()`

```cpp
void BFilePanel::SetPanelDirectory(const BEntry * entry)
```

Sets the entry ref of the panel to the directory referenced by *entry*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `entry` | The [BEntry](classBEntry.md) object pointing to the desired directory. |





**Since:** BeOS R3

---

### `SetPanelDirectory()`

```cpp
void BFilePanel::SetPanelDirectory(const char * path)
```

Sets the entry ref of the panel to the directory referenced by *path*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `path` | The path of the desired directory. |





**Since:** BeOS R3

---

### `SetPanelDirectory()`

```cpp
void BFilePanel::SetPanelDirectory(const entry_ref * ref)
```

Sets the entry ref of the panel to the directory contained by *ref*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The entry contained by the desired panel directory. |





**Since:** BeOS R3

---

### `SetRefFilter()`

```cpp
void BFilePanel::SetRefFilter(BRefFilter * filter)
```

Sets the [BRefFilter](classBRefFilter.md) used by the panel to filter entries. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `filter` | The [BRefFilter](classBRefFilter.md) object to set. |





**See also:** [BRefFilter::Filter()](classBRefFilter.md#ab6cd680428bb5d60a747a8b033795a7d)



**Since:** BeOS R3

---

### `SetSaveText()`

```cpp
void BFilePanel::SetSaveText(const char * text)
```

Set some save text to display in the save dialog. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `text` | The text to display. |





**Since:** BeOS R3

---

### `SetTarget()`

```cpp
void BFilePanel::SetTarget(BMessenger target)
```

Sets the target messenger. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | the target [BMessenger](../application_kit/classBMessenger.md) object to set. |





**Since:** BeOS R3

---

### `Show()`

```cpp
void BFilePanel::Show()
```

Displays the file panel on screen. 



**Since:** BeOS R3

---

### `WasHidden()`

```cpp
void BFilePanel::WasHidden()
```

Hook method that gets called when the file panel is hidden due to a user action. 


[WasHidden()](classBFilePanel.md#a9fcdbb4061db0553ac931caee266c567) is not called if you call [Hide()](classBFilePanel.md#acd03421c7c41f16ef98748511bf93892) manually.



**Since:** BeOS R3

---

### `Window()`

```cpp
BWindow * BFilePanel::Window()const
```

Gets a pointer to the [BWindow](../interface_kit/classBWindow.md) object used by the file panel. 



**Returns:** A pointer to the [BWindow](../interface_kit/classBWindow.md) object used by the file panel.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBFilePanel.html).
