---
name: BControl
type: class
kit: interface_kit
brief: "BControl is the base class for user-event handling objects"
source: haiku-book
---

# BControl Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

[BControl](classBControl.md) is the base class for user-event handling objects. 


[BControl](classBControl.md) is a pseudo-abstract class that adds four main attributes to a [BView](classBView.md). It adds [IsEnabled()](classBControl.md#a179de32505328b72911cd85bf2c3cfe8) and [SetEnabled()](classBControl.md#a54529bfa2d272ef17f1b790d27c7ff17) methods, adds [Value()](classBControl.md#a759e9aebe200495c3773d2920e19e91f) and [SetValue()](classBControl.md#a7841a122e7fa9ab5efb5217c562e763d), it is a [BInvoker](../application_kit/classBInvoker.md) with [Invoke()](classBControl.md#afa04e938d3c42b1de43baa48edb8fd3e) and [Message()](../application_kit/classBInvoker.md#ab0b73729de282c93b4da51e6b9dbc170) methods and it adds [SetIcon()](classBControl.md#acf788aa66dd061c78256f357df691765), [SetIconBitmap()](classBControl.md#a1017ff0cf130fa1246291a016b2a7f2b), and [IconBitmap()](classBControl.md#a186746c30c79d2645fb94301ef05dfff). A basic implementation is included, you are expected to add to it in your subclass. Call [BControl::Invoke()](classBControl.md#afa04e938d3c42b1de43baa48edb8fd3e) to add default message constants.


Simple controls such as [BCheckBox](classBCheckBox.md) and [BButton](classBButton.md) deviate only a bit from [BControl](classBControl.md), whereas more complicated controls such as [BColorControl](classBColorControl.md) and BSlider reimplement much more functionality. Whether you are building a simple control or something more complicated you should inherit from [BControl](classBControl.md) as it provides a common set of methods for intercepting received messages from mouse and keyboard events.


Controls have state which they keep in their value. The value of a control, stored as an `int32`, is read and set by the virtual [Value()](classBControl.md#a759e9aebe200495c3773d2920e19e91f) and [SetValue()](classBControl.md#a7841a122e7fa9ab5efb5217c562e763d) methods. [BControl](classBControl.md) defines `B_CONTROL_ON` and `B_CONTROL_OFF` values that you can use as a convenience if your control has a simple on/off state. If your [BControl](classBControl.md) derived class stores a larger set of states then you should define your own integer values instead.


You are expected to set colors on your [BControl](classBControl.md) implementation class. Use control colors on the inside of your [BControl](classBControl.md) subclass where appropriate. By default parent colors are used on the outside for example if you include a label next to your control it would typically go on panel colors. Button-like controls should use only control colors.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BControl](#ae2bd77f0349ca0197b7599393a6ae3ca) (BRect frame, const char *name, const char *label, BMessage *message, uint32 resizingMode, uint32 flags) — Construct a control in the frame with a name, label, model message, resizingMode, and creation flags.
* [BControl](#a6243ab82eecb7ac3a5c35592a057845d) (const char *name, const char *label, BMessage *message, uint32 flags) — Construct a control with a name, label, model message, and creation flags suitable for use with the Layout API.
* `virtual` [~BControl](#a82c073b898fb760954b80ada2c731962) () — Frees all memory used by the BControl object including the memory used by the model message.
* `virtual void` [AllAttached](#a2abeec720f873da7c4bc3a2709ff8be0) () — Similar to AttachedToWindow() but this method is triggered after all child views have already been detached from a window.
* `virtual void` [AllDetached](#a991c0eecd0279cbc27c5f9a0fbc37920) () — Similar to AttachedToWindow() but this method is triggered after all child views have already been detached from a window.
* `virtual void` [AttachedToWindow](#a460fa93bcdd5309d8d86f8bfcd53b584) () — Hook method called when the control is attached to a window.
* `virtual void` [DetachedFromWindow](#a588fea0ded4cdc4c1b4fb5d1f5565f27) () — Hook method called when the control is detached from a window.
* `virtual void` [GetPreferredSize](#a22455c705a4ed0fd09908b36a8dda3ae) (float *_width, float *_height) — Fill out the preferred width and height of the control into the _width and _height parameters.
* `virtual status_t` [GetSupportedSuites](#a3b545ffe2ee04f62eaa567582225adba) (BMessage *message) — Report the suites of messages this control understands.
* `const BBitmap *` [IconBitmap](#a186746c30c79d2645fb94301ef05dfff) (uint32 which) const — Get the currently set bitmap for a specific state.
* `virtual status_t` [Invoke](#afa04e938d3c42b1de43baa48edb8fd3e) (BMessage *message=NULL) — Sends a copy of the model message to the designated target.
* `bool` [IsEnabled](#a179de32505328b72911cd85bf2c3cfe8) () const — Gets whether or not the control is currently enabled.
* `virtual void` [KeyDown](#ade80a87b7da08e9b84b188c629ec36c8) (const char *bytes, int32 numBytes) — Hook method called when a keyboard key is pressed.
* `const char *` [Label](#a0c345befac88d6af592ce2b3e7d7214e) () const — Gets the label of the control.
* `virtual void` [MakeFocus](#aaeeae39969b598868ad0e8d3298efb00) (bool focus=true) — Gives or removes focus from the control.
* `virtual void` [MessageReceived](#a19960b4d0a96144f73065a6ea1f2f8e2) (BMessage *message) — Handle message received by the associated looper.
* `virtual void` [MouseDown](#aae264c07bf8006acf1fa96ceedc5f74d) (BPoint where) — Hook method called when a mouse button is pressed.
* `virtual void` [MouseMoved](#aafa3507bfcf6f058d269a6e3bd6d30be) (BPoint where, uint32 code, const BMessage *dragMessage) — Hook method called when the mouse is moved.
* `virtual void` [MouseUp](#aeef31f13aee4d5d0b3dbb0f7e12beb39) (BPoint where) — Hook method called when a mouse button is released.
* `virtual status_t` [Perform](#a0b32524cd2abfb7ea37b9988b180c733) (perform_code d, void *arg)
* `virtual void` [ResizeToPreferred](#ad25f5ce6f17b5fe6fd6347021e9222e4) () — Resize the control to its preferred size.
* `virtual BHandler *` [ResolveSpecifier](#a084be37bbc0c49627c42a078c4b4dac8) (BMessage *message, int32 index, BMessage *specifier, int32 what, const char *property)
* `virtual void` [SetEnabled](#a54529bfa2d272ef17f1b790d27c7ff17) (bool enabled) — Enables or disables the control.
* `virtual status_t` [SetIcon](#acf788aa66dd061c78256f357df691765) (const BBitmap *bitmap, uint32 flags=0) — This convenience method is used to set the bitmaps for the standard states from a single bitmap.
* `status_t` [SetIconBitmap](#a1017ff0cf130fa1246291a016b2a7f2b) (const BBitmap *bitmap, uint32 which, uint32 flags=0) — Icon bitmaps for various states of the control (off, on, partially on, each enabled or disabled, plus up to 125 custom states) can be set individually.
* `virtual void` [SetLabel](#a2894bf781c41b3ab8a99417f098e71dc) (const char *string) — Sets the label of the control.
* `virtual void` [SetValue](#a7841a122e7fa9ab5efb5217c562e763d) (int32 value) — Sets the value of the control.
* `int32` [Value](#a759e9aebe200495c3773d2920e19e91f) () const — Gets the value of the control.
* `virtual void` [WindowActivated](#ab665fb93df191662a1757f78555a5b21) (bool active) — Hook method called when the attached window is activated or deactivated.
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
* `virtual void` [Draw](#aa55014241fc2f5556415850692b52db2) (BRect updateRect) — Draws the area of the view that intersects updateRect.
* `virtual void` [KeyUp](#acbc528bb70be49993bd99aa136dbb089) (const char *bytes, int32 numBytes) — Hook method called when a keyboard key is released.
* `virtual void` [Pulse](#a0ae8ec3e94ee3d41cb329e3df6966566) () — Hook method called when the view receives a B_PULSE message.
* `virtual void` [FrameMoved](#a551c22b45301e13a3ba959eece3cec7f) (BPoint newPosition) — Hook method called when the view is moved.
* `virtual void` [FrameResized](#a85d88f9c2bb6800560874b2061378fa0) (float newWidth, float newHeight) — Hook method called when the view is resized.
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
* `virtual BSize` [MinSize](#acfb0cffde35b853dab6bc5d1bb03265f) () — Return the minimum size of the view.
* `virtual BSize` [MaxSize](#ad1f1843a380e850948cf7e4ed2d5f1ba) () — Return the maximum size of the view.
* `virtual BSize` [PreferredSize](#a7f51d63e71b60a2721d04436ffbcfe36) () — Return the preferred size of the view.
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

* `bool` [IsFocusChanging](#aac106958d27f3e56b2d5ddd3eca5117a) () const — Check if the control is changing focus.
* `bool` [IsTracking](#a253dcd4904a221e750c58ce41cea6c8c) () const — Check whether this control is set to tracking.
* `void` [SetTracking](#a28daada6c5a36e5fd8445d1b5580b6c2) (bool state) — Modify the control's tracking state.
* `void` [SetValueNoUpdate](#a367df71f0b9b64905f3acb98cd111cda) (int32 value) — Sets the value of the control without redrawing.
* `virtual void` [LayoutInvalidated](#a0a552cc0d8678939c619f98dcc80d254) (bool descendants=false) — Hook method called when the layout is invalidated.
* `virtual void` [LayoutChanged](#ada521f848e4c800cd02eb4fe529e7ea0) () — Hook function that is called when the layout if this view, or one of its children, has changed.
* `status_t` [ScrollWithMouseWheelDelta](#a54991372110199183fed775598ae1912) (BScrollBar *, float) — Handle the scroll wheel changing over scrollbars.
* `virtual void` [DoLayout](#a9d766a06d0885200c6ababba4c87808b) () — Layout view within the layout context.
* `virtual bool` [GetToolTipAt](#afb826fe9b8964e4d843cae190170badf) (BPoint point, BToolTip **_tip) — Point _tip with the view's tool tip.
* `void` [BeginInvokeNotify](#ada272cb8671448d7f7efd607791f31a7) (uint32 kind=B_CONTROL_INVOKED) — Implement this method to set up an InvokeNotify() context.
* `void` [EndInvokeNotify](#a2169cfbba1c3da1921baa9a550581b54) () — Implement this method to tear down an InvokeNotify() context.
* `uint32` [InvokeKind](#a6e33e81c7ee307621295e8da6181d3f8) (bool *_notify=NULL) — Returns the kind set by InvokeNotify().

### Archiving

* [BControl](#a1224f952eb63f1b0d338720b88fdf220) (BMessage *data) — Creates a new BControl object from an data message.
* `virtual status_t` [Archive](#a2581a447a34eef102c62d0e998155290) (BMessage *data, bool deep=true) const — Archives the control into data.
* `static BArchivable *` [Instantiate](#ad5ba32b4f839a5a9bc60fcf037e23846) (BMessage *data) — Creates a new object from an data.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#a730a46bedfe8db2176e4c331330e7924) (BMessage *archive) — Creates a new BView object from the data message.
* `static BArchivable *` [Instantiate](#a0c23aeb48d578525f81ba6d47f968528) (BMessage *data) — Static method to instantiate a handler from an archived message.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BControl()`

```cpp
BControl::BControl(BRect frame, const char * name, const char * label, BMessage * message, uint32 resizingMode, uint32 flags)
```

Construct a control in the *frame* with a *name*, *label*, model *message*, *resizingMode*, and creation *flags*. 


The initial value of the control is set to 0 (`B_CONTROL_OFF`). The *label* and the *message* parameters can be set to `NULL`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `frame` | The *frame* to draw the control in. |
| `name` | The *name* of the control. |
| `label` | The *label* displayed along with the control. |
| `message` | The *message* to send when the control is activated. |
| `resizingMode` | Defines the behavior of the control as the parent view resizes, see [BView](classBView.md) for more details. |
| `flags` | Behavior *flags* for the control, see [BView](classBView.md) for details. |





**Since:** BeOS R3

---

### `BControl()`

```cpp
BControl::BControl(const char * name, const char * label, BMessage * message, uint32 flags)
```

Construct a control with a *name*, *label*, model *message*, and creation *flags* suitable for use with the Layout API. 


The initial value of the control is set to 0 (`B_CONTROL_OFF`). The *label* and the *message* parameters can be set to `NULL`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The *name* of the control. |
| `label` | The *label* displayed along with the control. |
| `message` | The *message* to send when the control is activated. |
| `flags` | Behavior *flags* for the control, see [BView](classBView.md) for details. |





**Since:** Haiku R1

---

### `~BControl()`

```cpp
BControl::~BControl()
```

Frees all memory used by the [BControl](classBControl.md) object including the memory used by the model message. 



**Since:** BeOS R3

---

### `BControl()`

```cpp
BControl::BControl(BMessage * data)
```

Creates a new [BControl](classBControl.md) object from an *data* message. 


This method is usually not called directly. If you want to build a control from a message you should call [Instantiate()](classBControl.md#ad5ba32b4f839a5a9bc60fcf037e23846) which can handle errors properly.


If the *data* deep, the [BControl](classBControl.md) object will also undata each of its child views recursively.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The *data* message to restore from. |





**Since:** BeOS R3

---

### `AllAttached()`

```cpp
void BControl::AllAttached()
```

Similar to [AttachedToWindow()](classBControl.md#a460fa93bcdd5309d8d86f8bfcd53b584) but this method is triggered after all child views have already been detached from a window. 



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a6d6379e0993bd525f2cac5f848718870).


Reimplemented in [BButton](classBButton.md#a9a888bcbcdcf8a924b6010ef6e7f46a9), [BChannelSlider](classBChannelSlider.md#abfb89e632dec0539147b79e770090b23), [BCheckBox](classBCheckBox.md#a3d555861d9a8ce0be86193cac484f1ac), [BColorControl](classBColorControl.md#a0429d5c2f2a748e50b556e03b60c3f84), [BOptionPopUp](classBOptionPopUp.md#a9fb0e8fefa909b2f7a25d0b2a3ba473e), [BPictureButton](classBPictureButton.md#a1d263b8ec7ccde013c7a462c702052dd), [BRadioButton](classBRadioButton.md#af941f0cf47d024337e30653bc4dcd5d2), and [BTextControl](classBTextControl.md#abae889f35648d9a08f5b997986381c06).

---

### `AllDetached()`

```cpp
void BControl::AllDetached()
```

Similar to [AttachedToWindow()](classBControl.md#a460fa93bcdd5309d8d86f8bfcd53b584) but this method is triggered after all child views have already been detached from a window. 



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a19dd2213f4b953b54524d7f523d9b406).


Reimplemented in [BButton](classBButton.md#a4c8d87c3ceb9b867dae9adc68526cb0b), [BChannelSlider](classBChannelSlider.md#a4339e7bc207a4c3887a4aef63bdff817), [BCheckBox](classBCheckBox.md#aabe966d7094a102a029eb86f53156b52), [BColorControl](classBColorControl.md#a3053cfbbb6aeff2b1fe9852a91fe6364), [BPictureButton](classBPictureButton.md#a699d006ff7d23e3448ee8b23555815c4), [BRadioButton](classBRadioButton.md#aa821c3cb4a2f47e3af2f7bde5b129427), and [BTextControl](classBTextControl.md#ad47ac17bae76e2be8786ec25ebd30b89).

---

### `Archive()`

```cpp
status_t BControl::Archive(BMessage * data, bool deep = true)const
```

Archives the control into *data*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The target *data* that the data will go into. |
| `deep` | Whether or not to recursively data child views. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The data operation was successful. |
| B_BAD_VALUE | `NULL` *data* message. |
| B_ERROR | The archive operation failed. |





**See also:** [BArchivable::Archive()](../support_kit/classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#ab6de1b48cbc3ef15a0d02113036f002d).


Reimplemented in [BPictureButton](classBPictureButton.md#ab476f82e9d75a3b4a9b54ca35d1ad036), [BTextControl](classBTextControl.md#af68449ec551e8a089a441fd270954b99), [BButton](classBButton.md#adce5e4839a58c3bb85965398a490d720), [BChannelControl](classBChannelControl.md#aa71189c8b008cb3329c17b58f786617e), [BCheckBox](classBCheckBox.md#a75511a8252ef3ffa1177f57af97b67ca), [BColorControl](classBColorControl.md#a6437907efd1d39a492db1f55b5f4dc36), [BRadioButton](classBRadioButton.md#aeed1a7a2142b1ac7b1499234f884caae), and [BChannelSlider](classBChannelSlider.md#ac216b412d86275115516b886c4f9b578).

---

### `AttachedToWindow()`

```cpp
void BControl::AttachedToWindow()
```

Hook method called when the control is attached to a window. 


This method overrides [BView::AttachedToWindow()](classBView.md#ae8117cb4634f4a4413988eea07cf75a0) setting the low color and view color of the [BControl](classBControl.md) so that it matches the view color of the control's parent view. It also makes the attached window the default target for [Invoke()](classBControl.md#afa04e938d3c42b1de43baa48edb8fd3e) as long as another target has not already been set.



**See also:** [BView::AttachedToWindow()](classBView.md#ae8117cb4634f4a4413988eea07cf75a0)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#ae8117cb4634f4a4413988eea07cf75a0).


Reimplemented in [BButton](classBButton.md#a8514d1d173d5a852f52354107dedce7f), [BChannelControl](classBChannelControl.md#aaed17a427fd040df721062ea646ee360), [BChannelSlider](classBChannelSlider.md#a896559c9ffdf6c29fec0071f7e74326e), [BCheckBox](classBCheckBox.md#a6975f3d06240cfc32d9422163d21760c), [BColorControl](classBColorControl.md#a0a4c898ee218990de45a53a90663d12e), [BOptionPopUp](classBOptionPopUp.md#a5c301cf20c932c72700eea57a427e68d), [BPictureButton](classBPictureButton.md#ae6b51e465aa9807d707316a00b6fe22d), [BRadioButton](classBRadioButton.md#abacc25df48c377cd37ae3cb5eaf3917d), and [BTextControl](classBTextControl.md#ae3adb78b19be6c737882972695c5f84f).

---

### `DetachedFromWindow()`

```cpp
void BControl::DetachedFromWindow()
```

Hook method called when the control is detached from a window. 



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a8abc2ea500951a0a22cf018e958ba791).


Reimplemented in [BButton](classBButton.md#a2324e5b37fa2c3c4e8d2c63763172d12), [BChannelControl](classBChannelControl.md#a2ba05bb52a1d79b9e840c28e08531e98), [BChannelSlider](classBChannelSlider.md#a0e62e869e80944ad32a2c0dc8b813e35), [BCheckBox](classBCheckBox.md#a9d332c16b89814d6255fa7ff96827943), [BColorControl](classBColorControl.md#ae1b42162705172630cf7961d4af876f2), [BPictureButton](classBPictureButton.md#ac5c3a2f7ac5f4876cdc6f74b467b763a), [BRadioButton](classBRadioButton.md#a0c66b7a3964716897d10713a6880bc9c), and [BTextControl](classBTextControl.md#a6a6832d8df544412d84839a1011c6da0).

---

### `GetPreferredSize()`

```cpp
void BControl::GetPreferredSize(float * _width, float * _height)
```

Fill out the preferred width and height of the control into the *_width* and *_height* parameters. 


Derived classes can override this method to set the preferred width and height of the control.


Parameters

| Parameter | Description |
| :--- | :--- |
| `_width` | Pointer to a `float` to hold the width of the control. |
| `_height` | Pointer to a `float` to hold the height of the control. |





**See also:** [BView::GetPreferredSize()](classBView.md#a089c3ff794c454388a9388c7b6568478)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a089c3ff794c454388a9388c7b6568478).


Reimplemented in [BButton](classBButton.md#adba3ed10370f960a0a408413569adf30), [BChannelSlider](classBChannelSlider.md#a0f2838b9bd42bd8454658dbdd78b179b), [BCheckBox](classBCheckBox.md#aff828221de6947696a0b60d73241315c), [BColorControl](classBColorControl.md#a20210c9c80b0bfd88a0e6d5d89da0a64), [BOptionPopUp](classBOptionPopUp.md#ae2fcf40dcd30ba8560ee3f737485fcc5), [BPictureButton](classBPictureButton.md#a2f2dddfafa62ccea5770aab99893dae9), [BRadioButton](classBRadioButton.md#a2129a420a7dfc70b6d9a97b1458764f6), [BTextControl](classBTextControl.md#a9ebbd271bca4c72ba2a5db8dc1876082), and [BChannelControl](classBChannelControl.md#aacccdb670d6553e5204c8ae317f6029a).

---

### `GetSupportedSuites()`

```cpp
status_t BControl::GetSupportedSuites(BMessage * message)
```

Report the suites of messages this control understands. 


Adds the string "suite/vnd.Be-control" to the message.



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a772462d751d457f63ee0fc56d8ba02d1).


Reimplemented in [BChannelControl](classBChannelControl.md#abfb5744f9faf08ed02d22a33ae9e9ab8), [BChannelSlider](classBChannelSlider.md#affd29de4f880e122c72d4d3b25b7ed9d), [BColorControl](classBColorControl.md#a5f10efed53781673b0f5a3f40b7d527d), [BPictureButton](classBPictureButton.md#a08e86268e927d332501bee63892fb2bd), [BTextControl](classBTextControl.md#a9281b5fa852c3fe841bc7f102a96078a), [BButton](classBButton.md#af912fac07ee02f90a12a4011e5a493cb), [BCheckBox](classBCheckBox.md#a6075229f070c3723a0fc102e7984e8f2), and [BRadioButton](classBRadioButton.md#a513f368c4eb7c7d1aa81da79bee492ea).

---

### `IconBitmap()`

```cpp
const BBitmap * BControl::IconBitmap(uint32 which)const
```

Get the currently set bitmap for a specific state. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `which` | The state to retrieve the icon for. |





**Returns:** A pointer to the icon set for the state, or `NULL` in case there is no icon set for that state.



**Since:** Haiku R1

---

### `Instantiate()`

```cpp
BArchivable * BControl::Instantiate(BMessage * data)
```

Creates a new object from an *data*. 


If the message is a valid object then the instance created from the passed in *data* will be returned. Otherwise this method will return `NULL`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | The *data* message. |





**Returns:** An instance of the object if *data* is valid or `NULL`.



**See also:** [BArchivable::Instantiate()](../support_kit/classBArchivable.md#a04efcb17fa2a64a776923cc12303efcd)



**Since:** BeOS R3

---

### `Invoke()`

```cpp
status_t BControl::Invoke(BMessage * message = NULL)
```

Sends a copy of the model *message* to the designated target. 


[BControl::Invoke()](classBControl.md#afa04e938d3c42b1de43baa48edb8fd3e) overrides [BInvoker::Invoke()](../application_kit/classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c). Derived classes should use this method in their [MouseDown()](classBControl.md#aae264c07bf8006acf1fa96ceedc5f74d) and [KeyDown()](classBControl.md#ade80a87b7da08e9b84b188c629ec36c8) methods and should call [IsEnabled()](classBControl.md#a179de32505328b72911cd85bf2c3cfe8) to check if the control is enabled before calling [Invoke()](classBControl.md#afa04e938d3c42b1de43baa48edb8fd3e).


The following fields added to the [BMessage](../application_kit/classBMessage.md):


* "when" `B_INT64_TYPE` system_time()

* "source" `B_POINTER_TYPE` A pointer to the [BControl](classBControl.md) object.



Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The *message* to send. |





**Returns:** `B_OK` if the control was invoked, otherwise an error code is returned.



**See also:** [BInvoker::Invoke()](../application_kit/classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c)



**Since:** BeOS R3


Reimplemented from [BInvoker](../application_kit/classBInvoker.md#ad4eb9ad4b3b8286f2a155ad7f087511c).


Reimplemented in [BButton](classBButton.md#ad9942f380f9e8337147f307972e02a9b), [BChannelControl](classBChannelControl.md#a29dcbf2de885c423dc2981c95b225691), [BCheckBox](classBCheckBox.md#a90978d140f092824dc9aeff535bd8638), [BColorControl](classBColorControl.md#a40cd8db37322ffb2770896ded8ec1600), [BPictureButton](classBPictureButton.md#ad3f58a97ed8348711aff7128ebf0b5dd), [BRadioButton](classBRadioButton.md#ae0aec96932eaa5f1de8591392a739b0b), and [BTextControl](classBTextControl.md#ae82b482d40833e4a2903301839e37f8c).

---

### `IsEnabled()`

```cpp
bool BControl::IsEnabled()const
```

Gets whether or not the control is currently enabled. 



**Returns:** `true` if the control is enabled, `false` if it is disabled.



**Since:** BeOS R3

---

### `IsFocusChanging()`

```cpp
bool BControl::IsFocusChanging()const
```

Check if the control is changing focus. 


Many controls have different looks depending on whether they have focus or not. You can use this method within your [Draw()](classBView.md#aa55014241fc2f5556415850692b52db2) call to determine whether you are asked to redraw because the focus is changing, meaning your control is getting in or out of focus, so that you can conditionally run the drawing code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The [Draw()](classBView.md#aa55014241fc2f5556415850692b52db2) method was called because of a focus change for this control. |
| false | The [Draw()](classBView.md#aa55014241fc2f5556415850692b52db2) method was not called because of a focus change for this control. |





**Since:** BeOS R5

---

### `IsTracking()`

```cpp
bool BControl::IsTracking()const
```

Check whether this control is set to tracking. 


See [SetTracking()](classBControl.md#a28daada6c5a36e5fd8445d1b5580b6c2) for the usage pattern. By default, the control wil return `false`.



**Since:** Haiku R1

---

### `KeyDown()`

```cpp
void BControl::KeyDown(const char * bytes, int32 numBytes)
```

Hook method called when a keyboard key is pressed. 


Overrides [BView::KeyDown()](classBView.md#abea50ea665ce5fcb76b32f1302a6852d) to toggle the control value and then calls [Invoke()](classBControl.md#afa04e938d3c42b1de43baa48edb8fd3e) for `B_SPACE` or `B_ENTER`. If this is not desired you should override this method in derived classes.


The [KeyDown()](classBControl.md#ade80a87b7da08e9b84b188c629ec36c8) method is only called if the [BControl](classBControl.md) is the focus view in the active window. If the window has a default button, `B_ENTER` will be passed to that object instead of the focus view.


Parameters

| Parameter | Description |
| :--- | :--- |
| `bytes` | The bytes of the key combination pressed. |
| `numBytes` | The number of bytes in *bytes*. |





**See also:** [BView::KeyDown()](classBView.md#abea50ea665ce5fcb76b32f1302a6852d)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#abea50ea665ce5fcb76b32f1302a6852d).


Reimplemented in [BButton](classBButton.md#a1946a6658404aef5e374bf37e0d276ad), [BChannelSlider](classBChannelSlider.md#acea7a9db888f42a0a20640efd9ad0a4b), [BCheckBox](classBCheckBox.md#a4b02a354633080c08f03bdf39e1bdec6), [BColorControl](classBColorControl.md#a94675a83e628146d8bb9670064d59242), [BPictureButton](classBPictureButton.md#a0a7cfc055ee00a2435f25138a5bbcd40), [BRadioButton](classBRadioButton.md#a2f39aded0be52643dd5f541f62699d34), and [BChannelControl](classBChannelControl.md#a37ac118342e3d4fe79faa33b88e56813).

---

### `Label()`

```cpp
const char * BControl::Label()const
```

Gets the label of the control. 



**Returns:** The control's label.



**Since:** BeOS R3

---

### `MakeFocus()`

```cpp
void BControl::MakeFocus(bool focus = true)
```

Gives or removes focus from the control. 


[BControl::MakeFocus()](classBControl.md#aaeeae39969b598868ad0e8d3298efb00) overrides [BView::MakeFocus()](classBView.md#a266a368d81c6e1668b2b9b22b5016853) to call [Draw()](classBView.md#aa55014241fc2f5556415850692b52db2) when the focus changes. Derived classes generally don't have to re-implement [MakeFocus()](classBControl.md#aaeeae39969b598868ad0e8d3298efb00).


[IsFocusChanging()](classBControl.md#aac106958d27f3e56b2d5ddd3eca5117a) returns `true` when [Draw()](classBView.md#aa55014241fc2f5556415850692b52db2) is called from this method.


Parameters

| Parameter | Description |
| :--- | :--- |
| `focus` | *true* to set focus, *false* to remove it. |





**See also:** [BView::MakeFocus()](classBView.md#a266a368d81c6e1668b2b9b22b5016853)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a266a368d81c6e1668b2b9b22b5016853).


Reimplemented in [BButton](classBButton.md#abc826951b0a87f2ce4cf6cc10eb792d6), [BPictureButton](classBPictureButton.md#a70245c6a6207a737c74a6092cc2374a6), [BRadioButton](classBRadioButton.md#a1f2f84e388730e3f018e0e16d682bf37), [BTextControl](classBTextControl.md#abf98183ccf195db2a411dc5a1f67ee33), [BCheckBox](classBCheckBox.md#a0b638537dadfd72221c21dbb6fd48a46), [BColorControl](classBColorControl.md#a82b299852c7650b09af6662581cedaae), and [BChannelSlider](classBChannelSlider.md#affd38edbaca04a9db31ef3e749b119e7).

---

### `MessageReceived()`

```cpp
void BControl::MessageReceived(BMessage * message)
```

Handle *message* received by the associated looper. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The *message* received by the associated looper. |





**See also:** [BHandler::MessageReceived()](../application_kit/classBHandler.md#aeecda5017e0081db617f23bbff71fb53)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#aca0a16b0e04288e1fdc0b63690ea7a6d).


Reimplemented in [BButton](classBButton.md#a9954aa8549ffb7cddd1a401997fd07a7), [BChannelControl](classBChannelControl.md#a7c3c5174a2f31f0a24c3fe4258d372da), [BChannelSlider](classBChannelSlider.md#aa60391cfc92b6c1a59ae7e92aa1f5bae), [BCheckBox](classBCheckBox.md#a668832dfbcab06cad06d0fb7d9a6244a), [BColorControl](classBColorControl.md#a9cf939fb5e7ef82a70e0792ccc0cfc1f), [BOptionControl](classBOptionControl.md#a6bff9c89ab78d899edfb88d3f9e2300c), [BOptionPopUp](classBOptionPopUp.md#a05b397e2521fe0b10ae3a2b05e78acae), [BPictureButton](classBPictureButton.md#a7b6a5dc266664f155b6191d101ce48cd), [BRadioButton](classBRadioButton.md#a2f07af2fe9eedce7ffecd2b29a4b5d6a), and [BTextControl](classBTextControl.md#afad72eca02699a6577c4bc0949e1c9ae).

---

### `MouseDown()`

```cpp
void BControl::MouseDown(BPoint where)
```

Hook method called when a mouse button is pressed. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `where` | The point on the screen where the mouse pointer is when the mouse button is pressed. |





**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a5f5bd975d15df94f2ebbc80eb79cc3f6).


Reimplemented in [BButton](classBButton.md#a479d27a48b957709b47159360c04157f), [BChannelSlider](classBChannelSlider.md#a858647630d03d081d3a2817e00f2e548), [BCheckBox](classBCheckBox.md#a641e4f5e6cf5b87302af5feb146969a0), [BColorControl](classBColorControl.md#a45399dd2cd33d8761709ee9e378fab56), [BPictureButton](classBPictureButton.md#aee724ca332fa7a49b2ea2fa5c680f8a4), [BRadioButton](classBRadioButton.md#a0aef53a65bca065d5c23a254fbf87c82), [BTextControl](classBTextControl.md#ab1a5a0a5efb5e08a1ec98432529f02d9), and [BChannelControl](classBChannelControl.md#a00e4315bf31cfe8b0a071cf5766427a8).

---

### `MouseMoved()`

```cpp
void BControl::MouseMoved(BPoint where, uint32 code, const BMessage * dragMessage)
```

Hook method called when the mouse is moved. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `where` | The new location of the mouse in the view's coordinate system. |
| `code` | One of the following: * `B_ENTERED_VIEW` The cursor has just entered the view.  * `B_INSIDE_VIEW` The cursor is inside the view.  * `B_EXITED_VIEW` The cursor has left the view's bounds. This only gets sent if the scope of the mouse events that the view can receive has been expanded by [SetEventMask()](classBView.md#a5d8d6b469a8a11a577d1d138cfc31162) or [SetMouseEventMask()](classBView.md#ae7705783d064a8613dcc6f36a2866ab2).  * `B_OUTSIDE_VIEW` The cursor is outside the view. This only gets sent if the scope of the mouse events that the view can receive has been expanded by [SetEventMask()](classBView.md#a5d8d6b469a8a11a577d1d138cfc31162) or [SetMouseEventMask()](classBView.md#ae7705783d064a8613dcc6f36a2866ab2). |
| `dragMessage` | If a drag-and-drop operation is taking place this is a pointer to a [BMessage](../application_kit/classBMessage.md) that holds the drag information, otherwise the pointer is `NULL`. |





**See also:** [SetEventMask()](classBView.md#a5d8d6b469a8a11a577d1d138cfc31162), [SetMouseEventMask()](classBView.md#ae7705783d064a8613dcc6f36a2866ab2)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#ac8b20516e42bab2f1eeb130e2432bde0).


Reimplemented in [BColorControl](classBColorControl.md#af1aa066eeb6541eaf1c3c72d72758a5d), [BButton](classBButton.md#a8ba8b18062ea15ecd55d83458885adf1), [BCheckBox](classBCheckBox.md#ac18ca09f358bcd8acf7c5c00572ddfd9), [BPictureButton](classBPictureButton.md#af8e6d077c64b703b0e939458508bdd75), [BRadioButton](classBRadioButton.md#a013acca6d097f0b6d889b9f8e32e5064), [BChannelSlider](classBChannelSlider.md#a54f043d454c571fdc1291946c54ff214), and [BTextControl](classBTextControl.md#ae34f333c6ccd0ce7f98fe15a31973536).

---

### `MouseUp()`

```cpp
void BControl::MouseUp(BPoint where)
```

Hook method called when a mouse button is released. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `where` | The point on the screen where the mouse pointer is when the mouse button is released. |





> [!NOTE]
> Calling [GetMouse()](classBView.md#a830ce9cf2ac2ffb5f73f526ee5d6e53d) in [MouseUp()](classBControl.md#aeef31f13aee4d5d0b3dbb0f7e12beb39) will return the new state of the mouse buttons (after the mouse button was released). If you want to know which button was released, you have to compare that with the previous state of the buttons, that you can memorize for example by calling [GetMouse()](classBView.md#a830ce9cf2ac2ffb5f73f526ee5d6e53d) in [MouseDown()](classBControl.md#aae264c07bf8006acf1fa96ceedc5f74d).



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#acdb92b30069157b2e3c522a3ef9d6ae4).


Reimplemented in [BColorControl](classBColorControl.md#a22dc58e1aebc262b91d105ae8db1b779), [BButton](classBButton.md#abdf9eedcccc9bbf8edce48b32361a749), [BChannelSlider](classBChannelSlider.md#a0d9fccc6e4a04d86c1fbf78ae0cb6eba), [BCheckBox](classBCheckBox.md#ae24408c8af1f1e0792564b0bb4109547), [BPictureButton](classBPictureButton.md#a0770c7585a64a6c5cc1a960f2a01569b), [BRadioButton](classBRadioButton.md#a8cfb56dd13ec44c09cf6b2790c155fc2), and [BTextControl](classBTextControl.md#aa9f01c01c01799296e81f3a075890db5).

---

### `Perform()`

```cpp
status_t BControl::Perform(perform_code code, void * _data)
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


Reimplemented from [BView](classBView.md#a512a6c8dca1a62b14cdcb1c22070129b).


Reimplemented in [BCheckBox](classBCheckBox.md#abcac265789890adbf485f42d34d8c8e3), [BPictureButton](classBPictureButton.md#a57e7eef2e379994c13b8c93eeb5cf3c5), [BButton](classBButton.md#aee74330d076b7b8487fe21443118b03d), and [BRadioButton](classBRadioButton.md#a44c726ed88d3a132e9d3055ebf98f3e6).

---

### `ResizeToPreferred()`

```cpp
void BControl::ResizeToPreferred()
```

Resize the control to its preferred size. 



**See also:** [BView::ResizeToPreferred()](classBView.md#abe8c63c85555e800e063388e7cf3e1a7)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#abe8c63c85555e800e063388e7cf3e1a7).


Reimplemented in [BButton](classBButton.md#a6468013205fd98f26440cd63911b9b34), [BChannelControl](classBChannelControl.md#a6df6fe17dedbf19a1d4e868ad24410f6), [BCheckBox](classBCheckBox.md#a0dedbdd99597789621ef09bb4e8f4b2b), [BColorControl](classBColorControl.md#a4c2ba5009024549e36b6d06b68ece03c), [BOptionPopUp](classBOptionPopUp.md#aa2c5587ec3c4202409b19a32b425ea08), [BPictureButton](classBPictureButton.md#ac16a945ef32c4ae9fc066fd066da1242), [BRadioButton](classBRadioButton.md#ab7975b6bd97b13278719aab270ca40de), and [BTextControl](classBTextControl.md#a5072df60c0f2c20d5b1ff4a2dbecbe7b).

---

### `ResolveSpecifier()`

```cpp
BHandler * BControl::ResolveSpecifier(BMessage * message, int32 index, BMessage * specifier, int32 what, const char * property)
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


Reimplemented from [BView](classBView.md#a4c0c6d3b21ae92056e5e40fe4d3ec175).


Reimplemented in [BChannelSlider](classBChannelSlider.md#ab95b5eebb6adcc7502c856789f08b6d2), [BButton](classBButton.md#a16b56f270bcba826cd8a1eb043adb474), [BChannelControl](classBChannelControl.md#af12f883b6e60f2ea071bb18724593350), [BCheckBox](classBCheckBox.md#ae860f1cfc296c79754697d95fc289a9e), [BColorControl](classBColorControl.md#a2bc94c2bffc9dec2b1a844c21833cb93), [BPictureButton](classBPictureButton.md#a8553ac7d4f76b03d53dce14073cb50de), [BRadioButton](classBRadioButton.md#a767171da7c902ec3e06d19951f8b1404), and [BTextControl](classBTextControl.md#a666a6fd256b57c98f9e75b3c19a03a89).

---

### `SetEnabled()`

```cpp
void BControl::SetEnabled(bool enabled)
```

Enables or disables the control. 


[BControl](classBControl.md) objects are enabled by default. If the control changes enabled state then it is redrawn.


Disabled controls generally won't allow the user to focus on them (The `B_NAVIGABLE` flag is turned off), and don't post any messages.


Disabled controls in derived classes should be drawn in subdued colors to visually indicate that they are disabled and should not respond to keyboard or mouse events.


Parameters

| Parameter | Description |
| :--- | :--- |
| `enabled` | If `true` enables the control, if `false`, disables it. |





**Since:** BeOS R3


Reimplemented in [BTextControl](classBTextControl.md#a2cd97358b190f50977b9b4d74c607474), [BOptionPopUp](classBOptionPopUp.md#a7c9182a20b3481e7a4900d655eb4d817), [BChannelSlider](classBChannelSlider.md#a345cf8ee4d0c063df32e8ac21b0eafcf), and [BColorControl](classBColorControl.md#aa34f71fa3963c172c9a71fc5cfb5f191).

---

### `SetIcon()`

```cpp
status_t BControl::SetIcon(const BBitmap * icon, uint32 flags = 0)
```

This convenience method is used to set the bitmaps for the standard states from a single bitmap. 


It also supports cropping the icon to its non-transparent area. The icon is meant as an addition to or replacement of the label.


Parameters

| Parameter | Description |
| :--- | :--- |
| `icon` | The *icon* to set. |
| `flags` | Modify how the icon is set. * `B_TRIM_ICON_BITMAP` Crop the bitmap to the not fully transparent area, may change the icon size.  * `B_TRIM_ICON_BITMAP_KEEP_ASPECT` Like `B_TRIM_BITMAP`, but keeps the aspect ratio.  * `B_CREATE_ACTIVE_ICON_BITMAP`  * `B_CREATE_PARTIALLY_ACTIVE_ICON_BITMAP`  * `B_CREATE_DISABLED_ICON_BITMAPS` |





**Returns:** `B_OK` if the icon was set or an error code otherwise.



**Since:** Haiku R1


Reimplemented in [BButton](classBButton.md#ad167627166b5988a41c90bfa95ece336), [BCheckBox](classBCheckBox.md#a66c449d2c003034e2f9a5767ae9ea0c0), [BColorControl](classBColorControl.md#aef3688503bf82355812f2fbc4be0985a), [BPictureButton](classBPictureButton.md#a477263b77a52c15550436447a25ffd73), [BRadioButton](classBRadioButton.md#a65c54a649a091b163625f43af69ffbb9), and [BTextControl](classBTextControl.md#a025b67f14fb0868be05813b6f72d9c39).

---

### `SetIconBitmap()`

```cpp
status_t BControl::SetIconBitmap(const BBitmap * bitmap, uint32 which, uint32 flags = 0)
```

Icon bitmaps for various states of the control (off, on, partially on, each enabled or disabled, plus up to 125 custom states) can be set individually. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The *bitmap* icon to set. |
| `which` | The state to set the icon for. |
| `flags` | Modify how the icon is set. * `B_KEEP_ICON_BITMAP` Transfer ownership of the bitmap to the control. |





**Returns:** `B_OK` if the icon was set or an error code otherwise.



**Since:** Haiku R1

---

### `SetLabel()`

```cpp
void BControl::SetLabel(const char * label)
```

Sets the *label* of the control. 


If the *label* changes the control is redrawn.


Parameters

| Parameter | Description |
| :--- | :--- |
| `label` | The *label* to set, can be `NULL`. |





**Since:** BeOS R3


Reimplemented in [BButton](classBButton.md#addc58de70c9b2acff2c1e407696f772f), and [BOptionPopUp](classBOptionPopUp.md#ab288fd4c009a1ca297fba4150247a215).

---

### `SetTracking()`

```cpp
void BControl::SetTracking(bool state)
```

Modify the control's tracking state. 


The tracking state is a feature of this [BControl](classBControl.md) class, that allows you to set a flag when you are watching the behavior of users when they interact with your control.


For example, a button may have a draw state when it is not pressed, and when it is pressed. When the user presses their mouse down, within the control, the control will be drawn in the pressed state. The code can set the tracking flag, so that in the case of the mouse up event, the control knows it has to redraw.


This flag does not affect anything within this class, other than the return value of the [IsTracking()](classBControl.md#a253dcd4904a221e750c58ce41cea6c8c) method, so it can be used at will by custom implementations of this class.


Parameters

| Parameter | Description |
| :--- | :--- |
| `state` | Pass `true` if the control is in a tracking state, or `false` if it is not. |





**Since:** Haiku R1

---

### `SetValue()`

```cpp
void BControl::SetValue(int32 value)
```

Sets the value of the control. 


If the *value* changes the control is redrawn.


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The *value* to set. |





**See also:** [SetValueNoUpdate()](classBControl.md#a367df71f0b9b64905f3acb98cd111cda)



**Since:** BeOS R3


Reimplemented in [BColorControl](classBColorControl.md#a7e29f94f4ccdcbcea0e377e61cd720f8), [BButton](classBButton.md#a2944b5facaa051c2e2f20b2f9874b494), [BChannelControl](classBChannelControl.md#a689d5c240ce7cea39f2b9da865ad5627), [BCheckBox](classBCheckBox.md#ab5f2a0687c785b84ccb9c7fea3efbfda), [BOptionPopUp](classBOptionPopUp.md#a7d73205017815c1227487467a7a441ec), [BPictureButton](classBPictureButton.md#a0ee7dd1bc8976d7cb82a6525505789f6), [BRadioButton](classBRadioButton.md#a3c65e4237040ba5d6554882bcf36569d), and [BTextControl](classBTextControl.md#a81e42842670062d0b6add0478d8f52dc).

---

### `SetValueNoUpdate()`

```cpp
void BControl::SetValueNoUpdate(int32 value)
```

Sets the value of the control without redrawing. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The *value* to set. |





**See also:** [SetValue()](classBControl.md#a7841a122e7fa9ab5efb5217c562e763d)



**Since:** Haiku R1

---

### `Value()`

```cpp
int32 BControl::Value()const
```

Gets the value of the control. 



**Returns:** The control's value.



**Since:** BeOS R3

---

### `WindowActivated()`

```cpp
void BControl::WindowActivated(bool active)
```

Hook method called when the attached window is activated or deactivated. 


Redraws the focus ring around the control when the window is activated or deactivated if it is the window's current focus view.


Parameters

| Parameter | Description |
| :--- | :--- |
| `active` | `true` if the window becomes activated, `false` if the window becomes deactivated. |





**See also:** [BView::WindowActivated()](classBView.md#a5b7aeff0b2608ec63e2c01153a7717f6)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a5b7aeff0b2608ec63e2c01153a7717f6).


Reimplemented in [BButton](classBButton.md#ace1f01da01eef93adbecd91ce2d49ac1), [BCheckBox](classBCheckBox.md#af3e0b0e3afc3d2adfb2e3cf0f9bb3b82), [BPictureButton](classBPictureButton.md#a2c1edfc72af90482e70328b152998001), [BRadioButton](classBRadioButton.md#a5f15ba4b79b38cb260b2b95e52c60a83), [BTextControl](classBTextControl.md#a38f83894076d23f426e1e347f7ef933d), [BChannelSlider](classBChannelSlider.md#aa9d3e2bfcd8fbd5901b82960c11484bf), and [BColorControl](classBColorControl.md#acea993086cd5dd46f36e12149017930c).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBControl.html).
