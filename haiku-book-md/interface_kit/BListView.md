---
name: BListView
type: class
kit: interface_kit
brief: "Displays a list of items that the user can select and invoke"
source: haiku-book
---

# BListView Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Displays a list of items that the user can select and invoke. 


[BListView](classBListView.md)'s can be one of two types set by the type parameter of the constructor:


* `B_SINGLE_SELECTION_LIST` Can select only one item in the list at a time. This is the default.

* `B_MULTIPLE_SELECTION_LIST` Can select any number of items by holding down Option for a discontinuous selection, or Shift for a contiguous selection.



An example of a [BListView](classBListView.md) looks like this: 




Click on an item to select it and double-click an item to invoke it. The [BListView](classBListView.md) doesn't define what it means to "invoke" an item. See [BListView::SetSelectionMessage()](classBListView.md#a5a89c2ca0da9111bf1e701d30235d597) and [BListView::SetInvocationMessage()](classBListView.md#abe78c4cf6c7fc1327f9eee1822080b45) to set a message to be set when these actions occur. You can also select and invoke items with keyboard keys such as the up and down arrow keys, Page Up and Page Down and the Enter key or Space key to invoke the item.


This class is based on the [BList](../support_kit/classBList.md) class from the Support Kit and many of the methods it uses behave similarly.


Although a [BListView](classBListView.md) is scrollable, it doesn't provide scroll bars by itself. You should add the [BListView](classBListView.md) as a child of a [BScrollView](classBScrollView.md) to make it scrollable.


The code to add a [BListView](classBListView.md) to a [BScrollView](classBScrollView.md) looks something like this:



```cpp
BListView* list = new BListView(frame, "List", B_SINGLE_SELECTION_LIST);
list->AddItem(new BStringItem("Item 1"));
list->AddItem(new BStringItem("Item 2"));
...
view->AddChild(new BScrollView("scroll_view", list,
 B_FOLLOW_LEFT | B_FOLLOW_TOP, 0, false, true));
```


