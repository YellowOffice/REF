---
name: BMessage
type: class
kit: application_kit
brief: "A container that can be send and received using the Haiku messaging subsystem"
source: haiku-book
---

# BMessage Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A container that can be send and received using the Haiku messaging subsystem. 


This class is at the center of the web of messaging classes, in the sense that it defines the actual structure of the messages. Messages have two **important elements**: the [what](classBMessage.md#ad074faab0857f51fba778f0d8558df1e) identifier, and the data members. The first can be directly manipulated, the latter can be manipulated through [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad), [FindData()](classBMessage.md#a1e896648ee668dd5d6c8a4311d6cfa94) and [ReplaceData()](classBMessage.md#a79bc7d526090a5b1f4d8958d72e55d31) and their derivatives. Neither of these elements are mandatory.


The second important role of [BMessage](classBMessage.md) is that it stores **meta data**: who sent the message and with what intention? The methods of [BMessage](classBMessage.md) will disclose if the message was a reply ([IsReply()](classBMessage.md#a01c7dd891b3b05eb7f458a621c5181d4)), where it came from ([IsSourceRemote()](classBMessage.md#a3735f85fdf75af5309d0e61279d452c3)), whether a reply is expected ([IsSourceWaiting()](classBMessage.md#acd51918e26e998067ee6412a55068abc)), and in case the message is a reply, what it's a reply to ([Previous()](classBMessage.md#a57c84d02e54ef19fd1516d9bf7e3fe45)).


Mostly, messages are used to pass information between the the objects in your application, but because messages are such flexible data containers, they are also often used for other **data storage purposes**. Many applications store their settings as messages. Because messages can be flattened to data streams (such as files), they provide an easy but powerful tool for data storage.


All methods can be classified in these areas:


* Adding, Finding, Replacing and Removing Data.

* Statistics and Miscellaneous information.

* Delivery information.

* Utilities to reply to messages.



To see how messages fit in with the greater picture, have a look at the [Messaging Introduction](app_messaging.md).



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BMessage](#a2d0749c439c93a1ca938378b6c890d07) () — Construct an empty message, without any data members and with a what constant set to 0.
* [BMessage](#a6ab8aaec65db99134ea76790884c3af7) (const BMessage &other) — Construct a new message that is a copy of another message.
* [BMessage](#ae56247b7b613c0b1b626d1ea57f5beab) (uint32 what) — Construct an empty message with the what member set to the specified value.
* `virtual` [~BMessage](#a264503e3c60e6ddbc5512ab69e4b336e) () — Free the data members associated with the message.
* `BMessage &` [operator=](#a1e1473dc796d132c5bfe00412aa84a12) (const BMessage &other) — Copy one message into another.
* `void *` [operator new](#a9f516c2831c6185460f0867cdb18ffec) (size_t size) — Allocates size bytes of memory for a BMessage.
* `void *` [operator new](#a74b2733acbeb02a5688fa76cd15811b0) (size_t, void *pointer) — Allocates size bytes of memory for a BMessage.
* `void *` [operator new](#a28f0b7a5e132048e2966a99367342552) (size_t, const std::nothrow_t &noThrow) — Allocates size bytes of memory for a BMessage.
* `void` [operator delete](#abab1f65386f27ad49ae8b767c69bbb39) (void *pointer, size_t size) — Frees memory allocated by new.
* `status_t` [GetInfo](#a48d11318915368351b481984af21baee) (type_code typeRequested, int32 index, char **nameFound, type_code *typeFound, int32 *countFound=NULL) const — Retrieve the name, the type and the number of items in a message by an index.
* `status_t` [GetInfo](#a525991f82f8574bd6eb68796568eb340) (const char *name, type_code *typeFound, int32 *countFound=NULL) const — Retrieve the type and the number of data items in this message that are associated with a name.
* `status_t` [GetInfo](#a6c8080ba2bdff134fd20e923145e4200) (const char *name, type_code *typeFound, bool *fixedSize) const — Retrieve the type and whether or not the size of the data is fixed associated with a name.
* `status_t` [GetInfo](#a055eb9be666ebf7adad3880083606bb3) (const char *name, type_code *typeFound, int32 *countFound, bool *fixedSize) const — Retrieve the type and whether or not the size of the data is fixed associated with a name.
* `int32` [CountNames](#abca8c45f6dffd0f8e95d61ce8527b50f) (type_code type) const — Count the number of names of a certain type.
* `bool` [IsEmpty](#a773590d77b8d751ce9249e6acf3a463b) () const — Check if the message has data members.
* `bool` [IsSystem](#a74a596ec83515e50217ab478f302bd99) () const — Check if the message is a system message.
* `bool` [IsReply](#a01c7dd891b3b05eb7f458a621c5181d4) () const — Check if the message is a reply to a (previous) message.
* `void` [PrintToStream](#a6aa2006d1e5c6fcba3f5c6e8467a50a1) () const — Print the message to the standard output.
* `status_t` [Rename](#a2191de782a8ccef0252007d87c8f379c) (const char *oldEntry, const char *newEntry) — Rename a data label.
* `bool` [WasDelivered](#aaddd7356ffcac4ab4d6a26e8d393e12a) () const — Check if this message was delivered through the delivery methods.
* `bool` [IsSourceWaiting](#acd51918e26e998067ee6412a55068abc) () const — Check if the sender expects a reply.
* `bool` [IsSourceRemote](#a3735f85fdf75af5309d0e61279d452c3) () const — Check if the message is sent by another application.
* `BMessenger` [ReturnAddress](#a50545f6ec66e4f1fdda026381bca0be4) () const — Get a messenger that points to the sender of the message.
* `const BMessage *` [Previous](#a57c84d02e54ef19fd1516d9bf7e3fe45) () const — Get the message to which this message is a reply.
* `bool` [WasDropped](#ac66a35a4ef389a02bc36ace2cddb073e) () const — Check if the message was delivered through 'drag and drop'.
* `BPoint` [DropPoint](#a6785e345338000b685a3b5b182cc993a) (BPoint *offset=NULL) const — Get the coordinates of the drop point of the message.
* `status_t` [SendReply](#aad1eb085346e2c91133e372e7924637c) (uint32 command, BHandler *replyTo=NULL) — Asynchronously send a reply to this message.
* `status_t` [SendReply](#a08a2f161642de20dc483afb0ac4db167) (BMessage *reply, BHandler *replyTo=NULL, bigtime_t timeout=B_INFINITE_TIMEOUT) — Asynchronously send a reply to this message.
* `status_t` [SendReply](#a410113620d52a30f7622a96f8a7077c6) (BMessage *reply, BMessenger replyTo, bigtime_t timeout=B_INFINITE_TIMEOUT) — Asynchronously send a reply to this message.
* `status_t` [SendReply](#a039a8ff8563bbc58c54a50ca417ac75e) (uint32 command, BMessage *replyToReply) — Synchronously send a reply to this message, and wait for a reply back.
* `status_t` [SendReply](#a5461fc22f8bf044d21fd5429b7977213) (BMessage *reply, BMessage *replyToReply, bigtime_t sendTimeout=B_INFINITE_TIMEOUT, bigtime_t replyTimeout=B_INFINITE_TIMEOUT) — Synchronously send a reply to this message, and wait for a reply back.
* `ssize_t` [FlattenedSize](#a2e3967d45e2ab17e6ab05dc45989f8c6) () const — Return the size in bytes required when you want to flatten this message to a stream of bytes.
* `status_t` [Flatten](#a736092eded1a6846cba89cd43bca26d3) (char *buffer, ssize_t size) const — Flatten the message to a buffer.
* `status_t` [Flatten](#ae0b47fbff10bc50153144b178fc1537d) (BDataIO *stream, ssize_t *size=NULL) const — Flatten the message to a stream.
* `status_t` [Unflatten](#a6704fc8df822fc366b616c3abf36ae9f) (const char *flatBuffer) — Unflatten a message from a buffer and put it into the current object.
* `status_t` [Unflatten](#a7ded81e10fed9a25b1a22934e04928dc) (BDataIO *stream) — Unflatten a message from a stream and put it into the current object.
* `status_t` [AddSpecifier](#a8f6efbc2f8c4faf38d1a6dab304b8880) (const char *property) — Undocumented.
* `status_t` [AddSpecifier](#a1e904ab6672cd0b29007fa9859ffe685) (const char *property, int32 index) — Undocumented.
* `status_t` [AddSpecifier](#a1ae990808fff37361f1abe3688dbb181) (const char *property, int32 index, int32 range) — Undocumented.
* `status_t` [AddSpecifier](#a3ba4e7e99c78281226c2befb8912e327) (const char *property, const char *name) — Undocumented.
* `status_t` [AddSpecifier](#a29406ecff2333e64d28850548a3b463c) (const BMessage *specifier) — Undocumented.
* `status_t` [SetCurrentSpecifier](#aa4bcec94162df7498208a1136c0f05ba) (int32 index) — Undocumented.
* `status_t` [GetCurrentSpecifier](#a641086c9321e56195843a3224bb0f11d) (int32 *index, BMessage *specifier=NULL, int32 *what=NULL, const char **property=NULL) const — Undocumented.
* `bool` [HasSpecifiers](#a70f59c7377d4d67f47feb212b73c8b25) () const — Undocumented.
* `status_t` [PopSpecifier](#aeab6b578828566453d03152bfb446e1a) () — Undocumented.
* `status_t` [AddAlignment](#a4fa4e6bcc354814dc17b61532480837d) (const char *name, const BAlignment &alignment) — Convenience method to add a BAlignment to the label name.
* `status_t` [AddRect](#a42d9e94fb88d457699d193eb5094a24c) (const char *name, BRect rect) — Convenience method to add a BRect to the label name.
* `status_t` [AddPoint](#afde5dc7d76c57e5d062de58954fb2548) (const char *name, BPoint point) — Convenience method to add a BPoint to the label name.
* `status_t` [AddSize](#a37d4771d6d726a439e0c0f36943d9e52) (const char *name, BSize size) — Convenience method to add a BSize to the label name.
* `status_t` [AddString](#a342311ccdf68206c4b879bcd0f2d6e83) (const char *name, const char *string) — Convenience method to add a C-string to the label name.
* `status_t` [AddString](#a76d63dc8621996c05a8c2b8186b28efb) (const char *name, const BString &string) — Convenience method to add a BString to the label name.
* `status_t` [AddStrings](#a4b3643ef27b1a9edffceac01f9d2ae89) (const char *name, const BStringList &list) — Convenience method to add list of strings to the label name.
* `status_t` [AddInt8](#a224c55f626ae3a4552d06788539c7d60) (const char *name, int8 value) — Convenience method to add an int8 to the label name.
* `status_t` [AddUInt8](#a98bbc2ca6c4fcb26bcd162c06ea0f46f) (const char *name, uint8 value) — Convenience method to add an uint8 to the label name.
* `status_t` [AddInt16](#a8e865679288281553721414aa17a7fea) (const char *name, int16 value) — Convenience method to add an int16 to the label name.
* `status_t` [AddUInt16](#aa43cedc7a1d6ecdc26041e6657c9288d) (const char *name, uint16 value) — Convenience method to add an uint16 to the label name.
* `status_t` [AddInt32](#aa4d9d24d521c499aefd512b18d1e38c5) (const char *name, int32 value) — Convenience method to add an int32 to the label name.
* `status_t` [AddUInt32](#acc2a562d501b88ce8fe55ae4017d3bb6) (const char *name, uint32 value) — Convenience method to add an uint32 to the label name.
* `status_t` [AddInt64](#ad172f4c606396d8457a686fb16d0be31) (const char *name, int64 value) — Convenience method to add an int64 to the label name.
* `status_t` [AddUInt64](#a1c6b3d4ee371ccb4ddfc6c0fd1dc8e58) (const char *name, uint64 value) — Convenience method to add an uint64 to the label name.
* `status_t` [AddBool](#a2976642c2259ebad33704d1b127bae60) (const char *name, bool value) — Convenience method to add a bool to the label name.
* `status_t` [AddFloat](#acdffd573b491074deef980df9f7f6e07) (const char *name, float value) — Convenience method to add a float to the label name.
* `status_t` [AddDouble](#a77a042d689d478572e23e87c3ad9982f) (const char *name, double value) — Convenience method to add a double to the label name.
* `status_t` [AddColor](#ae6e41cb30d1fb757a264a38ca6c27224) (const char *name, rgb_color value) — Convenience method to add a rgb_color to the label name.
* `status_t` [AddPointer](#a3dc68e69cb8da2ca0f7512e42c4393fe) (const char *name, const void *pointer) — Convenience method to add a pointer to the label name.
* `status_t` [AddMessenger](#ac7f46a46a04dcbfd9fd2af6dfb2d3850) (const char *name, BMessenger messenger) — Convenience method to add a messenger to the label name.
* `status_t` [AddRef](#a8e67d1398ecbfc5c75ab90ee2e602af5) (const char *name, const entry_ref *ref) — Convenience method to add an entry_ref to the label name.
* `status_t` [AddNodeRef](#a4e486773f6adca4610d01d96c0bd6d23) (const char *name, const node_ref *ref) — Convenience method to add a node_ref with the label name.
* `status_t` [AddMessage](#a421a8dee0e636fe619e9ebf561aafa0a) (const char *name, const BMessage *message) — Convenience method to add a message to the label name.
* `status_t` [AddFlat](#a1d1ea741ffa1841ef1667a3daa1ce7fd) (const char *name, BFlattenable *object, int32 count=1) — Convenience method to add a flattenable to the label name.
* `status_t` [AddFlat](#ac04c2914f73813a766c5644765a506a4) (const char *name, const BFlattenable *object, int32 count=1) — Convenience method to add a flattenable to the label name.
* `status_t` [AddData](#a4b99de85becfb1058a893fc6e40c48ad) (const char *name, type_code type, const void *data, ssize_t numBytes, bool isFixedSize=true, int32 count=1) — Add data of a certain type to the message.
* `status_t` [Append](#ac2441b6ef13598fb8289c392b6588882) (const BMessage &message) — Append the data of another message to this message.
* `status_t` [RemoveData](#a72ce9596ebe74ce6e995705304b7fc7d) (const char *name, int32 index=0) — Remove data associated with name at a specified index.
* `status_t` [RemoveName](#a5db9b5a9ddc0b04173afb8dbc1c69e5c) (const char *name) — Remove all data associated with a name.
* `status_t` [MakeEmpty](#abac76b537c88ce7f1a127fa6425c3279) () — Clear all data and metadata in this message.
* `status_t` [FindAlignment](#abf81526338001abe288b5831fcb88874) (const char *name, BAlignment *alignment) const — Find an alignment at the label name.
* `status_t` [FindAlignment](#ac124217fb122b3e012ee431fb3cbd68f) (const char *name, int32 index, BAlignment *alignment) const — Find an alignment at the label name at an index.
* `status_t` [FindRect](#a84e6020b903936f61538e33988792956) (const char *name, BRect *rect) const — Find a rectangle at the label name.
* `status_t` [FindRect](#abc4398bca7420cc74c4d5cc76ccba018) (const char *name, int32 index, BRect *rect) const — Find a rectangle at the label name at an index.
* `status_t` [FindPoint](#a88507a5c41974ab5c13dd5da800a68d7) (const char *name, BPoint *point) const — Find a point at the label name.
* `status_t` [FindPoint](#a9a53e98aa4593529103051dbcd0186d4) (const char *name, int32 index, BPoint *point) const — Find a point at the label name at an index.
* `status_t` [FindSize](#a463777b0384a8ee580709c62dfbfa2ca) (const char *name, BSize *size) const — Find a size at the label name.
* `status_t` [FindSize](#a769dcfc011f91c8372512f7396e6e59e) (const char *name, int32 index, BSize *size) const — Find a size at the label name at an index.
* `status_t` [FindString](#ac2a5b50960210666f57952b3a050530d) (const char *name, const char **string) const — Find a string at the label name.
* `status_t` [FindString](#a4370bfd828545100484adaf51a38df47) (const char *name, int32 index, const char **string) const — Find a string at the label name at an index.
* `status_t` [FindString](#a2930978f62db0238b780d67a1e74e69b) (const char *name, BString *string) const — Find a string at the label name.
* `status_t` [FindString](#a35f163b19ec1862a2f117d1d1ac3ef46) (const char *name, int32 index, BString *string) const — Find a string at the label name at an index.
* `status_t` [FindStrings](#a1a482768af8c3361ae84f5458d674175) (const char *name, BStringList *list) const — Find all the strings at the label name.
* `status_t` [FindInt8](#a757685e8e85ac38f882e28bd281e9f9d) (const char *name, int8 *value) const — Find an integer at the label name.
* `status_t` [FindInt8](#aed840d1a802546534eaa95e5f1247a53) (const char *name, int32 index, int8 *value) const — Find an integer at the label name at an index.
* `status_t` [FindUInt8](#a37170512c52bac977fb81e7c9d44ef95) (const char *name, uint8 *value) const — Find an integer at the label name.
* `status_t` [FindUInt8](#ab5ce6415eb074f94f1f8dc59f8c3985e) (const char *name, int32 index, uint8 *value) const — Find an integer at the label name at an index.
* `status_t` [FindInt16](#a4dd27c3a8fc6e2e0366d77254b2095e6) (const char *name, int16 *value) const — Find an integer at the label name.
* `status_t` [FindInt16](#afedef75ac1e9c5a1d3f069b641975041) (const char *name, int32 index, int16 *value) const — Find an integer at the label name at an index.
* `status_t` [FindUInt16](#a5653c46ede97ff7667d0e823674b5953) (const char *name, uint16 *value) const — Find an integer at the label name.
* `status_t` [FindUInt16](#a761a6bb39440a15176c5dc600d7b7041) (const char *name, int32 index, uint16 *value) const — Find an integer at the label name at an index.
* `status_t` [FindInt32](#af6ee3d278ed11bdafb60047b03c18ab9) (const char *name, int32 *value) const — Find an integer at the label name.
* `status_t` [FindInt32](#afce55a9ef851c34fa07d21bcf9e2f1f2) (const char *name, int32 index, int32 *value) const — Find an integer at the label name at an index.
* `status_t` [FindUInt32](#a486a2138fb0edc7bf17b1a9676d5ecde) (const char *name, uint32 *value) const — Find an integer at the label name.
* `status_t` [FindUInt32](#a10e79ec598190c30d3d07c46c297eacf) (const char *name, int32 index, uint32 *value) const — Find an integer at the label name at an index.
* `status_t` [FindInt64](#aedbef710d7c8e61cd4ff93efbb32889a) (const char *name, int64 *value) const — Find an integer at the label name.
* `status_t` [FindInt64](#ab3eef33595e98a3df56d18ade5f41a98) (const char *name, int32 index, int64 *value) const — Find an integer at the label name at an index.
* `status_t` [FindUInt64](#a20f4b14c6c45c4a24a3cbeea4347f79a) (const char *name, uint64 *value) const — Find an integer at the label name.
* `status_t` [FindUInt64](#abd21bedb93952f87cd12bf50c89d8612) (const char *name, int32 index, uint64 *value) const — Find an integer at the label name at an index.
* `status_t` [FindBool](#a886d79a7c580d3563940333cfa7f3870) (const char *name, bool *value) const — Find a boolean at the label name.
* `status_t` [FindBool](#a99405de493bf7e49ce033ef8cac8825b) (const char *name, int32 index, bool *value) const — Find a boolean at the label name at an index.
* `status_t` [FindFloat](#ac26f15d78b69e330f9cb933db8c0500b) (const char *name, float *value) const — Find a float at the label name.
* `status_t` [FindFloat](#af5d62fe0dba7074556b877a52d1cecb2) (const char *name, int32 index, float *value) const — Find a float at the label name at an index.
* `status_t` [FindDouble](#a32672932ca24ee53b3642bf9d25f709d) (const char *name, double *value) const — Find a double at the label name.
* `status_t` [FindDouble](#ac332368de00ff51eb06097e134244e5a) (const char *name, int32 index, double *value) const — Find a double at the label name at an index.
* `status_t` [FindColor](#a8980e233e8afb3f302dc5218483a5456) (const char *name, rgb_color *value) const — Find a color with the label name.
* `status_t` [FindColor](#a6e05596bbf62217b061e54a18fa51a72) (const char *name, int32 index, rgb_color *value) const — Find a color at the label name at an index.
* `status_t` [FindPointer](#aee05fc5fe7053a1d85deb3169742e05a) (const char *name, void **pointer) const — Find a pointer at the label name.
* `status_t` [FindPointer](#a4de3e5f0cb4d25da0e00b13e33d28a66) (const char *name, int32 index, void **pointer) const — Find a pointer at the label name at an index.
* `status_t` [FindMessenger](#a1b01edbdb7740ad1a06b2e81366fd47d) (const char *name, BMessenger *messenger) const — Find a messenger at the label name.
* `status_t` [FindMessenger](#a87a4b0591e87332366a99d09462d9be8) (const char *name, int32 index, BMessenger *messenger) const — Find a messenger at the label name at an index.
* `status_t` [FindRef](#a85035f98a61911e973af9a8821b5e254) (const char *name, entry_ref *ref) const — Find a reference to a file at the label name.
* `status_t` [FindRef](#a4b1c2190d9f3742c86edc72c3c49eeca) (const char *name, int32 index, entry_ref *ref) const — Find a reference to a file at the label name at an index.
* `status_t` [FindNodeRef](#acfb1819b93db7eadd0cabcd1cf1d45ec) (const char *name, node_ref *ref) const — Find a reference to a node at the label name.
* `status_t` [FindNodeRef](#a4a4b0e9e0a52151ec8d1df979925857a) (const char *name, int32 index, node_ref *ref) const — Find a reference to a node at the label name at an index.
* `status_t` [FindMessage](#a8286c1590191f37641ac6916aaf6418b) (const char *name, BMessage *message) const — Find a message at the label name.
* `status_t` [FindMessage](#aecdfe05be151ea5a978225152486d44a) (const char *name, int32 index, BMessage *message) const — Find a message at the label name at an index.
* `status_t` [FindFlat](#ae910af356e0732edaa09260e47e1bbd0) (const char *name, BFlattenable *object) const — Find a flattened object at the label name.
* `status_t` [FindFlat](#a017c619934572443bf1ac5161dcdb2c2) (const char *name, int32 index, BFlattenable *object) const — Find a flattened object at the label name at an index.
* `status_t` [FindData](#a1e896648ee668dd5d6c8a4311d6cfa94) (const char *name, type_code type, const void **data, ssize_t *numBytes) const — Find data that is stored in this message.
* `status_t` [FindData](#aea11107bcd353be1dfde351850fe7ee0) (const char *name, type_code type, int32 index, const void **data, ssize_t *numBytes) const — Find data that is stored in this message at an index.
* `status_t` [ReplaceAlignment](#a7613f4cdd1154b3e70771fdc9a4e3e04) (const char *name, const BAlignment &alignment) — Replace an alignment at the label name.
* `status_t` [ReplaceAlignment](#ae6f32ad46aa14db07c9d324656daf871) (const char *name, int32 index, const BAlignment &alignment) — Replace an alignment at the label name at a specified index.
* `status_t` [ReplaceRect](#aa24fb4e8fbc39011d1b7fb55c7f752c1) (const char *name, BRect rect) — Replace a rectangle at the label name.
* `status_t` [ReplaceRect](#a2e38c3d43259b9157cc5c8647030dac0) (const char *name, int32 index, BRect rect) — Replace a rectangle at the label name at a specified index.
* `status_t` [ReplacePoint](#ac1b948f0c5867720173ef96450201859) (const char *name, BPoint aPoint) — Replace a point at the label name.
* `status_t` [ReplacePoint](#a4897600b32e200802cf7c5d397f7e8cf) (const char *name, int32 index, BPoint aPoint) — Replace a point at the label name at a specified index.
* `status_t` [ReplaceSize](#a440d37083df7c8845d3337cc8c9d695a) (const char *name, BSize aSize) — Replace a size at the label name.
* `status_t` [ReplaceSize](#a9ff6d6940725e22e2fab190bf42a1659) (const char *name, int32 index, BSize aSize) — Replace a size at the label name at a specified index.
* `status_t` [ReplaceString](#a3a606679aa72f7530034994f9cf4ad32) (const char *name, const char *string) — Replace a string at the label name.
* `status_t` [ReplaceString](#aceeabb6ee480223b56d58e42a87ba7f5) (const char *name, int32 index, const char *string) — Replace a string at the label name at a specified index.
* `status_t` [ReplaceString](#a15b2ce4ff50f420a64422545079af452) (const char *name, const BString &string) — Replace a string at the label name.
* `status_t` [ReplaceString](#a59a40f04a1fc5b0fe523a6e025d9860e) (const char *name, int32 index, const BString &string) — Replace a string at the label name at a specified index.
* `status_t` [ReplaceInt8](#a55f909d237c7c1abfca5f918a8a5ffb9) (const char *name, int8 value) — Replace an integer at the label name.
* `status_t` [ReplaceInt8](#a8ae3786000645416e1911fe2b618c432) (const char *name, int32 index, int8 value) — Replace an integer at the label name at a specified index.
* `status_t` [ReplaceUInt8](#aee573704ea412f6b53e1904e22e65454) (const char *name, uint8 value) — Replace an integer at the label name.
* `status_t` [ReplaceUInt8](#aff3cffe95f04bf5576393f65bb378a1c) (const char *name, int32 index, uint8 value) — Replace an integer at the label name at a specified index.
* `status_t` [ReplaceInt16](#a525deaa699950007c8fdab78c82ada32) (const char *name, int16 value) — Replace an integer at the label name.
* `status_t` [ReplaceInt16](#a05b21498414818bc51e76451a26a143f) (const char *name, int32 index, int16 value) — Replace an integer at the label name at a specified index.
* `status_t` [ReplaceUInt16](#a0029cb535e97ed753ee9529c646d763b) (const char *name, uint16 value) — Replace an integer at the label name.
* `status_t` [ReplaceUInt16](#ab5d7606278375f280ab402b9f7e388be) (const char *name, int32 index, uint16 value) — Replace an integer at the label name at a specified index.
* `status_t` [ReplaceInt32](#ad7b41f02b8a298bcd6699e972b88c82e) (const char *name, int32 value) — Replace an integer at the label name.
* `status_t` [ReplaceInt32](#ae1fe7f9855edb57e186cac617569cb79) (const char *name, int32 index, int32 value) — Replace an integer at the label name at a specified index.
* `status_t` [ReplaceUInt32](#afdfe554348e5e672a1a358f3b944d63e) (const char *name, uint32 value) — Replace an integer at the label name.
* `status_t` [ReplaceUInt32](#a8bd5a2123e4097377f33d12aca43b615) (const char *name, int32 index, uint32 value) — Replace an integer at the label name at a specified index.
* `status_t` [ReplaceInt64](#a97220953786ff1cbb286e7e1113510ff) (const char *name, int64 value) — Replace an integer at the label name.
* `status_t` [ReplaceInt64](#ac92d2b43a1dbc3e6591e0ddb03880e9b) (const char *name, int32 index, int64 value) — Replace an integer at the label name at a specified index.
* `status_t` [ReplaceUInt64](#ad906dc7124f3dab9f41ca94f678c29d4) (const char *name, uint64 value) — Replace an integer at the label name.
* `status_t` [ReplaceUInt64](#a66c1638d29c7474762e7ce3799785ffa) (const char *name, int32 index, uint64 value) — Replace an integer at the label name at a specified index.
* `status_t` [ReplaceBool](#a64357e8743595d49dd53975e3f534a3f) (const char *name, bool aBoolean) — Replace a boolean at the label name.
* `status_t` [ReplaceBool](#af6bfc87ac8fe3f470b8d73a01dca388a) (const char *name, int32 index, bool value) — Replace a boolean at the label name at a specified index.
* `status_t` [ReplaceFloat](#ab0c54a885d2cf1826dcb2fa53cfd0175) (const char *name, float value) — Replace a float at the label name.
* `status_t` [ReplaceFloat](#ad081e12c8b593d03c7fbee4ea61c8f34) (const char *name, int32 index, float value) — Replace a float at the label name at a specified index.
* `status_t` [ReplaceDouble](#a023f8e3aa932cd312acd5653ecebaca4) (const char *name, double value) — Replace a double at the label name.
* `status_t` [ReplaceDouble](#aee50e26caa09886d0cdcbc753a91317f) (const char *name, int32 index, double value) — Replace a double at the label name at a specified index.
* `status_t` [ReplaceColor](#af712a6b0c6921803023c1314e39b09fd) (const char *name, rgb_color value) — Replace a color at the label name.
* `status_t` [ReplaceColor](#ae0e39566d16d42b40a55e9809a3e93f9) (const char *name, int32 index, rgb_color value) — Replace a rgb_color at the label name at a specified index.
* `status_t` [ReplacePointer](#aaa543367787ed528566a4f629e78f60b) (const char *name, const void *pointer) — Replace a pointer at the label name.
* `status_t` [ReplacePointer](#a77be90c4ecd92ca28cea4dbc46f8e8a2) (const char *name, int32 index, const void *pointer) — Replace a pointer at the label name at a specified index.
* `status_t` [ReplaceMessenger](#ada775f0c198e3968eedd03a6ad2daa49) (const char *name, BMessenger messenger) — Replace a messenger at the label name.
* `status_t` [ReplaceMessenger](#ad21e673615ff361bb5facce2632b57c1) (const char *name, int32 index, BMessenger messenger) — Replace a messenger at the label name at a specified index.
* `status_t` [ReplaceRef](#a44077e7618f42a388db207724075c0a6) (const char *name, const entry_ref *ref) — Replace a reference to a file at the label name.
* `status_t` [ReplaceRef](#acb93b69f6693499b1886173a4900b8c7) (const char *name, int32 index, const entry_ref *ref) — Replace a reference to a file at the label name at a specified index.
* `status_t` [ReplaceNodeRef](#a57fb9d5c2b6aafc45932e5a10f1747a7) (const char *name, const node_ref *ref) — Replace a reference to a node at the label name.
* `status_t` [ReplaceNodeRef](#a4749eff1c0bfe6a258570536033dd698) (const char *name, int32 index, const node_ref *ref) — Replace a reference to a node at the label name at a specified index.
* `status_t` [ReplaceMessage](#a7c9f522c31ffee206e1df06aa8246f30) (const char *name, const BMessage *message) — Replace a message at the label name.
* `status_t` [ReplaceMessage](#afc72518025d6c772e82acafad8669bc3) (const char *name, int32 index, const BMessage *message) — Replace a message at the label name at a specified index.
* `status_t` [ReplaceFlat](#aaa8c8f67ea3314d93f39e1618b19621e) (const char *name, BFlattenable *object) — Replace a flattened object at the label name.
* `status_t` [ReplaceFlat](#a32f79d59881b7bf9df0f1ab819fd9390) (const char *name, int32 index, BFlattenable *object) — Replace a flattened object at the label name at a specified index.
* `status_t` [ReplaceData](#a79bc7d526090a5b1f4d8958d72e55d31) (const char *name, type_code type, const void *data, ssize_t numBytes) — Replace the data at label name.
* `status_t` [ReplaceData](#a8d5e1ec791c56202414c6c1c407163d4) (const char *name, type_code type, int32 index, const void *data, ssize_t numBytes) — Replace the data at label name at a specified index.
* `bool` [HasSameData](#a6cfbd78a1801c5b199fd2b9c20f1edc0) (const BMessage &other, bool ignoreFieldOrder=true, bool deep=false) const — Experimental method to compare two messages.
* `bool` [HasAlignment](#adda48b9629ff85f0b6f5c14de1fb3089) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasRect](#a4470bc9810d3157abf300958299b3a8e) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasPoint](#ac273669ad82b047d7df59f5d96789b36) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasSize](#ae196d8af4c0205d1a3f68b300fede30d) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasString](#a21593fb0e2ba2d554f5e73aa69682509) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasInt8](#ac4c6e7e0e7ccd94119ca7b1fb8a95ab0) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasUInt8](#a6aa77ba54a0aeb5e368b1ae0b2ebcc0e) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasInt16](#afc15a565ef75a9acc96b5e7fc5f8a99f) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasUInt16](#a375487bace52f5629d38a90ab82e3501) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasInt32](#a3b8dc2a6990cca27044c581e960c4815) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasUInt32](#a61edd5753b91bef212a6d20618fc2115) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasInt64](#a5298eb19cf9387a592cf348804bbb543) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasUInt64](#a4718b00776b779d72f48cfcb044d09c7) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasBool](#af83659da0a00c4652bc410868e10d3e3) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasFloat](#a4ed1ab46d69555bed8656b88cfbedf80) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasDouble](#a10cc5f06813d7d11df126e351b43c19e) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasColor](#aa17b02befd19088e560ff218b69b4336) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasPointer](#aa573c41ac9b8882a1f6c5ade73d6a090) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasMessenger](#aea46bfdce87d5de4344e3aa6f45aa7ef) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasRef](#a963c126685bfc3e5f8e1240a024fedfa) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasNodeRef](#a0284024009482818cbc57970ab51ceff) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasMessage](#af9f8c20181a4f95e6a4fbadddb2d39c7) (const char *name, int32 n=0) const — Deprecated.
* `bool` [HasFlat](#a74043f885d59434afca9368419f5608a) (const char *name, const BFlattenable *object) const — Deprecated.
* `bool` [HasFlat](#a8dfa876ddb1775a21f3cbfe92db599c2) (const char *name, int32 n, const BFlattenable *object) const — Deprecated.
* `bool` [HasData](#ae3d1dd24246884e316fd9587d4a28906) (const char *name, type_code, int32 n=0) const — Deprecated.
* `BRect` [FindRect](#a9713057fc44d53b1771ff071341482ac) (const char *name, int32 n=0) const — Deprecated.
* `BPoint` [FindPoint](#a813615a6d10f5ec02573a45f14c1241c) (const char *name, int32 n=0) const — Deprecated.
* `const char *` [FindString](#a36103667f4d215f1a06add5b381c2037) (const char *name, int32 n=0) const — Deprecated.
* `int8` [FindInt8](#a941d54ffe9d43bc4f06b0f51b05fc9a4) (const char *name, int32 n=0) const — Deprecated.
* `int16` [FindInt16](#a7fb486ea27ffbf2711e2290bb65ab106) (const char *name, int32 n=0) const — Deprecated.
* `int32` [FindInt32](#ac3c3455d0b3b60fc8cabcf250ec45d86) (const char *name, int32 n=0) const — Deprecated.
* `int64` [FindInt64](#ac098297494e5013484455204339a17d7) (const char *name, int32 n=0) const — Deprecated.
* `bool` [FindBool](#acbb4500a7a1118cd1ee554fbc726d19f) (const char *name, int32 n=0) const — Deprecated.
* `float` [FindFloat](#a6d647b74485e51f9831b7e18e455b55a) (const char *name, int32 n=0) const — Deprecated.
* `double` [FindDouble](#aa58f382932f2bfdcdb5f3a390c8312de) (const char *name, int32 n=0) const — Deprecated.
* `bool` [GetBool](#aff0242cacf8613b9e58dde7871c4c21c) (const char *name, bool defaultValue=false) const — Return the boolean value from message with name, or defaultValue if not found.
* `bool` [GetBool](#a7de758471bcc9e642064b350c32459c7) (const char *name, int32 index, bool defaultValue) const — Return the boolean value from message with name and index, or defaultValue if not found.
* `int8` [GetInt8](#a822fcf4b8182566bfaebb8dd04cd2b97) (const char *name, int8 defaultValue) const — Return the int8 value from message with name, or defaultValue if not found.
* `int8` [GetInt8](#aad10c23206e76e694eb6d8ee90ae7710) (const char *name, int32 index, int8 defaultValue) const — Return the int8 value from message with name and index, or defaultValue if not found.
* `uint8` [GetUInt8](#a146182cecba5ad8a802d0c60627b695a) (const char *name, uint8 defaultValue) const — Return the uint8 value from message with name, or defaultValue if not found.
* `uint8` [GetUInt8](#af8f4251e140340b254a26f62fe3df880) (const char *name, int32 index, uint8 defaultValue) const — Return the uint8 message from message with name and index, or defaultValue if not found.
* `int16` [GetInt16](#aafc68a78c8b550fec01c4129683520b2) (const char *name, int16 defaultValue) const — Return the int16 value from message with name, or defaultValue if not found.
* `int16` [GetInt16](#afd2db75cacae2f4b44f93c5ea3fb0e0f) (const char *name, int32 index, int16 defaultValue) const — Return the int16 value from message with name and index, or defaultValue if not found.
* `uint16` [GetUInt16](#a20d02e3b2687cf4d884d5e308c5a55cb) (const char *name, uint16 defaultValue) const — Return the uint16 value from message with name, or defaultValue if not found.
* `uint16` [GetUInt16](#a9a3612c486e40bc08800f72e48d2b214) (const char *name, int32 index, uint16 defaultValue) const — Return the uint16 value from message with name and index, or defaultValue if not found.
* `int32` [GetInt32](#a526ebda92481d1c0da2786b93253efd1) (const char *name, int32 defaultValue) const — Return the int32 value from message with name, or defaultValue if not found.
* `int32` [GetInt32](#a1da13cf9b5913f1fcd6c8835f440b5f6) (const char *name, int32 index, int32 defaultValue) const — Return the int32 value from message with name and index, or defaultValue if not found.
* `uint32` [GetUInt32](#aa90efd88a6a15fef748c62c5c46f2f65) (const char *name, uint32 defaultValue) const — Return the uint32 value from message with name, or defaultValue if not found.
* `uint32` [GetUInt32](#a771c61eb89e5952e0fc890bb586365a1) (const char *name, int32 index, uint32 defaultValue) const — Return the uint32 value from message with name and index, or defaultValue if not found.
* `int64` [GetInt64](#a2bb8e387b504dfe4ff47b7860ead1be9) (const char *name, int64 defaultValue) const — Return the int64 value from message with name, or defaultValue if not found.
* `int64` [GetInt64](#a00e136d7bdfa978b2376ae993b200e64) (const char *name, int32 index, int64 defaultValue) const — Return the int64 value from message with name and index, or defaultValue if not found.
* `uint64` [GetUInt64](#a4d8f178f02212949cdd497c392ff6f13) (const char *name, uint64 defaultValue) const — Return the uint64 value from message with name, or defaultValue if not found.
* `uint64` [GetUInt64](#a9dce5b9af2a32cc3b1f185b3521ee61a) (const char *name, int32 index, uint64 defaultValue) const — Return the uint64 value from message with name and index, or defaultValue if not found.
* `float` [GetFloat](#a2f5426192ec8ca235dd9f936510c4e93) (const char *name, float defaultValue) const — Return the float value from message with name, or defaultValue if not found.
* `float` [GetFloat](#ad60572e86e9e605b27afcc50efcb1d24) (const char *name, int32 index, float defaultValue) const — Return the float value from message with name and index, or defaultValue if not found.
* `double` [GetDouble](#a018eed03b3b69e4248518e2a7c4a1c03) (const char *name, double defaultValue) const — Return the double value from message with name, or defaultValue if not found.
* `double` [GetDouble](#af0486856061e17452614c6ece2cfab64) (const char *name, int32 index, double defaultValue) const — Return the double value from message with name and index, or defaultValue if not found.
* `rgb_color` [GetColor](#a9471fc71d82ff91681ed35ee714041b8) (const char *name, rgb_color defaultValue) const — Return the rgb_color value from message with name, or defaultValue if not found.
* `rgb_color` [GetColor](#a30560420a899803f2ca07c395f3c3670) (const char *name, int32 index, rgb_color defaultValue) const — Return the rgb_color value from message with name and index, or defaultValue if not found.
* `const void *` [GetPointer](#a817c8b7db104a1525ad15616bd06e284) (const char *name, int32 index, const void *defaultValue=NULL) const — Return the pointer type from message with name and index, or defaultValue if not found.
* `const void *` [GetPointer](#a1141c4e98a497041cd46e2fce31ff880) (const char *name, const void *defaultValue=NULL) const — Return the pointer type from message with name, or defaultValue if not found.
* `const char *` [GetString](#acf98ba0c69ac6dd433153b6e3e06c64f) (const char *name, const char *defaultValue=NULL) const — Return the string from message with name, or defaultValue if not found.
* `const char *` [GetString](#a6e65f922253e4ab511507e015ce023f8) (const char *name, int32 index, const char *defaultValue) const — Return the string from message with name and index, or defaultValue if not found.
* `BAlignment` [GetAlignment](#af7ad0b5467ac972bb5f400d48a37bec9) (const char *name, int32 index, const BAlignment &defaultValue) const — Return the BAlignment object from message with name and index, or defaultValue if not found.
* `BAlignment` [GetAlignment](#a03bf0cc134fec0cb12f4e1a8fe74d555) (const char *name, const BAlignment &defaultValue) const — Return the BAlignment object from message with name, or defaultValue if not found.
* `BRect` [GetRect](#ac830b029ae38dce1f6a2f823f289f222) (const char *name, int32 index, const BRect &defaultValue) const — Return the BRect object from message with name and index, or defaultValue if not found.
* `BRect` [GetRect](#ab813849c1d23d484fff039204198e6f6) (const char *name, const BRect &defaultValue) const — Return the BRect object from message with name, or defaultValue if not found.
* `BPoint` [GetPoint](#a46167045bba07334db6acaa3c37e0498) (const char *name, int32 index, const BPoint &defaultValue) const — Return the BPoint object from message with name and index, or defaultValue if not found.
* `BPoint` [GetPoint](#ad68b28e3f6a38b8d832f2277c8be9372) (const char *name, const BPoint &defaultValue) const — Return the BPoint object from message with name, or defaultValue if not found.
* `BSize` [GetSize](#ae88c4239718d5a5ad14162e03889db9f) (const char *name, int32 index, const BSize &defaultValue) const — Return the BSize object from message with name and index, or defaultValue if not found.
* `BSize` [GetSize](#a8e61a348444f29b08027d99eb5042ac8) (const char *name, const BSize &defaultValue) const — Return the BSize object from message with name, or defaultValue if not found.
* `status_t` [SetBool](#a60e079b535d604425d79d21f6c2ff331) (const char *name, bool value) — Set the data with at the label name to value.
* `status_t` [SetInt8](#a43dd2dd4ef948377bd1c208e8fb1397a) (const char *name, int8 value) — Set the data with at the label name to value.
* `status_t` [SetUInt8](#a2b2c442855633f18d2575f081c426cfb) (const char *name, uint8 value) — Set the data with at the label name to value.
* `status_t` [SetInt16](#a8572ce07a58fb1d08e21bf10aefd3f61) (const char *name, int16 value) — Set the data with at the label name to value.
* `status_t` [SetUInt16](#adc67eb8a3f7f7b25d0581bf839d8f994) (const char *name, uint16 value) — Set the data with at the label name to value.
* `status_t` [SetInt32](#ad3912ab5d568e4035ffb12aa74feda3f) (const char *name, int32 value) — Set the data with at the label name to value.
* `status_t` [SetUInt32](#a036ff5c9b6a87427fc0682f0afe0fc2d) (const char *name, uint32 value) — Set the data with at the label name to value.
* `status_t` [SetInt64](#a488e4670f9d00491385a5a85f42c67d9) (const char *name, int64 value) — Set the data with at the label name to value.
* `status_t` [SetUInt64](#a39ea15b60e3551cf3f81af7ff2e8a6ee) (const char *name, uint64 value) — Set the data with at the label name to value.
* `status_t` [SetColor](#aed1d0c3762ab5a8438b1a82a0d67c6c7) (const char *name, rgb_color value) — Set the data with at the label name to value.
* `status_t` [SetPointer](#a7d2a78283d63010daf55315eae6983da) (const char *name, const void *value) — Set the data with at the label name to value.
* `status_t` [SetString](#a7bbb5edf6eaec7d8ead471063ba05720) (const char *name, const char *string) — Set the string with at the label name to string.
* `status_t` [SetString](#a3581bea5b303469e21c2dbc0c77d0682) (const char *name, const BString &string) — Set the string with at the label name to string.
* `status_t` [SetFloat](#a70bada6ab725e3c49d6be3f7b9cd32b0) (const char *name, float value) — Set the data with at the label name to value.
* `status_t` [SetDouble](#ac63da648d43ba6f4ac4b6b78ce20fc14) (const char *name, double value) — Set the data with at the label name to value.
* `status_t` [SetAlignment](#a68d1c8c3faf0425085dd4c7368115445) (const char *name, const BAlignment &value) — Set the data with at the label name to value.
* `status_t` [SetPoint](#a5c573737d146370197cbbac1d0b85a12) (const char *name, const BPoint &value) — Set the data with at the label name to value.
* `status_t` [SetRect](#a1f6691ff69fe9d9027179d8f2a3c8165) (const char *name, const BRect &value) — Set the data with at the label name to value.
* `status_t` [SetSize](#a6981d8f08fd09740c20d1ba96cd5b85f) (const char *name, const BSize &value) — Set the data with at the label name to value.
* `status_t` [SetData](#af5a3adafad9f0e26ae63c5ebe6fe1f2a) (const char *name, type_code type, const void *data, ssize_t numBytes, bool fixedSize=true, int count=1) — Low level function to set data to a certain value.

### Public Attributes

* `uint32` [what](#ad074faab0857f51fba778f0d8558df1e) — A 4-byte constant that determines the type of message.

## Detailed Member Documentation

### `BMessage()`

```cpp
BMessage::BMessage()
```

Construct an empty message, without any data members and with a *what* constant set to `0`. 



**See also:** [BMessage(uint32 what)](classBMessage.md#ae56247b7b613c0b1b626d1ea57f5beab)



**Since:** BeOS R3

---

### `BMessage()`

```cpp
BMessage::BMessage(uint32 what)
```

Construct an empty message with the *what* member set to the specified value. 



**See also:** [BMessage::BMessage()](classBMessage.md#a2d0749c439c93a1ca938378b6c890d07)



**Since:** BeOS R3

---

### `BMessage()`

```cpp
BMessage::BMessage(const BMessage & other)
```

Construct a new message that is a copy of another message. 


The *what* member and the data values are copied. The metadata, such as whether or not the message is a drop message or reply information is not copied. If the original message is a reply to a previous message this will make [IsReply()](classBMessage.md#a01c7dd891b3b05eb7f458a621c5181d4) return `true`, while calling the same method on a copy of the message will return `false`.


RemarksBeOS kept the metadata of the message while Haiku deviates from this behavior. Use the Haiku implementation of message copying as the default behavior to keep your applications backwards compatible.

**See also:** [BMessage::BMessage()](classBMessage.md#a2d0749c439c93a1ca938378b6c890d07)



**Since:** BeOS R3

---

### `~BMessage()`

```cpp
BMessage::~BMessage()
```

Free the data members associated with the message. 


If there still is a sender waiting for a reply, the `B_NO_REPLY` message will be sent to inform them that there won't be a reply.



**Since:** BeOS R3

---

### `AddAlignment()`

```cpp
status_t BMessage::AddAlignment(const char * name, const BAlignment & alignment)
```

Convenience method to add a [BAlignment](../interface_kit/classBAlignment.md) to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_ALIGNMENT_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `alignment` | The alignment to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** Haiku R1

---

### `AddBool()`

```cpp
status_t BMessage::AddBool(const char * name, bool aBoolean)
```

Convenience method to add a `bool` to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_BOOL_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `aBoolean` | The value to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddColor()`

```cpp
status_t BMessage::AddColor(const char * name, rgb_color aColor)
```

Convenience method to add a `rgb_color` to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_RGB_32_BIT_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `aColor` | The value to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddColor()](classBMessage.md#ae6e41cb30d1fb757a264a38ca6c27224) for a more detailed overview of the inner workings.



**Since:** Haiku R1

---

### `AddData()`

```cpp
status_t BMessage::AddData(const char * name, type_code type, const void * data, ssize_t numBytes, bool isFixedSize = true, int32 count = 1)
```

Add *data* of a certain *type* to the message. 


The amount of *numBytes* is copied into the message. The data is stored at the label specified in *name*. You are responsible for specifying the correct *type*. The Haiku API already specifies many constants, such as `B_FLOAT_TYPE` or `B_RECT_TYPE`. See [TypeConstants.h](TypeConstants_8h.md) for more information on the system-wide defined types.


If the field with the *name* already exists, the data is added in an array-like form. If you are adding a certain *name* for the first time, you are able to specify some properties of this array. You can fix the size of each data entry, and you can also instruct [BMessage](classBMessage.md) to allocate a *count* of items. The latter does not mean that the number of items is fixed; the array will grow nonetheless. Also, note that every *name* can only be associated with one *type* of data.


If consecutive method calls specify a different *type* than the initial, these calls will fail.


There is no limit to the number of labels, or the amount of data, but note that searching of data members is linear, as well as that some messages will be copied whilst being passed around, so if the amount of data you need to pass is too big, find another way to pass it.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which this data needs to be associated. If the *name* already exists, the new data will be added in an array-like style. |
| `type` | The type of data. If you are adding data to the same *name*, make sure it is the same type. |
| `data` | The data buffer to copy the bytes from. |
| `numBytes` | The number of bytes to be copied. If this is the first call to this method for this type of data, and you set *isFixedSize* to `true`, this will specify the size of all consecutive calls to this method. |
| `isFixedSize` | If this is the first call to this method with this *name*, you can specify the whether or not all items in this array should have the same fixed size. |
| `count` | If this is the first call to this method with this *name*, you can instruct this message to allocate a number of items in advance. This does not limit the amount of items though. The array will grow if needed. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The *data* is succesfully added. |
| B_BAD_VALUE | The *numBytes* is less than, or equal to `0`, or the size of this item is larger than the *name* allows, since it has been specified to have a fixed size. |
| B_ERROR | There was an error whilst creating the label with your *name*. |
| B_BAD_TYPE | The *type* you specified is different than the one already associated with *name*. |





**Since:** BeOS R3

---

### `AddDouble()`

```cpp
status_t BMessage::AddDouble(const char * name, double aDouble)
```

Convenience method to add a `double` to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_DOUBLE_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `aDouble` | The value to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddFlat()`

```cpp
status_t BMessage::AddFlat(const char * name, BFlattenable * object, int32 count = 1)
```

Convenience method to add a flattenable to the label *name*. 



**Since:** BeOS R3

---

### `AddFlat()`

```cpp
status_t BMessage::AddFlat(const char * name, const BFlattenable * object, int32 count = 1)
```

Convenience method to add a flattenable to the label *name*. 


This method uses [BFlattenable::TypeCode()](../support_kit/classBFlattenable.md#a819507fa1b0906f14299db15f6e990d1) to determine the type. It also uses [BFlattenable::IsFixedSize()](../support_kit/classBFlattenable.md#ac019f502749a0cc78082f5ec7c8f5b56) to determine whether or not the size of the object is supposedly always the same. You can specify a *count*, to pre-allocate more entries if you are going to add more than one of this type.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `object` | The object to flatten into the message. |
| `count` | The number of items to pre-allocate associated with this *name*. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** Haiku R1

---

### `AddFloat()`

```cpp
status_t BMessage::AddFloat(const char * name, float aFloat)
```

Convenience method to add a `float` to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_FLOAT_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `aFloat` | The value to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddInt16()`

```cpp
status_t BMessage::AddInt16(const char * name, int16 value)
```

Convenience method to add an `int16` to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_INT16_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `value` | The value to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddInt32()`

```cpp
status_t BMessage::AddInt32(const char * name, int32 value)
```

Convenience method to add an `int32` to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_INT32_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `value` | The value to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddInt64()`

```cpp
status_t BMessage::AddInt64(const char * name, int64 value)
```

Convenience method to add an `int64` to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_INT64_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `value` | The value to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddInt8()`

```cpp
status_t BMessage::AddInt8(const char * name, int8 value)
```

Convenience method to add an `int8` to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_INT8_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `value` | The value to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddMessage()`

```cpp
status_t BMessage::AddMessage(const char * name, const BMessage * message)
```

Convenience method to add a message to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_MESSAGE_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `message` | The message to store in this message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddMessenger()`

```cpp
status_t BMessage::AddMessenger(const char * name, BMessenger messenger)
```

Convenience method to add a messenger to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_MESSENGER_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `messenger` | The messenger to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddNodeRef()`

```cpp
status_t BMessage::AddNodeRef(const char * name, const node_ref * ref)
```

Convenience method to add a `node_ref` with the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_NODE_REF_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `ref` | The node reference to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** Haiku R1

---

### `AddPoint()`

```cpp
status_t BMessage::AddPoint(const char * name, BPoint aPoint)
```

Convenience method to add a [BPoint](../interface_kit/classBPoint.md) to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_POINT_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `aPoint` | The point to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddPointer()`

```cpp
status_t BMessage::AddPointer(const char * name, const void * aPointer)
```

Convenience method to add a `pointer` to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_POINTER_TYPE` *type*.



> [!WARNING]
> If you want to share objects between applications, remember that each application has its own address space, and that it therefore is useless to try to pass around objects by sending pointers in messages. You should think about copying the entire object in the message, or you should consider using shared memory.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `aPointer` | The value to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddRect()`

```cpp
status_t BMessage::AddRect(const char * name, BRect aRect)
```

Convenience method to add a [BRect](../interface_kit/classBRect.md) to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_RECT_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `aRect` | The rectangle to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddRef()`

```cpp
status_t BMessage::AddRef(const char * name, const entry_ref * ref)
```

Convenience method to add an `entry_ref` to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_REF_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `ref` | The reference to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddSize()`

```cpp
status_t BMessage::AddSize(const char * name, BSize size)
```

Convenience method to add a [BSize](../interface_kit/classBSize.md) to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_SIZE_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `size` | The [BSize](../interface_kit/classBSize.md) to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** Haiku R1

---

### `AddSpecifier()`

```cpp
status_t BMessage::AddSpecifier(const BMessage * specifier)
```

Undocumented. 



**Since:** BeOS R3

---

### `AddSpecifier()`

```cpp
status_t BMessage::AddSpecifier(const char * property)
```

Undocumented. 



**Since:** BeOS R3

---

### `AddSpecifier()`

```cpp
status_t BMessage::AddSpecifier(const char * property, const char * name)
```

Undocumented. 



**Since:** BeOS R3

---

### `AddSpecifier()`

```cpp
status_t BMessage::AddSpecifier(const char * property, int32 index)
```

Undocumented. 



**Since:** BeOS R3

---

### `AddSpecifier()`

```cpp
status_t BMessage::AddSpecifier(const char * property, int32 index, int32 range)
```

Undocumented. 



**Since:** BeOS R3

---

### `AddString()`

```cpp
status_t BMessage::AddString(const char * name, const BString & aString)
```

Convenience method to add a [BString](../support_kit/classBString.md) to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_STRING_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `aString` | The string to copy to the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R5

---

### `AddString()`

```cpp
status_t BMessage::AddString(const char * name, const char * aString)
```

Convenience method to add a C-string to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_STRING_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `aString` | The string to copy to the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddStrings()`

```cpp
status_t BMessage::AddStrings(const char * name, const BStringList & list)
```

Convenience method to add list of strings to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_STRING_TYPE` *type* for each string in the [BStringList](../support_kit/classBStringList.md).


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `list` | The list of strings to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** Haiku R1

---

### `AddUInt16()`

```cpp
status_t BMessage::AddUInt16(const char * name, uint16 value)
```

Convenience method to add an `uint16` to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_UINT16_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `value` | The value to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddUInt32()`

```cpp
status_t BMessage::AddUInt32(const char * name, uint32 value)
```

Convenience method to add an `uint32` to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_UINT32_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `value` | The value to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddUInt64()`

```cpp
status_t BMessage::AddUInt64(const char * name, uint64 value)
```

Convenience method to add an `uint64` to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_UINT64_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `value` | The value to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `AddUInt8()`

```cpp
status_t BMessage::AddUInt8(const char * name, uint8 value)
```

Convenience method to add an `uint8` to the label *name*. 


This method calls [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) with the `B_UINT8_TYPE` *type*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to associate the data with. |
| `value` | The value to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.



**See also:** [AddData()](classBMessage.md#a4b99de85becfb1058a893fc6e40c48ad) for a more detailed overview of the inner workings.



**Since:** BeOS R3

---

### `Append()`

```cpp
status_t BMessage::Append(const BMessage & message)
```

Append the data of another *message* to this message. 


This copies all the data of the *message* to this message. If an item already exists with a given name, and the incoming data is of the same type, the new items will be added to that label. If the item exists but has a different type, then the call will fail. This might leave your message in an incomplete state, because data is processed field by field, so it could be that some data was copied succesfully. After encountering an incompatible data type, any data after that field will not be processed.


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The message with the data you want to append. This message will not be modified. |





**Returns:** A status code, `B_OK` on success or an error code.

---

### `CountNames()`

```cpp
int32 BMessage::CountNames(type_code type)const
```

Count the number of names of a certain *type*. 


This method can be used to count the number of items of a certain type. It's practical use is limited to debugging purposes.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The type you want to find. If you pass `B_ANY_TYPE`, this method will return the total number of data items. |





**Returns:** The number of data items in this message with the specified *type*, or `0` in case no items match the type.



**Since:** BeOS R3

---

### `DropPoint()`

```cpp
BPoint BMessage::DropPoint(BPoint * offset = NULL)const
```

Get the coordinates of the drop point of the message. 


If the message has been delivered because of drag and drop, which can be verified with the [WasDropped()](classBMessage.md#ac66a35a4ef389a02bc36ace2cddb073e) method, this method will return a [BPoint](../interface_kit/classBPoint.md) to where exactly the drop off was made.


Because drop messages are delivered to the [BWindow](../interface_kit/classBWindow.md) in which they were dropped, and [BWindow](../interface_kit/classBWindow.md) is a subclass of [BLooper](classBLooper.md), you can use [BWindow](../interface_kit/classBWindow.md) to determine based on the location, how you should react to it.


If this message was not delivered through drag and drop, it will return a `NULL` pointer.



**See also:** [WasDropped()](classBMessage.md#ac66a35a4ef389a02bc36ace2cddb073e)



**Since:** BeOS R3

---

### `FindAlignment()`

```cpp
status_t BMessage::FindAlignment(const char * name, BAlignment * alignment)const
```

Find an alignment at the label *name*. 


This is an overloaded version of [FindAlignment(const char*, int32, BAlignment*) const](classBMessage.md#ac124217fb122b3e012ee431fb3cbd68f) where the data is sought at *index* `0`.



**Since:** Haiku R1

---

### `FindAlignment()`

```cpp
status_t BMessage::FindAlignment(const char * name, int32 index, BAlignment * alignment)const
```

Find an alignment at the label *name* at an *index*. 


This method looks for the data with the `B_ALIGNMENT_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `alignment` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindAlignment(const char*, BAlignment*) const](classBMessage.md#abf81526338001abe288b5831fcb88874)



**Since:** Haiku R1

---

### `FindBool()`

```cpp
status_t BMessage::FindBool(const char * name, bool * value)const
```

Find a boolean at the label *name*. 


This is an overloaded version of [FindBool(const char*, int32, bool*) const](classBMessage.md#a99405de493bf7e49ce033ef8cac8825b) where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `FindBool()`

```cpp
status_t BMessage::FindBool(const char * name, int32 index, bool * value)const
```

Find a boolean at the label *name* at an *index*. 


This method looks for the data with the `B_BOOL_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindBool(const char*, bool*) const](classBMessage.md#a886d79a7c580d3563940333cfa7f3870)



**Since:** BeOS R3

---

### `FindBool()`

```cpp
bool BMessage::FindBool(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `FindColor()`

```cpp
status_t BMessage::FindColor(const char * name, int32 index, rgb_color * value)const
```

Find a color at the label *name* at an *index*. 


This method looks for the data with the `B_RGB_32_BIT_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindColor(const char*, rgb_color*) const](classBMessage.md#a8980e233e8afb3f302dc5218483a5456)



**Since:** BeOS R3

---

### `FindColor()`

```cpp
status_t BMessage::FindColor(const char * name, rgb_color * value)const
```

Find a color with the label *name*. 


This is an overloaded version of [FindColor(const char*, int32, rgb_color*) const](classBMessage.md#a6e05596bbf62217b061e54a18fa51a72) where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** Haiku R1

---

### `FindData()`

```cpp
status_t BMessage::FindData(const char * name, type_code type, const void ** data, ssize_t * numBytes)const
```

Find *data* that is stored in this message. 


This is an overloaded version of [FindData(const char*, type_code, int32, const void**, ssize_t*) const](classBMessage.md#aea11107bcd353be1dfde351850fe7ee0) where data is sought at *index* `0`.



**Since:** BeOS R3

---

### `FindData()`

```cpp
status_t BMessage::FindData(const char * name, type_code type, int32 index, const void ** data, ssize_t * numBytes)const
```

Find *data* that is stored in this message at an *index*. 


This method matches the label *name* with the *type* you are asking for, and it looks for the data that is stored at a certain *index* number. If all these things match, you will get a pointer to the internal buffer, and the method will put the size of the item in *numBytes*.


Note that only this method, and FindString(const char*, const char**), pass a pointer to the internal buffer. The other more specific methods, such as [FindBool()](classBMessage.md#a886d79a7c580d3563940333cfa7f3870) and [FindRect()](classBMessage.md#a84e6020b903936f61538e33988792956) copy the data into a buffer you specify. This means that the data retrieved with this method is valid until the message is deleted.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label the data should be associated with. |
| `type` | The type of data you want to retrieve. You can pass `B_ANY_TYPE` if you don't mind which type the data is. |
| `index` | The index in the array of the data that you want to retrieve. Note that the array is zero-based. |
| `data` | A pointer to a pointer where the data can point to. |
| `numBytes` | The size of the data will be put in this parameter. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The *name* was found, matches the type, and the data at *index* has been put in *data*. |
| B_BAD_VALUE | One of the output arguments were `NULL`. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [status_t](SupportDefs_8h.md#ab6735558965995709a53691ae913c81b) [FindData(const char*, type_code, int32,
	const void**, ssize_t*) const](classBMessage.md#aea11107bcd353be1dfde351850fe7ee0)



**Since:** BeOS R3

---

### `FindDouble()`

```cpp
status_t BMessage::FindDouble(const char * name, double * value)const
```

Find a double at the label *name*. 


This is an overloaded version of [FindDouble(const char*, int32, double*) const](classBMessage.md#ac332368de00ff51eb06097e134244e5a) where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `FindDouble()`

```cpp
status_t BMessage::FindDouble(const char * name, int32 index, double * value)const
```

Find a double at the label *name* at an *index*. 


This method looks for the data with the `B_DOUBLE_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindDouble(const char*, double*) const](classBMessage.md#a32672932ca24ee53b3642bf9d25f709d)



**Since:** BeOS R3

---

### `FindDouble()`

```cpp
double BMessage::FindDouble(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `FindFlat()`

```cpp
status_t BMessage::FindFlat(const char * name, BFlattenable * object)const
```

Find a flattened object at the label *name*. 


This is an overloaded version of [FindFlat(const char*, int32, BFlattenable*) const](classBMessage.md#a017c619934572443bf1ac5161dcdb2c2) where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `object` | The object in which the data should be unflattened. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `FindFlat()`

```cpp
status_t BMessage::FindFlat(const char * name, int32 index, BFlattenable * object)const
```

Find a flattened object at the label *name* at an *index*. 


The type is determined by the type of the passed object. If that type is available at the specified label, then the [Unflatten()](classBMessage.md#a6704fc8df822fc366b616c3abf36ae9f) method of that object will be called.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be unflattened. |
| `object` | The object in which the data should be unflattened. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindFlat(const char*, BFlattenable*) const](classBMessage.md#ae910af356e0732edaa09260e47e1bbd0)



**Since:** BeOS R3

---

### `FindFloat()`

```cpp
status_t BMessage::FindFloat(const char * name, float * value)const
```

Find a float at the label *name*. 


This is an overloaded version of [FindFloat(const char*, int32, float*) const](classBMessage.md#af5d62fe0dba7074556b877a52d1cecb2) where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `FindFloat()`

```cpp
status_t BMessage::FindFloat(const char * name, int32 index, float * value)const
```

Find a float at the label *name* at an *index*. 


This method looks for the data with the `B_FLOAT_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindFloat(const char*, float*) const](classBMessage.md#ac26f15d78b69e330f9cb933db8c0500b)



**Since:** BeOS R3

---

### `FindFloat()`

```cpp
float BMessage::FindFloat(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `FindInt16()`

```cpp
status_t BMessage::FindInt16(const char * name, int16 * value)const
```

Find an integer at the label *name*. 


This is an overloaded version of [FindInt16(const char*, int32, int16*) const](classBMessage.md#afedef75ac1e9c5a1d3f069b641975041) where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `FindInt16()`

```cpp
status_t BMessage::FindInt16(const char * name, int32 index, int16 * value)const
```

Find an integer at the label *name* at an *index*. 


This method looks for the data with the `B_INT16_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindInt16(const char*, int16*) const](classBMessage.md#a4dd27c3a8fc6e2e0366d77254b2095e6)



**Since:** BeOS R3

---

### `FindInt16()`

```cpp
int16 BMessage::FindInt16(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `FindInt32()`

```cpp
status_t BMessage::FindInt32(const char * name, int32 * value)const
```

Find an integer at the label *name*. 


This is an overloaded version of [FindInt32(const char*, int32, int32*) const](classBMessage.md#afce55a9ef851c34fa07d21bcf9e2f1f2) where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `FindInt32()`

```cpp
status_t BMessage::FindInt32(const char * name, int32 index, int32 * value)const
```

Find an integer at the label *name* at an *index*. 


This method looks for the data with the `B_INT32_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindInt32(const char*, int32*) const](classBMessage.md#af6ee3d278ed11bdafb60047b03c18ab9)



**Since:** BeOS R3

---

### `FindInt32()`

```cpp
int32 BMessage::FindInt32(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `FindInt64()`

```cpp
status_t BMessage::FindInt64(const char * name, int32 index, int64 * value)const
```

Find an integer at the label *name* at an *index*. 


This method looks for the data with the `B_INT64_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindInt64(const char*, int64*) const](classBMessage.md#aedbef710d7c8e61cd4ff93efbb32889a)



**Since:** BeOS R3

---

### `FindInt64()`

```cpp
int64 BMessage::FindInt64(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `FindInt64()`

```cpp
status_t BMessage::FindInt64(const char * name, int64 * value)const
```

Find an integer at the label *name*. 


This is an overloaded version of [FindInt64(const char*, int32, int64*) const](classBMessage.md#ab3eef33595e98a3df56d18ade5f41a98) where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `FindInt8()`

```cpp
status_t BMessage::FindInt8(const char * name, int32 index, int8 * value)const
```

Find an integer at the label *name* at an *index*. 


This method looks for the data with the `B_INT8_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindInt8(const char*, int8*) const](classBMessage.md#a757685e8e85ac38f882e28bd281e9f9d)



**Since:** BeOS R3

---

### `FindInt8()`

```cpp
int8 BMessage::FindInt8(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `FindInt8()`

```cpp
status_t BMessage::FindInt8(const char * name, int8 * value)const
```

Find an integer at the label *name*. 


This is an overloaded version of [FindInt8(const char*, int32, int8*) const](classBMessage.md#aed840d1a802546534eaa95e5f1247a53) where the data is sought at *index* `0`.



**Since:** BeOS R3

---

### `FindMessage()`

```cpp
status_t BMessage::FindMessage(const char * name, BMessage * message)const
```

Find a message at the label *name*. 


This is an overloaded version of [FindMessage(const char*, int32, BMessage*) const](classBMessage.md#aecdfe05be151ea5a978225152486d44a) where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `message` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `FindMessage()`

```cpp
status_t BMessage::FindMessage(const char * name, int32 index, BMessage * message)const
```

Find a message at the label *name* at an *index*. 


This method looks for the data with the `B_MESSAGE_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `message` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindMessage(const char*, BMessage*) const](classBMessage.md#a8286c1590191f37641ac6916aaf6418b)



**Since:** BeOS R3

---

### `FindMessenger()`

```cpp
status_t BMessage::FindMessenger(const char * name, BMessenger * messenger)const
```

Find a messenger at the label *name*. 


This is an overloaded version of [FindMessenger(const char*, int32, BMessenger*) const](classBMessage.md#a87a4b0591e87332366a99d09462d9be8) where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `messenger` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `FindMessenger()`

```cpp
status_t BMessage::FindMessenger(const char * name, int32 index, BMessenger * messenger)const
```

Find a messenger at the label *name* at an *index*. 


This method looks for the data with the `B_MESSENGER_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `messenger` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindMessenger(const char*, BMessenger*) const](classBMessage.md#a1b01edbdb7740ad1a06b2e81366fd47d)



**Since:** BeOS R3

---

### `FindNodeRef()`

```cpp
status_t BMessage::FindNodeRef(const char * name, int32 index, node_ref * ref)const
```

Find a reference to a node at the label *name* at an *index*. 


This method looks for the data with the `B_NODE_REF_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `ref` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindNodeRef(const char*, node_ref*) const](classBMessage.md#acfb1819b93db7eadd0cabcd1cf1d45ec)



**Since:** Haiku R1

---

### `FindNodeRef()`

```cpp
status_t BMessage::FindNodeRef(const char * name, node_ref * ref)const
```

Find a reference to a node at the label *name*. 


This is an overloaded version of [FindNodeRef(const char*, int32, node_ref*) const](classBMessage.md#a4a4b0e9e0a52151ec8d1df979925857a) where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `ref` | The object into which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** Haiku R1

---

### `FindPoint()`

```cpp
status_t BMessage::FindPoint(const char * name, BPoint * point)const
```

Find a point at the label *name*. 


This is an overloaded version of [FindPoint(const char*, int32, BPoint*) const](classBMessage.md#a9a53e98aa4593529103051dbcd0186d4) where the data is sought at *index* `0`.



**Since:** BeOS R3

---

### `FindPoint()`

```cpp
status_t BMessage::FindPoint(const char * name, int32 index, BPoint * point)const
```

Find a point at the label *name* at an *index*. 


This method looks for the data with the `B_POINT_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `point` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindPoint(const char*, BPoint*) const](classBMessage.md#a88507a5c41974ab5c13dd5da800a68d7)



**Since:** BeOS R3

---

### `FindPoint()`

```cpp
BPoint BMessage::FindPoint(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `FindPointer()`

```cpp
status_t BMessage::FindPointer(const char * name, int32 index, void ** pointer)const
```

Find a pointer at the label *name* at an *index*. 


This method looks for the data with the `B_POINTER_TYPE`, and copies it into a provided buffer.



> [!WARNING]
> If you want to share objects between applications, remember that each application has its own address space, and that it therefore is useless to try to pass around objects by sending pointers in messages. You should think about copying the entire object in the message, or you should consider using shared memory.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `pointer` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** FindPointer(const char*, void*) const



**Since:** BeOS R3

---

### `FindPointer()`

```cpp
status_t BMessage::FindPointer(const char * name, void ** pointer)const
```

Find a pointer at the label *name*. 


This is an overloaded version of FindPointer(const char*, int32, void*) const where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `pointer` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `FindRect()`

```cpp
status_t BMessage::FindRect(const char * name, BRect * rect)const
```

Find a rectangle at the label *name*. 


This is an overloaded version of [FindRect(const char*, int32, BRect*) const](classBMessage.md#abc4398bca7420cc74c4d5cc76ccba018) where the data is sought at *index* `0`.



**Since:** BeOS R3

---

### `FindRect()`

```cpp
status_t BMessage::FindRect(const char * name, int32 index, BRect * rect)const
```

Find a rectangle at the label *name* at an *index*. 


This method looks for the data with the `B_RECT_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `rect` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindRect(const char*, BRect*) const](classBMessage.md#a84e6020b903936f61538e33988792956)



**Since:** BeOS R3

---

### `FindRect()`

```cpp
BRect BMessage::FindRect(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `FindRef()`

```cpp
status_t BMessage::FindRef(const char * name, entry_ref * ref)const
```

Find a reference to a file at the label *name*. 


This is an overloaded version of [FindRef(const char*, int32, entry_ref*) const](classBMessage.md#a4b1c2190d9f3742c86edc72c3c49eeca) where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `ref` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `FindRef()`

```cpp
status_t BMessage::FindRef(const char * name, int32 index, entry_ref * ref)const
```

Find a reference to a file at the label *name* at an *index*. 


This method looks for the data with the `B_REF_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `ref` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindRef(const char*, entry_ref*) const](classBMessage.md#a85035f98a61911e973af9a8821b5e254)



**Since:** BeOS R3

---

### `FindSize()`

```cpp
status_t BMessage::FindSize(const char * name, BSize * size)const
```

Find a size at the label *name*. 


This is an overloaded version of [FindSize(const char*, int32, BSize*) const](classBMessage.md#a769dcfc011f91c8372512f7396e6e59e) where the data is sought at *index* `0`.



**Since:** Haiku R1

---

### `FindSize()`

```cpp
status_t BMessage::FindSize(const char * name, int32 index, BSize * size)const
```

Find a size at the label *name* at an *index*. 


This method looks for the data with the `B_SIZE_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `size` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindSize(const char*, BSize*) const](classBMessage.md#a463777b0384a8ee580709c62dfbfa2ca)



**Since:** Haiku R1

---

### `FindString()`

```cpp
status_t BMessage::FindString(const char * name, BString * string)const
```

Find a string at the label *name*. 


This is an overloaded version of [FindString(const char*, int32, BString*) const](classBMessage.md#a35f163b19ec1862a2f117d1d1ac3ef46) where the data is sought at *index* `0`.



**Since:** BeOS R5

---

### `FindString()`

```cpp
status_t BMessage::FindString(const char * name, const char ** string)const
```

Find a string at the label *name*. 


This is an overloaded version of [FindString(const char*, int32, const char**) const](classBMessage.md#a4370bfd828545100484adaf51a38df47) where the data is sought at *index* `0`.



**Since:** BeOS R3

---

### `FindString()`

```cpp
status_t BMessage::FindString(const char * name, int32 index, BString * string)const
```

Find a string at the label *name* at an *index*. 


This method looks for the data with the `B_STRING_TYPE`, and copies it into the *string* object.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `string` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindString(const char*, BString*) const](classBMessage.md#a2930978f62db0238b780d67a1e74e69b)



**Since:** BeOS R5

---

### `FindString()`

```cpp
status_t BMessage::FindString(const char * name, int32 index, const char ** string)const
```

Find a string at the label *name* at an *index*. 


This method looks for the data with the `B_STRING_TYPE`, and returns a pointer to the internal buffer of the message. Note that this pointer is valid, until the message is deleted.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `string` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindString(const char*, const char**) const](classBMessage.md#ac2a5b50960210666f57952b3a050530d)



**Since:** BeOS R3

---

### `FindString()`

```cpp
const char * BMessage::FindString(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `FindStrings()`

```cpp
status_t BMessage::FindStrings(const char * name, BStringList * list)const
```

Find all the strings at the label *name*. 


This method fetches all the strings that are stored at label *name*, and copies all the entries into the *list*.



**Since:** Haiku R1

---

### `FindUInt16()`

```cpp
status_t BMessage::FindUInt16(const char * name, int32 index, uint16 * value)const
```

Find an integer at the label *name* at an *index*. 


This method looks for the data with the `B_UINT16_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindUInt16(const char*, uint16*) const](classBMessage.md#a5653c46ede97ff7667d0e823674b5953)



**Since:** BeOS R3

---

### `FindUInt16()`

```cpp
status_t BMessage::FindUInt16(const char * name, uint16 * value)const
```

Find an integer at the label *name*. 


This is an overloaded version of [FindUInt16(const char*, int32, uint16*) const](classBMessage.md#a761a6bb39440a15176c5dc600d7b7041) where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `FindUInt32()`

```cpp
status_t BMessage::FindUInt32(const char * name, int32 index, uint32 * value)const
```

Find an integer at the label *name* at an *index*. 


This method looks for the data with the `B_UINT32_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindUInt32(const char*, uint32*) const](classBMessage.md#a486a2138fb0edc7bf17b1a9676d5ecde)



**Since:** BeOS R3

---

### `FindUInt32()`

```cpp
status_t BMessage::FindUInt32(const char * name, uint32 * value)const
```

Find an integer at the label *name*. 


This is an overloaded version of [FindUInt32(const char*, int32, uint32*) const](classBMessage.md#a10e79ec598190c30d3d07c46c297eacf) where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `FindUInt64()`

```cpp
status_t BMessage::FindUInt64(const char * name, int32 index, uint64 * value)const
```

Find an integer at the label *name* at an *index*. 


This method looks for the data with the `B_UINT64_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindUInt64(const char*, uint64*) const](classBMessage.md#a20f4b14c6c45c4a24a3cbeea4347f79a)



**Since:** BeOS R3

---

### `FindUInt64()`

```cpp
status_t BMessage::FindUInt64(const char * name, uint64 * value)const
```

Find an integer at the label *name*. 


This is an overloaded version of [FindUInt64(const char*, int32, uint64*) const](classBMessage.md#abd21bedb93952f87cd12bf50c89d8612) where the data is sought at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `FindUInt8()`

```cpp
status_t BMessage::FindUInt8(const char * name, int32 index, uint8 * value)const
```

Find an integer at the label *name* at an *index*. 


This method looks for the data with the `B_UINT8_TYPE`, and copies it into a provided buffer.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The label to which the data is associated. |
| `index` | The index from which the data should be copied. |
| `value` | The object in which the data should be copied. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_BAD_INDEX | The *index* does not exist. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [FindUInt8(const char*, uint8*) const](classBMessage.md#a37170512c52bac977fb81e7c9d44ef95)



**Since:** BeOS R3

---

### `FindUInt8()`

```cpp
status_t BMessage::FindUInt8(const char * name, uint8 * value)const
```

Find an integer at the label *name*. 


This is an overloaded version of [FindUInt8(const char*, int32, uint8*) const](classBMessage.md#ab5ce6415eb074f94f1f8dc59f8c3985e) where the data is sought at *index* `0`.



**Since:** BeOS R3

---

### `Flatten()`

```cpp
status_t BMessage::Flatten(BDataIO * stream, ssize_t * size = NULL)const
```

Flatten the message to a *stream*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `stream` | The stream to flatten the message to. |
| `size` | The method writes the number of bytes actually written to this argument. |





**Returns:** `B_OK` in case of success, or an error code in case something went awry.



> [!WARNING]
> Make sure the subclass of the [BDataIO](../support_kit/classBDataIO.md) interface either protects against buffer overwrites, or check if the number of bytes that is going to be written isn't larger than it can handle.



**See also:** [FlattenedSize()](classBMessage.md#a2e3967d45e2ab17e6ab05dc45989f8c6)



**Since:** BeOS R3

---

### `Flatten()`

```cpp
status_t BMessage::Flatten(char * buffer, ssize_t size)const
```

Flatten the message to a *buffer*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | The buffer to write the data to. |
| `size` | The size of the buffer. |





**Returns:** `B_OK` in case of success, or an error code in case something went awry.



> [!WARNING]
> Make sure the buffer is large enough to hold the message. This method does not double-check for you!



**See also:** [FlattenedSize()](classBMessage.md#a2e3967d45e2ab17e6ab05dc45989f8c6)



**Since:** BeOS R3

---

### `FlattenedSize()`

```cpp
ssize_t BMessage::FlattenedSize()const
```

Return the size in bytes required when you want to flatten this message to a stream of bytes. 



**Since:** BeOS R3

---

### `GetAlignment()`

```cpp
BAlignment BMessage::GetAlignment(const char * name, const BAlignment & defaultValue)const
```

Return the [BAlignment](../interface_kit/classBAlignment.md) object from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetAlignment()`

```cpp
BAlignment BMessage::GetAlignment(const char * name, int32 index, const BAlignment & defaultValue)const
```

Return the [BAlignment](../interface_kit/classBAlignment.md) object from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetBool()`

```cpp
bool BMessage::GetBool(const char * name, bool defaultValue = false)const
```

Return the boolean value from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetBool()`

```cpp
bool BMessage::GetBool(const char * name, int32 index, bool defaultValue)const
```

Return the boolean value from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetColor()`

```cpp
rgb_color BMessage::GetColor(const char * name, int32 index, rgb_color defaultValue)const
```

Return the [rgb_color](../interface_kit/structrgb__color.md) value from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetColor()`

```cpp
rgb_color BMessage::GetColor(const char * name, rgb_color defaultValue)const
```

Return the [rgb_color](../interface_kit/structrgb__color.md) value from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetCurrentSpecifier()`

```cpp
status_t BMessage::GetCurrentSpecifier(int32 * index, BMessage * specifier = NULL, int32 * what = NULL, const char ** property = NULL)const
```

Undocumented. 



**Since:** BeOS R3

---

### `GetDouble()`

```cpp
double BMessage::GetDouble(const char * name, double defaultValue)const
```

Return the double value from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetDouble()`

```cpp
double BMessage::GetDouble(const char * name, int32 index, double defaultValue)const
```

Return the double value from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetFloat()`

```cpp
float BMessage::GetFloat(const char * name, float defaultValue)const
```

Return the float value from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetFloat()`

```cpp
float BMessage::GetFloat(const char * name, int32 index, float defaultValue)const
```

Return the float value from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetInfo()`

```cpp
status_t BMessage::GetInfo(const char * name, type_code * typeFound, bool * fixedSize)const
```

Retrieve the type and whether or not the size of the data is fixed associated with a *name*. 


This method is the same as [GetInfo(const char*, type_code*, int32*) const](classBMessage.md#a525991f82f8574bd6eb68796568eb340), with the difference that you can find out whether or not the size of the data associated with the *name* is fixed. You will get this value in the variable you passed as *fixedSize* parameter.



**Since:** BeOS R4

---

### `GetInfo()`

```cpp
status_t BMessage::GetInfo(const char * name, type_code * typeFound, int32 * countFound, bool * fixedSize)const
```

Retrieve the type and whether or not the size of the data is fixed associated with a *name*. 


This method is the same as [GetInfo(const char*, type_code*, int32*) const](classBMessage.md#a525991f82f8574bd6eb68796568eb340), with the difference that you can find out whether or not the size of the data associated with the *name* is fixed. You will get this value in the variable you passed as *fixedSize* parameter.



**Since:** BeOS R4

---

### `GetInfo()`

```cpp
status_t BMessage::GetInfo(const char * name, type_code * typeFound, int32 * countFound = NULL)const
```

Retrieve the type and the number of data items in this message that are associated with a *name*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the data member that you are looking for. |
| `typeFound` | In case of a match, the name of the data member will be put in this parameter. In case you are not interested, you can pass `NULL`. |
| `countFound` | In case of a match, the number of items at this label will be in this parameter. In case you are not interested, you can safely pass `NULL`. |





**Returns:** If the message has data associated with the given *name*, the other parameters will contain information associated with the data, else, the method will return with an error.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | A match was found. The other parameters have been filled in. |
| B_BAD_VALUE | You passed `NULL` as argument to *name*. |
| B_NAME_NOT_FOUND | There is no data with the label *name*. |





**Since:** BeOS R3

---

### `GetInfo()`

```cpp
status_t BMessage::GetInfo(type_code typeRequested, int32 index, char ** nameFound, type_code * typeFound, int32 * countFound = NULL)const
```

Retrieve the name, the type and the number of items in a message by an *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `typeRequested` | If you want to limit the search to only one type, pass that type code here. If you don't care which type the data has, you can pass `B_ANY_TYPE`. |
| `index` | The index of the data you want to investigate. |
| `nameFound` | The name of the item if it is found. Haiku will fill in a pointer to the internal name buffer in the message. This means that you should not manipulate this name. If you are not interested in the name, you can safely pass `NULL`. |
| `typeFound` | The type of the item at *index*. If you are not interested in the type (because you specifically asked for a type), you can safely pass `NULL`. |
| `countFound` | The number of items at *index*. If data items have the same name, they will be placed under the same index. |





**Returns:** If the *index* is found, and matches the requested type, then the other parameters will be filled in. If this is not the case, the method will return with an error.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | An match was found. The values have been filled in. |
| B_BAD_INDEX | The *index* was out of range. None of the passed variables have been altered. |
| B_BAD_TYPE | The data field at *index* does not have the requested type. |





**Since:** BeOS R3

---

### `GetInt16()`

```cpp
int16 BMessage::GetInt16(const char * name, int16 defaultValue)const
```

Return the int16 value from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetInt16()`

```cpp
int16 BMessage::GetInt16(const char * name, int32 index, int16 defaultValue)const
```

Return the int16 value from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetInt32()`

```cpp
int32 BMessage::GetInt32(const char * name, int32 defaultValue)const
```

Return the int32 value from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetInt32()`

```cpp
int32 BMessage::GetInt32(const char * name, int32 index, int32 defaultValue)const
```

Return the int32 value from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetInt64()`

```cpp
int64 BMessage::GetInt64(const char * name, int32 index, int64 defaultValue)const
```

Return the int64 value from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetInt64()`

```cpp
int64 BMessage::GetInt64(const char * name, int64 defaultValue)const
```

Return the int64 value from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetInt8()`

```cpp
int8 BMessage::GetInt8(const char * name, int32 index, int8 defaultValue)const
```

Return the int8 value from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetInt8()`

```cpp
int8 BMessage::GetInt8(const char * name, int8 defaultValue)const
```

Return the int8 value from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetPoint()`

```cpp
BPoint BMessage::GetPoint(const char * name, const BPoint & defaultValue)const
```

Return the [BPoint](../interface_kit/classBPoint.md) object from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetPoint()`

```cpp
BPoint BMessage::GetPoint(const char * name, int32 index, const BPoint & defaultValue)const
```

Return the [BPoint](../interface_kit/classBPoint.md) object from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetPointer()`

```cpp
const void * BMessage::GetPointer(const char * name, const void * defaultValue = NULL)const
```

Return the pointer type from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetPointer()`

```cpp
rgb_color BMessage::GetPointer(const char * name, int32 index, const void * defaultValue = NULL)const
```

Return the pointer type from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetRect()`

```cpp
BRect BMessage::GetRect(const char * name, const BRect & defaultValue)const
```

Return the [BRect](../interface_kit/classBRect.md) object from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetRect()`

```cpp
BRect BMessage::GetRect(const char * name, int32 index, const BRect & defaultValue)const
```

Return the [BRect](../interface_kit/classBRect.md) object from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetSize()`

```cpp
BSize BMessage::GetSize(const char * name, const BSize & defaultValue)const
```

Return the [BSize](../interface_kit/classBSize.md) object from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetSize()`

```cpp
BSize BMessage::GetSize(const char * name, int32 index, const BSize & defaultValue)const
```

Return the [BSize](../interface_kit/classBSize.md) object from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetString()`

```cpp
const char * BMessage::GetString(const char * name, const char * defaultValue = NULL)const
```

Return the string from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetString()`

```cpp
const char * BMessage::GetString(const char * name, int32 index, const char * defaultValue)const
```

Return the string from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetUInt16()`

```cpp
uint16 BMessage::GetUInt16(const char * name, int32 index, uint16 defaultValue)const
```

Return the uint16 value from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetUInt16()`

```cpp
uint16 BMessage::GetUInt16(const char * name, uint16 defaultValue)const
```

Return the uint16 value from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetUInt32()`

```cpp
uint32 BMessage::GetUInt32(const char * name, int32 index, uint32 defaultValue)const
```

Return the uint32 value from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetUInt32()`

```cpp
uint32 BMessage::GetUInt32(const char * name, uint32 defaultValue)const
```

Return the uint32 value from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetUInt64()`

```cpp
uint64 BMessage::GetUInt64(const char * name, int32 index, uint64 defaultValue)const
```

Return the uint64 value from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetUInt64()`

```cpp
uint64 BMessage::GetUInt64(const char * name, uint64 defaultValue)const
```

Return the uint64 value from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetUInt8()`

```cpp
uint8 BMessage::GetUInt8(const char * name, int32 index, uint8 defaultValue)const
```

Return the uint8 message from message with *name* and *index*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `index` | The index of the item to retrieve if there is more than one. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `GetUInt8()`

```cpp
uint8 BMessage::GetUInt8(const char * name, uint8 defaultValue)const
```

Return the uint8 value from message with *name*, or *defaultValue* if not found. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item to retrieve. |
| `defaultValue` | The value to use if the item specified by *name* is not found. |





**Returns:** The item with *name*, or *defaultValue* if not found.



**Since:** Haiku R1

---

### `HasAlignment()`

```cpp
bool BMessage::HasAlignment(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** Haiku R1

---

### `HasBool()`

```cpp
bool BMessage::HasBool(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasColor()`

```cpp
bool BMessage::HasColor(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** Haiku R1

---

### `HasData()`

```cpp
bool BMessage::HasData(const char * name, type_code, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasDouble()`

```cpp
bool BMessage::HasDouble(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasFlat()`

```cpp
bool BMessage::HasFlat(const char * name, const BFlattenable * object)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasFlat()`

```cpp
bool BMessage::HasFlat(const char * name, int32 n, const BFlattenable * object)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasFloat()`

```cpp
bool BMessage::HasFloat(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasInt16()`

```cpp
bool BMessage::HasInt16(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasInt32()`

```cpp
bool BMessage::HasInt32(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasInt64()`

```cpp
bool BMessage::HasInt64(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasInt8()`

```cpp
bool BMessage::HasInt8(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasMessage()`

```cpp
bool BMessage::HasMessage(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasMessenger()`

```cpp
bool BMessage::HasMessenger(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasNodeRef()`

```cpp
bool BMessage::HasNodeRef(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** Haiku R1.

---

### `HasPoint()`

```cpp
bool BMessage::HasPoint(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasPointer()`

```cpp
bool BMessage::HasPointer(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasRect()`

```cpp
bool BMessage::HasRect(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasRef()`

```cpp
bool BMessage::HasRef(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasSameData()`

```cpp
bool BMessage::HasSameData(const BMessage & other, bool ignoreFieldOrder = true, bool deep = false)const
```

Experimental method to compare two messages. 


This helper method will compare the data of this message to another message. The name if the fields, and the contents of the fields are compared. Metadata (like the delivery status) and the [BMessage::what](classBMessage.md#ad074faab0857f51fba778f0d8558df1e) field are not compared.


The order of the fields is determined by the order that the fields are added. You may use the *ignoreFieldOrder* argument to tweak whether you care that not only the data is identical, but also the ordering of the data.


When there are BMessages attached to this message, you might want to use this algorithm to compare them as well (as to ignore non-data fields of the *other* message or the ordering of fields during the comparison). Setting the *deep* parameter will cause any data of the `B_MESSAGE_TYPE` to be compared using this method, thus ignoring non-data differences. If you set *deep* to `false`, the data will be compared on a byte by byte basis and these differences in the non-data fields will not be ignored.


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The other message to compare to. |
| `ignoreFieldOrder` | Whether you want to see if the field order is the same. |
| `deep` | Whether you want to recursively inspect BMessages embedded in this message. |





**Returns:** `true` if the data is the same, `false` otherwise



**Since:** Haiku R1

---

### `HasSize()`

```cpp
bool BMessage::HasSize(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** Haiku R1

---

### `HasSpecifiers()`

```cpp
bool BMessage::HasSpecifiers()const
```

Undocumented. 



**Since:** BeOS R3

---

### `HasString()`

```cpp
bool BMessage::HasString(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasUInt16()`

```cpp
bool BMessage::HasUInt16(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasUInt32()`

```cpp
bool BMessage::HasUInt32(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasUInt64()`

```cpp
bool BMessage::HasUInt64(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `HasUInt8()`

```cpp
bool BMessage::HasUInt8(const char * name, int32 n = 0)const
```

Deprecated. 



> [!WARNING]
> This method is deprecated, do not use.



**Since:** BeOS R3

---

### `IsEmpty()`

```cpp
bool BMessage::IsEmpty()const
```

Check if the message has data members. 



**Returns:** If this message contains data members, this method will return `true`, else it will return `false`.



**See also:** [MakeEmpty()](classBMessage.md#abac76b537c88ce7f1a127fa6425c3279)



**Since:** BeOS R3

---

### `IsReply()`

```cpp
bool BMessage::IsReply()const
```

Check if the message is a reply to a (previous) message. 



**Returns:** If this message is a reply, this method will return `true`.



**Since:** BeOS R3

---

### `IsSourceRemote()`

```cpp
bool BMessage::IsSourceRemote()const
```

Check if the message is sent by another application. 



**Since:** BeOS R3

---

### `IsSourceWaiting()`

```cpp
bool BMessage::IsSourceWaiting()const
```

Check if the sender expects a reply. 


This method will return `true`, if the sender flagged that it is waiting for a reply, and such a reply has not yet been sent.



**Since:** BeOS R3

---

### `IsSystem()`

```cpp
bool BMessage::IsSystem()const
```

Check if the message is a system message. 



**Returns:** If this message is a system message, the method will return `true`.



**Since:** BeOS R3

---

### `MakeEmpty()`

```cpp
status_t BMessage::MakeEmpty()
```

Clear all data and metadata in this message. 


Everything is cleared out, all labels and all associated data, as well as metadata such as reply info.



**Returns:** This method always returns `B_OK`.



**See also:** [RemoveData()](classBMessage.md#a72ce9596ebe74ce6e995705304b7fc7d)



**Since:** BeOS R3

---

### `operator delete()`

```cpp
void BMessage::operator delete(void * pointer, size_t size)
```

Frees memory allocated by new. 



**Since:** BeOS R5

---

### `operator new()`

```cpp
void * BMessage::operator new(size_t size)
```

Allocates *size* bytes of memory for a [BMessage](classBMessage.md). 



**Since:** BeOS R3

---

### `operator new()`

```cpp
void * BMessage::operator new(size_t, const std::nothrow_t & noThrow)
```

Allocates *size* bytes of memory for a [BMessage](classBMessage.md). 



**Since:** Haiku R1

---

### `operator new()`

```cpp
void * BMessage::operator new(size_t, void * pointer)
```

Allocates *size* bytes of memory for a [BMessage](classBMessage.md). 



**Since:** BeOS R3

---

### `operator=()`

```cpp
BMessage & BMessage::operator=(const BMessage & other)
```

Copy one message into another. 


See the copy constructor, [BMessage(const BMessage& other)](classBMessage.md#a6ab8aaec65db99134ea76790884c3af7), for details on what is copied, and what isn't.



**Since:** BeOS R3

---

### `PopSpecifier()`

```cpp
status_t BMessage::PopSpecifier()
```

Undocumented. 



**Since:** BeOS R3

---

### `Previous()`

```cpp
const BMessage * BMessage::Previous()const
```

Get the message to which this message is a reply. 



**Returns:** Returns a new [BMessage](classBMessage.md) with the same data stuctures as the message to which this message is a reply. The pointer is only valid as long as this message is still allocated, you do not get ownership. If this message isn't a reply to another message, this method will return `NULL`.



**Since:** BeOS R3

---

### `PrintToStream()`

```cpp
void BMessage::PrintToStream()const
```

Print the message to the standard output. 


This method can be used to debug your application. It can be used to check if it creates the messages properly, by checking if all the required fields are present, and it can be used to debug your message handling routines, especially the handling of those that are sent by external applications, to see if you understand the semantics correctly.



**Since:** BeOS R3

---

### `RemoveData()`

```cpp
status_t BMessage::RemoveData(const char * name, int32 index = 0)
```

Remove data associated with *name* at a specified *index*. 


If this is the only instance of the data, then the entire label will be removed. This means you can recreate it with another type.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The *name* of which the associated data should be cleared. |
| `index` | The *index* of the item that should be cleared. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The data has been removed. |
| B_BAD_VALUE | The *index* is less than `0`. |
| B_BAD_INDEX | The *index* is out of bounds. |
| B_NAME_NOT_FOUND | The *name* does not have any data associated with it. |





**See also:** [RemoveName()](classBMessage.md#a5db9b5a9ddc0b04173afb8dbc1c69e5c)



**Since:** BeOS R3

---

### `RemoveName()`

```cpp
status_t BMessage::RemoveName(const char * name)
```

Remove all data associated with a *name*. 


This also removes the label, so that you can recreate it with another type, if you want to.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The *name* that refers to the data you want to clear out. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | All the data is removed. |
| B_BAD_VALUE | The *name* pointer points to `NULL`. |
| B_NAME_NOT_FOUND | The *name* does not exist in this message. |





**See also:** [RemoveData()](classBMessage.md#a72ce9596ebe74ce6e995705304b7fc7d)



**Since:** BeOS R3

---

### `Rename()`

```cpp
status_t BMessage::Rename(const char * oldEntry, const char * newEntry)
```

Rename a data label. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `oldEntry` | The name of the label you want to rename. |
| `newEntry` | The new name of the data entry. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Renaming succeeded. |
| B_BAD_VALUE | Either the *oldEntry* or the *newEntry* pointers are `NULL`. |
| B_NAME_NOT_FOUND | There is no data associated with the label *oldEntry*. |





**Since:** Haiku R1

---

### `ReplaceAlignment()`

```cpp
status_t BMessage::ReplaceAlignment(const char * name, const BAlignment & alignment)
```

Replace an alignment at the label *name*. 


This method is an overloaded method of [ReplaceAlignment(const char*, int32, const BAlignment&)](classBMessage.md#ae6f32ad46aa14db07c9d324656daf871). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `alignment` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** Haiku R1

---

### `ReplaceAlignment()`

```cpp
status_t BMessage::ReplaceAlignment(const char * name, int32 index, const BAlignment & alignment)
```

Replace an alignment at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_ALIGNMENT_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `alignment` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceAlignment(const char*, const BAlignment&)](classBMessage.md#a7613f4cdd1154b3e70771fdc9a4e3e04)



**Since:** Haiku R1

---

### `ReplaceBool()`

```cpp
status_t BMessage::ReplaceBool(const char * name, bool aBoolean)
```

Replace a boolean at the label *name*. 


This method is an overloaded method of [ReplaceBool(const char*, int32, bool)](classBMessage.md#af6bfc87ac8fe3f470b8d73a01dca388a). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `aBoolean` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceBool()`

```cpp
status_t BMessage::ReplaceBool(const char * name, int32 index, bool aBoolean)
```

Replace a boolean at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_BOOL_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `aBoolean` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceBool(const char*, bool)](classBMessage.md#a64357e8743595d49dd53975e3f534a3f)



**Since:** BeOS R5

---

### `ReplaceColor()`

```cpp
status_t BMessage::ReplaceColor(const char * name, int32 index, rgb_color aColor)
```

Replace a [rgb_color](../interface_kit/structrgb__color.md) at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_RGB_32_BIT_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `aColor` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceColor(const char*, rgb_color)](classBMessage.md#af712a6b0c6921803023c1314e39b09fd)



**Since:** Haiku R1

---

### `ReplaceColor()`

```cpp
status_t BMessage::ReplaceColor(const char * name, rgb_color aColor)
```

Replace a color at the label *name*. 


This method is an overloaded method of [ReplaceColor(const char*, int32, rgb_color)](classBMessage.md#ae0e39566d16d42b40a55e9809a3e93f9). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `aColor` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** Haiku R1

---

### `ReplaceData()`

```cpp
status_t BMessage::ReplaceData(const char * name, type_code type, const void * data, ssize_t numBytes)
```

Replace the data at label *name*. 


This method is an overloaded method that replaces the data at *index* `0`. See [ReplaceData(const char*, type_code, int32, const void*, ssize_t)](classBMessage.md#a8d5e1ec791c56202414c6c1c407163d4).


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `type` | The type of the data. |
| `data` | A pointer to the new data that needs to be copied into the message. |
| `numBytes` | The size of the new data. |





**Returns:** A status code, `B_OK` on success or an error code.



**Since:** BeOS R3

---

### `ReplaceData()`

```cpp
status_t BMessage::ReplaceData(const char * name, type_code type, int32 index, const void * data, ssize_t numBytes)
```

Replace the data at label *name* at a specified *index*. 


The conditions for replacing data are that the*name* is correct, the *type* matches and the data entry at *index* exists.


There is also a collection of convenience methods, that allow you to efficiently replace rectanges ([ReplaceRect()](classBMessage.md#aa24fb4e8fbc39011d1b7fb55c7f752c1)), booleans ([ReplaceBool()](classBMessage.md#a64357e8743595d49dd53975e3f534a3f)), and so on.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `type` | The type of the data. |
| `index` | The index in the array to replace. |
| `data` | A pointer to the new data that needs to be copied into the message. |
| `numBytes` | The size of the new data. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_VALUE | One of the input parameters are invalid. Check that you did not pass `NULL`, and in case the field has fixed sized data, check that *numBytes* is the same as the specified fixed size. |
| B_BAD_INDEX | The *index* is out of range. |





**Since:** BeOS R3

---

### `ReplaceDouble()`

```cpp
status_t BMessage::ReplaceDouble(const char * name, double aDouble)
```

Replace a double at the label *name*. 


This method is an overloaded method of [ReplaceDouble(const char*, int32, double)](classBMessage.md#aee50e26caa09886d0cdcbc753a91317f). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `aDouble` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceDouble()`

```cpp
status_t BMessage::ReplaceDouble(const char * name, int32 index, double aDouble)
```

Replace a double at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_DOUBLE_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `aDouble` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceDouble(const char*, double)](classBMessage.md#a023f8e3aa932cd312acd5653ecebaca4)



**Since:** BeOS R3

---

### `ReplaceFlat()`

```cpp
status_t BMessage::ReplaceFlat(const char * name, BFlattenable * object)
```

Replace a flattened object at the label *name*. 


This method is an overloaded method of [ReplaceFlat(const char*, int32, BFlattenable*)](classBMessage.md#a32f79d59881b7bf9df0f1ab819fd9390).


It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `object` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceFlat()`

```cpp
status_t BMessage::ReplaceFlat(const char * name, int32 index, BFlattenable * object)
```

Replace a flattened object at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the type returned by your object. This method uses [BFlattenable::TypeCode()](../support_kit/classBFlattenable.md#a819507fa1b0906f14299db15f6e990d1) to determine the type of the object.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `object` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceFlat(const char*, BFlattenable*)](classBMessage.md#aaa8c8f67ea3314d93f39e1618b19621e)



**Since:** BeOS R3

---

### `ReplaceFloat()`

```cpp
status_t BMessage::ReplaceFloat(const char * name, float aFloat)
```

Replace a float at the label *name*. 


This method is an overloaded method of [ReplaceFloat(const char*, int32, float)](classBMessage.md#ad081e12c8b593d03c7fbee4ea61c8f34). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `aFloat` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceFloat()`

```cpp
status_t BMessage::ReplaceFloat(const char * name, int32 index, float aFloat)
```

Replace a float at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_FLOAT_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `aFloat` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceFloat(const char*, float)](classBMessage.md#ab0c54a885d2cf1826dcb2fa53cfd0175)



**Since:** BeOS R3

---

### `ReplaceInt16()`

```cpp
status_t BMessage::ReplaceInt16(const char * name, int16 value)
```

Replace an integer at the label *name*. 


This method is an overloaded method of [ReplaceInt16(const char*, int32, int16)](classBMessage.md#a05b21498414818bc51e76451a26a143f). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `value` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceInt16()`

```cpp
status_t BMessage::ReplaceInt16(const char * name, int32 index, int16 value)
```

Replace an integer at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_INT16_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `value` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceInt16(const char*, int16)](classBMessage.md#a525deaa699950007c8fdab78c82ada32)



**Since:** BeOS R3

---

### `ReplaceInt32()`

```cpp
status_t BMessage::ReplaceInt32(const char * name, int32 index, int32 value)
```

Replace an integer at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_INT32_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `value` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceInt32(const char*, int32)](classBMessage.md#ad7b41f02b8a298bcd6699e972b88c82e)



**Since:** BeOS R3

---

### `ReplaceInt32()`

```cpp
status_t BMessage::ReplaceInt32(const char * name, int32 value)
```

Replace an integer at the label *name*. 


This method is an overloaded method of [ReplaceInt32(const char*, int32, int32)](classBMessage.md#ae1fe7f9855edb57e186cac617569cb79). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `value` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceInt64()`

```cpp
status_t BMessage::ReplaceInt64(const char * name, int32 index, int64 value)
```

Replace an integer at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_INT64_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `value` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceInt64(const char*, int64)](classBMessage.md#a97220953786ff1cbb286e7e1113510ff)



**Since:** BeOS R3

---

### `ReplaceInt64()`

```cpp
status_t BMessage::ReplaceInt64(const char * name, int64 value)
```

Replace an integer at the label *name*. 


This method is an overloaded method of [ReplaceInt64(const char*, int32, int64)](classBMessage.md#ac92d2b43a1dbc3e6591e0ddb03880e9b). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `value` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceInt8()`

```cpp
status_t BMessage::ReplaceInt8(const char * name, int32 index, int8 value)
```

Replace an integer at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_INT8_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `value` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceInt8(const char*, int8)](classBMessage.md#a55f909d237c7c1abfca5f918a8a5ffb9)



**Since:** BeOS R3

---

### `ReplaceInt8()`

```cpp
status_t BMessage::ReplaceInt8(const char * name, int8 value)
```

Replace an integer at the label *name*. 


This method is an overloaded method of [ReplaceInt8(const char*, int32, int8)](classBMessage.md#a8ae3786000645416e1911fe2b618c432). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `value` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceMessage()`

```cpp
status_t BMessage::ReplaceMessage(const char * name, const BMessage * message)
```

Replace a message at the label *name*. 


This method is an overloaded method of ReplaceMessage(const char*, int32, BMessage*). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `message` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceMessage()`

```cpp
status_t BMessage::ReplaceMessage(const char * name, int32 index, const BMessage * message)
```

Replace a message at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_MESSAGE_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `message` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** ReplaceMessage(const char*, BMessage*)



**Since:** BeOS R3

---

### `ReplaceMessenger()`

```cpp
status_t BMessage::ReplaceMessenger(const char * name, BMessenger messenger)
```

Replace a messenger at the label *name*. 


This method is an overloaded method of [ReplaceMessenger(const char*, int32, BMessenger)](classBMessage.md#ad21e673615ff361bb5facce2632b57c1). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `messenger` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceMessenger()`

```cpp
status_t BMessage::ReplaceMessenger(const char * name, int32 index, BMessenger messenger)
```

Replace a messenger at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_MESSENGER_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `messenger` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceMessenger(const char*, BMessenger)](classBMessage.md#ada775f0c198e3968eedd03a6ad2daa49)



**Since:** BeOS R3

---

### `ReplaceNodeRef()`

```cpp
status_t BMessage::ReplaceNodeRef(const char * name, const node_ref * ref)
```

Replace a reference to a node at the label *name*. 


This method is an overloaded method of ReplaceNodeRef(const char*, int32, node_ref*). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `ref` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** Haiku R1

---

### `ReplaceNodeRef()`

```cpp
status_t BMessage::ReplaceNodeRef(const char * name, int32 index, const node_ref * ref)
```

Replace a reference to a node at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_NODE_REF_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `ref` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** ReplaceNodeRef(const char*, node_ref*)



**Since:** Haiku R1

---

### `ReplacePoint()`

```cpp
status_t BMessage::ReplacePoint(const char * name, BPoint aPoint)
```

Replace a point at the label *name*. 


This method is an overloaded method of [ReplacePoint(const char*, int32, BPoint)](classBMessage.md#a4897600b32e200802cf7c5d397f7e8cf). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `aPoint` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplacePoint()`

```cpp
status_t BMessage::ReplacePoint(const char * name, int32 index, BPoint aPoint)
```

Replace a point at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_POINT_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `aPoint` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplacePoint(const char*, BPoint)](classBMessage.md#ac1b948f0c5867720173ef96450201859)



**Since:** BeOS R3

---

### `ReplacePointer()`

```cpp
status_t BMessage::ReplacePointer(const char * name, const void * pointer)
```

Replace a pointer at the label *name*. 


This method is an overloaded method of [ReplacePointer(const char*, int32, const void*)](classBMessage.md#a77be90c4ecd92ca28cea4dbc46f8e8a2). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `pointer` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplacePointer()`

```cpp
status_t BMessage::ReplacePointer(const char * name, int32 index, const void * pointer)
```

Replace a pointer at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_POINTER_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `pointer` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplacePointer(const char*, const void*)](classBMessage.md#aaa543367787ed528566a4f629e78f60b)



**Since:** BeOS R3

---

### `ReplaceRect()`

```cpp
status_t BMessage::ReplaceRect(const char * name, BRect aRect)
```

Replace a rectangle at the label *name*. 


This method is an overloaded method of [ReplaceRect(const char*, int32, BRect)](classBMessage.md#a2e38c3d43259b9157cc5c8647030dac0). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `aRect` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceRect()`

```cpp
status_t BMessage::ReplaceRect(const char * name, int32 index, BRect aRect)
```

Replace a rectangle at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_RECT_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `aRect` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceRect(const char*, BRect)](classBMessage.md#aa24fb4e8fbc39011d1b7fb55c7f752c1)



**Since:** BeOS R3

---

### `ReplaceRef()`

```cpp
status_t BMessage::ReplaceRef(const char * name, const entry_ref * ref)
```

Replace a reference to a file at the label *name*. 


This method is an overloaded method of ReplaceRef(const char*, int32, entry_ref*). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `ref` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceRef()`

```cpp
status_t BMessage::ReplaceRef(const char * name, int32 index, const entry_ref * ref)
```

Replace a reference to a file at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_REF_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `ref` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** ReplaceRef(const char*, entry_ref*)



**Since:** BeOS R3

---

### `ReplaceSize()`

```cpp
status_t BMessage::ReplaceSize(const char * name, BSize aSize)
```

Replace a size at the label *name*. 


This method is an overloaded method of [ReplaceSize(const char*, int32, BSize)](classBMessage.md#a9ff6d6940725e22e2fab190bf42a1659). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `aSize` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object now contains the requested data. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** Haiku R1

---

### `ReplaceSize()`

```cpp
status_t BMessage::ReplaceSize(const char * name, int32 index, BSize aSize)
```

Replace a size at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_SIZE_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `aSize` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceSize(const char*, BSize)](classBMessage.md#a440d37083df7c8845d3337cc8c9d695a)



**Since:** Haiku R1

---

### `ReplaceString()`

```cpp
status_t BMessage::ReplaceString(const char * name, const BString & aString)
```

Replace a string at the label *name*. 


This method is an overloaded method of ReplaceString(const char*, int32, BString&). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `aString` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R5

---

### `ReplaceString()`

```cpp
status_t BMessage::ReplaceString(const char * name, const char * aString)
```

Replace a string at the label *name*. 


This method is an overloaded method of [ReplaceString(const char*, int32, const char*)](classBMessage.md#aceeabb6ee480223b56d58e42a87ba7f5). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `aString` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceString()`

```cpp
status_t BMessage::ReplaceString(const char * name, int32 index, const BString & aString)
```

Replace a string at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_STRING_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `aString` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** ReplaceString(const char*, BString&)



**Since:** BeOS R5

---

### `ReplaceString()`

```cpp
status_t BMessage::ReplaceString(const char * name, int32 index, const char * aString)
```

Replace a string at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_STRING_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `aString` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceString(const char*, const char*)](classBMessage.md#a3a606679aa72f7530034994f9cf4ad32)



**Since:** BeOS R3

---

### `ReplaceUInt16()`

```cpp
status_t BMessage::ReplaceUInt16(const char * name, int32 index, uint16 value)
```

Replace an integer at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_UINT16_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `value` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceUInt16(const char*, uint16)](classBMessage.md#a0029cb535e97ed753ee9529c646d763b)



**Since:** BeOS R3

---

### `ReplaceUInt16()`

```cpp
status_t BMessage::ReplaceUInt16(const char * name, uint16 value)
```

Replace an integer at the label *name*. 


This method is an overloaded method of [ReplaceUInt16(const char*, int32, uint16)](classBMessage.md#ab5d7606278375f280ab402b9f7e388be). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `value` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceUInt32()`

```cpp
status_t BMessage::ReplaceUInt32(const char * name, int32 index, uint32 value)
```

Replace an integer at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_UINT32_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `value` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceUInt32(const char*, uint32)](classBMessage.md#afdfe554348e5e672a1a358f3b944d63e)



**Since:** BeOS R3

---

### `ReplaceUInt32()`

```cpp
status_t BMessage::ReplaceUInt32(const char * name, uint32 value)
```

Replace an integer at the label *name*. 


This method is an overloaded method of [ReplaceUInt32(const char*, int32, uint32)](classBMessage.md#a8bd5a2123e4097377f33d12aca43b615). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `value` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceUInt64()`

```cpp
status_t BMessage::ReplaceUInt64(const char * name, int32 index, uint64 value)
```

Replace an integer at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_UINT64_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `value` | The object to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceUInt64(const char*, uint64)](classBMessage.md#ad906dc7124f3dab9f41ca94f678c29d4)



**Since:** BeOS R3

---

### `ReplaceUInt64()`

```cpp
status_t BMessage::ReplaceUInt64(const char * name, uint64 value)
```

Replace an integer at the label *name*. 


This method is an overloaded method of [ReplaceUInt64(const char*, int32, uint64)](classBMessage.md#a66c1638d29c7474762e7ce3799785ffa). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `value` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReplaceUInt8()`

```cpp
status_t BMessage::ReplaceUInt8(const char * name, int32 index, uint8 value)
```

Replace an integer at the label *name* at a specified *index*. 


The data at the specified *name* and *index* will be replaced, if it matches the `B_UINT8_TYPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `index` | The index in the array to replace. |
| `value` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_BAD_INDEX | The index was out of range. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**See also:** [ReplaceUInt8(const char*, uint8)](classBMessage.md#aee573704ea412f6b53e1904e22e65454)



**Since:** BeOS R3

---

### `ReplaceUInt8()`

```cpp
status_t BMessage::ReplaceUInt8(const char * name, uint8 value)
```

Replace an integer at the label *name*. 


This method is an overloaded method of [ReplaceUInt8(const char*, int32, uint8)](classBMessage.md#aff3cffe95f04bf5576393f65bb378a1c). It replaces the data at *index* `0`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name associated with the data to replace. |
| `value` | Where to store in the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The operation succeeded. |
| B_NAME_NOT_FOUND | There is no field with this *name*. |





**Since:** BeOS R3

---

### `ReturnAddress()`

```cpp
BMessenger BMessage::ReturnAddress()const
```

Get a messenger that points to the sender of the message. 


Using this method, you can fetch a [BMessenger](classBMessenger.md) that can be used to deliver replies to this message. This method works both for local and remote deliveries.


For remote deliveries, this approach is preferred over sending the reply using a standard [BMessenger](classBMessenger.md) that is created with the signature of the application. A standard [BMessenger](classBMessenger.md) sends the messages to the main [BLooper](classBLooper.md) of the application, the [BApplication](classBApplication.md) object. With the delivery data stored in the messages, the reply using this messenger will be directed at a specific looper that is able to handle the replies.


If this method is called on a message that has not been delivered (yet), it will return an empty [BMessenger](classBMessenger.md) object.



**Since:** BeOS R3

---

### `SendReply()`

```cpp
status_t BMessage::SendReply(BMessage * reply, BHandler * replyTo = NULL, bigtime_t timeout = B_INFINITE_TIMEOUT)
```

Asynchronously send a reply to this message. 


This is an overloaded member of [SendReply(BMessage*, BMessenger, bigtime_t)](classBMessage.md#a410113620d52a30f7622a96f8a7077c6). Use this variant if you want to send the message to a specific handler (instead of a complete messenger).



**Since:** BeOS R3

---

### `SendReply()`

```cpp
status_t BMessage::SendReply(BMessage * reply, BMessage * replyToReply, bigtime_t sendTimeout = B_INFINITE_TIMEOUT, bigtime_t replyTimeout = B_INFINITE_TIMEOUT)
```

Synchronously send a reply to this message, and wait for a reply back. 


This method sends a reply to this message to the sender. The *reply* is delivered, and then the method waits for a reply from the receiver. If a reply is received, that reply is copied into the *replyToReply* argument. If the message was delivered properly, but the receiver did not reply within the specified *replyTimeout*, the *what* member of *replyToReply* will be set to `B_NO_REPLY`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `reply` | The message that is in reply to this message. |
| `replyToReply` | The reply is copied into this argument. |
| `sendTimeout` | The maximum time in microseconds this delivery may take. The *timeout* is a relative timeout. You can also use `B_INFINITE_TIMEOUT` if you want to wait infinitely for the message to be delivered. |
| `replyTimeout` | The maximum time in microseconds you want to wait for a reply. Note that the timer starts when the message has been delivered. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The message has been delivered. |
| B_DUPLICATE_REPLY | There already has been a reply to this message. |
| B_BAD_VALUE | Either *reply* or *replyToReply* is `NULL`. |
| B_BAD_PORT_ID | The reply address is not valid (anymore). |
| B_WOULD_BLOCK | The delivery *timeout* was `B_INFINITE_TIMEOUT` (`0`) and the target port was full when trying to deliver the message. |
| B_TIMED_OUT | The timeout expired while trying to deliver the message. |
| B_NO_MORE_PORTS | All reply ports are in use. |





**See also:** [SendReply(uint32 command, BMessage* replyToReply)](classBMessage.md#a039a8ff8563bbc58c54a50ca417ac75e)



**Since:** BeOS R3

---

### `SendReply()`

```cpp
status_t BMessage::SendReply(BMessage * reply, BMessenger replyTo, bigtime_t timeout = B_INFINITE_TIMEOUT)
```

Asynchronously send a reply to this message. 


This method sends a reply to this message to the sender. On your turn, you specify a messenger that handles a reply back to the message you specify as the *reply* argument. You can set a timeout for the message to be delivered. This method blocks until the message has been received, or the *timeout* has been reached.


Parameters

| Parameter | Description |
| :--- | :--- |
| `reply` | The message that is in reply to this message. |
| `replyTo` | In case the receiver needs to reply to the message you are sending, you can specify the return address with this argument. |
| `timeout` | The maximum time in microseconds this delivery may take. The *timeout* is a relative timeout. You can also use `B_INFINITE_TIMEOUT` if you want to wait infinitely for the message to be delivered. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The message has been delivered. |
| B_DUPLICATE_REPLY | There already has been a reply to this message. |
| B_BAD_PORT_ID | The reply address is not valid (anymore). |
| B_WOULD_BLOCK | The delivery *timeout* was `B_INFINITE_TIMEOUT` (`0`) and the target port was full when trying to deliver the message. |
| B_TIMED_OUT | The timeout expired while trying to deliver the message. |





**See also:** [SendReply(uint32 command, BHandler* replyTo)](classBMessage.md#aad1eb085346e2c91133e372e7924637c)



**Since:** Haiku R1

---

### `SendReply()`

```cpp
status_t BMessage::SendReply(uint32 command, BHandler * replyTo = NULL)
```

Asynchronously send a reply to this message. 


This is an overloaded member of [SendReply(BMessage*, BMessenger, bigtime_t)](classBMessage.md#a410113620d52a30f7622a96f8a7077c6). Use this variant if you want to send a message without data members.



**Since:** BeOS R3

---

### `SendReply()`

```cpp
status_t BMessage::SendReply(uint32 command, BMessage * replyToReply)
```

Synchronously send a reply to this message, and wait for a reply back. 


This is an overloaded member of [SendReply(BMessage*, BMessage*, bigtime_t, bigtime_t)](classBMessage.md#a5461fc22f8bf044d21fd5429b7977213) Use this variant if you want to send a message without data members.



**Since:** BeOS R3

---

### `SetAlignment()`

```cpp
status_t BMessage::SetAlignment(const char * name, const BAlignment & value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls [AddAlignment(const char*, const BAlignment &)](classBMessage.md#a4fa4e6bcc354814dc17b61532480837d) in case the item does not exist yet, and [ReplaceAlignment(const char*, const BAlignment &)](classBMessage.md#a7613f4cdd1154b3e70771fdc9a4e3e04) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetBool()`

```cpp
status_t BMessage::SetBool(const char * name, bool value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls [AddBool(const char*, bool)](classBMessage.md#a2976642c2259ebad33704d1b127bae60) in case the item does not exist yet, and [ReplaceBool(const char*, bool)](classBMessage.md#a64357e8743595d49dd53975e3f534a3f) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetColor()`

```cpp
status_t BMessage::SetColor(const char * name, rgb_color value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls [AddColor(const char*, rgb_color)](classBMessage.md#ae6e41cb30d1fb757a264a38ca6c27224) in case the item does not exist yet, and [ReplaceColor(const char*, rgb_color)](classBMessage.md#af712a6b0c6921803023c1314e39b09fd) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetCurrentSpecifier()`

```cpp
status_t BMessage::SetCurrentSpecifier(int32 index)
```

Undocumented. 



**Since:** Haiku R1

---

### `SetData()`

```cpp
status_t BMessage::SetData(const char * name, type_code type, const void * data, ssize_t numBytes, bool fixedSize = true, int count = 1)
```

Low level function to set data to a certain value. 


This method is used internally. Use the Set* methods above.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetDouble()`

```cpp
status_t BMessage::SetDouble(const char * name, double value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls [AddDouble(const char*, double)](classBMessage.md#a77a042d689d478572e23e87c3ad9982f) in case the item does not exist yet, and [ReplaceDouble(const char*, double)](classBMessage.md#a023f8e3aa932cd312acd5653ecebaca4) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetFloat()`

```cpp
status_t BMessage::SetFloat(const char * name, float value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls [AddFloat(const char*, float)](classBMessage.md#acdffd573b491074deef980df9f7f6e07) in case the item does not exist yet, and [ReplaceFloat(const char*, float)](classBMessage.md#ab0c54a885d2cf1826dcb2fa53cfd0175) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetInt16()`

```cpp
status_t BMessage::SetInt16(const char * name, int16 value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls [AddInt16(const char*, int16)](classBMessage.md#a8e865679288281553721414aa17a7fea) in case the item does not exist yet, and [ReplaceInt16(const char*, int16)](classBMessage.md#a525deaa699950007c8fdab78c82ada32) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetInt32()`

```cpp
status_t BMessage::SetInt32(const char * name, int32 value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls [AddInt32(const char*, int32)](classBMessage.md#aa4d9d24d521c499aefd512b18d1e38c5) in case the item does not exist yet, and [ReplaceInt32(const char*, int32)](classBMessage.md#ad7b41f02b8a298bcd6699e972b88c82e) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetInt64()`

```cpp
status_t BMessage::SetInt64(const char * name, int64 value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls [AddInt64(const char*, int64)](classBMessage.md#ad172f4c606396d8457a686fb16d0be31) in case the item does not exist yet, and [ReplaceInt64(const char*, int64)](classBMessage.md#a97220953786ff1cbb286e7e1113510ff) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetInt8()`

```cpp
status_t BMessage::SetInt8(const char * name, int8 value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls [AddInt8(const char*, int8)](classBMessage.md#a224c55f626ae3a4552d06788539c7d60) in case the item does not exist yet, and [ReplaceInt8(const char*, int8)](classBMessage.md#a55f909d237c7c1abfca5f918a8a5ffb9) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetPoint()`

```cpp
status_t BMessage::SetPoint(const char * name, const BPoint & value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls AddPoint(const char*, const BPoint &) in case the item does not exist yet, and ReplacePoint(const char*, const BPoint &) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetPointer()`

```cpp
status_t BMessage::SetPointer(const char * name, const void * value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls [AddPointer(const char*, const void*)](classBMessage.md#a3dc68e69cb8da2ca0f7512e42c4393fe) in case the item does not exist yet, and [ReplacePointer(const char*, const void*)](classBMessage.md#aaa543367787ed528566a4f629e78f60b) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetRect()`

```cpp
status_t BMessage::SetRect(const char * name, const BRect & value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls AddRect(const char*, const BRect &) in case the item does not exist yet, and ReplaceRect(const char*, const BRect &) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetSize()`

```cpp
status_t BMessage::SetSize(const char * name, const BSize & value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls AddSize(const char*, const BSize &) in case the item does not exist yet, and ReplaceSize(const char*, const BSize &) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetString()`

```cpp
status_t BMessage::SetString(const char * name, const BString & string)
```

Set the string with at the label *name* to *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `string` | The value to set the item to. |




This function calls [AddString(const char*, const BString&)](classBMessage.md#a76d63dc8621996c05a8c2b8186b28efb) in case the item does not exist yet, and [ReplaceString(const char*, const BString&)](classBMessage.md#a15b2ce4ff50f420a64422545079af452) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetString()`

```cpp
status_t BMessage::SetString(const char * name, const char * string)
```

Set the string with at the label *name* to *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `string` | The value to set the item to. |




This function calls [AddString(const char*, const char*)](classBMessage.md#a342311ccdf68206c4b879bcd0f2d6e83) in case the item does not exist yet, and [ReplaceString(const char*, const char*)](classBMessage.md#a3a606679aa72f7530034994f9cf4ad32) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetUInt16()`

```cpp
status_t BMessage::SetUInt16(const char * name, uint16 value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls [AddUInt16(const char*, uint16)](classBMessage.md#aa43cedc7a1d6ecdc26041e6657c9288d) in case the item does not exist yet, and [ReplaceUInt16(const char*, uint16)](classBMessage.md#a0029cb535e97ed753ee9529c646d763b) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetUInt32()`

```cpp
status_t BMessage::SetUInt32(const char * name, uint32 value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls [AddUInt32(const char*, uint32)](classBMessage.md#acc2a562d501b88ce8fe55ae4017d3bb6) in case the item does not exist yet, and [ReplaceUInt32(const char*, uint32)](classBMessage.md#afdfe554348e5e672a1a358f3b944d63e) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetUInt64()`

```cpp
status_t BMessage::SetUInt64(const char * name, uint64 value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls [AddUInt64(const char*, uint64)](classBMessage.md#a1c6b3d4ee371ccb4ddfc6c0fd1dc8e58) in case the item does not exist yet, and [ReplaceUInt64(const char*, uint64)](classBMessage.md#ad906dc7124f3dab9f41ca94f678c29d4) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `SetUInt8()`

```cpp
status_t BMessage::SetUInt8(const char * name, uint8 value)
```

Set the data with at the label *name* to *value*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the item. |
| `value` | The value to set the item to. |




This function calls [AddUInt8(const char*, uint8)](classBMessage.md#a98bbc2ca6c4fcb26bcd162c06ea0f46f) in case the item does not exist yet, and [ReplaceUInt8(const char*, uint8)](classBMessage.md#aee573704ea412f6b53e1904e22e65454) in case it does.



**Returns:** A status code, `B_OK` in case of success and `B_BAD_TYPE` in case the item already exists with a different data type.



**Since:** Haiku R1

---

### `Unflatten()`

```cpp
status_t BMessage::Unflatten(BDataIO * stream)
```

Unflatten a message from a stream and put it into the current object. 


This action clears the current contents of the message.


Parameters

| Parameter | Description |
| :--- | :--- |
| `stream` | The stream that contains the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The message has been unflattened. |
| B_BAD_VALUE | The stream does not contain a valid message. |
| B_NO_MEMORY | An error occured whilst allocating memory for the data members. |





**See also:** [Flatten(BDataIO* stream, ssize_t* size) const](classBMessage.md#ae0b47fbff10bc50153144b178fc1537d)



**Since:** BeOS R3

---

### `Unflatten()`

```cpp
status_t BMessage::Unflatten(const char * flatBuffer)
```

Unflatten a message from a buffer and put it into the current object. 


This action clears the current contents of the message.


Parameters

| Parameter | Description |
| :--- | :--- |
| `flatBuffer` | The buffer that contains the message. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The buffer has been unflattened. |
| B_BAD_VALUE | The buffer does not contain a valid message. |
| B_NO_MEMORY | An error occured whilst allocating memory for the data members. |





**See also:** [Flatten(char* buffer, ssize_t size) const](classBMessage.md#a736092eded1a6846cba89cd43bca26d3)



**Since:** BeOS R3

---

### `WasDelivered()`

```cpp
bool BMessage::WasDelivered()const
```

Check if this message was delivered through the delivery methods. 


If this message is passed via a [BMessenger](classBMessenger.md) or [BLooper::PostMessage()](classBLooper.md#a0de6737bfbf8a8b4913adc8c74bb544e), this method will return `true`.



> [!WARNING]
> This method should not be abused by a thread that sends a message to track whether or not a message was delivered. This is because the ownership of the message goes to the receiving looper, which will delete the message as soon as it is done with it.



**Since:** BeOS R3

---

### `WasDropped()`

```cpp
bool BMessage::WasDropped()const
```

Check if the message was delivered through 'drag and drop'. 



**Returns:** This method returns `true` if the message has been delivered through drag and drop. It returns `false` if it has been delivered through the regular messaging functions, or if the message has not been delivered at all.



**See also:** [DropPoint()](classBMessage.md#a6785e345338000b685a3b5b182cc993a)



**Since:** BeOS R3

---

### `what`

```cpp
BMessage::what
```

A 4-byte constant that determines the type of message. 


You can directly manipulate this data member.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMessage.html).
