---
name: BMidiLocalProducer
type: class
kit: midi_2_kit
brief: "A producer endpoint that is created by your own application"
source: haiku-book
---

# BMidiLocalProducer Class
**Kit/Group:** [MIDI 2 Kit](../midi_2_kit/group__midi2.md)

## Description

A producer endpoint that is created by your own application. 


You create a [BMidiLocalProducer](classBMidiLocalProducer.md) if you want your application to send MIDI events. You use the various spray functions to send events to all connected consumers. If no consumers are connected to the producer, any calls to the spray functions are ignored.


Most spray functions accept a channel argument. Even though MIDI channels are really numbered 1 through 16, the spray functions work with channels 0 through 15. You can also specify the performance time for the event using the time argument. Specify 0 (or any time in the past) to perform the event "now", i.e. as soon as possible. You can also schedule events to be performed in the future, by passing a time such as system_time() + 5000000, which means 5 seconds from now.


Unlike [BMidiLocalConsumer](classBMidiLocalConsumer.md), which should be subclassed almost always, you hardly ever need to derive a class from [BMidiLocalProducer](classBMidiLocalProducer.md). The only reason for subclassing is when you need to know when the producer gets connected or disconnected.


Also unlike consumers, local producers have no thread of control directly associated with them. If you want to send out the MIDI events from a different thread, you will have to create one yourself.

## Member List

### Public Member Functions

