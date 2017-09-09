#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 8/8/17 10:53 AM
"""

"""
Function:
【教程】详解Python正则表达式之： (?:…) non-capturing group 非捕获组
http://www.crifan.com/detailed_explanation_about_python_regular_express_non_capturing_group/

Version:    2013-09-06
Author:     Crifan Li
Contact:    http://www.crifan.com/about/me/
"""

"""
1.non-capturing group，中文直译为，非捕获组。
# 如何关闭圆括号的捕获能力？而只是用它来做分组，方法是在左括号的后边加上?:

2.非捕获组的含义：

    非：不的意思
    捕获：捕获的含义，可以理解为：
        匹配
        且记录此处所匹配的内容，为一个对应的group组，为后续使用
        后续如何使用：
            比如.group(1)就是获得第一个捕获的组的值
    组：group，将此部分匹配的内容，用括号扩起来，称为一个组，是为了方便（看代码的）用户，更加明白其逻辑上的含义而已。
3.此处的，非捕获组，主要是，相对于，捕获的组来说的。
当你仅仅是希望分组,不希望提取时,.non-capturing group是非常方便的
当你在pattern中使用()时,并非总是需要它的提取结果,也许你仅仅是希望分组,以便于提取出真正希望的数据.
例如,提取HTML源文件的标题文字,它可能有2种形式: (1)标题文字 (2)标题文字 也就是说一些格式代码可能出现0次或1次.
如果你写成: r'()?(.+?)()?' 那么你要使用.group(2)才能得到自己想要的数据,你并不关心.group(1)和.group(3)是什么,
也不希望正则引擎去把它们提取出来.那么,你就需要使用非提取分组符: r'(?:)?(.+?)(?:)?'
"""

import re


def python_re_non_capturing_group():
    """
        demo Pyton non-capturing group
        https://www.crifan.com/detailed_explanation_about_python_regular_express_non_capturing_group/
    """
    inputStr = "hello 123 world 456 nihao 789";
    rePatternAllCapturingGroup = "\w+ (\d+) \w+ (\d+) \w+ (\d+)";
    rePatternWithNonCapturingGroup = "\w+ (\d+) \w+ (?:\d+) \w+ (\d+)";
    print("inputStr=", inputStr)
    print("rePatternAllCapturingGroup=", rePatternAllCapturingGroup)

    print("rePatternWithNonCapturingGroup=", rePatternWithNonCapturingGroup)

    print("--- 1. show normal case, all captured group ---")

    foundDigitsAllCapturingGroup = re.search(rePatternAllCapturingGroup, inputStr);
    if (foundDigitsAllCapturingGroup):
        firstGroup = foundDigitsAllCapturingGroup.group(1);
        print("firstGroup=", firstGroup)  # firstGroup= 123

        secondGroup = foundDigitsAllCapturingGroup.group(2);
        print("secondGroup=", secondGroup)  # secondGroup= 456

        thirdGroup = foundDigitsAllCapturingGroup.group(3);
        print("thirdGroup=", thirdGroup)  # thirdGroup= 789)

    print("--- 2. show with non-capturing group ---")

    foundDigitsWithNonCapturingGroup = re.search(rePatternWithNonCapturingGroup, inputStr);
    if (foundDigitsWithNonCapturingGroup):
        firstGroup = foundDigitsWithNonCapturingGroup.group(1);
        print("firstGroup=", firstGroup)  # firstGroup= 123
        secondGroup = foundDigitsWithNonCapturingGroup.group(2);
        print("secondGroup=", secondGroup)  # secondGroup= 789
        # thirdGroup = foundDigitsWithNonCapturingGroup.group(3); # will error -> IndexError: no such group
        print(
            """Explains:
    1. for second group (?:\d+),
    is something like (?:xxx)
    is a non-capturing group
    so only match this group,
    but not usable(indexable) later
    so, here second group is not 456, but is 789

    2. also, second group is omitted
    so there is not index=3 group
    so above use group(3) will cause error:
    IndexError: no such group
            """
        )


###############################################################################
if __name__ == "__main__":
    python_re_non_capturing_group();
