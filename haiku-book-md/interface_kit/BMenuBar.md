---
name: BMenuBar
type: class
kit: interface_kit
brief: "A window's root menu"
source: haiku-book
---

# BMenuBar Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A window's root menu. 


A menu bar, if a window has one, is typically drawn across the top of the window just below the tab and a window typically has just a single menu bar, although this is up to you.


One menu bar attached to a window is considered to be the "key" menu bar that can be navigated by the user using the keyboard. The last menu bar attached to a window is automatically set as the key menu bar for the window. To override this behavior and set a different key menu bar use the [BWindow::SetKeyMenuBar()](classBWindow.md#aa1e9322c76ffdad1886253171f8a5972) method.


When either the Menu key or Command+Esc keys are pressed the key menu bar opens and focuses its first menu item, typically a [BMenu](classBMenu.md). Once the menu bar is open the user can navigate around the attached menus and menu items using the arrow keys.


Like a [BMenu](classBMenu.md), a [BMenuBar](classBMenuBar.md) object starts without any items attached to it, you'll need to call [AddItem()](classBMenu.md#a93b3441be6f675d4f04b396a460f3edb) or [AddList()](classBMenu.md#a7e9495276526fabf009db1f923fcc036) to add some. The top-level items in a menu bar are typically menus which have menu items and menus added to them in turn.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BMenuBar](#ad083b4d1fcaa2c8483d73c0691cccd8f) (BMessage *archive) — Archive constructor.
* [BMenuBar](#a97f304a1b753aec98c4cf89af4174909) (BRect frame, const char *name, uint32 resizingMode=B_FOLLOW_LEFT_RIGHT|B_FOLLOW_TOP, menu_layout layout=B_ITEMS_IN_ROW, bool resizeToFit=true) — Create a new BMenuBar object.
* [BMenuBar](#a33de2272d8a5d2415d6204bdd92e51ee) (const char *name, menu_layout layout=B_ITEMS_IN_ROW, uint32 flags=B_WILL_DRAW|B_FRAME_EVENTS) — Create a new BMenuBar object suitable to use with the layout APIs.
* `virtual` [~BMenuBar](#a4a0e51a23570d9c9abf66121e88c1ea9) () — Destructor.
* `virtual void` [AllAttached](#ac02982cd861af6eb4771f260fcf50ed8) () — Similar to AttachedToWindow() but this method is triggered after all child views have already been attached to a window.
* `virtual void` [AllDetached](#a0c548adc7796603d8d686a401817d0d9) () — Similar to AttachedToWindow() but this method is triggered after all child views have already been detached from a window.
* `menu_bar_border` [Border](#aa105aa010f8a65da27fa268fb2c482d1) () const — Returns the currently set border style.
* `virtual void` [DetachedFromWindow](#aaf4b5448201a1d30c969ddc20f1d492d) () — Hook method called when the object is detached from a window.
* `virtual void` [FrameMoved](#aa711264d76e8f5faa0f974ca66d01ccf) (BPoint newPosition) — Hook method called when the view is moved.
* `virtual void` [GetPreferredSize](#ab4dd370f1363d89c1fb2918877595b02) (float *_width, float *_height) — Fill out the preferred width and height of the view into the _width and _height parameters.
* `virtual status_t` [GetSupportedSuites](#ad635f7e68997f901cbd4b15491b5f2a3) (BMessage *data)
* `virtual void` [Hide](#a7dfa53005734435d3b805161e3495e99) () — Hides the view without removing it from the view hierarchy.
* `virtual void` [MakeFocus](#a170fbfdd3be7b9bdc750777f31c216c0) (bool state=true) — Makes the view the current focus view of the window or gives up being the window's focus view.
* `virtual BSize` [MaxSize](#ad0dc5e934924d2511d82718d31da2740) () — Return the maximum size of the view.
* `virtual void` [MessageReceived](#a7d7c1d1674e059b56c82c81e381d4455) (BMessage *message) — Handles a message received by the associated looper.
* `virtual BSize` [MinSize](#ae0781646adecf0bd08123868c40ee218) () — Return the minimum size of the view.
* `virtual void` [MouseUp](#a4781bbe6cd7ccff992b0c12f2c4ea4b7) (BPoint where) — Hook method called when a mouse button is released.
* `virtual status_t` [Perform](#a4b8a4e16ace175bc3bad9d6ef6b42daf) (perform_code code, void *data) — Perform some action. (Internal Method)
* `virtual BSize` [PreferredSize](#ae3e3832dbc024a802a18c4253f01b05a) () — Return the preferred size of the view.
* `virtual void` [ResizeToPreferred](#a7e846a6abc075a0db6305e86cbed1760) () — Resizes the view to its preferred size keeping the position of the left top corner constant.
* `virtual BHandler *` [ResolveSpecifier](#ab8e2eb06afc52455be926b3cde21f935) (BMessage *message, int32 index, BMessage *specifier, int32 form, const char *property)
* `virtual void` [SetBorder](#a3d1f0ec6b4718c089f128bbcb864697d) (menu_bar_border border) — Specifies how the menu bar border is drawn.
* `virtual void` [Show](#ac0b9dafc30dd338e8f67b26eff7168f0) () — Shows the view making it visible.
* `virtual void` [WindowActivated](#a5e623033adfd89d43cca5b8030fb9ccf) (bool state) — Hook method called when the attached window is activated or deactivated.
* `virtual void` [AttachedToWindow](#a48b3c56f65222c9dc3e5faca5eb80319) () — Sets this as the key menubar for the window, lays out the menu items and resizes the menu to fit.
* `virtual void` [FrameResized](#ad3dcc7b2c1eeada95ef6986a21754324) (float newWidth, float newHeight) — Hook method that gets called when the menu bar is resized.
* `virtual void` [Draw](#a50f02992ee792e7f66b8f3148e75dcc8) (BRect updateRect) — Draws the menu bar.
* `virtual void` [MouseDown](#a0aa84693746c1cfe671c48a4dcc654c6) (BPoint where) — Hook method that is called when a mouse button is pressed.
* [BMenu](#a66018a8f741b47ff198cd0308bf75bb5) (BMessage *archive) — Archive constructor.
* [BMenu](#ab6ace1b9965547b7e2019818effc3e15) (const char *name, float width, float height) — Creates a new menu object with a B_ITEMS_IN_MATRIX layout and the specified name, width, and height.
* [BMenu](#a7a674ff3dbf2620a038bb1728edd4378) (const char *name, menu_layout layout=B_ITEMS_IN_COLUMN) — Creates a new menu object with the specified name and layout.
* `virtual` [~BMenu](#ad986f4d6a7b9c5a99f51535b55bdd4df) () — Destructor.
* `virtual bool` [AddDynamicItem](#a23bb62b2d8ebf6ebd539218273e31eb0) (add_state state) — Implemented by subclasses to add their own items to the menu.
* `bool` [AddItem](#a28e2ee1c1f97b5d7ab4b397493c1b37e) (BMenu *menu) — Add a submenu to the end of the list.
* `bool` [AddItem](#ae9d684a3d4ad604e19b0727939a1e1b3) (BMenu *menu, BRect frame) — Adds a submenu in the specified frame rectangle within the menu.
* `bool` [AddItem](#a627295137a1fb9d6567a03243cab27f4) (BMenu *menu, int32 index) — Add a submenu at the specified index.
* `bool` [AddItem](#a93b3441be6f675d4f04b396a460f3edb) (BMenuItem *item) — Adds a menu item to the end of the list.
* `bool` [AddItem](#af7369a0039d85b80bb43a87e069babf7) (BMenuItem *item, BRect frame) — Adds a menu item in the specified frame rectangle within the menu.
* `bool` [AddItem](#a54b0803984953195bf425f439f2877f3) (BMenuItem *item, int32 index) — Adds a menu item at the specified index.
* `bool` [AddList](#a7e9495276526fabf009db1f923fcc036) (BList *list, int32 index) — Add a list of menu items at the specified index.
* `bool` [AddSeparatorItem](#a9101f4977ee547e81e6a2544f891e493) () — Adds a separator item to the end of the menu.
* `virtual void` [AllAttached](#a2540cab39de9a2ed1a3e71e2c8ec52dc) () — Similar to AttachedToWindow() but this method is triggered after all child views have already been attached to a window.
* `virtual void` [AllDetached](#a40c41c3d2d1a8e23dfad97039615b208) () — Similar to AttachedToWindow() but this method is triggered after all child views have already been detached from a window.
* `bool` [AreTriggersEnabled](#a97d2138f50a3fd757b31407627e12eea) () const — Returns whether or not triggers are enabled.
* `int32` [CountItems](#ae2328de69b20f84bd925dc943e3ae3cc) () const — Returns the number of items added to the menu.
* `virtual void` [DetachedFromWindow](#a51b79eb8595e20234f2fefabf7899e21) () — Hook method called when the object is detached from a window.
* `virtual void` [DoLayout](#a981691c987e0f0a82a8f056284280032) () — Layout view within the layout context.
* `virtual void` [DrawBackground](#ae315f78a12586d80ea7db6247d7d8f1a) (BRect updateRect) — Draw the menu background within the bounds of updateRect.
* `BMenuItem *` [FindItem](#a28dc785b54ef7b7c820c173e607610ed) (const char *name) const — Returns a pointer to the menu item with the specified label.
* `BMenuItem *` [FindItem](#a8a9b9f676fb940ad648c76499219ee63) (uint32 command) const — Returns a pointer to the menu item with the specified command for its associated message.
* `BMenuItem *` [FindMarked](#a359ed911cbf2e38b93fdc8a7bcbd5439) () — Return a pointer to the first marked menu item.
* `int32` [FindMarkedIndex](#a79ac06123571bb519ae25cd15482497c) () — Return the index of the first marked menu item.
* `virtual void` [FrameMoved](#ab14bf3dc8b6f082f2609094c1f964577) (BPoint where) — Hook method called when the view is moved.
* `virtual void` [FrameResized](#ad6d6eac1f12e9456b9db896aee122181) (float width, float height) — Hook method called when the view is resized.
* `virtual void` [GetPreferredSize](#af60a7b8ec6f92749fd46ce2e9179dc17) (float *_width, float *_height) — Fill out the preferred width and height of the view into the _width and _height parameters.
* `virtual status_t` [GetSupportedSuites](#a2aa0277374bacf3b7644f738bc064637) (BMessage *data)
* `int32` [IndexOf](#a515c29525463092462e64105469dcdcf) (BMenu *menu) const — Returns the index of the specified submenu.
* `int32` [IndexOf](#a93256bdb0b477bf1ba52e6bd75f86694) (BMenuItem *item) const — Returns the index of the specified menu item.
* `bool` [IsEnabled](#a374ec27870b0d21e0f16d77e5aa12535) () const — Returns whether or not the menu is enabled.
* `bool` [IsLabelFromMarked](#ac2a915d6b9b323c3d12d29df7a2b5571) () — Returns whether or not the menu is in label-from-marked mode.
* `bool` [IsRadioMode](#a85e16e170b2d5e16a91c5608b31865fc) () const — Returns whether or not the menu is in radio mode.
* `bool` [IsRedrawAfterSticky](#aca1162897b36710a15957b7148907d24) () const — Returns whether or not the menu is in redraw-after-sticky mode.
* `BMenuItem *` [ItemAt](#a1612e6c652a53451bbd7da8ab52d0668) (int32 index) const — Returns a pointer to the menu item at the specified index.
* `virtual void` [MakeFocus](#a1465ef5881a0b85729118534d8ee3a15) (bool focus=true) — Makes the view the current focus view of the window or gives up being the window's focus view.
* `float` [MaxContentWidth](#ae35fd8bf7622196e8c1c7400cdad2823) () const — Return the maximum width of the menu items' content area.
* `virtual BSize` [MaxSize](#a5f94df489ae102d0e377df3b63d9864a) () — Return the maximum size of the view.
* `virtual BSize` [MinSize](#a659643414ede82d0233e62ce9da4c01e) () — Return the minimum size of the view.
* `virtual status_t` [Perform](#a6dedb98c6ba5ffbc44893ff43785c93c) (perform_code d, void *arg) — Perform some action. (Internal Method)
* `virtual BSize` [PreferredSize](#a03aad94d2eb22836823045530e58c052) () — Return the preferred size of the view.
* `bool` [RemoveItem](#ab221333103579b6c7a5d08c7c6005e20) (BMenu *menu) — Remove and delete a submenu from the menu.
* `bool` [RemoveItem](#a5bddcfe7908198f10046fd58e517d906) (BMenuItem *item) — Remove and delete the specified item from the menu.
* `BMenuItem *` [RemoveItem](#a3b28ecdc6fa0e04f8da5fea0a295d667) (int32 index) — Remove the item at the specified index from the menu.
* `bool` [RemoveItems](#a21410c37d9ff94ce58f00a4741126a7d) (int32 index, int32 count, bool deleteItems=false) — Remove count number of items from the menu starting at the specified index and delete them if deleteItems is true.
* `virtual void` [ResizeToPreferred](#a90a8228da7623e8e991a2fc7dc0e8898) () — Resizes the view to its preferred size keeping the position of the left top corner constant.
* `virtual BHandler *` [ResolveSpecifier](#adfd2e1d211f34a8ac748abb989adac48) (BMessage *message, int32 index, BMessage *specifier, int32 form, const char *property)
* `virtual void` [SetEnabled](#a68c7fe3263da4d1cb254bd0b6ee1f01f) (bool enable) — Enables or disables the menu.
* `void` [SetLabelFromMarked](#a6575006958cc1fd049fea76fed4c40ba) (bool on) — Sets whether or not the label of the menu is set according to the marked item.
* `virtual void` [SetMaxContentWidth](#ae0ccabdfaa67f0ffa7ec3e6e8efdcd03) (float maxWidth) — Sets the maximum width of the menu items' content area.
* `virtual void` [SetRadioMode](#a71036007fd11439ac43bccc05e833938) (bool on) — Turns radio mode on or off.
* `virtual status_t` [SetTargetForItems](#ab11e3f007322fc75a9943a1443339ac2) (BHandler *target) — Set the target to handler for each item in the menu.
* `virtual status_t` [SetTargetForItems](#aa6075b7d5ed82ba117904f3b5cec61ef) (BMessenger messenger) — Set the target to messenger for each item in the menu.
* `void` [SetTrackingHook](#a7718aab1bf69711c4eb1043424eb2a59) (menu_tracking_hook hook, void *state) — Sets a hook function that is called when tracking begins.
* `virtual void` [SetTriggersEnabled](#a67da7ae008cbe0f38196e5aafd79fe53) (bool enable) — Enables or disables triggers.
* `BMenu *` [SubmenuAt](#a51cad9f6d981ce27ca0094f74540ce29) (int32 index) const — Returns a pointer to a submenu at the specified index.
* `BMenuItem *` [Superitem](#a544cdc1fc6d05c535d677a65ad1ee3d9) () const — Returns the pointer to the menu item that this menu it attached to.
* `BMenu *` [Supermenu](#a205d32b63c8fc5a5a3a49249838af057) () const — Returns the pointer to the menu that this menu it attached to.
* `virtual void` [KeyDown](#a6c50b44b2da8caf0280854c5a250b8c2) (const char *bytes, int32 numBytes) — Hook method that is called when a keyboard key is pressed.
* `void` [SortItems](#a4a3000f320f707d70da1e72da79fca72) (int(*compare)(const BMenuItem *, const BMenuItem *)) — Sort items in the menu.
* `bool` [SwapItems](#a717c241c8234cbec4327e6f55b5df1b7) (int32 indexA, int32 indexB) — Swap the positions of two items in the menu.
* `bool` [MoveItem](#a52f15cd54ebd73143c0c0f68e7eb5a43) (int32 indexFrom, int32 indexTo) — Move a menu item to a new position in the menu.
* [BView](#ae982fac35c278cc64990c506efe3965e) (BMessage *archive) — Archive constructor.
* [BView](#ae3a1b2a66dc19690e766623be65c37e2) (BRect frame, const char *name, uint32 resizingMode, uint32 flags) — Standard constructor.
* [BView](#ab148f59c41c9a22ced87bf7a0221ed62) (const char *name, uint32 flags, BLayout *layout=NULL) — Layout constructor.
* `virtual` [~BView](#a7df0d7eaeb97a3c8a800f9e321f23f67) () — Destructor method.
* `BRect` [Bounds](#acbb8ea442346e91428689163db9d633e) () const — Returns the view's frame rectangle in the view's coordinate system.
* `void` [Flush](#a15465930f84d2d01f7818bd79bc91c3e) () const — Flushes the attached window's connection to App Server.
* `BRect` [Frame](#a487b04a3aaffdd1a1afb730dca36a7e2) () const — Returns the view's frame rectangle in the parent's coordinate system.
* `virtual void` [GetPreferredSize](#a089c3ff794c454388a9388c7b6568478) (float *_width, float *_height) — Fill out the preferred width and height of the view into the _width and _height parameters.
* `virtual status_t` [GetSupportedSuites](#a772462d751d457f63ee0fc56d8ba02d1) (BMessage *data)
* `virtual void` [Hide](#a7688dc04178a2955950154ee3670d029) () — Hides the view without removing it from the view hierarchy.
* `bool` [IsFocus](#a165719de682845f80735042a499692ff) () const — Returns whether or not the view is the window's current focus view.
* `bool` [IsHidden](#a33a65050c2315b19b4c5af16c48e3cdb) () const — Returns whether or not the view is hidden.
* `bool` [IsHidden](#a95cfa8ee585230ea8fb224e88eddc503) (const BView *looking_from) const — Returns whether or not the view is hidden from the perspective of lookingFrom.
* `bool` [IsPrinting](#a8e3f1722e40fdf01c5131e49199ec3ff) () const — Returns whether or not the view is drawing to a printer.
* `BPoint` [LeftTop](#a5d252dfe28eee049be2192d1a01ed6e3) () const — Returns the left top corner point.
* `virtual status_t` [Perform](#a512a6c8dca1a62b14cdcb1c22070129b) (perform_code code, void *data) — Perform some action. (Internal Method)
* `virtual void` [ResizeToPreferred](#abe8c63c85555e800e063388e7cf3e1a7) () — Resizes the view to its preferred size keeping the position of the left top corner constant.
* `uint32` [ResizingMode](#a1e93df523fc9edc807274ac6cfd2dc8d) () const — Returns the resizing mode flags mask set in the constructor or by SetResizingMode().
* `virtual BHandler *` [ResolveSpecifier](#a4c0c6d3b21ae92056e5e40fe4d3ec175) (BMessage *message, int32 index, BMessage *specifier, int32 form, const char *property)
* `virtual void` [SetResizingMode](#a38d29ea581880c3978d7e50dcc851696) (uint32 mode) — Sets the resizing mode of the view according to the mode mask.
* `void` [SetViewCursor](#a39b4878773b4436e3c76aee51c4fbc09) (const BCursor *cursor, bool sync=true) — Assigns cursor to the view.
* `virtual void` [Show](#a06e0584057d6c7a7c7e048b6272b7016) () — Shows the view making it visible.
* `void` [Sync](#a27e217abb3fefa45b6e4ceb7a54cb362) () const — Synchronizes the attached window's connection to App Server.
* `BWindow *` [Window](#a32733d357b76bc3504cae326d174f4a2) () const — Returns the window the view is attached to.
* `void` [AddChild](#ab6382c582e5e1be527d3199459d05e8f) (BView *child, BView *before=NULL) — Adds child to the view hierarchy immediately before before.
* `bool` [AddChild](#a5d30ae4fa0119bf5286f52f83c2f351c) (BLayoutItem *child) — Add the child layout item to the view hierarchy.
* `bool` [RemoveChild](#a5f93a23d06267da83c128bce222ceb17) (BView *child) — Removes child from the view hierarchy.
* `int32` [CountChildren](#ae30d094a1cb1f3357c4aa7caa4b0e29d) () const — Returns the number of child views that this view has.
* `BView *` [ChildAt](#aaf91592f50f2f44d16f23e7504f494cb) (int32 index) const — Returns a pointer to the child view found at index.
* `BView *` [NextSibling](#a76e7d862fe78e4d2766573bf073b9d30) () const — Returns a pointer to the next sibling view.
* `BView *` [PreviousSibling](#a2a46f78756eacca3f3d4c90d31c758b1) () const — Returns a pointer to the previous sibling view.
* `bool` [RemoveSelf](#a87e0848b1760a9f28aad4516467a03ed) () — Removes the view and all child views from the view hierarchy.
* `BView *` [FindView](#ab83ef89f1876913174c825ff7cd02c4a) (const char *name) const — Returns the view in the view hierarchy with the specified name.
* `BView *` [Parent](#a332f34d9862000dbc859fd4e308839dd) () const — Returns a pointer to the view's parent.
* `void` [ConvertToScreen](#aefefb1242613b869feb6b8e0cc119518) (BPoint *point) const — Convert point to the screen's coordinate system in place.
* `BPoint` [ConvertToScreen](#af90cdeb62cc60adf64eb9a669c37c153) (BPoint point) const — Returns point converted to the screen's coordinate system.
* `void` [ConvertFromScreen](#a4b794ccd899dc6a0cafd886169122df5) (BPoint *point) const — Convert point from the screen's coordinate system to the view's coordinate system in place.
* `BPoint` [ConvertFromScreen](#a75f1d68cf77bccc03930eb8e273f2967) (BPoint point) const — Returns point converted from the screen's coordinate system to the view's coordinate system.
* `void` [ConvertToScreen](#ad99f5af006f28c485f02484752a2ac5d) (BRect *rect) const — Convert rect to the screen's coordinate system in place.
* `BRect` [ConvertToScreen](#ae60c56c306d0cf3f504d710fac8b9bed) (BRect rect) const — Returns rect converted to the screen's coordinate system.
* `void` [ConvertFromScreen](#a3fbc496f437925cb02ccf9e817406e4e) (BRect *rect) const — Convert rect from the screen's coordinate system to the view's coordinate system in place.
* `BRect` [ConvertFromScreen](#a44c3b5174e4ccfa4c123e0d5d54e9408) (BRect rect) const — Returns rect converted from the screen's coordinate system to the view's coordinate system.
* `void` [ConvertToParent](#ab20700567eabd5f8135be179b4232e2c) (BPoint *point) const — Convert point to the parent's coordinate system in place.
* `BPoint` [ConvertToParent](#a91e6a7edab78547be47cb8dc84cfdecf) (BPoint point) const — Returns point converted to the parent's coordinate system.
* `void` [ConvertFromParent](#a43c16140dd4491a6a6f7bad11bbea1f9) (BPoint *point) const — Convert point from the parent's coordinate system to the view's coordinate system in place.
* `BPoint` [ConvertFromParent](#aa3201bdf5c489fbab7d67afe3453466d) (BPoint point) const — Returns point converted from the parent's coordinate system to the view's coordinate system.
* `void` [ConvertToParent](#ac7bd2e0e7aac40d1be9a47999b5701a9) (BRect *rect) const — Convert rect to the parent's coordinate system in place.
* `BRect` [ConvertToParent](#ae3b385e4d1b9f70bc848bf2fd0b7753c) (BRect rect) const — Returns rect converted to the parent's coordinate system.
* `void` [ConvertFromParent](#ab2aeeb14409a18f950173e7cb22e147c) (BRect *rect) const — Convert rect from the parent's coordinate system to the view's coordinate system in place.
* `BRect` [ConvertFromParent](#a45b405f10c29442aea8b70161410565f) (BRect rect) const — Returns rect converted from the parent's coordinate system to the view's coordinate system.
* `virtual void` [SetFlags](#a4740f9a1e1163073b042102a421a2e33) (uint32 flags) — Sets the view flags to the flags mask.
* `uint32` [Flags](#a561b10abf94dd65a26b02253af667508) () const — Return the view flags set in the constructor or by SetFlags().
* `void` [GetClippingRegion](#acf50a063c9621f35a84b1d0245b12d69) (BRegion *region) const — Fill out region with the view's clipping region.
* `virtual void` [ConstrainClippingRegion](#a656b8d82a6a7c7c6ab33c3dd08aad6ec) (BRegion *region) — Set the clipping region the region restricting the area that the view can draw in.
* `void` [ClipToPicture](#a9c92c9e8e306d00dbfef81f2b0282339) (BPicture *picture, BPoint where=B_ORIGIN, bool sync=true) — Intersects the current clipping region of the view with the pixels of picture.
* `void` [ClipToInversePicture](#a18d61bcae2a7ca8a1a0977ac23d15171) (BPicture *picture, BPoint where=B_ORIGIN, bool sync=true) — Intersects the current clipping region of the view with the pixels outside of picture.
* `void` [ClipToRect](#a22ff147a2f0a0bd65de494c9a039acee) (BRect rect) — Intersects the current clipping region of the view with the pixels of rect.
* `void` [ClipToInverseRect](#ad1762d160500ec3ce90c7bd73944d8a7) (BRect rect) — Intersects the current clipping region of the view with the pixels outside of rect.
* `void` [ClipToShape](#ac0884c62949361a7eb6a4834f46b902c) (BShape *shape) — Intersects the current clipping region of the view with the pixels of shape.
* `void` [ClipToInverseShape](#a17dcb4f2e92994cde9a9ece9caa619c2) (BShape *shape) — Intersects the current clipping region of the view with the pixels outside of shape.
* `virtual void` [SetDrawingMode](#a0c392ed0e36213e1007322a9cbca71c0) (drawing_mode mode) — Sets the drawing mode of the view.
* `drawing_mode` [DrawingMode](#ae7953a2e451fb6e5a439df9e9dc8451a) () const — Return the current drawing_mode.
* `void` [SetBlendingMode](#ad01fc0fd68e4683af9b9386bf33abf63) (source_alpha srcAlpha, alpha_function alphaFunc) — Set the blending mode which controls how transparency is used.
* `void` [GetBlendingMode](#ad50d5ba2249fdf3dd8640b3573c2a2e8) (source_alpha *srcAlpha, alpha_function *alphaFunc) const — Fill out srcAlpha and alphaFunc with the alpha mode and alpha function of the view.
* `virtual void` [SetPenSize](#a80ea4cb97d2e6e2c3088e610a9e157e6) (float size) — Set the pen size to size.
* `float` [PenSize](#a69d8657d26b49773fa2de914f263b204) () const — Return the current pen size.
* `bool` [HasDefaultColors](#a606e0e7e03516dccb53bf073827460a8) () const — Tests if the view has any colors set.
* `bool` [HasSystemColors](#aa9aacc95606b650e6a8d776b51cb902b) () const — Tests if the view is using system "panel" colors. B_PANEL_BACKGROUND_COLOR for ViewUIColor() B_PANEL_BACKGROUND_COLOR for LowUIColor() B_PANEL_TEXT_COLOR for HighUIColor()
* `void` [AdoptParentColors](#ac780f029d415ee0a915792b4e756fa77) () — Attempts to use the colors of any parent view. Will adopt view, low, and high colors. Should be called in AttachedToWindow() or AllAttached().
* `void` [AdoptSystemColors](#a0e429a82fe06e9ab390b06d993ee31be) () — Instructs view to use standard system "panel" colors. B_PANEL_BACKGROUND_COLOR for ViewUIColor() B_PANEL_BACKGROUND_COLOR for LowUIColor() B_PANEL_TEXT_COLOR for HighUIColor()
* `void` [AdoptViewColors](#ab68ad7103708884f9e6fd84e8a579746) (BView *view) — Attempts to use the colors of a given view. Will adopt view, low, and high colors.
* `virtual void` [SetViewColor](#ae8dde0e0330b394db016f3e609e7fb6a) (rgb_color color) — Set the view color of the view.
* `void` [SetViewColor](#a7dace2963c85b5ce55b7d8e96946625c) (uchar red, uchar green, uchar blue, uchar alpha=255) — Set the view color of the view.
* `rgb_color` [ViewColor](#a8b2b1d9e08ce0c1763dd6a077ed02fdd) () const — Return the current view color.
* `void` [SetViewUIColor](#a34f020c4bb1008cef972cf1eec7dba0f) (color_which which, float tint=B_NO_TINT) — Set the view color of the view to a system constant. The color will update live with user changes.
* `color_which` [ViewUIColor](#aec6c89446eb4f5ded151adced9126df8) (float *tint=NULL) const — Return the current view color constant being used.
* `virtual void` [SetHighColor](#ab5482f91a642d545bc3fcefe199f95e9) (rgb_color color) — Set the high color of the view.
* `void` [SetHighColor](#aff9e1ab5e88f33027e72b39874868e9b) (uchar red, uchar green, uchar blue, uchar alpha=255) — Set the high color of the view.
* `rgb_color` [HighColor](#abda3583967fba9f6ed9524058d00a6e9) () const — Return the current high color.
* `void` [SetHighUIColor](#a54eefc28bf7a4bc30612cf83aff2963b) (color_which which, float tint=B_NO_TINT) — Set the high color of the view to a system constant. The color will update live with user changes.
* `color_which` [HighUIColor](#aa86f548fba2e82d022066198be6d5af6) (float *tint=NULL) const — Return the current high color constant being used.
* `virtual void` [SetLowColor](#af0426243110fb150ad7ef0705209a12c) (rgb_color color) — Set the low color of the view.
* `void` [SetLowColor](#a929fb1ca47a00220c355ae55a0ea6077) (uchar red, uchar green, uchar blue, uchar alpha=255) — Set the low color of the view.
* `rgb_color` [LowColor](#a423c54f22ab95745b28b583af999e554) () const — Return the current low color.
* `void` [SetLowUIColor](#a879ab88d4e64345069f1041d3a7b652f) (color_which which, float tint=B_NO_TINT) — Set the low color of the view to a system constant. The color will update live with user changes.
* `color_which` [LowUIColor](#ae32ca6d8f106d44b5b51df82a7eb64c5) (float *tint=NULL) const — Return the current low color constant being used.
* `void` [SetLineMode](#ae97bfe6c0c93fce98bc7bbd93761dbfb) (cap_mode lineCap, join_mode lineJoin, float miterLimit=B_DEFAULT_MITER_LIMIT) — Set line mode to use PostScript-style line cap and join modes.
* `join_mode` [LineJoinMode](#a0aa47adb29d91b4cc6c4924b7f436012) () const — Returns the current line join mode.
* `cap_mode` [LineCapMode](#a551f5961188e4f26ef310eb5eea7c926) () const — Returns the current line cap mode.
* `float` [LineMiterLimit](#ab1cd7cf77a4fa01755d186a05163cfbe) () const — Returns the miter limit used for B_MITER_JOIN join mode.
* `void` [SetFillRule](#a2019def93337069c0b7d416e103522e9) (int32 rule) — Sets the fill rule for the view.
* `int32` [FillRule](#a3a2fd2d7313a9bb7dff359a4f4362a5f) () const — Return the current fill mode.
* `void` [SetOrigin](#a769e5fa6486adf12e7a3511ed372a06c) (BPoint where) — Sets the origin in the view's coordinate system.
* `void` [SetOrigin](#a7cf4e3ac5b0759b9c38d7b36517f2337) (float x, float y) — Sets the origin in the view's coordinate system.
* `BPoint` [Origin](#aefbf71a7a403900e960ffa3943dc9901) () const — Returns the origin point in the view's coordinate system.
* `void` [SetTransform](#afbd9b8f35226ba89980c450f7626fc85) (BAffineTransform transform) — Sets a BAffineTransform to transform the coordinate system.
* `BAffineTransform` [Transform](#ab16cc72cf8ae3b40abcf1f714e7e9b74) () const — Returns the current BAffineTransform that is applied to the coordinate system.
* `void` [TranslateBy](#a8ae6d4e1cdfeeee33b753d56bee6ae7f) (double x, double y) — Translate the current view by coordinates.
* `void` [ScaleBy](#ac83f9fdfb882f849e3ac79bfb06a0fd6) (double x, double y) — Scale the current view by factors x and y.
* `void` [RotateBy](#a02ab6b6196b140b20ae516a55680e30b) (double angleRadians) — Rotate the current view by angleRadians.
* `BAffineTransform` [TransformTo](#a98597d70ae48b2576683f25078135534) (coordinate_space basis) const — Return the BAffineTransform to convert from the current drawing space to basis.
* `void` [PushState](#a1dcb914cd0c6ef8d1291aa8492968d40) () — Saves the drawing state to the stack.
* `void` [PopState](#abc0d202fe13366b80703afbdb3832951) () — Restores the drawing state from the stack.
* `void` [MovePenTo](#acb61254a2121f569f6223a95cd835abd) (BPoint pt) — Move the pen to point in the view's coordinate system.
* `void` [MovePenTo](#ae32d7951a4ce9cff6b81899f5208a25f) (float x, float y) — Move the pen to the point specified by x and y in the view's coordinate system.
* `void` [MovePenBy](#a979f8f0090284919b6e7c6c04d91cbde) (float x, float y) — Move the pen by x pixels horizontally and y pixels vertically.
* `BPoint` [PenLocation](#a2774e13c2b12c6a5fee333e95b76b07d) () const — Return the current pen location as a BPoint object.
* `virtual void` [SetFont](#a9247127c151153542a3e6bc1f3904433) (const BFont *font, uint32 mask=B_FONT_ALL) — Set the font of the view.
* `void` [GetFont](#af244d01f85e6d9ae7f5fcca4637dc78c) (BFont *font) const — Fill out font with the font set to the view.
* `void` [TruncateString](#ac2e293fbdd999e4857b44b6e4d4c3820) (BString *in_out, uint32 mode, float width) const — Truncate string with truncation mode mode so that it is no wider than width set in the view's font.
* `float` [StringWidth](#adef480de8a8bcd2fff3129660501616e) (const char *string) const — Return the width of string set in the font of the view.
* `float` [StringWidth](#aef3638cf597407e6a9f31bc75cd42097) (const char *string, int32 length) const — Return the width of string set in the font of the view up to length characters.
* `void` [GetStringWidths](#aaae0dc93bc61d7f221465fbe0aecd30a) (char *stringArray[], int32 lengthArray[], int32 numStrings, float widthArray[]) const — Fill out widths of the strings in stringArray set in the font of the view into widthArray.
* `void` [SetFontSize](#a443e4d9ff182f85a6b1c8478ef22ffe8) (float size) — Set the size of the view's font to size.
* `void` [ForceFontAliasing](#a424161ccf6f52a354fdd67ed1376d196) (bool enable) — Turn anti-aliasing on and off when printing.
* `void` [GetFontHeight](#a5bf95d66754634c647b2ddf7d39b4dfb) (font_height *height) const — Fill out the font_height struct with the view font.
* `void` [SetScale](#a077136ea06f0a6b39aa0b8b24311cce8) (float scale) const — Sets the scale of the coordinate system the view uses for drawing.
* `float` [Scale](#a50e12d6b8080b3bc6bc617d31d1ab200) () const — Return the current drawing scale.
* `void` [SetViewBitmap](#ac247ddc58f1cb719d60e354a77c51c1e) (const BBitmap *bitmap, BRect srcRect, BRect dstRect, uint32 followFlags=B_FOLLOW_LEFT_TOP, uint32 options=B_TILE_BITMAP) — Sets the background bitmap of the view.
* `void` [SetViewBitmap](#a046a9c1656823db5401e530cf8121734) (const BBitmap *bitmap, uint32 followFlags=B_FOLLOW_LEFT_TOP, uint32 options=B_TILE_BITMAP) — Sets the background bitmap of the view.
* `void` [ClearViewBitmap](#ae7582b9a2b0b446a1de16c681f23baf9) () — Clears the background bitmap of the view if it has one.
* `status_t` [SetViewOverlay](#a576100502a8c6dfb46ff36b08cbe9405) (const BBitmap *overlay, BRect srcRect, BRect dstRect, rgb_color *colorKey, uint32 followFlags=B_FOLLOW_LEFT_TOP, uint32 options=0) — Sets the overlay bitmap of the view.
* `status_t` [SetViewOverlay](#a9770c1bb97d7ffd797f7c40ca1339f98) (const BBitmap *overlay, rgb_color *colorKey, uint32 followFlags=B_FOLLOW_LEFT_TOP, uint32 options=0) — Sets the overlay bitmap of the view.
* `void` [ClearViewOverlay](#a0ae48f37c3f56b422841638971488cc0) () — Clears the overlay bitmap of the view if it has one.
* `void` [StrokeLine](#a909ee03901fac4ae5504f7faf5e41a7c) (BPoint toPoint, ::pattern pattern=B_SOLID_HIGH) — Stroke a line from the current pen location to the point toPoint.
* `void` [StrokeLine](#ab713fc42e330d0a091a9774edfb9626f) (BPoint start, BPoint end, ::pattern pattern=B_SOLID_HIGH) — Stroke a line from point start to point end.
* `void` [BeginLineArray](#ab3f2e9f54d2b93952b27e182ac552983) (int32 count) — Begin a line array of up to count lines.
* `void` [AddLine](#a88440336a66ee9b1a4b1661e9ba9e59c) (BPoint start, BPoint end, rgb_color color) — Add a line to the line array drawn from start to end.
* `void` [EndLineArray](#a24ba922f9698936bc27f48b3c51349a1) () — End the line array drawing the lines.
* `void` [StrokePolygon](#ae871d03592c1bba5d6be3d5d982ea747) (const BPolygon *polygon, bool closed=true, ::pattern pattern=B_SOLID_HIGH) — Stroke a polygon shape.
* `void` [StrokePolygon](#a1638c58553467f3ebe5ee2b3683d4905) (const BPoint *pointArray, int32 numPoints, bool closed=true, ::pattern pattern=B_SOLID_HIGH) — Stroke a polygon shape made up of points specified by pointArray.
* `void` [StrokePolygon](#a1482fddababe3dd1377f86a038f7119b) (const BPoint *pointArray, int32 numPoints, BRect bounds, bool closed=true, ::pattern pattern=B_SOLID_HIGH) — Stroke a polygon shape made up of points specified by pointArray inscribed by bounds.
* `void` [FillPolygon](#ae72733cae8a1fc2da8feb47c0c2149fa) (const BPolygon *polygon, ::pattern pattern=B_SOLID_HIGH) — Fill a polygon shape.
* `void` [FillPolygon](#adc7d96f2d60a819f03685eb11b6945e2) (const BPoint *pointArray, int32 numPoints, ::pattern pattern=B_SOLID_HIGH) — Fill a polygon shape made up of points specified by pointArray.
* `void` [FillPolygon](#a1bdc02a311b2a051ad7fbdbf1789e958) (const BPoint *pointArray, int32 numPoints, BRect bounds, ::pattern pattern=B_SOLID_HIGH) — Fill a polygon shape made up of points specified by pointArray inscribed by bounds.
* `void` [FillPolygon](#a96cdb60a8c87e4958380a3077a2197a5) (const BPolygon *polygon, const BGradient &gradient) — Fill a polygon shape with the specified gradient pattern.
* `void` [FillPolygon](#a22a5ce1f024e622b6eade6a9176ff1f7) (const BPoint *pointArray, int32 numPoints, const BGradient &gradient) — Fill a polygon shape made up of points specified by pointArray with the specified gradient pattern.
* `void` [FillPolygon](#a57b0870cd6a0109c347d80c34ca2f34a) (const BPoint *pointArray, int32 numPoints, BRect bounds, const BGradient &gradient) — Fill a polygon shape made up of points specified by pointArray inscribed by bounds with the specified gradient pattern.
* `void` [StrokeTriangle](#a8221cce8942e590c2fea954f57933e78) (BPoint point1, BPoint point2, BPoint point3, BRect bounds, ::pattern pattern=B_SOLID_HIGH) — Stroke the triangle specified by points point1, point2, and point3 and enclosed by bounds.
* `void` [StrokeTriangle](#ae59fc9e9cfaba5e2d6e79a90723a3330) (BPoint point1, BPoint point2, BPoint point3, ::pattern pattern=B_SOLID_HIGH) — Stroke the triangle specified by points point1, point2, and point3.
* `void` [FillTriangle](#a46ec16609a402d03baa322a04d8c50e2) (BPoint point1, BPoint point2, BPoint point3, ::pattern pattern=B_SOLID_HIGH) — Fill the triangle specified by points point1, point2, and point3.
* `void` [FillTriangle](#af512b76752705cba87f89c8dac313005) (BPoint point1, BPoint point2, BPoint point3, BRect bounds, ::pattern pattern=B_SOLID_HIGH) — Fill the triangle specified by points point1, point2, and point3 and enclosed by bounds.
* `void` [FillTriangle](#a5dd1c64839c11a79e80581e37656cc26) (BPoint point1, BPoint point2, BPoint point3, const BGradient &gradient) — Fill the triangle specified by points point1, point2, and point3 with the specified gradient pattern.
* `void` [FillTriangle](#a0878dea14a61d58c951bd8e11c0a2ef6) (BPoint point1, BPoint point2, BPoint point3, BRect bounds, const BGradient &gradient) — Fill the triangle specified by points point1, point2, and point3 and enclosed by bounds with the specified gradient pattern.
* `void` [StrokeRect](#ad3893af66d3891855f9db7072bfb4de7) (BRect rect, ::pattern pattern=B_SOLID_HIGH) — Stroke the rectangle specified by rect.
* `void` [FillRect](#a4d074663998c7ba922a9d981d0cfe086) (BRect rect, ::pattern pattern=B_SOLID_HIGH) — Fill the rectangle specified by rect.
* `void` [FillRect](#aae6a3ff6683bb15ac8c647c946475e8f) (BRect rect, const BGradient &gradient) — Fill the rectangle specified by rect with the specified gradient pattern.
* `void` [FillRegion](#a4810086c415d90bffa25ab2963716936) (BRegion *rectegion, ::pattern pattern=B_SOLID_HIGH) — Fill region.
* `void` [FillRegion](#a56828d13947717462b661e1645305509) (BRegion *rectegion, const BGradient &gradient) — Fill region with the specified gradient pattern.
* `void` [InvertRect](#af7e5ebc41cd5a471dcdcfa1f3db801a5) (BRect rect) — Inverts the colors within rect.
* `void` [StrokeRoundRect](#acf743b2ba22b82c8bc38eb514513df55) (BRect rect, float xRadius, float yRadius, ::pattern pattern=B_SOLID_HIGH) — Stroke the rounded rectangle with horizontal radius xRadius and vertical radius yRadius.
* `void` [FillRoundRect](#a38d7e7b15a13591c20020599886402b5) (BRect rect, float xRadius, float yRadius, ::pattern pattern=B_SOLID_HIGH) — Fill the rounded rectangle with horizontal radius xRadius and vertical radius yRadius.
* `void` [FillRoundRect](#a73956d28b356b2eee83ebc19bd6e398b) (BRect rect, float xRadius, float yRadius, const BGradient &gradient) — Fill the rounded rectangle with horizontal radius xRadius and vertical radius yRadius with the specified gradient pattern.
* `void` [StrokeEllipse](#a042703445263f1d9a9213757fcf27414) (BPoint center, float xRadius, float yRadius, ::pattern pattern=B_SOLID_HIGH) — Stroke the outline of an ellipse starting at center with a horizontal radius of xRadius and a vertical radius of yRadius.
* `void` [StrokeEllipse](#ae7727ca808873634363e5306fdbcc09a) (BRect rect, ::pattern pattern=B_SOLID_HIGH) — Stroke the outline of an ellipse inscribed within rect.
* `void` [FillEllipse](#a06942f0dd4c13175bcfff6a88eae7cc0) (BPoint center, float xRadius, float yRadius, ::pattern pattern=B_SOLID_HIGH) — Fill an ellipse starting at center with a horizontal radius of xRadius and a vertical radius of yRadius.
* `void` [FillEllipse](#a98a73cbccb42edfc61b93f9aa6f4a13b) (BRect rect, ::pattern pattern=B_SOLID_HIGH) — Fill an ellipse inscribed within rect.
* `void` [FillEllipse](#a2738cf2f3d39f560d0cff90543f45afa) (BPoint center, float xRadius, float yRadius, const BGradient &gradient) — Fill an ellipse with the specified gradient pattern starting at center with a horizontal radius of xRadius and a vertical radius of yRadius.
* `void` [FillEllipse](#a86de91f260577187eaf22ba0fdf32fba) (BRect rect, const BGradient &gradient) — Fill an ellipse with the specified gradient pattern inscribed within rect.
* `void` [StrokeArc](#a57222cd40096dfe23e1df86a01277041) (BPoint center, float xRadius, float yRadius, float startAngle, float arcAngle, ::pattern pattern=B_SOLID_HIGH) — Stroke the outline of an arc starting at center with a horizontal radius of xRadius and a vertical radius of yRadius starting at startAngle and drawing arcAngle degrees.
* `void` [StrokeArc](#a9c958b9399925a8a0ea333afd337ebfd) (BRect rect, float startAngle, float arcAngle, ::pattern pattern=B_SOLID_HIGH) — Stroke the outline of an arc inscribed within rect starting at startAngle and drawing arcAngle degrees.
* `void` [FillArc](#af0e5d362474d39199116045aa9621aa5) (BPoint center, float xRadius, float yRadius, float startAngle, float arcAngle, ::pattern pattern=B_SOLID_HIGH) — Fill an arc starting at center with a horizontal radius of xRadius and a vertical radius of yRadius starting at startAngle and drawing arcAngle degrees.
* `void` [FillArc](#ac216c652253a21f0f28a7caef07deb77) (BRect rect, float startAngle, float arcAngle, ::pattern pattern=B_SOLID_HIGH) — Fill an arc inscribed within rect starting at startAngle and drawing arcAngle degrees.
* `void` [FillArc](#a49017edefe45ca5c74954e1227e673bb) (BPoint center, float xRadius, float yRadius, float startAngle, float arcAngle, const BGradient &gradient) — Fill an arc with the specified gradient pattern starting at center with a horizontal radius of xRadius and a vertical radius of yRadius starting at startAngle and drawing arcAngle degrees.
* `void` [FillArc](#a4304fe45708f72d0ba20b579870c24ce) (BRect rect, float startAngle, float arcAngle, const BGradient &gradient) — Fill an arc with the specified gradient pattern inscribed within rect starting at startAngle and drawing arcAngle degrees.
* `void` [StrokeBezier](#a64ea2ad06018b0b3b156113d201c7ad7) (BPoint *controlPoints, ::pattern pattern=B_SOLID_HIGH) — Stroke a bezier curve.
* `void` [FillBezier](#a531ad43e129d810ee64208123b550193) (BPoint *controlPoints, ::pattern pattern=B_SOLID_HIGH) — Fill a bezier curve.
* `void` [FillBezier](#a7cf8a5eaa5451b2c7df0d6fa392012bd) (BPoint *controlPoints, const BGradient &gradient) — Fill a bezier curve.
* `void` [StrokeShape](#a507e9b732e880ac8e6379e19e74d5757) (BShape *shape, ::pattern pattern=B_SOLID_HIGH) — Stroke shape.
* `void` [FillShape](#a91b9ce4b8b8ee13ff5f1071e1fb0d829) (BShape *shape, ::pattern pattern=B_SOLID_HIGH) — Fill shape.
* `void` [FillShape](#a9a82da733397e97b985875be941f77a6) (BShape *shape, const BGradient &gradient) — Fill shape with the specified gradient pattern.
* `void` [CopyBits](#a8ace5c5cc811c4ad16acf281ffd1a48d) (BRect src, BRect dst) — Copy the bits from the src rectangle to the dst rectangle in the view's coordinate system.
* `void` [DrawBitmapAsync](#ae66727344d35f05c56b6163ad70e360c) (const BBitmap *aBitmap, BRect bitmapRect, BRect viewRect, uint32 options) — Draws bitmap on the view within viewRect asynchronously. bitmap portion is scaled to fit viewRect.
* `void` [DrawBitmapAsync](#a0ef432afa41aefcb3fdd537e2d290001) (const BBitmap *aBitmap, BRect bitmapRect, BRect viewRect) — Draws bitmap on the view within viewRect asynchronously. bitmap portion is scaled to fit viewRect.
* `void` [DrawBitmapAsync](#aa3275b791787a66f3638611cd6a5ae09) (const BBitmap *aBitmap, BRect viewRect) — Draws bitmap on the view within viewRect asynchronously. bitmap is scaled to fit viewRect.
* `void` [DrawBitmapAsync](#a6931c5fe803eb5fa9e66438d347c4b6d) (const BBitmap *aBitmap, BPoint where) — Draws bitmap on the view offset by where asynchronously.
* `void` [DrawBitmapAsync](#ab50fba0500357abebb9f3ef3832f2e68) (const BBitmap *aBitmap) — Draws bitmap on the view asynchronously.
* `void` [DrawBitmap](#a6171150993fbf7c73966c7c302a95573) (const BBitmap *aBitmap, BRect bitmapRect, BRect viewRect, uint32 options) — Draws bitmap on the view within viewRect. bitmap portion is scaled to fit viewRect.
* `void` [DrawBitmap](#a63db7245fd9b9fefd461d7596c15f9cc) (const BBitmap *aBitmap, BRect bitmapRect, BRect viewRect) — Draws bitmap on the view within viewRect. bitmap portion is scaled to fit viewRect.
* `void` [DrawBitmap](#abce81666128d183d59b5cf2ed75c7f07) (const BBitmap *aBitmap, BRect viewRect) — Draws bitmap on the view within viewRect. bitmap is scaled to fit viewRect.
* `void` [DrawBitmap](#a1c8b6e3e9218388a68ae43dd408a187c) (const BBitmap *aBitmap, BPoint where) — Draws bitmap on the view offset by where.
* `void` [DrawBitmap](#a769c3e3dee7d86ed50308f7a3f46ef91) (const BBitmap *aBitmap) — Draws bitmap on the view.
* `void` [DrawTiledBitmapAsync](#ad281a4e40f212e3cb56c23fa6e574a84) (const BBitmap *aBitmap, BRect viewRect, BPoint phase=B_ORIGIN) — Draws bitmap on the view within viewRect asynchronously. If bitmap is smaller, it is cloned to fill remaining space in viewRect.
* `void` [DrawTiledBitmap](#a8848d931fd0354860a0e71934e66cb03) (const BBitmap *aBitmap, BRect viewRect, BPoint phase=B_ORIGIN) — Draws bitmap on the view within viewRect. If bitmap is smaller, it is cloned to fill remaining space in viewRect.
* `void` [DrawChar](#a02ba5c68f21d4345ec3ee683496ce851) (char aChar) — Draws character c onto to the view at the current pen position.
* `void` [DrawChar](#a2ed7c3628692426116fc0bb450c0f0c7) (char aChar, BPoint location) — Draws character c at the specified location in the view.
* `void` [DrawString](#a5c261dbbb4e8157799e85d6ad1530920) (const char *string, escapement_delta *delta=NULL) — Draw string onto the view at the current pen position.
* `void` [DrawString](#a83d77965bd9cda6212189d92b97d8198) (const char *string, BPoint location, escapement_delta *delta=NULL) — Draw string onto the view at the specified location in the view.
* `void` [DrawString](#ad3830d09ed0300a1144d47ac78cd2dde) (const char *string, int32 length, escapement_delta *delta=NULL) — Draw string up to length characters onto the view at the current pen position.
* `void` [DrawString](#a4e1f1c59352a1373ccace7255a0ccf23) (const char *string, int32 length, BPoint location, escapement_delta *delta=0L) — Draw string up to length characters onto the view at the specified location in the view.
* `void` [DrawString](#a5dacf5d193a0c492f296bc1e402e6370) (const char *string, const BPoint *locations, int32 locationCount) — Draw string locationCount times at the specified locations.
* `void` [DrawString](#a135868eb5cd1b35ee1c2d03517b9a33f) (const char *string, int32 length, const BPoint *locations, int32 locationCount) — Draw string up to length characters locationCount times at the specified locations.
* `void` [Invalidate](#a8c767d948dc9435c006cabdcab1cd08e) (BRect invalRect) — Sends a message to App Server to redraw the portion of the view specified by invalRect.
* `void` [Invalidate](#ac70b682819c0f9b008c428e02015b19b) (const BRegion *invalRegion) — Sends a message to App Server to redraw the portion of the view specified by region.
* `void` [Invalidate](#adfced0dcb244e199f872fdbd48349a05) () — Sends a message to App Server to redraw the view.
* `void` [DelayedInvalidate](#ae2a9da1ca04489dd60ef8aefa86331ed) (bigtime_t delay) — Sends a message to App Server to redraw the entire view after a certain, minimum, delay. Repeated calls to this method may be merged, but the view is guaranteed to be redrawn after the delay given in the first call of this method.
* `void` [DelayedInvalidate](#a6389a46cf1842eb0d412b44958955e61) (bigtime_t delay, BRect invalRect) — Sends a message to App Server to redraw the portion of the view specified by invalRect after a certain, minimum, delay. Repeated calls to this method may be merged, but the invalidated rect is guaranteed to be redrawn after the minimum delay given by the first call of this method.
* `void` [SetDiskMode](#a8ba0fe3a3dbeec1b7fd8c9655070ef64) (char *filename, long offset) — Unimplemented.
* `void` [BeginPicture](#a14155192773aad22ebe47a9975afac5f) (BPicture *a_picture) — Begins sending drawing instructions to picture.
* `void` [AppendToPicture](#a2d73d2f2b0b35390929cf54fbfa5ecff) (BPicture *a_picture) — Appends drawing instructions to picture without clearing it first.
* `BPicture *` [EndPicture](#ae01506892a9b2d39f6df13726be9d0af) () — Ends the drawing instruction recording session and returns the BPicture object passed to BeginPicture() or AppendToPicture().
* `void` [DrawPicture](#ae4b252943befd9f0b62e30517b3ecec2) (const BPicture *a_picture) — Draws the picture at the view's current pen position.
* `void` [DrawPicture](#a2fdf36421cccce9136cdd9966a971955) (const BPicture *a_picture, BPoint where) — Draws the picture at the location in the view specified by where.
* `void` [DrawPicture](#a9f5781a2b37113c55950c93b621984a7) (const char *filename, long offset, BPoint where) — Draws the picture from the file specified by filename offset by offset bytes at the location in the view specified by where.
* `void` [DrawPictureAsync](#a65498927c21d6681a0e77c4e3d29efba) (const BPicture *a_picture) — Draws the picture at the view's current pen position.
* `void` [DrawPictureAsync](#a05881f8b07989e1e9db0bd41f8181341) (const BPicture *a_picture, BPoint where) — Draws the picture at the location in the view specified by where.
* `void` [DrawPictureAsync](#a7f2fde4e7719bded5af33805b8242b06) (const char *filename, long offset, BPoint where) — Draws the picture from the file specified by filename offset by offset bytes at the location in the view specified by where.
* `void` [BeginLayer](#abe65757b7c83c8db390bf0c87457a343) (uint8 opacity) — Begins a drawing layer.
* `void` [EndLayer](#a9f54d4478a12823f116168a45af30898) () — Finish a layer and blend it in with the view.
* `void` [MoveBy](#a6e122baca4494f6ce739a507054fa81f) (float dh, float dv) — Moves the view deltaX pixels horizontally and deltaY pixels vertically in the parent view's coordinate system.
* `void` [MoveTo](#acce9c93118a3db24078f16bdabc6fbec) (BPoint where) — Move the view to the location specified by where in the parent view's coordinate system.
* `void` [MoveTo](#a1c9b2df47ba1b9f3a1ce3286995fb8bd) (float x, float y) — Move the view to the coordinates specified by x in the horizontal dimension and y in the vertical dimension in the parent view's coordinate system.
* `void` [ResizeBy](#ace23acc948bbc9b9272da8dc7f01d3ce) (float dh, float dv) — Resize the view by deltaWidth horizontally and deltaHeight vertically without moving the top left corner of the view.
* `void` [ResizeTo](#a742bccd6034ef9ade65b0e596fba55f2) (float width, float height) — Resize the view to the specified width and height.
* `void` [ResizeTo](#a6134097569f75679616257a361086d7a) (BSize size) — Resize the view to the dimension specified by size.
* `virtual status_t` [AllUnarchived](#ab7bd04272afed8b28bf57d1de33cbe05) (const BMessage *archive) — Hook method called when all views have been unarchived.
* `virtual status_t` [AllArchived](#a561e82ed41cbb93d3bacf371787497bf) (BMessage *archive) const — Hook method called when all views have been archived.
* `virtual void` [MouseMoved](#ac8b20516e42bab2f1eeb130e2432bde0) (BPoint where, uint32 code, const BMessage *dragMessage) — Hook method called when the mouse is moved.
* `virtual void` [KeyUp](#acbc528bb70be49993bd99aa136dbb089) (const char *bytes, int32 numBytes) — Hook method called when a keyboard key is released.
* `virtual void` [Pulse](#a0ae8ec3e94ee3d41cb329e3df6966566) () — Hook method called when the view receives a B_PULSE message.
* `virtual void` [TargetedByScrollView](#a668a4ed5419c86a7f2696ca7ece28df7) (BScrollView *scrollView) — Hook method called when the view becomes the target of scrollView.
* `virtual void` [DrawAfterChildren](#abb50623b4236926b068fc5a2264f6a48) (BRect updateRect) — Perform any drawing that needs to be done after child view have already been drawn.
* `void` [BeginRectTracking](#ac1eb1eeee67ec97205a4acc6955185bd) (BRect startRect, uint32 style=B_TRACK_WHOLE_RECT) — Displays an outline rectangle on the view and initiates tracking.
* `void` [EndRectTracking](#a7bcc3532c03eeeb929278de8fcc1fd25) () — Ends tracking removing the outline rectangle from the view.
* `void` [GetMouse](#a830ce9cf2ac2ffb5f73f526ee5d6e53d) (BPoint *location, uint32 *buttons, bool checkMessageQueue=true) — Fills out the cursor location and the current state of the mouse buttons.
* `void` [DragMessage](#a1f4f0c3c5946df1d14e6031e5e12f40b) (BMessage *message, BRect dragRect, BHandler *replyTo=NULL) — Initiates a drag-and-drop session.
* `void` [DragMessage](#a466287a3d939759cc09e4a6d1c9982cd) (BMessage *message, BBitmap *bitmap, BPoint offset, BHandler *replyTo=NULL) — Initiates a drag-and-drop session of an image.
* `void` [DragMessage](#ae1caa1d0bef9452db00c2adc8e3280b4) (BMessage *message, BBitmap *bitmap, drawing_mode dragMode, BPoint offset, BHandler *replyTo=NULL) — Initiates a drag-and-drop session of an image with drawing_mode set by dragMode.
* `status_t` [SetEventMask](#a5d8d6b469a8a11a577d1d138cfc31162) (uint32 mask, uint32 options=0) — Sets whether or not the view can accept mouse and keyboard events when not in focus.
* `uint32` [EventMask](#a8851d500773c732ddbb1a4b31f0ad664) () — Returns the current event mask.
* `status_t` [SetMouseEventMask](#ae7705783d064a8613dcc6f36a2866ab2) (uint32 mask, uint32 options=0) — Sets whether or not the view can accept mouse and keyboard events when not in focus from within MouseDown() until the following MouseUp() event.
* `void` [ScrollBy](#ae20e2a3c46fc30a2a292c832eead7387) (float dh, float dv) — Scroll the view by deltaX horizontally and deltaY vertically.
* `void` [ScrollTo](#a33ed2a9eeff474a756b548996a82b964) (float x, float y) — Scroll the view to the point specified by coordinates.
* `virtual void` [ScrollTo](#a2b76ddc60289ce92e1fb706332edbafc) (BPoint where) — Scroll the view to the point specified by where.
* `BScrollBar *` [ScrollBar](#a0878bc7981ba814190b822349599a120) (orientation direction) const — Returns the BScrollBar object that has the BView set as its target.
* `virtual BAlignment` [LayoutAlignment](#a2f74b3e7c602045d8c927f923f45eefa) () — Return the current BAlignemnt of the view.
* `void` [SetExplicitMinSize](#abfcb5c761f9b06da3b4a6788aad5d0ee) (BSize size) — Set this view's min size, to be used by MinSize().
* `void` [SetExplicitMaxSize](#acd759dd7505050f9cbd8213c71991b8b) (BSize size) — Set this view's max size, to be used by MaxSize().
* `void` [SetExplicitPreferredSize](#a98b7d450210099ed59b7cd34f2575e20) (BSize size) — Set this view's preferred size, to be used by PreferredSize().
* `void` [SetExplicitSize](#aeef8a27a5577db87251412ce44421494) (BSize size) — Set this view's size.
* `void` [SetExplicitAlignment](#a6906e47d4fdd6923dd51edb60a83ccea) (BAlignment alignment) — Set this view's alignment, to be used by Alignment().
* `BSize` [ExplicitMinSize](#a1b24db754473008766cdd0fd9c4ee3b7) () const — Returns the explicit minimum size.
* `BSize` [ExplicitMaxSize](#a4e63cc8ca1f604ccb20f5891adade70f) () const — Returns the explicit maximum size.
* `BSize` [ExplicitPreferredSize](#a218cd0d238104a6ff31c1d72ae2d9e6e) () const — Returns the explicit preferred size.
* `BAlignment` [ExplicitAlignment](#a1f078f5c987061c5cf3059f7091bcb1a) () const — Returns the explicit alignment size.
* `virtual bool` [HasHeightForWidth](#abd411461b7e23ad17e7294f8f5e1cbeb) () — Returns whether the layout of the view can calculate a height for a given width.
* `virtual void` [GetHeightForWidth](#ad34bee968b1ec98a0bf89343340b6b07) (float width, float *min, float *max, float *preferred) — Returns the min, max and preferred height for a given width.
* `void` [InvalidateLayout](#a4a711316094e43076a3f5478d937accf) (bool descendants=false) — Invalidate layout.
* `virtual void` [SetLayout](#acac1ebbba8c76e543e1b06e84dffab02) (BLayout *layout) — Sets the layout of the view.
* `BLayout *` [GetLayout](#aec2975b51966c397aa52b9e3eebd2c85) () const — Get the layout of the view.
* `void` [EnableLayoutInvalidation](#ad43cc5c22f83d95632d3d81eff73f425) () — Enable layout invalidation.
* `void` [DisableLayoutInvalidation](#aa165cbaac7d6915feaae6048c4378c85) () — Disable layout invalidation.
* `bool` [IsLayoutInvalidationDisabled](#a4e86b719129a12afbda7c10371eeca47) () — Returns whether or not layout invalidation is disabled.
* `bool` [IsLayoutValid](#a00a5d5d6edee7d488d77df03945b3e94) () const — Returns whether or not the layout is valid.
* `void` [ResetLayoutInvalidation](#a127933a3820f0bfe0497b5e7ddfa191f) () — Service call for BView derived classes re-enabling InvalidateLayout() notifications.
* `BLayoutContext *` [LayoutContext](#ae066513c0a788a9544744d409f28cada) () const — Returns the BLayoutContext for this View.
* `void` [Layout](#a854b6ca54eeca610db9eab8b58d68a8b) (bool force) — Layout the view.
* `void` [Relayout](#a2cf4e698a4322ecfb946e440e0f7ac62) () — Relayout the view.
* `void` [SetToolTip](#a75fb825a3ef69c1c6fbf3535ee2260ab) (const char *text) — Set the tool tip of the view to text.
* `void` [SetToolTip](#aa377bad64048a2d3cd1c2b272ae3079b) (BToolTip *tip) — Set the tool tip of the view to the tip object.
* `BToolTip *` [ToolTip](#a127ceec2101b12c0fbe1e0e66a7b9dc1) () const — Return the tool tip set to the view or NULL if not set.
* `void` [ShowToolTip](#a61d28f55d6fdc55b59c38c44b9788205) (BToolTip *tip=NULL) — Show the tool tip at the current mouse position.
* `void` [HideToolTip](#af75bbc1131ad6a90e299c6cbcf623fa7) () — Hide the view's tool tip.
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

### Archiving

* `virtual status_t` [Archive](#af4ae9bcc3c1cbe560e745c9868fb9c5f) (BMessage *archive, bool deep=true) const — Archives the the BMenuBar object into the data message.
* `static BArchivable *` [Instantiate](#ac26385837dc4b71f8c15282438148711) (BMessage *archive) — Creates a new BMenuBar object from an archive message.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#aabd77aafaee5d7185890e33c73b8d09e) (BMessage *archive) — Creates a new BMenu object from an archive message.
* `static BArchivable *` [Instantiate](#a730a46bedfe8db2176e4c331330e7924) (BMessage *archive) — Creates a new BView object from the data message.
* `static BArchivable *` [Instantiate](#a0c23aeb48d578525f81ba6d47f968528) (BMessage *data) — Static method to instantiate a handler from an archived message.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.
* [BMenu](#ad70c71bed508876fa919b63072bb5c72) (BRect frame, const char *name, uint32 resizeMask, uint32 flags, menu_layout layout, bool resizeToFit) — Implemented by derived classes to create a new menu object.
* `void` [GetItemMargins](#a46adc5db4b9a629a93c198a41a57ca36) (float *_left, float *_top, float *_right, float *_bottom) const — Fill out the margins into the passed in float pointers.
* `void` [Hide](#acebb809699f7efa7d72346f2ba0b869f) () — Hides the view without removing it from the view hierarchy.
* `menu_layout` [Layout](#a0a7706c4966b183b9790822bc512fd4e) () const — Returns the current menu_layout constant.
* `virtual void` [LayoutInvalidated](#ab5474abecef27e68bade9c58721caeed) (bool descendants) — Hook method called when the layout is invalidated.
* `void` [SetItemMargins](#a2f12a6614dfdea3b27e248b29be764dc) (float left, float top, float right, float bottom) — Set the menu item margins.
* `virtual void` [Show](#a880d9a96919d389e03106e978709bf9b) () — Shows the view making it visible.
* `BMenuItem *` [Track](#a22254e7fa893fea5c381ff59b2c8c3a8) (bool startOpened=false, BRect *specialRect=NULL) — Initiates tracking the cursor within the menu.
* `virtual void` [LayoutChanged](#ada521f848e4c800cd02eb4fe529e7ea0) () — Hook function that is called when the layout if this view, or one of its children, has changed.
* `status_t` [ScrollWithMouseWheelDelta](#a54991372110199183fed775598ae1912) (BScrollBar *, float) — Handle the scroll wheel changing over scrollbars.
* `virtual bool` [GetToolTipAt](#afb826fe9b8964e4d843cae190170badf) (BPoint point, BToolTip **_tip) — Point _tip with the view's tool tip.

## Detailed Member Documentation

### `BMenuBar()`

```cpp
BMenuBar::BMenuBar(BRect frame, const char * name, uint32 resizingMode = B_FOLLOW_LEFT_RIGHT | B_FOLLOW_TOP, menu_layout layout = B_ITEMS_IN_ROW, bool resizeToFit = true)
```

Create a new [BMenuBar](classBMenuBar.md) object. 


The default resizing mode, `B_FOLLOW_LEFT_RIGHT` | `B_FOLLOW_TOP` is meant to be used by a typical menu bar that is positioned along the top edge of a window. This resizing mode allows the menu bar to resize itself based on changes to the window's width while keeping it attached to the top of the window frame.


For menu bars in `B_ITEMS_IN_ROW` layout the height is automatically set to be the height of a single item, while menus bars in `B_ITEMS_IN_COLUMN` layout the width is automatically set to be the width of the widest item.


The width of a menu bar is set equal to the width of its parent for menu bars in `B_ITEMS_IN_ROW` layout and a *resizingMode* mask that includes `B_FOLLOW_LEFT_RIGHT` so that the menu bar will always be as wide as its attached window.


Likewise, the height of a menu bar is set equal to the height of its parent for menu bars in `B_ITEMS_IN_COLUMN` layout and a *resizingMode* mask that includes `B_FOLLOW_TOP_BOTTOM` so that the menu bar will always be as high as its attached window.


When *resizeToFit* is set to `true`, as is the default, the *frame* rectangle determines only where the menu bar is located, not its size. If the *layout* is set to `B_ITEMS_IN_MATRIX` the *resizeToFit* flag should be set to `false`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `frame` | The *frame* rectangle to create the menu bar in. |
| `name` | The *name* of the menu bar, used internally only. |
| `resizingMode` | The resizing mode flags, see [BView](classBView.md) for more details. |
| `layout` | The menu layout, possibilities include: * `B_ITEMS_IN_ROW` items are displayed in a single row,  * `B_ITEMS_IN_COLUMN` items are displayed in a single column,  * `B_ITEMS_IN_MATRIX` items are displayed in a custom matrix. |
| `resizeToFit` | Whether or not the menu bar should automatically resize itself to fit its contents, this will not work in `B_ITEMS_IN_MATRIX` layout. |





**Since:** BeOS R3

---

### `BMenuBar()`

```cpp
BMenuBar::BMenuBar(const char * name, menu_layout layout = B_ITEMS_IN_ROW, uint32 flags = B_WILL_DRAW | B_FRAME_EVENTS)
```

Create a new [BMenuBar](classBMenuBar.md) object suitable to use with the layout APIs. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The *name* of the menu bar, used internally only. |
| `flags` | The view *flags*, see [BView](classBView.md) for more details. |
| `layout` | The menu layout, possibilities include: * `B_ITEMS_IN_ROW` items are displayed in a single row,  * `B_ITEMS_IN_COLUMN` items are displayed in a single column,  * `B_ITEMS_IN_MATRIX` items are displayed in a custom matrix. |





**Since:** Haiku R1

---

### `BMenuBar()`

```cpp
BMenuBar::BMenuBar(BMessage * archive)
```

Archive constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The message data to construct the menu from. |





**Since:** BeOS R3

---

### `~BMenuBar()`

```cpp
BMenuBar::~BMenuBar()
```

Destructor. 


Also frees the memory used by any attached menus and menu items.



**Since:** BeOS R3

---

### `AllAttached()`

```cpp
virtual void BMenuBar::AllAttached()
```

Similar to [AttachedToWindow()](classBMenuBar.md#a48b3c56f65222c9dc3e5faca5eb80319) but this method is triggered after all child views have already been attached to a window. 



**Since:** BeOS R3


Reimplemented from [BMenu](classBMenu.md#a2540cab39de9a2ed1a3e71e2c8ec52dc).

---

### `AllDetached()`

```cpp
virtual void BMenuBar::AllDetached()
```

Similar to [AttachedToWindow()](classBMenuBar.md#a48b3c56f65222c9dc3e5faca5eb80319) but this method is triggered after all child views have already been detached from a window. 



**Since:** BeOS R3


Reimplemented from [BMenu](classBMenu.md#a40c41c3d2d1a8e23dfad97039615b208).

---

### `Archive()`

```cpp
status_t BMenuBar::Archive(BMessage * data, bool deep = true)const
```

Archives the the [BMenuBar](classBMenuBar.md) object into the *data* message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A pointer to the [BMessage](../application_kit/classBMessage.md) to archive the object into. |
| `deep` | Whether or not to archive attached menu items as well. |





**Returns:** A status code, `B_OK` if everything went well or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object was archived successfully. |
| B_NO_MEMORY | Ran out of memory while archiving the object. |





**Since:** BeOS R3


Reimplemented from [BMenu](classBMenu.md#a71bed24f541bdfb690863118ce3f716b).

---

### `AttachedToWindow()`

```cpp
void BMenuBar::AttachedToWindow()
```

Sets this as the key menubar for the window, lays out the menu items and resizes the menu to fit. 



**See also:** [BWindow::SetKeyMenuBar()](classBWindow.md#aa1e9322c76ffdad1886253171f8a5972)



**Since:** BeOS R3


Reimplemented from [BMenu](classBMenu.md#af38b2e6bf69d918e37bcf1e18711bb37).

---

### `Border()`

```cpp
menu_bar_border BMenuBar::Border()const
```

Returns the currently set border style. 



**See also:** [BMenuBar::SetBorder()](classBMenuBar.md#a3d1f0ec6b4718c089f128bbcb864697d) for details.



**Since:** BeOS R3

---

### `DetachedFromWindow()`

```cpp
virtual void BMenuBar::DetachedFromWindow()
```

Hook method called when the object is detached from a window. 



**Since:** BeOS R3


Reimplemented from [BMenu](classBMenu.md#a51b79eb8595e20234f2fefabf7899e21).

---

### `Draw()`

```cpp
void BMenuBar::Draw(BRect updateRect)
```

Draws the menu bar. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `updateRect` | The area to draw in. |





**Since:** BeOS R3


Reimplemented from [BMenu](classBMenu.md#a239982fa92e2f5a9c2ed0c267b7470b3).

---

### `FrameMoved()`

```cpp
virtual void BMenuBar::FrameMoved(BPoint newPosition)
```

Hook method called when the view is moved. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `newPosition` | The point of the top left corner of the frame that the view has been moved to. |





**Since:** BeOS R3


Reimplemented from [BMenu](classBMenu.md#ab14bf3dc8b6f082f2609094c1f964577).

---

### `FrameResized()`

```cpp
void BMenuBar::FrameResized(float newWidth, float newHeight)
```

Hook method that gets called when the menu bar is resized. 


Redraws the affected borders.


Parameters

| Parameter | Description |
| :--- | :--- |
| `newWidth` | The new width of the view. |
| `newHeight` | The new height of the view. |





**Since:** BeOS R3


Reimplemented from [BMenu](classBMenu.md#ad6d6eac1f12e9456b9db896aee122181).

---

### `GetPreferredSize()`

```cpp
virtual void BMenuBar::GetPreferredSize(float * _width, float * _height)
```

Fill out the preferred width and height of the view into the *_width* and *_height* parameters. 


Derived classes should override this method to set the preferred size of object.


RemarksEither the *_width* or *_height* parameter may be set to `NULL` if you only want to get the other one.
Parameters

| Parameter | Description |
| :--- | :--- |
| `_width` | Pointer to a float to store the width of the view. |
| `_height` | Pointer to a float to store the height of the view. |





**Since:** BeOS R3


Reimplemented from [BMenu](classBMenu.md#af60a7b8ec6f92749fd46ce2e9179dc17).

---

### `GetSupportedSuites()`

```cpp
virtual status_t BMenuBar::GetSupportedSuites(BMessage * data)
```

Reports the suites of messages and specifiers that derived classes understand.  



**Since:** BeOS R3


Reimplemented from [BMenu](classBMenu.md#a2aa0277374bacf3b7644f738bc064637).

---

### `Hide()`

```cpp
virtual void BMenuBar::Hide()
```

Hides the view without removing it from the view hierarchy. 


Calls to [Hide()](classBMenuBar.md#a7dfa53005734435d3b805161e3495e99) and [Show()](classBMenuBar.md#ac0b9dafc30dd338e8f67b26eff7168f0) are cumulative. A visible view becomes hidden once the number of [Hide()](classBMenuBar.md#a7dfa53005734435d3b805161e3495e99) calls exceeds the number of [Show()](classBMenuBar.md#ac0b9dafc30dd338e8f67b26eff7168f0) calls.



**See also:** [Show()](classBMenuBar.md#ac0b9dafc30dd338e8f67b26eff7168f0)



**Since:** BeOS R3


Reimplemented from [BMenu](classBMenu.md#acebb809699f7efa7d72346f2ba0b869f).

---

### `Instantiate()`

```cpp
BArchivable * BMenuBar::Instantiate(BMessage * data)
```

Creates a new [BMenuBar](classBMenuBar.md) object from an *archive* message. 



**Returns:** A newly created [BMenuBar](classBMenuBar.md) object or `NULL` if the message doesn't contain an archived [BMenuBar](classBMenuBar.md).



**Since:** BeOS R3

---

### `MakeFocus()`

```cpp
virtual void BMenuBar::MakeFocus(bool focus = true)
```

Makes the view the current focus view of the window or gives up being the window's focus view. 


The focus view handles selections and KeyDown events when the the attached window is active. There can be only one focus view at a time per window.


When called with *focus* set to `true` this method first calls [MakeFocus()](classBMenuBar.md#a170fbfdd3be7b9bdc750777f31c216c0) on the previously focused view with *focus* set to `false`.


The focus doesn't automatically change when [MouseDown()](classBMenuBar.md#a0aa84693746c1cfe671c48a4dcc654c6) is called so calling [MakeFocus()](classBMenuBar.md#a170fbfdd3be7b9bdc750777f31c216c0) is the only way to make a view the focus view of a window. Classes derived from [BView](classBView.md) that can display the current selection, or that can accept pasted data should call [MakeFocus()](classBMenuBar.md#a170fbfdd3be7b9bdc750777f31c216c0) in their [MouseDown()](classBMenuBar.md#a0aa84693746c1cfe671c48a4dcc654c6) method to update the focus view of the window on click.


If the view isn't attached to a window this method has no effect.


Parameters

| Parameter | Description |
| :--- | :--- |
| `focus` | *true* to set focus, *false* to remove it. |





**Since:** BeOS R3


Reimplemented from [BMenu](classBMenu.md#a1465ef5881a0b85729118534d8ee3a15).

---

### `MaxSize()`

```cpp
virtual BSize BMenuBar::MaxSize()
```

Return the maximum size of the view. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Returns:** The maximum size of the view as a [BSize](classBSize.md).



**See also:** [BAbstractLayout::MaxSize()](classBAbstractLayout.md#ad1ea5d04a5c8028f8295efde7106a66c)



**Since:** Haiku R1


Reimplemented from [BMenu](classBMenu.md#a5f94df489ae102d0e377df3b63d9864a).

---

### `MessageReceived()`

```cpp
virtual void BMenuBar::MessageReceived(BMessage * message)
```

Handles a *message* received by the associated looper. 


Responds to mouse wheel events scrolling the menu if it is too long to fit in the window. Hold `B_SHIFT_KEY` to cause the menu to scroll faster.


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The *message* received by the associated looper. |





**Since:** BeOS R3


Reimplemented from [BMenu](classBMenu.md#aca12e6b863279cc62772ac13ef286d31).

---

### `MinSize()`

```cpp
virtual BSize BMenuBar::MinSize()
```

Return the minimum size of the view. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Returns:** The minimum size of the view as a [BSize](classBSize.md).



**See also:** [BAbstractLayout::MinSize()](classBAbstractLayout.md#a3f692cb3306ce726e3cc6d2771824cd5)



**Since:** Haiku R1


Reimplemented from [BMenu](classBMenu.md#a659643414ede82d0233e62ce9da4c01e).

---

### `MouseDown()`

```cpp
void BMenuBar::MouseDown(BPoint where)
```

Hook method that is called when a mouse button is pressed. 


Right clicking on a menu bar sends the window to back or brings it to front.


Parameters

| Parameter | Description |
| :--- | :--- |
| `where` | The point on the screen where the mouse pointer is when the mouse button is pressed. |





**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a5f5bd975d15df94f2ebbc80eb79cc3f6).

---

### `MouseUp()`

```cpp
virtual void BMenuBar::MouseUp(BPoint where)
```

Hook method called when a mouse button is released. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `where` | The point on the screen where the mouse pointer is when the mouse button is released. |





> [!NOTE]
> Calling [GetMouse()](classBView.md#a830ce9cf2ac2ffb5f73f526ee5d6e53d) in [MouseUp()](classBMenuBar.md#a4781bbe6cd7ccff992b0c12f2c4ea4b7) will return the new state of the mouse buttons (after the mouse button was released). If you want to know which button was released, you have to compare that with the previous state of the buttons, that you can memorize for example by calling [GetMouse()](classBView.md#a830ce9cf2ac2ffb5f73f526ee5d6e53d) in [MouseDown()](classBMenuBar.md#a0aa84693746c1cfe671c48a4dcc654c6).



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#acdb92b30069157b2e3c522a3ef9d6ae4).

---

### `Perform()`

```cpp
virtual status_t BMenuBar::Perform(perform_code code, void * _data)
```

Perform some action. (Internal Method) 


This method is available to allow classes to be extended while maintaining binary compatibility.


The following perform codes are recognized:


* `PERFORM_CODE_MIN_SIZE:`

* `PERFORM_CODE_MAX_SIZE:`

* `PERFORM_CODE_PREFERRED_SIZE:`

* `PERFORM_CODE_LAYOUT_ALIGNMENT:`

* `PERFORM_CODE_HAS_HEIGHT_FOR_WIDTH:`

* `PERFORM_CODE_GET_HEIGHT_FOR_WIDTH:`

* `PERFORM_CODE_SET_LAYOUT:`

* `PERFORM_CODE_INVALIDATE_LAYOUT:`

* `PERFORM_CODE_DO_LAYOUT:`

* `PERFORM_CODE_GET_TOOL_TIP_AT:`

* `PERFORM_CODE_ALL_UNARCHIVED:`

* `PERFORM_CODE_ALL_ARCHIVED:`



Parameters

| Parameter | Description |
| :--- | :--- |
| `code` | The perform code. |
| `_data` | A pointer to store some data. |





**Returns:** A status code.



**Since:** Haiku R1


Reimplemented from [BMenu](classBMenu.md#a6dedb98c6ba5ffbc44893ff43785c93c).

---

### `PreferredSize()`

```cpp
virtual BSize BMenuBar::PreferredSize()
```

Return the preferred size of the view. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Returns:** The preferred size of the view as a [BSize](classBSize.md).



**See also:** [BAbstractLayout::PreferredSize()](classBAbstractLayout.md#af5f21d9900c85ca053dba3938bef3fd3)



**Since:** Haiku R1


Reimplemented from [BMenu](classBMenu.md#a03aad94d2eb22836823045530e58c052).

---

### `ResizeToPreferred()`

```cpp
virtual void BMenuBar::ResizeToPreferred()
```

Resizes the view to its preferred size keeping the position of the left top corner constant. 



> [!WARNING]
> It is not recommended to use this method for views that are part of a [BLayout](classBLayout.md).



**Since:** BeOS R3


Reimplemented from [BMenu](classBMenu.md#a90a8228da7623e8e991a2fc7dc0e8898).

---

### `ResolveSpecifier()`

```cpp
virtual BHandler * BMenuBar::ResolveSpecifier(BMessage * message, int32 index, BMessage * specifier, int32 what, const char * property)
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


Reimplemented from [BMenu](classBMenu.md#adfd2e1d211f34a8ac748abb989adac48).

---

### `SetBorder()`

```cpp
void BMenuBar::SetBorder(menu_bar_border border)
```

Specifies how the menu bar border is drawn. 


The default is `B_BORDER_FRAME`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `border` | Options include: * `B_BORDER_FRAME` The border is drawn around the entire menu bar.  * `B_BORDER_CONTENTS` The border is drawn around the list of items.  * `B_BORDER_EACH_ITEM` The border is drawn around each individual item. |





**Since:** BeOS R3

---

### `Show()`

```cpp
virtual void BMenuBar::Show()
```

Shows the view making it visible. 


Calls to [Hide()](classBMenuBar.md#a7dfa53005734435d3b805161e3495e99) and [Show()](classBMenuBar.md#ac0b9dafc30dd338e8f67b26eff7168f0) are cumulative. A hidden view becomes visible again once the number of [Show()](classBMenuBar.md#ac0b9dafc30dd338e8f67b26eff7168f0) calls matches the number of [Hide()](classBMenuBar.md#a7dfa53005734435d3b805161e3495e99) calls.



**See also:** [Hide()](classBMenuBar.md#a7dfa53005734435d3b805161e3495e99)



**Since:** BeOS R3


Reimplemented from [BMenu](classBMenu.md#a880d9a96919d389e03106e978709bf9b).

---

### `WindowActivated()`

```cpp
virtual void BMenuBar::WindowActivated(bool active)
```

Hook method called when the attached window is activated or deactivated. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `active` | `true` when the window becomes activated, `false` when the window becomes deactivated. |





**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a5b7aeff0b2608ec63e2c01153a7717f6).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMenuBar.html).
