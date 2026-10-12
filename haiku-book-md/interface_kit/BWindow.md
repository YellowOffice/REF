---
name: BWindow
type: class
kit: interface_kit
brief: "Window base class"
source: haiku-book
---

# BWindow Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Window base class. 


A [BWindow](classBWindow.md) is an on-screen window which contains views and is the target of keyboard and mouse events. A [BWindow](classBWindow.md) instance is nearly always subclassed.


[BWindow](classBWindow.md) draws by talking to App Server. If you want draw directly into the graphics card by-passing App Server, you need to use a [BDirectWindow](../game_kit/classBDirectWindow.md) or BWindowScreen.


Despite the fact that [BWindow](classBWindow.md) inherits from [BLooper](../application_kit/classBLooper.md), you should not invoke [Run()](classBWindow.md#ae49c02ad870d55514c800631b37b97cf) on a [BWindow](classBWindow.md), instead, call [Show()](classBWindow.md#af7009117df50add72cf0e799ff7d0fa5) to get the message loop started and show the window on screen. Once you've called [Show()](classBWindow.md#af7009117df50add72cf0e799ff7d0fa5) you may remove a window from the screen without interrupting the message loop by calling [Hide()](classBWindow.md#a53b85e4d43d34e5259b3b16ff6c52b32). Other message loop details such as locking and quitting are detailed in the [BLooper](../application_kit/classBLooper.md) class.


[BWindow](classBWindow.md) has the following built-in shortcuts:



| Shortcut | Action | Handler |
| :--- | :--- | :--- |
| Command+X | Cut | Focus view |
| Command+C | Copy | Focus view |
| Command+V | Paste | Focus view |
| Command+A | Select All | Focus view |
| Command+W | Close | Window (if closable) |
| Command+Q | Quit | Application (non-modal windows only) |
| Command+Control+M | Minimize | Window (if minimizable) |
| Command+Control+Z | Zoom | Window (if zoomable) |
| Command+Control+H | Hide | Window |
| Command+Control+F | Send to front | Window |
| Command+Control+B | Send behind | Window |
| Command+Control+← | Go to left workspace | Desktop window |
| Command+Control+→ | Go to right workspace | Desktop window |
| Command+Control+↑ | Go to above workspace | Desktop window |
| Command+Control+↓ | Go to below workspace | Desktop window |
| Command+Control+Shift+← | Send window and go to left workspace | Desktop window |
| Command+Control+Shift+→ | Send window and go to right workspace | Desktop window |
| Command+Control+Shift+↑ | Send window and go to above workspace | Desktop window |
| Command+Control+Shift+↓ | Send window and go to below workspace | Desktop window |



**Since:** BeOS R3

## Member List

### Public Member Functions

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

* `static BArchivable *` [Instantiate](#af03c3109307589d67a1888a26f516f3f) (BMessage *archive) — Creates a new BWindow object from the data message.
* `static BArchivable *` [Instantiate](#aee61314ab77c54a64f8122440189b73a) (BMessage *data) — Static method to instantiate a looper from an archived message.
* `static BLooper *` [LooperForThread](#acf16bb9628e7dbbace3920ebeff6dc34) (thread_id thread) — Static method to retrieve a BLooper for a specified thread.
* `static BArchivable *` [Instantiate](#a0c23aeb48d578525f81ba6d47f968528) (BMessage *data) — Static method to instantiate a handler from an archived message.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

### Additional Inherited Members

* `BMessage *` [MessageFromPort](#a1be73aad8e8fed41659b98633525e5b3) (bigtime_t=B_INFINITE_TIMEOUT) — Hook method to retrieve a message from the looper's port.

## Detailed Member Documentation

### `BWindow()`

```cpp
BWindow::BWindow(BRect frame, const char * title, window_type type, uint32 flags, uint32 workspace = B_CURRENT_WORKSPACE)
```

Creates a new [BWindow](classBWindow.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `frame` | The inner *frame* rectangle in the screen coordinate system. |
| `title` | The window *title* and thread title as "w>title". |
| `type` | window_type flag, one of the following: * `B_UNTYPED_WINDOW`  * `B_TITLED_WINDOW`  * `B_MODAL_WINDOW`  * `B_DOCUMENT_WINDOW`  * `B_BORDERED_WINDOW`  * `B_FLOATING_WINDOW` |
| `flags` | Mask that defines window attributes: * `B_NOT_MOVABLE` cannot be moved by the user  * `B_NOT_CLOSABLE` cannot be closed by the user, no close button displayed  * `B_NOT_ZOOMABLE` cannot be zoomed by the user, no zoom button displayed  * `B_NOT_MINIMIZABLE` cannot be minimized by the user  * `B_NOT_RESIZABLE` cannot be resized by the user  * `B_NOT_H_RESIZABLE` cannot be resized horizontally by the user  * `B_NOT_V_RESIZABLE` cannot be resized vertically by the user  * `B_AVOID_FRONT` cannot be brought to front by the user  * `B_AVOID_FOCUS` cannot receive keyboard focus  * `B_WILL_ACCEPT_FIRST_CLICK` The first click is processed by the window.  * `B_OUTLINE_RESIZE` draws only its outline as it's resized and doesn't draw its contents.  * `B_NO_WORKSPACE_ACTIVATION` Causes the current workspace to stay active when activated on another workspace.  * `B_NOT_ANCHORED_ON_ACTIVATE` Causes the window to move to the current workspace when activated if it already exists on another workspace.  * `B_QUIT_ON_WINDOW_CLOSE` Quit the application when the window closes.  * `B_SAME_POSITION_IN_ALL_WORKSPACES` Window maintains its position across workspaces.  * `B_AUTO_UPDATE_SIZE_LIMITS` Automatically adjust the size according to layout constraints.  * `B_CLOSE_ON_ESCAPE` Close when the user pushes the Escape key.  * `B_NO_SERVER_SIDE_WINDOW_MODIFIERS` ?? |
| `workspace` | Mask that indicates which of the 32 potential workspace(s) the window should be displayed in or `B_CURRENT_WORKSPACE` or `B_ALL_WORKSPACES` constants. |





**Since:** BeOS R3

---

### `BWindow()`

```cpp
BWindow::BWindow(BRect frame, const char * title, window_look look, window_feel feel, uint32 flags, uint32 workspace = B_CURRENT_WORKSPACE)
```

Creates a new [BWindow](classBWindow.md) object with the specified *look* and *feel*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `frame` | The inner *frame* rectangle in the screen coordinate system. |
| `title` | The window *title* and thread title as "w>title". |
| `look` | The window_look flags, one of the following: * `B_BORDERED_WINDOW_LOOK` No title bar, thin border, no resize control.  * `B_NO_BORDER_WINDOW_LOOK` A borderless rectangle with no provisions to move or close the window.  * `B_TITLED_WINDOW_LOOK` Like `B_DOCUMENT_WINDOW_LOOK`, but with a resize corner instead of a resize thumb.  * `B_DOCUMENT_WINDOW_LOOK` Large title bar, thick border, draggable resize corner thumb.  * `B_MODAL_WINDOW_LOOK` For modal dialogs: no title bar, thick border, resize corner depending on the `B_NOT_RESIZABLE` flag.  * `B_FLOATING_WINDOW_LOOK` For floating sub windows: small title bar, thin border, resize corner. |
| `feel` | The window_feel flags, one of the following: * `B_NORMAL_WINDOW_FEEL` Behaves like a normal, non-modal, non-floating window.  * `B_MODAL_SUBSET_WINDOW_FEEL` Blocks all windows in its subset when displayed. Visible only if a window in its subset is visible.  * `B_MODAL_APP_WINDOW_FEEL` Blocks all windows in its app when displayed. Visible only if a window in its app is visible.  * `B_MODAL_ALL_WINDOW_FEEL` Blocks all windows across the entire system when displayed. Always visible in all workspaces.  * `B_FLOATING_SUBSET_WINDOW_FEEL` Floats above all windows in its subset when displayed. Visible only if a window in its subset is the frontmost window.  * `B_FLOATING_APP_WINDOW_FEEL` Floats above all windows in its app when displayed. Visible only if a window in its app is the frontmost window.  * `B_FLOATING_ALL_WINDOW_FEEL` Floats above all windows across the entire system when displayed. Always visible in all workspaces. |
| `flags` | Mask that defines window attributes: * `B_NOT_MOVABLE` cannot be moved by the user  * `B_NOT_CLOSABLE` cannot be closed by the user, no close button displayed  * `B_NOT_ZOOMABLE` cannot be zoomed by the user, no zoom button displayed  * `B_NOT_MINIMIZABLE` cannot be minimized by the user  * `B_NOT_RESIZABLE` cannot be resized by the user  * `B_NOT_H_RESIZABLE` cannot be resized horizontally by the user  * `B_NOT_V_RESIZABLE` cannot be resized vertically by the user  * `B_AVOID_FRONT` cannot be brought to front by the user  * `B_AVOID_FOCUS` cannot receive keyboard focus  * `B_WILL_ACCEPT_FIRST_CLICK` The first click is processed by the window.  * `B_OUTLINE_RESIZE` draws only its outline as it's resized and doesn't draw its contents.  * `B_NO_WORKSPACE_ACTIVATION` Causes the current workspace to stay active when activated on another workspace.  * `B_NOT_ANCHORED_ON_ACTIVATE` Causes the window to move to the current workspace when activated if it already exists on another workspace.  * `B_QUIT_ON_WINDOW_CLOSE` Quit the application when the window closes.  * `B_SAME_POSITION_IN_ALL_WORKSPACES` Window maintains its position across workspaces.  * `B_AUTO_UPDATE_SIZE_LIMITS` Automatically adjust the size according to layout constraints.  * `B_CLOSE_ON_ESCAPE` Close when the user pushes the Escape key.  * `B_NO_SERVER_SIDE_WINDOW_MODIFIERS` ?? |
| `workspace` | Mask that indicates which of the 32 potential workspace(s) the window should be displayed in or `B_CURRENT_WORKSPACE` or `B_ALL_WORKSPACES` constants. |





**Since:** BeOS R3

---

### `~BWindow()`

```cpp
BWindow::~BWindow()
```

Destroys the [BWindow](classBWindow.md) object and all attached views. 



**Since:** BeOS R3

---

### `BWindow()`

```cpp
BWindow::BWindow(BMessage * data)
```

Archive constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A pointer to the [BMessage](../application_kit/classBMessage.md) object to build the object from. |





**Since:** BeOS R3

---

### `Activate()`

```cpp
void BWindow::Activate(bool active = true)
```

Activates or deactivates the window based on *active*. 


The title tab of the active window is drawn more brightly, the window is made frontmost, and it becomes the target of keyboard events. Calling [Show()](classBWindow.md#af7009117df50add72cf0e799ff7d0fa5) automatically activates the window calling the [WindowActivated()](classBWindow.md#a0a17d973a17bb8d3aef09d45d58a9aca) hook method.


Parameters

| Parameter | Description |
| :--- | :--- |
| `active` | `true` to activate the window, `false` to deactivate the window. |





**Since:** BeOS R3

---

### `AddChild()`

```cpp
void BWindow::AddChild(BLayoutItem * child)
```

Add the *child* layout item to the view hierarchy. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `child` | The child layout item to add. |





**Since:** Haiku R1

---

### `AddChild()`

```cpp
void BWindow::AddChild(BView * child, BView * before = NULL)
```

Adds *child* to the view hierarchy immediately before *before*. 


A view may only have one parent at a time so *child* must not have already been added to the view hierarchy. If *before* is `NULL` then *child* is added to the end of the view hierarchy.


The AttachedToWindow() method is invoked on *child* and all of its descendent views.


Parameters

| Parameter | Description |
| :--- | :--- |
| `child` | The child view to add. |
| `before` | The sibling view to add *child* before. |





**Since:** BeOS R3

---

### `AddShortcut()`

```cpp
void BWindow::AddShortcut(uint32 key, uint32 modifiers, BMessage * message)
```

Creates a keyboard shortcut that sends a *message* to the window. 



> [!WARNING]
> Don't use this method to a create menu shortcut, add a [BMenuItem](classBMenuItem.md) instead.


Parameters

| Parameter | Description |
| :--- | :--- |
| `key` | The character that activates the shortcut, case-insensitive. |
| `modifiers` | A bit mask of modifiers in addition to `B_COMMAND_KEY`, options include: * `B_SHIFT_KEY`  * `B_OPTION_KEY`  * `B_CONTROL_KEY`  * `B_MENU_KEY` To remove `B_COMMAND_KEY` specify `B_NO_COMMAND_KEY`. |
| `message` | The *message* to send when the shortcut is activated. The [BWindow](classBWindow.md) takes ownership of the *message*. |





**Since:** BeOS R3

---

### `AddShortcut()`

```cpp
void BWindow::AddShortcut(uint32 key, uint32 modifiers, BMessage * message, BHandler * target)
```

Creates a keyboard shortcut that sends a *message* to the specified *target*. 



> [!WARNING]
> Don't use this method to a create menu shortcut, add a [BMenuItem](classBMenuItem.md) instead.


Parameters

| Parameter | Description |
| :--- | :--- |
| `key` | The character that activates the shortcut, case-insensitive. |
| `modifiers` | A bit mask of modifiers in addition to `B_COMMAND_KEY`, options include one or more of the following: * `B_SHIFT_KEY`  * `B_OPTION_KEY`  * `B_CONTROL_KEY`  * `B_MENU_KEY` To remove `B_COMMAND_KEY` specify `B_NO_COMMAND_KEY`. |
| `message` | The *message* to send when the shortcut is activated. The [BWindow](classBWindow.md) takes ownership of the *message*. |
| `target` | The handler to send the message to. |





**Since:** BeOS R3

---

### `AddToSubset()`

```cpp
status_t BWindow::AddToSubset(BWindow * window)
```

Adds *window* to be in the subset of the [BWindow](classBWindow.md). 



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | *window* was added as a subset of the [BWindow](classBWindow.md). |
| B_BAD_VALUE | `window` is not `B_NORMAL_WINDOW_FEEL` or the [BWindow](classBWindow.md) object's feel is not set to `B_MODAL_SUBSET_WINDOW_FEEL` or `B_FLOATING_SUBSET_WINDOW_FEEL`. |
| B_ERROR | Could not lock the [BWindow](classBWindow.md) object. |





**Since:** BeOS R3

---

### `Archive()`

```cpp
status_t BWindow::Archive(BMessage * data, bool deep = true)const
```

Archives the object into the *data* message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A pointer to the [BMessage](../application_kit/classBMessage.md) object to archive the object into. |
| `deep` | Whether or not to archive child views as well. |





**Returns:** A status code, `B_OK` if the object was archived or an error code otherwise.



**Since:** BeOS R3


Reimplemented from [BLooper](../application_kit/classBLooper.md#a791ef8664f674b6683d551762888f1c2).


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#a39e69ba4bba5221b3099cf34129862c8), and [BAlert](classBAlert.md#aba312ca5f7e668bf4d96efc7f41625a3).

---

### `BeginViewTransaction()`

```cpp
void BWindow::BeginViewTransaction()
```

Stall updates to App Server allowing you to batch drawing commands to limit flickering. 


Unlike [DisableUpdates()](classBWindow.md#a83111af72c672b2b7029e712e9b702f3) the messages are sent but are not processed.



**Since:** Haiku R1

---

### `Bounds()`

```cpp
BRect BWindow::Bounds()const
```

Returns the bounding rectangle of the window. 



**Returns:** The bounding rectangle of the window as a [BRect](classBRect.md) in the window's coordinate system.



**See also:** [Frame()](classBWindow.md#ab6c744272c04751fa0b44e605b063a5d)



**Since:** BeOS R3

---

### `CenterIn()`

```cpp
void BWindow::CenterIn(const BRect & rect)
```

Center the window in *rect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The rectangle to center the window in. |





**Since:** Haiku R1

---

### `CenterOnScreen()`

```cpp
void BWindow::CenterOnScreen()
```

Centers the window on the screen the window is currently on. 



**Since:** Haiku R1

---

### `CenterOnScreen()`

```cpp
void BWindow::CenterOnScreen(screen_id id)
```

Centers the window on the screen with the passed in *id*. 



**Since:** Haiku R1

---

### `ChildAt()`

```cpp
BView * BWindow::ChildAt(int32 index)const
```

Returns a pointer to the child view found at *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index of the child view to return a pointer of. |





**Returns:** A pointer to the child view at *index* or `NULL` if not found.



**Since:** BeOS R3

---

### `Close()`

```cpp
void BWindow::Close()
```

Deprecated alias for [BWindow::Quit()](classBWindow.md#a054c0206836014dcc20c59e50bceab44). 


The advised way to close a window is to use [BWindow::Quit()](classBWindow.md#a054c0206836014dcc20c59e50bceab44).



**Since:** BeOS R3


References [Quit()](classBWindow.md#a054c0206836014dcc20c59e50bceab44).

---

### `ConvertFromScreen()`

```cpp
void BWindow::ConvertFromScreen(BPoint * point)const
```

Convert *point* from the screen's coordinate system to the window's coordinate system in place. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | A pointer to a [BPoint](classBPoint.md) object to convert. |





**Since:** BeOS R3

---

### `ConvertFromScreen()`

```cpp
BPoint BWindow::ConvertFromScreen(BPoint point)const
```

Returns *point* converted from the screen's coordinate system to the window's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | A [BPoint](classBPoint.md) object to convert. |





**Returns:** A new [BPoint](classBPoint.md) object in the window's coordinate system.



**Since:** BeOS R3

---

### `ConvertFromScreen()`

```cpp
void BWindow::ConvertFromScreen(BRect * rect)const
```

Convert *rect* from the screen's coordinate system to the window's coordinate system in place. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | A pointer to a [BRect](classBRect.md) object to convert. |





**Since:** BeOS R3

---

### `ConvertFromScreen()`

```cpp
BRect BWindow::ConvertFromScreen(BRect rect)const
```

Returns *rect* converted from the screen's coordinate system to the window's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | A [BRect](classBRect.md) object to convert. |





**Returns:** A new [BRect](classBRect.md) object in the window's coordinate system.



**Since:** BeOS R3

---

### `ConvertToScreen()`

```cpp
void BWindow::ConvertToScreen(BPoint * point)const
```

Convert *point* to the screen's coordinate system in place. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | A pointer to a [BPoint](classBPoint.md) object to convert. |





**Since:** BeOS R3

---

### `ConvertToScreen()`

```cpp
BPoint BWindow::ConvertToScreen(BPoint point)const
```

Returns *point* converted to the screen's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | A [BPoint](classBPoint.md) object to convert. |





**Returns:** A new [BPoint](classBPoint.md) object in the screen's coordinate system.



**Since:** BeOS R3

---

### `ConvertToScreen()`

```cpp
void BWindow::ConvertToScreen(BRect * rect)const
```

Convert *rect* to the screen's coordinate system in place. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | A pointer to a [BRect](classBRect.md) object to convert. |





**Since:** BeOS R3

---

### `ConvertToScreen()`

```cpp
BRect BWindow::ConvertToScreen(BRect rect)const
```

Returns *rect* converted to the screen's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | A [BRect](classBRect.md) object to convert. |





**Returns:** A new [BRect](classBRect.md) object in the screen's coordinate system.



**Since:** BeOS R3

---

### `CountChildren()`

```cpp
int32 BWindow::CountChildren()const
```

Returns the number of child views that the window has. 



**Returns:** The number of child views as an int32.



**Since:** BeOS R3

---

### `CurrentFocus()`

```cpp
BView * BWindow::CurrentFocus()const
```

Returns a pointer to the current focus view of the window. 



**Returns:** A pointer to the current focus view of the window or `NULL` if not found.



**Since:** BeOS R3

---

### `DecoratorFrame()`

```cpp
BRect BWindow::DecoratorFrame()const
```

Returns the frame rectangle of the window decorator. 



**Returns:** The bounding rectangle of the window decorator as a [BRect](classBRect.md) in the screen coordinate system.



**Since:** Haiku R1

---

### `DefaultButton()`

```cpp
BButton * BWindow::DefaultButton()const
```

Returns a pointer to the default button set on the window. 



**Returns:** A pointer to the window's default button or `NULL` if it doesn't have one.



**Since:** BeOS R3

---

### `DisableUpdates()`

```cpp
void BWindow::DisableUpdates()
```

Suppresses drawing within the window. 


If you want the results of several drawing operations to appear in the window all at once you disable updates, draw, and then re-enable updates.



**Since:** BeOS R3

---

### `DispatchMessage()`

```cpp
void BWindow::DispatchMessage(BMessage * message, BHandler * target)
```

Window's central message-processing method. 


This method called automatically as messages arrive in the queue, you should never call [DispatchMessage()](classBWindow.md#a2089af8a214389c3f673c06420457b16) yourself.



> [!WARNING]
> Don't override this method in your [BWindow](classBWindow.md) subclass. Override [MessageReceived()](classBWindow.md#a1ce544ea7d9adcc6941759817a42affe) instead to alter the window's message dispatching mechanism.



**See also:** [BLooper::DispatchMessage()](../application_kit/classBLooper.md#add21ca8765c67b0dbf95b8f0361afa73)



**Since:** BeOS R3


Reimplemented from [BLooper](../application_kit/classBLooper.md#add21ca8765c67b0dbf95b8f0361afa73).


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#a62952e05d331dde0b091998db878a9f6), and [BAlert](classBAlert.md#a29b871841d182889a147b58b16a7c111).

---

### `EnableUpdates()`

```cpp
void BWindow::EnableUpdates()
```

Re-enable drawing within the window. 


If you want the results of several drawing operations to appear in the window all at once you disable updates, draw, and then re-enable updates.



**Since:** BeOS R3

---

### `EndViewTransaction()`

```cpp
void BWindow::EndViewTransaction()
```

Ends a view transaction allowing update to go to App Server again. 



**Since:** Haiku R1

---

### `Feel()`

```cpp
window_feel BWindow::Feel()const
```

Returns the current window feel flag. 



**Returns:** The currently set window feel flag.



**Since:** BeOS R3

---

### `FindView()`

```cpp
BView * BWindow::FindView(BPoint point)const
```

Returns a pointer to the attached view located at the specified *point*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The *point* to get the view at in the window's coordinate system. |





**Returns:** A pointer to the [BView](classBView.md) object or `NULL` if no view is found.



**Since:** BeOS R3

---

### `FindView()`

```cpp
BView * BWindow::FindView(const char * viewName)const
```

Returns the attached view with the specified *viewName*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `viewName` | The name of the attached view to look for. |





**Returns:** A pointer to the [BView](classBView.md) object or `NULL` if no view is found.



**Since:** BeOS R3

---

### `Flags()`

```cpp
uint32 BWindow::Flags()const
```

Returns the current window flags. 



**Returns:** The currently set window flags.



**Since:** BeOS R3

---

### `Flush()`

```cpp
void BWindow::Flush()const
```

Flushes the window's connection to App Server causing any pending messages to be processed then returns immediately. 



**Since:** BeOS R3

---

### `Frame()`

```cpp
BRect BWindow::Frame()const
```

Returns the frame rectangle of the window. 



**Returns:** The bounding rectangle of the window as a [BRect](classBRect.md) in the screen coordinate system.



**See also:** [Bounds()](classBWindow.md#ab1084c04b99938ec93d2865962ec6bc2)



**Since:** BeOS R3

---

### `FrameMoved()`

```cpp
void BWindow::FrameMoved(BPoint newPosition)
```

Hook method that gets called when the window is moved. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `newPosition` | The point of the top left corner of the frame rectangle that the window has been moved to. |





**Since:** BeOS R3


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#a90091f68f028a04d9454201603c27638).

---

### `FrameResized()`

```cpp
void BWindow::FrameResized(float newWidth, float newHeight)
```

Hook method that gets called when the window is resized. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `newWidth` | The new *width* of the window. |
| `newHeight` | The new *height* of the window. |





**Since:** BeOS R3


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#a8d5888adb8fa39a0affbbdaae6bcfd24), and [BAlert](classBAlert.md#a8409d243d503b948dc7da5d95e6ed66b).

---

### `GetDecoratorSettings()`

```cpp
status_t BWindow::GetDecoratorSettings(BMessage * settings)const
```

Fill out the window's decorator settings into *settings*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `settings` | A pointer to a [BMessage](../application_kit/classBMessage.md) object to fill out. |





**Returns:** `B_OK` if the decorator settings were filled out successfully or an error code otherwise.



**Since:** Haiku R1

---

### `GetLayout()`

```cpp
BLayout * BWindow::GetLayout()const
```

Get the layout of the window. 



**Returns:** The layout of the window.



**Since:** Haiku R1

---

### `GetSizeLimits()`

```cpp
void BWindow::GetSizeLimits(float * _minWidth, float * _maxWidth, float * _minHeight, float * _maxHeight)
```

Fills out the size limits set on the window. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `_minWidth` | The minimum width of the window. |
| `_maxWidth` | The maximum width of the window. |
| `_minHeight` | The minimum height of the window. |
| `_maxHeight` | The maximum height of the window. |





**Since:** BeOS R3

---

### `GetSupportedSuites()`

```cpp
status_t BWindow::GetSupportedSuites(BMessage * data)
```

Reports the suites of messages and specifiers understood by the window. 



**Since:** BeOS R3


Reimplemented from [BLooper](../application_kit/classBLooper.md#a915a50de7d5b6263f0fd1a349a9a6d92).


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#a55e920fcba8972f5173bd3714f416c13), and [BAlert](classBAlert.md#a9e658b2f7dc50b2c5da3191d77a22594).

---

### `GetWindowAlignment()`

```cpp
status_t BWindow::GetWindowAlignment(window_alignment * mode = NULL, int32 * h = NULL, int32 * hOffset = NULL, int32 * width = NULL, int32 * widthOffset = NULL, int32 * v = NULL, int32 * vOffset = NULL, int32 * height = NULL, int32 * heightOffset = NULL)const
```

Fills out the pointers with the alignment of the content of the window on the screen. 



**Since:** BeOS R3

---

### `HasShortcut()`

```cpp
bool BWindow::HasShortcut(uint32 key, uint32 modifiers)
```

Returns whether or not the specified shortcut is set on the window. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `key` | The character to check, case-insensitive. |
| `modifiers` | A bit mask of modifiers in addition to `B_COMMAND_KEY`, options include one or more of the following: * `B_SHIFT_KEY`  * `B_OPTION_KEY`  * `B_CONTROL_KEY`  * `B_MENU_KEY` To remove `B_COMMAND_KEY` specify `B_NO_COMMAND_KEY`. |





**Returns:** `true` if the window has the specified shortcut, `false` otherwise.



**Since:** Haiku R1

---

### `Hide()`

```cpp
void BWindow::Hide()
```

Removes the window from the screen, removes it from Deskbar's window list, and passes active status to another window. 


Calls to [Hide()](classBWindow.md#a53b85e4d43d34e5259b3b16ff6c52b32) and [Show()](classBWindow.md#af7009117df50add72cf0e799ff7d0fa5) are cumulative.



**Since:** BeOS R3


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#af9258f81376f03c05192a1c0627722bd).

---

### `Instantiate()`

```cpp
BArchivable * BWindow::Instantiate(BMessage * data)
```

Creates a new [BWindow](classBWindow.md) object from the *data* message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A pointer to the [BMessage](../application_kit/classBMessage.md) object to build the object from. |





**Returns:** A newly created [BWindow](classBWindow.md) object or `NULL` if the message doesn't contain an archived [BWindow](classBWindow.md).



**Since:** BeOS R3

---

### `InvalidateLayout()`

```cpp
void BWindow::InvalidateLayout(bool descendants = false)
```

Invalidate layout. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `descendants` | Also invalidate its children windows. |





**Since:** Haiku R1

---

### `InViewTransaction()`

```cpp
bool BWindow::InViewTransaction()const
```

Returns whether or not the window is currently in a view transaction. 



**Returns:** `true` if the window is currently in a view transaction, `false` otherwise.



**Since:** Haiku R1

---

### `IsActive()`

```cpp
bool BWindow::IsActive()const
```

Returns whether or not the window is active. 



**Returns:** `true` if the window is active, `false` otherwise.



**Since:** BeOS R3

---

### `IsFloating()`

```cpp
bool BWindow::IsFloating()const
```

Returns whether or not the window is floating. 



**Returns:** `true` if the window is floating, `false` otherwise.



**Since:** BeOS R3

---

### `IsFront()`

```cpp
bool BWindow::IsFront()const
```

Returns whether or not the window is the frontmost on screen. 



**Returns:** `true` if window is the frontmost on screen, `false` otherwise.



**Since:** BeOS R3

---

### `IsHidden()`

```cpp
bool BWindow::IsHidden()const
```

Returns whether or not the window is hidden. 


Windows are hidden by default, you must call [Show()](classBWindow.md#af7009117df50add72cf0e799ff7d0fa5) to show the window starting the message loop going.



**Since:** BeOS R3

---

### `IsMinimized()`

```cpp
bool BWindow::IsMinimized()const
```

Returns whether or not the window is minimized. 



**Returns:** `true` if the window is minimized, `false` otherwise.



**Since:** BeOS R5

---

### `IsModal()`

```cpp
bool BWindow::IsModal()const
```

Returns whether or not the window is modal. 



**Returns:** `true` if the window is modal, `false` otherwise.



**Since:** BeOS R3

---

### `IsOffscreenWindow()`

```cpp
bool BWindow::IsOffscreenWindow()const
```

Tests if window is used for drawing into a [BBitmap](classBBitmap.md). This is mostly used by the Interface Kit itself. 



**Returns:** True if the window is used for drawing into a [BBitmap](classBBitmap.md).



**Since:** Haiku R1

---

### `KeyMenuBar()`

```cpp
BMenuBar * BWindow::KeyMenuBar()const
```

Returns a pointer to the key menu bar set to the window. 


If the window contains only one menu bar it is automatically considered to be the key menu bar for the window. If more than one menu bar is attached to the window then the last one added to the window's view hierarchy is considered to be the key menu bar for the window.


To explicitly set a menu bar as the key menu bar call [SetKeyMenuBar()](classBWindow.md#aa1e9322c76ffdad1886253171f8a5972).



**Returns:** A pointer to the key menu bar or `NULL` is not is set.



**Since:** BeOS R3

---

### `LastMouseMovedView()`

```cpp
BView * BWindow::LastMouseMovedView()const
```

Returns a pointer to the attached view that most recently received a `B_MOUSE_MOVED` message. 



**Returns:** A pointer the [BView](classBView.md) object that most recently received a `B_MOUSE_MOVED` message or `NULL` if not found.



**Since:** BeOS R3

---

### `Layout()`

```cpp
void BWindow::Layout(bool force)
```

Update the size limits and do the layout of the topmost view attached to the window. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `force` | If `true`, layout even if valid. |





**Since:** Haiku R1

---

### `Look()`

```cpp
window_look BWindow::Look()const
```

Returns the current window look flag. 



**Returns:** The currently set window look flag.



**Since:** BeOS R3

---

### `MenusBeginning()`

```cpp
void BWindow::MenusBeginning()
```

Hook method that gets called just before a menu owned by the window is shown. 


It will also be invoked while dispatching shortcuts.



> [!NOTE]
> This method is not invoked by a message.



**Since:** BeOS R3


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#af05688e3cffca075a7c88c4d8707c9b9).

---

### `MenusEnded()`

```cpp
void BWindow::MenusEnded()
```

Hook method that gets called just before a menu owned by the window is hidden. 


It will also be invoked after dispatching shortcuts.



> [!NOTE]
> This method is not invoked by a message.



**Since:** BeOS R3


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#a4aa81f5f362906c8cf7b41230dce3879).

---

### `MessageReceived()`

```cpp
void BWindow::MessageReceived(BMessage * message)
```

Handle *message* received by the associated looper. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The *message* received by the looper. |





**See also:** [BHandler::MessageReceived()](../application_kit/classBHandler.md#aeecda5017e0081db617f23bbff71fb53)



**Since:** BeOS R3


Reimplemented from [BLooper](../application_kit/classBLooper.md#a89303d11c987dae76cdfc38ad5d3c4c2).


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#a1eb5e6dfeee341e9baf3d688ff66194a), and [BAlert](classBAlert.md#a1300fdf51e73dd4f8a24b908d6fc2e1e).

---

### `Minimize()`

```cpp
void BWindow::Minimize(bool minimize)
```

Minimizes or un-minimizes the window based on *minimize*. 


Unlike [Hide()](classBWindow.md#a53b85e4d43d34e5259b3b16ff6c52b32) an [Show()](classBWindow.md#af7009117df50add72cf0e799ff7d0fa5), [Minimize()](classBWindow.md#aabe75f91b52b94de6989b4cf49bd89b5) dims and un-dims the entry for the window in Deskbar's window list rather than removing it. Also [Minimize()](classBWindow.md#aabe75f91b52b94de6989b4cf49bd89b5) calls are not cumulative like [Hide()](classBWindow.md#a53b85e4d43d34e5259b3b16ff6c52b32) and [Show()](classBWindow.md#af7009117df50add72cf0e799ff7d0fa5); one `false` call will undo multiple `true` calls.


[Minimize()](classBWindow.md#aabe75f91b52b94de6989b4cf49bd89b5) also acts as a hook method that is invoked when the user double- clicks on the title tab of the window or selects the window from the DeskBar window list. The *minimize* parameter is `true` if the window is about to be hidden and `false` if it is about to be shown.


If you override [Minimize()](classBWindow.md#aabe75f91b52b94de6989b4cf49bd89b5) and you want to inherit [BWindow](classBWindow.md)'s behavior, you must call [BWindow::Minimize()](classBWindow.md#aabe75f91b52b94de6989b4cf49bd89b5).



**Since:** BeOS R3


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#a8107850d1d7710dc11a1acf1bbf16972).

---

### `MoveBy()`

```cpp
void BWindow::MoveBy(float dx, float dy)
```

Move the window by *dx* pixels horizontally and *dy* pixels vertically. 


*dx* and *dy* must be integral units.


Parameters

| Parameter | Description |
| :--- | :--- |
| `dx` | The number of pixels to move the window vertically. |
| `dy` | The number of pixels to move the window horizontally. |





**Since:** BeOS R3

---

### `MoveOnScreen()`

```cpp
void BWindow::MoveOnScreen(uint32 flags = 0)
```

Update window size and position to make it visible on screen. 


This convenience method helps you to automatically move and resize a window to make it visible on the screen, in case the window is partially off screen because of its size or its position. This method will do nothing if the window fits on the screen.


The default behavior is as follows:


* If the window size is larger than the screen, the window is resized so that it fits on the screen.

* If the window is still partially off-screen, it will then be centered horizontally and vertically so that it is fully visible.



Note that this does not affect window size and positions for windows that are currently visible on the screen. Also note that this method does not affect whether the window is covered by other windows that are on top. You can use [BWindow::Activate()](classBWindow.md#a24ef781656049451c5c6ed06eeb98c06) to bring a window to the top.


The behavior of this method can be altered by passing either or both of the following modifiers in the *flags* parameter:


* [B_DO_NOT_RESIZE_TO_FIT](Window_8h.md#afccd240f973cf154952fb917c9209719aa378a9df433b2886f8df647db7b6c2c3) Do not resize the window. If the window is too large to be on the screen, then it will at least be moved so that the left-top of the window is visible, and only the right and/or bottom of the window will be off screen.

* [B_MOVE_IF_PARTIALLY_OFFSCREEN](Window_8h.md#afccd240f973cf154952fb917c9209719aa2f8362b59b670aaa704eaa3f9ce976d) Use this parameter if instead of centering the window in the middle of the screen, you only want to do the minimum movement so that at least the top left part of the window is visible on screen.



Parameters

| Parameter | Description |
| :--- | :--- |
| `flags` | Can be `0` for the default behavior, or a any combination of `B_DO_NOT_RESIZE_TO_FIT` and `B_MOVE_IF_PARTIALLY_OFFSCREEN`. |





**Since:** Haiku R1

---

### `MoveTo()`

```cpp
void BWindow::MoveTo(BPoint point)
```

Move the window to *point*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | the location to move the window in the screen's coordinate system. |





**Since:** BeOS R3

---

### `MoveTo()`

```cpp
void BWindow::MoveTo(float x, float y)
```

Move the window to the specified *x* and *y* coordinates. 


*x* and *y* must be integral units.


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | The horizontal coordinate to move the window to in the screen's coordinate system. |
| `y` | The vertical coordinate to move the window to in the screen's coordinate system. |





**Since:** BeOS R3

---

### `NeedsUpdate()`

```cpp
bool BWindow::NeedsUpdate()const
```

Returns whether or not any of the attached views need to be updated. 



**Returns:** `true` if an attached view needs to be updated, `false` otherwise.



**Since:** BeOS R3

---

### `Perform()`

```cpp
virtual status_t BWindow::Perform(perform_code d, void * arg)
```

Internal method. 



**Since:** Haiku R1


Reimplemented from [BLooper](../application_kit/classBLooper.md#adfc642544ce22888d412e6a4be25fa72).


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#a113afd3534fca8b81bcc86f8e55738be), and [BAlert](classBAlert.md#a3d2769c5bf9b9822f21770e38e561fd6).

---

### `PulseRate()`

```cpp
bigtime_t BWindow::PulseRate()const
```

Returns the pulse rate of the window. 


`B_PULSE` messages are sent by default every 500,000 microseconds provided that no other messages are pending.



**Returns:** The pulse rate of the window as a bigtime_t.



**Since:** BeOS R3

---

### `Quit()`

```cpp
void BWindow::Quit()
```

Deletes the window and all child views, destroys the window thread, removes the window's connection to the Application Server, and deletes the object. 


Use this method to destroy a window rather than using the delete operator.


This method works much like the [BLooper::Quit()](../application_kit/classBLooper.md#a10d5a4873f14fd247890a6dfc9b8b949), it doesn't return when called from the [BWindow](classBWindow.md)'s thread and it returns after all messages have been processed when called from another thread and the [BWindow](classBWindow.md) and its thread has been destroyed.



> [!WARNING]
> The window must first be locked before calling [Quit()](classBWindow.md#a054c0206836014dcc20c59e50bceab44).



**See also:** [BLooper::Quit()](../application_kit/classBLooper.md#a10d5a4873f14fd247890a6dfc9b8b949)



**Since:** BeOS R3


Reimplemented from [BLooper](../application_kit/classBLooper.md#a10d5a4873f14fd247890a6dfc9b8b949).


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#a0e078c054a66514021099c529cfdde2f), and [BAlert](classBAlert.md#a691fe42dc7dc5acea09771e9c080dd0e).


Referenced by [Close()](classBWindow.md#a3be508837c0b14b176b916e45c9c1f31).

---

### `QuitRequested()`

```cpp
bool BWindow::QuitRequested()
```

Hook method that gets called when the window receives a *B_QUIT_REQUESTED* message. 



**See also:** [Quit()](classBWindow.md#a054c0206836014dcc20c59e50bceab44)



**Since:** BeOS R3


Reimplemented from [BLooper](../application_kit/classBLooper.md#aff7aaf066538383f0e0ea28d18eb8863).


Reimplemented in [BAlert](classBAlert.md#ae91bb7bb3b99006f0b2616d47cf85985).

---

### `RemoveChild()`

```cpp
bool BWindow::RemoveChild(BView * child)
```

Removes *child* from the view hierarchy. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `child` | The child view to remove. |





**Returns:** Whether or not *child* was removed from the view hierarchy.



**Since:** BeOS R3

---

### `RemoveFromSubset()`

```cpp
status_t BWindow::RemoveFromSubset(BWindow * window)
```

Remove *window* from the subset of the [BWindow](classBWindow.md). 



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | *window* was removed from the subset of the [BWindow](classBWindow.md). |
| B_BAD_VALUE | `window` is not `B_NORMAL_WINDOW_FEEL` or the [BWindow](classBWindow.md) object's feel is not set to `B_MODAL_SUBSET_WINDOW_FEEL` or `B_FLOATING_SUBSET_WINDOW_FEEL`. |
| B_ERROR | Could not lock the [BWindow](classBWindow.md) object. |





**Since:** BeOS R3

---

### `RemoveShortcut()`

```cpp
void BWindow::RemoveShortcut(uint32 key, uint32 modifiers)
```

Removes the specified shortcut from the window. 


The memory used by the shortcut message is freed.


Parameters

| Parameter | Description |
| :--- | :--- |
| `key` | The character to remove, case-insensitive. |
| `modifiers` | A bit mask of modifiers in addition to `B_COMMAND_KEY`, options include one or more of the following: * `B_SHIFT_KEY`  * `B_OPTION_KEY`  * `B_CONTROL_KEY`  * `B_MENU_KEY` To remove `B_COMMAND_KEY` specify `B_NO_COMMAND_KEY`. |





**Since:** BeOS R3

---

### `ResizeBy()`

```cpp
void BWindow::ResizeBy(float dx, float dy)
```

Resize the window by *dx* pixels horizontally and *dy* pixels vertically. 


*dx* and *dy* must be integral units.


dx The number of pixels to resize the window horizontally.


dy The number of pixels to resize the window vertically.



**Since:** BeOS R3

---

### `ResizeTo()`

```cpp
void BWindow::ResizeTo(float width, float height)
```

Resize the window to the specified *width* and *height*. 


*width* and *height* must be integral units.


Parameters

| Parameter | Description |
| :--- | :--- |
| `width` | The width to resize the window to. |
| `height` | The height to resize the window to. |





**Since:** BeOS R3

---

### `ResizeToPreferred()`

```cpp
void BWindow::ResizeToPreferred()
```

Resize the window to the preferred size of the window's layout. 



**Since:** Haiku R1

---

### `ResolveSpecifier()`

```cpp
BHandler * BWindow::ResolveSpecifier(BMessage * message, int32 index, BMessage * specifier, int32 what, const char * property)
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


Reimplemented from [BLooper](../application_kit/classBLooper.md#a16b494160d9b37d4dbbc0d426a22c946).


Reimplemented in [BAlert](classBAlert.md#a22285daeb96ea0936faab97b077115e6), and [BDirectWindow](../game_kit/classBDirectWindow.md#aee5db7142cabc984cb16e61eaa7baa36).

---

### `Run()`

```cpp
thread_id BWindow::Run()
```

Spawns the message loop thread and starts the window running. 



**See also:** [BLooper::Run()](../application_kit/classBLooper.md#a88bb85410e0c4124bdc6f16168df4811)



**Since:** BeOS R3


Reimplemented from [BLooper](../application_kit/classBLooper.md#a88bb85410e0c4124bdc6f16168df4811).

---

### `ScreenChanged()`

```cpp
void BWindow::ScreenChanged(BRect screenSize, color_space depth)
```

Hook method that is called when the screen that the window is located on changes size or location or the color space of the screen changes. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `screenSize` | The new screen size in the screen's coordinate system. |
| `depth` | The new color space of the screen. |





**Since:** BeOS R3


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#af260392459433e8abf6e47e869065975).

---

### `SendBehind()`

```cpp
status_t BWindow::SendBehind(const BWindow * window)
```

Moves the [BWindow](classBWindow.md) object behind *window*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `window` | A pointer to the window to move behind. |





**Returns:** `B_OK` on success or `B_ERROR` on failure.



**Since:** BeOS R3

---

### `SetDecoratorSettings()`

```cpp
status_t BWindow::SetDecoratorSettings(const BMessage & settings)
```

Set the window decorator settings according to *settings*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `settings` | The decorator *settings* message to set. |





**Returns:** `B_OK` if the decorator settings were set successfully or an error code otherwise.



**Since:** Haiku R1

---

### `SetDefaultButton()`

```cpp
void BWindow::SetDefaultButton(BButton * button)
```

Set the default button of the window to *button*. 


The default button has a grey outline and is activated by the user pushing the Enter key. The user can activate the default button even if another view is currently set to be the focus view of the window.


A window may only have one default button at a time, to remove the current default without setting another button you may pass in `NULL`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `button` | A pointer to the button to set as the default or `NULL` to unset. |





**Since:** BeOS R3

---

### `SetFeel()`

```cpp
status_t BWindow::SetFeel(window_feel feel)
```

Changes the window feel set in the constructor to *feel*. 



**Returns:** `B_OK` on success or an error code on failure.



**Since:** BeOS R3

---

### `SetFlags()`

```cpp
status_t BWindow::SetFlags(uint32 flags)
```

Changes the window flags set in the constructor to *flags*. 



**Returns:** `B_OK` on success or an error code on failure.



**Since:** BeOS R3

---

### `SetKeyMenuBar()`

```cpp
void BWindow::SetKeyMenuBar(BMenuBar * bar)
```

Set the specified menu *bar* as the key menu bar for the window. 


The key menu bar is the one located at the top of the window at the root of the menu hierarchy that the user can navigate with the keyboard.


Parameters

| Parameter | Description |
| :--- | :--- |
| `bar` | A pointer to the menu *bar* to set as as the key menu *bar* for the window. |





**Since:** BeOS R3

---

### `SetLayout()`

```cpp
void BWindow::SetLayout(BLayout * layout)
```

Sets the *layout* of the window. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `layout` | The *layout* to set. |





**Since:** Haiku R1


Referenced by [BLayoutBuilder::Cards< ParentBuilder >::Cards()](classBLayoutBuilder_1_1Cards.md#a08329883aebee0490f3faf96d86f1108), [BLayoutBuilder::Grid< ParentBuilder >::Grid()](classBLayoutBuilder_1_1Grid.md#ad7bd68789548063830f46a0bb279e17a), and [BLayoutBuilder::Group< ParentBuilder >::Group()](classBLayoutBuilder_1_1Group.md#adebaf628afb53fdd86d6b153d60cf0ea).

---

### `SetLook()`

```cpp
status_t BWindow::SetLook(window_look look)
```

Changes the window look set in the constructor to *look*. 



**Returns:** `B_OK` on success or an error code on failure.



**Since:** BeOS R3

---

### `SetPulseRate()`

```cpp
void BWindow::SetPulseRate(bigtime_t rate)
```

Sets how often `B_PULSE` messages are posted to the window. 


All BViews attached to a window share the same pulse rate.


*rate* should not be set to less than 100,000 microseconds, differences less than 50,000 microseconds may not be noticeable.


Setting the *rate* to 0 disables pulsing for all views attache to the window.


Parameters

| Parameter | Description |
| :--- | :--- |
| `rate` | The pulse rate to set. |





**Since:** BeOS R3

---

### `SetSizeLimits()`

```cpp
void BWindow::SetSizeLimits(float minWidth, float maxWidth, float minHeight, float maxHeight)
```

Set size limits on the window. 


The user won't be able to resize the window beyond the limits set by this method. [SetSizeLimits()](classBWindow.md#a8668ecf18ad145391f66704c3339eb3d) constrains the user, not the programmer, you may still resize the window outside of the size limits set by this method by calling [ResizeBy()](classBWindow.md#a6aba4ddafc654f362799b6a96e6c76cd) or [ResizeTo()](classBWindow.md#a31e2ea325258646128cfe8618cb79edc).


Parameters

| Parameter | Description |
| :--- | :--- |
| `minWidth` | The minimum width of the window to set. |
| `maxWidth` | The maximum width of the window to set. |
| `minHeight` | The minimum height of the window to set. |
| `maxHeight` | The maximum height of the window to set. |





**Since:** BeOS R3

---

### `SetTitle()`

```cpp
void BWindow::SetTitle(const char * title)
```

Sets the window title to *title*. 


Also renames the window thread to "w>title" where "title" is the passed in title string.



**Since:** BeOS R5

---

### `SetType()`

```cpp
status_t BWindow::SetType(window_type type)
```

Changes the window type set in the constructor to *type*. 



**Returns:** `B_OK` on success or an error code on failure.



**Since:** BeOS R3

---

### `SetWindowAlignment()`

```cpp
status_t BWindow::SetWindowAlignment(window_alignment mode, int32 h, int32 hOffset = 0, int32 width = 0, int32 widthOffset = 0, int32 v = 0, int32 vOffset = 0, int32 height = 0, int32 heightOffset = 0)
```

Sets the alignment of the content of the window on the screen. 



**Since:** BeOS R3

---

### `SetWorkspaces()`

```cpp
void BWindow::SetWorkspaces(uint32 workspaces)
```

Sets the set of workspaces where the window can be displayed. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `workspaces` | * `B_CURRENT_WORKSPACE` to place the window in the currently displayed workspace removing it from all others.  * `B_ALL_WORKSPACES` to make the window show up in all workspaces. |





**Since:** BeOS R3

---

### `SetZoomLimits()`

```cpp
void BWindow::SetZoomLimits(float maxWidth, float maxHeight)
```

Sets the maximum size that the window will zoom to when [Zoom()](classBWindow.md#a722772f2902e82bf65010ac2c13570bc) is called. 


The window will zoom to the minimum of the screen size, the maximum values set by [SetSizeLimits()](classBWindow.md#a8668ecf18ad145391f66704c3339eb3d), and the maximum values set by this method.


/see [Zoom()](classBWindow.md#a722772f2902e82bf65010ac2c13570bc)



**Since:** BeOS R3

---

### `Show()`

```cpp
void BWindow::Show()
```

Shows the window on screen, places it frontmost on the screen, adds the window to Deskbar's window list, and makes it the active window. 


If this is the first time [Show()](classBWindow.md#af7009117df50add72cf0e799ff7d0fa5) has been called on the window the message loop is started and it is unlocked.


Calls to [Hide()](classBWindow.md#a53b85e4d43d34e5259b3b16ff6c52b32) and [Show()](classBWindow.md#af7009117df50add72cf0e799ff7d0fa5) are cumulative.



**Since:** BeOS R3


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#a48d82b1d72a1def5188b1985b5f51f33).

---

### `Size()`

```cpp
BSize BWindow::Size()const
```

Returns the size of the window. 



**Returns:** The size of the window as a [BSize](classBSize.md) in the screen coordinate system.



**Since:** Haiku R1

---

### `Sync()`

```cpp
void BWindow::Sync()const
```

Synchronizes the attached window's connection to App Server causing any pending messages to be processed and then waits for the App Server to respond. 



**Since:** BeOS R3

---

### `Title()`

```cpp
const char * BWindow::Title()const
```

Returns the window title as set by the constructor or [SetTitle()](classBWindow.md#a7cd4bf7dc0079e9a52b0ac1e7e2f897b). 



**Returns:** A pointer to the window title.



**Since:** BeOS R3

---

### `Type()`

```cpp
window_type BWindow::Type()const
```

Returns the current window type flag. 



**Returns:** The currently set window type flag.



**Since:** BeOS R3

---

### `UpdateIfNeeded()`

```cpp
void BWindow::UpdateIfNeeded()
```

Invokes Draw() immediately on each child view that needs updating. 


This method is synchronous, it waits for each child view to update before returning. This method is ignored unless it is called from within the message loop of the thread that the [BWindow](classBWindow.md) is running in.


You may call this method as part of a hook function such as MouseMoved() or KeyDown() to force invalid views to be immediately redrawn without having to wait for the hook function to finish.



**Since:** BeOS R3

---

### `UpdateSizeLimits()`

```cpp
void BWindow::UpdateSizeLimits()
```

Updates the window's size limits from the minimum and maximum sizes of its top view. 


This method does nothing unless the `B_AUTO_UPDATE_SIZE_LIMITS` window flag is set.


The method is called automatically after a layout invalidation. Since it is invoked asynchronously, calling this method manually is necessary, if it is desired to adjust the limits (and as a possible side effect the window size) earlier, e.g. before the first call to the [Show()](classBWindow.md#af7009117df50add72cf0e799ff7d0fa5) method.)



**Since:** Haiku R1

---

### `WindowActivated()`

```cpp
void BWindow::WindowActivated(bool active)
```

Hook method that gets called when the window becomes activated or deactivated. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `active` | `true` if the window has become activated, `false` if the window has become deactivated. |





**Since:** BeOS R3


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#a1521e3361a53816b665861141b3d651a).

---

### `WorkspaceActivated()`

```cpp
void BWindow::WorkspaceActivated(int32 workspace, bool state)
```

Hook method that gets called when the active workspace changes. 


This method is only called when a workspace in which the window resides is activated or deactivated.


Parameters

| Parameter | Description |
| :--- | :--- |
| `workspace` | The *workspace* number that was activated/deactivated. |
| `state` | `true` if activated, `false` if deactivated. |





**Since:** BeOS R3


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#a965f35341d9515e1f5c9c93eaa3404eb).

---

### `Workspaces()`

```cpp
uint32 BWindow::Workspaces()const
```

Returns the set of workspaces where the window can be displayed. 



**Since:** BeOS R3

---

### `WorkspacesChanged()`

```cpp
void BWindow::WorkspacesChanged(uint32 oldWorkspaces, uint32 newWorkspaces)
```

Hook method that gets called whenever the workspaces the window is in changes. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `oldWorkspaces` | The old set of workspaces the window was visible in. |
| `newWorkspaces` | The new set of workspaces the window is visible in. |





**Since:** BeOS R3


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#a566f11807e382e2e09610619a2029f63).

---

### `Zoom()`

```cpp
void BWindow::Zoom()
```

Resize the window to the minimum of the screen size, the maximum values set by [SetSizeLimits()](classBWindow.md#a8668ecf18ad145391f66704c3339eb3d), and the maximum values set by [SetZoomLimits()](classBWindow.md#ad3c2e560e41b377456faf9bd5dabcdc0). 


You may call [Zoom()](classBWindow.md#a722772f2902e82bf65010ac2c13570bc) even if the window has the `B_NOT_ZOOMABLE` flag set.


This is the method called when the user clicks the window's zoom button. It can also be called programmatically.


The window dimensions are calculated from the smallest of three rectangles:


1. the screen frame,

2. the rectangle defined by [SetZoomLimits()](classBWindow.md#ad3c2e560e41b377456faf9bd5dabcdc0),

3. the rectangle defined by [SetSizeLimits()](classBWindow.md#a8668ecf18ad145391f66704c3339eb3d).



However if the window frame already matches these new dimensions, [Zoom()](classBWindow.md#a722772f2902e82bf65010ac2c13570bc) uses the previous size and location of the window instead.


This method calls [Zoom(BPoint, float, float)](classBWindow.md#ae7bea03df00c760d7f489acd3e312290) to do the actualy zooming.



**See also:** [Zoom(BPoint, float, float)](classBWindow.md#ae7bea03df00c760d7f489acd3e312290);



**Since:** BeOS R3

---

### `Zoom()`

```cpp
void BWindow::Zoom(BPoint origin, float width, float height)
```

Move window to *origin*, then resize to *width* and *height*. 


You may call [Zoom()](classBWindow.md#a722772f2902e82bf65010ac2c13570bc) even if the window has the `B_NOT_ZOOMABLE` flag set.


This method may move and resize the window resulting in both the [FrameMoved()](classBWindow.md#a95f6fb2941250e7ed54fce6671f782c6) and [FrameResized()](classBWindow.md#a280fab2b2900abc61dd4bcb7a2a4793f) hook methods to be called.


You can override this method to change how your window behaves when the user clicks the zoom button or when [Zoom()](classBWindow.md#a722772f2902e82bf65010ac2c13570bc) is called.


Parameters

| Parameter | Description |
| :--- | :--- |
| `origin` | The point that the window was moved to. |
| `width` | The new width of the window. |
| `height` | The new height of the window. |





**Since:** BeOS R3


Reimplemented in [BDirectWindow](../game_kit/classBDirectWindow.md#afa7f05be4a2964c593b3287a3216b041).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBWindow.html).
