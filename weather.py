def main():
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]
    average_temperature = 0
    fukuoka_temperature = 0
    count = 0
    f_count = 0
    o_station =[]
    for data in weather_information:
        average_temperature += data["temperature"]
        count += 1
        if data['prefecture'] == "大阪府":
            o_station.append(data['station'])

        if data['prefecture'] == "福岡県":
            fukuoka_temperature += data["temperature"]
            f_count += 1

    print(average_temperature/count)
    print(','.join(o_station))
    print(fukuoka_temperature/f_count)


if __name__ == '__main__':
    main()