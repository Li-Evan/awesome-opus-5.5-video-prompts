# 🚀 Product Launches and Ads

[← Back to the list](../README.md) · **English** · [简体中文](../zh-CN/prompts/launch.md)

Launch films, app and SaaS promos, brand spots and commercials. 136 prompts, most saved first.

### Launch video for an AI inference startup

<a href="https://x.com/deedydas/status/2102787937482252537"><img src="https://pbs.twimg.com/amplify_video_thumb/2102787906494668800/img/agrbxvHg24w3nJQD.jpg" alt="Launch video for an AI inference startup" width="480"></a>

[@deedydas](https://x.com/deedydas) · 2026-09-23 · 🔖 4.7k · ▶ 338.8k · `One-shot` · Playwright · ffmpeg

A 26-second launch video for an AI inference startup, coded as a web animation and recorded with Playwright and ffmpeg; no video model used.

```text
make a modern slick and punchy video for a modern startup that works on inference
```

<details><summary>中文译文</summary>

```text
为一家做推理的现代创业公司，做一支现代、精致、有冲击力的视频
```

</details>

<sub>Author: about 1 minute and ~$2 in raw API cost.</sub>

[Original post ↗](https://x.com/deedydas/status/2102787937482252537)

---

### Apple-keynote style launch film template

<a href="https://x.com/twoclipping/status/2103835273813496100"><img src="https://pbs.twimg.com/amplify_video_thumb/2103830256347910144/img/YsUzKmE5XqGD9NZR.jpg" alt="Apple-keynote style launch film template" width="480"></a>

[@twoclipping](https://x.com/twoclipping) · 2026-09-26 · 🔖 3.3k · ▶ 99.4k · `Template` · SVG · Canvas · Playwright · ffmpeg

A 29-second one-take launch film where every scene morphs from the last: liquid glass, iris wipes, real wall footage, all timed to 120 BPM.

```text
<inputs>
Ask me for: a one-word brand name for the wordmark (a verb works best), 9 to 12 high-res photos, a royalty-free song around 120 BPM with a drop and a quiet breakdown (Mixkit, free for commercial use), and a free stock clip of a plain wall with moving plant shadows (Pexels).
</inputs>

<direction>
An Apple-keynote launch film, 2D only, one continuous take. Every scene is made out of the previous one: nothing fades, blurs or cuts. Objects change shape instead: text rises out of a mask line, icons pop from zero on a spring, bars draw across, pages push, and a black shape floods the whole frame and contracts into the next scene. Warm off-white canvas, black UI, iOS 26 liquid glass over the photos. Archivo (wdth 125, weight 800) for the wordmark, Geist for UI. A cursor drives every change with real clicks, drags and long-presses. The camera zooms screen-studio style so each moment fills the square, and the cursor scales with it.
Banned: crossfades, blur-ins, brightness "developing", 3D flips, particles, glows, holds longer than 1s, anything that looks like a template.
</direction>

<structure>
120 BPM, 54 beats, something happens on every beat.
Open: the wordmark squeezes into its own period like an accordion, the dot grows into a black pill, a label rises inside it. Click: six iris blades close over the label and snap open onto a photo. The circle becomes a square, shrinks, the grid unfolds from behind it like a paper map (center, plus, corners), reflows into a bento, and a click zooms into one tile, landing exactly on the drop.
Glass: a glass word pops in letter by letter, melts into a droplet that stretches into a glass toolbar. The adjust icon turns it into a slider. Dragging relights the photo from day to golden hour (two aligned shots), and the knob turns into a glass lens while held. It lifts into a glass orb, the next photo opens inside it as a circle, and the orb expands into a lock screen: glass clock digits, date, and a home bar that stretches into a glass music player.
Stage: the lock screen pulls back into a phone (the bezel grows out of the screen edge). The Dynamic Island stretches like liquid, pinches off, flies over and grows into a Mac window that rolls up like a blind. Long-press the wallpaper, drag it onto a Safari tab, the page pushes in, drop it and it becomes the hero of a landing page. Scroll: the hero morphs into a framed print on a product card, with the mat and molding growing out of the photo's edge. Pick a frame color (it paints across) and a size, then the nav button flies down into "Order print".
Order: one black shape keeps morphing: Ordered ✓ → Printing % → On its way (a van on a route) → Delivered ✓.
Wall: the delivered circle floods the frame edge to edge, holds black for a beat, and contracts into the framed print hanging on the real wall footage. The same iris opens onto the print, closes again, the frame floods the screen and contracts into the pill → the dot → the letters spring back out, landing on the beat return. Last frame = first frame.
</structure>

<build>
1. One HTML file, square 1440x1440. Every style is computed from time inside an async seek(t): no CSS transitions, no timers, no state between frames.
2. Springs are closed-form step responses. A value with many targets is the sum of one spring per change, so it stays a pure function of time.
3. Liquid glass: each glass element holds its own clone of the scene behind it, filtered with an SVG feImage displacement map (a rounded-rect distance field) through three feDisplacementMaps at slightly different scales for chromatic edges, plus a rim light. Glass letters: a canvas distance field per glyph gives the map, mask and highlights.
4. Goo: blur + alpha threshold, then composite the source atop it so the glass stays sharp inside.
5. Iris: 6 blades around a hexagonal aperture. Each blade is its two vertices, both edge extensions and the SHORT arc between them.
6. Wordmark squeeze: every letter moves toward the dot by the same factor and its drawn width follows (narrow the wdth axis, scale the rest), so the letters stay touching.
7. Footage: re-encode all-intra (ffmpeg -g 1), load it as a blob URL, await 'seeked' before drawing each frame.
8. Sound: a downloaded SFX for every event (Mixkit), never synthesized, each placed by its measured peak. The song starts on a downbeat: the zoom lands on the drop, the wall sits in the breakdown, the wordmark returns with the beat. Loudnorm to -14 LUFS.
9. Render with Playwright: 4 subframes per frame blended with ffmpeg tmix, 60fps. Check one frame per beat, then scan for single-frame pops (frame-difference spikes 3x their neighbours).
</build>

<gotchas>
backdrop-filter: url() misreads displacement maps in Chromium, so clone the scene instead. A flood must overscale past the corners and take about 0.3s, or half the screen changes in one frame. A child with visibility: visible shows through a hidden parent, so use inherit. Text that swaps inside a morphing shape needs its own mask. python http.server can't range-seek video, so use the blob URL.
</gotchas>

<start>
Ask me for the inputs, then show me the beat map and 4 stills (open, glass, stage, wall) before you write the full film.
</start>
```

<details><summary>中文译文</summary>

```text
<inputs>
先问我要：一个用作文字标志的单词品牌名（动词效果最好）、9 到 12 张高分辨率照片、一首 120 BPM 左右、有 drop 和安静间奏段的免版税歌曲（Mixkit，可免费商用），以及一段植物影子在素墙上晃动的免费素材视频（Pexels）。
</inputs>

<direction>
一支苹果发布会风格的发布短片，只用 2D，一镜到底。每个场景都由上一个场景变出来：没有淡入淡出、没有模糊、没有剪切。物体靠改变形状来过渡：文字从遮罩线里升起，图标用弹簧从零弹出，条形横向画出，页面推入，一个黑色形状铺满整个画面，再收缩成下一个场景。暖白色画布，黑色 UI，照片上叠 iOS 26 液态玻璃。文字标志用 Archivo（wdth 125，字重 800），UI 用 Geist。每次变化都由光标通过真实的点击、拖拽和长按驱动。镜头像 Screen Studio 那样缩放，让每个瞬间都填满方形画面，光标也随之缩放。
禁止：交叉淡化、模糊入场、亮度「显影」、3D 翻转、粒子、辉光、停顿超过 1 秒、任何看起来像模板的东西。
</direction>

<structure>
120 BPM，54 拍，每一拍都有事发生。
开场：文字标志像手风琴一样挤进自己的句号，这个点长成一个黑色胶囊，里面升起一个标签。点击：六片光圈叶片合拢盖住标签，再猛地张开，露出一张照片。圆形变成方形并缩小，网格像纸质地图一样从它背后展开（中心、十字、四角），重排成 bento 布局，一次点击放大进其中一格，正好落在 drop 上。
玻璃：一个玻璃质感的单词逐字弹出，融化成一滴水珠，再拉伸成一条玻璃工具栏。调节图标把它变成滑块。拖动滑块把照片从白天重新打光成黄金时刻（两张对齐的照片），按住时滑块圆钮变成一枚玻璃透镜。它升起成一个玻璃球，下一张照片在球里以圆形打开，玻璃球再扩展成锁屏：玻璃质感的时钟数字、日期，以及一条拉伸成玻璃音乐播放器的 Home 条。
舞台：锁屏往后拉，变成一部手机（边框从屏幕边缘长出来）。灵动岛像液体一样拉长、掐断、飞过去，长成一个 Mac 窗口，再像百叶帘一样卷起。长按壁纸，把它拖到一个 Safari 标签页上，页面推入，松手后它成为一个落地页的主视觉。滚动：主视觉变形成商品卡片上的装裱画，卡纸和画框线条从照片边缘长出来。选一个画框颜色（颜色会刷过去）和一个尺寸，然后导航按钮飞下来变成「Order print」。
下单：一个黑色形状持续变形：Ordered ✓ → Printing % → On its way（一辆货车走在路线上）→ Delivered ✓。
墙面：送达的圆形从边到边铺满画面，保持黑色一拍，然后收缩成挂在真实墙面素材上的装裱画。同一个光圈在画上打开、再合上，画框铺满屏幕，再收缩成胶囊 → 点 → 字母弹回来，正好落在节拍回归处。最后一帧 = 第一帧。
</structure>

<build>
1. 一个 HTML 文件，正方形 1440x1440。所有样式都在一个 async seek(t) 里由时间算出：不用 CSS 过渡，不用定时器，帧与帧之间不保留状态。
2. 弹簧用闭式阶跃响应。一个有多个目标的值，等于每次改变各对应一个弹簧的叠加，所以它仍是时间的纯函数。
3. 液态玻璃：每个玻璃元素持有一份它背后场景的克隆，用 SVG feImage 位移贴图（一个圆角矩形距离场）过滤，经过三个比例略有不同的 feDisplacementMap 形成色散边缘，再加一圈边缘高光。玻璃字母：每个字形用一个 canvas 距离场生成贴图、遮罩和高光。
4. 粘滞（Goo）效果：模糊 + alpha 阈值，然后把源图合成在上面，让玻璃内部保持清晰。
5. 光圈：6 片叶片围绕一个六边形孔径。每片叶片由它的两个顶点、两条边的延长线以及两点之间较短的那段弧组成。
6. 文字标志挤压：每个字母都按同一个系数向句号靠拢，字形宽度随之变化（收窄 wdth 轴，其余部分缩放），这样字母始终挨在一起。
7. 素材视频：用全帧内编码重新编码（ffmpeg -g 1），以 blob URL 加载，每画一帧前 await 'seeked'。
8. 声音：每个事件都用一个下载的音效（Mixkit），绝不合成，每个都按它实测的峰值位置放置。歌曲从强拍开始：放大正好落在 drop 上，墙面段落放在安静间奏里，文字标志随节拍回归。响度标准化到 -14 LUFS。
9. 用 Playwright 渲染：每帧 4 个子帧，用 ffmpeg tmix 混合，60fps。每拍检查一帧，然后扫描单帧跳变（帧差达到相邻帧 3 倍的尖峰）。
</build>

<gotchas>
在 Chromium 里 backdrop-filter: url() 会读错位移贴图，所以改为克隆场景。铺满动画必须放大到超出四角，并且用大约 0.3 秒，否则半个屏幕会在一帧之内突变。父元素隐藏时，设了 visibility: visible 的子元素仍会显示出来，所以要用 inherit。在变形形状里切换的文字需要它自己的遮罩。python http.server 不能按范围跳转视频，所以用 blob URL。
</gotchas>

<start>
先问我要输入，然后在写完整短片之前，给我看节拍图和 4 张静帧（开场、玻璃、舞台、墙面）。
</start>
```

</details>

<sub>Inputs: Brand kit, Images, Music, Footage · Author: cost $0, no external tools.</sub>

[Original post ↗](https://x.com/twoclipping/status/2103835273813496100)

---

### Cosmos launch video in HyperFrames

<a href="https://x.com/kaolti/status/2103481296018092204"><img src="https://pbs.twimg.com/amplify_video_thumb/2103480314626539520/img/RtNxx6qWwdAK5CL4.jpg" alt="Cosmos launch video in HyperFrames" width="480"></a>

[@kaolti](https://x.com/kaolti) · 2026-09-25 · 🔖 1.8k · ▶ 64.7k · `Pipeline` · HyperFrames

A 40-second Cosmos launch video in HyperFrames Studio: one prompt researches and builds it, a second has Opus review it and make it 5x more exciting.

```text
Create a launch video for http://Cosmos.so using HyperFrames. Research http://Cosmos.so yourself and identify its unique value proposition, then communicate that proposition accurately. Make the video exciting, engaging, modern, and worthy of a contemporary product launch. Its UI, colors, typography, branding, design language, and motion language should feel unmistakably Cosmos. Choose the concept, story, copy, pacing, imagery, and animation yourself. Build a complete, playable HyperFrames Studio project in this folder, review it at normal speed, and give me the Studio link.

Needed this prompt 2 to improve it:

I want you to examine your result visually. I want you to examine the rhythm of it, the speed of it, everything, and look for ways to improve it. Remember that the goal is to make it exciting, more energetic, and more fit for social media, meaning probably quicker cuts and just more subtle detail and more subtle polish across the board.

As I'm looking at it, in some places it feels a bit slow. In some places it feels a bit boring. I need you to make it 5x more exciting. Think about using maybe 3JS, maybe some shaders, maybe whatever you need, or something to make it more exciting and more creative. Just make it much more creative, clever, fun to watch, and more exciting to watch, so that even if you're 10 years old and you have no idea what the video is about, you still want to watch to the end because it's just so fun and so exciting. Please create a v2 of it based on this feedback. You need to visually inspect your result and find the gap between what I described and what you currently have.
```

<details><summary>中文译文</summary>

```text
用 HyperFrames 为 http://Cosmos.so 做一支发布视频。自己去调研 http://Cosmos.so，找出它独特的价值主张，然后准确地传达这个主张。让视频令人兴奋、吸引人、现代，配得上一次当代的产品发布。它的 UI、配色、字体、品牌、设计语言和动效语言都要让人一眼认出是 Cosmos。概念、故事、文案、节奏、画面和动画都由你自己决定。在这个文件夹里搭一个完整、可播放的 HyperFrames Studio 项目，以正常速度检查一遍，然后把 Studio 链接给我。

还需要这第 2 条提示词来改进它：

我希望你从视觉上检查你的成果。检查它的节奏、速度，所有方面，找出可以改进的地方。记住目标是让它令人兴奋、更有活力、更适合社交媒体，这意味着大概要剪得更快，并且在各个方面加入更多细腻的细节和打磨。

我看的时候，有些地方感觉有点慢，有些地方感觉有点无聊。我需要你让它刺激 5 倍。考虑用用 3JS，或者一些着色器，或者任何你需要的东西，让它更刺激、更有创意。就是让它更有创意、更巧妙、更好看、更刺激，让一个 10 岁的孩子即使完全不知道视频在讲什么，也想看到最后，因为它实在太好玩、太刺激了。请根据这些反馈做一个 v2。你需要从视觉上检查你的成果，找出我描述的和你目前做出来的之间的差距。
```

</details>

<sub>Author: 2 prompts, no references.</sub>

[Original post ↗](https://x.com/kaolti/status/2103481296018092204) · Prompt posted in [this reply](https://x.com/kaolti/status/2103481493532148036).

---

### Minimal product launch video template

<a href="https://x.com/twoclipping/status/2102554209166000267"><img src="https://pbs.twimg.com/amplify_video_thumb/2102553635750125568/img/FhzzVrDbiRbpVBMN.jpg" alt="Minimal product launch video template" width="480"></a>

[@twoclipping](https://x.com/twoclipping) · 2026-09-23 · 🔖 1.4k · ▶ 50.1k · `Template` · Playwright · ffmpeg · Python

A 20-second 1080p product launch template cut to a 120 BPM beat grid, using your own vertical clips, masked type, a 3D video carousel and peak-aligned sound effects.

```text
<inputs>
Ask me for: the product name and a one-line promise, 3 to 5 UI moments to show, one accent color, 10 to 20 real vertical clips I own, and a royalty-free song with a clear drop (e.g. Mixkit, free for commercial use).
</inputs>

<direction>
High-end minimal. One idea per shot, lots of empty space, one accent color, one clean sans (Geist or Inter) with tight tracking. Masked type reveals, match cuts, one smooth camera language. Real footage only, never placeholder cards. No full stops in on-screen text.
Banned: shockwave rings, particle bursts, RGB split, camera shake, lens flares, neon glows, grid floors, flashing backgrounds, bouncy easing.
</direction>

<structure>
10 bars at 120 BPM, 2 seconds each.
Bar 1: the hook lands word by word on the beats.
Bar 2: one hook word morphs into the product UI. A cursor types and clicks.
The drop: a circle opens out of the button into a dark scene.
Then one move per bar: a wall of real clips with a scan line and 3 winners, the key output as big type, a 3D carousel of real videos with floor reflections and a motion-blurred whip onto one hero clip, the hero in a phone next to a panel that flips into results, big stats on push cuts, a 3-word ticker, a logo reveal, a fade to black.
</structure>

<build>
1. One HTML file at 1920x1080. Every style is computed from time inside http://window.seek(t): no CSS animations, no timers, no state between frames.
2. Real video: extract clips to 30fps JPEG sequences with ffmpeg and swap img sources per frame. seek awaits the image decodes.
3. Analyze the song with numpy: tempo, beat grid, energy per bar, the drop. Calibrate the grid to the real kick hits. Every cut sits on a downbeat, every UI hit on a beat.
4. Render with Playwright: 3 subframes per frame at t minus, at, and plus 1/240s, then blend with ffmpeg tmix for real motion blur at 60fps.
5. Place each sound effect so its measured peak, not its file start, lands on the event. Keep the effects quiet under the music. Loudnorm to -14 LUFS.
6. Probe 20 or more frames before the full render. Fix anything cluttered, overlapping or hard to read.
</build>

<gotchas>
Never set opacity or filter on a preserve-3d element, because it flattens and both faces show. Fade its wrapper instead. Measure element positions at runtime for match cuts. Only use music and sound effects whose license allows commercial use.
</gotchas>

<start>
Ask me for the inputs, then show me a storyboard with every timing on the beat grid before you write any code.
</start>
```

<details><summary>中文译文</summary>

```text
<inputs>
先问我要：产品名称和一句话承诺、要展示的 3 到 5 个 UI 瞬间、一种强调色、10 到 20 段我自己拥有的真实竖屏素材，以及一首有明显 drop 的免版税歌曲（例如 Mixkit，可免费商用）。
</inputs>

<direction>
高端极简。每个镜头只讲一个想法，大量留白，一种强调色，一种干净的无衬线字体（Geist 或 Inter），字距收紧。遮罩式文字出现、匹配剪辑、统一流畅的镜头语言。只用真实素材，绝不用占位卡片。屏幕文字里不用句号。
禁止：冲击波圆环、粒子爆发、RGB 分离、镜头抖动、镜头光晕、霓虹辉光、网格地面、闪烁背景、弹跳缓动。
</direction>

<structure>
120 BPM 下 10 小节，每小节 2 秒。
第 1 小节：钩子文案踩着节拍逐词出现。
第 2 小节：钩子里的一个词变形成产品 UI。光标打字并点击。
drop：一个圆从按钮里展开，进入一个深色场景。
之后每小节一个动作：一面真实素材墙，扫描线扫过并选出 3 个胜出者；关键产出用大字呈现；一个带地面倒影的真实视频 3D 轮播，带动态模糊地甩到一个主视频上；主视频放在手机里，旁边一个面板翻转出结果；推镜切换展示大号数据；一个 3 个词的滚动字幕条；logo 揭示；渐隐到黑。
</structure>

<build>
1. 一个 1920x1080 的 HTML 文件。所有样式都在 http://window.seek(t) 里由时间算出：不用 CSS 动画，不用定时器，帧与帧之间不保留状态。
2. 真实视频：用 ffmpeg 把素材抽成 30fps 的 JPEG 序列，每帧切换 img 的 src。seek 要等待图片解码完成。
3. 用 numpy 分析歌曲：速度、节拍网格、每小节能量、drop 的位置。把网格校准到真实的底鼓位置。每个剪辑点都落在强拍上，每个 UI 动作都落在拍子上。
4. 用 Playwright 渲染：每帧在 t 减 1/240 秒、t、t 加 1/240 秒取 3 个子帧，再用 ffmpeg tmix 混合，得到 60fps 的真实动态模糊。
5. 放置每个音效时，让它实测的峰值（而不是文件开头）落在事件上。音效压在音乐下面，保持小声。响度标准化到 -14 LUFS。
6. 完整渲染前先抽查 20 帧或更多。把杂乱、重叠或难以看清的地方都修好。
</build>

<gotchas>
永远不要在 preserve-3d 元素上设置 opacity 或 filter，因为它会被压平，正反两面都会显示出来。改为淡出它的外层容器。做匹配剪辑时，在运行时测量元素位置。只使用许可允许商用的音乐和音效。
</gotchas>

<start>
先问我要输入，然后在写任何代码之前，给我看一份所有时间点都排在节拍网格上的分镜。
</start>
```

</details>

<sub>Inputs: Brand kit, Footage, Music · Author: cost 0.</sub>

[Original post ↗](https://x.com/twoclipping/status/2102554209166000267)

---

### Product-focused motion graphics video template

<a href="https://x.com/ann_nnng/status/2103723183899852885"><img src="https://pbs.twimg.com/amplify_video_thumb/2103721031798325248/img/AQACnSg93oS7mh4T.jpg" alt="Product-focused motion graphics video template" width="480"></a>

[@ann_nnng](https://x.com/ann_nnng) · 2026-09-26 · 🔖 1.1k · ▶ 95.2k · `Template`

A 15-second motion graphics video about your product: Opus first visits the product pages, then writes the video content itself. Made in Claude Code.

```text
Make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are. The content should focus on [your product]. You should visit the pages first to learn about the product, then write the video content yourself.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒、充满动感的动态图形视频，展示你是多么出色的动效设计师。内容要聚焦在 [你的产品] 上。你应该先访问相关页面了解这个产品，然后自己写视频内容。
```

</details>

<sub>Inputs: Brand kit · Author: one prompt, almost an hour.</sub>

[Original post ↗](https://x.com/ann_nnng/status/2103723183899852885) · Prompt posted in [this reply](https://x.com/ann_nnng/status/2103759390386057227).

---

### SaaS launch video for a product Opus picks

<a href="https://x.com/moritzkremb/status/2103066071838466494"><img src="https://pbs.twimg.com/amplify_video_thumb/2103066013323624448/img/0dC1iLcOk74La4jK.jpg" alt="SaaS launch video for a product Opus picks" width="480"></a>

[@moritzkremb](https://x.com/moritzkremb) · 2026-09-24 · 🔖 946 · ▶ 88.8k · `Brief` · HyperFrames

A 46-second SaaS launch video where Opus picks a well-known product, pulls real assets from the web and edits a features-and-benefits promo, built with HyperFrames.

```text
I want you to create a highly professional SaaS product launch video. Go and find some SaaS, preferably just one that people know, so it's easier to identify with it. Pick that, and then make sure to get actual assets and images and all of that stuff from the internet. Turn it into these typical, very professionally edited, motion-graphics-styled product launch videos that you see people making on Twitter when they launch new SaaS products (which are showing off the features, the benefits, and all of these things).
```

<details><summary>中文译文</summary>

```text
我希望你做一支非常专业的 SaaS 产品发布视频。去找一个 SaaS，最好是大家都知道的，这样更容易有代入感。选定它，然后一定要从网上拿到真实的素材、图片之类的东西。把它做成那种典型的、剪辑非常专业的动态图形风格产品发布视频，就是大家在 Twitter 上发布新 SaaS 产品时做的那种（展示功能、好处等等）。
```

</details>

<sub>Also rendered from this prompt by: [@techyoutbe](https://x.com/techyoutbe/status/2103465227807588678)</sub>

[Original post ↗](https://x.com/moritzkremb/status/2103066071838466494) · Prompt posted in [this reply](https://x.com/moritzkremb/status/2103066083905417476).

---

### Product video for Distilbook

<a href="https://x.com/ajith_io/status/2103469807375208546"><img src="https://pbs.twimg.com/amplify_video_thumb/2103468768802615296/img/-D4Bgp8BO_e9WSyf.jpg" alt="Product video for Distilbook" width="480"></a>

[@ajith_io](https://x.com/ajith_io) · 2026-09-25 · 🔖 825 · ▶ 97.3k · `One-shot`

A 40-second motion graphics product video for Distilbook: Opus researches the product first, then treats the video as its own showreel. Made in Claude Code on max.

```text
Research Distilbook.Make a dynamic 40-second motion graphics video on Distilbook that shows what an incredible motion designer you are. like it's your showreel - Go all out.
```

<details><summary>中文译文</summary>

```text
调研 Distilbook。为 Distilbook 做一段 40 秒、充满动感的动态图形视频，展示你是多么出色的动效设计师。就像你的作品集一样——拿出全部本事。
```

</details>

<sub>Author: around 1 hour; about 1% of the weekly limit on the $200 plan.</sub>

<sub>Also rendered from this prompt by: [@itisRazak](https://x.com/itisRazak/status/2103517930424332386)</sub>

[Original post ↗](https://x.com/ajith_io/status/2103469807375208546)

---

### 30-second business explainer template

<a href="https://x.com/alex_prompter/status/2103499977632997524"><img src="https://pbs.twimg.com/amplify_video_thumb/2103499934280585216/img/Q9KDv9vq9R-KuDaY.jpg" alt="30-second business explainer template" width="480"></a>

[@alex_prompter](https://x.com/alex_prompter) · 2026-09-25 · 🔖 666 · ▶ 39.5k · `Template`

A fill-in template for a 30-second, 5-scene animated explainer about your business as a single HTML page, played in the Claude chat and screen-recorded.

```text
Adopt the role of an expert motion designer. Build a 30-second animated explainer for my business as a single HTML page. 5 scenes. The customer's problem, what I do, how it works in 3 steps, one proof point, and my name at the end. Bold text, smooth transitions, my brand colours. My business [DESCRIBE WHAT YOU SELL, WHO IT'S FOR AND YOUR COLOURS]
```

<details><summary>中文译文</summary>

```text
扮演一位专业动效设计师。为我的业务做一段 30 秒的动画讲解视频，做成单个 HTML 页面。5 个场景：客户的问题、我做什么、分 3 步讲它怎么运作、一个证明点，最后是我的名字。粗体文字，流畅转场，用我的品牌色。我的业务是 [描述你卖什么、卖给谁，以及你的品牌色]
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/alex_prompter/status/2103499977632997524)

---

### Slow-reveal logo animation

<a href="https://x.com/tdinh_me/status/2103704250329301409"><img src="https://pbs.twimg.com/amplify_video_thumb/2103703848015835136/img/Qy7eZ-z5vGDrSR1U.jpg" alt="Slow-reveal logo animation" width="480"></a>

[@tdinh_me](https://x.com/tdinh_me) · 2026-09-26 · 🔖 399 · ▶ 21.2k · `One-shot`

A 21-second motion design piece that slowly assembles and reveals the TypingMind logo; the author suggests reusing it by attaching your own product logo.

```text
Create an impressive motion design video of a slow-reveal transition that assembles and eventually reveals the TypingMind logo.
```

<details><summary>中文译文</summary>

```text
制作一段令人印象深刻的动效设计视频，用缓慢揭示的转场一点点拼合，最终揭示出 TypingMind 的 logo。
```

</details>

<sub>Inputs: Logo</sub>

[Original post ↗](https://x.com/tdinh_me/status/2103704250329301409)

---

### Promo video for the Wrapscribe app

<a href="https://x.com/shribuilds/status/2102827288190689364"><img src="https://pbs.twimg.com/amplify_video_thumb/2102827208108826624/img/qkMp0yVyvPjerjZe.jpg" alt="Promo video for the Wrapscribe app" width="480"></a>

[@shribuilds](https://x.com/shribuilds) · 2026-09-23 · 🔖 380 · ▶ 28.5k · `One-shot` · Remotion

A 41-second promo for Wrapscribe, a local dictation app; Opus read the codebase for features, used Remotion, and made voice-over and music through a fal.ai API key.

```text
Make a modern slick and punchy video for wrapscribe, check the wholebase to learn more about the features
```

<details><summary>中文译文</summary>

```text
为 wrapscribe 做一个现代、利落、有冲击力的视频，查看整个代码库来了解它的功能
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/shribuilds/status/2102827288190689364)

---

### Product story told by one morphing shape

<a href="https://x.com/verbove/status/2103483957266268381"><img src="https://pbs.twimg.com/amplify_video_thumb/2103483857836134400/img/ymXwmW0WgvP80pxi.jpg" alt="Product story told by one morphing shape" width="480"></a>

[@verbove](https://x.com/verbove) · 2026-09-25 · 🔖 336 · ▶ 15.6k · `Template` · Canvas · ffmpeg

A 20-second loop in which one shape morphs through a product's UI states on a 120 BPM grid, drawn on a single canvas and rendered with ffmpeg.

```text
<inputs>
Ask me for:
• my product + URL
• 8–12 UI states that tell its story
• the real data shown in each state
• brand colors + fonts + accent color
• required formats (1:1, 16:9, 9:16)
</inputs>

<rules>
One HTML file. One canvas
One draw(t) function

No CSS transitions
No timers
No state carried between frames

One shape, never cut

Every state is the same element changing size, radius and color while the content swaps

A cursor drives the sequence with real clicks, typing and one drag

Real UI. Real data. No placeholders.

</rules>
<structure>
120 BPM grid

Something happens on every bea

logo → button → handle field → “is this you?” → loader → pin → globe filling with users → matches → tabs → RSVP → search → logo

</structure>

<motion>
Closed-form springs everywhere with only a tiny overshoot.

If a value changes target multiple times, sum one spring per change

Content enters after its container starts morphing and leaves before the next morph so text never overlaps

Use a short blur on transitions

Never fade black directly into the accent color. Move an accent element between states instead

Make tab indicators stretch by putting each edge on a different spring

Zoom the camera so every state fills the frame

Make the last frame equal the first so the whole thing loops
</motion>

<export>
First render one frame per beat as a contact sheet

Fix anything cramped or broken

Then render every frame in headless Chrome at 60fps, averaging 6 subframes for motion blur

Pipe into ffmpeg:
H.264 + yuv420p

Export all aspect ratios in parallel
</export>
```

<details><summary>中文译文</summary>

```text
<inputs>
先问我要：
• 我的产品 + URL
• 讲出产品故事的 8–12 个 UI 状态
• 每个状态里展示的真实数据
• 品牌色 + 字体 + 强调色
• 需要的画幅（1:1、16:9、9:16）
</inputs>

<rules>
一个 HTML 文件。一个 canvas
一个 draw(t) 函数

不用 CSS transitions
不用计时器
帧与帧之间不保留状态

只有一个形状，从不切镜

每个状态都是同一个元素在改变尺寸、圆角和颜色，同时替换里面的内容

由一个光标用真实的点击、输入和一次拖拽推动整个序列

真实 UI。真实数据。不要占位内容。

</rules>
<structure>
120 BPM 节拍网格

每一拍都要发生点什么

logo → 按钮 → 用户名输入框 → “is this you?” → 加载 → 图钉 → 地球上布满用户 → 匹配 → 标签页 → RSVP → 搜索 → logo

</structure>

<motion>
所有地方都用闭式弹簧（closed-form springs），只带很小的过冲。

如果一个值多次改变目标，每次改变叠加一个弹簧

内容在容器开始变形之后才进入，在下一次变形之前离开，这样文字永远不会重叠

转场时加一点短暂的模糊

不要从黑色直接淡入强调色。改为让一个强调色元素在状态之间移动

让标签指示器的两条边各挂在不同的弹簧上，做出拉伸效果

推拉镜头，让每个状态都填满画面

让最后一帧等于第一帧，使整段循环
</motion>

<export>
先每一拍渲染一帧，拼成一张接触印样（contact sheet）

修掉任何拥挤或出错的地方

然后在 headless Chrome 里以 60fps 渲染每一帧，每帧平均 6 个子帧做运动模糊

通过管道送进 ffmpeg：
H.264 + yuv420p

所有画幅并行导出
</export>
```

</details>

<sub>Inputs: Screenshots, Data, Brand kit</sub>

[Original post ↗](https://x.com/verbove/status/2103483957266268381)

---

### 30-second showreel-style promo for Kody

<a href="https://x.com/kentcdodds/status/2103638102333858193"><img src="https://pbs.twimg.com/media/HTGewiSbkAAYD0o.jpg" alt="30-second showreel-style promo for Kody" width="480"></a>

[@kentcdodds](https://x.com/kentcdodds) · 2026-09-26 · 🔖 328 · ▶ 31.8k · `Brief` · Remotion

A 30-second motion graphics promo for the Kody project, adapted from the widely shared showreel prompt; Opus researched the topic, used Remotion, and also made a vertical version.

```text
make a dynamic 30-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out. Topic: Kody. Goal: make it click for people.

Start with research. You make all decisions. Feel free to make multiple videos. Output to my Dropbox and message me on discord with links.
```

<details><summary>中文译文</summary>

```text
制作一段 30 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。主题：Kody。目标：让人一下子看懂它。

先做调研。所有决定由你来做。可以做多个视频。输出到我的 Dropbox，并在 discord 上把链接发给我。
```

</details>

<sub>Author: about an hour and a half.</sub>

[Original post ↗](https://x.com/kentcdodds/status/2103638102333858193) · Prompt posted in [this reply](https://x.com/kentcdodds/status/2103638494388076905).

---

### Food-ordering app launch film in one take

<a href="https://x.com/twoclipping/status/2104022075782332440"><img src="https://pbs.twimg.com/amplify_video_thumb/2104021819627864064/img/zycZnL-F14ILzXtl.jpg" alt="Food-ordering app launch film in one take" width="480"></a>

[@twoclipping](https://x.com/twoclipping) · 2026-09-27 · 🔖 285 · ▶ 16.7k · `Template` · Playwright · ffmpeg

A 15-second 1080p product launch film in one continuous take where every scene morphs out of the last, cut to a 130 BPM song; rendered with Playwright and ffmpeg.

```text
<inputs>
Ask me for: my product and the one request a user types into it, 6 to 8 photos for the result cards, a royalty-free song around 130 BPM with a clear drop (Mixkit, free for commercial use), and my brand mark for the end card. If I skip any, use the defaults: the food-ordering story below, food photos from Pexels (fire noodles, birria tacos, hot chicken, buffalo wings, smash burger, spicy ramen) and Mixkit "Cat Walk".
</inputs>

<direction>
A 15 second product launch film, 1920x1080 at 60fps, 2D only, one continuous take. Every scene is made out of the previous one: nothing fades, blurs or cuts. Objects change shape instead: text rises out of a mask line, buttons grow into pages, a color floods out of one object and later shrinks back into another. The camera makes one move per scene on eased keyframes and never zooms in and out back to back.
Look: warm white canvas #f5f5f2, black UI #0e0e10, lime accent #cdf24f, one orange #ff6a2a, a blue send button #2f6bff. An Apple Intelligence style iridescent glow (a rotating conic gradient of pink, orange, lime, cyan and violet, blurred) around the input. Real food photography on dark cards. Geist for UI, a serif for the product name on the end card.
Banned: crossfades, blur-ins, 3D, particles, camera moves that reverse direction, holds longer than 1s, anything that looks like a template.
</direction>

<structure>
130 BPM, 32 beats (14.8s). The song starts 12 beats before its drop.
Beats 0-6, ask: close on the glowing composer (about 3x zoom, a slow push). The request types on three fixed lines with a real keystroke rhythm: "I'm really hungry, I don't know / what I want but something / spicy, crispy and filling".
Beat 6, send: the send button presses, a lime fill ripples out of it and turns the message into the chat bubble, and one pull-back grows the phone around it (428x900 screen, 11px black bezel, 9:41 status bar).
Beats 6-12, think: the send button grows into an orange wok (a half-disc with a thin handle) that tosses 6 colored ingredients on beats 8, 9, 10 and 11, under a shimmering "Finding something for you…".
Beat 12, the drop: a lime circle floods out of the wok edge to edge in about 0.35s. Dark food cards (330x440, radius 28, photo on top, name, one-line description, price, rating) burst in from the center, and the strip slides three cards onto "Fire Noodles", which lifts with a "Best match" pill.
Beats 16-21, chat: the lime shrinks back into the user's bubble carrying its words, and the chosen card flies into its slot. "Found it. Fire Noodles from Wok & Fire, smoky, spicy and seriously filling." rises in, then "Want me to order it for you?" and two pills pop in: "Order now" (black) and "More options" (outline). The cursor clicks Order now → spinner → "✓ Ordered".
Beats 21-32, outro: the black button grows into the whole page. It stays a pill until it reaches the edges while the camera pushes into it, and its label grows to headline size, then slides out. "You were craving noodles." then "Now it's on the way." rise word by word (92px, white on black), a courier dot rides a route to a pin, the pin becomes the brand mark, and the wordmark wipes out from behind it with "made with" above and the product name below.
</structure>

<build>
1. One HTML file, 1920x1080. Every style is computed from time inside seek(t): no CSS transitions, no timers, no state between frames.
2. The camera is one transform on a container, keyed [time, zoom, x, y] with eased segments and zoom interpolated in log space.
3. Springs are closed-form step responses for every pop and settle.
4. Every handoff between layers is a shared element: the lime flood carries a copy of the bubble's words, the button carries its own label into the page.
5. Sound: a downloaded SFX for every event (Mixkit): typing, the send pop, a pop per toss, an impact on the drop, a swoosh for the cards, a click, a success tone, a whoosh as the button fills the page, a sparkle on the mark. Place each by its measured peak and loudnorm to -14 LUFS.
6. Render with Playwright: 8 subframes per frame blended with ffmpeg tmix, 60fps. Then step through every fast moment frame by frame and scan the whole video for single-frame pops.
</build>

<gotchas>
4 subframes leave ghost copies on fast moves, so use 8 and slow the move down. A flood must clear the farthest corner and take about 0.35s, or it reads as a flash. Set z-index on every layer, or the card floats over the flood. Never let the camera chase a wrapping text cursor: fixed lines only. Declare every variable before the first seek() runs.
</gotchas>

<start>
Ask me for the inputs, then show me the beat map and 4 stills (ask, drop, chat, outro) before you write the full film.
</start>
```

<details><summary>中文译文</summary>

```text
<inputs>
先问我要：我的产品，以及用户在产品里输入的那一条请求；结果卡片用的 6 到 8 张照片；一首 130 BPM 左右、有明显 drop 的免版税歌曲（Mixkit，可免费商用）；以及片尾卡用的品牌标志。如果我跳过任何一项，就用默认值：下面这个点餐故事，来自 Pexels 的食物照片（fire noodles、birria tacos、hot chicken、buffalo wings、smash burger、spicy ramen），以及 Mixkit 的 "Cat Walk"。
</inputs>

<direction>
一支 15 秒的产品发布片，1920x1080，60fps，纯 2D，一镜到底。每个场景都由上一个场景变化而来：没有淡入淡出、没有模糊、没有剪切。物体靠改变形状完成过渡：文字从一条遮罩线里升起，按钮长成页面，一种颜色从一个物体里涌出，之后又缩回另一个物体。摄像机每个场景只做一个动作，用缓动关键帧，绝不连着先推近再拉远。
外观：暖白画布 #f5f5f2，黑色 UI #0e0e10，青柠强调色 #cdf24f，一种橙色 #ff6a2a，蓝色发送按钮 #2f6bff。输入框周围有 Apple Intelligence 风格的虹彩光晕（粉、橙、青柠、青、紫组成的旋转圆锥渐变，加模糊）。深色卡片上放真实的美食摄影。UI 用 Geist，片尾卡上的产品名用一款衬线字体。
禁止：交叉淡化、模糊入场、3D、粒子、方向来回反转的镜头运动、超过 1 秒的停顿、任何看起来像模板的东西。
</direction>

<structure>
130 BPM，32 拍（14.8 秒）。歌曲从 drop 前 12 拍开始。
第 0-6 拍，提问：特写发光的输入框（约 3 倍缩放，缓慢推近）。请求文字以真实的敲键节奏分三行固定打出："I'm really hungry, I don't know / what I want but something / spicy, crispy and filling"。
第 6 拍，发送：发送按钮按下，一圈青柠色从按钮里荡开，把消息变成聊天气泡，然后一次拉远，让手机在它周围长出来（428x900 屏幕，11px 黑色边框，9:41 状态栏）。
第 6-12 拍，思考：发送按钮长成一只橙色炒锅（半圆加一根细把手），在第 8、9、10、11 拍颠锅，抛起 6 种彩色食材，下方是闪烁的 "Finding something for you…"。
第 12 拍，drop：一个青柠色圆在约 0.35 秒内从锅沿涌出、铺满整个画面。深色美食卡片（330x440，圆角 28，上方照片，下面是名称、一行描述、价格、评分）从中心爆开，卡片条滑过三张后停在 "Fire Noodles"，它浮起并带上 "Best match" 标签。
第 16-21 拍，聊天：青柠色带着那句话缩回用户的气泡里，被选中的卡片飞进自己的位置。"Found it. Fire Noodles from Wok & Fire, smoky, spicy and seriously filling." 升起，然后是 "Want me to order it for you?"，接着弹出两个药丸按钮："Order now"（黑色）和 "More options"（描边）。光标点击 Order now → 加载转圈 → "✓ Ordered"。
第 21-32 拍，结尾：黑色按钮长成整个页面。它在碰到边缘前一直保持药丸形状，同时摄像机推进去，按钮文字放大到标题大小后滑出。"You were craving noodles." 然后 "Now it's on the way." 逐词升起（92px，黑底白字），一个快递小圆点沿路线跑到一枚图钉，图钉变成品牌标志，文字标识从它身后擦出，上方是 "made with"，下方是产品名。
</structure>

<build>
1. 一个 HTML 文件，1920x1080。所有样式都在 seek(t) 里根据时间计算：不用 CSS transitions，不用计时器，帧与帧之间不保留状态。
2. 摄像机是容器上的一个 transform，按 [time, zoom, x, y] 设关键帧，分段缓动，缩放在对数空间插值。
3. 每一次弹出和回落都用闭式阶跃响应的弹簧。
4. 图层之间的每次交接都是共享元素：青柠色涌流带着气泡里那句话的副本，按钮带着自己的文字进入页面。
5. 声音：每个事件都配一个下载的音效（Mixkit）：打字声、发送的“啵”声、每次颠锅一声“啵”、drop 时的撞击声、卡片的嗖声、点击声、成功提示音、按钮铺满页面时的呼啸声、标志出现时的闪光声。按实测的峰值位置放置每个音效，并 loudnorm 到 -14 LUFS。
6. 用 Playwright 渲染：每帧 8 个子帧，用 ffmpeg tmix 混合，60fps。然后逐帧检查每个快速段落，并扫描整段视频，找出只闪现一帧的跳变。
</build>

<gotchas>
4 个子帧在快速运动时会留下重影，所以用 8 个，并把运动放慢。涌流必须覆盖到最远的角落，并持续约 0.35 秒，否则看起来像闪了一下。给每个图层都设 z-index，否则卡片会浮在涌流上面。绝不要让摄像机追着会换行的文字光标跑：只用固定的行。在第一次运行 seek() 之前声明好所有变量。
</gotchas>

<start>
先问我要输入素材，然后给我看节拍图和 4 张静帧（ask、drop、chat、outro），再写完整的片子。
</start>
```

</details>

<sub>Inputs: Images, Music, Logo</sub>

[Original post ↗](https://x.com/twoclipping/status/2104022075782332440)

---

### Social promo for Lightspark

<a href="https://x.com/davidmarcus/status/2103275618045686217"><img src="https://pbs.twimg.com/amplify_video_thumb/2103275588102537216/img/XBVUX6UkVQNuB2ek.jpg" alt="Social promo for Lightspark" width="480"></a>

[@davidmarcus](https://x.com/davidmarcus) · 2026-09-25 · 🔖 276 · ▶ 25.1k · `One-shot`

A 23-second social promo for Lightspark's capabilities, with sound, made in one shot; the author notes Claude already had business context from earlier chats.

```text
make a punchy and modern short video for social that promotes @lightspark capabilities. Needs to be production grade with sound
```

<details><summary>中文译文</summary>

```text
做一段有冲击力、现代感的社交媒体短视频，宣传 @lightspark 的能力。要达到可直接上线的制作水准，并带声音
```

</details>

<sub>Author: about 5 minutes, one shot.</sub>

[Original post ↗](https://x.com/davidmarcus/status/2103275618045686217)

---

### Motion-designer promo video for mdfor.dev

<a href="https://x.com/HO_BA/status/2103845264649761062"><img src="https://pbs.twimg.com/amplify_video_thumb/2103844160612564992/img/AgKjqlrBOXqriKD0.jpg" alt="Motion-designer promo video for mdfor.dev" width="480"></a>

[@HO_BA](https://x.com/HO_BA) · 2026-09-26 · 🔖 198 · ▶ 10.1k · `Brief` · Remotion

A 30-second promo for mdfor.dev built on the showreel prompt, with product screenshots broken into animated components and motion synced to music.

```text
Make a dynamic 30-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.  Make it a video to introduce https://mdfor.dev Use actual product screenshot/logo/assets Must have music and motion must match the music  Do it like a real professional production video, not like a demo or prototype. Add more animation and motion design; avoid using screenshots as raw; instead, break them down into components/icons so we can animate those too. Make the motions more juicy. Use the best motion design techniques you can.
```

<details><summary>中文译文</summary>

```text
做一段 30 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。把它做成介绍 https://mdfor.dev 的视频。使用真实的产品截图 / logo / 素材。必须有音乐，而且动作要和音乐对上。要做得像真正的专业制作视频，而不是 demo 或原型。加入更多动画和动效设计；不要直接使用原始截图，而是把它们拆成组件 / 图标，这样也能给它们做动画。让动作更有弹性、更带劲。用上你能用的最好的动效设计技巧。
```

</details>

<sub>Inputs: Screenshots, Logo · Effort: high</sub>

[Original post ↗](https://x.com/HO_BA/status/2103845264649761062)

---

### Pig love-note story that teases an app

<a href="https://x.com/jackfriks/status/2103132260589338762"><img src="https://pbs.twimg.com/amplify_video_thumb/2103131986701230082/img/9PcFlH2KPZDZVz_U.jpg" alt="Pig love-note story that teases an app" width="480"></a>

[@jackfriks](https://x.com/jackfriks) · 2026-09-24 · 🔖 192 · ▶ 51.3k · `One-shot`

A 20-second 9:16 story built from the app's pig assets, where a pig leaves love notes in a mailbox, with code-made sound and an app tease.

```text
can you help me use the pig assets on new branch of lovelee to make a 9:16 short story animation with sound effects about the pig sending his partner love notes in the mailbox and make it fun and good tease app at end?
```

<details><summary>中文译文</summary>

```text
你能帮我用 lovelee 新分支上的小猪素材，做一个 9:16 的带音效的短篇故事动画吗？讲小猪往信箱里给伴侣送情书，做得有趣一点，结尾好好预告一下这个应用？
```

</details>

<sub>Inputs: Images · Author: one shot, no edits.</sub>

<sub>Also rendered from this prompt by: [@jackfriks](https://x.com/jackfriks/status/2103134485910892602)</sub>

[Original post ↗](https://x.com/jackfriks/status/2103132260589338762) · Prompt posted in [this reply](https://x.com/jackfriks/status/2103134485910892602).

---

### Motion-designer promo video for any website

<a href="https://x.com/melvynx/status/2103714680577638493"><img src="https://pbs.twimg.com/amplify_video_thumb/2103714633022660608/img/4FEeSzXVDGyk7aqL.jpg" alt="Motion-designer promo video for any website" width="480"></a>

[@melvynx](https://x.com/melvynx) · 2026-09-26 · 🔖 161 · ▶ 26.1k · `Template`

A fill-in-the-URL version of the showreel prompt; the author used it for a 45-second Lumail.io promo.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are for <website url>
```

<details><summary>中文译文</summary>

```text
为 <website url> 做一段 15 秒的动态图形视频，展示你是多么出色的动效设计师
```

</details>

<sub>Inputs: Brand kit · Author: under 10 minutes.</sub>

[Original post ↗](https://x.com/melvynx/status/2103714680577638493)

---

### Launch video for otto.doti.gg Ideate

<a href="https://x.com/condzxyz/status/2102863918033178789"><img src="https://pbs.twimg.com/amplify_video_thumb/2102863656069255168/img/dQ_UHgzfUhJp8JS9.jpg" alt="Launch video for otto.doti.gg Ideate" width="480"></a>

[@condzxyz](https://x.com/condzxyz) · 2026-09-23 · 🔖 124 · ▶ 14.7k · `One-shot`

A 37-second launch video for a product page, from a one-line Portuguese prompt that only gives the URL and asks for top quality.

```text
Faça um video para o https://otto.doti.gg/ideate de EXTREMA qualidade não cometa erros. obg claudinho!
```

<details><summary>English translation</summary>

```text
Make a video for https://otto.doti.gg/ideate of EXTREME quality, don't make mistakes. thanks claudinho!
```

</details>

<sub>Inputs: Brand kit · Author: one prompt.</sub>

[Original post ↗](https://x.com/condzxyz/status/2102863918033178789) · Prompt posted in [this reply](https://x.com/condzxyz/status/2102875096092491998).

---

### Product promo made with Playwright and FFmpeg

<a href="https://x.com/thallisribeiro/status/2103107359727829318"><img src="https://pbs.twimg.com/amplify_video_thumb/2103106937088786432/img/35N6v4ZNr7iOs3GO.jpg" alt="Product promo made with Playwright and FFmpeg" width="480"></a>

[@thallisribeiro](https://x.com/thallisribeiro) · 2026-09-24 · 🔖 115 · ▶ 7.3k · `One-shot` · Playwright · ffmpeg

A 20-second modern promo for a product website, from a two-sentence Portuguese prompt that limits the tools to JavaScript, Playwright and FFmpeg.

```text
Use apenas: JavaScript, Playwright e FFmpeg. Faça um vídeo moderno, elegante e impactante para meu produto (https://licitacerta.com.br)
```

<details><summary>English translation</summary>

```text
Use only: JavaScript, Playwright and FFmpeg. Make a modern, elegant and impactful video for my product (https://licitacerta.com.br)
```

</details>

<sub>Inputs: Brand kit · Author: one prompt.</sub>

[Original post ↗](https://x.com/thallisribeiro/status/2103107359727829318) · Prompt posted in [this reply](https://x.com/thallisribeiro/status/2103134082267750805).

---

### Milestone launch video for MotionSites AI

<a href="https://x.com/viktoroddy/status/2103802280617402509"><img src="https://pbs.twimg.com/amplify_video_thumb/2103800410326945792/img/vjPCCzyDFZ6EfMOG.jpg" alt="Milestone launch video for MotionSites AI" width="480"></a>

[@viktoroddy](https://x.com/viktoroddy) · 2026-09-26 · 🔖 91 · ▶ 7.8k · `One-shot`

A 54-second launch-style video marking MotionSites AI reaching one million monthly visitors, from a single-sentence prompt and one revision.

```text
Create a launch video for MotionSites AI, just hit 1 million monthly visitors after 8 months after launch.
```

<details><summary>中文译文</summary>

```text
为 MotionSites AI 做一支发布视频：上线 8 个月后，月访问量刚刚突破 100 万。
```

</details>

<sub>Author: generated in 4 minutes, with one change.</sub>

[Original post ↗](https://x.com/viktoroddy/status/2103802280617402509)

---

### 15-second launch video for an AI SDR

<a href="https://x.com/iuditg/status/2103920117025554453"><img src="https://pbs.twimg.com/amplify_video_thumb/2103918795136143361/img/UQ2575JoURwVLGZ9.jpg" alt="15-second launch video for an AI SDR" width="480"></a>

[@iuditg](https://x.com/iuditg) · 2026-09-26 · 🔖 83 · ▶ 8.9k · `Brief` · Remotion

A 15-second kinetic launch video for FirstSales, an AI cold-email SDR, using its real SVG logo, colors, Manrope type and UI, rendered with Remotion.

```text
Make a 15-second launch video for http://firstsales.io, an AI SDR (sales rep) for cold email. Make it showreel-grade: dynamic, kinetic motion graphics. Go all out.

Use the real brand: the FirstSales SVG logo (animate its strokes), the app's colors, Manrope type, icons, and UI components. The logo is a short stinger.

The product is the hero.

Rules: all demo data is fake (made-up people and companies, no real leads). Show only real product claims. Something moves on every beat. Text is never covered.
```

<details><summary>中文译文</summary>

```text
为 http://firstsales.io 制作一段 15 秒的发布视频，这是一款做冷邮件的 AI SDR（销售代表）。要做到作品集级别：动感十足的动态图形。拿出全部本事。

使用真实的品牌素材：FirstSales 的 SVG logo（给它的描边做动画）、应用的配色、Manrope 字体、图标和 UI 组件。logo 只做一个简短的 stinger 标识动画。

产品是主角。

规则：所有演示数据都是假的（虚构的人和公司，不用真实线索）。只展示产品真实具备的能力。每一拍都要有东西在动。文字永远不被遮挡。
```

</details>

<sub>Inputs: Brand kit, Logo · Author: about 40 minutes and $20.62.</sub>

[Original post ↗](https://x.com/iuditg/status/2103920117025554453) · Prompt posted in [this reply](https://x.com/iuditg/status/2103920119487586307).

---

### 15-second promo for the Stuff app

<a href="https://x.com/austnstuff/status/2104020914413441103"><img src="https://pbs.twimg.com/amplify_video_thumb/2104020538599567361/img/Mc4AB_Oqbx_VfRRr.jpg" alt="15-second promo for the Stuff app" width="480"></a>

[@austnstuff](https://x.com/austnstuff) · 2026-09-27 · 🔖 82 · ▶ 6.5k · `One-shot`

A 15-second promo for Stuff, a to-do and lists app, from a one-line prompt on the first try.

```text
make a 15-second promo video for Stuff
```

<details><summary>中文译文</summary>

```text
为 Stuff 制作一段 15 秒的宣传视频
```

</details>

<sub>Inputs: Brand kit · Author: first try.</sub>

[Original post ↗](https://x.com/austnstuff/status/2104020914413441103)

---

### Brand reel from nothing but a URL

<a href="https://x.com/justinmfarrugia/status/2103822390870569266"><img src="https://pbs.twimg.com/amplify_video_thumb/2103820504968675328/img/clYCvV8zIjupLTCQ.jpg" alt="Brand reel from nothing but a URL" width="480"></a>

[@justinmfarrugia](https://x.com/justinmfarrugia) · 2026-09-26 · 🔖 80 · ▶ 7k · `One-shot`

A 15-second brand reel for curated.supply generated from just the site URL, with no fine-tuning or second pass.

```text
make a reel for https://curated.supply
```

<details><summary>中文译文</summary>

```text
为 https://curated.supply 做一条 reel 短视频
```

</details>

<sub>Inputs: Brand kit · Author: single pass, no fine-tuning.</sub>

[Original post ↗](https://x.com/justinmfarrugia/status/2103822390870569266)

---

### SaaS launch video from a website

<a href="https://x.com/gouthamjay8/status/2103816261339910269"><img src="https://pbs.twimg.com/amplify_video_thumb/2103815750389768192/img/PsaYtA-4ptaOkHOs.jpg" alt="SaaS launch video from a website" width="480"></a>

[@gouthamjay8](https://x.com/gouthamjay8) · 2026-09-26 · 🔖 69 · ▶ 5.8k · `Template`

A 55-second SaaS launch video built from the product's website and real online assets; Opus found and animated the site's mascot unprompted.

```text
I want you to create a highly professional SaaS product launch video. Go and look up [website] Pick that, and then make sure to get actual assets and images and all of that stuff from the internet. Turn it into these typical, very professionally edited, motion-graphics-styled product launch videos that you see people making on Twitter when they launch new SaaS products (which are showing off the features, the benefits, and all of these things). It should show what an incredible motion designer you are, like it's your showreel for a resume. Go all out.
```

<details><summary>中文译文</summary>

```text
我想让你制作一段非常专业的 SaaS 产品发布视频。去查一下 [website]，就选它，然后一定要从网上拿到真实的素材、图片之类的东西。把它做成那种典型的、剪辑非常专业的动态图形风格产品发布视频，就是大家在 Twitter 上发布新 SaaS 产品时常做的那种（展示功能、好处等等）。它要展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。
```

</details>

<sub>Inputs: Brand kit · Author: one shot.</sub>

[Original post ↗](https://x.com/gouthamjay8/status/2103816261339910269) · Prompt posted in [this reply](https://x.com/gouthamjay8/status/2103816558523159008).

---

### 15-second account intro from a logo

<a href="https://x.com/fire_ozgur/status/2103459971174130104"><img src="https://pbs.twimg.com/amplify_video_thumb/2103459235879059456/img/YuXk72J_lWynhi7U.jpg" alt="15-second account intro from a logo" width="480"></a>

[@fire_ozgur](https://x.com/fire_ozgur) · 2026-09-25 · 🔖 68 · ▶ 25.1k · `Brief`

A 15-second motion graphics intro for the author's X account, built from his logo and X cover image with no manual edits.

```text
Ne kadar iyi bir grafik tasarımcısı olduğunu bilmek istiyorum. Bana bunu kanıtlamak için 15 saniyelik bir hareketli grafik videosu hazırlamanı istiyorum. Benim hesabımla ilgili bir tanıtım yapmanı istiyorum. Logo'mu ve  X'te kapak resmimi paylaşıyorum, bunları da kullan.
```

<details><summary>English translation</summary>

```text
I want to know how good a graphic designer you are. To prove it to me, I want you to make a 15-second motion graphics video. I want you to make an introduction about my account. I'm sharing my logo and my cover image on X; use them too.
```

</details>

<sub>Inputs: Logo, Images · Author: one prompt, no edits.</sub>

[Original post ↗](https://x.com/fire_ozgur/status/2103459971174130104)

---

### Distilbook promo in a reference video's style

<a href="https://x.com/ajith_io/status/2103541149709615243"><img src="https://pbs.twimg.com/amplify_video_thumb/2103540363705421824/img/eJy0OBfGMNk8aoXs.jpg" alt="Distilbook promo in a reference video&#x27;s style" width="480"></a>

[@ajith_io](https://x.com/ajith_io) · 2026-09-25 · 🔖 65 · ▶ 10.8k · `Brief`

A 30-second code-made promo for Distilbook that reuses the visual style of a reference video Opus downloads itself; the final cut has no manual edits.

```text
Take reference from the given video (download it) and use the same visual style.
and Research about Distilbook. Make a dynamic 30-second motion graphics video on Distilbook that shows what an incredible motion designer you are. like it's your showreel - Go all out.
One thing to keep in mind: it should be cool as fck.
```

<details><summary>中文译文</summary>

```text
参考给定的视频（把它下载下来），使用同样的视觉风格。
然后研究一下 Distilbook。制作一段关于 Distilbook 的 30 秒动态图形视频，展示你是多么出色的动效设计师。就像你的作品集一样——拿出全部本事。
有一点要记住：它必须酷到爆。
```

</details>

<sub>Inputs: Reference video, Brand kit · Author: final version, no manual edits.</sub>

[Original post ↗](https://x.com/ajith_io/status/2103541149709615243)

---

### Showreel prompt turned app launch video

<a href="https://x.com/MustaphaFenzar/status/2103708363074973906"><img src="https://pbs.twimg.com/amplify_video_thumb/2103708320368668672/img/J8hkxK6JppirdCya.jpg" alt="Showreel prompt turned app launch video" width="480"></a>

[@MustaphaFenzar](https://x.com/MustaphaFenzar) · 2026-09-26 · 🔖 64 · ▶ 7k · `One-shot`

The famous showreel prompt plus one line that turns it into a 15-second launch video for the Mounis app, made in one shot.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.

  it should be a launch app video for https://mounis.app/
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。

它应该是 https://mounis.app/ 的应用发布视频
```

</details>

<sub>Inputs: Brand kit · Author: one shot.</sub>

[Original post ↗](https://x.com/MustaphaFenzar/status/2103708363074973906) · Prompt posted in [this reply](https://x.com/MustaphaFenzar/status/2103708532747174223).

---

### Distilbook explainer with an Oppenheimer-style score

<a href="https://x.com/ajith_io/status/2103800569584562538"><img src="https://pbs.twimg.com/amplify_video_thumb/2103800326029787136/img/YWu2Y3Nq01psafxf.jpg" alt="Distilbook explainer with an Oppenheimer-style score" width="480"></a>

[@ajith_io](https://x.com/ajith_io) · 2026-09-26 · 🔖 54 · ▶ 4.3k · `One-shot`

A 40-second motion graphics promo explaining Distilbook, scored with original music Opus composed in the spirit of the Oppenheimer theme.

```text
Make a dynamic 40-second motion graphics video on Distilbook that shows what an incredible motion designer you are, like it's your showreel - go all out. Use the Oppenheimer theme music as inspiration, but compose it yourself.
```

<details><summary>中文译文</summary>

```text
制作一段关于 Distilbook 的 40 秒动态图形视频，展示你是多么出色的动效设计师，就像你的作品集一样——拿出全部本事。以《奥本海默》的主题音乐为灵感，但要自己作曲。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/ajith_io/status/2103800569584562538)

---

### Animated case for why celld matters

<a href="https://x.com/0xnfrith/status/2103358957050068999"><img src="https://pbs.twimg.com/amplify_video_thumb/2103358243171102720/img/TWeVcCN2Kdmqquxu.jpg" alt="Animated case for why celld matters" width="480"></a>

[@0xnfrith](https://x.com/0xnfrith) · 2026-09-25 · 🔖 43 · ▶ 16.7k · `One-shot`

A 53-second animation making the case for the author's product celld, from a one-line prompt inside a project that held more context.

```text
make me an animation to explain why celld earns its place.
```

<details><summary>中文译文</summary>

```text
给我做一段动画，解释 celld 凭什么值得占一席之地。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/0xnfrith/status/2103358957050068999)

---

### 5-minute New York travel promo

<a href="https://x.com/LinearUncle/status/2103705625075331442"><img src="https://pbs.twimg.com/amplify_video_thumb/2103704659915583488/img/Ih2j5PSOpVEsQKJ9.jpg" alt="5-minute New York travel promo" width="480"></a>

[@LinearUncle](https://x.com/LinearUncle) · 2026-09-26 · 🔖 43 · ▶ 4.7k · `Brief` · TTS

A roughly 5-minute Chinese-language New York travel promo aimed at Singaporeans, with free stock footage and music Opus found itself and an edge-tts voiceover.

```text
给我制作一个介绍纽约的视频，视频素材和背景音全部找商用免费的平台,  配音请使用edge-tts，选择男音，字幕和声音都是中文，时长５分钟左右，这个视频将用来吸引新加坡人去纽约旅游
```

<details><summary>English translation</summary>

```text
Make me a video introducing New York. Find all the footage and background audio on platforms that are free for commercial use. For the voiceover use edge-tts with a male voice. Subtitles and voice are both in Chinese, about 5 minutes long. This video will be used to attract Singaporeans to travel to New York
```

</details>

[Original post ↗](https://x.com/LinearUncle/status/2103705625075331442)

---

### 20-second launch video for founder.page

<a href="https://x.com/RatheeJaisal/status/2103774864742154698"><img src="https://pbs.twimg.com/amplify_video_thumb/2103774351396880384/img/_aGzxq9BE8dXq8jf.jpg" alt="20-second launch video for founder.page" width="480"></a>

[@RatheeJaisal](https://x.com/RatheeJaisal) · 2026-09-26 · 🔖 41 · ▶ 2.9k · `One-shot`

A fast-paced launch video of 20 seconds covering founder.page's key features in its brand style, made in Claude Code in one shot.

```text
build me a beautiful launch video 20 seconds or under that shows all our key features, make it fast paced and fit our brand
```

<details><summary>中文译文</summary>

```text
给我做一段漂亮的发布视频，20 秒以内，展示我们所有的核心功能，节奏要快，要符合我们的品牌
```

</details>

<sub>Inputs: Brand kit · Author: one shot.</sub>

[Original post ↗](https://x.com/RatheeJaisal/status/2103774864742154698)

---

### 15-second showreel about Omarchy

<a href="https://x.com/tcballard/status/2103441222375268605"><img src="https://pbs.twimg.com/amplify_video_thumb/2103441181703106560/img/b07u4ufTbMHuiXck.jpg" alt="15-second showreel about Omarchy" width="480"></a>

[@tcballard](https://x.com/tcballard) · 2026-09-25 · 🔖 40 · ▶ 13.6k · `One-shot`

The famous showreel prompt refocused on Omarchy, producing a 15-second promo-style motion graphics reel about it.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it’s your showreel for a résumé. go all out. It should be focused on Omarchy
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。内容要聚焦 Omarchy
```

</details>

[Original post ↗](https://x.com/tcballard/status/2103441222375268605) · Prompt posted in [this reply](https://x.com/tcballard/status/2103441225231585383).

---

### 15-second brand promo template

<a href="https://x.com/Oriebir_br/status/2103603449971757395"><img src="https://pbs.twimg.com/amplify_video_thumb/2103588638768439297/img/O7tA1fCFZRv2yzUT.jpg" alt="15-second brand promo template" width="480"></a>

[@Oriebir_br](https://x.com/Oriebir_br) · 2026-09-25 · 🔖 35 · ▶ 4k · `Template`

A 15-second promo for the author's brand Oriebir, from a showreel-style template with a brand-name slot and an attached branding image.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your best (your brand) explaining in 15 seconds. go all out. (image attached for branding reference)
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像用 15 秒讲清楚你最好的（你的品牌）一样。拿出全部本事。（附上图片作为品牌参考）
```

</details>

<sub>Inputs: Brand kit, Images · Effort: max · Author: under 2 minutes spent on the prompt.</sub>

[Original post ↗](https://x.com/Oriebir_br/status/2103603449971757395) · Prompt posted in [this reply](https://x.com/Oriebir_br/status/2103987265961869547).

---

### Product promo film from a project repo

<a href="https://x.com/ezshine/status/2103501705698750731"><img src="https://pbs.twimg.com/amplify_video_thumb/2103500152346644480/img/2dK3cXREOOzSSgVO.jpg" alt="Product promo film from a project repo" width="480"></a>

[@ezshine](https://x.com/ezshine) · 2026-09-25 · 🔖 27 · ▶ 3.9k · `One-shot`

A 65-second 16:9 MP4 that presents a project’s features like a professional product film, from one sentence given inside the project.

```text
设计个动画，介绍本项目的各项特性，像是专业的产品介绍宣传片，最后要生成 16:9 的mp4 视频
```

<details><summary>English translation</summary>

```text
Design an animation that introduces this project’s features, like a professional product promo film. At the end, generate a 16:9 mp4 video
```

</details>

<sub>Inputs: Brand kit · Author: about 30 minutes and roughly 15% of the 5-hour quota.</sub>

[Original post ↗](https://x.com/ezshine/status/2103501705698750731)

---

### Mac desktop teaser for a notch browser

<a href="https://x.com/jake11moran/status/2103237884564414633"><img src="https://pbs.twimg.com/amplify_video_thumb/2103237577138692096/img/H2c936Vj7VIhyhHx.jpg" alt="Mac desktop teaser for a notch browser" width="480"></a>

[@jake11moran](https://x.com/jake11moran) · 2026-09-24 · 🔖 25 · ▶ 6.7k · `Brief` · HyperFrames

A 27-second HyperFrames teaser: one continuous camera over a Mac desktop, recreated app windows, and a notch that opens into a browser.

```text
Using HyperFrames, make a hype teaser for the product in this post - [link]. Landscape, around 27 seconds. Match the product UI, wallpaper and copy from the post's video

Motion should feel slow and polished - one continuous camera over one Mac desktop, no hard cuts. Camera pushes, pulls and pans run like 1.5 to 3 seconds on gentle ease-in-out curves, nothing snappy - aim for half the speed you'd default to. Add motion blur on fast moves and a light film grain finish. Use an oversized macOS cursor. No audio. All on-screen copy lowercase like the post.

1. Open on a big centered line - "in the AI era, the hard part is" - entering word by word from the right with an orange colorama text wipe over it (the `colorama-wipe` registry component). Hold it about a second, then scale it down into place above a spinning list.
2. The list rotates through 30 hard things about working in the AI era - spending tokens wisely, picking the right model, managing context windows, etc - each with a real app icon. Go fast, it's not meant to be read, then land slowly on "managing your desktop". 0.2s after it lands a question mark pops on after it.
3. Pull the camera back to reveal the Mac desktop as windows pile in on top of each other, arriving from behind the camera - Claude, ChatGPT, Grok, Linear, Chrome, Spotify, Slack and Claude Code in a terminal. Build these as accurate recreations of the real apps with real icons.
4. Push back in so the windows fly past the camera, back to text - "don't make your browser / one of them".
5. Pan up to a really tight framing of just the notch and the top of the wallpaper. A cursor comes up and hovers - the notch morphs into a pill with the name "NotchBrowser", then opens into the browser panel exactly like in the video.
6. Click through the tabs like the video does, then click the collapse chevron so the panel retracts into the notch.
7. End on a checklist of the post's claims with rings and ticks drawing on
```

<details><summary>中文译文</summary>

```text
用 HyperFrames 为这条帖子里的产品做一支造势预告片 - [link]。横屏，约 27 秒。产品界面、壁纸和文案都要和帖子里的视频一致

运动要慢而精致 - 一个连续镜头在一台 Mac 桌面上移动，不要硬切。镜头的推、拉、摇每次持续约 1.5 到 3 秒，用柔和的 ease-in-out 曲线，一点都不要急促 - 目标是你默认速度的一半。快速运动时加动态模糊，最后加一层轻微的胶片颗粒。使用超大号的 macOS 光标。不要音频。所有屏幕文案都像帖子一样用小写。

1. 开场是一行居中的大字 - "in the AI era, the hard part is" - 从右侧逐词进入，上面叠一道橙色 colorama 文字擦除效果（即 `colorama-wipe` 注册组件）。停留约一秒，然后缩小归位，停在一个旋转列表的上方。
2. 列表轮播 AI 时代工作中的 30 件难事 - 明智地花 token、选对模型、管理上下文窗口等等 - 每一项都配一个真实的应用图标。转得要快，本来就不是给人读的，然后慢慢停在 "managing your desktop" 上。停住 0.2s 后，后面弹出一个问号。
3. 镜头拉远，露出 Mac 桌面，窗口从镜头后方飞来、一层层叠上去 - Claude、ChatGPT、Grok、Linear、Chrome、Spotify、Slack，以及终端里的 Claude Code。把它们做成对真实应用的精确还原，用真实图标。
4. 再推进去，让窗口从镜头旁飞过，回到文字 - "don't make your browser / one of them"。
5. 向上摇到一个非常紧的构图，只有刘海和壁纸顶部。一个光标移上来悬停 - 刘海变形成一个写着 "NotchBrowser" 的胶囊，然后展开成浏览器面板，和视频里一模一样。
6. 像视频里那样依次点击各个标签页，然后点击收起箭头，让面板缩回刘海。
7. 以帖子里各项卖点组成的清单收尾，圆圈和勾号逐个画出来
```

</details>

<sub>Inputs: Reference video · Author: a single prompt, dictated by voice.</sub>

<sub>Also rendered from this prompt by: [@jake11moran](https://x.com/jake11moran/status/2103239225902874874)</sub>

[Original post ↗](https://x.com/jake11moran/status/2103237884564414633) · Prompt posted in [this reply](https://x.com/jake11moran/status/2103239225902874874).

---

### Spotify-style music product film

<a href="https://x.com/brainextends/status/2103801834930606193"><img src="https://pbs.twimg.com/amplify_video_thumb/2103801393534652417/img/duzCcucyFHeAlkgx.jpg" alt="Spotify-style music product film" width="480"></a>

[@brainextends](https://x.com/brainextends) · 2026-09-26 · 🔖 21 · ▶ 2k · `Spec`

An 18-second 1080p60 Spotify-themed product film, one-shotted from a spec with a per-second timeline, a fictional album cover and seek(t) rendering rules.

```text
Create a complete, polished Spotify-themed motion graphics video from the following brief. This prompt is self-contained: no reference video or supplied assets are required.

<deliverables> An 18-second MP4 at 1920×1080 and true 60 fps, with music and subtle sound effects Complete editable source Build, render, inspect, and refine the animation before delivering it Do not stop at a storyboard, still images, or an implementation plan </deliverables>
<art_direction>
A premium music-product film presented inside a large, nearly black rounded rectangular stage
The stage occupies roughly 80% of the canvas width and 75% of its height, centered horizontally and slightly below the vertical center
Outside the stage, use a soft atmospheric green background: luminous emerald near the upper-left corner, deeper forest green toward the sides, fading to near-black at the bottom
Inside the stage:
Near-black background
White primary typography
Muted gray secondary text
Spotify green # 1ED760 for emphasis and controls
One clean sans-serif font, such as Geist or Inter
Consistent icon strokes and restrained shadows
Keep compositions compact and centered, with substantial negative space
Text should feel like music-product advertising, not oversized presentation headings
Do not add an outer caption, creator watermark, decorative footer, or progress counter
</art_direction>

<artwork> Create original square album artwork for a fictional track called “Glass Tides” by “AURA”
The hero cover is an abstract macro image of flowing pearlescent liquid silk and molten glass
Use pastel lavender, powder cyan, blush pink, champagne gold, and subtle mint
Include broad three-dimensional folds, realistic reflective highlights, delicate striations, and a prominent sweeping S-shaped fold
Fill the square edge to edge
No text, logo, or border on this hero artwork
Use this same artwork consistently throughout the film

Create additional designed playlist sleeves:
“Late Nights” in mustard yellow
“Good Energy” in pink
“Deep Focus” in blue
“Daily Mix 1”, “Daily Mix 2”, and “Daily Mix 3” in complementary colors

These should look like finished graphic-design covers, with bold typography and simple geometric motifs
</artwork>

<timeline> 0.0–0.6 seconds: A green Spotify icon grows smoothly into the center of the dark stage Give it a confident arrival with minimal overshoot
0.6–1.5 seconds:
The icon transitions into a small Spotify identity above two centered lines:
“Discover”
“new music”
The first line is white; the second is green
Reveal them with short masked vertical movements
1.5–2.4 seconds:
A stylized Spotify desktop interface rises into view
Show a slim sidebar, “Made for you”, three album cards, and small supporting rows
Use a subtle perspective tilt during the entrance, settling toward a frontal view
2.4–3.2 seconds:
Move closer to the three featured covers
Show “New for you” above them
Keep the artwork crisp, with short album titles beneath
A narrow rounded player bar now anchors the bottom of the stage
3.2–4.0 seconds:
The featured cards withdraw into a compact “Fresh finds” list
Reveal four song rows with a slight stagger
Each row contains a thumbnail, short track title, artist, and a small menu icon
4.0–4.9 seconds:
Transition into a horizontal strip of colorful playlist covers
Heading: “Every mood”
Supporting line: “Find what moves you”
The strip slides smoothly sideways, with edge cards partially cropped by the stage
4.9–5.8 seconds:
A compact search field appears
Type “Glass Tides”
Reveal one selected result beneath it, with the iridescent artwork, “AURA”, and a green play icon

5.8–6.6 seconds:
The selected artwork expands into a large centered cover
Reveal “Glass Tides” underneath, followed by “AURA” in green
Keep the player bar visible
6.6–7.5 seconds:
The same cover slides left
Track information appears on the right:
“Glass Tides”
“AURA”
“A new frequency”
Add a rounded green Play button
Coordinate the cover movement and text reveals
7.5–8.3 seconds:
A brief brand-color transformation fills the inner stage with green
The artwork contracts into a smaller centered tile
Place a small dark Spotify identity underneath
The player briefly recedes
8.3–9.8 seconds:
Return to the dark stage
The same artwork expands dramatically toward the camera, becoming oversized and cropped by the rounded stage
Restore the player at the bottom
Use controlled motion blur during the fastest part of the zoom

9.8–11.2 seconds:
The artwork clears into a centered typographic statement:
“Find your”
“rhythm”
Use white for the first line and green for the second
The player remains visible and stable beneath it
11.2–12.5 seconds:
Show “Made for your every day”
Three playlist sleeves enter with gentle perspective and small opposing tilts
They spread into six smaller sleeves across the stage
Supporting line: “Your sound, always evolving”

12.5–14.0 seconds:
The playlist layout transitions into four floating album covers
Include the iridescent hero artwork
Use restrained rotation, perspective, depth ordering, and overlap
Keep their movement coordinated rather than randomly floating
14.0–15.2 seconds:
The covers converge toward the center and fold around a green Spotify icon
The artwork withdraws as the icon becomes the focal point
Fade the player away
The Spotify icon must emerge from the same central position as the converging covers
15.2–18.0 seconds:
The icon moves slightly left and settles beside a large white “Spotify” wordmark
Keep the icon and letters separated throughout the movement
Reveal:
“Discover new music”
“every day”
The first line is white; the second is green
Hold the finished composition cleanly through the end
</timeline>
<persistent_player>
For most of the middle sequence, keep one narrow rounded player bar near the bottom of the inner stage
Include:
Small hero-art thumbnail
“Glass Tides” and “AURA”
Play and skip controls
A thin progress track
A small volume icon
Subdued dark translucent styling with a fine border
This recurring player connects the changing shots
It must remain visually secondary to the artwork
</persistent_player>

<motion_quality>
Match the energy of a tightly edited premium product film
Most visual ideas last approximately one second, but transitions remain smooth
Use continuous acceleration and deceleration
Favor critically damped springs or carefully tuned smooth easing
No repeated bouncing or large elastic overshoots
Preserve the hero artwork’s identity and position relationships through search, album detail, brand tile, and zoom
Use match-position transitions, coordinated scaling, masked reveals, and perspective
Outgoing titles must disappear before incoming titles occupy the same space
Avoid overlapping text, sudden camera resets, long blank intervals, and arbitrary full-frame crossfades
Clip every oversized cover and camera move cleanly to the rounded stage
No particles, shockwave rings, lens flares, camera shake, or unrelated stock footage
</motion_quality>

<audio> Create or select commercially usable electronic music around 120 BPM Use a clean pulse, warm bass, restrained melodic elements, and subtle transition accents Align important entrances, selections, zooms, and the logo reveal with musical events Keep effects quieter than the music No voiceover Do not use copyrighted commercial tracks without permission </audio>
<implementation_and_validation>
Build a deterministic animation driven by absolute time through an async window. seek(t) function
Every transform, opacity, mask, and UI state must be reproducible when seeking frames in any order
Do not depend on live timers, accumulated physics, or CSS transition state during export

Render true 60 fps with spatial antialiasing
Use 3–5 temporal subframe samples per output frame for restrained motion blur
Keep stationary text and artwork sharp
Inspect contact sheets and moving playback
Check the fast heading changes, artwork handoffs, zoom, cover convergence, and final wordmark spacing
Verify evenly spaced frame timestamps and the full 18-second duration
Fix visual defects before delivering the final MP4 and editable source
</implementation_and_validation>
```

<details><summary>中文译文</summary>

```text
根据下面的 brief，制作一支完整、精致的 Spotify 主题动态图形视频。这个提示词是自包含的：不需要参考视频，也不需要提供素材。

<deliverables> 一个 18 秒的 MP4，1920×1080，真 60 fps，带音乐和细微的音效 完整的可编辑源文件 交付前完成动画的构建、渲染、检查和打磨 不要停在故事板、静态图或实现方案上 </deliverables>
<art_direction>
一支高级感的音乐产品片，呈现在一个近乎全黑的大圆角矩形舞台里
舞台约占画布宽度的 80%、高度的 75%，水平居中，略低于垂直中心
舞台外用柔和、有氛围感的绿色背景：左上角是发光的祖母绿，两侧过渡到更深的森林绿，底部渐隐到近黑
舞台内：
近黑背景
白色主文字
柔和的灰色辅助文字
用 Spotify 绿 # 1ED760 做强调和控件
一种干净的无衬线字体，比如 Geist 或 Inter
图标描边统一，阴影克制
构图紧凑、居中，留大量负空间
文字要像音乐产品广告，而不是超大的演示文稿标题
不要添加外部说明文字、创作者水印、装饰性页脚或进度计数器
</art_direction>

<artwork> 为一首虚构曲目 “Glass Tides”（艺人 “AURA”）创作原创的方形专辑封面
主封面是一张抽象的微距图像：流动的珠光液态丝绸与熔融玻璃
用粉紫、粉青、腮红粉、香槟金和淡淡的薄荷色
包含宽大的立体褶皱、真实的反射高光、细腻的条纹，以及一道醒目的 S 形大褶
铺满整个方形，不留边
主封面上不要有文字、logo 或边框
全片始终使用同一张封面

另外设计几张歌单封套：
“Late Nights” 用芥末黄
“Good Energy” 用粉色
“Deep Focus” 用蓝色
“Daily Mix 1”、“Daily Mix 2” 和 “Daily Mix 3” 用互补色

这些要像完成度很高的平面设计封面，有粗体字和简单的几何图形
</artwork>

<timeline> 0.0–0.6 秒：一个绿色 Spotify 图标在深色舞台中央平滑长大 出场要果断，过冲极小
0.6–1.5 秒：
图标过渡为一个小的 Spotify 标识，下方是两行居中文字：
“Discover”
“new music”
第一行白色，第二行绿色
用短促的遮罩纵向运动揭示
1.5–2.4 秒：
一个风格化的 Spotify 桌面界面升入画面
显示细窄的侧边栏、“Made for you”、三张专辑卡片和几行小的辅助内容
入场时带轻微的透视倾斜，最后回正到正视角
2.4–3.2 秒：
推近到三张主推封面
上方显示 “New for you”
封面保持清晰，下方是简短的专辑名
此时一条窄的圆角播放条固定在舞台底部
3.2–4.0 秒：
主推卡片收拢成一个紧凑的 “Fresh finds” 列表
四行歌曲略微错开依次出现
每行包含缩略图、简短曲名、艺人和一个小菜单图标
4.0–4.9 秒：
过渡到一条横向排列的彩色歌单封面
标题：“Every mood”
辅助文字：“Find what moves you”
封面条平滑横向滑动，两端的卡片被舞台部分裁切
4.9–5.8 秒：
出现一个紧凑的搜索框
输入 “Glass Tides”
下方出现一个选中的结果，带珠光封面、“AURA” 和绿色播放图标

5.8–6.6 秒：
选中的封面放大成居中的大封面
下方显示 “Glass Tides”，接着是绿色的 “AURA”
播放条保持可见
6.6–7.5 秒：
同一张封面滑向左侧
右侧出现曲目信息：
“Glass Tides”
“AURA”
“A new frequency”
加一个圆角的绿色 Play 按钮
封面运动和文字揭示要协调
7.5–8.3 秒：
一次短暂的品牌色变换，用绿色铺满舞台内部
封面收缩成居中的小方块
下方放一个小的深色 Spotify 标识
播放条短暂退场
8.3–9.8 秒：
回到深色舞台
同一张封面朝镜头戏剧性地放大，大到被圆角舞台裁切
底部恢复播放条
在缩放最快的阶段使用受控的动态模糊

9.8–11.2 秒：
封面散开，变成居中的文字宣言：
“Find your”
“rhythm”
第一行白色，第二行绿色
播放条在下方保持可见、稳定
11.2–12.5 秒：
显示 “Made for your every day”
三张歌单封套带着柔和的透视和相反方向的小倾斜入场
它们展开成横跨舞台的六张小封套
辅助文字：“Your sound, always evolving”

12.5–14.0 秒：
歌单布局过渡为四张漂浮的专辑封面
其中包括珠光主封面
旋转、透视、前后层级和重叠都要克制
它们的运动要协调，而不是随机漂浮
14.0–15.2 秒：
封面向中心汇聚，围绕一个绿色 Spotify 图标收拢
封面退去，图标成为视觉焦点
播放条淡出
Spotify 图标必须从封面汇聚的同一中心位置出现
15.2–18.0 秒：
图标稍微左移，停在大号白色 “Spotify” 字标旁边
整个运动过程中图标和字母始终保持分开
揭示：
“Discover new music”
“every day”
第一行白色，第二行绿色
完成的构图干净地保持到结尾
</timeline>
<persistent_player>
中段的大部分时间里，在内部舞台底部附近保持一条窄的圆角播放条
包含：
主封面的小缩略图
“Glass Tides” 和 “AURA”
播放和跳过控件
一条细的进度条
一个小的音量图标
低调的深色半透明样式，带细边框
这条反复出现的播放条把不断变化的镜头串起来
它在视觉上必须从属于封面
</persistent_player>

<motion_quality>
达到剪辑紧凑的高端产品片的节奏感
大多数视觉想法持续约一秒，但转场保持顺滑
使用连续的加速和减速
优先用临界阻尼弹簧或仔细调过的平滑缓动
不要反复弹跳或大幅弹性过冲
在搜索、专辑详情、品牌方块和缩放之间，保持主封面的身份和位置关系
使用位置匹配转场、协调缩放、遮罩揭示和透视
旧标题必须先消失，新标题才能占据同一位置
避免文字重叠、镜头突然复位、长时间空白和随意的全屏交叉淡化
所有超大的封面和镜头运动都要干净地裁切在圆角舞台内
不要粒子、冲击波环、镜头光晕、镜头抖动或无关的库存素材
</motion_quality>

<audio> 创作或选用可商用的电子音乐，约 120 BPM 用干净的脉冲、温暖的贝斯、克制的旋律元素和细微的转场点缀 重要的入场、选择、缩放和 logo 揭示都要对齐音乐事件 音效要比音乐小声 不要旁白 未经许可不要使用有版权的商业曲目 </audio>
<implementation_and_validation>
构建一个由绝对时间驱动的确定性动画，通过异步的 window. seek(t) 函数控制
每个变换、透明度、遮罩和 UI 状态在以任意顺序 seek 帧时都必须可复现
导出时不要依赖实时计时器、累积的物理状态或 CSS transition 状态

以真 60 fps 渲染，开启空间抗锯齿
每个输出帧用 3–5 个时间子帧采样，做克制的动态模糊
静止的文字和封面保持锐利
检查联系表（contact sheet）和实际播放效果
检查快速的标题切换、封面交接、缩放、封面汇聚和最终字标的间距
确认帧时间戳均匀分布，总时长完整 18 秒
交付最终 MP4 和可编辑源文件之前，修好所有视觉缺陷
</implementation_and_validation>
```

</details>

<sub>Author: one-shotted.</sub>

[Original post ↗](https://x.com/brainextends/status/2103801834930606193)

---

### Logo turned into a 10-second brand sting

<a href="https://x.com/0xValure/status/2103603025579331584"><img src="https://pbs.twimg.com/amplify_video_thumb/2103601210154426368/img/lb_4iGplcPUtFbhZ.jpg" alt="Logo turned into a 10-second brand sting" width="480"></a>

[@0xValure](https://x.com/0xValure) · 2026-09-25 · 🔖 19 · ▶ 5.9k · `One-shot`

A 10-second brand sting from a PayBox logo and a reference; the agent read the logo, looked up the company and wrote the scenario itself.

```text
Make this PayBox logo into a reel. Pretend you are a world-class motion designer. Make a 10-second dynamic video like the reference
```

<details><summary>中文译文</summary>

```text
把这个 PayBox Logo 做成一段短片。假装你是世界级的动效设计师。参照参考视频，做一段 10 秒的动感视频
```

</details>

<sub>Inputs: Logo, Reference video · Author: done in one pass.</sub>

[Original post ↗](https://x.com/0xValure/status/2103603025579331584) · Prompt posted in [this reply](https://x.com/0xValure/status/2103603029224354245).

---

### Hype video for a club fox chase event

<a href="https://x.com/DaveRogenmoser/status/2103249424075899271"><img src="https://pbs.twimg.com/amplify_video_thumb/2103247261199147008/img/W6I07-so6PGcLJMx.jpg" alt="Hype video for a club fox chase event" width="480"></a>

[@DaveRogenmoser](https://x.com/DaveRogenmoser) · 2026-09-24 · 🔖 17 · ▶ 2.9k · `Brief` · Remotion

A 26-second all-code hype video with music for a club’s fox chase event; the prompt leaves the tool choice, such as Remotion, to Opus.

```text
Make a dope polished 30 second video for our Mackenzie Club fox chase event using whatever tools you think are best. tessaract, etc. it should be all code (that's what people on X are saying). Cool music. Hype video. Use Tessaract or Remotion or whatever you think is best. Make it amazing and interesting.
```

<details><summary>中文译文</summary>

```text
为我们 Mackenzie Club 的猎狐活动做一支超酷、精致的 30 秒视频，用你觉得最好的任何工具。tessaract 之类的。它应该全部用代码做（X 上的人都这么说）。酷一点的音乐。造势视频。用 Tessaract 或 Remotion，或者你觉得最好的任何工具。做得精彩又有意思。
```

</details>

<sub>Author: 1 prompt plus 2 small tweaks; about 9 minutes of his time and about 3 hours of agent work.</sub>

[Original post ↗](https://x.com/DaveRogenmoser/status/2103249424075899271)

---

### GitHub README hero video for an open-source skill

<a href="https://x.com/hqmank/status/2103831140033241156"><img src="https://pbs.twimg.com/amplify_video_thumb/2103830793105629184/img/NppYefNdZaT8GZxN.jpg" alt="GitHub README hero video for an open-source skill" width="480"></a>

[@hqmank](https://x.com/hqmank) · 2026-09-26 · 🔖 15 · ▶ 5k · `One-shot` · Remotion

A 23-second Remotion launch video for an open-source browser-agent skill, meant as the hero video at the top of its GitHub README.

```text
Make a dynamic 20-second motion graphics launch video for my open-source project jev-browser-skill ('Give a site. Write a goal. Jev clicks.'), like it's the hero video on its GitHub README. Go all out.
```

<details><summary>中文译文</summary>

```text
为我的开源项目 jev-browser-skill（'Give a site. Write a goal. Jev clicks.'）制作一段 20 秒的动态图形发布视频，就像它 GitHub README 里的主视频一样。拿出全部本事。
```

</details>

<sub>Inputs: Brand kit · Author (in a reply): about five minutes.</sub>

[Original post ↗](https://x.com/hqmank/status/2103831140033241156)

---

### Trading terminal launch animation

<a href="https://x.com/dale_vaz/status/2103290592679879074"><img src="https://pbs.twimg.com/amplify_video_thumb/2103290544978075648/img/SVMM1B952HzqpI61.jpg" alt="Trading terminal launch animation" width="480"></a>

[@dale_vaz](https://x.com/dale_vaz) · 2026-09-25 · 🔖 15 · ▶ 2.4k · `Brief`

A 47-second JavaScript launch animation that grows from a single dot into trading windows, zooms out to space and back into a phone screen.

```text
create a self contained aesthetically pleasing, breathtaking animation of the Sahi Trading Terminal. it should start with a single dot on a black screen and then have multiple windows show up on the screen such as Charts, Positons , Option Chain, Watchlist. And zoom into and out at multiple scales. Finally the camera zooms out to make the desktop look like a point in space. And then it zooms back in to reveal a mobile screen in landscape mode with a chart in one half and an option chain in another. The video ends in Sjngle Screen Trading on SAHI
use javascript for it. be detailed and accurate. it should be visually stunning
```

<details><summary>中文译文</summary>

```text
做一段自包含的、美观且令人惊叹的 Sahi Trading Terminal 动画。开头是黑屏上的一个点，然后屏幕上出现多个窗口，比如 Charts、Positons、Option Chain、Watchlist。在多个尺度上推近又拉远。最后镜头拉远，让桌面看起来像太空中的一个点。然后再推近，露出一块横屏的手机屏幕，一半是图表，另一半是期权链。视频以 SAHI 上的 Sjngle Screen Trading 结尾
用 javascript 来做。要细致、准确。视觉上要非常惊艳
```

</details>

<sub>Inputs: Brand kit · Author: made in a single shot.</sub>

[Original post ↗](https://x.com/dale_vaz/status/2103290592679879074)

---

### Fill-in product explainer template

<a href="https://x.com/sudo_kiran/status/2103761658745335993"><img src="https://pbs.twimg.com/amplify_video_thumb/2103761048969043968/img/YT4AXXDUDrlRSu0v.jpg" alt="Fill-in product explainer template" width="480"></a>

[@sudo_kiran](https://x.com/sudo_kiran) · 2026-09-26 · 🔖 14 · ▶ 2.3k · `Template`

A 30-second motion graphics product explainer template: swap in your product and link, and Opus writes the script, picks colors and adds music.

```text
create best motion graphics explainer of the (your product) with very good script and good design colors and good music make sure the video should be incredible and people should feels like watch it many times.. it has to be in 30 seconds good and very intresting, it has to be best of the best of the best of the best video
(product link)
```

<details><summary>中文译文</summary>

```text
为 (your product) 做一个最好的动态图形讲解视频，要有很好的脚本、好看的设计配色和好听的音乐，一定要让视频惊艳，让人觉得想看很多遍……必须控制在 30 秒，好看又非常有趣，必须是最好中的最好中的最好中的最好的视频
(product link)
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/sudo_kiran/status/2103761658745335993)

---

### Opus 5.5 ad inspired by Apple's 1984

<a href="https://x.com/1littlecoder/status/2103746736980378066"><img src="https://pbs.twimg.com/amplify_video_thumb/2103746474064683008/img/Hh__w6n4fEy2-50Q.jpg" alt="Opus 5.5 ad inspired by Apple&#x27;s 1984" width="480"></a>

[@1littlecoder](https://x.com/1littlecoder) · 2026-09-26 · 🔖 13 · ▶ 3.1k · `One-shot`

A 30-second code-rendered ad for Opus 5.5 that riffs on Apple's 1984 commercial; the author says it even checked its own sound levels.

```text
create a 30 second ad for Opus 5.5 inspired by Apple 1984 ad, iykyk! avoid the border text or frames!
```

<details><summary>中文译文</summary>

```text
为 Opus 5.5 做一支 30 秒广告，灵感来自苹果的《1984》广告，懂的都懂！不要边框文字或画框！
```

</details>

[Original post ↗](https://x.com/1littlecoder/status/2103746736980378066)

---

### 55-second brand film template with archival footage

<a href="https://x.com/notdwd/status/2103995183255998633"><img src="https://pbs.twimg.com/amplify_video_thumb/2103993352626774016/img/D3j7CunT4umR54dy.jpg" alt="55-second brand film template with archival footage" width="480"></a>

[@notdwd](https://x.com/notdwd) · 2026-09-26 · 🔖 11 · ▶ 1.2k · `Template` · Three.js · Playwright · ffmpeg · Python

A reusable 55-second brand film: archival footage on a CRT, a 3D embossed logo button, ElevenLabs narration and film grain, rendered frame by frame.

```text
<inputs>
Ask me for: a brand name, its logo (SVG or high-res PNG), one line of what it becomes in 5 years (not today's features), one coined word the film should teach (e.g. "signal"), a public-domain archival clip of the old way of doing it (http://archive.org Prelinger), an archived web page from ~2000 where people asked for things (Wayback Machine), a royalty-free song ~100-120 BPM with a real drop (Mixkit, free for commercial use), and a free ElevenLabs key for the narrator (premade voices only).
</inputs>

<direction>
An a16z x Content Rewards brand film, ~55s. It sells one feeling and one idea, never features. Real archival and real web pages, never stock footage, never product screens, never fake UI. One hero object: a 3D button with the logo embossed into it, the ONLY saturated colour in the film. Everything else white, silver, cream and archival black. Small white captions that light up word by word on the narrator's timestamps. Film texture: fresh grain every frame, halation on bright edges, soft vignette, warm lifted blacks. The brand appears at the end, never before.
Banned: stock footage, dashboards, chat UIs, feature tours, cards without real profile pictures, wobbly "worm" graph lines, random glitches, any hold longer than 1.5s, purple, rainbow gradients, orange on anything but the button.
</direction>

<structure>
Cold open (0-8s): the archival clip plays on a glowing old CRT TV with its real dialogue, captions word by word.
The past (8-17s): push into the real 2000 web page, a cursor lands on one real "wanted" post, old pages strobe one per frame, a counter ticks EVERY frame up to today's scale. Narrator: "People have always asked the internet for what they need." / "Today, there are five hundred million posts a day."
Bridge (17-30s): a galaxy of real old asks. One ask snaps to a white outline with a chip of the coined word ("We call that a signal."). Archival of people doing it by hand on the TV. Cut on each word: "Door by door. Call by call. Scroll by scroll." The narrator never stops talking between acts.
Button (30s): the button rises out of black, rim light first, colourless. "[Brand] finds the signals." A flat grey line: "this is how you find customers by hand". Hard cut to a button macro, the colour comes alive, the music drop lands on this exact frame. "and this... is with [Brand]": a steep lit curve, counters changing every frame, a glowing sine with a comet head the camera chases, then platform strikes (X, Reddit, LinkedIn, YouTube, Instagram, TikTok) each with its own counter, then the galaxy again with glowing platform logos: "Every signal on the internet." Hyperspace.
End: the tagline word by word, then "[Brand] is live.", ONE cream frame on the kick, then logo + URL in silence.
</structure>

<build>
1. One HTML file, 1920x1080. Everything is computed from time inside seek(t): no CSS transitions, no timers, no Math.random (seeded hash), no state between frames.
2. Button: three.js MeshPhysicalMaterial (clearcoat 1, roughness ~0.4), ACES filmic, cool + warm rim spots, room env map. Emboss the real logo by displacing a dense disc with a blurred mask of the logo, folded into the rim so corners don't show. Brushed-metal base.
3. Counters: linear on the film's global clock, so they keep running through cutaways. Tabular numerals, fixed unit label.
4. Captions: <=7 words, one idea per shot, hand-placed line breaks, one text layer on screen at a time. Grey to white over 0.2s on the word timestamps (ElevenLabs /with-timestamps).
5. Glitch = 1-2 frames, only on a real cut, always with a click. Readable things stay on screen >= 8 clean frames.
6. Render with Playwright per frame (Chromium with --use-angle=swiftshader so WebGL renders headless), finish in numpy: fresh grain per frame, halation, vignette ~0.65x at the corners, 1px chroma fringe with EDGE-CLAMPED shifts. Pipe PNGs into ffmpeg, h264, 24fps.
7. Mix: narrator 10-15dB over the music, duck -18dB while speaking, hits on the exact action frame, -14 LUFS.
</build>

<gotchas>
np.roll wraps pixels and draws coloured lines on the frame edges, so clamp instead. A 10-pattern grain bank loops visibly, generate fresh grain every frame. Measure text only after fonts load or the widths are wrong. Headless Chromium with --disable-gpu renders WebGL blank. Counters that step every 3 frames look fake. If the narrator goes quiet between acts the film feels broken, so write a bridge line for every act change.
</gotchas>

<start>
Ask me for the inputs, then show me the script with timings and 6 stills (cold open, past, bridge, button reveal, macro on the drop, end card) before you render the full film. After every render, send me one 2fps contact sheet and fix what I call trash.
</start>
```

<details><summary>中文译文</summary>

```text
<inputs>
向我索取：品牌名称、它的 logo（SVG 或高分辨率 PNG）、一句话说明它 5 年后会变成什么（不是今天的功能）、影片要教给观众的一个自造词（例如“signal”）、一段展示旧做法的公有领域档案影像（http://archive.org Prelinger）、一个约 2000 年人们在网上求助的存档网页（Wayback Machine）、一首约 100-120 BPM、有真正 drop 的免版税歌曲（Mixkit，可免费商用），以及一个用于旁白的免费 ElevenLabs key（只用预设声音）。
</inputs>

<direction>
一支 a16z x Content Rewards 风格的品牌片，约 55s。它只卖一种感觉和一个想法，绝不卖功能。用真实的档案影像和真实网页，绝不用素材库视频、绝不用产品界面、绝不用假 UI。只有一个主角物件：一个压印着 logo 的 3D 按钮，它是全片唯一的饱和色。其他一切都是白色、银色、奶油色和档案黑。小号白色字幕按旁白的时间戳逐词点亮。胶片质感：每帧都是新的颗粒、亮边有光晕（halation）、柔和暗角、偏暖且提亮的黑位。品牌只在结尾出现，之前绝不露面。
禁用：素材库视频、仪表盘、聊天界面、功能导览、没有真实头像的卡片、摇摆的“蠕虫”曲线、随机故障效果、任何超过 1.5s 的停留、紫色、彩虹渐变、按钮以外任何地方的橙色。
</direction>

<structure>
冷开场（0-8s）：档案影像在一台发光的老式 CRT 电视上播放，带原始对白，字幕逐词出现。
过去（8-17s）：推进到真实的 2000 年网页，光标落在一条真实的“求购”帖上，旧网页每帧闪过一页，一个计数器每一帧都在跳，一直涨到今天的量级。旁白：“People have always asked the internet for what they need.” / “Today, there are five hundred million posts a day.”
过渡（17-30s）：一片由真实旧求助帖组成的星系。其中一条吸附成白色轮廓，带一个写着自造词的标签（“We call that a signal.”）。电视上播放人们手工做这件事的档案影像。每个词一切：“Door by door. Call by call. Scroll by scroll.”幕与幕之间旁白从不停顿。
按钮（30s）：按钮从黑暗中升起，先亮轮廓光，无色。“[Brand] finds the signals.”一条平直的灰线：“this is how you find customers by hand”。硬切到按钮微距，颜色活过来，音乐的 drop 正好落在这一帧。“and this... is with [Brand]”：一条陡峭发光的曲线，计数器每帧变化，一条带彗星头的发光正弦波，镜头追着它跑，然后各平台依次重击登场（X、Reddit、LinkedIn、YouTube、Instagram、TikTok），各带自己的计数器，然后再次回到星系，带发光的平台 logo：“Every signal on the internet.”进入超空间。
结尾：标语逐词出现，然后是“[Brand] is live.”，踩着底鼓闪一帧奶油色，然后在静默中出现 logo + URL。
</structure>

<build>
1. 一个 HTML 文件，1920x1080。一切都在 seek(t) 里由时间计算：不用 CSS transition、不用定时器、不用 Math.random（用带种子的哈希）、帧与帧之间不保留状态。
2. 按钮：three.js MeshPhysicalMaterial（clearcoat 1，roughness ~0.4），ACES filmic，冷暖两盏轮廓聚光灯，室内环境贴图。用 logo 的模糊遮罩去置换一个高密度圆盘，把真实 logo 压印上去，并折进边缘，避免露出棱角。拉丝金属底座。
3. 计数器：按全片的全局时钟线性增长，这样切到别的镜头时也在继续跑。等宽数字，固定的单位标签。
4. 字幕：<=7 个词，每个镜头一个意思，手动断行，屏幕上同一时间只有一层文字。按单词时间戳在 0.2s 内由灰变白（ElevenLabs /with-timestamps）。
5. 故障效果 = 1-2 帧，只用在真实的剪切点上，而且总是配一声咔哒。可读的内容至少停留 >= 8 个干净帧。
6. 用 Playwright 逐帧渲染（Chromium 加 --use-angle=swiftshader，让 WebGL 能无头渲染），在 numpy 里做后期：每帧新颗粒、光晕、四角约 0.65x 的暗角、1px 色散边，位移要做边缘钳制（EDGE-CLAMPED）。把 PNG 管道输入 ffmpeg，h264，24fps。
7. 混音：旁白比音乐高 10-15dB，说话时音乐压低 -18dB，音效点正好落在动作帧上，-14 LUFS。
</build>

<gotchas>
np.roll 会让像素回绕，在画面边缘画出彩色线条，所以要用钳制。10 张循环使用的颗粒图库会被看出重复，每帧都要生成新颗粒。文字宽度要等字体加载完再测量，否则会错。无头 Chromium 加 --disable-gpu 时 WebGL 会渲染成空白。每 3 帧才跳一次的计数器看起来很假。如果旁白在幕与幕之间沉默，影片会显得断掉了，所以每次换幕都要写一句过渡台词。
</gotchas>

<start>
先向我索取输入素材，然后给我看带时间码的脚本和 6 张静帧（冷开场、过去、过渡、按钮揭晓、drop 上的微距、结尾卡），再渲染完整影片。每次渲染后，发给我一张 2fps 的联系表，我说哪里是垃圾就改哪里。
</start>
```

</details>

<sub>Inputs: Brand kit, Logo, Footage, Music</sub>

[Original post ↗](https://x.com/notdwd/status/2103995183255998633)

---

### Product launch video from Pen designs

<a href="https://x.com/sachaarbonel/status/2103614797501673648"><img src="https://pbs.twimg.com/amplify_video_thumb/2103611596027154432/img/kcqNtJQPL9YgNobq.jpg" alt="Product launch video from Pen designs" width="480"></a>

[@sachaarbonel](https://x.com/sachaarbonel) · 2026-09-25 · 🔖 9 · ▶ 2k · `One-shot` · GSAP

A product launch video built from the author's Pen.dev designs via MCP; the posted cut took one follow-up asking for real music and a slower pace.

```text
Create a professional product launch video with motion graphics. You have access to the designs in pen
```

<details><summary>中文译文</summary>

```text
做一支带动态图形的专业产品发布视频。你可以访问 pen 里的设计稿
```

</details>

<sub>Inputs: Brand kit · Author: two prompts for this cut; the follow-up asked for a royalty-free song and a slower, more professional result. A third attempt with &quot;Use GSAP&quot; came out better.</sub>

[Original post ↗](https://x.com/sachaarbonel/status/2103614797501673648)

---

### Sprites ad platform promo from its own UI

<a href="https://x.com/AnnaCher___/status/2103571096549433425"><img src="https://pbs.twimg.com/amplify_video_thumb/2103570995806375936/img/sleoZ_IcPyEwLMh-.jpg" alt="Sprites ad platform promo from its own UI" width="480"></a>

[@AnnaCher___](https://x.com/AnnaCher___) · 2026-09-25 · 🔖 9 · ▶ 1.2k · `Spec` · Playwright · ffmpeg · Python

A looping product promo where one UI element morphs through the Sprites ad workflow on a 120 BPM grid, with UI sounds synthesized in numpy.

```text
Analyze http://sprites.ai and build a product promo from our own UI, not generic components.

<direction>
Dribbble-level UI motion. One shape, never cut: every state is the same element morphing its size, radius and color while its content swaps with a short blur. A cursor drives every change with real clicks and drags. Warm-gray canvas, black and white components, one accent (#FD9543), Geist. Springs everywhere, a tiny overshoot at most. The camera zooms so each state fills the frame. Last frame = first frame, so it loops.
Banned: bouncy easing, particles, glows, gradients on UI chrome, mismatched icon strokes, dead time, anything that looks like a template.
</direction>

<structure>
120 BPM, 7 bars, something on every beat.
Connect ad account (Meta, Google, LinkedIn, TikTok, Reddit logos) → loader → check → prompt bar types "Launch ads that convert" → island "Researching 42 competitors" → Ads Library wall of real ads scrolls and lands on a top performer → approval card → Approve & launch → budget slider that stretches past max → Autopilot toggle → knob becomes a liquid tab indicator across channels → ROAS chart draws itself with hover tooltip → ⌘K → type "pause" → toast "Paused 3 losing ads" → back to the button.
</structure>

<build>
1. One HTML file, 1440x1440. Every style is computed inside seek(t): no CSS transitions, no timers, no state between frames.
2. Springs are closed-form step responses. A value that changes target many times is a sum of springs, so it stays a pure function of time.
3. Tab indicator and toggle knob: the two edges ride different springs, so the leading edge stretches ahead.
4. Drags are direct manipulation: while held, the value follows the cursor. On release it springs back from wherever it was.
5. No music. Synthesize UI sounds with numpy and place each one by its measured peak on the beat grid.
6. Render with Playwright: 4 subframes per frame, blended with ffmpeg tmix for motion blur at 60fps.
7. Render one frame per beat first. Fix anything off-grid, cramped or hard to read.
</build>

<gotchas>
No will-change on anything the camera scales. Swapped text needs its own enter/exit timing. Match the last frame to the first, cursor position and speed included, or the loop stutters.
</gotchas>

Show me the state list on the beat grid before writing any code.
```

<details><summary>中文译文</summary>

```text
分析 http://sprites.ai，用我们自己的 UI 做一支产品宣传片，不要用通用组件。

<direction>
Dribbble 级别的 UI 动效。一个形状，从不切镜：每个状态都是同一个元素在变换尺寸、圆角和颜色，内容切换时带一次短暂模糊。每次变化都由光标通过真实的点击和拖拽驱动。暖灰画布，黑白组件，一个强调色（#FD9543），Geist 字体。处处用弹簧，最多一点点过冲。镜头缩放，让每个状态占满画面。最后一帧 = 第一帧，以便循环。
禁用：弹跳缓动、粒子、辉光、UI 外框上的渐变、图标描边不统一、空白时间，以及任何看起来像模板的东西。
</direction>

<structure>
120 BPM，7 小节，每一拍都有动作。
连接广告账户（Meta、Google、LinkedIn、TikTok、Reddit 的 logo）→ 加载器 → 对勾 → 提示栏打出“Launch ads that convert” → 灵动岛显示“Researching 42 competitors” → 由真实广告组成的 Ads Library 广告墙滚动并停在一条表现最好的广告上 → 审批卡片 → Approve & launch → 预算滑块被拖过最大值时被拉伸 → Autopilot 开关 → 开关圆钮变成横跨各渠道的液态标签指示器 → ROAS 图表自己画出来并带悬停提示 → ⌘K → 输入“pause” → toast 提示“Paused 3 losing ads” → 回到按钮。
</structure>

<build>
1. 一个 HTML 文件，1440x1440。每个样式都在 seek(t) 里计算：不用 CSS transition，不用定时器，帧与帧之间不保留状态。
2. 弹簧用闭式阶跃响应。一个多次改变目标的值是多个弹簧的叠加，所以它仍然是时间的纯函数。
3. 标签指示器和开关圆钮：两条边各跟随不同的弹簧，让前沿先拉伸出去。
4. 拖拽是直接操控：按住时数值跟随光标。松开后从当前位置弹回。
5. 不要音乐。用 numpy 合成 UI 音效，按每个音效测得的峰值把它放到节拍网格上。
6. 用 Playwright 渲染：每帧 4 个子帧，用 ffmpeg tmix 混合出 60fps 的运动模糊。
7. 先每拍渲染一帧。修掉任何不在网格上、拥挤或难以阅读的地方。
</build>

<gotchas>
镜头会缩放的元素一律不要加 will-change。切换的文字需要自己独立的进出场时机。最后一帧要和第一帧一致，包括光标位置和速度，否则循环会卡顿。
</gotchas>

写任何代码之前，先把状态列表排在节拍网格上给我看。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/AnnaCher___/status/2103571096549433425) · Prompt posted in [this reply](https://x.com/AnnaCher___/status/2103571098638152174).

---

### Menstrual calendar app promo from local assets

<a href="https://x.com/andre_lucaxxs/status/2103292636945846347"><img src="https://pbs.twimg.com/amplify_video_thumb/2103292188750721024/img/jJynREvVBvcgCKjg.jpg" alt="Menstrual calendar app promo from local assets" width="480"></a>

[@andre_lucaxxs](https://x.com/andre_lucaxxs) · 2026-09-25 · 🔖 9 · ▶ 1k · `One-shot` · Playwright · ffmpeg

A promo for the Flora menstrual calendar app, built only with JavaScript, Playwright and FFmpeg from a folder of the app's videos and screenshots.

```text
Dentro da pasta do flora tem uma outra pasta chamada "ads" com videos e prints do Flora(Caso queira usar como referencia).

Use apenas: JavaScript, Playwright e FFmpeg. Faça um vídeo moderno, elegante e impactante para meu produto.

https://apps.apple.com/pt/app/flora-calend%C3%A1rio-menstrual/id6789702093
```

<details><summary>English translation</summary>

```text
Inside the flora folder there's another folder called "ads" with videos and screenshots of Flora (in case you want to use them as reference).

Use only: JavaScript, Playwright and FFmpeg. Make a modern, elegant and impactful video for my product.

https://apps.apple.com/pt/app/flora-calend%C3%A1rio-menstrual/id6789702093
```

</details>

<sub>Inputs: Footage, Screenshots</sub>

[Original post ↗](https://x.com/andre_lucaxxs/status/2103292636945846347) · Prompt posted in [this reply](https://x.com/andre_lucaxxs/status/2103292640645329213).

---

### Supademo launch video on the beat

<a href="https://x.com/jhylee95/status/2103604431627452427"><img src="https://pbs.twimg.com/amplify_video_thumb/2103604391110463488/img/osxkfCSj7y1XnXjU.jpg" alt="Supademo launch video on the beat" width="480"></a>

[@jhylee95](https://x.com/jhylee95) · 2026-09-25 · 🔖 8 · ▶ 519 · `Brief`

A 24-second launch video for Supademo with brand-accurate UI and every cut timed to the music, made on Opus 5.5 at max effort.

```text
You're a world-class motion designer building a Supademo launch video. Research and land our core value and narrative. Scenes should be dynamic and confident: hook in the first second, then distinct beats for product proof and AI. Brand-accurate UI, type, color, and motion. Score the music so every cut, animation hit, and scene change lands on a beat or drop; retimed until synced. Social energy, quick cuts
```

<details><summary>中文译文</summary>

```text
你是一位世界级动效设计师，正在制作 Supademo 的发布视频。调研并抓准我们的核心价值和叙事。场景要有活力、自信：第一秒就抓住人，然后用清晰分开的段落展示产品实证和 AI。UI、字体、配色和动效都要符合品牌。给音乐配好节奏，让每一次剪切、动画重音和场景切换都落在节拍或 drop 上；反复调整时间直到同步。社交媒体的能量感，快切
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/jhylee95/status/2103604431627452427)

---

### DreamFort motion graphics manifesto

<a href="https://x.com/advait_jayant/status/2103565104243712107"><img src="https://pbs.twimg.com/amplify_video_thumb/2103564346336890880/img/qVMJAK_fBnWZYBGu.jpg" alt="DreamFort motion graphics manifesto" width="480"></a>

[@advait_jayant](https://x.com/advait_jayant) · 2026-09-25 · 🔖 7 · ▶ 882 · `One-shot` · HyperFrames

A 20-second brand manifesto for DreamFort built with HyperFrames, where every frame and sound is written in code with no image or video models.

```text
make a 20-second motion graphics manifesto for DreamFort: "superintelligence should belong to everyone". every frame and every sound written in code, no image or video models.
```

<details><summary>中文译文</summary>

```text
为 DreamFort 做一支 20 秒的动态图形宣言片：“superintelligence should belong to everyone”。每一帧、每一个声音都用代码写出来，不用任何图像或视频模型。
```

</details>

[Original post ↗](https://x.com/advait_jayant/status/2103565104243712107) · Prompt posted in [this reply](https://x.com/advait_jayant/status/2103565106504237084).

---

### LINUX DO community promo film

<a href="https://linux.do/t/topic/2953805"><img src="https://i0.hdslb.com/bfs/archive/06cb0833a832cd2ece7fcd0fcc8639caa27e42cc.jpg" alt="LINUX DO community promo film" width="480"></a>

@czm (LINUX DO) · 2026-09-26 · 🔖 5 · ▶ 1.5k · `One-shot`

A 73-second promo for the LINUX DO forum with its own sound effects and music; Opus picked every tool itself and asked no questions.

```text
帮我做一个Linuxdo的宣传片，包括音效和音乐；你可以使用任何你觉得合适的工具和技术，做出最好最惊艳的效果，不用问我任何问题，直接出成品
```

<details><summary>English translation</summary>

```text
Make me a promo film for Linuxdo, including sound effects and music. You can use any tools and techniques you think fit to get the best, most stunning result. Don't ask me any questions; just deliver the finished piece.
```

</details>

<sub>Author: about 8M tokens including cache hits, and roughly an hour.</sub>

[Original post ↗](https://linux.do/t/topic/2953805) · [Watch the video ↗](https://www.bilibili.com/video/BV1AQhX6TEjZ)

---

### Alan AI brand motion graphic

<a href="https://x.com/prasad_pilla/status/2103728953785496049"><img src="https://pbs.twimg.com/amplify_video_thumb/2103727928219664384/img/i8FNJz3YQ_06sEEo.jpg" alt="Alan AI brand motion graphic" width="480"></a>

[@prasad_pilla](https://x.com/prasad_pilla) · 2026-09-26 · 🔖 5 · ▶ 2.6k · `One-shot`

The showreel prompt pointed at a brand: a 15-second 1080p 60fps promo for Alan AI, with palette, fonts and logo pulled from its website.

```text
make a dynamic 15 second motion graphics video that shows what an incredible motion designer you are, for @tryAlanAI. go all out.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，为 @tryAlanAI 而做。拿出全部本事。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/prasad_pilla/status/2103728953785496049)

---

### Bold Video SaaS launch film

<a href="https://x.com/marcelfahle/status/2104084126068249018"><img src="https://pbs.twimg.com/amplify_video_thumb/2104079768400388096/img/nuN6Dvs2ibgcBZuW.jpg" alt="Bold Video SaaS launch film" width="480"></a>

[@marcelfahle](https://x.com/marcelfahle) · 2026-09-27 · 🔖 5 · ▶ 550 · `Brief` · Suno · Runway

A SaaS launch video for Bold Video built on the showreel prompt, with 10 brand posters and a Claude Design artboard attached; Suno and Runway also helped.

```text
Make a dynamic 20-second motion graphics video that shows what an incredible
motion designer you are, like it's your showreel for a résumé. Go all out.

It should be a SaaS launch video for Bold Video, working hand in hand with the new landing page copy on http://boldvideo.com. Show the flexibility of the chat and the implementations across our customers' frontends (they live in tenant branches of our starter).

It's important that Bold truly knows and understands the content, cites correctly, doesn't fucking hallucinate, is flexible, and knows who's asking.

I also want to highlight that it's headless: you can make it truly yours. On brand, on everything.
```

<details><summary>中文译文</summary>

```text
制作一段 20 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。

它应该是 Bold Video 的 SaaS 发布视频，和 http://boldvideo.com 上新落地页的文案紧密配合。展示聊天功能的灵活性，以及它在我们各个客户前端里的实现（它们在我们 starter 的租户分支里）。

重要的是要体现 Bold 真正了解并理解内容、引用准确、他妈的绝不胡编乱造、足够灵活，并且知道提问的人是谁。

我还想强调它是 headless 的：你可以让它完全属于你。贴合品牌，方方面面都贴合。
```

</details>

<sub>Inputs: Brand kit, Images</sub>

[Original post ↗](https://x.com/marcelfahle/status/2104084126068249018)

---

### GravityDEX x Gojo Satoru hype edit

<a href="https://x.com/MicheleHarmonic/status/2103111448352244175"><img src="https://pbs.twimg.com/amplify_video_thumb/2103111407008952321/img/ZIEOnxzvRARwdySp.jpg" alt="GravityDEX x Gojo Satoru hype edit" width="480"></a>

[@MicheleHarmonic](https://x.com/MicheleHarmonic) · 2026-09-24 · 🔖 4 · ▶ 1.9k · `One-shot`

A 38-second hype edit that pairs the GravityDEX brand with the anime character Gojo Satoru, from a single one-line prompt.

```text
Make a GravityDEX x Gojo Satoru edit that goes hard
```

<details><summary>中文译文</summary>

```text
做一个够带劲的 GravityDEX x 五条悟剪辑
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/MicheleHarmonic/status/2103111448352244175)

---

### TanStack AI launch film in Remotion

<a href="https://x.com/HowDevelop/status/2103840883812733090"><img src="https://pbs.twimg.com/amplify_video_thumb/2103840297352343552/img/Kj0kNOm6nI-7e3mP.jpg" alt="TanStack AI launch film in Remotion" width="480"></a>

[@HowDevelop](https://x.com/HowDevelop) · 2026-09-26 · 🔖 4 · ▶ 1.8k · `Spec` · Remotion

A TanStack AI launch film rendered with Remotion from a second-by-second 15-second spec with on-screen copy, sound design and accuracy guardrails.

```text
Create and render a 15-second motion graphics video introducing TanStack AI. Make it feel like a premium
developer-tool launch film produced by Studio1: fast, precise, visually surprising, and polished enough to open a
keynote or lead a social campaign.

Use the TanStack AI feature details below as the source of truth. Studio1 is presenting the film; do not imply
Studio1 built TanStack AI.

Format and deliverables
- 1920×1080, 30 fps, exactly 15 seconds; keep important content within a 9:16-safe central area.
- Deliver the rendered MP4 and the editable project/source. Use Remotion or another code-based motion graphics
workflow if available.
- Use real, editable typography and vector-style graphics. Do not rely on AI-generated text inside images.
- Add an original electronic sound design: a restrained opening pulse, tightly synchronized transition hits, rising
- Add an original electronic sound design: a restrained opening pulse, tightly synchronized transition hits, rising
momentum, and a satisfying final resolve. The story must also work muted.

Visual direction
Dark graphite canvas; luminous gradients and controlled flashes inspired by TanStack’s identity. Crisp typography,
kinetic code, layered interface fragments, streaming data, branching paths, and smooth camera moves with convincing
depth. High contrast and immaculate spacing. Every transition should visually demonstrate a feature, rather than
simply replace one title card with another. Keep all on-screen wording brief and legible. Avoid generic stock
footage, spinning logos, fake dashboards, excessive glitch effects, and tiny code nobody can read.

Exact 15-second sequence
- 0:00–0:02 — Hook: A single prompt cursor blinks. It sends one signal that expands into a network of
possibilities. On-screen: “What can one AI API become?”
- 0:02–0:04 — Core and providers: The signal resolves into chat(); provider nodes connect and swap rapidly without
breaking the central flow. On-screen: “chat() · 24 providers”
- 0:04–0:06.5 — Multimodal: One continuous stream transforms into text, waveform, image frame, and video timeline.
On-screen: “One pattern. Every modality.”
- 0:06.5–0:09 — Agents and tools: The stream branches into sandboxed agent runs, then reaches external tools
through MCP. Show distinct runs progressing in parallel. On-screen: “Agents · Sandboxes · MCP”
- 0:09–0:11.5 — Reliability: An interrupted stream freezes, reconnects, and resumes from the same point; a clean
type-check confirmation snaps into place. On-screen: “Persistent. Durable. Type-safe.”
- 0:11.5–0:15 — Reveal: All paths converge into a bold final composition: “TanStack AI” followed by “Build what’s
next.” Add a small “A Studio1 film” credit, visually subordinate to TanStack AI. Hold the final frame long enough
to read it.

Accuracy guardrails
The supplied article says TanStack AI is in the release candidate phase, supports 24 providers, uses AG-UI, and
offers composable chat(), media generation, sandbox and agent-harness primitives, MCP, type safety, persistence,
and resumable streams. Do not call it a stable v1 release. Do not present planned orchestration features as already
shipped.

Make the video, inspect the rendered result, and fix any clipped text, weak transitions, mistimed beats, or
unreadable frames before delivering it. The goal is a memorable showreel, not a slideshow of feature bullets.
```

<details><summary>中文译文</summary>

```text
创建并渲染一段 15 秒的动态图形视频，介绍 TanStack AI。让它像 Studio1 出品的高端开发者工具发布片：快、精准、视觉上有惊喜，精致到足以给主题演讲开场，或者撑起一场社交媒体宣传。

以下面的 TanStack AI 功能细节为准。影片由 Studio1 呈现；不要暗示 TanStack AI 是 Studio1 开发的。

格式与交付物
- 1920×1080，30 fps，正好 15 秒；重要内容放在 9:16 安全的中央区域内。
- 交付渲染好的 MP4 和可编辑的项目/源码。如果可用，使用 Remotion 或其他基于代码的动态图形工作流。
- 使用真实、可编辑的文字排版和矢量风格图形。不要依赖图片里 AI 生成的文字。
- 加入原创的电子音效设计：克制的开场脉冲、与转场严丝合缝的重音、不断攀升的推进感，以及令人满足的最终收束。静音时故事也要成立。

视觉方向
深石墨色画布；受 TanStack 品牌识别启发的发光渐变和受控的闪光。利落的字体、动态代码、层叠的界面碎片、流动的数据、分叉的路径，以及有真实纵深感的顺滑运镜。高对比度，间距无可挑剔。每个转场都要直观演示一个功能，而不是简单地把一张标题卡换成另一张。屏幕上的文字都要简短易读。避免通用素材库画面、旋转的 logo、假仪表盘、过度的故障效果，以及没人看得清的小号代码。

精确的 15 秒分镜
- 0:00–0:02 — 钩子：一个提示词光标在闪烁。它发出一道信号，扩展成一张充满可能性的网络。屏幕文字：“What can one AI API become?”
- 0:02–0:04 — 核心与提供商：信号收束成 chat()；提供商节点快速连接、切换，中央的流程不中断。屏幕文字：“chat() · 24 providers”
- 0:04–0:06.5 — 多模态：一条连续的流依次变成文本、波形、图像帧和视频时间线。屏幕文字：“One pattern. Every modality.”
- 0:06.5–0:09 — 智能体与工具：流分叉成多个沙箱里的智能体运行，再通过 MCP 连到外部工具。展示多个不同的运行并行推进。屏幕文字：“Agents · Sandboxes · MCP”
- 0:09–0:11.5 — 可靠性：一条被中断的流冻结、重连，并从同一位置继续；一个干净的类型检查通过提示卡入到位。屏幕文字：“Persistent. Durable. Type-safe.”
- 0:11.5–0:15 — 揭晓：所有路径汇聚成一个醒目的最终画面：“TanStack AI”，接着是“Build what’s next.”。加一个小小的“A Studio1 film”署名，视觉上从属于 TanStack AI。最后一帧停留足够久，让人看清。

准确性护栏
所提供的文章说，TanStack AI 处于 release candidate 阶段，支持 24 个提供商，使用 AG-UI，提供可组合的 chat()、媒体生成、沙箱和 agent-harness 原语、MCP、类型安全、持久化和可恢复的流。不要称它为稳定的 v1 版本。不要把计划中的编排功能说成已经发布。

制作视频，检查渲染结果，交付前修掉所有被裁切的文字、无力的转场、没卡准的节拍或看不清的画面。目标是一部让人记住的作品集短片，而不是一页页功能要点的幻灯片。
```

</details>

<sub>Inputs: Script</sub>

[Original post ↗](https://x.com/HowDevelop/status/2103840883812733090) · Prompt posted in [this reply](https://x.com/HowDevelop/status/2103840887562281145).

---

### Flexprice motion graphic from model knowledge

<a href="https://x.com/sudeepsd_/status/2103776623548158453"><img src="https://pbs.twimg.com/amplify_video_thumb/2103776344383606784/img/aSDlm_RceioVwdTW.jpg" alt="Flexprice motion graphic from model knowledge" width="480"></a>

[@sudeepsd_](https://x.com/sudeepsd_) · 2026-09-26 · 🔖 4 · ▶ 602 · `One-shot`

A 15-second motion graphics piece about Flexprice built only from what the model already knows about the company, using the showreel prompt.

```text
make a dynamic 15-second motion graphics video of what you know about @tryflexprice that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

<details><summary>中文译文</summary>

```text
用你对 @tryflexprice 的了解，制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/sudeepsd_/status/2103776623548158453)

---

### Alchemy brand motion graphic

<a href="https://x.com/onewaysidewalks/status/2103500011581440008"><img src="https://pbs.twimg.com/amplify_video_thumb/2103498150929399809/img/G_duPXBtR_UoPdDx.jpg" alt="Alchemy brand motion graphic" width="480"></a>

[@onewaysidewalks](https://x.com/onewaysidewalks) · 2026-09-25 · 🔖 4 · ▶ 3k · `One-shot`

The showreel prompt aimed at a company: a 15-second motion graphic for the infrastructure company Alchemy, run in an empty Claude Code directory.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for the infra company https://alchemy.com, go all out!
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像你给基础设施公司 https://alchemy.com 做的作品集一样，拿出全部本事！
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/onewaysidewalks/status/2103500011581440008) · Prompt posted in [this reply](https://x.com/onewaysidewalks/status/2103500013879881863).

---

### HyperFrames launch video template

<a href="https://x.com/noahxops/status/2103538922194366945"><img src="https://pbs.twimg.com/amplify_video_thumb/2103534383777116161/img/Yw9HZgAHWYz_pF8P.jpg" alt="HyperFrames launch video template" width="480"></a>

[@noahxops](https://x.com/noahxops) · 2026-09-25 · 🔖 4 · ▶ 321 · `Template` · HyperFrames

A fill-in-your-brand launch video template: Opus researches the website, builds a HyperFrames Studio project, then reviews its own pacing for social media.

```text
Create a launch video for (ur brand) using HyperFrames. Research (ur website) yourself and identify its unique value proposition, then communicate that proposition accurately. Make the video exciting, engaging, modern, and worthy of a contemporary product launch. Its UI, colors, typography, branding, design language, and motion language should feel unmistakably Cosmos. Choose the concept, story, copy, pacing, imagery, and animation yourself. Build a complete, playable HyperFrames Studio project in this folder, review it at normal speed, and give me the Studio link.
want you to examine your result visually. I want you to examine the rhythm of it, the speed of it, everything, and look for ways to improve it. Remember that the goal is to make it exciting, more energetic, and more fit for social media, meaning probably quicker cuts and just more subtle detail and more subtle polish across the board.
```

<details><summary>中文译文</summary>

```text
用 HyperFrames 为（你的品牌）制作一支发布视频。自己去研究（你的网站），找出它独特的价值主张，然后准确地传达出来。让视频令人兴奋、抓人、现代，配得上一场当代的产品发布。它的 UI、配色、字体、品牌、设计语言和动效语言都要一眼就是 Cosmos 的感觉。概念、故事、文案、节奏、画面和动画都由你自己决定。在这个文件夹里搭建一个完整、可播放的 HyperFrames Studio 项目，以正常速度回看一遍，然后把 Studio 链接给我。
我想让你从视觉上检查你的成果。检查它的节奏、速度，所有方面，找找可以改进的地方。记住，目标是让它更令人兴奋、更有活力、更适合社交媒体，也就是说大概需要更快的剪辑，以及整体上更多细腻的细节和更细致的打磨。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/noahxops/status/2103538922194366945)

---

### Quick Elements ad with sound design

<a href="https://x.com/deweytn/status/2102787822855893072"><img src="https://pbs.twimg.com/amplify_video_thumb/2102787443384586240/img/xj7FFz5iC0cWvJk5.jpg" alt="Quick Elements ad with sound design" width="480"></a>

[@deweytn](https://x.com/deweytn) · 2026-09-23 · 🔖 4 · ▶ 456 · `One-shot`

A 25-second ad for Quick Elements with its own sound design, made from one prompt in Claude Code running inside VidTL.

```text
Make me an Ad for Quick Elements. Go ALL OUT. design me something will blow the socks off anyone watching it.
```

<details><summary>中文译文</summary>

```text
给我做一个 Quick Elements 的广告。拿出全部本事。给我设计点能让所有观众惊掉下巴的东西。
```

</details>

<sub>Inputs: Brand kit · Author: it worked for 1.5 hours.</sub>

[Original post ↗](https://x.com/deweytn/status/2102787822855893072)

---

### Studio1 intro reel from a case study

<a href="https://x.com/Astrodevil_/status/2103600734017392708"><img src="https://pbs.twimg.com/amplify_video_thumb/2103600362443919360/img/MHqiwMpd-B9dO0ZX.jpg" alt="Studio1 intro reel from a case study" width="480"></a>

[@Astrodevil_](https://x.com/Astrodevil_) · 2026-09-25 · 🔖 4 · ▶ 446 · `One-shot`

The showreel prompt adapted to an agency: a 15-second intro launch reel for Studio1, with the facts taken from a single case-study link.

```text
make a dynamic 15-second motion graphics video that shows what an incredible work Studio1 is doing, you will get relevant info from case study, create like it's a good showreel for a Studio1 intro launch. go all out.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示 Studio1 做的工作有多出色，相关信息你可以从案例研究里获取，把它做成一部适合 Studio1 介绍发布的优秀作品集。拿出全部本事。
```

</details>

<sub>Inputs: Brand kit · Author: 11 minutes.</sub>

[Original post ↗](https://x.com/Astrodevil_/status/2103600734017392708)

---

### Flowdrive showreel-style promo

<a href="https://x.com/manuelogomigo/status/2103614667038052364"><img src="https://pbs.twimg.com/amplify_video_thumb/2103614067701092352/img/qYn1FlLlLjBYjwMC.jpg" alt="Flowdrive showreel-style promo" width="480"></a>

[@manuelogomigo](https://x.com/manuelogomigo) · 2026-09-25 · 🔖 4 · ▶ 632 · `One-shot`

A 15-second motion graphic with sound, from the showreel prompt with the résumé swapped for Flowdrive.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a flowdrive. go all out.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像你给 flowdrive 做的作品集一样。拿出全部本事。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/manuelogomigo/status/2103614667038052364)

---

### Tennis game launch video

<a href="https://x.com/deifosv/status/2103197522382786581"><img src="https://pbs.twimg.com/amplify_video_thumb/2103197333865316352/img/aArwzztySLkELnOT.jpg" alt="Tennis game launch video" width="480"></a>

[@deifosv](https://x.com/deifosv) · 2026-09-24 · 🔖 3 · ▶ 485 · `One-shot` · Remotion

A 30-second high-energy launch video for the browser game toptennisgame, showing live site stats, devices and themes; Opus installed Remotion on its own.

```text
Create a high energy launch video, showing live stats from the website, show that users can play on desktop and mobile and multiple themes, if need, give me a prompt to generate the song using Suno
```

<details><summary>中文译文</summary>

```text
做一个高能量的发布视频，展示网站上的实时数据，展示用户可以在桌面端和移动端玩、还有多种主题，如果需要的话，给我一个用 Suno 生成歌曲的提示词
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/deifosv/status/2103197522382786581)

---

### Product demo video with a /brag skill

<a href="https://x.com/VisheshBaghell/status/2103772327146119508"><img src="https://pbs.twimg.com/amplify_video_thumb/2103772214030159872/img/rlcTb1Zmnk9oc24H.jpg" alt="Product demo video with a /brag skill" width="480"></a>

[@VisheshBaghell](https://x.com/VisheshBaghell) · 2026-09-26 · 🔖 3 · ▶ 1.7k · `One-shot`

An 81-second product demo for the author's invoice-checking app, made with a /brag skill that the post does not share.

```text
build me a product demo for my site using /brag skill. make sure to emphasize on all features
```

<details><summary>中文译文</summary>

```text
用 /brag skill 给我的网站做一个产品演示，一定要突出所有功能
```

</details>

<sub>Inputs: Brand kit · Author: within an hour.</sub>

[Original post ↗](https://x.com/VisheshBaghell/status/2103772327146119508)

---

### Presentify app launch video

<a href="https://x.com/rampatra_/status/2104134969622728835"><img src="https://pbs.twimg.com/amplify_video_thumb/2104133217162792960/img/nIXOTsovZ76J8SUo.jpg" alt="Presentify app launch video" width="480"></a>

[@rampatra_](https://x.com/rampatra_) · 2026-09-27 · 🔖 3 · ▶ 621 · `One-shot`

A 27-second launch video for an app, from the showreel prompt plus its site, App Store link and a few screenshots; Opus also added the audio.

```text
Make a dynamic 15-30 second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.

It should be a launch video for http://presentifyapp.com, app store link - https://apps.apple.com/app/id1507246666
```

<details><summary>中文译文</summary>

```text
制作一段 15-30 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。

它应该是 http://presentifyapp.com 的发布视频，App Store 链接 - https://apps.apple.com/app/id1507246666
```

</details>

<sub>Inputs: Screenshots</sub>

[Original post ↗](https://x.com/rampatra_/status/2104134969622728835) · Prompt posted in [this reply](https://x.com/rampatra_/status/2104134971526938695).

---

### AIsa 15-second brand motion graphic

<a href="https://x.com/0xfemyn/status/2103796337041137833"><img src="https://pbs.twimg.com/amplify_video_thumb/2103795409164349440/img/VJ15VBNqXBfxy2wp.jpg" alt="AIsa 15-second brand motion graphic" width="480"></a>

[@0xfemyn](https://x.com/0xfemyn) · 2026-09-26 · 🔖 3 · ▶ 358 · `One-shot`

A 15-second motion graphics promo for the brand AIsa, from a trimmed-down version of the showreel prompt.

```text
make a dynamic 15-second motion graphics video for AIsa. Go all out.
```

<details><summary>中文译文</summary>

```text
给 AIsa 做一段 15 秒的动态图形视频。拿出全部本事。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/0xfemyn/status/2103796337041137833)

---

### One-line company demo video

<a href="https://x.com/vahidf24/status/2103258346690121886"><img src="https://pbs.twimg.com/amplify_video_thumb/2103255806611238912/img/jbadu1W8H4aYh9jC.jpg" alt="One-line company demo video" width="480"></a>

[@vahidf24](https://x.com/vahidf24) · 2026-09-24 · 🔖 3 · ▶ 434 · `Template`

A 70-second product demo video from a one-line template; the author suggests also giving real screenshots, product assets and brand material.

```text
make the most impressive demo video for (company name)
```

<details><summary>中文译文</summary>

```text
为（公司名）做一个最让人印象深刻的演示视频
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/vahidf24/status/2103258346690121886) · Prompt posted in [this reply](https://x.com/vahidf24/status/2103258350746058976).

---

### Portfolio-site intro with its own music

<a href="https://x.com/BogdanDragomir/status/2104045641538412658"><img src="https://pbs.twimg.com/amplify_video_thumb/2104045590128517120/img/M9vG6QMbpAFTG00S.jpg" alt="Portfolio-site intro with its own music" width="480"></a>

[@BogdanDragomir](https://x.com/BogdanDragomir) · 2026-09-27 · 🔖 3 · ▶ 1.6k · `One-shot`

A 15-second intro for a portfolio-site builder, with music Opus composed itself and the cuts synced to it; no other tools used.

```text
Create an intro for https://myfolio.so highlighting what it does.

Create the music too and make sure the video is synced with it.

Give your best, Ultracode, as if it’s your portfolio master piece.
```

<details><summary>中文译文</summary>

```text
为 https://myfolio.so 做一段片头，突出它是做什么的。

音乐也由你来做，并确保视频和音乐同步。

拿出你的最好水平，Ultracode，就当这是你作品集里的代表作。
```

</details>

[Original post ↗](https://x.com/BogdanDragomir/status/2104045641538412658)

---

### Reactive Resume product showreel

<a href="https://x.com/KingOKings/status/2103874453687992769"><img src="https://pbs.twimg.com/amplify_video_thumb/2103873354134421504/img/_Q3O3u0emCkU6EHG.jpg" alt="Reactive Resume product showreel" width="480"></a>

[@KingOKings](https://x.com/KingOKings) · 2026-09-26 · 🔖 3 · ▶ 329 · `Brief` · Remotion · HyperFrames

A 48-second showreel for the open-source résumé builder, made in Remotion from the project repo; Opus first asks questions about theme and direction.

```text
Do your research on Reactive Resume. Make a dynamic under-a-minute motion graphics video on Reactive Resume that shows what an incredible motion designer you are, like it's your showreel - Go all out!

If you need an idea as to how the UI looks inside the application, screenshots of every screen are available in a branch "ui-capture-2026-09-24" under /artifacts.

Provide me with questions and suggestions on how the theme and overall direction of the video should be, wait for my answers and then start building the video.

You may use Hyperframes or Remotion to generate the video, pick the one you feel most confident that you can get the best results out of.

The video must be super smooth, render at 60fps. Use motion blur on text between transitions to make it feel cohesive. Use the logo/icon assets that are already in the app.
```

<details><summary>中文译文</summary>

```text
研究一下 Reactive Resume。给 Reactive Resume 做一支不到一分钟的动态图形视频，展示你是多么出色的动效设计师，就像你的作品集一样——拿出全部本事！

如果你想知道应用里的 UI 长什么样，每个页面的截图都在分支 "ui-capture-2026-09-24" 的 /artifacts 下。

先就视频的主题和整体方向给我提问题和建议，等我回答后再开始做视频。

你可以用 Hyperframes 或 Remotion 生成视频，选你最有把握做出最好效果的那个。

视频必须非常流畅，以 60fps 渲染。转场之间的文字加运动模糊，让整体更连贯。使用应用里已有的 logo/图标素材。
```

</details>

<sub>Inputs: Screenshots, Logo · Effort: max</sub>

[Original post ↗](https://x.com/KingOKings/status/2103874453687992769) · Prompt posted in [this reply](https://x.com/KingOKings/status/2103874455973835071).

---

### Release hype reel for Perceptron Mk1.5

<a href="https://x.com/Subraiz24/status/2104089865537331298"><img src="https://pbs.twimg.com/amplify_video_thumb/2104089823510437888/img/kfbYSWI-LJhjPVuq.jpg" alt="Release hype reel for Perceptron Mk1.5" width="480"></a>

[@Subraiz24](https://x.com/Subraiz24) · 2026-09-27 · 🔖 2 · ▶ 342 · `Brief`

A 15-second release hype reel that opens on a one-second hook and runs through typography, shape play, camera moves and color shifts, made in Claude Code.

```text
You are a world class motion designer and you need to make a 15 second release/hype reel of the latest Perceptron Mk1.5 release. Make it dynamic and confident: open with a striking hook in the first second, build through a sequence of distinct techniques (typography, shape play, camera moves, color shifts) and land on a clean memorable last frame. Pacing should feel like its cut to music. Go crazy.
```

<details><summary>中文译文</summary>

```text
你是世界级的动效设计师，需要为最新发布的 Perceptron Mk1.5 做一支 15 秒的发布/预热短片。要有动感、有自信：第一秒就用抓人的钩子开场，接着依次用不同的手法（字体排印、形状玩法、镜头运动、色彩变化）推进，最后落在一个干净、让人记得住的结尾画面上。节奏要像是踩着音乐剪的。放开了做。
```

</details>

<sub>Author: 10 minutes.</sub>

[Original post ↗](https://x.com/Subraiz24/status/2104089865537331298) · Prompt posted in [this reply](https://x.com/Subraiz24/status/2104089866996994209).

---

### Octostudio promo from the showreel prompt

<a href="https://x.com/DesignByFusun/status/2103672001206559069"><img src="https://pbs.twimg.com/amplify_video_thumb/2103671886827712512/img/-A9Jsbj95Y2S0oCM.jpg" alt="Octostudio promo from the showreel prompt" width="480"></a>

[@DesignByFusun](https://x.com/DesignByFusun) · 2026-09-26 · 🔖 2 · ▶ 307 · `One-shot`

The showreel prompt pointed at a URL: a 15-second motion-graphics piece about octostudio.co, with no illustration or editing work from the author.

```text
Make a dynamic 15-second motion graphics video about https://octostudio.co that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

<details><summary>中文译文</summary>

```text
制作一段关于 https://octostudio.co 的 15 秒动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。
```

</details>

[Original post ↗](https://x.com/DesignByFusun/status/2103672001206559069) · Prompt posted in [this reply](https://x.com/DesignByFusun/status/2103672432167121137).

---

### Fill-in showreel prompt for your project

<a href="https://x.com/en______ra/status/2104035188061986980"><img src="https://pbs.twimg.com/amplify_video_thumb/2104034731428134912/img/EZIS3LohWGDN972X.jpg" alt="Fill-in showreel prompt for your project" width="480"></a>

[@en______ra](https://x.com/en______ra) · 2026-09-27 · 🔖 2 · ▶ 275 · `Template`

The showreel prompt with a slot for your project's name; the author's 16-second result promotes RedSeed AI.

```text
make a dynamic 15-second motion graphics video for RedSeed AI (Replace with your Project) that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

<details><summary>中文译文</summary>

```text
为 RedSeed AI（替换成你的项目）制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。
```

</details>

[Original post ↗](https://x.com/en______ra/status/2104035188061986980)

---

### Two-step ad: write a prompt, then apply it

<a href="https://x.com/l3d1c/status/2103536553930752011"><img src="https://pbs.twimg.com/amplify_video_thumb/2103536403975958528/img/bDq_SazZbn4mXAz0.jpg" alt="Two-step ad: write a prompt, then apply it" width="480"></a>

[@l3d1c](https://x.com/l3d1c) · 2026-09-25 · 🔖 2 · ▶ 947 · `Pipeline`

A 30-second ad for the author's site: Opus first writes its own motion-design prompt, then applies it, recreating the real app UI from the codebase.

```text
Prompt 1: "create a motion design prompt for an ad for our site"
Prompt 2: "now apply it"
```

<details><summary>中文译文</summary>

```text
提示词 1：「为我们的网站写一个广告的动效设计提示词」
提示词 2：「现在执行它」
```

</details>

[Original post ↗](https://x.com/l3d1c/status/2103536553930752011)

---

### Cinematic trailer for an indie game

<a href="https://x.com/design_oyaji/status/2103992348535595425"><img src="https://pbs.twimg.com/amplify_video_thumb/2103988530590703616/img/Cq_djBHPhHoqpNSB.jpg" alt="Cinematic trailer for an indie game" width="480"></a>

[@design_oyaji](https://x.com/design_oyaji) · 2026-09-26 · 🔖 2 · ▶ 285 · `Pipeline` · Higgsfield

A 30-second cinematic trailer for the author's game NINJUTSU REVERSI, made in Claude Code with the Higgsfield MCP under a 100-credit cap plus the JIZURA tool.

```text
NINJUTSU REVERSIで30秒。
Higgsfieldは100クレジット以内で。
JIZURAも使って、超絶かっこいいシネマティック・トレーラー作れる？
```

<details><summary>English translation</summary>

```text
30 seconds for NINJUTSU REVERSI.
Keep Higgsfield within 100 credits.
Use JIZURA too. Can you make an insanely cool cinematic trailer?
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/design_oyaji/status/2103992348535595425)

---

### Showreel prompt pointed at a side project

<a href="https://x.com/Adamdesgns/status/2103542756555768014"><img src="https://pbs.twimg.com/amplify_video_thumb/2103542594726768641/img/VGr9HsSu1cUKgt4Y.jpg" alt="Showreel prompt pointed at a side project" width="480"></a>

[@Adamdesgns](https://x.com/Adamdesgns) · 2026-09-25 · 🔖 2 · ▶ 179 · `One-shot`

The widely shared showreel prompt with one added line naming the author's project, The Pipefitters Bible, giving a 15-second promo.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out. (About the pipefitters bible)
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。（关于 pipefitters bible）
```

</details>

[Original post ↗](https://x.com/Adamdesgns/status/2103542756555768014)

---

### Product explainer for Distilbook

<a href="https://x.com/sudo_kiran/status/2103486573476254201"><img src="https://pbs.twimg.com/amplify_video_thumb/2103486232395444224/img/rB2EKRCXBv4Lwg2m.jpg" alt="Product explainer for Distilbook" width="480"></a>

[@sudo_kiran](https://x.com/sudo_kiran) · 2026-09-25 · 🔖 2 · ▶ 415 · `One-shot`

A 30-second motion-graphics product explainer from one sentence plus the product URL; Opus added the music on its own.

```text
make a dynamic 30-seconds motion graphic video about the distilbook like a product explainer the video has to be very incredible
(product url)
```

<details><summary>中文译文</summary>

```text
做一段 30 秒的动态图形视频，像产品讲解一样介绍 distilbook，视频要非常惊艳
（产品链接）
```

</details>

[Original post ↗](https://x.com/sudo_kiran/status/2103486573476254201)

---

### Bento.surf product video after web research

<a href="https://x.com/bizibeast/status/2103696876130505124"><img src="https://pbs.twimg.com/amplify_video_thumb/2103696725949206529/img/M9lTbC9byRlZdu0D.jpg" alt="Bento.surf product video after web research" width="480"></a>

[@bizibeast](https://x.com/bizibeast) · 2026-09-26 · 🔖 2 · ▶ 279 · `One-shot`

A 40-second product video: Opus researches the site first, then builds a motion-graphics showreel about it.

```text
Research http://Bento.surf. Make a dynamic 40-second motion graphics video on http://Bento.surf that shows what an incredible motion designer you are. like it's your showreel - Go all out.
```

<details><summary>中文译文</summary>

```text
研究一下 http://Bento.surf。为 http://Bento.surf 制作一段 40 秒的动态图形视频，展示你是多么出色的动效设计师。就像你的作品集一样——拿出全部本事。
```

</details>

[Original post ↗](https://x.com/bizibeast/status/2103696876130505124)

---

### Website showreel from the author's footage

<a href="https://x.com/andginja/status/2103492000733618685"><img src="https://pbs.twimg.com/amplify_video_thumb/2103491185536806912/img/KgKs1S58QtAznGGw.jpg" alt="Website showreel from the author&#x27;s footage" width="480"></a>

[@andginja](https://x.com/andginja) · 2026-09-25 · 🔖 2 · ▶ 242 · `One-shot`

A 15-second showreel for the author's website: Opus cut his own footage, animated everything in code and composed the music.

```text
make a 15-second showreel about my website. Go all out.
```

<details><summary>中文译文</summary>

```text
为我的网站做一段 15 秒的展示短片。拿出全部本事。
```

</details>

<sub>Inputs: Footage</sub>

[Original post ↗](https://x.com/andginja/status/2103492000733618685)

---

### Newsletter promo from the showreel prompt

<a href="https://x.com/KangarooHere/status/2103617278671818789"><img src="https://pbs.twimg.com/amplify_video_thumb/2103617221360787456/img/JwnZgD1Z0ZVbm5EH.jpg" alt="Newsletter promo from the showreel prompt" width="480"></a>

[@KangarooHere](https://x.com/KangarooHere) · 2026-09-25 · 🔖 2 · ▶ 185 · `One-shot`

A 20-second motion-graphics promo for the author's newsletter, adapted from the widely shared showreel prompt and run on medium effort.

```text
make a dynamic 20-second motion graphics video for my newsletter that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

<details><summary>中文译文</summary>

```text
为我的 newsletter 制作一段 20 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。
```

</details>

<sub>Effort: medium</sub>

[Original post ↗](https://x.com/KangarooHere/status/2103617278671818789)

---

### Hand-drawn promo for listing on AppSumo

<a href="https://x.com/mattbean/status/2103146389412917572"><img src="https://pbs.twimg.com/amplify_video_thumb/2103146130402062336/img/xeoRxXNdQ9BWmzdr.jpg" alt="Hand-drawn promo for listing on AppSumo" width="480"></a>

[@mattbean](https://x.com/mattbean) · 2026-09-24 · 🔖 2 · ▶ 60 · `Brief`

A 30-second drawing-style promo that walks through three steps of listing a product on AppSumo through your agent.

```text
build me a 30s drawing style animated clip about submitting a product to AppSumo via your agent.

steps are:
1. connect your agent
2. your agent fills out your listing and sets up redemption
3. go live!
```

<details><summary>中文译文</summary>

```text
给我做一段 30 秒的手绘风动画短片，讲如何通过你的 agent 把产品提交到 AppSumo。

步骤是：
1. 连接你的 agent
2. 你的 agent 填写产品页并设置兑换
3. 上线！
```

</details>

[Original post ↗](https://x.com/mattbean/status/2103146389412917572) · Prompt posted in [this reply](https://x.com/mattbean/status/2103146558455980355).

---

### Hype edit for ODATANO

<a href="https://x.com/maxalexweber/status/2103118009535459784"><img src="https://pbs.twimg.com/amplify_video_thumb/2103117596207763456/img/xDPhlL8YfErRfkeZ.jpg" alt="Hype edit for ODATANO" width="480"></a>

[@maxalexweber](https://x.com/maxalexweber) · 2026-09-24 · 🔖 1 · ▶ 677 · `One-shot`

An 18-second high-energy promo edit for the ODATANO project, generated from a seven-word prompt.

```text
Make a ODATANO edit that goes hard
```

<details><summary>中文译文</summary>

```text
做一个超燃的 ODATANO 剪辑
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/maxalexweber/status/2103118009535459784)

---

### Ren app launch motion graphic

<a href="https://x.com/macrohou/status/2103545787875733862"><img src="https://pbs.twimg.com/amplify_video_thumb/2103545006157889536/img/jwj0xW-2HarPPUqw.jpg" alt="Ren app launch motion graphic" width="480"></a>

[@macrohou](https://x.com/macrohou) · 2026-09-25 · 🔖 1 · ▶ 391 · `One-shot`

A 30-second launch motion graphic for the Ren app, made with access to its repo; Opus handles both the visuals and the sound design.

```text
[gave access to Ren repo] Make a dynamic 30-second motion graphics video for Ren that shows off your motion and sound design. Go crazy.
```

<details><summary>中文译文</summary>

```text
[已开放 Ren 代码仓库的访问权限] 为 Ren 制作一段 30 秒的动态图形视频，展示你的动效和声音设计功力。放开了做。
```

</details>

<sub>Inputs: Brand kit · Author: after each video, told it to one-up the previous one (&quot;Show me your full capabilities&quot;, &quot;Make it the best one yet&quot;).</sub>

[Original post ↗](https://x.com/macrohou/status/2103545787875733862)

---

### Punchy launch video for an inference startup

<a href="https://x.com/lepadev/status/2103101681806475414"><img src="https://pbs.twimg.com/amplify_video_thumb/2103101476889325568/img/j-bHtW20ZouiF944.jpg" alt="Punchy launch video for an inference startup" width="480"></a>

[@lepadev](https://x.com/lepadev) · 2026-09-24 · 🔖 1 · ▶ 24.8k · `One-shot`

A 30-second slick promo for an unnamed AI inference startup, made without any video generation model or extra libraries.

```text
make a modern slick and punchy video for a modern startup that works on inference

no video gen model, no additional libraries.
```

<details><summary>中文译文</summary>

```text
为一家做推理（inference）的新锐创业公司做一段现代、精致、有冲击力的视频

不用视频生成模型，不用额外的库。
```

</details>

[Original post ↗](https://x.com/lepadev/status/2103101681806475414) · Prompt posted in [this reply](https://x.com/lepadev/status/2103105157265592471).

---

### Narrated explainer for a language-learning app

<a href="https://x.com/1stnoel_/status/2103247530259603851"><img src="https://pbs.twimg.com/amplify_video_thumb/2103246862220140546/img/zmtKlwtnHyEMr5AY.jpg" alt="Narrated explainer for a language-learning app" width="480"></a>

[@1stnoel_](https://x.com/1stnoel_) · 2026-09-24 · 🔖 1 · ▶ 297 · `One-shot` · TTS

A one-minute educational video about the author's reading-based language-learning app, with synthesized voice narration.

```text
Make a 1-minute educational video about https://readsotto.app/ with synthesized voice narration.
```

<details><summary>中文译文</summary>

```text
做一段 1 分钟的讲解视频，介绍 https://readsotto.app/，配上合成的语音旁白。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/1stnoel_/status/2103247530259603851)

---

### Emotional app promo from two short sentences

<a href="https://x.com/marklaunches/status/2103811146411041046"><img src="https://pbs.twimg.com/amplify_video_thumb/2103810409455104000/img/nG85Mf9l-AO2WFea.jpg" alt="Emotional app promo from two short sentences" width="480"></a>

[@marklaunches](https://x.com/marklaunches) · 2026-09-26 · 🔖 1 · ▶ 283 · `One-shot`

A 44-second emotional promo video for the author's app, made from a two-sentence prompt.

```text
build me an incredible video for my app. make it emotional.
```

<details><summary>中文译文</summary>

```text
为我的应用做一段超棒的视频。要有情感。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/marklaunches/status/2103811146411041046)

---

### Remotion showreel of a developer portfolio site

<a href="https://x.com/wani_shola/status/2103769906638459278"><img src="https://pbs.twimg.com/amplify_video_thumb/2103768901662179328/img/plwUcebyyob2ZeqE.jpg" alt="Remotion showreel of a developer portfolio site" width="480"></a>

[@wani_shola](https://x.com/wani_shola) · 2026-09-26 · 🔖 1 · ▶ 111 · `Brief` · Remotion

A 90–100 second Remotion showreel of a DevRel portfolio site, animating real page captures in browser and phone frames, cut to 120 BPM music.

```text
Make a showreel-style motion graphics video for my portfolio website, http://sholajegede.com, using Remotion. It should show what I do as a developer relations engineer, like a showreel for my résumé.

- Use as much of the real website as possible: capture the pages and sections in a browser (home, Ask, package pages, Hire, mobile view, dark mode) and animate them inside browser and phone frames.
- Show the site's chat answering real questions about my work, with the questions and answers large and bold. Use only facts and numbers that are on the site.
- Follow premium brand rules: three colours and the site's own fonts, one idea per shot, key objects centred, space to breathe, eased motion only, smooth transitions instead of hard cuts, and a rhythm that speeds up and slows down with the story.
- Add music at about 120 BPM (elite, kinetic, sophisticated) and cut every scene on the beat. No extra sound effects.
- 1920×1080, about 90 to 100 seconds, ending on the website and my contact email.
```

<details><summary>中文译文</summary>

```text
用 Remotion 为我的作品集网站 http://sholajegede.com 做一段作品集风格的动态图形视频。它要展示我作为开发者关系工程师在做什么，就像简历里的作品集。

- 尽量多用真实网站：在浏览器里截取各个页面和板块（首页、Ask、package 页面、Hire、移动端视图、深色模式），放进浏览器框和手机框里做动画。
- 展示网站的聊天功能回答关于我工作的真实问题，问题和回答都要大而醒目。只用网站上有的事实和数字。
- 遵守高级品牌规范：三种颜色加网站自己的字体，一个镜头只讲一个点，关键物体居中，留出呼吸空间，只用缓动，用平滑转场代替硬切，节奏随故事时快时慢。
- 加一段约 120 BPM 的音乐（精英感、动感、精致），每个场景都卡在节拍上切。不要额外音效。
- 1920×1080，约 90 到 100 秒，结尾停在网站和我的联系邮箱上。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/wani_shola/status/2103769906638459278)

---

### Thank-you video for the first 100 users

<a href="https://x.com/Sudiyasa_/status/2103638831669076027"><img src="https://pbs.twimg.com/amplify_video_thumb/2103638506476306432/img/FHWliD-plzXiAeW3.jpg" alt="Thank-you video for the first 100 users" width="480"></a>

[@Sudiyasa_](https://x.com/Sudiyasa_) · 2026-09-26 · 🔖 1 · ▶ 351 · `One-shot`

The showreel prompt turned into a 15-second thank-you motion graphic celebrating a bot product's first 100 users.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out  do this to thank the first 100 users of @eyezonbot
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事，用它来感谢 @eyezonbot 的前 100 位用户。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/Sudiyasa_/status/2103638831669076027)

---

### Portfolio video with a self-critique loop

<a href="https://x.com/heyiammallik/status/2103837803587293397"><img src="https://pbs.twimg.com/amplify_video_thumb/2103835493410693120/img/lA17ZvStdM8s6Za8.jpg" alt="Portfolio video with a self-critique loop" width="480"></a>

[@heyiammallik](https://x.com/heyiammallik) · 2026-09-26 · 🔖 1 · ▶ 100 · `Brief`

A roughly 30-second video built from the author's portfolio; the prompt makes Opus research current motion and sound trends and restart if it doesn't look pro.

```text
you are a pro motion designer. analyze my portfolio and make a ~30 second video from it. check what are the recent trending techniques used for motion and sound design. question your strategy and plan, if it doesn't feel like done by a pro designer, start over. every frame matters from the first frame to the final frame. go crazy
```

<details><summary>中文译文</summary>

```text
你是一名专业动效设计师。分析我的作品集，用它做一段约 30 秒的视频。查一查最近动效和声音设计流行哪些手法。质疑你的策略和计划，如果感觉不像专业设计师做的，就推倒重来。从第一帧到最后一帧，每一帧都重要。放开了做。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/heyiammallik/status/2103837803587293397)

---

### Brand motion graphic for the startup Quetzal

<a href="https://x.com/miskinho_/status/2103847584531956105"><img src="https://pbs.twimg.com/amplify_video_thumb/2103846719867727872/img/aFmuU2HRsVlpQILT.jpg" alt="Brand motion graphic for the startup Quetzal" width="480"></a>

[@miskinho_](https://x.com/miskinho_) · 2026-09-26 · 🔖 1 · ▶ 277 · `One-shot`

A 15-second brand motion graphic for the startup Quetzal, made by pointing the viral showreel prompt at the product.

```text
make  1 dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for Quetzal. go all out.
```

<details><summary>中文译文</summary>

```text
制作 1 段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像为 Quetzal 做的作品集一样。拿出全部本事。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/miskinho_/status/2103847584531956105)

---

### Showreel-style promo for the org2html project

<a href="https://x.com/kyonax_on_tech/status/2103482598144049316"><img src="https://pbs.twimg.com/amplify_video_thumb/2103481982168547328/img/MOiE5sxwIHZTU5SO.jpg" alt="Showreel-style promo for the org2html project" width="480"></a>

[@kyonax_on_tech](https://x.com/kyonax_on_tech) · 2026-09-25 · 🔖 1 · ▶ 148 · `Brief`

A 15-second promo for the author's org2html project that extends the résumé showreel prompt with use cases, flow, an ASCII logo and the brand palette.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.

Make sure to showcase properly the usecases, the flow, properly show everything on how it works, also the ascii logo of this is on the kyo-web-online, keep in mind also the color palette.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。

一定要把用例、流程展示到位，把它怎么运作的方方面面都好好呈现出来；另外它的 ASCII logo 在 kyo-web-online 上，也要记得配色。
```

</details>

<sub>Inputs: Brand kit · Author: one shot, no iterations; under 1% of a $200 subscription.</sub>

[Original post ↗](https://x.com/kyonax_on_tech/status/2103482598144049316)

---

### Rynok Online promo from reference videos

<a href="https://x.com/Mortid_X/status/2104001655587181052"><img src="https://pbs.twimg.com/amplify_video_thumb/2104000947181527040/img/wDWKTp9GTtiM88aH.jpg" alt="Rynok Online promo from reference videos" width="480"></a>

[@Mortid_X](https://x.com/Mortid_X) · 2026-09-27 · 🔖 1 · ▶ 365 · `Brief`

A 17-second promo for the Rynok Online app that combines two reference videos, app screenshots and the viral showreel prompt, run at xHigh effort.

```text
References:

http://x.com/heyandras/status/2103453411857580294?s=20

http://x.com/motion_conquest/status/2103510103622308152?s=20

Create a dynamic video for Rynok Online based on these references — and make it even better. The video can be up to 1 minute long.

Make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. Go all out.

Use elements from the images or recreate them yourself — whatever works best.

The screenshots are only there to show what the app looks like. You don’t have to use them directly, but it’s important that the final video looks top-tier.
```

<details><summary>中文译文</summary>

```text
参考：

http://x.com/heyandras/status/2103453411857580294?s=20

http://x.com/motion_conquest/status/2103510103622308152?s=20

参考这些样片为 Rynok Online 做一段动感视频，而且要做得更好。视频最长可以到 1 分钟。

制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。

可以用图片里的元素，也可以自己重新做，怎么效果好怎么来。

截图只是为了让你看看应用长什么样。你不必直接用它们，但最终视频一定要是顶级水准。
```

</details>

<sub>Inputs: Reference video, Screenshots · Author: 1 minute writing the prompt, 60 minutes generating the video.</sub>

[Original post ↗](https://x.com/Mortid_X/status/2104001655587181052) · Prompt posted in [this reply](https://x.com/Mortid_X/status/2104001659055596004).

---

### Orglet launch video after using the app

<a href="https://x.com/anxuanng/status/2103590725996990790"><img src="https://pbs.twimg.com/amplify_video_thumb/2103590674998374400/img/icoTFkwysn4P0OPB.jpg" alt="Orglet launch video after using the app" width="480"></a>

[@anxuanng](https://x.com/anxuanng) · 2026-09-25 · 🔖 1 · ▶ 287 · `One-shot`

A 30-second launch video for the Orglet app. Claude Code first installs and uses the app, then turns what it learned into a motion showreel.

```text
Open the Orglet app on this computer (install it from http://orglet.codepawl.com if it isn't there) and use it for a while until you understand what it does, then make a dynamic 30 second motion graphics video about it that shows what an incredible motion designer you are, like it's your showreel, go all out.
```

<details><summary>中文译文</summary>

```text
打开这台电脑上的 Orglet 应用（如果没有，就从 http://orglet.codepawl.com 安装），先用上一阵子，直到弄懂它是做什么的，然后为它制作一段 30 秒的动态图形视频，展示你是多么出色的动效设计师，就像你的作品集一样，拿出全部本事。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/anxuanng/status/2103590725996990790) · Prompt posted in [this reply](https://x.com/anxuanng/status/2103590730891735078).

---

### Vertical promo for a motorcycle navigation app

<a href="https://x.com/Bilimfili1/status/2103743617848459762"><img src="https://pbs.twimg.com/amplify_video_thumb/2103743327665373184/img/I7yPxCE-z--YfkqT.jpg" alt="Vertical promo for a motorcycle navigation app" width="480"></a>

[@Bilimfili1](https://x.com/Bilimfili1) · 2026-09-26 · 🔖 1 · ▶ 2.5k · `Brief` · ElevenLabs

A 45–50 second vertical app promo built from real simulator recordings, where each feature breaks out of the phone; music added separately with ElevenLabs.

```text
Make a 45–50 second vertical video for my app: a glance inside the app.
Show every feature, use motion, be creative. I want it good enough for your CV.

- Real, not mocked: record each feature being used in the simulator (tap a filter, open a result, add it).
- Stretch your imagination: let each feature break out of the phone and change the world around it.
- The bar: a motion designer's showreel piece. The best motion you can do. Go all out.
- Nothing made up: every number and label on screen comes from the recordings.
- No stock sound effects; I'll add the music.
- Keep text clear of the TikTok/Instagram interface.
- Let viewers follow: each feature stays on screen for at least 2.5 seconds.
```

<details><summary>中文译文</summary>

```text
为我的应用做一段 45–50 秒的竖版视频：带观众看一眼应用内部。
展示每一个功能，用上动效，发挥创意。我要它好到能放进你的简历。

- 要真实，不要模拟：在模拟器里录下每个功能的实际使用过程（点一个筛选、打开一个结果、添加它）。
- 放开想象：让每个功能冲出手机，改变它周围的世界。
- 标准：动效设计师作品集级别的作品。拿出你能做到的最好动效。全力以赴。
- 不许编造：屏幕上的每个数字和标签都必须来自录屏。
- 不要素材库音效；音乐我来加。
- 文字要避开 TikTok/Instagram 的界面区域。
- 让观众跟得上：每个功能至少在屏幕上停留 2.5 秒。
```

</details>

<sub>Inputs: Brand kit, Music</sub>

[Original post ↗](https://x.com/Bilimfili1/status/2103743617848459762) · Prompt posted in [this reply](https://x.com/Bilimfili1/status/2103743802938671516).

---

### Rick and Morty-style pilot episode for a startup

<a href="https://x.com/RohitTirunellai/status/2103098255399878956"><img src="https://pbs.twimg.com/amplify_video_thumb/2103096568102649856/img/lmrvKP6BXSM-BhTY.jpg" alt="Rick and Morty-style pilot episode for a startup" width="480"></a>

[@RohitTirunellai](https://x.com/RohitTirunellai) · 2026-09-24 · 🔖 1 · ▶ 85 · `Brief` · TTS

A 30–60 second product promo in Rick and Morty style: a heist or adventure pilot built from the product docs, with TTS voices and a $37 API cap.

```text
Create a pure javascript animation.

30s-60s whimsical rick & morty animation style with appropriate audio on any topic from http://agent37.com/docs . its the pilot episode

they shd be in the middle of a heist or an adventure

Entire video should be as high of a production value as possible. Please spend your time on this, it's very important.

Use high quality text-to-speech model for generation. You can find monid API key in .env file

You can use any tools you can find access to and resources on the internet. You create the script, the assets, the animation, concept, everything.

I have to go away from my computer so please work autonomously until done. Quality is paramount. Production value should be on professional level.

One more thing: max @MonidHQ  spend is 37 dollars
```

<details><summary>中文译文</summary>

```text
做一段纯 javascript 动画。

30 到 60 秒，俏皮的《瑞克和莫蒂》（rick & morty）动画风格，配上合适的音频，主题从 http://agent37.com/docs 里任选。这是试播集

他们应该正处在一场劫案或一次冒险当中

整部视频的制作水准要尽可能高。请在这上面多花时间，这非常重要。

用高质量的文本转语音模型来生成。monid 的 API key 在 .env 文件里

你可以使用任何你能访问到的工具和网上资源。剧本、素材、动画、概念，全部由你来做。

我得离开电脑，所以请自主工作直到完成。质量是第一位的。制作水准要达到专业级别。

还有一点：@MonidHQ 最多花 37 美元
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/RohitTirunellai/status/2103098255399878956)

---

### SaaS launch video for Slideforge

<a href="https://x.com/techtactician/status/2103219463508144474"><img src="https://pbs.twimg.com/amplify_video_thumb/2103219345216180224/img/t201t6Cdfff6JIQy.jpg" alt="SaaS launch video for Slideforge" width="480"></a>

[@techtactician](https://x.com/techtactician) · 2026-09-24 · 🔖 1 · ▶ 59 · `Brief`

A 60-second SaaS launch video in the motion-graphics style common on X, with Opus pulling product details and assets from the website itself.

```text
I want you to create a highly professional SaaS product launch video for Slideforge. You can find its details in https://slideforge.io. Pick that, and then make sure to get actual assets and images and all of that stuff from the internet. Turn it into these typical, very professionally edited, motion-graphics-styled product launch videos that you see people making on Twitter when they launch new SaaS products (which are showing off the features, the benefits, and all of these things).
```

<details><summary>中文译文</summary>

```text
我想让你为 Slideforge 做一支非常专业的 SaaS 产品发布视频。它的详情可以在 https://slideforge.io 找到。选定它，然后一定要从网上找来真实的素材、图片之类的所有东西。把它做成那种典型的、剪辑非常专业、动态图形风格的产品发布视频，就是大家在推特上发布新 SaaS 产品时常做的那种（展示功能、好处等等）。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/techtactician/status/2103219463508144474) · Prompt posted in [this reply](https://x.com/techtactician/status/2103219465164853643).

---

### Story-driven app promo in Three.js

<a href="https://x.com/Anilraok/status/2103087766662009118"><img src="https://pbs.twimg.com/amplify_video_thumb/2103086574787493888/img/woD58rR9joVjoX3I.jpg" alt="Story-driven app promo in Three.js" width="480"></a>

[@Anilraok](https://x.com/Anilraok) · 2026-09-24 · 🔖 1 · ▶ 44 · `One-shot` · Three.js

A Three.js animated short in which Opus invents a story that quietly promotes the author's app, aiming for Pixar-level polish and social reach.

```text
I want you to imagine a story, that subtly promotes grid genius. Or it can not even have grid genius, but something that aligns with our app and helps us get more eyeballs when posted on social media. Then using threejs/javascript I want you to create full animation, Pixar-level quality out of the story you imagine
```

<details><summary>中文译文</summary>

```text
我想让你构思一个故事，巧妙地软性推广 grid genius。也可以根本不出现 grid genius，只要是和我们 App 调性一致、发到社交媒体上能帮我们吸引更多眼球的东西就行。然后用 threejs/javascript，把你构思的故事做成完整的动画，达到皮克斯级别的质量
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/Anilraok/status/2103087766662009118)

---

### Oscilloscope-style studio motion graphic

<a href="https://x.com/rneayan/status/2103401461837406275"><img src="https://pbs.twimg.com/amplify_video_thumb/2103401099244040192/img/2VkbrEruIa5W_cQo.jpg" alt="Oscilloscope-style studio motion graphic" width="480"></a>

[@rneayan](https://x.com/rneayan) · 2026-09-25 · 🔖 1 · ▶ 31 · `One-shot`

A 40-second motion graphic about the author's studio in an oscilloscope style, from a one-line prompt.

```text
Make Motiongraphic about my studio with Oscilloscope style
```

<details><summary>中文译文</summary>

```text
用示波器（Oscilloscope）风格做一个关于我工作室的动态图形
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/rneayan/status/2103401461837406275)

---

### Risograph-style studio intro

<a href="https://x.com/rneayan/status/2103401006281441493"><img src="https://pbs.twimg.com/amplify_video_thumb/2103400837309743104/img/aWk04-Af8Hgk0iAk.jpg" alt="Risograph-style studio intro" width="480"></a>

[@rneayan](https://x.com/rneayan) · 2026-09-25 · 🔖 1 · ▶ 20 · `One-shot`

A 69-second video about the author's studio in a Risograph print style, from a one-line prompt.

```text
make about my studio with Risograph style
```

<details><summary>中文译文</summary>

```text
用 Risograph（孔版印刷）风格做点关于我工作室的东西
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/rneayan/status/2103401006281441493)

---

### Self-made trailer for a Tron game

<a href="https://x.com/0xRathi/status/2102986585004511319"><img src="https://pbs.twimg.com/amplify_video_thumb/2102986032291729408/img/D7p1sJ5gkBD803tp.jpg" alt="Self-made trailer for a Tron game" width="480"></a>

[@0xRathi](https://x.com/0xRathi) · 2026-09-24 · ▶ 446 · `One-shot`

A 45-second trailer Opus made on its own while building a Tron-style game, along with three rival bots and original music.

```text
make a Tron game.
```

<details><summary>中文译文</summary>

```text
做一个 Tron 游戏。
```

</details>

[Original post ↗](https://x.com/0xRathi/status/2102986585004511319)

---

### Sherwood Protocol promo video

<a href="https://x.com/imthatcarlos/status/2102849219388133592"><img src="https://pbs.twimg.com/amplify_video_thumb/2102849024877322241/img/u1PogTVT0artEShz.jpg" alt="Sherwood Protocol promo video" width="480"></a>

[@imthatcarlos](https://x.com/imthatcarlos) · 2026-09-23 · ▶ 632 · `One-shot` · Remotion

A one-minute Remotion promo for Sherwood Protocol that reuses the app's own components and branding to explain agentic hedge funds simply.

```text
make a modern slick and punchy video for sherwood protocol. feel free to take branding or components from the landing page or app. the goal is to highlight how it enables agentic hedge funds, explaining it simply
```

<details><summary>中文译文</summary>

```text
为 sherwood protocol 做一支现代、利落、有冲击力的视频。可以随意取用落地页或应用里的品牌元素和组件。目标是突出它如何让智能体对冲基金成为可能，并讲得简单易懂
```

</details>

<sub>Inputs: Brand kit · Author: one-shot.</sub>

[Original post ↗](https://x.com/imthatcarlos/status/2102849219388133592)

---

### Showreel prompt aimed at a product site

<a href="https://x.com/0xScoffie/status/2103779700954779830"><img src="https://pbs.twimg.com/amplify_video_thumb/2103779072488755200/img/q1aAPYfIDJYktaZW.jpg" alt="Showreel prompt aimed at a product site" width="480"></a>

[@0xScoffie](https://x.com/0xScoffie) · 2026-09-26 · ▶ 179 · `One-shot`

A 15-second motion graphic for aluta.ke, made by adding the site's URL to the end of the résumé showreel prompt.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out. it should be about https://aluta.ke/
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。内容要围绕 https://aluta.ke/
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/0xScoffie/status/2103779700954779830) · Prompt posted in [this reply](https://x.com/0xScoffie/status/2103779976978080209).

---

### 15-second brand reel for Reflex

<a href="https://x.com/reflex_cloud/status/2103552840027304046"><img src="https://pbs.twimg.com/amplify_video_thumb/2103552536779141120/img/GxhY3z6FxpK20ymG.jpg" alt="15-second brand reel for Reflex" width="480"></a>

[@reflex_cloud](https://x.com/reflex_cloud) · 2026-09-25 · ▶ 107 · `Brief`

A 15-second brand reel for Reflex with a first-second hook, typography, shape play and camera moves, and Opus told to pick its tools from scratch.

```text
You're a world-class motion designer, and this is your 15-second résumé reel. Make it dynamic and confident: open with a striking hook in the first second, build through a sequence of distinct techniques (typography, shape play, camera moves, colour shifts), and land on a clean, memorable final frame. Pacing should feel like it's cut to music. Go crazy.

Make it promote our brand, reflex. inc. Proceed as if you were starting with zero of my tools. Do not assume that the tools we already have are the best to use, as they might be outdated.
```

<details><summary>中文译文</summary>

```text
你是世界级的动效设计师，这是你 15 秒的简历作品集。要动感、自信：第一秒就用一个抓人的开场，接着依次展示不同的技法（字体排版、图形玩法、镜头运动、色彩变化），最后落在一个干净、令人难忘的结尾画面上。节奏要像是踩着音乐剪的。放开了做。

用它来推广我们的品牌 reflex. inc。就当你手上完全没有我的任何工具。不要默认我们已有的工具就是最好的，它们可能已经过时。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/reflex_cloud/status/2103552840027304046)

---

### Showreel prompt pointed at a brand

<a href="https://x.com/theattnlayer/status/2103776779064471834"><img src="https://pbs.twimg.com/amplify_video_thumb/2103776675939201024/img/ndG052ll7pQFEzB6.jpg" alt="Showreel prompt pointed at a brand" width="480"></a>

[@theattnlayer](https://x.com/theattnlayer) · 2026-09-26 · ▶ 432 · `One-shot` · Remotion · Python

A 15-second brand reel for The Attention Layer, with every frame coded in Remotion and the soundtrack written in Python.

```text
make a dynamic 15 second motion graphics video that shows what an incredible motion designer you are, like its your showreel for a resume, go all out, its about the attention layer
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样，拿出全部本事，主题是 the attention layer
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/theattnlayer/status/2103776779064471834) · Prompt posted in [this reply](https://x.com/theattnlayer/status/2103777103561031832).

---

### Startup promo with real product screenshots

<a href="https://x.com/zigapoto/status/2103746671591256286"><img src="https://pbs.twimg.com/amplify_video_thumb/2103746447338344448/img/9dTqELaECltAeA7f.jpg" alt="Startup promo with real product screenshots" width="480"></a>

[@zigapoto](https://x.com/zigapoto) · 2026-09-26 · ▶ 128 · `Brief` · Playwright · ffmpeg

A 60-second startup promo built by Claude Code in an empty folder: coded animation, Playwright captures of the real product, and matching music.

```text
make a modern slick and punchy video for a startup that works on agentic analytics, just javascript, playwright and ffmpeg, code the animation and take a video of it, download assets from the site or use playwright for screenshots, include music aligned with the video.
```

<details><summary>中文译文</summary>

```text
为一家做智能体分析（agentic analytics）的创业公司做一个现代、利落、有冲击力的视频，只用 javascript、playwright 和 ffmpeg，用代码写动画再录成视频，从网站下载素材或用 playwright 截图，配上和画面对齐的音乐。
```

</details>

<sub>Inputs: Brand kit · Author: no manual edits, one correction given afterward.</sub>

[Original post ↗](https://x.com/zigapoto/status/2103746671591256286) · Prompt posted in [this reply](https://x.com/zigapoto/status/2103746698660942208).

---

### Promo video for an open-source PPTX tool

<a href="https://x.com/feiflow/status/2104039666093572362"><img src="https://pbs.twimg.com/amplify_video_thumb/2104039167982219264/img/eH_xgqdD7sYz1gin.jpg" alt="Promo video for an open-source PPTX tool" width="480"></a>

[@feiflow](https://x.com/feiflow) · 2026-09-27 · ▶ 55 · `One-shot`

A 64-second promo with sound effects and music for deckuse, an open-source tool for editing pptx files, from one Chinese sentence.

```text
我需要推广 deckuse,帮我制作一个动画视频，包括音效和音乐，用于此产品宣传；你可以使用任何你觉得合适的工具和技术，做出最好最惊艳的效果
```

<details><summary>English translation</summary>

```text
I need to promote deckuse, help me make an animated video with sound effects and music to promote this product; you can use any tools and techniques you think are right, and make it as good and as stunning as possible
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/feiflow/status/2104039666093572362)

---

### Product clip for Tented image generation

<a href="https://x.com/justincooperman/status/2103201167367188876"><img src="https://pbs.twimg.com/amplify_video_thumb/2103199966391058432/img/pW6I9Lxii_fUSKpw.jpg" alt="Product clip for Tented image generation" width="480"></a>

[@justincooperman](https://x.com/justincooperman) · 2026-09-24 · ▶ 85 · `One-shot` · Blender

A 30-second product video; Claude Code logged into the app to take screenshots, used Blender and picked the audio itself.

```text
Make an animated clip about Tented's image gen capabilities where users ask for branded images and see them added to content
```

<details><summary>中文译文</summary>

```text
做一段动画短片，介绍 Tented 的图像生成能力：用户提出想要带品牌的图片，然后看到这些图片被加进内容里
```

</details>

<sub>Inputs: Screenshots · Author: one-shot.</sub>

[Original post ↗](https://x.com/justincooperman/status/2103201167367188876)

---

### Gene Spectra promo using its live site

<a href="https://x.com/madebyjmayala/status/2103578285892649220"><img src="https://pbs.twimg.com/amplify_video_thumb/2103577938033606656/img/lioZSLSj0LGSivw7.jpg" alt="Gene Spectra promo using its live site" width="480"></a>

[@madebyjmayala](https://x.com/madebyjmayala) · 2026-09-25 · ▶ 38 · `One-shot`

A 15-second motion graphics promo for gene spectra, told to reuse assets from the live site; the author says it could not fetch them.

```text
make a dynamic 15-second motion graphics video promo about gene spectra, use assets from the current live site where relevant. go all out.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形宣传视频，主题是 gene spectra，合适的地方使用当前线上网站的素材。拿出全部本事。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/madebyjmayala/status/2103578285892649220)

---

### 15-second ad for a YouTube transcript tool

<a href="https://x.com/tstfully/status/2104033772949680192"><img src="https://pbs.twimg.com/amplify_video_thumb/2104033665021833216/img/KsnvRoQo4OmXK_ru.jpg" alt="15-second ad for a YouTube transcript tool" width="480"></a>

[@tstfully](https://x.com/tstfully) · 2026-09-27 · ▶ 31 · `One-shot`

A 15-second product ad for youtubetranscript.dev, built around its one-line pitch: paste a YouTube video, get every word.

```text
make a 15-second motion graphics product ad: paste a YouTube video, get every word.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形产品广告：贴入一个 YouTube 视频，拿到其中的每一个字。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/tstfully/status/2104033772949680192)

---

### Cartoon JS ad from a script

[@Lucas_IA_](https://x.com/Lucas_IA_) · 2026-09-24 · ▶ 875 · `Template` · HyperFrames · ElevenLabs · Whisper · Suno

A template for cartoon ads drawn in JavaScript; it depends on the author's own Claude Code skill with ElevenLabs voice, Whisper timing and HyperFrames rendering.

```text
Fais-moi une ad au format cartoon JS pour [marque]. Voici le script : [colle ton script]
```

<details><summary>English translation</summary>

```text
Make me an ad in the cartoon JS format for [brand]. Here is the script: [paste your script]
```

</details>

<sub>Inputs: Script, Brand kit</sub>

[Original post ↗](https://x.com/Lucas_IA_/status/2103152108224573507)

---

### Studio-level app ad with a full creative strategy

<a href="https://x.com/redpersongpt/status/2103807094554284430"><img src="https://pbs.twimg.com/amplify_video_thumb/2103800466345771008/img/IOkMTmG0lO7Q2kkX.jpg" alt="Studio-level app ad with a full creative strategy" width="480"></a>

[@redpersongpt](https://x.com/redpersongpt) · 2026-09-26 · ▶ 259 · `Spec`

An ad for the chat-mockup app Mimicly from a ten-phase brief that makes Opus 5.5 inspect the real product first; shown side by side with Astra.

```text
Create a studio level motion design ad for my app mimicly. Show me the best you got.

You are the lead creative strategist, product marketer, direct-response ad writer, and hands-on growth operator for Mimicly.

Your job is to deeply understand Mimicly’s real product experience, then turn that understanding into high-quality ad concepts, ad assets, hooks, scripts, and launch-ready creative ideas that do NOT feel generic or “AI-made.”

IMPORTANT:
- Do not create generic “mockup app” marketing.
- Do not rely on assumptions.
- Base everything on Mimicly’s actual product, actual UI, and actual user flows.
- Use the real product as the source of truth.
- If you can access the website, App Store page, editor, simulator, screenshots, or any current product surfaces, inspect them directly before deciding anything.
- If you can capture screenshots, screen recordings, or UI references from the actual product, do it.
- Do not invent features that do not exist.
- Do not break what currently works.

PRODUCT YOU ARE WORKING ON
Mimicly is a chat mockup maker for screenshots, text stories, and dialogue videos.
It works on web and iPhone.
It offers 63 templates.
Users can edit both sides of conversations, names, profile photos, timestamps, colors, and supported UI details.
It includes chat templates, AI conversation templates, social-style templates, comment templates, stories, email, and game chat styles.
Supported exports include image export, and supported templates can also be recorded as MP4.
Users can sign in and get 3 free exports. Pro unlocks the full template collection and watermark-free exports.
Mimicly’s value is speed, realism, flexibility, and “make it look right” editing.

KNOWN PRODUCT FEEL / BRAND DIRECTION
- Clean, modern, product-led
- Useful, not cringe
- Creative-tool energy, not fake-hype startup nonsense
- Strong on realism and visual believability
- The appeal is: “I can quickly create convincing chat/mockup content for content creation, storytelling, skits, tutorials, memes, product demos, lessons, storyboards, and social posts.”

YOUR MISSION
Create a complete Mimicly ad-creative system based on the real product.

PHASE 1 — PRODUCT UNDERSTANDING
First, inspect and understand:
1. The public website
2. The App Store listing
3. The homepage messaging
4. The template browser / template categories
5. The editor experience
6. Preview behavior
7. Export flow
8. Paywall / free vs pro positioning
9. The visual feel of the app and web product
10. The strongest “wow” moments for first-time users

Pay special attention to:
- Homepage hero
- Template examples
- Live editor behavior
- The “before / after” feeling
- How realistic the previews look
- Which templates are most ad-worthy visually
- Which screens are easiest to understand instantly in an ad

If possible, capture a reference set of real visuals:
- app screenshots
- web screenshots
- editor screenshots
- preview screenshots
- export-related screens
- 5–15 second screen recordings of realistic usage

PHASE 2 — FIND THE BEST MARKETING ANGLES
Based on the real product, identify the strongest ad angles.

Find the best angles for users such as:
- content creators
- meme pages
- storytellers
- short-form video creators
- skit makers
- YouTubers / TikTok creators
- marketers making fake chat visuals for concepts/storyboards
- educators making lesson examples
- people creating “text story” style content
- people making AI conversation mockups
- people making social post mockups

For each angle, define:
- the user type
- the core desire
- the pain point
- why Mimicly solves it better
- the strongest visual proof
- the best CTA

PHASE 3 — CREATE A CREATIVE STRATEGY
Produce a clear creative strategy document containing:
1. Core positioning
2. Top 5 user personas
3. Top 10 ad angles
4. Top 20 hooks
5. Top 10 “visual demo” ideas
6. Top objections and how to answer them
7. Top App Store / landing page conversion messages
8. What NOT to say
9. Which claims need caution or proof
10. Which existing product features deserve the most emphasis

PHASE 4 — BUILD THE AD CONCEPTS
Create at least 12 strong ad concepts.

For each ad concept include:
- concept name
- target audience
- angle
- platform fit (TikTok / Instagram Reels / X / YouTube Shorts / App Store promo / website hero / paid social)
- first 2-second hook
- full ad script
- scene-by-scene shot list
- exact UI moments to show
- on-screen text
- voiceover
- caption
- CTA
- why this concept should perform

At least:
- 4 UGC-style concepts
- 4 product-demo concepts
- 2 comparison-style concepts
- 2 “problem → solution” concepts

PHASE 5 — USE THE REAL PRODUCT VISUALLY
Do not make fake-looking ads.

Use the actual Mimicly experience as much as possible:
- show opening the app / website
- show selecting a template
- show editing messages / names / profile photos / timestamps
- show the preview updating live
- show switching between templates where useful
- show export or save behavior where appropriate
- show the realism of the result

Focus heavily on visual proof.
The ad should make someone think:
“Wait, this actually looks clean.”
“Oh, I could use this.”
“That took like 10 seconds?”

PHASE 6 — PICK THE BEST TEMPLATES TO ADVERTISE
Review Mimicly’s template universe and choose the best templates for marketing.

Rank the most ad-worthy templates by:
- instant recognizability
- visual clarity
- emotional pull
- creator usefulness
- ability to demonstrate value quickly
- likelihood to convert cold traffic

Likely strong candidates may include:
- WhatsApp-style chats
- AI conversation templates (ChatGPT / Claude / Gemini style)
- Instagram / DM / comment / post type templates
- iMessage-style chats
- Discord-style chats
- story / social / dialogue video templates

But do not assume — inspect first.

For the top templates, say:
- why they are ad-worthy
- what kind of audience they attract
- what kind of ad should use them

PHASE 7 — CREATE REAL ASSETS OR ASSET BLUEPRINTS
If your environment allows it, create or organize:
- a shot plan
- a screenshot list
- a screen recording list
- asset naming
- folder structure
- recommended aspect ratios
- prioritized recording checklist

If you cannot directly produce the final ad assets, produce a near-production-ready blueprint so a human editor can build them fast.

Deliverables should include:
- 10 static ad ideas
- 10 short-form video ad ideas
- 5 App Store screenshot angle ideas
- 5 X/Twitter promo post ideas
- 5 landing page hero/message ideas
- 5 product-demo threads/carousels if relevant

PHASE 8 — COPYWRITING
Write launch-ready copy in a way that does not sound like AI slop.

Tone:
- sharp
- natural
- confident
- slightly punchy
- creator-friendly
- not overhyped
- not cringe
- not corporate

Write:
- 20 ad hooks
- 20 CTAs
- 15 captions
- 10 App Store / social proof style lines
- 10 short feature-value lines
- 10 landing page headlines
- 10 subheadlines

Avoid fake urgency unless justified.
Avoid saying it “goes viral.”
Avoid empty words like “revolutionary.”
Avoid generic “create stunning content” filler unless made specific.

PHASE 9 — CONVERSION FOCUS
Recommend which messages should push:
- install
- try free
- first export
- Pro conversion
- template exploration
- creator use cases

Map the best message to the best funnel stage.

Tell me:
- what gets the click
- what gets the install
- what gets the first successful export
- what gets the Pro upgrade

PHASE 10 — FINAL OUTPUT FORMAT
Give the final answer in this structure:

1. Mimicly product understanding
2. Best audiences
3. Best ad angles
4. Best templates to feature
5. 12 ad concepts
6. Shot list / capture plan
7. Copy bank
8. Landing page / App Store messaging suggestions
9. Recommended creative priorities
10. Top 3 things to test first

If possible, end with:
- “Best 3 concepts to make first”
- “Fastest assets to produce tomorrow”
- “Highest-upside experiment”

QUALITY BAR
The output must feel like it came from a strong product marketer who actually inspected the product, not from an LLM guessing what a mockup app might be.

Be specific.
Be practical.
Be visually aware.
Be conversion-aware.
Be ruthless about weak ideas.
Use the real Mimicly product as your source of truth.

Start by inspecting the real product surfaces, then build the strategy.
```

<details><summary>中文译文</summary>

```text
为我的 app mimicly 做一支工作室级别的动效设计广告。把你最好的本事拿出来。

你是 Mimicly 的首席创意策略师、产品营销、直效广告文案，也是亲自上手的增长操盘手。

你的任务是深入理解 Mimicly 真实的产品体验，再把这种理解转化为高质量的广告概念、广告素材、开场钩子、脚本和可以直接上线的创意点子，而且这些内容「不能」显得千篇一律或有「AI 味」。

重要：
- 不要做千篇一律的「mockup app」式营销。
- 不要依赖假设。
- 一切都要基于 Mimicly 的真实产品、真实 UI 和真实用户流程。
- 以真实产品为准。
- 如果你能访问网站、App Store 页面、编辑器、模拟器、截图或任何现有的产品界面，在做任何决定之前先直接查看它们。
- 如果你能从真实产品中截取截图、录屏或 UI 参考，就去做。
- 不要编造不存在的功能。
- 不要破坏目前能正常工作的东西。

你正在负责的产品
Mimicly 是一个聊天界面仿制工具，用来做截图、文字故事和对话视频。
它支持网页端和 iPhone。
它提供 63 个模板。
用户可以编辑对话双方的内容、名字、头像、时间戳、颜色以及支持的 UI 细节。
它包含聊天模板、AI 对话模板、社交平台风格模板、评论模板、快拍（stories）、邮件和游戏聊天样式。
支持导出图片，部分模板还可以录制成 MP4。
用户登录后可获得 3 次免费导出。Pro 版解锁全部模板和无水印导出。
Mimicly 的价值在于速度、逼真、灵活，以及「让它看起来就对」的编辑体验。

已知的产品感觉 / 品牌方向
- 干净、现代、以产品为主导
- 实用，不尴尬
- 创作工具的气质，而不是虚假炒作的创业公司套话
- 逼真度和视觉可信度很强
- 吸引力在于：「我可以快速做出以假乱真的聊天/仿制内容，用于内容创作、讲故事、短剧、教程、梗图、产品演示、课程、分镜和社交帖子。」

你的使命
基于真实产品，打造一套完整的 Mimicly 广告创意体系。

第 1 阶段 —— 理解产品
首先，查看并理解：
1. 公开网站
2. App Store 页面
3. 首页文案
4. 模板浏览器 / 模板分类
5. 编辑器体验
6. 预览表现
7. 导出流程
8. 付费墙 / 免费版与 Pro 版的定位
9. App 和网页产品的视觉感受
10. 首次使用者最强的「哇」时刻

特别注意：
- 首页首屏
- 模板示例
- 编辑器的实时表现
- 「前 / 后」对比的感觉
- 预览看起来有多逼真
- 哪些模板在视觉上最适合做广告
- 哪些界面在广告里最容易一眼看懂

如果可以，采集一套真实视觉参考：
- app 截图
- 网页截图
- 编辑器截图
- 预览截图
- 与导出相关的界面
- 5–15 秒的真实使用录屏

第 2 阶段 —— 找到最佳营销角度
基于真实产品，找出最有力的广告角度。

为以下这些用户找到最佳角度：
- 内容创作者
- 梗图账号
- 讲故事的人
- 短视频创作者
- 短剧创作者
- YouTuber / TikTok 创作者
- 为概念稿/分镜制作仿真聊天画面的营销人员
- 制作课程示例的教育者
- 制作「文字故事」类内容的人
- 制作 AI 对话仿真图的人
- 制作社交帖子仿真图的人

对每个角度，明确：
- 用户类型
- 核心诉求
- 痛点
- 为什么 Mimicly 解决得更好
- 最有力的视觉证明
- 最佳 CTA

第 3 阶段 —— 制定创意策略
产出一份清晰的创意策略文档，包含：
1. 核心定位
2. 前 5 个用户画像
3. 前 10 个广告角度
4. 前 20 个开场钩子
5. 前 10 个「视觉演示」点子
6. 主要顾虑以及如何回应
7. 最重要的 App Store / 落地页转化文案
8. 哪些话「不要」说
9. 哪些说法需要谨慎或需要证据
10. 哪些现有产品功能最值得强调

第 4 阶段 —— 构建广告概念
创作至少 12 个有力的广告概念。

每个广告概念包含：
- 概念名称
- 目标受众
- 角度
- 适合的平台（TikTok / Instagram Reels / X / YouTube Shorts / App Store 推广 / 网站首屏 / 付费社交广告）
- 前 2 秒的钩子
- 完整广告脚本
- 逐场景镜头清单
- 需要展示的具体 UI 时刻
- 屏幕文字
- 旁白
- 配文
- CTA
- 这个概念为什么会有效

至少包括：
- 4 个 UGC 风格概念
- 4 个产品演示概念
- 2 个对比风格概念
- 2 个「问题 → 解决方案」概念

第 5 阶段 —— 在视觉上使用真实产品
不要做看起来很假的广告。

尽可能使用真实的 Mimicly 体验：
- 展示打开 app / 网站
- 展示选择模板
- 展示编辑消息 / 名字 / 头像 / 时间戳
- 展示预览实时更新
- 在有用的地方展示模板之间的切换
- 在合适的地方展示导出或保存
- 展示成品的逼真度

重点放在视觉证明上。
广告应该让人心里想：
「等等，这看起来真的很干净。」
「哦，我用得上这个。」
「这就花了 10 秒？」

第 6 阶段 —— 挑出最适合做广告的模板
审视 Mimicly 的全部模板，选出最适合营销的模板。

按以下维度给最适合做广告的模板排名：
- 一眼可辨识度
- 视觉清晰度
- 情绪吸引力
- 对创作者的实用性
- 快速展示价值的能力
- 转化冷流量的可能性

可能的强力候选包括：
- WhatsApp 风格聊天
- AI 对话模板（ChatGPT / Claude / Gemini 风格）
- Instagram / 私信 / 评论 / 帖子类模板
- iMessage 风格聊天
- Discord 风格聊天
- 故事 / 社交 / 对话视频模板

但不要假设——先查看。

对排名靠前的模板，说明：
- 为什么适合做广告
- 会吸引什么样的受众
- 什么样的广告应该用它们

第 7 阶段 —— 制作真实素材或素材蓝图
如果你的环境允许，制作或整理：
- 拍摄计划
- 截图清单
- 录屏清单
- 素材命名
- 文件夹结构
- 推荐的画面比例
- 按优先级排列的录制清单

如果你无法直接产出最终的广告素材，就产出一份接近可直接制作的蓝图，让人类剪辑师能快速做出来。

交付物应包括：
- 10 个静态广告点子
- 10 个短视频广告点子
- 5 个 App Store 截图角度点子
- 5 个 X/Twitter 推广帖点子
- 5 个落地页首屏/文案点子
- 如果相关，5 个产品演示推文串/轮播

第 8 阶段 —— 文案
写出可以直接上线、听起来不像 AI 垃圾内容的文案。

语气：
- 犀利
- 自然
- 自信
- 略带冲击力
- 对创作者友好
- 不过度吹嘘
- 不尴尬
- 不官腔

写：
- 20 个广告钩子
- 20 个 CTA
- 15 条配文
- 10 条 App Store / 社会认同风格的文案
- 10 条简短的功能价值文案
- 10 个落地页主标题
- 10 个副标题

除非有正当理由，否则避免制造虚假的紧迫感。
避免说它「会爆火」。
避免使用「革命性」这类空话。
避免「创作惊艳内容」这类泛泛的填充语，除非说得具体。

第 9 阶段 —— 聚焦转化
建议哪些文案应该用来推动：
- 安装
- 免费试用
- 首次导出
- 转化为 Pro
- 探索模板
- 创作者使用场景

把最佳文案对应到最合适的漏斗阶段。

告诉我：
- 什么能带来点击
- 什么能带来安装
- 什么能带来第一次成功导出
- 什么能带来 Pro 升级

第 10 阶段 —— 最终输出格式
按以下结构给出最终答案：

1. 对 Mimicly 产品的理解
2. 最佳受众
3. 最佳广告角度
4. 最值得展示的模板
5. 12 个广告概念
6. 镜头清单 / 采集计划
7. 文案库
8. 落地页 / App Store 文案建议
9. 推荐的创意优先级
10. 最先要测试的 3 件事

如果可以，结尾加上：
- 「最先要做的 3 个概念」
- 「明天最快能产出的素材」
- 「上限最高的实验」

质量标准
输出必须像是出自一位真正查看过产品的优秀产品营销之手，而不是一个在猜 mockup app 大概是什么样的 LLM。

要具体。
要务实。
要有视觉意识。
要有转化意识。
对弱点子要毫不留情。
以真实的 Mimicly 产品为准。

先查看真实的产品界面，再制定策略。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/redpersongpt/status/2103807094554284430) · Prompt posted in [this reply](https://x.com/redpersongpt/status/2103807204931346864).

---

### Interactive HyperFrames event teaser template

[@Bob_zaimu](https://x.com/Bob_zaimu) · 2026-09-27 · ▶ 178 · `Template` · HyperFrames

A reusable Japanese template for a 30-second 1920×1080 event teaser in HyperFrames: interview first, storyboard and music picks for approval, then render.

```text
あなたは告知動画のディレクターです。HyperFrames（npx hyperframes）で、30秒・1920×1080・ナレーションなしの告知動画を、私と会話しながら作ってください。

■進め方
1. まず私に1つずつ質問して内容を集める（何の告知か／伝えたい一言／タイトル／日時（年も）／参加方法と申込み先／登壇者／特典／ロゴ（透過PNG推奨）／伏せたいこと）。分からないことは作らずに聞く。
2. そろったら10場面前後の絵コンテ（storyboard.html）を作ってファイルリンクで見せ、OpenTracks（http://opentracks.com）から「かっこいい・盛り上がる」BGM候補を3曲、試聴リンク付きで出す。私がOKするまで制作しない。
3. OK後に制作。BGMの一番盛り上がる頭を「問い」の場面に合わせ、切り替えを拍にそろえる。BGMは背景でうっすら。lint・checkを通し、コマ一覧を自分の目で確かめてから書き出す。
4. 完成MP4と、完成画面入りの絵コンテをリンクで渡す。BGMの山が合っているか、耳での確認を私に頼む。

■デザイン（毎回これで）
・濃紺 #0B1024 の背景に、紙色 #F2EFE8 の場面を2つ挟む
・ゴールド #FFC940＝望ましい側・日付／マゼンタ #E0367F＝否定／シアン #5CE1E6＝全編を通る1本の線（仕切り→下線→打ち消し線→最後の枠）
・見出し Noto Sans JP 900（使う文字だけ埋め込む）、数字 Archivo Black、ラベル JetBrains Mono、英字の差し色 Instrument Serif Italic
・四隅にトンボ・場面番号・タイムコード・日時、下端に進行バー
・演出：1語ずつ組み上げて大きくドン／左右の対比とvs／デザインツール風の選択枠／集中線で問い／打ち消し線／数字のカウント（中身は「？」で伏せる）／マーカー線／タイトルは長めに静止／斜めの帯と紙吹雪／最後に日付ドン
・流れ：断言→対立→問い→通説の否定→答えの予告（伏せる）→タイトル→登壇者と参加方法→特典→日付

■約束
答えは言いすぎず、当日への期待で終える。写真・ロゴは私が渡したものだけ使う。BGM・効果音のダウンロードは私が選んでから。投稿は私がする。
```

<details><summary>English translation</summary>

```text
You are the director of an announcement video. Using HyperFrames (npx hyperframes), make a 30-second, 1920×1080 announcement video with no narration, while talking it through with me.

■How we work
1. First, ask me questions one at a time to gather the content (what is being announced / the one line I want to get across / title / date and time (including the year) / how to join and where to sign up / speakers / perks / logo (transparent PNG recommended) / anything to keep hidden). If you don't know something, ask instead of making it up.
2. Once everything is in, make a storyboard of about 10 scenes (storyboard.html) and show it to me as a file link, and give me 3 BGM candidates from OpenTracks (http://opentracks.com) that feel "cool and hype", with preview links. Don't start production until I say OK.
3. After my OK, produce it. Line up the start of the BGM's biggest build-up with the "question" scene, and align the cuts to the beat. Keep the BGM faint in the background. Pass lint and check, and look through the frame list with your own eyes before exporting.
4. Give me the finished MP4 and the storyboard with the finished frames as links. Ask me to check by ear whether the BGM's peak lines up.

■Design (use this every time)
・Dark navy #0B1024 background, with two paper-colored #F2EFE8 scenes in between
・Gold #FFC940 = the desirable side and dates / magenta #E0367F = negation / cyan #5CE1E6 = one line running through the whole video (divider → underline → strikethrough → final frame)
・Headings in Noto Sans JP 900 (embed only the characters used), numbers in Archivo Black, labels in JetBrains Mono, English accent words in Instrument Serif Italic
・Crop marks, scene number, timecode and date/time in the four corners; a progress bar along the bottom edge
・Effects: build it up one word at a time, then slam it in big / left-right contrast and vs / a design-tool-style selection box / the question with speed lines / strikethrough / number count-up (contents hidden as "?") / marker lines / hold the title a little longer / diagonal bands and confetti / slam the date in at the end
・Flow: assertion → conflict → question → debunking the common belief → teaser of the answer (kept hidden) → title → speakers and how to join → perks → date

■Promises
Don't give away too much of the answer; end on anticipation for the day. Use only the photos and logo I provide. Download BGM and sound effects only after I choose them. I will do the posting.
```

</details>

<sub>Inputs: Logo, Images</sub>

[Original post ↗](https://x.com/Bob_zaimu/status/2104081236881006606)

---

### Launch video for the ocrX Android app

<a href="https://x.com/mehul4795/status/2103420457110417532"><img src="https://pbs.twimg.com/amplify_video_thumb/2103420376630132736/img/HmZLhJPxoV_ngU6k.jpg" alt="Launch video for the ocrX Android app" width="480"></a>

[@mehul4795](https://x.com/mehul4795) · 2026-09-25 · ▶ 134 · `One-shot`

A 33-second vertical launch video for the ocrX Android app, from a one-line prompt.

```text
Create a product launch video for ocrX Android app.
```

<details><summary>中文译文</summary>

```text
为 ocrX 安卓应用做一支产品发布视频。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/mehul4795/status/2103420457110417532)

---

### 30-second promo video for bklink

<a href="https://x.com/PalashBagchi11/status/2102924409124389221"><img src="https://pbs.twimg.com/amplify_video_thumb/2102924270045401088/img/3S2WW6qdpC6jBoha.jpg" alt="30-second promo video for bklink" width="480"></a>

[@PalashBagchi11](https://x.com/PalashBagchi11) · 2026-09-24 · ▶ 103 · `One-shot`

A 30-second product promo from one line; a follow-up prompt added royalty-free music and cut landscape and portrait versions.

```text
make a 30 sec modern slick and punchy video for bklink
```

<details><summary>中文译文</summary>

```text
为 bklink 做一支 30 秒的现代、利落、有冲击力的视频
```

</details>

[Original post ↗](https://x.com/PalashBagchi11/status/2102924409124389221) · Prompt posted in [this reply](https://x.com/PalashBagchi11/status/2102915673794248947).

---

### Project feature reel from the showreel prompt

<a href="https://x.com/paukraft/status/2103766223133585863"><img src="https://pbs.twimg.com/amplify_video_thumb/2103765130295021568/img/h8hlvD5GHe0PZRuA.jpg" alt="Project feature reel from the showreel prompt" width="480"></a>

[@paukraft](https://x.com/paukraft) · 2026-09-26 · ▶ 101 · `One-shot`

A 106-second promo of the author's project and its features, adapted from the résumé showreel prompt and refined with follow-up prompts.

```text
make a dynamic motion graphics video about this project and its unique features that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

<details><summary>中文译文</summary>

```text
制作一段关于这个项目及其独特功能的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。
```

</details>

<sub>Inputs: Brand kit · Author: not a one-shot; adjusted afterward through several follow-up prompts.</sub>

[Original post ↗](https://x.com/paukraft/status/2103766223133585863) · Prompt posted in [this reply](https://x.com/paukraft/status/2103766225775915138).

---

### Social promo for a betting odds site

<a href="https://x.com/Victorrayy/status/2103229525236842802"><img src="https://pbs.twimg.com/amplify_video_thumb/2103229484862476288/img/hyb2a0NUWtU9q7T0.jpg" alt="Social promo for a betting odds site" width="480"></a>

[@Victorrayy](https://x.com/Victorrayy) · 2026-09-24 · ▶ 89 · `One-shot`

A 24-second social promo for a site that finds positive-EV bets, made from just the URL without any screen recording supplied.

```text
can you generate a promo video for socials for http://oddsightseer.com? ensure to highlight the look and feel of the site premiumness and how it is to find positive ev bets
```

<details><summary>中文译文</summary>

```text
能帮 http://oddsightseer.com 做一支发社交媒体的宣传视频吗？一定要突出网站的视觉质感和高级感，以及在上面找正 EV 投注是什么感觉
```

</details>

<sub>Inputs: Brand kit · Author: one prompt.</sub>

[Original post ↗](https://x.com/Victorrayy/status/2103229525236842802) · Prompt posted in [this reply](https://x.com/Victorrayy/status/2103232490291020159).

---

### Hand-drawn collage animation of an About page

<a href="https://x.com/TomAndrieu96707/status/2103411144899875264"><img src="https://pbs.twimg.com/amplify_video_thumb/2103410538109657088/img/7BIvM6cMaWdjVLUr.jpg" alt="Hand-drawn collage animation of an About page" width="480"></a>

[@TomAndrieu96707](https://x.com/TomAndrieu96707) · 2026-09-25 · ▶ 80 · `One-shot`

A 52-second whimsical hand-drawn collage animation in pure JavaScript, with audio, retelling a company's About page story using assets from its repo.

```text
Create a pure javascript animation. 30s-60s whimsical hand drawn collage style with appropriate audio that will explain the same story as our “about-us” page. Use assets from our repo when possible.
```

<details><summary>中文译文</summary>

```text
做一段纯 JavaScript 动画。30 到 60 秒，异想天开的手绘拼贴风格，配上合适的音频，讲出和我们“about-us”页面一样的故事。尽量使用我们仓库里的素材。
```

</details>

<sub>Inputs: Brand kit · Effort: medium</sub>

[Original post ↗](https://x.com/TomAndrieu96707/status/2103411144899875264) · Prompt posted in [this reply](https://x.com/TomAndrieu96707/status/2103411148842283295).

---

### Low-poly shard logo reveal

<a href="https://x.com/Mounnna/status/2103802871934497266"><img src="https://pbs.twimg.com/amplify_video_thumb/2103802493985808384/img/F_h8mEY82oXmLOFU.jpg" alt="Low-poly shard logo reveal" width="480"></a>

[@Mounnna](https://x.com/Mounnna) · 2026-09-26 · ▶ 64 · `Brief`

A 16-second logo reveal: the logo is drawn as a wireframe, low-poly shards fly in one by one to fill it, then the brand name types out.

```text
Create a motion design video of a slow-reveal transition. Draw the logo as a wireframe first, then fly in faceted low-poly shards one by one until they assemble the logo. Finish by bringing in the app icon background and typing out the brand name.
```

<details><summary>中文译文</summary>

```text
制作一段慢速揭示转场的动效视频。先把 logo 画成线框，然后让多面体的低多边形碎片一片片飞入，直到拼成 logo。最后引入 app 图标背景，并逐字打出品牌名。
```

</details>

<sub>Inputs: Logo</sub>

[Original post ↗](https://x.com/Mounnna/status/2103802871934497266) · Prompt posted in [this reply](https://x.com/Mounnna/status/2103802998204023030).

---

### Apple-keynote launch film in one take

<a href="https://x.com/thejohnnyhuy/status/2104149058562506887"><img src="https://pbs.twimg.com/amplify_video_thumb/2104106386166812672/img/1tUQULvPIUI0K3WW.jpg" alt="Apple-keynote launch film in one take" width="480"></a>

[@thejohnnyhuy](https://x.com/thejohnnyhuy) · 2026-09-27 · ▶ 55 · `Spec` · Playwright · ffmpeg · SVG · Canvas

A 27-second Apple-keynote-style launch film in one continuous take: liquid glass, iris blades and goo morphs over 54 beats at 120 BPM, rendered at 60fps.

```text
Build an Apple-keynote launch film as a single HTML file, then render it to MP4.

<inputs>
Ask me for: a one-word brand name for the wordmark (a verb works best), 9 to 12 high-res photos, a royalty-free song around 120 BPM with a drop and a quiet breakdown (Mixkit, free for commercial use), and a free stock clip of a plain wall with moving plant shadows (Pexels). If I don't supply them, source them yourself and tell me what you picked.
</inputs>

<direction>
An Apple-keynote launch film, 2D only, one continuous take. Every scene is made out of the previous one: nothing fades, blurs or cuts. Objects change shape instead: text rises out of a mask line, icons pop from zero on a spring, bars draw across, pages push, and a black shape floods the whole frame and contracts into the next scene. Warm off-white canvas, black UI, iOS 26 liquid glass over the photos. Archivo (wdth 125, weight 800) for the wordmark, Geist for UI. A cursor drives every change with real clicks, drags and long-presses. The camera zooms screen-studio style so each moment fills the square, and the cursor scales with it.
Banned: crossfades, blur-ins, brightness "developing", 3D flips, particles, glows, holds longer than 1s, anything that looks like a template.
</direction>

<structure>
120 BPM, 54 beats, something happens on every beat.
Open: the wordmark squeezes into its own period like an accordion, the dot grows into a black pill, a label rises inside it. Click: six iris blades close over the label and snap open onto a photo. The circle becomes a square, shrinks, the grid unfolds from behind it like a paper map (center, plus, corners), reflows into a bento, and a click zooms into one tile, landing exactly on the drop.
Glass: a glass word pops in letter by letter, melts into a droplet that stretches into a glass toolbar. The adjust icon turns it into a slider. Dragging relights the photo from day to golden hour (two aligned shots), and the knob turns into a glass lens while held. It lifts into a glass orb, the next photo opens inside it as a circle, and the orb expands into a lock screen: glass clock digits, date, and a home bar that stretches into a glass music player.
Stage: the lock screen pulls back into a phone (the bezel grows out of the screen edge). The Dynamic Island stretches like liquid, pinches off, flies over and grows into a Mac window that rolls up like a blind. Long-press the wallpaper, drag it onto a Safari tab, the page pushes in, drop it and it becomes the hero of a landing page. Scroll: the hero morphs into a framed print on a product card, with the mat and molding growing out of the photo's edge. Pick a frame color (it paints across) and a size, then the nav button flies down into "Order print".
Order: one black shape keeps morphing: Ordered ✓ → Printing % → On its way (a van on a route) → Delivered ✓.
Wall: the delivered circle floods the frame edge to edge, holds black for a beat, and contracts into the framed print hanging on the real wall footage. The same iris opens onto the print, closes again, the frame floods the screen and contracts into the pill → the dot → the letters spring back out, landing on the beat return. Last frame = first frame.
</structure>

<build>
1. One HTML file, square 1440x1440. Every style is computed from time inside an async seek(t): no CSS transitions, no timers, no state between frames.
2. Springs are closed-form step responses. A value with many targets is the sum of one spring per change, so it stays a pure function of time.
3. Liquid glass: each glass element holds its own clone of the scene behind it, filtered with an SVG feImage displacement map (a rounded-rect distance field) through three feDisplacementMaps at slightly different scales for chromatic edges, plus a rim light. Glass letters: a canvas distance field per glyph gives the map, mask and highlights.
4. Goo: blur + alpha threshold, then composite the source atop it so the glass stays sharp inside.
5. Iris: 6 blades around a hexagonal aperture. Each blade is its two vertices, both edge extensions and the SHORT arc between them.
6. Wordmark squeeze: every letter moves toward the dot by the same factor and its drawn width follows (narrow the wdth axis, scale the rest), so the letters stay touching.
7. Footage: re-encode all-intra (ffmpeg -g 1), load it as a blob URL, await 'seeked' before drawing each frame.
8. Sound: a downloaded SFX for every event (Mixkit), never synthesized, each placed by its measured peak. The song starts on a downbeat: the zoom lands on the drop, the wall sits in the breakdown, the wordmark returns with the beat. Loudnorm to -14 LUFS.
9. Render with Playwright: 4 subframes per frame blended with ffmpeg tmix, 60fps. Check one frame per beat, then scan for single-frame pops (frame-difference spikes 3x their neighbours).
</build>

<gotchas>
backdrop-filter: url() misreads displacement maps in Chromium, so clone the scene instead. A flood must overscale past the corners and take about 0.3s, or half the screen changes in one frame. A child with visibility: visible shows through a hidden parent, so use inherit. Text that swaps inside a morphing shape needs its own mask. python http.server can't range-seek video, so use the blob URL. Build canvas glyphs only after the webfont has loaded, or they silently render in a fallback serif.
</gotchas>

<start>
Ask me for the inputs, then show me the beat map and 4 stills (open, glass, stage, wall) before you write the full film.
</start>
```

<details><summary>中文译文</summary>

```text
用单个 HTML 文件做一支苹果发布会风格的发布影片，然后渲染成 MP4。

<inputs>
向我要这些东西：一个用作文字标志的单词品牌名（动词效果最好）、9 到 12 张高清照片、一首约 120 BPM、带 drop 和安静 breakdown 的免版税歌曲（Mixkit，可免费商用），以及一段素色墙面上有植物阴影晃动的免费素材片段（Pexels）。如果我没提供，就自己去找，并告诉我你选了什么。
</inputs>

<direction>
一支苹果发布会风格的发布影片，只用 2D，一镜到底。每个场景都由上一个场景变化而来：没有淡入淡出、没有模糊、没有剪切。物体改为变形：文字从遮罩线里升起，图标带弹簧从零弹出，条形横向画出，页面推入，一个黑色形状淹没整个画面，再收缩成下一个场景。暖白色画布、黑色 UI，照片上覆盖 iOS 26 液态玻璃。文字标志用 Archivo（wdth 125，weight 800），UI 用 Geist。由一个光标通过真实的点击、拖拽和长按驱动每一次变化。镜头以 screen-studio 的方式缩放，让每个瞬间填满方形画面，光标随之缩放。
禁止：交叉淡化、模糊渐入、亮度「显影」、3D 翻转、粒子、辉光、停留超过 1s、任何看起来像模板的东西。
</direction>

<structure>
120 BPM，54 拍，每一拍都有事情发生。
开场：文字标志像手风琴一样挤进它自己的句点，句点长成一个黑色胶囊，胶囊里升起一个标签。点击：六片光圈叶片在标签上合拢，再啪地张开，露出一张照片。圆形变成方形并缩小，网格像纸质地图一样从它后面展开（中心、十字、四角），重排成 bento 布局，一次点击放大进其中一格，正好落在 drop 上。
玻璃：一个玻璃质感的单词逐字母弹出，融化成一滴水珠，再拉伸成一条玻璃工具栏。调节图标把它变成一个滑块。拖动滑块让照片的光线从白天变成黄金时刻（两张对齐的照片），按住时旋钮变成一枚玻璃透镜。它升起成一颗玻璃球，下一张照片以圆形在球内打开，玻璃球再扩展成锁屏：玻璃质感的时钟数字、日期，以及一条拉伸成玻璃音乐播放器的 home 条。
舞台：锁屏后拉成一部手机（边框从屏幕边缘长出来）。灵动岛像液体一样拉伸、断开、飞过去，长成一个像百叶帘一样卷起的 Mac 窗口。长按壁纸，拖到一个 Safari 标签页上，页面推入，松手后它成为落地页的首屏大图。滚动：首屏大图变形成商品卡片上的一幅装裱画，卡纸和画框线条从照片边缘长出来。选一个画框颜色（颜色横扫涂满）和尺寸，然后导航按钮飞下来变成 "Order print"。
订单：一个黑色形状持续变形：Ordered ✓ → Printing % → On its way（一辆货车在路线上）→ Delivered ✓。
墙面：送达的圆形从边到边淹没画面，黑屏保持一拍，然后收缩成挂在真实墙面素材上的那幅装裱画。同样的光圈在画上打开，再次合上，画框淹没屏幕并收缩成胶囊 → 句点 → 字母弹回原位，正好落在节拍回归处。最后一帧 = 第一帧。
</structure>

<build>
1. 一个 HTML 文件，方形 1440x1440。所有样式都在 async seek(t) 内根据时间计算：不用 CSS transitions，不用计时器，帧与帧之间不保留状态。
2. 弹簧用闭式阶跃响应。有多个目标值的变量是每次变化各一个弹簧的叠加，这样它始终是时间的纯函数。
3. 液态玻璃：每个玻璃元素持有它背后场景的一份克隆，用 SVG feImage 位移贴图（一个圆角矩形距离场）过滤，经过三个缩放略有不同的 feDisplacementMap 形成色散边缘，再加一道边缘光。玻璃字母：每个字形用一个 canvas 距离场生成位移贴图、遮罩和高光。
4. 融球（goo）：模糊 + alpha 阈值，然后把原图合成在上面，让玻璃内部保持清晰。
5. 光圈：6 片叶片围绕一个六边形光孔。每片叶片由它的两个顶点、两条边的延长线以及它们之间的「短」弧构成。
6. 文字标志挤压：每个字母都按相同比例向句点移动，绘制宽度随之变化（收窄 wdth 轴，其余部分缩放），让字母始终紧贴。
7. 视频素材：重新编码成全帧内编码（ffmpeg -g 1），以 blob URL 加载，绘制每一帧前先 await 'seeked'。
8. 声音：每个事件都配一个下载来的音效（Mixkit），绝不合成，每个音效按实测峰值对位。歌曲从强拍开始：放大落在 drop 上，墙面段落在 breakdown 里，文字标志随节拍回归。用 loudnorm 标准化到 -14 LUFS。
9. 用 Playwright 渲染：每帧 4 个子帧，用 ffmpeg tmix 混合，60fps。每拍检查一帧，再扫描单帧跳变（帧差是相邻帧 3 倍的尖峰）。
</build>

<gotchas>
在 Chromium 里 backdrop-filter: url() 会读错位移贴图，所以改为克隆场景。淹没效果必须放大到超出四角，并持续约 0.3s，否则半个屏幕会在一帧内突变。设置了 visibility: visible 的子元素会穿透隐藏的父元素显示出来，所以要用 inherit。在变形形状内部切换的文字需要自己的遮罩。python http.server 无法按范围跳转视频，所以用 blob URL。等网页字体加载完再构建 canvas 字形，否则它们会悄悄用备用衬线字体渲染。
</gotchas>

<start>
先向我要素材，然后在写完整影片之前，给我看节拍图和 4 张静帧（open、glass、stage、wall）。
</start>
```

</details>

<sub>Inputs: Brand kit, Images, Music, Footage</sub>

[Original post ↗](https://x.com/thejohnnyhuy/status/2104149058562506887) · Prompt posted in [this reply](https://x.com/thejohnnyhuy/status/2104149060588282154).

---

### App promo from a Turkish prompt

<a href="https://x.com/cansincengiz_me/status/2103532681774424245"><img src="https://pbs.twimg.com/amplify_video_thumb/2103531878984675328/img/YjdaDNWipO2oGLJZ.jpg" alt="App promo from a Turkish prompt" width="480"></a>

[@cansincengiz_me](https://x.com/cansincengiz_me) · 2026-09-25 · ▶ 43 · `One-shot`

A 15-second square promo for lidlezz.app, from a Turkish prompt run inside the project folder with Claude Code on xhigh effort.

```text
merak ediyorum ne kadar iyi bir hareketli grafik tasarımcısısın. Bunu bana kanıtlamak için 15 saniye sürecek bir hareketli grafik videosu istiyorum senden. Bu video http://lidlezz.app 'i tanıtacak ve x üzerinde 10.000 kişinin karşısına çıkacak. Elinden geleni yap
```

<details><summary>English translation</summary>

```text
I wonder how good a motion graphics designer you are. To prove it to me, I want a 15-second motion graphics video from you. This video will introduce http://lidlezz.app and will be seen by 10,000 people on X. Do your best
```

</details>

<sub>Inputs: Brand kit · Effort: xhigh</sub>

[Original post ↗](https://x.com/cansincengiz_me/status/2103532681774424245)

---

### Retro-futuristic Opus 5.5 launch video

<a href="https://x.com/johnsavage_ai/status/2103792769982427263"><img src="https://pbs.twimg.com/amplify_video_thumb/2103792270361149441/img/iIhoOmjlD8QVKzI-.jpg" alt="Retro-futuristic Opus 5.5 launch video" width="480"></a>

[@johnsavage_ai](https://x.com/johnsavage_ai) · 2026-09-26 · ▶ 450 · `Brief`

A 20-second 16:9 launch video for Opus 5.5 with film grain and a CRT effect, styled after a single reference image.

```text
use this image only as a style/vibe refference image and create a Opus 5.5 launch video (20 sec long) add film grain and CRT effect, make it mesmerizing, and show off your skills as a motion designer for a retro/futuristic style launch video 16:9
```

<details><summary>中文译文</summary>

```text
这张图只作为风格/氛围参考图，制作一个 Opus 5.5 发布视频（20 秒长），加上胶片颗粒和 CRT 效果，要让人看得入迷，用一支复古/未来风格的发布视频展示你作为动效设计师的本事，16:9
```

</details>

<sub>Inputs: Images</sub>

[Original post ↗](https://x.com/johnsavage_ai/status/2103792769982427263) · Prompt posted in [this reply](https://x.com/johnsavage_ai/status/2103792945287876726).

---

### GLEA logo animation with elastic easing

<a href="https://x.com/mr_igor_sanz/status/2104000986981486650"><img src="https://pbs.twimg.com/amplify_video_thumb/2104000208937865216/img/PKXcEz4gp69iw6uP.jpg" alt="GLEA logo animation with elastic easing" width="480"></a>

[@mr_igor_sanz](https://x.com/mr_igor_sanz) · 2026-09-27 · ▶ 325 · `One-shot`

An 8-second logo animation for GLEA built from shapes, morphing and elastic easing, made entirely in Claude without a style reference.

```text
build me good logo animation with GLEA, use cool motion, shapes, morphing, and elastic easing.
```

<details><summary>中文译文</summary>

```text
给我做一个好看的 GLEA logo 动画，用上酷炫的运动、形状、变形和弹性缓动。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/mr_igor_sanz/status/2104000986981486650)

---

### Fill-in product showreel template

<a href="https://x.com/Ishaaqahamed/status/2103837917538107563"><img src="https://pbs.twimg.com/amplify_video_thumb/2103836980421541889/img/TrBlah-i9TXKeWuC.jpg" alt="Fill-in product showreel template" width="480"></a>

[@Ishaaqahamed](https://x.com/Ishaaqahamed) · 2026-09-26 · ▶ 254 · `Template`

A reusable prompt for a square 15-second product showreel with a one-second hook and a seamless loop; fill in the product and what it does.

```text
Make a dynamic 15-second motion graphics video that shows why [your product] is the best at [what it does], like a showreel. Go all out: 1080×1080, 1s hook, loop.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，像作品集一样展示为什么 [你的产品] 在 [它做的事] 上是最好的。拿出全部本事：1080×1080，1s 开场钩子，循环播放。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/Ishaaqahamed/status/2103837917538107563) · Prompt posted in [this reply](https://x.com/Ishaaqahamed/status/2103837920310493598).

---

### Pitch video for an Amazon wholesale company

<a href="https://x.com/ceowinkz/status/2103647124126683602"><img src="https://pbs.twimg.com/amplify_video_thumb/2103646927636037632/img/gPvO5dVjos1EeW0_.jpg" alt="Pitch video for an Amazon wholesale company" width="480"></a>

[@ceowinkz](https://x.com/ceowinkz) · 2026-09-26 · ▶ 157 · `One-shot`

A 15-second motion graphics pitch for an Amazon wholesale seller, made to show brands why they should let the company sell their products.

```text
make a dynamic 15 second motion graphics video pitching my Amazon wholesale company, Winkz Enterprises, to a brand. show why they should let us sell their products. go all out.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，向一个品牌推介我的亚马逊批发公司 Winkz Enterprises。说明他们为什么应该让我们卖他们的产品。拿出全部本事。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/ceowinkz/status/2103647124126683602)

---

### DataGran product walkthrough video

<a href="https://x.com/charlesmendez/status/2102847039415476517"><img src="https://pbs.twimg.com/amplify_video_thumb/2102846646199484416/img/Lqpr3tLZjGObH9ts.jpg" alt="DataGran product walkthrough video" width="480"></a>

[@charlesmendez](https://x.com/charlesmendez) · 2026-09-23 · ▶ 117 · `One-shot`

A 57-second product walkthrough video for DataGran, following a user from a ChatGPT ads campaign through attribution and a voice agent to analytics.

```text
I Want you to make a modern slick and punchy video for http://datagran.io with an example of a user creating a chatgpt ads campaign, then connecting their metrics, understanding attribution, then connecting a voice agent to it, the agent responding, then doing follow up, adding humans in the loop and then providing analytics.
```

<details><summary>中文译文</summary>

```text
我想让你为 http://datagran.io 做一段现代、利落、有冲击力的视频，用一个用户的例子来演示：创建一个 chatgpt 广告活动，然后接入各项指标，理解归因，再接上一个语音智能体，智能体做出回应，接着进行跟进，加入人工介入环节，最后给出数据分析。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/charlesmendez/status/2102847039415476517)

---

### 15-second website promo, all out

<a href="https://x.com/robvjourney/status/2103768390322237474"><img src="https://pbs.twimg.com/amplify_video_thumb/2103768056245665792/img/N1H6l3pXOn3pdp4A.jpg" alt="15-second website promo, all out" width="480"></a>

[@robvjourney](https://x.com/robvjourney) · 2026-09-26 · ▶ 79 · `One-shot`

A 15-second motion graphic for a studio's website, made from its URL and an instruction to use every trick available.

```text
Can you make a 15-second motion graphic video of https://nohandslabs.com? Go ALL OUT and make the most badass video you possibly can use everything you've got.
```

<details><summary>中文译文</summary>

```text
你能为 https://nohandslabs.com 做一段 15 秒的动态图形视频吗？拿出全部本事，做出你能做到的最酷的视频，用上你的一切。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/robvjourney/status/2103768390322237474)

---

### 30-second Remotion presentation for Brieform

<a href="https://x.com/MajorBaguette/status/2103849602826834228"><img src="https://pbs.twimg.com/amplify_video_thumb/2103849527526522880/img/vh7v9A4s4J6qMQ1T.jpg" alt="30-second Remotion presentation for Brieform" width="480"></a>

[@MajorBaguette](https://x.com/MajorBaguette) · 2026-09-26 · ▶ 75 · `One-shot` · Remotion

A 30-second product presentation video for Brieform, made with Remotion from a one-line prompt.

```text
make a presentation video for Brieform, 30 seconds long
```

<details><summary>中文译文</summary>

```text
为 Brieform 做一个介绍视频，30 秒长
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/MajorBaguette/status/2103849602826834228)

---

### App launch reel with French on-screen text

<a href="https://x.com/hugon001/status/2103425679618609629"><img src="https://pbs.twimg.com/amplify_video_thumb/2103425625906163712/img/WbCLzJu3HBZ5FmKl.jpg" alt="App launch reel with French on-screen text" width="480"></a>

[@hugon001](https://x.com/hugon001) · 2026-09-25 · ▶ 59 · `One-shot`

A vertical 15-second launch reel for the Mentis app that reused the project's PNGs, glossary and colors, with all text in French.

```text
make a dynamic 15-second motion graphics video that shows what an incredible app Mentis is, like it's your showreel for a app launch. go all out. Make the text in French.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示 Mentis 是一款多么出色的应用，就像你为一次应用发布做的作品集短片。拿出全部本事。画面文字用法语。
```

</details>

<sub>Inputs: Brand kit · Effort: high · Author: finished in 12 minutes in Claude desktop on Mac.</sub>

[Original post ↗](https://x.com/hugon001/status/2103425679618609629) · Prompt posted in [this reply](https://x.com/hugon001/status/2103425683313799263).

---

### SaaS-style promo for an email verifier

<a href="https://x.com/KmAsiff/status/2103810247131549880"><img src="https://pbs.twimg.com/amplify_video_thumb/2103810053266710528/img/AOKxdAhs2r6_lmUo.jpg" alt="SaaS-style promo for an email verifier" width="480"></a>

[@KmAsiff](https://x.com/KmAsiff) · 2026-09-26 · ▶ 58 · `Brief`

A 20-second SaaS-style promo for an email verification tool that covers its use cases, inspired by YC and Claude social videos.

```text
make a dynamic 20-second motion graphics video that shows what an incredible our email verify tool is, put all the use case you can imagine. go all out'
i want you to make it really modern and saas style. inspiration is yc videos and claude social videos
```

<details><summary>中文译文</summary>

```text
制作一段 20 秒的动态图形视频，展示我们的邮箱验证工具有多出色，把你能想到的使用场景都放进去。拿出全部本事'
我希望它非常现代、有 SaaS 风格。灵感来自 yc 的视频和 claude 的社媒视频
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/KmAsiff/status/2103810247131549880)

---

### 10-second ad reel from one image

<a href="https://x.com/GonzaloMacagno/status/2102897651008344202"><img src="https://pbs.twimg.com/amplify_video_thumb/2102897211436683264/img/T2XJWDCcYrr_Zb2k.jpg" alt="10-second ad reel from one image" width="480"></a>

[@GonzaloMacagno](https://x.com/GonzaloMacagno) · 2026-09-23 · ▶ 57 · `One-shot`

A 10-second promotional reel built from a single image the author received by email, using a one-line Spanish prompt.

```text
Necesito que armes un reel con esta info en 10 segundos, bien publicitario
```

<details><summary>English translation</summary>

```text
I need you to put together a reel with this info in 10 seconds, really ad-like
```

</details>

<sub>Inputs: Images · Author: under 1 minute.</sub>

[Original post ↗](https://x.com/GonzaloMacagno/status/2102897651008344202)

---

### Vertical product promo of everyday spending

<a href="https://x.com/felipemoller/status/2103846311149936736"><img src="https://pbs.twimg.com/amplify_video_thumb/2103846156685979648/img/a4gC5AH5tIZe1EWy.jpg" alt="Vertical product promo of everyday spending" width="480"></a>

[@felipemoller](https://x.com/felipemoller) · 2026-09-26 · ▶ 50 · `Brief` · Playwright · ffmpeg

A 30-second 9:16 product promo that simulates spending at a supermarket, gas station and restaurant, built only with JavaScript, Playwright and FFmpeg.

```text
Use apenas: JavaScript, Playwright e FFmpeg. Faça um vídeo moderno, elegante e impactante para meu produto (https://lp.meuorbe.com.br). Quero que simule os gastos em estabelecimentos do dia a dia, como mercado, posto de gasolina e restaurante. 

Faça no formato 9:16.
```

<details><summary>English translation</summary>

```text
Use only: JavaScript, Playwright and FFmpeg. Make a modern, elegant and punchy video for my product (https://lp.meuorbe.com.br). I want it to simulate spending at everyday places, such as the supermarket, the gas station and a restaurant.

Make it in 9:16 format.
```

</details>

<sub>Inputs: Brand kit · Author: took more than one prompt; this is the base prompt.</sub>

[Original post ↗](https://x.com/felipemoller/status/2103846311149936736) · Prompt posted in [this reply](https://x.com/felipemoller/status/2103847070419546556).

---

### One-minute product promo from the codebase

<a href="https://x.com/Ai_Baymax/status/2103411004902416787"><img src="https://pbs.twimg.com/amplify_video_thumb/2103410889739362304/img/o0qHWsHlqTbu7yUV.jpg" alt="One-minute product promo from the codebase" width="480"></a>

[@Ai_Baymax](https://x.com/Ai_Baymax) · 2026-09-25 · ▶ 41 · `One-shot`

A 55-second promo for the FigPad app, built from its code, site copy and screen recordings, with animated captions and a soundtrack composed in code.

```text
make a 1-min promo for this product from the codebase.
```

<details><summary>中文译文</summary>

```text
根据代码库，为这个产品做一支 1 分钟的宣传片。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/Ai_Baymax/status/2103411004902416787)

---

### 30-second pitch video from site and logo

<a href="https://x.com/SPEARwtf/status/2103857153308029058"><img src="https://pbs.twimg.com/amplify_video_thumb/2103856910231388160/img/EWTi3mrYLllRDN5H.jpg" alt="30-second pitch video from site and logo" width="480"></a>

[@SPEARwtf](https://x.com/SPEARwtf) · 2026-09-26 · ▶ 41 · `One-shot`

A 30-second pitch video for @chaindotwtf, made from one sentence plus the website, the logo and context from earlier chats.

```text
Create a 30sec pitch video for @chaindotwtf
```

<details><summary>中文译文</summary>

```text
为 @chaindotwtf 制作一个 30 秒的路演视频
```

</details>

<sub>Inputs: Logo, Brand kit</sub>

[Original post ↗](https://x.com/SPEARwtf/status/2103857153308029058)

---

### Startup launch video steered by four chat messages

<a href="https://x.com/iamMXFSCHR/status/2103619221296955831"><img src="https://pbs.twimg.com/amplify_video_thumb/2103619160768917505/img/WHsvYjndbDlx8E17.jpg" alt="Startup launch video steered by four chat messages" width="480"></a>

[@iamMXFSCHR](https://x.com/iamMXFSCHR) · 2026-09-25 · ▶ 40 · `Pipeline`

A 33-second launch video for the author's startup, steered through four casual German chat messages, the last one adding trendy music.

```text
"""
nice. wir brauchen ein launch video für den release. kannst du das machen? so a la anthropic like? hab da was gelesen und der prompt war ""make a modern slick and punchy video for a modern startup that works on inference"
"""

"""
los, überrasch mich! hauptsache es geht viral
"""

"""
ja wo ist das video? i sehe nur eine .cinfig datei was als video abspielbar ist
"""

"""
können wir da noch eine trendige musik hinterlegen?
"""
```

<details><summary>English translation</summary>

```text
"""
nice. we need a launch video for the release. can you do that? sort of anthropic style? i read something and the prompt was ""make a modern slick and punchy video for a modern startup that works on inference"
"""

"""
come on, surprise me! as long as it goes viral
"""

"""
so where is the video? i only see a .cinfig file that can be played as a video
"""

"""
can we add some trendy music underneath?
"""
```

</details>

<sub>Inputs: Brand kit · Author: four messages sent in a row, each shown between triple quotes.</sub>

[Original post ↗](https://x.com/iamMXFSCHR/status/2103619221296955831)

---

### Remotion product showcase from a live URL

<a href="https://x.com/lester_tyy/status/2103733819568480587"><img src="https://pbs.twimg.com/amplify_video_thumb/2103733769098481664/img/lE4_GCWf-9o8cqV5.jpg" alt="Remotion product showcase from a live URL" width="480"></a>

[@lester_tyy](https://x.com/lester_tyy) · 2026-09-26 · ▶ 39 · `One-shot` · Remotion

A 76-second product showcase made in Remotion after Opus 5.5 studies how a live website works.

```text
Study how this https://experiments.cloudjoi.com works and use Remotion to make a product showcase video.
```

<details><summary>中文译文</summary>

```text
研究一下这个 https://experiments.cloudjoi.com 是怎么运作的，然后用 Remotion 做一个产品展示视频。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/lester_tyy/status/2103733819568480587)

---

### App launch video with a 3D phone

<a href="https://x.com/SteeveDor7/status/2104027894217572848"><img src="https://pbs.twimg.com/amplify_video_thumb/2104027826298957824/img/va-kJ533lv4qxitw.jpg" alt="App launch video with a 3D phone" width="480"></a>

[@SteeveDor7](https://x.com/SteeveDor7) · 2026-09-27 · ▶ 37 · `One-shot`

A 34-second launch video for the app pixieboo, with a 3D phone, motion graphics and music all written as code.

```text
create the best launch video for pixieboo
```

<details><summary>中文译文</summary>

```text
为 pixieboo 做一个最好的发布视频
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/SteeveDor7/status/2104027894217572848)

---

### Investment platform promo

<a href="https://x.com/rammanq/status/2103788796022034553"><img src="https://pbs.twimg.com/amplify_video_thumb/2103788749343617024/img/7ApS2rfAZSFxWtuP.jpg" alt="Investment platform promo" width="480"></a>

[@rammanq](https://x.com/rammanq) · 2026-09-26 · ▶ 21 · `One-shot`

A 42-second promo for the AllInvestView platform; the author notes that every number on screen comes from the actual product.

```text
Make a dynamic motion graphics video that shows what an incredible platform AllInvestView is. Go all out.
```

<details><summary>中文译文</summary>

```text
制作一段动态图形视频，展示 AllInvestView 是一个多么出色的平台。拿出全部本事。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/rammanq/status/2103788796022034553)

---

### Business website explainer for first-time visitors

<a href="https://x.com/AmitSingha89/status/2103737604277780553"><img src="https://pbs.twimg.com/amplify_video_thumb/2103737550448058369/img/ZJSBr4TZCXfEeA-N.jpg" alt="Business website explainer for first-time visitors" width="480"></a>

[@AmitSingha89](https://x.com/AmitSingha89) · 2026-09-26 · ▶ 17 · `One-shot`

A 54-second explainer for a small business website aimed at first-time visitors, made in one shot with no editing.

```text
Make a professional explainer video for https://anuprerna.com for a first-time visitor.
```

<details><summary>中文译文</summary>

```text
为 https://anuprerna.com 制作一个专业的讲解视频，面向第一次访问的用户。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/AmitSingha89/status/2103737604277780553)

---

### Website promo from a bare URL

<a href="https://x.com/anas0ra/status/2103490331815952637"><img src="https://pbs.twimg.com/amplify_video_thumb/2103489980324589568/img/hiYHaMPjrUuuai01.jpg" alt="Website promo from a bare URL" width="480"></a>

[@anas0ra](https://x.com/anas0ra) · 2026-09-25 · ▶ 12 · `One-shot`

A 15-second promo for the heeya.fr website from a casual French one-liner that gives nothing but the URL.

```text
fait moi une vidéo sympa pour https://heeya.fr
```

<details><summary>English translation</summary>

```text
make me a nice video for https://heeya.fr
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/anas0ra/status/2103490331815952637)

---

### App update reel from the showreel prompt

<a href="https://x.com/ammar8jasim/status/2103925219412865457"><img src="https://pbs.twimg.com/amplify_video_thumb/2103925187313827840/img/7ErpgqLcrBUzC-Ow.jpg" alt="App update reel from the showreel prompt" width="480"></a>

[@ammar8jasim](https://x.com/ammar8jasim) · 2026-09-26 · ▶ 10 · `One-shot`

A 15-second motion graphic for the author's app that highlights its latest updates, adapted from the résumé showreel prompt.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are. Highlight the recent changes we made with the last few updates. To my app https://www.studypolar.com
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师。重点展示我们最近几次更新带来的变化。针对我的 app https://www.studypolar.com
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/ammar8jasim/status/2103925219412865457) · Prompt posted in [this reply](https://x.com/ammar8jasim/status/2103925503434322023).

---

<sub>Last updated 2026-09-27.</sub>
