# FastApi Setup

A simple boilerplate setup for a Python FastAPI application.

This boilerplate style separates and groups together related logic, like API-endponints from
their request handling logic

There is another style which contains together the endpoint, handlers and it's own db schema
separately in a coupled group, if you prefer that style; then I have uploaded that [here]()

**Note:** There is one inconvenience with pony, in that you will have to manually update
the sql database tables if you decide to change the schema after you have done the initial
migration. This will not be an issue in development but is something to keep note of
