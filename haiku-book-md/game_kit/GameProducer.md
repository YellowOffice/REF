---
name: GameProducer
type: class
kit: game_kit
brief: "A MediaKit producer node which mixes sound from the GameKit and sends them to the audio mixer"
source: haiku-book
---

# GameProducer Class
**Kit/Group:** [Game Kit](../game_kit/group__game.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A MediaKit producer node which mixes sound from the GameKit and sends them to the audio mixer. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [GameProducer](#aa9eb7fe088fb20d25feefa608335b71d) (GameSoundBuffer *object, const gs_audio_format *format) — Initializes the GameProducer with the passed in GameSoundBuffer and gs_audio_format.
* [~GameProducer](#a45e523240dba62dcb4c33e6341860d24) () — Destroys the GameProducer object and stops the BMediaEventLooper thread.
* `void` [AdditionalBufferRequested](#adb226cc677bd7c19524c307ff877c978) (const media_source &source, media_buffer_id prev_buffer, bigtime_t prev_time, const media_seek_tag *prev_tag) — Offline modes are not supported for now, does nothing.
* `BMediaAddOn *` [AddOn](#ac58080e502326c3251ad7114244092b6) (int32 *internal_id) const — Unimplemented.
* `void` [Connect](#a7e7d3a9577520c42454cdd5bc46b8abd) (status_t error, const media_source &source, const media_destination &destination, const media_format &format, char *ioName) — Connects to the output device.
* `void` [Disconnect](#ac590c0f891d7dd01ba819e5122d8e74b) (const media_source &what, const media_destination &where) — Disconnects from the output device.
* `status_t` [DisposeOutputCookie](#ae72595aea8d0d279b0db736490993b6d) (int32 cookie) — Does nothing because the cookie has no use as of yet.
* `void` [EnableOutput](#a20afcfb827ed3f5188d558d8af564b26) (const media_source &what, bool enabled, int32 *_deprecated_) — Enable or disable an output.
* `status_t` [FormatChangeRequested](#a46331fee7ce6db1ce7436a6a94217215) (const media_source &source, const media_destination &destination, media_format *io_format, int32 *_deprecated_) — We don't support any other formats, so we just reject any format changes.
* `status_t` [FormatProposal](#ad2c46ce0100e7892e534c00f472c2a0e) (const media_source &output, media_format *format) — Attempts to change the media format.
* `status_t` [FormatSuggestionRequested](#abf591d844f4337af76861a345bcf60bd) (media_type type, int32 quality, media_format *format) — Checks if a certain media format works with the GameProducer.
* `status_t` [GetLatency](#a52ca79556bcec4da5bc883753d2311e4) (bigtime_t *_latency) — Gets the total latency, including internal downstream plus scheduling.
* `status_t` [GetNextOutput](#a56ee8d7d908b12e7bad1568a2568adb0) (int32 *cookie, media_output *_output) — Gets the next output cookie.
* `void` [HandleEvent](#a4c5d92087936c3f0837bb5e4431c9c02) (const media_timed_event *event, bigtime_t lateness, bool realTimeEvent=false) — Handles when an event is triggered.
* `status_t` [HandleMessage](#ae3769c1fde1c9705f3d046a4beeb3264) (int32 message, const void *data, size_t size) — Private messages are not supported, returns B_ERROR.
* `void` [LatencyChanged](#a80726424be3cb7deaec035f141491b29) (const media_source &source, const media_destination &destination, bigtime_t new_latency, uint32 flags) — Sets the event latency in the case that the latency changed.
* `void` [LateNoticeReceived](#a92ed2a9808441275f3a11333c621e52a) (const media_source &what, bigtime_t howMuch, bigtime_t performanceDuration) — Attempts to catch up to the buffer.
* `void` [NodeRegistered](#a36de3a61af1c634eba064eff6d5afc42) () — Handles when an output source node is registered.
* `status_t` [PrepareToConnect](#a74d15289af196719049d49313fe96010) (const media_source &what, const media_destination &where, media_format *format, media_source *_source, char *out_name) — Confirms that the media format and wild cards are valid.
* `status_t` [SetBufferGroup](#aa595436831df537816654cb28bd4b906) (const media_source &forSource, BBufferGroup *group) — Changes the buffer group from the current one, to the specified one.
* `status_t` [SetPlayRate](#a2c219b6e1dcdf02f12d6ecbc1e64d0f2) (int32 numerator, int32 denominator) — Play rates are not supported, returns B_ERROR.
* `void` [SetRunMode](#a11ccc26c3e903fc3051815d59feeaefc) (run_mode mode) — Offline mode is not supported.

## Detailed Member Documentation

### `GameProducer()`

```cpp
GameProducer::GameProducer(GameSoundBuffer * object, const gs_audio_format * format)
```

Initializes the [GameProducer](classGameProducer.md) with the passed in GameSoundBuffer and gs_audio_format. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `object` | The GameSoundBuffer to 'sync' the [GameProducer](classGameProducer.md) with. |
| `format` | The gs_audio_format to set the [GameProducer](classGameProducer.md)'s format. |





**Since:** Haiku R1

---

### `~GameProducer()`

```cpp
GameProducer::~GameProducer()
```

Destroys the [GameProducer](classGameProducer.md) object and stops the [BMediaEventLooper](classBMediaEventLooper.md) thread. 



**Since:** Haiku R1

---

### `AdditionalBufferRequested()`

```cpp
void GameProducer::AdditionalBufferRequested(const media_source & source, media_buffer_id prev_buffer, bigtime_t prev_time, const media_seek_tag * prev_tag)
```

Offline modes are not supported for now, does nothing. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `source` | The media output source. |
| `prev_buffer` | The previous buffer. |
| `prev_time` | The previous buffer time. |
| `prev_tag` | The previous buffer delimiter. |





**Since:** Haiku R1

---

### `AddOn()`

```cpp
BMediaAddOn * GameProducer::AddOn(int32 * internal_id)const
```

Unimplemented. 



**Since:** Haiku R1


Implements [BMediaNode](classBMediaNode.md).

---

### `Connect()`

```cpp
void GameProducer::Connect(status_t error, const media_source & source, const media_destination & destination, const media_format & format, char * ioName)
```

Connects to the output device. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `error` | The variable that holds an error, should one arise. |
| `source` | The output source to connect to. |
| `destination` | The media destination, that is connected to. |
| `format` | The variable that holds the format type. |
| `ioName` | The variable that holds the output name. |

---

### `Disconnect()`

```cpp
void GameProducer::Disconnect(const media_source & what, const media_destination & where)
```

Disconnects from the output device. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `what` | The media destination. |
| `where` | The media's output source. |





**Since:** Haiku R1

---

### `DisposeOutputCookie()`

```cpp
status_t GameProducer::DisposeOutputCookie(int32 cookie)
```

Does nothing because the cookie has no use as of yet. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `cookie` | The cookie index. |





**Returns:** Always returns B_OK.



**Since:** Haiku R1

---

### `EnableOutput()`

```cpp
void GameProducer::EnableOutput(const media_source & what, bool enabled, int32 * _deprecated_)
```

Enable or disable an output. 



> [!IMPORTANT]
> This method is deprecated.


Parameters

| Parameter | Description |
| :--- | :--- |
| `what` | The media output source. |
| `enabled` | Sets the output to enabled or disabled. |
| `_deprecated_` | This method is deprecated. |





**Since:** Haiku R1

---

### `FormatChangeRequested()`

```cpp
status_t GameProducer::FormatChangeRequested(const media_source & source, const media_destination & destination, media_format * io_format, int32 * _deprecated_)
```

We don't support any other formats, so we just reject any format changes. 



> [!IMPORTANT]
> This method is deprecated.


Parameters

| Parameter | Description |
| :--- | :--- |
| `source` | The output source. |
| `destination` | The media's destination. |
| `io_format` | The format of the media |
| `_deprecated_` | This method is deprecated. |





**Returns:** B_ERROR as this function is deprecated, it has been removed, and now only returns *B_ERROR*.



**Since:** Haiku R1

---

### `FormatProposal()`

```cpp
status_t GameProducer::FormatProposal(const media_source & output, media_format * format)
```

Attempts to change the media format. 



> [!WARNING]
> Only supports raw audio and wildcard audio types.


Parameters

| Parameter | Description |
| :--- | :--- |
| `output` | The source that the media outputs to. |
| `format` | The type of media being proposed. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The *format* is supported. |
| B_MEDIA_BAD_SOURCE | The *output* doesn't match the current output source. |
| B_MEDIA_BAD_FORMAT | The *format* is not supported. |





**Since:** Haiku R1

---

### `FormatSuggestionRequested()`

```cpp
status_t GameProducer::FormatSuggestionRequested(media_type type, int32 quality, media_format * format)
```

Checks if a certain media format works with the [GameProducer](classGameProducer.md). 



> [!WARNING]
> Only supports raw audio at this point.


Parameters

| Parameter | Description |
| :--- | :--- |
| `type` | The media format being tested. |
| `quality` | The quality of the media – Not used in the method. |
| `format` | The media format to send through. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | *type* is supported. |
| B_BAD_VALUE | No *format* was received. |
| B_MEDIA_BAD_FORMAT | The *format* is not supported. |





**Since:** Haiku R1

---

### `GetLatency()`

```cpp
status_t GameProducer::GetLatency(bigtime_t * _latency)
```

Gets the total latency, including internal downstream plus scheduling. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `_latency` | Gets set to the current latency. |





**Returns:** B_OK.



**Since:** Haiku R1

---

### `GetNextOutput()`

```cpp
status_t GameProducer::GetNextOutput(int32 * cookie, media_output * _output)
```

Gets the next output cookie. 


Cookie can only be zero, as [GameProducer](classGameProducer.md) supports one output.


Parameters

| Parameter | Description |
| :--- | :--- |
| `cookie` | The output cookie value. |
| `_output` | The output that the cookie represents. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The cookie was successfully incremented. |
| B_BAD_INDEX | The cookie is not equal to zero. |





**Since:** Haiku R1

---

### `HandleEvent()`

```cpp
void GameProducer::HandleEvent(const media_timed_event * event, bigtime_t lateness, bool realTimeEvent = false)
```

Handles when an event is triggered. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `event` | The type of event. |
| `lateness` | Unused. |
| `realTimeEvent` | Unused. |





**Since:** Haiku R1


Implements [BMediaEventLooper](classBMediaEventLooper.md).

---

### `HandleMessage()`

```cpp
status_t GameProducer::HandleMessage(int32 message, const void * data, size_t size)
```

Private messages are not supported, returns `B_ERROR`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The message to be sent. |
| `data` | The data to be sent. |
| `size` | The size of the message. |





**Returns:** Always returns `B_ERROR` since private messages aren't supported.



**Since:** Haiku R1


Reimplemented from [BMediaNode](classBMediaNode.md).

---

### `LatencyChanged()`

```cpp
void GameProducer::LatencyChanged(const media_source & source, const media_destination & destination, bigtime_t new_latency, uint32 flags)
```

Sets the event latency in the case that the latency changed. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `source` | The media output source. |
| `destination` | The connected output destination. |
| `new_latency` | The new amount of latency. |
| `flags` | Unused. |





**Since:** Haiku R1

---

### `LateNoticeReceived()`

```cpp
void GameProducer::LateNoticeReceived(const media_source & what, bigtime_t howMuch, bigtime_t performanceDuration)
```

Attempts to catch up to the buffer. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `what` | The media output source. |
| `howMuch` | The amount of 'lateness'. |
| `performanceDuration` | Unused. |





**Since:** Haiku R1

---

### `NodeRegistered()`

```cpp
void GameProducer::NodeRegistered()
```

Handles when an output source node is registered. 



**Since:** Haiku R1


Reimplemented from [BMediaEventLooper](classBMediaEventLooper.md).

---

### `PrepareToConnect()`

```cpp
status_t GameProducer::PrepareToConnect(const media_source & what, const media_destination & where, media_format * format, media_source * _source, char * out_name)
```

Confirms that the media format and wild cards are valid. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `what` | The media source to output to. |
| `where` | The destination for the connection. |
| `format` | The format to finish specializing. |
| `_source` | The output source that the method retrieves. |
| `out_name` | The variable that holds the output name. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The connection preparations have finished. |
| B_MEDIA_BAD_SOURCE | The *output* doesn't match the current output source. |
| B_MEDIA_ALREADY_CONNECTED | The [GameProducer](classGameProducer.md) is already connected. |
| B_MEDIA_BAD_FORMAT | The *format* is not supported. |





**Since:** Haiku R1

---

### `SetBufferGroup()`

```cpp
status_t GameProducer::SetBufferGroup(const media_source & forSource, BBufferGroup * newGroup)
```

Changes the buffer group from the current one, to the specified one. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `forSource` | The output source. Can't be equivalent to the current output source. |
| `newGroup` | The new BBufferGroup to assign the buffer group to. |





**Returns:** A status code.


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| B_OK | The change has succeeded. |
| B_MEDIA_BAD_SOURCE | *forSource* is equal to the current output source. |
| B_BAD_VALUE | The new BBufferGroup's buffer list returns an error. |





**Since:** Haiku R1

---

### `SetPlayRate()`

```cpp
status_t GameProducer::SetPlayRate(int32 numerator, int32 denominator)
```

Play rates are not supported, returns `B_ERROR`. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `numerator` | The top part of the fraction. |
| `denominator` | The bottom part of the fraction. |





**Returns:** Always returns `B_ERROR` since play rates aren't supported.



**Since:** Haiku R1

---

### `SetRunMode()`

```cpp
void GameProducer::SetRunMode(run_mode mode)
```

Offline mode is not supported. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `mode` | The mode of running. |





**Since:** Haiku R1


Reimplemented from [BMediaEventLooper](classBMediaEventLooper.md).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classGameProducer.html).
