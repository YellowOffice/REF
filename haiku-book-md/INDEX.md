# Haiku Book API Index

Generated from Haiku documentation dated Tue Sep 29 2026 18:24:13.

| Name | Type | Kit | Brief |
| :--- | :--- | :--- | :--- |
| [app_info](application_kit/app__info.md) | struct | application_kit | Provides info for a running app |
| [Application Level API Incompatibilities with BeOS](special_topics/compatibility.md) | topic | special_topics | Haiku R1 (x86) was designed and is being implemented to be binary and source compatible with applications written for BeOS R5 (x86) to a large extent, but not the other way around |
| [BAbstractSocket](network_kit/BAbstractSocket.md) | class | network_kit | Abstract interface for all socket connections |
| [BAffineTransform](interface_kit/BAffineTransform.md) | class | interface_kit | Undocumented class |
| [BAlert](interface_kit/BAlert.md) | class | interface_kit | The BAlert class defines a modal alert dialog which displays a short message and provides a set of labeled buttons that allow the user to respond |
| [BAlignment](interface_kit/BAlignment.md) | class | interface_kit | Undocumented class |
| [BAppFileInfo](storage_kit/BAppFileInfo.md) | class | storage_kit | Provides access to the metadata associated with executables, libraries and add-ons |
| [BApplication](application_kit/BApplication.md) | class | application_kit | A container object for an application |
| [BArchivable](support_kit/BArchivable.md) | class | support_kit | Interface for objects that can be archived into a BMessage |
| [BArchiver](support_kit/BArchiver.md) | class | support_kit | A class that simplifies the archiving of complicated BArchivable hierarchies |
| [BAttributedMailAttachment](mail_kit/BAttributedMailAttachment.md) | class | mail_kit | Represents an mail attachment compatible with Be File System attributes |
| [BAutolock](support_kit/BAutolock.md) | class | support_kit | Convenient utility to make parts of your code thread-safe easily |
| [BBitmap](interface_kit/BBitmap.md) | class | interface_kit | Access and manipulate digital images commonly known as bitmaps |
| [BBitmapStream](translation_kit/BBitmapStream.md) | class | translation_kit | Provides for the conversion of a Translation Kit bitmap object to a BBitmap |
| [BBlockCache](support_kit/BBlockCache.md) | class | support_kit | A class that creates and maintains a pool of memory blocks |
| [BBox](interface_kit/BBox.md) | class | interface_kit | A rectangular view with a border and an optional label to group related subviews visually |
| [BBuffer](media_kit/BBuffer.md) | class | media_kit | A reference to a chunk of memory useful for sharing media data between applications and nodes |
| [BBufferedDataIO](support_kit/BBufferedDataIO.md) | class | support_kit | Undocumented class |
| [BBufferIO](support_kit/BBufferIO.md) | class | support_kit | A buffered adapter for BPositionIO objects |
| [BButton](interface_kit/BButton.md) | class | interface_kit | A control used to initiate an action |
| [BCardLayout](interface_kit/BCardLayout.md) | class | interface_kit | The BCardLayout class is a simple BLayout subclass that arranges the items as a stack of cards with only one card being on top and visible to the user |
| [BCatalog](locale_kit/BCatalog.md) | class | locale_kit | String localization handling |
| [BCertificate](network_kit/BCertificate.md) | class | network_kit | BCertificate is a class that represents a digital certificate used in encrypted network connections, such as X.509 certificates |
| [BChannelControl](interface_kit/BChannelControl.md) | class | interface_kit | BChannelControl is the base class for controls that have several |
| [BChannelSlider](interface_kit/BChannelSlider.md) | class | interface_kit | Undocumented class |
| [BCheckBox](interface_kit/BCheckBox.md) | class | interface_kit | A user interface element used to make a binary decision |
| [BClipboard](application_kit/BClipboard.md) | class | application_kit | Used for short-term data storage between documents and applications via copy and paste operations |
| [BCollator](locale_kit/BCollator.md) | class | locale_kit | Class for handling locale-aware collation (sorting) of strings |
| [BColorControl](interface_kit/BColorControl.md) | class | interface_kit | BColorControl displays an on-screen color picker |
| [BControl](interface_kit/BControl.md) | class | interface_kit | BControl is the base class for user-event handling objects |
| [BCountry](locale_kit/BCountry.md) | class | locale_kit | Class representing a country |
| [BCursor](application_kit/BCursor.md) | class | application_kit | BCursor describes a view-wide or application-wide cursor |
| [BDatagramSocket](network_kit/BDatagramSocket.md) | class | network_kit | BAbstractSocket implementation for datagram connections |
| [BDataIO](support_kit/BDataIO.md) | class | support_kit | Abstract interface for objects that provide read and write access to data |
| [BDateFormat](locale_kit/BDateFormat.md) | class | locale_kit | Formatter for dates |
| [BDateTimeFormat](locale_kit/BDateTimeFormat.md) | class | locale_kit | Formatter for datetimes |
| [BDeskbar](interface_kit/BDeskbar.md) | class | interface_kit | Undocumented class |
| [BDirectory](storage_kit/BDirectory.md) | class | storage_kit | A directory in the file system |
| [BDirectWindow](game_kit/BDirectWindow.md) | class | game_kit | Provides direct access to the video card graphics frame buffer |
| [BDragger](interface_kit/BDragger.md) | class | interface_kit | A view that allows the user drag and drop a target view |
| [BDurationFormat](locale_kit/BDurationFormat.md) | class | locale_kit | Formatter for time intervals |
| [BEntry](storage_kit/BEntry.md) | class | storage_kit | A location in the filesystem |
| [BEntryList](storage_kit/BEntryList.md) | class | storage_kit | Interface for iterating through a list of filesystem entries |
| [BFile](storage_kit/BFile.md) | class | storage_kit | Provides the ability to read and write the data of a file |
| [BFileGameSound](game_kit/BFileGameSound.md) | class | game_kit | Playback audio from a sound file on disk |
| [BFileInterface](media_kit/BFileInterface.md) | class | media_kit | A node that can read and write data to a file on disk |
| [BFilePanel](storage_kit/BFilePanel.md) | class | storage_kit | Displays a standard Open/Save dialog |
| [BFlattenable](support_kit/BFlattenable.md) | class | support_kit | Interface for classes that can flatten and unflatten themselves to a stream of bytes |
| [BFont](interface_kit/BFont.md) | class | interface_kit | Represents a typeface including its family, style and size |
| [BGameSound](game_kit/BGameSound.md) | class | game_kit | BGameSound is the base class used in the other sound classes in the kit |
| [BGroupView](interface_kit/BGroupView.md) | class | interface_kit | Container view for a collection of views organized in a horizontal or vertical row |
| [BHandler](application_kit/BHandler.md) | class | application_kit | Handles messages that are passed on by a BLooper |
| [BIconUtils](interface_kit/BIconUtils.md) | class | interface_kit | The BIconUtils class provide utility methods for managing and drawing vector icons |
| [BInputDevice](interface_kit/BInputDevice.md) | class | interface_kit | Undocumented class |
| [BInvoker](application_kit/BInvoker.md) | class | application_kit | An object that can be \"invoked\" to send a message to a BHandler |
| [BJoystick](device_kit/BJoystick.md) | class | device_kit | Class that provides an interface to joysticks and game controllers |
| [BKey](application_kit/BKey.md) | class | application_kit | Class that represents a generic key for or from the Haiku key store |
| [BKeyStore](application_kit/BKeyStore.md) | class | application_kit | The BKeyStore lets you query, retrieve and store keys in the system's key store |
| [BLayout](interface_kit/BLayout.md) | class | interface_kit | The BLayout class provides an interface, and some basic implementation to manage the positioning and sizing of BLayoutItem s |
| [BLayoutItem](interface_kit/BLayoutItem.md) | class | interface_kit | Abstract class representing things that are positionable and resizable by objects of the BLayout class |
| [BList](support_kit/BList.md) | class | support_kit | An ordered container that is designed to hold generic void* objects |
| [BListItem](interface_kit/BListItem.md) | class | interface_kit | A list item, a member of a BListView or BOutlineListView |
| [BListView](interface_kit/BListView.md) | class | interface_kit | Displays a list of items that the user can select and invoke |
| [BLocale](locale_kit/BLocale.md) | class | locale_kit | Class for representing a locale and its settings |
| [BLocaleRoster](locale_kit/BLocaleRoster.md) | class | locale_kit | Main class for accessing the Locale Kit data |
| [BLocker](support_kit/BLocker.md) | class | support_kit | Semaphore-type class for thread safety |
| [BLooper](application_kit/BLooper.md) | class | application_kit | Receive and process messages in a separate thread |
| [BMailAttachment](mail_kit/BMailAttachment.md) | class | mail_kit | Abstract interface for objects that handle mail attachments |
| [BMailComponent](mail_kit/BMailComponent.md) | class | mail_kit | The base class for most of the Mail Kit |
| [BMailDaemon](mail_kit/BMailDaemon.md) | class | mail_kit | Provides user level access to the mail_daemon to perform common mail tasks such as check for new messages or send queued messages |
| [BMallocIO](support_kit/BMallocIO.md) | class | support_kit | A BPositionIO derived class that creates a memory buffer |
| [BMemoryIO](support_kit/BMemoryIO.md) | class | support_kit | A BPositionIO derived class that works on memory buffers |
| [BMemoryRingIO](support_kit/BMemoryRingIO.md) | class | support_kit | An implementation of a ring buffer with a BDataIO interface |
| [BMenu](interface_kit/BMenu.md) | class | interface_kit | Displays a list of menu items including additional menus arranged hierarchically |
| [BMenuBar](interface_kit/BMenuBar.md) | class | interface_kit | A window's root menu |
| [BMenuField](interface_kit/BMenuField.md) | class | interface_kit | A labeled pop-up menu |
| [BMenuItem](interface_kit/BMenuItem.md) | class | interface_kit | Display item for the BMenu class |
| [BMessage](application_kit/BMessage.md) | class | application_kit | A container that can be send and received using the Haiku messaging subsystem |
| [BMessageFilter](application_kit/BMessageFilter.md) | class | application_kit | Describes a message filter for BLooper and BHandler |
| [BMessageQueue](application_kit/BMessageQueue.md) | class | application_kit | A container that maintains a queue of messages |
| [BMessageRunner](application_kit/BMessageRunner.md) | class | application_kit | Provides a mechanism for sending one or more messages to a messenger at a specified interval and receive reply messages |
| [BMessenger](application_kit/BMessenger.md) | class | application_kit | A class to send messages to a target BLooper or BHandler |
| [BMidiConsumer](midi_2_kit/BMidiConsumer.md) | class | midi_2_kit | Receives MIDI events from a producer |
| [BMidiEndpoint](midi_2_kit/BMidiEndpoint.md) | class | midi_2_kit | Base class for all MIDI endpoints |
| [BMidiLocalConsumer](midi_2_kit/BMidiLocalConsumer.md) | class | midi_2_kit | A consumer endpoint that is created by your own application |
| [BMidiLocalProducer](midi_2_kit/BMidiLocalProducer.md) | class | midi_2_kit | A producer endpoint that is created by your own application |
| [BMidiProducer](midi_2_kit/BMidiProducer.md) | class | midi_2_kit | Streams MIDI events to connected consumers |
| [BMidiRoster](midi_2_kit/BMidiRoster.md) | class | midi_2_kit | Interface to the system-wide Midi Roster |
| [BMimeType](storage_kit/BMimeType.md) | class | storage_kit | A class that represents a MIME (Multi-purpose Internet Mail Extensions) type string |
| [BNetworkAddress](network_kit/BNetworkAddress.md) | class | network_kit | BNetworkAddress class represents a network address |
| [BNetworkDevice](network_kit/BNetworkDevice.md) | class | network_kit | BNetworkDevice class represents a network device |
| [BNetworkRoster](network_kit/BNetworkRoster.md) | class | network_kit | BNetworkRoster class allows to manage network interfaces as well as persistent (wireless) networks |
| [BNetworkRoute](network_kit/BNetworkRoute.md) | class | network_kit | BNetworkRoute class represents a network route, a path for traffic across one or multiple networks |
| [BNode](storage_kit/BNode.md) | class | storage_kit | A BNode represents a chunk of data in the filesystem |
| [BNodeInfo](storage_kit/BNodeInfo.md) | class | storage_kit | Provides access to file type meta data on a node |
| [BNotification](application_kit/BNotification.md) | class | application_kit | Construct system-default notifications to be displayed to the user |
| [BNumberFormat](locale_kit/BNumberFormat.md) | class | locale_kit | Formatter for numbers and monetary values |
| [BObjectList< T, Owning > Template Reference](support_kit/BObjectList.md) | class | support_kit | BObjectList is a wrapper around BList that adds type safety, optional object ownership, search, and insert operations |
| [BOptionControl](interface_kit/BOptionControl.md) | class | interface_kit | Undocumented class |
| [BOptionPopUp](interface_kit/BOptionPopUp.md) | class | interface_kit | A BMenuField based BControl implementation |
| [BOutlineListView](interface_kit/BOutlineListView.md) | class | interface_kit | Expands upon BListView to display a hierarchical list of items |
| [BPasswordKey](application_kit/BPasswordKey.md) | class | application_kit | Class that represents a password for or from the Haiku key store |
| [BPath](storage_kit/BPath.md) | class | storage_kit | A class representing a file system path |
| [BPathFinder](storage_kit/BPathFinder.md) | class | storage_kit | Helper class to retrieve paths in the file system layout |
| [BPicture](interface_kit/BPicture.md) | class | interface_kit | Records a series of drawing instructions that can be \"replayed\" later |
| [BPictureButton](interface_kit/BPictureButton.md) | class | interface_kit | A button draw with a BPicture image instead of a text label |
| [BPoint](interface_kit/BPoint.md) | class | interface_kit | A point on a two-dimensional Cartesian coordinate system |
| [BPolygon](interface_kit/BPolygon.md) | class | interface_kit | A closed, many-sided figure which defines an area in a two-dimensional Cartesian coordinate system |
| [BPopUpMenu](interface_kit/BPopUpMenu.md) | class | interface_kit | Displays a pop-up menu |
| [BPositionIO](support_kit/BPositionIO.md) | class | support_kit | Abstract interface that provides advanced read, write and seek access to data |
| [BPrivate::Network::BBorrow< T > Template Reference](netservices_kit/BPrivate_1_1Network_1_1BBorrow.md) | class | netservices_kit | Smart pointer that borrows an object from a BExclusiveBorrow owner |
| [BPrivate::Network::BBorrowError](netservices_kit/BPrivate_1_1Network_1_1BBorrowError.md) | class | netservices_kit | Error while handling a BExclusiveBorrow or BBorrow object |
| [BPrivate::Network::BError](netservices_kit/BPrivate_1_1Network_1_1BError.md) | class | netservices_kit | Abstract base class for advanced error objects |
| [BPrivate::Network::BExclusiveBorrow< T > Template Reference](netservices_kit/BPrivate_1_1Network_1_1BExclusiveBorrow.md) | class | netservices_kit | Smart pointer that allows shared ownership of an object with exclusive access |
| [BPrivate::Network::BHttpAuthentication](netservices_kit/BPrivate_1_1Network_1_1BHttpAuthentication.md) | struct | netservices_kit | Describe username and password for basic authentication for the request |
| [BPrivate::Network::BHttpBody](netservices_kit/BPrivate_1_1Network_1_1BHttpBody.md) | struct | netservices_kit | Represents a HTTP response body |
| [BPrivate::Network::BHttpFields](netservices_kit/BPrivate_1_1Network_1_1BHttpFields.md) | class | netservices_kit | Represents the field section of a HTTP header |
| [BPrivate::Network::BHttpFields::Field](netservices_kit/BPrivate_1_1Network_1_1BHttpFields_1_1Field.md) | class | netservices_kit | Represents a HTTP header field |
| [BPrivate::Network::BHttpFields::FieldName](netservices_kit/BPrivate_1_1Network_1_1BHttpFields_1_1FieldName.md) | class | netservices_kit | Representation of a HTTP header name |
| [BPrivate::Network::BHttpFields::InvalidInput](netservices_kit/BPrivate_1_1Network_1_1BHttpFields_1_1InvalidInput.md) | class | netservices_kit | Error that represents when a string input contains characters that are incompatible with the HTTP specification |
| [BPrivate::Network::BHttpMethod](netservices_kit/BPrivate_1_1Network_1_1BHttpMethod.md) | class | netservices_kit | Represent a HTTP method |
| [BPrivate::Network::BHttpMethod::InvalidMethod](netservices_kit/BPrivate_1_1Network_1_1BHttpMethod_1_1InvalidMethod.md) | class | netservices_kit | Error that represents when a custom method does not conform to the HTTP standard |
| [BPrivate::Network::BHttpRequest](netservices_kit/BPrivate_1_1Network_1_1BHttpRequest.md) | class | netservices_kit | Represent a HTTP request |
| [BPrivate::Network::BHttpRequest::Body](netservices_kit/BPrivate_1_1Network_1_1BHttpRequest_1_1Body.md) | struct | netservices_kit | Describe the body for a network request |
| [BPrivate::Network::BHttpResult](netservices_kit/BPrivate_1_1Network_1_1BHttpResult.md) | class | netservices_kit | Unique object to wait for and access a HTTP response data |
| [BPrivate::Network::BHttpSession](netservices_kit/BPrivate_1_1Network_1_1BHttpSession.md) | class | netservices_kit | Schedule, execute and manage HTTP requests |
| [BPrivate::Network::BHttpStatus](netservices_kit/BPrivate_1_1Network_1_1BHttpStatus.md) | struct | netservices_kit | Represents the HTTP status code and status text of an incoming response |
| [BPrivate::Network::BHttpTime](netservices_kit/BPrivate_1_1Network_1_1BHttpTime.md) | class | netservices_kit | Utility class that can parse and format HTTP Date strings |
| [BPrivate::Network::BHttpTime::InvalidInput](netservices_kit/BPrivate_1_1Network_1_1BHttpTime_1_1InvalidInput.md) | class | netservices_kit | Error that indicates that a string cannot be parsed as a valid HTTP timestamp |
| [BPrivate::Network::BInvalidUrl](netservices_kit/BPrivate_1_1Network_1_1BInvalidUrl.md) | class | netservices_kit | Error that indicates that the URL is not valid |
| [BPrivate::Network::BNetworkRequestError](netservices_kit/BPrivate_1_1Network_1_1BNetworkRequestError.md) | class | netservices_kit | Error that indicates there was an issue executing the network request |
| [BPrivate::Network::BRuntimeError](netservices_kit/BPrivate_1_1Network_1_1BRuntimeError.md) | class | netservices_kit | Advanced error object for runtime errors |
| [BPrivate::Network::BSystemError](netservices_kit/BPrivate_1_1Network_1_1BSystemError.md) | class | netservices_kit | Advanced error object that wrap low-level system errors |
| [BPrivate::Network::BUnsupportedProtocol](netservices_kit/BPrivate_1_1Network_1_1BUnsupportedProtocol.md) | class | netservices_kit | Error that indicates that the protocol is not supported |
| [BPropertyInfo](application_kit/BPropertyInfo.md) | class | application_kit | Class used to manage scripting |
| [BProxySecureSocket](network_kit/BProxySecureSocket.md) | class | network_kit | BProxySecureSocket is a class that extends BSecureSocket to have an encrypted connection via an HTTP proxy server |
| [BQuery](storage_kit/BQuery.md) | class | storage_kit | Provides an interface for creating file system queries and implements BEntryList methods for iterating through the results |
| [BRadioButton](interface_kit/BRadioButton.md) | class | interface_kit | A user interface control used to select between a set of mutually exclusive options |
| [BRect](interface_kit/BRect.md) | class | interface_kit | Defines a rectangular area aligned along pixel dimensions |
| [BReference< Type > Template Reference](support_kit/BReference.md) | class | support_kit | A reference to a BReferenceable object |
| [BReferenceable](support_kit/BReferenceable.md) | class | support_kit | Implementation of reference-counted memory management |
| [BRefFilter](storage_kit/BRefFilter.md) | class | storage_kit | Allows you to filter the items displayed in a file panel |
| [BRegion](interface_kit/BRegion.md) | class | interface_kit | An area composed of rectangles |
| [BResources](storage_kit/BResources.md) | class | storage_kit | Provides an interface for accessing and manipulating file resources |
| [BRoster](application_kit/BRoster.md) | class | application_kit | The BRoster class lets you launch apps and keeps track of apps that are running |
| [BScreen](interface_kit/BScreen.md) | class | interface_kit | The BScreen class provides methods to retrieve and change display settings |
| [BScrollBar](interface_kit/BScrollBar.md) | class | interface_kit | User interface element used to scroll a target view vertically or horizontally |
| [BScrollView](interface_kit/BScrollView.md) | class | interface_kit | A convenience class used to add scrolling to a target view |
| [BSecureSocket](network_kit/BSecureSocket.md) | class | network_kit | BSecureSocket is a class that extends BSocket to provide encrypted connection using the TLS or SSL protocols |
| [BSeparatorItem](interface_kit/BSeparatorItem.md) | class | interface_kit | Display separator item for BMenu class |
| [BSeparatorView](interface_kit/BSeparatorView.md) | class | interface_kit | Undocumented class |
| [BSerialPort](device_kit/BSerialPort.md) | class | device_kit | BSerialPort provides an interface for communicating with devices connected through a serial port |
| [BShape](interface_kit/BShape.md) | class | interface_kit | Encapsulates a Postscript-style \"path\ |
| [BShapeIterator](interface_kit/BShapeIterator.md) | class | interface_kit | Allows you to iterate through BShape operations |
| [BShelf](interface_kit/BShelf.md) | class | interface_kit | A container attached to a BView that accepts BDragger objects (replicants) |
| [BSimpleGameSound](game_kit/BSimpleGameSound.md) | class | game_kit | BSimpleGameSound represents a simple sound effect that remains in memory |
| [BSimpleMailAttachment](mail_kit/BSimpleMailAttachment.md) | class | mail_kit | Represents a basic mail attachment |
| [BSize](interface_kit/BSize.md) | class | interface_kit | A two-dimensional size |
| [BSocket](network_kit/BSocket.md) | class | network_kit | BSocket is a class used to perform stream-based socket connections |
| [BStackOrHeapArray< Type, StackSize > Template Reference](support_kit/BStackOrHeapArray.md) | class | support_kit | Undocumented class |
| [BStatable](storage_kit/BStatable.md) | class | storage_kit | Pure abstract class that provides a wrapper interface to the POSIX® stat() function |
| [BStatusBar](interface_kit/BStatusBar.md) | class | interface_kit | Undocumented class |
| [BStopWatch](support_kit/BStopWatch.md) | class | support_kit | A simple class used to time events like a stop watch |
| [BString](support_kit/BString.md) | class | support_kit | String class supporting common string operations |
| [BStringItem](interface_kit/BStringItem.md) | class | interface_kit | A list item of a text string used as a member of a BListView or BOutlineListView |
| [BStringList](support_kit/BStringList.md) | class | support_kit | Undocumented class |
| [BStringView](interface_kit/BStringView.md) | class | interface_kit | Draws a non-editable single-line text string, most commonly used as a label |
| [BSymLink](storage_kit/BSymLink.md) | class | storage_kit | Provides an interface for creating, manipulating, and accessing the contents of symbolic links |
| [BTab](interface_kit/BTab.md) | class | interface_kit | A tab that goes in a BTabView |
| [BTabView](interface_kit/BTabView.md) | class | interface_kit | A container for BTab objects to display all tabs |
| [BTextControl](interface_kit/BTextControl.md) | class | interface_kit | Displays a labeled text view control |
| [BTextMailComponent](mail_kit/BTextMailComponent.md) | class | mail_kit | A component that stores plain text |
| [BTextView](interface_kit/BTextView.md) | class | interface_kit | Displays and manipulates styled text |
| [BTimeFormat](locale_kit/BTimeFormat.md) | class | locale_kit | Formatter for times |
| [BTimeZone](locale_kit/BTimeZone.md) | class | locale_kit | Defines the time zone API which specifies a time zone, allows you to display it to the user, and converts between GMT and local time |
| [BTranslator](translation_kit/BTranslator.md) | class | translation_kit | Abstract class that defines the necessary functionality of a translator |
| [BTranslatorRoster](translation_kit/BTranslatorRoster.md) | class | translation_kit | Class that serves as an interface between applications and translators |
| [buffer_clone_info](media_kit/buffer__clone__info.md) | struct | media_kit | A struct that stores where in memory a BBuffer object is in memory as well as the buffer flags |
| [BUnarchiver](support_kit/BUnarchiver.md) | class | support_kit | A class that simplifies the unarchiving of complicated BArchivable hierarchies |
| [BUnicodeChar](locale_kit/BUnicodeChar.md) | class | locale_kit | Management of all information about characters |
| [BUrl](support_kit/BUrl.md) | class | support_kit | Represents and manipulates an URL (Uniform Resource Locator) |
| [BUSBConfiguration](device_kit/BUSBConfiguration.md) | class | device_kit | Represents one of possibly multiple configurations a device might have |
| [BUSBDevice](device_kit/BUSBDevice.md) | class | device_kit | Represents an interface to a USB device |
| [BUSBEndpoint](device_kit/BUSBEndpoint.md) | class | device_kit | Represents a device endpoint that can be used to send or receive data |
| [BUSBInterface](device_kit/BUSBInterface.md) | class | device_kit | Represents an interface of a configuration in a USB device |
| [BUSBRoster](device_kit/BUSBRoster.md) | class | device_kit | Abstract class to implement to watch for devices that get attached or removed from the USB bus |
| [BView](interface_kit/BView.md) | class | interface_kit | View base class |
| [BVolume](storage_kit/BVolume.md) | class | storage_kit | Provides an interface for querying information about a volume |
| [BVolumeRoster](storage_kit/BVolumeRoster.md) | class | storage_kit | Provides an interface for iterating through available volumes and watching for mounting/unmounting |
| [BWindow](interface_kit/BWindow.md) | class | interface_kit | Window base class |
| [ConditionVariable](unknown_kit/ConditionVariable.md) | struct | unknown_kit | Condition variable for thread and interrupt synchronization |
| [ConditionVariableEntry](unknown_kit/ConditionVariableEntry.md) | struct | unknown_kit | Waiting on a condition variable |
| [Credits](special_topics/credits.md) | topic | special_topics | This version of the Haiku Book is brought to you by the Haiku Documentation Team |
| [direct_buffer_info](game_kit/direct__buffer__info.md) | struct | game_kit | Direct butter info struct |
| [Documenting the API](special_topics/apidoc.md) | topic | special_topics | This article explains how to document the API |
| [Drivers](special_topics/drivers.md) | topic | special_topics |  |
| [edge_info](interface_kit/edge__info.md) | struct | interface_kit | The distance that a character outline is inset from its escapement boundaries |
| [entry_ref](storage_kit/entry__ref.md) | struct | storage_kit | A filesystem entry represented as a name in a concrete directory |
| [escapement_delta](interface_kit/escapement__delta.md) | struct | interface_kit | A struct that allows you to specify extra horizontal space to surround each character with |
| [font_cache_info](interface_kit/font__cache__info.md) | struct | interface_kit | Font cache parameters |
| [font_height](interface_kit/font__height.md) | struct | interface_kit | The amount of vertical space surrounding a character |
| [GameProducer](game_kit/GameProducer.md) | class | game_kit | A MediaKit producer node which mixes sound from the GameKit and sends them to the audio mixer |
| [Global functions](support_kit/group__support__globals.md) | topic | support_kit |  |
| [image_info](unknown_kit/image__info.md) | struct | unknown_kit | Contains information about a running image |
| [Introduction to the Layout API](special_topics/layout_intro.md) | topic | special_topics | Haiku's Layout API is centered around the BLayoutItem and BLayout classes |
| [Json Handling](special_topics/json.md) | topic | special_topics | JSON is a simple textual description of a data structure |
| [Keyboard](special_topics/keyboard.md) | topic | special_topics | This page details how Haiku reads keys from the keyboard including modifier key and special characters, and how you can read and process these encoded characters in your application |
| [menu_info](interface_kit/menu__info.md) | struct | interface_kit | Information about a menu such as font size and family, background color, and flags |
| [node_ref](storage_kit/node__ref.md) | struct | storage_kit | Reference structure to a particular vnode on a device |
| [pattern](interface_kit/pattern.md) | struct | interface_kit | A pattern to use when drawing |
| [property_info](application_kit/property__info.md) | struct | application_kit | Property info struct containing lists of commands and specifiers |
| [rgb_color](interface_kit/rgb__color.md) | struct | interface_kit | Structure representing a 32 bit RGBA color |
| [text_run](interface_kit/text__run.md) | struct | interface_kit | text run struct |
| [text_run_array](interface_kit/text__run__array.md) | struct | interface_kit | text run array struct |
| [The old Midi Kit (libmidi.so)](special_topics/midi1.md) | topic | special_topics | The old Midi Kit, or midi1 for short, goes all the way back to DR8, when the BeOS only ran on BeBoxen |
| [tuned_font_info](interface_kit/tuned__font__info.md) | struct | interface_kit | Tuning information of fonts used to make it look better when displayed on-screen |
| [unicode_block](interface_kit/unicode__block.md) | class | interface_kit | Describes the blocks of Unicode characters supported by a font |
| [wireless_network](network_kit/wireless__network.md) | struct | network_kit | Describes a wireless network |
