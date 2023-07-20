import argparse
import json
import random

def parser_data():
    """
    从命令行读取用户参数
    做出如下约定：
    1. -f 为必选参数，表示输入题库文件
    2. -a 为可选参数，表示选择哪一篇文章
    ...

    :return: 参数
    """
    parser = argparse.ArgumentParser(
        prog="Word filling game",
        description="A simple game",
        allow_abbrev=True
    )

    parser.add_argument("-f", "--file", help="题库文件", required=True)
    # DONE: 添加更多参数
    parser.add_argument("-a", "--article", help="指定的文章名，可选参数，为空表示不指定文章", required=False)
    
    args = parser.parse_args()
    return args



def read_articles(filename):
    """
    读取题库文件

    :param filename: 题库文件名

    :return: 一个字典，题库内容
    """
    with open(filename, 'r', encoding="utf-8") as f:
        # DONE: 用 json 解析文件 f 里面的内容，存储到 data 中
        data = json.load(f)
    
    return data



def get_inputs(hints):
    """
    获取用户输入

    :param hints: 提示信息

    :return: 用户输入的单词
    """

    keys = []
    for hint in hints:
        print(f"请输入{hint}：")
        # TODO: 读取一个用户输入并且存储到 keys 当中

    return keys


# def replace(article, keys):
#     """
#     替换文章内容

#     :param article: 文章内容
#     :param keys: 用户输入的单词

#     :return: 替换后的文章内容

#     """
#     for i in range(len(keys)):
#         # TODO: 将 article 中的 {{i}} 替换为 keys[i]
#         # hint: 你可以用 str.replace() 函数，也可以尝试学习 re 库，用正则表达式替换

#     return article


if __name__ == "__main__":
    args = parser_data()
    data = read_articles(args.file)
    articles = data["articles"]

    # TODO: 根据参数或随机从 articles 中选择一篇文章
    if (args.article is None):
        # 打印所有文章的编号和标题
        for i in range(len(articles)):
            print(f"{i + 1}. {articles[i]['title']}")
        article_num = input("您未指定文章，您可以输入编号从以上文章中选一篇，如果不输入则将为您随机选一篇：")
        if (article_num != ""):
            if (not article_num.isdigit() or int(article_num) > len(articles) or int(article_num) < 1):
                print("ERROR: 输入的文章编号不合法！")
                exit(0)
            article = articles[int(article_num) - 1]
        else:
            article = random.choice(articles)
        # Debug信息
        print(article["title"])
    else:
        article_exist = False   # 文章是否存在
        for article_ in articles:
            if (article_["title"] == args.article):
                article = article_
                article_exist = True
                break
        if (not article_exist): # 文章不存在
            print("EROOR: 文章不存在！")
            exit(0)
        # Debug信息
        print(article["title"])
    # TODO: 给出合适的输出，提示用户输入
    # TODO: 获取用户输入并进行替换
    # TODO: 给出结果



