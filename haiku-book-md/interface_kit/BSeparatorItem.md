---
name: BSeparatorItem
type: class
kit: interface_kit
brief: "Display separator item for BMenu class"
source: haiku-book
---

# BSeparatorItem Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Display separator item for [BMenu](classBMenu.md) class. 


A [BSeparatorItem](classBSeparatorItem.md) is used to separate groups of menu items in a [BMenu](classBMenu.md). It is drawn as a horizontal or vertical line depending on menu layout and cannot be selected or highlighted.



> [!WARNING]
> BSeparatorItems are only meant to be used with menus whose items are arranged in a `B_ITEMS_IN_COLUMN` or `B_ITEMS_IN_ROW` layout.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BSeparatorItem](#a2fc8f18fb4f675ed282a9749a54b14bf) () — Creates a new BSeparatorItem object.
* [BSeparatorItem](#aba8be62ea90296248d266ac2889d602f) (BMessage *data) — Archive constructor.
* `virtual` [~BSeparatorItem](#ab3457195dea6bbea4c47d0264252e08e) () — Destructor, does nothing.
* `virtual void` [SetEnabled](#a5fe4819a9a7dfefa298aa7943c45d1b0) (bool enable) — Does nothing, this method is defined to override the default BMenuItem behavior.
* [BMenuItem](#ac9f0315f4285fa9e29c1b4e043f67a4a) (BMenu *menu, BMessage *message=NULL) — Creates a new BMenuItem object with the specified menu and message.
* [BMenuItem](#a8056c978d88925e2dc379c2b576838a4) (BMessage *data) — Archive constructor.
* [BMenuItem](#aa36818438ad07752252f6aa6640d5d8c) (const char *label, BMessage *message, char shortcut=0, uint32 modifiers=0) — Creates a new BMenuItem object with the specified label and message.
* `virtual` [~BMenuItem](#a4581d0d7f2ca677157bb60d59bdbd58a) () — Destructor.
* `BRect` [Frame](#a13749743bcc7f435d074bf57297a7860) () const — Returns the bounds rectangle of the menu item.
* `bool` [IsEnabled](#a5b4747f5ff345a8068257697f083fc6b) () const — Returns whether or not the item is enabled.
* `bool` [IsMarked](#a9492b89007241180fe84058000adf121) () const — Returns whether or not the item is marked.
* `const char *` [Label](#ab0e1137c2da0aebcb42c5e07d73e2043) () const — Returns the item's label.
* `BMenu *` [Menu](#ab6abecc541115fb6dd61cf16c25636c8) () const — Returns a pointer to the menu that the item is attached to.
* `virtual void` [SetEnabled](#a1179e9734ed7b84d4f1ba829ed721e22) (bool enable) — Enables or disables the menu item.
* `virtual void` [SetLabel](#a83c794e5d75b300a51e8bb70c5255677) (const char *name) — Sets the menu item label to string.
* `virtual void` [SetMarked](#a0b896795700a46215ee7884940b39119) (bool mark) — Marks or unmarks the menu item.
* `virtual void` [SetShortcut](#aec7480dc85b1f62ff9678a22ba2b6ff3) (char shortcut, uint32 modifiers) — Set the keyboard shortcut of the menu item.
* `virtual void` [SetTrigger](#a559d29474bdd2608ab263f831a1a9ac4) (char trigger) — Set the character that activates this menu item. The triggered character is drawn underlined in the menu.
* `char` [Shortcut](#a0a27adb900a9a831a7ff4a72685a2fe0) (uint32 *_modifiers=NULL) const — Returns the currently set shortcut and fills out modifiers with a bitmap of the modifier keys required to invoke the item.
* `BMenu *` [Submenu](#a143dcb6b5906e6598f8fb594b7f36757) () const — Returns a pointer to the attached menu.
* `char` [Trigger](#aeebb4d9309ca000aafda565e40e8561e) () const — Returns the item's trigger character.
* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).
* [BInvoker](#ad03149db91cd6460f12adb72780a7080) () — Initializes a BInvoker without a message or target.
* [BInvoker](#adaf9b3df1b4a318e10df04a5eb9f59ee) (BMessage *message, BMessenger target) — Initializes the BInvoker with message and sets the target messenger where the message is sent when Invoke() is called.
* [BInvoker](#a6405334f1589c7a9fc3604ff8a4c8c83) (BMessage *message, const BHandler *handler, const BLooper *looper=NULL) — Initializes the BInvoker with message and sets the target to either a local handler or as the preferred handler of a local looper where the message is sent when Invoke() is called.
* `virtual` [~BInvoker](#a68714c3b78a2cf2931daf54f5dc94dca) () — Destructor method, deletes the BMessage object if set.
* `uint32` [Command](#a6eb323ab957a5ee99e8db2b2fb0e9800) () const — Returns the message's what data member.
* `BHandler *` [HandlerForReply](#a710e78abc03eb29e9e25d11d34c874cc) () const — Returns the previously set reply handler or NULL if not set.
* `virtual status_t` [Invoke](#ad4eb9ad4b3b8286f2a155ad7f087511c) (BMessage *message=NULL) — Sends the message to the invoker's target.
* `status_t` [InvokeNotify](#ab009fe9c6a1f64798c614612e8c3db20) (BMessage *message, uint32 kind=B_CONTROL_INVOKED) — Sends the message to its target, using the notification code specified by kind.
* `bool` [IsTargetLocal](#a17470932a103267815f01d0df9e891e9) () const — Returns whether or not the invoker and its target belong to the same team.
* `BMessage *` [Message](#ab0b73729de282c93b4da51e6b9dbc170) () const — Returns a pointer to the invoker's message object.
* `BMessenger` [Messenger](#aac0992846032f0caaed3d968cd9a1fca) () const — Returns the BMessenger object that the invoker uses to send its messages.
* `virtual status_t` [SetHandlerForReply](#a9983897bef828eea70f574f9571b8e85) (BHandler *handler) — Sets the BHandler object responsible for handling reply messages.
* `virtual status_t` [SetMessage](#a42fae8f984af3765c1a6af404dc36816) (BMessage *message) — Assigns message to the invoker, deleting any previously assigned message.
* `virtual status_t` [SetTarget](#a17e8040bfd829b6b084c2f6234776e11) (BMessenger messenger) — Sets the invoker's target to messenger.
* `virtual status_t` [SetTarget](#ac857ceb882d95a5826447dc12dd06c74) (const BHandler *handler, const BLooper *looper=NULL) — Sets the target to either a local handler or as the preferred handler of a local looper.
* `status_t` [SetTimeout](#ab3c4f55b01f3775832871944b5c943de) (bigtime_t timeout) — Sets the timeout to use when sending the message to the target.
* `BHandler *` [Target](#aba5a469f2e0c94c08553ebe59c238cc8) (BLooper **_looper=NULL) const — Invoke BMessenger::Target() on the internal messenger.
* `bigtime_t` [Timeout](#af2632aee4882b11ed1bc34ce55ef4bbe) () const — Returns the current timeout value.

### Protected Member Functions

* `virtual void` [Draw](#a25d7ee3298d7550a78244ccdf84eed2c) () — Hook method used to draw the menu items.
* `virtual void` [GetContentSize](#a52e1802108ed4e78b61b51f5ac4a241e) (float *_width, float *_height) — Fills out _width and _height with the content rectangle dimensions.
* `BPoint` [ContentLocation](#af3f9cdc6f9be160df96682820c143298) () const — Returns the top-left point of the content rectangle.
* `virtual void` [Draw](#a357779f4b5add35e0e9307b206614d0e) () — Hook method used to draw the menu items.
* `virtual void` [DrawContent](#a2db4048523e94676b1cd6338a2c27ab9) () — Hook method used to draw the menu items contents.
* `virtual void` [GetContentSize](#a8e567edeb0be62c013dec07e2943629d) (float *_width, float *_height) — Fills out _width and _height with the content rectangle dimensions.
* `virtual void` [Highlight](#a56b0f747a556427aa296193fe115a74e) (bool highlight) — Highlights or unhighlights the menu item.
* `virtual status_t` [Invoke](#ae51fbc9628a915b133b5862e436314a4) (BMessage *message=NULL) — Sends a copy of the model message to the target.
* `bool` [IsSelected](#a7f9bb278f056c48b2615b7c87de6a791) () const — Returns whether or not the item is selected.
* `virtual void` [TruncateLabel](#af8af2c4606e2cee362e3238d9220bd2e) (float maxWidth, char *newLabel) — Truncates the label and stashes it into newLabel.
* `void` [BeginInvokeNotify](#ada272cb8671448d7f7efd607791f31a7) (uint32 kind=B_CONTROL_INVOKED) — Implement this method to set up an InvokeNotify() context.
* `void` [EndInvokeNotify](#a2169cfbba1c3da1921baa9a550581b54) () — Implement this method to tear down an InvokeNotify() context.
* `uint32` [InvokeKind](#a6e33e81c7ee307621295e8da6181d3f8) (bool *_notify=NULL) — Returns the kind set by InvokeNotify().

### Archiving

* `virtual status_t` [Archive](#a37151f2e9c361bb173e016bca536dd9e) (BMessage *data, bool deep=true) const — Archives the the BSeparatorItem object into the data message.
* `static BArchivable *` [Instantiate](#ac41289d27cefbc2411d7e13fd5eff673) (BMessage *data) — Creates a new BSeparatorItem object from an data message.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#adbc431076e81504889553ed348c55b94) (BMessage *archive) — Creates a new BMenuItem object from an data message.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BSeparatorItem()`

```cpp
BSeparatorItem::BSeparatorItem()
```

Creates a new [BSeparatorItem](classBSeparatorItem.md) object. 


The creates a new [BSeparatorItem](classBSeparatorItem.md) from [BMenuItem](classBMenuItem.md) with a blank label and `NULL` message, then disables it.



**Since:** BeOS R3

---

### `BSeparatorItem()`

```cpp
BSeparatorItem::BSeparatorItem(BMessage * data)
```

Archive constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The message *data* to construct the separator item from. |





**Since:** BeOS R3

---

### `~BSeparatorItem()`

```cpp
BSeparatorItem::~BSeparatorItem()
```

Destructor, does nothing. 



**Since:** BeOS R3

---

### `Archive()`

```cpp
status_t BSeparatorItem::Archive(BMessage * data, bool deep = true)const
```

Archives the the [BSeparatorItem](classBSeparatorItem.md) object into the *data* message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A pointer to the [BMessage](../application_kit/classBMessage.md) to archive the object into. |
| `deep` | This parameter has no effect for this class. |





**Returns:** A status code, `B_OK` if everything went well or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object was archived successfully. |
| B_NO_MEMORY | Ran out of memory while archiving the object. |





**Since:** BeOS R3


Reimplemented from [BMenuItem](classBMenuItem.md#a0e31758c36db589a4549549ead272f6b).

---

### `Draw()`

```cpp
void BSeparatorItem::Draw()
```

Hook method used to draw the menu items. 


This method is called by automatically by [BMenu::Draw()](classBMenu.md#a239982fa92e2f5a9c2ed0c267b7470b3). You should not need to call this method yourself but you may want to override it in a derived class to do something other than the default.


The default draws a light grey horizontal or vertical line through the middle of the item.



**Since:** BeOS R3


Reimplemented from [BMenuItem](classBMenuItem.md#a357779f4b5add35e0e9307b206614d0e).

---

### `GetContentSize()`

```cpp
void BSeparatorItem::GetContentSize(float * _width, float * _height)
```

Fills out *_width* and *_height* with the content rectangle dimensions. 


You only need to call this method if you're implementing your own [DrawContent()](classBMenuItem.md#a2db4048523e94676b1cd6338a2c27ab9) method to override how the contents of the separator are drawn.


Parameters

| Parameter | Description |
| :--- | :--- |
| `_width` | Filled out with the width of the content rectangle. |
| `_height` | Filled out with the height of the content rectangle. |





**See also:** [ContentLocation()](classBMenuItem.md#af3f9cdc6f9be160df96682820c143298)



**Since:** BeOS R3


Reimplemented from [BMenuItem](classBMenuItem.md#a8e567edeb0be62c013dec07e2943629d).

---

### `Instantiate()`

```cpp
BArchivable * BSeparatorItem::Instantiate(BMessage * data)
```

Creates a new [BSeparatorItem](classBSeparatorItem.md) object from an *data* message. 



**Returns:** A newly created [BSeparatorItem](classBSeparatorItem.md) object or `NULL` if the message doesn't contain an archived [BSeparatorItem](classBSeparatorItem.md).



**Since:** BeOS R3

---

### `SetEnabled()`

```cpp
void BSeparatorItem::SetEnabled(bool enable)
```

Does nothing, this method is defined to override the default [BMenuItem](classBMenuItem.md) behavior. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `enable` | Not used. |





**Since:** BeOS R3


Reimplemented from [BMenuItem](classBMenuItem.md#a1179e9734ed7b84d4f1ba829ed721e22).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBSeparatorItem.html).
