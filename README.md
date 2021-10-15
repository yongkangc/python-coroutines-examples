# Learnings and Projects with Asyncio, Requests, Aiohttp | Make faster API Calls

## Defintiions:

Event Loop : We can let some stuff take a long time to do in the background. When its done, event loop wil pick up the event
Blocking Call : A function that takes a long time to complete

- Analogy:
  Synchronous: Cook rice then cook meat
  Asynchronous: Cook rice in the background, and cook meat. Check to see if rice is done

The general idea is that we have a bunch of functions that take a long time to complete. We want to run these functions in the background.

- We define the functions as async functions.
- We can combine these functions into a task and add them to the event loop.
- We await the functions to complete.
- We run the functions in the background by using the event loop.
