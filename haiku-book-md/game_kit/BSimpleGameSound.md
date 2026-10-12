---
name: BSimpleGameSound
type: class
kit: game_kit
brief: "BSimpleGameSound represents a simple sound effect that remains in memory"
source: haiku-book
---

# BSimpleGameSound Class
**Kit/Group:** [Game Kit](../game_kit/group__game.md)

## Description

[BSimpleGameSound](classBSimpleGameSound.md) represents a simple sound effect that remains in memory. 


To use [BSimpleGameSound](classBSimpleGameSound.md) is enough to create an instance of it and then call [StartPlaying()](classBGameSound.md#ab596b7535d67a2128dd9559b4ddfa86b) to start the playback:



```cpp
const char* filename = ... ;
BSimpleGameSound* sound = new BGameSound(filename);
 
sound->StartPlaying();
```

The *device* parameter in all of the constructors is currently unused and has to be defined as `NULL`. Its base class [BGameSound](classBGameSound.md) takes care of that by initializing the default sound device.



**Since:** BeOS R4.5

## Member List

### Public Member Functions

* [BSimpleGameSound](#a1731002e3bb741d694927b298b060478) (const BSimpleGameSound &other) — Copy constructor.
* [BSimpleGameSound](#a0d92666217e67280053347483ea82979) (const char *file, BGameSoundDevice *device=NULL) — Creates and initializes a BSimpleGameSound object from a sound file path and prepares it to be ready for playback.
* [BSimpleGameSound](#ae1e3e3b9da63830d7c83833b4da6e31e) (const entry_ref *file, BGameSoundDevice *device=NULL) — Creates and initializes a BSimpleGameSound object from a sound file's entry_ref and prepares it to be ready for playback.
* [BSimpleGameSound](#aae14a7c07f91f2c34f41626afe002c94) (const void *data, size_t frameCount, const gs_audio_format *format, BGameSoundDevice *device=NULL) — Creates and initializes a BSimpleGameSound object from a data buffer in memory of frameCount frames in a format.
* `virtual` [~BSimpleGameSound](#a76a0693935d6a145bed2f561d6b694b6) () — Frees all resources associated with the object.
* `virtual BGameSound *` [Clone](#a0b0a3d7b7d77051e02a442231da969bb) () const — Returns a copy of this BSimpleGameSound object.
* `bool` [IsLooping](#a34f453b26be17bf4998b04ba0c162623) () const — Returns whether looping is enabled or not.
* `status_t` [SetIsLooping](#a312af48b11115ededa427e94a435b623) (bool looping) — Enables or disables the playback looping of the sound.
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

### `BSimpleGameSound()`

```cpp
BSimpleGameSound::BSimpleGameSound(const entry_ref * file, BGameSoundDevice * device = NULL)
```

Creates and initializes a [BSimpleGameSound](classBSimpleGameSound.md) object from a sound file's [entry_ref](../storage_kit/structentry__ref.md) and prepares it to be ready for playback. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | An [entry_ref](../storage_kit/structentry__ref.md) reference of the sound file. |
| `device` | The sound device where the sound should be played. Setting it to `NULL` makes it to use the default sound device. |





**Since:** BeOS R4.5

---

### `BSimpleGameSound()`

```cpp
BSimpleGameSound::BSimpleGameSound(const char * file, BGameSoundDevice * device = NULL)
```

Creates and initializes a [BSimpleGameSound](classBSimpleGameSound.md) object from a sound file path and prepares it to be ready for playback. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `file` | The filename path of the sound file. |
| `device` | The sound device where the sound should be played. Setting it to `NULL` makes it to use the default sound device. |





**Since:** BeOS R5

---

### `BSimpleGameSound()`

```cpp
BSimpleGameSound::BSimpleGameSound(const void * data, size_t frameCount, const gs_audio_format * format, BGameSoundDevice * device = NULL)
```

Creates and initializes a [BSimpleGameSound](classBSimpleGameSound.md) object from a *data* buffer in memory of *frameCount* frames in a *format*. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | A pointer to the sound data in memory. |
| `frameCount` | The number of frames in the sound data. |
| `format` | The format of the sound data. |
| `device` | The sound device where the sound should be played. Setting it to `NULL` makes it to use the default sound device. |





**Since:** BeOS R4.5

---

### `BSimpleGameSound()`

```cpp
BSimpleGameSound::BSimpleGameSound(const BSimpleGameSound & other)
```

Copy constructor. 


It creates a deep copy of the sound data in *other*.


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The other [BSimpleGameSound](classBSimpleGameSound.md) object from where to initialize this instance. |





**Since:** BeOS R4.5

---

### `~BSimpleGameSound()`

```cpp
BSimpleGameSound::~BSimpleGameSound()
```

Frees all resources associated with the object. 



**Since:** BeOS R4.5

---

### `Clone()`

```cpp
BGameSound * BSimpleGameSound::Clone()const
```

Returns a copy of this [BSimpleGameSound](classBSimpleGameSound.md) object. 



**Since:** BeOS R4.5


Implements [BGameSound](classBGameSound.md#a05ef6d0734e04c6cc586d42fdf92b946).

---

### `IsLooping()`

```cpp
bool BSimpleGameSound::IsLooping()const
```

Returns whether looping is enabled or not. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | Looping is currently enabled. |
| false | Looping is currently disabled. |





**See also:** [SetIsLooping()](classBSimpleGameSound.md#a312af48b11115ededa427e94a435b623)



**Since:** BeOS R4.5

---

### `SetIsLooping()`

```cpp
status_t BSimpleGameSound::SetIsLooping(bool looping)
```

Enables or disables the playback looping of the sound. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `looping` | If it is `true` turns on looping, and if it is `false` turns it off. |




Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The looping was toggled on or off successfully. |
| B_ERROR | There was an internal error trying to find the sound data. |





**See also:** [IsLooping()](classBSimpleGameSound.md#a34f453b26be17bf4998b04ba0c162623)



**Since:** BeOS R4.5

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBSimpleGameSound.html).
