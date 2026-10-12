---
name: BHandler
type: class
kit: application_kit
brief: "Handles messages that are passed on by a BLooper"
source: haiku-book
---

# BHandler Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Handles messages that are passed on by a [BLooper](classBLooper.md). 


The [BHandler](classBHandler.md) class implements two important pieces of functionality. It provides the foundations for **handling messages**, and it serves as a **state machine** that sends out notifications of the state changes.


The most common use of this class is to **handle messages**. Handlers can be tied to loopers, which are the objects that send and receive messages. As soon as a message is received, the looper passes through its list of associated handlers and tries them in a certain order until the message is handled, or the options are exhausted.


You should know that a looper is a subclass of a handler, and as such, loopers can be self-contained and do not need additional handlers. In many cases, this construction will suffice. You will simply subclass the looper, override its [MessageReceived()](classBHandler.md#aeecda5017e0081db617f23bbff71fb53) hook and handle the messages you receive. In some cases, you might opt in for a more ingenious construction. A real-world example is the interface kit. Within that kit, the windows are represented by a [BLooper](classBLooper.md), and all the views and controls in that kit are derived from [BHandler](classBHandler.md). If you put a control in a window, then whenever messages such as clicks are received, the window loops the handlers until there is a handler that is at the screen position the click was in. It is not unlikely that you will some day want to use this functionality of the API.


If your handler is limited to a certain type of messages, you can set a filter that the looper will apply to your message before passing it on to your overridden [MessageReceived()](classBHandler.md#aeecda5017e0081db617f23bbff71fb53) method. The [BMessageFilter](classBMessageFilter.md) class provides the framework for the flexible filtering options, and using [AddFilter()](classBHandler.md#a862bea548363faac6f883b348cbed838) you can apply filters to this handler. Note that a filter object should only be applied to one handler. They cannot be shared.


For more information on the handling chain, have a look at the documentation of the [BLooper](classBLooper.md) class.


Using [BHandler](classBHandler.md) as a **state machine** is a second area of functionality. Since handlers process messages, and perform actions associated with those, they are the center of keeping track on the current state of things within an application. If you want to synchronize these states between different parts of your application, you could perform this manually by sending messages to the interested components, or you can use the more flexible approach with observers.


Observers watch a certain state. A handler can track one or more different states. Each state is represented by a four byte constant - just like the `what` property of a message. Using the [StartWatching()](classBHandler.md#af7d600e33a0586af7444d9abc8500504) methods, you can register observers both within your team, and in other applications. As an argument of that method, you can supply the state you want to watch, or you can register an observer using [StartWatchingAll()](classBHandler.md#a58d7c8d30e47fbb7590f10dea1f21166) to watch all the states the handler tracks. When the handler needs to emit a state change, you can use [SendNotices()](classBHandler.md#a71bf72dc17a64bcd42656722271a9e0c). You can specify the exact state change, and some data that you want to be send to the observers. This data is in the form of the very flexible [BMessage](classBMessage.md), as such you are almost free to pass anything you want.


Whenever [SendNotices()](classBHandler.md#a71bf72dc17a64bcd42656722271a9e0c) is called, all interested observers will receive a message of the *B_OBSERVER_NOTICE_CHANGE* type. Please note that the constant that is associated with the state itself is not transmitted. If you require this information, consider using the message that is passed on to describe the state change.


[BHandler](classBHandler.md) is a part of the chain in the eloquent messaging structure. For a proper understanding of all its facets, have a look at the [messaging overview](app_messaging.md).



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BHandler](#a2142e21fe781b24f914ec2086e5f05b7) (const char *name=NULL) — Construct a new handler with a name.
* `virtual` [~BHandler](#a928254034959d19ef588b7898a6f8194) () — Free the filters of this handler, as well as the list of observers.
* `virtual status_t` [Perform](#a4e6ebc7ebcb72855a1f0fee7bde99766) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).
* [BHandler](#add8fa081a7bb8633581e78777b215d0b) (BMessage *data) — Construct a handler from an archived message.
* `virtual status_t` [Archive](#ac2711ccff5e7f711244c88a5642c83db) (BMessage *data, bool deep=true) const — Archive a handler to a message.
* `virtual void` [MessageReceived](#aeecda5017e0081db617f23bbff71fb53) (BMessage *message) — Handle message that has been received by the associated looper.
* `BLooper *` [Looper](#ac8e949959b12e602e3b0c4f023c60e6c) () const — Return a pointer to the looper that this handler is associated with.
* `void` [SetName](#abf861126df4b6e71b9261a99da4ad0eb) (const char *name) — Set or change the name of this handler.
* `const char *` [Name](#a40b246ac272e09b2f641d1290be21200) () const — Return the name of this handler.
* `virtual void` [SetNextHandler](#a02f78779c8141987d6030e73c22e734a) (BHandler *handler) — Set the next handler in the chain that the message is passed on to if this handler cannot process it.
* `BHandler *` [NextHandler](#a92855d8f88f6072e7225bde292feaa38) () const — Return the next hander in the chain to which the message is passed on.
* `virtual void` [AddFilter](#a862bea548363faac6f883b348cbed838) (BMessageFilter *filter) — Add filter as a prerequisite to this handler.
* `virtual bool` [RemoveFilter](#a2b608135b27f283802648e7c6f8cdc83) (BMessageFilter *filter) — Remove filter from the filter list.
* `virtual void` [SetFilterList](#a503344dc801858e1f5f419be3919e9cf) (BList *filters) — Set the internal list of filters to filters.
* `BList *` [FilterList](#a909662a049856f6863a934cf18161554) () — Return a pointer to the list of filters.
* `bool` [LockLooper](#a9d64bf66b4914918e24390d117e83477) () — Lock the looper associated with this handler.
* `status_t` [LockLooperWithTimeout](#afa0099ff6defcb6d64e3ee1c2fb47afe) (bigtime_t timeout) — Lock the looper associated with this handler, with a time out value.
* `void` [UnlockLooper](#ab131af7eb7aa2b9eea3a11ac1bfd4c03) () — Unlock the looper.
* `virtual BHandler *` [ResolveSpecifier](#a76439ffaf84e65232698d2a4a3317d22) (BMessage *message, int32 index, BMessage *specifier, int32 what, const char *property) — Determine the proper handler for a scripting message.
* `virtual status_t` [GetSupportedSuites](#acf34435dada239f411e8e034e0ea36b5) (BMessage *data) — Reports the suites of messages and specifiers that derived classes understand.
* `status_t` [StartWatching](#af7d600e33a0586af7444d9abc8500504) (BMessenger target, uint32 what) — Subscribe this handler to watch a specific state change of a target.
* `status_t` [StartWatchingAll](#a58d7c8d30e47fbb7590f10dea1f21166) (BMessenger target) — Subscribe this handler to watch a target for all events.
* `status_t` [StopWatching](#a9d1f0d55b3dc7337058aba769b4e4f93) (BMessenger target, uint32 what) — Unsubscribe this handler from watching a specific state.
* `status_t` [StopWatchingAll](#a199c167e0dcee95aa65d09435804b3d9) (BMessenger target) — Unsubscribe this handler from watching all states.
* `status_t` [StartWatching](#a20713ff6ee9df49a014f391374eaf689) (BHandler *observer, uint32 what) — Subscribe an observer for a specific state change of this handler.
* `status_t` [StartWatchingAll](#a31927c51d89e0e3b3bf609a786ee6c3b) (BHandler *observer) — Subscribe an observer for a all state changes.
* `status_t` [StopWatching](#ad3544be491270f856a0af8d36ce02d78) (BHandler *observer, uint32 what) — Unsubscribe an observer from watching a specific state.
* `status_t` [StopWatchingAll](#a8b9a424ce63f5932666094b6eadf10cf) (BHandler *observer) — Unsubscribe an observer from watching all states.
* `virtual void` [SendNotices](#a71bf72dc17a64bcd42656722271a9e0c) (uint32 what, const BMessage *notice=NULL) — Emit a state change to the observers.
* `bool` [IsWatched](#a581b84f0f067afa88768ce6a0c07f59f) () const — Check if there are any observers watching this handler.
* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).

### Static Public Member Functions

* `static BArchivable *` [Instantiate](#a0c23aeb48d578525f81ba6d47f968528) (BMessage *data) — Static method to instantiate a handler from an archived message.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BHandler()`

```cpp
BHandler::BHandler(const char * name = NULL)
```

Construct a new handler with a *name*. 


The newly constructed handler is not associated with a looper until you explicitly request this to happen. To associate this handler with a looper, use [BLooper::AddHandler()](classBLooper.md#a484be74814014e3c48c1a16f44e34074).



**Since:** BeOS R3

---

### `~BHandler()`

```cpp
BHandler::~BHandler()
```

Free the filters of this handler, as well as the list of observers. 


This method does not remove the handler from the looper to which this handler is associated. You should do this yourself, using [BLooper::RemoveHandler()](classBLooper.md#a5af57140bf018388a2e64343f46ac330).



> [!WARNING]
> This constructor does no type check whatsoever. Since you can pass any [BMessage](classBMessage.md), you should - if you are not sure about the exact type - use the [Instantiate()](classBHandler.md#a0c23aeb48d578525f81ba6d47f968528) method, which does check the type.



**Since:** BeOS R3

---

### `BHandler()`

```cpp
BHandler::BHandler(BMessage * data)
```

Construct a handler from an archived message. 


This *data* has to be created using the [BHandler::Archive()](classBHandler.md#ac2711ccff5e7f711244c88a5642c83db) method. Note that only the name is stored. The filters, the associated looper and the observers are not stored, and should be manually added when you are using this object.



**Since:** BeOS R3

---

### `AddFilter()`

```cpp
void BHandler::AddFilter(BMessageFilter * filter)
```

Add *filter* as a prerequisite to this handler. 


If the handler is associated with a looper, this looper needs to be locked in order for this operation to succeed.


Note that the filter is not copied, rather a pointer to the *filter* is stored. As such, you need to make sure that the *filter* object exists as long as it is added to this handler.



**See also:** [RemoveFilter()](classBHandler.md#a2b608135b27f283802648e7c6f8cdc83)



**Since:** BeOS R3

---

### `Archive()`

```cpp
status_t BHandler::Archive(BMessage * data, bool deep = true)const
```

Archive a handler to a message. 


Currently, only the name is archived. The filters, the associated looper and the observers are not stored.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The message to archive the object in. |
| `deep` | This parameter is ignored, as [BHandler](classBHandler.md) does not have children. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Archiving succeeded. |
| B_BAD_VALUE | The *data* parameter is not a valid message. |





**See also:** [BHandler::Instantiate(BMessage* data)](classBHandler.md#a0c23aeb48d578525f81ba6d47f968528)



**Since:** BeOS R3


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44).


Reimplemented in [BBox](../interface_kit/classBBox.md#abd1a762e132a6196076617cee1eb81ac), [BMenu](../interface_kit/classBMenu.md#a71bed24f541bdfb690863118ce3f716b), [BMenuBar](../interface_kit/classBMenuBar.md#af4ae9bcc3c1cbe560e745c9868fb9c5f), [BMenuField](../interface_kit/classBMenuField.md#ada677e4339d5a5eca5c945c4165b6a3e), [BOutlineListView](../interface_kit/classBOutlineListView.md#af590f60f193f47989f63c34dda0e6916), [BPictureButton](../interface_kit/classBPictureButton.md#ab476f82e9d75a3b4a9b54ca35d1ad036), [BPopUpMenu](../interface_kit/classBPopUpMenu.md#af81e6dc2ddcc3063eb33a1a5cf3b9088), [BScrollBar](../interface_kit/classBScrollBar.md#a2d8cea93fe440bbed02685c135b0f802), [BScrollView](../interface_kit/classBScrollView.md#a7858c5f97152c910831db817b80f5f95), [BShelf](../interface_kit/classBShelf.md#a098c2a557715a3a4fa91a66125653f0e), [BStatusBar](../interface_kit/classBStatusBar.md#a05e0e95a3cee49d1fa7f1a48e26ae20b), [BStringView](../interface_kit/classBStringView.md#adbafb44b6614c69a645d3e2de818c5f5), [BTextControl](../interface_kit/classBTextControl.md#af68449ec551e8a089a441fd270954b99), [BTextView](../interface_kit/classBTextView.md#a0f3fb624378a2d13617773713efedd98), [BView](../interface_kit/classBView.md#ab6de1b48cbc3ef15a0d02113036f002d), [BWindow](../interface_kit/classBWindow.md#a69163d40d8f1eda77c9134ad4ab745a2), [BApplication](classBApplication.md#aa36536582835264341376064cbc96a27), [BLooper](classBLooper.md#a791ef8664f674b6683d551762888f1c2), [BDirectWindow](../game_kit/classBDirectWindow.md#a39e69ba4bba5221b3099cf34129862c8), [BAlert](../interface_kit/classBAlert.md#aba312ca5f7e668bf4d96efc7f41625a3), [BButton](../interface_kit/classBButton.md#adce5e4839a58c3bb85965398a490d720), [BChannelControl](../interface_kit/classBChannelControl.md#aa71189c8b008cb3329c17b58f786617e), [BCheckBox](../interface_kit/classBCheckBox.md#a75511a8252ef3ffa1177f57af97b67ca), [BColorControl](../interface_kit/classBColorControl.md#a6437907efd1d39a492db1f55b5f4dc36), [BControl](../interface_kit/classBControl.md#a2581a447a34eef102c62d0e998155290), [BDragger](../interface_kit/classBDragger.md#aece5cd86ccd46a23f1188697f4bffa55), [BListView](../interface_kit/classBListView.md#a89277e72296cc9ec516777e000f100e3), [BRadioButton](../interface_kit/classBRadioButton.md#aeed1a7a2142b1ac7b1499234f884caae), [BChannelSlider](../interface_kit/classBChannelSlider.md#ac216b412d86275115516b886c4f9b578), [BSeparatorView](../interface_kit/classBSeparatorView.md#a41d7d43196ee70cc26986f95b5c3e262), [BSplitView](classBSplitView.md#a2c4ab843dd62815ebeb7201e21d3199b), and [BTabView](../interface_kit/classBTabView.md#a3354f9343238295b7ed0a24339106cd5).

---

### `FilterList()`

```cpp
BList * BHandler::FilterList()
```

Return a pointer to the list of filters. 



**Returns:** A pointer to the list of filters. Do not manipulate the list of filters directly, but use the methods provided by this class, in order to maintain internal consistency.



**See also:** [AddFilter()](classBHandler.md#a862bea548363faac6f883b348cbed838)



**Since:** BeOS R3

---

### `GetSupportedSuites()`

```cpp
status_t BHandler::GetSupportedSuites(BMessage * data)
```

Reports the suites of messages and specifiers that derived classes understand. 



**Since:** BeOS R3


Reimplemented in [BApplication](classBApplication.md#a0fb9cc161a785cad42925075a087fc16), [BLooper](classBLooper.md#a915a50de7d5b6263f0fd1a349a9a6d92), [BDirectWindow](../game_kit/classBDirectWindow.md#a55e920fcba8972f5173bd3714f416c13), [BAlert](../interface_kit/classBAlert.md#a9e658b2f7dc50b2c5da3191d77a22594), [BChannelControl](../interface_kit/classBChannelControl.md#abfb5744f9faf08ed02d22a33ae9e9ab8), [BChannelSlider](../interface_kit/classBChannelSlider.md#affd29de4f880e122c72d4d3b25b7ed9d), [BColorControl](../interface_kit/classBColorControl.md#a5f10efed53781673b0f5a3f40b7d527d), [BDragger](../interface_kit/classBDragger.md#a9d014b5632dfd7c4dbb43f45ea2175ef), [BListView](../interface_kit/classBListView.md#acc1fa37e73b342b27d16e13aa3d3024a), [BMenu](../interface_kit/classBMenu.md#a2aa0277374bacf3b7644f738bc064637), [BMenuBar](../interface_kit/classBMenuBar.md#ad635f7e68997f901cbd4b15491b5f2a3), [BMenuField](../interface_kit/classBMenuField.md#ad765cb012c296a6f676e070c80c929e3), [BOutlineListView](../interface_kit/classBOutlineListView.md#a293dd0ed9a59c56ddd2738981c6c48b6), [BPictureButton](../interface_kit/classBPictureButton.md#a08e86268e927d332501bee63892fb2bd), [BPopUpMenu](../interface_kit/classBPopUpMenu.md#aab6d894d982b8841569be6d5766b88e2), [BShelf](../interface_kit/classBShelf.md#a5b14d8c9f67cdec075beab9bfefa281d), [BStatusBar](../interface_kit/classBStatusBar.md#afd6b9bb4d38d8c418d3f0aa65a84aea3), [BStringView](../interface_kit/classBStringView.md#ab294fcbe6b75394cb2cd4d6db1a908c4), [BTextControl](../interface_kit/classBTextControl.md#a9281b5fa852c3fe841bc7f102a96078a), [BTextView](../interface_kit/classBTextView.md#a9cb6a32b918a5c90489b6fb7e27fcb6a), [BView](../interface_kit/classBView.md#a772462d751d457f63ee0fc56d8ba02d1), [BWindow](../interface_kit/classBWindow.md#a8c2f3013601609b54778af99fa6a25ca), [BBox](../interface_kit/classBBox.md#ab1ff66b8efec609137264522016f09c6), [BButton](../interface_kit/classBButton.md#af912fac07ee02f90a12a4011e5a493cb), [BCheckBox](../interface_kit/classBCheckBox.md#a6075229f070c3723a0fc102e7984e8f2), [BControl](../interface_kit/classBControl.md#a3b545ffe2ee04f62eaa567582225adba), [BRadioButton](../interface_kit/classBRadioButton.md#a513f368c4eb7c7d1aa81da79bee492ea), [BScrollBar](../interface_kit/classBScrollBar.md#a543695199844d6b485ab0cb43c65a950), [BScrollView](../interface_kit/classBScrollView.md#ae23327464d7c7db975defe845c4cfdf9), and [BTabView](../interface_kit/classBTabView.md#aed45f36a1cdcc1bb23fc964714cbe20d).

---

### `Instantiate()`

```cpp
BArchivable * BHandler::Instantiate(BMessage * data)
```

Static method to instantiate a handler from an archived message. 



**Returns:** A pointer to the instantiated handler, or `NULL` if the *data* is not a valid archived [BHandler](classBHandler.md) object.



**See also:** [BHandler(BMessage* data)](classBHandler.md#add8fa081a7bb8633581e78777b215d0b)



**Since:** BeOS R3

---

### `IsWatched()`

```cpp
bool BHandler::IsWatched()const
```

Check if there are any observers watching this handler. 



**Since:** BeOS R5

---

### `LockLooper()`

```cpp
bool BHandler::LockLooper()
```

Lock the looper associated with this handler. 



**Returns:** `true` if the looper is locked, `false` if there was an error acquiring the lock.



**See also:** [LockLooperWithTimeout()](classBHandler.md#afa0099ff6defcb6d64e3ee1c2fb47afe)



**Since:** BeOS R4

---

### `LockLooperWithTimeout()`

```cpp
status_t BHandler::LockLooperWithTimeout(bigtime_t timeout)
```

Lock the looper associated with this handler, with a time out value. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `timeout` | The time to wait for acquiring the lock in microseconds. You may also use `B_INFINITE_TIMEOUT`, in which this method will wait as long as it takes to acquire the lock. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Locking succeeded. |
| B_BAD_VALUE | This handler is not associated with a looper (anymore). |
| B_TIMED_OUT | The time specified in *timeout* has passed without locking the looper. |





**See also:** [LockLooper()](classBHandler.md#a9d64bf66b4914918e24390d117e83477)



**Since:** BeOS R4

---

### `Looper()`

```cpp
BLooper * BHandler::Looper()const
```

Return a pointer to the looper that this handler is associated with. 



**Returns:** If the handler is not yet associated with a looper, it will return `NULL`.



**See also:** [BLooper::AddHandler()](classBLooper.md#a484be74814014e3c48c1a16f44e34074)



**Since:** BeOS R3

---

### `MessageReceived()`

```cpp
void BHandler::MessageReceived(BMessage * message)
```

Handle *message* that has been received by the associated looper. 


This method is reimplemented by subclasses. If the messages that have been received by a looper pass through the filters, then they end up in the [MessageReceived()](classBHandler.md#aeecda5017e0081db617f23bbff71fb53) methods.


The example below shows a very common way to handle *message*. Usually, this involves parsing the [BMessage::what](classBMessage.md#ad074faab0857f51fba778f0d8558df1e) constant and then perform an action based on that.



```cpp
void
ShowImageApp::MessageReceived(BMessage *message)
{
 switch (message->what) {
 case MSG_FILE_OPEN:
            fOpenPanel->Show();
 break;
 
 case B_CANCEL:
 // File open panel was closed,
 // start checking count of open windows.
            StartPulse();
 break;
 
 default:
 // We do not handle this message, pass it on to the base class.
 BApplication::MessageReceived(message); 
 break;
    }
}
```

If your handler cannot process this *message*, you should pass it on to the base class. Eventually, it will reach the base implementation, which will reply with `B_MESSAGE_NOT_UNDERSTOOD`.



> [!IMPORTANT]
> If you want to keep or manipulate the *message*, have a look at [BLooper::DetachCurrentMessage()](classBLooper.md#a7c8f05bcc354bc1d53026417417120e3) to receive ownership of the *message*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The message that needs to be handled. |





**Since:** BeOS R3


Reimplemented in [BApplication](classBApplication.md#aa010d676b8d372d522b7da39ddfb3b03), [BLooper](classBLooper.md#a89303d11c987dae76cdfc38ad5d3c4c2), [BDirectWindow](../game_kit/classBDirectWindow.md#a1eb5e6dfeee341e9baf3d688ff66194a), [BAlert](../interface_kit/classBAlert.md#a1300fdf51e73dd4f8a24b908d6fc2e1e), [BBox](../interface_kit/classBBox.md#a30d9348112e19b908181b037edc291de), [BButton](../interface_kit/classBButton.md#a9954aa8549ffb7cddd1a401997fd07a7), [BChannelControl](../interface_kit/classBChannelControl.md#a7c3c5174a2f31f0a24c3fe4258d372da), [BChannelSlider](../interface_kit/classBChannelSlider.md#aa60391cfc92b6c1a59ae7e92aa1f5bae), [BCheckBox](../interface_kit/classBCheckBox.md#a668832dfbcab06cad06d0fb7d9a6244a), [BColorControl](../interface_kit/classBColorControl.md#a9cf939fb5e7ef82a70e0792ccc0cfc1f), [BControl](../interface_kit/classBControl.md#a19960b4d0a96144f73065a6ea1f2f8e2), [BDragger](../interface_kit/classBDragger.md#acdf8b8402a8e253ca24ab01ba63b914c), [BListView](../interface_kit/classBListView.md#ac00efce3ca37ce6e89c3f3fb5717311c), [BMenu](../interface_kit/classBMenu.md#aca12e6b863279cc62772ac13ef286d31), [BMenuBar](../interface_kit/classBMenuBar.md#a7d7c1d1674e059b56c82c81e381d4455), [BMenuField](../interface_kit/classBMenuField.md#ab73739dc3316044b9269718bd0852d39), [BOptionControl](../interface_kit/classBOptionControl.md#a6bff9c89ab78d899edfb88d3f9e2300c), [BOptionPopUp](../interface_kit/classBOptionPopUp.md#a05b397e2521fe0b10ae3a2b05e78acae), [BOutlineListView](../interface_kit/classBOutlineListView.md#aad47f3bf68a98024413aa06a45b0bdad), [BPictureButton](../interface_kit/classBPictureButton.md#a7b6a5dc266664f155b6191d101ce48cd), [BPopUpMenu](../interface_kit/classBPopUpMenu.md#a4b5937dbd7baa9d98b5368d6de9ca23c), [BRadioButton](../interface_kit/classBRadioButton.md#a2f07af2fe9eedce7ffecd2b29a4b5d6a), [BScrollBar](../interface_kit/classBScrollBar.md#a8d578e9e134aeaafdc6dc542e2d214f7), [BScrollView](../interface_kit/classBScrollView.md#ad06771333c1897571f984ca9e533b69d), [BShelf](../interface_kit/classBShelf.md#a6355e985c4a15187a523035c983f3063), [BSplitView](classBSplitView.md#ad4737f5224faa2d34c84299750ab92ec), [BStatusBar](../interface_kit/classBStatusBar.md#aee4044255aaae32db5a0d8bc2046840d), [BStringView](../interface_kit/classBStringView.md#a03521ef18f82081e3a54f404217c2c6c), [BTabView](../interface_kit/classBTabView.md#a5827436caab3b27791f2280d2d151624), [BTextControl](../interface_kit/classBTextControl.md#afad72eca02699a6577c4bc0949e1c9ae), [BTextView](../interface_kit/classBTextView.md#a4d7d7990e57ce7286f78698f27c89e60), [BView](../interface_kit/classBView.md#aca0a16b0e04288e1fdc0b63690ea7a6d), and [BWindow](../interface_kit/classBWindow.md#a1ce544ea7d9adcc6941759817a42affe).

---

### `Name()`

```cpp
const char * BHandler::Name()const
```

Return the name of this handler. 



**See also:** [SetName()](classBHandler.md#abf861126df4b6e71b9261a99da4ad0eb)



**Since:** BeOS R3

---

### `NextHandler()`

```cpp
BHandler * BHandler::NextHandler()const
```

Return the next hander in the chain to which the message is passed on. 



**See also:** [SetNextHandler()](classBHandler.md#a02f78779c8141987d6030e73c22e734a)



**Since:** BeOS R3

---

### `Perform()`

```cpp
virtual status_t BHandler::Perform(perform_code d, void * arg)
```

Perform some action (Internal method defined for binary compatibility purposes). 


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a827fa92febcf925f07545aa9777df9de).


Reimplemented in [BPopUpMenu](../interface_kit/classBPopUpMenu.md#a8f92a8866c4ffd63cdfcf07957f5ba22), [BDirectWindow](../game_kit/classBDirectWindow.md#a113afd3534fca8b81bcc86f8e55738be), [BListView](../interface_kit/classBListView.md#aa0afeb194104738a01c7e60195fe50d0), [BCheckBox](../interface_kit/classBCheckBox.md#abcac265789890adbf485f42d34d8c8e3), [BDragger](../interface_kit/classBDragger.md#ad47a007f4126b9847a315263aa64ad93), [BMenuBar](../interface_kit/classBMenuBar.md#a4b8a4e16ace175bc3bad9d6ef6b42daf), [BOutlineListView](../interface_kit/classBOutlineListView.md#acb2775731d5da2cf52995e4d0b75c1d6), [BPictureButton](../interface_kit/classBPictureButton.md#a57e7eef2e379994c13b8c93eeb5cf3c5), [BSeparatorView](../interface_kit/classBSeparatorView.md#af56310d344ae63781e6b299d56c34e99), [BShelf](../interface_kit/classBShelf.md#afbf73f485603cf3a50ff1bd4c99d9a6a), [BTextView](../interface_kit/classBTextView.md#a6519856e1dbf6e021911529b8a0a15c6), [BView](../interface_kit/classBView.md#a512a6c8dca1a62b14cdcb1c22070129b), [BWindow](../interface_kit/classBWindow.md#afde7d74e5526f740dedb82a1d10faa7a), [BApplication](classBApplication.md#ab8fea9f4a96bdee62ce77a089d472973), [BLooper](classBLooper.md#adfc642544ce22888d412e6a4be25fa72), [BAlert](../interface_kit/classBAlert.md#a3d2769c5bf9b9822f21770e38e561fd6), [BBox](../interface_kit/classBBox.md#adcd9b77028e7c820ce29a8a9db950adb), [BButton](../interface_kit/classBButton.md#aee74330d076b7b8487fe21443118b03d), [BCardView](classBCardView.md#aa784b33c5b2c62791cf86fa38d1704ba), [BControl](../interface_kit/classBControl.md#a0b32524cd2abfb7ea37b9988b180c733), [BGridView](classBGridView.md#a1409f66c0dfe65882e3bfa3b0fe000dc), [BGroupView](../interface_kit/classBGroupView.md#ad8e96a8f8d76e75b5bb6815866529112), [BMenu](../interface_kit/classBMenu.md#a6dedb98c6ba5ffbc44893ff43785c93c), [BMenuField](../interface_kit/classBMenuField.md#a78923e5f07ff7c288980a72f6a953001), [BScrollBar](../interface_kit/classBScrollBar.md#adfb4e4e74d00970fd154c652e467b66e), [BScrollView](../interface_kit/classBScrollView.md#a1bd8a27f2883ca0e6b5b9dde0e9e638a), [BSplitView](classBSplitView.md#a9aaf09f717a61303d5aca6e92d96b103), [BStatusBar](../interface_kit/classBStatusBar.md#a4b9eb3ec267be64d9293af3b920c48de), [BTabView](../interface_kit/classBTabView.md#a708fd8766fddb7b0cd72566c57c2977a), and [BRadioButton](../interface_kit/classBRadioButton.md#a44c726ed88d3a132e9d3055ebf98f3e6).

---

### `RemoveFilter()`

```cpp
bool BHandler::RemoveFilter(BMessageFilter * filter)
```

Remove *filter* from the filter list. 


If the handler is associated with a looper, this looper needs to be locked in order for this operation to succeed.


Note that the *filter* is not deleted, merely removed from the list. You need to take care of the memory yourself.



**Returns:** `true` if the *filter* was in the filter list and is removed, `false` if the *filter* was not found in the filter list.



**See also:** [AddFilter()](classBHandler.md#a862bea548363faac6f883b348cbed838)



**Since:** BeOS R3

---

### `ResolveSpecifier()`

```cpp
BHandler * BHandler::ResolveSpecifier(BMessage * message, int32 index, BMessage * specifier, int32 what, const char * property)
```

Determine the proper handler for a scripting message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The scripting message to determine the handler. |
| `index` | The index of the specifier. |
| `specifier` | The message which contains the specifier. |
| `what` | The 'what' field of the specifier message. |
| `property` | The name of the target property. |





**Returns:** A pointer to the proper [BHandler](classBHandler.md) for the given scripting message.



**Since:** BeOS R3


Reimplemented in [BApplication](classBApplication.md#a044d40580b05617288c91748cbd30513), [BAlert](../interface_kit/classBAlert.md#a22285daeb96ea0936faab97b077115e6), [BChannelSlider](../interface_kit/classBChannelSlider.md#ab95b5eebb6adcc7502c856789f08b6d2), [BDragger](../interface_kit/classBDragger.md#ad21b28192fb7b7005129b5f517209e99), [BMenu](../interface_kit/classBMenu.md#adfd2e1d211f34a8ac748abb989adac48), [BMenuBar](../interface_kit/classBMenuBar.md#ab8e2eb06afc52455be926b3cde21f935), [BMenuField](../interface_kit/classBMenuField.md#a8af84b2aecbc3e6b3041e3ef70b36cfd), [BPopUpMenu](../interface_kit/classBPopUpMenu.md#acefc54d0514f6efbe059d9a36b837fe1), [BShelf](../interface_kit/classBShelf.md#af4294354dfabd65838909b174990db8c), [BStringView](../interface_kit/classBStringView.md#af7522569583e8aea625adea9fc2471fc), [BTextView](../interface_kit/classBTextView.md#a3e0e67bcd942c0b738043235e56fdf29), [BView](../interface_kit/classBView.md#a4c0c6d3b21ae92056e5e40fe4d3ec175), [BLooper](classBLooper.md#a16b494160d9b37d4dbbc0d426a22c946), [BDirectWindow](../game_kit/classBDirectWindow.md#aee5db7142cabc984cb16e61eaa7baa36), [BBox](../interface_kit/classBBox.md#aa171ac58aa5857a404f9431e63ad6792), [BButton](../interface_kit/classBButton.md#a16b56f270bcba826cd8a1eb043adb474), [BChannelControl](../interface_kit/classBChannelControl.md#af12f883b6e60f2ea071bb18724593350), [BCheckBox](../interface_kit/classBCheckBox.md#ae860f1cfc296c79754697d95fc289a9e), [BColorControl](../interface_kit/classBColorControl.md#a2bc94c2bffc9dec2b1a844c21833cb93), [BControl](../interface_kit/classBControl.md#a084be37bbc0c49627c42a078c4b4dac8), [BListView](../interface_kit/classBListView.md#a2c6144558d144fd5b134021de4c01183), [BOutlineListView](../interface_kit/classBOutlineListView.md#a835a18d28691bdc9daad7cf0598e8a5f), [BPictureButton](../interface_kit/classBPictureButton.md#a8553ac7d4f76b03d53dce14073cb50de), [BRadioButton](../interface_kit/classBRadioButton.md#a767171da7c902ec3e06d19951f8b1404), [BScrollBar](../interface_kit/classBScrollBar.md#abcf203657944c36c94a4a55e59338c8a), [BScrollView](../interface_kit/classBScrollView.md#a6565e85e02890afd9e37f22935bf01b1), [BStatusBar](../interface_kit/classBStatusBar.md#a930eda32bb19c6fb583a95947bc4eec9), [BTabView](../interface_kit/classBTabView.md#a2d18bd3eeb63be72e3954b6d58cf3809), [BTextControl](../interface_kit/classBTextControl.md#a666a6fd256b57c98f9e75b3c19a03a89), and [BWindow](../interface_kit/classBWindow.md#aaf328e28799cf868ec31df2847a4ed37).

---

### `SendNotices()`

```cpp
void BHandler::SendNotices(uint32 what, const BMessage * notice = NULL)
```

Emit a state change to the observers. 


The actual state (specified by *what*) will not be transmitted. This is merely for internal bookkeeping. It is not entirely unimaginable that you still want to inform the observers of what actually took place. You can use the *msg* to transmit this, and any other data you want. Note that the message will be copied and slightly altered: the `what` member of the message will be `B_OBSERVER_NOTICE_CHANGE`, and the `what` constant you specified will be stored in the [B_OBSERVE_ORIGINAL_WHAT](Handler_8h.md#a9a087275b074ec202d3fc0352862956a) label.


Parameters

| Parameter | Description |
| :--- | :--- |
| `what` | The identifier of the state. |
| `notice` | Any data associated with the state change. You retain ownership of this data, so make sure you dispose it when you are done. |





**Since:** BeOS R5

---

### `SetFilterList()`

```cpp
void BHandler::SetFilterList(BList * filters)
```

Set the internal list of filters to *filters*. 


If the handler is associated with a looper, this looper needs to be locked in order for this operation to succeed.


The internal list will be replaced with the new list of *filters*. All the existing filters will be **deleted**.



**See also:** [AddFilter()](classBHandler.md#a862bea548363faac6f883b348cbed838), [FilterList()](classBHandler.md#a909662a049856f6863a934cf18161554)



**Since:** BeOS R3

---

### `SetName()`

```cpp
void BHandler::SetName(const char * name)
```

Set or change the name of this handler. 



**See also:** [Name()](classBHandler.md#a40b246ac272e09b2f641d1290be21200)



**Since:** BeOS R3

---

### `SetNextHandler()`

```cpp
void BHandler::SetNextHandler(BHandler * handler)
```

Set the next handler in the chain that the message is passed on to if this *handler* cannot process it. 


This method has three requirements:


1. This *handler* should belong to a looper.

2. The looper needs to be locked. See [LockLooper()](classBHandler.md#a9d64bf66b4914918e24390d117e83477).

3. The *handler* that you pass must be associated with the same looper.



Failure to meet any of these requirements will result in your application crashing.


By default, the handlers are chained in order that they were associated to a looper with BLooper::AddHander().



**See also:** [NextHandler()](classBHandler.md#a92855d8f88f6072e7225bde292feaa38)



**Since:** BeOS R3

---

### `StartWatching()`

```cpp
status_t BHandler::StartWatching(BHandler * observer, uint32 what)
```

Subscribe an *observer* for a specific state change of this handler. 


Use this method to subscribe observers to watch this handler. State changes of this handler that match the *what* argument, will be sent.



```cpp
// Handler B wants to observe Handler A
BHandler A, B;
 
A.StartWatching(&B, kNetworkConnection);
```

Since pointers to handlers can only exist in the local namespace, have a look at [StartWatching(BMessenger, uint32)](classBHandler.md#af7d600e33a0586af7444d9abc8500504) for inter-team watching.


Parameters

| Parameter | Description |
| :--- | :--- |
| `observer` | The observer for this handler. |
| `what` | The state that needs to be watched. |





**Returns:** During the call of this method, a notification will be transmitted using the *observer*. If this works, then this method will return `B_OK`.



**See also:** [StartWatchingAll(BHandler*)](classBHandler.md#a31927c51d89e0e3b3bf609a786ee6c3b), [StopWatching(BHandler*, uint32)](classBHandler.md#ad3544be491270f856a0af8d36ce02d78)



**Since:** BeOS R5

---

### `StartWatching()`

```cpp
status_t BHandler::StartWatching(BMessenger target, uint32 what)
```

Subscribe this handler to watch a specific state change of a *target*. 


Use this method to subscribe messengers to watch state changes in this handler, this also means that observers from other teams can be subscribed.



```cpp
// Handler B watches Handler A
BHandler A, B;
BMessenger messengerA(&A)
 
B.StartWatching(messengerA, kNetworkConnection);
```

Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | The messenger from which the notifications would be received. |
| `what` | The state that needs to be watched. |





**Returns:** During the call of this method, a notification will be transmitted using the *target*. If this works, then this method will return `B_OK`.



**See also:** [StartWatchingAll(BMessenger)](classBHandler.md#a58d7c8d30e47fbb7590f10dea1f21166), [StopWatching(BMessenger, uint32)](classBHandler.md#a9d1f0d55b3dc7337058aba769b4e4f93)



**Since:** BeOS R5

---

### `StartWatchingAll()`

```cpp
status_t BHandler::StartWatchingAll(BHandler * observer)
```

Subscribe an *observer* for a all state changes. 


This method performs the same task as StartWatching(BHandler, uint32), but it will subscribe the *observer* to all the state changes this handler tracks.



**See also:** [StartWatching(BHandler*, uint32)](classBHandler.md#a20713ff6ee9df49a014f391374eaf689), [StopWatchingAll(BHandler*)](classBHandler.md#a8b9a424ce63f5932666094b6eadf10cf)



**Since:** BeOS R5

---

### `StartWatchingAll()`

```cpp
status_t BHandler::StartWatchingAll(BMessenger target)
```

Subscribe this handler to watch a *target* for all events. 


This method performs the same task as [StartWatching(BMessenger, uint32)](classBHandler.md#af7d600e33a0586af7444d9abc8500504), but it will subscribe to all the state changes the *target* knows.



**See also:** [StartWatching(BMessenger, uint32)](classBHandler.md#af7d600e33a0586af7444d9abc8500504), [StopWatchingAll(BMessenger)](classBHandler.md#a199c167e0dcee95aa65d09435804b3d9)



**Since:** BeOS R5

---

### `StopWatching()`

```cpp
status_t BHandler::StopWatching(BHandler * handler, uint32 what)
```

Unsubscribe an observer from watching a specific state. 


This method will unsubscribe the *handler* from watching a specific event.



**See also:** [StartWatching(BHandler*, uint32)](classBHandler.md#a20713ff6ee9df49a014f391374eaf689)



**Since:** BeOS R5

---

### `StopWatching()`

```cpp
status_t BHandler::StopWatching(BMessenger target, uint32 what)
```

Unsubscribe this handler from watching a specific state. 


This method will unsubscribe this handler from watching a specific event in a *target*.



**See also:** [StartWatching(BMessenger, uint32)](classBHandler.md#af7d600e33a0586af7444d9abc8500504)



**Since:** BeOS R5

---

### `StopWatchingAll()`

```cpp
status_t BHandler::StopWatchingAll(BHandler * handler)
```

Unsubscribe an observer from watching all states. 


This method will unsubscribe the *handler* from watching all state changes.



**See also:** [StartWatchingAll(BHandler*)](classBHandler.md#a31927c51d89e0e3b3bf609a786ee6c3b)



**Since:** BeOS R5

---

### `StopWatchingAll()`

```cpp
status_t BHandler::StopWatchingAll(BMessenger target)
```

Unsubscribe this handler from watching all states. 


This method will unsubscribe the *target* from watching all state changes.



**See also:** [StartWatchingAll(BMessenger)](classBHandler.md#a58d7c8d30e47fbb7590f10dea1f21166)



**Since:** BeOS R5

---

### `UnlockLooper()`

```cpp
void BHandler::UnlockLooper()
```

Unlock the looper. 



**Since:** BeOS R4

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBHandler.html).
