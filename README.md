# 🌟 我的个人导航页 (Personal Bookmarks)

这是一个极简、响应式的个人浏览器导航页。基于纯 HTML/CSS/JS 单文件开发，无后端，加载速度快，易于部署。

## 🚀 在线演示
**[点击这里访问我的导航站](https://spongegg.github.io/-/)**
*(请将上方链接修改为你自己的 GitHub Pages 实际地址)*

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
