import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    embed = re.search(r'^<iframe[ ](?:width="560"[ ]height="315"[ ])?src="https?://(?:www\.)?youtube\.com/embed/(.+)"(?:[ ]title="YouTube[ ]video[ ]player"[ ]frameborder="0"[ ]allow="accelerometer;[ ]autoplay;[ ]clipboard-write;[ ]encrypted-media;[ ]gyroscope;[ ]picture-in-picture"[ ]allowfullscreen)?></iframe>$', s, re.IGNORECASE)
    if embed:
        return f"https://youtu.be/{embed.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
