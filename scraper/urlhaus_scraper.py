from urllib import request, parse
import csv

URL = "https://urlhaus.abuse.ch/downloads/csv_online/"


def load_hosts() -> list[str]:
    """
    Scrapes csv-file from URLHaus active malware database
    and parses the CSV file for the "mirai" tag and separates the IP/domain.

    :return: A list of scraped IPs/domains
    """
    ips = []
    with request.urlopen(URL) as connection:
        raw = str(connection.read().decode("utf-8")).split("\n")
        csv_reader = csv.reader(raw)

        for line in csv_reader:
            if (len(line) == 8) and ('mirai' in line[5] or 'x86' in line[2] or 'bins.sh' in line[2]):
                ips.append(parse.urlparse(line[2]).hostname)

    return ips


if __name__ == '__main__':
    print(load_hosts())
