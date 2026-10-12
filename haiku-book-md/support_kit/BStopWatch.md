---
name: BStopWatch
type: class
kit: support_kit
brief: "A simple class used to time events like a stop watch"
source: haiku-book
---

# BStopWatch Class
**Kit/Group:** [Support Kit](../support_kit/group__support.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

A simple class used to time events like a stop watch. 


The interface of this class is designed to behave like a physical stop watch. It is useful for debugging parts of your code acting as a quick and dirty profiler.


To use this class first create a [BStopWatch](classBStopWatch.md) object, this starts the timer going. You may call [Suspend()](classBStopWatch.md#a375f8b983fb8bfd6afa91fc8c4aba6e9) and [Resume()](classBStopWatch.md#add07ccf4401109f0f88974ea3063d16c) to start and stop the stop watch. Call [ElapsedTime()](classBStopWatch.md#ab4978bf1acb340342bc4754745f8f255) to get the current timer count at any time. You may call [Lap()](classBStopWatch.md#aa3b2d59dc0f5581912b3b2767de4d1db) to start a new lap (up to 10 laps are supported) or call [Reset()](classBStopWatch.md#ad51af987bd2e704609d45fb31817d226) to reset the timer back to 0 clearing all lap info. When the object is destroyed the timing information is streamed to standard out unless you set the *silent* parameter to `true` in the constructor.



**Since:** BeOS R3

## Member List

### Public Member Functions

* [BStopWatch](#aabb1a2f52cf9d2da34304c84bbb3a360) (const char *name, bool silent=false) — Constructs a BStopWatch object and starts the timer.
* `virtual` [~BStopWatch](#a1765b93b121693f2afcb5e27168d435b) () — Destroys the object stopping the timer.
* `bigtime_t` [ElapsedTime](#ab4978bf1acb340342bc4754745f8f255) () const — Gets the elapsed time the object has counted.
* `bigtime_t` [Lap](#aa3b2d59dc0f5581912b3b2767de4d1db) () — Starts a new timer lap.
* `const char *` [Name](#a5a38a8f863850e3cf3a2d9be9e8e5dbe) () const — Returns the name of the stop watch.
* `void` [Reset](#ad51af987bd2e704609d45fb31817d226) () — Restarts the timer.
* `void` [Resume](#add07ccf4401109f0f88974ea3063d16c) () — Resume the timer from a suspended state.
* `void` [Suspend](#a375f8b983fb8bfd6afa91fc8c4aba6e9) () — Suspend the timer.

## Detailed Member Documentation

### `BStopWatch()`

```cpp
BStopWatch::BStopWatch(const char * name, bool silent = false)
```

Constructs a [BStopWatch](classBStopWatch.md) object and starts the timer. 


This method creates a new [BStopWatch](classBStopWatch.md) object. As soon as the object is created the timer starts ticking away.


If you are profiling your code with this class pass `false` to the *silent* parameter to cause the elapsed time information to be streamed to standard output when the object is destroyed.


Parameters

| Parameter | Description |
| :--- | :--- |
| `name` | The name of the stop watch. You may pass `NULL` to create an anonymous stop watch. |
| `silent` | Pass `true` to suppress time information from streaming to standard output when the object is destroyed. |





**Since:** BeOS R3

---

### `~BStopWatch()`

```cpp
BStopWatch::~BStopWatch()
```

Destroys the object stopping the timer. 


If *silent* was set to `false` in the constructor then this method will print elapsed time information to standard output.



**Since:** BeOS R3

---

### `ElapsedTime()`

```cpp
bigtime_t BStopWatch::ElapsedTime()const
```

Gets the elapsed time the object has counted. 



**Returns:** The elapsed time in microseconds.



**Since:** BeOS R3

---

### `Lap()`

```cpp
bigtime_t BStopWatch::Lap()
```

Starts a new timer lap. 


In the current implementation you are unable to actually retrieve the timings of each lap, they are only printed to the standard output when the object is destroyed. This makes the [Lap()](classBStopWatch.md#aa3b2d59dc0f5581912b3b2767de4d1db) method only usable when doing some types of profiling.



> [!NOTE]
> The current implementation is limited to 10 laps. The value returned is the time that has passed since the timer was last started (not the time that has passed since the last lap). Any call to [Lap()](classBStopWatch.md#aa3b2d59dc0f5581912b3b2767de4d1db) beyond the 10th lap will overwrite the last value. Calling [Lap()](classBStopWatch.md#aa3b2d59dc0f5581912b3b2767de4d1db) while the timer is suspended does nothing and returns 0.



**Since:** BeOS R3

---

### `Name()`

```cpp
const char * BStopWatch::Name()const
```

Returns the name of the stop watch. 


If name was set to `NULL` in the constructor this method returns a blank string.



**Returns:** the name of the stop watch set in the constructor.



**Since:** BeOS R3

---

### `Reset()`

```cpp
void BStopWatch::Reset()
```

Restarts the timer. 


Resets the stop watch clearing the start time and stored laps and restarts the timer.



**Since:** BeOS R3

---

### `Resume()`

```cpp
void BStopWatch::Resume()
```

Resume the timer from a suspended state. 



**See also:** [Suspend()](classBStopWatch.md#a375f8b983fb8bfd6afa91fc8c4aba6e9)



**Since:** BeOS R3

---

### `Suspend()`

```cpp
void BStopWatch::Suspend()
```

Suspend the timer. 



**See also:** [Resume()](classBStopWatch.md#add07ccf4401109f0f88974ea3063d16c)



**Since:** BeOS R3

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBStopWatch.html).
