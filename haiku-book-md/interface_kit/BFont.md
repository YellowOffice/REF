---
name: BFont
type: class
kit: interface_kit
brief: "Represents a typeface including its family, style and size"
source: haiku-book
---

# BFont Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Represents a typeface including its family, style and size. 


The Interface Kit provides three prebuilt [BFont](classBFont.md) objects which can be used but not modified.


* `const` BFont* `be_plain_font` A plain font used by many controls.

* `const` BFont* `be_bold_font` A bold font used by titles.

* `const` BFont* `be_fixed_font` A fixed-width font.



A [BFont](classBFont.md) object does nothing on its own but is used in combination with a view or control. Here is an example of creating a [BFont](classBFont.md) object from a system font and assigning it to a view:



```cpp
BFont font(be_plain_font);
font.SetSize(12.0);
font.SetEncoding(B_ISO_8859_1);
view->SetFont(&font);
```

You may also create a [BFont](classBFont.md) object from a view, modify it and reassign it back to the view like this:



```cpp
BFont font;
view->GetFont(&font);
font.SetFace(B_ITALIC_FACE);
font.SetSpacing(B_CHAR_SPACING);
myView->SetFont(&font);
```

You can change the way a font renders with the [SetFamilyAndStyle()](classBFont.md#aadfd617a19b12a433d51dcdd75e356c1), [SetFamilyAndFace()](classBFont.md#a1ddd1ad258ca1cb017dcbcf9f218ebb2), [SetSize()](classBFont.md#a433aa71874a3dbee8119d31b2f6307fe), [SetShear()](classBFont.md#a1dc08c49306eabc5b197bf8c59571ab3), [SetRotation()](classBFont.md#a77545e73f293e08b9c9ddc7d6a547808), [SetFalseBoldWidth()](classBFont.md#aef0c684bbe795fb491807d81cfb0827e), [SetSpacing()](classBFont.md#a60124c81326dc4ded81c7271669f111a), [SetEncoding()](classBFont.md#afdb8a74829abab2dd57591eb471e7901), [SetFace()](classBFont.md#afded119b1f1e6912d78d83fd23962adb), and [SetFlags()](classBFont.md#aaf75531591c0b34fd58319dde7e73490) methods.


More information about the space taken up by a font can be determined by querying a [BFont](classBFont.md) object using the following methods: [StringWidth()](classBFont.md#a752ca8369dbd8eb6be6dcebf168fb236), [GetStringWidths()](classBFont.md#a876823361e0c90c6c5e2a1fb3ab7c317) [GetEscapements()](classBFont.md#aca49530c494a52f06fd5ea88d66a0f31), [GetEdges()](classBFont.md#aa08a3467e1720dd4431fb7264a242c45), [GetHeight()](classBFont.md#a9748877645b9e3ab98a3a43a5375f392), [BoundingBox()](classBFont.md#ae8ad82beb4f332876a5ad93cd527cdb3) [GetBoundingBoxesAsGlyphs()](classBFont.md#afe3a10678a3dbe21fd04a1bac05a850d), [GetBoundingBoxesAsString()](classBFont.md#a6fd11aac2f55781dfe60d021e40cd7f7), and [GetBoundingBoxesForStrings()](classBFont.md#a3a0625c7fcb2af6fe24a4c961ed8a937).


You can also perform intelligent string truncation with the [TruncateString()](classBFont.md#a91c0d35cea2f5142cc7c5a01505de80f) and [GetTruncatedStrings()](classBFont.md#abbee20530f5e414a27b4437220459aec) methods.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BFont](#ad66965429ac72d5b3d0cce32fc855e3c) () — Creates a BFont object initialized to be_plain_font.
* [BFont](#a6a6820b1f9b64355195bbc859da96195) (const BFont &font) — Creates and initializes a BFont object from another BFont object.
* [BFont](#a5ad29ba7ce99d5d7a1788ab94d1b498c) (const BFont *font) — Creates and initializes a BFont object from a pointer to a BFont object.
* `unicode_block` [Blocks](#a8151aa73d7f435cd9c4115a8b92f62cc) () const — Gets a unicode_block object that identifies the Unicode blocks supported by this font face and family.
* `BRect` [BoundingBox](#ae8ad82beb4f332876a5ad93cd527cdb3) () const — Gets a BRect that encloses the font text.
* `int32` [CountTuned](#aeb2d8695b587d341116bda8bd272ae1f) () const — Gets the number of tuned fonts for the font family and style.
* `font_direction` [Direction](#a035e23156c1224ae163edef7c4cc3f42) () const — Gets the font direction, left-to-right or right-to left.
* `uint8` [Encoding](#a0a9a61b8b505f3853ff4f2e2354a8645) () const — Gets the character encoding constant.
* `uint16` [Face](#a4ebe97df6ee2e3afe23a74e12f3268f9) () const — Gets the font face flags bitmap.
* `float` [FalseBoldWidth](#a3c9abfe103d7d57f665e61442f89005b) () const — Gets the width of the font as if it were bold.
* `uint32` [FamilyAndStyle](#af1fd7295648a7202cfedff55c557353e) () const — Gets the code of the font family and style combination.
* `font_file_format` [FileFormat](#a40f571f695c6c684c52fc82a3ea22a52) () const — Gets whether the font is a TrueType™ or PostScript™ Type1 font.
* `uint32` [Flags](#a0aff01f09a6f66531bf84ff9291ce3c3) () const — Gets the antialiasing flags.
* `void` [GetBoundingBoxesAsGlyphs](#afe3a10678a3dbe21fd04a1bac05a850d) (const char charArray[], int32 numChars, font_metric_mode mode, BRect boundingBoxArray[]) const — Writes an array of BRect objects to boundingBoxArray representing the bounding rectangles of each character in charArray.
* `void` [GetBoundingBoxesAsString](#a6fd11aac2f55781dfe60d021e40cd7f7) (const char charArray[], int32 numChars, font_metric_mode mode, escapement_delta *delta, BRect boundingBoxArray[]) const — Writes an array of BRect objects to boundingBoxArray representing the bounding rectangles of each character in charArray with consideration to the horizontal space provided by the escapement delta.
* `void` [GetBoundingBoxesForStrings](#a3a0625c7fcb2af6fe24a4c961ed8a937) (const char *stringArray[], int32 numStrings, font_metric_mode mode, escapement_delta deltas[], BRect boundingBoxArray[]) const — Writes an array of BRect objects to boundingBoxArray representing the bounding rectangles of each string in stringArray with consideration to the horizontal space provided by the escapement deltas.
* `void` [GetEdges](#aa08a3467e1720dd4431fb7264a242c45) (const char charArray[], int32 numBytes, edge_info edgeArray[]) const — Determines the edge information for each character in charArray and writes the result in edgeArray.
* `void` [GetEscapements](#aa8c8b0cdba41438877b020549ac9d479) (const char charArray[], int32 numChars, escapement_delta *delta, BPoint escapementArray[]) const — Determines the escapements for each char in charArray and writes the result in escapementArray as an array of BPoint objects with consideration to the horizontal space provided by the escapement delta.
* `void` [GetEscapements](#ae89a618b3b920d802c67b6ce39e8e010) (const char charArray[], int32 numChars, escapement_delta *delta, BPoint escapementArray[], BPoint offsetArray[]) const — Determines the escapements for each char in charArray and writes the result in escapementArray as an array of BPoint objects with consideration to the horizontal space provided by the escapement delta and writes the offsets to offsetArray.
* `void` [GetEscapements](#aa39a97d880d8794025af782f14a40a74) (const char charArray[], int32 numChars, escapement_delta *delta, float escapementArray[]) const — Determines the escapements for each char in charArray and writes the result in escapementArray with consideration to the horizontal space provided by the escapement delta.
* `void` [GetEscapements](#aca49530c494a52f06fd5ea88d66a0f31) (const char charArray[], int32 numChars, float escapementArray[]) const — Determines the escapements for each char in charArray and writes the result in escapementArray.
* `void` [GetFamilyAndStyle](#ae2dc43eff88752137b4f4323a8666efa) (font_family *family, font_style *style) const — Writes out the name of the font family and/or font style.
* `void` [GetGlyphShapes](#ac51729d5adbaabf69520f9d2342af1b1) (const char charArray[], int32 numChars, BShape *glyphShapeArray[]) const — Writes an array of BShape objects to glyphShapeArray representing the glyph shapes of each character in charArray.
* `void` [GetHasGlyphs](#ad00446a1de8b804235e76c8160f056e3) (const char charArray[], int32 numChars, bool hasArray[]) const — Fills out hasArray with whether or not the font has a glyph for each character in charArray.
* `void` [GetHasGlyphs](#a48ba29558e02367418aadcafe74c50f3) (const char charArray[], int32 numChars, bool hasArray[], bool useFallbacks) const — Fills out hasArray with whether or not the font has a glyph for each character in charArray.
* `void` [GetHeight](#a9748877645b9e3ab98a3a43a5375f392) (font_height *height) const — Fills out the font_height struct with the amount of vertical space surrounding a character.
* `void` [GetStringWidths](#a876823361e0c90c6c5e2a1fb3ab7c317) (const char *stringArray[], const int32 lengthArray[], int32 numStrings, float widthArray[]) const — Determines the amount of space required to draw each string in stringArray and writes the result in widthArray.
* `void` [GetTruncatedStrings](#abbee20530f5e414a27b4437220459aec) (const char *stringArray[], int32 numStrings, uint32 mode, float width, BString resultArray[]) const — Write truncated BString objects to resultArray given source BString objects in stringArray.
* `void` [GetTruncatedStrings](#aa8313e73eb3a0a2aac8799f8d0cd52bc) (const char *stringArray[], int32 numStrings, uint32 mode, float width, char *resultArray[]) const — Write truncated strings to resultArray given source BString objects in stringArray.
* `void` [GetTunedInfo](#a763a5d1ed2a35417906502a90649fd4a) (int32 index, tuned_font_info *info) const — Writes information about the tuned font at index into info.
* `bool` [IncludesBlock](#a4ff3f4ffa944efcfa87499942d5174c0) (uint32 start, uint32 end) const — Gets whether the font includes the specified Unicode block.
* `bool` [IsFixed](#a206276168f466f05b8b59cb5b4532b02) () const — Gets whether or not the font is fixed width.
* `bool` [IsFullAndHalfFixed](#ab740fb49c0e04f29fc70ce8b3f61841b) () const — Returns whether or not the font is fixed-width and contains both full and half-width characters.
* `bool` [operator!=](#a9ddc9342d0276ec8a88e7031aec601fe) (const BFont &font) const — Inequality comparison overload method.
* `BFont &` [operator=](#ad729bd608054c0d2a32a576b6bbd3109) (const BFont &font) — Assignment overload method.
* `bool` [operator==](#a610dd945338bae7c426f55e22210818a) (const BFont &font) const — Equality comparison overload method.
* `void` [PrintToStream](#a36f7ff96cbbf27b03fec141ca1846f5f) () const — Writes information about the font to stdout.
* `float` [Rotation](#a8b6fbf57e4a5ac50aff40828c5429131) () const — Gets the font rotation.
* `void` [SetEncoding](#afdb8a74829abab2dd57591eb471e7901) (uint8 encoding) — Sets the character encoding of the font for example B_UNICODE_UTF8 or B_ISO_8859_1.
* `void` [SetFace](#afded119b1f1e6912d78d83fd23962adb) (uint16 face) — Sets the font face according to the flags set by face.
* `void` [SetFalseBoldWidth](#aef0c684bbe795fb491807d81cfb0827e) (float width) — Sets the false bold width.
* `status_t` [SetFamilyAndFace](#a1ddd1ad258ca1cb017dcbcf9f218ebb2) (const font_family family, uint16 face) — Sets the font's family and face all at once.
* `status_t` [SetFamilyAndStyle](#aadfd617a19b12a433d51dcdd75e356c1) (const font_family family, const font_style style) — Sets the font's family and style all at once.
* `void` [SetFamilyAndStyle](#ae15269df487fd4de01d1ce13612625af) (uint32 code) — Sets the font's family and style from a font identifier.
* `void` [SetFlags](#aaf75531591c0b34fd58319dde7e73490) (uint32 flags) — Sets font flags controlling antialiasing.
* `void` [SetRotation](#a77545e73f293e08b9c9ddc7d6a547808) (float rotation) — Sets the font rotation from the baseline in degrees.
* `void` [SetShear](#a1dc08c49306eabc5b197bf8c59571ab3) (float shear) — Sets the angle in degrees relative to the baseline.
* `void` [SetSize](#a433aa71874a3dbee8119d31b2f6307fe) (float size) — Sets the font size.
* `void` [SetSpacing](#a60124c81326dc4ded81c7271669f111a) (uint8 spacing) — Sets how characters are horizontally spaced relative to each other.
* `float` [Shear](#a4f13782b1626e9f48ac4a5e0d6a76f8c) () const — Gets the font shear.
* `float` [Size](#a97fd1a9309aee35a38ed236e7d0413d7) () const — Gets the font size.
* `uint8` [Spacing](#a95ad6df520a33a4e762f70b1d7d9bf47) () const — Gets the spacing constant.
* `float` [StringWidth](#a752ca8369dbd8eb6be6dcebf168fb236) (const char *string) const — Determines the amount of space required to draw string in the current font.
* `float` [StringWidth](#a53db68d7afb883f5b3be53c449faa765) (const char *string, int32 length) const — Determines the amount of space required to draw string in the current font up to length characters.
* `void` [TruncateString](#a91c0d35cea2f5142cc7c5a01505de80f) (BString *inOut, uint32 mode, float width) const — Truncates inOut to be no longer than width using the supplied truncation mode.

## Detailed Member Documentation

### `BFont()`

```cpp
BFont::BFont()
```

Creates a [BFont](classBFont.md) object initialized to `be_plain_font`. 



**See also:** [BView::GetFont()](classBView.md#af244d01f85e6d9ae7f5fcca4637dc78c)



**Since:** BeOS R3

---

### `BFont()`

```cpp
BFont::BFont(const BFont & font)
```

Creates and initializes a [BFont](classBFont.md) object from another [BFont](classBFont.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `font` | The [BFont](classBFont.md) object to initialize from. |





**Since:** BeOS R3

---

### `BFont()`

```cpp
BFont::BFont(const BFont * font)
```

Creates and initializes a [BFont](classBFont.md) object from a pointer to a [BFont](classBFont.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `font` | The pointer to a [BFont](classBFont.md) object to initialize from. |





**Since:** BeOS R3


Parameters

| Parameter | Description |
| :--- | :--- |
| `font` | The pointer to a [BFont](classBFont.md) object to initialize from. |





**Since:** BeOS R3

---

### `Blocks()`

```cpp
unicode_block BFont::Blocks()const
```

Gets a `unicode_block` object that identifies the Unicode blocks supported by this font face and family. 



**Returns:** A `unicode_block` object containing supported Unicode blocks.



**Since:** BeOS R4

---

### `BoundingBox()`

```cpp
BRect BFont::BoundingBox()const
```

Gets a [BRect](classBRect.md) that encloses the font text. 



**Returns:** A [BRect](classBRect.md) that encloses the font text.



**Since:** BeOS R4

---

### `CountTuned()`

```cpp
int32 BFont::CountTuned()const
```

Gets the number of tuned fonts for the font family and style. 



**Returns:** The number of tuned fonts.



**Since:** BeOS R3

---

### `Direction()`

```cpp
font_direction BFont::Direction()const
```

Gets the font direction, left-to-right or right-to left. 



**Returns:** The font direction.



**Since:** BeOS R3

---

### `Encoding()`

```cpp
uint8 BFont::Encoding()const
```

Gets the character encoding constant. 



**Returns:** The character encoding constant.



**See also:** [SetEncoding()](classBFont.md#afdb8a74829abab2dd57591eb471e7901)



**Since:** BeOS R3

---

### `Face()`

```cpp
uint16 BFont::Face()const
```

Gets the font face flags bitmap. 



**Returns:** The font face flags bitmap.



**See also:** [SetFace()](classBFont.md#afded119b1f1e6912d78d83fd23962adb)



**Since:** BeOS R3

---

### `FalseBoldWidth()`

```cpp
float BFont::FalseBoldWidth()const
```

Gets the width of the font as if it were bold. 



**Returns:** The font width of the bold font variety.



**See also:** [SetFalseBoldWidth()](classBFont.md#aef0c684bbe795fb491807d81cfb0827e)



**Since:** Haiku R1

---

### `FamilyAndStyle()`

```cpp
uint32 BFont::FamilyAndStyle()const
```

Gets the code of the font family and style combination. 



**Returns:** The family and style combination encoded as a unique integer.



**See also:** [SetFamilyAndStyle(uint32 code)](classBFont.md#ae15269df487fd4de01d1ce13612625af)



**Since:** BeOS R3

---

### `FileFormat()`

```cpp
font_file_format BFont::FileFormat()const
```

Gets whether the font is a TrueType™ or PostScript™ Type1 font. 



**Returns:** A `font_file_format` struct containing the font file format.



**Since:** BeOS R4

---

### `Flags()`

```cpp
uint32 BFont::Flags()const
```

Gets the antialiasing flags. 



**Returns:** The antialiasing flags.



**See also:** [SetFlags()](classBFont.md#aaf75531591c0b34fd58319dde7e73490)



**Since:** BeOS R3

---

### `GetBoundingBoxesAsGlyphs()`

```cpp
void BFont::GetBoundingBoxesAsGlyphs(const char charArray[], int32 numChars, font_metric_mode mode, BRect boundingBoxArray[])const
```

Writes an array of [BRect](classBRect.md) objects to *boundingBoxArray* representing the bounding rectangles of each character in *charArray*. 


Each [BRect](classBRect.md) object corresponds to the glyph of one character.


The `font_metric_mode` should contain one of the following values:


* `B_SCREEN_METRIC` The bounding boxes should use the screen metric.

* `B_PRINTING_METRIC` The bounding boxes should use the print metric.



Parameters

| Parameter | Description |
| :--- | :--- |
| `charArray` | The source character array. |
| `numChars` | The number of characters to consider in *charArray*. |
| `mode` | The `font_metric_mode` to use, screen or printing. |
| `boundingBoxArray` | The destination array of [BRect](classBRect.md) bounding boxes. |





**Since:** BeOS R4

---

### `GetBoundingBoxesAsString()`

```cpp
void BFont::GetBoundingBoxesAsString(const char charArray[], int32 numChars, font_metric_mode mode, escapement_delta * delta, BRect boundingBoxArray[])const
```

Writes an array of [BRect](classBRect.md) objects to *boundingBoxArray* representing the bounding rectangles of each character in *charArray* with consideration to the horizontal space provided by the escapement *delta*. 


Each [BRect](classBRect.md) object corresponds to the glyph of one character.


The `font_metric_mode` should contain one of the following values:


* `B_SCREEN_METRIC` The bounding boxes should use the screen metric.

* `B_PRINTING_METRIC` The bounding boxes should use the print metric.



The provided escapement *delta* is applied as part of the bounding box calculations. This lets you specify a character spacing is looser or tighter than normal.


The [escapement_delta](structescapement__delta.md) structure contains the following values:


* `nonspace` The amount of horizontal space to surround a visible glyph character with.

* `space` The amount of horizontal space to surround a whitespace character with, for example `B_TAB` or `B_SPACE`.



Parameters

| Parameter | Description |
| :--- | :--- |
| `charArray` | The source character array. |
| `numChars` | The number of characters to consider in *charArray*. |
| `mode` | The `font_metric_mode` to use, screen or printing. |
| `delta` | The [escapement_delta](structescapement__delta.md) structure to use. |
| `boundingBoxArray` | The destination array of [BRect](classBRect.md) bounding boxes. |





**Since:** BeOS R4

---

### `GetBoundingBoxesForStrings()`

```cpp
void BFont::GetBoundingBoxesForStrings(const char * stringArray[], int32 numStrings, font_metric_mode mode, escapement_delta deltas[], BRect boundingBoxArray[])const
```

Writes an array of [BRect](classBRect.md) objects to *boundingBoxArray* representing the bounding rectangles of each string in *stringArray* with consideration to the horizontal space provided by the escapement *deltas*. 


Each [BRect](classBRect.md) object corresponds to the bounding box of the entire string.


The `font_metric_mode` should contain one of the following values:


* `B_SCREEN_METRIC` The bounding boxes should use the screen metric.

* `B_PRINTING_METRIC` The bounding boxes should use the print metric.



The provided escapement *deltas* are applied as part of the bounding box calculations. This lets you specify a character spacing is looser or tighter than normal.


The [escapement_delta](structescapement__delta.md) structure contains the following values:


* `nonspace` The amount of horizontal space to surround a visible glyph character with.

* `space` The amount of horizontal space to surround a whitespace character with, for example `B_TAB` or `B_SPACE`.



Parameters

| Parameter | Description |
| :--- | :--- |
| `stringArray` | The source string array. |
| `numStrings` | The number of strings to consider in *stringArray*. |
| `mode` | The `font_metric_mode` to use, screen or printing. |
| `deltas` | The array of [escapement_delta](structescapement__delta.md) structures to use. |
| `boundingBoxArray` | The destination array of [BRect](classBRect.md) bounding boxes. |





**Since:** BeOS R4

---

### `GetEdges()`

```cpp
void BFont::GetEdges(const char charArray[], int32 numChars, edge_info edgeArray[])const
```

Determines the edge information for each character in *charArray* and writes the result in *edgeArray*. 


The `edge_info` struct contains the following values:


* `left` The distance that the character outline is inset from the left escapement boundary.

* `right` The distance that the character outline is inset from the right escapement boundary.



Parameters

| Parameter | Description |
| :--- | :--- |
| `charArray` | The source character array. |
| `numChars` | The number of characters to consider in *charArray*. |
| `edgeArray` | The destination array of `edge_info` structs. |





**Since:** BeOS R3

---

### `GetEscapements()`

```cpp
void BFont::GetEscapements(const char charArray[], int32 numChars, escapement_delta * delta, BPoint escapementArray[])const
```

Determines the escapements for each char in *charArray* and writes the result in *escapementArray* as an array of [BPoint](classBPoint.md) objects with consideration to the horizontal space provided by the escapement *delta*. 


The [escapement_delta](structescapement__delta.md) structure contains the following values:


* `nonspace` The amount of horizontal space to surround a visible glyph character with.

* `space` The amount of horizontal space to surround a whitespace character with, for example `B_TAB` or `B_SPACE`.



Parameters

| Parameter | Description |
| :--- | :--- |
| `charArray` | The source character array. |
| `numChars` | The number of characters to consider in *charArray*. |
| `delta` | The [escapement_delta](structescapement__delta.md) structure to use. |
| `escapementArray` | The destination array of escapements as [BPoint](classBPoint.md) objects. |





**Since:** BeOS R4

---

### `GetEscapements()`

```cpp
void BFont::GetEscapements(const char charArray[], int32 numChars, escapement_delta * delta, BPoint escapementArray[], BPoint offsetArray[])const
```

Determines the escapements for each char in *charArray* and writes the result in *escapementArray* as an array of [BPoint](classBPoint.md) objects with consideration to the horizontal space provided by the escapement *delta* and writes the offsets to *offsetArray*. 


The [escapement_delta](structescapement__delta.md) structure contains the following values:


* `nonspace` The amount of horizontal space to surround a visible glyph character with.

* `space` The amount of horizontal space to surround a whitespace character with, for example `B_TAB` or `B_SPACE`.



Parameters

| Parameter | Description |
| :--- | :--- |
| `charArray` | The source character array. |
| `numChars` | The number of characters to consider in *charArray*. |
| `delta` | The [escapement_delta](structescapement__delta.md) structure to use. |
| `escapementArray` | The destination array of escapements as [BPoint](classBPoint.md) objects. |
| `offsetArray` | The destination array of offsets as [BPoint](classBPoint.md) objects. |





**Since:** BeOS R4

---

### `GetEscapements()`

```cpp
void BFont::GetEscapements(const char charArray[], int32 numChars, escapement_delta * delta, float escapementArray[])const
```

Determines the escapements for each char in *charArray* and writes the result in *escapementArray* with consideration to the horizontal space provided by the escapement *delta*. 


The [escapement_delta](structescapement__delta.md) structure contains the following values:


* `nonspace` The amount of horizontal space to surround a visible glyph character with.

* `space` The amount of horizontal space to surround a whitespace character with, for example `B_TAB` or `B_SPACE`.



Parameters

| Parameter | Description |
| :--- | :--- |
| `charArray` | The source character array. |
| `numChars` | The number of characters to consider in *charArray*. |
| `delta` | The [escapement_delta](structescapement__delta.md) structure to use. |
| `escapementArray` | The destination array to put the escapements. |





**Since:** BeOS R3

---

### `GetEscapements()`

```cpp
void BFont::GetEscapements(const char charArray[], int32 numChars, float escapementArray[])const
```

Determines the escapements for each char in *charArray* and writes the result in *escapementArray*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `charArray` | The source character array. |
| `numChars` | The number of characters to consider in *charArray*. |
| `escapementArray` | The destination array to put the escapements. |





**Since:** BeOS R3

---

### `GetFamilyAndStyle()`

```cpp
void BFont::GetFamilyAndStyle(font_family * family, font_style * style)const
```

Writes out the name of the font family and/or font style. 


This method may be called with either *family* or *style* set to `NULL` in order to get one or the other.


Parameters

| Parameter | Description |
| :--- | :--- |
| `family` | A font_family pointer to be filled out. |
| `style` | A font_style pointer to be filled out. |





**Since:** BeOS R3

---

### `GetGlyphShapes()`

```cpp
void BFont::GetGlyphShapes(const char charArray[], int32 numChars, BShape * glyphShapeArray[])const
```

Writes an array of [BShape](classBShape.md) objects to *glyphShapeArray* representing the glyph shapes of each character in *charArray*. 


Each [BShape](classBShape.md) object corresponds to the glyph of one character.


Parameters

| Parameter | Description |
| :--- | :--- |
| `charArray` | The source character array. |
| `numChars` | The number of characters to consider in *charArray*. |
| `glyphShapeArray` | The destination array of [BShape](classBShape.md) glyphs. |





**Since:** BeOS R4

---

### `GetHasGlyphs()`

```cpp
void BFont::GetHasGlyphs(const char charArray[], int32 numChars, bool hasArray[])const
```

Fills out *hasArray* with whether or not the font has a glyph for each character in *charArray*. 


`true` is written in *hasArray* if a glyph is found for the character, `false` otherwise.


RemarksAfter the introduction of fallback fonts for missing glyphs, this is not exaclty what the name or the original desciption imply. As the objective of this method is to know if a string can be presented to the user without getting "no glyph" symbols, it will still write `true` if the queried font does not provide a glyph for a character but a fallback font does.
Parameters

| Parameter | Description |
| :--- | :--- |
| `charArray` | The source character array. |
| `numChars` | The number of characters to consider in *charArray*. |
| `hasArray` | The destination array of booleans. |





**Since:** BeOS R4

---

### `GetHasGlyphs()`

```cpp
void BFont::GetHasGlyphs(const char charArray[], int32 numChars, bool hasArray[], bool useFallbacks)const
```

Fills out *hasArray* with whether or not the font has a glyph for each character in *charArray*. 


`true` is written in *hasArray* if the character has a glyph in the current font and `false` otherwise. Fallback fonts are also considered in the search if *useFallbacks* is `true`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `charArray` | The source character array. |
| `numChars` | The number of characters to consider in *charArray*. |
| `hasArray` | The destination array of booleans. |
| `useFallbacks` | Whether to consider fallback fonts in the answer. |





**Since:** Haiku R1

---

### `GetHeight()`

```cpp
void BFont::GetHeight(font_height * _height)const
```

Fills out the `font_height` struct with the amount of vertical space surrounding a character. 


The `font_height` struct contains the following values:


* `ascent` The distance characters can ascend above the baseline.

* `descent` The distance characters can descend below the baseline.

* `leading` The distance between lines, descent above to ascent below.



Parameters

| Parameter | Description |
| :--- | :--- |
| `_height` | The `font_height` struct to fill out. |





**Since:** BeOS R3

---

### `GetStringWidths()`

```cpp
void BFont::GetStringWidths(const char * stringArray[], const int32 lengthArray[], int32 numStrings, float widthArray[])const
```

Determines the amount of space required to draw each string in *stringArray* and writes the result in *widthArray*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `stringArray` | The source string array. |
| `lengthArray` | The number of characters to consider for each string in *stringArray* |
| `numStrings` | The number of strings in *stringArray*. |
| `widthArray` | The destination array to put the widths required to draw each string. |





**Since:** BeOS R3

---

### `GetTruncatedStrings()`

```cpp
void BFont::GetTruncatedStrings(const char * stringArray[], int32 numStrings, uint32 mode, float width, BString resultArray[])const
```

Write truncated [BString](../support_kit/classBString.md) objects to *resultArray* given source [BString](../support_kit/classBString.md) objects in *stringArray*. 


The following truncation modes are supported:


* `B_TRUNCATE_BEGINNING` Truncate from the beginning of the string.

* `B_TRUNCATE_MIDDLE` Truncate from the middle of the string.

* `B_TRUNCATE_END` Truncate from the end of the string.

* `B_TRUNCATE_SMART` Truncate from anywhere, but do so so that each string is made unique after being truncated.



Parameters

| Parameter | Description |
| :--- | :--- |
| `stringArray` | The source string array. |
| `numStrings` | The number of strings in *stringArray*. |
| `mode` | Truncation mode to use. |
| `width` | The maximum width to truncate to. |
| `resultArray` | The destination string array. |





**Since:** BeOS R5

---

### `GetTruncatedStrings()`

```cpp
void BFont::GetTruncatedStrings(const char * stringArray[], int32 numStrings, uint32 mode, float width, char * resultArray[])const
```

Write truncated strings to *resultArray* given source [BString](../support_kit/classBString.md) objects in *stringArray*. 


*resultArray* is an array of pointers to string buffers which should be allocated ahead of time and should be at least 3 bytes longer than the matching input string. The 3 extra bytes provide enough room for the truncated output given that [GetTruncatedStrings()](classBFont.md#abbee20530f5e414a27b4437220459aec) truncates only a single-byte character from the input string and replaces it with an ellipsis character (which takes three bytes for the UTF-8 encoding), and adds a `NUL-terminator`.


The following truncation modes are supported:


* `B_TRUNCATE_BEGINNING` Truncate from the beginning of the string.

* `B_TRUNCATE_MIDDLE` Truncate from the middle of the string.

* `B_TRUNCATE_END` Truncate from the end of the string.

* `B_TRUNCATE_SMART` Truncate from anywhere, but do so so that each string is made unique after being truncated.



Parameters

| Parameter | Description |
| :--- | :--- |
| `stringArray` | The source string array. |
| `numStrings` | The number of strings in *stringArray*. |
| `mode` | Truncation mode to use. |
| `width` | The maximum width to truncate to. |
| `resultArray` | The destination string array. |





**Since:** BeOS R5

---

### `GetTunedInfo()`

```cpp
void BFont::GetTunedInfo(int32 index, tuned_font_info * info)const
```

Writes information about the tuned font at *index* into *info*. 


The index begins at 0 and counts tuned fonts for current font family and style only.


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index of desired tuned font. |
| `info` | The *turned_font_info* struct to be filled out. |





**Since:** BeOS R3

---

### `IncludesBlock()`

```cpp
bool BFont::IncludesBlock(uint32 start, uint32 end)const
```

Gets whether the font includes the specified Unicode block. 



**Since:** Haiku R1

---

### `IsFixed()`

```cpp
bool BFont::IsFixed()const
```

Gets whether or not the font is fixed width. 



**Returns:** `true` if the font is fixed width, `false` otherwise.



**Since:** BeOS R4

---

### `IsFullAndHalfFixed()`

```cpp
bool BFont::IsFullAndHalfFixed()const
```

Returns whether or not the font is fixed-width and contains both full and half-width characters. 


A full-and-half-fixed font is one that contains characters of only two sizes, so that CJK languages can be properly supported.



> [!NOTE]
> This was unimplemented in BeOS R5, but is implemented in Haiku.



**Since:** BeOS R4

---

### `operator!=()`

```cpp
bool BFont::operator!=(const BFont & font)const
```

Inequality comparison overload method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `font` | The [BFont](classBFont.md) object to compare the current font to. |





**Returns:** `true` if the fonts objects are NOT identical, `true` otherwise.



**Since:** BeOS R3

---

### `operator=()`

```cpp
BFont & BFont::operator=(const BFont & font)
```

Assignment overload method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `font` | The [BFont](classBFont.md) object to assign from. |





**Since:** BeOS R3

---

### `operator==()`

```cpp
bool BFont::operator==(const BFont & font)const
```

Equality comparison overload method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `font` | The [BFont](classBFont.md) object to compare the current font to. |





**Returns:** `true` if the fonts objects are identical, `false` otherwise.



**Since:** BeOS R3

---

### `PrintToStream()`

```cpp
void BFont::PrintToStream()const
```

Writes information about the font to `stdout`. 


printf("BFont { %s (%d), %s (%d) 0x%x %f/%f %fpt (%f %f %f), %d }\n", family, fFamilyID, style, fStyleID, fFace, fShear, fRotation, fSize, fHeight.ascent, fHeight.descent, fHeight.leading, fEncoding);



**Since:** BeOS R3

---

### `Rotation()`

```cpp
float BFont::Rotation()const
```

Gets the font rotation. 



**Returns:** The font rotation as an angle in degrees.



**See also:** [SetRotation()](classBFont.md#a77545e73f293e08b9c9ddc7d6a547808)



**Since:** BeOS R3

---

### `SetEncoding()`

```cpp
void BFont::SetEncoding(uint8 encoding)
```

Sets the character encoding of the font for example `B_UNICODE_UTF8` or `B_ISO_8859_1`. 


The following character encodings are supported:


* `B_UNICODE_UTF8`

* `B_ISO_8859_1` aka Latin 1 aka "Western European".

* `B_ISO_8859_2` aka Latin 2 aka "Eastern European".

* `B_ISO_8859_3` aka Latin 3 aka "South European".

* `B_ISO_8859_4` aka Latin 4 aka "Northern European".

* `B_ISO_8859_5` aka "Latin/Cyrillic".

* `B_ISO_8859_6` aka "Latin/Arabic".

* `B_ISO_8859_7` aka "Latin/Greek".

* `B_ISO_8859_8` aka "Latin/Hebrew".

* `B_ISO_8859_9` aka Latin 5 aka "Latin/Turkish".

* `B_ISO_8859_10` aka Latin 6 aka "Nordic".

* `B_MACINTOSH_ROMAN`



UTF-8 is the standard encoding used by classes in the Interface Kit. It is part of the Unicode® standard and allows Haiku to represent characters from all over the world while maintaining backwards compatibility with 7-bit ASCII codes.


Each of the encodings extend the ASCII codes and differ from each other only when the highest bit is set to 1, in other words, the value is greater than 127. Furthermore each of the encodings except for UTF-8 are represented by a single byte and consequently encompass a limited set of characters. Most of the encodings are in the ISO/IEC 8859 family of character codes with the notable exception of Macintosh Roman which is the standard encoding used by the classic Mac OS®.


If the value of the first byte of a UTF-8 character is greater than 127 it indicates that the character is a multibyte character and therefore you must look at the next byte (and possibly the third byte, or rarely even forth byte) to get the whole character.


Setting the character encoding on a view determines how [BView::DrawString()](classBView.md#a5c261dbbb4e8157799e85d6ad1530920) interprets the values passed to it and also how [BView::KeyDown()](classBView.md#abea50ea665ce5fcb76b32f1302a6852d) interprets the values representing the keys that the user presses.


Parameters

| Parameter | Description |
| :--- | :--- |
| `encoding` | The character encoding to set the font to. |





**Since:** BeOS R3

---

### `SetFace()`

```cpp
void BFont::SetFace(uint16 face)
```

Sets the font face according to the flags set by *face*. 


The following font face flags are supported:


* `B_ITALIC_FACE` Characters are slanted to the right.

* `B_UNDERSCORE_FACE` Characters are underlined.

* `B_NEGATIVE_FACE` High and low colors are reversed when drawing characters.

* `B_OUTLINED_FACE` Characters are drawn hollowed out.

* `B_STRIKEOUT_FACE` A horizontal line is drawn through their middle.

* `B_BOLD_FACE` Characters are bold.

* `B_REGULAR_FACE` Characters are drawn normally.

* `B_CONDENSED_FACE` Characters are drawn condensed. Not in BeOS 5.

* `B_LIGHT_FACE` Characters are drawn thiner than normal. Not in BeOS 5.

* `B_HEAVY_FACE` Characters are drawn heavier than normal. Not in BeOS 5.



Parameters

| Parameter | Description |
| :--- | :--- |
| `face` | The bitmap of font face flags to set. |





**Since:** BeOS R3

---

### `SetFalseBoldWidth()`

```cpp
void BFont::SetFalseBoldWidth(float width)
```

Sets the false bold width. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `width` | The false bold width to set. |





**Since:** Haiku R1

---

### `SetFamilyAndFace()`

```cpp
status_t BFont::SetFamilyAndFace(const font_family family, uint16 face)
```

Sets the font's family and face all at once. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `family` | Font family to set. |
| `face` | Font face to set. |





> [!NOTE]
> To comply with the BeBook, this function will only set valid values, i.e. passing a nonexistent family will cause only the face to be set. Additionally, if a particular face does not exist in a family, the closest match will be chosen.



**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_ERROR | Family does not exists or face has an invalid value. |





**Since:** BeOS R4

---

### `SetFamilyAndStyle()`

```cpp
status_t BFont::SetFamilyAndStyle(const font_family family, const font_style style)
```

Sets the font's family and style all at once. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `family` | Font family to set. |
| `style` | Font style to set. |





**Returns:** A status code, `B_OK` on success or an error code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_BAD_VALUE | *family* is `NULL` and *style* is `NULL`. |
| B_NAME_NOT_FOUND | Family or style do not exist. |





**Since:** BeOS R3

---

### `SetFamilyAndStyle()`

```cpp
void BFont::SetFamilyAndStyle(uint32 code)
```

Sets the font's family and style from a font identifier. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `code` | Unique font identifier obtained from the server. |





**Since:** BeOS R3

---

### `SetFlags()`

```cpp
void BFont::SetFlags(uint32 flags)
```

Sets font flags controlling antialiasing. 


The following flags are supported:


* `B_DISABLE_ANTIALIASING` Disable antialiasing.

* `B_FORCE_ANTIALIASING` Force antialiasing.



Parameters

| Parameter | Description |
| :--- | :--- |
| `flags` | The bitmap of flags to set. |





**Since:** Haiku R1

---

### `SetRotation()`

```cpp
void BFont::SetRotation(float rotation)
```

Sets the font rotation from the baseline in degrees. 


The default baseline is 0° and rotates counterclockwise. Rotation is not supported by [BTextView](classBTextView.md).


Parameters

| Parameter | Description |
| :--- | :--- |
| `rotation` | The rotation in degrees to set the font to. |





**Since:** BeOS R3

---

### `SetShear()`

```cpp
void BFont::SetShear(float shear)
```

Sets the angle in degrees relative to the baseline. 


The default shear is 90.0° measured counterclockwise. The shear range is from 45.0° to 135.0°.


Parameters

| Parameter | Description |
| :--- | :--- |
| `shear` | The shear in degrees to set the font to. |





**Since:** BeOS R3

---

### `SetSize()`

```cpp
void BFont::SetSize(float size)
```

Sets the font size. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `size` | The point size to set the font to. |





**Since:** BeOS R3

---

### `SetSpacing()`

```cpp
void BFont::SetSpacing(uint8 spacing)
```

Sets how characters are horizontally spaced relative to each other. 



* `B_CHAR_SPACING` Position each character without adjustment. Best mode for printing. Characters may collide or overlap at small font sizes.

* `B_STRING_SPACING` Optimizes the position of each character within its space. Collisions are unlikely but characters may touch each other. Best mode to use when the screen needs to match what appears on the printed page. Adding new characters requires the entire string to be redrawn.

* `B_BITMAP_SPACING` The widths of the characters are chosen so that they never collide and rarely touch. Best mode for drawing small amounts of text. Character widths are integral values. Spacing on screen will not match spacing used by `B_CHAR_SPACING` mode for printing.

* `B_FIXED_SPACING` Positions characters at a constant width. Must be used with fixed-width fonts otherwise `B_CHAR_SPACING` mode is used. All characters have an identical integral escapement.



`B_STRING_SPACING` and `B_BITMAP_SPACING` modes are relevant only for font sizes from 7.0pt to 18.0pt, above and below that range `B_CHAR_SPACING` produces nicer results. `B_CHAR_SPACING` is also always used for rotated or sheared text and when antialiasing is disabled.


Parameters

| Parameter | Description |
| :--- | :--- |
| `spacing` | The spacing mode to set. |





**See also:** [BView::DrawString()](classBView.md#a5c261dbbb4e8157799e85d6ad1530920)



**Since:** BeOS R3

---

### `Shear()`

```cpp
float BFont::Shear()const
```

Gets the font shear. 



**Returns:** The font shear as an angle from 45.0° to 135.0°.



**See also:** [SetShear()](classBFont.md#a1dc08c49306eabc5b197bf8c59571ab3)



**Since:** BeOS R3

---

### `Size()`

```cpp
float BFont::Size()const
```

Gets the font size. 



**Returns:** The font size in points.



**See also:** [SetSize()](classBFont.md#a433aa71874a3dbee8119d31b2f6307fe)



**Since:** BeOS R3

---

### `Spacing()`

```cpp
uint8 BFont::Spacing()const
```

Gets the spacing constant. 



**Returns:** The spacing constant.



**See also:** [SetSpacing()](classBFont.md#a60124c81326dc4ded81c7271669f111a)



**Since:** BeOS R3

---

### `StringWidth()`

```cpp
float BFont::StringWidth(const char * string)const
```

Determines the amount of space required to draw *string* in the current font. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The source string. |





**Returns:** The width required to draw the string.



**Since:** BeOS R3

---

### `StringWidth()`

```cpp
float BFont::StringWidth(const char * string, int32 length)const
```

Determines the amount of space required to draw *string* in the current font up to *length* characters. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The source string. |
| `length` | The number of characters in *string* to consider. |





**Returns:** The width required to draw the string.



**Since:** BeOS R3

---

### `TruncateString()`

```cpp
void BFont::TruncateString(BString * inOut, uint32 mode, float width)const
```

Truncates *inOut* to be no longer than *width* using the supplied truncation *mode*. 


The following truncation modes are supported:


* `B_NO_TRUNCATION` Does nothing.

* `B_TRUNCATE_BEGINNING` Truncate from the beginning of the string.

* `B_TRUNCATE_MIDDLE` Truncate from the middle of the string.

* `B_TRUNCATE_END` Truncate from the end of the string.

* `B_TRUNCATE_SMART` Truncate from anywhere, but do so so that each string is made unique after being truncated.



Parameters

| Parameter | Description |
| :--- | :--- |
| `inOut` | The [BString](../support_kit/classBString.md) to truncate. |
| `mode` | Truncation mode to use. |
| `width` | The maximum width to truncate to. |





**Since:** BeOS R5

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBFont.html).
