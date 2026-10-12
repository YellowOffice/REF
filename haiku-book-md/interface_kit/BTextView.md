---
name: BTextView
type: class
kit: interface_kit
brief: "Displays and manipulates styled text"
source: haiku-book
---

# BTextView Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Displays and manipulates styled text. 


Each [BTextView](classBTextView.md) instance has a [TextRect()](classBTextView.md#ada039d479fde2de2f4ea2375cf71edc2) that keeps track of the bounds of the text inside it. [BTextView](classBTextView.md) will resize and reposition [TextRect()](classBTextView.md#ada039d479fde2de2f4ea2375cf71edc2) as the view size changes in [FrameResized()](classBTextView.md#a77ca110829a03b040b59a784caf327fb). You must set the initial text rect either in the constructor, or using [SetTextRect()](classBTextView.md#a5dfe405b8963dec0acf22d571566f335).


The dynamic layout versions of the constructor set the initial [TextRect()](classBTextView.md#ada039d479fde2de2f4ea2375cf71edc2) to [Bounds()](classBView.md#acbb8ea442346e91428689163db9d633e). [TextRect()](classBTextView.md#ada039d479fde2de2f4ea2375cf71edc2) uses the view's coordinate system.


Setting the text rect to [Bounds()](classBView.md#acbb8ea442346e91428689163db9d633e) will add some default insets repositioning the text inside the view. If you do not want this you may override the default insets by calling [SetInsets()](classBTextView.md#a3dccebc1ff74ad040d660e36cb13ddbc). It is recommended that you use [SetInsets()](classBTextView.md#a3dccebc1ff74ad040d660e36cb13ddbc) to offset the initial text rect position instead of offsetting the text rect passed into the constructor. [SetInsets()](classBTextView.md#a3dccebc1ff74ad040d660e36cb13ddbc) will retain insets with changing alignment and word-wrap while the distance of the initial [TextRect()](classBTextView.md#ada039d479fde2de2f4ea2375cf71edc2) from the view [Bounds()](classBView.md#acbb8ea442346e91428689163db9d633e) is not retained.


[TextRect()](classBTextView.md#ada039d479fde2de2f4ea2375cf71edc2) can be wider or narrower than the view and it can be taller or shorter. As you type, delete, cut, and paste the width and height of the text rect may change. If word-wrap is on, [TextRect()](classBTextView.md#ada039d479fde2de2f4ea2375cf71edc2) width will always be set to the width of the view minus insets. If word-wrap is off [TextRect()](classBTextView.md#ada039d479fde2de2f4ea2375cf71edc2) width will be set to the width of the longest line of text. The top and bottom of [TextRect()](classBTextView.md#ada039d479fde2de2f4ea2375cf71edc2) will always be set to the top and bottom of the text. [Highlight()](classBTextView.md#a9388556beb45f15e16883fd1ee0ca505) will highlight multiple lines at least to the edge of the text view even if [TextRect()](classBTextView.md#ada039d479fde2de2f4ea2375cf71edc2) is narrower.


When [TextRect()](classBTextView.md#ada039d479fde2de2f4ea2375cf71edc2) is made wider or taller than the view scroll bars will activate if present. You may scroll using [ScrollToOffset()](classBTextView.md#a029331301f5b9c6f2e02f309695e6439) to scroll the text so that the character at the given offset is visible or you may call [ScrollToSelection()](classBTextView.md#a115416adbb7a2c9f6bb3c845396d31b9) to scroll the text so that the character that begins the selection is visible.


Call [SetText()](classBTextView.md#a6af0844c93f0a548e0717e0b4e2b8e33) to change the text. This will resize [TextRect()](classBTextView.md#ada039d479fde2de2f4ea2375cf71edc2).


Call [SetWordWrap()](classBTextView.md#afe3b998f71371ae8479ac72ef3b4fb08) to turn word-wrap on and off. This will resize [TextRect()](classBTextView.md#ada039d479fde2de2f4ea2375cf71edc2).


Call [SetAlignment()](classBTextView.md#ae71fcc418e9934a852b0e5c9d6d6961b) to change the alignment to `B_ALIGN_CENTER` or `B_ALIGN_RIGHT`. This will reposition [TextRect()](classBTextView.md#ada039d479fde2de2f4ea2375cf71edc2).


Call [SetStylable()](classBTextView.md#af7ff7c6ed79a7deaf1ff180b0b2fc597) to allow multiple font styles.


Call [SetTabWidth()](classBTextView.md#a692c0cf4d5ad343d35ca12bcdf7e44f0) to set the width of hard tabs. You may turn auto-indentation off with [SetAutoindent()](classBTextView.md#abd09cfa6752d3e808770d17065d6d4ec).


Call [MakeSelectable()](classBTextView.md#aa7bbd890c204b973daae9b82b657e117) and [MakeEditable()](classBTextView.md#aebdfde8ef7cf1a490c96fc4f0d822873) to turn the ability for text to be selectable or editable off. A non-editable, non-selectable text view can be useful as a [BStringView](classBStringView.md) that wraps.


Call [AdoptSystemColors()](classBTextView.md#a26acfabf11a50b255127624dc544a61d) to set default colors.


Call [MakeResizable()](classBTextView.md#a106796bac011113352981917f001f24f) to make the view width track with text width, this can be useful for short single-line text views.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BTextView](#a9ed3c44d9376ae18e5b2ad06595e5936) (BMessage *archive) — Creates a BTextView object from the passed in archive.
* [BTextView](#a93a2741707da3d1cbfa2d102bb2b6ba2) (BRect frame, const char *name, BRect textRect, const BFont *initialFont, const rgb_color *initialColor, uint32 resizeMask, uint32 flags) — Creates a new BTextView object and sets the initial font and color.
* [BTextView](#a3a15a66e85637c767c5f531f92fe86e7) (BRect frame, const char *name, BRect textRect, uint32 resizeMask, uint32 flags=B_WILL_DRAW|B_PULSE_NEEDED) — Creates a new BTextView object.
* [BTextView](#a60f4c56c03150727f757953f91a779b0) (const char *name, const BFont *initialFont, const rgb_color *initialColor, uint32 flags) — Creates a new BTextView object and sets the initial font and color, dynamic layout version.
* [BTextView](#a47484886491aceabb4153844ab6ef284) (const char *name, uint32 flags=B_WILL_DRAW|B_PULSE_NEEDED) — Creates a BTextView object, dynamic layout version.
* `virtual` [~BTextView](#a2f8f9f4590d6436a4fe3cbbafb9db8cd) () — Frees the memory allocated and destroys the object.
* `virtual void` [GetHeightForWidth](#aec7881d97bdc508b01a6caa80f51d963) (float width, float *min, float *max, float *preferred) — Returns the min, max and preferred height for a given width.
* `virtual void` [GetPreferredSize](#a5b31f120d4476b83beb08f3333cfc85d) (float *_width, float *_height) — Fill out the preferred width and height of the view into the _width and _height parameters.
* `virtual status_t` [GetSupportedSuites](#a9cb6a32b918a5c90489b6fb7e27fcb6a) (BMessage *data)
* `virtual bool` [HasHeightForWidth](#a099a44a6619914db20a02a6ccf611b70) () — Returns whether the layout of the view can calculate a height for a given width.
* `virtual void` [MakeFocus](#ac0bc816f13b04fd2ec2668c618ab8ca8) (bool focus=true) — Highlight or unhighlight the selection when the text view acquires or loses its focus state.
* `virtual BSize` [MaxSize](#af8e32e9318d9368137940d2511d3dff2) () — Return the maximum size of the view.
* `virtual BSize` [MinSize](#a3a03f5bff63cba54276025e3788520d9) () — Return the minimum size of the view.
* `virtual status_t` [Perform](#a6519856e1dbf6e021911529b8a0a15c6) (perform_code code, void *data) — Perform some action. (Internal Method)
* `virtual BSize` [PreferredSize](#ad46589273b8c8acb8737efde58407d3d) () — Return the preferred size of the view.
* `virtual void` [ResizeToPreferred](#ae288597c33c40f5f42abfe3ed41fce86) () — Resizes the view to its preferred size keeping the position of the left top corner constant.
* `virtual BHandler *` [ResolveSpecifier](#a3e0e67bcd942c0b738043235e56fdf29) (BMessage *message, int32 index, BMessage *specifier, int32 form, const char *property)
* `virtual void` [AttachedToWindow](#a73a892fb4d5e7e3575064f326b67867a) () — Hook method called when the text view is added to the view hierarchy.
* `virtual void` [DetachedFromWindow](#a79356aad15f3cd52203d81cb5b163461) () — Hook method that is called when the text view is removed from the view hierarchy.
* `virtual void` [Draw](#ad1b1f366a371aaecdbc39e2b13f6100b) (BRect updateRect) — Hook method called to draw the contents of the text view.
* `virtual void` [MouseDown](#a581a2b2877b29d275771ae5010d6706d) (BPoint where) — Hook method that is called when a mouse button is pushed down while the cursor is contained in the view.
* `virtual void` [MouseUp](#a72a0cd6839b541db996d751f240e59a1) (BPoint where) — Hook method that is called when a mouse button is released while the cursor is contained in the view.
* `virtual void` [MouseMoved](#a95bc494682c45ba41c457029639f2d55) (BPoint where, uint32 code, const BMessage *dragMessage) — Hook method that is called whenever the mouse cursor enters, exits or moves inside the view.
* `virtual void` [WindowActivated](#ad60669080665218ce09f2773b7470f2d) (bool active) — Hook method that is called when the window becomes the active window or gives up that status.
* `virtual void` [KeyDown](#a38ae9b87206a3236527d533b1f33d951) (const char *bytes, int32 numBytes) — Hook method that is called when a key is pressed while the view is the focus view of the active window.
* `virtual void` [Pulse](#ada90a85565bd3e6bbe130901299c6da8) () — Hook method that is called at a set interval.
* `virtual void` [FrameResized](#a77ca110829a03b040b59a784caf327fb) (float newWidth, float newHeight) — Hook method that is called when the frame is resized.
* `virtual void` [MessageReceived](#a4d7d7990e57ce7286f78698f27c89e60) (BMessage *message) — Hook method called with a message is received by the text view.
* `virtual void` [AllAttached](#a525a3a00911c36ee0acf05daa2ff8716) ()
* `virtual void` [AllDetached](#a2ff4cd2084da7717a7c08c7c95651614) ()
* `void` [SetText](#a6af0844c93f0a548e0717e0b4e2b8e33) (const char *text, const text_run_array *runs=NULL) — Copies text from the text buffer replacing any text currently set in the BTextView with the font and color formats set by runs.
* `void` [SetText](#ad1a7f628f620e6c547e42d2dbbd18ac8) (const char *text, int32 length, const text_run_array *runs=NULL) — Copies text from the text buffer up to length characters replacing any text currently set in the BTextView with the font and color formats set by runs.
* `void` [SetText](#ad10cfbcd1fabaf0300568e154ceab53a) (BFile *file, int32 offset, int32 length, const text_run_array *runs=NULL) — Copies text from the file starting at the given offset up to length characters replacing any text currently set in the BTextView with the font and color formats set by runs.
* `void` [Insert](#a0ee743c15e51c89e15eefe5b0145b1e1) (const char *text, const text_run_array *runs=NULL) — Inserts text from the text buffer at the end of the BTextView with the font and color formats set by runs.
* `void` [Insert](#ae0883c03c0361d12cf278f0bf5ea503d) (const char *text, int32 length, const text_run_array *runs=NULL) — Inserts text from the text buffer up to length characters at the end of the BTextView with the font and color formats set by runs.
* `void` [Insert](#aecff7b0c2868a7aea0b195162863cbc5) (int32 offset, const char *text, int32 length, const text_run_array *runs=NULL) — Inserts text starting at the given offset from the text buffer up to length characters into the BTextView with the font and color formats set by runs.
* `void` [Delete](#a9926ac3ab300b04c931dc8c6c01d648f) () — Deletes the text within the current selection.
* `void` [Delete](#a9652d7c8741a1ccc55caa61102f70244) (int32 startOffset, int32 endOffset) — Deletes the text enclosed within the given offsets.
* `const char *` [Text](#aa4abaa45b5c4f1ac15fd7d613d71317b) () const — Returns the BTextView text as a byte array.
* `int32` [TextLength](#a0ea8237b7c2aadce8e2f0ed97b3aa282) () const — Returns the text length of the BTextView text.
* `void` [GetText](#a849d5c8a43d17ab4dee07d1758e5a839) (int32 offset, int32 length, char *buffer) const — Fills out buffer with the text of the BTextView starting at offset and grabbing at most length bytes.
* `uint8` [ByteAt](#afb783ae7c839313c9f915b122e6f3ce7) (int32 offset) const — Returns the character at the given offset.
* `int32` [CountLines](#a6bf21da74122ae112746c7c0be5d9880) () const — Returns the number of lines that the BTextView object contains.
* `int32` [CurrentLine](#a93a13dc6c0d1ca316555cfe57cdfe611) () const — Returns the index of the current line.
* `void` [GoToLine](#a466d34e311879ee43a77e42e18c2b516) (int32 lineNumber) — Moves the caret to the specified line.
* `virtual void` [Cut](#a1f1d1c35f94cd4b172000e0eed1e97bd) (BClipboard *clipboard) — Moves the current selection to the clipboard.
* `virtual void` [Copy](#a0353fc7b7d2d8e579ddce27b07519929) (BClipboard *clipboard) — Copies the current selection to the clipboard.
* `virtual void` [Paste](#a1c19ed827e74edbd3c749c7b67667aaa) (BClipboard *clipboard) — Copy the text contained in the clipboard to the BTextView.
* `virtual bool` [AcceptsPaste](#a88c2b8661082c2d122736649d6b64e77) (BClipboard *clipboard) — Returns whether or not the BTextView can accept the clipboard data.
* `virtual bool` [AcceptsDrop](#a3485b6f78a3a9208902d5c01e7766fc9) (const BMessage *message) — Returns whether or not the BTextView can accept the dropped message data.
* `void` [Clear](#ab1f47a18c9c4ba4469b08cc07f06ad3a) () — Deletes the currently selected text.
* `virtual void` [Select](#a35737d4bef49712542b12b1a5add2520) (int32 startOffset, int32 endOffset) — Selects the text contained within the given offsets.
* `void` [SelectAll](#ac3ec307c452a5e38c911e0089427fe4e) () — Selects all text contained in the BTextView.
* `void` [GetSelection](#abc61acda4dd214033c7e4cb23d531c0d) (int32 *_start, int32 *_end) const — Fills out _start and _end with the start and end offsets of the current selection.
* `text_run_array *` [RunArray](#afc72592044583011e10b903f4868c3af) (int32 startOffset, int32 endOffset, int32 *_size=NULL) const — Returns a text_run_array for the text within the given offsets.
* `int32` [LineAt](#acb733c2928f582f5d157ceed1c44727f) (int32 offset) const — Returns the line number of the character at the given offset.
* `int32` [LineAt](#afb1697f452277bd09e6894863db9960f) (BPoint point) const — Returns the line number for the passed point.
* `BPoint` [PointAt](#a32ada6e38d904b78822eb9fa7e2a9987) (int32 offset, float *_height=NULL) const — Returns the location of the character at the given offset.
* `int32` [OffsetAt](#a550bbadd24a65086f5c053082338d055) (BPoint point) const — Returns the offset at the passed in point.
* `int32` [OffsetAt](#a318bb090cb159095b23b5a3a29ea07b5) (int32 line) const — Returns the offset of the given line.
* `virtual void` [FindWord](#a1c3eacdbbac660e81960d47da42f4b4e) (int32 offset, int32 *_fromOffset, int32 *_toOffset) — Fills out _fromOffset and _toOffset for a sequence of character that qualifies as a word starting at offset.
* `virtual bool` [CanEndLine](#ad30ce400c0a7f586d9a14509139dcb30) (int32 offset) — Returns whether or not the character at the given offset can be the last character of a line.
* `float` [LineWidth](#a399a56365f69f5bbc765c7087e4a8b9d) (int32 lineNumber=0) const — Returns the width of the line at the given lineNumber.
* `float` [LineHeight](#ace81a4936220c72d6ab088c7f9bb9b79) (int32 lineNumber=0) const — Returns the height of the line at the given lineNumber.
* `float` [TextHeight](#abda2968c60959c9909c54a42fb771fe0) (int32 startLine, int32 endLine) const — Returns the height of the text enclosed within the given lines.
* `void` [Highlight](#a9388556beb45f15e16883fd1ee0ca505) (int32 startOffset, int32 endOffset) — Highlight the text enclosed within the given offsets.
* `void` [AdoptSystemColors](#a26acfabf11a50b255127624dc544a61d) () — Adopts document colors tinted to match panel background if uneditable.
* `bool` [HasSystemColors](#a3350d32c812789042cd7f769220d0ed9) () const — Tests whether or not the text view is using system colors.
* `void` [SetFontAndColor](#a48d9cccd617a4cab0e7a8ac26d0b63b9) (const BFont *font, uint32 mode=B_FONT_ALL, const rgb_color *color=NULL) — Set font and text color of the current selection. The default mode is B_FONT_ALL.
* `void` [SetFontAndColor](#a2b5e64f896b1dd9974450f7959d773f7) (int32 startOffset, int32 endOffset, const BFont *font, uint32 mode=B_FONT_ALL, const rgb_color *color=NULL) — Set the font and color of a selection starting at startoffset ending at endOffset. The default mode is B_FONT_ALL.
* `void` [GetFontAndColor](#a38f2492dc77db1be6f4a79eb1df25bb3) (int32 offset, BFont *_font, rgb_color *_color=NULL) const — Fill out _font and _color at specified text offset.
* `void` [GetFontAndColor](#aad46fd5283ed45f76f12e2ce8313cc68) (BFont *_font, uint32 *_mode, rgb_color *_color=NULL, bool *_sameColor=NULL) const — Fill out _font, _mode, _color and sameColor with the font and color of the current selection.
* `virtual void` [ScrollToOffset](#a029331301f5b9c6f2e02f309695e6439) (int32 offset) — Scrolls the text so that the character at offset is visible.
* `void` [ScrollToSelection](#a115416adbb7a2c9f6bb3c845396d31b9) () — Scrolls the text so that the character that begins the selection is visible.
* `void` [SetTextRect](#a5dfe405b8963dec0acf22d571566f335) (BRect rect) — Sets the object's text frame to the passed in rect.
* `BRect` [TextRect](#ada039d479fde2de2f4ea2375cf71edc2) () const — Returns the BTextView's text frame.
* `void` [SetInsets](#a3dccebc1ff74ad040d660e36cb13ddbc) (float left, float top, float right, float bottom) — Sets the insets within the bounds for the object's text frame.
* `void` [GetInsets](#a50d67716d54b7ac5bb14e59e1b504d49) (float *_left, float *_top, float *_right, float *_bottom) const — Fills out the parameters with the objects's text insets.
* `void` [SetStylable](#af7ff7c6ed79a7deaf1ff180b0b2fc597) (bool stylable) — Sets whether or not the object accepts multiple font styles.
* `bool` [IsStylable](#aed17086d3059cd6ca790420a6e5446f5) () const — Returns whether or not the object accepts multiple font styles.
* `void` [SetTabWidth](#a692c0cf4d5ad343d35ca12bcdf7e44f0) (float width) — Sets the distance between tab stops in pixels.
* `float` [TabWidth](#acc5bfe534c4c1ef13b0a9df231cded18) () const — Returns the tab width of the BTextView.
* `void` [MakeSelectable](#aa7bbd890c204b973daae9b82b657e117) (bool selectable=true) — Sets whether or not the text is selectable.
* `bool` [IsSelectable](#a2ca91f84ade13166b46cbe1aedf7da0f) () const — Returns whether or not the text is selectable.
* `void` [MakeEditable](#aebdfde8ef7cf1a490c96fc4f0d822873) (bool editable=true) — Sets whether or not the text is editable.
* `bool` [IsEditable](#a78ca6e19fc0b418a6912024771d1e739) () const — Returns whether or not the text is editable.
* `void` [SetWordWrap](#afe3b998f71371ae8479ac72ef3b4fb08) (bool wrap) — Activate or deactivate word wrapping mode.
* `bool` [DoesWordWrap](#a226fee862ed32ded1029a63140b90c8d) () const — Returns whether or not word wrapping is activated.
* `void` [SetMaxBytes](#a233e3150486c81394d3bfe44dad0babe) (int32 max) — Sets the maximum number of bytes that the BTextView can contain.
* `int32` [MaxBytes](#afad6c3190c1dc5e2aa83568f0b84cd15) () const — Returns the maximum number of bytes that the BTextView can contain.
* `void` [DisallowChar](#a91836216cb18b6030bb7949c0a72a4dd) (uint32 character) — Adds the character to the disallowed characters list.
* `void` [AllowChar](#aa2b793d153eb61478f5d849fa32a5084) (uint32 character) — Removes the character from the disallowed characters list.
* `void` [SetAlignment](#ae71fcc418e9934a852b0e5c9d6d6961b) (alignment align) — Sets the way text is aligned within the frame.
* `alignment` [Alignment](#a3cdbecd490374de1d479c747e81377cc) () const — Returns the current text alignment.
* `void` [SetAutoindent](#abd09cfa6752d3e808770d17065d6d4ec) (bool state) — Sets whether or not new lines of text are automatically indented.
* `bool` [DoesAutoindent](#a81448d18e95a7426ee98c63596d539d4) () const — Returns whether or not automatic indenting is active.
* `void` [SetColorSpace](#aaf45743e5d825b7e4eb77fe770d14cb3) (color_space colors) — Set the color space of the offscreen BBitmap object.
* `color_space` [ColorSpace](#ad2668d62c775d15b171506ee9faf0ad3) () const — Returns the colorspace set to the offscreen BBitmap object.
* `void` [MakeResizable](#a106796bac011113352981917f001f24f) (bool resize, BView *resizeView=NULL) — Activates and deactivates automatic resizing.
* `bool` [IsResizable](#ab6475a654386b4e07a897992294a7fae) () const — Returns whether or not the object is resizable.
* `void` [SetDoesUndo](#a21286b9caeb086eff3728daea6d5f9ac) (bool undo) — Enables and disables the undo mechanism.
* `bool` [DoesUndo](#a6b3e89d72238e1d92e3d6aa558ad5b06) () const — Returns whether or not the undo mechanism is enabled.
* `void` [HideTyping](#a0461eff711af1cc8f797143ea4a932f1) (bool enabled) — Enables and disables type hiding.
* `bool` [IsTypingHidden](#a0609e9935d9c7563df37d05957c4f7fd) () const — Returns whether or not typing is hidden.
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
* `virtual void` [KeyUp](#acbc528bb70be49993bd99aa136dbb089) (const char *bytes, int32 numBytes) — Hook method called when a keyboard key is released.
* `virtual void` [FrameMoved](#a551c22b45301e13a3ba959eece3cec7f) (BPoint newPosition) — Hook method called when the view is moved.
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

### Protected Member Functions

* `virtual void` [DoLayout](#a5126538fd4fc16a0deec2c256c62ce51) () — Layout view within the layout context.
* `virtual void` [LayoutInvalidated](#ab97f9e2be3de9c163ed7b78a9fc7b74f) (bool descendants) — Hook method called when the layout is invalidated.
* `virtual void` [LayoutChanged](#ada521f848e4c800cd02eb4fe529e7ea0) () — Hook function that is called when the layout if this view, or one of its children, has changed.
* `status_t` [ScrollWithMouseWheelDelta](#a54991372110199183fed775598ae1912) (BScrollBar *, float) — Handle the scroll wheel changing over scrollbars.
* `virtual bool` [GetToolTipAt](#afb826fe9b8964e4d843cae190170badf) (BPoint point, BToolTip **_tip) — Point _tip with the view's tool tip.

### Archiving

* `virtual status_t` [Archive](#a0f3fb624378a2d13617773713efedd98) (BMessage *archive, bool deep=true) const — Archives the object into the data message.
* `static BArchivable *` [Instantiate](#af3b2b4ad032238d71385bbfbf4933112) (BMessage *archive) — Instantiates a BTextView object from the passed in archive.

### Additional Inherited Members

* `static BArchivable *` [Instantiate](#a730a46bedfe8db2176e4c331330e7924) (BMessage *archive) — Creates a new BView object from the data message.
* `static BArchivable *` [Instantiate](#a0c23aeb48d578525f81ba6d47f968528) (BMessage *data) — Static method to instantiate a handler from an archived message.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BTextView()`

```cpp
BTextView::BTextView(BRect frame, const char * name, BRect textRect, uint32 resizeMask, uint32 flags = B_WILL_DRAW | B_PULSE_NEEDED)
```

Creates a new [BTextView](classBTextView.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `frame` | The frame rectangle of the view. |
| `name` | The name of the view. |
| `textRect` | The area of the text within the view. |
| `resizeMask` | Resizing mask, passed to [BView](classBView.md). |
| `flags` | *flags* passed to [BView](classBView.md), `B_FRAME_EVENTS`, `B_PULSE_NEEDED` and `B_INPUT_METHOD_AWARE` are always set. |





**See also:** [SetFontAndColor()](classBTextView.md#a48d9cccd617a4cab0e7a8ac26d0b63b9)



**Since:** BeOS R3

---

### `BTextView()`

```cpp
BTextView::BTextView(BRect frame, const char * name, BRect textRect, const BFont * initialFont, const rgb_color * initialColor, uint32 resizeMask, uint32 flags)
```

Creates a new [BTextView](classBTextView.md) object and sets the initial font and color. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `frame` | The [BTextView](classBTextView.md) frame rectangle. |
| `name` | The name of the object. |
| `textRect` | The area of the text within the [BTextView](classBTextView.md) object. |
| `initialFont` | The text font to display. |
| `initialColor` | The text color to display. |
| `resizeMask` | Resizing mask, passed to [BView](classBView.md). |
| `flags` | *flags* passed to [BView](classBView.md), `B_FRAME_EVENTS`, `B_PULSE_NEEDED` and `B_INPUT_METHOD_AWARE` are always set. |





**Since:** BeOS R3

---

### `BTextView()`

```cpp
BTextView::BTextView(const char * name, uint32 flags = B_WILL_DRAW | B_PULSE_NEEDED)
```

Creates a [BTextView](classBTextView.md) object, dynamic layout version. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the object. |
| `flags` | *flags* passed to [BView](classBView.md), `B_FRAME_EVENTS`, `B_PULSE_NEEDED` and `B_INPUT_METHOD_AWARE` are always set. |





**See also:** [SetFontAndColor()](classBTextView.md#a48d9cccd617a4cab0e7a8ac26d0b63b9)



**Since:** Haiku R1

---

### `BTextView()`

```cpp
BTextView::BTextView(const char * name, const BFont * initialFont, const rgb_color * initialColor, uint32 flags)
```

Creates a new [BTextView](classBTextView.md) object and sets the initial font and color, dynamic layout version. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the object. |
| `initialFont` | The text font to display. |
| `initialColor` | The text color to display. |
| `flags` | *flags* passed to [BView](classBView.md), `B_FRAME_EVENTS`, `B_PULSE_NEEDED` and `B_INPUT_METHOD_AWARE` are always set. |





**Since:** Haiku R1

---

### `BTextView()`

```cpp
BTextView::BTextView(BMessage * archive)
```

Creates a [BTextView](classBTextView.md) object from the passed in *archive*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The [BMessage](../application_kit/classBMessage.md) object from which the object is created. |





**Since:** BeOS R3

---

### `~BTextView()`

```cpp
BTextView::~BTextView()
```

Frees the memory allocated and destroys the object. 



**Since:** BeOS R3

---

### `AcceptsDrop()`

```cpp
bool BTextView::AcceptsDrop(const BMessage * message)
```

Returns whether or not the [BTextView](classBTextView.md) can accept the dropped *message* data. 



**Returns:** `true` if the [BTextView](classBTextView.md) can accept the dropped message data, `false` otherwise.



**Since:** BeOS R3

---

### `AcceptsPaste()`

```cpp
bool BTextView::AcceptsPaste(BClipboard * clipboard)
```

Returns whether or not the [BTextView](classBTextView.md) can accept the *clipboard* data. 



**Returns:** `true` if the [BTextView](classBTextView.md) can accept the pasted clipboard data, `false` otherwise.



**Since:** BeOS R3

---

### `AdoptSystemColors()`

```cpp
BTextView::AdoptSystemColors()
```

Adopts document colors tinted to match panel background if uneditable. 



* `B_DOCUMENT_BACKGROUND_COLOR` for [ViewUIColor()](classBView.md#aec6c89446eb4f5ded151adced9126df8)

* `B_DOCUMENT_BACKGROUND_COLOR` for [LowUIColor()](classBView.md#ae32ca6d8f106d44b5b51df82a7eb64c5)

* `B_DOCUMENT_TEXT_COLOR` for [HighUIColor()](classBView.md#aa86f548fba2e82d022066198be6d5af6)



This is reimplemented from [BView](classBView.md) which uses panel colors.


View and low colors tinted `B_DARKEN_1_TINT` (inverse on dark) if uneditable.


Does not alter text color.



**See also:** [BView::AdoptSystemColors()](classBView.md#a0e429a82fe06e9ab390b06d993ee31be), [MakeEditable()](classBTextView.md#aebdfde8ef7cf1a490c96fc4f0d822873), [HasSystemColors()](classBTextView.md#a3350d32c812789042cd7f769220d0ed9)



**Since:** Haiku R1

---

### `Alignment()`

```cpp
alignment BTextView::Alignment()const
```

Returns the current text alignment. 



**Returns:** The current alignment flag.



**See also:** [SetAlignment()](classBTextView.md#ae71fcc418e9934a852b0e5c9d6d6961b)



**Since:** BeOS R3

---

### `AllAttached()`

```cpp
void BTextView::AllAttached()
```

Similar to [AttachedToWindow()](classBTextView.md#a73a892fb4d5e7e3575064f326b67867a) but this method is triggered after all child views have already been attached to a window.  



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a6d6379e0993bd525f2cac5f848718870).

---

### `AllDetached()`

```cpp
void BTextView::AllDetached()
```

Similar to [AttachedToWindow()](classBTextView.md#a73a892fb4d5e7e3575064f326b67867a) but this method is triggered after all child views have already been detached from a window.  



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a19dd2213f4b953b54524d7f523d9b406).

---

### `AllowChar()`

```cpp
void BTextView::AllowChar(uint32 character)
```

Removes the *character* from the disallowed characters list. 


After this method returns, the *character* will be accepted by the textview.


Parameters

| Parameter | Description |
| :--- | :--- |
| `character` | The character to allow. |





**See also:** [DisallowChar()](classBTextView.md#a91836216cb18b6030bb7949c0a72a4dd)



**Since:** BeOS R3

---

### `Archive()`

```cpp
status_t BTextView::Archive(BMessage * data, bool deep = true)const
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
| B_OK | The object was archived. |
| B_NO_MEMORY | Ran out of memory while archiving the object. |





**Since:** BeOS R3


Reimplemented from [BView](classBView.md#ab6de1b48cbc3ef15a0d02113036f002d).

---

### `AttachedToWindow()`

```cpp
void BTextView::AttachedToWindow()
```

Hook method called when the text view is added to the view hierarchy. 


Sets the pulse rate to 2 per second and adjust scrollbars if needed.



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#ae8117cb4634f4a4413988eea07cf75a0).

---

### `ByteAt()`

```cpp
uchar BTextView::ByteAt(int32 offset)const
```

Returns the character at the given offset. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `offset` | The offset to the desired character. |





**Returns:** The character at the given offset.



**Since:** BeOS R3

---

### `CanEndLine()`

```cpp
bool BTextView::CanEndLine(int32 offset)
```

Returns whether or not the character at the given offset can be the last character of a line. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `offset` | The offset of the character. |





**Returns:** `true` if the character can be the last character of a line, `false` otherwise.



**Since:** BeOS R3

---

### `Clear()`

```cpp
void BTextView::Clear()
```

Deletes the currently selected text. 



**Since:** BeOS R4

---

### `ColorSpace()`

```cpp
color_space BTextView::ColorSpace()const
```

Returns the colorspace set to the offscreen [BBitmap](classBBitmap.md) object. 



**Returns:** The colorspace of the offscreen [BBitmap](classBBitmap.md) object.



**See also:** [SetColorSpace()](classBTextView.md#aaf45743e5d825b7e4eb77fe770d14cb3)



**Since:** BeOS R3

---

### `Copy()`

```cpp
void BTextView::Copy(BClipboard * clipboard)
```

Copies the current selection to the clipboard. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `clipboard` | The clipboard object to copy the selected text to. |





**Since:** BeOS R3

---

### `CountLines()`

```cpp
int32 BTextView::CountLines()const
```

Returns the number of lines that the [BTextView](classBTextView.md) object contains. 



**Returns:** The number of lines contained in the [BTextView](classBTextView.md) object.



**Since:** BeOS R3

---

### `CurrentLine()`

```cpp
int32 BTextView::CurrentLine()const
```

Returns the index of the current line. 



**Returns:** The index of the current line.



**Since:** BeOS R3

---

### `Cut()`

```cpp
void BTextView::Cut(BClipboard * clipboard)
```

Moves the current selection to the clipboard. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `clipboard` | The clipboard object to move the text to. |





**Since:** BeOS R3

---

### `Delete()`

```cpp
void BTextView::Delete()
```

Deletes the text within the current selection. 



**Since:** BeOS R3

---

### `Delete()`

```cpp
void BTextView::Delete(int32 startOffset, int32 endOffset)
```

Deletes the text enclosed within the given offsets. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `startOffset` | The offset where the text to delete starts. |
| `endOffset` | The offset where the text to delete ends. |





**Since:** BeOS R3

---

### `DetachedFromWindow()`

```cpp
void BTextView::DetachedFromWindow()
```

Hook method that is called when the text view is removed from the view hierarchy. 



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a8abc2ea500951a0a22cf018e958ba791).

---

### `DisallowChar()`

```cpp
void BTextView::DisallowChar(uint32 character)
```

Adds the *character* to the disallowed characters list. 


After this method returns, the *character* won't be accepted by the textview anymore.


Parameters

| Parameter | Description |
| :--- | :--- |
| `character` | The character to disallow. |





**See also:** [AllowChar()](classBTextView.md#aa2b793d153eb61478f5d849fa32a5084)



**Since:** BeOS R3

---

### `DoesAutoindent()`

```cpp
bool BTextView::DoesAutoindent()const
```

Returns whether or not automatic indenting is active. 



**Returns:** `true` if automatic indenting is activated, `false` otherwise.



**See also:** [SetAutoindent()](classBTextView.md#abd09cfa6752d3e808770d17065d6d4ec)



**Since:** BeOS R3

---

### `DoesUndo()`

```cpp
bool BTextView::DoesUndo()const
```

Returns whether or not the undo mechanism is enabled. 



**Returns:** `true` if undo is enabled, `false` otherwise.



**See also:** [SetDoesUndo()](classBTextView.md#a21286b9caeb086eff3728daea6d5f9ac)



**Since:** BeOS R3

---

### `DoesWordWrap()`

```cpp
bool BTextView::DoesWordWrap()const
```

Returns whether or not word wrapping is activated. 



**Returns:** `true` if word wrapping is activated, `false` is word wrapping if not activated.



**See also:** [SetWordWrap()](classBTextView.md#afe3b998f71371ae8479ac72ef3b4fb08)



**Since:** BeOS R3

---

### `DoLayout()`

```cpp
virtual void BTextView::DoLayout()
```

Layout view within the layout context. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Since:** Haiku R1


Reimplemented from [BView](classBView.md#a9d766a06d0885200c6ababba4c87808b).

---

### `Draw()`

```cpp
void BTextView::Draw(BRect updateRect)
```

Hook method called to draw the contents of the text view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `updateRect` | The rectangular area to draw. |





**Since:** BeOS R3


Reimplemented from [BView](classBView.md#aa55014241fc2f5556415850692b52db2).

---

### `FindWord()`

```cpp
void BTextView::FindWord(int32 offset, int32 * _fromOffset, int32 * _toOffset)
```

Fills out *_fromOffset* and *_toOffset* for a sequence of character that qualifies as a word starting at *offset*. 


A word is a sequence of characters that the user can select by double- clicking.


Parameters

| Parameter | Description |
| :--- | :--- |
| `offset` | The offset where to start looking. |
| `_fromOffset` | A pointer to an integer to write the starting offset. |
| `_toOffset` | A pointer to an integer to write the ending offset. |





**Since:** BeOS R3

---

### `FrameResized()`

```cpp
void BTextView::FrameResized(float newWidth, float newHeight)
```

Hook method that is called when the frame is resized. 


This method updates any associated scrollbars.


Parameters

| Parameter | Description |
| :--- | :--- |
| `newWidth` | The new width of the view. |
| `newHeight` | The new height of the view. |





**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a85d88f9c2bb6800560874b2061378fa0).

---

### `GetFontAndColor()`

```cpp
void BTextView::GetFontAndColor(BFont * _font, uint32 * _mode, rgb_color * _color = NULL, bool * _sameColor = NULL)const
```

Fill out *_font*, *_mode*, *_color* and *sameColor* with the font and color of the current selection. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `_font` | The [BFont](classBFont.md) to fill out. |
| `_mode` | The font mode. |





**See also:** [SetFontAndColor()](classBTextView.md#a48d9cccd617a4cab0e7a8ac26d0b63b9) for mode.


Parameters

| Parameter | Description |
| :--- | :--- |
| `_color` | The [rgb_color](structrgb__color.md) to fill out. |
| `_sameColor` | Whether or not the color is the same as passed in. |





**Since:** BeOS R3

---

### `GetFontAndColor()`

```cpp
void BTextView::GetFontAndColor(int32 offset, BFont * _font, rgb_color * _color = NULL)const
```

Fill out *_font* and *_color* at specified text *offset*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `offset` | The text *offset* to fill in the *_font* and *_color* from. |
| `_font` | The [BFont](classBFont.md) to fill out. |
| `_color` | The [rgb_color](structrgb__color.md) to fill out. |





**Since:** BeOS R3

---

### `GetHeightForWidth()`

```cpp
virtual void BTextView::GetHeightForWidth(float width, float * min, float * max, float * preferred)
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


Reimplemented from [BView](classBView.md#ad34bee968b1ec98a0bf89343340b6b07).

---

### `GetInsets()`

```cpp
void BTextView::GetInsets(float * _left, float * _top, float * _right, float * _bottom)const
```

Fills out the parameters with the objects's text insets. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `_left` | A pointer to set to the frame's left inset. |
| `_top` | A pointer to set to the frame's top inset. |
| `_right` | A pointer to set to the frame's right inset. |
| `_bottom` | A pointer to set to the frame's bottom inset. |





**Since:** BeOS R3

---

### `GetPreferredSize()`

```cpp
virtual void BTextView::GetPreferredSize(float * _width, float * _height)
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


Reimplemented from [BView](classBView.md#a089c3ff794c454388a9388c7b6568478).

---

### `GetSelection()`

```cpp
void BTextView::GetSelection(int32 * _start, int32 * _end)const
```

Fills out *_start* and *_end* with the start and end offsets of the current selection. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `_start` | A pointer to an int32 to contain the selection's start offset. |
| `_end` | A pointer to an int32 to contain the selection's end offset. |





**See also:** [Select()](classBTextView.md#a35737d4bef49712542b12b1a5add2520)



**Since:** BeOS R3

---

### `GetSupportedSuites()`

```cpp
virtual status_t BTextView::GetSupportedSuites(BMessage * data)
```

Reports the suites of messages and specifiers that derived classes understand.  



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a772462d751d457f63ee0fc56d8ba02d1).

---

### `GetText()`

```cpp
BTextView::GetText(int32 offset, int32 length, char * buffer)const
```

Fills out *buffer* with the text of the [BTextView](classBTextView.md) starting at *offset* and grabbing at most *length* bytes. 


You must provide a *buffer* that is large enough to hold at least *length* bytes.


Parameters

| Parameter | Description |
| :--- | :--- |
| `offset` | Where to start grabbing text from. |
| `length` | The number of bytes of text to grab. |
| `buffer` | A *buffer* to write the text to. |





**See also:** BString::GetString(int32 offset, int32 length, char* buffer)



**Since:** BeOS R3

---

### `GoToLine()`

```cpp
void BTextView::GoToLine(int32 index)
```

Moves the caret to the specified line. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index of the line. |





**Since:** BeOS R3

---

### `HasHeightForWidth()`

```cpp
virtual bool BTextView::HasHeightForWidth()
```

Returns whether the layout of the view can calculate a height for a given width. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).
Use [GetHeightForWidth()](classBTextView.md#aec7881d97bdc508b01a6caa80f51d963) to actually get the preferred size.



**Returns:** `true` if the height values can be calculated, `false` if they cannot.



**Since:** Haiku R1


Reimplemented from [BView](classBView.md#abd411461b7e23ad17e7294f8f5e1cbeb).

---

### `HasSystemColors()`

```cpp
bool BTextView::HasSystemColors()const
```

Tests whether or not the text view is using system colors. 



* `B_DOCUMENT_BACKGROUND_COLOR` for [ViewUIColor()](classBView.md#aec6c89446eb4f5ded151adced9126df8) either untinted or `B_DARKEN_1_TINT`

* `B_DOCUMENT_BACKGROUND_COLOR` for [LowUIColor()](classBView.md#ae32ca6d8f106d44b5b51df82a7eb64c5) either untinted or `B_DARKEN_1_TINT`

* `B_DOCUMENT_TEXT_COLOR` for [HighUIColor()](classBView.md#aa86f548fba2e82d022066198be6d5af6) untinted



Does not consider text color.



**Returns:** `true` if using system colors either untinted or using uneditable tint `false` otherwise.



**See also:** [AdoptSystemColors()](classBTextView.md#a26acfabf11a50b255127624dc544a61d), [MakeEditable()](classBTextView.md#aebdfde8ef7cf1a490c96fc4f0d822873)



**Since:** Haiku R1

---

### `HideTyping()`

```cpp
void BTextView::HideTyping(bool enabled)
```

Enables and disables type hiding. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `enabled` | Pass in `true` to enable type hiding, `false` to disable it. |





**Since:** BeOS R5

---

### `Highlight()`

```cpp
void BTextView::Highlight(int32 startOffset, int32 endOffset)
```

Highlight the text enclosed within the given offsets. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `startOffset` | The start offset of the text to highlight. |
| `endOffset` | The end offset of the text to highlight. |





**Since:** BeOS R3

---

### `Insert()`

```cpp
void BTextView::Insert(const char * text, const text_run_array * runs = NULL)
```

Inserts text from the *text* buffer at the end of the [BTextView](classBTextView.md) with the font and color formats set by *runs*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `text` | The text to insert. |
| `runs` | The text styling to set, can be `NULL`. |





**Since:** BeOS R3

---

### `Insert()`

```cpp
void BTextView::Insert(const char * text, int32 length, const text_run_array * runs = NULL)
```

Inserts text from the *text* buffer up to *length* characters at the end of the [BTextView](classBTextView.md) with the font and color formats set by *runs*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `text` | The text to insert. |
| `length` | The number of bytes of text to insert. |
| `runs` | The text styling to use, can be `NULL`. |





**Since:** BeOS R3

---

### `Insert()`

```cpp
void BTextView::Insert(int32 offset, const char * text, int32 length, const text_run_array * runs = NULL)
```

Inserts text starting at the given *offset* from the *text* buffer up to *length* characters into the [BTextView](classBTextView.md) with the font and color formats set by *runs*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `offset` | The position to start inserting text. |
| `text` | The text to set. |
| `length` | The number of bytes of text to insert. |
| `runs` | The text styling to use, can be `NULL`. |





**Since:** BeOS R3

---

### `Instantiate()`

```cpp
BArchivable * BTextView::Instantiate(BMessage * archive)
```

Instantiates a [BTextView](classBTextView.md) object from the passed in *archive*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The [BMessage](../application_kit/classBMessage.md) object that the object is created from. |





**Returns:** A new [BTextView](classBTextView.md) object as a [BArchivable](../support_kit/classBArchivable.md).



**Since:** BeOS R3

---

### `IsEditable()`

```cpp
bool BTextView::IsEditable()const
```

Returns whether or not the text is editable. 



**Returns:** `true` if the text is editable, `false` if the text is not editable.



**See also:** [MakeEditable()](classBTextView.md#aebdfde8ef7cf1a490c96fc4f0d822873)



**Since:** BeOS R3

---

### `IsResizable()`

```cpp
bool BTextView::IsResizable()const
```

Returns whether or not the object is resizable. 



**Returns:** `true` if the object is resizable, `false` otherwise.



**See also:** [MakeResizable()](classBTextView.md#a106796bac011113352981917f001f24f)



**Since:** BeOS R3

---

### `IsSelectable()`

```cpp
bool BTextView::IsSelectable()const
```

Returns whether or not the text is selectable. 



**Returns:** `true` if the text is selectable, `false` if the text is not selectable.



**See also:** [MakeSelectable()](classBTextView.md#aa7bbd890c204b973daae9b82b657e117)



**Since:** BeOS R3

---

### `IsStylable()`

```cpp
bool BTextView::IsStylable()const
```

Returns whether or not the object accepts multiple font styles. 



**Returns:** `true` if the object is accepts multiple font styles, `false` otherwise.



**See also:** [SetStylable()](classBTextView.md#af7ff7c6ed79a7deaf1ff180b0b2fc597)



**Since:** BeOS R3

---

### `IsTypingHidden()`

```cpp
bool BTextView::IsTypingHidden()const
```

Returns whether or not typing is hidden. 



**Returns:** `true` if typing is hidden, `false` otherwise.



**See also:** [HideTyping()](classBTextView.md#a0461eff711af1cc8f797143ea4a932f1)



**Since:** BeOS R5

---

### `KeyDown()`

```cpp
void BTextView::KeyDown(const char * bytes, int32 numBytes)
```

Hook method that is called when a key is pressed while the view is the focus view of the active window. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `bytes` | The bytes of the key combination pressed. |
| `numBytes` | The number of bytes in *bytes*. |





**Since:** BeOS R3


Reimplemented from [BView](classBView.md#abea50ea665ce5fcb76b32f1302a6852d).

---

### `LayoutInvalidated()`

```cpp
virtual void BTextView::LayoutInvalidated(bool descendants)
```

Hook method called when the layout is invalidated. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `descendants` | Whether or not child views have also been invalidated. |





**Since:** Haiku R1


Reimplemented from [BView](classBView.md#a0a552cc0d8678939c619f98dcc80d254).

---

### `LineAt()`

```cpp
int32 BTextView::LineAt(BPoint point)const
```

Returns the line number for the passed point. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The point to get the line number of. |





**Returns:** The line number for the passed in point.



**Since:** BeOS R3

---

### `LineAt()`

```cpp
int32 BTextView::LineAt(int32 offset)const
```

Returns the line number of the character at the given offset. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `offset` | The offset of the wanted character. |





**Returns:** The line number of the character at the given offset.



**Since:** BeOS R3

---

### `LineHeight()`

```cpp
float BTextView::LineHeight(int32 lineNumber = 0)const
```

Returns the height of the line at the given *lineNumber*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `lineNumber` | The index of the line to get the height of, 0-indexed. |





**Returns:** The height of the line at the given *lineNumber* as a float.



**Since:** BeOS R3

---

### `LineWidth()`

```cpp
float BTextView::LineWidth(int32 lineNumber = 0)const
```

Returns the width of the line at the given *lineNumber*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `lineNumber` | The index of the line to get the width of, 0-indexed. |





**Returns:** The width of the line at the given *lineNumber* as a float.



**Since:** BeOS R3

---

### `MakeEditable()`

```cpp
void BTextView::MakeEditable(bool editable = true)
```

Sets whether or not the text is editable. 


Will automatically tint document colors to indicate uneditable if you have previously called [AdoptSystemColors()](classBTextView.md#a26acfabf11a50b255127624dc544a61d).


Parameters

| Parameter | Description |
| :--- | :--- |
| `editable` | Pass in `true` to set the text to be editable, `false` to set the object to be not editable. |





**See also:** [AdoptSystemColors()](classBTextView.md#a26acfabf11a50b255127624dc544a61d)



**Since:** BeOS R3

---

### `MakeFocus()`

```cpp
void BTextView::MakeFocus(bool focus = true)
```

Highlight or unhighlight the selection when the text view acquires or loses its focus state. 


The focus view handles selections and KeyDown events when the the attached window is active. There can be only one focus view at a time per window.


When called with *focus* set to `true` this method first calls [MakeFocus()](classBTextView.md#ac0bc816f13b04fd2ec2668c618ab8ca8) on the previously focused view with *focus* set to `false`.


The focus doesn't automatically change when [MouseDown()](classBTextView.md#a581a2b2877b29d275771ae5010d6706d) is called so calling [MakeFocus()](classBTextView.md#ac0bc816f13b04fd2ec2668c618ab8ca8) is the only way to make a view the focus view of a window. Classes derived from [BView](classBView.md) that can display the current selection, or that can accept pasted data should call [MakeFocus()](classBTextView.md#ac0bc816f13b04fd2ec2668c618ab8ca8) in their [MouseDown()](classBTextView.md#a581a2b2877b29d275771ae5010d6706d) method to update the focus view of the window on click.


If the view isn't attached to a window this method has no effect.


Parameters

| Parameter | Description |
| :--- | :--- |
| `focus` | *true* to set focus, *false* to remove it. |





**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a266a368d81c6e1668b2b9b22b5016853).

---

### `MakeResizable()`

```cpp
void BTextView::MakeResizable(bool resize, BView * resizeView = NULL)
```

Activates and deactivates automatic resizing. 


The resizing mechanism is alternative to [BView](classBView.md) resizing. The container view (the one passed to this function) should not automatically resize itself when the parent is resized.


Parameters

| Parameter | Description |
| :--- | :--- |
| `resize` | Pass in `true` to set the the [BTextView](classBTextView.md) to automatically resize itself, `false` to disable automatic resizing. |
| `resizeView` | The [BTextView](classBTextView.md) object's parent view that resizes itself. |





**Since:** BeOS R3

---

### `MakeSelectable()`

```cpp
void BTextView::MakeSelectable(bool selectable = true)
```

Sets whether or not the text is selectable. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `selectable` | Pass in `true` to set the text to be selectable, `false` to set the text to be not selectable. |





**Since:** BeOS R3

---

### `MaxBytes()`

```cpp
int32 BTextView::MaxBytes()const
```

Returns the maximum number of bytes that the [BTextView](classBTextView.md) can contain. 



**Returns:** the maximum number of bytes that the [BTextView](classBTextView.md) can contain.



**See also:** [SetMaxBytes()](classBTextView.md#a233e3150486c81394d3bfe44dad0babe)



**Since:** BeOS R3

---

### `MaxSize()`

```cpp
virtual BSize BTextView::MaxSize()
```

Return the maximum size of the view. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Returns:** The maximum size of the view as a [BSize](classBSize.md).



**See also:** [BAbstractLayout::MaxSize()](classBAbstractLayout.md#ad1ea5d04a5c8028f8295efde7106a66c)



**Since:** Haiku R1


Reimplemented from [BView](classBView.md#ad1f1843a380e850948cf7e4ed2d5f1ba).

---

### `MessageReceived()`

```cpp
void BTextView::MessageReceived(BMessage * message)
```

Hook method called with a message is received by the text view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The *message* received by the associated looper. |





**See also:** [BHandler::MessageReceived()](../application_kit/classBHandler.md#aeecda5017e0081db617f23bbff71fb53)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#aca0a16b0e04288e1fdc0b63690ea7a6d).

---

### `MinSize()`

```cpp
virtual BSize BTextView::MinSize()
```

Return the minimum size of the view. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Returns:** The minimum size of the view as a [BSize](classBSize.md).



**See also:** [BAbstractLayout::MinSize()](classBAbstractLayout.md#a3f692cb3306ce726e3cc6d2771824cd5)



**Since:** Haiku R1


Reimplemented from [BView](classBView.md#acfb0cffde35b853dab6bc5d1bb03265f).

---

### `MouseDown()`

```cpp
void BTextView::MouseDown(BPoint where)
```

Hook method that is called when a mouse button is pushed down while the cursor is contained in the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `where` | The point on the screen where the mouse pointer is when the mouse button is pressed. |





**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a5f5bd975d15df94f2ebbc80eb79cc3f6).

---

### `MouseMoved()`

```cpp
void BTextView::MouseMoved(BPoint where, uint32 code, const BMessage * dragMessage)
```

Hook method that is called whenever the mouse cursor enters, exits or moves inside the view. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `where` | The new location of the mouse in the view's coordinate system. |
| `code` | One of the following: * `B_ENTERED_VIEW` The cursor has just entered the view.  * `B_INSIDE_VIEW` The cursor is inside the view.  * `B_EXITED_VIEW` The cursor has left the view's bounds. This only gets sent if the scope of the mouse events that the view can receive has been expanded by [SetEventMask()](classBView.md#a5d8d6b469a8a11a577d1d138cfc31162) or [SetMouseEventMask()](classBView.md#ae7705783d064a8613dcc6f36a2866ab2).  * `B_OUTSIDE_VIEW` The cursor is outside the view. This only gets sent if the scope of the mouse events that the view can receive has been expanded by [SetEventMask()](classBView.md#a5d8d6b469a8a11a577d1d138cfc31162) or [SetMouseEventMask()](classBView.md#ae7705783d064a8613dcc6f36a2866ab2). |
| `dragMessage` | If a drag-and-drop operation is taking place this is a pointer to a [BMessage](../application_kit/classBMessage.md) that holds the drag information, otherwise the pointer is `NULL`. |





**See also:** [SetEventMask()](classBView.md#a5d8d6b469a8a11a577d1d138cfc31162), [SetMouseEventMask()](classBView.md#ae7705783d064a8613dcc6f36a2866ab2)



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#ac8b20516e42bab2f1eeb130e2432bde0).

---

### `MouseUp()`

```cpp
void BTextView::MouseUp(BPoint where)
```

Hook method that is called when a mouse button is released while the cursor is contained in the view. 


This method stops asynchronous mouse tracking.


Parameters

| Parameter | Description |
| :--- | :--- |
| `where` | The point on the screen where the mouse pointer is when the mouse button is released. |





> [!NOTE]
> Calling [GetMouse()](classBView.md#a830ce9cf2ac2ffb5f73f526ee5d6e53d) in [MouseUp()](classBTextView.md#a72a0cd6839b541db996d751f240e59a1) will return the new state of the mouse buttons (after the mouse button was released). If you want to know which button was released, you have to compare that with the previous state of the buttons, that you can memorize for example by calling [GetMouse()](classBView.md#a830ce9cf2ac2ffb5f73f526ee5d6e53d) in [MouseDown()](classBTextView.md#a581a2b2877b29d275771ae5010d6706d).



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#acdb92b30069157b2e3c522a3ef9d6ae4).

---

### `OffsetAt()`

```cpp
int32 BTextView::OffsetAt(BPoint point)const
```

Returns the offset at the passed in point. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | The desired point. |





**Returns:** The offset for the passed in point.



**Since:** BeOS R3

---

### `OffsetAt()`

```cpp
int32 BTextView::OffsetAt(int32 line)const
```

Returns the offset of the given line. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `line` | A line number. |





**Returns:** The offset of the passed line.



**Since:** BeOS R3

---

### `Paste()`

```cpp
void BTextView::Paste(BClipboard * clipboard)
```

Copy the text contained in the clipboard to the [BTextView](classBTextView.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `clipboard` | A pointer to the clipboard. |





**Since:** BeOS R3

---

### `Perform()`

```cpp
virtual status_t BTextView::Perform(perform_code code, void * _data)
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

---

### `PointAt()`

```cpp
BPoint BTextView::PointAt(int32 offset, float * _height = NULL)const
```

Returns the location of the character at the given offset. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `offset` | The offset of the character. |
| `_height` | A pointer to write the height of the character. |





**Returns:** A [BPoint](classBPoint.md) object set to the location of the character.



**Since:** BeOS R3

---

### `PreferredSize()`

```cpp
virtual BSize BTextView::PreferredSize()
```

Return the preferred size of the view. 


RemarksThis is only meaningful if the view is part of a [BLayout](classBLayout.md).

**Returns:** The preferred size of the view as a [BSize](classBSize.md).



**See also:** [BAbstractLayout::PreferredSize()](classBAbstractLayout.md#af5f21d9900c85ca053dba3938bef3fd3)



**Since:** Haiku R1


Reimplemented from [BView](classBView.md#a7f51d63e71b60a2721d04436ffbcfe36).

---

### `Pulse()`

```cpp
void BTextView::Pulse()
```

Hook method that is called at a set interval. 


This method is used to make the I-beam cursor blink.


An action is performed each time the App Server calls the [Pulse()](classBTextView.md#ada90a85565bd3e6bbe130901299c6da8) method. The pulse rate is set by SetPulseRate(). You can implement [Pulse()](classBTextView.md#ada90a85565bd3e6bbe130901299c6da8) to do anything you want. The default version does nothing. The pulse granularity is no better than once per 100,000 microseconds.



**See also:** SetPulseRate()



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a0ae8ec3e94ee3d41cb329e3df6966566).

---

### `ResizeToPreferred()`

```cpp
virtual void BTextView::ResizeToPreferred()
```

Resizes the view to its preferred size keeping the position of the left top corner constant. 



> [!WARNING]
> It is not recommended to use this method for views that are part of a [BLayout](classBLayout.md).



**Since:** BeOS R3


Reimplemented from [BView](classBView.md#abe8c63c85555e800e063388e7cf3e1a7).

---

### `ResolveSpecifier()`

```cpp
BHandler * BTextView::ResolveSpecifier(BMessage * message, int32 index, BMessage * specifier, int32 what, const char * property)
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

---

### `RunArray()`

```cpp
text_run_array * BTextView::RunArray(int32 startOffset, int32 endOffset, int32 * _size = NULL)const
```

Returns a `text_run_array` for the text within the given offsets. 


The returned `text_run_array` belongs to the caller, so you must free it once you no longer need it.


Parameters

| Parameter | Description |
| :--- | :--- |
| `startOffset` | The text start offset. |
| `endOffset` | The text end offset. |
| `_size` | A pointer to an int32 to fill out the run array size. |





**Returns:** A `text_run_array` for the text in the given offsets.



**See also:** SetRunArray()



**Since:** BeOS R3

---

### `ScrollToOffset()`

```cpp
void BTextView::ScrollToOffset(int32 offset)
```

Scrolls the text so that the character at *offset* is visible. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `offset` | The offset of the character to scroll to. |





**Since:** BeOS R3

---

### `ScrollToSelection()`

```cpp
void BTextView::ScrollToSelection()
```

Scrolls the text so that the character that begins the selection is visible. 



**Since:** BeOS R3

---

### `Select()`

```cpp
void BTextView::Select(int32 startOffset, int32 endOffset)
```

Selects the text contained within the given offsets. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `startOffset` | The offset where the text to select starts. |
| `endOffset` | The offset where the text to select ends. |





**Since:** BeOS R3

---

### `SelectAll()`

```cpp
void BTextView::SelectAll()
```

Selects all text contained in the [BTextView](classBTextView.md). 



**See also:** [Select()](classBTextView.md#a35737d4bef49712542b12b1a5add2520)



**Since:** BeOS R3

---

### `SetAlignment()`

```cpp
void BTextView::SetAlignment(alignment flag)
```

Sets the way text is aligned within the frame. 


Choices are:


* `B_ALIGN_LEFT`

* `B_ALIGN_RIGHT`

* `B_ALIGN_CENTER`



Parameters

| Parameter | Description |
| :--- | :--- |
| `flag` | The text alignment to set. |





**Since:** BeOS R3

---

### `SetAutoindent()`

```cpp
void BTextView::SetAutoindent(bool state)
```

Sets whether or not new lines of text are automatically indented. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `state` | Pass in `true` to automatically indent the text, `false` to turn off automatic text indenting. |





**Since:** BeOS R3

---

### `SetColorSpace()`

```cpp
void BTextView::SetColorSpace(color_space colors)
```

Set the color space of the offscreen [BBitmap](classBBitmap.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `colors` | The colorspace to set on the offscreen [BBitmap](classBBitmap.md) object. |





**Since:** BeOS R3

---

### `SetDoesUndo()`

```cpp
void BTextView::SetDoesUndo(bool undo)
```

Enables and disables the undo mechanism. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `undo` | Pass in `true` to enable the undo mechanism, `false` to disable it. |





**Since:** BeOS R3

---

### `SetFontAndColor()`

```cpp
void BTextView::SetFontAndColor(const BFont * font, uint32 mode = B_FONT_ALL, const rgb_color * color = NULL)
```

Set *font* and text *color* of the current selection. The default *mode* is `B_FONT_ALL`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `font` | The [BFont](classBFont.md) to set, a copy is made. |
| `mode` | Font mode bitmap of one or more the following constants: * `B_FONT_ALL`  * `B_FONT_FAMILY_AND_STYLE`  * `B_FONT_SIZE`  * `B_FONT_SHEAR`  * `B_FONT_ROTATION`  * `B_FONT_SPACING`  * `B_FONT_ENCODING`  * `B_FONT_FACE`  * `B_FONT_FLAGS`  * `B_FONT_FALSE_BOLD_WIDTH` |
| `color` | The text color to set, a copy is made. `NULL` to keep the current color. |





**Since:** BeOS R3

---

### `SetFontAndColor()`

```cpp
void BTextView::SetFontAndColor(int32 startOffset, int32 endOffset, const BFont * font, uint32 mode = B_FONT_ALL, const rgb_color * color = NULL)
```

Set the font and color of a selection starting at *startoffset* ending at *endOffset*. The default *mode* is `B_FONT_ALL`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `startOffset` | The start offset. |
| `endOffset` | The end offset. |
| `font` | The [BFont](classBFont.md) to set, a copy is made. |
| `mode` | Font mode bitmap of one or more the following constants: * `B_FONT_ALL`  * `B_FONT_FAMILY_AND_STYLE`  * `B_FONT_SIZE`  * `B_FONT_SHEAR`  * `B_FONT_ROTATION`  * `B_FONT_SPACING`  * `B_FONT_ENCODING`  * `B_FONT_FACE`  * `B_FONT_FLAGS`  * `B_FONT_FALSE_BOLD_WIDTH` |
| `color` | The text color to set, a copy is made. `NULL` to keep the current color. |





**Since:** BeOS R3

---

### `SetInsets()`

```cpp
void BTextView::SetInsets(float left, float top, float right, float bottom)
```

Sets the insets within the bounds for the object's text frame. 



> [!NOTE]
> Insets cannot be negative, will result in 0 inset.


Parameters

| Parameter | Description |
| :--- | :--- |
| `left` | The left inset to set. |
| `top` | The top inset to set. |
| `right` | The right inset to set. |
| `bottom` | The bottom inset to set. |





**Since:** Haiku R1

---

### `SetMaxBytes()`

```cpp
void BTextView::SetMaxBytes(int32 max)
```

Sets the maximum number of bytes that the [BTextView](classBTextView.md) can contain. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `max` | The maximum number of bytes to set. |





**Since:** BeOS R3

---

### `SetStylable()`

```cpp
void BTextView::SetStylable(bool stylable)
```

Sets whether or not the object accepts multiple font styles. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `stylable` | `true` to accept multiple font styles, `false` to NOT accept multiple font styles. |





**Since:** BeOS R3

---

### `SetTabWidth()`

```cpp
void BTextView::SetTabWidth(float width)
```

Sets the distance between tab stops in pixels. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `width` | The distance in pixel between tab stops to set. |





**Since:** BeOS R3

---

### `SetText()`

```cpp
void BTextView::SetText(BFile * file, int32 offset, int32 length, const text_run_array * runs = NULL)
```

Copies text from the *file* starting at the given *offset* up to *length* characters replacing any text currently set in the [BTextView](classBTextView.md) with the font and color formats set by *runs*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | The file to set the text from. |
| `offset` | The position in the file to start reading text. |
| `length` | The number of bytes of text to read from the file. |
| `runs` | Set the font and color formats of the new text if provided. Only applies if the [BTextView](classBTextView.md) permits multiple character formats. |





**Since:** BeOS R3

---

### `SetText()`

```cpp
void BTextView::SetText(const char * text, const text_run_array * runs = NULL)
```

Copies text from the *text* buffer replacing any text currently set in the [BTextView](classBTextView.md) with the font and color formats set by *runs*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `text` | The text to set. |
| `runs` | Set the font and color formats of the new text if provided. Only applies if the [BTextView](classBTextView.md) permits multiple character formats. |





**Since:** BeOS R3

---

### `SetText()`

```cpp
void BTextView::SetText(const char * text, int32 length, const text_run_array * runs = NULL)
```

Copies text from the *text* buffer up to *length* characters replacing any text currently set in the [BTextView](classBTextView.md) with the font and color formats set by *runs*. 


*text* must be at least *length* characters long. *length* may be set to 0 to clear the text from the [BTextView](classBTextView.md).


Parameters

| Parameter | Description |
| :--- | :--- |
| `text` | The text to set. |
| `length` | The maximum number of bytes of *text* to use. |
| `runs` | Set the font and color formats of the new text if provided. Only applies if the [BTextView](classBTextView.md) permits multiple character formats. |





**Since:** BeOS R3

---

### `SetTextRect()`

```cpp
void BTextView::SetTextRect(BRect rect)
```

Sets the object's text frame to the passed in *rect*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `rect` | A [BRect](classBRect.md) object to set the text frame to. |





**Since:** BeOS R3

---

### `SetWordWrap()`

```cpp
void BTextView::SetWordWrap(bool wrap)
```

Activate or deactivate word wrapping mode. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `wrap` | Pass in `true` to turn on word wrapping mode, `false` to turn off word wrapping mode. |





**Since:** BeOS R3

---

### `TabWidth()`

```cpp
float BTextView::TabWidth()const
```

Returns the tab width of the [BTextView](classBTextView.md). 



**Returns:** The tab width of the [BTextView](classBTextView.md).



**See also:** [SetTabWidth()](classBTextView.md#a692c0cf4d5ad343d35ca12bcdf7e44f0)



**Since:** BeOS R3

---

### `Text()`

```cpp
const char * BTextView::Text()const
```

Returns the [BTextView](classBTextView.md) text as a byte array. 



> [!WARNING]
> It is possible that the [BTextView](classBTextView.md) object had to do some operations on the text to be able to return it as a C string. If you need to call [Text()](classBTextView.md#aa4abaa45b5c4f1ac15fd7d613d71317b) repeatedly, you'd better use [GetText()](classBTextView.md#a849d5c8a43d17ab4dee07d1758e5a839) instead.



**Returns:** A pointer to the text as a byte array.



**Since:** BeOS R3

---

### `TextHeight()`

```cpp
float BTextView::TextHeight(int32 startLine, int32 endLine)const
```

Returns the height of the text enclosed within the given lines. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `startLine` | The index of the starting line. |
| `endLine` | The index of the ending line. |





**Returns:** The height height of the text enclosed within the given lines as a float.



**Since:** BeOS R3

---

### `TextLength()`

```cpp
int32 BTextView::TextLength()const
```

Returns the text length of the [BTextView](classBTextView.md) text. 



**Returns:** The text length of the [BTextView](classBTextView.md) text.



**Since:** BeOS R3

---

### `TextRect()`

```cpp
BRect BTextView::TextRect()const
```

Returns the [BTextView](classBTextView.md)'s text frame. 



**Returns:** The [BTextView](classBTextView.md)'s text frame.



**See also:** [SetTextRect()](classBTextView.md#a5dfe405b8963dec0acf22d571566f335)



**Since:** BeOS R3

---

### `WindowActivated()`

```cpp
void BTextView::WindowActivated(bool active)
```

Hook method that is called when the window becomes the active window or gives up that status. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `active` | `true` when the window becomes activated, `false` when the window becomes deactivated. |





**Since:** BeOS R3


Reimplemented from [BView](classBView.md#a5b7aeff0b2608ec63e2c01153a7717f6).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBTextView.html).
