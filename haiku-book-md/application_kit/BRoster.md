---
name: BRoster
type: class
kit: application_kit
brief: "The BRoster class lets you launch apps and keeps track of apps that are running"
source: haiku-book
---

# BRoster Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

The [BRoster](classBRoster.md) class lets you launch apps and keeps track of apps that are running. 


The global [be_roster](Roster_8h.md#a47f4c3d7d062ea2e32ba2790a3fb75f8) object represents the default [BRoster](classBRoster.md), while the [app_info](structapp__info.md) structure provides info for a running app.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BRoster](#a8988d01f8ea090047c37562e5e7f2d24) () — Creates a new BRoster and sets up the connection to the roster service.
* [~BRoster](#a74187ff803039d8b7b4ea5f735068305) () — Does nothing.
* `bool` [IsRunning](#ad503f418df5b24b049029394a67750a9) (const char *signature) const — Returns whether or not an application with the supplied signature is currently running.
* `bool` [IsRunning](#a8b83d4e28852d4743e1ddbe260fe079e) (entry_ref *ref) const — Returns whether or not an application ran from an executable referred to by the supplied entry_ref is currently running.
* `team_id` [TeamFor](#a51a41674f9598fb5185b83bcdc617b76) (const char *signature) const — Returns the team ID of a currently running application with the supplied signature.
* `team_id` [TeamFor](#a147169f7ed1642f88913ba9d1be80554) (entry_ref *ref) const — Returns the team ID of a currently running application executing the executable referred to by the supplied entry_ref.
* `void` [GetAppList](#a50a074cf5199fdba4c53555e2d6f60e8) (BList *teamIDList) const — Returns a list of all currently running applications.
* `void` [GetAppList](#a00df68600d9ea16a0c6984641e3047df) (const char *signature, BList *teamIDList) const — Returns a list of all currently running applications with the specified signature.
* `status_t` [GetAppInfo](#ae0083d735bb8ebb40e66218b95693ab7) (const char *signature, app_info *info) const — Returns the app_info of a currently running application with the supplied signature.
* `status_t` [GetAppInfo](#a6c8eff6e1213c9cd6bd0ffa62a11db42) (entry_ref *ref, app_info *info) const — Returns the app_info of a currently running application executing the executable referred to by the supplied entry_ref.
* `status_t` [GetRunningAppInfo](#a119e6efd032a83f32cd76c327785cc22) (team_id team, app_info *info) const — Returns the app_info of a currently running application identified by the supplied team ID.
* `status_t` [GetActiveAppInfo](#a0c144191815ffac1c18b04fe659ff82b) (app_info *info) const — Returns the app_info of a currently active application.
* `status_t` [FindApp](#a04481f026126b69901a9e55bbf1c665a) (const char *mimeType, entry_ref *app) const — Finds an application associated with a MIME type.
* `status_t` [FindApp](#a0eec22b3e46838bddbe899b0efd671c0) (entry_ref *ref, entry_ref *app) const — Finds an application associated with a file.
* `status_t` [Broadcast](#a272a11486eba4683a8adb06f3a1c8493) (BMessage *message) const — Sends a message to all running applications.
* `status_t` [Broadcast](#a3d7db167d728e879dd4ee9437d217563) (BMessage *message, BMessenger replyTo) const — Sends a message to all running applications.
* `status_t` [StartWatching](#a2cd20378ab189c4df1eba833f1079dae) (BMessenger target, uint32 eventMask=B_REQUEST_LAUNCHED|B_REQUEST_QUIT) const — Adds a new roster application monitor.
* `status_t` [StopWatching](#a5a792a6d4af01978a6c1d55222c70c73) (BMessenger target) const — Removes a roster application monitor added with StartWatching().
* `status_t` [ActivateApp](#a29069168723243621a07f0c818201e77) (team_id team) const — Activates the application identified by the supplied team ID.
* `status_t` [Launch](#a7336c58b9bea76b181c83c0d6e635360) (const char *mimeType, BMessage *initialMessage=NULL, team_id *_appTeam=NULL) const — Launches the application associated with the supplied MIME type.
* `status_t` [Launch](#af6944dafa4a8bebbd3ffeff0e3d54ec8) (const char *mimeType, BList *messageList, team_id *_appTeam=NULL) const — Launches the application associated with the supplied MIME type.
* `status_t` [Launch](#a368caecd9e793e22fe8000c308c1a4f5) (const char *mimeType, int argc, const char *const *args, team_id *_appTeam=NULL) const — Launches the application associated with the supplied MIME type.
* `status_t` [Launch](#adb2e6bbbb2e7b0c7491156ba7530a39f) (const entry_ref *ref, const BMessage *initialMessage=NULL, team_id *_appTeam=NULL) const — Launches the application associated with the entry referred to by the supplied entry_ref.
* `status_t` [Launch](#abb7825d52e76d9e2bc036d6b9920b315) (const entry_ref *ref, const BList *messageList, team_id *_appTeam=NULL) const — Launches the application associated with the entry referred to by the supplied entry_ref.
* `status_t` [Launch](#a9c340c91a997d96072e118ec472e7b91) (const entry_ref *ref, int argc, const char *const *args, team_id *_appTeam=NULL) const — Launches the application associated with the entry referred to by the supplied entry_ref.
* `void` [GetRecentDocuments](#a6ea514268be5a0fc822b635c5e6da03a) (BMessage *refList, int32 maxCount, const char *fileType=NULL, const char *signature=NULL) const — Returns a list of the most recently used documents.
* `void` [GetRecentDocuments](#a6076e34c87fd63cc69725773b7a0be59) (BMessage *refList, int32 maxCount, const char *fileTypes[], int32 fileTypesCount, const char *signature=NULL) const — Returns a list of the most recently used documents.
* `void` [GetRecentFolders](#a9b435176e4c956e94d61467b0a03b06f) (BMessage *refList, int32 maxCount, const char *signature=NULL) const — Returns a list of recently accessed folders.
* `void` [GetRecentApps](#abdb0b9a9974ef3475249a225f296a810) (BMessage *refList, int32 maxCount) const — Returns a list of the most recently launched applications.
* `void` [AddToRecentDocuments](#a87bfbcc4065029bb146685c811530426) (const entry_ref *document, const char *signature=NULL) const — Adds the document to the list of recent documents.
* `void` [AddToRecentFolders](#a656310d69bc34979dec2e712373076f9) (const entry_ref *folder, const char *signature=NULL) const — Adds folder to the list of recent folders.

## Detailed Member Documentation

### `BRoster()`

```cpp
BRoster::BRoster()
```

Creates a new [BRoster](classBRoster.md) and sets up the connection to the roster service. 


You should not need to call this, use the [be_roster](Roster_8h.md#a47f4c3d7d062ea2e32ba2790a3fb75f8) global instead.



**Since:** BeOS R3

---

### `~BRoster()`

```cpp
BRoster::~BRoster()
```

Does nothing. 



**Since:** BeOS R3

---

### `ActivateApp()`

```cpp
status_t BRoster::ActivateApp(team_id team)const
```

Activates the application identified by the supplied team ID. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `team` | The app's team ID |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_TEAM_ID | *team* does not identify a running application. |





**Since:** BeOS R3

---

### `AddToRecentDocuments()`

```cpp
void BRoster::AddToRecentDocuments(const entry_ref * document, const char * signature = NULL)const
```

Adds the *document* to the list of recent documents. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `document` | The *document* to add. |
| `signature` | To record that a specific application used the document. |





**Since:** BeOS R5

---

### `AddToRecentFolders()`

```cpp
void BRoster::AddToRecentFolders(const entry_ref * folder, const char * signature = NULL)const
```

Adds *folder* to the list of recent folders. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `folder` | The *folder* to add. |
| `signature` | To record that a specific application used the folder. |





**Since:** BeOS R5

---

### `Broadcast()`

```cpp
status_t BRoster::Broadcast(BMessage * message)const
```

Sends a message to all running applications. 


The methods doesn't broadcast the message itself, but it asks the roster to do so. It immediatly returns after sending the request. The return value only tells about whether the request has successfully been sent.


The message is sent asynchronously. Replies to it go to the application. (`be_app_messenger`).


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The message to be broadcast. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *message*. |





**Since:** BeOS R3

---

### `Broadcast()`

```cpp
status_t BRoster::Broadcast(BMessage * message, BMessenger replyTo)const
```

Sends a message to all running applications. 


The methods doesn't broadcast the message itself, but it asks the roster to do so. It immediatly returns after sending the request. The return value only tells about whether the request has successfully been sent.


The message is sent asynchronously. Replies to it go to the specified target (*replyTo*).


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The message to be broadcast. |
| `replyTo` | Reply target for the message. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *message*. |





**Since:** BeOS R4

---

### `FindApp()`

```cpp
status_t BRoster::FindApp(const char * mimeType, entry_ref * app)const
```

Finds an application associated with a MIME type. 


The method gets the signature of the supplied type's preferred application and the signature of the super type's preferred application. It will also get all supporting applications for the type and super type and build a list of candiate handlers. In the case that a preferred handler is configured for the sub-type, other supporting apps will be inserted in the candidate list before the super-type preferred and supporting handlers, since it is assumed that the super type handlers are not well suited for the sub-type. The following resolving algorithm is performed on each signature of the resulting list: The MIME database is asked which executable is associated with the signature. If the database doesn't have a reference to an exectuable, the boot volume is queried for a file with the signature. If more than one file has been found, the one with the greatest version is picked, or if no file has a version info, the one with the most recent modification date. The first application from the signature list which can be successfully resolved by this algorithm is returned. Contrary to BeOS behavior, this means that if the preferred application of the provided MIME type cannot be resolved, or if it does not have a preferred application associated, the method will return other applications with direct support for the MIME type before it resorts to the preferred application or supporting applications of the super type.


Parameters

| Parameter | Description |
| :--- | :--- |
| `mimeType` | The MIME type for which an application shall be found. |
| `app` | A pointer to a pre-allocated [entry_ref](../storage_kit/structentry__ref.md) to be filled with a reference to the found application's executable. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *mimeType* or *app*. |
| B_LAUNCH_FAILED_NO_PREFERRED_APP | Neither with the supplied type nor with its supertype (if the supplied isn't a supertype itself) a preferred application is associated and no other supporting applications could be identified. |
| B_LAUNCH_FAILED_APP_NOT_FOUND | The supplied type was not installed or its preferred application could not be found. |
| B_LAUNCH_FAILED_APP_IN_TRASH | The supplied type's only supporting application was in the trash. |





**Since:** BeOS R3

---

### `FindApp()`

```cpp
status_t BRoster::FindApp(entry_ref * ref, entry_ref * app)const
```

Finds an application associated with a file. 


The method first checks, if the file has a preferred application associated with it (see [BNodeInfo::GetPreferredApp()](../storage_kit/classBNodeInfo.md#a7efa86ade48aec51d4a4b7ff4762c163)) and if so, tries to find the executable the same way FindApp(const char*, entry_ref*) does. If not, it gets the MIME type of the file and searches an application for it exactly like the first [FindApp()](classBRoster.md#a04481f026126b69901a9e55bbf1c665a) method.


The type of the file is defined in a file attribute ([BNodeInfo::GetType()](../storage_kit/classBNodeInfo.md#a9bfd75065d98e817d078c968d02228e4)), but if it is not set yet, the method tries to guess it via [BMimeType::GuessMimeType()](../storage_kit/classBMimeType.md#a014ae51a0763796a1c9ed57c942fd46e).


As a special case the file may have execute permission. Then preferred application and type are ignored and an [entry_ref](../storage_kit/structentry__ref.md) to the file itself is returned.


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | An [entry_ref](../storage_kit/structentry__ref.md) referring to the file for which an application shall be found. |
| `app` | A pointer to a pre-allocated [entry_ref](../storage_kit/structentry__ref.md) to be filled with a reference to the found application's executable. |





**Returns:** 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *mimeType* or *app*. |
| B_LAUNCH_FAILED_NO_PREFERRED_APP | Neither with the supplied type nor with its supertype (if the supplied isn't a supertype itself) a preferred application is associated. |
| B_LAUNCH_FAILED_APP_NOT_FOUND | The supplied type was not installed or its preferred application could not be found. |
| B_LAUNCH_FAILED_APP_IN_TRASH | The supplied type's preferred application was in the trash. |





**Since:** BeOS R3

---

### `GetActiveAppInfo()`

```cpp
status_t BRoster::GetActiveAppInfo(app_info * info)const
```

Returns the [app_info](structapp__info.md) of a currently active application. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `info` | A pointer to a pre-allocated [app_info](structapp__info.md) structure to be filled in by this method. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *info* was `NULL`. |
| B_ERROR | No application was currently active. |





**Since:** BeOS R3


Parameters

| Parameter | Description |
| :--- | :--- |
| `info` | A pointer to a pre-allocated [app_info](structapp__info.md) structure to be filled in by this method. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *info* was `NULL`. |
| B_ERROR | No application was currently active. |





**Since:** BeOS R3

---

### `GetAppInfo()`

```cpp
status_t BRoster::GetAppInfo(const char * signature, app_info * info)const
```

Returns the [app_info](structapp__info.md) of a currently running application with the supplied *signature*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | The application *signature*. |
| `info` | A pointer to a pre-allocated [app_info](structapp__info.md) structure to be filled by this method. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *sig* is `NULL`. |
| B_ERROR | No application with the supplied signature is currently running. |





**Since:** BeOS R3

---

### `GetAppInfo()`

```cpp
status_t BRoster::GetAppInfo(entry_ref * ref, app_info * info)const
```

Returns the [app_info](structapp__info.md) of a currently running application executing the executable referred to by the supplied [entry_ref](../storage_kit/structentry__ref.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The app's [entry_ref](../storage_kit/structentry__ref.md) |
| `info` | A pointer to a pre-allocated [app_info](structapp__info.md) structure to be filled in by this method. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *ref* is `NULL`. |
| B_ERROR | No application executing the file referred to by *ref* was currently running. |





**Since:** BeOS R3

---

### `GetAppList()`

```cpp
void BRoster::GetAppList(BList * teamIDList)const
```

Returns a list of all currently running applications. 


The supplied list is not emptied before adding the team IDs of the running applications. The list elements are team_id's, not pointers.


Parameters

| Parameter | Description |
| :--- | :--- |
| `teamIDList` | A pointer to a pre-allocated [BList](../support_kit/classBList.md) to be filled with the team IDs. |





**Since:** BeOS R3

---

### `GetAppList()`

```cpp
void BRoster::GetAppList(const char * signature, BList * teamIDList)const
```

Returns a list of all currently running applications with the specified *signature*. 


The supplied list is not emptied before adding the team IDs of the running applications. The list elements are team_id's, not pointers. If *sig* is `NULL` or invalid, no team IDs are added to the list.


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | The application *signature*. |
| `teamIDList` | A pointer to a pre-allocated [BList](../support_kit/classBList.md) to be filled with the team IDs. |





**Since:** BeOS R3

---

### `GetRecentApps()`

```cpp
void BRoster::GetRecentApps(BMessage * refList, int32 maxCount)const
```

Returns a list of the most recently launched applications. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `refList` | Filled out with information about recently used apps. |
| `maxCount` | The maximum number of apps to get information on. |





**Since:** BeOS R5

---

### `GetRecentDocuments()`

```cpp
void BRoster::GetRecentDocuments(BMessage * refList, int32 maxCount, const char * fileType = NULL, const char * signature = NULL)const
```

Returns a list of the most recently used documents. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `refList` | Filled out with information about recently used documents. |
| `maxCount` | The maximum number of documents to get information on. |
| `fileType` | Filter documents by MIME-type string. |
| `signature` | Get info only on documents that were used by a specific application. |





**Since:** BeOS R5

---

### `GetRecentDocuments()`

```cpp
void BRoster::GetRecentDocuments(BMessage * refList, int32 maxCount, const char * fileTypes[], int32 fileTypesCount, const char * signature = NULL)const
```

Returns a list of the most recently used documents. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `refList` | Filled out with information about recently used documents. |
| `maxCount` | The maximum number of documents to get information on. |
| `fileTypes` | Filter documents by and array of MIME-type string. |
| `fileTypesCount` | The number of MIME-types in *fileType*. |
| `signature` | Get info only on documents that were used by a specific application. |





**Since:** BeOS R5

---

### `GetRecentFolders()`

```cpp
void BRoster::GetRecentFolders(BMessage * refList, int32 maxCount, const char * signature = NULL)const
```

Returns a list of recently accessed folders. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `refList` | Filled out with information about recently used folders. |
| `maxCount` | The maximum number of folders to get information on. |
| `signature` | Get info only on folders that were used by a specific application. |





**Since:** BeOS R5

---

### `GetRunningAppInfo()`

```cpp
status_t BRoster::GetRunningAppInfo(team_id team, app_info * info)const
```

Returns the [app_info](structapp__info.md) of a currently running application identified by the supplied team ID. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `team` | The app's team ID. |
| `info` | A pointer to a pre-allocated [app_info](structapp__info.md) structure to be filled in by this method. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | *info* was `NULL`. |
| B_BAD_TEAM_ID | *team* did not identify a running application. |





**Since:** BeOS R3

---

### `IsRunning()`

```cpp
bool BRoster::IsRunning(const char * signature)const
```

Returns whether or not an application with the supplied signature is currently running. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | The app *signature*. |





**Returns:** `true`, if the supplied *signature* is not `NULL` and an application with this *signature* is running, `false` otherwise.



**Since:** BeOS R3

---

### `IsRunning()`

```cpp
bool BRoster::IsRunning(entry_ref * ref)const
```

Returns whether or not an application ran from an executable referred to by the supplied [entry_ref](../storage_kit/structentry__ref.md) is currently running. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The app's [entry_ref](../storage_kit/structentry__ref.md) |





**Returns:** `true`, if the supplied [entry_ref](../storage_kit/structentry__ref.md) is not `NULL` and an application executing this file is running, `false` otherwise.



**Since:** BeOS R3

---

### `Launch()`

```cpp
status_t BRoster::Launch(const char * mimeType, BList * messageList, team_id * appTeam = NULL)const
```

Launches the application associated with the supplied MIME type. 


The application to be started is searched the same way [FindApp()](classBRoster.md#a04481f026126b69901a9e55bbf1c665a) does it.


*messageList* contains messages to be sent to the application "on launch", i.e. before ReadyToRun() is invoked on the [BApplication](classBApplication.md) object. The caller retains ownership of the supplied [BList](../support_kit/classBList.md) and the contained BMessages. In case the method fails with `B_ALREADY_RUNNING` the messages are delivered to the already running instance.


Parameters

| Parameter | Description |
| :--- | :--- |
| `mimeType` | MIME type for which the application shall be launched. |
| `messageList` | Optional list of messages to be sent to the application "on launch". May be `NULL`. |
| `appTeam` | Pointer to a pre-allocated team_id variable to be set to the team ID of the launched application. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *mimeType* |
| B_LAUNCH_FAILED_NO_PREFERRED_APP | Neither with the supplied type nor with its supertype (if the supplied isn't a supertype itself) a preferred application is associated. |
| B_LAUNCH_FAILED_APP_NOT_FOUND | The supplied type is not installed or its preferred application could not be found. |
| B_LAUNCH_FAILED_APP_IN_TRASH | The supplied type's preferred application was in the trash. |
| B_LAUNCH_FAILED_EXECUTABLE | The found application was not executable. |





**Since:** BeOS R3

---

### `Launch()`

```cpp
status_t BRoster::Launch(const char * mimeType, BMessage * initialMessage = NULL, team_id * appTeam = NULL)const
```

Launches the application associated with the supplied MIME type. 


The application to be started is searched the same way [FindApp()](classBRoster.md#a04481f026126b69901a9e55bbf1c665a) does it.


*initialMessage* is a message to be sent to the application "on launch", i.e. before ReadyToRun() is invoked on the [BApplication](classBApplication.md) object. The caller retains ownership of the supplied [BMessage](classBMessage.md). In case the method fails with `B_ALREADY_RUNNING` the message is delivered to the already running instance.


Parameters

| Parameter | Description |
| :--- | :--- |
| `mimeType` | MIME type for which the application shall be launched. |
| `initialMessage` | Optional message to be sent to the application "on launch". May be `NULL`. |
| `appTeam` | Pointer to a pre-allocated team_id variable to be set to the team ID of the launched application. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *mimeType* |
| B_LAUNCH_FAILED_NO_PREFERRED_APP | Neither with the supplied type nor with its supertype (if the supplied isn't a supertype itself) a preferred application is associated. |
| B_LAUNCH_FAILED_APP_NOT_FOUND | The supplied type is not installed or its preferred application could not be found. |
| B_LAUNCH_FAILED_APP_IN_TRASH | The supplied type's preferred application was in the trash. |
| B_LAUNCH_FAILED_EXECUTABLE | The found application was not executable. |
| B_ALREADY_RUNNING | The application's app flags specify |
| B_SINGLE_LAUNCH | or `B_EXCLUSIVE_LAUNCH` and the application (the very same (single) or at least one with the same signature (exclusive)) is already running. |





**Since:** BeOS R3

---

### `Launch()`

```cpp
status_t BRoster::Launch(const char * mimeType, int argc, const char *const * args, team_id * appTeam = NULL)const
```

Launches the application associated with the supplied MIME type. 


The application to be started is searched the same way [FindApp()](classBRoster.md#a04481f026126b69901a9e55bbf1c665a) does it.


The supplied *argc* and *args* are (if containing at least one argument) put into a `B_ARGV_RECEIVED` message and sent to the launched application "on launch". The caller retains ownership of the supplied *args*. In case the method fails with `B_ALREADY_RUNNING` the message is delivered to the already running instance.


Parameters

| Parameter | Description |
| :--- | :--- |
| `mimeType` | MIME type for which the application shall be launched. |
| `argc` | Specifies the number of elements in *args*. |
| `args` | An array of C-strings to be sent as B_ARGV_RECEIVED messaged to the launched application. |
| `appTeam` | Pointer to a pre-allocated team_id variable to be set to the team ID of the launched application. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *mimeType* |
| B_LAUNCH_FAILED_NO_PREFERRED_APP | Neither with the supplied type nor with its supertype (if the supplied isn't a supertype itself) a preferred application is associated. |
| B_LAUNCH_FAILED_APP_NOT_FOUND | The supplied type is not installed or its preferred application could not be found. |
| B_LAUNCH_FAILED_APP_IN_TRASH | The supplied type's preferred application was in the trash. |
| B_LAUNCH_FAILED_EXECUTABLE | The found application was not executable. |





**Since:** BeOS R3

---

### `Launch()`

```cpp
status_t BRoster::Launch(const entry_ref * ref, const BList * messageList, team_id * appTeam = NULL)const
```

Launches the application associated with the entry referred to by the supplied [entry_ref](../storage_kit/structentry__ref.md). 


The application to be started is searched the same way [FindApp()](classBRoster.md#a04481f026126b69901a9e55bbf1c665a) does it.


If *ref* does refer to an application executable, that application is launched. Otherwise the respective application is searched and launched, and *ref* is sent to it in a `B_REFS_RECEIVED` message.


*messageList* contains messages to be sent to the application "on launch", i.e. before ReadyToRun() is invoked on the [BApplication](classBApplication.md) object. The caller retains ownership of the supplied [BList](../support_kit/classBList.md) and the contained BMessages. In case the method fails with `B_ALREADY_RUNNING` the messages are delivered to the already running instance. The same applies to the `B_REFS_RECEIVED` message.


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | [entry_ref](../storage_kit/structentry__ref.md) referring to the file for which an application shall be launched. |
| `messageList` | Optional list of messages to be sent to the application "on launch". May be `NULL`. |
| `appTeam` | Pointer to a pre-allocated team_id variable to be set to the team ID of the launched application. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *mimeType* |
| B_LAUNCH_FAILED_NO_PREFERRED_APP | Neither with the supplied type nor with its supertype (if the supplied isn't a supertype itself) a preferred application is associated. |
| B_LAUNCH_FAILED_APP_NOT_FOUND | The supplied type is not installed or its preferred application could not be found. |
| B_LAUNCH_FAILED_APP_IN_TRASH | The supplied type's preferred application was in the trash. |
| B_LAUNCH_FAILED_EXECUTABLE | The found application was not executable. |





**Since:** BeOS R3

---

### `Launch()`

```cpp
status_t BRoster::Launch(const entry_ref * ref, const BMessage * initialMessage = NULL, team_id * appTeam = NULL)const
```

Launches the application associated with the entry referred to by the supplied [entry_ref](../storage_kit/structentry__ref.md). 


The application to be started is searched the same way [FindApp()](classBRoster.md#a04481f026126b69901a9e55bbf1c665a) does it.


If *ref* does refer to an application executable, that application is launched. Otherwise the respective application is searched and launched, and *ref* is sent to it in a `B_REFS_RECEIVED` message.


*initialMessage* is a message to be sent to the application "on launch", i.e. before ReadyToRun() is invoked on the [BApplication](classBApplication.md) object. The caller retains ownership of the supplied [BMessage](classBMessage.md). In case the method fails with `B_ALREADY_RUNNING` the message is delivered to the already running instance. The same applies to the `B_REFS_RECEIVED` message.


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | [entry_ref](../storage_kit/structentry__ref.md) referring to the file for which an application shall be launched. |
| `initialMessage` | Optional message to be sent to the application "on launch". May be `NULL`. |
| `appTeam` | Pointer to a pre-allocated team_id variable to be set to the team ID of the launched application. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *mimeType* |
| B_LAUNCH_FAILED_NO_PREFERRED_APP | Neither with the supplied type nor with its supertype (if the supplied isn't a supertype itself) a preferred application is associated. |
| B_LAUNCH_FAILED_APP_NOT_FOUND | The supplied type is not installed or its preferred application could not be found. |
| B_LAUNCH_FAILED_APP_IN_TRASH | The supplied type's preferred application was in the trash. |
| B_LAUNCH_FAILED_EXECUTABLE | The found application was not executable. |
| B_ALREADY_RUNNING | The application's app flags specify `B_SINGLE_LAUNCH` or `B_EXCLUSIVE_LAUNCH` and the application (the very same (single) or at least one with the same signature (exclusive)) was already running. |





**Since:** BeOS R3

---

### `Launch()`

```cpp
status_t BRoster::Launch(const entry_ref * ref, int argc, const char *const * args, team_id * appTeam = NULL)const
```

Launches the application associated with the entry referred to by the supplied [entry_ref](../storage_kit/structentry__ref.md). 


The application to be started is searched the same way [FindApp()](classBRoster.md#a04481f026126b69901a9e55bbf1c665a) does it.


If *ref* does refer to an application executable, that application is launched. Otherwise the respective application is searched and launched, and *ref* is sent to it in a `B_REFS_RECEIVED` message, unless other arguments are passed via *argc* and *args* – then the [entry_ref](../storage_kit/structentry__ref.md) is converted into a path (C-string) and added to the argument vector.


The supplied *argc* and *args* are (if containing at least one argument) put into a `B_ARGV_RECEIVED` message and sent to the launched application "on launch". The caller retains ownership of the supplied *args*. In case the method fails with `B_ALREADY_RUNNING` the message is delivered to the already running instance. The same applies to the `B_REFS_RECEIVED` message, if no arguments are supplied via *argc* and *args*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | [entry_ref](../storage_kit/structentry__ref.md) referring to the file for which an application shall be launched. |
| `argc` | Specifies the number of elements in *args*. |
| `args` | An array of C-strings to be sent as B_ARGV_RECEIVED messaged to the launched application. |
| `appTeam` | Pointer to a pre-allocated team_id variable to be set to the team ID of the launched application. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | `NULL` *mimeType* |
| B_LAUNCH_FAILED_NO_PREFERRED_APP | Neither with the supplied type nor with its supertype (if the supplied isn't a supertype itself) a preferred application is associated. |
| B_LAUNCH_FAILED_APP_NOT_FOUND | The supplied type is not installed or its preferred application could not be found. |
| B_LAUNCH_FAILED_APP_IN_TRASH | The supplied type's preferred application was in the trash. |
| B_LAUNCH_FAILED_EXECUTABLE | The found application was not executable. |





**Since:** BeOS R3

---

### `StartWatching()`

```cpp
status_t BRoster::StartWatching(BMessenger target, uint32 eventMask = B_REQUEST_LAUNCHED | B_REQUEST_QUIT)const
```

Adds a new roster application monitor. 


After [StartWatching()](classBRoster.md#a2cd20378ab189c4df1eba833f1079dae) event messages will be sent to the supplied target according to the specified flags until a respective [StopWatching()](classBRoster.md#a5a792a6d4af01978a6c1d55222c70c73) call.


*eventMask* must be a bitwise OR of one or more of the following flags:


* `B_REQUEST_LAUNCHED:` A `B_SOME_APP_LAUNCHED` is sent, whenever an application has been launched.

* `B_REQUEST_QUIT:` A `B_SOME_APP_QUIT` is sent, whenever an application has quit.

* `B_REQUEST_ACTIVATED:` A `B_SOME_APP_ACTIVATED` is sent, whenever an application has been activated.



All event messages contain the following fields supplying more information about the concerned application:


* `"be:signature"`, `B_STRING_TYPE:` The signature of the application.

* `"be:team"`, `B_INT32_TYPE:` The team ID of the application (`team_id`).

* `"be:thread"`, `B_INT32_TYPE:` The ID of the application's main thread (`thread_id`).

* `"be:flags"`, `B_INT32_TYPE:` The application flags (`uint32`).

* `"be:ref"`, `B_REF_TYPE:` An [entry_ref](../storage_kit/structentry__ref.md) referring to the application's executable.



A second call to [StartWatching()](classBRoster.md#a2cd20378ab189c4df1eba833f1079dae) with the same *target* simply sets the new *eventMask*. The messages won't be sent twice to the target.


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | The target the event messages shall be sent to. |
| `eventMask` | Specifies the events the caller is interested in. |





**Returns:** `B_OK` if everything went fine or an error code, if some error occurred.



**Since:** BeOS R4

---

### `StopWatching()`

```cpp
status_t BRoster::StopWatching(BMessenger target)const
```

Removes a roster application monitor added with [StartWatching()](classBRoster.md#a2cd20378ab189c4df1eba833f1079dae). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `target` | The target that shall not longer receive any event messages. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went fine. |
| B_BAD_VALUE | No application monitor has been associated with the specified *target* before. |





**Since:** BeOS R4

---

### `TeamFor()`

```cpp
team_id BRoster::TeamFor(const char * signature)const
```

Returns the team ID of a currently running application with the supplied *signature*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `signature` | The app *signature*. |





**Returns:** The team ID of a running application with the supplied *signature*.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | *signature* is `NULL`. |
| B_ERROR | No application with the supplied *signature* is currently running. |





**Since:** BeOS R3

---

### `TeamFor()`

```cpp
team_id BRoster::TeamFor(entry_ref * ref)const
```

Returns the team ID of a currently running application executing the executable referred to by the supplied [entry_ref](../storage_kit/structentry__ref.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `ref` | The app's [entry_ref](../storage_kit/structentry__ref.md) |





**Returns:** The team ID of a running application executing the file referred to by *ref*.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | *ref* is `NULL`. |
| B_ERROR | No application executing the file referred to by *ref* is currently running. |





**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBRoster.html).
