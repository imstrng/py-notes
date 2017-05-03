import asyncio
 
def cancel_call(handle):
    """
    This method cancels the call wrapped in the asyncio.Handle received as an argument
    """
    handle.cancel()
 
def just_print_messages(loop):
    """
    This method prints a message and schedules another call to itself after three seconds
    Then, the method schedules a callback that cancels the previously scheduled callback
    """
    print('Just printing a new message every three seconds')
    handle = loop.call_later(3, just_print_messages, loop)
    loop.call_later(1, cancel_call, handle)
 
def main():
    loop = asyncio.get_event_loop()
    try:
        loop.call_soon(just_print_messages, loop)
        loop.run_forever()
    finally:
        loop.close()
 
if __name__ == '__main__':
    main()