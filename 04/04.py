import re

# load data from file
with open('input') as f:
    lines = f.read().splitlines()
    # sort the entries in a chronological order
    lines.sort(key=lambda line: line.split("]")[0])


def part1(lines):
    pattern = {}
    totals = {}
    # define regexes to fetch data from input
    guard_r = re.compile("Guard #(\d+)")
    asleep_r = re.compile(".+:(\d\d).*falls.*$")
    wakeup_r = re.compile(".+:(\d\d).*wakes.*$")
    # parse input
    for entry in lines:
        if guard_r.search(entry):
            guardID = guard_r.findall(entry)[0]
        elif asleep_r.search(entry):
            sleep = int(asleep_r.findall(entry)[0])
        elif wakeup_r.search(entry):
            wake = int(wakeup_r.findall(entry)[0])
            # populate dictionary based on guard id
            for minute in range(sleep, wake):
                num = 1
                if guardID not in pattern:
                    pattern[guardID] = {}
                if minute in pattern[guardID]:
                    num = pattern[guardID][minute]
                    num += 1
                pattern[guardID][minute] = num
    # calculate total sleep time for each guard
    for key in pattern.keys():
        totals[key] = sum(pattern[key].values())
    # find a guard who sleeps the most
    sleeper = (max(totals, key=totals.get))
    # find the most slept minute for that guard (sleeper)
    minutes = dict(pattern[sleeper].items())
    most_slept_minute=(max(minutes, key=minutes.get))
    # result for part 1
    target = int(sleeper)*int(most_slept_minute)
    print("Target =", target)


def part2(lines):
    # the same pattern for parsing input, actually this could be moved to it's own function
    pattern = {}
    totals = {}
    guard_r = re.compile("Guard #(\d+)")
    asleep_r = re.compile(".+:(\d\d).*falls.*$")
    wakeup_r = re.compile(".+:(\d\d).*wakes.*$")
    for entry in lines:
        if guard_r.search(entry):
            guardID = guard_r.findall(entry)[0]
        elif asleep_r.search(entry):
            sleep = int(asleep_r.findall(entry)[0])
        elif wakeup_r.search(entry):
            wake = int(wakeup_r.findall(entry)[0])
            for minute in range(sleep, wake):
                num = 1
                if guardID not in pattern:
                    pattern[guardID] = {}
                if minute in pattern[guardID]:
                    num = pattern[guardID][minute]
                    num += 1
                pattern[guardID][minute] = num
    reg = []
    h_dur = 0
    h_min = 0
    h_id = 0
    # find most slept minute, and it's duration as well as id
    for gid, value in pattern.items():
        most_slep_minute = (max(value, key=value.get))
        sleep_duration = (value.get(max(value, key=value.get)))
        reg.append([gid, most_slep_minute, sleep_duration])
        # while parsing list find the biggest value and record the rest of metadata
        if sleep_duration > h_dur:
            h_dur = sleep_duration
            h_min = most_slep_minute
            h_id = gid
    # result for part 2
    print("Guard id:",h_id,"minute:", h_min, "result:", int(h_id)*int(h_min))

part1(lines)
part2(lines)