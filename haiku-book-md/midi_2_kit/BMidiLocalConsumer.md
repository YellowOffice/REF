---
name: BMidiLocalConsumer
type: class
kit: midi_2_kit
brief: "A consumer endpoint that is created by your own application"
source: haiku-book
---

# BMidiLocalConsumer Class
**Kit/Group:** [MIDI 2 Kit](../midi_2_kit/group__midi2.md)

## Description

A consumer endpoint that is created by your own application. 


If you want to create a consumer that reacts to MIDI events, you should subclass [BMidiLocalConsumer](classBMidiLocalConsumer.md).


Each local consumer has its own thread that receives and dispatches the MIDI events. Whenever MIDI data arrives, the [Data()](classBMidiLocalConsumer.md#a4b99be774374a9098cdb7535baef51bb) hook passes the MIDI event on to a more specific hook function: [NoteOn()](classBMidiLocalConsumer.md#af8986251fbb08548712e0273c13dd87e), [NoteOff()](classBMidiLocalConsumer.md#a25329db05d4e210e7495d0618cc7e2cd), [SystemExclusive()](classBMidiLocalConsumer.md#a64798d8363e51044b516addc23937788), and so on. Calls to these hook functions are serialized – they will never have to be re-entrant. They also should not be called from outside the thread that is invoking them.


Your subclass can override any of the MIDI event hooks. [BMidiLocalConsumer](classBMidiLocalConsumer.md) doesn't provide default implementations for them, so you don't have to call a hook's default implementation if you override it. For complete control, you can also override [Data()](classBMidiLocalConsumer.md#a4b99be774374a9098cdb7535baef51bb).


Most hook functions take a channel argument. Even though MIDI channels are really numbered 1 through 16, the hook functions work with channels 0 through 15. The performance time for the event is specified in microseconds relative to the system time base. A performance time that is 0 (or really any time in the past) means "play as soon as possible". See the [introduction](midi2_intro.md#midi2time) for more information about timing and consumers.


The thread driving the consumer's events is a very high priority real time thread. Events should be handled as quickly as possible (not counting snoozing). If non-time-critical computation is needed it may be wise to queue events up for a lower priority thread to handle them external to the main event thread.

## Member List

### Public Member Functions

* [BMidiLocalConsumer](#af5599649a8dcb2b5b378d140648d6e1c) (const char *name=NULL) — Creates a new local consumer endpoint.
* `virtual void` AllNotesOff (bool justChannel, [bigtime_t](#a29bb8e432e460af113ef8938cef96f8b) time) — Not used.
* `virtual void` [ChannelPressure](#af44b9be98bfa1993de27a3d557eb7699) (uchar channel, uchar pressure, bigtime_t time) — Invoked when a Channel Pressure event is received.
* `virtual void` [ControlChange](#a48ae4c29a7044c1f53fa2901f0aad548) (uchar channel, uchar controlNumber, uchar controlValue, bigtime_t time) — Invoked when a Controller Change event is received.
* `virtual void` [Data](#a4b99be774374a9098cdb7535baef51bb) (uchar *data, size_t length, bool atomic, bigtime_t time) — Invoked when raw MIDI is received.
* `int32` [GetProducerID](#a5fdd8a43dbaec4e2c96f476b2b008783) () — Returns the ID of the producer that most recently sent a MIDI event to this consumer.
* `virtual void` [KeyPressure](#a40bd466df44bc73cb896123e693cb96b) (uchar channel, uchar note, uchar pressure, bigtime_t time) — Invoked when a Polyphonic Pressure (Aftertouch) event is received.
* `virtual void` [NoteOff](#a25329db05d4e210e7495d0618cc7e2cd) (uchar channel, uchar note, uchar velocity, bigtime_t time) — Invoked when a Note Off event is received.
* `virtual void` [NoteOn](#af8986251fbb08548712e0273c13dd87e) (uchar channel, uchar note, uchar velocity, bigtime_t time) — Invoked when a Note On event is received.
* `virtual void` [PitchBend](#a0aeef8a6c7ac0933c290e34ec413b679) (uchar channel, uchar lsb, uchar msb, bigtime_t time) — Invoked when a Pitch Bend event is received.
* `virtual void` [ProgramChange](#abc694df60305b285bfd82291709cf3f7) (uchar channel, uchar programNumber, bigtime_t time) — Invoked when a Program Change event is received.
* `void` [SetLatency](#a63fc7918e61adf5bee4ec3a24cb7cbb7) (bigtime_t latency) — Changes the published latency of the consumer.
* `void` [SetTimeout](#a92d0d4dc591ca2c90bc51a3ac883ce29) (bigtime_t when, void *data) — Requests that the Timeout() hook will be called at some point.
* `virtual void` [SystemCommon](#a269746afdbeed326f7d95ba897e8d10c) (uchar status, uchar data1, uchar data2, bigtime_t time) — Invoked when a System Common event is received.
* `virtual void` [SystemExclusive](#a64798d8363e51044b516addc23937788) (void *data, size_t length, bigtime_t time) — Invoked when a System Exclusive event is received.
* `virtual void` [SystemRealTime](#a3a36cf048a1bb7d92a9d97e98ffc3dc4) (uchar status, bigtime_t time) — Invoked when a Real Time event is received.
* `virtual void` [TempoChange](#aa86d74b50c5b0ff5f2a49c8d0ad9e01d) (int32 beatsPerMinute, bigtime_t time) — Invoked when a Tempo Change event is received.
* `virtual void` [Timeout](#a1331cbaa81327455ed000ec45dff0f27) (void *data) — Hook function that is called per your own request.
* `bigtime_t` [Latency](#a11a23be136f1eaa0f797d1e8b5b4e460) () const — Returns the latency of this consumer.
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

### `BMidiLocalConsumer()`

```cpp
BMidiLocalConsumer::BMidiLocalConsumer(const char * name = NULL)
```

Creates a new local consumer endpoint. 


The new endpoint is not visible to other applications until you [Register()](classBMidiEndpoint.md#a6a818947b6098488a46e5a934d254186) it.


You can tell the constructor what the name of the new consumer will be. If you pass NULL (or use the default argument), then the consumer's name will be an empty string. It won't be NULL, since endpoint names cannot be NULL.


There is no guarantee that the endpoint will be successfully created. For example, the Midi Server may not be running. Therefore, you should always call [IsValid()](classBMidiEndpoint.md#a0c9f93e72f5302f6f0c631e5a4f0ddb2) after creating a new endpoint to make sure that everything went okay. If not, [Release()](classBMidiEndpoint.md#a368ed2bdb2b76afe1466daf0cc0e2b08) the object to reclaim memory and abort gracefully.



```cpp
MyConsumer* cons = new MyConsumer(...);
if (!cons->IsValid())
{
    cons->Release();
    ...exit gracefully...
}
```

---

### `ChannelPressure()`

```cpp
void BMidiLocalConsumer::ChannelPressure(uchar channel, uchar pressure, bigtime_t time)
```

Invoked when a Channel Pressure event is received. 



**See also:** [BMidiLocalProducer::SprayChannelPressure()](classBMidiLocalProducer.md#a29eacce2dc50b1e193903ae28b5e5feb)

---

### `ControlChange()`

```cpp
void BMidiLocalConsumer::ControlChange(uchar channel, uchar controlNumber, uchar controlValue, bigtime_t time)
```

Invoked when a Controller Change event is received. 



**See also:** [BMidiLocalProducer::SprayControlChange()](classBMidiLocalProducer.md#a25e58f5d855eadfebd50d8ac5e9db423)

---

### `Data()`

```cpp
void BMidiLocalConsumer::Data(uchar * data, size_t length, bool atomic, bigtime_t time)
```

Invoked when raw MIDI is received. 


What the default implementation of [Data()](classBMidiLocalConsumer.md#a4b99be774374a9098cdb7535baef51bb) does depends on the value of atomic. If atomic is true, the data received comprises a single MIDI event; i.e. one status byte followed by the appropriate number of data bytes and nothing else. In this case, [Data()](classBMidiLocalConsumer.md#a4b99be774374a9098cdb7535baef51bb) calls the event-specific hook function that corresponds to that status byte. This optimization is used by the Midi Kit to allow faster dispatch of events generated by the specific Spray functions from [BMidiLocalProducer](classBMidiLocalProducer.md).


If atomic is false, [Data()](classBMidiLocalConsumer.md#a4b99be774374a9098cdb7535baef51bb) ignores the MIDI event. If you want a consumer to handle non-atomic events, you have to override [Data()](classBMidiLocalConsumer.md#a4b99be774374a9098cdb7535baef51bb) and program this yourself. In that case, you probably also want to call the default implementation to handle the "normal" MIDI events.


[Data()](classBMidiLocalConsumer.md#a4b99be774374a9098cdb7535baef51bb) is rarely overridden, but you can override it if you want to. If you do, remember that the data buffer is owned by the Midi Kit. Do not attempt to modify or free it, lest you wish to be laughed at by other developers.


Parameters

| Parameter | Description |
| :--- | :--- |
| `data` | the MIDI event data |
| `length` | byte size of the data buffer |
| `atomic` | whether the data buffer contains a single complete MIDI event |
| `time` | the requested performance time of the event |





**See also:** [BMidiLocalProducer::SprayData()](classBMidiLocalProducer.md#ae8cabda990298dbb11a3c4d70edcb047)

---

### `GetProducerID()`

```cpp
int32 BMidiLocalConsumer::GetProducerID()
```

Returns the ID of the producer that most recently sent a MIDI event to this consumer. 


You can call this from one of the hooks to determine which producer the event came from.

---

### `KeyPressure()`

```cpp
void BMidiLocalConsumer::KeyPressure(uchar channel, uchar note, uchar pressure, bigtime_t time)
```

Invoked when a Polyphonic Pressure (Aftertouch) event is received. 



**See also:** [BMidiLocalProducer::SprayKeyPressure()](classBMidiLocalProducer.md#a7508488d1d0268d0061146c706392e5c)

---

### `NoteOff()`

```cpp
void BMidiLocalConsumer::NoteOff(uchar channel, uchar note, uchar velocity, bigtime_t time)
```

Invoked when a Note Off event is received. 



**See also:** [BMidiLocalProducer::SprayNoteOff()](classBMidiLocalProducer.md#a9a8eaf2c2993e435f4b766ebc3dc0135)

---

### `NoteOn()`

```cpp
void BMidiLocalConsumer::NoteOn(uchar channel, uchar note, uchar velocity, bigtime_t time)
```

Invoked when a Note On event is received. 



**See also:** [BMidiLocalProducer::SprayNoteOn()](classBMidiLocalProducer.md#ae894fdb7f04b2c65329720592cb525dd)

---

### `PitchBend()`

```cpp
void BMidiLocalConsumer::PitchBend(uchar channel, uchar lsb, uchar msb, bigtime_t time)
```

Invoked when a Pitch Bend event is received. 



**See also:** [BMidiLocalProducer::SprayPitchBend()](classBMidiLocalProducer.md#ab8bf5919d03bd48cb245868d6765da72)

---

### `ProgramChange()`

```cpp
void BMidiLocalConsumer::ProgramChange(uchar channel, uchar programNumber, bigtime_t time)
```

Invoked when a Program Change event is received. 



**See also:** [BMidiLocalProducer::SprayProgramChange()](classBMidiLocalProducer.md#a1996b1a5486d0ff0008e7705138fe9d6)

---

### `SetLatency()`

```cpp
void BMidiLocalConsumer::SetLatency(bigtime_t latency)
```

Changes the published latency of the consumer. 



**See also:** [Latency()](classBMidiConsumer.md#a11a23be136f1eaa0f797d1e8b5b4e460)

---

### `SetTimeout()`

```cpp
void BMidiLocalConsumer::SetTimeout(bigtime_t when, void * data)
```

Requests that the [Timeout()](classBMidiLocalConsumer.md#a1331cbaa81327455ed000ec45dff0f27) hook will be called at some point. 


This method asks the consumer thread to call the [Timeout()](classBMidiLocalConsumer.md#a1331cbaa81327455ed000ec45dff0f27) hook as soon as possible after the timeout expires. For every call to [SetTimeout()](classBMidiLocalConsumer.md#a92d0d4dc591ca2c90bc51a3ac883ce29), the [Timeout()](classBMidiLocalConsumer.md#a1331cbaa81327455ed000ec45dff0f27) hook is only called once. Note: the term "timeout" may be a little misleading; the hook will *always* be called, even if events are received in the mean time. Apparently, this facility is handy for dealing with early events.


Note that the event thread blocks on the consumer's port as long as no events arrive. By default no timeout is set, and as a result the thread blocks forever. Your call to [SetTimeout()](classBMidiLocalConsumer.md#a92d0d4dc591ca2c90bc51a3ac883ce29) doesn't change this. The new timeout value will go into effect the next time the thread tries to read from the port, i.e. after the first event has been received. If no event ever comes in, the [Timeout()](classBMidiLocalConsumer.md#a1331cbaa81327455ed000ec45dff0f27) hook will never be called. This also means that you cannot cancel a timeout once you have set it. To repeat, calling [SetTimeout()](classBMidiLocalConsumer.md#a92d0d4dc591ca2c90bc51a3ac883ce29) only takes effect after at least one new event has been received.


Parameters

| Parameter | Description |
| :--- | :--- |
| `when` | An absolute time that's measured against the system clock. |
| `data` | A pointer to a "cookie" that you can pass along to [Timeout()](classBMidiLocalConsumer.md#a1331cbaa81327455ed000ec45dff0f27). The data is not copied, so you must ensure that the pointer remains valid until [Timeout()](classBMidiLocalConsumer.md#a1331cbaa81327455ed000ec45dff0f27) is called. You typically delete the data inside [Timeout()](classBMidiLocalConsumer.md#a1331cbaa81327455ed000ec45dff0f27). |

---

### `SystemCommon()`

```cpp
void BMidiLocalConsumer::SystemCommon(uchar status, uchar data1, uchar data2, bigtime_t time)
```

Invoked when a System Common event is received. 


Not all data bytes are used for all common events. Unused bytes are set to 0.



**See also:** [BMidiLocalProducer::SpraySystemCommon()](classBMidiLocalProducer.md#a7e0de2eea30f60f75ef06a8bc03b853e)

---

### `SystemExclusive()`

```cpp
void BMidiLocalConsumer::SystemExclusive(void * data, size_t length, bigtime_t time)
```

Invoked when a System Exclusive event is received. 


The data does not include the sysex start and end control bytes (0xF0 and 0xF7), only the payload of the sysex message.


The data belongs to the Midi Kit and is only valid for the duration of this event. You may not modify or free it.



**See also:** [BMidiLocalProducer::SpraySystemExclusive()](classBMidiLocalProducer.md#af7aeb206b4e0b343d95f42e68db5d956)

---

### `SystemRealTime()`

```cpp
void BMidiLocalConsumer::SystemRealTime(uchar status, bigtime_t time)
```

Invoked when a Real Time event is received. 



**See also:** [BMidiLocalProducer::SpraySystemRealTime()](classBMidiLocalProducer.md#a776c12865641386d826145a37796bd54)

---

### `TempoChange()`

```cpp
void BMidiLocalConsumer::TempoChange(int32 beatsPerMinute, bigtime_t time)
```

Invoked when a Tempo Change event is received. 



**See also:** [BMidiLocalProducer::SprayTempoChange()](classBMidiLocalProducer.md#ae7302b78045f6e99a50bb43ec255b848)

---

### `Timeout()`

```cpp
void BMidiLocalConsumer::Timeout(void * data)
```

Hook function that is called per your own request. 



**See also:** [SetTimeout()](classBMidiLocalConsumer.md#a92d0d4dc591ca2c90bc51a3ac883ce29)

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMidiLocalConsumer.html).
