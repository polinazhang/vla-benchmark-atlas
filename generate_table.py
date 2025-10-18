import yaml


def bool_icon(value):
    return "✅" if value else "❌"


def safe_get(entry, key):
    return entry.get(key, "—")


def generate_markdown(datasets):
    header = (
        "| Name | Robot | Type | Data | Control | Lang Cond. | Env |\n"
        "|------|-------|------|------|---------|-------------|-----|\n"
    )
    rows = []
    collapsibles = []

    for dataset in datasets:
        name = dataset.get("name", "Unnamed Dataset")
        name_link = f"[{name}]({dataset['link']})" if "link" in dataset else name

        rows.append(
            "| {name} | {robot} | {dtype} | {data} | {control} | {lang_cond} | {env} |".format(
                name=name_link,
                robot=safe_get(dataset, "robot"),
                dtype=safe_get(dataset, "type"),
                data=safe_get(dataset, "data"),
                control=safe_get(dataset, "control"),
                lang_cond=bool_icon(dataset.get("language_conditioned", False)),
                env=safe_get(dataset, "env"),
            )
        )

        papers = dataset.get("papers")
        if papers:
            paper_lines = []
            for paper in papers:
                title = paper.get("title", "Untitled")
                authors = paper.get("authors", "Unknown")
                year = paper.get("year", "TBD")
                link = paper.get("link")
                paper_label = f"{title} ({authors}, {year})"
                paper_lines.append(f"- [{paper_label}]({link})" if link else f"- {paper_label}")

            collapsibles.append(
                "<details>\n"
                f"<summary>📄 Papers using {name} (click to expand)</summary>\n\n"
                f"{'\n'.join(paper_lines)}\n\n"
                "</details>\n"
            )

    table_md = header + "\n".join(rows)
    collapsibles_md = "\n".join(collapsibles)
    return table_md + ("\n\n" + collapsibles_md if collapsibles_md else "")


def main():
    with open("benchmarks/datasets.yaml", "r") as dataset_file:
        datasets = yaml.safe_load(dataset_file) or []

    markdown = generate_markdown(datasets)

    with open("tables/datasets.md", "w") as out_file:
        out_file.write("# 📚 Demonstration Datasets\n\n")
        out_file.write(markdown)

    print("✅ Markdown table generated at tables/datasets.md")


if __name__ == "__main__":
    main()
