---
name: BMessenger
type: class
kit: application_kit
brief: "A class to send messages to a target BLooper or BHandler"
source: haiku-book
---

# BMessenger Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A class to send messages to a target [BLooper](classBLooper.md) or [BHandler](classBHandler.md). 


A [BMessenger](classBMessenger.md) can send messages to local and remote targets. If the target belongs to the same team as the [BMessenger](classBMessenger.md) it is a local target, otherwise if the target lives in a separate address space it is a remote target.


The most significant (set of) method(s) in the class is [SendMessage()](classBMessenger.md#aebe5aba546fa4a4696988b1bf6028f3c), which sends its message to the target. For a local target [SendMessage()](classBMessenger.md#aebe5aba546fa4a4696988b1bf6028f3c) is roughly equivalent in terms of efficiency to posting a message directly to the messenger's target (i.e. [BLooper::PostMessage()](classBLooper.md#a0de6737bfbf8a8b4913adc8c74bb544e)).


If you supply a target [BMessenger](classBMessenger.md) or [BHandler](classBHandler.md) to [SendMessage()](classBMessenger.md#aebe5aba546fa4a4696988b1bf6028f3c) the method will return immediately after delivery and the response will be handled asynchronously, otherwise the method will return once the reply has been delivered or after a set timeout.


The global *be_app_messenger* pointer targets the main message loop of *be_app* is automatically initialized for you when you create a [BApplication](classBApplication.md) object, you can use it wherever a [BMessenger](classBMessenger.md) is called for.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BMessenger](#a369f2de1289d74e8459d1c04ace3caa7) () — Creates an uninitialized BMessenger.
* [BMessenger](#a48dceac75712d5cd8853d62d031e4dd1) (const BHandler *handler, const BLooper *looper=NULL, status_t *result=NULL) — Creates a BMessenger and initializes it to target the local BHandler and/or BLooper.
* [BMessenger](#a8357653912eb9acce80ff4fb9011d0c8) (const BMessenger &other) — Creates a BMessenger and initializes it to have the same target as the supplied messenger.
* [BMessenger](#a9a97e301b9c9cabb816a9b74e94ff237) (const char *signature, team_id team=-1, status_t *result=NULL) — Creates a BMessenger and initializes it to target the already running application identified by its signature and/or team ID.
* [~BMessenger](#ab5c0b585a6d49d4f3ae84356401ea075) () — Frees all resources associated with this object.
* `uint32` [HashValue](#a34e4ce5acb6251a5691e328e02977a91) () const — Returns a hash value that uniquely identifies the messenger.
* `bool` [IsValid](#a0094e94e04aacad5a8d5a0c3988be300) () const — Returns whether the messenger's target looper still exists.
* `team_id` [Team](#abf7a4bbb4d1480efcfead072f598bafa) () const — Returns the ID of the team that the messenger's target belongs to.
* `bool` [IsTargetLocal](#ac0b8b1360dd6ed6c0edf8def5ef390b7) () const — Returns whether the messenger and target belong to the same team.
* `BHandler *` [Target](#a763e36f482699e201795a04b39aabf1a) (BLooper **looper) const — Returns the handler and looper targeted by the messenger (if the target is local).
* `bool` [LockTarget](#a2a5eecda17bf16a4981db49a0d5773f1) () const — Locks the BLooper targeted by the messenger (if the target is local).
* `status_t` [LockTargetWithTimeout](#ab568c74c5ea2be4a5c684613f9116505) (bigtime_t timeout) const — Locks the BLooper targeted by the messenger with a timeout (if the target is local).
* `status_t` [SendMessage](#aebe5aba546fa4a4696988b1bf6028f3c) (uint32 command, BHandler *replyTo=NULL) const — Delivers a BMessage with command what identifier to the messenger's target. A response may be sent to the replyTo handler asynchronously.
* `status_t` [SendMessage](#afee0227707703adc712c2b8e4064d45a) (BMessage *message, BHandler *replyTo=NULL, bigtime_t timeout=B_INFINITE_TIMEOUT) const — Delivers a message to the messenger's target. A response message may be sent back to the replyTo handler asynchronously.
* `status_t` [SendMessage](#ad1ac7efa3b7193245908adc7f293fb93) (BMessage *message, BMessenger replyTo, bigtime_t timeout=B_INFINITE_TIMEOUT) const — Delivers a message to the messenger's target. A response message may be sent back to the replyTo messenger's target asynchronously.
* `status_t` [SendMessage](#a3d305370d4df56903c881cf083a655ca) (uint32 command, BMessage *reply) const — Delivers a BMessage with command what identifier to the messenger's target and waits for a reply BMessage synchronously.
* `status_t` [SendMessage](#a18c896b7957702a5b44a080300ab7cef) (BMessage *message, BMessage *reply, bigtime_t deliveryTimeout=B_INFINITE_TIMEOUT, bigtime_t replyTimeout=B_INFINITE_TIMEOUT) const — Delivers a message to the messenger's target and waits for a reply to come back synchronously.
* `status_t` [SetTo](#a24f7642b053481247cdbaa17068f38f6) (const char *signature, team_id team=-1) — Reinitializes a BMessenger to target the already running application identified by the supplied signature and/or team ID.
* `status_t` [SetTo](#ad7a2b0adc3affbdad8090308ec8e1892) (const BHandler *handler, const BLooper *looper=NULL) — Reinitializes a BMessenger to target the local BHandler and/or BLooper.
* `BMessenger &` [operator=](#afc7c0f773cff59935505bf5d57c82f2b) (const BMessenger &other) — Assignment operator, makes this BMessenger a copy of other.
* `bool` [operator==](#ac5227eb37527e0fb53ecfad6a95cc1bd) (const BMessenger &other) const — Comparison operator, returns whether this and other have the same target.

## Detailed Member Documentation

### `BMessenger()`

```cpp
BMessenger::BMessenger()
```

Creates an uninitialized [BMessenger](classBMessenger.md). 



**Since:** BeOS R3

---

### `BMessenger()`

```cpp
BMessenger::BMessenger(const char * signature, team_id team = -1, status_t * result = NULL)
```

Creates a [BMessenger](classBMessenger.md) and initializes it to target the already running application identified by its signature and/or team ID. 


When only a *signature* is given, and multiple instances of the application are running it is indeterminate which one is chosen as the target. In case only a *team* ID is passed, the target application is identified uniquely. If both are supplied, the application identified by the *team* ID must have a matching signature, otherwise the initialization fails.


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | The target application's signature. May be `NULL`. |
| `team` | The target application's team ID. May be < 0. |
| `result` | An optional pointer to a pre-allocated status_t into which the result of the initialization is written. |





**Since:** BeOS R3

---

### `BMessenger()`

```cpp
BMessenger::BMessenger(const BHandler * handler, const BLooper * looper = NULL, status_t * _result = NULL)
```

Creates a [BMessenger](classBMessenger.md) and initializes it to target the local [BHandler](classBHandler.md) and/or [BLooper](classBLooper.md). 


When a `NULL` *handler* is supplied, the preferred handler in the *looper* is targeted. If no *looper* is supplied the looper that *handler* belongs to is used instead – that means in particular, that the *handler* must already belong to a looper. If both are supplied the *handler* must belong to the *looper*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `handler` | The target handler. May be `NULL`. |
| `looper` | The target looper. May be `NULL`. |
| `_result` | An optional pointer to a pre-allocated status_t into which the result of the initialization is written. |





**Since:** BeOS R3

---

### `BMessenger()`

```cpp
BMessenger::BMessenger(const BMessenger & other)
```

Creates a [BMessenger](classBMessenger.md) and initializes it to have the same target as the supplied messenger. 



**Since:** BeOS R3

---

### `~BMessenger()`

```cpp
BMessenger::~BMessenger()
```

Frees all resources associated with this object. 



**Since:** BeOS R3

---

### `HashValue()`

```cpp
uint32 BMessenger::HashValue()const
```

Returns a hash value that uniquely identifies the messenger. 



**Since:** Haiku R1

---

### `IsTargetLocal()`

```cpp
bool BMessenger::IsTargetLocal()const
```

Returns whether the messenger and target belong to the same team. 



**Returns:** `true` if the messenger is properly initialized and its target belong ot the same team, `false` if they reside in separate address spaces.



**Since:** BeOS R3

---

### `IsValid()`

```cpp
bool BMessenger::IsValid()const
```

Returns whether the messenger's target looper still exists. 



> [!WARNING]
> This method does not check whether the target handler also still exists.



**Returns:** `true`, if the messenger's target looper still exists, `false` otherwise.



**Since:** BeOS R3

---

### `LockTarget()`

```cpp
bool BMessenger::LockTarget()const
```

Locks the [BLooper](classBLooper.md) targeted by the messenger (if the target is local). 


This method is a shorthand for retrieving the targeted looper via [Target()](classBMessenger.md#a763e36f482699e201795a04b39aabf1a) and calling [BLooper::Lock()](classBLooper.md#a757a3e406ea3b7bb9a1ad16d04689b1d) on the looper afterwards.



**See also:** [BLooper::Lock()](classBLooper.md#a757a3e406ea3b7bb9a1ad16d04689b1d) for details.



**Returns:** `true`, if the looper was locked successfully, `false`, if the messenger was not properly initialized, the target was remote, or the targeted looper was invalid.



**Since:** BeOS R3

---

### `LockTargetWithTimeout()`

```cpp
status_t BMessenger::LockTargetWithTimeout(bigtime_t timeout)const
```

Locks the [BLooper](classBLooper.md) targeted by the messenger with a *timeout* (if the target is local). 


This method is a shorthand for retrieving the targeted looper via [Target()](classBMessenger.md#a763e36f482699e201795a04b39aabf1a) and calling [BLooper::LockWithTimeout()](classBLooper.md#a734cdb06bfe92efdea24528c9b43bfc1) on the looper afterwards.



**See also:** [BLooper::LockWithTimeout()](classBLooper.md#a734cdb06bfe92efdea24528c9b43bfc1) for details.



**Returns:** A status code, `B_OK` on success or an error code otherwise, all other error codes returned by [BLooper::LockWithTimeout()](classBLooper.md#a734cdb06bfe92efdea24528c9b43bfc1).


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | if the looper could be locked successfully, |
| B_BAD_VALUE | if the messenger is not properly initialized, the target is remote, or the targeted looper is invalid. |





**See also:** [BLooper::LockWithTimeout()](classBLooper.md#a734cdb06bfe92efdea24528c9b43bfc1) for more error codes.



**Since:** BeOS R3

---

### `operator=()`

```cpp
BMessenger & BMessenger::operator=(const BMessenger & other)
```

Assignment operator, makes this [BMessenger](classBMessenger.md) a copy of *other*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | the messenger to be copied. |





**Returns:** A reference to this object.



**Since:** BeOS R3

---

### `operator==()`

```cpp
bool BMessenger::operator==(const BMessenger & other)const
```

Comparison operator, returns whether this and *other* have the same target. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The messenger to be compared to. |





**Returns:** `true`, if the messengers have the same target or if both aren't properly initialized, `false` otherwise.



**Since:** BeOS R3

---

### `SendMessage()`

```cpp
status_t BMessenger::SendMessage(BMessage * message, BHandler * replyTo = NULL, bigtime_t timeout = B_INFINITE_TIMEOUT)const
```

Delivers a *message* to the messenger's target. A response message may be sent back to the *replyTo* handler asynchronously. 


A copy of the supplied message is sent and the caller retains ownership of *message*.


If the target's message port is full, the method waits until space becomes available in the port or the specified timeout occurs (whichever happens first). After delivery the method returns immediately. It does not wait until the target processes the message or even sends a reply.


This method does not return by default until the message has been delivered. You can set a delivery *timeout* in microseconds.


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The message to be sent. |
| `replyTo` | The handler for a response message to be sent. May be `NULL`. |
| `timeout` | The message delivery timeout in microseconds. (optional) |





**Returns:** A status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_PORT_ID | The messenger was not properly initialized or its target didn't exist. |
| B_WOULD_BLOCK | A delivery timeout of 0 was supplied and the target port was full when trying to deliver the message. |
| B_TIMED_OUT | The timeout expired while trying to deliver the message. |





**Since:** BeOS R3

---

### `SendMessage()`

```cpp
status_t BMessenger::SendMessage(BMessage * message, BMessage * reply, bigtime_t deliveryTimeout = B_INFINITE_TIMEOUT, bigtime_t replyTimeout = B_INFINITE_TIMEOUT)const
```

Delivers a *message* to the messenger's target and waits for a *reply* to come back synchronously. 


A copy of the supplied message is sent and the caller retains ownership of *message*.


The method does wait for a reply. The reply message is copied into *reply*. If the target doesn't send a reply or if a reply timeout occurs, the `what` field of *reply* is set to `B_NO_REPLY`.


This method does not return by default until the message has been delivered and the reply has come back. You can set a *deliveryTimeout* and a *replyTimeout* in microseconds.


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The message to be sent. |
| `reply` | A pointer to a pre-allocated [BMessage](classBMessage.md) which the reply message will be copied into. |
| `deliveryTimeout` | The message delivery timeout in microseconds. (optional) |
| `replyTimeout` | The reply message timeout in microseconds. (optional) |





**Returns:** A status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_PORT_ID | The messenger was not properly initialized or its target didn't exist. |
| B_WOULD_BLOCK | A delivery timeout of 0 was supplied and the target port was full when trying to deliver the message. |
| B_TIMED_OUT | The timeout expired while trying to deliver the message. |
| B_NO_MORE_PORTS | All reply ports were in use. |





**Since:** BeOS R3

---

### `SendMessage()`

```cpp
status_t BMessenger::SendMessage(BMessage * message, BMessenger replyTo, bigtime_t timeout = B_INFINITE_TIMEOUT)const
```

Delivers a *message* to the messenger's target. A response message may be sent back to the *replyTo* messenger's target asynchronously. 


A copy of the supplied message is sent and the caller retains ownership of *message*.


If the target's message port is full, the method waits until space becomes available in the port or the specified timeout occurs (whichever happens first). After delivery the method returns immediately. It does not wait until the target processes the message or even sends a reply.


This method does not return by default until the message has been delivered. You can set a delivery *timeout* in microseconds.


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The message to be sent. |
| `replyTo` | A messenger specifying the target for a response message. |
| `timeout` | The message delivery timeout in microseconds. (optional) |





**Returns:** A status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_PORT_ID | The messenger was not properly initialized or its target didn't exist. |
| B_WOULD_BLOCK | A delivery timeout of 0 was supplied and the target port was full when trying to deliver the message. |
| B_TIMED_OUT | The timeout expired while trying to deliver the message. |





**Since:** BeOS R4

---

### `SendMessage()`

```cpp
status_t BMessenger::SendMessage(uint32 command, BHandler * replyTo = NULL)const
```

Delivers a [BMessage](classBMessage.md) with *command* `what` identifier to the messenger's target. A response may be sent to the *replyTo* handler asynchronously. 


If the target's message port is full, the method waits indefinitely, until space becomes available in the port. After delivery the method returns immediately. It does not wait until the target processes the message or even sends a reply.


Parameters

| Parameter | Description |
| :--- | :--- |
| `command` | The what field of the message to deliver. |
| `replyTo` | The handler to which a reply to the message shall be sent. May be `NULL`. |





**Returns:** A status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_PORT_ID | The messenger is not properly initialized or its target doesn't exist anymore. |





**Since:** BeOS R3

---

### `SendMessage()`

```cpp
status_t BMessenger::SendMessage(uint32 command, BMessage * reply)const
```

Delivers a [BMessage](classBMessage.md) with *command* `what` identifier to the messenger's target and waits for a *reply* [BMessage](classBMessage.md) synchronously. 


The method does wait for a reply. The reply message is copied into *reply*. If the target doesn't send a reply, the `what` field of *reply* is set to `B_NO_REPLY`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `command` | The what field of the message to deliver. |
| `reply` | A pointer to a pre-allocated [BMessage](classBMessage.md) object which the reply message will be copied into. |





**Returns:** A status code, `B_OK` on success or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_PORT_ID | The messenger was not properly initialized or its target didn't exist. |
| B_NO_MORE_PORTS | All reply ports were in use. |





**Since:** BeOS R3

---

### `SetTo()`

```cpp
status_t BMessenger::SetTo(const BHandler * handler, const BLooper * looper = NULL)
```

Reinitializes a [BMessenger](classBMessenger.md) to target the local [BHandler](classBHandler.md) and/or [BLooper](classBLooper.md). 


When a `NULL` handler is supplied, the preferred handler in the given looper is targeted. If no looper is supplied the looper the given handler belongs to is used – that means in particular, that the handler must already belong to a looper. If both are supplied the handler must actually belong to looper.


Parameters

| Parameter | Description |
| :--- | :--- |
| `handler` | The target handler. May be `NULL`. |
| `looper` | The target looper. May be `NULL`. |





**Returns:** A status code, `B_OK` if the reinitialization was successful or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The reinitialization was successful. |
| B_BAD_VALUE | Both *handler* and *looper* were `NULL` or invalid. |
| B_MISMATCHED_VALUES | The looper of the supplied *handler* and *looper* didn't match. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BMessenger::SetTo(const char * signature, team_id team = -1)
```

Reinitializes a [BMessenger](classBMessenger.md) to target the already running application identified by the supplied signature and/or team ID. 


When only a signature is given, and multiple instances of the application are running it is indeterminate which one is chosen as the target. In case only a team ID is passed, the target application is identified uniquely. If both are supplied, the application identified by the team ID must have a matching signature, otherwise the initialization fails.


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | The target application's signature. May be `NULL`. |
| `team` | The target application's team ID. May be negative. |





**Returns:** A status code, `B_OK` if the reinitialization was successful or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The reinitialization was successful. |
| B_BAD_VALUE | No application with the given *signature* or *team* ID was running. |
| B_BAD_TYPE | No *team* ID was given and the *signature* was `NULL`. |
| B_MISMATCHED_VALUES | The supplied *signature* and the signature of the team didn't match. |





**Since:** Haiku R1

---

### `Target()`

```cpp
BHandler * BMessenger::Target(BLooper ** _looper)const
```

Returns the handler and looper targeted by the messenger (if the target is local). 


The handler is returned directly, the looper by reference. If both are `NULL`, the object is either not properly initialized, the target objects have been deleted or the target is remote. If only the returned handler is `NULL`, either the looper's preferred handler is targeted or the handler has been deleted.


Parameters

| Parameter | Description |
| :--- | :--- |
| `_looper` | A pointer to a pre-allocated [BLooper](classBLooper.md) pointer into which the pointer to the targeted looper is written. |





**Returns:** The [BHandler](classBHandler.md) targeted by the messenger.



**Since:** BeOS R3

---

### `Team()`

```cpp
team_id BMessenger::Team()const
```

Returns the ID of the team that the messenger's target belongs to. 



**Returns:** The team of the messenger's target.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMessenger.html).
