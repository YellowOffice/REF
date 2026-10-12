---
name: BArchivable
type: class
kit: support_kit
brief: "Interface for objects that can be archived into a BMessage"
source: haiku-book
---

# BArchivable Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Interface for objects that can be archived into a [BMessage](../application_kit/classBMessage.md). 


[BArchivable](classBArchivable.md) provides an interface for objects that can be put into message archives and extracted into objects in another location. Using this you are able to send objects between applications, or even between computers across networks.


[BArchivable](classBArchivable.md) differs from [BFlattenable](classBFlattenable.md) in that [BFlattenable](classBFlattenable.md) is designed to store objects into flat streams of data, the main objective being storage to disk. The objective of this interface, however, is to store objects that will later be restored as new (but identical) objects. To illustrate this point, [BArchivable](classBArchivable.md) objects can be restored automatically to the correct class, whereas [BFlattenable](classBFlattenable.md) objects have a data type which you need to map to classes manually.


Archiving is done with the [Archive()](classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44) method. If your class supports it, the caller can request it to store into a deep archive, meaning that all child objects in it will be stored. Extracting the archive works with the [Instantiate()](classBArchivable.md#a04efcb17fa2a64a776923cc12303efcd) method, which is static. Since the interface is designed to extract objects without the caller knowing what kind of object it actually is, the global function [instantiate_object()](group__support__globals.md#gac98d3af4a84cd0880d8a853f7c526764) instantiates a message without you manually having to determine the class the message is from. This adds considerable flexibility and allows [BArchivable](classBArchivable.md) to be used in combination with other add-ons.


To provide this interface in your classes you should publicly inherit this class. You should implement [Archive()](classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44) and [Instantiate()](classBArchivable.md#a04efcb17fa2a64a776923cc12303efcd), and provide one constructor that takes one [BMessage](../application_kit/classBMessage.md) argument.


If your class holds references to other [BArchivable](classBArchivable.md) objects that you wish to archive, then you should consider using the [BArchiver](classBArchiver.md) and [BUnarchiver](classBUnarchiver.md) classes in your [Archive()](classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44) method and archive constructor, respectively. You should also consider implementing the [AllArchived()](classBArchivable.md#a4075315c407443a3b0dbb3d7551b53c9) and [AllUnarchived()](classBArchivable.md#a2b1d74c147ea18e4b4bfacd42f11e0d2) methods, which were designed to ease archiving and unarchiving in such a situation.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).

### Static Public Member Functions

* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BArchivable()`

```cpp
BArchivable::BArchivable(BMessage * from)
```

Constructor. Does important behind-the-scenes work in the unarchiving process. 


If you inherit this interface you should provide at least one constructor that takes one [BMessage](../application_kit/classBMessage.md) argument. In that constructor, you should call your parent class' archive constructor (even if your parent class is [BArchivable](classBArchivable.md)).



**Since:** BeOS R3

---

### `BArchivable()`

```cpp
BArchivable::BArchivable()
```

Constructor. Does nothing. 



**Since:** BeOS R3

---

### `~BArchivable()`

```cpp
BArchivable::~BArchivable()
```

Destructor. Does nothing. 



**Since:** BeOS R3

---

### `AllArchived()`

```cpp
status_t BArchivable::AllArchived(BMessage * into)const
```

Method relating to the use of `BArchiver`. 


This hook function is called once the first [BArchiver](classBArchiver.md) that was created in an archiving session is either destroyed, or has its Finish() method called. Implementations of this method can be used, in conjunction with [BArchiver::IsArchived()](classBArchiver.md#a77f099b123416c719be2cd78eb999d19), to reference objects in your archive that you do not own, depending on whether or not those objects were archived by their owners. Implementations of this method should call the implementation of their parent class, the same as for the [Archive()](classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44) method.



> [!WARNING]
> To guarantee that your [AllArchived()](classBArchivable.md#a4075315c407443a3b0dbb3d7551b53c9) method will be called during archival, you must create a [BArchiver](classBArchiver.md) object in your [Archive()](classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44) implementation.



**See also:** [BArchiver](classBArchiver.md) [BArchiver::Finish()](classBArchiver.md#a7c82dbc0fb42795c575ac2c6a5405297)



**Since:** Haiku R1


Reimplemented in [BAbstractLayout](classBAbstractLayout.md#a73b50e5ee03b980b4e8f08c875528162), [BCardLayout](../interface_kit/classBCardLayout.md#ac561655882cd31e4f8a8b214de846fb6), [BLayout](../interface_kit/classBLayout.md#ab9747436e251333693d54d29d472e2f9), [BView](../interface_kit/classBView.md#a561e82ed41cbb93d3bacf371787497bf), [BGridLayout](classBGridLayout.md#adddbabf3f060e0e3d20af12cf3f3dab1), [BGroupLayout](classBGroupLayout.md#a62670753e05e05601592d49f0b5f438f), [BLayoutItem](../interface_kit/classBLayoutItem.md#a13ec3faa075b23b3073f97531365102c), [BMenuField](../interface_kit/classBMenuField.md#ae8acba317c58f2767aae7956974536c9), [BSplitView](classBSplitView.md#a8677380375e36b4bc2380a929dc69a69), [BTextControl](../interface_kit/classBTextControl.md#a5b73780d200fa037f99f6cec5cbf74ec), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#adb001699008fe0cb2eff51661da175e6).

---

### `AllUnarchived()`

```cpp
status_t BArchivable::AllUnarchived(const BMessage * archive)
```

Method relating to the use of `BUnarchiver`. 


This hook function is called triggered in the [BUnarchiver::Finish()](classBUnarchiver.md#a7640fa5d84dc6dca19d7513326d2bba2) method. In this method, you can rebuild references to objects that may be direct children of your object, or may be children of other objects. Implementations of this method should call the implementation of their parent class, the same as for the [Archive()](classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44) method.



> [!WARNING]
> To guarantee that your [AllUnarchived()](classBArchivable.md#a2b1d74c147ea18e4b4bfacd42f11e0d2) method will be called during unarchival, you must create a [BUnarchiver](classBUnarchiver.md) object in your archive constructor.



**See also:** [BUnarchiver](classBUnarchiver.md), [BUnarchiver::Finish()](classBUnarchiver.md#a7640fa5d84dc6dca19d7513326d2bba2)



**Since:** Haiku R1


Reimplemented in [BScrollView](../interface_kit/classBScrollView.md#adfed255a897cd481127f6b911b329c3d), [BView](../interface_kit/classBView.md#ab7bd04272afed8b28bf57d1de33cbe05), [BAbstractLayout](classBAbstractLayout.md#a2664ac14ab5dbe33a18cee88d420aa22), [BCardLayout](../interface_kit/classBCardLayout.md#a30c68436cd5efd9708c1cfd75655647a), [BGridLayout](classBGridLayout.md#a2cd9bd9915c14ac32c0081234e12a5fb), [BGroupLayout](classBGroupLayout.md#a25bd4f838e672aa3eb611a616c5ec5e0), [BLayout](../interface_kit/classBLayout.md#a3517e73d524672645425f80ebd4f53c7), [BLayoutItem](../interface_kit/classBLayoutItem.md#af78b72941cf1532299c2396cfeb7f9ed), [BMenuField](../interface_kit/classBMenuField.md#ad7e9ecb63a3df86c848bf8a9e7409ee7), [BSplitView](classBSplitView.md#a5c4cc359d801e27e39f28469c24bbd76), [BTabView](../interface_kit/classBTabView.md#a6cc6ca514c10001b8610e5937f96b48e), [BTextControl](../interface_kit/classBTextControl.md#abc5bfb77b1ab96dddec5c37d76657a89), and [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#a67ba660a95e7cf8647be8835184b6cc3).

---

### `Archive()`

```cpp
status_t BArchivable::Archive(BMessage * into, bool deep = true)const
```

Archive the object into a [BMessage](../application_kit/classBMessage.md). 


You should call this method from your derived implementation as it adds the data needed to instantiate your object to the message.


Parameters

| Parameter | Description |
| :--- | :--- |
| `into` | The message you store your object in. |
| `deep` | If `true`, all children of this object should be archived as well. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The archive operation was successful. |
| B_BAD_VALUE | `NULL` *archive* message. |
| B_ERROR | The archive operation failed. |





**Since:** BeOS R3


Reimplemented in [BCollator](../locale_kit/classBCollator.md#a6ad070bcec766bb2e4b3963f2af53e90), [BCursor](../application_kit/classBCursor.md#acae76743745b2ed1fd08de01edab9279), [BNotification](../application_kit/classBNotification.md#a8fb050723adcf52d9f8179808c0bea07), [BBox](../interface_kit/classBBox.md#abd1a762e132a6196076617cee1eb81ac), [BListItem](../interface_kit/classBListItem.md#a3fa7ca1250e123e3cf1488b1d88901d3), [BMenu](../interface_kit/classBMenu.md#a71bed24f541bdfb690863118ce3f716b), [BMenuBar](../interface_kit/classBMenuBar.md#af4ae9bcc3c1cbe560e745c9868fb9c5f), [BMenuField](../interface_kit/classBMenuField.md#ada677e4339d5a5eca5c945c4165b6a3e), [BMenuItem](../interface_kit/classBMenuItem.md#a0e31758c36db589a4549549ead272f6b), [BOutlineListView](../interface_kit/classBOutlineListView.md#af590f60f193f47989f63c34dda0e6916), [BPictureButton](../interface_kit/classBPictureButton.md#ab476f82e9d75a3b4a9b54ca35d1ad036), [BPopUpMenu](../interface_kit/classBPopUpMenu.md#af81e6dc2ddcc3063eb33a1a5cf3b9088), [BScrollBar](../interface_kit/classBScrollBar.md#a2d8cea93fe440bbed02685c135b0f802), [BScrollView](../interface_kit/classBScrollView.md#a7858c5f97152c910831db817b80f5f95), [BShape](../interface_kit/classBShape.md#ae132d554f4df208974b5019436ad1b36), [BShelf](../interface_kit/classBShelf.md#a098c2a557715a3a4fa91a66125653f0e), [BStatusBar](../interface_kit/classBStatusBar.md#a05e0e95a3cee49d1fa7f1a48e26ae20b), [BStringItem](../interface_kit/classBStringItem.md#acf33097176356dbfbe1229d40ca4453a), [BStringView](../interface_kit/classBStringView.md#adbafb44b6614c69a645d3e2de818c5f5), [BTextControl](../interface_kit/classBTextControl.md#af68449ec551e8a089a441fd270954b99), [BTextView](../interface_kit/classBTextView.md#a0f3fb624378a2d13617773713efedd98), [BView](../interface_kit/classBView.md#ab6de1b48cbc3ef15a0d02113036f002d), [BWindow](../interface_kit/classBWindow.md#a69163d40d8f1eda77c9134ad4ab745a2), [BApplication](../application_kit/classBApplication.md#aa36536582835264341376064cbc96a27), [BHandler](../application_kit/classBHandler.md#ac2711ccff5e7f711244c88a5642c83db), [BLooper](../application_kit/classBLooper.md#a791ef8664f674b6683d551762888f1c2), [BDirectWindow](../game_kit/classBDirectWindow.md#a39e69ba4bba5221b3099cf34129862c8), [BAlert](../interface_kit/classBAlert.md#aba312ca5f7e668bf4d96efc7f41625a3), [BBitmap](../interface_kit/classBBitmap.md#a331444d4bc838444f65f534cbbd66f41), [BButton](../interface_kit/classBButton.md#adce5e4839a58c3bb85965398a490d720), [BChannelControl](../interface_kit/classBChannelControl.md#aa71189c8b008cb3329c17b58f786617e), [BCheckBox](../interface_kit/classBCheckBox.md#a75511a8252ef3ffa1177f57af97b67ca), [BColorControl](../interface_kit/classBColorControl.md#a6437907efd1d39a492db1f55b5f4dc36), [BControl](../interface_kit/classBControl.md#a2581a447a34eef102c62d0e998155290), [BDragger](../interface_kit/classBDragger.md#aece5cd86ccd46a23f1188697f4bffa55), [BListView](../interface_kit/classBListView.md#a89277e72296cc9ec516777e000f100e3), [BPicture](../interface_kit/classBPicture.md#a9854a69b51d30728a20fd8688ce7a0f0), [BRadioButton](../interface_kit/classBRadioButton.md#aeed1a7a2142b1ac7b1499234f884caae), [BSeparatorItem](../interface_kit/classBSeparatorItem.md#a37151f2e9c361bb173e016bca536dd9e), [BTab](../interface_kit/classBTab.md#aac9d5205065158ab4079c2b8913c495d), [BAbstractLayout](classBAbstractLayout.md#a76c6e663adb27a10972dafe22c898bf7), [BCardLayout](../interface_kit/classBCardLayout.md#a0cfce7f1c906b28d8e3abaca74bcda56), [BChannelSlider](../interface_kit/classBChannelSlider.md#ac216b412d86275115516b886c4f9b578), [BGridLayout](classBGridLayout.md#aab5e2df95091bb76bb93628dcd01013e), [BGroupLayout](classBGroupLayout.md#aae43bdb3a725755664e55f13a054b510), [BLayout](../interface_kit/classBLayout.md#a0d5f0b0a3ca81f5f7d54dae6ab7a099f), [BLayoutItem](../interface_kit/classBLayoutItem.md#af2c2593e6179ee367ef26eff7ab7409f), [BSeparatorView](../interface_kit/classBSeparatorView.md#a41d7d43196ee70cc26986f95b5c3e262), [BSpaceLayoutItem](classBSpaceLayoutItem.md#a27a757bd5903c14dce5a54af00177d4a), [BSplitView](classBSplitView.md#a2c4ab843dd62815ebeb7201e21d3199b), [BTabView](../interface_kit/classBTabView.md#a3354f9343238295b7ed0a24339106cd5), [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#a405b207a3fa1770d5349de6d66705390), [BUrl](classBUrl.md#a7a31ffee9b9a2a2c0ed5e1469926b0fa), and [BTranslatorRoster](../translation_kit/classBTranslatorRoster.md#a3da914e839d12c865bfc1f7a89d902e9).

---

### `Instantiate()`

```cpp
static BArchivable * BArchivable::Instantiate(BMessage * archive)
```

Static member to restore objects from messages. 


You should always check that the *archive* argument actually corresponds to your class. The automatic functions, such as [instantiate_object()](group__support__globals.md#gac98d3af4a84cd0880d8a853f7c526764) and [BUnarchiver::InstantiateObject()](classBUnarchiver.md#a3bf0c1cbca1644015d17850424d0c374) will not choose the wrong class but manual calls to this member might be faulty. You can verify that `archive` stores an object of your class with the [validate_instantiation()](group__support__globals.md#gae5dd9c83f4d3ab639edd84deb6bfd1c5) function.


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The message with the data of the object to restore. |





**Returns:** A pointer to a [BArchivable](classBArchivable.md) object.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| You | should return a pointer to the object you create with `archive`, or `NULL` if the unarchival fails. |





> [!WARNING]
> The default implementation will always return `NULL`. Even though it is possible to store plain [BArchivable](classBArchivable.md) objects, it is impossible to restore them.



**See also:** [instantiate_object(BMessage*)](group__support__globals.md#ga1ad60dbee75973620a85b2559e02d62d)



**Since:** BeOS R3

---

### `Perform()`

```cpp
status_t BArchivable::Perform(perform_code d, void * arg)
```

Perform some action (Internal method defined for binary compatibility purposes). 


Reimplemented in [BPopUpMenu](../interface_kit/classBPopUpMenu.md#a8f92a8866c4ffd63cdfcf07957f5ba22), [BDirectWindow](../game_kit/classBDirectWindow.md#a113afd3534fca8b81bcc86f8e55738be), [BListItem](../interface_kit/classBListItem.md#a4b764176db576c63b8bedda260c76f91), [BListView](../interface_kit/classBListView.md#aa0afeb194104738a01c7e60195fe50d0), [BPicture](../interface_kit/classBPicture.md#acb9a2bdcbad655692e126a3dc2be3166), [BStringItem](../interface_kit/classBStringItem.md#a68a5af5b0d0c958fa9528090c1ec6bcf), [BCheckBox](../interface_kit/classBCheckBox.md#abcac265789890adbf485f42d34d8c8e3), [BDragger](../interface_kit/classBDragger.md#ad47a007f4126b9847a315263aa64ad93), [BMenuBar](../interface_kit/classBMenuBar.md#a4b8a4e16ace175bc3bad9d6ef6b42daf), [BOutlineListView](../interface_kit/classBOutlineListView.md#acb2775731d5da2cf52995e4d0b75c1d6), [BPictureButton](../interface_kit/classBPictureButton.md#a57e7eef2e379994c13b8c93eeb5cf3c5), [BSeparatorView](../interface_kit/classBSeparatorView.md#af56310d344ae63781e6b299d56c34e99), [BShelf](../interface_kit/classBShelf.md#afbf73f485603cf3a50ff1bd4c99d9a6a), [BTextView](../interface_kit/classBTextView.md#a6519856e1dbf6e021911529b8a0a15c6), [BView](../interface_kit/classBView.md#a512a6c8dca1a62b14cdcb1c22070129b), [BWindow](../interface_kit/classBWindow.md#afde7d74e5526f740dedb82a1d10faa7a), [BApplication](../application_kit/classBApplication.md#ab8fea9f4a96bdee62ce77a089d472973), [BHandler](../application_kit/classBHandler.md#a4e6ebc7ebcb72855a1f0fee7bde99766), [BLooper](../application_kit/classBLooper.md#adfc642544ce22888d412e6a4be25fa72), [BAbstractLayout](classBAbstractLayout.md#aa4d7d592de1e566f73f440576d1c2cac), [BAlert](../interface_kit/classBAlert.md#a3d2769c5bf9b9822f21770e38e561fd6), [BBox](../interface_kit/classBBox.md#adcd9b77028e7c820ce29a8a9db950adb), [BButton](../interface_kit/classBButton.md#aee74330d076b7b8487fe21443118b03d), [BCardLayout](../interface_kit/classBCardLayout.md#a7b75708b091f51e8dce826477f28e33a), [BCardView](classBCardView.md#aa784b33c5b2c62791cf86fa38d1704ba), [BControl](../interface_kit/classBControl.md#a0b32524cd2abfb7ea37b9988b180c733), [BGridLayout](classBGridLayout.md#a0ab603b381b9ba4d7efb3efbeae4940f), [BGridView](classBGridView.md#a1409f66c0dfe65882e3bfa3b0fe000dc), [BGroupLayout](classBGroupLayout.md#a31d82f6cd2fdecdc0a04d60d6e3943f7), [BGroupView](../interface_kit/classBGroupView.md#ad8e96a8f8d76e75b5bb6815866529112), [BLayout](../interface_kit/classBLayout.md#adb8e95073f7626f04fe78337ca7114f8), [BLayoutItem](../interface_kit/classBLayoutItem.md#a38b237fb8bbd1d0054e3a2b4cbc1fd15), [BMenu](../interface_kit/classBMenu.md#a6dedb98c6ba5ffbc44893ff43785c93c), [BMenuField](../interface_kit/classBMenuField.md#a78923e5f07ff7c288980a72f6a953001), [BScrollBar](../interface_kit/classBScrollBar.md#adfb4e4e74d00970fd154c652e467b66e), [BScrollView](../interface_kit/classBScrollView.md#a1bd8a27f2883ca0e6b5b9dde0e9e638a), [BSplitView](classBSplitView.md#a9aaf09f717a61303d5aca6e92d96b103), [BStatusBar](../interface_kit/classBStatusBar.md#a4b9eb3ec267be64d9293af3b920c48de), [BTabView](../interface_kit/classBTabView.md#a708fd8766fddb7b0cd72566c57c2977a), [BTwoDimensionalLayout](classBTwoDimensionalLayout.md#aac851d9c86397296d0e7e69716c01926), [BRadioButton](../interface_kit/classBRadioButton.md#a44c726ed88d3a132e9d3055ebf98f3e6), and [BTab](../interface_kit/classBTab.md#a4db961b6bd5104b4c9d76b6136bd6856).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBArchivable.html).
