from functools import lru_cache

@lru_cache
def countArrangements(record: str, streaks: tuple[int], streak: int = 0) -> int:

    if not streaks:
        return 0 if streak > 0 or '#' in record else 1

    if not record:
        return 1 if streaks == (streak,) else 0
    
    if streak > streaks[0]:
        return 0
    
    if len(record) + streak < sum(streaks):
        return 0

    match (record[0]):
        case '#':
            return countArrangements(record[1:], streaks, streak + 1)
        case '.':
            if streak == 0:
                return countArrangements(record[1:], streaks, 0)
            elif streak == streaks[0]:
                return countArrangements(record[1:], streaks[1:], 0)
            else:
                return 0
        case '?':
            if streak > 0:
                if streak < streaks[0]:
                    return countArrangements('#' + record[1:], streaks, streak)
                elif streak == streaks[0]:
                    return countArrangements('.' + record[1:], streaks, streak)
                else:
                    return 0
            else:
                a = countArrangements('#' + record[1:], streaks, streak)
                b = countArrangements('.' + record[1:], streaks, streak)
                return a + b
        case _:
            return 0

with open('src/12/input.txt') as file:
    total = 0
    for line in file:
        if not line.isspace():
            record, streaks = line.strip().split()
            record = '?'.join([record] * 5)
            streaks = tuple(map(int, streaks.split(','))) * 5
            arrangements = countArrangements(record, streaks)
            total += arrangements
            print(total, '+=', arrangements)
    print('---')
    print(total)
