# Application Server

## Class Descriptions

Application Management

* [AppServer class](AppServer.md)

    * [Member Functions](AppServer.md#member-functions)

    * [Global Functions](AppServer.md#global-functions)

    * [AppServer(void)](AppServer.md#appserver-void)

    * [~AppServer(void)](AppServer.md#id1)

    * [void MainLoop(void)](AppServer.md#void-mainloop-void)

    * [void DispatchMessage(int32 code, int8 *buffer)](AppServer.md#void-dispatchmessage-int32-code-int8-buffer)

        * [CREATE_APP](AppServer.md#create-app)

        * [DELETE_APP](AppServer.md#delete-app)

        * [GET_SCREEN_MODE](AppServer.md#get-screen-mode)

        * [B_QUIT_REQUESTED](AppServer.md#b-quit-requested)

        * [SET_DECORATOR](AppServer.md#set-decorator)

    * [void Run(void)](AppServer.md#void-run-void)

    * [bool LoadDecorator(const char *path)](AppServer.md#bool-loaddecorator-const-char-path)

    * [static int32 Picasso(void *data)](AppServer.md#static-int32-picasso-void-data)

    * [static int32 Poller(void *data)](AppServer.md#static-int32-poller-void-data)

    * [Decorator * instantiate_decorator(Layer *owner, uint32 wflags, uint32 wlook)](AppServer.md#decorator-instantiate-decorator-layer-owner-uint32-wflags-uint32-wlook)

    * [void Broadcast(int32 code)](AppServer.md#void-broadcast-int32-code)

    * [void HandleKeyMessage(int32 code, int8 *buffer)](AppServer.md#void-handlekeymessage-int32-code-int8-buffer)

        * [B_KEY_DOWN](AppServer.md#b-key-down)

        * [B_KEY_UP](AppServer.md#b-key-up)

        * [B_UNMAPPED_KEY_DOWN](AppServer.md#b-unmapped-key-down)

        * [B_UNMAPPED_KEY_UP](AppServer.md#b-unmapped-key-up)

        * [B_MODIFIERS_CHANGED](AppServer.md#b-modifiers-changed)

* [ServerApp class](ServerApp.md)

    * [Member Functions](ServerApp.md#member-functions)

        * [ServerApp(port_id sendport, port_id rcvport, const char *sig, thread_id thread_bapp)](ServerApp.md#serverapp-port-id-sendport-port-id-rcvport-const-char-sig-thread-id-thread-bapp)

        * [~ServerApp(void)](ServerApp.md#serverapp-void)

        * [bool Run(void)](ServerApp.md#bool-run-void)

        * [static int32 MonitorApp(void *data)](ServerApp.md#static-int32-monitorapp-void-data)

        * [bool IsActive(void)](ServerApp.md#bool-isactive-void)

        * [void PingTarget(void)](ServerApp.md#void-pingtarget-void)

        * [void DispatchMessage(int32 code, int8 *buffer)](ServerApp.md#void-dispatchmessage-int32-code-int8-buffer)

            * [CREATE_WINDOW](ServerApp.md#create-window)

            * [DELETE_APP](ServerApp.md#delete-app)

            * [SET_CURSOR_DATA](ServerApp.md#set-cursor-data)

            * [SET_CURSOR_BCURSOR](ServerApp.md#set-cursor-bcursor)

            * [B_QUIT_REQUESTED](ServerApp.md#b-quit-requested)

            * [UPDATE_DECORATOR](ServerApp.md#update-decorator)

        * [void WindowBroadcast(int32 code)](ServerApp.md#void-windowbroadcast-int32-code)

        * [void Lock(void), void Unlock(void), bool IsLocked(void)](ServerApp.md#void-lock-void-void-unlock-void-bool-islocked-void)

* [SharedObject class](SharedObject.md)

    * [Member Functions](SharedObject.md#member-functions)

* [TokenHandler class](TokenHandler.md)

    * [Member Functions](TokenHandler.md#member-functions)

        * [TokenHandler(void)](TokenHandler.md#tokenhandler-void)

        * [~TokenHandler(void)](TokenHandler.md#id1)

        * [int32 GetToken(void)](TokenHandler.md#int32-gettoken-void)

        * [void Reset(void)](TokenHandler.md#void-reset-void)

        * [void ExcludeValue(int32 value)](TokenHandler.md#void-excludevalue-int32-value)

        * [void ResetExcludes(void)](TokenHandler.md#void-resetexcludes-void)

        * [bool IsExclude(int32 value)](TokenHandler.md#bool-isexclude-int32-value)

* [Debug Utility functions](DebugTools.md)

Graphics Management

* [BitmapManager class](BitmapManager.md)

    * [Member Functions](BitmapManager.md#member-functions)

        * [BitmapManager(void)](BitmapManager.md#bitmapmanager-void)

        * [~BitmapManager(void)](BitmapManager.md#id1)

        * [ServerBitmap *CreateBitmap(BRect bounds, color_space space, int32 flags, int32 bytes_per_row=-1, screen_id screen=B_MAIN_SCREEN_ID)](BitmapManager.md#serverbitmap-createbitmap-brect-bounds-color-space-space-int32-flags-int32-bytes-per-row-1-screen-id-screen-b-main-screen-id)

        * [void DeleteBitmap(ServerBitmap *bitmap)](BitmapManager.md#void-deletebitmap-serverbitmap-bitmap)

* [ColorUtils](ColorUtils.md)

    * [Global Functions](ColorUtils.md#global-functions)

        * [void SetRGBColor32(rgb_color *col, uint8 r, uint8 g, uint8 b, uint8 a=255)](ColorUtils.md#void-setrgbcolor32-rgb-color-col-uint8-r-uint8-g-uint8-b-uint8-a-255)

        * [void SetRGBAColor32(rgb_color *col, uint16 color16)](ColorUtils.md#void-setrgbacolor32-rgb-color-col-uint16-color16)

        * [void SetRGBColor16(uint16 *col, uint8 r, uint8 g, uint8 b)](ColorUtils.md#void-setrgbcolor16-uint16-col-uint8-r-uint8-g-uint8-b)

        * [void SetRGBAColor15(uint16 *col, uint8 r, uint8 g, uint8 b, bool opaque=true)](ColorUtils.md#void-setrgbacolor15-uint16-col-uint8-r-uint8-g-uint8-b-bool-opaque-true)

        * [uint8 FindClosestColor(rgb_color *palette,rgb_color col)](ColorUtils.md#uint8-findclosestcolor-rgb-color-palette-rgb-color-col)

        * [uint16 FindClosestColor16(rgb_color col)](ColorUtils.md#uint16-findclosestcolor16-rgb-color-col)

        * [uint16 FindClosestColor15(rgb_color col)](ColorUtils.md#uint16-findclosestcolor15-rgb-color-col)

        * [rgb_color MakeBlendColor(rgb_color col, rgb_color col2, float position)](ColorUtils.md#rgb-color-makeblendcolor-rgb-color-col-rgb-color-col2-float-position)

* [CursorManager class](CursorManager.md)

    * [Enumerated Types](CursorManager.md#enumerated-types)

        * [cursor_which](CursorManager.md#cursor-which)

    * [Member Functions](CursorManager.md#member-functions)

        * [CursorManager(void)](CursorManager.md#cursormanager-void)

        * [~CursorManager(void)](CursorManager.md#id1)

        * [int32 AddCursor(ServerCursor *sc)](CursorManager.md#int32-addcursor-servercursor-sc)

        * [void DeleteCursor(int32 ctoken)](CursorManager.md#void-deletecursor-int32-ctoken)

        * [void RemoveAppCursors(ServerApp *app)](CursorManager.md#void-removeappcursors-serverapp-app)

        * [void ShowCursor(void), void HideCursor(void), void ObscureCursor(void)](CursorManager.md#void-showcursor-void-void-hidecursor-void-void-obscurecursor-void)

        * [void SetCursor(int32 token), void SetCursor(cursor_which cursor)](CursorManager.md#void-setcursor-int32-token-void-setcursor-cursor-which-cursor)

        * [ServerCursor *GetCursor(cursor_which which)](CursorManager.md#servercursor-getcursor-cursor-which-which)

        * [void ChangeCursor(cursor_which which, int32 token)](CursorManager.md#void-changecursor-cursor-which-which-int32-token)

        * [cursor_which GetCursorWhich(void)](CursorManager.md#cursor-which-getcursorwhich-void)

* [Decorator class](Decorator.md)

    * [Member Functions](Decorator.md#member-functions)

        * [Decorator(BRect int32 wlook, int32 wfeel, int32 wflags)](Decorator.md#decorator-brect-int32-wlook-int32-wfeel-int32-wflags)

        * [~Decorator(void)](Decorator.md#decorator-void)

        * [void SetColors(color_set colors)](Decorator.md#void-setcolors-color-set-colors)

        * [void SetDriver(DisplayDriver *driver)](Decorator.md#void-setdriver-displaydriver-driver)

        * [void SetClose(bool is_down)](Decorator.md#void-setclose-bool-is-down)

        * [void SetMinimize(bool is_down)](Decorator.md#void-setminimize-bool-is-down)

        * [void SetZoom(bool is_down)](Decorator.md#void-setzoom-bool-is-down)

        * [void SetFlags(int32 wflags)](Decorator.md#void-setflags-int32-wflags)

        * [void SetFeel(int32 wfeel)](Decorator.md#void-setfeel-int32-wfeel)

        * [void SetLook(int32 wlook)](Decorator.md#void-setlook-int32-wlook)

        * [bool GetClose(void)](Decorator.md#bool-getclose-void)

        * [bool GetMinimize(void)](Decorator.md#bool-getminimize-void)

        * [bool GetZoom(void)](Decorator.md#bool-getzoom-void)

        * [int32 GetLook(void)](Decorator.md#int32-getlook-void)

        * [int32 GetFeel(void)](Decorator.md#int32-getfeel-void)

        * [int32 GetFlags(void)](Decorator.md#int32-getflags-void)

        * [void SetTitle(const char *string)](Decorator.md#void-settitle-const-char-string)

        * [void SetFont(SFont *sf)](Decorator.md#void-setfont-sfont-sf)

        * [int32 _ClipTitle(float width)](Decorator.md#int32-cliptitle-float-width)

        * [void SetFocus(bool is_active)](Decorator.md#void-setfocus-bool-is-active)

        * [bool GetFocus(void)](Decorator.md#bool-getfocus-void)

        * [int32 _TitleWidth(void)](Decorator.md#int32-titlewidth-void)

    * [Virtual Functions](Decorator.md#virtual-functions)

        * [void MoveBy(float x, float y)](Decorator.md#void-moveby-float-x-float-y)

        * [void MoveBy(BPoint pt)](Decorator.md#void-moveby-bpoint-pt)

        * [void ResizeBy(float x, float y)](Decorator.md#void-resizeby-float-x-float-y)

        * [void ResizeBy(BPoint pt)](Decorator.md#void-resizeby-bpoint-pt)

        * [void Draw(BRect r)](Decorator.md#void-draw-brect-r)

        * [void Draw(void)](Decorator.md#void-draw-void)

        * [void DrawClose(void)](Decorator.md#void-drawclose-void)

        * [protected: void _DrawClose(BRect r)](Decorator.md#protected-void-drawclose-brect-r)

        * [void DrawMinimize(void)](Decorator.md#void-drawminimize-void)

        * [protected: void _DrawMinimize(BRect r)](Decorator.md#protected-void-drawminimize-brect-r)

        * [void DrawZoom(void)](Decorator.md#void-drawzoom-void)

        * [protected: void _DrawZoom(BRect r)](Decorator.md#protected-void-drawzoom-brect-r)

        * [void DrawFrame(void)](Decorator.md#void-drawframe-void)

        * [protected: void _DrawFrame(BRect r)](Decorator.md#protected-void-drawframe-brect-r)

        * [void DrawTab(void)](Decorator.md#void-drawtab-void)

        * [protected: void _DrawTab(BRect r)](Decorator.md#protected-void-drawtab-brect-r)

        * [void DrawTitle(void)](Decorator.md#void-drawtitle-void)

        * [protected: void _DrawTitle(BRect r)](Decorator.md#protected-void-drawtitle-brect-r)

        * [void _SetFocus(void)](Decorator.md#void-setfocus-void)

        * [SRegion GetFootprint(void)](Decorator.md#sregion-getfootprint-void)

        * [click_type Clicked(BPoint pt, int32 buttons, int32 modifiers)](Decorator.md#click-type-clicked-bpoint-pt-int32-buttons-int32-modifiers)

        * [BRect SlideTab(float dx, dy=0)](Decorator.md#brect-slidetab-float-dx-dy-0)

    * [Exported C Functions](Decorator.md#exported-c-functions)

        * [extern “C” Decorator *create_decorator(BRect frame, int32 wlook, int32 wfeel, int32 wflags)](Decorator.md#extern-c-decorator-create-decorator-brect-frame-int32-wlook-int32-wfeel-int32-wflags)

        * [extern “C” float get_decorator_version(void)](Decorator.md#extern-c-float-get-decorator-version-void)

    * [Enumerated Types](Decorator.md#enumerated-types)

        * [click_type](Decorator.md#click-type)

* [Desktop module](Desktop.md)

    * [Global Functions](Desktop.md#global-functions)

        * [void InitDesktop(void)](Desktop.md#void-initdesktop-void)

        * [void ShutdownDesktop(void)](Desktop.md#void-shutdowndesktop-void)

        * [void AddWorkspace(int32 index=-1)](Desktop.md#void-addworkspace-int32-index-1)

        * [void DeleteWorkspace(int32 index)](Desktop.md#void-deleteworkspace-int32-index)

        * [int32 CountWorkspaces(void)](Desktop.md#int32-countworkspaces-void)

        * [void SetWorkspaceCount(int32 count)](Desktop.md#void-setworkspacecount-int32-count)

        * [int32 CurrentWorkspace(screen_id screen=B_MAIN_SCREEN_ID)](Desktop.md#int32-currentworkspace-screen-id-screen-b-main-screen-id)

        * [void SetWorkspace(int32 workspace, screen_id screen=B_MAIN_SCREEN_ID)](Desktop.md#void-setworkspace-int32-workspace-screen-id-screen-b-main-screen-id)

        * [void SetScreen(screen_id id)](Desktop.md#void-setscreen-screen-id-id)

        * [int32 CountScreens(void)](Desktop.md#int32-countscreens-void)

        * [screen_id ActiveScreen(void)](Desktop.md#screen-id-activescreen-void)

        * [DisplayDriver *GetGfxDriver(screen_id screen=B_MAIN_SCREEN_ID)](Desktop.md#displaydriver-getgfxdriver-screen-id-screen-b-main-screen-id)

        * [status_t SetSpace(int32 index, int32 res, bool stick=true, screen_id screen=B_MAIN_SCREEN_ID)](Desktop.md#status-t-setspace-int32-index-int32-res-bool-stick-true-screen-id-screen-b-main-screen-id)

        * [void AddWindowToDesktop(ServerWindow *win, int32 workspace=B_CURRENT_WORKSPACE, screen_id screen=B_MAIN_SCREEN_ID)](Desktop.md#void-addwindowtodesktop-serverwindow-win-int32-workspace-b-current-workspace-screen-id-screen-b-main-screen-id)

        * [void RemoveWindowFromDesktop(ServerWindow *win)](Desktop.md#void-removewindowfromdesktop-serverwindow-win)

        * [ServerWindow *GetActiveWindow(void)](Desktop.md#serverwindow-getactivewindow-void)

        * [void SetActiveWindow(ServerWindow *win)](Desktop.md#void-setactivewindow-serverwindow-win)

        * [Layer *GetRootLayer(int32 workspace=B_CURRENT_WORKSPACE, screen_id screen=B_MAIN_SCREEN_ID)](Desktop.md#layer-getrootlayer-int32-workspace-b-current-workspace-screen-id-screen-b-main-screen-id)

        * [void set_drag_message(int32 size, int8 *flattened)](Desktop.md#void-set-drag-message-int32-size-int8-flattened)

        * [int8* get_drag_message(int32 *size)](Desktop.md#int8-get-drag-message-int32-size)

        * [void empty_drag_ message(void)](Desktop.md#void-empty-drag-message-void)

    * [Namespaces](Desktop.md#namespaces)

        * [desktop_private](Desktop.md#desktop-private)

* [Screen class](DesktopClasses.md)

    * [Member Functions](DesktopClasses.md#member-functions)

        * [Screen(DisplayDriver *gfxmodule, uint8 workspaces)](DesktopClasses.md#screen-displaydriver-gfxmodule-uint8-workspaces)

        * [~Screen(void)](DesktopClasses.md#screen-void)

        * [void AddWorkspace(int32 index=-1)](DesktopClasses.md#void-addworkspace-int32-index-1)

        * [void DeleteWorkspace(int32 index)](DesktopClasses.md#void-deleteworkspace-int32-index)

        * [int32 CountWorkspaces(void)](DesktopClasses.md#int32-countworkspaces-void)

        * [void SetWorkspaceCount(int32 count)](DesktopClasses.md#void-setworkspacecount-int32-count)

        * [int32 CurrentWorkspace(void)](DesktopClasses.md#int32-currentworkspace-void)

        * [void SetWorkspace(int32 workspace)](DesktopClasses.md#void-setworkspace-int32-workspace)

        * [void Activate(bool active=true)](DesktopClasses.md#void-activate-bool-active-true)

        * [DisplayDriver *GetDriver(void)](DesktopClasses.md#displaydriver-getdriver-void)

        * [status_t SetSpace(int32 index, int32 res, bool stick=true)](DesktopClasses.md#status-t-setspace-int32-index-int32-res-bool-stick-true)

        * [void AddWindow(ServerWindow *win, int32 workspace=B_CURRENT_WORKSPACE)](DesktopClasses.md#void-addwindow-serverwindow-win-int32-workspace-b-current-workspace)

        * [void RemoveWindow(ServerWindow *win)](DesktopClasses.md#void-removewindow-serverwindow-win)

        * [ServerWindow *ActiveWindow(void)](DesktopClasses.md#serverwindow-activewindow-void)

        * [void SetActiveWindow(ServerWindow *win)](DesktopClasses.md#void-setactivewindow-serverwindow-win)

        * [Layer *GetRootLayer(int32 workspace=B_CURRENT_WORKSPACE)](DesktopClasses.md#layer-getrootlayer-int32-workspace-b-current-workspace)

        * [bool IsInitialized(void)](DesktopClasses.md#bool-isinitialized-void)

        * [Workspace *GetActiveWorkspace(void)](DesktopClasses.md#workspace-getactiveworkspace-void)

    * [Workspace class members](DesktopClasses.md#workspace-class-members)

        * [Workspace(void)](DesktopClasses.md#workspace-void)

        * [~Workspace(void)](DesktopClasses.md#id1)

        * [void SetBGColor(const RGBColor &c)](DesktopClasses.md#void-setbgcolor-const-rgbcolor-c)

        * [RGBColor BGColor(void)](DesktopClasses.md#rgbcolor-bgcolor-void)

        * [RootLayer *GetRoot(void)](DesktopClasses.md#rootlayer-getroot-void)

        * [void SetData(graphics_card_info *gcinfo, frame_buffer_info *fbinfo)](DesktopClasses.md#void-setdata-graphics-card-info-gcinfo-frame-buffer-info-fbinfo)

        * [void GetData(graphics_card_info *gcinfo, frame_buffer_info *fbinfo)](DesktopClasses.md#void-getdata-graphics-card-info-gcinfo-frame-buffer-info-fbinfo)

    * [RootLayer class members](DesktopClasses.md#rootlayer-class-members)

        * [~RootLayer(void)](DesktopClasses.md#rootlayer-void)

        * [void RequestDraw(const BRect &r)](DesktopClasses.md#void-requestdraw-const-brect-r)

        * [void MoveBy(BPoint pt), void MoveBy(float x, float y)](DesktopClasses.md#void-moveby-bpoint-pt-void-moveby-float-x-float-y)

        * [void SetDriver(DisplayDriver *d)](DesktopClasses.md#void-setdriver-displaydriver-d)

        * [void RebuildRegions(bool recursive=false)](DesktopClasses.md#void-rebuildregions-bool-recursive-false)

* [DisplayDriver class](DisplayDriver.md)

    * [Member Functions](DisplayDriver.md#member-functions)

        * [DisplayDriver(void)](DisplayDriver.md#displaydriver-void)

        * [~DisplayDriver(void)](DisplayDriver.md#id1)

        * [bool Initialize(void)](DisplayDriver.md#bool-initialize-void)

        * [void Shutdown(void)](DisplayDriver.md#void-shutdown-void)

        * [void CopyBits(BRect src, BRect dest)](DisplayDriver.md#void-copybits-brect-src-brect-dest)

        * [void InvertRect(BRect r)](DisplayDriver.md#void-invertrect-brect-r)

        * [void DrawBitmap(ServerBitmap *bmp, BRect src, BRect dest, render_mode mode)](DisplayDriver.md#void-drawbitmap-serverbitmap-bmp-brect-src-brect-dest-render-mode-mode)

        * [void DrawPicture(SPicture *pic, BPoint pt)](DisplayDriver.md#void-drawpicture-spicture-pic-bpoint-pt)

        * [void DrawChar(char c, BPoint pt)](DisplayDriver.md#void-drawchar-char-c-bpoint-pt)

        * [void DrawString(const char *string, int32 length, BPoint pt, escapement_delta *delta=NULL)](DisplayDriver.md#void-drawstring-const-char-string-int32-length-bpoint-pt-escapement-delta-delta-null)

        * [void StrokeArc(BRect r, float angle, float span, layerdata *d, int8 *pattern)](DisplayDriver.md#void-strokearc-brect-r-float-angle-float-span-layerdata-d-int8-pattern)

        * [void FillArc(BRect r, float angle, float span, layerdata *d, int8 *pattern)](DisplayDriver.md#void-fillarc-brect-r-float-angle-float-span-layerdata-d-int8-pattern)

        * [void StrokeBezier(BPoint *pts, layerdata *d, int8 *pat)](DisplayDriver.md#void-strokebezier-bpoint-pts-layerdata-d-int8-pat)

        * [void FillBezier(BPoint *pts, layerdata *d, int8 *pat)](DisplayDriver.md#void-fillbezier-bpoint-pts-layerdata-d-int8-pat)

        * [void StrokeEllipse(BRect r, layerdata *d, int8 *pattern)](DisplayDriver.md#void-strokeellipse-brect-r-layerdata-d-int8-pattern)

        * [void FillEllipse(BRect r, layerdata *d, int8 *pattern)](DisplayDriver.md#void-fillellipse-brect-r-layerdata-d-int8-pattern)

        * [void StrokeLine(BPoint start, BPoint end, layerdata *d, int8 *pattern)](DisplayDriver.md#void-strokeline-bpoint-start-bpoint-end-layerdata-d-int8-pattern)

        * [void StrokeLineArray(BPoint *pts, int32 numlines, rgb_color *colors, layerdata *d)](DisplayDriver.md#void-strokelinearray-bpoint-pts-int32-numlines-rgb-color-colors-layerdata-d)

        * [void StrokePolygon(BPoint *ptlist, int32 numpts, BRect rect, layerdata *d, int8 *pattern, bool is_closed=true)](DisplayDriver.md#void-strokepolygon-bpoint-ptlist-int32-numpts-brect-rect-layerdata-d-int8-pattern-bool-is-closed-true)

        * [void FillPolygon(BPoint *ptlist, int32 numpts, BRect rect, layerdata *d, int8 *pattern)](DisplayDriver.md#void-fillpolygon-bpoint-ptlist-int32-numpts-brect-rect-layerdata-d-int8-pattern)

        * [void StrokeRect(BRect r, layerdata *d, int8 *pattern)](DisplayDriver.md#void-strokerect-brect-r-layerdata-d-int8-pattern)

        * [void FillRect(BRect r, layerdata *d, int8 *pattern)](DisplayDriver.md#void-fillrect-brect-r-layerdata-d-int8-pattern)

        * [void StrokeRoundRect(BRect r, float xrad, float yrad, layerdata *d, int8 *pattern)](DisplayDriver.md#void-strokeroundrect-brect-r-float-xrad-float-yrad-layerdata-d-int8-pattern)

        * [void FillRoundRect(BRect r, float xrad, float yrad, layerdata *d, int8 *pattern)](DisplayDriver.md#void-fillroundrect-brect-r-float-xrad-float-yrad-layerdata-d-int8-pattern)

        * [void StrokeShape(SShape *sh, layerdata *d, int8 *pattern)](DisplayDriver.md#void-strokeshape-sshape-sh-layerdata-d-int8-pattern)

        * [void FillShape(SShape *sh, layerdata *d, int8 *pattern)](DisplayDriver.md#void-fillshape-sshape-sh-layerdata-d-int8-pattern)

        * [void StrokeTriangle(BPoints *pts, BRect r, layerdata *d, int8 *pattern)](DisplayDriver.md#void-stroketriangle-bpoints-pts-brect-r-layerdata-d-int8-pattern)

        * [void FillTriangle(BPoints *pts, BRect r, layerdata *d, int8 *pattern)](DisplayDriver.md#void-filltriangle-bpoints-pts-brect-r-layerdata-d-int8-pattern)

        * [void ShowCursor(void)](DisplayDriver.md#void-showcursor-void)

        * [void HideCursor(void)](DisplayDriver.md#void-hidecursor-void)

        * [void ObscureCursor(void)](DisplayDriver.md#void-obscurecursor-void)

        * [bool IsCursorHidden(void)](DisplayDriver.md#bool-iscursorhidden-void)

        * [void SetCursor(ServerCursor *csr)](DisplayDriver.md#void-setcursor-servercursor-csr)

        * [float StringWidth(const char *string, int32 length, LayerData *d)](DisplayDriver.md#float-stringwidth-const-char-string-int32-length-layerdata-d)

        * [float StringHeight(const char *string, int32 length, LayerData *d)](DisplayDriver.md#float-stringheight-const-char-string-int32-length-layerdata-d)

    * [Protected Functions](DisplayDriver.md#protected-functions)

        * [uint8 GetDepth(void)](DisplayDriver.md#uint8-getdepth-void)

        * [uint16 GetHeight(void)](DisplayDriver.md#uint16-getheight-void)

        * [uint16 GetWidth(void)](DisplayDriver.md#uint16-getwidth-void)

        * [screen_mode GetMode(void)](DisplayDriver.md#screen-mode-getmode-void)

        * [void SetMode(screen_mode mode)](DisplayDriver.md#void-setmode-screen-mode-mode)

        * [bool DumpToFile(const char *path)](DisplayDriver.md#bool-dumptofile-const-char-path)

        * [void Lock(void)](DisplayDriver.md#void-lock-void)

        * [void Unlock(void)](DisplayDriver.md#void-unlock-void)

        * [void SetDepthInternal(uint8 d)](DisplayDriver.md#void-setdepthinternal-uint8-d)

        * [void SetHeightInternal(uint16 h)](DisplayDriver.md#void-setheightinternal-uint16-h)

        * [void SetWidthInternal(uint16 w)](DisplayDriver.md#void-setwidthinternal-uint16-w)

        * [void SetModeInternal(int32 m)](DisplayDriver.md#void-setmodeinternal-int32-m)

        * [void SetCursorHidden(bool state)](DisplayDriver.md#void-setcursorhidden-bool-state)

        * [void SetCursorObscured(bool state)](DisplayDriver.md#void-setcursorobscured-bool-state)

        * [bool IsCursorObscured(void)](DisplayDriver.md#bool-iscursorobscured-void)

* [Layer class](Layer.md)

    * [Member Functions](Layer.md#member-functions)

        * [Layer(BRect frame, const char *name, int32 resize, int32 flags, ServerWindow *win)](Layer.md#layer-brect-frame-const-char-name-int32-resize-int32-flags-serverwindow-win)

        * [~Layer(void)](Layer.md#layer-void)

        * [void AddChild(Layer *child, Layer *before=NULL, bool rebuild=true)](Layer.md#void-addchild-layer-child-layer-before-null-bool-rebuild-true)

        * [RemoveChild(Layer *child, bool rebuild=true)](Layer.md#removechild-layer-child-bool-rebuild-true)

        * [void RemoveSelf(bool rebuild=true)](Layer.md#void-removeself-bool-rebuild-true)

        * [void Invalidate(BRect r)](Layer.md#void-invalidate-brect-r)

        * [void Invalidate(BRegion *region)](Layer.md#void-invalidate-bregion-region)

        * [BRect Frame(void), BRect Bounds(void)](Layer.md#brect-frame-void-brect-bounds-void)

        * [void MoveBy(BPoint pt), void MoveBy(float x, float y)](Layer.md#void-moveby-bpoint-pt-void-moveby-float-x-float-y)

        * [void ResizeBy(BPoint pt), void ResizeBy(float x, float y)](Layer.md#void-resizeby-bpoint-pt-void-resizeby-float-x-float-y)

        * [int32 CountChildren(void)](Layer.md#int32-countchildren-void)

        * [bool IsDirty(void)](Layer.md#bool-isdirty-void)

        * [BRect ConvertToTop(const BRect &r), BRegion ConvertToTop(const BRegion &r)](Layer.md#brect-converttotop-const-brect-r-bregion-converttotop-const-bregion-r)

        * [BRect ConvertFromTop(const BRect &r), BRegion ConvertFromTop(const BRegion &r)](Layer.md#brect-convertfromtop-const-brect-r-bregion-convertfromtop-const-bregion-r)

        * [BRect ConvertFromParent(const BRect &r), BRegion ConvertFromParent(const BRegion &r)](Layer.md#brect-convertfromparent-const-brect-r-bregion-convertfromparent-const-bregion-r)

        * [void RebuildRegions(bool recursive=false)](Layer.md#void-rebuildregions-bool-recursive-false)

        * [void MakeTopChild(void)](Layer.md#void-maketopchild-void)

        * [void MakeBottomChild(void)](Layer.md#void-makebottomchild-void)

        * [void RequestDraw(const BRect &r)](Layer.md#void-requestdraw-const-brect-r)

        * [Layer *FindLayer(int32 token)](Layer.md#layer-findlayer-int32-token)

        * [Layer *GetChildAt(BPoint pt, bool recursive=false)](Layer.md#layer-getchildat-bpoint-pt-bool-recursive-false)

        * [PortLink *GetLink(void)](Layer.md#portlink-getlink-void)

* [PatternHandler class](PatternHandler.md)

    * [Enumerated Types](PatternHandler.md#enumerated-types)

        * [pattern_enum](PatternHandler.md#pattern-enum)

    * [Member Functions](PatternHandler.md#member-functions)

        * [PatternHandler()](PatternHandler.md#patternhandler)

        * [~PatternHandler()](PatternHandler.md#id1)

        * [void SetTarget(int8 *pattern)](PatternHandler.md#void-settarget-int8-pattern)

        * [void SetColors(RGBColor c1, RGBColor c2)](PatternHandler.md#void-setcolors-rgbcolor-c1-rgbcolor-c2)

        * [RGBColor GetColor(BPoint pt) RGBColor GetColor (float x, float y)](PatternHandler.md#rgbcolor-getcolor-bpoint-pt-rgbcolor-getcolor-float-x-float-y)

        * [bool GetValue(BPoint pt) bool GetValue (float x, float y)](PatternHandler.md#bool-getvalue-bpoint-pt-bool-getvalue-float-x-float-y)

* [RGBColor class](RGBColor.md)

    * [Member Functions](RGBColor.md#member-functions)

        * [RGBColor(uint8 r, uint8 g, uint8 b, uint8 a=255)](RGBColor.md#rgbcolor-uint8-r-uint8-g-uint8-b-uint8-a-255)

        * [RGBColor(rgb_color col)](RGBColor.md#rgbcolor-rgb-color-col)

        * [RGBColor(uint16 color16)](RGBColor.md#rgbcolor-uint16-color16)

        * [RGBColor(uint8 color8)](RGBColor.md#rgbcolor-uint8-color8)

        * [RGBColor(const RGBColor &color)](RGBColor.md#rgbcolor-const-rgbcolor-color)

        * [RGBColor(void)](RGBColor.md#rgbcolor-void)

        * [void PrintToStream(void)](RGBColor.md#void-printtostream-void)

        * [uint8 GetColor8(void)](RGBColor.md#uint8-getcolor8-void)

        * [uint16 GetColor16(void)](RGBColor.md#uint16-getcolor16-void)

        * [rgb_color GetColor32(void)](RGBColor.md#rgb-color-getcolor32-void)

        * [void SetColor(const RGBColor &color)](RGBColor.md#void-setcolor-const-rgbcolor-color)

        * [void SetColor(uint8 r, uint8 g, uint8 b, uint8 a=255)](RGBColor.md#void-setcolor-uint8-r-uint8-g-uint8-b-uint8-a-255)

        * [void SetColor(rgb_color col)](RGBColor.md#void-setcolor-rgb-color-col)

        * [void SetColor(uint16 color16)](RGBColor.md#void-setcolor-uint16-color16)

        * [void SetColor(uint8 color8)](RGBColor.md#void-setcolor-uint8-color8)

        * [RGBColor & operator=(const RGBColor &from)](RGBColor.md#rgbcolor-operator-const-rgbcolor-from)

        * [bool operator==(const RGBColor &from)](RGBColor.md#bool-operator-const-rgbcolor-from)

        * [bool operator!=(const RGBColor &from)](RGBColor.md#id1)

        * [RGBColor MakeBlendColor(RGBColor c, float position)](RGBColor.md#rgbcolor-makeblendcolor-rgbcolor-c-float-position)

* [ServerBitmap class](ServerBitmap.md)

    * [Member Functions](ServerBitmap.md#member-functions)

        * [ServerBitmap(BRect r, color_space cspace, int32 flags, int32 bytesperrow=-1, screen_id screen=B_MAIN_SCREEN_ID)](ServerBitmap.md#serverbitmap-brect-r-color-space-cspace-int32-flags-int32-bytesperrow-1-screen-id-screen-b-main-screen-id)

        * [~ServerBitmap(void)](ServerBitmap.md#serverbitmap-void)

        * [uint8 *Bits(void)](ServerBitmap.md#uint8-bits-void)

        * [area_id Area(void)](ServerBitmap.md#area-id-area-void)

        * [uint32 BitsLength(void)](ServerBitmap.md#uint32-bitslength-void)

        * [BRect Bounds(void)](ServerBitmap.md#brect-bounds-void)

        * [int32 BytesPerRow(void)](ServerBitmap.md#int32-bytesperrow-void)

        * [void _HandleSpace(color_space cs, int32 bytesperline=-1)](ServerBitmap.md#void-handlespace-color-space-cs-int32-bytesperline-1)

* [SystemPalette class](SystemPalette.md)

    * [Member Functions](SystemPalette.md#member-functions)

        * [SystemPalette(void)](SystemPalette.md#systempalette-void)

        * [~SystemPalette(void)](SystemPalette.md#id1)

        * [void SetPalette(uint8 index, RGBColor col), void SetPalette(uint8 index, rgb_color col)](SystemPalette.md#void-setpalette-uint8-index-rgbcolor-col-void-setpalette-uint8-index-rgb-color-col)

        * [RGBColor GetPalette(uint8 index)](SystemPalette.md#rgbcolor-getpalette-uint8-index)

        * [void SetGUIColor(color_which which, RGBColor col)](SystemPalette.md#void-setguicolor-color-which-which-rgbcolor-col)

        * [RGBColor GetGUIColor(color_which which)](SystemPalette.md#rgbcolor-getguicolor-color-which-which)

        * [color_set GetGUIColors(void)](SystemPalette.md#color-set-getguicolors-void)

        * [void SetGUIColors(color_set cset)](SystemPalette.md#void-setguicolors-color-set-cset)

        * [protected: void _GenerateSystemPalette(rgb_color *palette)](SystemPalette.md#protected-void-generatesystempalette-rgb-color-palette)

            * [Grays:](SystemPalette.md#grays)

            * [Blues:](SystemPalette.md#blues)

            * [Reds:](SystemPalette.md#reds)

            * [Greens:](SystemPalette.md#greens)

        * [protected: void _SetDefaultGUIColors(void)](SystemPalette.md#protected-void-setdefaultguicolors-void)

    * [Structures](SystemPalette.md#structures)

* [WinBorder class : public Layer](WinBorder.md)

    * [Member Functions](WinBorder.md#member-functions)

        * [WinBorder(BRect r, const char *name, int32 resize, int32 flags, ServerWindow *win)](WinBorder.md#winborder-brect-r-const-char-name-int32-resize-int32-flags-serverwindow-win)

        * [~WinBorder(void)](WinBorder.md#winborder-void)

        * [void RequestDraw(void)](WinBorder.md#void-requestdraw-void)

        * [void MoveBy(BPoint pt), void MoveBy(float x, float y)](WinBorder.md#void-moveby-bpoint-pt-void-moveby-float-x-float-y)

        * [void ResizeBy(BPoint pt), void ResizeBy(float x, float y)](WinBorder.md#void-resizeby-bpoint-pt-void-resizeby-float-x-float-y)

        * [void MouseDown(int8 *buffer)](WinBorder.md#void-mousedown-int8-buffer)

        * [void MouseUp(int8 *buffer)](WinBorder.md#void-mouseup-int8-buffer)

        * [void MouseMoved(int8 *buffer)](WinBorder.md#void-mousemoved-int8-buffer)

        * [void UpdateDecorator(void)](WinBorder.md#void-updatedecorator-void)

        * [void UpdateColors(void)](WinBorder.md#void-updatecolors-void)

        * [void UpdateFont(void)](WinBorder.md#void-updatefont-void)

        * [void UpdateScreen(void)](WinBorder.md#void-updatescreen-void)

        * [void RebuildRegions(bool recursive=true)](WinBorder.md#void-rebuildregions-bool-recursive-true)

        * [void Activate(bool state)](WinBorder.md#void-activate-bool-state)

    * [Global Functions](WinBorder.md#global-functions)

        * [bool is_moving_window(void), void set_is_moving_window(bool state)](WinBorder.md#bool-is-moving-window-void-void-set-is-moving-window-bool-state)

        * [bool is_resizing_window(void), void set_is_resizing_window(bool state)](WinBorder.md#bool-is-resizing-window-void-void-set-is-resizing-window-bool-state)

        * [void set_active_winborder(WinBorder *win), WinBorder * get_active_winborder(void)](WinBorder.md#void-set-active-winborder-winborder-win-winborder-get-active-winborder-void)

    * [Namespaces](WinBorder.md#namespaces)

Font Infrastructure

* [FontServer class](FontServer.md)

    * [Member Functions](FontServer.md#member-functions)

        * [FontServer(void)](FontServer.md#fontserver-void)

        * [~FontServer(void)](FontServer.md#id1)

        * [void Lock(void), void Unlock(void)](FontServer.md#void-lock-void-void-unlock-void)

        * [void SaveList(void)](FontServer.md#void-savelist-void)

        * [status_t ScanDirectory(const char *path)](FontServer.md#status-t-scandirectory-const-char-path)

        * [FontStyle *GetFont(font_family family, font_style face)](FontServer.md#fontstyle-getfont-font-family-family-font-style-face)

        * [FontInstance *GetInstance(font_family family, font_style face, int16 size, int16 rotation, int16 shear)](FontServer.md#fontinstance-getinstance-font-family-family-font-style-face-int16-size-int16-rotation-int16-shear)

        * [int32 CountFamilies(void)](FontServer.md#int32-countfamilies-void)

        * [status_t IsInitialized(void)](FontServer.md#status-t-isinitialized-void)

        * [int32 CountStyles(font_family family)](FontServer.md#int32-countstyles-font-family-family)

        * [FontStyle *GetStyle(font_family family, font_style style)](FontServer.md#fontstyle-getstyle-font-family-family-font-style-style)

        * [void RemoveFamily(const char *family)](FontServer.md#void-removefamily-const-char-family)

        * [FontFamily *_FindFamily(const char *name)](FontServer.md#fontfamily-findfamily-const-char-name)

        * [ServerFont *GetSystemPlain(void), ServerFont *GetSystemBold(void), ServerFont *GetSystemFixed(void)](FontServer.md#serverfont-getsystemplain-void-serverfont-getsystembold-void-serverfont-getsystemfixed-void)

        * [bool SetSystemPlain(const char *family, const char *style, float size)](FontServer.md#bool-setsystemplain-const-char-family-const-char-style-float-size)

        * [bool SetSystemBold(const char *family, const char *style, float size)](FontServer.md#bool-setsystembold-const-char-family-const-char-style-float-size)

        * [bool SetSystemFixed(const char *family, const char *style, float size)](FontServer.md#bool-setsystemfixed-const-char-family-const-char-style-float-size)

        * [void RemoveUnusedFamilies(void)](FontServer.md#void-removeunusedfamilies-void)

        * [bool FontsNeedUpdated(void)](FontServer.md#bool-fontsneedupdated-void)

* [FontFamily class](FontFamily.md)

    * [Member Functions](FontFamily.md#member-functions)

        * [FontFamily(const char *name)](FontFamily.md#fontfamily-const-char-name)

        * [~FontFamily(void)](FontFamily.md#fontfamily-void)

        * [const char *GetName(void)](FontFamily.md#const-char-getname-void)

        * [void AddStyle(const char *path, FT_Face face)](FontFamily.md#void-addstyle-const-char-path-ft-face-face)

        * [void RemoveStyle(const char *style)](FontFamily.md#void-removestyle-const-char-style)

        * [FontStyle *GetStyle(const char *style)](FontFamily.md#fontstyle-getstyle-const-char-style)

        * [const char *GetStyle(int32 index)](FontFamily.md#const-char-getstyle-int32-index)

        * [int32 CountStyles(void)](FontFamily.md#int32-countstyles-void)

        * [bool HasStyle(const char *stylename)](FontFamily.md#bool-hasstyle-const-char-stylename)

## Other Documents

* [App Server Interface Specification v0.3](asis.md)

    * [Purpose:](asis.md#purpose)

    * [Tasks:](asis.md#tasks)

    * [Graphics:](asis.md#graphics)

        * [Desktop Initialization](asis.md#desktop-initialization)

            * [Load Accelerant](asis.md#load-accelerant)

            * [Set up workspaces](asis.md#set-up-workspaces)

            * [Display](asis.md#display)

        * [Window management](asis.md#window-management)

            * [ServerApps](asis.md#serverapps)

            * [ServerWindows](asis.md#serverwindows)

            * [Layers](asis.md#layers)

            * [WindowBorders](asis.md#windowborders)

            * [Decorators](asis.md#decorators)

            * [How It All Works](asis.md#how-it-all-works)

        * [Screen Updates](asis.md#screen-updates)

        * [Cursor Management](asis.md#cursor-management)

        * [Display Drivers](asis.md#display-drivers)

    * [Process Management](asis.md#process-management)

        * [BApplication execution](asis.md#bapplication-execution)

        * [non-BApplication execution](asis.md#non-bapplication-execution)

        * [Killing/Exiting Applications](asis.md#killing-exiting-applications)

        * [System Shutdown](asis.md#system-shutdown)

    * [Input Processing](asis.md#input-processing)

        * [Input Server messages](asis.md#input-server-messages)

        * [Mouse](asis.md#mouse)

            * [B_MOUSE_DOWN](asis.md#b-mouse-down)

            * [B_MOUSE_UP](asis.md#b-mouse-up)

            * [B_MOUSE_MOVED](asis.md#b-mouse-moved)

            * [B_MOUSE_WHEEL_CHANGED](asis.md#b-mouse-wheel-changed)

        * [Keyboard](asis.md#keyboard)

            * [B_KEY_DOWN](asis.md#b-key-down)

            * [B_KEY_UP](asis.md#b-key-up)

            * [B_UNMAPPED_KEY_DOWN](asis.md#b-unmapped-key-down)

            * [B_UNMAPPED_KEY_UP](asis.md#b-unmapped-key-up)

            * [B_MODIFIERS_CHANGED](asis.md#b-modifiers-changed)

    * [Messaging](asis.md#messaging)

        * [Inter-Application Messaging](asis.md#inter-application-messaging)

        * [Drag-and-drop](asis.md#drag-and-drop)

        * [Methods](asis.md#methods)

* [Multiple Monitor Support Spec](MultiMonitor.htm)

Generated from the [original source documentation](https://pulkomandy.tk/drop/haiku_internals/servers/app_server/toc.html).
