---
name: BMidiEndpoint
type: class
kit: midi_2_kit
brief: "Base class for all MIDI endpoints"
source: haiku-book
---

# BMidiEndpoint Class
**Kit/Group:** [MIDI 2 Kit](../midi_2_kit/group__midi2.md)

## Description

Base class for all MIDI endpoints. 


[BMidiEndpoint](classBMidiEndpoint.md) is the abstract base class that represents either a producer or consumer endpoint. It may be used to obtain the state, name, properties, or system-wide ID of the object. [BMidiEndpoint](classBMidiEndpoint.md) also provides the ability to change the name and properties of endpoints that were created locally.


Remember, you cannot call the destructor of [BMidiEndpoint](classBMidiEndpoint.md) and its subclasses directly. Endpoint objects are destructed automatically when their reference count drops to zero. If necessary, the destructor of a local endpoint first breaks off any connections and [Unregister()](classBMidiEndpoint.md#ad60d3fd6a9706a63f57851acf84db042)'s the endpoint before it is deleted. However, for good style and bonus points you should really [Disconnect()](classBMidiProducer.md#a7f68b65fd703766a0fccb5d9535ea6ed) and [Unregister()](classBMidiEndpoint.md#ad60d3fd6a9706a63f57851acf84db042) the object yourself and not rely on the destructor to do this.

## Member List

### Public Member Functions

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

### `Acquire()`

```cpp
status_t BMidiEndpoint::Acquire()
```

Increments the endpoint's reference count. 


Each [BMidiEndpoint](classBMidiEndpoint.md) has a reference count associated with it, so that [BMidiRoster](classBMidiRoster.md) can do proper bookkeeping. [Acquire()](classBMidiEndpoint.md#a504efce89310e4473c4a9ae77da7a641) increments this reference count, and [Release()](classBMidiEndpoint.md#a368ed2bdb2b76afe1466daf0cc0e2b08) decrements it. Once the count reaches zero, the endpoint is deleted.


When you are done with the endpoint, whether local or remote, you should always [Release()](classBMidiEndpoint.md#a368ed2bdb2b76afe1466daf0cc0e2b08) it!


Upon construction, local endpoints start with a reference count of 1. Any objects you obtain from [BMidiRoster](classBMidiRoster.md) using the NextXXX() or FindXXX() functions have their reference counts incremented in the process. If you forget to call [Release()](classBMidiEndpoint.md#a368ed2bdb2b76afe1466daf0cc0e2b08), the objects won't be properly cleaned up and you'll make a fool out of yourself.


After you [Release()](classBMidiEndpoint.md#a368ed2bdb2b76afe1466daf0cc0e2b08) an object, you are advised not to use it any further. If you do, your app will probably crash. That also happens if you [Release()](classBMidiEndpoint.md#a368ed2bdb2b76afe1466daf0cc0e2b08) an object too many times.


Typically, you don't need to call [Acquire()](classBMidiEndpoint.md#a504efce89310e4473c4a9ae77da7a641), unless you have two disparate parts of your application working with the same endpoint, and you don't want to have to keep track of who needs to [Release()](classBMidiEndpoint.md#a368ed2bdb2b76afe1466daf0cc0e2b08) the endpoint. Now you simply have both of them release it.



**Returns:** Always returns B_OK



**See also:** [Release()](classBMidiEndpoint.md#a368ed2bdb2b76afe1466daf0cc0e2b08)

---

### `GetProperties()`

```cpp
status_t BMidiEndpoint::GetProperties(BMessage * props)const
```

Reads the properties of the endpoint. 


Usage example:



```cpp
BMessage props;
if (endpoint->GetProperties(&props) == B_OK)
{
    ...examine the contents of the message...
}
```

Note that [GetProperties()](classBMidiEndpoint.md#a5c6c8dc7f451e7c908df05319f24a64f) overwrites the contents of your [BMessage](../application_kit/classBMessage.md).



**See also:** [SetProperties()](classBMidiEndpoint.md#a58cf2c701ba336b640067db743ba9746)

---

### `ID()`

```cpp
int32 BMidiEndpoint::ID()const
```

Returns the ID of the endpoint. 


An ID uniquely identifies an endpoint in the system. The ID is a signed 32-bit number that is assigned by the Midi Server when the endpoint is created. (So even if a local endpoint is not published, it still has a unique ID.) Valid IDs range from 1 to 0x7FFFFFFF, the largest value an int32 can have. 0 and negative values are **not** valid IDs.

---

### `IsConsumer()`

```cpp
bool BMidiEndpoint::IsConsumer()const
```

Determines whether this endpoint is a [BMidiConsumer](classBMidiConsumer.md). 


If it is, you can use a dynamic_cast to convert this object into a consumer:



```cpp
if (endp->IsConsumer())
{
 BMidiConsumer* cons = dynamic_cast<BMidiConsumer*>(endp);
 
    ....
 
}
```

---

### `IsLocal()`

```cpp
bool BMidiEndpoint::IsLocal()const
```

Determines whether this endpoint represents a local object. 


An endpoint is "local" when it is created by this application; in other words, a [BMidiLocalConsumer](classBMidiLocalConsumer.md) or [BMidiLocalProducer](classBMidiLocalProducer.md).

---

### `IsPersistent()`

```cpp
bool BMidiEndpoint::IsPersistent()const
```

Not used. 


The purpose of this function is unclear, and as a result it doesn't do anything in the Haiku Midi Kit implementation.



**Returns:** `false` always.

---

### `IsProducer()`

```cpp
bool BMidiEndpoint::IsProducer()const
```

Determines whether this endpoint is a [BMidiProducer](classBMidiProducer.md). 


If it is, you can use a dynamic_cast to convert this object into a producer:



```cpp
if (endp->IsProducer())
{
 BMidiProducer* prod = dynamic_cast<BMidiProducer*>(endp);
 
    ....
 
}
```

---

### `IsRemote()`

```cpp
bool BMidiEndpoint::IsRemote()const
```

Determines whether this endpoint is a proxy for a remote object. 


An endpoint is "remote" when it is created by another application. Obviously, the remote object is [Register()](classBMidiEndpoint.md#a6a818947b6098488a46e5a934d254186)'ed as well, otherwise you would not be able to see it.

---

### `IsValid()`

```cpp
bool BMidiEndpoint::IsValid()const
```

Determines whether the endpoint still exists. 


Suppose you obtained a proxy object for a remote endpoint by querying the [BMidiRoster](classBMidiRoster.md). What if the application that published this endpoint quits, or less drastically, [Unregister()](classBMidiEndpoint.md#ad60d3fd6a9706a63f57851acf84db042)'s that endpoint? Even though you still have a [BMidiEndpoint](classBMidiEndpoint.md) proxy object, the real endpoint no longer exists. You can use [IsValid()](classBMidiEndpoint.md#a0c9f93e72f5302f6f0c631e5a4f0ddb2) to check for this.


Don't worry, operations on invalid objects, such as [GetProperties()](classBMidiEndpoint.md#a5c6c8dc7f451e7c908df05319f24a64f), will return an error code (typically B_ERROR), but not cause a crash. Local objects are always are considered to be valid, even if you did not [Register()](classBMidiEndpoint.md#a6a818947b6098488a46e5a934d254186) them. (The only time a local endpoint is not valid is when there was a problem constructing it.)


If the application that created the remote endpoint crashes, then there is no guarantee that the Midi Server immediately recognizes this. In that case, [IsValid()](classBMidiEndpoint.md#a0c9f93e72f5302f6f0c631e5a4f0ddb2) may still return true. Eventually, the stale endpoint will be removed from the roster, though. From then on, [IsValid()](classBMidiEndpoint.md#a0c9f93e72f5302f6f0c631e5a4f0ddb2) correctly returns `false`.

---

### `Name()`

```cpp
const char * BMidiEndpoint::Name()const
```

Returns the name of the endpoint. 


The function never returns NULL. If you created a local endpoint by passing a `NULL` name into its constructor (or passing no name, which is the same thing), then [Name()](classBMidiEndpoint.md#a685e4d64cfbf56e30c7a3c5849fc72d8) will return an empty string, not `NULL`.



**See also:** [SetName()](classBMidiEndpoint.md#afa167950f7b60558712224798f7e50aa)

---

### `Register()`

```cpp
status_t BMidiEndpoint::Register()
```

Publishes the endpoint on the roster. 


MIDI objects created by an application are invisible to other applications until they are published. To publish an object use the [Register()](classBMidiEndpoint.md#a6a818947b6098488a46e5a934d254186) method. The corresponding [Unregister()](classBMidiEndpoint.md#ad60d3fd6a9706a63f57851acf84db042) method will cause an object to once again become invisible to remote applications.


[BMidiRoster](classBMidiRoster.md) also has [Register()](classBMidiEndpoint.md#a6a818947b6098488a46e5a934d254186) and [Unregister()](classBMidiEndpoint.md#ad60d3fd6a9706a63f57851acf84db042) methods. You may also use those methods to publish or hide your endpoints; both do the same thing.


Although it is considered bad style, calling [Register()](classBMidiEndpoint.md#a6a818947b6098488a46e5a934d254186) on local endpoints that are already registered won't mess things up. The Midi Server will simply ignore your request. Likewise for [Unregister()](classBMidiEndpoint.md#ad60d3fd6a9706a63f57851acf84db042)'ing more than once. Attempts to [Register()](classBMidiEndpoint.md#a6a818947b6098488a46e5a934d254186) or [Unregister()](classBMidiEndpoint.md#ad60d3fd6a9706a63f57851acf84db042) remote endpoints will fail, of course.


If you are [watching](classBMidiRoster.md#afe537ff3a6fc157e07436e7f62163622), you will **not** receive notifications for any local endpoints you register or unregister. Of course, other applications *will* be notified about your endpoints.


Existing connections will not be broken when an object is unregistered, but future remote connections will be denied. When objects are destroyed, they automatically become unregistered.



**Returns:** B_OK on success, or an error code (typically `B_ERROR`) if something went wrong.



**See also:** [Unregister()](classBMidiEndpoint.md#ad60d3fd6a9706a63f57851acf84db042)

---

### `Release()`

```cpp
status_t BMidiEndpoint::Release()
```

Decrements the endpoint's reference count. 



**Returns:** Always returns B_OK



**See also:** [Acquire()](classBMidiEndpoint.md#a504efce89310e4473c4a9ae77da7a641)

---

### `SetName()`

```cpp
void BMidiEndpoint::SetName(const char * name)
```

Changes the name of the endpoint. 


Names don't have to be unique, but it is recommended that you give any endpoints you publish meaningful and unique names, so users can easily recognize what each endpoint does. There is no limit to the size of endpoint names.


Even though you can call this function on both remote and local objects, you are only allowed to change the names of local endpoints; [SetName()](classBMidiEndpoint.md#afa167950f7b60558712224798f7e50aa) calls on remote endpoints are ignored.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The new name. If you pass `NULL` the name won't be changed. |





**See also:** [Name()](classBMidiEndpoint.md#a685e4d64cfbf56e30c7a3c5849fc72d8)

---

### `SetProperties()`

```cpp
status_t BMidiEndpoint::SetProperties(const BMessage * props)
```

Changes the properties of the endpoint. 


Endpoints can have properties, which is any kind of information that might be useful to associate with a MIDI object. The properties are stored in a [BMessage](../application_kit/classBMessage.md).


Usage example:



```cpp
BMessage props;
if (endpoint->GetProperties(&props) == B_OK)
{
    ...add data to the message...
    endpoint->SetProperties(&props);
}
```

You are only allowed to call [SetProperties()](classBMidiEndpoint.md#a58cf2c701ba336b640067db743ba9746) on a local object.


Properties should follow a protocol, so different applications will know how to read each other's properties. The current protocol is very limited – it only allows you to associate icons with your endpoints. Be planned to publish a more complete protocol that included additional information, such as vendor/model names, copyright/version info, category, etc., but they never got around to it.



| Col 1 | Col 2 |
| :--- | :--- |
| property | Vector icon (raw data) |
| field name | "icon" |
| field type | 'VICN' |


This vector icon is available under Haiku only, and comes as raw data, not a [BBitmap](../interface_kit/classBBitmap.md). Before being able to display it, you first must render the vector icon in the size of your choice.



| Col 1 | Col 2 |
| :--- | :--- |
| property | Large (32x32) icon |
| field name | "be:large_icon" |
| field type | 'ICON' |



| Col 1 | Col 2 |
| :--- | :--- |
| property | Small (16x16) icon |
| field name | "be:mini_icon" |
| field type | 'MICN' |


The MidiUtil package (downloadable from [https://www.haiku-os.org/files/MidiUtil-1_0.zip](https://www.haiku-os.org/files/MidiUtil-1_0.zip)) contains a number of convenient functions to associate icons with endpoints, so you don't have to write that code all over again.



**See also:** [GetProperties()](classBMidiEndpoint.md#a5c6c8dc7f451e7c908df05319f24a64f)

---

### `Unregister()`

```cpp
status_t BMidiEndpoint::Unregister()
```

Hides the endpoint from the roster/. 



**See also:** [Register()](classBMidiEndpoint.md#a6a818947b6098488a46e5a934d254186)

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMidiEndpoint.html).
