from feedparser import parse
from html2markdown import convert

url = "https://cubable.date/rss/"


def func(url):
    feed = parse(url).entries
    latest = [
        f"""[📝 {str(i.title)}]({str(i.link)})  \n{str(i.description)} - {str(i.published)}\n\n---------------------"""
        for i in list(feed)
    ]
    print(latest)
    farr = []
    with open("README.md", "r", encoding="utf8") as x:
        for line in x:
            if line.strip() == "<!--bp-->":
                break
            farr.append(line)

    with open("README.md", "w", encoding="utf8") as x:
        x.writelines(farr)
        x.write("<!--bp-->\n\n")
        [x.write(convert(i) + "\n\n") for i in latest]


if __name__ == "__main__":
    func(url=url)
