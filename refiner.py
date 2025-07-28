from collections import Counter

def refine_headings(blocks):
    blocks = [b for b in blocks if b["text"].strip()]
    for b in blocks:
        b["font_size"] = round(b["font_size"], 1)

    if not blocks:
        return "Unknown Title", []

    size_freq = Counter([b["font_size"] for b in blocks])
    sorted_sizes = [s[0] for s in size_freq.most_common()]

    size_to_level = {}
    if len(sorted_sizes) > 0:
        size_to_level[sorted_sizes[0]] = "PARA"
    if len(sorted_sizes) > 1:
        size_to_level[sorted_sizes[1]] = "H3"
    if len(sorted_sizes) > 2:
        size_to_level[sorted_sizes[2]] = "H2"
    if len(sorted_sizes) > 3:
        size_to_level[sorted_sizes[3]] = "H1"
    if len(sorted_sizes) > 4:
        size_to_level[sorted_sizes[4]] = "TITLE"

    title = None
    outline = []

    for b in blocks:
        level = size_to_level.get(b["font_size"], None)
        if level == "TITLE" and b["page"] == 1 and not title:
            title = b["text"]
        elif level in ("H1", "H2", "H3"):
            outline.append({
                "level": level,
                "text": b["text"],
                "page": b["page"]
            })

    return title or "Unknown Title", outline
