def valid(data) -> bool:
    counter = 0

    for item in data:
        if item != '':
            counter += 1

    return bool(counter == len(data))
