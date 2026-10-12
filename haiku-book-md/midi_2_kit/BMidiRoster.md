---
name: BMidiRoster
type: class
kit: midi_2_kit
brief: "Interface to the system-wide Midi Roster"
source: haiku-book
---

# BMidiRoster Class
**Kit/Group:** [MIDI 2 Kit](../midi_2_kit/group__midi2.md)

## Description

Interface to the system-wide Midi Roster. 


[BMidiRoster](classBMidiRoster.md) allows you to find available MIDI consumer and producer objects. You can locate these objects using the iterative [NextEndpoint()](classBMidiRoster.md#afbf8efb9cfac2ac8f16c7a399f23039b), [NextProducer()](classBMidiRoster.md#a314b7e6366c2e0bb561f15f5d508be38), and [NextConsumer()](classBMidiRoster.md#a6c42527bb3ed1651ca3918f7708d041a) methods or by requesting notification messages to be sent with [StartWatching()](classBMidiRoster.md#afe537ff3a6fc157e07436e7f62163622). Notification messages may contain object IDs which can be resolved using the [FindEndpoint()](classBMidiRoster.md#aa093ac8e2baf81b1fbaa3cdadf4adeab), [FindProducer()](classBMidiRoster.md#a8fbecc301ebc83a0439d021cb26e7795), and [FindConsumer()](classBMidiRoster.md#adb6d1d3d9eeb5de0d4e21e5d310eab36) methods.


The constructor and destructor of [BMidiRoster](classBMidiRoster.md) are private, which means that you cannot create or delete your own [BMidiRoster](classBMidiRoster.md) objects. Every application can have only one instance of [BMidiRoster](classBMidiRoster.md), which is automatically created the very first time you use a Midi Kit function. You can call [BMidiRoster](classBMidiRoster.md)'s functions like this: 


```cpp
producer = BMidiRoster::FindProducer(someID);
```

 Or using the slightly more annoying: 


```cpp
BMidiRoster* roster = BMidiRoster::MidiRoster();
if (roster != NULL)
{
    producer = roster->FindProducer(someID);
}
```

## Member List

### Static Public Member Functions

* `static BMidiConsumer *` [FindConsumer](#adb6d1d3d9eeb5de0d4e21e5d310eab36) (int32 id, bool localOnly=false) — Finds the consumer with the specified id.
* `static BMidiEndpoint *` [FindEndpoint](#aa093ac8e2baf81b1fbaa3cdadf4adeab) (int32 id, bool localOnly=false) — Returns the endpoint with the specified id.
* `static BMidiProducer *` [FindProducer](#a8fbecc301ebc83a0439d021cb26e7795) (int32 id, bool localOnly=false) — Finds the producer with the specified id.
* `static BMidiRoster *` [MidiRoster](#a258aff3bfde5f2d9f375db492e13b94b) () — Returns a pointer to the only instance of BMidiRoster.
* `static BMidiConsumer *` [NextConsumer](#a6c42527bb3ed1651ca3918f7708d041a) (int32 *id) — Returns the next consumer from the roster.
* `static BMidiEndpoint *` [NextEndpoint](#afbf8efb9cfac2ac8f16c7a399f23039b) (int32 *id) — Returns the next endpoint from the roster.
* `static BMidiProducer *` [NextProducer](#a314b7e6366c2e0bb561f15f5d508be38) (int32 *id) — Returns the next producer from the roster.
* `static status_t` [Register](#a6fcc9df349fdd3ce7f6daa0786fd4371) (BMidiEndpoint *endp) — Publishes an endpoint to other applications.
* `static void` [StartWatching](#afe537ff3a6fc157e07436e7f62163622) (const BMessenger *msngr) — Start receiving notifications from the Midi Roster.
* `static void` [StopWatching](#a3af22b3fbb289a1298c7725423d3cdbb) () — Stop receiving notifications from the Midi Roster.
* `static status_t` [Unregister](#a6e6f401eeaa94204701732f977663fd1) (BMidiEndpoint *endp) — Hides an endpoint from other applications.

## Detailed Member Documentation

### `FindConsumer()`

```cpp
BMidiConsumer * BMidiRoster::FindConsumer(int32 id, bool localOnly = false)
```

Finds the consumer with the specified *id*. 


Like [FindEndpoint()](classBMidiRoster.md#aa093ac8e2baf81b1fbaa3cdadf4adeab), but only looks for consumer endpoints. Returns `NULL` if no endpoint with that ID exists, or if that endpoint is not a consumer.



**See also:** [FindProducer](classBMidiRoster.md#a8fbecc301ebc83a0439d021cb26e7795)

---

### `FindEndpoint()`

```cpp
BMidiEndpoint * BMidiRoster::FindEndpoint(int32 id, bool localOnly = false)
```

Returns the endpoint with the specified *id*. 


[FindEndpoint()](classBMidiRoster.md#aa093ac8e2baf81b1fbaa3cdadf4adeab) will always find **any** local endpoints created by this application; they do not have to be published with [Register()](classBMidiRoster.md#a6fcc9df349fdd3ce7f6daa0786fd4371) first. If localOnly is false, [FindEndpoint()](classBMidiRoster.md#aa093ac8e2baf81b1fbaa3cdadf4adeab) also looks at remote endpoints, otherwise only local endpoints will be resolved. Returns NULL if no such endpoint could be found.


You should use a dynamic_cast to convert the [BMidiEndpoint](classBMidiEndpoint.md) into a producer or consumer: 


```cpp
BMidiEndpoint* endp = ...;
BMidiProducer* prod = NULL;
BMidiConsumer* cons = NULL;
if (endp->IsProducer())
{
    prod = dynamic_cast<BMidiProducer*>(endp);
}
else if (endp->IsConsumer())
{
    cons = dynamic_cast<BMidiConsumer*>(endp);
}
```

Remember that [FindEndpoint()](classBMidiRoster.md#aa093ac8e2baf81b1fbaa3cdadf4adeab) increments the endpoint's reference count, so you should always [Release()](classBMidiEndpoint.md#a368ed2bdb2b76afe1466daf0cc0e2b08) an endpoint when you are done with it: 


```cpp
BMidiEndpoint* endp = BMidiRoster::FindEndpoint(someID);
if (endp != NULL)
{
    ...do stuff with the endpoint...
    endp->Release();
}
```

---

### `FindProducer()`

```cpp
BMidiProducer * BMidiRoster::FindProducer(int32 id, bool localOnly = false)
```

Finds the producer with the specified *id*. 


Like [FindEndpoint()](classBMidiRoster.md#aa093ac8e2baf81b1fbaa3cdadf4adeab), but only looks for producer endpoints. Returns `NULL` if no endpoint with that ID exists, or if that endpoint is not a producer.



**See also:** [FindConsumer](classBMidiRoster.md#adb6d1d3d9eeb5de0d4e21e5d310eab36)

---

### `MidiRoster()`

```cpp
BMidiRoster * BMidiRoster::MidiRoster()
```

Returns a pointer to the only instance of [BMidiRoster](classBMidiRoster.md). 


There is no real reason use this function, since all [BMidiRoster](classBMidiRoster.md)'s public function are static.

---

### `NextConsumer()`

```cpp
BMidiConsumer * BMidiRoster::NextConsumer(int32 * id)
```

Returns the next consumer from the roster. 


Like [NextEndpoint()](classBMidiRoster.md#afbf8efb9cfac2ac8f16c7a399f23039b), but only returns consumer endpoints.



**See also:** [NextProducer](classBMidiRoster.md#a314b7e6366c2e0bb561f15f5d508be38)

---

### `NextEndpoint()`

```cpp
BMidiEndpoint * BMidiRoster::NextEndpoint(int32 * id)
```

Returns the next endpoint from the roster. 


The "next endpoint" means: the endpoint with the ID that follows *id*. So if you set id to 3, the first possible endpoint it returns is endpoint 4. No endpoint can have ID 0, so passing 0 gives you the first endpoint. If you pass `NULL` instead of an ID, [NextEndpoint()](classBMidiRoster.md#afbf8efb9cfac2ac8f16c7a399f23039b) always returns `NULL`. When the function returns, it sets *id* to the ID of the endpoint that was found. If no more endpoints exist, [NextEndpoint()](classBMidiRoster.md#afbf8efb9cfac2ac8f16c7a399f23039b) returns `NULL` and id is not changed. [NextEndpoint()](classBMidiRoster.md#afbf8efb9cfac2ac8f16c7a399f23039b) does **not** return locally created endpoints, even if they are [Register()](classBMidiRoster.md#a6fcc9df349fdd3ce7f6daa0786fd4371)'ed.


Usage example: 


```cpp
int32 id = 0;
BMidiEndpoint* endp;
while ((endp = BMidiRoster::NextEndpoint(&id)) != NULL)
{
    ... do something with endpoint ...
    endp->Release();  // don't forget!
}
```

 Remember that [NextEndpoint()](classBMidiRoster.md#afbf8efb9cfac2ac8f16c7a399f23039b) bumps the endpoint's reference count, so you should always [Release()](classBMidiEndpoint.md#a368ed2bdb2b76afe1466daf0cc0e2b08) it when you are done.

---

### `NextProducer()`

```cpp
BMidiProducer * BMidiRoster::NextProducer(int32 * id)
```

Returns the next producer from the roster. 


Like [NextEndpoint()](classBMidiRoster.md#afbf8efb9cfac2ac8f16c7a399f23039b), but only returns producer endpoints.



**See also:** [NextConsumer](classBMidiRoster.md#a6c42527bb3ed1651ca3918f7708d041a)

---

### `Register()`

```cpp
status_t BMidiRoster::Register(BMidiEndpoint * object)
```

Publishes an endpoint to other applications. 


Calls [BMidiEndpoint](classBMidiEndpoint.md)'s [Register()](classBMidiEndpoint.md#a6a818947b6098488a46e5a934d254186) method to publish an endpoint, which makes it visible to other applications.

---

### `StartWatching()`

```cpp
void BMidiRoster::StartWatching(const BMessenger * msngr)
```

Start receiving notifications from the Midi Roster. 


When you start watching, [BMidiRoster](classBMidiRoster.md) sends you notifications for all currently **published** `remote` endpoints, and all the current connections between them. (At this point, [BMidiRoster](classBMidiRoster.md) does not let you know about connections between unpublished endpoints, nor does it tell you anything about your local endpoints, even though they may be published.)


Thereafter, you'll receive notifications any time something important happens to an object. The application that performs these operations is itself not notified. The assumption here is that you already know about these changes, because you are the one that is performing them.


The notifications are BMessages with code B_MIDI_EVENT. You specify the [BMessenger](../application_kit/classBMessenger.md) that will be used to send these messages. Each message contains a field called be:op that describes the type of notification.


The "registered" and "unregistered" notifications are sent when a remote endpoint [Register()](classBMidiRoster.md#a6fcc9df349fdd3ce7f6daa0786fd4371)'s or [Unregister()](classBMidiRoster.md#a6e6f401eeaa94204701732f977663fd1)'s, respectively. You don't receive these notifications when you register or unregister your local endpoints, but the other apps will.



| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| be:op | int32 | `B_MIDI_REGISTERED` |
| be:id | int32 | id of the endpoint |
| be:type | string | "producer" or "consumer" |



| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| be:op | int32 | `B_MIDI_UNREGISTERED` |
| be:id | int32 | id of the endpoint |
| be:type | string | "producer" or "consumer" |


The "connected" and "disconnected" notifications are sent when a consumer [Connect()](classBMidiProducer.md#ae1fe6a25736a3f8eb154158429fc224a)'s to a producer, or when they [Disconnect()](classBMidiProducer.md#a7f68b65fd703766a0fccb5d9535ea6ed). You will receive these notifications when **any** two endpoints connect or disconnect, even if they are not published. (The purpose of which is debatable.) You won't receive the notifications if you are the one making the connection, even if both endpoints are remote. You **will** be notified when another app connects one of your published endpoints. 


| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| be:op | `int32` | `B_MIDI_CONNECTED` |
| be:producer | `int32` | id of the connector |
| be:consumer | `int32` | id of the connectee |



| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| be:op | `int32` | `B_MIDI_DISCONNECTED` |
| be:producer | `int32` | id of the connector |
| be:consumer | int32 | id of the connectee |


the following notifications are sent when an endpoint's attributes are changed. you receive these notifications only if another application is changing one of its published endpoints.



| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| be:op | `int32` | `B_MIDI_CHANGED_NAME` |
| be:id | `int32` | id of the endpoint |
| be:type | string | "producer" or "consumer" |
| be:name | string | the endpoint's new name |



| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| be:op | `int32` | `B_MIDI_CHANGED_LATENCY` |
| be:id | `int32` | id of the endpoint |
| be:type | string | "producer" or "consumer" |
| be:latency | int64 | the new latency (microseconds) |



| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| be:op | int32 | `B_MIDI_CHANGED_PROPERTIES` |
| be:id | `int32` | id of the endpoint |
| be:type | string | "producer" or "consumer" |
| be:properties | bmessage | the new properties |


Typical usage example:



```cpp
void MyView::AttachedToWindow()
{
 BMessenger msgr(this);
 BMidiRoster::StartWatching(&msgr);
}
void MyView::MessageReceived(BMessage* msg)
{
 switch (msg->what)
    {
 case B_MIDI_EVENT:
            HandleMidiEvent(msg);
 break;
 default:
            super::MessageReceived(msg);
 break;
    }
}
```

For the possible midi options, see BMidiOp

---

### `StopWatching()`

```cpp
void BMidiRoster::StopWatching()
```

Stop receiving notifications from the Midi Roster. 



**See also:** [StartWatching()](classBMidiRoster.md#afe537ff3a6fc157e07436e7f62163622)

---

### `Unregister()`

```cpp
status_t BMidiRoster::Unregister(BMidiEndpoint * object)
```

Hides an endpoint from other applications. 


Calls [BMidiEndpoint](classBMidiEndpoint.md)'s [Unregister()](classBMidiEndpoint.md#ad60d3fd6a9706a63f57851acf84db042) method to hide a previously published endpoint from other applications.

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMidiRoster.html).
