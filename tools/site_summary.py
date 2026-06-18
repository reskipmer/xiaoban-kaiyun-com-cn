"""
site_summary.py - 站点摘要生成模块
"""

SITES = [
    {
        "name": "开云官网",
        "url": "https://xiaoban-kaiyun.com.cn",
        "tags": ["开云", "官网", "平台"],
        "description": "开云综合服务平台，提供多种在线服务与资讯。",
    },
    {
        "name": "开云帮助中心",
        "url": "https://xiaoban-kaiyun.com.cn/help",
        "tags": ["开云", "帮助", "FAQ"],
        "description": "用户常见问题解答与操作指南。",
    },
    {
        "name": "开云博客",
        "url": "https://xiaoban-kaiyun.com.cn/blog",
        "tags": ["开云", "博客", "资讯"],
        "description": "行业动态、产品更新与技术分享。",
    },
]

KEYWORD = "开云"


def format_tags(tags):
    return "、".join(tags)


def generate_entry(site):
    name = site["name"]
    url = site["url"]
    tags = site["tags"]
    desc = site["description"]
    tag_str = format_tags(tags)
    return (
        f"站点名称：{name}\n"
        f"站点URL：{url}\n"
        f"标签：{tag_str}\n"
        f"简介：{desc}\n"
    )


def generate_summary(sites, keyword):
    parts = []
    parts.append(f"关键词：{keyword}")
    parts.append(f"站点数量：{len(sites)}")
    parts.append("")
    for i, site in enumerate(sites, 1):
        parts.append(f"--- 站点 {i} ---")
        parts.append(generate_entry(site))
    return "\n".join(parts)


def main():
    summary = generate_summary(SITES, KEYWORD)
    print(summary)


if __name__ == "__main__":
    main()