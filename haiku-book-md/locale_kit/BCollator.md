---
name: BCollator
type: class
kit: locale_kit
brief: "Class for handling locale-aware collation (sorting) of strings"
source: haiku-book
---

# BCollator Class
**Kit/Group:** [Locale Kit](../locale_kit/group__locale.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Class for handling locale-aware collation (sorting) of strings. 


[BCollator](classBCollator.md) is designed to handle collation (sorting) of strings. Unlike string sorting using strcmp() or similar functions that compare raw bytes the collation is done using a set of rules that changes from one locale to another. For example, in Spanish, 'ch' is considered to be a letter and is sorted between 'c' and 'd'. This class is also able to perform natural number sorting so that 2 is sorted before 10 unlike byte-based sorting.



> [!WARNING]
> This class is not multithread-safe. So if you want to use a [BCollator](classBCollator.md) from more than one thread you need to protect it with a lock.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BCollator](#ae07621ec715d5376a93b2fa5c614246b) () — Construct a collator with the default locale and strength.
* [BCollator](#aeff16f67a2e8ac21ae710e6784295ec2) (BMessage *archive) — Unarchive a collator from a message.
* [BCollator](#a07418d21aace37e019ba08f4e1df41e9) (const BCollator &other) — Copy constructor.
* [BCollator](#ab1ca4b563ded3abaa3a97e5c8d1bcdbf) (const char *locale, int8 strength=B_COLLATE_PRIMARY, bool ignorePunctuation=false) — Construct a collator for the given locale and strength.
* [~BCollator](#adf50b517d043af89cda41625c6f97538) () — Destructor method.
* `status_t` [Archive](#a6ad070bcec766bb2e4b3963f2af53e90) (BMessage *archive, bool deep) const — Archive the object into a BMessage.
* `int` [Compare](#a3af1c9ae97365dab40d0d43a4fd11d5c) (const char *s1, const char *s2) const — Returns the difference betweens the two strings.
* `bool` [Equal](#a5fee4e2861f85e1a4a65625ed72ff08b) (const char *s1, const char *s2) const — Compares two strings for equality.
* `status_t` [GetSortKey](#a7566b825b2d37eb54df9dee49ce991ac) (const char *string, BString *key) const — Compute the sortkey of a string.
* `bool` [Greater](#a149a4ff29c1dd8aa118333168fc0a357) (const char *s1, const char *s2) const — Determine if a string is greater than another.
* `bool` [GreaterOrEqual](#a3460ddd8a21965501e73855a6be074bb) (const char *s1, const char *s2) const — Determines if one string is greater than another.
* `bool` [IgnorePunctuation](#a1a952b5156f2949d4fd5339c23b02969) () const — Gets the behavior of the collator with regards to punctuation.
* `BCollator &` [operator=](#ad9bf170ccbe66f710a7a0fdbb220d9b6) (const BCollator &source) — Assignment operator.
* `void` [SetIgnorePunctuation](#a15c509d0aec3ba488b729b39126b51e0) (bool ignore) — Enable or disable punctuation handling.
* `status_t` [SetNumericSorting](#aef84d3e2cce998b10c850526c772937d) (bool enable) — Enable or disable numeric order sorting.
* `status_t` [SetStrength](#afb899892efad8cfcc4c9e5847ba3827e) (int8 strength) const — Set the strength of the collator.
* [BArchivable](#a66e6b947f092d32f287913a8c253290f) () — Constructor. Does nothing.
* [BArchivable](#aed4f0566f9659b03912a859077c27c89) (BMessage *from) — Constructor. Does important behind-the-scenes work in the unarchiving process.
* `virtual` [~BArchivable](#af1a37be4b953423787b0d0be0b345ff3) () — Destructor. Does nothing.
* `virtual status_t` [AllArchived](#a4075315c407443a3b0dbb3d7551b53c9) (BMessage *archive) const — Method relating to the use of BArchiver.
* `virtual status_t` [AllUnarchived](#a2b1d74c147ea18e4b4bfacd42f11e0d2) (const BMessage *archive) — Method relating to the use of BUnarchiver.
* `virtual status_t` [Archive](#a051c5263dd1a75dcf28787b60825dc44) (BMessage *into, bool deep=true) const — Archive the object into a BMessage.
* `virtual status_t` [Perform](#a827fa92febcf925f07545aa9777df9de) (perform_code d, void *arg) — Perform some action (Internal method defined for binary compatibility purposes).

### Static Public Member Functions

* `static BArchivable *` [Instantiate](#af4c8d97e7647b25094c3fb370e6bab7e) (BMessage *archive) — Unarchive the collator.
* `static BArchivable *` [Instantiate](#a04efcb17fa2a64a776923cc12303efcd) (BMessage *archive) — Static member to restore objects from messages.

## Detailed Member Documentation

### `BCollator()`

```cpp
BCollator::BCollator()
```

Construct a collator with the default locale and strength. 



> [!IMPORTANT]
> The default collator should be constructed by the [BLocale](classBLocale.md) instead since it is aware of the currently defined locale.


This constructor uses `B_COLLATE_PRIMARY` strength.



**Since:** Haiku R1

---

### `BCollator()`

```cpp
BCollator::BCollator(const char * locale, int8 strength = B_COLLATE_PRIMARY, bool ignorePunctuation = false)
```

Construct a collator for the given *locale* and *strength*. 


This constructor loads the data for the given locale. You can also set the *strength* and choose if the collator should take punctuation into account or not.


Parameters

| Parameter | Description |
| :--- | :--- |
| `locale` | The *locale* to build the constructor for. |
| `strength` | The collator class provide four level of *strength*.  * `B_COLLATE_PRIMARY` doesn't differentiate e from é,  * `B_COLLATE_SECONDARY` takes letter accents into account,  * `B_COLLATE_TERTIARY` is case sensitive,  * `B_COLLATE_QUATERNARY` is very strict. Most of the time you shouldn't need to go this far. |
| `ignorePunctuation` | Ignore punctuation during sorting. |





**Since:** Haiku R1

---

### `BCollator()`

```cpp
BCollator::BCollator(BMessage * archive)
```

Unarchive a collator from a message. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The message to unarchive the [BCollator](classBCollator.md) object from. |





**Since:** Haiku R1

---

### `BCollator()`

```cpp
BCollator::BCollator(const BCollator & other)
```

Copy constructor. 


Copies a [BCollator](classBCollator.md) object from another [BCollator](classBCollator.md) object.


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BCollator](classBCollator.md) to copy from. |





**Since:** Haiku R1

---

### `~BCollator()`

```cpp
BCollator::~BCollator()
```

Destructor method. 


Deletes the [BCollator](classBCollator.md) object freeing the resources it consumes.



**Since:** Haiku R1

---

### `Archive()`

```cpp
status_t BCollator::Archive(BMessage * into, bool deep)const
```

Archive the object into a [BMessage](../application_kit/classBMessage.md). 


You should call this method from your derived implementation as it adds the data needed to instantiate your object to the message.


Parameters

| Parameter | Description |
| :--- | :--- |
| `into` | The message you store your object in. |
| `deep` | If `true`, all children of this object should be archived as well. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The archive operation was successful. |
| B_BAD_VALUE | `NULL` *archive* message. |
| B_ERROR | The archive operation failed. |





**Since:** BeOS R3


Reimplemented from [BArchivable](../support_kit/classBArchivable.md#a051c5263dd1a75dcf28787b60825dc44).

---

### `Compare()`

```cpp
int BCollator::Compare(const char * s1, const char * s2)const
```

Returns the difference betweens the two strings. 


const 


This method should be used in place of the strcmp() function to perform locale-aware comparisons.


Parameters

| Parameter | Description |
| :--- | :--- |
| `s1` | The first string to compare. |
| `s2` | The second string to compare. |





**Returns:** An integer value representing how the strings compare to each other.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| 0 | if the strings are equal. |
| <0 | if s1 is less than s2. |
| >0 | if s1 is greater than s2. |





**Since:** Haiku R1


Referenced by [Equal()](classBCollator.md#a5fee4e2861f85e1a4a65625ed72ff08b), [Greater()](classBCollator.md#a149a4ff29c1dd8aa118333168fc0a357), and [GreaterOrEqual()](classBCollator.md#a3460ddd8a21965501e73855a6be074bb).

---

### `Equal()`

```cpp
bool BCollator::Equal(const char * s1, const char * s2)const
```

Compares two strings for equality. 


const 


Note that strings that are not byte-by-byte identical may end up being treated as equal by this method. For example two strings may be considered equal if the only differences between them are in case and punctuation, depending on the *strength* used. Using `B_QUANTERNARY_STRENGTH` will force this method return `true` only if the strings are byte-for-byte identical.


Parameters

| Parameter | Description |
| :--- | :--- |
| `s1` | The first string to compare. |
| `s2` | The second string to compare. |





**Returns:** `true` if the strings are identical, `false` otherwise.



**Since:** Haiku R1


References [Compare()](classBCollator.md#a3af1c9ae97365dab40d0d43a4fd11d5c).

---

### `GetSortKey()`

```cpp
status_t BCollator::GetSortKey(const char * string, BString * key)const
```

Compute the sortkey of a *string*. 


const 


The sortkey is a modified version of the input *string* that you can use to perform faster comparisons with other sortkeys using strcmp() or a similar comparison function. If you need to compare one string with other many times, storing the sortkey will allow you to perform the comparisons faster.


Parameters

| Parameter | Description |
| :--- | :--- |
| `string` | String from which to compute the sortkey. |
| `key` | The resulting sortkey. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | if everything went well. |
| B_ERROR | if an error occurred generating the sortkey. |





**Since:** Haiku R1

---

### `Greater()`

```cpp
bool BCollator::Greater(const char * s1, const char * s2)const
```

Determine if a string is greater than another. 


const 



> [!NOTE]
> !Greater(s1, s2) is the same as GreaterOrEqual(s2, s1). This means there is no need for Lesser(s1, s2) and LesserOrEqual(s1, s2) methods.


Parameters

| Parameter | Description |
| :--- | :--- |
| `s1` | The first string to compare. |
| `s2` | The second string to compare. |





**Returns:** `true` if s1 is greater than, but not equal to, s2.



**Since:** Haiku R1


References [Compare()](classBCollator.md#a3af1c9ae97365dab40d0d43a4fd11d5c).

---

### `GreaterOrEqual()`

```cpp
bool BCollator::GreaterOrEqual(const char * s1, const char * s2)const
```

Determines if one string is greater than another. 


const 



> [!NOTE]
> !GreaterOrEqual(s1, s2) is the same as Greater(s2, s1).


Parameters

| Parameter | Description |
| :--- | :--- |
| `s1` | The first string to compare. |
| `s2` | The second string to compare. |





**Returns:** `true` if s1 is greater or equal than s2.



**Since:** Haiku R1


References [Compare()](classBCollator.md#a3af1c9ae97365dab40d0d43a4fd11d5c).

---

### `IgnorePunctuation()`

```cpp
bool BCollator::IgnorePunctuation()const
```

Gets the behavior of the collator with regards to punctuation. 



**Returns:** `true` if the collator will take punctuation into account when sorting, `false` otherwise.



**Since:** Haiku R1

---

### `Instantiate()`

```cpp
static BArchivable * BCollator::Instantiate(BMessage * archive)
```

Unarchive the collator. 


This method allows you to restore a collator that you previously archived.


Parameters

| Parameter | Description |
| :--- | :--- |
| `archive` | The message to restore the collator from. |





**Returns:** A pointer to a [BArchivable](../support_kit/classBArchivable.md) object containing the [BCollator](classBCollator.md) or `NULL` if an error occurred restoring the *archive*.



**Since:** Haiku R1

---

### `operator=()`

```cpp
Bcollator & BCollator::operator=(const BCollator & other)
```

Assignment operator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | the [BCollator](classBCollator.md) object to assign from. |





**Since:** Haiku R1

---

### `SetIgnorePunctuation()`

```cpp
void BCollator::SetIgnorePunctuation(bool ignore)
```

Enable or disable punctuation handling. 


This function enables or disables the handling of punctuation.


Parameters

| Parameter | Description |
| :--- | :--- |
| `ignore` | Whether or not punctuation should be ignored. |





**Since:** Haiku R1

---

### `SetNumericSorting()`

```cpp
void BCollator::SetNumericSorting(bool ignore)
```

Enable or disable numeric order sorting. 


Numeric sorting enables the collator to identify strings of digits as numbers, and sort them in ascending number. For example, the string "123" is sorted after "234". Numbers and other characters can be mixed in the same string.



**Since:** Haiku R1

---

### `SetStrength()`

```cpp
void BCollator::SetStrength(int8 strength)const
```

Set the *strength* of the collator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `strength` | The collator class provide four level of *strength*.  * `B_COLLATE_PRIMARY` doesn't differentiate e from é,  * `B_COLLATE_SECONDARY` takes letter accents into account,  * `B_COLLATE_TERTIARY` is case sensitive,  * `B_COLLATE_QUATERNARY` is very strict. Most of the time you shouldn't need to go this far. |





**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBCollator.html).
