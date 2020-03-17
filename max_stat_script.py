stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
all_stats = []


for value in stats.values():
    all_stats.append(value)

for channel, stats in stats.items():
    if stats == max(all_stats):
        print(channel)
