---
name: BMidiConsumer
type: class
kit: midi_2_kit
brief: "Receives MIDI events from a producer"
source: haiku-book
---

# BMidiConsumer Class
**Kit/Group:** [MIDI 2 Kit](../midi_2_kit/group__midi2.md)

## Description

Receives MIDI events from a producer. 


A consumer is an object that knows how to deal with incoming MIDI events. A consumer can be connected to multiple producers at the same time. There is no way to find out which producers are connected to this consumer just by looking at the [BMidiConsumer](classBMidiConsumer.md) object; you will have to consult [BMidiRoster](classBMidiRoster.md) for that.


A [BMidiConsumer](classBMidiConsumer.md) either represents a local consumer, i.e. a class extending from [BMidiLocalConsumer](classBMidiLocalConsumer.md), or is a proxy for a remote object published by another app.

## Member List

### Public Member Functions

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

### `Latency()`

```cpp
bigtime_t BMidiConsumer::Latency()const
```

Returns the latency of this consumer. 


The latency is measured in microseconds. Producers should attempt to get MIDI events to this consumer by *(when - latency)*. You do this by subtracting the latency from the performance time when you spray the events (provided that you spray these events ahead of time, of course).


You cannot *set* the latency on a [BMidiConsumer](classBMidiConsumer.md), only on a [BMidiLocalConsumer](classBMidiLocalConsumer.md).


The latency issue gets slightly more complicated when multiple endpoints are chained together, as in the following picture:


+-------+     +-------------+     +-------+
|       |     |             |     |       |
| prodA |---->| consB prodB |---->| consC |
|       |     |             |     |       |
+-------+     +-------------+     +-------+
  appA          appB (filter)       appC
Suppose consC has 200ms latency, and consB has 100ms latency. If consB simply reports 100ms, then prodA will schedule its events for (t - 100), which is really 200ms too late. (Of course, producers send out their events as soon as possible, so depending on the load of the system, everything may work out just fine.)


ConsB should report the latency of the consumer that is hooked up to its output, consC, in addition to its own latency. In other words, the full downstream latency. So, the reported latency in this case would be 300ms. This also means that appB should change the latency of consB when prodB makes or breaks a connection, and when consC reports a latency change. (If multiple consumers are connected to prodB, you should take the slowest one.) Unfortunately, the Midi Kit provides no easy mechanism for doing any of this, so you are on your own here.

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMidiConsumer.html).
