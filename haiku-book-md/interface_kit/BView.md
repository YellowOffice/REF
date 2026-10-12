---
name: BView
type: class
kit: interface_kit
brief: "View base class"
source: haiku-book
---

# BView Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

View base class. 


A [BView](classBView.md) is a rectangular area within a window that responds to mouse clicks and key presses, and acts as a surface for you to draw on.


Most Interface Kit classes, with the notable exception of [BWindow](classBWindow.md) inherit from [BView](classBView.md). Some of the time you might use a [BView](classBView.md) object as is, but most of the time you subclass [BView](classBView.md) to do something unique.


To create a subclass of [BView](classBView.md) you generally override one or more of [BView](classBView.md)'s hook methods to respond to user events such as [MouseDown()](classBView.md#a5f5bd975d15df94f2ebbc80eb79cc3f6) or [FrameMoved()](classBView.md#a551c22b45301e13a3ba959eece3cec7f). By default a [BView](classBView.md) does nothing in its hook methods unless otherwise stated, it's up to you to define what happens. To override the look of a [BView](classBView.md) you should override the [Draw()](classBView.md#aa55014241fc2f5556415850692b52db2) or [DrawAfterChildren()](classBView.md#abb50623b4236926b068fc5a2264f6a48) methods. See the section on Hook Methods below for more details.


When a [BView](classBView.md) object is first created it has no parent or child views. How you add a view to the view hierarchy depends on if you want to use a standard view with a defined frame rectangle or to use the Layout APIs to position and size your view instead.


If you create a standard view you need to add it to a window or another view using the [AddChild()](classBView.md#ab6382c582e5e1be527d3199459d05e8f) method, if you create a layout view you need to add your view to a layout using [BLayout::AddView()](classBLayout.md#a83f286f504a1a735f07304c7647ba7f9) or by adding it to a layout builder.


Views are not very interesting until they, or one of their parents, are attached to a window as many of [BView](classBView.md)'s methods depend on a connection to the App Server to do their work. In order to prevent multiple views from altering the window simultaneously though locking is required. To perform an action while the window is locked you issue the following code:



```cpp
if (Window()->LockLooper()) {
    ...
 Window()->UnlockLooper()
}
```

Whenever App Server calls a hook method it automatically locks the [BWindow](classBWindow.md) for you.


Only one view attached to a window is able to receive keyboard events at a time. The view that is able to receive keyboard events such as [KeyDown()](classBView.md#abea50ea665ce5fcb76b32f1302a6852d) is called the "focus view". [MakeFocus()](classBView.md#a266a368d81c6e1668b2b9b22b5016853) gives or removes focus from a view. Call [IsFocus()](classBView.md#a165719de682845f80735042a499692ff) to determine whether or not the view is the window's current focus view.


When a view has focus an indicator should be drawn to inform the user. Typically the view is surrounded by a blue rectangle to indicate that it is the window's focus view. The color can be queried using the keyboard_navigation_color() function in [InterfaceDefs.h](InterfaceDefs_8h.md)


Each view has its own coordinate system with the origin point (0.0, 0.0) located at the top left corner. You can convert a [BPoint](classBPoint.md) or [BRect](classBRect.md) to or from the view's coordinate system to the coordinate system of its parent, or of the screen's coordinate system. See the section on Coordinate Conversion Methods for more details.


The Application Server clips a [BView](classBView.md) to the region where it's permitted to draw which is never larger than the view's bound rectangle. A view can never draw outside its bounds nor can it draw outside of the bounds rectangle of any parent view.


You may limit the clipping region further by passing a [BRegion](classBRegion.md) object to [ConstrainClippingRegion()](classBView.md#a656b8d82a6a7c7c6ab33c3dd08aad6ec). You can obtain the current clipping region by calling [GetClippingRegion()](classBView.md#acf50a063c9621f35a84b1d0245b12d69).


Each view has a [ViewColor()](classBView.md#a8b2b1d9e08ce0c1763dd6a077ed02fdd) that fills the frame rectangle before the view does any drawing of its own. The default view color is white, you may change the view color by calling [SetViewColor()](classBView.md#ae8dde0e0330b394db016f3e609e7fb6a) or, as of Haiku R1, [SetViewUIColor()](classBView.md#a34f020c4bb1008cef972cf1eec7dba0f). A commonly used view color is `B_PANEL_BACKGROUND_COLOR` which is a user-defined color used as the view color of most applications. If you set the view color to `B_TRANSPARENT_COLOR` then the Application Server won't erase the clipping region of the view before updating, this should only be used if the view erases itself by drawing on every pixel in the clipping region.


If you want to set the view color of a view to be the same as its parent you need to set it within the [AttachedToWindow()](classBView.md#ae8117cb4634f4a4413988eea07cf75a0) method of the view like so:



```cpp
SetViewColor(Parent()->ViewColor());
```


**Since:** BeOS R3

## Member List

### Public Member Functions

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

* `virtual status_t` [Archive](#ab6de1b48cbc3ef15a0d02113036f002d) (BMessage *archive, bool deep=true) const — Archives the object into the data message.
* `static BArchivable *` [Instantiate](#a730a46bedfe8db2176e4c331330e7924) (BMessage *archive) — Creates a new BView object from the data message.

### Hook Methods

* `virtual status_t` [AllUnarchived](#ab7bd04272afed8b28bf57d1de33cbe05) (const BMessage *archive) — Hook method called when all views have been unarchived.
* `virtual status_t` [AllArchived](#a561e82ed41cbb93d3bacf371787497bf) (BMessage *archive) const — Hook method called when all views have been archived.
* `virtual void` [AttachedToWindow](#ae8117cb4634f4a4413988eea07cf75a0) () — Hook method called when the object is attached to a window.
* `virtual void` [AllAttached](#a6d6379e0993bd525f2cac5f848718870) () — Similar to AttachedToWindow() but this method is triggered after all child views have already been attached to a window.
* `virtual void` [DetachedFromWindow](#a8abc2ea500951a0a22cf018e958ba791) () — Hook method called when the object is detached from a window.
* `virtual void` [AllDetached](#a19dd2213f4b953b54524d7f523d9b406) () — Similar to AttachedToWindow() but this method is triggered after all child views have already been detached from a window.
* `virtual void` [MessageReceived](#aca0a16b0e04288e1fdc0b63690ea7a6d) (BMessage *message) — Handle message received by the associated looper.
* `virtual void` [Draw](#aa55014241fc2f5556415850692b52db2) (BRect updateRect) — Draws the area of the view that intersects updateRect.
* `virtual void` [MouseDown](#a5f5bd975d15df94f2ebbc80eb79cc3f6) (BPoint where) — Hook method called when a mouse button is pressed.
* `virtual void` [MouseUp](#acdb92b30069157b2e3c522a3ef9d6ae4) (BPoint where) — Hook method called when a mouse button is released.
* `virtual void` [MouseMoved](#ac8b20516e42bab2f1eeb130e2432bde0) (BPoint where, uint32 code, const BMessage *dragMessage) — Hook method called when the mouse is moved.
* `virtual void` [WindowActivated](#a5b7aeff0b2608ec63e2c01153a7717f6) (bool active) — Hook method called when the attached window is activated or deactivated.
* `virtual void` [KeyDown](#abea50ea665ce5fcb76b32f1302a6852d) (const char *bytes, int32 numBytes) — Hook method called when a keyboard key is pressed.
* `virtual void` [KeyUp](#acbc528bb70be49993bd99aa136dbb089) (const char *bytes, int32 numBytes) — Hook method called when a keyboard key is released.
* `virtual void` [Pulse](#a0ae8ec3e94ee3d41cb329e3df6966566) () — Hook method called when the view receives a B_PULSE message.
* `virtual void` [FrameMoved](#a551c22b45301e13a3ba959eece3cec7f) (BPoint newPosition) — Hook method called when the view is moved.
* `virtual void` [FrameResized](#a85d88f9c2bb6800560874b2061378fa0) (float newWidth, float newHeight) — Hook method called when the view is resized.
* `virtual void` [TargetedByScrollView](#a668a4ed5419c86a7f2696ca7ece28df7) (BScrollView *scrollView) — Hook method called when the view becomes the target of scrollView.
* `virtual void` [DrawAfterChildren](#abb50623b4236926b068fc5a2264f6a48) (BRect updateRect) — Perform any drawing that needs to be done after child view have already been drawn.
* `virtual void` [LayoutInvalidated](#a0a552cc0d8678939c619f98dcc80d254) (bool descendants=false) — Hook method called when the layout is invalidated.
* `virtual void` [LayoutChanged](#ada521f848e4c800cd02eb4fe529e7ea0) () — Hook function that is called when the layout if this view, or one of its children, has changed.

### Input Related

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
* `virtual void` [MakeFocus](#a266a368d81c6e1668b2b9b22b5016853) (bool focus=true) — Makes the view the current focus view of the window or gives up being the window's focus view.
* `BScrollBar *` [ScrollBar](#a0878bc7981ba814190b822349599a120) (orientation direction) const — Returns the BScrollBar object that has the BView set as its target.
* `status_t` [ScrollWithMouseWheelDelta](#a54991372110199183fed775598ae1912) (BScrollBar *, float) — Handle the scroll wheel changing over scrollbars.

### Layouting

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
* `virtual void` [DoLayout](#a9d766a06d0885200c6ababba4c87808b) () — Layout view within the layout context.

### Tool Tips

* `void` [SetToolTip](#a75fb825a3ef69c1c6fbf3535ee2260ab) (const char *text) — Set the tool tip of the view to text.
* `void` [SetToolTip](#aa377bad64048a2d3cd1c2b272ae3079b) (BToolTip *tip) — Set the tool tip of the view to the tip object.
* `BToolTip *` [ToolTip](#a127ceec2101b12c0fbe1e0e66a7b9dc1) () const — Return the tool tip set to the view or NULL if not set.
* `void` [ShowToolTip](#a61d28f55d6fdc55b59c38c44b9788205) (BToolTip *tip=NULL) — Show the tool tip at the current mouse position.
* `void` [HideToolTip](#af75bbc1131ad6a90e299c6cbcf623fa7) () — Hide the view's tool tip.
* `virtual bool` [GetToolTipAt](#afb826fe9b8964e4d843cae190170badf) (BPoint point, BToolTip **_tip) — Point _tip with the view's tool tip.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#a0c23aeb48d578525f81ba6d47f968528) (BMessage *data) — Static method to instantiate a handler from an archived message.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BView()`

```cpp
BView::BView(const char * name, uint32 flags, BLayout * layout = NULL)
```

Layout constructor. 


To be used as part of a [BLayout](classBLayout.md). You may use the Layout Methods found below to set the size and alignment constraints of the view.


`B_SUPPORTS_LAYOUT` is automatically set to the view. The view flags can be set after the view has been constructed by calling the [SetFlags()](classBView.md#a4740f9a1e1163073b042102a421a2e33) methods.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the view, can be `NULL`. |
| `flags` | The view flags, a mask of one or more of the following: * `B_FULL_UPDATE_ON_RESIZE` Redraw the entire view on resize.  * `B_WILL_DRAW` Indicates that the view will do its own drawing.  * `B_PULSE_NEEDED` The view accepts [Pulse()](classBView.md#a0ae8ec3e94ee3d41cb329e3df6966566) messages.  * `B_NAVIGABLE_JUMP` Default for keyboard navigation.  * `B_FRAME_EVENTS` Responds to move and resize events.  * `B_NAVIGABLE` Able to receive keyboard navigation focus.  * `B_SUBPIXEL_PRECISE` Draws with sub-pixel precision.  * `B_DRAW_ON_CHILDREN` Responds to [DrawAfterChildren()](classBView.md#abb50623b4236926b068fc5a2264f6a48).  * `B_INPUT_METHOD_AWARE` Allows access input method add-ons.  * `B_SUPPORTS_LAYOUT` Supports the layout APIs, i.e. it doesn't use a frame rectangle.  * `B_INVALIDATE_AFTER_LAYOUT` Is redraw after added to a layout. |
| `layout` | A *layout* to set the view to. |





**Since:** Haiku R1

---

### `BView()`

```cpp
BView::BView(BRect frame, const char * name, uint32 resizingMode, uint32 flags)
```

Standard constructor. 


A newly constructed [BView](classBView.md) object has no parent, you must assign it one by passing it into the [AddChild()](classBView.md#ab6382c582e5e1be527d3199459d05e8f) method of another view or window. Once the view or a parent view has been attached to a window the view becomes part of that window's view hierarchy.


When the [BView](classBView.md) object is added as a child the *frame* values are interpreted in the parent's coordinate system. The frame rectangle should be specified in integral values to align on pixel boundaries, decimal values will be rounded.


The resizing mode flags and view flags can be set after the view has been constructed by calling the [SetResizingMode()](classBView.md#a38d29ea581880c3978d7e50dcc851696) and [SetFlags()](classBView.md#a4740f9a1e1163073b042102a421a2e33) methods.


Parameters

| Parameter | Description |
| :--- | :--- |
| `frame` | The *frame* rectangle of the view. |
| `name` | The name of the view, can be `NULL`. |
| `resizingMode` | Defines the view's behavior when its parent is resized.      It combines one of the following horizontal resizing constants:  * `B_FOLLOW_TOP` The margin between the top of the view and the top of its parent remains constant.  * `B_FOLLOW_BOTTOM` The margin between the bottom of the view and the bottom of its parent remains constant.  * `B_FOLLOW_TOP_BOTTOM` The margin between the top and bottom sides of the view and the top and bottom sides of the parent both remain constant.  * `B_FOLLOW_V_CENTER` Maintains a constant relationship to the vertical center of the parent view.    with one of the following vertical resizing constants:  * `B_FOLLOW_LEFT` The margin between the left side of the view and the left side of its parent remains constant.  * `B_FOLLOW_RIGHT` The margin between the right side of the view and the right side of the parent remains constant.  * `B_FOLLOW_LEFT_RIGHT` The margin between the left and right sides of the view and the left and right sides of its parent both remain constant.  * `B_FOLLOW_H_CENTER` The view maintains a constant relationship to the horizontal center of the parent view.    or use one of the following combined horizontal/vertical constants:  * `B_FOLLOW_NONE` Equivalent to `B_FOLLOW_LEFT` | `B_FOLLOW_TOP`.  * `B_FOLLOW_ALL_SIDES` Equivalent to `B_FOLLOW_LEFT_RIGHT` | `B_FOLLOW_TOP_BOTTOM`. |
| `flags` | The view flags, a mask of one or more of the following: * `B_FULL_UPDATE_ON_RESIZE` Redraw the entire view on resize.  * `B_WILL_DRAW` Indicates that the view will do its own drawing.  * `B_PULSE_NEEDED` The view accepts [Pulse()](classBView.md#a0ae8ec3e94ee3d41cb329e3df6966566) messages.  * `B_NAVIGABLE_JUMP` Default for keyboard navigation.  * `B_FRAME_EVENTS` Responds to move and resize events.  * `B_NAVIGABLE` Able to receive keyboard navigation focus.  * `B_SUBPIXEL_PRECISE` Draws with sub-pixel precision.  * `B_DRAW_ON_CHILDREN` Responds to [DrawAfterChildren()](classBView.md#abb50623b4236926b068fc5a2264f6a48).  * `B_INPUT_METHOD_AWARE` Allows access input method add-ons.  * `B_SUPPORTS_LAYOUT` Supports the layout APIs, i.e. it doesn't use a frame rectangle.  * `B_INVALIDATE_AFTER_LAYOUT` Is redraw after added to a layout. |





**Since:** BeOS R3

---

### `~BView()`

```cpp
BView::~BView()
```

Destructor method. 


Deletes the view and all children freeing any memory used.



**Since:** BeOS R3

---

### `BView()`

```cpp
BView::BView(BMessage * archive)
```

Archive constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The message data to construct the view from. |





**Since:** BeOS R3

---

### `AddChild()`

```cpp
bool BView::AddChild(BLayoutItem * child)
```

Add the *child* layout item to the view hierarchy. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `child` | The child layout item to add. |





**Returns:** Whether or not *child* was added to the view layout hierarchy.



**Since:** Haiku R1

---

### `AddChild()`

```cpp
void BView::AddChild(BView * child, BView * before = NULL)
```

Adds *child* to the view hierarchy immediately before *before*. 


A view may only have one parent at a time so *child* must not have already been added to the view hierarchy. If *before* is `NULL` then *child* is added to the end of the tree. If the view is attached to a window *child* and all of its descendent views also become attached to the window invoking an [AttachedToWindow()](classBView.md#ae8117cb4634f4a4413988eea07cf75a0) method on each view.


Parameters

| Parameter | Description |
| :--- | :--- |
| `child` | The child view to add. |
| `before` | The sibling view to add *child* before. |





**Since:** BeOS R3

---

### `AddLine()`

```cpp
void BView::AddLine(BPoint start, BPoint end, rgb_color color)
```

Add a line to the line array drawn from *start* to *end*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `start` | The *start* point of the line. |
| `end` | The *end* point of the line. |
| `color` | The *color* to draw the line. |





**Since:** BeOS R3

---

### `AdoptParentColors()`

```cpp
void BView::AdoptParentColors()
```

Attempts to use the colors of any parent view. Will adopt view, low, and high colors. Should be called in [AttachedToWindow()](classBView.md#ae8117cb4634f4a4413988eea07cf75a0) or [AllAttached()](classBView.md#a6d6379e0993bd525f2cac5f848718870). 



**Since:** Haiku R1

---

### `AdoptSystemColors()`

```cpp
void BView::AdoptSystemColors()
```

Instructs view to use standard system "panel" colors. B_PANEL_BACKGROUND_COLOR for [ViewUIColor()](classBView.md#aec6c89446eb4f5ded151adced9126df8) B_PANEL_BACKGROUND_COLOR for [LowUIColor()](classBView.md#ae32ca6d8f106d44b5b51df82a7eb64c5) B_PANEL_TEXT_COLOR for [HighUIColor()](classBView.md#aa86f548fba2e82d022066198be6d5af6) 



**Since:** Haiku R1


Referenced by [BLayoutBuilder::Grid< ParentBuilder >::Grid()](classBLayoutBuilder_1_1Grid.md#ad7bd68789548063830f46a0bb279e17a), and [BLayoutBuilder::Group< ParentBuilder >::Group()](classBLayoutBuilder_1_1Group.md#adebaf628afb53fdd86d6b153d60cf0ea).

---

### `AdoptViewColors()`

```cpp
void BView::AdoptViewColors(BView * view)
```

Attempts to use the colors of a given view. Will adopt view, low, and high colors. 



**Since:** Haiku R1

---

### `AllArchived()`

```cpp
status_t BView::AllArchived(BMessage * into)const
```

Hook method called when all views have been archived. 



**Since:** BeOS R3


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a4075315c407443a3b0dbb3d7551b53c9).


Reimplemented in [BMenuField](classBMenuField.md#ae8acba317c58f2767aae7956974536c9), [BSplitView](classBSplitView.md#a8677380375e36b4bc2380a929dc69a69), and [BTextControl](classBTextControl.md#a5b73780d200fa037f99f6cec5cbf74ec).

---

### `AllAttached()`

```cpp
void BView::AllAttached()
```

Similar to [AttachedToWindow()](classBView.md#ae8117cb4634f4a4413988eea07cf75a0) but this method is triggered after all child views have already been attached to a window. 



**Since:** BeOS R3


Reimplemented in [BBox](classBBox.md#a7d2b3254a2179ba55a133450c7f6344b), [BButton](classBButton.md#a9a888bcbcdcf8a924b6010ef6e7f46a9), [BChannelSlider](classBChannelSlider.md#abfb89e632dec0539147b79e770090b23), [BCheckBox](classBCheckBox.md#a3d555861d9a8ce0be86193cac484f1ac), [BColorControl](classBColorControl.md#a0429d5c2f2a748e50b556e03b60c3f84), [BControl](classBControl.md#a2abeec720f873da7c4bc3a2709ff8be0), [BDragger](classBDragger.md#ac417cb3cb2f104981fbf37533425ed39), [BListView](classBListView.md#ae916566577d7d1b310d00861b26ef651), [BMenu](classBMenu.md#a2540cab39de9a2ed1a3e71e2c8ec52dc), [BMenuBar](classBMenuBar.md#ac02982cd861af6eb4771f260fcf50ed8), [BMenuField](classBMenuField.md#a55e723717b6ec14973ed513cb50a42c2), [BOptionPopUp](classBOptionPopUp.md#a9fb0e8fefa909b2f7a25d0b2a3ba473e), [BOutlineListView](classBOutlineListView.md#a991cfdba0dd36ccebc812c10ced9f4a0), [BPictureButton](classBPictureButton.md#a1d263b8ec7ccde013c7a462c702052dd), [BPopUpMenu](classBPopUpMenu.md#ae9b5eaf528d9fc3924e29ba05b0c5675), [BRadioButton](classBRadioButton.md#af941f0cf47d024337e30653bc4dcd5d2), [BScrollBar](classBScrollBar.md#a36e2edccc25e4aa196ae7e940b4f072b), [BScrollView](classBScrollView.md#aa36878223be666cb2f7b1a1c20cee965), [BStatusBar](classBStatusBar.md#ae76d315835000366025553b7db17c798), [BStringView](classBStringView.md#a01bf8802d1b9506079e4d3399ea720f9), [BTabView](classBTabView.md#a8243f114472f895f2491b1bf051da93d), [BTextControl](classBTextControl.md#abae889f35648d9a08f5b997986381c06), and [BTextView](classBTextView.md#a525a3a00911c36ee0acf05daa2ff8716).

---

### `AllDetached()`

```cpp
void BView::AllDetached()
```

Similar to [AttachedToWindow()](classBView.md#ae8117cb4634f4a4413988eea07cf75a0) but this method is triggered after all child views have already been detached from a window. 



**Since:** BeOS R3


Reimplemented in [BBox](classBBox.md#aeb7d158b1ac7aecfcd17eabeecbcc85b), [BButton](classBButton.md#a4c8d87c3ceb9b867dae9adc68526cb0b), [BChannelSlider](classBChannelSlider.md#a4339e7bc207a4c3887a4aef63bdff817), [BCheckBox](classBCheckBox.md#aabe966d7094a102a029eb86f53156b52), [BColorControl](classBColorControl.md#a3053cfbbb6aeff2b1fe9852a91fe6364), [BControl](classBControl.md#a991c0eecd0279cbc27c5f9a0fbc37920), [BDragger](classBDragger.md#a257579686db16a793c1e6fc0b8c6a100), [BListView](classBListView.md#a5f97a604910fbf576aa1acde9e4b8f36), [BMenu](classBMenu.md#a40c41c3d2d1a8e23dfad97039615b208), [BMenuBar](classBMenuBar.md#a0c548adc7796603d8d686a401817d0d9), [BMenuField](classBMenuField.md#a635e98f17b0268ad3454579516852c8e), [BOutlineListView](classBOutlineListView.md#a677488c290fcd8c263472840e06ea2b2), [BPictureButton](classBPictureButton.md#a699d006ff7d23e3448ee8b23555815c4), [BPopUpMenu](classBPopUpMenu.md#a6dda50def6c5f6fd880595d1ac0d7ce1), [BRadioButton](classBRadioButton.md#aa821c3cb4a2f47e3af2f7bde5b129427), [BScrollBar](classBScrollBar.md#a707a012fa7d5c7f66cd54f31f0d42175), [BScrollView](classBScrollView.md#a2597e5c03b836e4c79c05a19e5e1e338), [BStatusBar](classBStatusBar.md#a1525e8925eaa5c372da8756b13b45e0b), [BStringView](classBStringView.md#afdb3c189ea4a0f8e5d5472a6cf50caa7), [BTabView](classBTabView.md#aaaa411a7931a91b7b840d2db3785ed04), [BTextControl](classBTextControl.md#ad47ac17bae76e2be8786ec25ebd30b89), and [BTextView](classBTextView.md#a2ff4cd2084da7717a7c08c7c95651614).

---

### `AllUnarchived()`

```cpp
status_t BView::AllUnarchived(const BMessage * from)
```

Hook method called when all views have been unarchived. 



**Since:** BeOS R3


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a2b1d74c147ea18e4b4bfacd42f11e0d2).


Reimplemented in [BScrollView](classBScrollView.md#adfed255a897cd481127f6b911b329c3d), [BMenuField](classBMenuField.md#ad7e9ecb63a3df86c848bf8a9e7409ee7), [BSplitView](classBSplitView.md#a5c4cc359d801e27e39f28469c24bbd76), [BTabView](classBTabView.md#a6cc6ca514c10001b8610e5937f96b48e), and [BTextControl](classBTextControl.md#abc5bfb77b1ab96dddec5c37d76657a89).

---

### `AppendToPicture()`

```cpp
void BView::AppendToPicture(BPicture * picture)
```

Appends drawing instructions to *picture* without clearing it first. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `picture` | The [BPicture](classBPicture.md) object to record drawing instructions to. |





**Since:** BeOS R3

---

### `Archive()`

```cpp
status_t BView::Archive(BMessage * data, bool deep = true)const
```

Archives the object into the *data* message. 


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


Reimplemented from [BHandler](../application_kit/classBHandler.md#ac2711ccff5e7f711244c88a5642c83db).


Reimplemented in [BBox](classBBox.md#abd1a762e132a6196076617cee1eb81ac), [BMenu](classBMenu.md#a71bed24f541bdfb690863118ce3f716b), [BMenuBar](classBMenuBar.md#af4ae9bcc3c1cbe560e745c9868fb9c5f), [BMenuField](classBMenuField.md#ada677e4339d5a5eca5c945c4165b6a3e), [BOutlineListView](classBOutlineListView.md#af590f60f193f47989f63c34dda0e6916), [BPictureButton](classBPictureButton.md#ab476f82e9d75a3b4a9b54ca35d1ad036), [BPopUpMenu](classBPopUpMenu.md#af81e6dc2ddcc3063eb33a1a5cf3b9088), [BScrollBar](classBScrollBar.md#a2d8cea93fe440bbed02685c135b0f802), [BScrollView](classBScrollView.md#a7858c5f97152c910831db817b80f5f95), [BStatusBar](classBStatusBar.md#a05e0e95a3cee49d1fa7f1a48e26ae20b), [BStringView](classBStringView.md#adbafb44b6614c69a645d3e2de818c5f5), [BTextControl](classBTextControl.md#af68449ec551e8a089a441fd270954b99), [BTextView](classBTextView.md#a0f3fb624378a2d13617773713efedd98), [BButton](classBButton.md#adce5e4839a58c3bb85965398a490d720), [BChannelControl](classBChannelControl.md#aa71189c8b008cb3329c17b58f786617e), [BCheckBox](classBCheckBox.md#a75511a8252ef3ffa1177f57af97b67ca), [BColorControl](classBColorControl.md#a6437907efd1d39a492db1f55b5f4dc36), [BControl](classBControl.md#a2581a447a34eef102c62d0e998155290), [BDragger](classBDragger.md#aece5cd86ccd46a23f1188697f4bffa55), [BListView](classBListView.md#a89277e72296cc9ec516777e000f100e3), [BRadioButton](classBRadioButton.md#aeed1a7a2142b1ac7b1499234f884caae), [BChannelSlider](classBChannelSlider.md#ac216b412d86275115516b886c4f9b578), [BSeparatorView](classBSeparatorView.md#a41d7d43196ee70cc26986f95b5c3e262), [BSplitView](classBSplitView.md#a2c4ab843dd62815ebeb7201e21d3199b), and [BTabView](classBTabView.md#a3354f9343238295b7ed0a24339106cd5).

---

### `AttachedToWindow()`

```cpp
void BView::AttachedToWindow()
```

Hook method called when the object is attached to a window. 



**Since:** BeOS R3


Reimplemented in [BBox](classBBox.md#a79f7b5e92fd6c2976f6b82d6bb0113e4), [BButton](classBButton.md#a8514d1d173d5a852f52354107dedce7f), [BChannelControl](classBChannelControl.md#aaed17a427fd040df721062ea646ee360), [BChannelSlider](classBChannelSlider.md#a896559c9ffdf6c29fec0071f7e74326e), [BCheckBox](classBCheckBox.md#a6975f3d06240cfc32d9422163d21760c), [BColorControl](classBColorControl.md#a0a4c898ee218990de45a53a90663d12e), [BControl](classBControl.md#a460fa93bcdd5309d8d86f8bfcd53b584), [BDragger](classBDragger.md#a6f1804718035a60dc652691694e004a1), [BListView](classBListView.md#a172497b23a2c4ab6da666363ad51d90e), [BMenu](classBMenu.md#af38b2e6bf69d918e37bcf1e18711bb37), [BMenuBar](classBMenuBar.md#a48b3c56f65222c9dc3e5faca5eb80319), [BMenuField](classBMenuField.md#a63f6e3879897c8b42a6eb49667b84b2b), [BOptionPopUp](classBOptionPopUp.md#a5c301cf20c932c72700eea57a427e68d), [BPictureButton](classBPictureButton.md#ae6b51e465aa9807d707316a00b6fe22d), [BPopUpMenu](classBPopUpMenu.md#a2bb158bea8366e9afc2f10c440042585), [BRadioButton](classBRadioButton.md#abacc25df48c377cd37ae3cb5eaf3917d), [BScrollBar](classBScrollBar.md#a0b4d0fc3f451b05a0598a4e3f4adce9b), [BScrollView](classBScrollView.md#a8ecce6ba6ebd8825a39717796b187960), [BSplitView](classBSplitView.md#a5864715e720854c6a6947f0f730e88c5), [BStatusBar](classBStatusBar.md#ad5d62923df2112d6bde6c51f85f8db8a), [BStringView](classBStringView.md#a4205042958e6bb45dea702bc35667df9), [BTabView](classBTabView.md#a88bc95e53bc3a3cbc7fddfb7b9ce736a), [BTextControl](classBTextControl.md#ae3adb78b19be6c737882972695c5f84f), and [BTextView](classBTextView.md#a73a892fb4d5e7e3575064f326b67867a).

---

### `BeginLayer()`

```cpp
void BView::BeginLayer(uint8 opacity)
```

Begins a drawing layer. 


This feature of [BView](classBView.md) allows you to create a separate layer, draw on it, and blend it in with the rest of the view with a given *opacity*. Internally, the method creates a new drawing buffer, that you can draw on using the methods of [BView](classBView.md). After finishing your layer, you call [EndLayer()](classBView.md#a9f54d4478a12823f116168a45af30898) to apply the *opacity* to the layer, and blend it in with the existing drawing.


You can nest layers, meaning you can call this method while drawing a layer, to create a sublayer. The layers are mixed and blended in order.


This work was done to support drawing for WebKit.



**See also:** [EndLayer()](classBView.md#a9f54d4478a12823f116168a45af30898)



**Since:** Haiku R1

---

### `BeginLineArray()`

```cpp
void BView::BeginLineArray(int32 count)
```

Begin a line array of up to *count* lines. 


This is a more efficient way of drawing a large number of lines than calling [StrokeLine()](classBView.md#a909ee03901fac4ae5504f7faf5e41a7c) repeatedly. First call [BeginLineArray()](classBView.md#ab3f2e9f54d2b93952b27e182ac552983) to begin drawing lines, then call [AddLine()](classBView.md#a88440336a66ee9b1a4b1661e9ba9e59c) for each line you wish to draw, and finally call [EndLineArray()](classBView.md#a24ba922f9698936bc27f48b3c51349a1) to finish the line array and draw the lines.


These methods don't move the current pen location or change the high or low colors of the view. *count* should be close to the number of lines you wish to draw and should be below 256 to draw efficiently.


Parameters

| Parameter | Description |
| :--- | :--- |
| `count` | The maximum number of lines in the line array to draw. |





**See also:** [StrokeLine()](classBView.md#a909ee03901fac4ae5504f7faf5e41a7c)



**Since:** BeOS R3

---

### `BeginPicture()`

```cpp
void BView::BeginPicture(BPicture * picture)
```

Begins sending drawing instructions to *picture*. 


The *[BPicture](classBPicture.md)* object is cleared and any successive drawing instructions sent to the view are redirected to *picture* until [EndPicture()](classBView.md#ae01506892a9b2d39f6df13726be9d0af) is called. To append drawing instructions to a [BPicture](classBPicture.md) object without clearing it first call [AppendToPicture()](classBView.md#a2d73d2f2b0b35390929cf54fbfa5ecff) instead.


The view doesn't display anything to the screen while it's recording to *picture*. Use the [DrawPicture()](classBView.md#ae4b252943befd9f0b62e30517b3ecec2) method to render the *picture*.


Only drawing instructions performed directly on the view, not its child views are sent to the [BPicture](classBPicture.md) object and [BPicture](classBPicture.md) captures only primitive graphics operations. The view must be attached to a window for the drawing instruction to be recorded. Drawing instructions are recorded even if the view is hidden or resides outside the clipping region or the window is off-screen.


Parameters

| Parameter | Description |
| :--- | :--- |
| `picture` | The [BPicture](classBPicture.md) object to record drawing instructions to. |





**Since:** BeOS R3

---

### `BeginRectTracking()`

```cpp
void BView::BeginRectTracking(BRect startRect, uint32 style = B_TRACK_WHOLE_RECT)
```

Displays an outline rectangle on the view and initiates tracking. 


This method is typically called from the [MouseDown()](classBView.md#a5f5bd975d15df94f2ebbc80eb79cc3f6) while [EndRectTracking()](classBView.md#a7bcc3532c03eeeb929278de8fcc1fd25) is typically called from the MouseUp method().


Parameters

| Parameter | Description |
| :--- | :--- |
| `startRect` | The initial frame in the view's coordinate system. |
| `style` | This parameter is set to one of the following: * `B_TRACK_WHOLE_RECT` The position of the rect changes with the cursor while its size remains the same.  * `B_TRACK_RECT_CORNER` The left top corner is fixed while the right and bottom edges move with the cursor. |





**Since:** BeOS R3

---

### `Bounds()`

```cpp
BRect BView::Bounds()const
```

Returns the view's frame rectangle in the view's coordinate system. 



**Returns:** The view's bounding rectangle in the view's coordinate system.



**Since:** BeOS R3

---

### `ChildAt()`

```cpp
BView * BView::ChildAt(int32 index)const
```

Returns a pointer to the child view found at *index*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index of the child view to return a pointer of. |





**Returns:** A pointer to the child view at *index* or `NULL` if not found.



**Since:** BeOS R3

---

### `ClearViewBitmap()`

```cpp
void BView::ClearViewBitmap()
```

Clears the background bitmap of the view if it has one. 



**Since:** BeOS R4

---

### `ClearViewOverlay()`

```cpp
void BView::ClearViewOverlay()
```

Clears the overlay bitmap of the view if it has one. 



**Since:** BeOS R5

---

### `ClipToInversePicture()`

```cpp
void BView::ClipToInversePicture(BPicture * picture, BPoint where = B_ORIGIN, bool sync = true)
```

Intersects the current clipping region of the view with the pixels outside of *picture*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `picture` | The [BPicture](classBPicture.md) object to intersect with. |
| `where` | Offset in the view's coordinate system. |
| `sync` | If `false`, this method will execute asynchronously. |





**See also:** [ClipToPicture()](classBView.md#a9c92c9e8e306d00dbfef81f2b0282339)



**Since:** BeOS R5

---

### `ClipToInverseRect()`

```cpp
void BView::ClipToInverseRect(BRect rect)
```

Intersects the current clipping region of the view with the pixels outside of *rect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The [BRect](classBRect.md) that describes the rectangle to intersect with. |





**See also:** [ClipToRect()](classBView.md#a22ff147a2f0a0bd65de494c9a039acee)



**Since:** Haiku R1

---

### `ClipToInverseShape()`

```cpp
void BView::ClipToInverseShape(BShape * shape)
```

Intersects the current clipping region of the view with the pixels outside of *shape*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `shape` | The [BShape](classBShape.md) that describes the area to intersect with. |





**See also:** [ClipToShape()](classBView.md#ac0884c62949361a7eb6a4834f46b902c)



**Since:** Haiku R1

---

### `ClipToPicture()`

```cpp
void BView::ClipToPicture(BPicture * picture, BPoint where = B_ORIGIN, bool sync = true)
```

Intersects the current clipping region of the view with the pixels of *picture*. 


[BPicture](classBPicture.md) instances are resolution independent, *picture* is effectively drawn at the view's resolution and the bitmap produced is used to modify the clipping region.


The pixels that are at least partially opaque are the ones drawn by *picture*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `picture` | The [BPicture](classBPicture.md) object to intersect with. |
| `where` | Offset in the view's coordinate system. |
| `sync` | If `false`, this method will execute asynchronously. |





**Since:** BeOS R5

---

### `ClipToRect()`

```cpp
void BView::ClipToRect(BRect rect)
```

Intersects the current clipping region of the view with the pixels of *rect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The [BRect](classBRect.md) that describes the rectangle to intersect with. |





**Since:** Haiku R1

---

### `ClipToShape()`

```cpp
void BView::ClipToShape(BShape * shape)
```

Intersects the current clipping region of the view with the pixels of *shape*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `shape` | The [BShape](classBShape.md) that describes the area to intersect with. |





**Since:** Haiku R1

---

### `ConstrainClippingRegion()`

```cpp
void BView::ConstrainClippingRegion(BRegion * region)
```

Set the clipping region the *region* restricting the area that the view can draw in. 


The Application Server keeps track of the clipping region for each view attached to a window so that the view can't draw outside of it, consequently this method works only for views that are attached to a window.


The default clipping region contains the visible area of the view. By passing a region to this method the clipping area is further restricted. Passing in `NULL` resets the clipping region back to the default.


Calls to [ConstrainClippingRegion()](classBView.md#a656b8d82a6a7c7c6ab33c3dd08aad6ec) are not cumulative, each time this method is called it replaces the old clipping region. However, clipping regions from previous states are intersected to compute the effective clipping.


Region-based clipping is not affected by the view transform. If you need to constrain drawing to a transformed region, use [ClipToPicture()](classBView.md#a9c92c9e8e306d00dbfef81f2b0282339) and [FillRegion()](classBView.md#a4810086c415d90bffa25ab2963716936) instead.


Parameters

| Parameter | Description |
| :--- | :--- |
| `region` | The region to set the clipping region to or `NULL` to reset to default. |





**Since:** BeOS R3

---

### `ConvertFromParent()`

```cpp
void BView::ConvertFromParent(BPoint * point)const
```

Convert *point* from the parent's coordinate system to the view's coordinate system in place. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | A pointer to a [BPoint](classBPoint.md) object to convert. |





**Since:** BeOS R3

---

### `ConvertFromParent()`

```cpp
BPoint BView::ConvertFromParent(BPoint point)const
```

Returns *point* converted from the parent's coordinate system to the view's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | A [BPoint](classBPoint.md) object to convert. |





**Returns:** A new [BPoint](classBPoint.md) object in the view's coordinate system.



**Since:** BeOS R3

---

### `ConvertFromParent()`

```cpp
void BView::ConvertFromParent(BRect * rect)const
```

Convert *rect* from the parent's coordinate system to the view's coordinate system in place. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | A pointer to a [BRect](classBRect.md) object to convert. |





**Since:** BeOS R3

---

### `ConvertFromParent()`

```cpp
BRect BView::ConvertFromParent(BRect rect)const
```

Returns *rect* converted from the parent's coordinate system to the view's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | A [BRect](classBRect.md) object to convert. |





**Returns:** A new [BRect](classBRect.md) object in the view's coordinate system.



**Since:** BeOS R3

---

### `ConvertFromScreen()`

```cpp
void BView::ConvertFromScreen(BPoint * point)const
```

Convert *point* from the screen's coordinate system to the view's coordinate system in place. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | A pointer to a [BPoint](classBPoint.md) object to convert. |





**Since:** BeOS R3

---

### `ConvertFromScreen()`

```cpp
BPoint BView::ConvertFromScreen(BPoint point)const
```

Returns *point* converted from the screen's coordinate system to the view's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | A [BPoint](classBPoint.md) object to convert. |





**Returns:** A new [BPoint](classBPoint.md) object in the view's coordinate system.



**Since:** BeOS R3

---

### `ConvertFromScreen()`

```cpp
void BView::ConvertFromScreen(BRect * rect)const
```

Convert *rect* from the screen's coordinate system to the view's coordinate system in place. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | A pointer to a [BRect](classBRect.md) object to convert. |





**Since:** BeOS R3

---

### `ConvertFromScreen()`

```cpp
BRect BView::ConvertFromScreen(BRect rect)const
```

Returns *rect* converted from the screen's coordinate system to the view's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | A [BRect](classBRect.md) object to convert. |





**Returns:** A new [BRect](classBRect.md) object in the view's coordinate system.



**Since:** BeOS R3

---

### `ConvertToParent()`

```cpp
void BView::ConvertToParent(BPoint * point)const
```

Convert *point* to the parent's coordinate system in place. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | A pointer to a [BPoint](classBPoint.md) object to convert. |





**Since:** BeOS R3

---

### `ConvertToParent()`

```cpp
BPoint BView::ConvertToParent(BPoint point)const
```

Returns *point* converted to the parent's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | A [BPoint](classBPoint.md) object to convert. |





**Returns:** A new [BPoint](classBPoint.md) object in the parent's coordinate system.



**Since:** BeOS R3

---

### `ConvertToParent()`

```cpp
void BView::ConvertToParent(BRect * rect)const
```

Convert *rect* to the parent's coordinate system in place. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | A pointer to a [BRect](classBRect.md) object to convert. |





**Since:** BeOS R3

---

### `ConvertToParent()`

```cpp
BRect BView::ConvertToParent(BRect rect)const
```

Returns *rect* converted to the parent's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | A [BRect](classBRect.md) object to convert. |





**Returns:** A new [BRect](classBRect.md) object in the parent's coordinate system.



**Since:** BeOS R3

---

### `ConvertToScreen()`

```cpp
void BView::ConvertToScreen(BPoint * point)const
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
BPoint BView::ConvertToScreen(BPoint point)const
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
void BView::ConvertToScreen(BRect * rect)const
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
BRect BView::ConvertToScreen(BRect rect)const
```

Returns *rect* converted to the screen's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | A [BRect](classBRect.md) object to convert. |





**Returns:** A new [BRect](classBRect.md) object in the screen's coordinate system.



**Since:** BeOS R3

---

### `CopyBits()`

```cpp
void BView::CopyBits(BRect src, BRect dst)
```

Copy the bits from the *src* rectangle to the *dst* rectangle in the view's coordinate system. 


If the rectangles are of different sizes than *src* is scaled to fit. *src* is clipped if a part of *dst* lies outside of the visible region of the view. Only the visible portions of *src* are copied.


The view must be attached to a window for this method to work.


Parameters

| Parameter | Description |
| :--- | :--- |
| `src` | The source rectangle to copy bits from. |
| `dst` | The destination rectangle to copy bits to. |





**Since:** BeOS R3

---

### `CountChildren()`

```cpp
int32 BView::CountChildren()const
```

Returns the number of child views that this view has. 



**Returns:** The number of child views.



**Since:** BeOS R3

---

### `DelayedInvalidate()`

```cpp
void BView::DelayedInvalidate(bigtime_t delay)
```

Sends a message to App Server to redraw the entire view after a certain, minimum, delay. Repeated calls to this method may be merged, but the view is guaranteed to be redrawn after the delay given in the first call of this method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `delay` | The time, in microseconds, to wait until redrawing the view. |





**Since:** Haiku R1

---

### `DelayedInvalidate()`

```cpp
void BView::DelayedInvalidate(bigtime_t delay, BRect invalRect)
```

Sends a message to App Server to redraw the portion of the view specified by *invalRect* after a certain, minimum, delay. Repeated calls to this method may be merged, but the invalidated rect is guaranteed to be redrawn after the minimum delay given by the first call of this method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `delay` | The time, in microseconds, to wait until redrawing the view. |
| `invalRect` | The rectangular area of the view to redraw. |





**Since:** Haiku R1

---

### `DetachedFromWindow()`

```cpp
void BView::DetachedFromWindow()
```

Hook method called when the object is detached from a window. 



**Since:** BeOS R3


Reimplemented in [BBox](classBBox.md#a7fec55f824c589025110d7562b55ee91), [BButton](classBButton.md#a2324e5b37fa2c3c4e8d2c63763172d12), [BChannelControl](classBChannelControl.md#a2ba05bb52a1d79b9e840c28e08531e98), [BChannelSlider](classBChannelSlider.md#a0e62e869e80944ad32a2c0dc8b813e35), [BCheckBox](classBCheckBox.md#a9d332c16b89814d6255fa7ff96827943), [BColorControl](classBColorControl.md#ae1b42162705172630cf7961d4af876f2), [BControl](classBControl.md#a588fea0ded4cdc4c1b4fb5d1f5565f27), [BDragger](classBDragger.md#a8dcd78025adb8eb65fce16c5914c880d), [BListView](classBListView.md#a06439547091d244eec75cdb9b078d5ac), [BMenu](classBMenu.md#a51b79eb8595e20234f2fefabf7899e21), [BMenuBar](classBMenuBar.md#aaf4b5448201a1d30c969ddc20f1d492d), [BMenuField](classBMenuField.md#aeea6d476c34d48f1325956c64b4dd70d), [BOutlineListView](classBOutlineListView.md#a7c71e9e2a55689bc05d63ef4c7a7cfde), [BPictureButton](classBPictureButton.md#ac5c3a2f7ac5f4876cdc6f74b467b763a), [BPopUpMenu](classBPopUpMenu.md#a9b5a2a077b54a2c9e451d0f916358420), [BRadioButton](classBRadioButton.md#a0c66b7a3964716897d10713a6880bc9c), [BScrollBar](classBScrollBar.md#a844007152b75523f25890ce70c123254), [BScrollView](classBScrollView.md#af455b68fa6dd09a825c0afc6aed9898e), [BStatusBar](classBStatusBar.md#adedd63326aac3a6d73267ea6f1244fa1), [BStringView](classBStringView.md#a8b690fbe586fa7136c6e795b3c55af65), [BTabView](classBTabView.md#a6fdc45a6555af003617cfac94c3866ae), [BTextControl](classBTextControl.md#a6a6832d8df544412d84839a1011c6da0), and [BTextView](classBTextView.md#a79356aad15f3cd52203d81cb5b163461).

---

### `DisableLayoutInvalidation()`

```cpp
void BView::DisableLayoutInvalidation()
```

Disable layout invalidation. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Since:** Haiku R1

---

### `DoLayout()`

```cpp
void BView::DoLayout()
```

Layout view within the layout context. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Since:** Haiku R1


Reimplemented in [BBox](classBBox.md#a3379df36cfad5a63b74aea2ab1dfb298), [BMenu](classBMenu.md#a981691c987e0f0a82a8f056284280032), [BMenuField](classBMenuField.md#ace976f3319627ec56e46c77f3b3c48de), [BScrollView](classBScrollView.md#afecb9e8df5e62393e1694de56598a590), [BSeparatorView](classBSeparatorView.md#a61cb9c3f7237acf305b6cf2453d91d77), [BTextControl](classBTextControl.md#ad2f9995715ea117902b9255a08d6f4a2), and [BTextView](classBTextView.md#a5126538fd4fc16a0deec2c256c62ce51).

---

### `DragMessage()`

```cpp
void BView::DragMessage(BMessage * message, BBitmap * image, BPoint offset, BHandler * replyTo = NULL)
```

Initiates a drag-and-drop session of an *image*. 



> [!WARNING]
> This method only works if the [BView](classBView.md) objects are attached to a window.


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | Contains data to be dragged and dropped on the destination view. The caller retains responsibility for this object. |
| `image` | Bitmap image dragged by the user. The memory used by the bitmap is freed automatically when the message is dropped. |
| `offset` | The offset to the hotspot within the image in the bitmap's coordinate system. |
| `replyTo` | The target set to handle the message sent in reply to the dragged message. If `NULL` the reply is instead directed to the [BView](classBView.md) object that initiated the drag-and-drop session. |





**Since:** BeOS R3

---

### `DragMessage()`

```cpp
void BView::DragMessage(BMessage * message, BBitmap * image, drawing_mode dragMode, BPoint offset, BHandler * replyTo = NULL)
```

Initiates a drag-and-drop session of an *image* with drawing_mode set by *dragMode*. 



> [!WARNING]
> This method only works if the [BView](classBView.md) objects are attached to a window.


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | Contains data to be dragged and dropped on the destination view. The caller retains responsibility for this object. |
| `image` | Bitmap image dragged by the user. The memory used by the bitmap is freed automatically when the message is dropped. |
| `dragMode` | Sets the drawing_mode used to draw the dragged image. Set to `B_OP_ALPHA` to drag-and-drop partially transparent images. |
| `offset` | The offset to the hotspot within the image in the bitmap's coordinate system. |
| `replyTo` | The target set to handle the message sent in reply to the dragged message. If `NULL` the reply is instead directed to the [BView](classBView.md) object that initiated the drag-and-drop session. |





**Since:** BeOS R5

---

### `DragMessage()`

```cpp
void BView::DragMessage(BMessage * message, BRect dragRect, BHandler * replyTo = NULL)
```

Initiates a drag-and-drop session. 



> [!WARNING]
> This method only works if the [BView](classBView.md) objects are attached to a window.


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | Contains data to be dragged and dropped on the destination view. The caller retains responsibility for this object. |
| `dragRect` | An outline rectangle used in place of a bitmap image set in the view's coordinate system. |
| `replyTo` | The target set to handle the message sent in reply to the dragged message. If `NULL` the reply is instead directed to the [BView](classBView.md) object that initiated the drag-and-drop session. |





**Since:** BeOS R3

---

### `Draw()`

```cpp
void BView::Draw(BRect updateRect)
```

Draws the area of the view that intersects *updateRect*. 


Derived classes should override this method to draw their view.


RemarksThis is an hook method called by the Interface Kit, you don't have to call it yourself. If you need to forcefully redraw the view consider calling [Invalidate()](classBView.md#adfced0dcb244e199f872fdbd48349a05) instead.
Parameters

| Parameter | Description |
| :--- | :--- |
| `updateRect` | The rectangular area to be drawn. |





**Since:** BeOS R3


Reimplemented in [BStringView](classBStringView.md#a8b9e9c371957ddedaf6a22de5d1f216f), [BBox](classBBox.md#a36f1bd498f8c0470ee7e01457795cf63), [BButton](classBButton.md#adc0ec950461375f62cf5da3355aebf53), [BChannelSlider](classBChannelSlider.md#a08090615a13b65d7877b2e38958fb725), [BCheckBox](classBCheckBox.md#a0dfaafaf971ca13f8d882de6fc8814e4), [BColorControl](classBColorControl.md#a839fb51f1aa457ef7efb8fbc8cf84553), [BDragger](classBDragger.md#aa8f8a7bfd289a37242695216db17093c), [BListView](classBListView.md#a7c284b74a68c3f15e7266ac7bca65d24), [BMenu](classBMenu.md#a239982fa92e2f5a9c2ed0c267b7470b3), [BMenuBar](classBMenuBar.md#a50f02992ee792e7f66b8f3148e75dcc8), [BMenuField](classBMenuField.md#afae9ce554a41405c5d272c349e7fee57), [BPictureButton](classBPictureButton.md#a1fecb18731921b32f7fe926a75e0f48c), [BRadioButton](classBRadioButton.md#a34ec883efcfff5f3dc9ab3095d8050b3), [BScrollBar](classBScrollBar.md#adc34c89c750a72fa6d09b61262cba5e4), [BScrollView](classBScrollView.md#a1026d80f4935375a237e9d567a0054d1), [BSeparatorView](classBSeparatorView.md#a542695a2d0bf49db1670e0de9b7108ec), [BSplitView](classBSplitView.md#ae760c25461d9565a0868d48b7061af46), [BStatusBar](classBStatusBar.md#aee5177f0609d82b4cff6ad7aa71ce351), [BTabView](classBTabView.md#adafa3b55c2565daffe2c7df0f7c50fc7), [BTextControl](classBTextControl.md#a55cee4b3b608fa7be0a9ca4bead151ef), [BTextView](classBTextView.md#ad1b1f366a371aaecdbc39e2b13f6100b), and [BChannelControl](classBChannelControl.md#ae898048a4dab959bb37dfbbbdd0bc8f4).

---

### `DrawAfterChildren()`

```cpp
void BView::DrawAfterChildren(BRect updateRect)
```

Perform any drawing that needs to be done after child view have already been drawn. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `updateRect` | The rectangular area to drawn in. |





**Since:** BeOS R5


Reimplemented in [BSplitView](classBSplitView.md#a5ebd7844fea0b1352c061b8180fb31d4).

---

### `DrawBitmap()`

```cpp
void BView::DrawBitmap(const BBitmap * bitmap)
```

Draws *bitmap* on the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The bitmap to draw onto the view. |





**Since:** BeOS R3

---

### `DrawBitmap()`

```cpp
void BView::DrawBitmap(const BBitmap * bitmap, BPoint where)
```

Draws *bitmap* on the view offset by *where*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The bitmap to draw onto the view. |
| `where` | The location to draw the bitmap in the view's coordinate system. |





**Since:** BeOS R3

---

### `DrawBitmap()`

```cpp
void BView::DrawBitmap(const BBitmap * bitmap, BRect bitmapRect, BRect viewRect)
```

Draws *bitmap* on the view within *viewRect*. *bitmap* portion is scaled to fit *viewRect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The bitmap to draw onto the view. |
| `bitmapRect` | The portion of the bitmap to draw in the bitmap's coordinate system. |
| `viewRect` | The area in the view's coordinate system to draw the bitmap in. |





**Since:** BeOS R3

---

### `DrawBitmap()`

```cpp
void BView::DrawBitmap(const BBitmap * bitmap, BRect bitmapRect, BRect viewRect, uint32 options)
```

Draws *bitmap* on the view within *viewRect*. *bitmap* portion is scaled to fit *viewRect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The bitmap to draw onto the view. |
| `bitmapRect` | The portion of the bitmap to draw in the bitmap's coordinate system. |
| `viewRect` | The area in the view's coordinate system to draw the bitmap in. |
| `options` | ?? |





**Since:** Haiku R1

---

### `DrawBitmap()`

```cpp
void BView::DrawBitmap(const BBitmap * bitmap, BRect viewRect)
```

Draws *bitmap* on the view within *viewRect*. *bitmap* is scaled to fit *viewRect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The bitmap to draw onto the view. |
| `viewRect` | The area in the view's coordinate system to draw the bitmap in. |





**Since:** BeOS R3

---

### `DrawBitmapAsync()`

```cpp
void BView::DrawBitmapAsync(const BBitmap * bitmap)
```

Draws *bitmap* on the view asynchronously. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The bitmap to draw onto the view. |





**Since:** BeOS R3

---

### `DrawBitmapAsync()`

```cpp
void BView::DrawBitmapAsync(const BBitmap * bitmap, BPoint where)
```

Draws *bitmap* on the view offset by *where* asynchronously. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The bitmap to draw onto the view. |
| `where` | The location to draw the bitmap in the view's coordinate system. |





**Since:** BeOS R3

---

### `DrawBitmapAsync()`

```cpp
void BView::DrawBitmapAsync(const BBitmap * bitmap, BRect bitmapRect, BRect viewRect)
```

Draws *bitmap* on the view within *viewRect* asynchronously. *bitmap* portion is scaled to fit *viewRect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The bitmap to draw onto the view. |
| `bitmapRect` | The portion of the bitmap to draw in the bitmap's coordinate system. |
| `viewRect` | The area in the view's coordinate system to draw the bitmap in. |





**Since:** BeOS R3

---

### `DrawBitmapAsync()`

```cpp
void BView::DrawBitmapAsync(const BBitmap * bitmap, BRect bitmapRect, BRect viewRect, uint32 options)
```

Draws *bitmap* on the view within *viewRect* asynchronously. *bitmap* portion is scaled to fit *viewRect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The bitmap to draw onto the view. |
| `bitmapRect` | The portion of the bitmap to draw in the bitmap's coordinate system. |
| `viewRect` | The area in the view's coordinate system to draw the bitmap in. |
| `options` | combination of *bitmap_drawing_options* flags |





**Since:** Haiku R1

---

### `DrawBitmapAsync()`

```cpp
void BView::DrawBitmapAsync(const BBitmap * bitmap, BRect viewRect)
```

Draws *bitmap* on the view within *viewRect* asynchronously. *bitmap* is scaled to fit *viewRect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The bitmap to draw onto the view. |
| `viewRect` | The area in the view's coordinate system to draw the bitmap in. |





**Since:** BeOS R3

---

### `DrawChar()`

```cpp
void BView::DrawChar(char c)
```

Draws character *c* onto to the view at the current pen position. 


The character is drawn in the view's current font.


Parameters

| Parameter | Description |
| :--- | :--- |
| `c` | The character to draw. |





**Since:** BeOS R3

---

### `DrawChar()`

```cpp
void BView::DrawChar(char c, BPoint location)
```

Draws character *c* at the specified *location* in the view. 


The character is drawn in the view's current font.


Parameters

| Parameter | Description |
| :--- | :--- |
| `c` | The character to draw. |
| `location` | The location in the view to draw the character. |





**Since:** BeOS R3

---

### `DrawingMode()`

```cpp
drawing_mode BView::DrawingMode()const
```

Return the current drawing_mode. 



**Returns:** The current drawing_mode.



**Since:** BeOS R3

---

### `DrawPicture()`

```cpp
void BView::DrawPicture(const BPicture * picture)
```

Draws the *picture* at the view's current pen position. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `picture` | The [BPicture](classBPicture.md) object to draw. |





**Since:** BeOS R3

---

### `DrawPicture()`

```cpp
void BView::DrawPicture(const BPicture * picture, BPoint where)
```

Draws the *picture* at the location in the view specified by *where*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `picture` | The [BPicture](classBPicture.md) object to draw. |
| `where` | The point on the view to draw *picture*. |





**Since:** BeOS R3

---

### `DrawPicture()`

```cpp
void BView::DrawPicture(const char * filename, long offset, BPoint where)
```

Draws the *picture* from the file specified by *filename* offset by *offset* bytes at the location in the view specified by *where*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `filename` | The filename of the file containing the picture to draw. |
| `where` | The point on the view to draw the picture. |
| `offset` | The number of bytes to offset in the file to find the picture. |





**Since:** BeOS R4

---

### `DrawPictureAsync()`

```cpp
void BView::DrawPictureAsync(const BPicture * picture)
```

Draws the *picture* at the view's current pen position. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `picture` | The [BPicture](classBPicture.md) object to draw. |





**Since:** BeOS R5

---

### `DrawPictureAsync()`

```cpp
void BView::DrawPictureAsync(const BPicture * picture, BPoint where)
```

Draws the *picture* at the location in the view specified by *where*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `picture` | The [BPicture](classBPicture.md) object to draw. |
| `where` | The point on the view to draw *picture*. |





**Since:** BeOS R5

---

### `DrawPictureAsync()`

```cpp
void BView::DrawPictureAsync(const char * filename, long offset, BPoint where)
```

Draws the *picture* from the file specified by *filename* offset by *offset* bytes at the location in the view specified by *where*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `filename` | The filename of the file containing the picture to draw. |
| `where` | The point on the view to draw the picture. |
| `offset` | The number of bytes to offset in the file to find the picture. |





**Since:** BeOS R5

---

### `DrawString()`

```cpp
void BView::DrawString(const char * string, BPoint location, escapement_delta * delta = NULL)
```

Draw *string* onto the view at the specified *location* in the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to draw. |
| `location` | The location in the view to draw the string. |
| `delta` | Adds additional width to each character according to the following fields: * nonspace(float) The amount of width to add to characters with visible glyphs.  * space(float) The amount of width to add to characters with escapements but don't have visible glyphs. |





**Since:** BeOS R3

---

### `DrawString()`

```cpp
void BView::DrawString(const char * string, const BPoint * locations, int32 locationCount)
```

Draw *string* *locationCount* times at the specified *locations*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to draw. |
| `locations` | A pointer to an array of [BPoint](classBPoint.md) objects to draw the string. |
| `locationCount` | The number of elements in *locations*. |





**Since:** Haiku R1

---

### `DrawString()`

```cpp
void BView::DrawString(const char * string, escapement_delta * delta = NULL)
```

Draw *string* onto the view at the current pen position. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to draw. |
| `delta` | Adds additional width to each character according to the following fields: * nonspace(float) The amount of width to add to characters with visible glyphs.  * space(float) The amount of width to add to characters with escapements but don't have visible glyphs. |





**Since:** BeOS R3

---

### `DrawString()`

```cpp
void BView::DrawString(const char * string, int32 length, BPoint location, escapement_delta * delta = 0L)
```

Draw *string* up to *length* characters onto the view at the specified *location* in the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to draw. |
| `length` | The maximum number of characters in *string* to draw. |
| `location` | The location in the view to draw the string. |
| `delta` | Adds additional width to each character according to the following fields: * nonspace(float) The amount of width to add to characters with visible glyphs.  * space(float) The amount of width to add to characters with escapements but don't have visible glyphs. |





**Since:** BeOS R3

---

### `DrawString()`

```cpp
void BView::DrawString(const char * string, int32 length, const BPoint * locations, int32 locationCount)
```

Draw *string* up to *length* characters *locationCount* times at the specified *locations*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to draw. |
| `length` | The maximum number of characters in *string* to draw. |
| `locations` | A pointer to an array of [BPoint](classBPoint.md) objects to draw the string. |
| `locationCount` | The number of elements in *locations*. |





**Since:** Haiku R1

---

### `DrawString()`

```cpp
void BView::DrawString(const char * string, int32 length, escapement_delta * delta = NULL)
```

Draw *string* up to *length* characters onto the view at the current pen position. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to draw. |
| `length` | The maximum number of characters in *string* to draw. |
| `delta` | Adds additional width to each character according to the following fields: * nonspace(float) The amount of width to add to characters with visible glyphs.  * space(float) The amount of width to add to characters with escapements but don't have visible glyphs. |





**Since:** BeOS R3

---

### `DrawTiledBitmap()`

```cpp
void BView::DrawTiledBitmap(const BBitmap * bitmap, BRect viewRect, BPoint phase = B_ORIGIN)
```

Draws *bitmap* on the view within *viewRect*. If *bitmap* is smaller, it is cloned to fill remaining space in *viewRect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The bitmap to draw onto the view. |
| `viewRect` | The area in the view's coordinate system to draw the bitmap in. |
| `phase` | Source bitmap offset used as starting point for drawing. |





**Since:** Haiku R1

---

### `DrawTiledBitmapAsync()`

```cpp
void BView::DrawTiledBitmapAsync(const BBitmap * bitmap, BRect viewRect, BPoint phase = B_ORIGIN)
```

Draws *bitmap* on the view within *viewRect* asynchronously. If *bitmap* is smaller, it is cloned to fill remaining space in *viewRect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The bitmap to draw onto the view. |
| `viewRect` | The area in the view's coordinate system to draw the bitmap in. |
| `phase` | Source bitmap offset used as starting point for drawing. |





**Since:** Haiku R1

---

### `EnableLayoutInvalidation()`

```cpp
void BView::EnableLayoutInvalidation()
```

Enable layout invalidation. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Since:** Haiku R1

---

### `EndLayer()`

```cpp
void BView::EndLayer()
```

Finish a layer and blend it in with the view. 


This is the counterpart to [BeginLayer()](classBView.md#abe65757b7c83c8db390bf0c87457a343). You can nest multiple layer. If this method is called and the current layer is nested in another layer, the current layer is applied to the layer above. If this is the only layer, it will directly blend in to the main view.



**See also:** [BeginLayer()](classBView.md#abe65757b7c83c8db390bf0c87457a343)



**Since:** Haiku R`

---

### `EndLineArray()`

```cpp
void BView::EndLineArray()
```

End the line array drawing the lines. 



**Since:** BeOS R3

---

### `EndPicture()`

```cpp
BPicture * BView::EndPicture()
```

Ends the drawing instruction recording session and returns the [BPicture](classBPicture.md) object passed to [BeginPicture()](classBView.md#a14155192773aad22ebe47a9975afac5f) or [AppendToPicture()](classBView.md#a2d73d2f2b0b35390929cf54fbfa5ecff). 



**Returns:** The [BPicture](classBPicture.md) object passed to [BeginPicture()](classBView.md#a14155192773aad22ebe47a9975afac5f) or [AppendToPicture()](classBView.md#a2d73d2f2b0b35390929cf54fbfa5ecff).



**Since:** BeOS R3

---

### `EndRectTracking()`

```cpp
void BView::EndRectTracking()
```

Ends tracking removing the outline rectangle from the view. 


[BeginRectTracking()](classBView.md#ac1eb1eeee67ec97205a4acc6955185bd) is typically called from the [MouseDown()](classBView.md#a5f5bd975d15df94f2ebbc80eb79cc3f6) while this method is typically called from the [MouseUp()](classBView.md#acdb92b30069157b2e3c522a3ef9d6ae4) method.



**Since:** BeOS R3

---

### `EventMask()`

```cpp
uint32 BView::EventMask()
```

Returns the current event mask. 



**Returns:** The current event mask as a uint32.



**See also:** [SetEventMask()](classBView.md#a5d8d6b469a8a11a577d1d138cfc31162)



**Since:** BeOS R5

---

### `ExplicitAlignment()`

```cpp
BSize BView::ExplicitAlignment()const
```

Returns the explicit alignment size. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).
This returns the value that was set by [SetExplicitAlignment()](classBView.md#a6906e47d4fdd6923dd51edb60a83ccea).



**Since:** Haiku R1

---

### `ExplicitMaxSize()`

```cpp
BSize BView::ExplicitMaxSize()const
```

Returns the explicit maximum size. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).
This returns the value that was set by [SetExplicitMaxSize()](classBView.md#acd759dd7505050f9cbd8213c71991b8b).



**Since:** Haiku R1

---

### `ExplicitMinSize()`

```cpp
BSize BView::ExplicitMinSize()const
```

Returns the explicit minimum size. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).
This returns the value that was set by [SetExplicitMinSize()](classBView.md#abfcb5c761f9b06da3b4a6788aad5d0ee).



**Since:** Haiku R1

---

### `ExplicitPreferredSize()`

```cpp
BSize BView::ExplicitPreferredSize()const
```

Returns the explicit preferred size. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).
This returns the value that was set by [SetExplicitPreferredSize()](classBView.md#a98b7d450210099ed59b7cd34f2575e20).



**Since:** Haiku R1

---

### `FillArc()`

```cpp
void BView::FillArc(BPoint center, float xRadius, float yRadius, float startAngle, float arcAngle, ::pattern pattern = B_SOLID_HIGH)
```

Fill an arc starting at *center* with a horizontal radius of *xRadius* and a vertical radius of *yRadius* starting at *startAngle* and drawing *arcAngle* degrees. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | The center point. |
| `xRadius` | The horizontal radius. |
| `yRadius` | The vertical radius. |
| `startAngle` | The angle to begin drawing at. |
| `arcAngle` | The number of degrees of the arc to draw. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `FillArc()`

```cpp
void BView::FillArc(BPoint center, float xRadius, float yRadius, float startAngle, float arcAngle, const BGradient & gradient)
```

Fill an arc with the specified *gradient* pattern starting at *center* with a horizontal radius of *xRadius* and a vertical radius of *yRadius* starting at *startAngle* and drawing *arcAngle* degrees. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | The center point. |
| `xRadius` | The horizontal radius. |
| `yRadius` | The vertical radius. |
| `startAngle` | The angle to begin drawing at. |
| `arcAngle` | The number of degrees of the arc to draw. |
| `gradient` | The gradient pattern to fill the arc with. |





**Since:** Haiku R1

---

### `FillArc()`

```cpp
void BView::FillArc(BRect rect, float startAngle, float arcAngle, ::pattern pattern = B_SOLID_HIGH)
```

Fill an arc inscribed within *rect* starting at startAngle and drawing *arcAngle* degrees. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The area within which to inscribe the shape. |
| `startAngle` | The angle to begin drawing at. |
| `arcAngle` | The number of degrees of the arc to draw. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `FillArc()`

```cpp
void BView::FillArc(BRect rect, float startAngle, float arcAngle, const BGradient & gradient)
```

Fill an arc with the specified *gradient* pattern inscribed within *rect* starting at startAngle and drawing *arcAngle* degrees. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The area within which to inscribe the shape. |
| `startAngle` | The angle to begin drawing at. |
| `arcAngle` | The number of degrees of the arc to draw. |
| `gradient` | The gradient pattern to fill the arc with. |





**Since:** Haiku R1

---

### `FillBezier()`

```cpp
void BView::FillBezier(BPoint * controlPoints, ::pattern pattern = B_SOLID_HIGH)
```

Fill a bezier curve. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `controlPoints` | The list of points that form the bezier curve. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `FillBezier()`

```cpp
void BView::FillBezier(BPoint * controlPoints, const BGradient & gradient)
```

Fill a bezier curve. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `controlPoints` | The list of points that form the bezier curve. |
| `gradient` | The gradient pattern to fill the bezier curve with. |





**Since:** Haiku R1

---

### `FillEllipse()`

```cpp
void BView::FillEllipse(BPoint center, float xRadius, float yRadius, ::pattern pattern = B_SOLID_HIGH)
```

Fill an ellipse starting at *center* with a horizontal radius of *xRadius* and a vertical radius of *yRadius*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | The center point. |
| `xRadius` | The horizontal radius. |
| `yRadius` | The vertical radius. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `FillEllipse()`

```cpp
void BView::FillEllipse(BPoint center, float xRadius, float yRadius, const BGradient & gradient)
```

Fill an ellipse with the specified *gradient* pattern starting at *center* with a horizontal radius of *xRadius* and a vertical radius of *yRadius*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | The center point. |
| `xRadius` | The horizontal radius. |
| `yRadius` | The vertical radius. |
| `gradient` | The gradient pattern to fill the ellipse with. |





**Since:** Haiku R1

---

### `FillEllipse()`

```cpp
void BView::FillEllipse(BRect rect, ::pattern pattern = B_SOLID_HIGH)
```

Fill an ellipse inscribed within *rect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The area within which to inscribe the shape. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `FillEllipse()`

```cpp
void BView::FillEllipse(BRect rect, const BGradient & gradient)
```

Fill an ellipse with the specified *gradient* pattern inscribed within *rect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The area within which to inscribe the shape. |
| `gradient` | The gradient pattern to fill the ellipse with. |





**Since:** Haiku R1

---

### `FillPolygon()`

```cpp
void BView::FillPolygon(const BPoint * pointArray, int32 numPoints, ::pattern pattern = B_SOLID_HIGH)
```

Fill a polygon shape made up of points specified by *pointArray*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `pointArray` | An array of points that specify the vertices of the polygon. |
| `numPoints` | The number of points in *pointArray*. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `FillPolygon()`

```cpp
void BView::FillPolygon(const BPoint * pointArray, int32 numPoints, BRect bounds, ::pattern pattern = B_SOLID_HIGH)
```

Fill a polygon shape made up of points specified by *pointArray* inscribed by *bounds*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `pointArray` | An array of points that specify the vertices of the polygon. |
| `numPoints` | The number of points in *pointArray*. |
| `bounds` | The smallest rectangle that encloses the points in *pointArray*. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `FillPolygon()`

```cpp
void BView::FillPolygon(const BPoint * pointArray, int32 numPoints, BRect bounds, const BGradient & gradient)
```

Fill a polygon shape made up of points specified by *pointArray* inscribed by *bounds* with the specified *gradient* pattern. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `pointArray` | An array of points that specify the vertices of the polygon. |
| `numPoints` | The number of points in *pointArray*. |
| `bounds` | The smallest rectangle that encloses the points in *pointArray*. |
| `gradient` | The gradient pattern to fill the polygon with. |





**Since:** Haiku R1

---

### `FillPolygon()`

```cpp
void BView::FillPolygon(const BPoint * pointArray, int32 numPoints, const BGradient & gradient)
```

Fill a polygon shape made up of points specified by *pointArray* with the specified *gradient* pattern. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `pointArray` | An array of points that specify the vertices of the polygon. |
| `numPoints` | The number of points in *pointArray*. |
| `gradient` | The gradient pattern to fill the polygon with. |





**Since:** Haiku R1

---

### `FillPolygon()`

```cpp
void BView::FillPolygon(const BPolygon * polygon, ::pattern pattern = B_SOLID_HIGH)
```

Fill a polygon shape. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `polygon` | The polygon shape to fill. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `FillPolygon()`

```cpp
void BView::FillPolygon(const BPolygon * polygon, const BGradient & gradient)
```

Fill a polygon shape with the specified *gradient* pattern. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `polygon` | The polygon shape to fill. |
| `gradient` | The gradient pattern to fill the polygon with. |





**Since:** Haiku R1

---

### `FillRect()`

```cpp
void BView::FillRect(BRect rect, ::pattern pattern = B_SOLID_HIGH)
```

Fill the rectangle specified by *rect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The rectangular area to fill. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `FillRect()`

```cpp
void BView::FillRect(BRect rect, const BGradient & gradient)
```

Fill the rectangle specified by *rect* with the specified *gradient* pattern. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The rectangular area to fill. |
| `gradient` | The gradient pattern to fill the rectangle with. |





**Since:** Haiku R1

---

### `FillRegion()`

```cpp
void BView::FillRegion(BRegion * region, ::pattern pattern = B_SOLID_HIGH)
```

Fill *region*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `region` | The *region* to fill. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `FillRegion()`

```cpp
void BView::FillRegion(BRegion * region, const BGradient & gradient)
```

Fill *region* with the specified *gradient* pattern. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `region` | The *region* to fill. |
| `gradient` | The gradient pattern to fill the *region* with. |





**Since:** Haiku R1

---

### `FillRoundRect()`

```cpp
void BView::FillRoundRect(BRect rect, float xRadius, float yRadius, ::pattern pattern = B_SOLID_HIGH)
```

Fill the rounded rectangle with horizontal radius *xRadius* and vertical radius *yRadius*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The rectangular area to fill the round rect within. |
| `xRadius` | The horizontal radius. |
| `yRadius` | The vertical radius. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `FillRoundRect()`

```cpp
void BView::FillRoundRect(BRect rect, float xRadius, float yRadius, const BGradient & gradient)
```

Fill the rounded rectangle with horizontal radius *xRadius* and vertical radius *yRadius* with the specified *gradient* pattern. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The rectangular area to fill the round rect within. |
| `xRadius` | The horizontal radius. |
| `yRadius` | The vertical radius. |
| `gradient` | The gradient pattern to fill the round rect with. |





**Since:** Haiku R1

---

### `FillRule()`

```cpp
int32 BView::FillRule()const
```

Return the current fill mode. 


See [BView::SetFillRule()](classBView.md#a2019def93337069c0b7d416e103522e9) for more information.



**Returns:** Returns `0` if no fill rule is applied, `B_EVEN_ODD` when the even-odd algorithm is applied, and `B_NONZERO` if the nonzero algorithm is applied.



**Since:** Haiku R1

---

### `FillShape()`

```cpp
void BView::FillShape(BShape * shape, ::pattern pattern = B_SOLID_HIGH)
```

Fill *shape*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `shape` | The *shape* to fill. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R5

---

### `FillShape()`

```cpp
void BView::FillShape(BShape * shape, const BGradient & gradient)
```

Fill *shape* with the specified *gradient* pattern. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `shape` | The *shape* to fill. |
| `gradient` | The gradient pattern to fill the *shape* with. |





**Since:** Haiku R1

---

### `FillTriangle()`

```cpp
void BView::FillTriangle(BPoint point1, BPoint point2, BPoint point3, ::pattern pattern = B_SOLID_HIGH)
```

Fill the triangle specified by points *point1*, *point2*, and *point3*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point1` | The first point of the triangle. |
| `point2` | The second point of the triangle. |
| `point3` | The third point of the triangle. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `FillTriangle()`

```cpp
void BView::FillTriangle(BPoint point1, BPoint point2, BPoint point3, BRect bounds, ::pattern pattern = B_SOLID_HIGH)
```

Fill the triangle specified by points *point1*, *point2*, and *point3* and enclosed by *bounds*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point1` | The first point of the triangle. |
| `point2` | The second point of the triangle. |
| `point3` | The third point of the triangle. |
| `bounds` | The rectangular area that encloses the triangle. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `FillTriangle()`

```cpp
void BView::FillTriangle(BPoint point1, BPoint point2, BPoint point3, BRect bounds, const BGradient & gradient)
```

Fill the triangle specified by points *point1*, *point2*, and *point3* and enclosed by *bounds* with the specified *gradient* pattern. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point1` | The first point of the triangle. |
| `point2` | The second point of the triangle. |
| `point3` | The third point of the triangle. |
| `bounds` | The rectangular area that encloses the triangle. |
| `gradient` | The gradient pattern to fill the triangle with. |





**Since:** Haiku R1

---

### `FillTriangle()`

```cpp
void BView::FillTriangle(BPoint point1, BPoint point2, BPoint point3, const BGradient & gradient)
```

Fill the triangle specified by points *point1*, *point2*, and *point3* with the specified *gradient* pattern. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point1` | The first point of the triangle. |
| `point2` | The second point of the triangle. |
| `point3` | The third point of the triangle. |
| `gradient` | The gradient pattern to fill the triangle with. |





**Since:** Haiku R1

---

### `FindView()`

```cpp
BView * BView::FindView(const char * name)const
```

Returns the view in the view hierarchy with the specified *name*. 



**Returns:** The view in the view hierarchy with the specified *name* or `NULL` if not found.



**Since:** BeOS R3

---

### `Flags()`

```cpp
uint32 BView::Flags()const
```

Return the view flags set in the constructor or by [SetFlags()](classBView.md#a4740f9a1e1163073b042102a421a2e33). 



**Returns:** The view flags as a uint32 mask.



**See also:** [SetFlags()](classBView.md#a4740f9a1e1163073b042102a421a2e33)



**Since:** BeOS R3

---

### `Flush()`

```cpp
void BView::Flush()const
```

Flushes the attached window's connection to App Server. 



> [!NOTE]
> If the view isn't attached to a window, [Flush()](classBView.md#a15465930f84d2d01f7818bd79bc91c3e) does nothing.



**Since:** BeOS R3

---

### `ForceFontAliasing()`

```cpp
void BView::ForceFontAliasing(bool enable)
```

Turn anti-aliasing on and off when printing. 


Typically want to turn font anti-aliasing off when printing by passing `true` to this method and then turn it on again by passing in `false`.


This method does not affect characters drawn to the screen.


Parameters

| Parameter | Description |
| :--- | :--- |
| `enable` | If `true` turn off anti-aliasing, if `false` turn on anti-aliasing. |





**Since:** BeOS R5

---

### `Frame()`

```cpp
BRect BView::Frame()const
```

Returns the view's frame rectangle in the parent's coordinate system. 



**Returns:** The view's frame rectangle in the parent's coordinate system.



**Since:** BeOS R3

---

### `FrameMoved()`

```cpp
void BView::FrameMoved(BPoint newPosition)
```

Hook method called when the view is moved. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `newPosition` | The point of the top left corner of the frame that the view has been moved to. |





**Since:** BeOS R3


Reimplemented in [BScrollBar](classBScrollBar.md#a8df64f7d9446f0e16c262d85391ce3dc), [BBox](classBBox.md#a4819e27795b8eb141fda945cea2c9d60), [BButton](classBButton.md#ac37b4c9e5a10b431ac7f31127c9829b5), [BCheckBox](classBCheckBox.md#a05c84e5cb90d5c53800c06c7c07c7b77), [BColorControl](classBColorControl.md#ac9b14ded26d0ae66803e4cc369837a32), [BDragger](classBDragger.md#a7c4ed6ef7d4716c1485a45496a3fecbe), [BListView](classBListView.md#aeed214d88c70fa121e1531a6c2cb9ba3), [BMenuBar](classBMenuBar.md#aa711264d76e8f5faa0f974ca66d01ccf), [BOutlineListView](classBOutlineListView.md#ab061fa01aa2099c3373b80861d0b34ba), [BPictureButton](classBPictureButton.md#a14c03727cfd9c1847a0234d0b2ac16f8), [BPopUpMenu](classBPopUpMenu.md#a29c0fbffd038df9bd3f79f328e074151), [BRadioButton](classBRadioButton.md#a3015f2ec4ab3786f83a233cb4da692c8), [BScrollView](classBScrollView.md#a7ee9706e9e9396eb7ecb64eadaabc1f9), [BStatusBar](classBStatusBar.md#ac6087674bae1c74b62c4887bb4d2107d), [BStringView](classBStringView.md#a8a1935f9fb051794420522c8235fec00), [BTabView](classBTabView.md#af1b6043bcdb3372a0800aa3a086b8218), [BTextControl](classBTextControl.md#aa3744f364427ae9af55b5193187a3fc2), [BMenu](classBMenu.md#ab14bf3dc8b6f082f2609094c1f964577), and [BMenuField](classBMenuField.md#ad35f91192f1f6986007a2234f42d6638).

---

### `FrameResized()`

```cpp
void BView::FrameResized(float newWidth, float newHeight)
```

Hook method called when the view is resized. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `newWidth` | The new width of the view. |
| `newHeight` | The new height of the view. |





**Since:** BeOS R3


Reimplemented in [BButton](classBButton.md#a5f2aca854bb9226c6c1dd37e693d89b4), [BChannelControl](classBChannelControl.md#a8fbfdedacf261023b38c28fc117cf6b5), [BCheckBox](classBCheckBox.md#a083ff4719c3168c853625441e618022f), [BColorControl](classBColorControl.md#a79dbf99fcaa48fd47a6c93c34d9c693a), [BDragger](classBDragger.md#a791b0c635b45d78c16441b243c86cfd2), [BListView](classBListView.md#af4fdd5e524c68a7aa318179c8a5acadd), [BMenuBar](classBMenuBar.md#ad3dcc7b2c1eeada95ef6986a21754324), [BOutlineListView](classBOutlineListView.md#af22b2e83a0298300f46e33c1319ca151), [BPictureButton](classBPictureButton.md#a5b0b8225164361af12fc689aeae751fd), [BPopUpMenu](classBPopUpMenu.md#a68d7f27c2a0e69a6b0396af02579217e), [BRadioButton](classBRadioButton.md#acd60fc8c7ad57a3c8388567d1172f120), [BScrollBar](classBScrollBar.md#ae3bc89d135f860a79da0850ca84a77f5), [BScrollView](classBScrollView.md#a554f85390c7e1d28f48fdabce9faa09b), [BStatusBar](classBStatusBar.md#a1ecc0c948356b2f6d180ce33712ae556), [BStringView](classBStringView.md#abcb433d9a1ccab609f133cbf93eacf45), [BTabView](classBTabView.md#adaacf9a6c7cc8d4afb23022b60bc71fb), [BTextControl](classBTextControl.md#a5da999355130852c6ff1cd3533e4cfcc), [BTextView](classBTextView.md#a77ca110829a03b040b59a784caf327fb), [BBox](classBBox.md#aa97074dae93cc40fc877b2c1e0da345f), [BChannelSlider](classBChannelSlider.md#a620b639a7f8051f8e47073873b2f0dd8), [BMenu](classBMenu.md#ad6d6eac1f12e9456b9db896aee122181), and [BMenuField](classBMenuField.md#a6c44f9eb74f2ae11ac2ac308a6e9bb5f).

---

### `GetBlendingMode()`

```cpp
void BView::GetBlendingMode(source_alpha * srcAlpha, alpha_function * alphaFunc)const
```

Fill out *srcAlpha* and *alphaFunc* with the alpha mode and alpha function of the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `srcAlpha` | The alpha mode to fill out. |
| `alphaFunc` | The alpha function to fill out. |





**Since:** BeOS R5

---

### `GetClippingRegion()`

```cpp
void BView::GetClippingRegion(BRegion * region)const
```

Fill out *region* with the view's clipping region. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `region` | The [BRegion](classBRegion.md) object to fill out. |




Get the current clipping region, which is an intersection of the view visible region on screen (which depends on the view bounds, any child view hiding parts of it, and overlapping windows) and the constrained clipping regions set by calls to [ConstrainClippingRegion()](classBView.md#a656b8d82a6a7c7c6ab33c3dd08aad6ec) in the current stack of drawing states.



**Since:** BeOS R3

---

### `GetFont()`

```cpp
void BView::GetFont(BFont * font)const
```

Fill out *font* with the font set to the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `font` | The [BFont](classBFont.md) object to fill out. |





**Since:** BeOS R3

---

### `GetFontHeight()`

```cpp
void BView::GetFontHeight(font_height * height)const
```

Fill out the [font_height](structfont__height.md) struct with the view font. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `height` | The [font_height](structfont__height.md) struct to fill out. |





**Since:** BeOS R3

---

### `GetHeightForWidth()`

```cpp
void BView::GetHeightForWidth(float width, float * min, float * max, float * preferred)
```

Returns the min, max and preferred height for a given width. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).
Parameters

| Parameter | Description |
| :--- | :--- |
| `width` | The width you want the height to be calculated for. |
| `min` | The minimum height that the layout will request. |
| `max` | The maximum height that the layout will request. |
| `preferred` | The preferred height for this *width*. |





**Since:** Haiku R1


Reimplemented in [BTextView](classBTextView.md#aec7881d97bdc508b01a6caa80f51d963).

---

### `GetLayout()`

```cpp
BLayout * BView::GetLayout()const
```

Get the layout of the view. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Returns:** The layout of the view.



**Since:** Haiku R1

---

### `GetMouse()`

```cpp
void BView::GetMouse(BPoint * _location, uint32 * _buttons, bool checkMessageQueue = true)
```

Fills out the cursor location and the current state of the mouse buttons. 


The cursor doesn't have to be located within the view for this method to work, however, the view must be attached to a window. Don't use this method to track the mouse in your derived view, implement [MouseMoved()](classBView.md#ac8b20516e42bab2f1eeb130e2432bde0) instead.


Parameters

| Parameter | Description |
| :--- | :--- |
| `_location` | Filled out with the cursor location in the view's coordinate system. |
| `_buttons` | Filled out with a mask of the following values: * `B_PRIMARY_MOUSE_BUTTON`  * `B_SECONDARY_MOUSE_BUTTON`  * `B_TERTIARY_MOUSE_BUTTON` |
| `checkMessageQueue` | If `true` pull from any pending [MouseMoved()](classBView.md#ac8b20516e42bab2f1eeb130e2432bde0) or [MouseUp()](classBView.md#acdb92b30069157b2e3c522a3ef9d6ae4) events in the message queue top down before filling out the current mouse cursor state. |





**Since:** BeOS R3

---

### `GetPreferredSize()`

```cpp
void BView::GetPreferredSize(float * _width, float * _height)
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


Reimplemented in [BBox](classBBox.md#abc3935933ba86ddfe9dacddce7fcf4b8), [BButton](classBButton.md#adba3ed10370f960a0a408413569adf30), [BChannelSlider](classBChannelSlider.md#a0f2838b9bd42bd8454658dbdd78b179b), [BCheckBox](classBCheckBox.md#aff828221de6947696a0b60d73241315c), [BColorControl](classBColorControl.md#a20210c9c80b0bfd88a0e6d5d89da0a64), [BControl](classBControl.md#a22455c705a4ed0fd09908b36a8dda3ae), [BDragger](classBDragger.md#acab77f447ccf51dedf686ea9e2c56fe1), [BListView](classBListView.md#af763f7195c72abd00143441bef002b25), [BMenu](classBMenu.md#af60a7b8ec6f92749fd46ce2e9179dc17), [BMenuBar](classBMenuBar.md#ab4dd370f1363d89c1fb2918877595b02), [BOptionPopUp](classBOptionPopUp.md#ae2fcf40dcd30ba8560ee3f737485fcc5), [BOutlineListView](classBOutlineListView.md#aa1b8b9ab01b3eb04a6e0fc1cd50833e4), [BPictureButton](classBPictureButton.md#a2f2dddfafa62ccea5770aab99893dae9), [BPopUpMenu](classBPopUpMenu.md#a68b1cc4ed9432b21e755bfe7b142efd3), [BRadioButton](classBRadioButton.md#a2129a420a7dfc70b6d9a97b1458764f6), [BScrollBar](classBScrollBar.md#ab5249d91d4f028b5a84a8074b0af2d0f), [BScrollView](classBScrollView.md#adc5802fb92fa7f72d4a50cb2314f9e8d), [BStatusBar](classBStatusBar.md#ae80597269df1aa5dfd4d07dba2c389fe), [BStringView](classBStringView.md#af068a3cc57ce813e92fecd498d106803), [BTabView](classBTabView.md#a331553465a07b7de9cef71e54d6b3ed0), [BTextControl](classBTextControl.md#a9ebbd271bca4c72ba2a5db8dc1876082), [BTextView](classBTextView.md#a5b31f120d4476b83beb08f3333cfc85d), [BMenuField](classBMenuField.md#a08fad29da3ccfb574bd4cf6fdc56b20b), [BSeparatorView](classBSeparatorView.md#af37a5222e47e1ab5429b8672926a6bd8), and [BChannelControl](classBChannelControl.md#aacccdb670d6553e5204c8ae317f6029a).

---

### `GetStringWidths()`

```cpp
void BView::GetStringWidths(char * stringArray[], int32 lengthArray[], int32 numStrings, float widthArray[])const
```

Fill out widths of the strings in *stringArray* set in the font of the view into *widthArray*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `stringArray` | The array of strings to get the lengths of. |
| `lengthArray` | The number of characters of the strings in *stringArray* to consider. |
| `numStrings` | The number of strings in *stringArray*. |
| `widthArray` | The array to store the widths of the strings in *stringArray*. |





**Since:** BeOS R3

---

### `GetSupportedSuites()`

```cpp
status_t BView::GetSupportedSuites(BMessage * data)
```

Reports the suites of messages and specifiers that derived classes understand.  



**Since:** BeOS R3


Reimplemented from [BHandler](../application_kit/classBHandler.md#acf34435dada239f411e8e034e0ea36b5).


Reimplemented in [BChannelControl](classBChannelControl.md#abfb5744f9faf08ed02d22a33ae9e9ab8), [BChannelSlider](classBChannelSlider.md#affd29de4f880e122c72d4d3b25b7ed9d), [BColorControl](classBColorControl.md#a5f10efed53781673b0f5a3f40b7d527d), [BDragger](classBDragger.md#a9d014b5632dfd7c4dbb43f45ea2175ef), [BListView](classBListView.md#acc1fa37e73b342b27d16e13aa3d3024a), [BMenu](classBMenu.md#a2aa0277374bacf3b7644f738bc064637), [BMenuBar](classBMenuBar.md#ad635f7e68997f901cbd4b15491b5f2a3), [BMenuField](classBMenuField.md#ad765cb012c296a6f676e070c80c929e3), [BOutlineListView](classBOutlineListView.md#a293dd0ed9a59c56ddd2738981c6c48b6), [BPictureButton](classBPictureButton.md#a08e86268e927d332501bee63892fb2bd), [BPopUpMenu](classBPopUpMenu.md#aab6d894d982b8841569be6d5766b88e2), [BStatusBar](classBStatusBar.md#afd6b9bb4d38d8c418d3f0aa65a84aea3), [BStringView](classBStringView.md#ab294fcbe6b75394cb2cd4d6db1a908c4), [BTextControl](classBTextControl.md#a9281b5fa852c3fe841bc7f102a96078a), [BTextView](classBTextView.md#a9cb6a32b918a5c90489b6fb7e27fcb6a), [BBox](classBBox.md#ab1ff66b8efec609137264522016f09c6), [BButton](classBButton.md#af912fac07ee02f90a12a4011e5a493cb), [BCheckBox](classBCheckBox.md#a6075229f070c3723a0fc102e7984e8f2), [BControl](classBControl.md#a3b545ffe2ee04f62eaa567582225adba), [BRadioButton](classBRadioButton.md#a513f368c4eb7c7d1aa81da79bee492ea), [BScrollBar](classBScrollBar.md#a543695199844d6b485ab0cb43c65a950), [BScrollView](classBScrollView.md#ae23327464d7c7db975defe845c4cfdf9), and [BTabView](classBTabView.md#aed45f36a1cdcc1bb23fc964714cbe20d).

---

### `GetToolTipAt()`

```cpp
bool BView::GetToolTipAt(BPoint point, BToolTip ** _tip)
```

Point *_tip* with the view's tool tip. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | Currently unused. |
| `_tip` | A pointer to a pointer to a BToolTip object to set. |





**Since:** Haiku R1

---

### `HasDefaultColors()`

```cpp
bool BView::HasDefaultColors()const
```

Tests if the view has any colors set. 



**Returns:** Boolean value, true if colors are not set.



**Since:** Haiku R1


Referenced by [BLayoutBuilder::Grid< ParentBuilder >::Grid()](classBLayoutBuilder_1_1Grid.md#a2542130d43283c471cee9f13523b9ee0), and [BLayoutBuilder::Group< ParentBuilder >::Group()](classBLayoutBuilder_1_1Group.md#ace860b547d56684445905033b112945e).

---

### `HasHeightForWidth()`

```cpp
bool BView::HasHeightForWidth()
```

Returns whether the layout of the view can calculate a height for a given width. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).
Use [GetHeightForWidth()](classBView.md#ad34bee968b1ec98a0bf89343340b6b07) to actually get the preferred size.



**Returns:** `true` if the height values can be calculated, `false` if they cannot.



**Since:** Haiku R1


Reimplemented in [BTextView](classBTextView.md#a099a44a6619914db20a02a6ccf611b70).

---

### `HasSystemColors()`

```cpp
bool BView::HasSystemColors()const
```

Tests if the view is using system "panel" colors. B_PANEL_BACKGROUND_COLOR for [ViewUIColor()](classBView.md#aec6c89446eb4f5ded151adced9126df8) B_PANEL_BACKGROUND_COLOR for [LowUIColor()](classBView.md#ae32ca6d8f106d44b5b51df82a7eb64c5) B_PANEL_TEXT_COLOR for [HighUIColor()](classBView.md#aa86f548fba2e82d022066198be6d5af6) 



**Returns:** Boolean value, true if colors are as described.



**Since:** Haiku R1

---

### `Hide()`

```cpp
void BView::Hide()
```

Hides the view without removing it from the view hierarchy. 


Calls to [Hide()](classBView.md#a7688dc04178a2955950154ee3670d029) and [Show()](classBView.md#a06e0584057d6c7a7c7e048b6272b7016) are cumulative. A visible view becomes hidden once the number of [Hide()](classBView.md#a7688dc04178a2955950154ee3670d029) calls exceeds the number of [Show()](classBView.md#a06e0584057d6c7a7c7e048b6272b7016) calls.



**See also:** [Show()](classBView.md#a06e0584057d6c7a7c7e048b6272b7016)



**Since:** BeOS R3


Reimplemented in [BMenu](classBMenu.md#acebb809699f7efa7d72346f2ba0b869f), and [BMenuBar](classBMenuBar.md#a7dfa53005734435d3b805161e3495e99).

---

### `HideToolTip()`

```cpp
void BView::HideToolTip()
```

Hide the view's tool tip. 



**Since:** Haiku R1

---

### `HighColor()`

```cpp
rgb_color BView::HighColor()const
```

Return the current high color. 



**Returns:** The current high color as an [rgb_color](structrgb__color.md) struct.



**See also:** [SetHighColor(rgb_color)](classBView.md#ab5482f91a642d545bc3fcefe199f95e9)



**Since:** BeOS R3

---

### `HighUIColor()`

```cpp
color_which BView::HighUIColor(float * tint = NULL)const
```

Return the current high color constant being used. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `tint` | Optional float pointer in which to store the tint value used to modify the system color constant. |





**Returns:** The current high color constant.



**See also:** [SetHighUIColor(color_which, float)](classBView.md#a54eefc28bf7a4bc30612cf83aff2963b)



**Since:** Haiku R1

---

### `Instantiate()`

```cpp
BArchivable * BView::Instantiate(BMessage * data)
```

Creates a new [BView](classBView.md) object from the *data* message. 



**Returns:** A newly created [BView](classBView.md) object or `NULL` if the message doesn't contain an archived [BView](classBView.md).



**Since:** BeOS R3

---

### `Invalidate()`

```cpp
void BView::Invalidate()
```

Sends a message to App Server to redraw the view. 



**Since:** BeOS R3

---

### `Invalidate()`

```cpp
void BView::Invalidate(BRect invalRect)
```

Sends a message to App Server to redraw the portion of the view specified by *invalRect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `invalRect` | The rectangular area of the view to redraw. |





**Since:** BeOS R3

---

### `Invalidate()`

```cpp
void BView::Invalidate(const BRegion * region)
```

Sends a message to App Server to redraw the portion of the view specified by *region*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `region` | The region of the view to redraw. |





**Since:** Haiku R1

---

### `InvalidateLayout()`

```cpp
void BView::InvalidateLayout(bool descendants = false)
```

Invalidate layout. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).
Parameters

| Parameter | Description |
| :--- | :--- |
| `descendants` | Also invalidate its children views. |





**Since:** Haiku R1

---

### `InvertRect()`

```cpp
void BView::InvertRect(BRect rect)
```

Inverts the colors within *rect*. 


This method is often used to draw a highlighted selection in a view.


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The rectangular area in the view to invert the colors of. |





**Since:** BeOS R3

---

### `IsFocus()`

```cpp
bool BView::IsFocus()const
```

Returns whether or not the view is the window's current focus view. 


The focus view changes as the user moves from one view to another either by pushing the tab key or by clicking a new view with the mouse. The change can be made programmatically via the [MakeFocus()](classBView.md#a266a368d81c6e1668b2b9b22b5016853) method.



**Returns:** `true` if the view is the current focus view, `false` otherwise.



**See also:** [MakeFocus()](classBView.md#a266a368d81c6e1668b2b9b22b5016853)



**Since:** BeOS R3

---

### `IsHidden()`

```cpp
bool BView::IsHidden()const
```

Returns whether or not the view is hidden. 


A view can be hidden either by calling [Hide()](classBView.md#a7688dc04178a2955950154ee3670d029) on the view, calling [Hide()](classBView.md#a7688dc04178a2955950154ee3670d029) on a parent view or calling [Hide()](classBView.md#a7688dc04178a2955950154ee3670d029) on the window that the view is attached to. When a [BWindow](classBWindow.md) or [BView](classBView.md) is hidden, all its descendants are also hidden.


This method only returns whether the view or an ancestor view has had the [Hide()](classBView.md#a7688dc04178a2955950154ee3670d029) method called on it, it doesn't consider if the view is obscured by another view or is off-screen. A [BView](classBView.md) is not hidden by default.



**Returns:** `true` if the view was hidden via the [Hide()](classBView.md#a7688dc04178a2955950154ee3670d029) method, `false` otherwise.



**Since:** BeOS R3

---

### `IsHidden()`

```cpp
bool BView::IsHidden(const BView * lookingFrom)const
```

Returns whether or not the view is hidden from the perspective of *lookingFrom*. 


A view is considered hidden if it, any of its parent views, or the window it's attached to has had the [Hide()](classBView.md#a7688dc04178a2955950154ee3670d029) method called on it. This method allows you to determine the hidden status of a view from a different point on the view hierarchy.


Parameters

| Parameter | Description |
| :--- | :--- |
| `lookingFrom` | The view used as a base when determining the hidden status of the [BView](classBView.md) object. |





**Returns:** `true` if the view was hidden via the [Hide()](classBView.md#a7688dc04178a2955950154ee3670d029) method, `false` otherwise.



**Since:** Haiku R1

---

### `IsLayoutInvalidationDisabled()`

```cpp
bool BView::IsLayoutInvalidationDisabled()
```

Returns whether or not layout invalidation is disabled. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Returns:** `true` of layout invalidation is disabled, `false` otherwise.



**Since:** Haiku R1

---

### `IsLayoutValid()`

```cpp
bool BView::IsLayoutValid()const
```

Returns whether or not the layout is valid. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Returns:** Returns `true` if the layout is valid, `false` otherwise.



**Since:** Haiku R1

---

### `IsPrinting()`

```cpp
bool BView::IsPrinting()const
```

Returns whether or not the view is drawing to a printer. 


This method should only be called from the [Draw()](classBView.md#aa55014241fc2f5556415850692b52db2) or [DrawAfterChildren()](classBView.md#abb50623b4236926b068fc5a2264f6a48) methods. If called from any other method this method returns `false`.


The view may choose different fonts, images, or colors when drawing to a printer vs. when drawing to the screen.



**Returns:** Returns `true` if drawing to a printer, `false` otherwise.



**Since:** BeOS R3

---

### `KeyDown()`

```cpp
void BView::KeyDown(const char * bytes, int32 numBytes)
```

Hook method called when a keyboard key is pressed. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bytes` | The bytes of the key combination pressed. |
| `numBytes` | The number of bytes in *bytes*. |





**Since:** BeOS R3


Reimplemented in [BButton](classBButton.md#a1946a6658404aef5e374bf37e0d276ad), [BChannelSlider](classBChannelSlider.md#acea7a9db888f42a0a20640efd9ad0a4b), [BCheckBox](classBCheckBox.md#a4b02a354633080c08f03bdf39e1bdec6), [BColorControl](classBColorControl.md#a94675a83e628146d8bb9670064d59242), [BControl](classBControl.md#ade80a87b7da08e9b84b188c629ec36c8), [BListView](classBListView.md#aed97ff09a629d740b91c8f72dcf5893a), [BMenu](classBMenu.md#a6c50b44b2da8caf0280854c5a250b8c2), [BMenuField](classBMenuField.md#a9b47c6e428138e3bfc65a1407b82f003), [BOutlineListView](classBOutlineListView.md#a93a3143a1e783bf5a945bfc6b58e021f), [BPictureButton](classBPictureButton.md#a0a7cfc055ee00a2435f25138a5bbcd40), [BRadioButton](classBRadioButton.md#a2f39aded0be52643dd5f541f62699d34), [BTabView](classBTabView.md#a6eca83e00f1649fbe6b6aacd3f0f66f6), [BTextView](classBTextView.md#a38ae9b87206a3236527d533b1f33d951), and [BChannelControl](classBChannelControl.md#a37ac118342e3d4fe79faa33b88e56813).

---

### `KeyUp()`

```cpp
void BView::KeyUp(const char * bytes, int32 numBytes)
```

Hook method called when a keyboard key is released. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bytes` | The bytes of the key combination pressed. |
| `numBytes` | The number of bytes in *bytes*. |





**Since:** BeOS R3


Reimplemented in [BChannelSlider](classBChannelSlider.md#a6a6a90c05aac31c7397b2327d4ea503e).

---

### `Layout()`

```cpp
void BView::Layout(bool force)
```

Layout the view. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).
Parameters

| Parameter | Description |
| :--- | :--- |
| `force` | If `true` layout even if valid. |





**Since:** Haiku R1

---

### `LayoutAlignment()`

```cpp
BAlignment BView::LayoutAlignment()
```

Return the current BAlignemnt of the view. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Since:** Haiku R1


Reimplemented in [BBox](classBBox.md#a336367ab4358ddeed9f95db4fee229f0), [BCheckBox](classBCheckBox.md#a3b62d62f6255934ede8f2bc1667d68b1), [BRadioButton](classBRadioButton.md#a9778545b92c25d2a71d5e814ff9d9a86), [BStringView](classBStringView.md#a710f4021da87b0631b5ff608053eaa23), and [BTextControl](classBTextControl.md#a75c2cebeaff174fb233eba0fac012aa2).

---

### `LayoutChanged()`

```cpp
void BView::LayoutChanged()
```

Hook function that is called when the layout if this view, or one of its children, has changed. 



**Since:** Haiku R1

---

### `LayoutContext()`

```cpp
BLayoutContext * BView::LayoutContext()const
```

Returns the BLayoutContext for this View. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Since:** Haiku R1

---

### `LayoutInvalidated()`

```cpp
void BView::LayoutInvalidated(bool descendants = false)
```

Hook method called when the layout is invalidated. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `descendants` | Whether or not child views have also been invalidated. |





**Since:** Haiku R1


Reimplemented in [BMenu](classBMenu.md#ab5474abecef27e68bade9c58721caeed), [BMenuField](classBMenuField.md#afa552d1804b1dbb61fce69b420299c87), [BTextControl](classBTextControl.md#a1ed22bad67d0851ea6ff182f668170b3), [BTextView](classBTextView.md#ab97f9e2be3de9c163ed7b78a9fc7b74f), [BBox](classBBox.md#a6d872ad7b4e4cbc856a3f8b99435980b), [BButton](classBButton.md#a88a1584e52ce63d14ceb4e234ca38a5b), [BCheckBox](classBCheckBox.md#afe8a80323716afa23fa7273b7ea33680), [BScrollView](classBScrollView.md#acbba1a0ae23691d9e66e77a0034ab39f), and [BStringView](classBStringView.md#af715b4e73aa8b1683662081eb9458590).

---

### `LeftTop()`

```cpp
BPoint BView::LeftTop()const
```

Returns the left top corner point. 



**Returns:** The left top corner of the view as a [BPoint](classBPoint.md) object.



**Since:** BeOS R3

---

### `LineCapMode()`

```cpp
cap_mode BView::LineCapMode()const
```

Returns the current line cap mode. 



**Returns:** The current line cap mode set to the view.



**Since:** BeOS R3

---

### `LineJoinMode()`

```cpp
join_mode BView::LineJoinMode()const
```

Returns the current line join mode. 



**Returns:** The current line join mode set to the view.



**Since:** BeOS R3

---

### `LineMiterLimit()`

```cpp
float BView::LineMiterLimit()const
```

Returns the miter limit used for `B_MITER_JOIN` join mode. 



**Returns:** The current miter limit set to the view.



**Since:** BeOS R3

---

### `LowColor()`

```cpp
rgb_color BView::LowColor()const
```

Return the current low color. 



**Returns:** The current low color as an [rgb_color](structrgb__color.md) struct.



**See also:** [SetLowColor(rgb_color)](classBView.md#af0426243110fb150ad7ef0705209a12c)



**Since:** BeOS R3

---

### `LowUIColor()`

```cpp
color_which BView::LowUIColor(float * tint = NULL)const
```

Return the current low color constant being used. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `tint` | Optional float pointer in which to store the tint value used to modify the system color constant. |





**Returns:** The current low color constant.



**See also:** [SetLowUIColor(color_which, float)](classBView.md#a879ab88d4e64345069f1041d3a7b652f)



**Since:** Haiku R1

---

### `MakeFocus()`

```cpp
void BView::MakeFocus(bool focus = true)
```

Makes the view the current focus view of the window or gives up being the window's focus view. 


The focus view handles selections and KeyDown events when the the attached window is active. There can be only one focus view at a time per window.


When called with *focus* set to `true` this method first calls [MakeFocus()](classBView.md#a266a368d81c6e1668b2b9b22b5016853) on the previously focused view with *focus* set to `false`.


The focus doesn't automatically change when [MouseDown()](classBView.md#a5f5bd975d15df94f2ebbc80eb79cc3f6) is called so calling [MakeFocus()](classBView.md#a266a368d81c6e1668b2b9b22b5016853) is the only way to make a view the focus view of a window. Classes derived from [BView](classBView.md) that can display the current selection, or that can accept pasted data should call [MakeFocus()](classBView.md#a266a368d81c6e1668b2b9b22b5016853) in their [MouseDown()](classBView.md#a5f5bd975d15df94f2ebbc80eb79cc3f6) method to update the focus view of the window on click.


If the view isn't attached to a window this method has no effect.


Parameters

| Parameter | Description |
| :--- | :--- |
| `focus` | *true* to set focus, *false* to remove it. |





**Since:** BeOS R3


Reimplemented in [BButton](classBButton.md#abc826951b0a87f2ce4cf6cc10eb792d6), [BControl](classBControl.md#aaeeae39969b598868ad0e8d3298efb00), [BDragger](classBDragger.md#af9ed413edb8156285e2d24d39a3c4fac), [BMenu](classBMenu.md#a1465ef5881a0b85729118534d8ee3a15), [BOutlineListView](classBOutlineListView.md#acf402ab948510cbe880b2e24c72f39f9), [BPictureButton](classBPictureButton.md#a70245c6a6207a737c74a6092cc2374a6), [BRadioButton](classBRadioButton.md#a1f2f84e388730e3f018e0e16d682bf37), [BScrollBar](classBScrollBar.md#aa0a296f1afc18513b90a7c098871a39d), [BScrollView](classBScrollView.md#ae54f2e6e7844ddd7cf9c1b0531ae2ec2), [BStatusBar](classBStatusBar.md#a615c000a88cd8b09070b5ff39d0477ec), [BStringView](classBStringView.md#a5c53710add5a3e16dfa3df6da1a39396), [BTextControl](classBTextControl.md#abf98183ccf195db2a411dc5a1f67ee33), [BTextView](classBTextView.md#ac0bc816f13b04fd2ec2668c618ab8ca8), [BMenuField](classBMenuField.md#a14d9a763b0d621a78d0aa8abdabe1f7b), [BBox](classBBox.md#a2c7f7fe098d0b65c9ba74da19da268ab), [BCheckBox](classBCheckBox.md#a0b638537dadfd72221c21dbb6fd48a46), [BColorControl](classBColorControl.md#a82b299852c7650b09af6662581cedaae), [BTabView](classBTabView.md#a0bba5d8ebb1263111769df12ab9b4c2a), [BChannelSlider](classBChannelSlider.md#affd38edbaca04a9db31ef3e749b119e7), [BListView](classBListView.md#a35117bf3eb7d1f64b777d5371558c626), [BMenuBar](classBMenuBar.md#a170fbfdd3be7b9bdc750777f31c216c0), and [BPopUpMenu](classBPopUpMenu.md#a134b3710cbd69229b093803ddb11ba27).

---

### `MaxSize()`

```cpp
BSize BView::MaxSize()
```

Return the maximum size of the view. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Returns:** The maximum size of the view as a [BSize](classBSize.md).



**See also:** [BAbstractLayout::MaxSize()](classBAbstractLayout.md#ad1ea5d04a5c8028f8295efde7106a66c)



**Since:** Haiku R1


Reimplemented in [BBox](classBBox.md#a38328d48b00d81833726e192403d130d), [BButton](classBButton.md#adeda5a0a1e19c006c422690d7bcdbd8f), [BCheckBox](classBCheckBox.md#ad80098e5c252495f592180b20f233795), [BListView](classBListView.md#a54878f820deb4ccc692f49bd6e8ce5c0), [BMenu](classBMenu.md#a5f94df489ae102d0e377df3b63d9864a), [BMenuBar](classBMenuBar.md#ad0dc5e934924d2511d82718d31da2740), [BMenuField](classBMenuField.md#a2d7e95c1f408178fdc44973b34ac00c3), [BRadioButton](classBRadioButton.md#a839d35bb528c77cf7da2c764911c572c), [BScrollBar](classBScrollBar.md#abba5a7c71ab0802984e2d566861ebcac), [BScrollView](classBScrollView.md#a3d8a3a2d5fcd00fd0f666d89a377c463), [BSeparatorView](classBSeparatorView.md#ada179e44bcb71680c5ce2c146b317e13), [BStatusBar](classBStatusBar.md#a328bde08f9576175c07b80726989b07e), [BStringView](classBStringView.md#aefa705718677d0d50b07975bb012ae64), [BTabView](classBTabView.md#ac7ab32a3a7ab1326820f11dea6ce834d), [BTextControl](classBTextControl.md#a5bf08635cd24d52f3775f93a1526c072), and [BTextView](classBTextView.md#af8e32e9318d9368137940d2511d3dff2).

---

### `MessageReceived()`

```cpp
void BView::MessageReceived(BMessage * message)
```

Handle *message* received by the associated looper. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The *message* received by the associated looper. |





**See also:** [BHandler::MessageReceived()](../application_kit/classBHandler.md#aeecda5017e0081db617f23bbff71fb53)



**Since:** BeOS R3


Reimplemented from [BHandler](../application_kit/classBHandler.md#aeecda5017e0081db617f23bbff71fb53).


Reimplemented in [BBox](classBBox.md#a30d9348112e19b908181b037edc291de), [BButton](classBButton.md#a9954aa8549ffb7cddd1a401997fd07a7), [BChannelControl](classBChannelControl.md#a7c3c5174a2f31f0a24c3fe4258d372da), [BChannelSlider](classBChannelSlider.md#aa60391cfc92b6c1a59ae7e92aa1f5bae), [BCheckBox](classBCheckBox.md#a668832dfbcab06cad06d0fb7d9a6244a), [BColorControl](classBColorControl.md#a9cf939fb5e7ef82a70e0792ccc0cfc1f), [BControl](classBControl.md#a19960b4d0a96144f73065a6ea1f2f8e2), [BDragger](classBDragger.md#acdf8b8402a8e253ca24ab01ba63b914c), [BListView](classBListView.md#ac00efce3ca37ce6e89c3f3fb5717311c), [BMenu](classBMenu.md#aca12e6b863279cc62772ac13ef286d31), [BMenuBar](classBMenuBar.md#a7d7c1d1674e059b56c82c81e381d4455), [BMenuField](classBMenuField.md#ab73739dc3316044b9269718bd0852d39), [BOptionControl](classBOptionControl.md#a6bff9c89ab78d899edfb88d3f9e2300c), [BOptionPopUp](classBOptionPopUp.md#a05b397e2521fe0b10ae3a2b05e78acae), [BOutlineListView](classBOutlineListView.md#aad47f3bf68a98024413aa06a45b0bdad), [BPictureButton](classBPictureButton.md#a7b6a5dc266664f155b6191d101ce48cd), [BPopUpMenu](classBPopUpMenu.md#a4b5937dbd7baa9d98b5368d6de9ca23c), [BRadioButton](classBRadioButton.md#a2f07af2fe9eedce7ffecd2b29a4b5d6a), [BScrollBar](classBScrollBar.md#a8d578e9e134aeaafdc6dc542e2d214f7), [BScrollView](classBScrollView.md#ad06771333c1897571f984ca9e533b69d), [BSplitView](classBSplitView.md#ad4737f5224faa2d34c84299750ab92ec), [BStatusBar](classBStatusBar.md#aee4044255aaae32db5a0d8bc2046840d), [BStringView](classBStringView.md#a03521ef18f82081e3a54f404217c2c6c), [BTabView](classBTabView.md#a5827436caab3b27791f2280d2d151624), [BTextControl](classBTextControl.md#afad72eca02699a6577c4bc0949e1c9ae), and [BTextView](classBTextView.md#a4d7d7990e57ce7286f78698f27c89e60).

---

### `MinSize()`

```cpp
BSize BView::MinSize()
```

Return the minimum size of the view. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Returns:** The minimum size of the view as a [BSize](classBSize.md).



**See also:** [BAbstractLayout::MinSize()](classBAbstractLayout.md#a3f692cb3306ce726e3cc6d2771824cd5)



**Since:** Haiku R1


Reimplemented in [BBox](classBBox.md#a2bb8047e0854627edc2a0bf55579593b), [BButton](classBButton.md#a44d82f5e5ec77df79ab955d48eb2f6cd), [BCheckBox](classBCheckBox.md#ab707cfe81f2f0ada73095f381de1fbae), [BListView](classBListView.md#acd2a6419c6ccad9f8ea52e1c728b1b9b), [BMenu](classBMenu.md#a659643414ede82d0233e62ce9da4c01e), [BMenuBar](classBMenuBar.md#ae0781646adecf0bd08123868c40ee218), [BMenuField](classBMenuField.md#a0587347fb25e87748d7c5207a344e3c5), [BScrollBar](classBScrollBar.md#aa647bf7a279bccf66a3ed3dcd1a619dd), [BScrollView](classBScrollView.md#aaa698d664d8a04deacdf1e3364bcbd71), [BSeparatorView](classBSeparatorView.md#ad97ce589194d2dcd66f81aa0bb1e22dd), [BStatusBar](classBStatusBar.md#a05c3ae557bd438f61f9ac1d4c890237f), [BStringView](classBStringView.md#aa228a2e46e9c9404f9706e352d08d33b), [BTabView](classBTabView.md#a9833a3bdc0cca3508a099e7054943fe1), [BTextControl](classBTextControl.md#aa356d1fd68346c51002ae1f582b70ffd), and [BTextView](classBTextView.md#a3a03f5bff63cba54276025e3788520d9).

---

### `MouseDown()`

```cpp
void BView::MouseDown(BPoint where)
```

Hook method called when a mouse button is pressed. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `where` | The point on the screen where the mouse pointer is when the mouse button is pressed. |





**Since:** BeOS R3


Reimplemented in [BBox](classBBox.md#a52b8a5339fffe5749a9c18853fd8dd83), [BStringView](classBStringView.md#aebc567839113910f4e83363e779ffd88), [BButton](classBButton.md#a479d27a48b957709b47159360c04157f), [BChannelSlider](classBChannelSlider.md#a858647630d03d081d3a2817e00f2e548), [BCheckBox](classBCheckBox.md#a641e4f5e6cf5b87302af5feb146969a0), [BColorControl](classBColorControl.md#a45399dd2cd33d8761709ee9e378fab56), [BControl](classBControl.md#aae264c07bf8006acf1fa96ceedc5f74d), [BDragger](classBDragger.md#acc770fc2b6e0e248804252e4d11c234e), [BListView](classBListView.md#aad39bfe4a5db5d70a8adbf1c41b8edf3), [BMenuBar](classBMenuBar.md#a0aa84693746c1cfe671c48a4dcc654c6), [BMenuField](classBMenuField.md#a0f35ede494cc2169455c429798e575ae), [BOutlineListView](classBOutlineListView.md#ae974e26e01f4f31a2b7eb64d91f1a22b), [BPictureButton](classBPictureButton.md#aee724ca332fa7a49b2ea2fa5c680f8a4), [BPopUpMenu](classBPopUpMenu.md#a3683f05e2d65018ec35c684b6bca1c77), [BRadioButton](classBRadioButton.md#a0aef53a65bca065d5c23a254fbf87c82), [BScrollBar](classBScrollBar.md#a20e8f54dd49d2bd67f0415c9233dbc24), [BScrollView](classBScrollView.md#aa89bae025998624f2080d9f180bf4c94), [BSplitView](classBSplitView.md#a00b41035774b35159b7f0d33da769eeb), [BStatusBar](classBStatusBar.md#af19565c2448a379a5b9a71829fb7a7d9), [BTabView](classBTabView.md#a0300bd5b05234996a9eab7c6afc9479e), [BTextControl](classBTextControl.md#ab1a5a0a5efb5e08a1ec98432529f02d9), [BTextView](classBTextView.md#a581a2b2877b29d275771ae5010d6706d), and [BChannelControl](classBChannelControl.md#a00e4315bf31cfe8b0a071cf5766427a8).

---

### `MouseMoved()`

```cpp
void BView::MouseMoved(BPoint where, uint32 code, const BMessage * dragMessage)
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


Reimplemented in [BColorControl](classBColorControl.md#af1aa066eeb6541eaf1c3c72d72758a5d), [BBox](classBBox.md#a70dd1fd1fac643b8b95d51b199b894e5), [BStringView](classBStringView.md#a58b93d2ff9ba970bec85f1d2a886d6fd), [BButton](classBButton.md#a8ba8b18062ea15ecd55d83458885adf1), [BCheckBox](classBCheckBox.md#ac18ca09f358bcd8acf7c5c00572ddfd9), [BControl](classBControl.md#aafa3507bfcf6f058d269a6e3bd6d30be), [BListView](classBListView.md#aa83292db971a1bf0801d9669052c2b78), [BPictureButton](classBPictureButton.md#af8e6d077c64b703b0e939458508bdd75), [BRadioButton](classBRadioButton.md#a013acca6d097f0b6d889b9f8e32e5064), [BScrollBar](classBScrollBar.md#aadee76484a35dd25468d2d9a47ee84e8), [BScrollView](classBScrollView.md#aeaa4d0c426d9c2d536fc97ab21244442), [BTextView](classBTextView.md#a95bc494682c45ba41c457029639f2d55), [BChannelSlider](classBChannelSlider.md#a54f043d454c571fdc1291946c54ff214), [BDragger](classBDragger.md#ae1a96fefe6ad6ebd639d974493b9982d), [BMenuField](classBMenuField.md#acbd5b0849384a650560940de14b6e24b), [BPopUpMenu](classBPopUpMenu.md#ac15743e549a70af3f245ba0ef1e1dfad), [BStatusBar](classBStatusBar.md#ac81efe02e62ed0a58c1eee11d365158a), [BTabView](classBTabView.md#a482f5de48a2c17f2898b39602849a820), [BTextControl](classBTextControl.md#ae34f333c6ccd0ce7f98fe15a31973536), and [BSplitView](classBSplitView.md#ac8e0a72e43f68b840f3e52e125023f9d).

---

### `MouseUp()`

```cpp
void BView::MouseUp(BPoint where)
```

Hook method called when a mouse button is released. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `where` | The point on the screen where the mouse pointer is when the mouse button is released. |





> [!NOTE]
> Calling [GetMouse()](classBView.md#a830ce9cf2ac2ffb5f73f526ee5d6e53d) in [MouseUp()](classBView.md#acdb92b30069157b2e3c522a3ef9d6ae4) will return the new state of the mouse buttons (after the mouse button was released). If you want to know which button was released, you have to compare that with the previous state of the buttons, that you can memorize for example by calling [GetMouse()](classBView.md#a830ce9cf2ac2ffb5f73f526ee5d6e53d) in [MouseDown()](classBView.md#a5f5bd975d15df94f2ebbc80eb79cc3f6).



**Since:** BeOS R3


Reimplemented in [BBox](classBBox.md#aa493fe0b7f8c211747f8ad78d0490a30), [BColorControl](classBColorControl.md#a22dc58e1aebc262b91d105ae8db1b779), [BStringView](classBStringView.md#a53bd5b0c21fc5f55f7ebf239b3b5586c), [BButton](classBButton.md#abdf9eedcccc9bbf8edce48b32361a749), [BChannelSlider](classBChannelSlider.md#a0d9fccc6e4a04d86c1fbf78ae0cb6eba), [BCheckBox](classBCheckBox.md#ae24408c8af1f1e0792564b0bb4109547), [BControl](classBControl.md#aeef31f13aee4d5d0b3dbb0f7e12beb39), [BDragger](classBDragger.md#ab80ac5b1cb42d9f95ebb221c2fbb3573), [BListView](classBListView.md#a008356d002e19a7b3f2633e4298b4053), [BMenuBar](classBMenuBar.md#a4781bbe6cd7ccff992b0c12f2c4ea4b7), [BMenuField](classBMenuField.md#aee41e24ee5b2055a9714112d61b86b9d), [BOutlineListView](classBOutlineListView.md#a65d774552d88ba39b6c4bb5bcccb048a), [BPictureButton](classBPictureButton.md#a0770c7585a64a6c5cc1a960f2a01569b), [BPopUpMenu](classBPopUpMenu.md#ad3e5938c019d6cfdb070fa16a3b6142e), [BRadioButton](classBRadioButton.md#a8cfb56dd13ec44c09cf6b2790c155fc2), [BScrollBar](classBScrollBar.md#ac726ce78354c6c85dbe7c64f6db46e1d), [BScrollView](classBScrollView.md#a23f2e9f5ea9ccadf9d99799af63fa293), [BSplitView](classBSplitView.md#a6ff5943b9c00dc30a2803681f0aa08c2), [BStatusBar](classBStatusBar.md#a4c489713a857fa7e483c105da46012a7), [BTabView](classBTabView.md#a9f889b22d3b00132a15b82c6d322a21a), [BTextControl](classBTextControl.md#aa9f01c01c01799296e81f3a075890db5), and [BTextView](classBTextView.md#a72a0cd6839b541db996d751f240e59a1).

---

### `MoveBy()`

```cpp
void BView::MoveBy(float deltaX, float deltaY)
```

Moves the view *deltaX* pixels horizontally and *deltaY* pixels vertically in the parent view's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `deltaX` | The number of pixels to move the view horizontally. |
| `deltaY` | The number of pixels to move the view vertically. |





**Since:** BeOS R3

---

### `MovePenBy()`

```cpp
void BView::MovePenBy(float x, float y)
```

Move the pen by *x* pixels horizontally and *y* pixels vertically. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | The number of pixels to move the pen horizontally. |
| `y` | The number of pixels to move the pen vertically. |





**Since:** BeOS R3

---

### `MovePenTo()`

```cpp
void BView::MovePenTo(BPoint point)
```

Move the pen to *point* in the view's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | the location to move the pen to. |





**Since:** BeOS R3

---

### `MovePenTo()`

```cpp
void BView::MovePenTo(float x, float y)
```

Move the pen to the point specified by *x* and *y* in the view's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | The horizontal coordinate to move the pen to. |
| `y` | The vertical coordinate to move the pen to. |





**Since:** BeOS R3

---

### `MoveTo()`

```cpp
void BView::MoveTo(BPoint where)
```

Move the view to the location specified by *where* in the parent view's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `where` | The location to move the view to. |





**Since:** BeOS R3

---

### `MoveTo()`

```cpp
void BView::MoveTo(float x, float y)
```

Move the view to the coordinates specified by *x* in the horizontal dimension and *y* in the vertical dimension in the parent view's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | The horizontal coordinate to move the view to. |
| `y` | The vertical coordinate to move the view to. |





**Since:** BeOS R3

---

### `NextSibling()`

```cpp
BView * BView::NextSibling()const
```

Returns a pointer to the next sibling view. 



**Returns:** A pointer to the next sibling view or *NULL* if not found.



**Since:** BeOS R3

---

### `Origin()`

```cpp
BPoint BView::Origin()const
```

Returns the origin point in the view's coordinate system. 



**Returns:** The local origin point in the view's coordinate system.



**See also:** [SetOrigin()](classBView.md#a769e5fa6486adf12e7a3511ed372a06c)



**Since:** BeOS R3

---

### `Parent()`

```cpp
BView * BView::Parent()const
```

Returns a pointer to the view's parent. 



**Returns:** A pointer to the parent view or `NULL` if not attached.



**Since:** BeOS R3

---

### `PenLocation()`

```cpp
BPoint BView::PenLocation()const
```

Return the current pen location as a [BPoint](classBPoint.md) object. 



**Returns:** The current pen location in the view's coordinate system.



**See also:** [MovePenTo(BPoint)](classBView.md#acb61254a2121f569f6223a95cd835abd)



**Since:** BeOS R3

---

### `PenSize()`

```cpp
float BView::PenSize()const
```

Return the current pen size. 



**Returns:** The current pen size as a float.



**See also:** [SetPenSize()](classBView.md#a80ea4cb97d2e6e2c3088e610a9e157e6)



**Since:** BeOS R3

---

### `Perform()`

```cpp
status_t BView::Perform(perform_code code, void * _data)
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


Reimplemented from [BHandler](../application_kit/classBHandler.md#a4e6ebc7ebcb72855a1f0fee7bde99766).


Reimplemented in [BPopUpMenu](classBPopUpMenu.md#a8f92a8866c4ffd63cdfcf07957f5ba22), [BListView](classBListView.md#aa0afeb194104738a01c7e60195fe50d0), [BCheckBox](classBCheckBox.md#abcac265789890adbf485f42d34d8c8e3), [BDragger](classBDragger.md#ad47a007f4126b9847a315263aa64ad93), [BMenuBar](classBMenuBar.md#a4b8a4e16ace175bc3bad9d6ef6b42daf), [BOutlineListView](classBOutlineListView.md#acb2775731d5da2cf52995e4d0b75c1d6), [BPictureButton](classBPictureButton.md#a57e7eef2e379994c13b8c93eeb5cf3c5), [BSeparatorView](classBSeparatorView.md#af56310d344ae63781e6b299d56c34e99), [BTextView](classBTextView.md#a6519856e1dbf6e021911529b8a0a15c6), [BBox](classBBox.md#adcd9b77028e7c820ce29a8a9db950adb), [BButton](classBButton.md#aee74330d076b7b8487fe21443118b03d), [BCardView](classBCardView.md#aa784b33c5b2c62791cf86fa38d1704ba), [BControl](classBControl.md#a0b32524cd2abfb7ea37b9988b180c733), [BGridView](classBGridView.md#a1409f66c0dfe65882e3bfa3b0fe000dc), [BGroupView](classBGroupView.md#ad8e96a8f8d76e75b5bb6815866529112), [BMenu](classBMenu.md#a6dedb98c6ba5ffbc44893ff43785c93c), [BMenuField](classBMenuField.md#a78923e5f07ff7c288980a72f6a953001), [BScrollBar](classBScrollBar.md#adfb4e4e74d00970fd154c652e467b66e), [BScrollView](classBScrollView.md#a1bd8a27f2883ca0e6b5b9dde0e9e638a), [BSplitView](classBSplitView.md#a9aaf09f717a61303d5aca6e92d96b103), [BStatusBar](classBStatusBar.md#a4b9eb3ec267be64d9293af3b920c48de), [BTabView](classBTabView.md#a708fd8766fddb7b0cd72566c57c2977a), and [BRadioButton](classBRadioButton.md#a44c726ed88d3a132e9d3055ebf98f3e6).

---

### `PopState()`

```cpp
void BView::PopState()
```

Restores the drawing state from the stack. 



**Since:** BeOS R3

---

### `PreferredSize()`

```cpp
BSize BView::PreferredSize()
```

Return the preferred size of the view. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Returns:** The preferred size of the view as a [BSize](classBSize.md).



**See also:** [BAbstractLayout::PreferredSize()](classBAbstractLayout.md#af5f21d9900c85ca053dba3938bef3fd3)



**Since:** Haiku R1


Reimplemented in [BBox](classBBox.md#a6c675d6acd48626e736ef4a16171ff1d), [BButton](classBButton.md#abe79a7ea1bff9983c64108da1c065599), [BCheckBox](classBCheckBox.md#ac51f2d73b650b34eb0f39c5bb3822953), [BListView](classBListView.md#aa353bb8e9a5d229141134df2fa3eddaf), [BMenu](classBMenu.md#a03aad94d2eb22836823045530e58c052), [BMenuBar](classBMenuBar.md#ae3e3832dbc024a802a18c4253f01b05a), [BMenuField](classBMenuField.md#a2930a668aaf18292c83211e4ef8386e4), [BScrollBar](classBScrollBar.md#a6b402fb319ad6d0ebf457d0940e6d7bf), [BScrollView](classBScrollView.md#a09eddb487494a14a9b35dc7753d88b96), [BSeparatorView](classBSeparatorView.md#a549abf3d5fd609ad5dd5291c269407cd), [BStatusBar](classBStatusBar.md#afea297b1b756ac28e8f8cf273a699b30), [BStringView](classBStringView.md#abe9e0597018b1ad8312a921a46db9f69), [BTabView](classBTabView.md#a0a9aebb15a78aab7ffd6a9286a6e9dca), [BTextControl](classBTextControl.md#a36fbf916956c923dbb6f393a5503de30), and [BTextView](classBTextView.md#ad46589273b8c8acb8737efde58407d3d).

---

### `PreviousSibling()`

```cpp
BView * BView::PreviousSibling()const
```

Returns a pointer to the previous sibling view. 



**Returns:** A pointer to the previous sibling view or *NULL* if not found.



**Since:** BeOS R3

---

### `Pulse()`

```cpp
void BView::Pulse()
```

Hook method called when the view receives a `B_PULSE` message. 


An action is performed each time the App Server calls the [Pulse()](classBView.md#a0ae8ec3e94ee3d41cb329e3df6966566) method. The pulse rate is set by SetPulseRate(). You can implement [Pulse()](classBView.md#a0ae8ec3e94ee3d41cb329e3df6966566) to do anything you want. The default version does nothing. The pulse granularity is no better than once per 100,000 microseconds.



**See also:** SetPulseRate()



**Since:** BeOS R3


Reimplemented in [BTabView](classBTabView.md#ac5411bc039523eb177d52f9e1b357cbd), and [BTextView](classBTextView.md#ada90a85565bd3e6bbe130901299c6da8).

---

### `PushState()`

```cpp
void BView::PushState()
```

Saves the drawing state to the stack. 


The drawing state contains the following elements:


* local and global origins

* local and global scales

* local and global clipping regions

* the current drawing mode

* pen size and location

* the font context

* foreground and background color

* line cap and join modes

* miter limit

* stipple pattern



A new state context is created after [PushState()](classBView.md#a1dcb914cd0c6ef8d1291aa8492968d40) is called with a local scale at 0, a local origin at (0, 0), and no clipping region.



**Since:** BeOS R3

---

### `Relayout()`

```cpp
void BView::Relayout()
```

Relayout the view. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Since:** Haiku R1

---

### `RemoveChild()`

```cpp
bool BView::RemoveChild(BView * child)
```

Removes *child* from the view hierarchy. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `child` | The child view to remove. |





**Returns:** Whether or not *child* was removed from the view hierarchy.



**Since:** BeOS R3

---

### `RemoveSelf()`

```cpp
bool BView::RemoveSelf()
```

Removes the view and all child views from the view hierarchy. 



**Returns:** Whether or not the view was removed from the view hierarchy.



**Since:** BeOS R3

---

### `ResetLayoutInvalidation()`

```cpp
void BView::ResetLayoutInvalidation()
```

Service call for [BView](classBView.md) derived classes re-enabling [InvalidateLayout()](classBView.md#a4a711316094e43076a3f5478d937accf) notifications. 


[BLayout](classBLayout.md) and [BView](classBView.md) will avoid calling InvalidateLayout on views that have already been invalidated, but if the view caches internal layout information which it updates in methods other than [DoLayout()](classBView.md#a9d766a06d0885200c6ababba4c87808b), it has to invoke this method, when it has done so, since otherwise the information might become obsolete without the layout noticing.


This is only meaningful if the view is part of a [BLayout](classBLayout.md).



**Since:** Haiku R1

---

### `ResizeBy()`

```cpp
void BView::ResizeBy(float deltaWidth, float deltaHeight)
```

Resize the view by *deltaWidth* horizontally and *deltaHeight* vertically without moving the top left corner of the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `deltaWidth` | The number of pixels to resize the view by horizontally. |
| `deltaHeight` | The number of pixels to resize the view by vertically. |





**Since:** BeOS R3

---

### `ResizeTo()`

```cpp
void BView::ResizeTo(BSize size)
```

Resize the view to the dimension specified by *size*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `size` | The *size* to resize the view to. |





**Since:** Haiku R1

---

### `ResizeTo()`

```cpp
void BView::ResizeTo(float width, float height)
```

Resize the view to the specified *width* and *height*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `width` | The width to resize the view to. |
| `height` | The height to resize the view to. |





**Since:** BeOS R3

---

### `ResizeToPreferred()`

```cpp
void BView::ResizeToPreferred()
```

Resizes the view to its preferred size keeping the position of the left top corner constant. 



> [!WARNING]
> It is not recommended to use this method for views that are part of a [BLayout](classBLayout.md).



**Since:** BeOS R3


Reimplemented in [BBox](classBBox.md#ad3c5e6892dcda099198f1e12f3696f60), [BButton](classBButton.md#a6468013205fd98f26440cd63911b9b34), [BChannelControl](classBChannelControl.md#a6df6fe17dedbf19a1d4e868ad24410f6), [BCheckBox](classBCheckBox.md#a0dedbdd99597789621ef09bb4e8f4b2b), [BColorControl](classBColorControl.md#a4c2ba5009024549e36b6d06b68ece03c), [BControl](classBControl.md#ad25f5ce6f17b5fe6fd6347021e9222e4), [BDragger](classBDragger.md#ab9a21c6a7b2f4d818082dad1a258cd0d), [BListView](classBListView.md#aec8ab9ba29dffb6b14bfbc9530c88fbf), [BMenu](classBMenu.md#a90a8228da7623e8e991a2fc7dc0e8898), [BMenuBar](classBMenuBar.md#a7e846a6abc075a0db6305e86cbed1760), [BMenuField](classBMenuField.md#a33f83798e1f30279bba074a078a595d3), [BOptionPopUp](classBOptionPopUp.md#aa2c5587ec3c4202409b19a32b425ea08), [BOutlineListView](classBOutlineListView.md#a053c8871392cc82965ad42bb0302399c), [BPictureButton](classBPictureButton.md#ac16a945ef32c4ae9fc066fd066da1242), [BPopUpMenu](classBPopUpMenu.md#a9983fca5936e0ebcf728ac5af7cc1004), [BRadioButton](classBRadioButton.md#ab7975b6bd97b13278719aab270ca40de), [BScrollBar](classBScrollBar.md#adb49da3971427af671953b4b751ab97a), [BScrollView](classBScrollView.md#a391fff7c7d3bec75c877a7f4626afc4c), [BStatusBar](classBStatusBar.md#a202fddf87baa8bbda2638d19a36180b4), [BStringView](classBStringView.md#ad6d63a369f1e27649fb7f72c519a0fd1), [BTabView](classBTabView.md#ae71c385d5a612edaaac3aa2d43ecd959), [BTextControl](classBTextControl.md#a5072df60c0f2c20d5b1ff4a2dbecbe7b), and [BTextView](classBTextView.md#ae288597c33c40f5f42abfe3ed41fce86).

---

### `ResizingMode()`

```cpp
uint32 BView::ResizingMode()const
```

Returns the resizing mode flags mask set in the constructor or by [SetResizingMode()](classBView.md#a38d29ea581880c3978d7e50dcc851696). 



**Returns:** the current resizing mode flags as a uint32 mask.



**See also:** [SetResizingMode()](classBView.md#a38d29ea581880c3978d7e50dcc851696)



**Since:** BeOS R3

---

### `ResolveSpecifier()`

```cpp
BHandler * BView::ResolveSpecifier(BMessage * message, int32 index, BMessage * specifier, int32 what, const char * property)
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


Reimplemented from [BHandler](../application_kit/classBHandler.md#a76439ffaf84e65232698d2a4a3317d22).


Reimplemented in [BChannelSlider](classBChannelSlider.md#ab95b5eebb6adcc7502c856789f08b6d2), [BDragger](classBDragger.md#ad21b28192fb7b7005129b5f517209e99), [BMenu](classBMenu.md#adfd2e1d211f34a8ac748abb989adac48), [BMenuBar](classBMenuBar.md#ab8e2eb06afc52455be926b3cde21f935), [BMenuField](classBMenuField.md#a8af84b2aecbc3e6b3041e3ef70b36cfd), [BPopUpMenu](classBPopUpMenu.md#acefc54d0514f6efbe059d9a36b837fe1), [BStringView](classBStringView.md#af7522569583e8aea625adea9fc2471fc), [BTextView](classBTextView.md#a3e0e67bcd942c0b738043235e56fdf29), [BBox](classBBox.md#aa171ac58aa5857a404f9431e63ad6792), [BButton](classBButton.md#a16b56f270bcba826cd8a1eb043adb474), [BChannelControl](classBChannelControl.md#af12f883b6e60f2ea071bb18724593350), [BCheckBox](classBCheckBox.md#ae860f1cfc296c79754697d95fc289a9e), [BColorControl](classBColorControl.md#a2bc94c2bffc9dec2b1a844c21833cb93), [BControl](classBControl.md#a084be37bbc0c49627c42a078c4b4dac8), [BListView](classBListView.md#a2c6144558d144fd5b134021de4c01183), [BOutlineListView](classBOutlineListView.md#a835a18d28691bdc9daad7cf0598e8a5f), [BPictureButton](classBPictureButton.md#a8553ac7d4f76b03d53dce14073cb50de), [BRadioButton](classBRadioButton.md#a767171da7c902ec3e06d19951f8b1404), [BScrollBar](classBScrollBar.md#abcf203657944c36c94a4a55e59338c8a), [BScrollView](classBScrollView.md#a6565e85e02890afd9e37f22935bf01b1), [BStatusBar](classBStatusBar.md#a930eda32bb19c6fb583a95947bc4eec9), [BTabView](classBTabView.md#a2d18bd3eeb63be72e3954b6d58cf3809), and [BTextControl](classBTextControl.md#a666a6fd256b57c98f9e75b3c19a03a89).

---

### `RotateBy()`

```cpp
void BView::RotateBy(double angleRadians)
```

Rotate the current view by *angleRadians*. 


The rotation is applied to the current transformation, not instead of, so it is an additive action.



**See also:** See [Transform()](classBView.md#ab16cc72cf8ae3b40abcf1f714e7e9b74) to get the current transformations, [SetTransform()](classBView.md#afbd9b8f35226ba89980c450f7626fc85), [ScaleBy()](classBView.md#ac83f9fdfb882f849e3ac79bfb06a0fd6) and [TranslateBy()](classBView.md#a8ae6d4e1cdfeeee33b753d56bee6ae7f) for additional transformation options.



**Since:** Haiku R1

---

### `Scale()`

```cpp
float BView::Scale()const
```

Return the current drawing scale. 



**Returns:** The current drawing scale.



**Since:** BeOS R3

---

### `ScaleBy()`

```cpp
void BView::ScaleBy(double x, double y)
```

Scale the current view by factors *x* and *y*. 


The scaling with factors *x* and *y* are applied to the current transformation, not instead of, so it is an additive action.



**See also:** See [Transform()](classBView.md#ab16cc72cf8ae3b40abcf1f714e7e9b74) to get the current transformations, [SetTransform()](classBView.md#afbd9b8f35226ba89980c450f7626fc85), [TranslateBy()](classBView.md#a8ae6d4e1cdfeeee33b753d56bee6ae7f) and [RotateBy()](classBView.md#a02ab6b6196b140b20ae516a55680e30b) for additional transformation options.



**Since:** Haiku R1

---

### `ScrollBar()`

```cpp
BScrollBar * BView::ScrollBar(orientation posture)const
```

Returns the [BScrollBar](classBScrollBar.md) object that has the [BView](classBView.md) set as its target. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `posture` | Either `B_VERTICAL` to get the vertical scroll bar or `B_HORIZONTAL` to get the horizontal scroll bar. |





**Returns:** the Scrollbar object requested or `NULL` if none found.



**See also:** [BScrollBar::SetTarget()](classBScrollBar.md#ade9625dc766b03f674b02116286d8bd8)



**Since:** BeOS R3

---

### `ScrollBy()`

```cpp
void BView::ScrollBy(float deltaX, float deltaY)
```

Scroll the view by *deltaX* horizontally and *deltaY* vertically. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `deltaX` | The amount to scroll horizontally. |
| `deltaY` | The amount to scroll vertically. |





**Since:** BeOS R3

---

### `ScrollTo()`

```cpp
void BView::ScrollTo(BPoint where)
```

Scroll the view to the point specified by *where*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `where` | The location to scroll the view to. |





**Since:** BeOS R3


Reimplemented in [BListView](classBListView.md#a13605eb8e35d09d2795281e541aa5784).

---

### `ScrollTo()`

```cpp
void BView::ScrollTo(float x, float y)
```

Scroll the view to the point specified by coordinates. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | The x-coordinate to scroll the view to. |
| `y` | The y-coordinate to scroll the view to. |





**Since:** BeOS R3


References [ScrollTo()](classBView.md#a33ed2a9eeff474a756b548996a82b964).


Referenced by [ScrollTo()](classBView.md#a33ed2a9eeff474a756b548996a82b964).

---

### `ScrollWithMouseWheelDelta()`

```cpp
void BView::ScrollWithMouseWheelDelta(BScrollBar * scrollBar, float delta)
```

Handle the scroll wheel changing over scrollbars. 



* Extract the scrollbar change based on the mouse wheel *delta* into a protected method of [BView](classBView.md).

* The method is called from the [MessageReceived()](classBView.md#aca0a16b0e04288e1fdc0b63690ea7a6d) method of [BScrollBar](classBScrollBar.md).



With this change it is now a bit easier to scroll horizontally around the system by putting the mouse cursor over a horizontal scrollbar and using the wheel.



**Since:** Haiku R1

---

### `SetBlendingMode()`

```cpp
void BView::SetBlendingMode(source_alpha srcAlpha, alpha_function alphaFunc)
```

Set the blending mode which controls how transparency is used. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `srcAlpha` | Set to one of the following: * `B_CONSTANT_ALPHA` Use the high color's alpha channel.  * `B_PIXEL_ALPHA` Use the alpha value of each pixel when drawing a bitmap. |
| `alphaFunc` | Set to one of the following: * `B_ALPHA_OVERLAY` Used for drawing a image with transparency over an opaque background.  * `B_ALPHA_COMPOSITE_*` Used to composite two or more transparent images together offscreen to produce a new image drawn using `B_ALPHA_OVERLAY` mode. |





> [!NOTE]
> Modes other than `B_ALPHA_OVERLAY` and `B_ALPHA_COMPOSITE` work only with `B_PIXEL_ALPHA`.



**Since:** BeOS R5

---

### `SetDiskMode()`

```cpp
void BView::SetDiskMode(char * filename, long offset)
```

Unimplemented. 



**Since:** Haiku R1

---

### `SetDrawingMode()`

```cpp
void BView::SetDrawingMode(drawing_mode mode)
```

Sets the drawing mode of the view. 


The default drawing mode is `B_OP_COPY`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `mode` | Set to one of the following: * `B_OP_COPY`  * `B_OP_OVER`  * `B_OP_ERASE`  * `B_OP_INVERT`  * `B_OP_SELECT`  * `B_OP_ALPHA`  * `B_OP_MIN`  * `B_OP_MAX`  * `B_OP_ADD`  * `B_OP_SUBTRACT`  * `B_OP_BLEND` |





**Since:** BeOS R3

---

### `SetEventMask()`

```cpp
status_t BView::SetEventMask(uint32 mask, uint32 options = 0)
```

Sets whether or not the view can accept mouse and keyboard events when not in focus. 


If *mask* includes `B_POINTER_EVENTS` then the view will receive mouse events even when the mouse isn't over the view and if it includes `B_KEYBOARD_EVENTS` the view will receive keyboard events even if it isn't in focus.


The *options* mask options are as follows:


* `B_NO_POINTER_HISTORY` Tells App Server to only send the most recent [MouseMoved()](classBView.md#ac8b20516e42bab2f1eeb130e2432bde0) event to the view sacrificing some granularity.

* `B_FULL_POINTER_HISTORY` Tells App Server to send all [MouseMoved()](classBView.md#ac8b20516e42bab2f1eeb130e2432bde0) events to the view.



Parameters

| Parameter | Description |
| :--- | :--- |
| `mask` | The *mask* of `B_POINTER_EVENTS` and `B_KEYBOARD_EVENTS` to set. |
| `options` | Sets other event-handling options. |





**Returns:** `B_OK` if everything went fine or an error code, usually `B_ERROR` if something went wrong.



**See also:** [EventMask()](classBView.md#a8851d500773c732ddbb1a4b31f0ad664)



**Since:** BeOS R5

---

### `SetExplicitAlignment()`

```cpp
void BView::SetExplicitAlignment(BAlignment alignment)
```

Set this view's alignment, to be used by Alignment(). 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**See also:** [BAbstractLayout::SetExplicitAlignment()](classBAbstractLayout.md#a3e7f4071b63452d77210f852cb92604d)



**Since:** Haiku R1

---

### `SetExplicitMaxSize()`

```cpp
void BView::SetExplicitMaxSize(BSize size)
```

Set this view's max size, to be used by [MaxSize()](classBView.md#ad1f1843a380e850948cf7e4ed2d5f1ba). 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**See also:** [BAbstractLayout::SetExplicitMaxSize()](classBAbstractLayout.md#aeb41b2e1e0b6414d0de4eeb4e5fb93e4)



**Since:** Haiku R1

---

### `SetExplicitMinSize()`

```cpp
void BView::SetExplicitMinSize(BSize size)
```

Set this view's min size, to be used by [MinSize()](classBView.md#acfb0cffde35b853dab6bc5d1bb03265f). 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**See also:** [BAbstractLayout::SetExplicitMinSize()](classBAbstractLayout.md#af63e5777fabfb9be1f29286bf6931fe6)



**Since:** Haiku R1

---

### `SetExplicitPreferredSize()`

```cpp
void BView::SetExplicitPreferredSize(BSize size)
```

Set this view's preferred size, to be used by [PreferredSize()](classBView.md#a7f51d63e71b60a2721d04436ffbcfe36). 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**See also:** [BAbstractLayout::SetExplicitPreferredSize()](classBAbstractLayout.md#a577b9839ac8e726bbecc7f3e40bb01a3)



**Since:** Haiku R1

---

### `SetExplicitSize()`

```cpp
void BView::SetExplicitSize(BSize size)
```

Set this view's size. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).
This is a convenience function that calls both [SetExplicitMinSize()](classBView.md#abfcb5c761f9b06da3b4a6788aad5d0ee) and [SetExplicitMaxSize()](classBView.md#acd759dd7505050f9cbd8213c71991b8b) with the *size* parameter.



**Since:** Haiku R1

---

### `SetFillRule()`

```cpp
void BView::SetFillRule(int32 rule)
```

Sets the fill rule for the view. 


A fill rule is a rule that describes an algorithm that is used to find out what the inside of a shape is. The concept comes from the SVG format.


See [the Mozilla documentation on the fill property of SVG](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/fill-rule) for more information.


Parameters

| Parameter | Description |
| :--- | :--- |
| `rule` | There are two algorithms: the `B_NONZERO` and the `B_EVEN_ODD` algorithm. |





**Since:** Haiku R1

---

### `SetFlags()`

```cpp
void BView::SetFlags(uint32 flags)
```

Sets the view flags to the *flags* mask. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `flags` | The view flags to set as a uint32 mask. |





**See also:** [Flags()](classBView.md#a561b10abf94dd65a26b02253af667508)



**Since:** BeOS R3


Reimplemented in [BTabView](classBTabView.md#a15a7a76d27f6faff9faedd740b10f485), and [BTextControl](classBTextControl.md#af5c66bb6443a999c9cfa3a4be1cad091).

---

### `SetFont()`

```cpp
void BView::SetFont(const BFont * font, uint32 mask = B_FONT_ALL)
```

Set the font of the view. 


By passing `B_FONT_ALL` to the *mask* parameter as is the default all font properties from *font* are set on the view.


Parameters

| Parameter | Description |
| :--- | :--- |
| `font` | A pointer to a const [BFont](classBFont.md) object to set on the view. |
| `mask` | A mask to determine what font properties to set, either pass in `B_FONT_ALL` to set all font properties or create a mask containing one or more of the following values to set: * `B_FONT_FAMILY_AND_STYLE`  * `B_FONT_SPACING`  * `B_FONT_SIZE`  * `B_FONT_ENCODING`  * `B_FONT_SHEAR`  * `B_FONT_FACE`  * `B_FONT_ROTATION`  * `B_FONT_FLAGS` |





**See also:** [BFont](classBFont.md) for more details.



**Since:** BeOS R3


Reimplemented in [BChannelControl](classBChannelControl.md#ac410bc781b8679e529663607a4134951), [BChannelSlider](classBChannelSlider.md#af208806038eee0044da24f6b8ebe1d5c), [BListView](classBListView.md#a7b0bd589bd4b1fb410b6e007fe107c62), and [BStringView](classBStringView.md#a57563eb3072229d1739fd91a10b991d7).

---

### `SetFontSize()`

```cpp
void BView::SetFontSize(float size)
```

Set the size of the view's font to *size*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `size` | The font size to set to the view in points. |





**Since:** BeOS R3

---

### `SetHighColor()`

```cpp
void BView::SetHighColor(rgb_color color)
```

Set the high color of the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `color` | The color to set. |





**Since:** BeOS R3


Referenced by [SetHighColor()](classBView.md#aff9e1ab5e88f33027e72b39874868e9b).

---

### `SetHighColor()`

```cpp
void BView::SetHighColor(uchar red, uchar green, uchar blue, uchar alpha = 255)
```

Set the high color of the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `red` | The *red* component of the high color. |
| `green` | The *green* component of the high color. |
| `blue` | The *blue* component of the high color. |
| `alpha` | The *alpha* component of the high color. |





**Since:** BeOS R3


References [rgb_color::alpha](structrgb__color.md#a089265e492dbf6743a6eaaa23fa94699), [rgb_color::blue](structrgb__color.md#adbc9af28f1ec74ac8e7cc8f7fc1e6ce3), [rgb_color::green](structrgb__color.md#ac0259068653969121d72739ad8509979), [rgb_color::red](structrgb__color.md#ad8f118f509b77a245d9e38829336f0ec), and [SetHighColor()](classBView.md#ab5482f91a642d545bc3fcefe199f95e9).

---

### `SetHighUIColor()`

```cpp
void BView::SetHighUIColor(color_which which, float tint = B_NO_TINT)
```

Set the high color of the view to a system constant. The color will update live with user changes. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `which` | The color_which constant to set. |
| `tint` | Optional tint value to use. |





**Since:** Haiku R1

---

### `SetLayout()`

```cpp
void BView::SetLayout(BLayout * layout)
```

Sets the *layout* of the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `layout` | The *layout* to set. |





**Since:** Haiku R1


Reimplemented in [BCardView](classBCardView.md#a1865908cb88618262b8b830f4d87f137), [BColorControl](classBColorControl.md#a9af6daf0d381071e52cc2876871da6d4), [BGridView](classBGridView.md#a336f566b4745de0f3331dd8fdc90e9fd), [BGroupView](classBGroupView.md#a6cfb414319ec6bf1134b908253ed5122), and [BSplitView](classBSplitView.md#aaee57e8169084b071c518adfbac4d97a).


Referenced by [BLayoutBuilder::Cards< ParentBuilder >::Cards()](classBLayoutBuilder_1_1Cards.md#ab6c081cb9ee9b90230621b2972d003a8), [BLayoutBuilder::Grid< ParentBuilder >::Grid()](classBLayoutBuilder_1_1Grid.md#a2542130d43283c471cee9f13523b9ee0), and [BLayoutBuilder::Group< ParentBuilder >::Group()](classBLayoutBuilder_1_1Group.md#ace860b547d56684445905033b112945e).

---

### `SetLineMode()`

```cpp
void BView::SetLineMode(cap_mode lineCap, join_mode lineJoin, float miterLimit = B_DEFAULT_MITER_LIMIT)
```

Set line mode to use PostScript-style line cap and join modes. 


*lineCap* determines the shape of the endpoints of stroked paths while *lineJoin* determines the shape of the corners where two lines meet.


The default miter limit is 10.0 which gives an angle of 11.478341°.


Parameters

| Parameter | Description |
| :--- | :--- |
| `lineCap` | One of the following: * `B_ROUND_CAP` A semicircle with diameter of line width is drawn at the endpoint.  * `B_BUTT_CAP` A straight edge is drawn without extending beyond the endpoint.  * `B_SQUARE_CAP` A straight edge is drawn extending past the endpoint by half the line width. |
| `lineJoin` | One of the following: * `B_ROUND_JOIN` Same as `B_ROUND_CAP` but for a join.  * `B_MITER_JOIN` The lines are extended until they meet. If angle that they meet at is greater than the 2*arcsin(1/*miterLimit*) than a bevel join is used instead.  * `B_BEVEL_JOIN` The area between the caps is filled with a triangle.  * `B_BUTT_JOIN` Same as `B_BUTT_CAP` but for a join.  * `B_SQUARE_JOIN` Same as `B_SQUARE_CAP` but for a join. |
| `miterLimit` | Sets the cut off angle before a miter join becomes a bevel join calculated by 2*arcsin(1/*miterLimit*). |





**Since:** BeOS R3

---

### `SetLowColor()`

```cpp
void BView::SetLowColor(rgb_color color)
```

Set the low color of the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `color` | The color to set. |





**Since:** BeOS R3


Referenced by [SetLowColor()](classBView.md#a929fb1ca47a00220c355ae55a0ea6077).

---

### `SetLowColor()`

```cpp
void BView::SetLowColor(uchar red, uchar green, uchar blue, uchar alpha = 255)
```

Set the low color of the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `red` | The *red* component of the low color. |
| `green` | The *green* component of the low color. |
| `blue` | The *blue* component of the low color. |
| `alpha` | The *alpha* component of the low color. |





**Since:** BeOS R3


References [rgb_color::alpha](structrgb__color.md#a089265e492dbf6743a6eaaa23fa94699), [rgb_color::blue](structrgb__color.md#adbc9af28f1ec74ac8e7cc8f7fc1e6ce3), [rgb_color::green](structrgb__color.md#ac0259068653969121d72739ad8509979), [rgb_color::red](structrgb__color.md#ad8f118f509b77a245d9e38829336f0ec), and [SetLowColor()](classBView.md#af0426243110fb150ad7ef0705209a12c).

---

### `SetLowUIColor()`

```cpp
void BView::SetLowUIColor(color_which which, float tint = B_NO_TINT)
```

Set the low color of the view to a system constant. The color will update live with user changes. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `which` | The color_which constant to set. |
| `tint` | Optional tint value to use. |





**Since:** Haiku R1

---

### `SetMouseEventMask()`

```cpp
status_t BView::SetMouseEventMask(uint32 mask, uint32 options = 0)
```

Sets whether or not the view can accept mouse and keyboard events when not in focus from within [MouseDown()](classBView.md#a5f5bd975d15df94f2ebbc80eb79cc3f6) until the following [MouseUp()](classBView.md#acdb92b30069157b2e3c522a3ef9d6ae4) event. 


The *options* mask options are as follows:


* `B_NO_POINTER_HISTORY` Tells App Server to send only the most recent [MouseMoved()](classBView.md#ac8b20516e42bab2f1eeb130e2432bde0) event to the view sacrificing mouse movement granularity.

* `B_FULL_POINTER_HISTORY` Tells App Server to send all [MouseMoved()](classBView.md#ac8b20516e42bab2f1eeb130e2432bde0) events to the view.

* `B_SUSPEND_VIEW_FOCUS` Events normally sent to the focus view are suppressed. While the mouse is held down, the keyboard is ignored. The view receiving the [MouseDown()](classBView.md#a5f5bd975d15df94f2ebbc80eb79cc3f6) messages doesn't have to be the focus view to suppress focused messages.

* `B_LOCK_WINDOW_FOCUS` Prevents the attached window from losing its focused state while the mouse is held down, even if the mouse leaves the bounds of the window.



Parameters

| Parameter | Description |
| :--- | :--- |
| `mask` | The *mask* of `B_POINTER_EVENTS` and `B_KEYBOARD_EVENTS` to set. |
| `options` | Sets other event-handling options. |





**Returns:** `B_OK` if everything went fine or an error code, usually `B_ERROR` if something went wrong.



**Since:** BeOS R5

---

### `SetOrigin()`

```cpp
void BView::SetOrigin(BPoint where)
```

Sets the origin in the view's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `where` | The point to set the origin to. |





**See also:** [Origin()](classBView.md#aefbf71a7a403900e960ffa3943dc9901)



**Since:** BeOS R3

---

### `SetOrigin()`

```cpp
void BView::SetOrigin(float x, float y)
```

Sets the origin in the view's coordinate system. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | The x-coordinate to set the origin to. |
| `y` | The y-coordinate to set the origin to. |





**See also:** [Origin()](classBView.md#aefbf71a7a403900e960ffa3943dc9901)



**Since:** BeOS R3

---

### `SetPenSize()`

```cpp
void BView::SetPenSize(float size)
```

Set the pen size to *size*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `size` | The pen size to set. |





**Since:** BeOS R3

---

### `SetResizingMode()`

```cpp
void BView::SetResizingMode(uint32 mode)
```

Sets the resizing mode of the view according to the *mode* mask. 


The resizing mode is first set in the [BView](classBView.md) constructor.



**See also:** [ResizingMode()](classBView.md#a1e93df523fc9edc807274ac6cfd2dc8d)



**Since:** BeOS R3


Reimplemented in [BTabView](classBTabView.md#ac291b408315b6070e217bec7960243c7).

---

### `SetScale()`

```cpp
void BView::SetScale(float scale)const
```

Sets the scale of the coordinate system the view uses for drawing. 


The default scale is 1.0. A *scale* value lower than 1.0 reduces the size of the drawing coordinate system, a *scale* value greater than 1.0 magnifies the coordinate system; for example, a *scale* value of 0.5 cuts the drawing drawing area in half moving the drawing closer to the origin while a *scale* value of 2.0 doubles the drawing area and moving it away from the origin.


Updating the *scale* of view won't update previously drawn elements.


[SetScale()](classBView.md#a077136ea06f0a6b39aa0b8b24311cce8) calls are not commutative unless you call them across different drawing states as the following:



```cpp
view->SetScale(2);
view->SetScale(2);
// view's scale is 2
 
view2->SetScale(2);
view2->PushState();
view2->SetScale(2);
// view2's scale is 4
```

Parameters

| Parameter | Description |
| :--- | :--- |
| `scale` | The scale factor to set. |





**Since:** BeOS R3

---

### `SetToolTip()`

```cpp
void BView::SetToolTip(BToolTip * tip)
```

Set the tool tip of the view to the *tip* object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `tip` | The tool tip object to set the view to or `NULL` to unset. |





**Since:** Haiku R1

---

### `SetToolTip()`

```cpp
void BView::SetToolTip(const char * text)
```

Set the tool tip of the view to *text*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `text` | The *text* to set the view to or `NULL` or blank to unset. |





**Since:** Haiku R1

---

### `SetTransform()`

```cpp
void BView::SetTransform(BAffineTransform transform)
```

Sets a [BAffineTransform](classBAffineTransform.md) to transform the coordinate system. 



**See also:** See [Transform()](classBView.md#ab16cc72cf8ae3b40abcf1f714e7e9b74) to get the current transformations, and [TranslateBy()](classBView.md#a8ae6d4e1cdfeeee33b753d56bee6ae7f), [ScaleBy()](classBView.md#ac83f9fdfb882f849e3ac79bfb06a0fd6) and [RotateBy()](classBView.md#a02ab6b6196b140b20ae516a55680e30b) for additional transformation options.



**Since:** Haiku R1

---

### `SetViewBitmap()`

```cpp
void BView::SetViewBitmap(const BBitmap * bitmap, BRect srcRect, BRect dstRect, uint32 followFlags = B_FOLLOW_LEFT_TOP, uint32 options = B_TILE_BITMAP)
```

Sets the background *bitmap* of the view. 


All drawing to the view occurs over *bitmap*. Any visible regions not covered by *bitmap* are filled with the current background color.


Once *bitmap* has been passed in and this method returns the caller may safely delete the object.


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The background bitmap to set to the view. |
| `srcRect` | Specifies the area of *bitmap* to use. |
| `dstRect` | Specifies the area of the view to set *bitmap* to. |
| `followFlags` | Specifies the as the view is resized. See the [BView](classBView.md) constructor for more details. |
| `options` | Specifies additional view options. The only option currently available is `B_TILE_BITMAP` which tiles the bitmap across the view. |





**Since:** BeOS R4

---

### `SetViewBitmap()`

```cpp
void BView::SetViewBitmap(const BBitmap * bitmap, uint32 followFlags = B_FOLLOW_LEFT_TOP, uint32 options = B_TILE_BITMAP)
```

Sets the background *bitmap* of the view. 


All drawing to the view occurs over *bitmap*. Any visible regions not covered by *bitmap* are filled with the current background color.


Once *bitmap* has been passed in and this method returns the caller may safely delete the object.


Parameters

| Parameter | Description |
| :--- | :--- |
| `bitmap` | The background bitmap to set to the view. |
| `followFlags` | Specifies the as the view is resized. See the [BView](classBView.md) constructor for more details. |
| `options` | Specifies additional view options. The only option currently available is `B_TILE_BITMAP` which tiles the bitmap across the view. |





**Since:** BeOS R4

---

### `SetViewColor()`

```cpp
void BView::SetViewColor(rgb_color color)
```

Set the view color of the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `color` | The color to set. |





**Since:** BeOS R3


Referenced by [BLayoutBuilder::Cards< ParentBuilder >::Cards()](classBLayoutBuilder_1_1Cards.md#a08329883aebee0490f3faf96d86f1108), and [SetViewColor()](classBView.md#a7dace2963c85b5ce55b7d8e96946625c).

---

### `SetViewColor()`

```cpp
void BView::SetViewColor(uchar red, uchar green, uchar blue, uchar alpha = 255)
```

Set the view color of the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `red` | The *red* component of the view color. |
| `green` | The *green* component of the view color. |
| `blue` | The *blue* component of the view color. |
| `alpha` | The *alpha* component of the view color. |





**Since:** BeOS R3


References [rgb_color::alpha](structrgb__color.md#a089265e492dbf6743a6eaaa23fa94699), [rgb_color::blue](structrgb__color.md#adbc9af28f1ec74ac8e7cc8f7fc1e6ce3), [rgb_color::green](structrgb__color.md#ac0259068653969121d72739ad8509979), [rgb_color::red](structrgb__color.md#ad8f118f509b77a245d9e38829336f0ec), and [SetViewColor()](classBView.md#ae8dde0e0330b394db016f3e609e7fb6a).

---

### `SetViewCursor()`

```cpp
void BView::SetViewCursor(const BCursor * cursor, bool sync = true)
```

Assigns *cursor* to the view. 


This cursor will be displayed when the mouse is positioned inside the view.


Parameters

| Parameter | Description |
| :--- | :--- |
| `cursor` | The [BCursor](../application_kit/classBCursor.md) object to assign to the view. |
| `sync` | If `true` App Server is synchronized immediately forcing the change to occur. If `false`, the change will be put in the queue and will take effect when the pending requests are processed. |





**Since:** BeOS R5

---

### `SetViewOverlay()`

```cpp
status_t BView::SetViewOverlay(const BBitmap * overlay, BRect srcRect, BRect dstRect, rgb_color * colorKey, uint32 followFlags = B_FOLLOW_LEFT_TOP, uint32 options = 0)
```

Sets the *overlay* bitmap of the view. 


*colorKey* specifies which color pixels in *overlay* are treated as transparent allowing the pixels of the view to show through.


Once *overlay* has been passed in and this method returns the caller may safely delete the object.


Parameters

| Parameter | Description |
| :--- | :--- |
| `overlay` | The overlay bitmap to set to the view. |
| `srcRect` | Specifies the area of *overlay* to use. |
| `dstRect` | Specifies the area of the view to set *overlay* to. |
| `colorKey` | The color in *overlay* to treat as transparent. |
| `followFlags` | Specifies the as the view is resized. See the [BView](classBView.md) constructor for more details. |
| `options` | Specifies additional view options. The only option currently available is `B_TILE_BITMAP` which tiles the bitmap across the view. |





**Since:** BeOS R5

---

### `SetViewOverlay()`

```cpp
status_t BView::SetViewOverlay(const BBitmap * overlay, rgb_color * colorKey, uint32 followFlags = B_FOLLOW_LEFT_TOP, uint32 options = 0)
```

Sets the *overlay* bitmap of the view. 


*colorKey* specifies which color pixels in *overlay* are treated as transparent allowing the pixels of the view to show through.


Once *overlay* has been passed in and this method returns the caller may safely delete the object.


Parameters

| Parameter | Description |
| :--- | :--- |
| `overlay` | The overlay bitmap to set to the view. |
| `colorKey` | The color in *overlay* to treat as transparent. |
| `followFlags` | Specifies the as the view is resized. See the [BView](classBView.md) constructor for more details. |
| `options` | Specifies additional view options. The only option currently available is `B_TILE_BITMAP` which tiles the bitmap across the view. |





**Since:** BeOS R5

---

### `SetViewUIColor()`

```cpp
void BView::SetViewUIColor(color_which which, float tint = B_NO_TINT)
```

Set the view color of the view to a system constant. The color will update live with user changes. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `which` | The color_which constant to set. |
| `tint` | Optional tint value to use. |





**Since:** Haiku R1

---

### `Show()`

```cpp
void BView::Show()
```

Shows the view making it visible. 


Calls to [Hide()](classBView.md#a7688dc04178a2955950154ee3670d029) and [Show()](classBView.md#a06e0584057d6c7a7c7e048b6272b7016) are cumulative. A hidden view becomes visible again once the number of [Show()](classBView.md#a06e0584057d6c7a7c7e048b6272b7016) calls matches the number of [Hide()](classBView.md#a7688dc04178a2955950154ee3670d029) calls.



**See also:** [Hide()](classBView.md#a7688dc04178a2955950154ee3670d029)



**Since:** BeOS R3


Reimplemented in [BMenu](classBMenu.md#a880d9a96919d389e03106e978709bf9b), and [BMenuBar](classBMenuBar.md#ac0b9dafc30dd338e8f67b26eff7168f0).

---

### `ShowToolTip()`

```cpp
void BView::ShowToolTip(BToolTip * tip = NULL)
```

Show the tool tip at the current mouse position. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `tip` | The BToolTip object to show. |





**Since:** Haiku R1

---

### `StringWidth()`

```cpp
float BView::StringWidth(const char * string)const
```

Return the width of *string* set in the font of the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to get the width of. |





**Returns:** The width of the string in the view's font as a float.



**Since:** BeOS R3

---

### `StringWidth()`

```cpp
float BView::StringWidth(const char * string, int32 length)const
```

Return the width of *string* set in the font of the view up to *length* characters. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to get the width of. |
| `length` | The maximum number of characters in *string* to consider. |





**Returns:** The width of the string in the view's font as a float.



**Since:** BeOS R3

---

### `StrokeArc()`

```cpp
void BView::StrokeArc(BPoint center, float xRadius, float yRadius, float startAngle, float arcAngle, ::pattern pattern = B_SOLID_HIGH)
```

Stroke the outline of an arc starting at *center* with a horizontal radius of *xRadius* and a vertical radius of *yRadius* starting at *startAngle* and drawing *arcAngle* degrees. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | The center point. |
| `xRadius` | The horizontal radius. |
| `yRadius` | The vertical radius. |
| `startAngle` | The angle to begin drawing at. |
| `arcAngle` | The number of degrees of the arc to draw. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `StrokeArc()`

```cpp
void BView::StrokeArc(BRect rect, float startAngle, float arcAngle, ::pattern pattern = B_SOLID_HIGH)
```

Stroke the outline of an arc inscribed within *rect* starting at *startAngle* and drawing *arcAngle* degrees. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The area within which to inscribe the shape. |
| `startAngle` | The angle to begin drawing at. |
| `arcAngle` | The number of degrees of the arc to draw. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `StrokeBezier()`

```cpp
void BView::StrokeBezier(BPoint * controlPoints, ::pattern pattern = B_SOLID_HIGH)
```

Stroke a bezier curve. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `controlPoints` | The list of points that form the bezier curve. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `StrokeEllipse()`

```cpp
void BView::StrokeEllipse(BPoint center, float xRadius, float yRadius, ::pattern pattern = B_SOLID_HIGH)
```

Stroke the outline of an ellipse starting at *center* with a horizontal radius of *xRadius* and a vertical radius of *yRadius*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | The center point. |
| `xRadius` | The horizontal radius. |
| `yRadius` | The vertical radius. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `StrokeEllipse()`

```cpp
void BView::StrokeEllipse(BRect rect, ::pattern pattern = B_SOLID_HIGH)
```

Stroke the outline of an ellipse inscribed within *rect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The area within which to inscribe the shape. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `StrokeLine()`

```cpp
void BView::StrokeLine(BPoint start, BPoint end, ::pattern pattern = B_SOLID_HIGH)
```

Stroke a line from point *start* to point *end*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `start` | The start point of the line. |
| `end` | The end point of the line. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `StrokeLine()`

```cpp
void BView::StrokeLine(BPoint toPoint, ::pattern pattern = B_SOLID_HIGH)
```

Stroke a line from the current pen location to the point *toPoint*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `toPoint` | The end point of the line. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `StrokePolygon()`

```cpp
void BView::StrokePolygon(const BPoint * pointArray, int32 numPoints, bool closed = true, ::pattern pattern = B_SOLID_HIGH)
```

Stroke a polygon shape made up of points specified by *pointArray*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `pointArray` | An array of points that specify the vertices of the polygon. |
| `numPoints` | The number of points in *pointArray*. |
| `closed` | Whether or not the last line of the polygon should intersect with the initial point. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `StrokePolygon()`

```cpp
void BView::StrokePolygon(const BPoint * pointArray, int32 numPoints, BRect bounds, bool closed = true, ::pattern pattern = B_SOLID_HIGH)
```

Stroke a polygon shape made up of points specified by *pointArray* inscribed by *bounds*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `pointArray` | An array of points that specify the vertices of the polygon. |
| `numPoints` | The number of points in *pointArray*. |
| `bounds` | The smallest rectangle that encloses the points in *pointArray*. |
| `closed` | Whether or not the last line of the polygon should intersect with the initial point. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `StrokePolygon()`

```cpp
void BView::StrokePolygon(const BPolygon * polygon, bool closed = true, ::pattern pattern = B_SOLID_HIGH)
```

Stroke a polygon shape. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `polygon` | The polygon shape to stroke. |
| `closed` | Whether or not the last line of the polygon should intersect with the initial point. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `StrokeRect()`

```cpp
void BView::StrokeRect(BRect rect, ::pattern pattern = B_SOLID_HIGH)
```

Stroke the rectangle specified by *rect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The rectangular area to stroke. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `StrokeRoundRect()`

```cpp
void BView::StrokeRoundRect(BRect rect, float xRadius, float yRadius, ::pattern pattern = B_SOLID_HIGH)
```

Stroke the rounded rectangle with horizontal radius *xRadius* and vertical radius *yRadius*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | The rectangular area to stroke the round rect within. |
| `xRadius` | The horizontal radius. |
| `yRadius` | The vertical radius. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `StrokeShape()`

```cpp
void BView::StrokeShape(BShape * shape, ::pattern pattern = B_SOLID_HIGH)
```

Stroke *shape*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `shape` | The *shape* to stroke. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R5

---

### `StrokeTriangle()`

```cpp
void BView::StrokeTriangle(BPoint point1, BPoint point2, BPoint point3, ::pattern pattern = B_SOLID_HIGH)
```

Stroke the triangle specified by points *point1*, *point2*, and *point3*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point1` | The first point of the triangle. |
| `point2` | The second point of the triangle. |
| `point3` | The third point of the triangle. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `StrokeTriangle()`

```cpp
void BView::StrokeTriangle(BPoint point1, BPoint point2, BPoint point3, BRect bounds, ::pattern pattern = B_SOLID_HIGH)
```

Stroke the triangle specified by points *point1*, *point2*, and *point3* and enclosed by *bounds*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point1` | The first point of the triangle. |
| `point2` | The second point of the triangle. |
| `point3` | The third point of the triangle. |
| `bounds` | The rectangular area that encloses the triangle. |
| `pattern` | One of the following: * `B_SOLID_HIGH`  * `B_SOLID_LOW`  * `B_MIXED_COLORS` |





**Since:** BeOS R3

---

### `Sync()`

```cpp
void BView::Sync()const
```

Synchronizes the attached window's connection to App Server. 



> [!WARNING]
> If the view isn't attached to a window, [Sync()](classBView.md#a27e217abb3fefa45b6e4ceb7a54cb362) might crash the application.



**Since:** BeOS R3

---

### `TargetedByScrollView()`

```cpp
void BView::TargetedByScrollView(BScrollView * scrollView)
```

Hook method called when the view becomes the target of *scrollView*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `scrollView` | The [BScrollView](classBScrollView.md) object that has targeted the view. |





**Since:** Haiku R1


Reimplemented in [BListView](classBListView.md#a453b373c9bd616f11a1bb195fb05bfbb).

---

### `ToolTip()`

```cpp
BToolTip * BView::ToolTip()const
```

Return the tool tip set to the view or `NULL` if not set. 



**Returns:** The BToolTip object set to the view.



**Since:** Haiku R1

---

### `Transform()`

```cpp
BAffineTransform BView::Transform()const
```

Returns the current [BAffineTransform](classBAffineTransform.md) that is applied to the coordinate system. 



**See also:** [SetTransform()](classBView.md#afbd9b8f35226ba89980c450f7626fc85)



**Since:** Haiku R1

---

### `TransformTo()`

```cpp
BAffineTransform BView::TransformTo(coordinate_space basis)const
```

Return the [BAffineTransform](classBAffineTransform.md) to convert from the current drawing space to *basis*. 


`B_PREVIOUS_STATE_COORDINATES` is equivalent to `B_CURRENT_STATE_COORDINATES` when there is no parent state.


`B_PARENT_VIEW_DRAW_COORDINATES` and `B_PARENT_VIEW_COORDINATES` are equivalent to `B_WINDOW_COORDINATES` when used on a root view.


`B_WINDOW_COORDINATES` works as `B_SCREEN_COORDINATES` for unattached views.



**See also:** [Transform()](classBView.md#ab16cc72cf8ae3b40abcf1f714e7e9b74)



**Since:** Haiku R1

---

### `TranslateBy()`

```cpp
void BView::TranslateBy(double x, double y)
```

Translate the current view by coordinates. 


The translation of *x* and *y* are applied to the current transformation, not instead of, so it is an additive action.



**See also:** See [Transform()](classBView.md#ab16cc72cf8ae3b40abcf1f714e7e9b74) to get the current transformations, [SetTransform()](classBView.md#afbd9b8f35226ba89980c450f7626fc85), [ScaleBy()](classBView.md#ac83f9fdfb882f849e3ac79bfb06a0fd6) and [RotateBy()](classBView.md#a02ab6b6196b140b20ae516a55680e30b) for additional transformation options.



**Since:** Haiku R1

---

### `TruncateString()`

```cpp
void BView::TruncateString(BString * string, uint32 mode, float width)const
```

Truncate *string* with truncation mode *mode* so that it is no wider than *width* set in the view's font. 


When the string is truncated the missing characters are replaced by a horizontal ellipses.


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to truncate in place. |
| `mode` | The truncation mode to use, one of the following: * `B_TRUNCATE_BEGINNING` Truncate from the beginning of the string.  * `B_TRUNCATE_MIDDLE` Truncate from the middle of the string.  * `B_TRUNCATE_END` Truncate from the end of the string.  * `B_TRUNCATE_SMART` Truncate from anywhere based on the string content. Not currently implemented. |
| `width` | The maximum width to truncate the string to. |





**Since:** BeOS R5

---

### `ViewColor()`

```cpp
rgb_color BView::ViewColor()const
```

Return the current view color. 



**Returns:** The current view color as an [rgb_color](structrgb__color.md) struct.



**See also:** [SetViewColor(rgb_color)](classBView.md#ae8dde0e0330b394db016f3e609e7fb6a)



**Since:** BeOS R3

---

### `ViewUIColor()`

```cpp
color_which BView::ViewUIColor(float * tint = NULL)const
```

Return the current view color constant being used. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `tint` | Optional float pointer in which to store the tint value used to modify the system color constant. |





**Returns:** The current view color constant.



**See also:** [SetViewUIColor(color_which, float)](classBView.md#a34f020c4bb1008cef972cf1eec7dba0f)



**Since:** Haiku R1

---

### `Window()`

```cpp
BWindow * BView::Window()const
```

Returns the window the view is attached to. 



**Returns:** The window the view is attached to or `NULL` if the view isn't attached to a window.



**Since:** BeOS R3

---

### `WindowActivated()`

```cpp
void BView::WindowActivated(bool active)
```

Hook method called when the attached window is activated or deactivated. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `active` | `true` when the window becomes activated, `false` when the window becomes deactivated. |





**Since:** BeOS R3


Reimplemented in [BBox](classBBox.md#a7a60147068c94405f7ba53a8eaba237b), [BButton](classBButton.md#ace1f01da01eef93adbecd91ce2d49ac1), [BCheckBox](classBCheckBox.md#af3e0b0e3afc3d2adfb2e3cf0f9bb3b82), [BControl](classBControl.md#ab665fb93df191662a1757f78555a5b21), [BListView](classBListView.md#a85153f43edc12ca463f981b92e187a11), [BMenuField](classBMenuField.md#a927eea4bf97ed4834e97f18e466bd952), [BPictureButton](classBPictureButton.md#a2c1edfc72af90482e70328b152998001), [BRadioButton](classBRadioButton.md#a5f15ba4b79b38cb260b2b95e52c60a83), [BScrollBar](classBScrollBar.md#ad44b780f97678d78d96c2b1c2eff2389), [BScrollView](classBScrollView.md#aa3a3e20ad81fb967bc3a0fb2aeb16117), [BTabView](classBTabView.md#a2935851b89461b8d5ff01b11948dd885), [BTextControl](classBTextControl.md#a38f83894076d23f426e1e347f7ef933d), [BTextView](classBTextView.md#ad60669080665218ce09f2773b7470f2d), [BChannelSlider](classBChannelSlider.md#aa9d3e2bfcd8fbd5901b82960c11484bf), [BColorControl](classBColorControl.md#acea993086cd5dd46f36e12149017930c), [BMenuBar](classBMenuBar.md#a5e623033adfd89d43cca5b8030fb9ccf), and [BStatusBar](classBStatusBar.md#a2b6dcc805b8598cd268568ea167445a3).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBView.html).
