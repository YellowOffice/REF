---
name: BMailDaemon
type: class
kit: mail_kit
brief: "Provides user level access to the mail_daemon to perform common mail tasks such as check for new messages or send queued messages"
source: haiku-book
---

# BMailDaemon Class
**Kit/Group:** [Mail Kit](../mail_kit/group__mail.md) | [Mail Kit library (libmail.so)](group__libmail.md)

## Description

Provides user level access to the mail_daemon to perform common mail tasks such as check for new messages or send queued messages. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BMailDaemon](#ae2d7d95639e49715dd145c7158e43bc6) () — Creates a BMailDaemon object that communicates with the mail_daemon server.
* `virtual` [~BMailDaemon](#afc6218de874ca48c008816e09c9f3e8e) () — Frees all resources associated with this object.
* `bool` [IsRunning](#a6bd11a8d01bfaa0f978af558a704be1d) () — Checks if the mail_daemon is running.
* `status_t` [Quit](#ac2eb6b1c4ab29541cc585ba78f09d7a9) () — Request the mail_daemon to quit.
* `status_t` [Launch](#a66090427843c6aedb79566e0646d50ab) () — Launches the mail_daemon.
* `status_t` [CheckMail](#ae5a5b1083eade42ca6b79f626638a7c6) (int32 accountID=-1) — Asks the mail_daemon to check if there are new messages for the account with ID accountID.
* `status_t` [CheckAndSendQueuedMail](#af6f645de9d9941f505e77cc683bf8bce) (int32 accountID=-1) — Asks the mail_daemon to check if there are new messages and to send any queued messages pending to be sent, for the account with ID accountID.
* `status_t` [SendQueuedMail](#ad0c9d9bab0891610f85475a79343b401) () — Asks the mail_daemon to send any queued message pending to be sent.
* `int32` [CountNewMessages](#afe901af3b3f5224b83500656501fbc4d) (bool waitForFetchCompletion=false) — Asks the mail_daemon how many new messages there are.
* `status_t` [MarkAsRead](#afd30c8ab7f3a47815abe049aff7e4f98) (int32 account, const entry_ref &ref, read_flags flag=B_READ) — Requests the mail_daemon to mark an e-mail message as read or unread.
* `status_t` [FetchBody](#af3df01fabcaa4da60f37971d9caf7480) (const entry_ref &ref, BMessenger *listener=NULL) — Requests the mail_daemon to retrieve the message's body.

## Detailed Member Documentation

### `BMailDaemon()`

```cpp
BMailDaemon::BMailDaemon()
```

Creates a [BMailDaemon](classBMailDaemon.md) object that communicates with the mail_daemon server. 



**Since:** Haiku R1

---

### `~BMailDaemon()`

```cpp
BMailDaemon::~BMailDaemon()
```

Frees all resources associated with this object. 



**Since:** Haiku R1

---

### `CheckAndSendQueuedMail()`

```cpp
status_t BMailDaemon::CheckAndSendQueuedMail(int32 accountID = -1)
```

Asks the mail_daemon to check if there are new messages and to send any queued messages pending to be sent, for the account with ID *accountID*. 


If *accountID* is `-1`, it will check for new messages and send the queued messages for all the available accounts.


Parameters

| Parameter | Description |
| :--- | :--- |
| `accountID` | The ID of the account. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The request has been sent successfully. |
| B_MAIL_NO_DAEMON | The mail_daemon is not currently running. |





**Since:** Haiku R1

---

### `CheckMail()`

```cpp
status_t BMailDaemon::CheckMail(int32 accountID = -1)
```

Asks the mail_daemon to check if there are new messages for the account with ID *accountID*. 


If *accountID* is `-1`, it will check for new messages for all the available accounts.


Parameters

| Parameter | Description |
| :--- | :--- |
| `accountID` | The ID of the account. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The request has been sent successfully. |
| B_MAIL_NO_DAEMON | The mail_daemon is not currently running. |





**Since:** Haiku R1

---

### `CountNewMessages()`

```cpp
int32 BMailDaemon::CountNewMessages(bool waitForFetchCompletion = false)
```

Asks the mail_daemon how many new messages there are. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `waitForFetchCompletion` | If `true`, it will make the count once the mail server fetching is completed. |





**Returns:** The number of new messages, or `B_MAIL_NO_DAEMON` if the mail_daemon is not currently running.



**Since:** Haiku R1

---

### `FetchBody()`

```cpp
status_t BMailDaemon::FetchBody(const entry_ref & ref, BMessenger * listener = NULL)
```

Requests the mail_daemon to retrieve the message's body. 


If *listener* is not `NULL`, it will receive a `B_MAIL_BODY_FETCHED` notification after the e-mail message's body was fetched successfully, or else an error code if something went wrong.


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The [entry_ref](../storage_kit/structentry__ref.md) of the target message. |
| `listener` | A [BMessenger](../application_kit/classBMessenger.md) where a reply will be sent to. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The request has been sent successfully. |
| B_MAIL_NO_DAEMON | The mail_daemon is not currently running. |





**Since:** Haiku R1

---

### `IsRunning()`

```cpp
bool BMailDaemon::IsRunning()
```

Checks if the mail_daemon is running. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The mail_daemon is running. |
| false | The mail_daemon is not running. |





**Since:** Haiku R1

---

### `Launch()`

```cpp
status_t BMailDaemon::Launch()
```

Launches the mail_daemon. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The mail_daemon has been launched successfully. |
| B_ALREADY_RUNNING | The mail_daemon is already running. |





**Since:** Haiku R1

---

### `MarkAsRead()`

```cpp
status_t BMailDaemon::MarkAsRead(int32 account, const entry_ref & ref, read_flags flag = B_READ)
```

Requests the mail_daemon to mark an e-mail message as read or unread. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `account` | The account's ID. |
| `ref` | The [entry_ref](../storage_kit/structentry__ref.md) of the target message. |
| `flag` | Can be one of these: `B_UNREAD`, `B_SEEN`, `B_READ`. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The request has been sent successfully. |
| B_MAIL_NO_DAEMON | The mail_daemon is not currently running. |





**Since:** Haiku R1

---

### `Quit()`

```cpp
status_t BMailDaemon::Quit()
```

Request the mail_daemon to quit. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The request has been sent successfully. |
| B_MAIL_NO_DAEMON | The mail_daemon is not currently running. |





**Since:** Haiku R1

---

### `SendQueuedMail()`

```cpp
status_t BMailDaemon::SendQueuedMail()
```

Asks the mail_daemon to send any queued message pending to be sent. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The request has been sent successfully. |
| B_MAIL_NO_DAEMON | The mail_daemon is not currently running. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMailDaemon.html).
