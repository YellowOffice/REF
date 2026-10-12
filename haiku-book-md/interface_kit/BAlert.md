---
name: BAlert
type: class
kit: interface_kit
brief: "The BAlert class defines a modal alert dialog which displays a short message and provides a set of labeled buttons that allow the user to respond"
source: haiku-book
---

# BAlert Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

The [BAlert](classBAlert.md) class defines a modal alert dialog which displays a short message and provides a set of labeled buttons that allow the user to respond. 


The alert can be configured with a set of one to three buttons. These buttons are assigned indexes 0, 1, and 2 from right-to-left respectively and are automatically positioned by the system. The user can either click on one of the buttons or use a shortcut key to select a button.


The layout of the buttons can be configured by setting the [button_width](InterfaceDefs_8h.md#a670732462ef1d0b9433a503a70c31ce6) and [button_spacing](Alert_8h.md#a47f2f4d6ffc88ea539803d1d793f9777) properties in the [BAlert](classBAlert.md) constructor. The icon displayed in the alert can also be configured by setting the [alert_type](Alert_8h.md#a4dcc7e3a1abbcb466174c1c955b6c628) property. The right-most button (index 0) is the default button which can be activated by pushing the Enter key.


Below is an example of an unsaved changes alert dialog:





When the user responds by selecting one of the buttons the alert window is removed from the screen. The index of the selected button is returned to the calling application and the [BAlert](classBAlert.md) object is deleted.


The code used to create and display an alert dialog like the one shown above is shown below:



```cpp
BAlert* alert = new BAlert("Close and save dialog", "Save changes to...",
 "Cancel", "Don't save", "Save", B_WIDTH_AS_USUAL, B_OFFSET_SPACING,
 B_WARNING_ALERT);
alert->SetShortcut(0, B_ESCAPE);
int32 button_index = alert->Go();
```

The messaged displayed in the dialog window along with the button labels are set by the strings in the contructor. The Cancel button is offset to the left relative to the other buttons by setting the `B_OFFSET_SPACING` flag. The `B_WARNING_ALERT` flag displays the exclamation mark icon in the dialog.


Any alert with a Cancel button should map the Escape key as shown in the example above. You can setup additional shortcut keys for the buttons with the [SetShortcut()](classBAlert.md#a1e7ca339e7ee4e76f8b9aaf39fc4adec) method.


The [Go()](classBAlert.md#a9d68ec9e1418bc9d60f0836adb20a05f) method does the work of loading up and removing the alert window and returns the index of the button that the user selected.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BAlert](#abc52a59c5d81d53ccb014bc1e0de6ad3) () — Create an unconfigured BAlert dialog.
* [BAlert](#ac33ce28b410a3ad4b6d3dae4c027a800) (BMessage *data) — Unarchives an alert from a BMessage.
* [BAlert](#ad01b88d57fb5ed3bb7fef11a0f05b030) (const char *title, const char *text, const char *button1, const char *button2, const char *button3, button_width width, button_spacing spacing, alert_type type=B_INFO_ALERT) — Creates and initializes a BAlert dialog.
* [BAlert](#ad9fa1afb315edb648f4be09d6b7e6e63) (const char *title, const char *text, const char *button1, const char *button2=NULL, const char *button3=NULL, button_width width=B_WIDTH_AS_USUAL, alert_type type=B_INFO_ALERT) — Creates and initializes a BAlert dialog.
* `virtual` [~BAlert](#aa185011f234afddaff64f15bd3a7d25e) () — Destructor method.
* `void` [AddButton](#a307d3434c813c48155167253f51d9695) (const char *label, char key=0) — Adds a button to the alert.
* `BButton *` [ButtonAt](#a2d03c23dac6725ed189ef413a1816a6a) (int32 index) const — Returns a pointer to the BButton at the specified index.
* `int32` [CountButtons](#a7752044914df5253fcc640b418b871d7) () const — Counts the number of buttons in the alert.
* `virtual void` [DispatchMessage](#a29b871841d182889a147b58b16a7c111) (BMessage *message, BHandler *handler) — Sends out a message.
* `virtual void` [FrameResized](#a8409d243d503b948dc7da5d95e6ed66b) (float newWidth, float newHeight) — Resizes the alert dialog.
* `virtual status_t` [GetSupportedSuites](#a9e658b2f7dc50b2c5da3191d77a22594) (BMessage *data)
* `int32` [Go](#a9d68ec9e1418bc9d60f0836adb20a05f) () — Displays the alert window.
* `status_t` [Go](#a17c4c936675ec048ce0f61c853f9af89) (BInvoker *invoker) — Displays the alert window from a specified invoker.
* `virtual void` [MessageReceived](#a1300fdf51e73dd4f8a24b908d6fc2e1e) (BMessage *message) — Initiates an action from a received message.
* `virtual status_t` [Perform](#a3d2769c5bf9b9822f21770e38e561fd6) (perform_code d, void *arg) — Perform some action. (Internal Method)
* `virtual void` [Quit](#a691fe42dc7dc5acea09771e9c080dd0e) () — Quits the window closing it.
* `virtual bool` [QuitRequested](#ae91bb7bb3b99006f0b2616d47cf85985) () — Hook method that gets called with the window is closed.
* `virtual BHandler *` [ResolveSpecifier](#a22285daeb96ea0936faab97b077115e6) (BMessage *message, int32 index, BMessage *specifier, int32 form, const char *property)
* `void` [SetButtonSpacing](#ab60c14ca88c918c2342c9d36aa9140be) (button_spacing spacing) — Set the button spacing for the alert.
* `void` [SetButtonWidth](#a199223f27db65b5a3e34f9288f9957d3) (button_width width) — Set the button width for the buttons of the alert.
* `void` [SetIcon](#a11927f603083674e1cd2e51f91258320) (BBitmap *bitmap) — Set a custom icon for the alert.
* `void` [SetShortcut](#a1e7ca339e7ee4e76f8b9aaf39fc4adec) (int32 buttonIndex, char key) — Sets the shortcut character which is mapped to a button at the specified index.
* `void` [SetText](#af0c80f0842d0b78e4b44971b6c31ed68) (const char *text) — Set the text for the alert.
* `void` [SetType](#a70c5c724cddc47f3bf5999a2170f960d) (alert_type type) — Set the type of the alert.
* `char` [Shortcut](#a306e3bbb3ea57cd3871cb67bf78ac549) (int32 buttonIndex) const — Gets the shortcut character which is mapped to a button at the specified index.
* `BTextView *` [TextView](#a2f694fe620286bc15276d9ecb9a63561) () const — Returns the Alert's TextView.
* `alert_type` [Type](#a431c183c6c71fdfaac3a9d762bdb51c9) () const — Get the alert_type of this alert.
* [BWindow](#a967856a612c3e7ad4d5d1f4970f744e3) (BMessage *archive) — Archive constructor.
* [BWindow](#a92dfad4d2089ea9a4e8ca8154776e82d) (BRect frame, const char *title, window_look look, window_feel feel, uint32 flags, uint32 workspace=B_CURRENT_WORKSPACE) — Creates a new BWindow object with the specified look and feel.
* [BWindow](#afe03898c4cefc6b853f304c57afee533) (BRect frame, const char *title, window_type type, uint32 flags, uint32 workspace=B_CURRENT_WORKSPACE) — Creates a new BWindow object.
* `virtual` [~BWindow](#a896913784046fcfde7d1f8891e54af08) () — Destroys the BWindow object and all attached views.
* `void` [Activate](#a24ef781656049451c5c6ed06eeb98c06) (bool=true) — Activates or deactivates the window based on active.
* `void` [AddChild](#a798386ef9d12eb4f0dafff375e3b85d6) (BLayoutItem *child) — Add the child layout item to the view hierarchy.
* `void` [AddChild](#ac3b09ede3b0256df9cbcc7b2a3d6eda4) (BView *child, BView *before=NULL) — Adds child to the view hierarchy immediately before before.
* `status_t` [AddToSubset](#ac2abecfda66af23ee5e944530ce69c97) (BWindow *window) — Adds window to be in the subset of the BWindow.
* `virtual status_t` [Archive](#a69163d40d8f1eda77c9134ad4ab745a2) (BMessage *archive, bool deep=true) const — Archives the object into the data message.
* `void` [BeginViewTransaction](#a160e5f8757a65eaf3fec463fd6f2ba33) () — Stall updates to App Server allowing you to batch drawing commands to limit flickering.
* `BRect` [Bounds](#ab1084c04b99938ec93d2865962ec6bc2) () const — Returns the bounding rectangle of the window.
* `void` [CenterIn](#a4ea700aa901a1ac76b23605d82c79de8) (const BRect &rect) — Center the window in rect.
* `void` [CenterOnScreen](#a1fbaa783dffbd7bb5f0b135cde5e0237) () — Centers the window on the screen the window is currently on.
* `void` [CenterOnScreen](#aa9890ed5cb76c2c2a8fb82d7cd664586) (screen_id id) — Centers the window on the screen with the passed in id.
* `BView *` [ChildAt](#aeaeec9bcb12b7b03132e61dba501b19b) (int32 index) const — Returns a pointer to the child view found at index.
* `void` [Close](#a3be508837c0b14b176b916e45c9c1f31) () — Deprecated alias for BWindow::Quit().
* `void` [ConvertFromScreen](#aaa76e90a0578a4081eb4765467d594ea) (BPoint *point) const — Convert point from the screen's coordinate system to the window's coordinate system in place.
* `BPoint` [ConvertFromScreen](#ac0f4cc714ef1cc817100ae028f75d496) (BPoint point) const — Returns point converted from the screen's coordinate system to the window's coordinate system.
* `void` [ConvertFromScreen](#a7b3b4a579b4e14cd6acf1a95aee75687) (BRect *rect) const — Convert rect from the screen's coordinate system to the window's coordinate system in place.
* `BRect` [ConvertFromScreen](#ae748ea5865c1905c56c30e110c2f4947) (BRect rect) const — Returns rect converted from the screen's coordinate system to the window's coordinate system.
* `void` [ConvertToScreen](#a218bb4c66ca3f58fbc203a36996fd119) (BPoint *point) const — Convert point to the screen's coordinate system in place.
* `BPoint` [ConvertToScreen](#ac139848b8a9075d0ede0e28d87d95872) (BPoint point) const — Returns point converted to the screen's coordinate system.
* `void` [ConvertToScreen](#a83c3d8f1fb020740f7b4c3658e5222b5) (BRect *rect) const — Convert rect to the screen's coordinate system in place.
* `BRect` [ConvertToScreen](#a6997351ff94fca3d18459b41a790ce73) (BRect rect) const — Returns rect converted to the screen's coordinate system.
* `int32` [CountChildren](#a742200112899822a889c2e69bf86db5d) () const — Returns the number of child views that the window has.
* `BView *` [CurrentFocus](#a31d98b696b4e2a98ae83c841e342fe1b) () const — Returns a pointer to the current focus view of the window.
* `BRect` [DecoratorFrame](#a8a990fd437ac8f94f7be26f35145048d) () const — Returns the frame rectangle of the window decorator.
* `BButton *` [DefaultButton](#a6995f1dcc605c006e4118cc4b687e766) () const — Returns a pointer to the default button set on the window.
* `void` [DisableUpdates](#a83111af72c672b2b7029e712e9b702f3) () — Suppresses drawing within the window.
* `virtual void` [DispatchMessage](#a2089af8a214389c3f673c06420457b16) (BMessage *message, BHandler *handler) — Window's central message-processing method.
* `void` [EnableUpdates](#ab71c5c4ddd8f1cc677115157ec1c0c96) () — Re-enable drawing within the window.
* `void` [EndViewTransaction](#a54d387b099fb88e5aa565bdc40f338eb) () — Ends a view transaction allowing update to go to App Server again.
* `window_feel` [Feel](#ab3cf63c90d209ec6cb1aaeadb7f61fb1) () const — Returns the current window feel flag.
* `BView *` [FindView](#a4c252d9c733a703ca25dcc4d3eae6209) (BPoint) const — Returns a pointer to the attached view located at the specified point.
* `BView *` [FindView](#ac295d2dff72e4c5254cf597d4b31f9c6) (const char *viewName) const — Returns the attached view with the specified viewName.
* `uint32` [Flags](#ab99cdac9e2a0270c8afc07cfae7a02a8) () const — Returns the current window flags.
* `void` [Flush](#a2e74fd82a8095399d73a28920cc7c9b9) () const — Flushes the window's connection to App Server causing any pending messages to be processed then returns immediately.
* `BRect` [Frame](#ab6c744272c04751fa0b44e605b063a5d) () const — Returns the frame rectangle of the window.
* `virtual void` [FrameMoved](#a95f6fb2941250e7ed54fce6671f782c6) (BPoint newPosition) — Hook method that gets called when the window is moved.
* `virtual void` [FrameResized](#a280fab2b2900abc61dd4bcb7a2a4793f) (float newWidth, float newHeight) — Hook method that gets called when the window is resized.
* `status_t` [GetDecoratorSettings](#a58fba1b0ad6c2035cf1dac6304d21912) (BMessage *settings) const — Fill out the window's decorator settings into settings.
* `BLayout *` [GetLayout](#adb07dc64e991f7a42dfad000b2a1b0c7) () const — Get the layout of the window.
* `void` [GetSizeLimits](#aebce716c628bac67367875d1129db8c5) (float *minWidth, float *maxWidth, float *minHeight, float *maxHeight) — Fills out the size limits set on the window.
* `virtual status_t` [GetSupportedSuites](#a8c2f3013601609b54778af99fa6a25ca) (BMessage *data) — Reports the suites of messages and specifiers understood by the window.
* `status_t` [GetWindowAlignment](#a62a354bee61a0b5cd5ac499b5f728b7f) (window_alignment *mode=NULL, int32 *h=NULL, int32 *hOffset=NULL, int32 *width=NULL, int32 *widthOffset=NULL, int32 *v=NULL, int32 *vOffset=NULL, int32 *height=NULL, int32 *heightOffset=NULL) const — Fills out the pointers with the alignment of the content of the window on the screen.
* `virtual void` [Hide](#a53b85e4d43d34e5259b3b16ff6c52b32) () — Removes the window from the screen, removes it from Deskbar's window list, and passes active status to another window.
* `void` [InvalidateLayout](#a6abf2efb0ab304b75d72df3b6a2b9df3) (bool descendants=false) — Invalidate layout.
* `bool` [InViewTransaction](#ae5d1ae4e9598ed736c557031b92753ce) () const — Returns whether or not the window is currently in a view transaction.
* `bool` [IsActive](#abbaa2f20d86a5c4d12591fefef0c49fa) () const — Returns whether or not the window is active.
* `bool` [IsFloating](#a54158d02e55dbeb212ccf9af5b5a2f23) () const — Returns whether or not the window is floating.
* `bool` [IsFront](#a61ab745cf98f47cac71ed3b750d4d21f) () const — Returns whether or not the window is the frontmost on screen.
* `bool` [IsHidden](#ae92c2b3b1340af7740b7c4e3e14dcd30) () const — Returns whether or not the window is hidden.
* `bool` [IsMinimized](#a6c209b1d5ab1b82f43993074b1373678) () const — Returns whether or not the window is minimized.
* `bool` [IsModal](#aa10b6592ab7e291ce7152a72605c68fa) () const — Returns whether or not the window is modal.
* `bool` [IsOffscreenWindow](#a61d9b0d1e0de31231b835cc5293f8ed2) () const — Tests if window is used for drawing into a BBitmap. This is mostly used by the Interface Kit itself.
* `BMenuBar *` [KeyMenuBar](#a3f4cf14e9f6453e63b58acfd7098941c) () const — Returns a pointer to the key menu bar set to the window.
* `BView *` [LastMouseMovedView](#a59ef137725976cea5008e5efd683357e) () const — Returns a pointer to the attached view that most recently received a B_MOUSE_MOVED message.
* `void` [Layout](#ae3f008c018e413d75ddea1a60b0c9df7) (bool force) — Update the size limits and do the layout of the topmost view attached to the window.
* `window_look` [Look](#a056fe3233f883b1c4518619e59d825cd) () const — Returns the current window look flag.
* `virtual void` [MenusBeginning](#a981d5c2993f4514fbcd1bdaf297a2a2d) () — Hook method that gets called just before a menu owned by the window is shown.
* `virtual void` [MenusEnded](#a7bb882de172223e68ee6249596b80564) () — Hook method that gets called just before a menu owned by the window is hidden.
* `virtual void` [MessageReceived](#a1ce544ea7d9adcc6941759817a42affe) (BMessage *message) — Handle message received by the associated looper.
* `virtual void` [Minimize](#aabe75f91b52b94de6989b4cf49bd89b5) (bool minimize) — Minimizes or un-minimizes the window based on minimize.
* `void` [MoveBy](#a146584fa5815bd413f71671f33a9de89) (float dx, float dy) — Move the window by dx pixels horizontally and dy pixels vertically.
* `void` [MoveOnScreen](#ae426291c30652864d0a464518f9cda12) (uint32 flags=0) — Update window size and position to make it visible on screen.
* `void` [MoveTo](#ae81b509d6ee2eb29b9a703c75ef07ee5) (BPoint) — Move the window to point.
* `void` [MoveTo](#af419313a1b9b73a2c1cdb2365ff16189) (float x, float y) — Move the window to the specified x and y coordinates.
* `bool` [NeedsUpdate](#a9c03d9a6a454edec5eb38657e5c66490) () const — Returns whether or not any of the attached views need to be updated.
* `virtual status_t` [Perform](#afde7d74e5526f740dedb82a1d10faa7a) (perform_code code, void *data) — Internal method.
* `bigtime_t` [PulseRate](#a8ea37743fc8c09aab2a511a7c14fa9c4) () const — Returns the pulse rate of the window.
* `virtual void` [Quit](#a054c0206836014dcc20c59e50bceab44) () — Deletes the window and all child views, destroys the window thread, removes the window's connection to the Application Server, and deletes the object.
* `virtual bool` [QuitRequested](#a8fccbfd10fceb2c6103c6036ca9e961a) () — Hook method that gets called when the window receives a B_QUIT_REQUESTED message.
* `bool` [RemoveChild](#ac271fe9be15e5d6e0a5d59b7b2ed3e8d) (BView *child) — Removes child from the view hierarchy.
* `status_t` [RemoveFromSubset](#af9ef1e4afee9bfde7c7d9d8e2796c2de) (BWindow *window) — Remove window from the subset of the BWindow.
* `void` [ResizeBy](#a6aba4ddafc654f362799b6a96e6c76cd) (float dx, float dy) — Resize the window by dx pixels horizontally and dy pixels vertically.
* `void` [ResizeTo](#a31e2ea325258646128cfe8618cb79edc) (float width, float height) — Resize the window to the specified width and height.
* `void` [ResizeToPreferred](#a68db6173b92973252fc1876c5376bcd4) () — Resize the window to the preferred size of the window's layout.
* `virtual BHandler *` [ResolveSpecifier](#aaf328e28799cf868ec31df2847a4ed37) (BMessage *message, int32 index, BMessage *specifier, int32 what, const char *property)
* `virtual thread_id` [Run](#ae49c02ad870d55514c800631b37b97cf) () — Spawns the message loop thread and starts the window running.
* `virtual void` [ScreenChanged](#ab53cad2a56a967f0a52d5603d806561b) (BRect screenSize, color_space depth) — Hook method that is called when the screen that the window is located on changes size or location or the color space of the screen changes.
* `status_t` [SendBehind](#a88c3aa6ee3ea29d7868bafec749f891e) (const BWindow *window) — Moves the BWindow object behind window.
* `status_t` [SetDecoratorSettings](#aecfdd5136ed18c193357a8e3130ba578) (const BMessage &settings) — Set the window decorator settings according to settings.
* `void` [SetDefaultButton](#ab6c969b403bd24dc8b1e9d846a4ae414) (BButton *button) — Set the default button of the window to button.
* `status_t` [SetFeel](#a2317402cb859f5a438bc69e186ee2f04) (window_feel feel) — Changes the window feel set in the constructor to feel.
* `status_t` [SetFlags](#a8f0caf4693a1952ac9bbe9a52bfdd778) (uint32) — Changes the window flags set in the constructor to flags.
* `void` [SetKeyMenuBar](#aa1e9322c76ffdad1886253171f8a5972) (BMenuBar *bar) — Set the specified menu bar as the key menu bar for the window.
* `virtual void` [SetLayout](#ad0e630f2691a0f7919b809b7ea265095) (BLayout *layout) — Sets the layout of the window.
* `status_t` [SetLook](#ac9ca5f4b8a78f95403dbc35ad9728e0c) (window_look look) — Changes the window look set in the constructor to look.
* `void` [SetPulseRate](#ad69001922aad8daf7b65f82eb4b439f0) (bigtime_t rate) — Sets how often B_PULSE messages are posted to the window.
* `void` [SetSizeLimits](#a8668ecf18ad145391f66704c3339eb3d) (float minWidth, float maxWidth, float minHeight, float maxHeight) — Set size limits on the window.
* `void` [SetTitle](#a7cd4bf7dc0079e9a52b0ac1e7e2f897b) (const char *title) — Sets the window title to title.
* `status_t` [SetType](#a0f8f96c37d83e8df9e97c25a69c68295) (window_type type) — Changes the window type set in the constructor to type.
* `status_t` [SetWindowAlignment](#a91d42de7f54efe1399c3838d35162d20) (window_alignment mode, int32 h, int32 hOffset=0, int32 width=0, int32 widthOffset=0, int32 v=0, int32 vOffset=0, int32 height=0, int32 heightOffset=0) — Sets the alignment of the content of the window on the screen.
* `void` [SetWorkspaces](#a3549fdb63a64637fa8e2054e8c21272d) (uint32) — Sets the set of workspaces where the window can be displayed.
* `void` [SetZoomLimits](#ad3c2e560e41b377456faf9bd5dabcdc0) (float maxWidth, float maxHeight) — Sets the maximum size that the window will zoom to when Zoom() is called.
* `virtual void` [Show](#af7009117df50add72cf0e799ff7d0fa5) () — Shows the window on screen, places it frontmost on the screen, adds the window to Deskbar's window list, and makes it the active window.
* `BSize` [Size](#afc61a0c6129f233e56fa373107bd8790) () const — Returns the size of the window.
* `void` [Sync](#a332bea9ef16fedc16134bf587b52fa09) () const — Synchronizes the attached window's connection to App Server causing any pending messages to be processed and then waits for the App Server to respond.
* `const char *` [Title](#a73c7a05ef33d579de61b83b5daaf3c6b) () const — Returns the window title as set by the constructor or SetTitle().
* `window_type` [Type](#a103e6f93287afd65ed72ff760403fdf6) () const — Returns the current window type flag.
* `void` [UpdateIfNeeded](#a49b0c49eeef751b17bdc08d2e4d58cb9) () — Invokes Draw() immediately on each child view that needs updating.
* `void` [UpdateSizeLimits](#a99df6b9964c69b1c69c47fab6262abee) () — Updates the window's size limits from the minimum and maximum sizes of its top view.
* `virtual void` [WindowActivated](#a0a17d973a17bb8d3aef09d45d58a9aca) (bool focus) — Hook method that gets called when the window becomes activated or deactivated.
* `virtual void` [WorkspaceActivated](#ac3c293ef3d60df9b3125fb15d0c67cf7) (int32 workspace, bool state) — Hook method that gets called when the active workspace changes.
* `uint32` [Workspaces](#aba3b83e88043338b66c2b2f501fbbbee) () const — Returns the set of workspaces where the window can be displayed.
* `virtual void` [WorkspacesChanged](#af8dc496d4239a2c343a364a4ad9aabc4) (uint32 oldWorkspaces, uint32 newWorkspaces) — Hook method that gets called whenever the workspaces the window is in changes.
* `void` [Zoom](#a722772f2902e82bf65010ac2c13570bc) () — Resize the window to the minimum of the screen size, the maximum values set by SetSizeLimits(), and the maximum values set by SetZoomLimits().
* `virtual void` [Zoom](#ae7bea03df00c760d7f489acd3e312290) (BPoint origin, float width, float height) — Move window to origin, then resize to width and height.
* `void` [AddShortcut](#a5b05894e227eb22cba63ddaff289a95b) (uint32 key, uint32 modifiers, BMessage *message) — Creates a keyboard shortcut that sends a message to the window.
* `void` [AddShortcut](#a169c891ff22f6a76f10c15bd16cde3c5) (uint32 key, uint32 modifiers, BMessage *message, BHandler *target) — Creates a keyboard shortcut that sends a message to the specified target.
* `bool` [HasShortcut](#a08765e38e5cd5f37e19981d217b985d3) (uint32 key, uint32 modifiers) — Returns whether or not the specified shortcut is set on the window.
* `void` [RemoveShortcut](#a81d5e6ed3a8a7b7f5013055bf69593ba) (uint32 key, uint32 modifiers) — Removes the specified shortcut from the window.
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

### Static Public Member Functions

* `static BPoint` [AlertPosition](#a53a50224f3429fd731f68a6efe5f2f33) (float width, float height) — Resizes the Alert window to the width and height specified and return the Point of the top-left corner of the alert window.
* `static BArchivable *` [Instantiate](#af03c3109307589d67a1888a26f516f3f) (BMessage *archive) — Creates a new BWindow object from the data message.
* `static BArchivable *` [Instantiate](#aee61314ab77c54a64f8122440189b73a) (BMessage *data) — Static method to instantiate a looper from an archived message.
* `static BLooper *` [LooperForThread](#acf16bb9628e7dbbace3920ebeff6dc34) (thread_id thread) — Static method to retrieve a BLooper for a specified thread.
* `static BArchivable *` [Instantiate](#a0c23aeb48d578525f81ba6d47f968528) (BMessage *data) — Static method to instantiate a handler from an archived message.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

### Archiving

* `virtual status_t` [Archive](#aba312ca5f7e668bf4d96efc7f41625a3) (BMessage *data, bool deep=true) const — Archives the BAlert into archive.
* `static BArchivable *` [Instantiate](#ad74d6975c67e14f290e7fcbfb3857143) (BMessage *data) — Instantiates a BAlert from a BMessage.

### Additional Inherited Members

* `BMessage *` [MessageFromPort](#a1be73aad8e8fed41659b98633525e5b3) (bigtime_t=B_INFINITE_TIMEOUT) — Hook method to retrieve a message from the looper's port.

## Detailed Member Documentation

### `BAlert()`

```cpp
BAlert::BAlert()
```

Create an unconfigured [BAlert](classBAlert.md) dialog. 


This method creates an unconfigured [BAlert](classBAlert.md). You can configure it with methods like [SetText()](classBAlert.md#af0c80f0842d0b78e4b44971b6c31ed68), [SetType()](classBAlert.md#a70c5c724cddc47f3bf5999a2170f960d) and SetButtonSpacing.


It is advised to use one of the other constructors that help set up all the configuration in one go, instead of doing it piece by piece with this method.



**Since:** BeOS R3

---

### `BAlert()`

```cpp
BAlert::BAlert(const char * title, const char * text, const char * button1, const char * button2 = NULL, const char * button3 = NULL, button_width width = B_WIDTH_AS_USUAL, alert_type type = B_INFO_ALERT)
```

Creates and initializes a [BAlert](classBAlert.md) dialog. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `title` | The title of the window. Since the alert window doesn't have a title tab, the title is not actually displayed anywhere but is useful for debugging purposes. |
| `text` | The text that is displayed at the top of the window. |
| `button1` | Button 1 label |
| `button2` | Button 2 label |
| `button3` | Button 3 label |
| `width` | A constant that describes how the button should be sized. Options are  * `B_WIDTH_AS_USUAL`  * `B_WIDTH_FROM_WIDEST`  * `B_WIDTH_FROM_LABEL`    See button_width for details. |
| `type` | Constant that determines which alert icon is displayed. Options are  * `B_EMPTY_ALERT`  * `B_INFO_ALERT`  * `B_IDEA_ALERT`  * `B_WARNING_ALERT`  * `B_STOP_ALERT`    See alert_type for details. |





**Since:** BeOS R3

---

### `BAlert()`

```cpp
BAlert::BAlert(const char * title, const char * text, const char * button1, const char * button2, const char * button3, button_width width, button_spacing spacing, alert_type type = B_INFO_ALERT)
```

Creates and initializes a [BAlert](classBAlert.md) dialog. 


You can also set the *spacing* with this constructor.


Parameters

| Parameter | Description |
| :--- | :--- |
| `title` | The title of the window. Since the alert window doesn't have a title tab, the title is not actually displayed anywhere but is useful for debugging purposes. |
| `text` | The text that is displayed at the top of the window. |
| `button1` | Button 1 label |
| `button2` | Button 2 label |
| `button3` | Button 3 label |
| `width` | A constant that describes how the button should be sized. Options are  * `B_WIDTH_AS_USUAL`  * `B_WIDTH_FROM_WIDEST`  * `B_WIDTH_FROM_LABEL`    See button_width for details. |
| `spacing` | Determines how the buttons are spaced. Options are  * `B_EVEN_SPACING`  * `B_OFFSET_SPACING`    See button_spacing for details. |
| `type` | Constant that determines which alert icon is displayed. Options are  * `B_EMPTY_ALERT`  * `B_INFO_ALERT`  * `B_IDEA_ALERT`  * `B_WARNING_ALERT`  * `B_STOP_ALERT`    See alert_type for details. |





**Since:** BeOS R4

---

### `BAlert()`

```cpp
BAlert::BAlert(BMessage * data)
```

Unarchives an alert from a [BMessage](../application_kit/classBMessage.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The archive. |





**Since:** BeOS R3

---

### `~BAlert()`

```cpp
BAlert::~BAlert()
```

Destructor method. 


Standard Destructor method to delete a [BAlert](classBAlert.md).



**Since:** BeOS R3

---

### `AddButton()`

```cpp
void BAlert::AddButton(const char * label, char key = 0)
```

Adds a button to the alert. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `label` | The label of the button. |
| `key` | The key a user can press to quickly select this button. |





**Since:** BeOS R3

---

### `AlertPosition()`

```cpp
BPoint BAlert::AlertPosition(float width, float height)
```

Resizes the Alert window to the width and height specified and return the Point of the top-left corner of the alert window. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `width` | The desired *width* of the alert window. |
| `height` | The desired *height* of the alert window. |





**Returns:** The [BPoint](classBPoint.md) of the top-left corner of the Alert window.



**Since:** BeOS R3

---

### `Archive()`

```cpp
status_t BAlert::Archive(BMessage * data, bool deep = true)const
```

Archives the [BAlert](classBAlert.md) into *archive*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The target archive which the [BAlert](classBAlert.md) *data* will go into. |
| `deep` | Whether or not to recursively archive the [BAlert](classBAlert.md)'s children. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The archive operation was successful. |
| B_BAD_VALUE | The archive operation failed. |





**Since:** BeOS R3


Reimplemented from [BWindow](classBWindow.md#a69163d40d8f1eda77c9134ad4ab745a2).

---

### `ButtonAt()`

```cpp
BButton * BAlert::ButtonAt(int32 index)const
```

Returns a pointer to the [BButton](classBButton.md) at the specified *index*. 


The *index* of the buttons begins at `0` and counts from left to right. If a [BButton](classBButton.md) does not exist for the specified *index* then `NULL` is returned.


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The *index* of the desired button. |





**Returns:** A pointer to the [BButton](classBButton.md) at the specified *index*.



**Since:** BeOS R3

---

### `CountButtons()`

```cpp
int32 BAlert::CountButtons()const
```

Counts the number of buttons in the alert. 



**Returns:** The number of buttons in this alert window.



**See also:** [AddButton()](classBAlert.md#a307d3434c813c48155167253f51d9695) and [ButtonAt()](classBAlert.md#a2d03c23dac6725ed189ef413a1816a6a)



**Since:** BeOS R3

---

### `DispatchMessage()`

```cpp
void BAlert::DispatchMessage(BMessage * msg, BHandler * handler)
```

Sends out a message. 


This method called automatically as messages arrive in the queue, you should never call [DispatchMessage()](classBAlert.md#a29b871841d182889a147b58b16a7c111) yourself.



> [!WARNING]
> Don't override this method in your [BWindow](classBWindow.md) subclass. Override [MessageReceived()](classBAlert.md#a1300fdf51e73dd4f8a24b908d6fc2e1e) instead to alter the window's message dispatching mechanism.



**See also:** [BLooper::DispatchMessage()](../application_kit/classBLooper.md#add21ca8765c67b0dbf95b8f0361afa73)



**Since:** BeOS R3


Reimplemented from [BWindow](classBWindow.md#a2089af8a214389c3f673c06420457b16).

---

### `FrameResized()`

```cpp
void BAlert::FrameResized(float newWidth, float newHeight)
```

Resizes the alert dialog. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `newWidth` | The new *width* of the window. |
| `newHeight` | The new *height* of the window. |





**Since:** BeOS R3


Reimplemented from [BWindow](classBWindow.md#a280fab2b2900abc61dd4bcb7a2a4793f).

---

### `GetSupportedSuites()`

```cpp
status_t BAlert::GetSupportedSuites(BMessage * data)
```

Reports the suites of messages and specifiers understood by the window.  



**Since:** BeOS R3


Reimplemented from [BWindow](classBWindow.md#a8c2f3013601609b54778af99fa6a25ca).

---

### `Go()`

```cpp
int32 BAlert::Go()
```

Displays the alert window. 


This version of [Go()](classBAlert.md#a9d68ec9e1418bc9d60f0836adb20a05f) that does not include an invoker is synchronous. [Go()](classBAlert.md#a9d68ec9e1418bc9d60f0836adb20a05f) returns once the user has clicked a button and the panel has been removed from the screen. The [BAlert](classBAlert.md) object is deleted before the method returns.


If the [BAlert](classBAlert.md) is sent a `B_QUIT_REQUESTED` message while the alert window is still on screen then [Go()](classBAlert.md#a9d68ec9e1418bc9d60f0836adb20a05f) returns -1.



**Returns:** The index of the button clicked.



**Since:** BeOS R3

---

### `Go()`

```cpp
status_t BAlert::Go(BInvoker * invoker)
```

Displays the alert window from a specified *invoker*. 


This version of [Go()](classBAlert.md#a9d68ec9e1418bc9d60f0836adb20a05f) with an *invoker* is asynchronous. It returns immediately with `B_OK` and the button *index* is set to the field of the [BMessage](../application_kit/classBMessage.md) that is sent to the target of the *invoker*.


[Go()](classBAlert.md#a9d68ec9e1418bc9d60f0836adb20a05f) deletes the [BAlert](classBAlert.md) object after the message is sent.


If you call [Go()](classBAlert.md#a9d68ec9e1418bc9d60f0836adb20a05f) with a `NULL` invoker argument than the [BMessage](../application_kit/classBMessage.md) is not sent.


If the [BAlert](classBAlert.md) is sent a `B_QUIT_REQUESTED` method while the alert window is still on screen then the message is not sent.



**Returns:** A status code.



**Since:** BeOS R3

---

### `Instantiate()`

```cpp
BArchivable * BAlert::Instantiate(BMessage * data)
```

Instantiates a [BAlert](classBAlert.md) from a [BMessage](../application_kit/classBMessage.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The message to instantiate the [BAlert](classBAlert.md). |





**Returns:** a [BArchivable](../support_kit/classBArchivable.md) object of the [BAlert](classBAlert.md).



**Since:** BeOS R3

---

### `MessageReceived()`

```cpp
void BAlert::MessageReceived(BMessage * message)
```

Initiates an action from a received message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The *message* received by the looper. |





**See also:** [BHandler::MessageReceived()](../application_kit/classBHandler.md#aeecda5017e0081db617f23bbff71fb53)



**Since:** BeOS R3


Reimplemented from [BWindow](classBWindow.md#a1ce544ea7d9adcc6941759817a42affe).

---

### `Perform()`

```cpp
status_t BAlert::Perform(perform_code code, void * _data)
```

Perform some action. (Internal Method) 


Parameters

| Parameter | Description |
| :--- | :--- |
| `code` | The perform code. |
| `_data` | A pointer to store some data. |





**Returns:** A status code.



**See also:** [BLooper::Perform()](../application_kit/classBLooper.md#adfc642544ce22888d412e6a4be25fa72)



**Since:** Haiku R1


Reimplemented from [BWindow](classBWindow.md#afde7d74e5526f740dedb82a1d10faa7a).

---

### `Quit()`

```cpp
void BAlert::Quit()
```

Quits the window closing it. 


Use this method to destroy a window rather than using the delete operator.


This method works much like the [BLooper::Quit()](../application_kit/classBLooper.md#a10d5a4873f14fd247890a6dfc9b8b949), it doesn't return when called from the [BWindow](classBWindow.md)'s thread and it returns after all messages have been processed when called from another thread and the [BWindow](classBWindow.md) and its thread has been destroyed.



> [!WARNING]
> The window must first be locked before calling [Quit()](classBAlert.md#a691fe42dc7dc5acea09771e9c080dd0e).



**See also:** [BLooper::Quit()](../application_kit/classBLooper.md#a10d5a4873f14fd247890a6dfc9b8b949)



**Since:** BeOS R3


Reimplemented from [BWindow](classBWindow.md#a054c0206836014dcc20c59e50bceab44).

---

### `QuitRequested()`

```cpp
bool BAlert::QuitRequested()
```

Hook method that gets called with the window is closed. 



**See also:** [Quit()](classBAlert.md#a691fe42dc7dc5acea09771e9c080dd0e)



**Since:** BeOS R3


Reimplemented from [BWindow](classBWindow.md#a8fccbfd10fceb2c6103c6036ca9e961a).

---

### `ResolveSpecifier()`

```cpp
BHandler * BAlert::ResolveSpecifier(BMessage * message, int32 index, BMessage * specifier, int32 what, const char * property)
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





**Returns:** A pointer to the proper [BHandler](../application_kit/classBHandler.md) for the given scripting message.



**Since:** BeOS R3


Reimplemented from [BWindow](classBWindow.md#aaf328e28799cf868ec31df2847a4ed37).

---

### `SetButtonSpacing()`

```cpp
void BAlert::SetButtonSpacing(button_spacing spacing)
```

Set the button spacing for the alert. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `spacing` | Pass one of the button_spacing values to configure the spacing. |





**Since:** BeOS R3

---

### `SetButtonWidth()`

```cpp
void BAlert::SetButtonWidth(button_width width)
```

Set the button width for the buttons of the alert. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `width` | Pass one of the button_width values to configure the width. |





**Since:** BeOS R3

---

### `SetIcon()`

```cpp
void BAlert::SetIcon(BBitmap * bitmap)
```

Set a custom icon for the alert. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | A valid [BBitmap](classBBitmap.md). The [BAlert](classBAlert.md) assumes ownership of the bitmap. |





**Since:** Haiku R1

---

### `SetShortcut()`

```cpp
void BAlert::SetShortcut(int32 index, char key)
```

Sets the shortcut character which is mapped to a button at the specified *index*. 


A button can only have one shortcut except for the rightmost button which, in addition to the shortcut you set, is always mapped to `B_ENTER`.


If you create a "Cancel" button then you should set its shortcut to `B_ESCAPE`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The *index* of the button to set the shortcut to. |
| `key` | The shortcut character to set. |





**Since:** BeOS R3

---

### `SetText()`

```cpp
void BAlert::SetText(const char * text)
```

Set the text for the alert. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `text` | The text you want the alert to display. |





**Since:** BeOS R3

---

### `SetType()`

```cpp
void BAlert::SetType(alert_type type)
```

Set the type of the alert. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | Pass one of the alert_type enum values to set the type. |





**Since:** BeOS R3

---

### `Shortcut()`

```cpp
char BAlert::Shortcut(int32 index)const
```

Gets the shortcut character which is mapped to a button at the specified *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The *index* of the button to get the shortcut of. |





**Returns:** The shortcut character mapped to the button at the specified *index*.



**Since:** BeOS R3

---

### `TextView()`

```cpp
BTextView * BAlert::TextView()const
```

Returns the Alert's TextView. 



**Since:** BeOS R3

---

### `Type()`

```cpp
alert_type BAlert::Type()const
```

Get the alert_type of this alert. 



**Returns:** Returns one of the values from the alert_type enum.



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBAlert.html).
