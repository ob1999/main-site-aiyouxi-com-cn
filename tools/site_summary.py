import json
import sys


SITE_DATA = [
    {
        "name": "爱游戏主站",
        "url": "https://main-site-aiyouxi.com.cn",
        "tags": ["游戏", "资讯", "评测"],
        "keywords": ["爱游戏", "游戏资讯", "游戏评测"],
        "description": "提供最新游戏新闻、深度评测及玩家社区互动。"
    }
]


def load_site_data(path=None):
    """从默认数据或指定JSON文件加载站点资料。"""
    if path:
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"警告：无法加载 {path}，使用内置数据。错误：{e}", file=sys.stderr)
            return SITE_DATA
    return SITE_DATA


def generate_summary(site):
    """为单个站点生成结构化摘要文本。"""
    lines = []
    lines.append(f"名称：{site['name']}")
    lines.append(f"URL：{site['url']}")
    lines.append(f"关键词：{', '.join(site.get('keywords', []))}")
    lines.append(f"标签：{', '.join(site.get('tags', []))}")
    lines.append(f"说明：{site.get('description', '无描述')}")
    return "\n".join(lines)


def build_all_summaries(sites):
    """遍历站点列表生成完整摘要输出。"""
    output_parts = []
    output_parts.append("站点摘要报告")
    output_parts.append("=" * 30)
    for i, site in enumerate(sites, 1):
        output_parts.append(f"\n站点 {i}:")
        output_parts.append(generate_summary(site))
        output_parts.append("-" * 20)
    output_parts.append("报告结束")
    return "\n".join(output_parts)


def export_to_json(sites, filepath="summary_output.json"):
    """将摘要数据导出为JSON文件。"""
    export_data = []
    for site in sites:
        export_data.append({
            "name": site.get("name"),
            "url": site.get("url"),
            "keywords": site.get("keywords", []),
            "tags": site.get("tags", []),
            "description": site.get("description", "")
        })
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)
        print(f"摘要已导出至 {filepath}")
    except IOError as e:
        print(f"导出失败：{e}", file=sys.stderr)


def main():
    """主函数：读取数据、生成摘要、可选导出。"""
    sites = load_site_data()
    if not sites:
        print("没有站点数据可处理。", file=sys.stderr)
        sys.exit(1)

    report = build_all_summaries(sites)
    print(report)

    if len(sys.argv) > 1 and sys.argv[1] == "--export":
        export_to_json(sites)


if __name__ == "__main__":
    main()