from tags.models import Tag
from bs4 import BeautifulSoup
import re


def get_tag_list(content):
    soup = BeautifulSoup(content, 'html.parser')
    content = soup.find_all(string=re.compile("^#"))
    content = str(content)[2:-2]
    from IPython import embed
    embed()
    tag_list = [
            word.replace("#", "")
            for word
            in content.split(" ")
            if word.startswith("#")
            ]
    return tag_list


def get_tagify_content(content):
    tag_list = get_tag_list(content)
    word_list = [
        word
        for word
        in content.split(" ")
    ]

    tagify_word_list = []

    for word in word_list:
        if word in ["#{tag_name}".format(tag_name=tag) for tag in tag_list]:
            word = "<a href='{tag_url}'>{tag_name}</a> ".format(
                tag_name=word,
                tag_url=Tag.objects.get(name=word.replace("#", "")).get_absolute_url(),
            )
        tagify_word_list.append(word)

    return " ".join(tagify_word_list)
