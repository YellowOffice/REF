---
name: BMessageRunner
type: class
kit: application_kit
brief: "Provides a mechanism for sending one or more messages to a messenger at a specified interval and receive reply messages"
source: haiku-book
---

# BMessageRunner Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Provides a mechanism for sending one or more messages to a messenger at a specified interval and receive reply messages. 


The application that creates the [BMessageRunner](classBMessageRunner.md) can specify the message, the [BMessenger](classBMessenger.md) to send the message to, how often to send the message, how many times to send the message, and the [BMessenger](classBMessenger.md) to send reply messages from.


The system roster handles dispatching the messages to the appropriate messengers at the specified time intervals. The target for any reply messages is `be_app_messenger` by default, or it can be specified in the constructor.


After initializing a [BMessageRunner](classBMessageRunner.md), the initialization can and should be checked by calling [InitCheck()](classBMessageRunner.md#a495c20a458d090edcd4d952abe41311e). [BMessageRunner](classBMessageRunner.md) will not take ownership of the message, you may freely change or delete the message after initialization.


The [BMessageRunner](classBMessageRunner.md) can be reconfigured (to change the interval or count) by calling [SetInterval()](classBMessageRunner.md#ab9e13888044ee17bc57727b05c104c73) and [SetCount()](classBMessageRunner.md#a6a37e56fa7938d946f2d5580bf9a4a3e). This is useful if you want to stop a [BMessageRunner](classBMessageRunner.md) from sending messages early or if messages are set to be sent forever.



**Since:** BeOS R5

## Member List

### Public Member Functions

* [BMessageRunner](#a41ea90009b9f038a3146ab5c7cbe5d4f) (BMessenger target, const BMessage &message, bigtime_t interval, int32 count, BMessenger replyTo) — Creates and initializes a new BMessageRunner and instructs the system roster to send the specified message to the target count times every interval microseconds.
* [BMessageRunner](#a3d78a38af76e15670808fa2761208dd3) (BMessenger target, const BMessage &message, bigtime_t interval, int32 count=-1) — Creates and initializes a new BMessageRunner and instructs the system roster to send the specified message to the target count times every interval microseconds, reply messages are sent to be_app_messenger.
* [BMessageRunner](#ad484c095eeda712b88c6e958cae1449c) (BMessenger target, const BMessage *message, bigtime_t interval, int32 count, BMessenger replyTo) — Creates and initializes a new BMessageRunner and instructs the system roster to send the specified message to the target count times every interval microseconds.
* [BMessageRunner](#a7297d589c21956749b131e12c1851a99) (BMessenger target, const BMessage *message, bigtime_t interval, int32 count=-1) — Creates and initializes a new BMessageRunner and instructs the system roster to send the specified message to the target count times every interval microseconds, reply messages are sent to be_app_messenger.
* `virtual` [~BMessageRunner](#a7df5fa65c8abdeb371f49c4d4401c6a4) () — Frees all resources associated with the object.
* `status_t` [GetInfo](#a18060e7228d1e35b1511421d8da0bf21) (bigtime_t *interval, int32 *count) const — Returns the time interval between two messages and the number of times the message has still to be sent.
* `status_t` [InitCheck](#a495c20a458d090edcd4d952abe41311e) () const — Returns the initialization status.
* `status_t` [SetCount](#a6a37e56fa7938d946f2d5580bf9a4a3e) (int32 count) — Sets the number of times message should be sent.
* `status_t` [SetInterval](#ab9e13888044ee17bc57727b05c104c73) (bigtime_t interval) — Sets the interval of time between messages.

### Static Public Member Functions

* `static status_t` [StartSending](#ae161adabfc1b87ec78ee38b7563d87ef) (BMessenger target, const BMessage *message, bigtime_t interval, int32 count) — Creates and initializes a detached BMessageRunner and instructs the system roster to send the specified message to the target count times every interval microseconds, reply messages are sent to be_app_messenger.
* `static status_t` [StartSending](#ad1c3fcfc9787b60c61a7704f268722cc) (BMessenger target, const BMessage *message, bigtime_t interval, int32 count, BMessenger replyTo) — Creates and initializes a detached BMessageRunner and instructs the system roster to send the specified message to the target count times every interval microseconds.

## Detailed Member Documentation

### `BMessageRunner()`

```cpp
BMessageRunner::BMessageRunner(BMessenger target, const BMessage * message, bigtime_t interval, int32 count = -1)
```

Creates and initializes a new [BMessageRunner](classBMessageRunner.md) and instructs the system roster to send the specified *message* to the *target* *count* times every *interval* microseconds, reply messages are sent to `be_app_messenger`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | The target of the message(s). |
| `message` | The message to be sent to the target. |
| `interval` | Period of time before the first message is sent and between messages (if more than one shall be sent) in microseconds. |
| `count` | Specifies how many times the message shall be sent. A negative value indicates that the message will be sent forever, or until the [BMessageRunner](classBMessageRunner.md) is reconfigured or deleted. |





**Since:** BeOS R5

---

### `BMessageRunner()`

```cpp
BMessageRunner::BMessageRunner(BMessenger target, const BMessage & message, bigtime_t interval, int32 count = -1)
```

Creates and initializes a new [BMessageRunner](classBMessageRunner.md) and instructs the system roster to send the specified *message* to the *target* *count* times every *interval* microseconds, reply messages are sent to `be_app_messenger`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | Target of the message(s). |
| `message` | The message to be sent to the target. |
| `interval` | Period of time before the first message is sent and between messages (if more than one shall be sent) in microseconds. |
| `count` | Specifies how many times the message shall be sent. A negative value indicates that the message will be sent forever, or until the [BMessageRunner](classBMessageRunner.md) is reconfigured or deleted. |





**Since:** Haiku R1

---

### `BMessageRunner()`

```cpp
BMessageRunner::BMessageRunner(BMessenger target, const BMessage * message, bigtime_t interval, int32 count, BMessenger replyTo)
```

Creates and initializes a new [BMessageRunner](classBMessageRunner.md) and instructs the system roster to send the specified *message* to the *target* *count* times every *interval* microseconds. 


This constructor also allows you to specify the target for replies to the delivered messages.


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | Target of the message(s). |
| `message` | The message to be sent to the target. |
| `interval` | Period of time before the first message is sent and between messages (if more than one shall be sent) in microseconds. |
| `count` | Specifies how many times the message shall be sent. A negative value indicates that the message will be sent forever, or until the [BMessageRunner](classBMessageRunner.md) is reconfigured or deleted. |
| `replyTo` | Target replies to the delivered message(s) shall be sent to. |





**Since:** BeOS R5

---

### `BMessageRunner()`

```cpp
BMessageRunner::BMessageRunner(BMessenger target, const BMessage & message, bigtime_t interval, int32 count, BMessenger replyTo)
```

Creates and initializes a new [BMessageRunner](classBMessageRunner.md) and instructs the system roster to send the specified *message* to the *target* *count* times every *interval* microseconds. 


This constructor also allows you to specify the target for replies to the delivered messages.


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | Target of the message(s). |
| `message` | The message to be sent to the target. |
| `interval` | Period of time before the first message is sent and between messages (if more than one shall be sent) in microseconds. |
| `count` | Specifies how many times the message shall be sent. A negative value indicates that the message will be sent forever, or until the [BMessageRunner](classBMessageRunner.md) is reconfigured or deleted. |
| `replyTo` | Target replies to the delivered message(s) shall be sent to. |





**Since:** Haiku R1

---

### `~BMessageRunner()`

```cpp
BMessageRunner::~BMessageRunner()
```

Frees all resources associated with the object. 



**Since:** BeOS R5

---

### `GetInfo()`

```cpp
status_t BMessageRunner::GetInfo(bigtime_t * interval, int32 * count)const
```

Returns the time interval between two messages and the number of times the message has still to be sent. 


Both parameters (*interval* and *count*) may be `NULL`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `interval` | Pointer to a pre-allocated bigtime_t variable to be set to the time interval. May be `NULL`. |
| `count` | Pointer to a pre-allocated int32 variable to be set to the number of times the message has still to be sent. May be `NULL`. |





**Returns:** A status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *interval* was 0 or negative, or the message runner had already sent all messages and became unusable. |





**Since:** BeOS R5

---

### `InitCheck()`

```cpp
status_t BMessageRunner::InitCheck()const
```

Returns the initialization status. 



> [!NOTE]
> As soon as the last message is sent, the message runner becomes unusable. [InitCheck()](classBMessageRunner.md#a495c20a458d090edcd4d952abe41311e) will still return `B_OK`, but [SetInterval()](classBMessageRunner.md#ab9e13888044ee17bc57727b05c104c73), [SetCount()](classBMessageRunner.md#a6a37e56fa7938d946f2d5580bf9a4a3e) and [GetInfo()](classBMessageRunner.md#a18060e7228d1e35b1511421d8da0bf21) will all fail.



**Returns:** `B_OK` if the object was properly initialized or an error code otherwise.



**Since:** BeOS R5

---

### `SetCount()`

```cpp
status_t BMessageRunner::SetCount(int32 count)
```

Sets the number of times message should be sent. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `count` | Specifies how many times the message shall be sent. A negative value indicates that the message will be sent forever, or until the [BMessageRunner](classBMessageRunner.md) is reconfigured or deleted. |





**Returns:** A status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The message runner was not properly initialized. |
| B_BAD_VALUE | *interval* was `0` or negative, or the message runner had already sent all messages and became unusable. |





**Since:** BeOS R5

---

### `SetInterval()`

```cpp
status_t BMessageRunner::SetInterval(bigtime_t interval)
```

Sets the interval of time between messages. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `interval` | The new interval in microseconds. |





**Returns:** A status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_NO_INIT | The message runner was not properly initialized. |
| B_BAD_VALUE | *interval* was `0` or negative, or the message runner had already sent all messages and became unusable. |





**Since:** BeOS R5

---

### `StartSending()`

```cpp
status_t BMessageRunner::StartSending(BMessenger target, const BMessage * message, bigtime_t interval, int32 count)
```

Creates and initializes a detached [BMessageRunner](classBMessageRunner.md) and instructs the system roster to send the specified *message* to the *target* *count* times every *interval* microseconds, reply messages are sent to `be_app_messenger`. 


You cannot alter the runner after the creation, and it will be deleted automatically the last message is sent.


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | Target of the message(s). |
| `message` | The message to be sent to the target. |
| `interval` | Period of time before the first message is sent and between messages (if more than one shall be sent) in microseconds. |
| `count` | Specifies how many times the message shall be sent. A negative value indicates that the message will be sent forever, or until the [BMessageRunner](classBMessageRunner.md) is reconfigured or deleted. |





**Since:** Haiku R1

---

### `StartSending()`

```cpp
status_t BMessageRunner::StartSending(BMessenger target, const BMessage * message, bigtime_t interval, int32 count, BMessenger replyTo)
```

Creates and initializes a detached [BMessageRunner](classBMessageRunner.md) and instructs the system roster to send the specified *message* to the *target* *count* times every *interval* microseconds. 


You cannot alter the runner after the creation, and it will be deleted automatically once the last message is sent.


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | Target of the message(s). |
| `message` | The message to be sent to the target. |
| `interval` | Period of time before the first message is sent and between messages (if more than one shall be sent) in microseconds. |
| `count` | Specifies how many times the message shall be sent. A negative value indicates that the message will be sent forever, or until the [BMessageRunner](classBMessageRunner.md) is reconfigured or deleted. |
| `replyTo` | Target replies to the delivered message(s) shall be sent to. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMessageRunner.html).
