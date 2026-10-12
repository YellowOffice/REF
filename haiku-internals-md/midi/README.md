# The MIDI Kit

* [Midi Kit design](design.md)

    * [Ooh, pictures](design.md#ooh-pictures)

    * [Housekeeping](design.md#housekeeping)

        * [Initialization](design.md#initialization)

        * [Error handling](design.md#error-handling)

        * [Creating and deleting endpoints](design.md#creating-and-deleting-endpoints)

        * [Changing endpoint attributes](design.md#changing-endpoint-attributes)

        * [Connections](design.md#connections)

        * [Watching](design.md#watching)

        * [Thread safety](design.md#thread-safety)

        * [Misc remarks](design.md#misc-remarks)

        * [The messages](design.md#the-messages)

    * [MIDI events](design.md#midi-events)

* [How libmidi1 works](midi1.md)

* [The softsynth](midi1.md#the-softsynth)

* [The BeOS R5 Midi Kit protocol](oldprotocol.md)

    * [Who does what?](oldprotocol.md#who-does-what)

    * [BMidiRoster::MidiRoster()](oldprotocol.md#bmidiroster-midiroster)

    * [BMidiLocalProducer constructor](oldprotocol.md#bmidilocalproducer-constructor)

    * [BMidiLocalConsumer constructor](oldprotocol.md#bmidilocalconsumer-constructor)

    * [BMidiEndpoint::Release()](oldprotocol.md#bmidiendpoint-release)

    * [BMidiEndpoint::SetName()](oldprotocol.md#bmidiendpoint-setname)

    * [BMidiEndpoint::GetProperties()](oldprotocol.md#bmidiendpoint-getproperties)

    * [BMidiEndpoint::SetProperties()](oldprotocol.md#bmidiendpoint-setproperties)

    * [BMidiLocalConsumer::SetLatency()](oldprotocol.md#bmidilocalconsumer-setlatency)

    * [BMidiProducer::Connect()](oldprotocol.md#bmidiproducer-connect)

    * [BMidiProducer::Disconnect()](oldprotocol.md#bmidiproducer-disconnect)

    * [Watchin’](oldprotocol.md#watchin)

    * [Other observations](oldprotocol.md#other-observations)

* [Misc notes](stuff.md)

* [Testing the Midi Kit](testing.md)

    * [Registering the application](testing.md#registering-the-application)

    * [Creating endpoints](testing.md#creating-endpoints)

    * [Deleting endpoints](testing.md#deleting-endpoints)

    * [Changing attributes](testing.md#changing-attributes)

    * [Consulting the roster](testing.md#consulting-the-roster)

    * [Making/breaking connections](testing.md#making-breaking-connections)

    * [Watching](testing.md#watching)

    * [Event tests](testing.md#event-tests)

    * [Other tests](testing.md#other-tests)

* [Midi Kit TO DO List](todo.md)

Generated from the [original source documentation](https://pulkomandy.tk/drop/haiku_internals/midi/index.html).
