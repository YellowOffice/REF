---
name: BFileGameSound
type: class
kit: game_kit
brief: "Playback audio from a sound file on disk"
source: haiku-book
---

# BFileGameSound Class
**Kit/Group:** [Game Kit](../game_kit/group__game.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Playback audio from a sound file on disk. 



**Since:** BeOS R5

## Member List

### Public Member Functions

* [BFileGameSound](#a56d4513b16fb58504ba017955ef208da) (BDataIO *data, bool looping=true, BGameSoundDevice *device=NULL) — Creates and initializes a BFileGameSound object from a BDataIO allowing you to play the specified sound data.
* [BFileGameSound](#a80fc5bda3aa7c454e0e4d0a4bf4a4c3e) (const char *file, bool looping=true, BGameSoundDevice *device=NULL) — Creates and initializes a BFileGameSound object from a file path allowing you to play the specified sound file.
* [BFileGameSound](#a32e07ec8a0a84570dcda8b1089241dc0) (const entry_ref *file, bool looping=true, BGameSoundDevice *device=NULL) — Creates and initializes a BFileGameSound object from an entry_ref allowing you to play the specified sound file.
* `virtual` [~BFileGameSound](#a8342c8f38dd256aaedd6770477584466) () — Destroys the BFileGameSound object.
* `virtual BGameSound *` [Clone](#aa3ad8d99f8cd7d642efea9e307f9c8f4) () const — Not implemented, always returns NULL.
* `virtual void` [FillBuffer](#adf02974b45c34d1ac78d820dfdcac7cb) (void *buffer, size_t byteCount) — Fill a buffer with sound data.
* `int32` [IsPaused](#acb5d4b27588ee1999df9fc806ff53499) () — Returns the current playback status.
* `status_t` [Preload](#a0c7bfa46aee6d2a5fd51130c489b96f0) () — Preload the sound file into memory so that playback won't be delayed.
* `virtual status_t` [SetPaused](#a4b695291af4641350f2410eb93291e04) (bool isPaused, bigtime_t rampTime) — Pauses playback if isPaused is true or resumes play if isPaused is false.
* `virtual status_t` [StartPlaying](#a7f6889ec5302c0becaec0a694e7358a4) () — Plays the sound file.
* `virtual status_t` [StopPlaying](#aad7e89669e17be574d347bad4ffd013b) () — Stops playback of the sound file.

## Detailed Member Documentation

### `BFileGameSound()`

```cpp
BFileGameSound::BFileGameSound(const entry_ref * file, bool looping = true, BGameSoundDevice * device = NULL)
```

Creates and initializes a [BFileGameSound](classBFileGameSound.md) object from an `entry_ref` allowing you to play the specified sound file. 


If *looping* is `true`, the sound automatically replays from the beginning once the end is reached. This is useful for playing background music in a loop.


You can specify the sound device to use by setting the *device* parameter. Setting *device* to `NULL` uses the default sound device.


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | The entry ref pointing to the sound file on disk. |
| `looping` | Whether or not to repeat the sound in a loop. |
| `device` | The sound device to use to play the sound, use `NULL` for default. |





**Since:** BeOS R5

---

### `BFileGameSound()`

```cpp
BFileGameSound::BFileGameSound(const char * file, bool looping = true, BGameSoundDevice * device = NULL)
```

Creates and initializes a [BFileGameSound](classBFileGameSound.md) object from a file path allowing you to play the specified sound file. 


If *looping* is `true`, the sound automatically replays from the beginning once the end is reached. This is useful for playing background music in a loop.


You can specify the sound device to use by setting the *device* parameter. Setting *device* to `NULL` uses the default sound device.


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | The path of the sound file on disk. |
| `looping` | Whether or not to repeat the sound in a loop. |
| `device` | The sound device to use to play the sound, use `NULL` for default. |





**Since:** BeOS R5

---

### `BFileGameSound()`

```cpp
BFileGameSound::BFileGameSound(BDataIO * source, bool looping = true, BGameSoundDevice * device = NULL)
```

Creates and initializes a [BFileGameSound](classBFileGameSound.md) object from a [BDataIO](../support_kit/classBDataIO.md) allowing you to play the specified sound data. 


This allows using [BFileGameSound](classBFileGameSound.md) with [BFile](../storage_kit/classBFile.md) as well as non-file based storage ([BMemoryIO](../support_kit/classBMemoryIO.md), etc).


If *looping* is `true`, the sound automatically replays from the beginning once the end is reached. This is useful for playing background music in a loop.


You can specify the sound device to use by setting the *device* parameter. Setting *device* to `NULL` uses the default sound device.


Parameters

| Parameter | Description |
| :--- | :--- |
| `source` | The place to get the data from. |
| `looping` | Whether or not to repeat the sound in a loop. |
| `device` | The sound device to use to play the sound, use `NULL` for default. |





**Since:** Haiku R1

---

### `~BFileGameSound()`

```cpp
BFileGameSound::~BFileGameSound()
```

Destroys the [BFileGameSound](classBFileGameSound.md) object. 



**Since:** BeOS R5

---

### `Clone()`

```cpp
BGameSound * BFileGameSound::Clone()const
```

Not implemented, always returns `NULL`. 



**Since:** BeOS R5


Implements [BGameSound](classBGameSound.md#a05ef6d0734e04c6cc586d42fdf92b946).

---

### `FillBuffer()`

```cpp
void BFileGameSound::FillBuffer(void * inBuffer, size_t inByteCount)
```

Fill a buffer with sound data. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `inBuffer` | The buffer to fill. |
| `inByteCount` | The number of bytes to fill buffer with. |





**Since:** BeOS R5

---

### `IsPaused()`

```cpp
int32 BFileGameSound::IsPaused()
```

Returns the current playback status. 



**Returns:** An integer indicating the current playback status.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_NOT_PAUSED | Sound is playing. |
| B_PAUSE_IN_PROGRESS | The sound is transitioning to or from a paused state. |
| B_PAUSED | Sound is paused. |





**Since:** BeOS R5

---

### `Preload()`

```cpp
status_t BFileGameSound::Preload()
```

Preload the sound file into memory so that playback won't be delayed. 



**Returns:** A status code, `B_OK` on success or an error code if we were unable to communicate with the sound port.



**Since:** BeOS R5

---

### `SetPaused()`

```cpp
status_t BFileGameSound::SetPaused(bool isPaused, bigtime_t rampTime)
```

Pauses playback if *isPaused* is `true` or resumes play if *isPaused* is `false`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `isPaused` | `true` to pause playback, `false` to resume playback. |
| `rampTime` | Determines how long the change in playback state should take to complete in microseconds. Set to 0 for an instantaneous change. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The playback state was updated. |
| EALREADY | Already in the requested playback state. |





**Since:** BeOS R5

---

### `StartPlaying()`

```cpp
status_t BFileGameSound::StartPlaying()
```

Plays the sound file. 



**Returns:** A status code, `B_OK` on success or an error code on error.



**Since:** BeOS R5


Reimplemented from [BGameSound](classBGameSound.md#ab596b7535d67a2128dd9559b4ddfa86b).

---

### `StopPlaying()`

```cpp
status_t BFileGameSound::StopPlaying()
```

Stops playback of the sound file. 



**Returns:** A status code, `B_OK` on success or an error code on error.



**Since:** BeOS R5


Reimplemented from [BGameSound](classBGameSound.md#a7861ba7d73251c11208d51f5a5eccf2b).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBFileGameSound.html).
