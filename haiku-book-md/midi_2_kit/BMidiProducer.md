---
name: BMidiProducer
type: class
kit: midi_2_kit
brief: "Streams MIDI events to connected consumers"
source: haiku-book
---

# BMidiProducer Class
**Kit/Group:** [MIDI 2 Kit](../midi_2_kit/group__midi2.md)

## Description

Streams MIDI events to connected consumers. 


A producer is an object that generate a stream of MIDI events. Each producer has a list of [BMidiConsumer](classBMidiConsumer.md) objects to which it is connected, and may be asked to connect to or disconnect from a [BMidiConsumer](classBMidiConsumer.md). A producer can spray its events to multiple consumers at the same time. A [BMidiProducer](classBMidiProducer.md) either represents a local producer, i.e. a class extending from [BMidiLocalProducer](classBMidiLocalProducer.md), or is a proxy for a remote object published by another app.

## Member List

### Public Member Functions

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

### `Connect()`

```cpp
status_t BMidiProducer::Connect(BMidiConsumer * cons)
```

Connects a consumer to this producer. 


Establishes a connection between this producer and the specified consumer endpoint. From now on, any events that this producer sprays will be sent to that consumer. You may connect multiple consumers to a producer.



**Returns:** B_OK on success, or an error code when the connection could not be established. If the consumer is a proxy for a remote object and that object no longer exists, [Connect()](classBMidiProducer.md#ae1fe6a25736a3f8eb154158429fc224a) returns B_ERROR. It also returns `B_ERROR` if you try to connect the same producer and consumer more than once.



**See also:** [Disconnect()](classBMidiProducer.md#a7f68b65fd703766a0fccb5d9535ea6ed)

---

### `Connections()`

```cpp
BList * BMidiProducer::Connections()const
```

Returns a list with all connected consumers. 


Returns a [BList](../support_kit/classBList.md) with pointers to [BMidiEndpoint](classBMidiEndpoint.md) objects for all consumers that are connected to this producer. You can examine the contents of the list as follows: 


```cpp
BList* list = prod->Connections();
for (int32 t = 0; t < list->CountItems(); ++t)
{
 BMidiEndpoint* endp = (BMidiEndpoint*) list->ItemAt(t);
    ...do stuff...
    endp->Release();  // yes, here too!
}
delete list;
```

 Every time you call this function, a new [BList](../support_kit/classBList.md) is allocated. The caller (that is you) is responsible for freeing this list. The [BMidiEndpoint](classBMidiEndpoint.md) objects in the list have their reference counts bumped, so you need to [Release()](classBMidiEndpoint.md#a368ed2bdb2b76afe1466daf0cc0e2b08) them before you delete the list or they will go all leaky on you.

---

### `Disconnect()`

```cpp
status_t BMidiProducer::Disconnect(BMidiConsumer * cons)
```

Disconnects a consumer from this producer. 


Terminates the connection between this producer and the specified consumer endpoint. From now on, any events that this producer sprays no longer go to that consumer.



**Returns:** B_OK on success, or an error code if there was no connection to break



**See also:** [Connect()](classBMidiProducer.md#ae1fe6a25736a3f8eb154158429fc224a)

---

### `IsConnected()`

```cpp
bool BMidiProducer::IsConnected(BMidiConsumer * cons)const
```

Determines whether a consumer is connected to this producer. 



**See also:** [Connect()](classBMidiProducer.md#ae1fe6a25736a3f8eb154158429fc224a)

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMidiProducer.html).
