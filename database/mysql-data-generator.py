import ast
import re
import random


def get_airports(path: str):
    _airports = {}
    with open(path, 'r', encoding='utf8') as fr:
        airport_pattern = r"^INSERT INTO `utopia`.`airport` \(`iata_id`, `name`, `city`, `country`, `longitude`, " \
                          r"`latitude`, `altitude`, `timezone`\) VALUES \('(.+)', '(.+)', '(.+)', " \
                          r"'(.+)', (.+), (.+), (.+), (.+)\);$"
        for line in fr:
            airport = re.match(airport_pattern, line)
            if airport:
                _airports[airport.group(1)] = (
                    airport.group(1), airport.group(2), airport.group(
                        3), airport.group(4), airport.group(5),
                    airport.group(6), airport.group(7), airport.group(8))
    return _airports


def get_routes(path: str):
    _routes = {}
    with open(path, 'r', encoding='utf8') as fr:
        routes_pattern = r"^INSERT INTO `utopia`.`route` \(`id`, `origin_id`, `destination_id`\) VALUES \((.+), '(.+)', '(.+)'\);$"
        for line in fr:
            route = re.match(routes_pattern, line)
            if route:
                _routes[route.group(1)] = (route.group(1), route.group(2), route.group(3))
    return _routes


def get_flights(path: str):
    _flights = {}
    with open(path, 'r', encoding='utf8') as fr:
        flight_pattern = r"^INSERT INTO `utopia`.`flight` \(`id`, `route_id`, `airplane_id`, `departure_time`, `reserved_seats`, `seat_price`\) VALUES \((.+), (.+), (.+), '(.+)', (.+), (.+)\);$"
        for line in fr:
            flight = re.match(flight_pattern, line)
            if flight:
                _flights[flight.group(1)] = (
                    flight.group(1), flight.group(2), flight.group(3), flight.group(4), flight.group(5),
                    flight.group(6))
    return _flights


def get_bookings(path: str):
    _bookings = {}
    with open(path, 'r', encoding='utf8') as fr:
        booking_pattern = r"^INSERT INTO `utopia`.`booking` \(`id`, `is_active`, `confirmation_code`\) VALUES \((.+), (.+), '(.+)'\);$"
        for line in fr:
            booking = re.match(booking_pattern, line)
            if booking:
                _bookings[booking.group(1)] = (booking.group(1), booking.group(2), booking.group(3))
    return _bookings


def get_users(path: str):
    _users = {}
    with open(path, 'r', encoding='utf8') as fr:
        user_pattern = r"^INSERT INTO `utopia`.`user` \(`id`, `role_id`, `given_name`, `family_name`, `username`, `password`, `email`, `phone`\) VALUES \((.+), (.+), '(.+)', '(.+)', '(.+)', '(.+)', '(.+)', '(.+)'\);$"
        for line in fr:
            users = re.match(user_pattern, line)
            if users:
                _users[users.group(1)] = (
                    users.group(1), users.group(2), users.group(
                        3), users.group(4), users.group(5),
                    users.group(6), users.group(7), users.group(8))
    return _users


def get_passengers(path: str):
    _passengers = {}
    with open(path, 'r', encoding='utf8') as fr:
        passenger_pattern = r"^INSERT INTO `utopia`.`passenger` \(`id`, `booking_id`, `given_name`, `family_name`, `dob`, `gender`, `address`\) VALUES \((.+), (.+), '(.+)', '(.+)', '(.+)', '(.+)', '(.+)'\);$"
        for line in fr:
            passenger = re.match(passenger_pattern, line)
            if passenger:
                _passengers[passenger.group(1)] = (
                    passenger.group(1), passenger.group(2), passenger.group(3), passenger.group(4), passenger.group(5),
                    passenger.group(6), passenger.group(7))
    return _passengers


def get_flight_bookings(path: str):
    _flight_bookings = {}
    with open(path, 'r', encoding='utf8') as fr:
        flight_booking_pattern = r"^INSERT INTO `utopia`.`flight_bookings` \(`flight_id`, `booking_id`\) VALUES \((.+), (.+)\);$"
        for line in fr:
            flight_booking = re.match(flight_booking_pattern, line)
            if flight_booking:
                _flight_bookings[flight_booking.group(1)] = (flight_booking.group(1), flight_booking.group(2))
    return _flight_bookings


