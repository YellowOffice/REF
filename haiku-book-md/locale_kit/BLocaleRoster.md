---
name: BLocaleRoster
type: class
kit: locale_kit
brief: "Main class for accessing the Locale Kit data"
source: haiku-book
---

# BLocaleRoster Class
**Kit/Group:** [Locale Kit](../locale_kit/group__locale.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Main class for accessing the Locale Kit data. 


The Locale Roster is the central part of the locale kit. It is a global object (`be_locale_roster`) storing all the useful locale data. Other classes from the Locale Kit can be constructed on their own, but only the Locale Roster allows you to do so while taking account of the user's locale settings.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [~BLocaleRoster](#ad6672b698c844bac6a6b663a24a123c4) () — Destructor. Does nothing.
* `status_t` [GetAvailableCatalogs](#a63549adde7995fec7acc00743aa8ba93) (BMessage *message, const char *sigPattern=NULL, const char *langPattern=NULL, int32 fingerprint=0) const — Get the available locales and catalogs.
* `status_t` [GetAvailableCountries](#a6df1035b9449247552c4d1be2c4b74c7) (BMessage *timeZones) const — Fills in the passed in message with one or more 'country' string fields, containing the (ISO-639) code of each country.
* `status_t` [GetAvailableLanguages](#ae5927ab7e48d8001233f853da7442bfe) (BMessage *message) const — Fills message with 'language'-fields containing the language ID(s) of all available languages.
* `status_t` [GetAvailableTimeZones](#a89336fc6c6975ea380466ad983bbc540) (BMessage *timeZones) const — Fills in the passed in timeZones message with all time zone strings for the locale.
* `status_t` [GetAvailableTimeZonesForCountry](#a62c4502b121114bb5e96b588e071d712) (BMessage *message, const char *countryCode) const — Fills in the passed in timeZones message with one or more time zone strings containing the time zones for the country specified by countryCode for the locale.
* `status_t` [GetDefaultTimeZone](#a7cb5f911107993a9c4816b52e9221572) (BTimeZone *timezone) const — Get the default timezone.
* `status_t` [GetFlagIconForCountry](#a683b5acbb28931d4ef5306c2085b08e4) (BBitmap *flagIcon, const char *countryCode) — Sets flagIcon to the flag for the passed in countryCode.
* `status_t` [GetFlagIconForLanguage](#a7878ec917e8d8d9733b7a6ff06218122) (BBitmap *flagIcon, const char *languageCode) — Sets flagIcon to the flag for the passed in languageCode.
* `status_t` [GetLanguage](#aef01ac9c948bbf836464c7bf79195e2e) (const char *languageCode, BLanguage **_language) const — Instantiate a language from its code.
* `status_t` [GetLocalizedFileName](#a2fd434b841e208a139510c14679588b9) (BString &localizedFileName, const entry_ref &ref, bool traverse=false) — Looks up a localized filename from a catalog.
* `status_t` [GetPreferredLanguages](#a8c0de7c09e1be6c30590a69c61753bf1) (BMessage *message) const — Return the list of user preferred languages.
* `bool` [IsFilesystemTranslationPreferred](#a967c86a687870d0fe59054dbfcce2453) () const — Returns whether or not filesystem translation is preferred.
* `status_t` [Refresh](#a127b816155049b4a96a653835a35da97) () — Refreshes the BLocalRoster.

### Static Public Member Functions

* `static BLocaleRoster *` [Default](#a72133385bc675be3d92da85bf564049b) () — Returns default BLocalRoster.

### Protected Member Functions

* [BLocaleRoster](#a1db4296b22fe68475894eea78a00c313) () — Constructor. Does nothing.

## Detailed Member Documentation

### `~BLocaleRoster()`

```cpp
BLocaleRoster::~BLocaleRoster()
```

Destructor. Does nothing. 



**Since:** Haiku R1

---

### `BLocaleRoster()`

```cpp
BLocaleRoster::BLocaleRoster()
```

Constructor. Does nothing. 



**Since:** Haiku R1

---

### `Default()`

```cpp
BLocaleRoster * BLocaleRoster::Default()
```

Returns default BLocalRoster. 



**Since:** Haiku R1

---

### `GetAvailableCatalogs()`

```cpp
status_t BLocaleRoster::GetAvailableCatalogs(BMessage * languageList, const char * sigPattern = NULL, const char * langPattern = NULL, int32 fingerprint = 0)const
```

Get the available locales and catalogs. 


Fills the passed *languageList* message with one or more 'locale' string fields containing the locale names.


The optional parameters can be used to filter the list and only get the locales for which a catalog is available for the given app (sigPattern, fingerprint), or the locales with a given language.



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went well. |
| B_BAD_VALUE | A `NULL` *languageList* message was passed in. |
| B_ERROR | Error locking the default RosterData. |





**Since:** Haiku R1

---

### `GetAvailableCountries()`

```cpp
status_t BLocaleRoster::GetAvailableCountries(BMessage * message)const
```

Fills in the passed in *message* with one or more 'country' string fields, containing the (ISO-639) code of each country. 



**Since:** Haiku R1

---

### `GetAvailableLanguages()`

```cpp
status_t BLocaleRoster::GetAvailableLanguages(BMessage * message)const
```

Fills `message` with 'language'-fields containing the language ID(s) of all available languages. 



**Since:** Haiku R1

---

### `GetAvailableTimeZones()`

```cpp
status_t BLocaleRoster::GetAvailableTimeZones(BMessage * timeZones)const
```

Fills in the passed in *timeZones* message with all time zone strings for the locale. 



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went well. |
| B_BAD_VALUE | A `NULL` *timeZones* message was passed in. |
| B_ERROR | An error occurred trying to retrieve the localized time zone strings. |





**Since:** Haiku R1

---

### `GetAvailableTimeZonesForCountry()`

```cpp
status_t BLocaleRoster::GetAvailableTimeZonesForCountry(BMessage * timeZones, const char * countryCode)const
```

Fills in the passed in *timeZones* message with one or more time zone strings containing the time zones for the country specified by *countryCode* for the locale. 



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went well. |
| B_BAD_VALUE | A `NULL` *timeZones* message was passed in. |
| B_ERROR | An error occurred trying to retrieve the localized time zones most likely due to an invalid *countryCode*. |





**Since:** Haiku R1

---

### `GetDefaultTimeZone()`

```cpp
status_t BLocaleRoster::GetDefaultTimeZone(BTimeZone * timezone)const
```

Get the default timezone. 



**Since:** Haiku R1

---

### `GetFlagIconForCountry()`

```cpp
status_t BLocaleRoster::GetFlagIconForCountry(BBitmap * flagIcon, const char * countryCode)
```

Sets *flagIcon* to the flag for the passed in *countryCode*. 



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went well. |
| B_BAD_VALUE | A `NULL` or invalid *countryCode* was passed in. |
| B_ERROR | Error locking the default RosterData. |
| B_NAME_NOT_FOUND | The flag could not be found for the *countryCode*. |





**Since:** Haiku R1

---

### `GetFlagIconForLanguage()`

```cpp
status_t BLocaleRoster::GetFlagIconForLanguage(BBitmap * flagIcon, const char * languageCode)
```

Sets *flagIcon* to the flag for the passed in *languageCode*. 


If a flag could not be located for the passed in *languageCode* then [GetFlagIconForLanguage()](classBLocaleRoster.md#a7878ec917e8d8d9733b7a6ff06218122) attempts to locate the default country's flag for the *languageCode* instead. The default country flag for a language is usually set to the country of the languages origin such as Germany for German or Spain for Spanish.



**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Everything went well. |
| B_BAD_VALUE | A `NULL` or invalid *languageCode* was passed in. |
| B_ERROR | Error locking the default RosterData. |
| B_NAME_NOT_FOUND | The flag could not be found for the default country's flag for the *languageCode*. |





**Since:** Haiku R1

---

### `GetLanguage()`

```cpp
status_t BLocaleRoster::GetLanguage(const char * languagecode, BLanguage ** _language)const
```

Instantiate a language from its code. 



**Since:** Haiku R1

---

### `GetLocalizedFileName()`

```cpp
status_t BLocaleRoster::GetLocalizedFileName(BString & localizedFileName, const entry_ref & ref, bool traverse = false)
```

Looks up a localized filename from a catalog. 


Attribute format: "signature:context:string" (no colon in any of signature, context and string)


Lookup is done for the top preferred language only. Lookup fails if a comment is present in the catalog entry.


Parameters

| Parameter | Description |
| :--- | :--- |
| `localizedFileName` | A pre-allocated [BString](../support_kit/classBString.md) object for the result of the lookup. |
| `ref` | An [entry_ref](../storage_kit/structentry__ref.md) with an attribute holding data for catalog lookup. |
| `traverse` | Determines if symlinks should be traversed. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | success |
| B_ENTRY_NOT_FOUND | failure. Attribute not found, entry not found in catalog, etc. |





**Since:** Haiku R1

---

### `GetPreferredLanguages()`

```cpp
status_t BLocaleRoster::GetPreferredLanguages(BMessage * message)const
```

Return the list of user preferred languages. 


This function fills in the given message with one or more language string fields. They constitute the ordered list of user-selected languages to use for string translation.



**Since:** Haiku R1

---

### `IsFilesystemTranslationPreferred()`

```cpp
bool BLocaleRoster::IsFilesystemTranslationPreferred()const
```

Returns whether or not filesystem translation is preferred. 



**Returns:** `B_ERROR` if there was an error locking the default RosterData.



**Since:** Haiku R1

---

### `Refresh()`

```cpp
status_t BLocaleRoster::Refresh()
```

Refreshes the BLocalRoster. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBLocaleRoster.html).
