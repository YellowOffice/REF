---
name: BNotification
type: class
kit: application_kit
brief: "Construct system-default notifications to be displayed to the user"
source: haiku-book
---

# BNotification Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Construct system-default notifications to be displayed to the user. 


Haiku provides a notification system that allows you to display messages to the user. There is quite some flexibility in how the message is presented. You may use this class to build and send the notification. The properties you can set are:


* The [type of notification](classBNotification.md#a4fa33dacdecb98a0d007feecbc678c2e), which can be an information message, a warning, an error, or a progress message.

* The [group](classBNotification.md#aa9560f4753f510f5c1a416983f062903), which allows you to organize notification display into different categories.

* A [title](classBNotification.md#ad01b2804337a3d2a2a97de71b2200c73), which is a distinct text element at the top of a notification view.

* The [content](classBNotification.md#a1ae33572f1ebcd9fb4ac6aad418dbaaa), which is the text message that is shown to the user.

* A [message identifier](classBNotification.md#aa3dd25a096e335700185985060e17e68) that allows you to modify the contents of a message that is being displayed, which is particularly useful for progress notifications.

* For progress notifications, the [percentage of completion](classBNotification.md#a1cdba659820f9a3fd3a36800113e7436) can be set.

* By default the notification uses the application's icon, but you may set an [alternative icon](classBNotification.md#a967120fe3a33bc132b66d3b8e80e58ed).

* Finally there are a few ways you can configure the actions that happen when a user clicks the notification. More on that below.



For example, with the following code, you may display a notification:



```cpp
BNotification notification(B_PROGRESS_NOTIFICATION);
notification.SetGroup("Group");
notification.SetTitle("Title");
notification.SetContent("This is the content");
notification.SetMessageID("mainwindow_progress");
notification.SetProgress(0.5);
notification.Send();
```




Note that in the previous code example, we set a [message identifier](classBNotification.md#aa3dd25a096e335700185985060e17e68), which will allow to update the notification when we have progressed. The use would be:



```cpp
// After sending the notification, you retain ownership so that you can update it
notification.SetProgress(0.7);
 
// In order to display the update, you send it again
notification.Send();
```

Furthermore, it is possible to support some form of follow-up action, when the user clicks the notification. First of all, you need to choose whether you want to [open a specific application](classBNotification.md#ad273375772837f2948a88a1e9d58cbeb), or whether you want to [open a specific file](classBNotification.md#a9e71982001e56a65c742cbd13f84a3c7) and have the system determine which application fits that. Additionally, you may specify [command line arguments](classBNotification.md#ab6613ca8fd4af20fe1401bfdbd9bfbaf) or pass additional [file references](classBNotification.md#ab0323e6d240cef4ea4b8d31748dfe8cc) for the receiving application to process.


Finally, a note about the `notification_server` and how it groups and handles messages coming from your application. The system is aware of the source of the notifications, and identifies your application by it's signature. That means that the identification of your application is consistent, even if it is restarted, or if you have multiple instances running. This impacts the [grouping](classBNotification.md#aa9560f4753f510f5c1a416983f062903) functionality and the [message updating](classBNotification.md#aa3dd25a096e335700185985060e17e68) functionality. If you have an application that can have multiple instances, you will need to make sure that you properly manage your group names and identifiers if you want to keep things separate.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BNotification](#a4d489ddd75407b3a2883ad7fb95ef326) (BMessage *archive) — Construct a notification from an archive.
* [BNotification](#a4fa33dacdecb98a0d007feecbc678c2e) (notification_type type) — Construct an empty message, with the specified type.
* `virtual` [~BNotification](#a7682ffdc4eb03e6275053abcf993b5a7) () — Frees all resources associated with the object.
* `status_t` [AddOnClickArg](#ab6613ca8fd4af20fe1401bfdbd9bfbaf) (const BString &arg) — Add to a list of arguments that are passed to an application when the user clicks on the notification.
* `status_t` [AddOnClickRef](#ab0323e6d240cef4ea4b8d31748dfe8cc) (const entry_ref *ref) — Add a ref to the list of arguments passed when a user clicks the notification.
* `virtual status_t` [Archive](#a8fb050723adcf52d9f8179808c0bea07) (BMessage *archive, bool deep=true) const — Archives the BNotification in the archive.
* `const char *` [Content](#a8c26d427a94033a9a3f8a59c97eb089e) () const — Returns the message of the notification.
* `int32` [CountOnClickArgs](#abe4207c02d859c9c540606092c8be38f) () const — Returns the number of args to be passed when the user clicks on the notification.
* `int32` [CountOnClickRefs](#ae6be8277157147f7b3cc086316b4c401) () const — Returns the number of refs to be passed when the user clicks on the notification.
* `const char *` [Group](#af5739072388055457d3c6978a8452050) () const — Returns the group of the notification.
* `const BBitmap *` [Icon](#a22e167cd5232a79e9dc17756dbc246ef) () const — Returns the icon for the notification.
* `status_t` [InitCheck](#a2df093ced99025ae2ed0b84e23e17ff1) () const — Returns the status of the constructor.
* `const char *` [MessageID](#a7d53fa51193ba570e2df359cef213141) () const — Returns the identifier of the notification.
* `const char *` [OnClickApp](#ab66cb0d4e76fe050bf7a548b62ac68bb) () const — Returns the signature of the application that will be called when the notification is clicked.
* `const char *` [OnClickArgAt](#a5800cb655c9a57d3fc09a8b3747a777c) (int32 index) const — Returns the arg that is stored at index.
* `const entry_ref *` [OnClickFile](#a03804c53c12166a2cad230b633633c41) () const — Returns the reference to the file that will be opened when the notification is clicked.
* `const entry_ref *` [OnClickRefAt](#ae97f2d2f2563442ca056a61838bbb90b) (int32 index) const — Returns the ref that is stored at index.
* `float` [Progress](#a58e816c637be7090021f0ae2e23d276c) () const — Returns the progress for the notification.
* `status_t` [Send](#a8c8d51fc222c94ae28fa292fd1aebe3f) (bigtime_t timeout=-1) — Send the notification to the notification_server.
* `void` [SetContent](#a1ae33572f1ebcd9fb4ac6aad418dbaaa) (const BString &content) — Set a message for the notification.
* `void` [SetGroup](#aa9560f4753f510f5c1a416983f062903) (const BString &group) — Set a group for the notifcation.
* `status_t` [SetIcon](#a967120fe3a33bc132b66d3b8e80e58ed) (const BBitmap *icon) — Set the icon of the notification.
* `void` [SetMessageID](#aa3dd25a096e335700185985060e17e68) (const BString &id) — Sets notification's message identifier.
* `void` [SetOnClickApp](#ad273375772837f2948a88a1e9d58cbeb) (const BString &app) — Set which application should be called when the notification is clicked by the user.
* `status_t` [SetOnClickFile](#a9e71982001e56a65c742cbd13f84a3c7) (const entry_ref *file) — Set which file should be opened when the notification is clicked by the user.
* `void` [SetProgress](#a1cdba659820f9a3fd3a36800113e7436) (float progress) — Sets progress information.
* `void` [SetTitle](#ad01b2804337a3d2a2a97de71b2200c73) (const BString &title) — Set a title for the notification.
* `const char *` [SourceName](#a65f95233321dd342d7dea96ebe7361ea) () const — Returns the name of the application where the notification originated.
* `const char *` [SourceSignature](#a14286e96129adf2266ed6ab3388ad8d5) () const — Returns signature of the application where the notification originated.
* `const char *` [Title](#a62cc78f8d317f3a9bf3e117d66a2305f) () const — Returns the title of the notification.
* `notification_type` [Type](#a916cdcb1c28676bd838e74073b5dbc08) () const — Returns the type of the notification.
* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).

### Static Public Member Functions

* `static BArchivable *` [Instantiate](#a7d8df816c5bf9c62d6e392450a53e367) (BMessage *archive) — Returns a new BNotification object from archive.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BNotification()`

```cpp
BNotification::BNotification(notification_type type)
```

Construct an empty message, with the specified *type*. 


The type influences the style of the notification view. See the [notification_type](Notification_8h.md#a370f98dad9f23a468a12fd1545825b39) enumerator for details.



**Since:** Haiku R1

---

### `BNotification()`

```cpp
BNotification::BNotification(BMessage * archive)
```

Construct a notification from an archive. 



**Since:** Haiku R1

---

### `~BNotification()`

```cpp
BNotification::~BNotification()
```

Frees all resources associated with the object. 



**Since:** Haiku R1

---

### `AddOnClickArg()`

```cpp
status_t BNotification::AddOnClickArg(const BString & arg)
```

Add to a list of arguments that are passed to an application when the user clicks on the notification. 


This method allows you to construct a list of arguments, that will be sent to the application specified by BNotification::AddOnClickApp(), or the one that is associated with BNotification::AddOnClickFile(). The args will be handled by the application's [BApplication::ArgvReceived()](classBApplication.md#a0826684edce56baa7a31c89c97a1d161) hook method.



**Since:** Haiku R1

---

### `AddOnClickRef()`

```cpp
status_t BNotification::AddOnClickRef(const entry_ref * ref)
```

Add a `ref` to the list of arguments passed when a user clicks the notification. 


This method allows you to construct a list of refs, that will be sent to the application specified by BNotification::AddOnClickApp(), or the one that is associated with BNotification::AddOnClickFile(). The refs will be handled by the application's [BApplication::RefsReceived()](classBApplication.md#a5fae9740458d9aec66f3b1d5c50fae87) hook method.



**Since:** Haiku R1

---

### `Archive()`

```cpp
status_t BNotification::Archive(BMessage * archive, bool deep = true)const
```

Archives the [BNotification](classBNotification.md) in the `archive`. 



**See also:** [BArchivable::Archive()](../support_kit/classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44), [Instantiate()](classBNotification.md#a7d8df816c5bf9c62d6e392450a53e367) static function.



**Returns:** `B_OK:` if everything went fine, or other errors that describe why archiving has failed.



**Since:** Haiku R1


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44).

---

### `Content()`

```cpp
const char * BNotification::Content()const
```

Returns the message of the notification. 



**Returns:** The message of the notification as a string.



**Since:** Haiku R1

---

### `CountOnClickArgs()`

```cpp
int32 BNotification::CountOnClickArgs()const
```

Returns the number of args to be passed when the user clicks on the notification. 



**See also:** [BNotification::AddOnClickArg()](classBNotification.md#ab6613ca8fd4af20fe1401bfdbd9bfbaf)



**Since:** Haiku R1

---

### `CountOnClickRefs()`

```cpp
int32 BNotification::CountOnClickRefs()const
```

Returns the number of refs to be passed when the user clicks on the notification. 



**See also:** [BNotification::AddOnClickRef()](classBNotification.md#ab0323e6d240cef4ea4b8d31748dfe8cc)



**Since:** Haiku R1

---

### `Group()`

```cpp
const char * BNotification::Group()const
```

Returns the group of the notification. 



**See also:** [BNotification::SetGroup()](classBNotification.md#aa9560f4753f510f5c1a416983f062903) for more information about groups.



**Returns:** The string of the notification's group.



**Since:** Haiku R1

---

### `Icon()`

```cpp
const BBitmap * BNotification::Icon()const
```

Returns the icon for the notification. 



**See also:** [BNotification::SetIcon()](classBNotification.md#a967120fe3a33bc132b66d3b8e80e58ed) for more information on this property.



**Returns:** Returns a borrowed unchangeable reference to the icon.



**Since:** Haiku R1

---

### `InitCheck()`

```cpp
status_t BNotification::InitCheck()const
```

Returns the status of the constructor. 



**Since:** Haiku R1

---

### `Instantiate()`

```cpp
static BArchivable * BNotification::Instantiate(BMessage * archive)
```

Returns a new [BNotification](classBNotification.md) object from *archive*. 


This class implements the archiving API, and as such, you can build a new [BNotification](classBNotification.md) object from a previously created [BMessage](classBMessage.md) archive. However, if the message doesn't contain an archived data for a [BNotification](classBNotification.md) object, this method returns `NULL`.



**Returns:** [BNotification](classBNotification.md) object from *archive* or `NULL` if it doesn't contain a valid [BNotification](classBNotification.md) object.



**Since:** Haiku R1

---

### `MessageID()`

```cpp
const char * BNotification::MessageID()const
```

Returns the identifier of the notification. 



**See also:** [BNotification::SetMessageID()](classBNotification.md#aa3dd25a096e335700185985060e17e68) for the purpose of having an identifier.



**Returns:** The identifier of the notification as a string.



**Since:** Haiku R1

---

### `OnClickApp()`

```cpp
const char * BNotification::OnClickApp()const
```

Returns the signature of the application that will be called when the notification is clicked. 



**See also:** More information about this property in [BNotification::SetOnClickApp()](classBNotification.md#ad273375772837f2948a88a1e9d58cbeb).



**Since:** Haiku R1

---

### `OnClickArgAt()`

```cpp
const char * BNotification::OnClickArgAt(int32 index)const
```

Returns the arg that is stored at `index`. 



**See also:** [BNotification::AddOnClickArg()](classBNotification.md#ab6613ca8fd4af20fe1401bfdbd9bfbaf)



**Since:** Haiku R1

---

### `OnClickFile()`

```cpp
const entry_ref * BNotification::OnClickFile()const
```

Returns the reference to the file that will be opened when the notification is clicked. 



**See also:** More information about this property in [BNotification::SetOnClickFile()](classBNotification.md#a9e71982001e56a65c742cbd13f84a3c7).



**Since:** Haiku R1

---

### `OnClickRefAt()`

```cpp
const entry_ref * BNotification::OnClickRefAt(int32 index)const
```

Returns the ref that is stored at `index`. 



**See also:** [BNotification::AddOnClickRef()](classBNotification.md#ab0323e6d240cef4ea4b8d31748dfe8cc)



**Since:** Haiku R1

---

### `Progress()`

```cpp
float BNotification::Progress()const
```

Returns the progress for the notification. 



**See also:** [BNotification::SetProgress()](classBNotification.md#a1cdba659820f9a3fd3a36800113e7436) for more information about this value.



**Returns:** A value between 0.0 and 1.0 if notification's type is `B_PROGRESS_NOTIFICATION`, or otherwise -1.



**Since:** Haiku R1

---

### `Send()`

```cpp
status_t BNotification::Send(bigtime_t timeout = -1)
```

Send the notification to the notification_server. 


The notification is delivered asynchronously to the notification_server, which will display it according to its settings and filters.


After sending, you retain ownership of the notification. The advantage is that you can re-use the notification at a later moment, or use the object to update the notification. See [BNotification::SetMessageID()](classBNotification.md#aa3dd25a096e335700185985060e17e68) about updating displayed notifications. If you allocate the notification on the heap, be sure to free the memory.


Parameters

| Parameter | Description |
| :--- | :--- |
| `timeout` | The *timeout* in microsecond that the notification should be displayed. If you want to use the default timing, use the default argument or pass `-1`. |





**Returns:** `B_OK` if everything went fine, `B_BAD_PORT_ID` if there was a problem connecting to the `notification_server`, or any other errors if something went wrong transmitting the notification.



**Since:** Haiku R1

---

### `SetContent()`

```cpp
void BNotification::SetContent(const BString & content)
```

Set a message for the notification. 



**Since:** Haiku R1

---

### `SetGroup()`

```cpp
void BNotification::SetGroup(const BString & group)
```

Set a group for the notifcation. 


The default behaviour of the `notification_server` is group the visible notifications per running application, and then in order in which they have been received. There may be situations where you want to override that behavior and group related notifications. When you set a group name, the `notification_server` will create a box with the `group` name as label, and insert all related notifications in that box.






**Since:** Haiku R1

---

### `SetIcon()`

```cpp
status_t BNotification::SetIcon(const BBitmap * icon)
```

Set the icon of the notification. 


Set the icon for the notification. By default, the application icon is used. This method makes a copy of the *icon*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `icon` | The icon that should be displayed with the notification. |





**Returns:** `B_OK` if everything went fine, `B_NO_MEMORY` when the *icon* could not be copied, or another error if something else went wrong.



**Since:** Haiku R1

---

### `SetMessageID()`

```cpp
void BNotification::SetMessageID(const BString & id)
```

Sets notification's message identifier. 


If you want to update the contents of an existing notification, you can set a identifier for this message. When you send a new or updated message with the same identifier, the `notification_server` will update the existing message with the new content.


In order to effectively use this feature, you will have to make sure the identifier is unique within the current application.



**Since:** Haiku R1

---

### `SetOnClickApp()`

```cpp
void BNotification::SetOnClickApp(const BString & app)
```

Set which application should be called when the notification is clicked by the user. 


The value `app` should be a valid application signature, for example `'application/x-vnd.Haiku-StyledEdit'`.


Using this property has precedence on when [BNotification::SetOnClickFile()](classBNotification.md#a9e71982001e56a65c742cbd13f84a3c7) is used. If you want interacting with the notification opening a specific file, then you should use this method in combination with [BNotification::AddOnClickRef()](classBNotification.md#ab0323e6d240cef4ea4b8d31748dfe8cc).



**See also:** Additional actions and parameters can be set through [BNotification::SetOnClickFile()](classBNotification.md#a9e71982001e56a65c742cbd13f84a3c7), [BNotification::AddOnClickRef()](classBNotification.md#ab0323e6d240cef4ea4b8d31748dfe8cc) and [BNotification::AddOnClickArg()](classBNotification.md#ab6613ca8fd4af20fe1401bfdbd9bfbaf).



**Since:** Haiku R1

---

### `SetOnClickFile()`

```cpp
status_t BNotification::SetOnClickFile(const entry_ref * file)
```

Set which file should be opened when the notification is clicked by the user. 


The file will be opened by the default application for this file type.


You cannot use this action in combination with [BNotification::SetOnClickApp()](classBNotification.md#ad273375772837f2948a88a1e9d58cbeb). If you use this way of setting an action, this action will be ignored.



**See also:** Additional actions and parameters can be set through [BNotification::SetOnClickApp()](classBNotification.md#ad273375772837f2948a88a1e9d58cbeb), [BNotification::AddOnClickRef()](classBNotification.md#ab0323e6d240cef4ea4b8d31748dfe8cc) and [BNotification::AddOnClickArg()](classBNotification.md#ab6613ca8fd4af20fe1401bfdbd9bfbaf).



**Since:** Haiku R1

---

### `SetProgress()`

```cpp
void BNotification::SetProgress(float progress)
```

Sets progress information. 


When you are building a notification of the type `B_PROGRESS_NOTIFICATION` the notification view will show a progress bar and a label that expresses the progress in a percentage. Using this method you can set what the bar and label express.


The valid range is between 0.0 and 1.0. If `progress` is lower than 0.0 (i.e. negative), the value will be set to 0.0. If it is higher than 1.0, it will be set to 1.0.



**Since:** Haiku R1

---

### `SetTitle()`

```cpp
void BNotification::SetTitle(const BString & title)
```

Set a title for the notification. 



**Since:** Haiku R1

---

### `SourceName()`

```cpp
const char * BNotification::SourceName()const
```

Returns the name of the application where the notification originated. 


When you build your own notifications, this will contain the name of the current application. If you receive notifications from other applications, it will include theirs.



**Returns:** Name of the source application.



**Since:** Haiku R1

---

### `SourceSignature()`

```cpp
const char * BNotification::SourceSignature()const
```

Returns signature of the application where the notification originated. 


When you build your own notifications, this will contain the signature of the current application. If you receive notifications from other applications, it will include theirs.



**Returns:** Signature of the source application.



**Since:** Haiku R1

---

### `Title()`

```cpp
const char * BNotification::Title()const
```

Returns the title of the notification. 



**Returns:** The title of the notification as a string.



**Since:** Haiku R1

---

### `Type()`

```cpp
notification_type BNotification::Type()const
```

Returns the type of the notification. 



**Returns:** A value of the `notification_type` enum that represents notification type.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBNotification.html).