def get_booking_users(path: str):
    _booking_users = {}
    with open(path, 'r', encoding='utf8') as fr:
        booking_user_pattern = r"^INSERT INTO `utopia`.`booking_user` \(`booking_id`, `user_id`\) VALUES \((.+), (.+)\);$"
        for line in fr:
            booking_user = re.match(booking_user_pattern, line)
            if booking_user:
                _booking_users[booking_user.group(1)] = (booking_user.group(1), booking_user.group(2))
    return _booking_users


def get_booking_guests(path: str):
    _booking_guests = {}
    with open(path, 'r', encoding='utf8') as fr:
        booking_guest_pattern = r"^INSERT INTO `utopia`.`booking_guest` \(`booking_id`, `contact_email`, `contact_phone`\) VALUES \((.+), '(.+)', '(.+)'\);$"
        for line in fr:
            booking_guest = re.match(booking_guest_pattern, line)
            if booking_guest:
                _booking_guests[booking_guest.group(1)] = (
                    booking_guest.group(1), booking_guest.group(2), booking_guest.group(3))
    return _booking_guests


def get_booking_agents(path: str):
    _booking_agents = {}
    with open(path, 'r', encoding='utf8') as fr:
        booking_agent_pattern = r"^INSERT INTO `utopia`.`booking_agent` \(`booking_id`, `agent_id`\) VALUES \((.+), (.+)\);$"
        for line in fr:
            booking_agent = re.match(booking_agent_pattern, line)
            if booking_agent:
                _booking_agents[booking_agent.group(1)] = (booking_agent.group(1), booking_agent.group(2))
    return _booking_agents


def generate_report(data, filename):
    with open(filename, 'w+', encoding='utf8') as fw:
        fw.write(data.__str__())


def get_table(filename):
    with open(filename, 'r', encoding='utf8') as fr:
        data = fr.read()
    return ast.literal_eval(data)


def change_genders(passengers: dict):
    for k, passenger in passengers.items():

        if passenger[5] != 'Male' or passenger[5] != 'Female':
            row = list(passenger)
            prob = random.randint(0, 100)
            row[5] = 'Male' if prob > 80 else 'Female'
            passengers[k] = tuple(row)
            # print(passenger[2], passenger[3], passengers[k][5])
    return passengers


def generate_sql_statements(statement: str, dataDic={}):
    if dataDic:
        for item in dataDic.values():
            args = [v for v in item]
            print(statement.format(*args))
            # print(statement.format(p[0], p[1], p[2], p[3], p[4], p[5], p[6]))


def generate_route_sql_statements(statement: str, routes: dict):
    j = 1
    for _, r in routes.items():
        print(statement.format(j, r[1], r[2]))
        j += 1
        print(statement.format(j, r[2], r[1]))
        j += 1


def combine_routes(routes: dict):
    airports = set()
    for _, r in routes.items():
        airports.add(r[1])
        airports.add(r[2])
    return airports


if __name__ == '__main__':
    print('start generating data...')

    # sql to dic
    # f = get_booking_agents('data.sql')
    # print(len(f), f)
    # generate_report(f, 'booking_agents.txt')

    # read dic from file
    # passengers = get_table('passengers.txt')
    # passengers = change_genders(passengers)
    # generate_report(passengers, 'passengers.txt')

    # # generate sql statements
    # passengers = get_table('passengers.txt')
    # generate_sql_statements(passengers, "INSERT INTO `utopia`.`passenger` (`id`, `booking_id`, `given_name`, `family_name`, `dob`, `gender`, `address`) VALUES ({0}, {1}, '{2}', '{3}', '{4}', '{5}', '{6}');")

    # generate sql statements
    routes = get_table('routes.txt')
    generate_route_sql_statements(
        "INSERT INTO `utopia`.`route` (`id`, `origin_id`, `destination_id`) VALUES ({0}, '{1}', '{2}');", routes)
    print('===================================done===================================')
