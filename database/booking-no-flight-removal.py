import re


def get_flight_booking_info(path: str):
    pattern_bf = r'^INSERT INTO `utopia`.`flight_bookings` \(`flight_id`, `booking_id`\) VALUES \(\d+, (\d+)\);$'
    pattern_b = r'^INSERT INTO `utopia`.`booking` \(`id`, `is_active`, `confirmation_code`\) ' \
                r'VALUES \((\d+), .*, \'.*\'\);$'
    count_bf = 0
    count_b = 0
    b_set = set()
    bf_set = set()
    with open(path, 'r', encoding='utf8') as fr:
        for line in fr:
            bf = re.match(pattern_bf, line)
            b = re.match(pattern_b, line)
            if bf:
                # print(bf.group(1))
                count_bf += 1
                bf_set.add(bf.group(1))
            elif b:
                # print(b.group(1))
                count_b += 1
                b_set.add(b.group(1))
    print(count_bf, count_b)
    for bid in b_set:
        if bid not in bf_set:
            print(bid)


if __name__ == '__main__':
    print('booking no flight removal')
    get_flight_booking_info('data.sql')
