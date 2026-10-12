---
name: BString
type: class
kit: support_kit
brief: "String class supporting common string operations"
source: haiku-book
---

# BString Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

String class supporting common string operations. 


[BString](classBString.md) is a string allocation and manipulation class. The object takes care to allocate and free memory for you, so it will always be "big enough" to store your strings.


While [BString](classBString.md) is in essence a wrapper around a byte-array, which can always be accessed with the [BString::String()](classBString.md#ae4fe78b06c8e3310093b80305e14ba87) method, it does have some understanding of UTF-8 and it can be used for the manipulation of UTF-8 strings. For all operations that perform on bytes, there is an equivalent that operates on UTF-8 strings. See for example the [BString::CopyInto()](classBString.md#aaaa5b02d053305f9cb22a5fb7b215931) and [BString::CopyCharsInto()](classBString.md#ad66fac3eb976b63fa11ee333fe05eb97) methods. The main difference is that if there are any position argumens, the regular method counts the bytes and the Chars methods counts characters.



**Since:** BeOS R5

## Member List

### Public Member Functions

* [BString](#ae436643748c316070942010faeaebfa1) () — Creates an empty BString.
* [BString](#ab1cb6ea986a501f59fe138e8e977fc87) (BString &&string) noexcept — Move the data from the string to this object.
* [BString](#a136b1237d54e934c5861924e69e2e97e) (const BString &string) — Creates and initializes a BString as a copy of another string.
* [BString](#ac590cf36bedda32a92b83ff7e43caa61) (const char *string) — Creates and initializes a BString from string.
* [BString](#aba35927a8b82161cc557628d5651b7b8) (const char *string, int32 maxLength) — Creates and initializes a BString from a string up to maxLength characters.
* [~BString](#af8eabd4ce66f2b0ab9595ece0658eb8e) () — Free all resources associated with the object.
* `BString &` [operator=](#a6f476b32944d005de684c11ccb5ecbaa) (const BString &string) — Re-initialize the object to a copy of the data of a BString.
* `BString &` [operator=](#a281d1abfd26fcf20f63c32053862611b) (const char *string) — Re-initialize the BString to a copy of the data of a string.
* `BString &` [operator=](#a4e9d677b97f1bbaf449c35066b7db996) (char c) — Re-initialize the BString to a character.
* `BString &` [operator=](#a701b1349ac015b29c88cb3f06b6c26cb) (BString &&string) noexcept — Move the contents of string to this BString object.
* `BString &` [SetTo](#a2669e638b5b7f72790df7110dbcf0e36) (const char *string) — Re-initialize the BString to a copy of the data of a string.
* `BString &` [SetTo](#a71bcdc15df3c1eb0be34877a25644874) (const char *string, int32 maxLength) — Re-initialize the BString to a copy of the data of a string.
* `BString &` [SetTo](#a5218576d7893f29d7fc51fdcb9e81474) (const BString &string) — Re-initialize the BString to a copy of the data of a BString.
* `BString &` [Adopt](#a5ff4a59b5827b6d2e435d44252b2dbca) (BString &from) — Adopt the data of the given BString object.
* `BString &` [SetTo](#a10f9c7bb1bee806540f81028301ff932) (const BString &string, int32 maxLength) — Re-initialize the string to a copy of the given BString object.
* `BString &` [Adopt](#a3d124f5a2ad90ef4fcf0c027125bd0c9) (BString &from, int32 maxLength) — Adopt the data of the given BString object up to maxLength characters.
* `BString &` [SetTo](#a5c6bcd8d133f8561a7d2355273da4901) (char c, int32 count) — Re-initialize the object to a string composed of a character you specify.
* `BString &` [SetToChars](#aeebfaa616dde1aac40cf73c63f99eefc) (const char *string, int32 charCount) — UTF-8 aware version of SetTo(const char*, int32)
* `BString &` [SetToChars](#a4d4520886cfef8eab82925c46cc57fa6) (const BString &string, int32 charCount) — UTF-8 aware version of SetTo(BString&, int32)
* `BString &` [AdoptChars](#afdffa6e960765b6ab05155e02274e94b) (BString &from, int32 charCount) — UTF-8 aware version of Adopt(BString&, int32)
* `BString &` [SetToFormat](#a41beabb582880a92965c632662c46fe7) (const char *format,...) — Sets the string to a formatted string ala sprintf().
* `BString &` [SetToFormatVarArgs](#a034adf1b10fd93ce8ade226461604867) (const char *format, va_list args) — Sets the string to a formatted string ala sprintf().
* `int` [ScanWithFormat](#a5176de54d44a37209861fc76875520c5) (const char *format,...) — Parse a formatted string and save elements to variables ala scanf().
* `int` [ScanWithFormatVarArgs](#a9928c16f310b8a04eb401a8cddaf617c) (const char *format, va_list args) — Parse a formatted string and save elements to variables ala scanf().
* `BString &` [CopyInto](#aaaa5b02d053305f9cb22a5fb7b215931) (BString &into, int32 fromOffset, int32 length) const — Copy the object's data (or part of it) into another BString.
* `void` [CopyInto](#aace25b8aa915c20c77a78e839aafa687) (char *into, int32 fromOffset, int32 length) const — Copy the BString data (or part of it) into the supplied buffer.
* `BString &` [CopyCharsInto](#ad66fac3eb976b63fa11ee333fe05eb97) (BString &into, int32 fromCharOffset, int32 charCount) const — UTF-8 aware version of CopyInto(BString&, int32, int32) const.
* `bool` [CopyCharsInto](#a9b80abd2d6e9ffb53dfaf36a7c5679c7) (char *into, int32 *intoLength, int32 fromCharOffset, int32 charCount) const — UTF-8 aware version of CopyInto(char*, int32, int32) const.
* `bool` [Split](#a5e862dbc2da0b2813cf0e848910a834f) (const char *separator, bool noEmptyStrings, BStringList &_list) const — Split the string by the separator chars into _list.
* `BString &` [operator+=](#a90698a990c4711bf01841e23495ffdeb) (const BString &string) — Append the given string to the end of the BString.
* `BString &` [operator+=](#a98889adc4a2b87b38479e7cfe241b066) (const char *string) — Append the given string to the end of the BString.
* `BString &` [operator+=](#a323b0866c0eadde4e981c7d9314f34dc) (char c) — Append the given character to the end of the BString.
* `BString &` [Append](#a48bc1f85e34ef48d1c5c3972e106262c) (const BString &string) — Append the given string to the end of the BString.
* `BString &` [Append](#a7f864616085bf5ff4261ab775f698ea3) (const char *string) — Append the string data to the end of the BString.
* `BString &` [Append](#a08141e8a3d6d35d7a9c590a7550ead5f) (const BString &string, int32 length) — Append a part of the given string to the end of the BString.
* `BString &` [Append](#a0a027c7e3843bdb54d75b7825e0778c4) (const char *string, int32 length) — Append a part of the given string to end of the BString.
* `BString &` [Append](#a6f181bee93ed5c280c93f18f32ee5751) (char c, int32 count) — Append the given character repeatedly to the end of the BString.
* `BString &` [AppendChars](#a54dc7837cc9b83344bc9223a26e97c39) (const BString &string, int32 charCount) — UTF-8 aware version of Append(const BString&, int32).
* `BString &` [AppendChars](#a469c25b8b5c400e00d05765b7c10112c) (const char *string, int32 charCount) — UTF-8 aware version of Append(const char*, int32).
* `BString &` [Prepend](#a7ee2c0002c617d8d1ba12a878d2c88ce) (const char *string) — Prepend the given string to the beginning of the BString.
* `BString &` [Prepend](#a6cb0db9ce9bc27d302870b0afb703e19) (const BString &string) — Prepend the given BString to the beginning of the BString.
* `BString &` [Prepend](#a24ffc4d0d34449f58e044e71bd74407a) (const char *string, int32 length) — Prepend the given string to the beginning of the BString.
* `BString &` [Prepend](#a52f9e38ca2c92373dc36d727e3e9b179) (const BString &string, int32 length) — Prepend the given BString to the beginning of the BString.
* `BString &` [Prepend](#a9a836eab3edf578cfb01f02f280e061e) (char c, int32 count) — Prepend the given character count times to the beginning of the BString.
* `BString &` [PrependChars](#aeaec6098d2b377d0b111881e0d808c23) (const char *string, int32 charCount) — UTF-8 aware version of Prepend(const char*, int32).
* `BString &` [PrependChars](#a07062bf52a8c5bbc53e278c6c6b4e172) (const BString &string, int32 charCount) — UTF-8 aware version of Prepend(const BString&, int32).
* `BString &` [Insert](#afb0fc47dfd9dcd9e8617efefbce9d529) (const char *string, int32 position) — Inserts the given string at the given position into the BString data.
* `BString &` [Insert](#a6520e5056a0d5aa7913f9e28d69156b3) (const char *string, int32 length, int32 position) — Inserts the given string at the given position into the BString data.
* `BString &` [Insert](#a889bdacd0e127d234418f74a978f35f3) (const char *string, int32 fromOffset, int32 length, int32 position) — Inserts the given string at the given position into the BString data.
* `BString &` [Insert](#ac0dce8c1f797eeebce8a16a03ef5ee47) (const BString &string, int32 position) — Inserts the given BString at the given position into the BString data.
* `BString &` [Insert](#a533b9a6d36e1d3e73bbaca66e9d6e28b) (const BString &string, int32 length, int32 position) — Inserts the given BString at the given position into the BString data.
* `BString &` [Insert](#abee262e92886c0f16f146faecd389ad3) (const BString &string, int32 fromOffset, int32 length, int32 position) — Inserts the given string at the given position into the BString data.
* `BString &` [Insert](#a38039ae5818c3fe85f5306b87c5e6462) (char c, int32 count, int32 position) — Inserts the given character repeatedly at the given position into the BString data.
* `BString &` [InsertChars](#a45ba52319aefb3f5b1cc2257a071c7e8) (const char *string, int32 charPosition) — UTF-8 aware version of Insert(const char*, int32).
* `BString &` [InsertChars](#a8a478c57baf2a8a2257dea9ce019d947) (const char *string, int32 charCount, int32 charPosition) — UTF-8 aware version of Insert(const char*, int32, int32).
* `BString &` [InsertChars](#a439203cf7987f6a4db5d975e0211f65f) (const char *string, int32 fromCharOffset, int32 charCount, int32 charPosition) — UTF-8 aware version of Insert(const char*, int32, int32, int32).
* `BString &` [InsertChars](#a66128d146a7b1ecdfdd05f7bfa0e2d48) (const BString &string, int32 charPosition) — UTF-8 aware version of Insert(const BString&, int32).
* `BString &` [InsertChars](#a4aa5c50712f6c1641dc0aec266a01691) (const BString &string, int32 charCount, int32 charPosition) — UTF-8 aware version of Insert(const BString&, int32, int32).
* `BString &` [InsertChars](#a190fe82234de8870a5ca176fa7bcb27a) (const BString &string, int32 fromCharOffset, int32 charCount, int32 charPosition) — UTF-8 aware version of Insert(const BString&, int32, int32, int32).
* `BString &` [Truncate](#a723a55429c837aa040673cc61d9f2452) (int32 newLength, bool lazy=true) — Truncate the string to the new length.
* `BString &` [TruncateChars](#a09e0e1b8622dee073ebcbe4e2dccb3c9) (int32 newCharCount, bool lazy=true) — UTF-8 aware version of Truncate(int32, bool).
* `BString &` [Remove](#a753af1661c9a723bf141518cdbcf9e05) (int32 from, int32 length) — Remove some bytes, starting at the given offset.
* `BString &` [RemoveChars](#a9be5bd09908575d98f6dc3de443fd3a8) (int32 fromCharOffset, int32 charCount) — UTF-8 aware version of Remove(int32, int32).
* `BString &` [RemoveFirst](#a6b0d529b77c4b160703fb94082eb8708) (const BString &string) — Remove the first occurrence of the given BString.
* `BString &` [RemoveLast](#aa8d7576976583ab0d19490ec7c597313) (const BString &string) — Remove the last occurrence of the given BString.
* `BString &` [RemoveAll](#ac83f3f16d78d9e481904ea40742f38aa) (const BString &string) — Remove all occurrences of the given BString.
* `BString &` [RemoveFirst](#ab62c80c4a2101ed8fe366d4a4b047340) (const char *string) — Remove the first occurrence of the given string.
* `BString &` [RemoveLast](#af81cd6acaed80eeb0703501f7f65471b) (const char *string) — Remove the last occurrence of the given string.
* `BString &` [RemoveAll](#ae39d87233489f74ff4e8608773e8069b) (const char *string) — Remove all occurrences of the given string.
* `BString &` [RemoveSet](#a3eb8f3427ed635028c745cefad043d02) (const char *setOfBytesToRemove) — Remove all the characters specified.
* `BString &` [RemoveCharsSet](#ae17488d24d13fcbf243c914736160271) (const char *setOfCharsToRemove) — UTF-8 aware version of RemoveSet(const char*).
* `BString &` [MoveInto](#a8425b164bcf405ae472e340455b70dc1) (BString &into, int32 from, int32 length) — Move the BString data (or part of it) into another BString.
* `void` [MoveInto](#aa486017d64fc2fb1d54924e0dd8e2729) (char *into, int32 from, int32 length) — Move the BString data (or part of it) into the given buffer.
* `BString &` [MoveCharsInto](#a116e29d64f4ba34b265b818ae9c70727) (BString &into, int32 fromCharOffset, int32 charCount) — UTF-8 aware version of MoveInto(BString&, int32, int32)
* `bool` [MoveCharsInto](#ae5c0161712c97d4ace5019f7f2f76c9e) (char *into, int32 *intoLength, int32 fromCharOffset, int32 charCount) — UTF-8 aware version of MoveInto(char*, int32*, int32, int32).
* `BString &` [Trim](#a3eccca884e2478ae8013488a46839d20) () — Removes spaces from the beginning and end of the string.
* `bool` [operator<](#add02ca2563f6feaf405587c38f1bdd21) (const BString &string) const — Lexicographically compare if this BString is less than the given string.
* `bool` [operator<=](#a723ff118808c6481722b2a53c3832485) (const BString &string) const — Lexicographically compare if this BString is less than or equal to the given string.
* `bool` [operator==](#a70bcc0ac40a18bc31d0cdb6b81d9235b) (const BString &string) const — Lexicographically compare if this BString is equal to the given string.
* `bool` [operator>=](#aabad700660a6c44424218d5c6057ab94) (const BString &string) const — Lexicographically compare if this BString is greater than or equal to the given string.
* `bool` [operator>](#a24212a40b3a0b409c20131f1175f4383) (const BString &string) const — Lexicographically compare if this BString is greater than the given string.
* `bool` [operator!=](#a52d78209b34b5e05eacc4e65cfd78300) (const BString &string) const — Lexicographically compare if this BString is not equal to the given string.
* `bool` [operator<](#aa6886f45135f335ed05f002bd19f842d) (const char *string) const — Lexicographically compare if this BString is less than the given string.
* `bool` [operator<=](#a7c660e1dd749f068967cfb0f900bd96d) (const char *string) const — Lexicographically compare if this BString is less than or equal to the given string.
* `bool` [operator==](#a67138abea38871ddb5dfc8646a1676f3) (const char *string) const — Lexicographically compare if this BString is equal to the given string.
* `bool` [operator>=](#acc3c2882848a1bcd43c37fb1a44e7665) (const char *string) const — Lexicographically compare if this string is more than or equal to a given string.
* `bool` [operator>](#af7bb77100b7103935c0b325b7666e3fa) (const char *string) const — Lexicographically compare if this string is more than a given string.
* `bool` [operator!=](#a68a2d28b93ee8348163a320bb1054b22) (const char *string) const — Lexicographically compare if this string is not equal to a given string.
* [operator const char *](#a37b1225aed929fc53e83616a7f693904) () const — Return an empty string.
* `int` [Compare](#a58a9b35feb85f415771c9270d01c1951) (const BString &string) const — Lexicographically compare this BString to another string.
* `int` [Compare](#a0fe7635d7e01c69fb5516b8d8ff73152) (const char *string) const — Lexicographically compare this BString to another string.
* `int` [Compare](#a869db6f939ee4465235969581a882403) (const BString &string, int32 length) const — Lexicographically compare length characters of this BString to another string.
* `int` [Compare](#a3eed375c60e77025662dc8676e683f19) (const char *string, int32 length) const — Lexicographically compare length characters of this BString to another string.
* `int` [CompareAt](#ac921329452137b65645e8e228970677c) (size_t offset, const BString &string, int32 length) const — Lexicographically compare length of characters of this BString to another string, starting at offset.
* `int` [CompareChars](#a9318df765a0691c02023cf37dffb76a6) (const BString &string, int32 charCount) const — UTF-8 aware version of Compare(const BString&, int32).
* `int` [CompareChars](#a4f01a732af22cca3441e08e1db3fedf2) (const char *string, int32 charCount) const — UTF-8 aware version of Compare(const char*, int32).
* `int` [ICompare](#afa13ca0ea3b514faf2f17fe3c4eb1a09) (const BString &string) const — Lexicographically compare this BString to another string case-insensitively.
* `int` [ICompare](#a74937047ffe3dd74335b051495c7f839) (const char *string) const — Lexicographically compare this BString to another string case-insensitively.
* `int` [ICompare](#aede54750b9c8de8ebce055863f2ce95d) (const BString &string, int32 length) const — Lexicographically compare length characters of this BString to another string.
* `int` [ICompare](#a39b56ad4107e3d45958e7b2a8ff6e33f) (const char *string, int32 length) const — Lexicographically compare length characters of this BString to another string.
* `int32` [FindFirst](#ac77d0a8511bb3d8a513c2aaa27aef8d7) (const BString &string) const — Find the first occurrence of the given string.
* `int32` [FindFirst](#a92a8f3038d38e86070c6053ce2ef7ad7) (const char *string) const — Find the first occurrence of the given string.
* `int32` [FindFirst](#a8b7c60afce76ec240a853efeaecb2fca) (const BString &string, int32 fromOffset) const — Find the first occurrence of the given string starting from the given offset.
* `int32` [FindFirst](#a6c15db8dcc662b33937c9006f1cbf9f6) (const char *string, int32 fromOffset) const — Find the first occurrence of the given string, starting from the given offset.
* `int32` [FindFirst](#a6ff0c2dcf64e0680b0a60e18fa5b04fd) (char c) const — Find the first occurrence of the given character.
* `int32` [FindFirst](#a739d481ce757dd7a8a8676e398c19341) (char c, int32 fromOffset) const — Find the first occurrence of the given character, starting from the given offset.
* `int32` [FindFirstChars](#ab4eace227c96f8af4d517ddf12a51af5) (const BString &string, int32 fromCharOffset) const — UTF-8 aware version of FindFirst(const BString&, int32).
* `int32` [FindFirstChars](#a51142a6d6fcee24230381d5a4dda0a7d) (const char *string, int32 fromCharOffset) const — UTF-8 aware version of FindFirst(const char*, int32).
* `int32` [FindLast](#a52c1769f4ff328dcaa18e61c92880e80) (const BString &string) const — Find the last occurrence of the given string.
* `int32` [FindLast](#a854708094e6e7b866fdc52ffccdcc4fa) (const char *string) const — Find the last occurrence of the given string.
* `int32` [FindLast](#ac495d2944faa115305f2dc6e04037e60) (const BString &string, int32 beforeOffset) const — Find the last occurrence of the given BString, starting from the given offset, and going backwards.
* `int32` [FindLast](#a90254f7f2a9bf4d7c365a1a1a604a67b) (const char *string, int32 beforeOffset) const — Find the last occurrence of the given string, starting from the given offset, and going backwards.
* `int32` [FindLast](#ae594d4ac076d0357fd4977827919a58b) (char c) const — Find the last occurrence of the given character.
* `int32` [FindLast](#ac0a2148cbad211382e39c0a3073bb51e) (char c, int32 beforeOffset) const — Find the last occurrence of the given character, starting from the given offset going backwards from the end.
* `int32` [FindLastChars](#a7322f44fc7d5849110501f502aa0618c) (const BString &string, int32 beforeCharOffset) const — UTF-8 aware version of FindLast(const BString&, int32).
* `int32` [FindLastChars](#ae38f115fc388c8341f6299e819898aec) (const char *string, int32 beforeCharOffset) const — UTF-8 aware version of FindLast(const char*, int32).
* `int32` [IFindFirst](#aa1b75e6600e3cad8a209ee465a6f5c75) (const BString &string) const — Find the first occurrence of the given string case-insensitively.
* `int32` [IFindFirst](#a2c26c2df73056c1e45d2cd1994e7f320) (const char *string) const — Find the first occurrence of the given string case-insensitively.
* `int32` [IFindFirst](#a20207dfcbd00f4047e3e40863e1ea1a1) (const BString &string, int32 fromOffset) const — Find the first occurrence of the given BString case-insensitively, starting from the given offset.
* `int32` [IFindFirst](#a76dc4af740f70c453ac24418756a8223) (const char *string, int32 fromOffset) const — Find the first occurrence of the given string case-insensitively, starting from the given offset.
* `int32` [IFindLast](#a6acb54d3f9306ae8b84b6152dbcfaa1c) (const BString &string) const — Find the last occurrence of the given BString case-insensitively.
* `int32` [IFindLast](#ab4f4422f4f307000883b64ffa02f8e69) (const char *string) const — Find the last occurrence of the given string case-insensitively.
* `int32` [IFindLast](#aa20bfbe578c40a794d28883cf0bc0ce1) (const BString &string, int32 beforeOffset) const — Find the last occurrence of the given BString case-insensitively, starting from the given offset going backwards.
* `int32` [IFindLast](#a3256d109e721c3d29812eae1cd9d6545) (const char *string, int32 beforeOffset) const — Find the last occurrence of the given string case-insensitively, starting from the given offset going backwards.
* `bool` [StartsWith](#a8febb7b4bf54738272cbfb9b4a72e8fb) (const BString &string) const — Returns whether or not the BString starts with string.
* `bool` [StartsWith](#ae729298df417b0c61a67f49e5619c72f) (const char *string) const — Returns whether or not the BString starts with string.
* `bool` [StartsWith](#ac78677d2cb95830828d2c4473248efa4) (const char *string, int32 length) const — Returns whether or not the BString starts with length characters of string.
* `bool` [IStartsWith](#a4e0e7b3f1721a3f6d04741e18e59fd1e) (const BString &string) const — Returns whether or not the BString starts with string case-insensitively.
* `bool` [IStartsWith](#aee8ed0416cce7f1f533e306fe1cd1e60) (const char *string) const — Returns whether or not the BString starts with string case-insensitively.
* `bool` [IStartsWith](#aaf5b20894c34262beafcee0c7c2e2e45) (const char *string, int32 length) const — Returns whether or not the BString starts with length characters of string case-insensitively.
* `bool` [EndsWith](#a3cf975e61a07d35896d7309451fbceed) (const BString &string) const — Returns whether or not the BString ends with string.
* `bool` [EndsWith](#a0694b2a8b30e9bdde683877177c883e2) (const char *string) const — Returns whether or not the BString ends with string.
* `bool` [EndsWith](#a9ed5ad367f0eede584a05b298685d8df) (const char *string, int32 length) const — Returns whether or not the BString ends with length characters of string.
* `bool` [IEndsWith](#a5031ad99a3b2f656090a9c6a5ac9d2c7) (const BString &string) const — Returns whether or not the BString ends with string case-insensitively.
* `bool` [IEndsWith](#a48cd9f748a80f88752c2a622642e711a) (const char *string) const — Returns whether or not the BString ends with string case-insensitively.
* `bool` [IEndsWith](#a3d8e68b317a450bdc93b943b8bbf13e3) (const char *string, int32 length) const — Returns whether or not the BString ends with length characters of string case-insensitively.
* `BString &` [ReplaceFirst](#a8070ebfed4804f0f647a134b938f7f59) (char replaceThis, char withThis) — Replace the first occurrence of a character with another character.
* `BString &` [ReplaceLast](#acf2cbd843abeb75441b5b4e6864eb502) (char replaceThis, char withThis) — Replace the last occurrence of a character with another character.
* `BString &` [ReplaceAll](#a018e210b478d3b85a5a6022995eb7ed7) (char replaceThis, char withThis, int32 fromOffset=0) — Replace all occurrences of a character with another character.
* `BString &` [Replace](#acc0e9d99f53374f3817088df50f58eba) (char replaceThis, char withThis, int32 maxReplaceCount, int32 fromOffset=0) — Replace a number of occurrences of a character with another character.
* `BString &` [ReplaceFirst](#af8228f347b375de12cee5df2cb6f0a43) (const char *replaceThis, const char *withThis) — Replace the first occurrence of a string with another string.
* `BString &` [ReplaceLast](#a7f5e6827f970ec77d27cc29680a3497b) (const char *replaceThis, const char *withThis) — Replace the last occurrence of a string with another string.
* `BString &` [ReplaceAll](#a599028f034e9725bcdbbb49e319580c8) (const char *replaceThis, const char *withThis, int32 fromOffset=0) — Replace all occurrences of a string with another string.
* `BString &` [Replace](#ab72f86cac1d7bd4ce6640cc419118f6f) (const char *replaceThis, const char *withThis, int32 maxReplaceCount, int32 fromOffset=0) — Replace a number of occurrences of a string with another string.
* `BString &` [ReplaceAllChars](#af3821e4a7a3747dbde8bbde5d352f540) (const char *replaceThis, const char *withThis, int32 fromCharOffset) — UTF-8 aware version of ReplaceAll(const char*, const char*, int32).
* `BString &` [ReplaceChars](#aef5e94ded7abb6e7c7d1599a333e929f) (const char *replaceThis, const char *withThis, int32 maxReplaceCount, int32 fromCharOffset) — UTF-8 aware version of ReplaceAll(const char*, const char*, int32, int32).
* `BString &` [IReplaceFirst](#ac2cf3c7a812fae37ac7878c68ee19501) (char replaceThis, char withThis) — Replace the first occurrence of a character with another character case-insensitively.
* `BString &` [IReplaceLast](#ac40dd4f1d5da500adc6b1da0da829b56) (char replaceThis, char withThis) — Replace the last occurrence of a character with another character case-insensitively.
* `BString &` [IReplaceAll](#a0b709adadf19668137df6208d322b119) (char replaceThis, char withThis, int32 fromOffset=0) — Replace all occurrences of a character with another character case-insensitively.
* `BString &` [IReplace](#aa5bb247095ca2201ac03dc7901ba8e1c) (char replaceThis, char withThis, int32 maxReplaceCount, int32 fromOffset=0) — Replace a number of occurrences of a character with another character case-insensitively.
* `BString &` [IReplaceFirst](#a93b277b98942e2f6030c520e6b81de3b) (const char *replaceThis, const char *withThis) — Replace the first occurrence of a string with another string case-insensitively.
* `BString &` [IReplaceLast](#ab2dc3159a9afc0efa32c8368dd3f6e39) (const char *replaceThis, const char *withThis) — Replace the last occurrence of a string with another string. Case-insensitive.
* `BString &` [IReplaceAll](#a0e6c4875e816bc208783af5902f64a6c) (const char *replaceThis, const char *withThis, int32 fromOffset=0) — Replace all occurrences of a string with another string case-insensitively.
* `BString &` [IReplace](#a92b00b20f909f73d9124fa656ddbd6f0) (const char *replaceThis, const char *withThis, int32 maxReplaceCount, int32 fromOffset=0) — Replace a number of occurrences of a string with another string case-insensitively.
* `BString &` [ReplaceSet](#a84e363d092254a7f8878ea7f7a0c9ae8) (const char *setOfBytes, char with) — Replaces characters that are in a certain set with a chosen character.
* `BString &` [ReplaceSet](#af5dcd88b301b12ff3c9246f3b7608769) (const char *setOfBytes, const char *with) — Replaces characters that are in a certain set with a chosen string.
* `BString &` [ReplaceCharsSet](#ab97b5f53d6fe485ac0cd6baeb1e2e9d8) (const char *setOfChars, const char *with) — UTF-8 aware version of ReplaceSet(const char*, const char*)
* `char` [operator[]](#aecae63545eeac7757fce1027e38cfbcf) (int32 index) const — Returns the character in the string at the given offset.
* `char` [ByteAt](#aed9151cb5999b9c42b8330d45fed0835) (int32 index) const — Returns the character in the string at the given offset.
* `const char *` [CharAt](#a98942505915adb4b028695c6cb8c7dae) (int32 charIndex, int32 *bytes=NULL) const — UTF-8 aware version of ByteAt(int32).
* `bool` [CharAt](#a7037862d1f99c300c6e7761f665fbe5b) (int32 charIndex, char *buffer, int32 *bytes) const — UTF-8 aware version of ByteAt(int32) with a buffer parameter.
* `char *` [LockBuffer](#abd7474f601d6a852de12c9dd9174b39e) (int32 maxLength) — Locks the buffer and return the internal string for manipulation.
* `BString &` [UnlockBuffer](#a82984246845313df80527b32f8a19cc8) (int32 length=-1) — Unlocks the buffer after you are done with low-level manipulation.
* `BString &` [SetByteAt](#a22478fe3f170fb3a21058cb12d264207) (int32 pos, char to) — Set a byte at position pos to character to.
* `BString &` [ToLower](#a505de23603c595b798612fd9cac8a3c9) () — Convert each of the characters in the BString to lowercase.
* `BString &` [ToUpper](#a114c552044efc5025e7b55a12f40ad45) () — Convert each of the characters in the BString to uppercase.
* `BString &` [Capitalize](#aad6528190ac4ee46da09be8927f812fa) () — Convert the first character to uppercase, and the rest to lowercase.
* `BString &` [CapitalizeEachWord](#ab15fd887bd3f17d8f7965a3867d1c9ab) () — Convert the first character of every word to uppercase, and the rest to lowercase.
* `BString &` [CharacterEscape](#a06eb6cf59137d2e4b8b61a9d1fede099) (const char *original, const char *setOfCharsToEscape, char escapeWith) — Escape selected characters on a given string.
* `BString &` [CharacterEscape](#a3a3f3ae002bddbd7d123730f5963bbec) (const char *setOfCharsToEscape, char escapeWith) — Escape selected characters of this string.
* `BString &` [CharacterDeescape](#ad0f34c930befb2406cb6e19f7f6cae2f) (const char *original, char escapeChar) — Remove the character to escape with from a given string.
* `BString &` [CharacterDeescape](#a06127f94d618622cef17252b95187544) (char escapeChar) — Remove the character to escape with from this string.
* `BString &` [operator<<](#a5bcac61c11f6641fdd6fb8561fe39ffc) (const char *string) — Append string to the BString.
* `BString &` [operator<<](#ad21facd867ea1af2fcf0807809b971ca) (const BString &string) — Append string to the BString.
* `BString &` [operator<<](#a262306145bac48a8ff4ca6e2387d277a) (char c) — Append c to the BString.
* `BString &` [operator<<](#a8dba0ae3f02dd71ee4a1fda622a695d3) (bool value) — Convert the bool value to a string and append it.
* `BString &` [operator<<](#a175f003163f6725a3aeaa33380249fe3) (int value) — Convert the int value to a string and append it.
* `BString &` [operator<<](#ada9a27cfa92c2af1445c0a1b88032bbf) (unsigned int value) — Convert the unsigned int value to a string and append it.
* `BString &` [operator<<](#a1916b773fabcdd0007162319d9cfb6bd) (unsigned long value) — Convert the unsigned long value to a string and append it.
* `BString &` [operator<<](#ab5070c8e89b58466f4ced7224223b4a6) (long value) — Convert the long value to a string and append it.
* `BString &` [operator<<](#a42a9ba45e33e16572a8843d428f7c692) (unsigned long long value) — Convert the unsigned long long value to a string and append it.
* `BString &` [operator<<](#afede9898aa451e5ce6144916e1a160da) (long long value) — Convert the long long value to a string and append it.
* `BString &` [operator<<](#a5cb121a81c913bf33110a03ec05871d3) (float value) — Convert the float value to a string and append it.
* `BString &` [operator<<](#af4181b4a4540e20077c8da261a9e1064) (double value) — Convert the double value to a string and append it.

### Access

* `const char *` [String](#ae4fe78b06c8e3310093b80305e14ba87) () const — Return a pointer to the object string, NUL terminated.
* `int32` [Length](#a5ca1e86dc0053bac5268d4e0057e103a) () const — Get the length of the string in bytes.
* `int32` [CountChars](#ab7324c44bfcbd8c8b590b257eafc7886) () const — Returns the length of the object measured in characters.
* `int32` [CountBytes](#a7f3becb1690bccc3bbda8be16b27b702) (int32 fromCharOffset, int32 charCount) const — Count the number of bytes starting from a specified character.
* `bool` [IsEmpty](#ad00595bb93ed1253c1f48b3fef24174c) () const — Check whether the string is empty.
* `uint32` [HashValue](#a7aa55c1fee43eab1ae357d1df3bb5ee7) () const — Return a hash value for the current string.
* `static uint32` [HashValue](#af8b4590dfe42afd26c24db5c583ce947) (const char *string) — Return the hash value of a specified string.

## Detailed Member Documentation

### `BString()`

```cpp
BString::BString()
```

Creates an empty [BString](classBString.md). 



**Since:** BeOS R5

---

### `BString()`

```cpp
BString::BString(const char * string)
```

Creates and initializes a [BString](classBString.md) from *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to copy from. |





**Since:** BeOS R5

---

### `BString()`

```cpp
BString::BString(const BString & string)
```

Creates and initializes a [BString](classBString.md) as a copy of another *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The [BString](classBString.md) object to copy from. |





**Since:** BeOS R5

---

### `BString()`

```cpp
BString::BString(const char * string, int32 maxLength)
```

Creates and initializes a [BString](classBString.md) from a *string* up to *maxLength* characters. 


If *maxLength* is greater than the length of the source *string* then the entire source *string* is copied. If *maxLength* is less than or equal to 0 then the result is an empty [BString](classBString.md).



> [!WARNING]
> In BeOS R5 passing in a negative *maxLength* argument will copy the entire *string*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* data to initialize the [BString](classBString.md) to. |
| `maxLength` | Maximum number of characters (bytes) to copy. |





**Since:** BeOS R5

---

### `BString()`

```cpp
BString::BString(BString && string)
```

Move the data from the *string* to this object. 


Create a new string object with the data of another *string*. The *string* will no longer point to the same contents.



> [!NOTE]
> This constructor is only available for modern C++ (C++11 or later).



**Since:** Haiku R1

---

### `~BString()`

```cpp
BString::~BString()
```

Free all resources associated with the object. 


The destructor also frees the internal buffer associated with the string.



**Since:** BeOS R5

---

### `Adopt()`

```cpp
BString & BString::Adopt(BString & from)
```

Adopt the data of the given [BString](classBString.md) object. 


This method adopts the data from a [BString](classBString.md) removing the data from *from* and putting it into the [BString](classBString.md).



> [!WARNING]
> The object that is adopted from is not deleted, only its private data is initialized to a `NULL` string. If the *from* object was created on the heap you need to clean it up yourself.


Parameters

| Parameter | Description |
| :--- | :--- |
| `from` | The string data to adopt. |





**Returns:** The function always returns `*this`.



**See also:** [operator=(const BString&)](classBString.md#a6f476b32944d005de684c11ccb5ecbaa)



**Since:** BeOS R5

---

### `Adopt()`

```cpp
BString & BString::Adopt(BString & from, int32 maxLength)
```

Adopt the data of the given [BString](classBString.md) object up to *maxLength* characters. 


This method adopts the data from a [BString](classBString.md) removing the data from *from* and putting it into the [BString](classBString.md).


Parameters

| Parameter | Description |
| :--- | :--- |
| `from` | The string object to adopt. |
| `maxLength` | Maximum number of characters (bytes) to adopt. |





**Returns:** The function always returns `*this`.



**See also:** [SetTo(const BString&, int32)](classBString.md#a10f9c7bb1bee806540f81028301ff932)



**Since:** BeOS R5

---

### `AdoptChars()`

```cpp
BString & BString::AdoptChars(BString & from, int32 charCount)
```

UTF-8 aware version of [Adopt(BString&, int32)](classBString.md#a3d124f5a2ad90ef4fcf0c027125bd0c9) 


Parameters

| Parameter | Description |
| :--- | :--- |
| `from` | The string data to start adopting from. |
| `charCount` | Number of UTF-8 characters to adopt. |





**Returns:** This method always returns `*this`.



**Since:** Haiku R1

---

### `Append()`

```cpp
BString & BString::Append(char c, int32 count)
```

Append the given character repeatedly to the end of the [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `c` | The character to append. |
| `count` | The number of times this character should be appended. |





**Returns:** This method always returns `*this`.



**See also:** [operator+=(char c)](classBString.md#a323b0866c0eadde4e981c7d9314f34dc)



**Since:** BeOS R5

---

### `Append()`

```cpp
BString & BString::Append(const BString & string)
```

Append the given *string* to the end of the [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to append. |





**Returns:** This method always returns `*this`.



**See also:** [Append(const BString&, int32)](classBString.md#a08141e8a3d6d35d7a9c590a7550ead5f)



**Since:** BeOS R5


References [Length()](classBString.md#a5ca1e86dc0053bac5268d4e0057e103a), and [String()](classBString.md#ae4fe78b06c8e3310093b80305e14ba87).

---

### `Append()`

```cpp
BString & BString::Append(const BString & string, int32 length)
```

Append a part of the given *string* to the end of the [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The [BString](classBString.md) to append. |
| `length` | The maximum number of bytes to append. |





**Returns:** This method always returns `*this`.



**See also:** [operator+=(const BString&)](classBString.md#a90698a990c4711bf01841e23495ffdeb)



**Since:** BeOS R5

---

### `Append()`

```cpp
BString & BString::Append(const char * str)
```

Append the string data to the end of the [BString](classBString.md). 


This method calls [operator+=(const char *str)](classBString.md#a98889adc4a2b87b38479e7cfe241b066).



**See also:** [Append(const char*, int32)](classBString.md#a0a027c7e3843bdb54d75b7825e0778c4)



**Since:** BeOS R5


References [operator+=()](classBString.md#a90698a990c4711bf01841e23495ffdeb).

---

### `Append()`

```cpp
BString & BString::Append(const char * str, int32 length)
```

Append a part of the given string to end of the [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `str` | A pointer to the string to append. |
| `length` | The maximum number of bytes to append. |





**Returns:** This method always returns `*this`.



**See also:** [operator+=(const char*)](classBString.md#a98889adc4a2b87b38479e7cfe241b066)



**Since:** BeOS R5

---

### `AppendChars()`

```cpp
BString & BString::AppendChars(const BString & string, int32 charCount)
```

UTF-8 aware version of [Append(const BString&, int32)](classBString.md#a08141e8a3d6d35d7a9c590a7550ead5f). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to append. |
| `charCount` | The maximum number of UTF-8 characters to append. |





**Returns:** This method always returns `*this`.



**See also:** [Append(const BString&, int32)](classBString.md#a08141e8a3d6d35d7a9c590a7550ead5f)



**Since:** Haiku R1

---

### `AppendChars()`

```cpp
BString & BString::AppendChars(const char * string, int32 charCount)
```

UTF-8 aware version of [Append(const char*, int32)](classBString.md#a0a027c7e3843bdb54d75b7825e0778c4). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to append. |
| `charCount` | The maximum number of UTF-8 characters to append. |





**Returns:** This method always returns `*this`.



**See also:** [Append(const char*, int32)](classBString.md#a0a027c7e3843bdb54d75b7825e0778c4)



**Since:** Haiku R1

---

### `ByteAt()`

```cpp
char BString::ByteAt(int32 index)const
```

Returns the character in the string at the given offset. 


This function can be used to read a single byte.


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index (zero-based) of the byte to get. |





**Returns:** A reference to the specified byte, if out of bounds return 0.



**Since:** BeOS R5


References [Length()](classBString.md#a5ca1e86dc0053bac5268d4e0057e103a).

---

### `Capitalize()`

```cpp
BString & BString::Capitalize()
```

Convert the first character to uppercase, and the rest to lowercase. 



**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `CapitalizeEachWord()`

```cpp
BString & BString::CapitalizeEachWord()
```

Convert the first character of every word to uppercase, and the rest to lowercase. 


Converts the first character of every "word" (series of alphabetical characters separated by non alphabetical characters) to uppercase, and the rest to lowercase.



**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `CharacterDeescape()`

```cpp
BString & BString::CharacterDeescape(char escapeChar)
```

Remove the character to escape with from this string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `escapeChar` | The character that was used to escape with. |





**Returns:** This method always returns `*this`.



**See also:** [CharacterEscape(const char*, char)](classBString.md#a3a3f3ae002bddbd7d123730f5963bbec)

---

### `CharacterDeescape()`

```cpp
BString & BString::CharacterDeescape(const char * original, char escapeChar)
```

Remove the character to escape with from a given string. 


This version sets itself to the string supplied in the `original` parameter, and then removes the escape characters.


Parameters

| Parameter | Description |
| :--- | :--- |
| `original` | The string to be escaped. |
| `escapeChar` | The character that was used to escape with. |





**Returns:** This method always returns `*this`.



**See also:** [CharacterEscape(const char*, const char*, char)](classBString.md#a06eb6cf59137d2e4b8b61a9d1fede099)



**Since:** BeOS R5

---

### `CharacterEscape()`

```cpp
BString & BString::CharacterEscape(const char * original, const char * setOfCharsToEscape, char escapeWith)
```

Escape selected characters on a given string. 


This version sets itself to the string supplied in the `original` parameter, and then escapes the selected characters with a supplied character.


Parameters

| Parameter | Description |
| :--- | :--- |
| `original` | The string to be escaped. |
| `setOfCharsToEscape` | The set of characters that need to be escaped. |
| `escapeWith` | The character to escape with. |





**Returns:** This method always returns `*this`.



**See also:** [CharacterDeescape(char)](classBString.md#a06127f94d618622cef17252b95187544)



**Since:** BeOS R5

---

### `CharacterEscape()`

```cpp
BString & BString::CharacterEscape(const char * setOfCharsToEscape, char escapeWith)
```

Escape selected characters of this string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `setOfCharsToEscape` | The set of characters that need to be escaped. |
| `escapeWith` | The character to escape with. |





**Returns:** This method always returns `*this`.



**See also:** [CharacterDeescape(char)](classBString.md#a06127f94d618622cef17252b95187544)



**Since:** BeOS R5

---

### `CharAt()`

```cpp
bool BString::CharAt(int32 charIndex, char * buffer, int32 * bytes)const
```

UTF-8 aware version of ByteAt(int32) with a *buffer* parameter. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `charIndex` | The index (zero-based) of the UTF-8 character to get. |
| `buffer` | Set to the position in the string where the character is found. |
| `bytes` | An int32 pointer to hold the UTF-8 character. |





**See also:** ByteAt(int32, char*, int32*)



**Since:** Haiku R1

---

### `CharAt()`

```cpp
const char * BString::CharAt(int32 charIndex, int32 * bytes = NULL)const
```

UTF-8 aware version of ByteAt(int32). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `charIndex` | The index (zero-based) of the UTF-8 character to get. |
| `bytes` | An int32 pointer to hold the UTF-8 character. |





**Returns:** A reference to the specified UTF-8 character, if out of bounds return 0.



**See also:** ByteAt(int32)



**Since:** Haiku R1

---

### `Compare()`

```cpp
int BString::Compare(const BString & string)const
```

Lexicographically compare this [BString](classBString.md) to another *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |





**Returns:** An int representing the strings relationship to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| >0 | The [BString](classBString.md) sorts lexicographically after *string*. |
| =0 | The [BString](classBString.md) is equal to *string*. |
| <0 | The [BString](classBString.md) sorts lexicographically before *string*. |





**Since:** BeOS R5

---

### `Compare()`

```cpp
int BString::Compare(const BString & string, int32 length)const
```

Lexicographically compare *length* characters of this [BString](classBString.md) to another *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |
| `length` | The number of bytes to compare. |





**Returns:** An int representing the strings relationship to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| >0 | The [BString](classBString.md) sorts lexicographically after *string*. |
| =0 | The [BString](classBString.md) is equal to *string*. |
| <0 | The [BString](classBString.md) sorts lexicographically before *string*. |





**Since:** BeOS R5

---

### `Compare()`

```cpp
int BString::Compare(const char * string)const
```

Lexicographically compare this [BString](classBString.md) to another *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |





**Returns:** An int representing the strings relationship to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| >0 | The [BString](classBString.md) sorts lexicographically after *string*. |
| =0 | The [BString](classBString.md) is equal to *string*. |
| <0 | The [BString](classBString.md) sorts lexicographically before *string*. |





**See also:** [Compare(const BString&) const](classBString.md#a58a9b35feb85f415771c9270d01c1951)



**Since:** BeOS R5

---

### `Compare()`

```cpp
int BString::Compare(const char * string, int32 length)const
```

Lexicographically compare *length* characters of this [BString](classBString.md) to another *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |
| `length` | The number of bytes to compare. |





**Returns:** An int representing the strings relationship to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| >0 | The [BString](classBString.md) sorts lexicographically after *string*. |
| =0 | The [BString](classBString.md) is equal to *string*. |
| <0 | The [BString](classBString.md) sorts lexicographically before *string*. |





**See also:** [Compare(const BString&, int32) const](classBString.md#a869db6f939ee4465235969581a882403)



**Since:** BeOS R5

---

### `CompareAt()`

```cpp
int BString::CompareAt(size_t offset, const BString & string, int32 length)const
```

Lexicographically compare *length* of characters of this [BString](classBString.md) to another *string*, starting at *offset*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `offset` | The offset (in bytes) to start comparison. |
| `string` | The *string* to compare against. |
| `length` | The number of bytes to compare. |





**Returns:** An int representing the strings relationship to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| >0 | The [BString](classBString.md) sorts lexicographically after *string*. |
| =0 | The [BString](classBString.md) is equal to *string*. |
| <0 | The [BString](classBString.md) sorts lexicographically before *string*. |





**See also:** [Compare(const BString&, int32) const](classBString.md#a869db6f939ee4465235969581a882403)



**Since:** Haiku R1

---

### `CompareChars()`

```cpp
int BString::CompareChars(const BString & string, int32 charCount)const
```

UTF-8 aware version of Compare(const BString&, int32). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |
| `charCount` | The number of UTF-8 characters to compare. |





**Returns:** An int representing the strings relationship to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| >0 | The [BString](classBString.md) sorts lexicographically after *string*. |
| =0 | The [BString](classBString.md) is equal to *string*. |
| <0 | The [BString](classBString.md) sorts lexicographically before *string*. |





**See also:** Compare(const BString&, int32)



**Since:** Haiku R1

---

### `CompareChars()`

```cpp
int BString::CompareChars(const char * string, int32 charCount)const
```

UTF-8 aware version of Compare(const char*, int32). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |
| `charCount` | The number of UTF-8 characters to compare. |





**Returns:** An int representing the strings relationship to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| >0 | The [BString](classBString.md) sorts lexicographically after *string*. |
| =0 | The [BString](classBString.md) is equal to *string*. |
| <0 | The [BString](classBString.md) sorts lexicographically before *string*. |





**See also:** Compare(const char*, int32)



**Since:** Haiku R1

---

### `CopyCharsInto()`

```cpp
BString & BString::CopyCharsInto(BString & into, int32 fromOffset, int32 charCount)const
```

UTF-8 aware version of [CopyInto(BString&, int32, int32) const](classBString.md#aaaa5b02d053305f9cb22a5fb7b215931). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `into` | The [BString](classBString.md) to copy into. |
| `fromOffset` | The (zero-based) offset in bytes where to begin the copy. |
| `charCount` | The number of UTF-8 characters to copy. |





**Returns:** This method always returns a pointer to the string passed as the `into` parameter.



**See also:** [CopyInto(BString&, int32, int32) const](classBString.md#aaaa5b02d053305f9cb22a5fb7b215931)



**Since:** Haiku R1

---

### `CopyCharsInto()`

```cpp
bool BString::CopyCharsInto(char * into, int32 * intoLength, int32 fromCharOffset, int32 charCount)const
```

UTF-8 aware version of [CopyInto(char*, int32, int32) const](classBString.md#aace25b8aa915c20c77a78e839aafa687). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `into` | The buffer where to copy the object. |
| `intoLength` | The length of *into* in bytes. |
| `fromCharOffset` | The (zero-based) offset UTF-8 characters where to begin the copy. |
| `charCount` | The number of UTF-8 characters to copy. |





**See also:** [CopyInto(char*, int32, int32) const](classBString.md#aace25b8aa915c20c77a78e839aafa687)



**Returns:** `false` if *into* was `NULL`, `true` otherwise.



**Since:** Haiku R1

---

### `CopyInto()`

```cpp
BString & BString::CopyInto(BString & into, int32 fromOffset, int32 length)const
```

Copy the object's data (or part of it) into another [BString](classBString.md). 


This methods makes sure you don't copy more bytes than are available in the string. If the length exceeds the length of the string, it only copies the number of characters that are actually available.


Parameters

| Parameter | Description |
| :--- | :--- |
| `into` | The [BString](classBString.md) to copy into. |
| `fromOffset` | The (zero-based) offset where to begin the copy. |
| `length` | The number of bytes to copy. |





**Returns:** This method always returns a pointer to the string passed as the `into` parameter.



**Since:** BeOS R5

---

### `CopyInto()`

```cpp
void BString::CopyInto(char * into, int32 fromOffset, int32 length)const
```

Copy the [BString](classBString.md) data (or part of it) into the supplied buffer. 


This methods makes sure you don't copy more bytes than are available in the string. If the length exceeds the length of the string, it only copies the number of characters that are actually available.


It's up to you to make sure your buffer is large enough.


Parameters

| Parameter | Description |
| :--- | :--- |
| `into` | The buffer where to copy the object. |
| `fromOffset` | The (zero-based) offset where to begin the copy. |
| `length` | The number of bytes to copy. |





**Since:** BeOS R5

---

### `CountBytes()`

```cpp
int32 BString::CountBytes(int32 fromCharOffset, int32 charCount)const
```

Count the number of bytes starting from a specified character. 


[BString](classBString.md) is somewhat aware of UTF-8 characters, which can take up more than one byte. With this method you can count the number of bytes a subset of the string contains.



> [!WARNING]
> This method does not check whether the input is outside of the boundaries, so make sure that you check your input values.


Parameters

| Parameter | Description |
| :--- | :--- |
| `fromCharOffset` | The index of the character (not the byte!) from which to start the count |
| `charCount` | The number of characters to count |





**Returns:** An integer with the number of bytes.



**Since:** Haiku R1

---

### `CountChars()`

```cpp
int32 BString::CountChars()const
```

Returns the length of the object measured in characters. 


[BString](classBString.md) is somewhat aware of UTF-8 characters, so this method will count the actual number of characters in the string.



**Returns:** An integer which is the number of characters in the string.



**See also:** [Length()](classBString.md#a5ca1e86dc0053bac5268d4e0057e103a)



**Since:** BeOS R5

---

### `EndsWith()`

```cpp
bool BString::EndsWith(const BString & string)const
```

Returns whether or not the [BString](classBString.md) ends with *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |





**Returns:** `true` if the [BString](classBString.md) ended with *string*, `false` otherwise.



**Since:** Haiku R1

---

### `EndsWith()`

```cpp
bool BString::EndsWith(const char * string)const
```

Returns whether or not the [BString](classBString.md) ends with *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |





**Returns:** `true` if the [BString](classBString.md) ended with *string*, `false` otherwise.



**Since:** Haiku R1

---

### `EndsWith()`

```cpp
bool BString::EndsWith(const char * string, int32 length)const
```

Returns whether or not the [BString](classBString.md) ends with *length* characters of *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |
| `length` | The number of characters (bytes) of *string* to search for. |





**Returns:** `true` if the [BString](classBString.md) ended with *length* characters of *string*, `false` otherwise.



**Since:** Haiku R1

---

### `FindFirst()`

```cpp
int32 BString::FindFirst(char c)const
```

Find the first occurrence of the given character. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `c` | The character to search for. |





**Returns:** The offset (zero-based) into the data where the given character was found, or `B_ERROR` if we could not find the character.



**Since:** BeOS R5

---

### `FindFirst()`

```cpp
int32 BString::FindFirst(char c, int32 fromOffset)const
```

Find the first occurrence of the given character, starting from the given offset. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `c` | The character to search for. |
| `fromOffset` | The offset where to start the search. |





**Returns:** The offset (zero-based) into the data where the given character was found, or `B_ERROR` if we could not find the character.



**Since:** BeOS R5

---

### `FindFirst()`

```cpp
int32 BString::FindFirst(const BString & string)const
```

Find the first occurrence of the given *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |





**Returns:** The offset (zero-based) into the data where the given [BString](classBString.md) was found or `B_ERROR` if we could not find `string`.



**See also:** [IFindFirst(const BString&) const](classBString.md#aa1b75e6600e3cad8a209ee465a6f5c75)



**Since:** BeOS R5

---

### `FindFirst()`

```cpp
int32 BString::FindFirst(const BString & string, int32 fromOffset)const
```

Find the first occurrence of the given *string* starting from the given offset. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |
| `fromOffset` | The offset in bytes to start the search. |





**Returns:** An integer which is the offset (zero-based) into the data where the given [BString](classBString.md) was found or `B_ERROR` if we could not find the `string`.



**See also:** [IFindFirst(const BString&, int32) const](classBString.md#a20207dfcbd00f4047e3e40863e1ea1a1)



**Since:** BeOS R5

---

### `FindFirst()`

```cpp
int32 BString::FindFirst(const char * string)const
```

Find the first occurrence of the given *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |





**Returns:** The offset (zero-based) into the data where the given string was found, `B_BAD_VALUE` if the `string` pointer is invalid, or `B_ERROR` if we could not find `string`.



**See also:** [IFindFirst(const char*) const](classBString.md#a2c26c2df73056c1e45d2cd1994e7f320)



**Since:** BeOS R5

---

### `FindFirst()`

```cpp
int32 BString::FindFirst(const char * string, int32 fromOffset)const
```

Find the first occurrence of the given *string*, starting from the given offset. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |
| `fromOffset` | The offset in bytes to start the search. |





**Returns:** The offset (zero-based) into the data where the given string was found, `B_BAD_VALUE` if the `string` pointer is invalid, or `B_ERROR` if we could not find the `string`.



**See also:** [IFindFirst(const char*, int32) const](classBString.md#a76dc4af740f70c453ac24418756a8223)



**Since:** BeOS R5

---

### `FindFirstChars()`

```cpp
int32 BString::FindFirstChars(const BString & string, int32 fromCharOffset)const
```

UTF-8 aware version of FindFirst(const BString&, int32). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |
| `fromCharOffset` | The offset in UTF-8 characters to start the search. |





**Returns:** An integer which is the offset (zero-based) into the data where the given [BString](classBString.md) was found or `B_ERROR` if we could not find the `string`.



**See also:** FindFirst(const BString&, int32)



**Since:** Haiku R1

---

### `FindFirstChars()`

```cpp
int32 BString::FindFirstChars(const char * string, int32 fromCharOffset)const
```

UTF-8 aware version of FindFirst(const char*, int32). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |
| `fromCharOffset` | The offset in UTF-8 characters to start the search. |





**See also:** FindChars(const char*, int32)



**Since:** Haiku R1

---

### `FindLast()`

```cpp
int32 BString::FindLast(char c)const
```

Find the last occurrence of the given character. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `c` | The character to search for. |





**Returns:** The offset (zero-based) into the data where the given [BString](classBString.md) was found, or `B_ERROR` if we could not find the character.



**Since:** BeOS R5

---

### `FindLast()`

```cpp
int32 BString::FindLast(char c, int32 beforeOffset)const
```

Find the last occurrence of the given character, starting from the given offset going backwards from the end. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `c` | The character to search for. |
| `beforeOffset` | The offset in bytes to start the search. |





**Returns:** The offset (zero-based) into the data where the given character was found, or `B_ERROR` Could not find the character.



**Since:** BeOS R5

---

### `FindLast()`

```cpp
int32 BString::FindLast(const BString & string)const
```

Find the last occurrence of the given *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |





**Returns:** The offset (zero-based) into the data where the given [BString](classBString.md) was found, or `B_ERROR` if we could not find the `string`.



**See also:** [IFindLast(const BString&) const](classBString.md#a6acb54d3f9306ae8b84b6152dbcfaa1c)



**Since:** BeOS R5

---

### `FindLast()`

```cpp
int32 BString::FindLast(const BString & string, int32 beforeOffset)const
```

Find the last occurrence of the given [BString](classBString.md), starting from the given offset, and going backwards. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The [BString](classBString.md) to search for. |
| `beforeOffset` | The offset in bytes to start the search. |





**Returns:** The offset (zero-based) into the data where the given [BString](classBString.md) was found, or `B_ERROR` if we could not find the `string`.



**See also:** [IFindLast(const BString&, int32) const](classBString.md#aa20bfbe578c40a794d28883cf0bc0ce1)



**Since:** BeOS R5

---

### `FindLast()`

```cpp
int32 BString::FindLast(const char * string)const
```

Find the last occurrence of the given string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to search for. |





**Returns:** The offset in bytes (zero-based) into the data where the given string was found, `B_BAD_VALUE` if the `string` pointer is invalid, or `B_ERROR` if we could not find the `string`.



**See also:** [IFindLast(const char*) const](classBString.md#ab4f4422f4f307000883b64ffa02f8e69)



**Since:** BeOS R5

---

### `FindLast()`

```cpp
int32 BString::FindLast(const char * string, int32 beforeOffset)const
```

Find the last occurrence of the given string, starting from the given offset, and going backwards. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to search for. |
| `beforeOffset` | The offset in bytes to start the search. |





**Returns:** The offset (zero-based) into the data where the given string was found, `B_BAD_VALUE` if the `string` pointer is invalid, or `B_ERROR` if we could not find the `string`.



**See also:** [IFindLast(const char*, int32) const](classBString.md#a3256d109e721c3d29812eae1cd9d6545)



**Since:** BeOS R5

---

### `FindLastChars()`

```cpp
int32 BString::FindLastChars(const BString & string, int32 beforeCharOffset)const
```

UTF-8 aware version of FindLast(const BString&, int32). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The [BString](classBString.md) to search for. |
| `beforeCharOffset` | The offset in UTF-8 characters to start the search. |





**Returns:** The offset in bytes (zero-based) into the data where the given [BString](classBString.md) was found, or `B_ERROR` if we could not find the `string`.



**See also:** FindLast(const BString&, int32)



**Since:** Haiku R1

---

### `FindLastChars()`

```cpp
int32 BString::FindLastChars(const char * string, int32 beforeCharOffset)const
```

UTF-8 aware version of FindLast(const char*, int32). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to search for. |
| `beforeCharOffset` | The offset in UTF-8 characters to start the search. |





**Returns:** The offset in bytes (zero-based) into the data where the given string was found, `B_BAD_VALUE` if the `string` pointer is invalid, or `B_ERROR` if we could not find the `string`.



**See also:** FindLast(const char*, int32)



**Since:** Haiku R1

---

### `HashValue()`

```cpp
uint32 BString::HashValue()const
```

Return a hash value for the current string. 



**See also:** [HashValue(const char*)](classBString.md#af8b4590dfe42afd26c24db5c583ce947)



**Since:** Haiku R1


References [HashValue()](classBString.md#a7aa55c1fee43eab1ae357d1df3bb5ee7), and [String()](classBString.md#ae4fe78b06c8e3310093b80305e14ba87).


Referenced by [HashValue()](classBString.md#a7aa55c1fee43eab1ae357d1df3bb5ee7).

---

### `HashValue()`

```cpp
static uint32 BString::HashValue(const char * string)
```

Return the hash value of a specified `string`. 


This allows you to use the [BString::HashValue()](classBString.md#a7aa55c1fee43eab1ae357d1df3bb5ee7) method on any arbitrary `string`.


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string that you want to have hashed. |





**See also:** [HashValue()](classBString.md#a7aa55c1fee43eab1ae357d1df3bb5ee7)



**Since:** Haiku R1

---

### `ICompare()`

```cpp
int BString::ICompare(const BString & string)const
```

Lexicographically compare this [BString](classBString.md) to another *string* case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |





**Returns:** An int representing the strings relationship to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| >0 | The [BString](classBString.md) sorts lexicographically after *string*. |
| =0 | The [BString](classBString.md) is equal to *string*. |
| <0 | The [BString](classBString.md) sorts lexicographically before *string*. |





**See also:** [Compare(const BString&) const](classBString.md#a58a9b35feb85f415771c9270d01c1951)



**Since:** BeOS R5

---

### `ICompare()`

```cpp
int BString::ICompare(const BString & string, int32 length)const
```

Lexicographically compare *length* characters of this [BString](classBString.md) to another *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |
| `length` | The number of characters to compare. |





**Returns:** An int representing the strings relationship to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| >0 | The [BString](classBString.md) sorts lexicographically after *string*. |
| =0 | The [BString](classBString.md) is equal to *string*. |
| <0 | The [BString](classBString.md) sorts lexicographically before *string*. |





**See also:** [Compare(const BString&, int32) const](classBString.md#a869db6f939ee4465235969581a882403)



**Since:** BeOS R5

---

### `ICompare()`

```cpp
int BString::ICompare(const char * string)const
```

Lexicographically compare this [BString](classBString.md) to another *string* case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |





**Returns:** An int representing the strings relationship to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| >0 | The [BString](classBString.md) sorts lexicographically after *string*. |
| =0 | The [BString](classBString.md) is equal to *string*. |
| <0 | The [BString](classBString.md) sorts lexicographically before *string*. |





**See also:** [Compare(const BString&) const](classBString.md#a58a9b35feb85f415771c9270d01c1951)



**Since:** BeOS R5

---

### `ICompare()`

```cpp
int BString::ICompare(const char * string, int32 length)const
```

Lexicographically compare *length* characters of this [BString](classBString.md) to another *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |
| `length` | The number of characters to compare |





**Returns:** An int representing the strings relationship to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| >0 | The [BString](classBString.md) sorts lexicographically after *string*. |
| =0 | The [BString](classBString.md) is equal to *string*. |
| <0 | The [BString](classBString.md) sorts lexicographically before *string*. |





**See also:** [Compare(const BString&, int32) const](classBString.md#a869db6f939ee4465235969581a882403)



**Since:** BeOS R5

---

### `IEndsWith()`

```cpp
bool BString::IEndsWith(const BString & string)const
```

Returns whether or not the [BString](classBString.md) ends with *string* case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |





**Returns:** `true` if the [BString](classBString.md) ended with *string* case-insensitively, `false` otherwise.



**Since:** Haiku R1

---

### `IEndsWith()`

```cpp
bool BString::IEndsWith(const char * string)const
```

Returns whether or not the [BString](classBString.md) ends with *string* case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |





**Returns:** `true` if the [BString](classBString.md) ended with *string* case-insensitively, `false` otherwise.



**Since:** Haiku R1

---

### `IEndsWith()`

```cpp
bool BString::IEndsWith(const char * string, int32 length)const
```

Returns whether or not the [BString](classBString.md) ends with *length* characters of *string* case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |
| `length` | The number of characters (bytes) of *string* to search for. |





**Returns:** `true` if the [BString](classBString.md) ended with *length* characters of *string* case-insensitively, `false` otherwise.



**Since:** Haiku R1

---

### `IFindFirst()`

```cpp
int32 BString::IFindFirst(const BString & string)const
```

Find the first occurrence of the given *string* case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |





**Returns:** The offset (zero-based) into the data where the given [BString](classBString.md) was found or `B_ERROR` if we could not find `string`.



**See also:** [IFindFirst(const BString&) const](classBString.md#aa1b75e6600e3cad8a209ee465a6f5c75)



**Since:** BeOS R5

---

### `IFindFirst()`

```cpp
int32 BString::IFindFirst(const BString & string, int32 fromOffset)const
```

Find the first occurrence of the given [BString](classBString.md) case-insensitively, starting from the given offset. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |
| `fromOffset` | The offset in bytes to start the search. |





**Returns:** An integer which is the offset (zero-based) into the data where the given [BString](classBString.md) was found or `B_ERROR` if we could not find the `string`.



**See also:** [IFindFirst(const BString&, int32) const](classBString.md#a20207dfcbd00f4047e3e40863e1ea1a1)



**Since:** BeOS R5

---

### `IFindFirst()`

```cpp
int32 BString::IFindFirst(const char * string)const
```

Find the first occurrence of the given *string* case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |





**Returns:** The offset (zero-based) into the data where the given string was found, `B_BAD_VALUE` if the `string` pointer is invalid, or `B_ERROR` if we could not find `string`.



**See also:** [IFindFirst(const char*) const](classBString.md#a2c26c2df73056c1e45d2cd1994e7f320)



**Since:** BeOS R5

---

### `IFindFirst()`

```cpp
int32 BString::IFindFirst(const char * string, int32 fromOffset)const
```

Find the first occurrence of the given string case-insensitively, starting from the given offset. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |
| `fromOffset` | The offset in bytes to start the search. |





**Returns:** The offset (zero-based) into the data where the given string was found, `B_BAD_VALUE` if the `string` pointer is invalid, or `B_ERROR` if we could not find the `string`.



**See also:** [IFindFirst(const char*, int32) const](classBString.md#a76dc4af740f70c453ac24418756a8223)



**Since:** BeOS R5

---

### `IFindLast()`

```cpp
int32 BString::IFindLast(const BString & string)const
```

Find the last occurrence of the given [BString](classBString.md) case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |





**Returns:** The offset (zero-based) into the data where the given [BString](classBString.md) was found, or `B_ERROR` if we could not find the `string`.



**See also:** [IFindLast(const BString&) const](classBString.md#a6acb54d3f9306ae8b84b6152dbcfaa1c)



**Since:** BeOS R5

---

### `IFindLast()`

```cpp
int32 BString::IFindLast(const BString & string, int32 beforeOffset)const
```

Find the last occurrence of the given [BString](classBString.md) case-insensitively, starting from the given offset going backwards. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The [BString](classBString.md) to search for. |
| `beforeOffset` | The offset in bytes to start the search. |





**Returns:** The offset (zero-based) into the data where the given [BString](classBString.md) was found, or `B_ERROR` if we could not find the `string`.



**See also:** [IFindLast(const BString&, int32) const](classBString.md#aa20bfbe578c40a794d28883cf0bc0ce1)



**Since:** BeOS R5

---

### `IFindLast()`

```cpp
int32 BString::IFindLast(const char * string)const
```

Find the last occurrence of the given string case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to search for. |





**Returns:** The offset in bytes (zero-based) into the data where the given string was found, `B_BAD_VALUE` if the `string` pointer is invalid, or `B_ERROR` if we could not find the `string`.



**See also:** [IFindLast(const char*) const](classBString.md#ab4f4422f4f307000883b64ffa02f8e69)



**Since:** BeOS R5

---

### `IFindLast()`

```cpp
int32 BString::IFindLast(const char * string, int32 beforeOffset)const
```

Find the last occurrence of the given string case-insensitively, starting from the given offset going backwards. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to search for. |
| `beforeOffset` | The offset in bytes to start the search. |





**Returns:** The offset (zero-based) into the data where the given string was found, `B_BAD_VALUE` if the `string` pointer is invalid, or `B_ERROR` if we could not find the `string`.



**See also:** [IFindLast(const char*, int32) const](classBString.md#a3256d109e721c3d29812eae1cd9d6545)



**Since:** BeOS R5

---

### `Insert()`

```cpp
BString & BString::Insert(char c, int32 count, int32 pos)
```

Inserts the given character repeatedly at the given position into the [BString](classBString.md) data. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `c` | The character to insert. |
| `count` | The number of times to insert the character. |
| `pos` | The offset in bytes into the data of the [BString](classBString.md) where to insert the string. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `Insert()`

```cpp
BString & BString::Insert(const BString & string, int32 fromOffset, int32 length, int32 position)
```

Inserts the given string at the given position into the [BString](classBString.md) data. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to insert. |
| `fromOffset` | The offset in bytes of the string to be inserted. |
| `length` | The amount of bytes to insert. |
| `position` | The offset in bytes into the data of the [BString](classBString.md) where to insert the string. |





**Returns:** This method always returns `*this`.



**See also:** [Insert(const BString&, int32)](classBString.md#ac0dce8c1f797eeebce8a16a03ef5ee47)



**Since:** BeOS R5

---

### `Insert()`

```cpp
BString & BString::Insert(const BString & string, int32 length, int32 position)
```

Inserts the given [BString](classBString.md) at the given position into the [BString](classBString.md) data. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to insert. |
| `length` | The number of bytes to insert. |
| `position` | The offset in bytes into the data of the [BString](classBString.md) where to insert the string. |





**Returns:** This method always returns `*this`.



**See also:** [Insert(const BString&, int32)](classBString.md#ac0dce8c1f797eeebce8a16a03ef5ee47)



**Since:** BeOS R5

---

### `Insert()`

```cpp
BString & BString::Insert(const BString & string, int32 position)
```

Inserts the given [BString](classBString.md) at the given position into the [BString](classBString.md) data. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to insert. |
| `position` | The offset in bytes into the data of the [BString](classBString.md) where to insert the string. |





**Returns:** This method always returns `*this`.



**See also:** [Insert(const BString&, int32, int32)](classBString.md#a533b9a6d36e1d3e73bbaca66e9d6e28b)



**Since:** BeOS R5

---

### `Insert()`

```cpp
BString & BString::Insert(const char * string, int32 fromOffset, int32 length, int32 position)
```

Inserts the given string at the given position into the [BString](classBString.md) data. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to insert. |
| `fromOffset` | The offset in bytes in the *string* to be inserted. |
| `length` | The number of bytes to insert. |
| `position` | The offset in bytes into the data of the [BString](classBString.md) where to insert the string. |





**Returns:** This method always returns `*this`.



**See also:** [Insert(const char*, int32)](classBString.md#afb0fc47dfd9dcd9e8617efefbce9d529)



**Since:** BeOS R5

---

### `Insert()`

```cpp
BString & BString::Insert(const char * string, int32 length, int32 position)
```

Inserts the given string at the given position into the [BString](classBString.md) data. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to insert. |
| `length` | The number of bytes to insert. |
| `position` | The offset in bytes into the data of the [BString](classBString.md) where to insert the string. |





**Returns:** This method always returns `*this`.



**See also:** [Insert(const char*, int32)](classBString.md#afb0fc47dfd9dcd9e8617efefbce9d529)



**Since:** BeOS R5

---

### `Insert()`

```cpp
BString & BString::Insert(const char * string, int32 position)
```

Inserts the given string at the given position into the [BString](classBString.md) data. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to insert. |
| `position` | The offset in bytes where to insert the *string* into the [BString](classBString.md)'s data. |





**Returns:** This method always returns `*this`.



**See also:** [Insert(const char*, int32, int32)](classBString.md#a6520e5056a0d5aa7913f9e28d69156b3)



**Since:** BeOS R5

---

### `InsertChars()`

```cpp
BString & BString::InsertChars(const BString & string, int32 charCount, int32 charPosition)
```

UTF-8 aware version of [Insert(const BString&, int32, int32)](classBString.md#a533b9a6d36e1d3e73bbaca66e9d6e28b). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to insert. |
| `charCount` | The number of UTF-8 characters to insert. |
| `charPosition` | The offset in UTF-8 characters where to insert the string into the data of the [BString](classBString.md). |





**Returns:** This method always returns `*this`.



**See also:** [Insert(const BString&, int32, int32)](classBString.md#a533b9a6d36e1d3e73bbaca66e9d6e28b)



**Since:** Haiku R1

---

### `InsertChars()`

```cpp
BString & BString::InsertChars(const BString & string, int32 charPosition)
```

UTF-8 aware version of [Insert(const BString&, int32)](classBString.md#ac0dce8c1f797eeebce8a16a03ef5ee47). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to insert. |
| `charPosition` | The offset in UTF-8 characters where to insert the string into the data of the [BString](classBString.md). |





**Returns:** This method always returns `*this`.



**See also:** [Insert(const BString&, int32)](classBString.md#ac0dce8c1f797eeebce8a16a03ef5ee47)



**Since:** Haiku R1

---

### `InsertChars()`

```cpp
BString & BString::InsertChars(const BString & string, int32 fromCharOffset, int32 charCount, int32 charPosition)
```

UTF-8 aware version of [Insert(const BString&, int32, int32, int32)](classBString.md#abee262e92886c0f16f146faecd389ad3). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to insert. |
| `fromCharOffset` | The offset in UTF-8 characters of the string to be inserted. |
| `charCount` | The number of UTF-8 characters to insert. |
| `charPosition` | The offset in UTF-8 characters where to insert the string into the data of the [BString](classBString.md). |





**Returns:** This method always returns `*this`.



**See also:** [Insert(const BString&, int32, int32, int32)](classBString.md#abee262e92886c0f16f146faecd389ad3)



**Since:** Haiku R1

---

### `InsertChars()`

```cpp
BString & BString::InsertChars(const char * string, int32 charCount, int32 charPosition)
```

UTF-8 aware version of [Insert(const char*, int32, int32)](classBString.md#a6520e5056a0d5aa7913f9e28d69156b3). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to insert. |
| `charCount` | The number of UTF-8 characters to insert. |
| `charPosition` | The offset in UTF-8 characters where to insert the string into the data of the [BString](classBString.md). |





**Returns:** This method always returns `*this`.



**See also:** [Insert(const char*, int32, int32)](classBString.md#a6520e5056a0d5aa7913f9e28d69156b3)



**Since:** Haiku R1

---

### `InsertChars()`

```cpp
BString & BString::InsertChars(const char * string, int32 charPosition)
```

UTF-8 aware version of [Insert(const char*, int32)](classBString.md#afb0fc47dfd9dcd9e8617efefbce9d529). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to insert. |
| `charPosition` | The offset in UTF-8 characters where to insert the string into the data of the [BString](classBString.md). |





**Returns:** This method always returns `*this`.



**See also:** [Insert(const char*, int32)](classBString.md#afb0fc47dfd9dcd9e8617efefbce9d529)



**Since:** Haiku R1

---

### `InsertChars()`

```cpp
BString & BString::InsertChars(const char * string, int32 fromCharOffset, int32 charCount, int32 charPosition)
```

UTF-8 aware version of [Insert(const char*, int32, int32, int32)](classBString.md#a889bdacd0e127d234418f74a978f35f3). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to insert. |
| `fromCharOffset` | The offset in UTF-8 characters of the string to be inserted. |
| `charCount` | The number of UTF-8 characters to insert. |
| `charPosition` | The offset in UTF-8 characters where to insert the string into the data of the [BString](classBString.md). |





**Returns:** This method always returns `*this`.



**See also:** [Insert(const char*, int32, int32, int32)](classBString.md#a889bdacd0e127d234418f74a978f35f3)



**Since:** Haiku R1

---

### `IReplace()`

```cpp
BString & BString::IReplace(char replaceThis, char withThis, int32 maxReplaceCount, int32 fromOffset = 0)
```

Replace a number of occurrences of a character with another character case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The char to replace. |
| `withThis` | The char to put in its place |
| `maxReplaceCount` | The maximum number of occurrences that should be replaced. |
| `fromOffset` | The offset where to start looking for the string |





**See also:** [Replace(char, char, int32, int32)](classBString.md#acc0e9d99f53374f3817088df50f58eba)



**Since:** BeOS R5

---

### `IReplace()`

```cpp
BString & BString::IReplace(const char * replaceThis, const char * withThis, int32 maxReplaceCount, int32 fromOffset = 0)
```

Replace a number of occurrences of a string with another string case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The string to replace. |
| `withThis` | The string to put in its place |
| `maxReplaceCount` | The maximum number of occurrences that should be replaced. |
| `fromOffset` | The offset where to start looking for the string |





**See also:** [Replace(const char*, const char*, int32, int32)](classBString.md#ab72f86cac1d7bd4ce6640cc419118f6f)



**Since:** BeOS R5

---

### `IReplaceAll()`

```cpp
BString & BString::IReplaceAll(char replaceThis, char withThis, int32 fromOffset = 0)
```

Replace all occurrences of a character with another character case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The string to replace. |
| `withThis` | The string to put in its place |
| `fromOffset` | The offset where to start looking for the string |





**See also:** [ReplaceAll(char, char, int32)](classBString.md#a018e210b478d3b85a5a6022995eb7ed7)



**Since:** BeOS R5

---

### `IReplaceAll()`

```cpp
BString & BString::IReplaceAll(const char * replaceThis, const char * withThis, int32 fromOffset = 0)
```

Replace all occurrences of a string with another string case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The string to replace. |
| `withThis` | The string to put in its place. |
| `fromOffset` | The offset where to start looking for the string. |





**See also:** [ReplaceAll(const char*, const char*, int32)](classBString.md#a599028f034e9725bcdbbb49e319580c8)



**Since:** BeOS R5

---

### `IReplaceFirst()`

```cpp
BString & BString::IReplaceFirst(char replaceThis, char withThis)
```

Replace the first occurrence of a character with another character case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The string to replace. |
| `withThis` | The string to put in its place |





**See also:** [ReplaceFirst(char, char)](classBString.md#a8070ebfed4804f0f647a134b938f7f59)



**Since:** BeOS R5

---

### `IReplaceFirst()`

```cpp
BString & BString::IReplaceFirst(const char * replaceThis, const char * withThis)
```

Replace the first occurrence of a string with another string case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The string to replace. |
| `withThis` | The string to put in its place. |





**See also:** [ReplaceFirst(const char*, const char*)](classBString.md#af8228f347b375de12cee5df2cb6f0a43)



**Since:** BeOS R5

---

### `IReplaceLast()`

```cpp
BString & BString::IReplaceLast(char replaceThis, char withThis)
```

Replace the last occurrence of a character with another character case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The string to replace. |
| `withThis` | The string to put in its place |





**See also:** [ReplaceLast(char, char)](classBString.md#acf2cbd843abeb75441b5b4e6864eb502)



**Since:** BeOS R5

---

### `IReplaceLast()`

```cpp
BString & BString::IReplaceLast(const char * replaceThis, const char * withThis)
```

Replace the last occurrence of a string with another string. Case-insensitive. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The string to replace. |
| `withThis` | The string to put in its place. |





**See also:** [ReplaceLast(const char*, const char*)](classBString.md#a7f5e6827f970ec77d27cc29680a3497b)



**Since:** BeOS R5

---

### `IsEmpty()`

```cpp
bool BString::IsEmpty()const
```

Check whether the string is empty. 



**Returns:** Returns `true` if the string is empty.



**Since:** Haiku R1


References [Length()](classBString.md#a5ca1e86dc0053bac5268d4e0057e103a).

---

### `IStartsWith()`

```cpp
bool BString::IStartsWith(const BString & string)const
```

Returns whether or not the [BString](classBString.md) starts with *string* case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |





**Returns:** `true` if the [BString](classBString.md) started with *string* case-insensitively, `false` otherwise.



**Since:** Haiku R1

---

### `IStartsWith()`

```cpp
bool BString::IStartsWith(const char * string)const
```

Returns whether or not the [BString](classBString.md) starts with *string* case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |





**Returns:** `true` if the [BString](classBString.md) started with *string* case-insensitively, `false` otherwise.



**Since:** Haiku R1

---

### `IStartsWith()`

```cpp
bool BString::IStartsWith(const char * string, int32 length)const
```

Returns whether or not the [BString](classBString.md) starts with *length* characters of *string* case-insensitively. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |
| `length` | The number of characters (bytes) of *string* to search for. |





**Returns:** `true` if the [BString](classBString.md) started with *length* characters of *string* case-insensitively, `false` otherwise.



**Since:** Haiku R1

---

### `Length()`

```cpp
int32 BString::Length()const
```

Get the length of the string in bytes. 



**Returns:** An integer with the length of the string, measured in bytes.



**See also:** [CountChars()](classBString.md#ab7324c44bfcbd8c8b590b257eafc7886)



**Since:** BeOS R5


Referenced by [Append()](classBString.md#a48bc1f85e34ef48d1c5c3972e106262c), [ByteAt()](classBString.md#aed9151cb5999b9c42b8330d45fed0835), [IsEmpty()](classBString.md#ad00595bb93ed1253c1f48b3fef24174c), and [operator+=()](classBString.md#a90698a990c4711bf01841e23495ffdeb).

---

### `LockBuffer()`

```cpp
char * BString::LockBuffer(int32 maxLength)
```

Locks the buffer and return the internal string for manipulation. 


If you want to do any low-level string manipulation on the internal buffer, you should call this method. This method includes the possibility to grow the buffer so that you don't have to worry about that yourself.


Make sure you call [UnlockBuffer()](classBString.md#a82984246845313df80527b32f8a19cc8) when you're done with the manipulation.


Parameters

| Parameter | Description |
| :--- | :--- |
| `maxLength` | The size of the buffer in bytes. If you don't want a bigger buffer, passing anything under the length of the string will simply return it as is. |





**Returns:** A pointer to the buffer to manipulate.



**See also:** [UnlockBuffer()](classBString.md#a82984246845313df80527b32f8a19cc8)



**Since:** BeOS R5

---

### `MoveCharsInto()`

```cpp
BString & BString::MoveCharsInto(BString & into, int32 fromCharOffset, int32 charCount)
```

UTF-8 aware version of [MoveInto(BString&, int32, int32)](classBString.md#a8425b164bcf405ae472e340455b70dc1) 


Parameters

| Parameter | Description |
| :--- | :--- |
| `into` | The [BString](classBString.md) where to move the string into. |
| `fromCharOffset` | The offset (zero-based) in UTF-8 characters where to begin the move. |
| `charCount` | The number of UTF-8 characters to move. |





**See also:** [MoveInto(BString&, int32, int32)](classBString.md#a8425b164bcf405ae472e340455b70dc1)



**Since:** Haiku R1

---

### `MoveCharsInto()`

```cpp
bool BString::MoveCharsInto(char * into, int32 * intoLength, int32 fromCharOffset, int32 charCount)
```

UTF-8 aware version of MoveInto(char*, int32*, int32, int32). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `into` | The buffer to move the string into. |
| `intoLength` | The offset (zero-based) in bytes where to begin the move. |
| `fromCharOffset` | The offset (zero-based) in UTF-8 characters where to begin the move. |
| `charCount` | The number of UTF-8 characters to move. |





**Returns:** `false` if *into* was `NULL`, `true` otherwise.



**See also:** MoveInto(char*, int32*, int32, int32)



**Since:** Haiku R1

---

### `MoveInto()`

```cpp
BString & BString::MoveInto(BString & into, int32 from, int32 length)
```

Move the [BString](classBString.md) data (or part of it) into another [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `into` | The [BString](classBString.md) to move the string into. |
| `from` | The offset (zero-based) in bytes where to begin the move. |
| `length` | The number of bytes to move. |





**Returns:** This method always returns `into`.



**Since:** BeOS R5

---

### `MoveInto()`

```cpp
void BString::MoveInto(char * into, int32 from, int32 length)
```

Move the [BString](classBString.md) data (or part of it) into the given buffer. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `into` | The buffer to move the string into. |
| `from` | The offset (zero-based) in bytes where to begin the move. |
| `length` | The number of bytes to move. |





**Since:** BeOS R5

---

### `operator const char *()`

```cpp
BString::operator const char *()const
```

Return an empty string. 



**Returns:** An empty string.



**Since:** Haiku R1

---

### `operator!=()`

```cpp
bool BString::operator!=(const BString & string)const
```

Lexicographically compare if this [BString](classBString.md) is not equal to the given *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to compare against. |





**Since:** BeOS R5


References [String()](classBString.md#ae4fe78b06c8e3310093b80305e14ba87).

---

### `operator!=()`

```cpp
bool BString::operator!=(const char * string)const
```

Lexicographically compare if this string is not equal to a given string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |





**Since:** BeOS R5


References [operator==()](classBString.md#a70bcc0ac40a18bc31d0cdb6b81d9235b).

---

### `operator+=()`

```cpp
BString & BString::operator+=(char c)
```

Append the given character to the end of the [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `c` | The character to append. |





**Returns:** This method always returns `*this`.



**See also:** [Append(char, int32)](classBString.md#a6f181bee93ed5c280c93f18f32ee5751)

---

### `operator+=()`

```cpp
BString & BString::operator+=(const BString & string)
```

Append the given *string* to the end of the [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to append. |





**Returns:** This method always returns `*this`.



**See also:** [Append(const BString&, int32)](classBString.md#a08141e8a3d6d35d7a9c590a7550ead5f)



**Since:** BeOS R5


References [Length()](classBString.md#a5ca1e86dc0053bac5268d4e0057e103a), and [String()](classBString.md#ae4fe78b06c8e3310093b80305e14ba87).


Referenced by [Append()](classBString.md#a7f864616085bf5ff4261ab775f698ea3).

---

### `operator+=()`

```cpp
BString & BString::operator+=(const char * str)
```

Append the given string to the end of the [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `str` | A pointer to the NULL-terminated string to append. |





**Returns:** This method always returns `*this`.



**See also:** [Append(const char*, int32)](classBString.md#a0a027c7e3843bdb54d75b7825e0778c4)



**Since:** BeOS R5

---

### `operator<()`

```cpp
bool BString::operator<(const BString & string)const
```

Lexicographically compare if this [BString](classBString.md) is less than the given *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |





**Since:** BeOS R5


References [String()](classBString.md#ae4fe78b06c8e3310093b80305e14ba87).

---

### `operator<()`

```cpp
bool BString::operator<(const char * string)const
```

Lexicographically compare if this [BString](classBString.md) is less than the given *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to compare against. |





**Since:** BeOS R5

---

### `operator<<()`

```cpp
BString & BString::operator<<(bool value)
```

Convert the `bool` `value` to a string and append it. 


In case the *value* is true, the string "true" is appended to the string. Otherwise, the string "false" is appended.


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The boolean `value` ("true" of "false") to append. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `operator<<()`

```cpp
BString & BString::operator<<(char c)
```

Append *c* to the [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `c` | The character to append. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `operator<<()`

```cpp
BString & BString::operator<<(const BString & string)
```

Append *string* to the [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to append. |





**Returns:** This method always returns `*this`.

---

### `operator<<()`

```cpp
BString & BString::operator<<(const char * string)
```

Append *string* to the [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to append. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `operator<<()`

```cpp
BString & BString::operator<<(double value)
```

Convert the `double` *value* to a string and append it. 


Using this operator will append using `%.2f` formatting.


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The `double` *value* to append. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `operator<<()`

```cpp
BString & BString::operator<<(float value)
```

Convert the `float` *value* to a string and append it. 


Using this operator will append using `%.2f` formatting.


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The `float` *value* to append. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `operator<<()`

```cpp
BString & BString::operator<<(int value)
```

Convert the `int` *value* to a string and append it. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The `int` *value* to append. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `operator<<()`

```cpp
BString & BString::operator<<(long long value)
```

Convert the `long long` *value* to a string and append it. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The `long long` *value* to append. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `operator<<()`

```cpp
BString & BString::operator<<(long value)
```

Convert the `long` *value* to a string and append it. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The `long` *value* to append. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `operator<<()`

```cpp
BString & BString::operator<<(unsigned int value)
```

Convert the `unsigned int` *value* to a string and append it. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The `unsigned int` *value* to append. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `operator<<()`

```cpp
BString & BString::operator<<(unsigned long long value)
```

Convert the `unsigned long long` *value* to a string and append it. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The `unsigned long long` *value* to append. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `operator<<()`

```cpp
BString & BString::operator<<(unsigned long value)
```

Convert the `unsigned long` *value* to a string and append it. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `value` | The `unsigned long` *value* to append. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `operator<=()`

```cpp
bool BString::operator<=(const BString & string)const
```

Lexicographically compare if this [BString](classBString.md) is less than or equal to the given *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |





**Since:** BeOS R5


References [String()](classBString.md#ae4fe78b06c8e3310093b80305e14ba87).

---

### `operator<=()`

```cpp
bool BString::operator<=(const char * string)const
```

Lexicographically compare if this [BString](classBString.md) is less than or equal to the given *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |





**Since:** BeOS R5

---

### `operator=()`

```cpp
BString & BString::operator=(BString && string)
```

Move the contents of *string* to this [BString](classBString.md) object. 


The *string* will no longer point to the same contents.



> [!NOTE]
> This method is only available for modern C++ (C++11 or later).



**Returns:** This method always returns `*this`.



**Since:** Haiku R1

---

### `operator=()`

```cpp
BString & BString::operator=(char c)
```

Re-initialize the [BString](classBString.md) to a character. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `c` | The `char` to re-initialize the [BString](classBString.md) to. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `operator=()`

```cpp
BString & BString::operator=(const BString & string)
```

Re-initialize the object to a copy of the data of a [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to copy. |





**Returns:** The function always returns `*this`.



**See also:** [Adopt(BString&)](classBString.md#a5ff4a59b5827b6d2e435d44252b2dbca)



**Since:** BeOS R5


Referenced by [SetTo()](classBString.md#a2669e638b5b7f72790df7110dbcf0e36).

---

### `operator=()`

```cpp
BString & BString::operator=(const char * str)
```

Re-initialize the [BString](classBString.md) to a copy of the data of a string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `str` | The string data to re-initialize the [BString](classBString.md) to. |





**Returns:** This method always returns `*this`.



**See also:** [SetTo(const char*, int32)](classBString.md#a71bcdc15df3c1eb0be34877a25644874)



**Since:** BeOS R5

---

### `operator==()`

```cpp
bool BString::operator==(const BString & string)const
```

Lexicographically compare if this [BString](classBString.md) is equal to the given *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |





**Since:** BeOS R5


References [String()](classBString.md#ae4fe78b06c8e3310093b80305e14ba87).


Referenced by [operator!=()](classBString.md#a68a2d28b93ee8348163a320bb1054b22).

---

### `operator==()`

```cpp
bool BString::operator==(const char * string)const
```

Lexicographically compare if this [BString](classBString.md) is equal to the given *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |





**Since:** BeOS R5

---

### `operator>()`

```cpp
bool BString::operator>(const BString & string)const
```

Lexicographically compare if this [BString](classBString.md) is greater than the given *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to compare against. |





**Since:** BeOS R5


References [String()](classBString.md#ae4fe78b06c8e3310093b80305e14ba87).

---

### `operator>()`

```cpp
bool BString::operator>(const char * string)const
```

Lexicographically compare if this string is more than a given string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |





**Since:** BeOS R5

---

### `operator>=()`

```cpp
bool BString::operator>=(const BString & string)const
```

Lexicographically compare if this [BString](classBString.md) is greater than or equal to the given *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string to compare against. |





**Since:** BeOS R5


References [String()](classBString.md#ae4fe78b06c8e3310093b80305e14ba87).

---

### `operator>=()`

```cpp
bool BString::operator>=(const char * string)const
```

Lexicographically compare if this string is more than or equal to a given *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to compare against. |





**Since:** BeOS R5

---

### `operator[]()`

```cpp
char BString::operator[](int32 index)const
```

Returns the character in the string at the given offset. 


This function can be used to read a byte. There is no bound checking though, use [ByteAt()](classBString.md#aed9151cb5999b9c42b8330d45fed0835) if you don't know if the `index` parameter is valid.


Parameters

| Parameter | Description |
| :--- | :--- |
| `index` | The index (zero-based) of the byte to get. |





**Returns:** Returns a reference to the specified byte.



**Since:** BeOS R5

---

### `Prepend()`

```cpp
BString & BString::Prepend(char c, int32 count)
```

Prepend the given character *count* times to the beginning of the [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `c` | The character to prepend. |
| `count` | The number of times this character should be prepended. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `Prepend()`

```cpp
BString & BString::Prepend(const BString & string)
```

Prepend the given [BString](classBString.md) to the beginning of the [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to prepend. |





**Returns:** This method always returns `*this`.



**See also:** [Prepend(const BString&, int32)](classBString.md#a52f9e38ca2c92373dc36d727e3e9b179)



**Since:** BeOS R5

---

### `Prepend()`

```cpp
BString & BString::Prepend(const BString & string, int32 length)
```

Prepend the given [BString](classBString.md) to the beginning of the [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to prepend. |
| `length` | The maximum number of bytes to prepend. |





**Returns:** This method always returns `*this`.



**See also:** [Prepend(const BString&)](classBString.md#a6cb0db9ce9bc27d302870b0afb703e19)



**Since:** BeOS R5

---

### `Prepend()`

```cpp
BString & BString::Prepend(const char * str)
```

Prepend the given string to the beginning of the [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `str` | The *string* to prepend. |





**Returns:** This method always returns `*this`.



**See also:** [Prepend(const char*, int32)](classBString.md#a24ffc4d0d34449f58e044e71bd74407a)



**Since:** BeOS R5

---

### `Prepend()`

```cpp
BString & BString::Prepend(const char * str, int32 length)
```

Prepend the given string to the beginning of the [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `str` | The *string* to prepend. |
| `length` | The maximum number of bytes to prepend. |





**Returns:** This method always returns `*this`.



**See also:** [Prepend(const char*)](classBString.md#a7ee2c0002c617d8d1ba12a878d2c88ce)



**Since:** BeOS R5

---

### `PrependChars()`

```cpp
BString & BString::PrependChars(const BString & string, int32 charCount)
```

UTF-8 aware version of [Prepend(const BString&, int32)](classBString.md#a52f9e38ca2c92373dc36d727e3e9b179). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to prepend. |
| `charCount` | The maximum number of UTF-8 characters to prepend. |





**Returns:** This method always returns `*this`.



**See also:** [Prepend(const BString&, int32)](classBString.md#a52f9e38ca2c92373dc36d727e3e9b179)



**Since:** Haiku R1

---

### `PrependChars()`

```cpp
BString & BString::PrependChars(const char * string, int32 charCount)
```

UTF-8 aware version of [Prepend(const char*, int32)](classBString.md#a24ffc4d0d34449f58e044e71bd74407a). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to prepend. |
| `charCount` | The maximum number of UTF-8 characters to prepend. |





**Returns:** This method always returns `*this`.



**See also:** [Prepend(const char*, int32)](classBString.md#a24ffc4d0d34449f58e044e71bd74407a)



**Since:** Haiku R1

---

### `Remove()`

```cpp
BString & BString::Remove(int32 from, int32 length)
```

Remove some bytes, starting at the given offset. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `from` | The offset in bytes to start removing. |
| `length` | The number of bytes to remove. |





**Returns:** This function always returns `*this`.



**Since:** BeOS R5

---

### `RemoveAll()`

```cpp
BString & BString::RemoveAll(const BString & string)
```

Remove all occurrences of the given [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The [BString](classBString.md) to remove. |





**Returns:** This function always returns `*this`.



**Since:** BeOS R5

---

### `RemoveAll()`

```cpp
BString & BString::RemoveAll(const char * str)
```

Remove all occurrences of the given string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `str` | A pointer to the string to remove. |





**Returns:** This function always returns `*this`.



**Since:** BeOS R5

---

### `RemoveChars()`

```cpp
BString & BString::RemoveChars(int32 fromCharOffset, int32 charCount)
```

UTF-8 aware version of [Remove(int32, int32)](classBString.md#a753af1661c9a723bf141518cdbcf9e05). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `fromCharOffset` | The offset in UTF-8 characters to start removing. |
| `charCount` | The number of UTF-8 characters to remove. |





**Returns:** This function always returns `*this`.



**See also:** [Remove(int32, int32)](classBString.md#a753af1661c9a723bf141518cdbcf9e05)



**Since:** Haiku R1

---

### `RemoveCharsSet()`

```cpp
BString & BString::RemoveCharsSet(const char * setOfCharsToRemove)
```

UTF-8 aware version of [RemoveSet(const char*)](classBString.md#a3eb8f3427ed635028c745cefad043d02). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `setOfCharsToRemove` | The set of characters to remove. |





**Returns:** This function always returns `*this`.



**See also:** [RemoveSet(const char*)](classBString.md#a3eb8f3427ed635028c745cefad043d02)



**Since:** Haiku R1

---

### `RemoveFirst()`

```cpp
BString & BString::RemoveFirst(const BString & string)
```

Remove the first occurrence of the given [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The [BString](classBString.md) to remove. |





**Returns:** This function always returns `*this`.



**Since:** BeOS R5

---

### `RemoveFirst()`

```cpp
BString & BString::RemoveFirst(const char * string)
```

Remove the first occurrence of the given string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | A pointer to the string to remove. |





**Returns:** This function always returns `*this`.



**Since:** BeOS R5

---

### `RemoveLast()`

```cpp
BString & BString::RemoveLast(const BString & string)
```

Remove the last occurrence of the given [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The [BString](classBString.md) to remove. |





**Returns:** This function always returns `*this`.



**Since:** BeOS R5

---

### `RemoveLast()`

```cpp
BString & BString::RemoveLast(const char * string)
```

Remove the last occurrence of the given string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | A pointer to the string to remove. |





**Returns:** This function always returns `*this`.



**Since:** BeOS R5

---

### `RemoveSet()`

```cpp
BString & BString::RemoveSet(const char * setOfCharsToRemove)
```

Remove all the characters specified. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `setOfCharsToRemove` | The set of characters to remove. |





**Returns:** This function always returns `*this`.



**Since:** BeOS R5

---

### `Replace()`

```cpp
BString & BString::Replace(char replaceThis, char withThis, int32 maxReplaceCount, int32 fromOffset = 0)
```

Replace a number of occurrences of a character with another character. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The character to replace. |
| `withThis` | The character to put in its place |
| `maxReplaceCount` | The maximum number of characters that should be replaced. |
| `fromOffset` | The offset in bytes to start looking for the character |





**Returns:** This method always returns `*this`.



**See also:** [IReplace(char, char, int32, int32)](classBString.md#aa5bb247095ca2201ac03dc7901ba8e1c)



**Since:** BeOS R5

---

### `Replace()`

```cpp
BString & BString::Replace(const char * replaceThis, const char * withThis, int32 maxReplaceCount, int32 fromOffset = 0)
```

Replace a number of occurrences of a string with another string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The string to replace. |
| `withThis` | The string to put in its place |
| `maxReplaceCount` | The maximum number of occurrences that should be replaced. |
| `fromOffset` | The offset in bytes to start looking for the string. |





**Returns:** This method always returns `*this`.



**See also:** [IReplace(const char*, const char*, int32, int32)](classBString.md#a92b00b20f909f73d9124fa656ddbd6f0)



**Since:** BeOS R5

---

### `ReplaceAll()`

```cpp
BString & BString::ReplaceAll(char replaceThis, char withThis, int32 fromOffset = 0)
```

Replace all occurrences of a character with another character. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The character to replace. |
| `withThis` | The character to put in its place |
| `fromOffset` | The offset in bytes to start looking for the character. |





**Returns:** This method always returns `*this`.



**See also:** [IReplaceAll(char, char, int32)](classBString.md#a0b709adadf19668137df6208d322b119)



**Since:** BeOS R5

---

### `ReplaceAll()`

```cpp
BString & BString::ReplaceAll(const char * replaceThis, const char * withThis, int32 fromOffset = 0)
```

Replace all occurrences of a string with another string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The string to replace. |
| `withThis` | The string to put in its place |
| `fromOffset` | The offset in bytes to start looking for the string. |





**Returns:** This method always returns `*this`.



**See also:** [IReplaceAll(const char*, const char*, int32)](classBString.md#a0e6c4875e816bc208783af5902f64a6c)



**Since:** BeOS R5

---

### `ReplaceAllChars()`

```cpp
BString & BString::ReplaceAllChars(const char * replaceThis, const char * withThis, int32 fromCharOffset)
```

UTF-8 aware version of [ReplaceAll(const char*, const char*, int32)](classBString.md#a599028f034e9725bcdbbb49e319580c8). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The string to replace. |
| `withThis` | The string to put in its place |
| `fromCharOffset` | The offset in UTF-8 characters to start looking for the string. |





**Returns:** This method always returns `*this`.



**See also:** [ReplaceAll(const char*, const char*, int32)](classBString.md#a599028f034e9725bcdbbb49e319580c8)



**Since:** Haiku R1

---

### `ReplaceChars()`

```cpp
BString & BString::ReplaceChars(const char * replaceThis, const char * withThis, int32 maxReplaceCount, int32 fromCharOffset)
```

UTF-8 aware version of ReplaceAll(const char*, const char*, int32, int32). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The string to replace. |
| `withThis` | The string to put in its place |
| `maxReplaceCount` | The maximum number of occurrences that should be replaced. |
| `fromCharOffset` | The offset in UTF-8 characters to start looking for the string. |





**Returns:** This method always returns `*this`.



**See also:** ReplaceAll(const char*, const char*, int32, int32)



**Since:** Haiku R1

---

### `ReplaceCharsSet()`

```cpp
BString & BString::ReplaceCharsSet(const char * setOfChars, const char * with)
```

UTF-8 aware version of [ReplaceSet(const char*, const char*)](classBString.md#af5dcd88b301b12ff3c9246f3b7608769) 


Parameters

| Parameter | Description |
| :--- | :--- |
| `setOfChars` | The set of UTF-8 characters that need to be replaced. |
| `with` | The string to replace the occurrences with. |





**Returns:** This method always returns `*this`.



**Since:** Haiku R1

---

### `ReplaceFirst()`

```cpp
BString & BString::ReplaceFirst(char replaceThis, char withThis)
```

Replace the first occurrence of a character with another character. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The character to replace. |
| `withThis` | The character to put in its place. |





**Returns:** This method always returns `*this`.



**See also:** [IReplaceFirst(char, char)](classBString.md#ac2cf3c7a812fae37ac7878c68ee19501)



**Since:** BeOS R5

---

### `ReplaceFirst()`

```cpp
BString & BString::ReplaceFirst(const char * replaceThis, const char * withThis)
```

Replace the first occurrence of a string with another string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The string to replace. |
| `withThis` | The string to put in its place |





**Returns:** This method always returns `*this`.



**See also:** [IReplaceFirst(const char*, const char*)](classBString.md#a93b277b98942e2f6030c520e6b81de3b)



**Since:** BeOS R5

---

### `ReplaceLast()`

```cpp
BString & BString::ReplaceLast(char replaceThis, char withThis)
```

Replace the last occurrence of a character with another character. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The character to replace. |
| `withThis` | The character to put in its place |





**Returns:** This method always returns `*this`.



**See also:** [IReplaceLast(char, char)](classBString.md#ac40dd4f1d5da500adc6b1da0da829b56)



**Since:** BeOS R5

---

### `ReplaceLast()`

```cpp
BString & BString::ReplaceLast(const char * replaceThis, const char * withThis)
```

Replace the last occurrence of a string with another string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `replaceThis` | The string to replace. |
| `withThis` | The string to put in its place |





**Returns:** This method always returns `*this`.



**See also:** [IReplaceLast(const char*, const char*)](classBString.md#ab2dc3159a9afc0efa32c8368dd3f6e39)



**Since:** BeOS R5

---

### `ReplaceSet()`

```cpp
BString & BString::ReplaceSet(const char * setOfBytes, char with)
```

Replaces characters that are in a certain set with a chosen character. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `setOfBytes` | The set of characters that need to be replaced. |
| `with` | The character to replace the occurrences with. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `ReplaceSet()`

```cpp
BString & BString::ReplaceSet(const char * setOfBytes, const char * with)
```

Replaces characters that are in a certain set with a chosen string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `setOfBytes` | The set of chars that need to be replaced. |
| `with` | The string to replace the occurrences with. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `ScanWithFormat()`

```cpp
int BString::ScanWithFormat(const char * format, ...)
```

Parse a formatted string and save elements to variables ala `scanf()`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `format` | The *format* string to use. |
| `...` | The parameters that you want to store the parsed data into. |





**Returns:** This method returns the number of items that were parsed.



**Since:** Haiku R1

---

### `ScanWithFormatVarArgs()`

```cpp
int BString::ScanWithFormatVarArgs(const char * format, va_list args)
```

Parse a formatted string and save elements to variables ala `scanf()`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `format` | The *format* string to use. |
| `args` | The parameters that you want to store the parsed data into. |





**Returns:** This method returns the number of items that were parsed.



**Since:** Haiku R1

---

### `SetByteAt()`

```cpp
BString & BString::SetByteAt(int32 pos, char to)
```

Set a byte at position *pos* to character *to*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `pos` | The index of the byte to replace. |
| `to` | The new value that should replace the previous byte. |





**Returns:** This method always returns `*this`.



**Since:** Haiku R1

---

### `SetTo()`

```cpp
BString & BString::SetTo(char c, int32 count)
```

Re-initialize the object to a string composed of a character you specify. 


This method lets you specify the length of a string and what character you want the string to contain repeatedly.


Parameters

| Parameter | Description |
| :--- | :--- |
| `c` | The character you want to initialize the [BString](classBString.md). |
| `count` | The length of the string. |





**Returns:** The function always returns `*this`.



**See also:** [operator=(char c)](classBString.md#a4e9d677b97f1bbaf449c35066b7db996)



**Since:** BeOS R5

---

### `SetTo()`

```cpp
BString & BString::SetTo(const BString & from)
```

Re-initialize the [BString](classBString.md) to a copy of the data of a [BString](classBString.md). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `from` | The string data to re-initialize the [BString](classBString.md) to. |





**Returns:** The function always returns `*this`.



**See also:** [SetTo(const BString&, int32)](classBString.md#a10f9c7bb1bee806540f81028301ff932)



**Since:** BeOS R5

---

### `SetTo()`

```cpp
BString & BString::SetTo(const BString & string, int32 maxLength)
```

Re-initialize the string to a copy of the given [BString](classBString.md) object. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The string data to re-initialize the [BString](classBString.md) to. |
| `maxLength` | Maximum number of characters (bytes) to copy. |





**Returns:** The function always returns `*this`.



**See also:** [operator=(const BString&)](classBString.md#a6f476b32944d005de684c11ccb5ecbaa)



**Since:** BeOS R5

---

### `SetTo()`

```cpp
BString & BString::SetTo(const char * str)
```

Re-initialize the [BString](classBString.md) to a copy of the data of a string. 


This method calls [operator=(const char*)](classBString.md#a281d1abfd26fcf20f63c32053862611b).


Parameters

| Parameter | Description |
| :--- | :--- |
| `str` | The string data to re-initialize the [BString](classBString.md) to. |





**Returns:** This method always returns `*this`.



**See also:** [SetTo(const char*, int32)](classBString.md#a71bcdc15df3c1eb0be34877a25644874)



**Since:** BeOS R5


References [operator=()](classBString.md#a6f476b32944d005de684c11ccb5ecbaa).

---

### `SetTo()`

```cpp
BString & BString::SetTo(const char * str, int32 maxLength)
```

Re-initialize the [BString](classBString.md) to a copy of the data of a string. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `str` | The string data to re-initialize the [BString](classBString.md) to. |
| `maxLength` | Maximum number of characters (bytes) to copy. |





**Returns:** This method always returns `*this`.



**See also:** [operator=(const char*)](classBString.md#a281d1abfd26fcf20f63c32053862611b)



**Since:** BeOS R5

---

### `SetToChars()`

```cpp
BString & BString::SetToChars(const BString & string, int32 charCount)
```

UTF-8 aware version of SetTo(BString&, int32) 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to copy. |
| `charCount` | The number of UTF-8 characters to copy. |





**See also:** SetTo(BString&, int32)



**Returns:** This method always returns `*this`.



**Since:** Haiku R1

---

### `SetToChars()`

```cpp
BString & BString::SetToChars(const char * string, int32 charCount)
```

UTF-8 aware version of [SetTo(const char*, int32)](classBString.md#a71bcdc15df3c1eb0be34877a25644874) 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to copy. |
| `charCount` | The number of UTF-8 characters to copy. |





**See also:** [SetTo(const char*, int32)](classBString.md#a71bcdc15df3c1eb0be34877a25644874)



**Since:** Haiku R1

---

### `SetToFormat()`

```cpp
BString & BString::SetToFormat(const char * format, ...)
```

Sets the string to a formatted string ala `sprintf()`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `format` | The *format* string to use. |
| `...` | The rest of the parameters that are filled into *format*. |





**Returns:** This method always returns `*this`.



**Since:** Haiku R1

---

### `SetToFormatVarArgs()`

```cpp
BString & BString::SetToFormatVarArgs(const char * format, va_list args)
```

Sets the string to a formatted string ala `sprintf()`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `format` | The *format* string to use. |
| `args` | The rest of the parameters that are filled into *format*. |





**Returns:** This method always returns `*this`.



**Since:** Haiku R1

---

### `Split()`

```cpp
bool BString::Split(const char * separator, bool noEmptyStrings, BStringList & _list)const
```

Split the string by the *separator* chars into *_list*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `separator` | The list of *separator* characters to split on. |
| `noEmptyStrings` | If `true`, do not add empty strings to *_list*. |
| `_list` | The [BStringList](classBStringList.md) to add the strings into. |





**Since:** Haiku R1

---

### `StartsWith()`

```cpp
bool BString::StartsWith(const BString & string)const
```

Returns whether or not the [BString](classBString.md) starts with *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |





**Returns:** `true` if the [BString](classBString.md) started with *string*, `false` otherwise.



**Since:** Haiku R1

---

### `StartsWith()`

```cpp
bool BString::StartsWith(const char * string)const
```

Returns whether or not the [BString](classBString.md) starts with *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |





**Returns:** `true` if the [BString](classBString.md) started with *string*, `false` otherwise.



**Since:** Haiku R1

---

### `StartsWith()`

```cpp
bool BString::StartsWith(const char * string, int32 length)const
```

Returns whether or not the [BString](classBString.md) starts with *length* characters of *string*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | The *string* to search for. |
| `length` | The number of characters (bytes) of *string* to search for. |





**Returns:** `true` if the [BString](classBString.md) started with *length* characters of *string*, `false` otherwise.



**Since:** Haiku R1

---

### `String()`

```cpp
const char * BString::String()const
```

Return a pointer to the object string, `NUL` terminated. 


The pointer to the object string is guaranteed to be `NUL` terminated. You can't modify or free the pointer. Once the [BString](classBString.md) object is deleted, the pointer becomes invalid.


If you want to manipulate the internal string of the object directly, have a look at [LockBuffer()](classBString.md#abd7474f601d6a852de12c9dd9174b39e).



**Returns:** A pointer to the object string.



**Since:** BeOS R5


Referenced by [Append()](classBString.md#a48bc1f85e34ef48d1c5c3972e106262c), [HashValue()](classBString.md#a7aa55c1fee43eab1ae357d1df3bb5ee7), [operator!=()](classBString.md#a52d78209b34b5e05eacc4e65cfd78300), [operator+=()](classBString.md#a90698a990c4711bf01841e23495ffdeb), [operator<()](classBString.md#add02ca2563f6feaf405587c38f1bdd21), [operator<=()](classBString.md#a723ff118808c6481722b2a53c3832485), [operator==()](classBString.md#a70bcc0ac40a18bc31d0cdb6b81d9235b), [operator>()](classBString.md#a24212a40b3a0b409c20131f1175f4383), and [operator>=()](classBString.md#aabad700660a6c44424218d5c6057ab94).

---

### `ToLower()`

```cpp
BString & BString::ToLower()
```

Convert each of the characters in the [BString](classBString.md) to lowercase. 



**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `ToUpper()`

```cpp
BString & BString::ToUpper()
```

Convert each of the characters in the [BString](classBString.md) to uppercase. 



**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `Trim()`

```cpp
BString & BString::Trim()
```

Removes spaces from the beginning and end of the string. 


The definition of a space is set by the `isspace()` function.



**Returns:** This method always returns `*this`.



**Since:** Haiku R1

---

### `Truncate()`

```cpp
BString & BString::Truncate(int32 newLength, bool lazy = true)
```

Truncate the string to the new length. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `newLength` | The new length of the string in bytes. |
| `lazy` | If true, the memory-optimization is postponed until later. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

### `TruncateChars()`

```cpp
BString & BString::TruncateChars(int32 newCharCount, bool lazy = true)
```

UTF-8 aware version of [Truncate(int32, bool)](classBString.md#a723a55429c837aa040673cc61d9f2452). 


Parameters

| Parameter | Description |
| :--- | :--- |
| `newCharCount` | The new length of the string in UTF-8 characters. |
| `lazy` | If true, the memory-optimization is postponed until later. |





**See also:** [Truncate(int32, bool)](classBString.md#a723a55429c837aa040673cc61d9f2452)



**Since:** Haiku R1

---

### `UnlockBuffer()`

```cpp
BString & BString::UnlockBuffer(int32 length = -1)
```

Unlocks the buffer after you are done with low-level manipulation. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `length` | The length in bytes to trim the string to in order to keep the internal buffer sane. If you don't pass a value in it, `strlen()` will be used to determine the length. |





**Returns:** This method always returns `*this`.



**Since:** BeOS R5

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBString.html).
