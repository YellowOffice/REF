---
name: BGameSound
type: class
kit: game_kit
brief: "BGameSound is the base class used in the other sound classes in the kit"
source: haiku-book
---

# BGameSound Class
**Kit/Group:** [Game Kit](../game_kit/group__game.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

[BGameSound](classBGameSound.md) is the base class used in the other sound classes in the kit. 


This class is not meant to be used directly. Any of the derived classes should be used instead.



**Since:** BeOS R4.5

## Member List

### Public Member Functions

* [BGameSound](#acddea7386d9096f233e5af4ee4e85689) (BGameSoundDevice *device=NULL) — Creates a BGameSound object.
* `virtual` [~BGameSound](#aaedf197039eb48ce026b4c9d296a5e04) () — Destroys the BGameSound object and frees the memory it uses.
* `virtual BGameSound *` [Clone](#a05ef6d0734e04c6cc586d42fdf92b946) () const =0 — Pure virtual method to create a copy of the BGameSound object.
* `BGameSoundDevice *` [Device](#adc2e67dc82d86b529ab843c7fc74de60) () const — Returns a pointer to the sound playback device.
* `const gs_audio_format &` [Format](#a67580a90f699c740e4f7ac09abbf0e86) () const — Returns a gs_audio_format struct instance with the format of the sound associated with the BGameSound object.
* `gs_id` [ID](#aa125786bc9af021d8edef146a930c706) () const — Returns the identifier of the sound associated with the BGameSound object.
* `status_t` [InitCheck](#ae5bc47926c79441500e37ca5cb556daf) () const — Verifies if the BGameSound object was successfully initialized.
* `virtual status_t` [StartPlaying](#ab596b7535d67a2128dd9559b4ddfa86b) () — Plays the sound in the playback device.
* `virtual bool` [IsPlaying](#a8d687581c8014d37442743d5d8bb39d4) () — Checks whether the sound is being played or not in the playback device.
* `virtual status_t` [StopPlaying](#a7861ba7d73251c11208d51f5a5eccf2b) () — Stops the playback of a sound currently playing.
* `status_t` [SetGain](#a9c0b80aa71e9c562c86c9fad6bb1c468) (float gain, bigtime_t duration=0) — Sets the gain of the sound, that is, the amount of amplification of the input signal.
* `status_t` [SetPan](#ae0cdb0db78ba012cccdb8249e9dfc580) (float pan, bigtime_t duration=0) — Sets the panning of the sound, that is, the distribution of the audio signal anywhere in the stereophonic sound field.
* `float` [Gain](#a9890be6265e7061be9df6ea671f6724c) () — Retrieves the current level of gain of the sound.
* `float` [Pan](#abed278ebeb1fc1606903d9e58b906536) () — Retrieves the current value of panning of the sound.
* `virtual status_t` [SetAttributes](#af6c6d9ca73e25eb44fb88727db45dc2a) (gs_attribute *attributes, size_t attributeCount) — Sets the attributes for the current sound.
* `virtual status_t` [GetAttributes](#a99a59ab9265646f2bf75decce2259c07) (gs_attribute *attributes, size_t attributeCount) — Retrieves the attributes of the current sound.

## Detailed Member Documentation

### `BGameSound()`

```cpp
BGameSound::BGameSound(BGameSoundDevice * device = NULL)
```

Creates a [BGameSound](classBGameSound.md) object. 


The *device* parameter is currently unused and has to be defined as `NULL`. Currently the class itself will retrieve the default device.


Parameters

| Parameter | Description |
| :--- | :--- |
| `device` | The sound device to be used. |





**Since:** BeOS R4.5

---

### `~BGameSound()`

```cpp
BGameSound::~BGameSound()
```

Destroys the [BGameSound](classBGameSound.md) object and frees the memory it uses. 


It releases any buffer connected to the game sound device and then releases the device itself.



**Since:** BeOS R4.5

---

### `Clone()`

```cpp
BGameSound * BGameSound::Clone()const
```

Pure virtual method to create a copy of the [BGameSound](classBGameSound.md) object. 



**Since:** BeOS R4.5


Implemented in [BFileGameSound](classBFileGameSound.md#aa3ad8d99f8cd7d642efea9e307f9c8f4), and [BSimpleGameSound](classBSimpleGameSound.md#a0b0a3d7b7d77051e02a442231da969bb).

---

### `Device()`

```cpp
BGameSoundDevice * BGameSound::Device()const
```

Returns a pointer to the sound playback device. 



**Since:** BeOS R4.5

---

### `Format()`

```cpp
const gs_audio_format & BGameSound::Format()const
```

Returns a gs_audio_format struct instance with the format of the sound associated with the [BGameSound](classBGameSound.md) object. 



**Since:** BeOS R4.5

---

### `Gain()`

```cpp
float BGameSound::Gain()
```

Retrieves the current level of gain of the sound. 


If there is no sound initialized, by default it returns 0.0.



**Since:** BeOS R4.5

---

### `GetAttributes()`

```cpp
status_t BGameSound::GetAttributes(gs_attribute * attributes, size_t attributeCount)
```

Retrieves the attributes of the current sound. 


*attributes* is a pre-allocated array of gs_attribute structures, with the "attribute" field of each one pre-filled with the desired attribute's identifier, for which the information is going to be retrieved.


Parameters

| Parameter | Description |
| :--- | :--- |
| `attributes` | The gs_attribute list where to save the attributes. |
| `attributeCount` | The number of items in the *attributes* list. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The attributes were retrieved successfully. |
| B_ERROR | The [BGameSound](classBGameSound.md)'s sound was not initialized. |





**Since:** BeOS R4.5

---

### `ID()`

```cpp
gs_id BGameSound::ID()const
```

Returns the identifier of the sound associated with the [BGameSound](classBGameSound.md) object. 



**Since:** BeOS R4.5

---

### `InitCheck()`

```cpp
status_t BGameSound::InitCheck()const
```

Verifies if the [BGameSound](classBGameSound.md) object was successfully initialized. 



**Since:** BeOS R4.5

---

### `IsPlaying()`

```cpp
bool BGameSound::IsPlaying()
```

Checks whether the sound is being played or not in the playback device. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | The sound is currently being played. |
| false | The sound is not being played. |





**Since:** BeOS R4.5

---

### `Pan()`

```cpp
float BGameSound::Pan()
```

Retrieves the current value of panning of the sound. 


If there is no sound initialized, by default it returns 0.0.



**Since:** BeOS R4.5

---

### `SetAttributes()`

```cpp
status_t BGameSound::SetAttributes(gs_attribute * attributes, size_t attributeCount)
```

Sets the attributes for the current sound. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `attributes` | An array of the group of attributes to be applied to the sound. |
| `attributeCount` | The number of those attributes. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The attributes were applied successfully, or no error. |
| B_ERROR | The [BGameSound](classBGameSound.md)'s sound was not initialized. |
| others | Depending on the type of attribute. |





**Since:** BeOS R4.5

---

### `SetGain()`

```cpp
status_t BGameSound::SetGain(float gain, bigtime_t duration = 0)
```

Sets the gain of the sound, that is, the amount of amplification of the input signal. 


The *gain* is represented as a proportion, from 0.0 as the lowest to 1.0 as the highest level of gain.


A non-zero *duration* makes the transition from the current gain to the new gain take place over time in the amount set (in microseconds). If it is `0`, the change occurs immediately instead.


Parameters

| Parameter | Description |
| :--- | :--- |
| `gain` | Level of sound gain. |
| `duration` | Duration of transition from the older gain level to the newer level. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The gain was applied successfully. |
| B_BAD_VALUE | An out-of-bounds value for the gain was provided (not being 0.0 <= gain <= 1.0). |





**Since:** BeOS R4.5

---

### `SetPan()`

```cpp
status_t BGameSound::SetPan(float pan, bigtime_t duration = 0)
```

Sets the panning of the sound, that is, the distribution of the audio signal anywhere in the stereophonic sound field. 


A value of *pan* of -1.0 sets the sound at the most left side, 0.0 at the front, and 1.0 at the most right side.


A non-zero *duration* makes the transition from the current pan to the new pan take place over time in the amount set (in microseconds). If it is `0`, the change occurs immediately instead.


Parameters

| Parameter | Description |
| :--- | :--- |
| `pan` | Level of panning. |
| `duration` | Duration of transition from the older panning value to the newer value. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The pan was applied successfully. |
| B_ERROR | The [BGameSound](classBGameSound.md)'s sound was not initialized. |
| B_BAD_VALUE | An out-of-bounds value for the pan was provided (not being -1.0 <= pan <= 1.0). |





**Since:** BeOS R4.5

---

### `StartPlaying()`

```cpp
status_t BGameSound::StartPlaying()
```

Plays the sound in the playback device. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | Playback started successfully. |





**Since:** BeOS R4.5


Reimplemented in [BFileGameSound](classBFileGameSound.md#a7f6889ec5302c0becaec0a694e7358a4).

---

### `StopPlaying()`

```cpp
status_t BGameSound::StopPlaying()
```

Stops the playback of a sound currently playing. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The sound stopped playing. |





**Since:** BeOS R4.5


Reimplemented in [BFileGameSound](classBFileGameSound.md#aad7e89669e17be574d347bad4ffd013b).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBGameSound.html).
