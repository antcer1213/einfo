
def run(command, entry, append=False):
    from ecore import Exe

    def received_data(cmd, event, append, *args, **kwargs):
        if append:
            output = event.data
            output = output.replace("\n", "")
            entry.entry_append(" (%s)" %output)
        else:
            entry.entry_set(event.data)

    def command_done(cmd, event, *args, **kwargs):
        if event.exit_code is not 0:
            entry.entry_set("N/A")

    cmd = Exe(command, 1|4)
    cmd.on_data_event_add(received_data, append)
    cmd.on_del_event_add(command_done)

def splitter(lst, breaker, search=False):
    current = []
    it = iter(lst)
    first = next(it)
    #~ assert first==breaker
    for item in it:
        if search == True and breaker in item:
            yield current
            current = []
        elif item == breaker:
            yield current
            current = []
        current.append(item)
    yield current
