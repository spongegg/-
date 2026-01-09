# 🌟 我的个人导航页 (Personal Bookmarks)

这是一个极简、响应式的个人浏览器导航页。基于纯 HTML/CSS/JS 单文件开发，无后端，加载速度快，易于部署。

## 🚀 在线演示
**[点击这里访问我的导航站](https://spongegg.github.io/-/)**
*(请确保上方链接是你正确的 GitHub Pages 地址)*

## ✨ 功能特点
- **单文件架构**：所有代码都在 `index.html` 中，方便迁移和备份。
- **响应式设计**：电脑、平板、手机端完美适配。
- **多引擎搜索**：支持 Google 和 Bing 搜索引擎一键切换。
- **分类清晰**：卡片式布局，图标直观。

---

## 🛠️ 如何修改内容

所有内容都存储在 `index.html` 文件中。你可以直接在 GitHub 网页上点击 `index.html` 右上角的 **✏️ (编辑)** 按钮进行修改。

### 1. 添加一个新的【书签】
找到你想要添加的分类区域（寻找 `<div class="grid">` 标签），在其中粘贴以下代码：

```html
<a href="https://目标网址.com" target="_blank" class="card">
    <!-- 图标部分：去 FontAwesome 找图标代码 -->
    <div class="card-icon"><i class="fas fa-link"></i></div>
    <div class="card-info">
        <span class="card-title">网站名称</span>
        <span class="card-desc">这里是一句简短的描述</span>
    </div>
</a>
```

### 2. 添加一个新的【分类】

```html
<div class="category">
    <!-- 修改下面的 fa-folder 为你喜欢的图标，修改文字为你的分类名 -->
    <h2 class="category-title"><i class="fas fa-folder"></i> 新分类名称</h2>
    <div class="grid">
        <!-- 在这里放入上面的书签代码 -->
    </div>
</a>
```

### 3. 修改图标
本项目使用 FontAwesome 6 图标库。
访问 FontAwesome 图标搜索。
搜索关键词（如 github, video, tool）。
复制图标代码，例如 fa-solid fa-house。
将代码填入 <i class="..."></i> 的 class 属性中



