---
name: BInvoker
type: class
kit: application_kit
brief: "An object that can be \"invoked\" to send a message to a BHandler"
source: haiku-book
---

# BInvoker Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

An object that can be "invoked" to send a message to a [BHandler](classBHandler.md). 


The designated [BHandler](classBHandler.md) of a [BInvoker](classBInvoker.md) is known as its "target".


[BInvoker](classBInvoker.md) is most often used as a mix-in class, for example, [BControl](../interface_kit/classBControl.md) derives from [BInvoker](classBInvoker.md) as well as from [BView](../interface_kit/classBView.md).



**See also:** [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c)



**Since:** BeOS R3

## Member List

### Public Member Functions

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

* `void` [BeginInvokeNotify](#ada272cb8671448d7f7efd607791f31a7) (uint32 kind=B_CONTROL_INVOKED) — Implement this method to set up an InvokeNotify() context.
* `void` [EndInvokeNotify](#a2169cfbba1c3da1921baa9a550581b54) () — Implement this method to tear down an InvokeNotify() context.
* `uint32` [InvokeKind](#a6e33e81c7ee307621295e8da6181d3f8) (bool *_notify=NULL) — Returns the kind set by InvokeNotify().

## Detailed Member Documentation

### `BInvoker()`

```cpp
BInvoker::BInvoker()
```

Initializes a [BInvoker](classBInvoker.md) without a message or target. 


You must call [SetTarget()](classBInvoker.md#ac857ceb882d95a5826447dc12dd06c74) to set the invoker's target before calling [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c) for the message to be sent.


You may call [SetMessage()](classBInvoker.md#a42fae8f984af3765c1a6af404dc36816) to set the message to send when calling [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c), alternatively you may pass a [BMessage](classBMessage.md) to [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c) each time you call it.



**See also:** [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c)



**Since:** BeOS R3

---

### `BInvoker()`

```cpp
BInvoker::BInvoker(BMessage * message, const BHandler * handler, const BLooper * looper = NULL)
```

Initializes the [BInvoker](classBInvoker.md) with *message* and sets the target to either a local *handler* or as the preferred handler of a local *looper* where the message is sent when [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c) is called. 



> [!NOTE]
> It is not necessary to specify both the *handler* and the *looper*, the unused parameter should be passed in as `NULL`.



**See also:** [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c)



**Since:** BeOS R3

---

### `BInvoker()`

```cpp
BInvoker::BInvoker(BMessage * message, BMessenger messenger)
```

Initializes the [BInvoker](classBInvoker.md) with *message* and sets the target *messenger* where the message is sent when [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c) is called. 


A [BMessenger](classBMessenger.md) can target either local or remote objects.



**See also:** [SetMessage()](classBInvoker.md#a42fae8f984af3765c1a6af404dc36816) for details.



**Since:** BeOS R3

---

### `~BInvoker()`

```cpp
BInvoker::~BInvoker()
```

Destructor method, deletes the [BMessage](classBMessage.md) object if set. 



**Since:** BeOS R3

---

### `BeginInvokeNotify()`

```cpp
void BInvoker::BeginInvokeNotify(uint32 kind = B_CONTROL_INVOKED)
```

Implement this method to set up an [InvokeNotify()](classBInvoker.md#ab009fe9c6a1f64798c614612e8c3db20) context. 


This is used by derive classes to emulate an [InvokeNotify()](classBInvoker.md#ab009fe9c6a1f64798c614612e8c3db20) call inside of [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c) without breaking binary compatibility.



**Since:** BeOS R5

---

### `Command()`

```cpp
uint32 BInvoker::Command()const
```

Returns the message's `what` data member. 



> [!NOTE]
> If a message has not been assigned to the invoker this method returns `0` instead.



**Since:** BeOS R3

---

### `EndInvokeNotify()`

```cpp
void BInvoker::EndInvokeNotify()
```

Implement this method to tear down an [InvokeNotify()](classBInvoker.md#ab009fe9c6a1f64798c614612e8c3db20) context. 



**Since:** BeOS R5

---

### `HandlerForReply()`

```cpp
BHandler * BInvoker::HandlerForReply()const
```

Returns the previously set reply handler or `NULL` if not set. 



**Since:** BeOS R3

---

### `Invoke()`

```cpp
status_t BInvoker::Invoke(BMessage * message = NULL)
```

Sends the *message* to the invoker's target. 


If *message* is `NULL` the default message is sent instead. You can set the default message using *SetMessage* or in the constructor.


This method also sends a B_CONTROL_INVOKED notification to handlers which registered themselves using StartWatching



**Since:** BeOS R3


Reimplemented in [BButton](../interface_kit/classBButton.md#ad9942f380f9e8337147f307972e02a9b), [BChannelControl](../interface_kit/classBChannelControl.md#a29dcbf2de885c423dc2981c95b225691), [BCheckBox](../interface_kit/classBCheckBox.md#a90978d140f092824dc9aeff535bd8638), [BColorControl](../interface_kit/classBColorControl.md#a40cd8db37322ffb2770896ded8ec1600), [BControl](../interface_kit/classBControl.md#afa04e938d3c42b1de43baa48edb8fd3e), [BListView](../interface_kit/classBListView.md#a88701bff61aeb58857ca33a5a8920e40), [BMenuItem](../interface_kit/classBMenuItem.md#ae51fbc9628a915b133b5862e436314a4), [BPictureButton](../interface_kit/classBPictureButton.md#ad3f58a97ed8348711aff7128ebf0b5dd), [BRadioButton](../interface_kit/classBRadioButton.md#ae0aec96932eaa5f1de8591392a739b0b), and [BTextControl](../interface_kit/classBTextControl.md#ae82b482d40833e4a2903301839e37f8c).

---

### `InvokeKind()`

```cpp
uint32 BInvoker::InvokeKind(bool * _notify = NULL)
```

Returns the kind set by [InvokeNotify()](classBInvoker.md#ab009fe9c6a1f64798c614612e8c3db20). 


Derived classes should implement this method and call it from within [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c) to determine what kind was specified when [InvokeNotify()](classBInvoker.md#ab009fe9c6a1f64798c614612e8c3db20) was called.


If you care whether [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c) or [InvokeNotify()](classBInvoker.md#ab009fe9c6a1f64798c614612e8c3db20) was originally called, you can use a bool pointer and set its value to `true` if [InvokeNotify()](classBInvoker.md#ab009fe9c6a1f64798c614612e8c3db20) was called, or `false` if [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c) was called. This lets you fetch the [InvokeNotify()](classBInvoker.md#ab009fe9c6a1f64798c614612e8c3db20) arguments from [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c) without breaking binary compatibility with older applications.



**Since:** BeOS R5

---

### `InvokeNotify()`

```cpp
status_t BInvoker::InvokeNotify(BMessage * message, uint32 kind = B_CONTROL_INVOKED)
```

Sends the *message* to its target, using the notification code specified by *kind*. 


If message is `NULL`, no message is sent to the target, but any watchers of the invoker's handler will receive their expected notifications. By default, *kind* is `B_CONTROL_INVOKED`, the same as sent by [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c).


[BInvoker](classBInvoker.md) does not send the notification itself, it is up to subclasses to do that as needed.



**See also:** [BLooper::StartWatching()](classBHandler.md#af7d600e33a0586af7444d9abc8500504)



**Since:** BeOS R5

---

### `IsTargetLocal()`

```cpp
bool BInvoker::IsTargetLocal()const
```

Returns whether or not the invoker and its target belong to the same team. 



**Returns:** `true` if the invoker and its target are in the same team, `false` if they reside in separate address spaces.



**Since:** BeOS R3

---

### `Message()`

```cpp
BMessage * BInvoker::Message()const
```

Returns a pointer to the invoker's message object. 



> [!NOTE]
> If a message has not been assigned to the invoker this method returns `NULL` instead.



**Since:** BeOS R3

---

### `Messenger()`

```cpp
BMessenger BInvoker::Messenger()const
```

Returns the [BMessenger](classBMessenger.md) object that the invoker uses to send its messages. 


If a target hasn't been set yet, the returned [BMessenger](classBMessenger.md) object will be invalid.



**See also:** [BMessenger::IsValid()](classBMessenger.md#a0094e94e04aacad5a8d5a0c3988be300)



**Since:** BeOS R3

---

### `SetHandlerForReply()`

```cpp
status_t BInvoker::SetHandlerForReply(BHandler * replyHandler)
```

Sets the [BHandler](classBHandler.md) object responsible for handling reply messages. 


When [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c) is called, the *replyHandler* is passed to the messenger's SendMessage() method, as follows:



```cpp
messenger->SendMessage(message, replyHandler);
```

By default, the handler for replies is `NULL`, consequently all reply messages will be sent to the [BApplication](classBApplication.md) instead.



**Returns:** Always returns `B_OK`.



**Since:** BeOS R3

---

### `SetMessage()`

```cpp
status_t BInvoker::SetMessage(BMessage * message)
```

Assigns *message* to the invoker, deleting any previously assigned message. 


You may pass `NULL` into *message* to delete the current message without replacing it.


When [Invoke()](classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c) is called with a `NULL` message parameter, a copy of the passed in *message* is sent to the target [BHandler](classBHandler.md). [BInvoker](classBInvoker.md) takes ownership of the [BMessage](classBMessage.md) object, so you must not delete it yourself.



**Since:** BeOS R3

---

### `SetTarget()`

```cpp
status_t BInvoker::SetTarget(BMessenger messenger)
```

Sets the invoker's target to *messenger*. 


A [BMessenger](classBMessenger.md) target can be used to designate a remote handler (living in another team).



**Since:** BeOS R3

---

### `SetTarget()`

```cpp
status_t BInvoker::SetTarget(const BHandler * handler, const BLooper * looper = NULL)
```

Sets the target to either a local *handler* or as the preferred handler of a local *looper*. 



> [!NOTE]
> It is not necessary to specify both the *handler* and the *looper*, the unused parameter should be passed in as `NULL`.


If given only a *handler*, it must already be attached to a [BLooper](classBLooper.md).


If given only a *looper*, the message will be sent to its preferred handler (in the case of a [BWindow](../interface_kit/classBWindow.md) that is the focused view).



**Since:** BeOS R3

---

### `SetTimeout()`

```cpp
status_t BInvoker::SetTimeout(bigtime_t timeout)
```

Sets the timeout to use when sending the message to the target. 


By default the timeout is set to `B_INFINITE_TIMEOUT`. The *timeout* value is passed into the timeout parameter of [BMessenger::SendMessage()](classBMessenger.md#aebe5aba546fa4a4696988b1bf6028f3c).



**See also:** BMessenger::SendMessage(BMessage*, BHandler*, bigtime_t) for details.



**Since:** BeOS R5

---

### `Target()`

```cpp
BHandler * BInvoker::Target(BLooper ** _looper = NULL)const
```

Invoke [BMessenger::Target()](classBMessenger.md#a763e36f482699e201795a04b39aabf1a) on the internal messenger. 



**See also:** [BMessenger::Target()](classBMessenger.md#a763e36f482699e201795a04b39aabf1a)



**Since:** BeOS R3

---

### `Timeout()`

```cpp
bigtime_t BInvoker::Timeout()const
```

Returns the current timeout value. 



**Since:** BeOS R5

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBInvoker.html).
