---
name: BTimeZone
type: class
kit: locale_kit
brief: "Defines the time zone API which specifies a time zone, allows you to display it to the user, and converts between GMT and local time"
source: haiku-book
---

# BTimeZone Class
**Kit/Group:** [Locale Kit](../locale_kit/group__locale.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Defines the time zone API which specifies a time zone, allows you to display it to the user, and converts between GMT and local time. 


When displaying the name of a time zone to the user, use the display name, not the time zone ID. The display name can be retrieved by the [BTimeZone::Name()](classBTimeZone.md#a988bd9a819880a15462246e2e7435c24), [BTimeZone::DaylightSavingName()](classBTimeZone.md#a4211ad141695d1cec33bae275b86ef87), [BTimeZone::ShortName()](classBTimeZone.md#ab3bc66c89dc42927deaedea4f7902744), and [BTimeZone::ShortDaylightSavingName()](classBTimeZone.md#a29c05bd4b8566a57287a51e14ceb0896) methods.



* The standard name looks like "Pacific Standard Time".

* The daylight savings time name looks like "Pacific Daylight Time".

* The short name looks like either "PST" or "PDT" depending on whether the standard or daylight savings time name is requested.




**See also:** [BTimeZone::ID()](classBTimeZone.md#afa38541edc05b13c25618f1bca75c6b0)



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BTimeZone](#aa5e7be09a61fd87932b574e07654d37a) (const BTimeZone &other) — Copy constructor.
* [BTimeZone](#a204a3fd38703d6bbc5cd938559206d33) (const char *zoneID=NULL, const BLanguage *language=NULL) — Construct a timezone from its zoneID and language.
* `const BString &` [DaylightSavingName](#a4211ad141695d1cec33bae275b86ef87) () const — Returns the localized daylight savings name of the time zone, for example "Pacific Daylight Time".
* `const BString &` [ID](#afa38541edc05b13c25618f1bca75c6b0) () const — Returns the ID of the time zone as a BString, for example, "America/Los_Angeles".
* `status_t` [InitCheck](#a330d847ad26653124a75e77557e91add) () const — Returns whether or not the constructor initialized the time zone.
* `const BString &` [Name](#a988bd9a819880a15462246e2e7435c24) () const — Returns the localized name of the time zone, for example "Pacific Standard Time".
* `int` [OffsetFromGMT](#ab9665fed389083b2146ea0ac01b5dc72) () const — Returns the offset, in milliseconds, between the standard time of a time zone and GMT.
* `BTimeZone &` [operator=](#aacbd8827aaac526be302eef3052c9b47) (const BTimeZone &source) — Assignment operator.
* `status_t` [SetTo](#a455608d35df365b966ee5904e77a1626) (const char *zoneID, const BLanguage *language=NULL) — Set the BTimeZone object to use a different time zone.
* `const BString &` [ShortDaylightSavingName](#a29c05bd4b8566a57287a51e14ceb0896) () const — Returns the localized daylight savings name of the time zone, for example "PDT".
* `const BString &` [ShortName](#ab3bc66c89dc42927deaedea4f7902744) () const — Returns the short name of the timezone, in the user's locale, for example "PST".
* `bool` [SupportsDaylightSaving](#a8b17bce378b46687db53bf7b48298316) () const — Returns whether or not if the time zone support daylight saving time.

## Detailed Member Documentation

### `BTimeZone()`

```cpp
BTimeZone::BTimeZone(const char * zoneID = NULL, const BLanguage * language = NULL)
```

Construct a timezone from its *zoneID* and *language*. 


The constructor only allows you to construct a timezone if you already know its code. If you don't know the code, you can instead go through the [BCountry](classBCountry.md) class which can enumerate all timezones in a country, or use the [BLocaleRoster](classBLocaleRoster.md), which knows the timezone selected by the user.


Parameters

| Parameter | Description |
| :--- | :--- |
| `zoneID` | A time zone ID, for example, "America/Los_Angeles". This ID is used to call up a specific real-world time zone. |
| `language` | The *language* to use when displaying the time zone. |





**Since:** Haiku R1

---

### `BTimeZone()`

```cpp
BTimeZone::BTimeZone(const BTimeZone & other)
```

Copy constructor. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The [BTimeZone](classBTimeZone.md) object to copy from. |





**Since:** Haiku R1

---

### `DaylightSavingName()`

```cpp
const BString & BTimeZone::DaylightSavingName()const
```

Returns the localized daylight savings name of the time zone, for example "Pacific Daylight Time". 



**Since:** Haiku R1

---

### `ID()`

```cpp
const BString & BTimeZone::ID()const
```

Returns the ID of the time zone as a [BString](../support_kit/classBString.md), for example, "America/Los_Angeles". 


When displaying the name of a time zone to the user, use the display name, not the time zone ID.



**Since:** Haiku R1

---

### `InitCheck()`

```cpp
status_t BTimeZone::InitCheck()const
```

Returns whether or not the constructor initialized the time zone. 



**Returns:** `true` if [BTimeZone](classBTimeZone.md) object was initialized successfully, `false` if there was an error initializing the [BTimeZone](classBTimeZone.md), for instance if the constructor or [SetTo()](classBTimeZone.md#a455608d35df365b966ee5904e77a1626) was called with an invalid timezone ID.



**Since:** Haiku R1

---

### `Name()`

```cpp
const BString & BTimeZone::Name()const
```

Returns the localized name of the time zone, for example "Pacific Standard Time". 


Use this method to display the time zone's name to the user.



**Since:** Haiku R1

---

### `OffsetFromGMT()`

```cpp
int BTimeZone::OffsetFromGMT()const
```

Returns the offset, in milliseconds, between the standard time of a time zone and GMT. 


Positive raw offsets are east of Greenwich, negative offsets are west of Greenwich.



**Returns:** The offset as a number of milliseconds from GMT, positive or negative.



**Since:** Haiku R1

---

### `operator=()`

```cpp
BTimeZone & BTimeZone::operator=(const BTimeZone & source)
```

Assignment operator. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `source` | The [BTimeZone](classBTimeZone.md) object to copy from. |





**Since:** Haiku R1

---

### `SetTo()`

```cpp
status_t BTimeZone::SetTo(const char * zoneCode, const BLanguage * language = NULL)
```

Set the [BTimeZone](classBTimeZone.md) object to use a different time zone. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `zoneCode` | The time zone ID to use, for example "America/Los_Angeles". |
| `language` | The *language* to use when displaying the time zone. |





**Returns:** `true` if time zone was set successfully, `false` if there was an error setting the time zone, for instance if this method was called using an invalid *zoneCode*.



**Since:** Haiku R1

---

### `ShortDaylightSavingName()`

```cpp
const BString & BTimeZone::ShortDaylightSavingName()const
```

Returns the localized daylight savings name of the time zone, for example "PDT". 



**Since:** Haiku R1

---

### `ShortName()`

```cpp
const BString & BTimeZone::ShortName()const
```

Returns the short name of the timezone, in the user's locale, for example "PST". 



**Since:** Haiku R1

---

### `SupportsDaylightSaving()`

```cpp
bool BTimeZone::SupportsDaylightSaving()const
```

Returns whether or not if the time zone support daylight saving time. 



**Returns:** `true` if the time zone supports daylight savings time, `false` otherwise.



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBTimeZone.html).
