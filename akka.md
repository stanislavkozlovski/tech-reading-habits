When defining Actors and their messages, keep these recommendations in mind:

* Since messages are the Actor’s public API, it is a good practice to define messages with good names and rich semantic and domain specific meaning, even if they just wrap your data type. This will make it easier to use, understand and debug actor-based systems.

* Messages should be immutable, since they are shared between different threads.

* It is a good practice to put an actor’s associated messages in its object. This makes it easier to understand what type of messages the actor expects and handles.

* It is a good practice obtain an actor’s initial behavior in the object’s apply method
