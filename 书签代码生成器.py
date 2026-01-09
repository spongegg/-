# 只需要修改这里的数据
bookmarks = [
    # (网址, 图标, 名称, 描述)
    ("https://www.ghxi.com/", "fas fa-link", "果核剥壳-互联网的净土", "果核剥壳"),
]

# 脚本逻辑
template = """
                <a href="{url}" target="_blank" class="card">
                    <div class="card-icon"><i class="{icon}"></i></div>
                    <div class="card-info"><span class="card-title">{title}</span><span class="card-desc">{desc}</span></div>
                </a>"""

for url, icon, title, desc in bookmarks:
    print(template.format(url=url, icon=icon, title=title, desc=desc))
