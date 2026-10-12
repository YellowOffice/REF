---
name: BLooper
type: class
kit: application_kit
brief: "Receive and process messages in a separate thread"
source: haiku-book
---

# BLooper Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Receive and process messages in a separate thread. 


When an object of this class is created, the message loop can be started with [Run()](classBLooper.md#a88bb85410e0c4124bdc6f16168df4811). This spawns the thread that receives messages and processes messages. Messages are actually passed on to [handlers](classBHandler.md) that are associated with this looper. By default there is always one handler available: the looper itself. To 'quit' a looper, you should pass a `B_QUIT_REQUESTED` message using one of the message post functions. When a looper receives such a request, it will **delete** itself. As such, looper should *always be created on the heap* (with `new`), and never on the stack.


Posting messages can be done using the various [PostMessage()](classBLooper.md#a0de6737bfbf8a8b4913adc8c74bb544e) methods. Whenever a message is posted, it will be added through to the message queue. It is possible to apply filters (see [AddCommonFilter()](classBLooper.md#a25adc41bdfd741e9c82d2b469a5086b0)) to filter out any messages that correspond with certain criteria. The method will copy the contents of the message and this copy is processed, so make sure you delete the original messages in case you create them on the heap. The handler for the message is chosen using the following criteria:



1. If [PostMessage()](classBLooper.md#a0de6737bfbf8a8b4913adc8c74bb544e) or the [BMessenger](classBMessenger.md) is set to a specific handler, and this handler is associated with this looper, than the message is processed by that handler.

2. Else, the preferred handler is used. You can set this using [SetPreferredHandler()](classBLooper.md#a07c6e5c65354b48465fde2b0b44e22c6).

3. If there is no preferred handler, then the looper itself will process the message.



Because a looper usually is used in multiple threads, you should make sure you [Lock()](classBLooper.md#a757a3e406ea3b7bb9a1ad16d04689b1d) and [Unlock()](classBLooper.md#ac84ea15405640082b9fda58f6672467c) it during most operations. Locking calls can be recursive (so multiple locks can come from a single thread), but make sure you pair every [Lock()](classBLooper.md#a757a3e406ea3b7bb9a1ad16d04689b1d) with an [Unlock()](classBLooper.md#ac84ea15405640082b9fda58f6672467c) call. Failing to do so will inevitably cause a deadlock.


Because a looper provides a separate thread, and the inherited handler is usually a default handler, you will most often use this class by subclassing it. For example, you are likely to subclass [BWindow](../interface_kit/classBWindow.md) (which is derived from [BLooper](classBLooper.md)) to customize your window and handle the messages sent to that window. You can override [Run()](classBLooper.md#a88bb85410e0c4124bdc6f16168df4811) in case you want to perform additional tasks before (or right after) starting the message loop. You can override [QuitRequested()](classBLooper.md#aff7aaf066538383f0e0ea28d18eb8863) if you want to decline quitting in certain circumstances. You can override [Quit()](classBLooper.md#a10d5a4873f14fd247890a6dfc9b8b949) in case you want to perform additional procedures during closing time. You can also override [DispatchMessage()](classBLooper.md#add21ca8765c67b0dbf95b8f0361afa73) if you want to do something with all incoming messages before they are dispatched to a handler.


[BLooper](classBLooper.md) is one of the major base classes of the Haiku application programmers interface. Closely related classes are [BMessage](classBMessage.md), [BHandler](classBHandler.md) and [BMessenger](classBMessenger.md). It is used in the interface kit, for example by the [BWindow](../interface_kit/classBWindow.md) class, which makes sure every window runs it its own thread.


[BLooper](classBLooper.md) is a part of the chain in the eloquent messaging structure. For a proper understanding of all its facets, have a look at the [messaging overview](app_messaging.md).



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BLooper](#a33fa84a6ed383e5a897d11380d72ce38) (const char *name=NULL, int32 priority=B_NORMAL_PRIORITY, int32 portCapacity=B_LOOPER_PORT_DEFAULT_CAPACITY) — Construct a new BLooper with a priority and an capacity.
* `virtual` [~BLooper](#ab2fa21c0315644144f55523adbdc0457) () — Destruct the looper.
* `virtual status_t` [Perform](#adfc642544ce22888d412e6a4be25fa72) (perform_code d, void *arg) — Internal method.
* `status_t` [PostMessage](#a0de6737bfbf8a8b4913adc8c74bb544e) (uint32 command) — Post a message with the command as what identifier to this looper.
* `status_t` [PostMessage](#ae79a7818ce950d8edcd238f7948df020) (BMessage *message) — Post a message to this looper.
* `status_t` [PostMessage](#a2dc16ecf211eb7e32eaa4b08863e856d) (uint32 command, BHandler *handler, BHandler *replyTo=NULL) — Sends a message with command what identifier to the handler associated with this looper. A response may be sent to the replyTo handler asynchronously.
* `status_t` [PostMessage](#ac75eed80e72b236650f19b4015de6e99) (BMessage *message, BHandler *handler, BHandler *replyTo=NULL) — Send a message to the handler associated with this looper. A response may be sent to the replyTo handler asynchronously.
* `virtual void` [DispatchMessage](#add21ca8765c67b0dbf95b8f0361afa73) (BMessage *message, BHandler *handler) — Dispatch a message to a handler. Override if there are messages that you want to catch before they are sent to the handlers.
* `virtual void` [MessageReceived](#a89303d11c987dae76cdfc38ad5d3c4c2) (BMessage *message) — Process a message received by the internal handler of this looper.
* `BMessage *` [CurrentMessage](#a6d244af065c4a12ea795bbbc7bb20e07) () const — Retrieve the current message.
* `BMessage *` [DetachCurrentMessage](#a7c8f05bcc354bc1d53026417417120e3) () — Get ownership of the message currently being processed.
* `void` [DispatchExternalMessage](#a3a2d3773466de19a6c117f3a04861b11) (BMessage *message, BHandler *handler, bool &_detached) — Internal method to support single-threaded GUI toolkits.
* `BMessageQueue *` [MessageQueue](#ad0643973ceda5cca540c4684a9f670ac) () const — Get a pointer to the internal message queue of this looper.
* `bool` [IsMessageWaiting](#a27fd22b9eeaeadbeff1e973ed5242a64) () const — Check if there is a message waiting.
* `void` [AddHandler](#a484be74814014e3c48c1a16f44e34074) (BHandler *handler) — Associate a handler to this looper.
* `bool` [RemoveHandler](#a5af57140bf018388a2e64343f46ac330) (BHandler *handler) — Disassociate a handler from this looper.
* `int32` [CountHandlers](#a6179629238d0be92d7a89503be24d4e3) () const — Get the number of handlers associated with this looper.
* `BHandler *` [HandlerAt](#a6976132123edacf4b3a2831eadf5f4bf) (int32 index) const — Get the handler at an index of the list of associated handlers.
* `int32` [IndexOf](#a3061534f6d2f3186efca4cddd19f378f) (BHandler *handler) const — Get the index of the handler that is in the associated handler list.
* `BHandler *` [PreferredHandler](#af1a4af6872abc40a887bfcabd55aff98) () const — Get the preferred handler.
* `void` [SetPreferredHandler](#a07c6e5c65354b48465fde2b0b44e22c6) (BHandler *handler) — Set a preferred handler.
* `thread_id` [LockingThread](#a1d5d9dbc9d890ed1329b69fbfe9254b3) () const — Return the thread id of the thread that currently holds the lock.
* `int32` [CountLocks](#a4eec703acd9bd7fe9a455af0f81e08f9) () const — Return the number of recursive locks that are currently being held on this looper.
* `int32` [CountLockRequests](#a64e7b89294df1f7b614d1267f870ecd9) () const — Return the number of pending locks.
* `sem_id` [Sem](#aa96df67561b0ce1428ae45148c21e01f) () const — Return the id of the semaphore that is used to lock this looper.
* `virtual BHandler *` [ResolveSpecifier](#a16b494160d9b37d4dbbc0d426a22c946) (BMessage *message, int32 index, BMessage *specifier, int32 what, const char *property) — Determine the proper handler for a scripting message.
* `virtual status_t` [GetSupportedSuites](#a915a50de7d5b6263f0fd1a349a9a6d92) (BMessage *data) — Reports the suites of messages and specifiers that derived classes understand.
* `virtual void` [AddCommonFilter](#a25adc41bdfd741e9c82d2b469a5086b0) (BMessageFilter *filter) — Add a common filter to the list of filters that are applied to all incoming messages.
* `virtual bool` [RemoveCommonFilter](#ad2233fa143e9deff912bff39eebac4a2) (BMessageFilter *filter) — Remove a filter from the common message filter list.
* `virtual void` [SetCommonFilterList](#a9b39e686873763cc6491c91f77b177b7) (BList *filters) — Set a new list of filters that need to be applied to all incoming messages.
* `BList *` [CommonFilterList](#ad64f1a98c1cce8087e7d492860461a62) () const — Return a list of filters applied to all incoming messages.
* [BHandler](#a2142e21fe781b24f914ec2086e5f05b7) (const char *name=NULL) — Construct a new handler with a name.
* `virtual` [~BHandler](#a928254034959d19ef588b7898a6f8194) () — Free the filters of this handler, as well as the list of observers.
* `virtual status_t` [Perform](#a4e6ebc7ebcb72855a1f0fee7bde99766) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).
* [BHandler](#add8fa081a7bb8633581e78777b215d0b) (BMessage *data) — Construct a handler from an archived message.
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

### Protected Member Functions

* `BMessage *` [MessageFromPort](#a1be73aad8e8fed41659b98633525e5b3) (bigtime_t=B_INFINITE_TIMEOUT) — Hook method to retrieve a message from the looper's port.

### Archiving

* [BLooper](#aad314758fd652fb48d61bcccab8b6ae3) (BMessage *data) — Construct a looper from an archived message.
* `virtual status_t` [Archive](#a791ef8664f674b6683d551762888f1c2) (BMessage *data, bool deep=true) const — Archive a looper to a message.
* `static BArchivable *` [Instantiate](#aee61314ab77c54a64f8122440189b73a) (BMessage *data) — Static method to instantiate a looper from an archived message.

### Loop Control

* `virtual thread_id` [Run](#a88bb85410e0c4124bdc6f16168df4811) () — Start the event loop.
* `void` [Loop](#a5cb1d2eb7640fdcbc1085ad19583691d) () — Run the event loop in the current thread.
* `virtual void` [Quit](#a10d5a4873f14fd247890a6dfc9b8b949) () — Hook method that is called after a B_QUIT_REQUESTED message.
* `virtual bool` [QuitRequested](#aff7aaf066538383f0e0ea28d18eb8863) () — Hook method that is called during a B_QUIT_REQUESTED message.
* `bool` [Lock](#a757a3e406ea3b7bb9a1ad16d04689b1d) () — Lock the looper.
* `void` [Unlock](#ac84ea15405640082b9fda58f6672467c) () — Unlock a locked looper.
* `bool` [IsLocked](#a525d6677c2fc76a84c2d48853dad142a) () const — Check if a looper is locked.
* `status_t` [LockWithTimeout](#a734cdb06bfe92efdea24528c9b43bfc1) (bigtime_t timeout) — Lock a looper with a timeout.
* `thread_id` [Thread](#a257d396d04d128edf7a0c9669ead36c0) () const — Return the thread id of the internal message looper thread.
* `team_id` [Team](#afeb7a4900f26e7746d6c8bdb5cf684f3) () const — Return the team id in which this looper exists.
* `static BLooper *` [LooperForThread](#acf16bb9628e7dbbace3920ebeff6dc34) (thread_id thread) — Static method to retrieve a BLooper for a specified thread.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#a0c23aeb48d578525f81ba6d47f968528) (BMessage *data) — Static method to instantiate a handler from an archived message.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BLooper()`

```cpp
BLooper::BLooper(const char * name = NULL, int32 priority = B_NORMAL_PRIORITY, int32 portCapacity = B_LOOPER_PORT_DEFAULT_CAPACITY)
```

Construct a new [BLooper](classBLooper.md) with a *priority* and an *capacity*. 


The new looper is, by default, not running yet. If you have set up everything properly, you may call [Run()](classBLooper.md#a88bb85410e0c4124bdc6f16168df4811).



> [!IMPORTANT]
> Remember that loopers should be created on the heap, because they will `delete` themselves in the [Quit()](classBLooper.md#a10d5a4873f14fd247890a6dfc9b8b949) method.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the looper. |
| `priority` | The priority of the message thread of this looper. The default priority should be good enough for most tasks. Also, some derived versions of [BLooper](classBLooper.md) will use a specialized priority. So it is advised to leave this setting at the default, unless you know why you would like another setting. |
| `portCapacity` | Loopers use ports to send and receive messages (see the kernel kit). Ports have a maximum capacity; if there are so many messages queued that the port is full, all other incoming messages are dropped. There are situations where the size of the port should be different from the default. This might be when your looper receives a lot of messages, or if the message handling thread runs at a lower priority than normal, which would decrease the processing speed. Finding a suitable value for these custom scenarios would be done by testing. |





**See also:** [Run()](classBLooper.md#a88bb85410e0c4124bdc6f16168df4811)



**Since:** BeOS R3

---

### `~BLooper()`

```cpp
BLooper::~BLooper()
```

Destruct the looper. 


You will never delete a looper yourself. You should pass a `B_QUIT_REQUESTED` message, or if you are destroying the looper from inside its own message handling thread, you should call [Quit()](classBLooper.md#a10d5a4873f14fd247890a6dfc9b8b949).



**See also:** [Quit()](classBLooper.md#a10d5a4873f14fd247890a6dfc9b8b949)



**Since:** BeOS R3

---

### `BLooper()`

```cpp
BLooper::BLooper(BMessage * data)
```

Construct a looper from an archived message. 


The *data* message has to be constructed by a [BLooper::Archive()](classBLooper.md#a791ef8664f674b6683d551762888f1c2) call. Note that the data that is restored, is merely the port capacity and the name of the looper/handler. Other data, such as filters, is not archived by the default archiver.



> [!WARNING]
> This constructor does no type check whatsoever. Since you can pass any [BMessage](classBMessage.md), you should - if you are not sure about the exact type - use the [Instantiate()](classBLooper.md#aee61314ab77c54a64f8122440189b73a) method, which does check the type.



**See also:** [Instantiate()](classBLooper.md#aee61314ab77c54a64f8122440189b73a)



**Since:** BeOS R3

---

### `AddCommonFilter()`

```cpp
void BLooper::AddCommonFilter(BMessageFilter * filter)
```

Add a common filter to the list of filters that are applied to all incoming messages. 


Filters can only be applied once, so they cannot be shared between loopers, a handler and a looper or between two handlers.


The *filter* is not copied; rather a pointer is stored. Keep the *filter* alive as long as it is used by a looper.



**See also:** [RemoveCommonFilter()](classBLooper.md#ad2233fa143e9deff912bff39eebac4a2)



**Since:** BeOS R3

---

### `AddHandler()`

```cpp
void BLooper::AddHandler(BHandler * handler)
```

Associate a *handler* to this looper. 


The *handler* will be associated to this looper. By default, the handler in this looper will be chained to the supplied *handler*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `handler` | The handler to associate with this looper. If the handler is already associated to another looper, the operation will fail silently. Check beforehand if you cannot be sure that the *handler* is unassociated. |





**See also:** [RemoveHandler()](classBLooper.md#a5af57140bf018388a2e64343f46ac330)



**Since:** BeOS R3

---

### `Archive()`

```cpp
status_t BLooper::Archive(BMessage * data, bool deep = true)const
```

Archive a looper to a message. 


Currently, only the name and the port capacity are archived. Any other data, such as the filters, is not stored.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The message to archive the object in. |
| `deep` | This parameter is ignored, as [BLooper](classBLooper.md) does not have children. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Archiving succeeded. |
| B_BAD_VALUE | The *data* parameter is not a valid message. |





**See also:** [BLooper::Instantiate(BMessage* data)](classBLooper.md#aee61314ab77c54a64f8122440189b73a)



**Since:** BeOS R3


Reimplemented from [BHandler](classBHandler.md#ac2711ccff5e7f711244c88a5642c83db).


Reimplemented in [BWindow](../interface_kit/classBWindow.md#a69163d40d8f1eda77c9134ad4ab745a2), [BApplication](classBApplication.md#aa36536582835264341376064cbc96a27), [BDirectWindow](../game_kit/classBDirectWindow.md#a39e69ba4bba5221b3099cf34129862c8), and [BAlert](../interface_kit/classBAlert.md#aba312ca5f7e668bf4d96efc7f41625a3).

---

### `CommonFilterList()`

```cpp
BList * BLooper::CommonFilterList()const
```

Return a list of filters applied to all incoming messages. 



**Returns:** A pointer to the internal filter list, or `NULL` if such a list has not yet been created. Please note that you should use the internal list management functions to manipulate the internal filter list, in order to maintain internal consistency.



**See also:** [AddCommonFilter()](classBLooper.md#a25adc41bdfd741e9c82d2b469a5086b0)



**Since:** BeOS R3

---

### `CountHandlers()`

```cpp
int32 BLooper::CountHandlers()const
```

Get the number of handlers associated with this looper. 



**See also:** [HandlerAt()](classBLooper.md#a6976132123edacf4b3a2831eadf5f4bf)



**Since:** BeOS R3

---

### `CountLockRequests()`

```cpp
int32 BLooper::CountLockRequests()const
```

Return the number of pending locks. 



**Since:** BeOS R3

---

### `CountLocks()`

```cpp
int32 BLooper::CountLocks()const
```

Return the number of recursive locks that are currently being held on this looper. 



**Since:** BeOS R3

---

### `CurrentMessage()`

```cpp
BMessage * BLooper::CurrentMessage()const
```

Retrieve the current message. 



> [!IMPORTANT]
> Only call this method from within the thread that processes the messages. It contains a pointer to the message that is currently being handled. Due to the multithreaded nature of the operating system, this method will not safely let you read the message that is being processed by this handler from outside the context of the processing. If you do want to use a message outside of the processing thread, have a look at [DetachCurrentMessage()](classBLooper.md#a7c8f05bcc354bc1d53026417417120e3) to safely retrieve a message.



**Returns:** A pointer to the message that is currently being processed. Note that calling it from outside the thread that processes the message, could give you a `NULL` pointer or an invalid pointer.



**Since:** BeOS R5

---

### `DetachCurrentMessage()`

```cpp
BMessage * BLooper::DetachCurrentMessage()
```

Get ownership of the message currently being processed. 


Retrieve the current message and gain ownership of it. This means that the message will not be deleted as soon as the looper is done processing it. You can then use it for different purposes.



> [!IMPORTANT]
> Only call this method from within the thread that processes the messages. Due to the multithreaded nature of the operating system, calling it from another thread is very likely to give you an invalid or a `NULL` pointer.



**Since:** BeOS R5

---

### `DispatchExternalMessage()`

```cpp
void BLooper::DispatchExternalMessage(BMessage * message, BHandler * handler, bool & _detached)
```

Internal method to support single-threaded GUI toolkits. 



**Since:** Haiku R1

---

### `DispatchMessage()`

```cpp
void BLooper::DispatchMessage(BMessage * message, BHandler * handler)
```

Dispatch a message to a handler. Override if there are messages that you want to catch before they are sent to the handlers. 


This method is called by the message looping thread to dispatch a message to *handler*. If you implement the [BLooper](classBLooper.md) class and your looper receives messages that absolutely have to be processed by the looper instead of any of the handlers, override this method. For example, the default implementation catches B_QUIT_REQUESTED messages before they are sent to the handlers, so that the looper will quit at those messages.


You are discouraged from using this method to filter out any messages you do not want to process. For this, there is a more generic method using the [BMessageFilter](classBMessageFilter.md) class. If you want to skip messages with certain patterns, have a look at the [AddCommonFilter()](classBLooper.md#a25adc41bdfd741e9c82d2b469a5086b0) and [SetCommonFilterList()](classBLooper.md#a9b39e686873763cc6491c91f77b177b7) methods.


If you do override this method, please remember to call the [DispatchMessage()](classBLooper.md#add21ca8765c67b0dbf95b8f0361afa73) method of the parent class.



**Since:** BeOS R3


Reimplemented in [BApplication](classBApplication.md#a034ef79fe7f1ca45e63193c76a6fd128), [BDirectWindow](../game_kit/classBDirectWindow.md#a62952e05d331dde0b091998db878a9f6), [BAlert](../interface_kit/classBAlert.md#a29b871841d182889a147b58b16a7c111), and [BWindow](../interface_kit/classBWindow.md#a2089af8a214389c3f673c06420457b16).

---

### `GetSupportedSuites()`

```cpp
status_t BLooper::GetSupportedSuites(BMessage * data)
```

Reports the suites of messages and specifiers that derived classes understand. 



**Since:** BeOS R3


Reimplemented from [BHandler](classBHandler.md#acf34435dada239f411e8e034e0ea36b5).


Reimplemented in [BApplication](classBApplication.md#a0fb9cc161a785cad42925075a087fc16), [BDirectWindow](../game_kit/classBDirectWindow.md#a55e920fcba8972f5173bd3714f416c13), [BAlert](../interface_kit/classBAlert.md#a9e658b2f7dc50b2c5da3191d77a22594), and [BWindow](../interface_kit/classBWindow.md#a8c2f3013601609b54778af99fa6a25ca).

---

### `HandlerAt()`

```cpp
BHandler * BLooper::HandlerAt(int32 index)const
```

Get the handler at an *index* of the list of associated handlers. 



**Returns:** A pointer to the handler at that *index*, or `NULL` if the *index* is out of range.



**See also:** [CountHandlers()](classBLooper.md#a6179629238d0be92d7a89503be24d4e3)



**Since:** BeOS R3

---

### `IndexOf()`

```cpp
int32 BLooper::IndexOf(BHandler * handler)const
```

Get the index of the *handler* that is in the associated handler list. 



**Returns:** The index of the handler in the list if the *handler* is in the list, else this method will return -1.



**Since:** BeOS R3

---

### `Instantiate()`

```cpp
BArchivable * BLooper::Instantiate(BMessage * data)
```

Static method to instantiate a looper from an archived message. 



**Returns:** A pointer to the instantiated looper, or `NULL` if the *data* is not a valid archived [BLooper](classBLooper.md) object.



**See also:** [BLooper(BMessage* data)](classBLooper.md#aad314758fd652fb48d61bcccab8b6ae3)



**Since:** BeOS R3

---

### `IsLocked()`

```cpp
bool BLooper::IsLocked()const
```

Check if a looper is locked. 



**Returns:** `true` if the looper is locked, `false` if the looper is not locked, or the looper has been deleted.



**See also:** [Lock()](classBLooper.md#a757a3e406ea3b7bb9a1ad16d04689b1d)



**Since:** BeOS R5

---

### `IsMessageWaiting()`

```cpp
bool BLooper::IsMessageWaiting()const
```

Check if there is a message waiting. 



**Returns:** `true` if there are still messages to be processed, `false` if there is no message waiting.

---

### `Lock()`

```cpp
bool BLooper::Lock()
```

Lock the looper. 


For most operations involving the internal data of the looper, you need to hold the lock. Each looper implements a global lock, which you can use to perform operations on internal data in a thread-safe manner.


Do not forget to pair each [Lock()](classBLooper.md#a757a3e406ea3b7bb9a1ad16d04689b1d) request with an [Unlock()](classBLooper.md#ac84ea15405640082b9fda58f6672467c) request. [Lock()](classBLooper.md#a757a3e406ea3b7bb9a1ad16d04689b1d) requests can be stacked, which means that recursively locking a looper from a thread that actually holds the lock, will not cause a deadlock. See [BLocker](../support_kit/classBLocker.md) for more information on locking internals.



**Returns:** `true` if the locking request succeeded, `false` if the locking request could not be completed. There are a variety of reasons for this to happen, for example when the looper is destroyed.



**See also:** [Unlock()](classBLooper.md#ac84ea15405640082b9fda58f6672467c)



**Since:** BeOS R5


Referenced by [BAutolock::Lock()](../support_kit/classBAutolock.md#a5808a41f3c76294ed35deef3864c9a7c).

---

### `LockingThread()`

```cpp
thread_id BLooper::LockingThread()const
```

Return the thread id of the thread that currently holds the lock. 



**Since:** BeOS R3

---

### `LockWithTimeout()`

```cpp
status_t BLooper::LockWithTimeout(bigtime_t timeout)
```

Lock a looper with a *timeout*. 


This method locks the looper like [Lock()](classBLooper.md#a757a3e406ea3b7bb9a1ad16d04689b1d), but if the locking request does not succeed within the provided *timeout*, the method will return.


Parameters

| Parameter | Description |
| :--- | :--- |
| `timeout` | The maximum time to wait for the lock request to succeed. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The lock is acquired. |
| B_BAD_VALUE | The looper has been destroyed. |
| other errors | There was an error acquiring the lock. |





**See also:** [Lock()](classBLooper.md#a757a3e406ea3b7bb9a1ad16d04689b1d)



**Since:** BeOS R5

---

### `Loop()`

```cpp
thread_id BLooper::Loop()
```

Run the event loop in the current thread. 


This method runs the event loop in an already existing thread. It blocks until the looper stops looping. This can be used to turn an existing thread into a [BLooper](classBLooper.md).


Make sure the looper is not yet running before you call this method.



**Since:** Haiku R1

---

### `LooperForThread()`

```cpp
BLooper * BLooper::LooperForThread(thread_id thread)
```

Static method to retrieve a [BLooper](classBLooper.md) for a specified *thread*. 



**Since:** BeOS R3

---

### `MessageFromPort()`

```cpp
BMessage * BLooper::MessageFromPort(bigtime_t timeout = B_INFINITE_TIMEOUT)
```

Hook method to retrieve a message from the looper's port. 


The default implementation is called by the internal message looping thread and retrieves the next message from the port that belongs to this looper.


If you use a looper in a context where it might receive messages from other sources, you can override this method in order to insert these methods into the message processing. Note that any messages that are returned by this method will be deleted by this looper, so make sure you have ownership of the message. If you override this method, remember to call the base implementation every now and then, in order to retrieve the messages arriving at the default port.



**Since:** Haiku R1

---

### `MessageQueue()`

```cpp
BMessageQueue * BLooper::MessageQueue()const
```

Get a pointer to the internal message queue of this looper. 


You can use this pointer to manipulate the message queue. Note that the message that is being processed is already detached from this queue.



**Returns:** A pointer to the internal message queue.



**Since:** BeOS R5

---

### `MessageReceived()`

```cpp
void BLooper::MessageReceived(BMessage * message)
```

Process a message received by the internal handler of this looper. 


Reimplemented from [BHandler::MessageReceived()](classBHandler.md#aeecda5017e0081db617f23bbff71fb53);



**Since:** BeOS R5


Reimplemented from [BHandler](classBHandler.md#aeecda5017e0081db617f23bbff71fb53).


Reimplemented in [BApplication](classBApplication.md#aa010d676b8d372d522b7da39ddfb3b03), [BDirectWindow](../game_kit/classBDirectWindow.md#a1eb5e6dfeee341e9baf3d688ff66194a), [BAlert](../interface_kit/classBAlert.md#a1300fdf51e73dd4f8a24b908d6fc2e1e), and [BWindow](../interface_kit/classBWindow.md#a1ce544ea7d9adcc6941759817a42affe).

---

### `Perform()`

```cpp
status_t BLooper::Perform(perform_code d, void * arg)
```

Internal method. 



**Since:** Haiku R1


Reimplemented from [BHandler](classBHandler.md#a4e6ebc7ebcb72855a1f0fee7bde99766).


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#a113afd3534fca8b81bcc86f8e55738be), [BWindow](../interface_kit/classBWindow.md#afde7d74e5526f740dedb82a1d10faa7a), [BApplication](classBApplication.md#ab8fea9f4a96bdee62ce77a089d472973), and [BAlert](../interface_kit/classBAlert.md#a3d2769c5bf9b9822f21770e38e561fd6).

---

### `PostMessage()`

```cpp
status_t BLooper::PostMessage(BMessage * message)
```

Post a *message* to this looper. 


Posting a message puts it in the message queue. The message passes through the default handler chain.


The *message* is copied, and as such, you should make sure you will not leak it. The best way to send messages is like this: 


```cpp
BMessage message;
message.what = B_DO_SOMETHING;
message.AddString("some_data", "This is data")
 
aLooper->PostMessage(&message);
```

Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The message you would like to pass to this method. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded, and the message is sent to the port. |
| B_ERROR | There was a general operation error. |
| B_BAD_VALUE | This looper is not yet running and therefore cannot receive messages. |





**See also:** [PostMessage(uint32)](classBLooper.md#a0de6737bfbf8a8b4913adc8c74bb544e) if you want to send a message without data members.



**Since:** BeOS R5

---

### `PostMessage()`

```cpp
status_t BLooper::PostMessage(BMessage * message, BHandler * handler, BHandler * replyTo = NULL)
```

Send a *message* to the *handler* associated with this looper. A response may be sent to the *replyTo* handler asynchronously. 


The target *handler* should be associated with this looper. This method bypasses the default message queue.


The *message* is copied, and as such, you should make sure you will not leak it. The best way to send messages is like this: 


```cpp
BMessage message;
message.what = B_DO_SOMETHING;
message.AddString("some_data", "This is data")
 
aLooper->PostMessage(&message, aHandler);
```

Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The message you want to pass. |
| `handler` | The handler you would like to pass this message to. |
| `replyTo` | If you would like to request a reply, pass the handler to which this reply should be directed to. If you pass `NULL`, you will not receive a reply. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded, and the message is sent to the port. |
| B_ERROR | There was a general operation error. |
| B_BAD_VALUE | This looper is not yet running and therefore cannot receive messages. |
| B_MISMATCHED_VALUES | The *handler* is not associated with this looper. |





**See also:** [PostMessage(uint32)](classBLooper.md#a0de6737bfbf8a8b4913adc8c74bb544e) if you want to send a message without data members.



**Since:** BeOS R5

---

### `PostMessage()`

```cpp
status_t BLooper::PostMessage(uint32 command)
```

Post a message with the *command* as `what` identifier to this looper. 


Posting a message puts it in the message queue. The message passes through the default handler chain.


Parameters

| Parameter | Description |
| :--- | :--- |
| `command` | The `what` identifier of the message to be sent. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded, and the message is sent to the port. |
| B_ERROR | There was a general operation error. |
| B_BAD_VALUE | This looper is not yet running and therefore cannot receive messages. |





**See also:** [PostMessage(BMessage *)](classBLooper.md#ae79a7818ce950d8edcd238f7948df020) if you want to send a message with data members.



**Since:** BeOS R5

---

### `PostMessage()`

```cpp
status_t BLooper::PostMessage(uint32 command, BHandler * handler, BHandler * replyTo = NULL)
```

Sends a message with *command* `what` identifier to the *handler* associated with this looper. A response may be sent to the *replyTo* handler asynchronously. 


The target *handler* should be associated with this looper. This method bypasses the default message queue.


Parameters

| Parameter | Description |
| :--- | :--- |
| `command` | The value you want as the message's `what` identifier. |
| `handler` | The handler you would like to pass this message to. |
| `replyTo` | If you would like to request a reply, pass the handler to which this reply should be directed to. If you pass `NULL`, you will not receive a reply. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded, and the message is sent to the port. |
| B_ERROR | There was a general operation error. |
| B_BAD_VALUE | This looper is not yet running and therefore cannot receive messages. |
| B_MISMATCHED_VALUES | The *handler* is not associated with this looper. |





**See also:** [PostMessage(uint32)](classBLooper.md#a0de6737bfbf8a8b4913adc8c74bb544e) if you want to send a message without data members.



**Since:** BeOS R5

---

### `PreferredHandler()`

```cpp
BHandler * BLooper::PreferredHandler()const
```

Get the preferred handler. 



**Returns:** A pointer to the preferred handler, or `NULL` if none is set.



**See also:** [SetPreferredHandler()](classBLooper.md#a07c6e5c65354b48465fde2b0b44e22c6)



**Since:** BeOS R3

---

### `Quit()`

```cpp
void BLooper::Quit()
```

Hook method that is called after a `B_QUIT_REQUESTED` message. 


If you want to quit and delete the looper, you should post a `B_QUIT_REQUESTED` message. This will first call the hook method [QuitRequested()](classBLooper.md#aff7aaf066538383f0e0ea28d18eb8863), which can be overridden in child classes in case there are conditions that would prevent the looper to be quit. If you really know what you are doing, and you definitely want to quit this looper, you may call this method, but only after performing a [Lock()](classBLooper.md#a757a3e406ea3b7bb9a1ad16d04689b1d) operation.


Override this method if your subclass needs to perform specific clean-up tasks. Remember to call the base class implementation when you're done.



> [!IMPORTANT]
> You will not have to delete the looper object, if a looper quits it will delete itself.



**Since:** BeOS R3


Reimplemented in [BApplication](classBApplication.md#abd8cb94d425105f89bf9e18f01552015), [BDirectWindow](../game_kit/classBDirectWindow.md#a0e078c054a66514021099c529cfdde2f), [BAlert](../interface_kit/classBAlert.md#a691fe42dc7dc5acea09771e9c080dd0e), and [BWindow](../interface_kit/classBWindow.md#a054c0206836014dcc20c59e50bceab44).

---

### `QuitRequested()`

```cpp
bool BLooper::QuitRequested()
```

Hook method that is called during a `B_QUIT_REQUESTED` message. 


This hook function is called by the looper thread when a `B_QUIT_REQUESTED` is received. The default implementation always accepts the message, but if your subclass needs a special condition to be met before actually accepting a quit message, you can test for that condition in this hook method. A good example is a window (which is a derivative of [BLooper](classBLooper.md)), which contains a modified document. The condition may be that a modal dialog requesting a path of action is closed.



**Returns:** `true` if the looper can be quit and destroyed, `false` if this method does not accept the quit message and continue processing messages.



**Since:** BeOS R3


Reimplemented in [BApplication](classBApplication.md#a4965aea57452c88022f0fdba2af65e0a), [BAlert](../interface_kit/classBAlert.md#ae91bb7bb3b99006f0b2616d47cf85985), and [BWindow](../interface_kit/classBWindow.md#a8fccbfd10fceb2c6103c6036ca9e961a).

---

### `RemoveCommonFilter()`

```cpp
bool BLooper::RemoveCommonFilter(BMessageFilter * filter)
```

Remove a *filter* from the common message filter list. 


Note that this will not free the memory used by the *filter*, so you should dispose of it yourself.



**See also:** [AddCommonFilter()](classBLooper.md#a25adc41bdfd741e9c82d2b469a5086b0)



**Since:** BeOS R3

---

### `RemoveHandler()`

```cpp
bool BLooper::RemoveHandler(BHandler * handler)
```

Disassociate a *handler* from this looper. 


If the handler is disassociated, it can be reassociated to another looper.



**Returns:** `true` if the *handler* has been removed from this looper, `false` The *handler* was invalid or the handler was not associated to this looper.



**See also:** [AddHandler()](classBLooper.md#a484be74814014e3c48c1a16f44e34074)



**Since:** BeOS R3

---

### `ResolveSpecifier()`

```cpp
BHandler * BLooper::ResolveSpecifier(BMessage * message, int32 index, BMessage * specifier, int32 what, const char * property)
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


Reimplemented from [BHandler](classBHandler.md#a76439ffaf84e65232698d2a4a3317d22).


Reimplemented in [BApplication](classBApplication.md#a044d40580b05617288c91748cbd30513), [BAlert](../interface_kit/classBAlert.md#a22285daeb96ea0936faab97b077115e6), [BDirectWindow](../game_kit/classBDirectWindow.md#aee5db7142cabc984cb16e61eaa7baa36), and [BWindow](../interface_kit/classBWindow.md#aaf328e28799cf868ec31df2847a4ed37).

---

### `Run()`

```cpp
thread_id BLooper::Run()
```

Start the event loop. 


After the looper has been constructed, it needs to be started using this method. A thread will be spawned, which will receive messages.


Make sure the looper is not yet running before you call this method.



**Returns:** A (positive) thread id if spawning the thread succeeded, or an error code.



**Since:** BeOS R3


Reimplemented in [BApplication](classBApplication.md#a3fd11f52918b337f01eab978e8a56bad), and [BWindow](../interface_kit/classBWindow.md#ae49c02ad870d55514c800631b37b97cf).

---

### `Sem()`

```cpp
sem_id BLooper::Sem()const
```

Return the id of the semaphore that is used to lock this looper. 



**Since:** BeOS R3

---

### `SetCommonFilterList()`

```cpp
void BLooper::SetCommonFilterList(BList * filters)
```

Set a new list of *filters* that need to be applied to all incoming messages. 


You are responsible for validating that all the items in the list of *filters* are actual filters. The old list is discarded; all the filters are **destroyed**.


Note that filters can only be applied to one looper or handler. If any of the filters is already associated with another one, this call will fail.



**See also:** [AddCommonFilter()](classBLooper.md#a25adc41bdfd741e9c82d2b469a5086b0)



**Since:** BeOS R3

---

### `SetPreferredHandler()`

```cpp
void BLooper::SetPreferredHandler(BHandler * handler)
```

Set a preferred handler. 


If messages are posted to this looper using one of the [PostMessage()](classBLooper.md#a0de6737bfbf8a8b4913adc8c74bb544e) methods without a specific [BHandler](classBHandler.md) argument, the messages will be handled by the looper itself (since a looper is a subclass of [BHandler](classBHandler.md), this is perfectly possible). If you want to override that behavior, you should set a preferred handler. This handler will be called if incoming messages do not ask to be directly passed on to a specific handler.


Parameters

| Parameter | Description |
| :--- | :--- |
| `handler` | The preferred handler you want undesignated messages to be handled by. If you want to unset the preferred handler, pass `NULL`. If the supplied *handler* is not associated with this looper, this call will fail silently and the current preferred handler will be unset. |





**See also:** [PreferredHandler()](classBLooper.md#af1a4af6872abc40a887bfcabd55aff98)



**Since:** BeOS R3

---

### `Team()`

```cpp
team_id BLooper::Team()const
```

Return the team id in which this looper exists. 



**Since:** BeOS R3

---

### `Thread()`

```cpp
thread_id BLooper::Thread()const
```

Return the thread id of the internal message looper thread. 


If the looper is not yet running, this method will return 0.



**See also:** [Run()](classBLooper.md#a88bb85410e0c4124bdc6f16168df4811)



**Since:** BeOS R3

---

### `Unlock()`

```cpp
void BLooper::Unlock()
```

Unlock a locked looper. 


Use this method paired with [Lock()](classBLooper.md#a757a3e406ea3b7bb9a1ad16d04689b1d) calls, to release a lock. Make sure that this method is only called on a locked looper.



**See also:** [Lock()](classBLooper.md#a757a3e406ea3b7bb9a1ad16d04689b1d)



**Since:** BeOS R5


Referenced by [BAutolock::Unlock()](../support_kit/classBAutolock.md#a62e220b72b39ffa459b51dae1ca50332).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBLooper.html).
