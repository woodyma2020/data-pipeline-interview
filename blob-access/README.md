# blob-access

## Blob Container: 

[https://interviewexample.blob.core.windows.net/example-events](https://interviewexample.blob.core.windows.net/example-events)

## Structure:

Flat file of eventOid(UUID) named JSON files, containing all the data for that individual event. eg:

    12345678-90ab-cdef-1234-567890abcdef.json

The basic schema of each event is provided in this repo:
    
    example-events.json

## Potential tasks:

1. Connect to blob with the SAS token
2. Load all streamed events from blob to your preferred flavor of database / table / event manager. 
3. Create a table/view/etc. of each of the event types present

*Bonus: Explain the event order / submit pattern for the different types of events*