**See also:** [BScrollView](classBScrollView.md) for more information on scrolling views.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BListView](#a7964733899af60778e474bfa98537c59) (BMessage *data) — Creates a BListView object from the archive message.
* [BListView](#a031bdcf6c1cb2bada476fe687b0bff5e) (BRect frame, const char *name, list_view_type type=B_SINGLE_SELECTION_LIST, uint32 resizeMask=B_FOLLOW_LEFT_TOP, uint32 flags=B_WILL_DRAW|B_FRAME_EVENTS|B_NAVIGABLE) — Creates a new list view. This is the non-layout constructor.
* [BListView](#a4ee70b28a29582516f70b2bf6ca0662c) (const char *name, list_view_type type=B_SINGLE_SELECTION_LIST, uint32 flags=B_WILL_DRAW|B_FRAME_EVENTS|B_NAVIGABLE) — Creates a new list view suitable as part of a layout with the specified name, type, and flags.
* [BListView](#a8e583dfd6d0cf8bcada0a431197e099d) (list_view_type type=B_SINGLE_SELECTION_LIST) — Creates a new list view suitable as part of a layout.
* `virtual` [~BListView](#a09090d56eae5eee0aca5073e2894efcf) () — Delete the BListView object and free the memory used by it.
* `virtual status_t` [GetSupportedSuites](#acc1fa37e73b342b27d16e13aa3d3024a) (BMessage *data) — Reports the suites of messages and specifiers that derived classes understand.
* `void` [InvalidateItem](#a2a9ee597042919a945526410d7547b3e) (int32 index) — Draws the list item at the specified index.
* `virtual status_t` [Invoke](#a88701bff61aeb58857ca33a5a8920e40) (BMessage *message=NULL) — Invoke the list view, either with the current invocation message or message if it is specified.
* `BRect` [ItemFrame](#abfc3d7aeaa14051912e1a1a14b994980) (int32 index) — Return the frame of the item at the specified index.
* `virtual void` [MakeFocus](#a35117bf3eb7d1f64b777d5371558c626) (bool state=true) — Highlight or unhighlight the selection when the list view acquires or loses its focus state.
* `bool` [MoveItem](#aa09faf9fa92d9cece2879e95d0f61bda) (int32 from, int32 to) — Move the item at index from to the position in the list at index to.
* `virtual status_t` [Perform](#aa0afeb194104738a01c7e60195fe50d0) (perform_code code, void *arg) — Performs an action give a perform_code and data. (Internal Method)
* `bool` [ReplaceItem](#ab3529031a7c4c01fa945e34d3f0c8169) (int32 index, BListItem *item) — Replace the item at index index with item.
* `virtual BHandler *` [ResolveSpecifier](#a2c6144558d144fd5b134021de4c01183) (BMessage *message, int32 index, BMessage *specifier, int32 what, const char *property) — Determines the proper handler for the passed in scripting message.
* `virtual void` [SetFont](#a7b0bd589bd4b1fb410b6e007fe107c62) (const BFont *font, uint32 mask=B_FONT_ALL) — Sets the font of the list view to font with the font parameters set by mask.
* `void` [SortItems](#ade1ff7c4334923ca43c6e768399a99e8) (int(*cmp)(const void *, const void *)) — Sort the items according the the passed in cmp function.
* `bool` [SwapItems](#a5c7798d8a0846377de740ca7e53fd343) (int32 a, int32 b) — Swap item a with item b.
* `virtual void` [Draw](#a7c284b74a68c3f15e7266ac7bca65d24) (BRect updateRect) — Hook method called to draw the contents of the text view.
* `virtual void` [AttachedToWindow](#a172497b23a2c4ab6da666363ad51d90e) () — Hook method called when the list view is added to the view hierarchy.
* `virtual void` [DetachedFromWindow](#a06439547091d244eec75cdb9b078d5ac) () — Hook method that is called when the list view is removed from the view hierarchy.
* `virtual void` [AllAttached](#ae916566577d7d1b310d00861b26ef651) () — Hook method called once all views are attached to the view.
* `virtual void` [AllDetached](#a5f97a604910fbf576aa1acde9e4b8f36) () — Hook method called once all views are detached from the view.
* `virtual void` [FrameResized](#af4fdd5e524c68a7aa318179c8a5acadd) (float newWidth, float newHeight) — Hook method called when the list view is resized.
* `virtual void` [FrameMoved](#aeed214d88c70fa121e1531a6c2cb9ba3) (BPoint newPosition) — Hook method called when the list view is moved.
* `virtual void` [TargetedByScrollView](#a453b373c9bd616f11a1bb195fb05bfbb) (BScrollView *view) — Hook method called when the list view is attached to a BScrollView.
* `virtual void` [WindowActivated](#a85153f43edc12ca463f981b92e187a11) (bool active) — Hook method that is called when the window becomes the active window or gives up that status.
* `virtual void` [MessageReceived](#ac00efce3ca37ce6e89c3f3fb5717311c) (BMessage *message) — Hook method called when a message is received by the list view.
* `virtual void` [KeyDown](#aed97ff09a629d740b91c8f72dcf5893a) (const char *bytes, int32 numBytes) — Hook method that is called when a key is pressed while the view is the focus view of the active window.
* `virtual void` [MouseDown](#aad39bfe4a5db5d70a8adbf1c41b8edf3) (BPoint where) — Hook method that is called when a mouse button is pushed down while the cursor is contained in the view.
* `virtual void` [MouseUp](#a008356d002e19a7b3f2633e4298b4053) (BPoint where) — Hook method that is called when a mouse button is released while the cursor is contained in the view.
* `virtual void` [MouseMoved](#aa83292db971a1bf0801d9669052c2b78) (BPoint where, uint32 code, const BMessage *dragMessage) — Hook method that is called whenever the mouse cursor enters, exits or moves inside the list view.
* `virtual void` [SelectionChanged](#aef207f651fbaeed044a389e3a1ece909) () — Hook method that is called when the selection changes.
* `virtual bool` [InitiateDrag](#aa59a023c30bb60920167495c9c9edfbf) (BPoint where, int32 index, bool wasSelected) — Hook method called when a drag and drop operation is initiated.
* `virtual void` [ResizeToPreferred](#aec8ab9ba29dffb6b14bfbc9530c88fbf) () — Resize the view to its preferred size.
* `virtual void` [GetPreferredSize](#af763f7195c72abd00143441bef002b25) (float *_width, float *_height) — Fill out the _width and _height parameters with the preferred width and height of the list view.
* `virtual BSize` [MinSize](#acd2a6419c6ccad9f8ea52e1c728b1b9b) () — Returns the minimum size of the list view.
* `virtual BSize` [MaxSize](#a54878f820deb4ccc692f49bd6e8ce5c0) () — Returns the maximum size of the list view.
* `virtual BSize` [PreferredSize](#aa353bb8e9a5d229141134df2fa3eddaf) () — Returns the preferred size of the list view.
* `virtual void` [ScrollTo](#a13605eb8e35d09d2795281e541aa5784) (BPoint where) — Scroll the view to the specified point.
* `void` [ScrollTo](#a04483ca67dbf75746977ab35eaf6ae09) (int32 index) — Scrolls to list item at index.
* `void` [ScrollToSelection](#a5a9efdb7c020e1a8048672812053e039) () — Scrolls to selected list item.
* `virtual bool` [AddItem](#a9c9daecdbf5b692e9d11660dc030af32) (BListItem *item, int32 atIndex) — Add an item to the list view at the specified index.
* `virtual bool` [AddList](#ad5a44bb1cc57a998d20e86d7bbc69f16) (BList *newItems) — Add a list of list items to the end of the list view.
* `virtual bool` [AddList](#a60e412803bdc9e8fc3f887519429064d) (BList *newItems, int32 atIndex) — Add a list of list items to the list view at the specified index.
* `virtual bool` [RemoveItem](#a7d78918da16893b4bec59a49cc24c3be) (BListItem *item) — Remove the specified list item.
* `virtual BListItem *` [RemoveItem](#a992402e7c2395376739b2129669aca57) (int32 index) — Remove the item at index from the list.
* `virtual bool` [RemoveItems](#af9ca954568e6397f02ebe13cd0eaafaf) (int32 index, int32 count) — Removes the items from index and the next count items.
* `virtual void` [SetSelectionMessage](#a5a89c2ca0da9111bf1e701d30235d597) (BMessage *message) — Sets the message that the list view sends when a new item is selected.
* `virtual void` [SetInvocationMessage](#abe78c4cf6c7fc1327f9eee1822080b45) (BMessage *message)
* `BMessage *` [SelectionMessage](#acfea321631c35ff7d6608f5038213b58) () const — Returns the message that is send when an item is selected.
* `uint32` [SelectionCommand](#af9230fcb15b3dc47dbf5757146df90c9) () const — Returns the what parameter of the message that is send when an item is selected.
* `BMessage *` [InvocationMessage](#a7eb35fca0ac1421ba172ea7436ec5f91) () const — Returns the message that is send when an item is invoked.
* `uint32` [InvocationCommand](#a15bf860ae1edbcf092e29ecd1a42f412) () const — Returns the what parameter of the current invocation method.
* `virtual void` [SetListType](#a001b324eb67c6646cd6058ecab0b8bfa) (list_view_type type) — Sets the list view type.
* `list_view_type` [ListType](#acfc235c5ec1d0a8662547e31042438f2) () const — Returns the current list view type.
* `BListItem *` [ItemAt](#abe632df2c2af3f94ff2eb13e5523b0ba) (int32 index) const — Returns the list item at the specified index.
* `int32` [IndexOf](#ab355cbfae34bdf8b97f4ce0c17fc93f7) (BPoint point) const — Returns the index of the item at the specified point.
* `int32` [IndexOf](#a8bf217aa8eb31b198b4131902a661bbc) (BListItem *item) const — Returns the index of the specified item.
* `BListItem *` [FirstItem](#a406ad1af19a84fcd6411f0b774e64ca4) () const — Returns a pointer to the first list item.
* `BListItem *` [LastItem](#ae5d3f9a69caba47be72d746fda76136d) () const — Returns a pointer to the last list item.
* `bool` [HasItem](#af05bfde78ba0e06666861ad8c931f512) (BListItem *item) const — Returns whether or not the list contains the specified item.
* `int32` [CountItems](#ad75347c236ecc4ddd46083e587f5f459) () const — Returns the number of items contained in the list view.
* `virtual void` [MakeEmpty](#a1b799b3004e142a491102a24a13b87b6) () — Empties the list view of all items.
* `bool` [IsEmpty](#aac64c30b47d51da3185f1fafa1955784) () const — Returns whether or not the list view is empty.
* `void` [DoForEach](#a9a0978cc612ab6c7ce9efdabd3e37283) (bool(*func)(BListItem *item)) — Calls the specified function on each item in the list.
* `void` [DoForEach](#a3f520bde0f5691d3c5714c7edefc25b3) (bool(*func)(BListItem *item, void *arg), void *arg) — Calls the specified function on each item in the list.
* `const BListItem **` [Items](#a6f9d113b935a8f5e998900be26758274) () const — Returns a pointer to the list of list items.
* `void` [Select](#aeeaff97dee9421ff4b7b01b89fec93c2) (int32 index, bool extend=false) — Selects the list item at the specified index.
* `void` [Select](#a459712f3015aed95a20008b847e7d225) (int32 from, int32 to, bool extend=false) — Select items from start to finish.
* `bool` [IsItemSelected](#abeaac6128e12908bd7ec9e170a37d161) (int32 index) const — Returns whether or not the item at index is selected.
* `int32` [CurrentSelection](#a6958f442fcd00dd19643e29ac29a46f3) (int32 index=0) const — Returns the index in the list of the index'th selected item.
* `void` [DeselectAll](#aeb2925448e33f555b15c151c87be4197) () — Deselect all items.
* `void` [DeselectExcept](#a61fd9e835431a93334e243585ec4faaa) (int32 exceptFrom, int32 exceptTo) — Deselect all items except the items with index in the range of exceptFrom to exceptTo.
* `void` [Deselect](#aae58b02f2bda70f7173e8234955397aa) (int32 index) — Deselect the item at index.
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
* `virtual void` [KeyUp](#acbc528bb70be49993bd99aa136dbb089) (const char *bytes, int32 numBytes) — Hook method called when a keyboard key is released.
* `virtual void` [Pulse](#a0ae8ec3e94ee3d41cb329e3df6966566) () — Hook method called when the view receives a B_PULSE message.
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
* [BInvoker](#ad03149db91cd6460f12adb72780a7080) () — Initializes a BInvoker without a message or target.
* [BInvoker](#adaf9b3df1b4a318e10df04a5eb9f59ee) (BMessage *message, BMessenger target) — Initializes the BInvoker with message and sets the target messenger where the message is sent when Invoke() is called.
* [BInvoker](#a6405334f1589c7a9fc3604ff8a4c8c83) (BMessage *message, const BHandler *handler, const BLooper *looper=NULL) — Initializes the BInvoker with message and sets the target to either a local handler or as the preferred handler of a local looper where the message is sent when Invoke() is called.
* `virtual` [~BInvoker](#a68714c3b78a2cf2931daf54f5dc94dca) () — Destructor method, deletes the BMessage object if set.
* `uint32` [Command](#a6eb323ab957a5ee99e8db2b2fb0e9800) () const — Returns the message's what data member.
* `BHandler *` [HandlerForReply](#a710e78abc03eb29e9e25d11d34c874cc) () const — Returns the previously set reply handler or NULL if not set.
* `virtual status_t` [Invoke](#ad4eb9ad4b3b8286f2a155ad7f087511c) (BMessage *message=NULL) — Sends the message to the invoker's target.
* `status_t` [InvokeNotify](#ab009fe9c6a1f64798c614612e8c3db20) (BMessage *message, uint32 kind=B_CONTROL_INVOKED) — Sends the message to its target, using the notification code specified by kind.
* `bool` [IsTargetLocal](#a17470932a103267815f01d0df9e891e9) () const — Returns whether or not the invoker and its target belong to the same team.
* `BMessage *` [Message](#ab0b73729de282c93b4da51e6b9dbc170) () const — Returns a pointer to the invoker's message object.
* `BMessenger` [Messenger](#aac0992846032f0caaed3d968cd9a1fca) () const — Returns the BMessenger object that the invoker uses to send its messages.
* `virtual status_t` [SetHandlerForReply](#a9983897bef828eea70f574f9571b8e85) (BHandler *handler) — Sets the BHandler object responsible for handling reply messages.
* `virtual status_t` [SetMessage](#a42fae8f984af3765c1a6af404dc36816) (BMessage *message) — Assigns message to the invoker, deleting any previously assigned message.
* `virtual status_t` [SetTarget](#a17e8040bfd829b6b084c2f6234776e11) (BMessenger messenger) — Sets the invoker's target to messenger.
* `virtual status_t` [SetTarget](#ac857ceb882d95a5826447dc12dd06c74) (const BHandler *handler, const BLooper *looper=NULL) — Sets the target to either a local handler or as the preferred handler of a local looper.
* `status_t` [SetTimeout](#ab3c4f55b01f3775832871944b5c943de) (bigtime_t timeout) — Sets the timeout to use when sending the message to the target.
* `BHandler *` [Target](#aba5a469f2e0c94c08553ebe59c238cc8) (BLooper **_looper=NULL) const — Invoke BMessenger::Target() on the internal messenger.
* `bigtime_t` [Timeout](#af2632aee4882b11ed1bc34ce55ef4bbe) () const — Returns the current timeout value.

### Protected Member Functions

* `virtual bool` [DoMiscellaneous](#afa476fbe7cb2db7dc3ebfff29c456408) (MiscCode code, MiscData *data) — Do a miscellaneous action.
* `virtual void` [LayoutInvalidated](#a0a552cc0d8678939c619f98dcc80d254) (bool descendants=false) — Hook method called when the layout is invalidated.
* `virtual void` [LayoutChanged](#ada521f848e4c800cd02eb4fe529e7ea0) () — Hook function that is called when the layout if this view, or one of its children, has changed.
* `status_t` [ScrollWithMouseWheelDelta](#a54991372110199183fed775598ae1912) (BScrollBar *, float) — Handle the scroll wheel changing over scrollbars.
* `virtual void` [DoLayout](#a9d766a06d0885200c6ababba4c87808b) () — Layout view within the layout context.
* `virtual bool` [GetToolTipAt](#afb826fe9b8964e4d843cae190170badf) (BPoint point, BToolTip **_tip) — Point _tip with the view's tool tip.
* `void` [BeginInvokeNotify](#ada272cb8671448d7f7efd607791f31a7) (uint32 kind=B_CONTROL_INVOKED) — Implement this method to set up an InvokeNotify() context.
* `void` [EndInvokeNotify](#a2169cfbba1c3da1921baa9a550581b54) () — Implement this method to tear down an InvokeNotify() context.
* `uint32` [InvokeKind](#a6e33e81c7ee307621295e8da6181d3f8) (bool *_notify=NULL) — Returns the kind set by InvokeNotify().

### Archiving

* `virtual status_t` [Archive](#a89277e72296cc9ec516777e000f100e3) (BMessage *data, bool deep=true) const — Archive the BListView object to a message.
* `static BArchivable *` [Instantiate](#aab88c58cf141c90e6e7fa020f9e07a0b) (BMessage *data) — Create a new BListView object from the message archive.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#a730a46bedfe8db2176e4c331330e7924) (BMessage *archive) — Creates a new BView object from the data message.
* `static BArchivable *` [Instantiate](#a0c23aeb48d578525f81ba6d47f968528) (BMessage *data) — Static method to instantiate a handler from an archived message.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BListView()`

```cpp
BListView::BListView(BRect frame, const char * name, list_view_type type = B_SINGLE_SELECTION_LIST, uint32 resizingMode = B_FOLLOW_LEFT_TOP, uint32 flags = B_WILL_DRAW | B_FRAME_EVENTS | B_NAVIGABLE)
```

Creates a new list view. This is the non-layout constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `frame` | The frame rectangle of the view. |
| `name` | The name of the view. |
| `type` | Whether the list view supports a single selection or multiple selections. |
| `resizingMode` | The resizing mode flags. See [BView](classBView.md) for details. |
| `flags` | The view flags. See [BView](classBView.md) for details. |





**Since:** BeOS R3

---

### `BListView()`

```cpp
BListView::BListView(const char * name, list_view_type type = B_SINGLE_SELECTION_LIST, uint32 flags = B_WILL_DRAW | B_FRAME_EVENTS | B_NAVIGABLE)
```

Creates a new list view suitable as part of a layout with the specified *name*, *type*, and *flags*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the view. |
| `type` | Whether the list view supports a single selection or multiple selections. |
| `flags` | The view flags. See [BView](classBView.md) for details. |





**Since:** Haiku R1

---

### `BListView()`

```cpp
BListView::BListView(list_view_type type = B_SINGLE_SELECTION_LIST)
```

Creates a new list view suitable as part of a layout. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | Whether the list view supports a single selection or multiple selections. |





**Since:** Haiku R1

---

### `BListView()`

```cpp
BListView::BListView(BMessage * archive)
```

Creates a [BListView](classBListView.md) object from the *archive* message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The message to create the object from. |





**Since:** BeOS R3

---

### `~BListView()`

```cpp
BListView::~BListView()
```

Delete the [BListView](classBListView.md) object and free the memory used by it. 


This method does not free the attached list items.



**Since:** BeOS R3

---

### `AddItem()`

```cpp
bool BListView::AddItem(BListItem * item, int32 index)
```

Add an *item* to the list view at the specified *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The list item to add. |
| `index` | The *index* of where to add the list item, if not specified the item is added to the end. |





**Returns:** `true` if the list item was added, `false` otherwise.



**Since:** BeOS R3


Reimplemented in [BOutlineListView](classBOutlineListView.md#a165c59487327a445c7a44eca1107c9dc).

---

### `AddList()`

```cpp
bool BListView::AddList(BList * list)
```

Add a *list* of list items to the end of the list view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `list` | The *list* of list items to add. |





**Returns:** `true` if the *list* was added, `false` otherwise.



**Since:** BeOS R3


Reimplemented in [BOutlineListView](classBOutlineListView.md#afb86c17efba9d7e4a00e228e00eda1dc).

---

### `AddList()`

```cpp
bool BListView::AddList(BList * list, int32 index)
```

Add a *list* of list items to the list view at the specified *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `list` | The *list* of list items to add. |
| `index` | The *index* of where to add the list, if not specified the *list* is added to the end. |





**Returns:** `true` if the *list* was added, `false` otherwise.



**Since:** BeOS R3


Reimplemented in [BOutlineListView](classBOutlineListView.md#a827688c8e95af1a8e9a02f3f873d9df5).

---

### `AllAttached()`

```cpp
void BListView::AllAttached()
```

Hook method called once all views are attached to the view. 



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a6d6379e0993bd525f2cac5f848718870).


Reimplemented in [BOutlineListView](classBOutlineListView.md#a991cfdba0dd36ccebc812c10ced9f4a0).

---

### `AllDetached()`

```cpp
void BListView::AllDetached()
```

Hook method called once all views are detached from the view. 



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a19dd2213f4b953b54524d7f523d9b406).


Reimplemented in [BOutlineListView](classBOutlineListView.md#a677488c290fcd8c263472840e06ea2b2).

---

### `Archive()`

```cpp
status_t BListView::Archive(BMessage * data, bool deep = true)const
```

Archive the [BListView](classBListView.md) object to a message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A pointer to the [BMessage](../application_kit/classBMessage.md) object to archive the object into. |
| `deep` | Whether or not to archive child views as well. |





**Returns:** A status code, `B_OK` if everything went well or an error code otherwise.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The object was archived successfully. |
| B_NO_MEMORY | Ran out of memory while archiving the object. |





**Since:** BeOS R3


Reimplemented from [BView](classBView.md#ab6de1b48cbc3ef15a0d02113036f002d).


Reimplemented in [BOutlineListView](classBOutlineListView.md#af590f60f193f47989f63c34dda0e6916).

---

### `AttachedToWindow()`

```cpp
void BListView::AttachedToWindow()
```

Hook method called when the list view is added to the view hierarchy. 



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#ae8117cb4634f4a4413988eea07cf75a0).

---

### `CountItems()`

```cpp
int32 BListView::CountItems()const
```

Returns the number of items contained in the list view. 



**Returns:** The number of items.



**Since:** BeOS R3

---

### `CurrentSelection()`

```cpp
int32 BListView::CurrentSelection(int32 index = 0)const
```

Returns the index in the list of the *index'th* selected item. 


A negative value is returned when there are not enough selected items.


For example, a list containing the sorted letters of the English alphabet with the vowels selected would return the following values:



| *index* | value |
| :--- | :--- |
| 0 | 0 (the list index of 'A') |
| 1 | 4 (the list index of 'E') |
| 2 | 8 (the list index of 'I') |
| 3 | 14 (the list index of 'O') |
| 4 | 20 (the list index of 'U') |
| 5 | -1 (no more items are selected) |


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The *index* in the selection set of the item to get. |





**Since:** BeOS R3

---

### `Deselect()`

```cpp
void BListView::Deselect(int32 index)
```

Deselect the item at *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The *index* of the item to deselect. |





**Since:** BeOS R3

---

### `DeselectAll()`

```cpp
void BListView::DeselectAll()
```

Deselect all items. 



**Since:** BeOS R3

---

### `DeselectExcept()`

```cpp
void BListView::DeselectExcept(int32 exceptFrom, int32 exceptTo)
```

Deselect all items except the items with index in the range of *exceptFrom* to *exceptTo*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `exceptFrom` | The index of the start of the exception list. |
| `exceptTo` | The index of the end of the exception list. |





**Since:** BeOS R3

---

### `DetachedFromWindow()`

```cpp
void BListView::DetachedFromWindow()
```

Hook method that is called when the list view is removed from the view hierarchy. 



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a8abc2ea500951a0a22cf018e958ba791).


Reimplemented in [BOutlineListView](classBOutlineListView.md#a7c71e9e2a55689bc05d63ef4c7a7cfde).

---

### `DoForEach()`

```cpp
void BListView::DoForEach(bool(*)(BListItem *item)func)
```

Calls the specified function on each item in the list. 


The *func* is called on the items in order starting with the item at index 0 and ending at the last item in the list. This method stops calling the *func* once it returns *true* or the end of the list is reached.


The first argument of *func* is a pointer to the list item.


Parameters

| Parameter | Description |
| :--- | :--- |
| `func` | The function to call on each item. |





**Since:** BeOS R3

---

### `DoForEach()`

```cpp
void BListView::DoForEach(bool(*)(BListItem *item, void *arg)func, void * arg)
```

Calls the specified function on each item in the list. 


The *func* is called on the items in order starting with the item at index 0 and ending at the last item in the list. This method stops calling the *func* once it returns *true* or the end of the list is reached.


The first argument of *func* is a pointer to the list item, *arg* is passed in as the second argument.


Parameters

| Parameter | Description |
| :--- | :--- |
| `func` | The function to call on each item. |
| `arg` | The second argument of the function. |





**Since:** BeOS R3

---

### `DoMiscellaneous()`

```cpp
bool BListView::DoMiscellaneous(MiscCode code, MiscData * data)
```

Do a miscellaneous action. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `code` | The action *code* to use. * `B_NO_OP:` Do nothing  * `B_REPLACE_OP:` Replace the item in *data*  * `B_MOVE_OP:` Move the item in *data*.  * `B_SWAP_OP:` Swap the items in *data*. |
| `data` | The *data* to act on. |





**Since:** Haiku R1


Reimplemented in [BOutlineListView](classBOutlineListView.md#ace0aa3336427b9eb2930925bed1f8d80).

---

### `Draw()`

```cpp
void BListView::Draw(BRect updateRect)
```

Hook method called to draw the contents of the text view. 


You should not have to call this method directly, use [Invalidate()](classBView.md#adfced0dcb244e199f872fdbd48349a05) instead.


Parameters

| Parameter | Description |
| :--- | :--- |
| `updateRect` | The rectangular area to draw. |





**See also:** [BView::Draw()](classBView.md#aa55014241fc2f5556415850692b52db2)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#aa55014241fc2f5556415850692b52db2).

---

### `FirstItem()`

```cpp
BListItem * BListView::FirstItem()const
```

Returns a pointer to the first list item. 



**Returns:** A pointer to the first item in the list or `NULL` if there are no items.



**Since:** BeOS R3

---

### `FrameMoved()`

```cpp
void BListView::FrameMoved(BPoint newPosition)
```

Hook method called when the list view is moved. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `newPosition` | The point of the top left corner of the frame that the view has been moved to. |





**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a551c22b45301e13a3ba959eece3cec7f).


Reimplemented in [BOutlineListView](classBOutlineListView.md#ab061fa01aa2099c3373b80861d0b34ba).

---

### `FrameResized()`

```cpp
void BListView::FrameResized(float newWidth, float newHeight)
```

Hook method called when the list view is resized. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `newWidth` | The new width of the view. |
| `newHeight` | The new height of the view. |





**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a85d88f9c2bb6800560874b2061378fa0).


Reimplemented in [BOutlineListView](classBOutlineListView.md#af22b2e83a0298300f46e33c1319ca151).

---

### `GetPreferredSize()`

```cpp
void BListView::GetPreferredSize(float * _width, float * _height)
```

Fill out the *_width* and *_height* parameters with the preferred width and height of the list view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `_width` | The list view's preferred width is written to *_width*. |
| `_height` | The list view's preferred height is written to *_height*. |





**See also:** [BView::GetPreferredSize()](classBView.md#a089c3ff794c454388a9388c7b6568478)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a089c3ff794c454388a9388c7b6568478).


Reimplemented in [BOutlineListView](classBOutlineListView.md#aa1b8b9ab01b3eb04a6e0fc1cd50833e4).

---

### `GetSupportedSuites()`

```cpp
status_t BListView::GetSupportedSuites(BMessage * data)
```

Reports the suites of messages and specifiers that derived classes understand. 


Reports the suites of messages and specifiers that derived classes understand.  



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a772462d751d457f63ee0fc56d8ba02d1).


Reimplemented in [BOutlineListView](classBOutlineListView.md#a293dd0ed9a59c56ddd2738981c6c48b6).

---

### `HasItem()`

```cpp
bool BListView::HasItem(BListItem * item)const
```

Returns whether or not the list contains the specified *item*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The list item to check. |





**Returns:** `true` if *item* is in the list, `false` otherwise.



**Since:** BeOS R3

---

### `IndexOf()`

```cpp
int32 BListView::IndexOf(BListItem * item)const
```

Returns the index of the specified *item*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The list item to get the index of. |





**Returns:** The index of the specified *item*.



**Since:** BeOS R3

---

### `IndexOf()`

```cpp
int32 BListView::IndexOf(BPoint point)const
```

Returns the index of the item at the specified *point*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The location of the list item to get the index of. |





**Returns:** The index of the list item at the specified *point*.



**Since:** BeOS R3

---

### `InitiateDrag()`

```cpp
bool BListView::InitiateDrag(BPoint point, int32 index, bool wasSelected)
```

Hook method called when a drag and drop operation is initiated. 


This method is used by derived classes to implement drag and drop. This method is called by the [MouseDown()](classBListView.md#aad39bfe4a5db5d70a8adbf1c41b8edf3) method. If the derived class initiates the drag & drop operation you should return `true`, otherwise return `false`. By default this method returns `false`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | Where the drag & drop operation started. |
| `index` |  |
| `wasSelected` | Indicates whether or not the item was selected. |





**Returns:** `true` if a drag & drop operation was initiated, `false` otherwise.



**Since:** BeOS R3

---

### `Instantiate()`

```cpp
BArchivable * BListView::Instantiate(BMessage * archive)
```

Create a new [BListView](classBListView.md) object from the message *archive*. 



**Returns:** A newly created [BView](classBView.md) object or `NULL` if the message doesn't contain an archived [BView](classBView.md).



**Since:** BeOS R3

---

### `InvalidateItem()`

```cpp
void BListView::InvalidateItem(int32 index)
```

Draws the list item at the specified *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The *index* of the list item to draw. |





**Since:** Haiku R1

---

### `InvocationCommand()`

```cpp
uint32 BListView::InvocationCommand()const
```

Returns the what parameter of the current invocation method. 



**Returns:** The what parameter of the currently set invocation method.



**See also:** [BInvoker::Command()](../application_kit/classBInvoker.md#a6eb323ab957a5ee99e8db2b2fb0e9800)



**Since:** BeOS R3

---

### `InvocationMessage()`

```cpp
BMessage * BListView::InvocationMessage()const
```

Returns the message that is send when an item is invoked. 



**Returns:** The current invocation method as a [BMessage](../application_kit/classBMessage.md).



**See also:** [BInvoker::Message()](../application_kit/classBInvoker.md#ab0b73729de282c93b4da51e6b9dbc170)



**Since:** BeOS R3

---

### `Invoke()`

```cpp
status_t BListView::Invoke(BMessage * message = NULL)
```

Invoke the list view, either with the current invocation message or *message* if it is specified. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The message to send or `NULL` to send the current invocation message. |





**See also:** [BControl::Invoke()](classBControl.md#afa04e938d3c42b1de43baa48edb8fd3e)



**Since:** BeOS R3


Reimplemented from [BInvoker](../application_kit/classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c).

---

### `IsEmpty()`

```cpp
bool BListView::IsEmpty()const
```

Returns whether or not the list view is empty. 



**Returns:** `true` if the list view is empty, `false` otherwise.



**Since:** BeOS R3

---

### `IsItemSelected()`

```cpp
bool BListView::IsItemSelected(int32 index)const
```

Returns whether or not the item at *index* is selected. 



**Returns:** `true` if the item was selected, `false` otherwise.



**Since:** BeOS R3

---

### `ItemAt()`

```cpp
BListItem * BListView::ItemAt(int32 index)const
```

Returns the list item at the specified *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` |  |





**Returns:** The list item at the specified *index*.



**Since:** BeOS R3

---

### `ItemFrame()`

```cpp
BRect BListView::ItemFrame(int32 index)
```

Return the frame of the item at the specified *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The *index* of the item to get the frame of. |





**Returns:** The frame of the item at *index*.



**Since:** BeOS R3

---

### `Items()`

```cpp
const BListItem ** BListView::Items()const
```

Returns a pointer to the list of list items. 



**Returns:** a pointer to the list of list items.



**Since:** BeOS R3

---

### `KeyDown()`

```cpp
void BListView::KeyDown(const char * bytes, int32 numBytes)
```

Hook method that is called when a key is pressed while the view is the focus view of the active window. 


The following keys are used by the list view by default:


* Up Arrow Selects the previous item.

* Down Arrow Selects the next item.

* Page Up Selects the item one view height above the current item.

* Page Down Selects the item one view height below the current item.

* Home Selects the first item in the list.

* End Select the last item in the list.

* Enter and Spacebar Invokes the currently selected item.



Parameters

| Parameter | Description |
| :--- | :--- |
| `bytes` | The *bytes* representing the keys pushed down. |
| `numBytes` | The size of *bytes*. |





**See also:** [BView::KeyDown()](classBView.md#abea50ea665ce5fcb76b32f1302a6852d)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#abea50ea665ce5fcb76b32f1302a6852d).


Reimplemented in [BOutlineListView](classBOutlineListView.md#a93a3143a1e783bf5a945bfc6b58e021f).

---

### `LastItem()`

```cpp
BListItem * BListView::LastItem()const
```

Returns a pointer to the last list item. 



**Returns:** A pointer to the last item in the list or `NULL` if there are no items.



**Since:** BeOS R3

---

### `ListType()`

```cpp
list_view_type BListView::ListType()const
```

Returns the current list view type. 



**Returns:** The list view type.



**Since:** BeOS R3

---

### `MakeEmpty()`

```cpp
void BListView::MakeEmpty()
```

Empties the list view of all items. 



**Since:** BeOS R3


Reimplemented in [BOutlineListView](classBOutlineListView.md#aa632085a0d8e60a727d9b701f1c4a72b).

---

### `MakeFocus()`

```cpp
void BListView::MakeFocus(bool focused = true)
```

Highlight or unhighlight the selection when the list view acquires or loses its focus state. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `focused` | `true` to receive focus or `false` to lose it. |





**See also:** [BView::MakeFocus()](classBView.md#a266a368d81c6e1668b2b9b22b5016853)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a266a368d81c6e1668b2b9b22b5016853).


Reimplemented in [BOutlineListView](classBOutlineListView.md#acf402ab948510cbe880b2e24c72f39f9).

---

### `MaxSize()`

```cpp
BSize BListView::MaxSize()
```

Returns the maximum size of the list view. 



**Returns:** The maximum size of the list view as a [BSize](classBSize.md).



**See also:** [BView::MaxSize()](classBView.md#ad1f1843a380e850948cf7e4ed2d5f1ba)



**Since:** Haiku R1


Reimplemented from [BView](classBView.md#ad1f1843a380e850948cf7e4ed2d5f1ba).

---

### `MessageReceived()`

```cpp
void BListView::MessageReceived(BMessage * message)
```

Hook method called when a message is received by the list view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The *message* received by the associated looper. |





**See also:** [BHandler::MessageReceived()](../application_kit/classBHandler.md#aeecda5017e0081db617f23bbff71fb53)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#aca0a16b0e04288e1fdc0b63690ea7a6d).


Reimplemented in [BOutlineListView](classBOutlineListView.md#aad47f3bf68a98024413aa06a45b0bdad).

---

### `MinSize()`

```cpp
BSize BListView::MinSize()
```

Returns the minimum size of the list view. 



**Returns:** The minimum size of the list view as a [BSize](classBSize.md).



**See also:** [BView::MinSize()](classBView.md#acfb0cffde35b853dab6bc5d1bb03265f)



**Since:** Haiku R1


Reimplemented from [BView](classBView.md#acfb0cffde35b853dab6bc5d1bb03265f).

---

### `MouseDown()`

```cpp
void BListView::MouseDown(BPoint point)
```

Hook method that is called when a mouse button is pushed down while the cursor is contained in the view. 


By default this method selects items on a single click, and invokes them on a double click. This method calls [InitiateDrag()](classBListView.md#aa59a023c30bb60920167495c9c9edfbf) to allow derived classes the opportunity to drag and drop items from the list.


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The *point* where the mouse button was pushed down. |





**See also:** [BView::MouseDown()](classBView.md#a5f5bd975d15df94f2ebbc80eb79cc3f6)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a5f5bd975d15df94f2ebbc80eb79cc3f6).


Reimplemented in [BOutlineListView](classBOutlineListView.md#ae974e26e01f4f31a2b7eb64d91f1a22b).

---

### `MouseMoved()`

```cpp
void BListView::MouseMoved(BPoint where, uint32 code, const BMessage * dragMessage)
```

Hook method that is called whenever the mouse cursor enters, exits or moves inside the list view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `where` | The point where the mouse cursor has moved to. |
| `code` | A code which indicating if the mouse entered or exited the view. |
| `dragMessage` | A message containing drag and drop information. |





**See also:** [BView::MouseMoved()](classBView.md#ac8b20516e42bab2f1eeb130e2432bde0)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#ac8b20516e42bab2f1eeb130e2432bde0).

---

### `MouseUp()`

```cpp
void BListView::MouseUp(BPoint where)
```

Hook method that is called when a mouse button is released while the cursor is contained in the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `where` | The location that the mouse button was released. |





**See also:** [BView::MouseUp()](classBView.md#acdb92b30069157b2e3c522a3ef9d6ae4)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#acdb92b30069157b2e3c522a3ef9d6ae4).


Reimplemented in [BOutlineListView](classBOutlineListView.md#a65d774552d88ba39b6c4bb5bcccb048a).

---

### `MoveItem()`

```cpp
bool BListView::MoveItem(int32 from, int32 to)
```

Move the item at index *from* to the position in the list at index *to*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `from` | The index of the item to move. |
| `to` | The index to move the item to. |





**Returns:** `true` if the item was moved, `false` otherwise.



**Since:** BeOS R3

---

### `Perform()`

```cpp
status_t BListView::Perform(perform_code code, void * _data)
```

Performs an action give a perform_code and data. (Internal Method) 


Reimplemented from [BView](classBView.md#a512a6c8dca1a62b14cdcb1c22070129b).


Reimplemented in [BOutlineListView](classBOutlineListView.md#acb2775731d5da2cf52995e4d0b75c1d6).

---

### `PreferredSize()`

```cpp
BSize BListView::PreferredSize()
```

Returns the preferred size of the list view. 



**Returns:** The preferred size of the list view as a [BSize](classBSize.md).



**See also:** [BView::PreferredSize()](classBView.md#a7f51d63e71b60a2721d04436ffbcfe36)



**Since:** Haiku R1


Reimplemented from [BView](classBView.md#a7f51d63e71b60a2721d04436ffbcfe36).

---

### `RemoveItem()`

```cpp
bool BListView::RemoveItem(BListItem * item)
```

Remove the specified list item. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `item` | The list item to remove. |





**Returns:** `true` if the *item* was removed, `false` otherwise.



**Since:** BeOS R3


Reimplemented in [BOutlineListView](classBOutlineListView.md#a09f458b8e48041518527cf2a72fa424d).

---

### `RemoveItem()`

```cpp
BListItem * BListView::RemoveItem(int32 index)
```

Remove the item at *index* from the list. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The *index* of the item to remove. |





**Returns:** `true` if the item was removed, `false` otherwise.



**Since:** BeOS R3


Reimplemented in [BOutlineListView](classBOutlineListView.md#a3e8dfd8556b9789e46be2920fe365e38).

---

### `RemoveItems()`

```cpp
bool BListView::RemoveItems(int32 index, int32 count)
```

Removes the items from *index* and the next *count* items. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The location to start removing items from. |
| `count` | The number of items past *index* to remove. |




return `true` if the *items* were removed, `false` otherwise.



**Since:** BeOS R3


Reimplemented in [BOutlineListView](classBOutlineListView.md#a2fc47d713bc4a5a5be6a9304581ee2b6).

---

### `ReplaceItem()`

```cpp
bool BListView::ReplaceItem(int32 index, BListItem * item)
```

Replace the item at index *index* with *item*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The *index* of the item to replace. |
| `item` | The *item* to replace the item at *index* with. |





**Returns:** `true` if the item was replaced, `false` otherwise.



**Since:** BeOS R3

---

### `ResizeToPreferred()`

```cpp
void BListView::ResizeToPreferred()
```

Resize the view to its preferred size. 



**See also:** [BView::ResizeToPreferred()](classBView.md#abe8c63c85555e800e063388e7cf3e1a7)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#abe8c63c85555e800e063388e7cf3e1a7).


Reimplemented in [BOutlineListView](classBOutlineListView.md#a053c8871392cc82965ad42bb0302399c).

---

### `ResolveSpecifier()`

```cpp
BHandler * BListView::ResolveSpecifier(BMessage * message, int32 index, BMessage * specifier, int32 what, const char * property)
```

Determines the proper handler for the passed in scripting *message*. 


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


Reimplemented from [BView](classBView.md#a4c0c6d3b21ae92056e5e40fe4d3ec175).


Reimplemented in [BOutlineListView](classBOutlineListView.md#a835a18d28691bdc9daad7cf0598e8a5f).

---

### `ScrollTo()`

```cpp
void BListView::ScrollTo(BPoint point)
```

Scroll the view to the specified *point*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The location to scroll the list view to. |





**See also:** [BView::ScrollTo()](classBView.md#a33ed2a9eeff474a756b548996a82b964)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a2b76ddc60289ce92e1fb706332edbafc).

---

### `ScrollTo()`

```cpp
void BListView::ScrollTo(int32 index)
```

Scrolls to list item at *index*. 


If above top scroll to first item, if below bottom scroll to last item otherwise scroll to item at *index*.



**See also:** [IndexOf()](classBListView.md#ab355cbfae34bdf8b97f4ce0c17fc93f7), [MouseMoved()](classBListView.md#aa83292db971a1bf0801d9669052c2b78), [ScrollToSelection()](classBListView.md#a5a9efdb7c020e1a8048672812053e039)



**Since:** Haiku R1

---

### `ScrollToSelection()`

```cpp
void BListView::ScrollToSelection()
```

Scrolls to selected list item. 



**Since:** BeOS R3

---

### `Select()`

```cpp
void BListView::Select(int32 start, int32 finish, bool extend = false)
```

Select items from *start* to *finish*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `start` | The index of the item to start the selection. |
| `finish` | The index of the item to end the selection. |
| `extend` | Whether or not to also select child items. |





**Since:** BeOS R3

---

### `Select()`

```cpp
void BListView::Select(int32 index, bool extend = false)
```

Selects the list item at the specified *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The *index* of the item to select. |
| `extend` | Whether or not to also select child items. |





**Since:** BeOS R3

---

### `SelectionChanged()`

```cpp
void BListView::SelectionChanged()
```

Hook method that is called when the selection changes. 


This method should be implemented by derived classes, the default implementation does nothing.



**Since:** BeOS R3

---

### `SelectionCommand()`

```cpp
uint32 BListView::SelectionCommand()const
```

Returns the what parameter of the message that is send when an item is selected. 



**Returns:** The what parameter of the current selection message.



**Since:** BeOS R3

---

### `SelectionMessage()`

```cpp
BMessage * BListView::SelectionMessage()const
```

Returns the message that is send when an item is selected. 



**Returns:** The current selection message as a [BMessage](../application_kit/classBMessage.md).



**Since:** BeOS R3

---

### `SetFont()`

```cpp
void BListView::SetFont(const BFont * font, uint32 mask = B_FONT_ALL)
```

Sets the font of the list view to *font* with the font parameters set by *mask*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `font` | The *font* to set the list view to. |
| `mask` | A *mask* indicating which properties of *font* to set. |





**See also:** [BView::SetFont()](classBView.md#a9247127c151153542a3e6bc1f3904433)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a9247127c151153542a3e6bc1f3904433).

---

### `SetInvocationMessage()`

```cpp
void BListView::SetInvocationMessage(BMessage * message)
```

Sets the *message* that the list view sends when an item is invoked.


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The invocation *message* to set. |





**See also:** [BInvoker::SetMessage()](../application_kit/classBInvoker.md#a42fae8f984af3765c1a6af404dc36816)



**Since:** BeOS R3

---

### `SetListType()`

```cpp
void BListView::SetListType(list_view_type type)
```

Sets the list view *type*. 



**Since:** BeOS R3


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The list view *type* to set. |

---

### `SetSelectionMessage()`

```cpp
void BListView::SetSelectionMessage(BMessage * message)
```

Sets the *message* that the list view sends when a new item is selected. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The selection *message* to set. |





**Since:** BeOS R3

---

### `SortItems()`

```cpp
void BListView::SortItems(int(*)(const void *, const void *)cmp)
```

Sort the items according the the passed in *cmp* function. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `cmp` | The compare function to use to sort the items. |





**Since:** BeOS R3

---

### `SwapItems()`

```cpp
bool BListView::SwapItems(int32 a, int32 b)
```

Swap item *a* with item *b*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `a` | The index of the first item to swap. |
| `b` | The index of the second item to swap. |





**Returns:** `true` if the items were swapped, `false` otherwise.



**Since:** BeOS R3

---

### `TargetedByScrollView()`

```cpp
void BListView::TargetedByScrollView(BScrollView * view)
```

Hook method called when the list view is attached to a [BScrollView](classBScrollView.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `view` | The [BScrollView](classBScrollView.md) the list view is attached to. |





**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a668a4ed5419c86a7f2696ca7ece28df7).

---

### `WindowActivated()`

```cpp
void BListView::WindowActivated(bool active)
```

Hook method that is called when the window becomes the active window or gives up that status. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `active` | `true` when the window becomes activated, `false` when the window becomes deactivated. |





**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a5b7aeff0b2608ec63e2c01153a7717f6).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBListView.html).
