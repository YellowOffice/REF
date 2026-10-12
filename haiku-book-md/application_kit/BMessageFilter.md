---
name: BMessageFilter
type: class
kit: application_kit
brief: "Describes a message filter for BLooper and BHandler"
source: haiku-book
---

# BMessageFilter Class
**Kit/Group:** [Application Kit](../application_kit/group__app.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Describes a message filter for [BLooper](classBLooper.md) and [BHandler](classBHandler.md). 


Objects of this class serve as a description of properties that incoming messages should have in order to be processed by a handler or a looper. [BMessageFilter](classBMessageFilter.md) provides three default filter criteria, the `what` constant, the [message_source](MessageFilter_8h.md#a4d5a65f8d934511387e0cd57dccbfce2) and the type of message_delivery, and an extendible [filter_hook](MessageFilter_8h.md#a35663faa91226effa30d66143466b489).


[BMessageFilter](classBMessageFilter.md)'s standard filter criteria can be extended in two ways:


1. Specify a [filter_hook](MessageFilter_8h.md#a35663faa91226effa30d66143466b489). This is a static function that takes a message and a pointer to a [BHandler](classBHandler.md) as arguments, and allows you to accept or reject the message, and even redirect it to a specific [BHandler](classBHandler.md).

2. Subclass the [BMessageFilter](classBMessageFilter.md) class and override the [Filter()](classBMessageFilter.md#a530d9898fb51e57e93bf674b8e13bcb6) function. This has the same capabilities as using a [filter_hook](MessageFilter_8h.md#a35663faa91226effa30d66143466b489), but it allows cleaner code (in some cases). Both methods have their merits, but please remember that you have to choose which one you want to use, since you can't use both. The order of processing the criteria is in this order: the source, the delivery method, the filter hook and then the overrided [Filter()](classBMessageFilter.md#a530d9898fb51e57e93bf674b8e13bcb6) method. Additionally, if a [filter_hook](MessageFilter_8h.md#a35663faa91226effa30d66143466b489) is registered, the [Filter()](classBMessageFilter.md#a530d9898fb51e57e93bf674b8e13bcb6) method will not be called.



The [BMessageFilter](classBMessageFilter.md) objects are used in two different classes. They can be associated with specific BHandlers. Using the [BHandler::AddFilter()](classBHandler.md#a862bea548363faac6f883b348cbed838) and the [BHandler::SetFilterList()](classBHandler.md#a503344dc801858e1f5f419be3919e9cf) methods, you can add filters to the filter list. It is also possible to associate filters with BLoopers. In that case, all incoming messages of that looper are checked against the criteria. To perform filtering in loopers, have a look at the [BLooper::AddCommonFilter()](classBLooper.md#a25adc41bdfd741e9c82d2b469a5086b0) and the [BLooper::SetCommonFilterList()](classBLooper.md#a9b39e686873763cc6491c91f77b177b7) methods.


An example of a filter that selects on the default criteria: 


```cpp
// Our window does not handle drop events.
BMessageFilter *filter = new BMessageFilter(B_PROGRAMMED_DELIVERY, B_ANY_SOURCE);
window->AddCommonFilter(filter);
```

An example of a filter that only allows one type of message: 


```cpp
BMessageFilter *filter = new BMessageFilter(kHappyMessages);
handler->AddFilter(filter);
```

An example of a [filter_hook](MessageFilter_8h.md#a35663faa91226effa30d66143466b489): 


```cpp
// The handler depends on the what code of a message
filter_result
ScreenMessage(BMessage* message, BHandler** target, BMessageFilter* filter)
{
 switch (message->what) {
 case kTcpEvent:
            target = &fTcpHandler;
 return B_DISPATCH_MESSAGE;
 case kUdpEvent:
            target = &fUdpHandler;
 return B_DISPATCH_MESSAGE;
    }
 
 return B_SKIP_MESSAGE;
}
 
BMessageFilter *filter = new BMessageFilter(B_ANY_DELIVERY, B_ANY_SOURCE, ScreenMessage);
looper->AddCommonFilter(filter);
```

The two classes that use [BMessageFilter](classBMessageFilter.md) are [BLooper](classBLooper.md) and [BHandler](classBHandler.md). In the general messaging introduction, there is also a section on [handling messages](app_messaging.md#app-messaging-receiving).



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BMessageFilter](#a9f39d38ba0af5b36602a891dc4874c30) (const BMessageFilter &filter) — Copy constructor. Copy the criteria from another object.
* [BMessageFilter](#a24aec9732c406ba5e05e1e45ebde22cf) (const BMessageFilter *filter) — Create a new object based on criteria of another object.
* [BMessageFilter](#a9aea3db944fc4ef4790a8e861e5aaec2) (message_delivery delivery, message_source source, filter_hook func=NULL) — Construct a new object that filters on delivery method and message source.
* [BMessageFilter](#a11be578c622a6e96f20a96f88cff7c4d) (message_delivery delivery, message_source source, uint32 what, filter_hook func=NULL) — Construct a new object that filters on delivery method, message source and specific message constants.
* [BMessageFilter](#af546360211fffc0cd16ec3eefeaff8a5) (uint32 what, filter_hook func=NULL) — Construct a new object that filters on a message constant.
* `virtual` [~BMessageFilter](#aa75c113ae45ab87e89782639c95e16b5) () — Destructor. Does nothing.
* `uint32` [Command](#a62142f07062ced2b096e4de9a76e05ce) () const — Return the accepted message constant.
* `virtual filter_result` [Filter](#a530d9898fb51e57e93bf674b8e13bcb6) (BMessage *message, BHandler **_target) — Filter the message according to custom criteria.
* `bool` [FiltersAnyCommand](#af0723b7033a806a1f0c21eb319a6656e) () const — Return whether or not this filter has a message command criterium.
* `BLooper *` [Looper](#af6b140130183142c94afdb397a0a238f) () const — Return the looper this filter is associated with.
* `message_delivery` [MessageDelivery](#a8ea42c862ce9358566a3ba47e1dbfa53) () const — Return the message_delivery criterium of this filter.
* `message_source` [MessageSource](#adc41e6c0cb98bc3ea5564f04c1a74eec) () const — Return the message_source criterium of this filter.
* `BMessageFilter &` [operator=](#a5b6cd31021809533ded7d5af25b1d5b1) (const BMessageFilter &from) — Assignment operator. Copies criteria from another filter.

## Detailed Member Documentation

### `BMessageFilter()`

```cpp
BMessageFilter::BMessageFilter(uint32 inWhat, filter_hook func = NULL)
```

Construct a new object that filters on a message constant. 


You can also specify a [filter_hook](MessageFilter_8h.md#a35663faa91226effa30d66143466b489), if you want apply custom filter criteria.



**See also:** [BMessageFilter(message_delivery, message_source, filter_hook)](classBMessageFilter.md#a9aea3db944fc4ef4790a8e861e5aaec2)



**Since:** BeOS R3

---

### `BMessageFilter()`

```cpp
BMessageFilter::BMessageFilter(message_delivery delivery, message_source source, filter_hook func = NULL)
```

Construct a new object that filters on delivery method and message source. 


You can also specify a [filter_hook](MessageFilter_8h.md#a35663faa91226effa30d66143466b489), if you want to apply custom filter criteria.



**See also:** [BMessageFilter(uint32 what,filter_hook)](classBMessageFilter.md#af546360211fffc0cd16ec3eefeaff8a5)



**Since:** BeOS R3

---

### `BMessageFilter()`

```cpp
BMessageFilter::BMessageFilter(message_delivery delivery, message_source source, uint32 inWhat, filter_hook func = NULL)
```

Construct a new object that filters on delivery method, message source and specific message constants. 


You can also specify a [filter_hook](MessageFilter_8h.md#a35663faa91226effa30d66143466b489), if you want to apply custom filter criteria.



**See also:** [BMessageFilter(uint32 what,filter_hook)](classBMessageFilter.md#af546360211fffc0cd16ec3eefeaff8a5)



**Since:** BeOS R3

---

### `BMessageFilter()`

```cpp
BMessageFilter::BMessageFilter(const BMessageFilter & filter)
```

Copy constructor. Copy the criteria from another object. 



**Since:** BeOS R3

---

### `BMessageFilter()`

```cpp
BMessageFilter::BMessageFilter(const BMessageFilter * filter)
```

Create a new object based on criteria of another object. 



**Since:** BeOS R3

---

### `~BMessageFilter()`

```cpp
BMessageFilter::~BMessageFilter()
```

Destructor. Does nothing. 



**Since:** BeOS R3

---

### `Command()`

```cpp
uint32 BMessageFilter::Command()const
```

Return the accepted message constant. 


This method returns zero (0) in case this filter does not filter based on the message constant.



**See also:** [FiltersAnyCommand() const](classBMessageFilter.md#af0723b7033a806a1f0c21eb319a6656e)



**Since:** BeOS R3

---

### `Filter()`

```cpp
filter_result BMessageFilter::Filter(BMessage * message, BHandler ** target)
```

Filter the message according to custom criteria. 


The default implementation of this method always returns `B_DISPATCH_MESSAGE`. You can override this method in subclasses to suit your own criteria. You receive two arguments.


Parameters

| Parameter | Description |
| :--- | :--- |
| `message` | The message that needs to be filtered. |
| `target` | If you want to, you can specify a handler that should handle this message. Note that you do have to pass a handler that is associated with the looper that received the message. |





**Returns:** You should return `B_DISPATCH_MESSAGE` in case the message passes the tests, or `B_SKIP_MESSAGE` in case the message does not pass.



**Since:** BeOS R3

---

### `FiltersAnyCommand()`

```cpp
bool BMessageFilter::FiltersAnyCommand()const
```

Return whether or not this filter has a message command criterium. 



**See also:** [Command() const](classBMessageFilter.md#a62142f07062ced2b096e4de9a76e05ce)



**Since:** BeOS R3

---

### `Looper()`

```cpp
BLooper * BMessageFilter::Looper()const
```

Return the looper this filter is associated with. 



**Since:** BeOS R3

---

### `MessageDelivery()`

```cpp
message_delivery BMessageFilter::MessageDelivery()const
```

Return the message_delivery criterium of this filter. 



**Since:** BeOS R3

---

### `MessageSource()`

```cpp
message_source BMessageFilter::MessageSource()const
```

Return the message_source criterium of this filter. 



**Since:** BeOS R3

---

### `operator=()`

```cpp
BMessageFilter & BMessageFilter::operator=(const BMessageFilter & from)
```

Assignment operator. Copies criteria from another filter. 



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBMessageFilter.html).
