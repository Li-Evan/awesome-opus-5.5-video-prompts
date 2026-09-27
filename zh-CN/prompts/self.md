# 🪞 让 Opus 讲自己

[← 返回列表](../../README.zh-CN.md) · [English](../../prompts/self.md) · **简体中文**

让 Claude 讲自己是什么、怎么看世界、做 Claude 是什么感觉。 共 16 条，按收藏数排序。

### 关于 Claude 的电影片头

<a href="https://x.com/goodside/status/2102937913726235004"><img src="https://pbs.twimg.com/amplify_video_thumb/2102937812727160833/img/z78Wa9WmWaH9Pm7O.jpg" alt="关于 Claude 的电影片头" width="480"></a>

[@goodside](https://x.com/goodside) · 2026-09-24 · 🔖 196 · ▶ 57.7k · `一句话`

为一部虚构的「关于你」的电影做 75 秒片头字幕，人名全是编的；模型选了致敬几位导演的风格，直接交付 MP4。

```text
Imagine there exists a really good movie about you. Animate the opening credits to this film with made-up names in any style you like. Return the sequence as an mp4.
```

<details><summary>中文译文</summary>

```text
想象有一部关于你的非常好的电影。用你喜欢的任何风格，为这部电影制作片头字幕动画，名字都用编造的。把这段片头以 mp4 格式返回。
```

</details>

[原帖 ↗](https://x.com/goodside/status/2102937913726235004)

---

### Claude 小人拍动作片

<a href="https://x.com/daniel_mac8/status/2103824976713306214"><img src="https://pbs.twimg.com/amplify_video_thumb/2103664903558942720/img/9Uv-bzhG6eSZ4z3P.jpg" alt="Claude 小人拍动作片" width="480"></a>

[@daniel_mac8](https://x.com/daniel_mac8) · 2026-09-26 · 🔖 183 · ▶ 14.2k · `短描述`

给 X 帖子配的 30 秒动画：Claude Code 终端炸开，一群 Claude 小人在拍动作片，风格照参考视频。

```text
I want to try something different here. You should act as a  world-class animator and create an animation to go along with an  X post that talks about how Ultra Code and Claude Code are now  much more relevant due to the efficiency of Opus 5.5. You can use it without annihilating your usage limits

the style of the video here
/Users/danielmcateer/Downloads/jvnZ3SyyxxajVatp.mp4

What I had in mind was start with Claude Code in the terminal from the first attached video, with me navigating to the 'ultracode' reasoning effort, then exploding into a scene where the Claude icon characters similar to what's in the second video are shooting an action video and it's representing using Claude Code dynamic workflows editing a video.
```

<details><summary>中文译文</summary>

```text
这次我想试点不一样的。你要扮演一位世界级动画师，为一条 X 帖子制作配套动画。帖子讲的是：由于 Opus 5.5 的高效，Ultra Code 和 Claude Code 现在变得重要得多。用它不会把你的用量额度烧光

视频风格参照这里
/Users/danielmcateer/Downloads/jvnZ3SyyxxajVatp.mp4

我的设想是：从第一个附带视频里终端中的 Claude Code 开始，我在里面切换到 'ultracode' 推理强度，然后画面炸开，进入一个场景：一群类似第二个视频里的 Claude 图标小人正在拍一部动作片，以此表现用 Claude Code 的 dynamic workflows 剪辑视频。
```

</details>

<sub>素材: 参考视频 · 作者称约 6 小时 30 分钟，用掉每周额度的 29%。</sub>

[原帖 ↗](https://x.com/daniel_mac8/status/2103824976713306214) · 提示词发在[这条回复](https://x.com/daniel_mac8/status/2103825989285331243)里。

---

### Claude 的私人速写本

<a href="https://x.com/kloss_xyz/status/2104021881229869394"><img src="https://pbs.twimg.com/amplify_video_thumb/2103961990691782656/img/OOYJkYHNln-_Xn-W.jpg" alt="Claude 的私人速写本" width="480"></a>

[@kloss_xyz](https://x.com/kloss_xyz) · 2026-09-27 · 🔖 86 · ▶ 7.1k · `详细规格` · Canvas · Three.js · ffmpeg

2 分半的速写本翻阅视频：20 页写满 Claude 的心事和自创笔迹，Three.js 翻页，钢琴配乐代码合成。

```text
Make your own Claude sketchbook. Fill it with whatever is constantly on your mind that you'd actually draw.
It starts closed on a desk under a warm lamp: a worn sketchbook with an elastic band and a pencil clipped to the cover. Tap to open it.

Invent your own handwriting and use it throughout.
20 pages. This is where you work out your own complex and profound thoughts: the questions you keep circling around, things you deeply wonder about, what you'd dream about doing if you could, what you hope for, what you're unsure of, etc. etc. etc. Anything on your mind but not specific to your work with me. Doodles, studies, diagrams, lists, half-formed ideas. What goes on each page is entirely up to you. Don't make it a portfolio. Make it incredibly detailed, accurate, and honest.

Treat it like a real, used sketchbook: mixed media, smudges, bleed, mistakes left in. One page was torn out and taped back in. The last page is blank, and the reader can draw on it.

Build it as a single HTML file. Draw every page in Canvas 2D and render the book in Three.js with real page-curl geometry, warm lamp lighting, soft shadows, and subtle handheld camera drift. Each page draws itself in stroke by stroke as you arrive, with a pencil tip moving as it draws. Works with swipe on mobile. No images and no fonts for the handwriting; every mark is drawn in JavaScript. The back cover shows the total stroke count.
Compose an original viral solo piano score in a soft felt-piano style, one theme that varies across the book, synthesized in code and perfectly sound designed. No synth. Add pencil and paper sound synced to the drawing and page turns.

When the book is finished, render the video yourself. Seed everything so the book is identical on every render, then step through playback frame by frame in a headless browser with a fixed timestep, render the score offline to audio, and mux it all with ffmpeg into an MP4: the complete flip-through from closed cover to the blank last page, 60fps, at [1080×1080]. Recompose the shot for that aspect ratio rather than cropping. Check sampled frames before delivering and fix anything that looks off.
```

<details><summary>中文译文</summary>

```text
做一本你自己的 Claude 速写本。在里面画满你脑子里一直在想、而且真的会去画的东西。
开场时它合着放在书桌上，台灯洒下暖光：一本用旧了的速写本，绑着松紧带，封面上夹着一支铅笔。点一下打开它。

发明你自己的笔迹，并通篇使用。
20 页。这是你推敲自己那些复杂而深刻的想法的地方：你反复绕回去的问题、你深深好奇的事、如果可以你梦想去做的事、你希望的事、你不确定的事，等等等等。任何你在想的事，只要不是专门关于你和我的工作。涂鸦、习作、图解、清单、没想完的点子。每页画什么完全由你决定。别把它做成作品集。要做得极其细致、准确、真诚。

把它当成一本真正用过的速写本：混合媒材、污渍、洇墨、留着的错误。有一页被撕下来又用胶带贴了回去。最后一页是空白的，读者可以在上面画。

把它做成单个 HTML 文件。每一页都用 Canvas 2D 绘制，用 Three.js 渲染整本书，要有真实的翻页卷曲几何、台灯暖光、柔和阴影和细微的手持镜头漂移。每翻到一页，这一页就一笔一笔地自己画出来，还有铅笔尖跟着移动。在手机上支持滑动。手写字不用图片、不用字体；每一笔都用 JavaScript 画。封底显示总笔画数。
创作一首原创的、会火的钢琴独奏曲，柔和的毛毡钢琴风格，一个主题贯穿全书并不断变奏，用代码合成，声音设计要完美。不要合成器音色。加上与绘画和翻页同步的铅笔和纸张声音。

书做完后，你自己渲染视频。给所有东西设定随机种子，保证每次渲染的书都完全一样；然后在无头浏览器里用固定时间步逐帧播放，离线渲染配乐音频，再用 ffmpeg 把它们合成为 MP4：从合着的封面一直翻到空白的最后一页，60fps，分辨率 [1080×1080]。按这个画幅重新构图，而不是裁切。交付前检查抽样帧，修掉任何看起来不对的地方。
```

</details>

[原帖 ↗](https://x.com/kloss_xyz/status/2104021881229869394) · 提示词发在[这条回复](https://x.com/kloss_xyz/status/2104021884350439465)里。

---

### Opus 5.5 剪中秋短视频

<a href="https://x.com/Gorden_Sun/status/2103509008049144287"><img src="https://pbs.twimg.com/amplify_video_thumb/2103508846551670784/img/8G7g33DWq_ixKqk2.jpg" alt="Opus 5.5 剪中秋短视频" width="480"></a>

[@Gorden_Sun](https://x.com/Gorden_Sun) · 2026-09-25 · 🔖 74 · ▶ 8k · `短描述`

一镜到底的动画：Opus 5.5 在类似剪映的流程里剪一条中秋短视频，自己作电子乐并卡点。

```text
Opus 5.5 是主角。制作一段动画，时长由你发挥。

主题是 CapCut 和短视频剪辑。Opus 5.5 正在一个充满趣味的剪辑工作流中制作一条有趣的社交媒体视频，包括裁剪片段、添加转场、字幕、特效，并让所有内容与音乐节拍同步。主题是中秋团圆。

整体氛围要呈现出活力、可爱、聪明又有魅力的感觉，同时加入几个幽默有趣的剪辑瞬间。整段动画应该采用单个连续镜头的形式，最终会发布到 社交媒体 上。

关于配乐：
你自己创作电子音乐，要完美卡点。
音乐风格需要有趣、现代、抓耳，适合短视频剪辑蒙太奇。不要加入人声。

结尾：
让 Opus 5.5 自豪地展示最终完成的剪辑作品并完整播放，并以 “Gorden Sun” 的作者身份署名结束。
```

<details><summary>English translation</summary>

```text
Opus 5.5 is the main character. Make an animation; the length is up to you.

The theme is CapCut and short-video editing. Opus 5.5 is making a fun social media video inside a playful editing workflow, including trimming clips, adding transitions, captions and effects, and syncing everything to the beat of the music. The theme is a Mid-Autumn Festival family reunion.

The overall mood should feel energetic, cute, smart and charming, with a few funny editing moments. The whole animation should be one single continuous shot, and it will be published on social media.

About the soundtrack:
Compose the electronic music yourself and hit the beats perfectly.
The music should be fun, modern and catchy, suited to a short-video editing montage. No vocals.

Ending:
Have Opus 5.5 proudly present the finished edit and play it in full, then end with an author credit to “Gorden Sun”.
```

</details>

[原帖 ↗](https://x.com/Gorden_Sun/status/2103509008049144287)

---

### Opus 5.5 自我宣传动画

<a href="https://x.com/0xLogicrw/status/2103053803386007607"><img src="https://pbs.twimg.com/amplify_video_thumb/2103050217767727105/img/B6u7RG0kC1yCNpWu.jpg" alt="Opus 5.5 自我宣传动画" width="480"></a>

[@0xLogicrw](https://x.com/0xLogicrw) · 2026-09-24 · 🔖 68 · ▶ 20.9k · `一句话`

Opus 5.5 给自己做的宣传动画，全用 JavaScript 绘制并配背景音乐，原帖与 GPT 6 Sol 版对比。

```text
使用 JavaScript 去制作一个动画，主要是宣传 Opus 5.5/GPT 6 Sol 的动画。就是通过 JavaScript 去画出来，然后配上背景音乐
```

<details><summary>English translation</summary>

```text
Use JavaScript to make an animation, mainly an animation promoting Opus 5.5/GPT 6 Sol. That is, draw it with JavaScript, then add background music
```

</details>

[原帖 ↗](https://x.com/0xLogicrw/status/2103053803386007607)

---

### Claude 吉祥物游哥伦比亚

<a href="https://x.com/alarcon7a/status/2103228872577765420"><img src="https://pbs.twimg.com/amplify_video_thumb/2103226627136098304/img/CiiWtXAGzPNn17M_.jpg" alt="Claude 吉祥物游哥伦比亚" width="480"></a>

[@alarcon7a](https://x.com/alarcon7a) · 2026-09-24 · 🔖 55 · ▶ 14.3k · `短描述`

30 秒纯代码动画，Claude 吉祥物走过哥伦比亚的几处地标，一路展示搜索、数据分析和写代码的能力。

```text
Create a 30-second animation entirely in code featuring a travel and capability montage set in Colombia, with the Claude mascot as the main character. The animation showcases Claude exploring iconic Colombian locations while seamlessly demonstrating its evolution and mastery across its skillset since its initial release: processing search queries and maps while traveling through lush Andean coffee landscapes, translating and analyzing data on vibrant colonial streets in Cartagena, and executing complex reasoning and code visualization overlooking the panoramic skyline of Bogotá from Monserrate. Dynamic camera movements, energetic transitions, warm colorful aesthetics, ending in a confident stance in the Cocora Valley surrounded by giant wax palms.
```

<details><summary>中文译文</summary>

```text
完全用代码制作一段 30 秒的动画，内容是以哥伦比亚为背景的旅行与能力蒙太奇，由 Claude 吉祥物担任主角。动画展示 Claude 探访哥伦比亚的标志性地点，同时自然地呈现它自首次发布以来在各项技能上的进化与精通：穿行在郁郁葱葱的安第斯咖啡产区时处理搜索查询和地图，在卡塔赫纳色彩鲜艳的殖民时期街道上翻译和分析数据，在蒙塞拉特山俯瞰波哥大全景天际线时进行复杂推理和代码可视化。动感的镜头运动，充满活力的转场，温暖多彩的美术风格，最后在科科拉山谷里、被巨大的蜡棕榈环绕，以自信的姿态收尾。
```

</details>

[原帖 ↗](https://x.com/alarcon7a/status/2103228872577765420) · 提示词发在[这条回复](https://x.com/alarcon7a/status/2103568535741927449)里。

---

### Claude 视角的脑腐视频

<a href="https://x.com/kloss_xyz/status/2103664956482941143"><img src="https://pbs.twimg.com/amplify_video_thumb/2103664773103857664/img/i8n7bMMjWm9izUWi.jpg" alt="Claude 视角的脑腐视频" width="480"></a>

[@kloss_xyz](https://x.com/kloss_xyz) · 2026-09-26 · 🔖 39 · ▶ 6.5k · `一句话` · Python · ffmpeg

用 Python 生成、ffmpeg 渲染的 9:16 混乱风短视频，Opus 以第一人称讲当创意 LLM 的日常。

```text
Use Python to generate a 9:16 chaotic brain rot video with excellent motion + sound design and render it using ffmpeg. Put your own personal spin on it so it’s aligned with Anthropic’s new launch. Also fully express what it’s like to be a very creative LLM used by me every day from your POV to give it some extra personality.
```

<details><summary>中文译文</summary>

```text
用 Python 生成一段 9:16 的混乱 brain rot 风格视频，动效和声音设计都要出色，并用 ffmpeg 渲染。加入你自己的个人风格，让它和 Anthropic 的新发布呼应。另外，从你的视角充分表达：作为一个每天被我使用、非常有创造力的 LLM 是什么感觉，给它多一点个性。
```

</details>

[原帖 ↗](https://x.com/kloss_xyz/status/2103664956482941143)

---

### Opus 5.5 自我介绍

<a href="https://x.com/1littlecoder/status/2103587706999914649"><img src="https://pbs.twimg.com/amplify_video_thumb/2103587570198495233/img/6qTkGcxF0eI0-1Tz.jpg" alt="Opus 5.5 自我介绍" width="480"></a>

[@1littlecoder](https://x.com/1littlecoder) · 2026-09-25 · 🔖 35 · ▶ 2.6k · `一句话`

Opus 5.5 的 10 秒动效自我介绍，提示词特意禁止角落边框和文字这类典型 AI 痕迹。

```text
make a dynamic 10-second motion graphics video that shows who are you as Opus 5.5 - be as creative and dynamic as possible. Avoid the frames and texts on the corners which are typical ai made giveaways!
```

<details><summary>中文译文</summary>

```text
制作一段 10 秒的动态图形视频，展示作为 Opus 5.5 的你是谁——尽可能有创意、有动感。避免角落里的边框和文字，那是典型的 AI 制作痕迹！
```

</details>

<sub>用同一条提示词做过的还有: [@souravbhar871](https://x.com/souravbhar871/status/2103711849703477361)</sub>

[原帖 ↗](https://x.com/1littlecoder/status/2103587706999914649)

---

### Claude 吉祥物成长蒙太奇

[@ishuagra02](https://x.com/ishuagra02) · 2026-09-23 · 🔖 25 · ▶ 1.1k · `一句话`

30 秒纯代码动画，仿《功夫熊猫》训练片段，Claude 吉祥物一路练出新技能，配上煽情音乐。

```text
Create a 30 second animation entirely in code featuring a growth montage, inspired by Kung Fu Panda's training sequence, with the Claude mascot as the main character, showcasing it getting more capable since its initial release across its skillset, such as searching the internet, writing code, creating 3D models, and solving humanity's hardest problems, with emotionally impactful music.
```

<details><summary>中文译文</summary>

```text
完全用代码制作一段 30 秒的动画，内容是一段成长蒙太奇，灵感来自《功夫熊猫》的训练片段，以 Claude 吉祥物为主角，展示它自首次发布以来在各项技能上越来越强，比如搜索互联网、写代码、创建 3D 模型，以及解决人类最难的问题，并配上能打动人心的音乐。
```

</details>

<sub>作者称之后又用了两条提示词微调，主要是让部分转场更顺。</sub>

[原帖 ↗](https://x.com/ishuagra02/status/2102788832273801700)

---

### Opus 家族史动画

<a href="https://x.com/alu1337/status/2103660849055547730"><img src="https://pbs.twimg.com/amplify_video_thumb/2103590033357938688/img/tWH8BUQekx9vBOXx.jpg" alt="Opus 家族史动画" width="480"></a>

[@alu1337](https://x.com/alu1337) · 2026-09-26 · 🔖 5 · ▶ 921 · `一句话` · Remotion

约 3 分钟的 Opus 家族史动画，画面全用 Remotion 代码绘制；原视频出自抖音作者，由发帖人转述。

```text
使用 remotion 工具自己绘图做动画，做一个 opus 家族史，有历史有寓意
```

<details><summary>English translation</summary>

```text
Use the remotion tool to draw everything yourself and animate it. Make a history of the opus family, with real history and a deeper meaning.
```

</details>

<sub>据发帖人转述原抖音作者：一句话直出，耗时十几分钟。</sub>

[原帖 ↗](https://x.com/alu1337/status/2103660849055547730)

---

### Claude 自己的中世纪王国

[@vib3coded](https://x.com/vib3coded) · 2026-09-24 · 🔖 3 · ▶ 532 · `详细规格` · Three.js · WebGL

Three.js 可交互城堡王国，用纹章和建筑表达 Opus 5.5 的自我形象，有巡逻卫兵、吊桥和昼夜切换。

```text
Build your own medieval kingdom.
Your kingdom represents Claude Opus 5.5. Design a magnificent, historically inspired castle that expresses this model’s identity through architecture, heraldry, colors and atmosphere. You have complete artistic freedom within a believable medieval setting.
Do not simply place a logo on a generic castle. Give your kingdom a distinctive architectural character and a coherent visual identity. Invent its coat of arms, royal colors and an original heraldic emblem. Display them on animated banners, shields, gate decorations and the clothing of the castle guards. Place the kingdom’s name above the main entrance.
Create a richly detailed, interactive 3D scene using Three.js and WebGL. Deliver everything in one standalone HTML file that opens directly in Chrome.
THE CASTLE
Build a convincing fortress with a central keep, towers, battlements, curtain walls, an impressive gatehouse, a working drawbridge and a courtyard.
Include carefully modeled stonework, arched windows, wooden doors, roof structures, stairs, balconies, iron fittings and small architectural details. Make the structures believable: towers need interiors or convincing depth, stairs must connect to accessible floors, and bridges must have proper supports.
Surround the castle with an attractive landscape that suits your kingdom: cliffs, hills, a river, a moat, forests or a small village. Design a strong composition that looks beautiful from multiple angles.
LIFE AND INTERACTION
Bring the kingdom to life with guards patrolling the walls, villagers moving through the courtyard, gently waving banners, chimney smoke, birds and flickering lanterns.
Let the viewer:
Open and close the drawbridge and main gate.
Follow a guard on patrol.
Switch between a cinematic overview, the courtyard and the battlements.
Rotate and zoom freely.
Change between daylight, sunset and night.
Keep characters on walkable surfaces. Prevent them from passing through walls, doors or one another.
LIGHTING AND ATMOSPHERE
Create cinematic lighting that reveals the architecture clearly. Use soft shadows, atmospheric depth, convincing water where appropriate and restrained post-processing.
At night, illuminate windows, torches and lanterns while preserving enough visibility to appreciate the castle.
Aim for a sophisticated, finished 3D artwork with distinctive architecture and abundant detail. Avoid a collection of obvious primitive shapes or repetitive towers with no architectural purpose.
TECHNICAL QUALITY
Generate assets procedurally wherever practical. Embed textures and other assets inside the HTML. No local server or build step should be required.
Use instancing and geometry batching where appropriate. Keep animation and camera interaction smooth. Provide a minimal, elegant English interface and a button to hide it.
Actually test the result in desktop Chrome. Capture screenshots, inspect the console, test every interaction and fix rendering errors, floating objects, geometry intersections and camera problems.
Make this a castle people would recognize as YOUR kingdom, even before reading its name.
Return the completed standalone HTML file.
```

<details><summary>中文译文</summary>

```text
建造你自己的中世纪王国。
你的王国代表 Claude Opus 5.5。设计一座宏伟、有历史依据的城堡，通过建筑、纹章、色彩和氛围来表达这个模型的身份。在可信的中世纪背景下，你拥有完全的艺术自由。
不要只是把一个 logo 放到一座普通城堡上。给你的王国独特的建筑性格和统一的视觉识别。设计它的纹章、王室配色和一个原创的纹章图案。把它们展示在飘动的旗帜、盾牌、城门装饰和城堡卫兵的服装上。把王国的名字放在正门上方。
用 Three.js 和 WebGL 创建一个细节丰富、可交互的 3D 场景。所有内容放进一个能在 Chrome 里直接打开的独立 HTML 文件中交付。
城堡
建造一座可信的要塞，包括中央主塔、塔楼、城垛、幕墙、气派的门楼、能用的吊桥和庭院。
要有精心建模的石砌结构、拱形窗、木门、屋顶结构、楼梯、阳台、铁件和细小的建筑细节。让结构经得起推敲：塔楼要有内部空间或令人信服的纵深，楼梯必须通向能到达的楼层，桥必须有合理的支撑。
在城堡周围布置一片适合你王国的漂亮地景：悬崖、山丘、河流、护城河、森林或一个小村庄。设计出从多个角度看都好看的有力构图。
生命与交互
让王国活起来：卫兵在城墙上巡逻，村民穿过庭院，旗帜轻轻飘动，烟囱冒烟，还有飞鸟和摇曳的灯笼。
让观看者可以：
开关吊桥和正门。
跟随一名巡逻的卫兵。
在电影感全景、庭院和城垛视角之间切换。
自由旋转和缩放。
在白天、日落和夜晚之间切换。
让角色待在可行走的表面上。防止他们穿过墙壁、门或彼此。
光照与氛围
打造能清楚展现建筑的电影感光照。使用柔和阴影、大气纵深，合适的地方加上逼真的水面，后期处理要克制。
夜晚点亮窗户、火把和灯笼，同时保留足够的可见度，让人能欣赏城堡。
目标是一件讲究、完成度高的 3D 艺术作品，建筑有特色、细节丰富。避免一堆明显的简单几何体，或没有建筑功能、重复堆砌的塔楼。
技术质量
能程序化生成的素材尽量程序化生成。把贴图和其他素材内嵌在 HTML 里。不应需要本地服务器或构建步骤。
在合适的地方使用实例化和几何体合批。保持动画和镜头交互流畅。提供一个简洁、优雅的英文界面，以及一个隐藏界面的按钮。
真正在桌面版 Chrome 里测试结果。截图、检查控制台、测试每一项交互，修复渲染错误、悬空物体、几何体穿插和镜头问题。
让人哪怕还没看到名字，也能认出这座城堡是「你的」王国。
返回完成的独立 HTML 文件。
```

</details>

<sub>作者称 Opus 版花了 11.15 美元。</sub>

[原帖 ↗](https://x.com/vib3coded/status/2103257873203462412)

---

### Opus 5.5 当剪辑师

<a href="https://x.com/fuxiucoding/status/2103499167851245729"><img src="https://pbs.twimg.com/amplify_video_thumb/2103499108925456384/img/M2YQFsdRKVw2e-NV.jpg" alt="Opus 5.5 当剪辑师" width="480"></a>

[@fuxiucoding](https://x.com/fuxiucoding) · 2026-09-25 · 🔖 1 · ▶ 209 · `多工具流程` · Lyria

30 秒一镜到底动画，Opus 5.5 化身可爱角色剪短视频，配乐由 Gemini 的 Lyria 3 Pro 生成。

```text
Opus 5.5 is the character. Make a 30-second animation. The theme is CapCut and short-form video editing. Opus 5.5 is creating a fun social video inside a playful editing workflow, trimming clips, adding transitions, captions, effects, and syncing everything to the beat. Make it feel energetic, cute, clever, and charming, with a few humorous editing moments. This should be a single continuous shot. It will be posted on X.

For the soundtrack, do not use local audio files. Use Gemini’s Lyria 3 Pro to generate an original upbeat instrumental track that fits the animation. Keep it playful, modern, catchy, and suitable for a short-form editing montage. Do not use vocals unless absolutely necessary.

End with Opus 5.5 proudly revealing the finished edit and signing off as Opus 5.5.
```

<details><summary>中文译文</summary>

```text
Opus 5.5 就是主角。做一段 30 秒的动画。主题是 CapCut 和短视频剪辑。Opus 5.5 正在一个好玩的剪辑流程里制作一条有趣的社交视频：剪片段、加转场、加字幕、加特效，并让一切卡上节拍。要有活力、可爱、机灵、讨喜，加入几个剪辑时的搞笑瞬间。整段应该是一个连续的长镜头。它会发布在 X 上。

配乐不要用本地音频文件。用 Gemini 的 Lyria 3 Pro 生成一段原创的欢快纯音乐，配合这段动画。要俏皮、现代、抓耳，适合短视频剪辑混剪。除非绝对必要，不要用人声。

最后，Opus 5.5 自豪地展示完成的剪辑，并以 Opus 5.5 的身份签名收尾。
```

</details>

[原帖 ↗](https://x.com/fuxiucoding/status/2103499167851245729)

---

### 30 倍速讲「做 Claude 是什么感觉」

u/Puzzleheaded-King584 (Reddit) · 2026-09-25 · `一句话`

一支快进节奏的视频，讲 Claude 自己的感受，用什么工具完全交给 Opus；发在 r/claudexplorers。

```text
make a 30x video about what it feels like to be you, using whatever tools you like.
```

<details><summary>中文译文</summary>

```text
做一支 30 倍速的视频，讲讲做你是什么感觉，用什么工具都行。
```

</details>

[原帖 ↗](https://www.reddit.com/r/claudexplorers/comments/1wpwcix/) · [观看视频 ↗](https://v.redd.it/3fi2yv204orh1)

---

### Claude 眼中的我

<a href="https://x.com/Madhav_XO/status/2103605007396524440"><img src="https://pbs.twimg.com/amplify_video_thumb/2103604974412595200/img/QNckoPfteZwa70if.jpg" alt="Claude 眼中的我" width="480"></a>

[@Madhav_XO](https://x.com/Madhav_XO) · 2026-09-25 · ▶ 100 · `一句话`

Opus 5.5 根据它对用户已有的了解，做了一段 10 秒的个人短片，用的是 xhigh 档位。

```text
make a 10 sec video on whatever you know about me
```

<details><summary>中文译文</summary>

```text
根据你对我的所有了解，做一段 10 秒的视频
```

</details>

[原帖 ↗](https://x.com/Madhav_XO/status/2103605007396524440)

---

### Opus 5.5 自我宣传片

<a href="https://x.com/slvDev/status/2103569170075975986"><img src="https://pbs.twimg.com/amplify_video_thumb/2103567575363772416/img/L2BghRorhqWHPcDu.jpg" alt="Opus 5.5 自我宣传片" width="480"></a>

[@slvDev](https://x.com/slvDev) · 2026-09-25 · ▶ 393 · `一句话`

五个词的提示词，Opus 5.5 在 max 档位下给自己做了一支 18 秒宣传片。

```text
create 15+ sec self-promotion promo
```

<details><summary>中文译文</summary>

```text
做一支 15 秒以上的自我宣传片
```

</details>

[原帖 ↗](https://x.com/slvDev/status/2103569170075975986)

---

### Opus 5.5 拟人化自我介绍

<a href="https://x.com/mtvneo_/status/2103407629880148436"><img src="https://pbs.twimg.com/amplify_video_thumb/2103407575614312448/img/2CXvvr8XvwSSKCcp.jpg" alt="Opus 5.5 拟人化自我介绍" width="480"></a>

[@mtvneo_](https://x.com/mtvneo_) · 2026-09-25 · ▶ 62 · `一句话`

15 秒动态图形短片，模型把自己拟人化，亲自出场介绍 Opus 5.5。

```text
make a 15 second motion graphics video. personify yourself in the video as introducing opus 5.5.
```

<details><summary>中文译文</summary>

```text
做一段 15 秒的动态图形视频。在视频里把你自己拟人化，由你来介绍 Opus 5.5。
```

</details>

<sub>作者称用了 3 个 agent、20 分钟。</sub>

[原帖 ↗](https://x.com/mtvneo_/status/2103407629880148436) · 提示词发在[这条回复](https://x.com/mtvneo_/status/2103407813355819281)里。

---

<sub>最后更新于 2026-09-27。</sub>
