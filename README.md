如何修改指南 (新手必读)
在静态网页中，所有的内容都是写死在 HTML 代码里的。
1. 如何添加一个新的【分类】？
找到代码中的 </main>（大约在第 350 行左右），在这个标签上方复制以下代码块并粘贴：
code
Html
<!-- 新分类 -->
<div class="category">
    <!-- 分类标题：修改 fa-folder 为你想要的图标，修改“我的新分类”为标题 -->
    <h2 class="category-title"><i class="fas fa-folder"></i> 我的新分类</h2>
    <div class="grid">
        <!-- 可以在这里放很多个书签 -->
    </div>
</div>
2. 如何添加一个新的【书签】？
找到你想要添加的分类下的 <div class="grid"> ... </div> 标签中间，复制粘贴下面的代码块：
code
Html
<a href="https://example.com" target="_blank" class="card">
    <!-- 图标部分：去 FontAwesome 找代码替换 fa-link -->
    <div class="card-icon"><i class="fas fa-link"></i></div>
    <div class="card-info">
        <span class="card-title">网站标题</span>
        <span class="card-desc">这里写简短的描述</span>
    </div>
</a>
3. 如何修改图标？
代码里用的是 FontAwesome 图标库（fas fa-xxx 或 fab fa-xxx）。
常用图标代码速查：
视频：fa-video, fa-play, fab fa-youtube, fab fa-bilibili
图片：fa-image, fa-camera, fa-photo-video
工具：fa-tools, fa-wrench, fa-cog
云端：fa-cloud, fa-server, fa-hdd
社交：fab fa-twitter, fab fa-github, fab fa-telegram
如何查找：去 FontAwesome官网 搜索关键词（英文），复制类似 <i class="fa-solid fa-house"></i> 中的 class 名字。
4. 如何删除？
直接选中从 <a href=...> 开始到 </a> 结束的代码，删除即可。