* [BMidiLocalProducer](#aaa7581cc02a64df6520abc42c6290b03) (const char *name=NULL) — Creates a new local producer endpoint.
* `virtual void` [Connected](#a7a399648299576dd5173d66140b5e91e) (BMidiConsumer *cons) — Invoked when a new consumer is connected to this producer.
* `virtual void` [Disconnected](#a26c3cef91310c467d46e6ada96ae194b) (BMidiConsumer *cons) — Invoked when a consumer is disconnected from this producer.
* `void` [SprayChannelPressure](#a29eacce2dc50b1e193903ae28b5e5feb) (uchar channel, uchar pressure, bigtime_t time=0) const — Sends a Channel Pressure event to all connected consumers.
* `void` [SprayControlChange](#a25e58f5d855eadfebd50d8ac5e9db423) (uchar channel, uchar controlNumber, uchar controlValue, bigtime_t time=0) const — Sends a Controller Change event to all connected consumers.
* `void` [SprayData](#ae8cabda990298dbb11a3c4d70edcb047) (void *data, size_t length, bool atomic=false, bigtime_t time=0) const — Sends raw MIDI data downstream to all connected consumers.
* `void` [SprayKeyPressure](#a7508488d1d0268d0061146c706392e5c) (uchar channel, uchar note, uchar pressure, bigtime_t time=0) const — Sends a Polyphonic Pressure (Aftertouch) event to all connected consumers.
* `void` [SprayNoteOff](#a9a8eaf2c2993e435f4b766ebc3dc0135) (uchar channel, uchar note, uchar velocity, bigtime_t time=0) const — Sends a Note Off event to all connected consumers.
* `void` [SprayNoteOn](#ae894fdb7f04b2c65329720592cb525dd) (uchar channel, uchar note, uchar velocity, bigtime_t time=0) const — Sends a Note On event to all connected consumers.
* `void` [SprayPitchBend](#ab8bf5919d03bd48cb245868d6765da72) (uchar channel, uchar lsb, uchar msb, bigtime_t time=0) const — Sends a Pitch Bend event to all connected consumers.
* `void` [SprayProgramChange](#a1996b1a5486d0ff0008e7705138fe9d6) (uchar channel, uchar programNumber, bigtime_t time=0) const — Sends a Program Change event to all connected consumers.
* `void` [SpraySystemCommon](#a7e0de2eea30f60f75ef06a8bc03b853e) (uchar status, uchar data1, uchar data2, bigtime_t time=0) const — Sends a System Common event to the connected consumers.
* `void` [SpraySystemExclusive](#af7aeb206b4e0b343d95f42e68db5d956) (void *data, size_t length, bigtime_t time=0) const — Sends a System Exclusive event to all connected consumers.
* `void` [SpraySystemRealTime](#a776c12865641386d826145a37796bd54) (uchar status, bigtime_t time=0) const — Sends a Real Time event to the connected consumers.
* `void` [SprayTempoChange](#ae7302b78045f6e99a50bb43ec255b848) (int32 beatsPerMinute, bigtime_t time=0) const — Sends a Tempo Change event to the connected consumers.
* `status_t` [Connect](#ae1fe6a25736a3f8eb154158429fc224a) (BMidiConsumer *cons) — Connects a consumer to this producer.
* `BList *` [Connections](#a86959b229758ec9c9cccec9f8631d6ab) () const — Returns a list with all connected consumers.
* `status_t` [Disconnect](#a7f68b65fd703766a0fccb5d9535ea6ed) (BMidiConsumer *cons) — Disconnects a consumer from this producer.
* `bool` [IsConnected](#a1aca7bf741e4765737dfda6685c50063) (BMidiConsumer *cons) const — Determines whether a consumer is connected to this producer.
* `status_t` [Acquire](#a504efce89310e4473c4a9ae77da7a641) () — Increments the endpoint's reference count.
* `status_t` [GetProperties](#a5c6c8dc7f451e7c908df05319f24a64f) (BMessage *properties) const — Reads the properties of the endpoint.
* `int32` [ID](#a3f5b840617bf84cddbca779c470cef17) () const — Returns the ID of the endpoint.
* `bool` [IsConsumer](#ae20fe83d79bd0d08cb818d3dda0fdc23) () const — Determines whether this endpoint is a BMidiConsumer.
* `bool` [IsLocal](#a3edca82a4aa8bfa2aad3874cc9192b4d) () const — Determines whether this endpoint represents a local object.
* `bool` [IsPersistent](#a20623d6d71190a701e9bccc23e646e6a) () const — Not used.
* `bool` [IsProducer](#a2555a377a070eaea225ca40b9e5bb696) () const — Determines whether this endpoint is a BMidiProducer.
* `bool` [IsRemote](#a11fc9a34aee618e137d9affcd67a7b36) () const — Determines whether this endpoint is a proxy for a remote object.
* `bool` [IsValid](#a0c9f93e72f5302f6f0c631e5a4f0ddb2) () const — Determines whether the endpoint still exists.
* `const char *` [Name](#a685e4d64cfbf56e30c7a3c5849fc72d8) () const — Returns the name of the endpoint.
* `status_t` [Register](#a6a818947b6098488a46e5a934d254186) () — Publishes the endpoint on the roster.
* `status_t` [Release](#a368ed2bdb2b76afe1466daf0cc0e2b08) () — Decrements the endpoint's reference count.
* `void` [SetName](#afa167950f7b60558712224798f7e50aa) (const char *name) — Changes the name of the endpoint.
* `status_t` [SetProperties](#a58cf2c701ba336b640067db743ba9746) (const BMessage *properties) — Changes the properties of the endpoint.
* `status_t` [Unregister](#ad60d3fd6a9706a63f57851acf84db042) () — Hides the endpoint from the roster/.

## Detailed Member Documentation

### `BMidiLocalProducer()`

```cpp
BMidiLocalProducer::BMidiLocalProducer(const char * name = NULL)
```

Creates a new local producer endpoint. 


The new endpoint is not visible to other applications until you [Register()](classBMidiEndpoint.md#a6a818947b6098488a46e5a934d254186) it. You can tell the constructor what the name of the new producer will be. If you pass NULL (or use the default argument), then the producer's name will be an empty string. It won't be NULL, since endpoint names cannot be NULL. There is no guarantee that the endpoint will be successfully created. For example, the Midi Server may not be running. Therefore, you should always call [IsValid()](classBMidiEndpoint.md#a0c9f93e72f5302f6f0c631e5a4f0ddb2) after creating a new endpoint to make sure that everything went okay. If not, [Release()](classBMidiEndpoint.md#a368ed2bdb2b76afe1466daf0cc0e2b08) the object to reclaim memory and abort gracefully. 


```cpp
BMidiLocalProducer* prod = new BMidiLocalProducer(...);
if (!prod->IsValid())
{
    prod->Release();
    ...exit gracefully...
}
```

---

### `Connected()`

```cpp
void BMidiLocalProducer::Connected(BMidiConsumer * cons)
```

Invoked when a new consumer is connected to this producer. 


Although typical notifications (i.e. from [BMidiRoster](classBMidiRoster.md)'s "watching" facility) are only sent if it is some other app that is performing the operation, [Connected()](classBMidiLocalProducer.md#a7a399648299576dd5173d66140b5e91e) is also called if you are making the connection yourself. If you override this hook, you don't have to call the default implementation, because that does nothing.


Parameters

| Parameter | Description |
| :--- | :--- |
| `cons` | The newly connected consumer. The reference count of the consumer object is not increased, so you should not [Release()](classBMidiEndpoint.md#a368ed2bdb2b76afe1466daf0cc0e2b08) it. However, if you want to keep track of the consumer beyond this function, you should first [Acquire()](classBMidiEndpoint.md#a504efce89310e4473c4a9ae77da7a641) it, and [Release()](classBMidiEndpoint.md#a368ed2bdb2b76afe1466daf0cc0e2b08) it when you are done. |





**See also:** [Disconnected()](classBMidiLocalProducer.md#a26c3cef91310c467d46e6ada96ae194b)

---

### `Disconnected()`

```cpp
void BMidiLocalProducer::Disconnected(BMidiConsumer * cons)
```

Invoked when a consumer is disconnected from this producer. 



**See also:** [Connected()](classBMidiLocalProducer.md#a7a399648299576dd5173d66140b5e91e)

---

### `SprayChannelPressure()`

```cpp
void BMidiLocalProducer::SprayChannelPressure(uchar channel, uchar pressure, bigtime_t time = 0)const
```

Sends a Channel Pressure event to all connected consumers. 



**See also:** [BMidiLocalConsumer::ChannelPressure()](classBMidiLocalConsumer.md#af44b9be98bfa1993de27a3d557eb7699)

---

### `SprayControlChange()`

```cpp
void BMidiLocalProducer::SprayControlChange(uchar channel, uchar controlNumber, uchar controlValue, bigtime_t time = 0)const
```

Sends a Controller Change event to all connected consumers. 



**See also:** [Midi2Defs.h](Midi2Defs_8h.md)

---

### `SprayData()`

```cpp
void BMidiLocalProducer::SprayData(void * data, size_t length, bool atomic = false, bigtime_t time = 0)const
```

Sends raw MIDI data downstream to all connected consumers. 


Typically you won't have to call [SprayData()](classBMidiLocalProducer.md#ae8cabda990298dbb11a3c4d70edcb047); the other spray functions will do just fine. If you do call it, remember that you retain ownership of the data and that you are responsible for freeing it at some point. (Even though data is not declared const, the function does not change it.) With atomic set to false, you can send a MIDI message in segments (perhaps for a large sysex dump). However, when you do this, you are on your own. The Midi Kit only tags the data as being non-atomic, but offers no] additional support.


The default implementation of [BMidiLocalConsumer](classBMidiLocalConsumer.md) completely ignores such events. To handle non-atomic MIDI data, you should override the [BMidiLocalConsumer::Data()](classBMidiLocalConsumer.md#a4b99be774374a9098cdb7535baef51bb) hook and process the MIDI event yourself. All of [BMidiLocalProducer](classBMidiLocalProducer.md)'s other spray functions always send atomic data.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | the MIDI event data. |
| `length` | byte size of the data buffer. |
| `atomic` | whether the data buffer contains a single complete MIDI event. |
| `time` | the required performance time of the event. |





**See also:** [BMidiLocalConsumer::Data()](classBMidiLocalConsumer.md#a4b99be774374a9098cdb7535baef51bb)

---

### `SprayKeyPressure()`

```cpp
void BMidiLocalProducer::SprayKeyPressure(uchar channel, uchar note, uchar pressure, bigtime_t time = 0)const
```

Sends a Polyphonic Pressure (Aftertouch) event to all connected consumers. 



**See also:** [BMidiLocalConsumer::KeyPressure()](classBMidiLocalConsumer.md#a40bd466df44bc73cb896123e693cb96b)

---

### `SprayNoteOff()`

```cpp
void BMidiLocalProducer::SprayNoteOff(uchar channel, uchar note, uchar velocity, bigtime_t time = 0)const
```

Sends a Note Off event to all connected consumers. 



**See also:** [BMidiLocalConsumer::NoteOff()](classBMidiLocalConsumer.md#a25329db05d4e210e7495d0618cc7e2cd)

---

### `SprayNoteOn()`

```cpp
void BMidiLocalProducer::SprayNoteOn(uchar channel, uchar note, uchar velocity, bigtime_t time = 0)const
```

Sends a Note On event to all connected consumers. 



**See also:** [BMidiLocalConsumer::NoteOn()](classBMidiLocalConsumer.md#af8986251fbb08548712e0273c13dd87e)

---

### `SprayPitchBend()`

```cpp
void BMidiLocalProducer::SprayPitchBend(uchar channel, uchar lsb, uchar msb, bigtime_t time = 0)const
```

Sends a Pitch Bend event to all connected consumers. 



**See also:** [BMidiLocalConsumer::PitchBend()](classBMidiLocalConsumer.md#a0aeef8a6c7ac0933c290e34ec413b679)

---

### `SprayProgramChange()`

```cpp
void BMidiLocalProducer::SprayProgramChange(uchar channel, uchar programNumber, bigtime_t time = 0)const
```

Sends a Program Change event to all connected consumers. 



**See also:** [BMidiLocalConsumer::ProgramChange()](classBMidiLocalConsumer.md#abc694df60305b285bfd82291709cf3f7)

---

### `SpraySystemCommon()`

```cpp
void BMidiLocalProducer::SpraySystemCommon(uchar status, uchar data1, uchar data2, bigtime_t time = 0)const
```

Sends a System Common event to the connected consumers. 


The status byte must be one of the following: 


| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| 0xF1 | `B_MIDI_TIME_CODE` | data1 only |
| 0xF2 | `B_SONG_POSITION` | data1 and data2 |
| 0xF3 | `B_SONG_SELECT` | data1 only |
| 0xF5 | `B_CABLE_MESSAGE` | data1 only |
| 0xF6 | `B_TUNE_REQUEST` | no data |
| 0xF7 | `B_SYS_EX_END` | no data |



**See also:** [BMidiLocalConsumer::SystemCommon()](classBMidiLocalConsumer.md#a269746afdbeed326f7d95ba897e8d10c)

---

### `SpraySystemExclusive()`

```cpp
void BMidiLocalProducer::SpraySystemExclusive(void * data, size_t length, bigtime_t time = 0)const
```

Sends a System Exclusive event to all connected consumers. 


You retain ownership of the data and are responsible for freeing it. Even though data is not declared const, the function does not change it. Even though the amount of data may be quite large, this function always sends sysex messages as an atomic block of data.



**See also:** [BMidiLocalConsumer::SystemExclusive()](classBMidiLocalConsumer.md#a64798d8363e51044b516addc23937788)

---

### `SpraySystemRealTime()`

```cpp
void BMidiLocalProducer::SpraySystemRealTime(uchar status, bigtime_t time = 0)const
```

Sends a Real Time event to the connected consumers. 


The status byte must be one of the following: 


| Col 1 | Col 2 |
| :--- | :--- |
| 0xf8 | `B_TIMING_CLOCK` |
| 0xfa | `B_START` |
| 0xfb | `B_CONTINUE` |
| 0xfc | `B_STOP` |
| 0xfe | `B_ACTIVE_SENSING` |
| 0xff | `B_SYSTEM_RESET` |


Because of their high priority, the MIDI specification allows real time messages to "interleave" with other MIDI messages. A large sysex dump, for example, may be interrupted by a real time event. The Midi Kit, however, doesn't care. If you (or another producer) have just sent a big system exclusive to a consumer, any following real time message will simply have to wait until the consumer has dealt with the sysex.



**See also:** [BMidiLocalConsumer::SystemRealTime()](classBMidiLocalConsumer.md#a3a36cf048a1bb7d92a9d97e98ffc3dc4)

---

### `SprayTempoChange()`

```cpp
void BMidiLocalProducer::SprayTempoChange(int32 bpm, bigtime_t time = 0)const
```

Sends a Tempo Change event to the connected consumers. 


This kind of Tempo Change event is not really part of the MIDI spec, rather it is an extension from the SMF (Standard MIDI File) format.



**See also:** [BMidiLocalConsumer::TempoChange()](classBMidiLocalConsumer.md#aa86d74b50c5b0ff5f2a49c8d0ad9e01d)

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMidiLocalProducer.html).
