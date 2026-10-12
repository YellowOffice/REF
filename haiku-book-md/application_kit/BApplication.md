---
name: BApplication
type: class
kit: application_kit
brief: "A container object for an application"
source: haiku-book
---

# BApplication Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A container object for an application. 


A [BApplication](classBApplication.md) establishes a connection between the application and the Application Server.


The most common task performed by a [BApplication](classBApplication.md) object is to handle messages sent to it. The [BApplication](classBApplication.md) object also is used to get information about your application such as the number of windows it has, its signature, executable location, and launch flags.


The [BApplication](classBApplication.md) object is automatically assigned to the global `be_app` variable. The `be_app` variable allows you to refer to your [BApplication](classBApplication.md) object from anywhere in the code.


To use a [BApplication](classBApplication.md) you first construct the object and then begin its message loop by calling the [Run()](classBApplication.md#a3fd11f52918b337f01eab978e8a56bad) method. The [Run()](classBApplication.md#a3fd11f52918b337f01eab978e8a56bad) method continues until the application is told to quit. Once [Run()](classBApplication.md#a3fd11f52918b337f01eab978e8a56bad) returns you should then delete the [BApplication](classBApplication.md) object to free its memory usage.


Typically, you initialize the [BApplication](classBApplication.md) object in the programs main() function. A typical main() function looks something like this:



```cpp
#include Application.h
 
main()
{
 /* Vendor is your vendor name, application is your application name */
 BApplication *app = new BApplication("application/x-vnd.vendor-application");
    app->Run();
 delete app;
 
 return 0;
}
```


**Since:** BeOS R3

## Member List

### Public Member Functions

* [BApplication](#a43b0671b327a0883720c6cc18d908149) (const char *signature) — Initialize a BApplication with the passed in signature.
* [BApplication](#a998f767f4ddcbb5588455c8b63e08f74) (const char *signature, status_t *error) — Initialize a BApplication with the passed in signature and a pointer to an error message.
* `virtual` [~BApplication](#a5563631a21adb4136b56ba1fb9cd4487) () — Destructor Method.
* `status_t` [InitCheck](#aef81a1f9e59c305f2af7a7ad8e240ae0) () const — Returns the status of the constructor.
* `virtual status_t` [Perform](#ab8fea9f4a96bdee62ce77a089d472973) (perform_code d, void *arg) — Internal method.
* `virtual thread_id` [Run](#a3fd11f52918b337f01eab978e8a56bad) () — Starts the message loop in the thread that it is called from, and doesn't return until the message loop stops.
* `virtual void` [Quit](#abd8cb94d425105f89bf9e18f01552015) () — Tells the thread to finish processing the message queue, disallowing any new messages.
* `virtual bool` [QuitRequested](#a4965aea57452c88022f0fdba2af65e0a) () — Hook method that gets invoked when the BApplication receives a B_QUIT_REQUESTED message.
* `virtual void` [ReadyToRun](#af912cef601090a89cc20cb3a7af48315) () — Hook method that's invoked when the BApplication receives a B_READY_TO_RUN message.
* `virtual void` [ArgvReceived](#a0826684edce56baa7a31c89c97a1d161) (int32 argc, char **argv) — Hook method that gets invoked when the application receives a B_ARGV_RECEIVED message.
* `virtual void` [AppActivated](#a71e7db8bc9e4f34137bcd4c5e3ed6a16) (bool active) — Hook method that gets invoked when the application receives B_APP_ACTIVATED message.
* `virtual void` [RefsReceived](#a5fae9740458d9aec66f3b1d5c50fae87) (BMessage *message) — Hook method that gets invoked when the application receives a B_REFS_RECEIVED message.
* `virtual void` [AboutRequested](#a47d9b29407642805b64f0478a21e5895) () — Hook method that gets invoked when the BApplication receives a B_ABOUT_REQUESTED message.
* `virtual void` [Pulse](#abf9de9bc0de3a8c504a4174f34ed82b4) () — Hook method that gets invoked when the BApplication receives a B_PULSE message.
* `void` [SetPulseRate](#a565e7ede16cd6a0e7df384c3c97ba860) (bigtime_t rate) — Sets the interval that the B_PULSE messages are sent.
* `virtual void` [MessageReceived](#aa010d676b8d372d522b7da39ddfb3b03) (BMessage *message)
* `virtual void` [DispatchMessage](#a034ef79fe7f1ca45e63193c76a6fd128) (BMessage *message, BHandler *handler)
* `virtual BHandler *` [ResolveSpecifier](#a044d40580b05617288c91748cbd30513) (BMessage *message, int32 index, BMessage *specifier, int32 form, const char *property)
* `virtual status_t` [GetSupportedSuites](#a0fb9cc161a785cad42925075a087fc16) (BMessage *data)
* `void` [ShowCursor](#ad21286f2cae75ee360d022fbacc8a21d) () — Restores the cursor.
* `void` [HideCursor](#a82504dfa192861bbf322e81550e53643) () — Hides the cursor from the screen.
* `void` [ObscureCursor](#a206c888fb8198a76c3b63668aadab0af) () — Hides the cursor until the mouse is moved.
* `bool` [IsCursorHidden](#a3503caddf7e23970a311b07d5db7576a) () const — Returns whether or not the cursor is hidden.
* `void` [SetCursor](#aa4262e1879bcdd8f82af94dab6d4650b) (const void *cursor) — Sets the cursor to be used when the application is active.
* `void` [SetCursor](#a08e75088c2f6396dfc9fc8c01a9c0545) (const BCursor *cursor, bool sync=true) — Sets the cursor to be used when the application is active with sync immediately option.
* `int32` [CountWindows](#a0cc9fc7396ac3717b238d61ab1f4b82b) () const — Returns the number of windows created by the application.
* `BWindow *` [WindowAt](#a8850d9542d628e11d91a4fd25279b65d) (int32 index) const — Returns the BWindow object at the specified index in the application's window list.
* `int32` [CountLoopers](#aa7ae6e5ae95ce7befab6e0022a2ec983) () const — Returns the number of BLoopers created by the application.
* `BLooper *` [LooperAt](#a68827a127ca45f4c421e3b30ca9500bf) (int32 index) const — Returns the BLooper object at the specified index in the application's looper list.
* `status_t` [RegisterLooper](#a2b46141e108da1167be0d3427ca37716) (BLooper *looper) — Register a looper to quit when the application quits.
* `status_t` [UnregisterLooper](#aac40a7828ef8cc9c65f65a30b14594f6) (BLooper *looper) — Remove a previously registered Looper from the quit-list.
* [BLooper](#a33fa84a6ed383e5a897d11380d72ce38) (const char *name=NULL, int32 priority=B_NORMAL_PRIORITY, int32 portCapacity=B_LOOPER_PORT_DEFAULT_CAPACITY) — Construct a new BLooper with a priority and an capacity.
* `virtual` [~BLooper](#ab2fa21c0315644144f55523adbdc0457) () — Destruct the looper.
* `virtual status_t` [Perform](#adfc642544ce22888d412e6a4be25fa72) (perform_code d, void *arg) — Internal method.
* `status_t` [PostMessage](#a0de6737bfbf8a8b4913adc8c74bb544e) (uint32 command) — Post a message with the command as what identifier to this looper.
* `status_t` [PostMessage](#ae79a7818ce950d8edcd238f7948df020) (BMessage *message) — Post a message to this looper.
* `status_t` [PostMessage](#a2dc16ecf211eb7e32eaa4b08863e856d) (uint32 command, BHandler *handler, BHandler *replyTo=NULL) — Sends a message with command what identifier to the handler associated with this looper. A response may be sent to the replyTo handler asynchronously.
* `status_t` [PostMessage](#ac75eed80e72b236650f19b4015de6e99) (BMessage *message, BHandler *handler, BHandler *replyTo=NULL) — Send a message to the handler associated with this looper. A response may be sent to the replyTo handler asynchronously.
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
* `virtual void` [AddCommonFilter](#a25adc41bdfd741e9c82d2b469a5086b0) (BMessageFilter *filter) — Add a common filter to the list of filters that are applied to all incoming messages.
* `virtual bool` [RemoveCommonFilter](#ad2233fa143e9deff912bff39eebac4a2) (BMessageFilter *filter) — Remove a filter from the common message filter list.
* `virtual void` [SetCommonFilterList](#a9b39e686873763cc6491c91f77b177b7) (BList *filters) — Set a new list of filters that need to be applied to all incoming messages.
* `BList *` [CommonFilterList](#ad64f1a98c1cce8087e7d492860461a62) () const — Return a list of filters applied to all incoming messages.
* [BLooper](#aad314758fd652fb48d61bcccab8b6ae3) (BMessage *data) — Construct a looper from an archived message.
* `void` [Loop](#a5cb1d2eb7640fdcbc1085ad19583691d) () — Run the event loop in the current thread.
* `bool` [Lock](#a757a3e406ea3b7bb9a1ad16d04689b1d) () — Lock the looper.
* `void` [Unlock](#ac84ea15405640082b9fda58f6672467c) () — Unlock a locked looper.
* `bool` [IsLocked](#a525d6677c2fc76a84c2d48853dad142a) () const — Check if a looper is locked.
* `status_t` [LockWithTimeout](#a734cdb06bfe92efdea24528c9b43bfc1) (bigtime_t timeout) — Lock a looper with a timeout.
* `thread_id` [Thread](#a257d396d04d128edf7a0c9669ead36c0) () const — Return the thread id of the internal message looper thread.
* `team_id` [Team](#afeb7a4900f26e7746d6c8bdb5cf684f3) () const — Return the team id in which this looper exists.
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

### Archiving

* [BApplication](#ae76219f7c7c91b14739e94c608f7349c) (BMessage *data) — Initialize a BApplication object from a message.
* `virtual status_t` [Archive](#aa36536582835264341376064cbc96a27) (BMessage *data, bool deep=true) const — Archive the BApplication object into a BMessage.
* `static BArchivable *` [Instantiate](#aa2814aceefbe18ac62814157f53a07c0) (BMessage *data) — Restores the BApplication object from a BMessage.

### Status

* `bool` [IsLaunching](#a49c3d8c8521a1b931f45fdcbaedb3f2d) () const — Returns whether or not the application is in the process of launching.
* `const char *` [Signature](#a9f22e1a76c3a742cc9139e947e2307b3) () const — Returns the signature of the Application.
* `status_t` [GetAppInfo](#a2b27a6149b1bf53e71a8d83382708308) (app_info *info) const — Fills out the info parameter with information about the application.
* `static BResources *` [AppResources](#a1aef5ac43f00eed24d6501b7afb50f47) () — Returns a BResources object for the application.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#aee61314ab77c54a64f8122440189b73a) (BMessage *data) — Static method to instantiate a looper from an archived message.
* `static BLooper *` [LooperForThread](#acf16bb9628e7dbbace3920ebeff6dc34) (thread_id thread) — Static method to retrieve a BLooper for a specified thread.
* `static BArchivable *` [Instantiate](#a0c23aeb48d578525f81ba6d47f968528) (BMessage *data) — Static method to instantiate a handler from an archived message.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.
* `BMessage *` [MessageFromPort](#a1be73aad8e8fed41659b98633525e5b3) (bigtime_t=B_INFINITE_TIMEOUT) — Hook method to retrieve a message from the looper's port.

## Detailed Member Documentation

### `BApplication()`

```cpp
BApplication::BApplication(const char * signature)
```

Initialize a [BApplication](classBApplication.md) with the passed in *signature*. 


The new [BApplication](classBApplication.md) is, by default, not running yet. If you have everything set up properly call [Run()](classBApplication.md#a3fd11f52918b337f01eab978e8a56bad) to start the application.


You should call [InitCheck()](classBApplication.md#aef81a1f9e59c305f2af7a7ad8e240ae0) to check for constructor initialization errors.


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | The *signature* of the application. |





**Since:** BeOS R3

---

### `BApplication()`

```cpp
BApplication::BApplication(const char * signature, status_t * _error)
```

Initialize a [BApplication](classBApplication.md) with the passed in *signature* and a pointer to an error message. 


Any error that occurs while constructing the [BApplication](classBApplication.md) will be set to the *_error* pointer. If *_error* points to a `status_t` error then you should not call [Run()](classBApplication.md#a3fd11f52918b337f01eab978e8a56bad).


Alternately, you can call [InitCheck()](classBApplication.md#aef81a1f9e59c305f2af7a7ad8e240ae0) to check for constructor initialization errors.


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | The *signature* of the application. |
| `_error` | A pointer to a `status_t` set by the [BApplication](classBApplication.md) constructor. |





**Since:** BeOS R5

---

### `~BApplication()`

```cpp
BApplication::~BApplication()
```

Destructor Method. 



**Since:** BeOS R3

---

### `BApplication()`

```cpp
BApplication::BApplication(BMessage * data)
```

Initialize a [BApplication](classBApplication.md) object from a message. 


The message must contain the signature of the application you wish to initialize in the "mime_sig" variable.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The message to initialize the [BApplication](classBApplication.md) from. |





**Since:** BeOS R3

---

### `AboutRequested()`

```cpp
void BApplication::AboutRequested()
```

Hook method that gets invoked when the [BApplication](classBApplication.md) receives a `B_ABOUT_REQUESTED` message. 


You should override this method to pop an alert to provide information about the application.


The default implementation pops a basic alert dialog.



**Since:** BeOS R3

---

### `AppActivated()`

```cpp
void BApplication::AppActivated(bool active)
```

Hook method that gets invoked when the application receives `B_APP_ACTIVATED` message. 


The message is sent whenever the application changes its active application status. The active flag set to is `true` when the application becomes active and is set to `false` when the application becomes inactive.


The application becomes activated in response to a user action such as clicking on or unhiding one of its windows. The application can have its active status set programmatically by calling either the [BWindow::Activate()](../interface_kit/classBWindow.md#a24ef781656049451c5c6ed06eeb98c06) or [BRoster::ActivateApp()](classBRoster.md#a29069168723243621a07f0c818201e77) methods.


This method is called after [ReadyToRun()](classBApplication.md#af912cef601090a89cc20cb3a7af48315) provided the application is displaying a window that can be set active.



**Since:** BeOS R3

---

### `AppResources()`

```cpp
BResources * BApplication::AppResources()
```

Returns a [BResources](../storage_kit/classBResources.md) object for the application. 



**Since:** BeOS R5

---

### `Archive()`

```cpp
status_t BApplication::Archive(BMessage * data, bool deep = true)const
```

Archive the [BApplication](classBApplication.md) object into a [BMessage](classBMessage.md). 



**See also:** [BArchivable::Archive()](../support_kit/classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44)



**Since:** BeOS R3


Reimplemented from [BLooper](classBLooper.md#a791ef8664f674b6683d551762888f1c2).

---

### `ArgvReceived()`

```cpp
void BApplication::ArgvReceived(int32 argc, char ** argv)
```

Hook method that gets invoked when the application receives a `B_ARGV_RECEIVED` message. 


If command line arguments are specified when the application is launched from the the shell, or if `argv/argc` values are passed to [BRoster::Launch()](classBRoster.md#a7336c58b9bea76b181c83c0d6e635360), then this method is executed.



> [!WARNING]
> [ArgvReceived()](classBApplication.md#a0826684edce56baa7a31c89c97a1d161) is not called if no command line arguments are specified, or if [BRoster::Launch()](classBRoster.md#a7336c58b9bea76b181c83c0d6e635360) was called without any `argv/argc` values.


The arguments passed to [ArgvReceived()](classBApplication.md#a0826684edce56baa7a31c89c97a1d161) are the constructed in the same way as those passed to command line programs. The number of command line arguments is passed in *argc* and the arguments themselves are passed as an array of strings in *argv*. The first *argv* string is the name of the program and the rest of the strings are the command line arguments.


[BRoster::Launch()](classBRoster.md#a7336c58b9bea76b181c83c0d6e635360) adds the program name to the front of the *argv* array and increments the *argc* value.


The `B_ARGV_RECEIVED` message (if sent) is sent only once, just before the `B_READY_TO_RUN` message is sent. However, if you try to relaunch an application that is already running and the application is set to `B_EXCLUSIVE_LAUNCH` or `B_SINGLE_LAUNCH` then the application will generate a `B_ARGV_RECEIVED` message and send it to the already running instance. Thus in this case the `B_ARGV_RECEIVED` message can show up at any time.



**Since:** BeOS R3

---

### `CountLoopers()`

```cpp
int32 BApplication::CountLoopers()const
```

Returns the number of BLoopers created by the application. 



> [!WARNING]
> This method may return `B_ERROR`.



**Returns:** The number of BLoopers in the application.



**Since:** BeOS R5

---

### `CountWindows()`

```cpp
int32 BApplication::CountWindows()const
```

Returns the number of windows created by the application. 



**Returns:** the number of windows created by the application.



**Since:** BeOS R3

---

### `DispatchMessage()`

```cpp
void BApplication::DispatchMessage(BMessage * message, BHandler * handler)
```

Dispatch a message to a handler. Override if there are messages that you want to catch before they are sent to the handlers.  


This method is called by the message looping thread to dispatch a message to *handler*. If you implement the [BLooper](classBLooper.md) class and your looper receives messages that absolutely have to be processed by the looper instead of any of the handlers, override this method. For example, the default implementation catches B_QUIT_REQUESTED messages before they are sent to the handlers, so that the looper will quit at those messages.


You are discouraged from using this method to filter out any messages you do not want to process. For this, there is a more generic method using the [BMessageFilter](classBMessageFilter.md) class. If you want to skip messages with certain patterns, have a look at the [AddCommonFilter()](classBLooper.md#a25adc41bdfd741e9c82d2b469a5086b0) and [SetCommonFilterList()](classBLooper.md#a9b39e686873763cc6491c91f77b177b7) methods.


If you do override this method, please remember to call the [DispatchMessage()](classBApplication.md#a034ef79fe7f1ca45e63193c76a6fd128) method of the parent class.



**Since:** BeOS R3


Reimplemented from [BLooper](classBLooper.md#add21ca8765c67b0dbf95b8f0361afa73).

---

### `GetAppInfo()`

```cpp
status_t BApplication::GetAppInfo(app_info * info)const
```

Fills out the *info* parameter with information about the application. 


This is equivalent to be_roster->GetRunningAppInfo(be_app->[Team()](classBLooper.md#afeb7a4900f26e7746d6c8bdb5cf684f3), info);



**Returns:** `B_NO_INIT` on an error or `B_OK` if all goes well.



**See also:** [BRoster::GetAppInfo()](classBRoster.md#ae0083d735bb8ebb40e66218b95693ab7)



**Since:** BeOS R3

---

### `GetSupportedSuites()`

```cpp
status_t BApplication::GetSupportedSuites(BMessage * data)
```

Reports the suites of messages and specifiers that derived classes understand.  



**Since:** BeOS R3


Reimplemented from [BLooper](classBLooper.md#a915a50de7d5b6263f0fd1a349a9a6d92).

---

### `HideCursor()`

```cpp
void BApplication::HideCursor()
```

Hides the cursor from the screen. 



**Since:** BeOS R3

---

### `InitCheck()`

```cpp
status_t BApplication::InitCheck()const
```

Returns the status of the constructor. 



**Returns:** If initialization succeeded returns `B_OK`, otherwise returns an error status.



**Since:** BeOS R5

---

### `Instantiate()`

```cpp
BArchivable * BApplication::Instantiate(BMessage * data)
```

Restores the [BApplication](classBApplication.md) object from a [BMessage](classBMessage.md). 



**See also:** [BArchivable::Instantiate()](../support_kit/classBArchivable.md#a04efcb17fa2a64a776923cc12303efcd)



**Since:** BeOS R3

---

### `IsCursorHidden()`

```cpp
bool BApplication::IsCursorHidden()const
```

Returns whether or not the cursor is hidden. 



**Returns:** `true` if the cursor is hidden, `false` if not.



**Since:** BeOS R3

---

### `IsLaunching()`

```cpp
bool BApplication::IsLaunching()const
```

Returns whether or not the application is in the process of launching. 



**Returns:** `true` if the application is launching, `false` if the application is already running.



**Since:** BeOS R3

---

### `LooperAt()`

```cpp
BLooper * BApplication::LooperAt(int32 index)const
```

Returns the [BLooper](classBLooper.md) object at the specified index in the application's looper list. 


If index is out of range, this function returns `NULL`.



**Returns:** The [BLooper](classBLooper.md) object at the specified *index* or `NULL` if the *index* is out of range.



**Since:** BeOS R5

---

### `MessageReceived()`

```cpp
void BApplication::MessageReceived(BMessage * message)
```

Handle *message* that has been received by the associated looper.  


This method is reimplemented by subclasses. If the messages that have been received by a looper pass through the filters, then they end up in the [MessageReceived()](classBApplication.md#aa010d676b8d372d522b7da39ddfb3b03) methods.


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


Reimplemented from [BLooper](classBLooper.md#a89303d11c987dae76cdfc38ad5d3c4c2).

---

### `ObscureCursor()`

```cpp
void BApplication::ObscureCursor()
```

Hides the cursor until the mouse is moved. 



**Since:** BeOS R3

---

### `Perform()`

```cpp
virtual status_t BApplication::Perform(perform_code d, void * arg)
```

Internal method. 



**Since:** Haiku R1


Reimplemented from [BLooper](classBLooper.md#adfc642544ce22888d412e6a4be25fa72).

---

### `Pulse()`

```cpp
void BApplication::Pulse()
```

Hook method that gets invoked when the [BApplication](classBApplication.md) receives a `B_PULSE` message. 


An action is performed each time app_server calls the [Pulse()](classBApplication.md#abf9de9bc0de3a8c504a4174f34ed82b4) method. The pulse rate is set by [SetPulseRate()](classBApplication.md#a565e7ede16cd6a0e7df384c3c97ba860). You can implement [Pulse()](classBApplication.md#abf9de9bc0de3a8c504a4174f34ed82b4) to do anything you want. The default version does nothing. The pulse granularity is no better than once per 100,000 microseconds.



**See also:** [SetPulseRate()](classBApplication.md#a565e7ede16cd6a0e7df384c3c97ba860)



**Since:** BeOS R3

---

### `Quit()`

```cpp
void BApplication::Quit()
```

Tells the thread to finish processing the message queue, disallowing any new messages. 


[Quit()](classBApplication.md#abd8cb94d425105f89bf9e18f01552015) doesn't kill the looper thread. After [Quit()](classBApplication.md#abd8cb94d425105f89bf9e18f01552015) returns, it doesn't wait for the message queue to empty. [Run()](classBApplication.md#a3fd11f52918b337f01eab978e8a56bad) will be then able to return.


[Quit()](classBApplication.md#abd8cb94d425105f89bf9e18f01552015) doesn't delete the [BApplication](classBApplication.md) object after [Run()](classBApplication.md#a3fd11f52918b337f01eab978e8a56bad) is called. You should delete the [BApplication](classBApplication.md) object yourself one [Run()](classBApplication.md#a3fd11f52918b337f01eab978e8a56bad) returns. However [Quit()](classBApplication.md#abd8cb94d425105f89bf9e18f01552015) does delete the object if it's called before the message loop starts i.e. before [Run()](classBApplication.md#a3fd11f52918b337f01eab978e8a56bad) is called.



**Since:** BeOS R3


Reimplemented from [BLooper](classBLooper.md#a10d5a4873f14fd247890a6dfc9b8b949).

---

### `QuitRequested()`

```cpp
bool BApplication::QuitRequested()
```

Hook method that gets invoked when the [BApplication](classBApplication.md) receives a `B_QUIT_REQUESTED` message. 


[BApplication](classBApplication.md) sends a [QuitRequested()](classBApplication.md#a4965aea57452c88022f0fdba2af65e0a) message to each of its [BWindow](../interface_kit/classBWindow.md) objects. If all of the [BWindow](../interface_kit/classBWindow.md) s return `true` then the windows are each destroyed (through [BWindow::Quit()](../interface_kit/classBWindow.md#a054c0206836014dcc20c59e50bceab44)) and [QuitRequested()](classBApplication.md#a4965aea57452c88022f0fdba2af65e0a) returns `true`. If any of the [BWindow](../interface_kit/classBWindow.md) returns `false`, the [BWindow](../interface_kit/classBWindow.md) s are not destroyed and [QuitRequested()](classBApplication.md#a4965aea57452c88022f0fdba2af65e0a) returns `false`.



**Returns:** `true` if the application quit or `false` if the application failed to quit.



**Since:** BeOS R3


Reimplemented from [BLooper](classBLooper.md#aff7aaf066538383f0e0ea28d18eb8863).

---

### `ReadyToRun()`

```cpp
void BApplication::ReadyToRun()
```

Hook method that's invoked when the [BApplication](classBApplication.md) receives a `B_READY_TO_RUN` message. 


The [ReadyToRun()](classBApplication.md#af912cef601090a89cc20cb3a7af48315) method is automatically called by the [Run()](classBApplication.md#a3fd11f52918b337f01eab978e8a56bad) method. It is sent after the initial `B_REFS_RECEIVED` and `B_ARGV_RECEIVED` messages (if any) have already been handled. [ReadyToRun()](classBApplication.md#af912cef601090a89cc20cb3a7af48315) is the only message that every running application is guaranteed to receive.


The default version of [ReadyToRun()](classBApplication.md#af912cef601090a89cc20cb3a7af48315) is empty. You should override the [ReadyToRun()](classBApplication.md#af912cef601090a89cc20cb3a7af48315) method to do whatever you want to do. If you haven't constructed any windows in your application yet then this would be a good place to do so.



**Since:** BeOS R3

---

### `RefsReceived()`

```cpp
void BApplication::RefsReceived(BMessage * message)
```

Hook method that gets invoked when the application receives a `B_REFS_RECEIVED` message. 


The message is sent in response to a user action such as a user drag-and-dropping a file on your app's icon or opening a file that the application is set to handle. You can use the [IsLaunching()](classBApplication.md#a49c3d8c8521a1b931f45fdcbaedb3f2d) method to discern whether the message arrived when the application is launched or after the application has already been running.


The default implementation is empty. You can override this method to do something with the received refs. Typically you create [BEntry](../storage_kit/classBEntry.md) or [BFile](../storage_kit/classBFile.md) objects from the passed in refs.


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | contains a single field named "be:refs" that contains one or more [entry_ref](../storage_kit/structentry__ref.md) (`B_REF_TYPE`) items, one for each file sent. |





**Since:** BeOS R3

---

### `RegisterLooper()`

```cpp
status_t BApplication::RegisterLooper(BLooper * looper)
```

Register a looper to quit when the application quits. 


There are situations where you create [BLooper](classBLooper.md) objects, that you may want to have [BApplication](classBApplication.md) quit properly, when the application is quitting. This method allows you to add Loopers under management of [BApplication](classBApplication.md).


Note that Windows are automatically handled by [BApplication](classBApplication.md), so there is no need to manually register BWindow-based loopers using this method.



**Returns:** `B_OK` when the looper was registered without an issue, `B_BAD_VALUE` when you try to register a [BWindow](../interface_kit/classBWindow.md), or `B_ERROR` when the looper was already registered.



**Since:** Haiku R1

---

### `ResolveSpecifier()`

```cpp
BHandler * BApplication::ResolveSpecifier(BMessage * message, int32 index, BMessage * specifier, int32 what, const char * property)
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


Reimplemented from [BLooper](classBLooper.md#a16b494160d9b37d4dbbc0d426a22c946).

---

### `Run()`

```cpp
thread_id BApplication::Run()
```

Starts the message loop in the thread that it is called from, and doesn't return until the message loop stops. 


[Run()](classBApplication.md#a3fd11f52918b337f01eab978e8a56bad) does not spawn a new thread.



**Returns:** The thread_id of the thread that the [BApplication](classBApplication.md) is called from.



**Since:** BeOS R3


Reimplemented from [BLooper](classBLooper.md#a88bb85410e0c4124bdc6f16168df4811).

---

### `SetCursor()`

```cpp
void BApplication::SetCursor(const BCursor * cursor, bool sync = true)
```

Sets the *cursor* to be used when the application is active with *sync* immediately option. 


The default BCursors to use are `B_CURSOR_SYSTEM_DEFAULT` for the hand cursor and `B_CURSOR_I_BEAM` for the I-beam cursor.


Parameters

| Parameter | Description |
| :--- | :--- |
| `cursor` | A [BCursor](classBCursor.md) object to set the *cursor* to. |
| `sync` | synchronize the cursor immediately. |





**Since:** BeOS R5

---

### `SetCursor()`

```cpp
void BApplication::SetCursor(const void * cursor)
```

Sets the *cursor* to be used when the application is active. 


You can pass one of the pre-defined cursor constants such as `B_HAND_CURSOR` or `B_I_BEAM_CURSOR` or you can create your own pass in your own cursor image. The cursor data format is described in the [BCursor](classBCursor.md) class.


Parameters

| Parameter | Description |
| :--- | :--- |
| `cursor` | The cursor data to set the cursor to. |





**Since:** BeOS R3

---

### `SetPulseRate()`

```cpp
void BApplication::SetPulseRate(bigtime_t rate)
```

Sets the interval that the `B_PULSE` messages are sent. 


If the *rate* is set to 0 then the `B_PULSE` messages are not sent. The pulse rate can be no faster than once per 100,000 microseconds or so.


Parameters

| Parameter | Description |
| :--- | :--- |
| `rate` | The rate at which `B_PULSE` messages are sent to the application. |





**Since:** BeOS R3

---

### `ShowCursor()`

```cpp
BApplication::ShowCursor()
```

Restores the cursor. 



**Since:** BeOS R3

---

### `Signature()`

```cpp
const char * BApplication::Signature()const
```

Returns the signature of the Application. 



**Since:** Haiku R1

---

### `UnregisterLooper()`

```cpp
status_t BApplication::UnregisterLooper(BLooper * looper)
```

Remove a previously registered Looper from the quit-list. 


If a looper has been added to the quit list using [BApplication::RegisterLooper](classBApplication.md#a2b46141e108da1167be0d3427ca37716), they can be unregistered using this method. You should do this in the case the looper quits before the application does.


Note that Windows are automatically handled by [BApplication](classBApplication.md), so you don't have to use this function to unregister windows.



**Returns:** `B_OK` when the looper has been removed, `B_BAD_VALUE` when you try to unregister a [BWindow](../interface_kit/classBWindow.md), or `B_ERROR` when the looper was not previously registered.



**Since:** Haiku R1

---

### `WindowAt()`

```cpp
BWindow * BApplication::WindowAt(int32 index)const
```

Returns the [BWindow](../interface_kit/classBWindow.md) object at the specified *index* in the application's window list. 


If *index* is out of range, this function returns `NULL`.



> [!WARNING]
> Locking the [BApplication](classBApplication.md) object doesn't lock the window list.


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The *index* of the desired [BWindow](../interface_kit/classBWindow.md). |





**Returns:** The [BWindow](../interface_kit/classBWindow.md) object at the specified *index* or `NULL` if the *index* is out of range.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBApplication.html).
