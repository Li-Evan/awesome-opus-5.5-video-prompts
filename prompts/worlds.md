# 🧊 3D, Shaders and Worlds

[← Back to the list](../README.md) · **English** · [简体中文](../zh-CN/prompts/worlds.md)

3D scenes, flythroughs, simulations, shaders and cosmic zooms. 15 prompts, most saved first.

### Pixel-art Paris night diorama lofi loop

<a href="https://x.com/minosdevs/status/2103112945341251920"><img src="https://pbs.twimg.com/amplify_video_thumb/2103112926575910912/img/iZVnHGYtDMTFx5O4.jpg" alt="Pixel-art Paris night diorama lofi loop" width="480"></a>

[@minosdevs](https://x.com/minosdevs) · 2026-09-24 · 🔖 1.4k · ▶ 135.3k · `Spec` · Canvas · Remotion

A seamless 4-minute pixel-art loop of rainy Paris at night with the Eiffel Tower, the Seine and falling euro notes, built as a lofi background.

```text
Fais-moi un diorama pixel-art animé de Paris la nuit, pour servir de fond en boucle à une vidéo lofi de 10 heures sur YouTube. Tout dans un seul fichier HTML (canvas + JavaScript, sans librairie).

AMBIANCE ET COULEURS
Joue à fond sur le contraste chaud / froid : une nuit pluvieuse bleu nuit et violette, avec des coins de lumière chaude. La tour Eiffel dorée, les fenêtres éclairées, les réverbères, un café.

LA SCÈNE (de l'arrière vers l'avant)
- Un ciel en dégradé tramé (dithering façon pixel art), une lune avec un halo, et plusieurs couches de nuages qui défilent lentement, éclairées par la lune au-dessus et par la ville en dessous.
- La tour Eiffel au centre, dorée, avec sa structure en treillis, ses 3 plateformes et son antenne. Son phare tourne et balaie le ciel. Elle scintille régulièrement (des points blancs qui clignotent partout), et une lumière rouge clignote tout en haut.
- Au fond, une ligne de toits parisiens avec des fenêtres qui s'allument et s'éteignent, le dôme doré des Invalides et le Sacré-Cœur blanc sur sa colline.
- Un quai avec des platanes et des réverbères.
- La Seine, avec les reflets de la tour et des lampadaires qui ondulent, de longues traînées de lumière dorée, des ronds de pluie sur l'eau, et un bateau-mouche éclairé qui traverse de temps en temps.
- À gauche, au premier plan, un immeuble haussmannien : toit en zinc mouillé, cheminée qui fume et crache des étincelles, un chat dans une lucarne qui bouge la queue, une fenêtre à la bougie qui vacille, une télé qui clignote en bleu, un balcon en fer forgé, un café avec un store rayé rouge et un néon « CAFÉ » qui grésille de temps en temps.
- À droite, un réverbère parisien avec un halo chaud, qui vacille parfois.
- Tout en bas, une balustrade en fer forgé avec des jardinières.

EFFETS
- De la pluie sur 3 profondeurs. Les gouttes deviennent orange quand elles passent dans une lumière, et elles éclaboussent sur les rebords, le store et la balustrade.
- DES BILLETS QUI TOMBENT DU CIEL : des billets de 100 €, 50 € et 20 €, sur plusieurs profondeurs. Ils virevoltent comme des feuilles (ils se balancent, pivotent, se retournent et brillent quand ils font face).
- De la fumée qui dérive avec le vent, des étincelles, des lumières qui vacillent, et 2 éclairs discrets dans les nuages par boucle.

TECHNIQUE (important)
- Le rendu interne est en 480×270, agrandi ×4 sans lissage (plus proche voisin), pour obtenir un 1920×1080 parfaitement net en plein écran.
- La boucle est PARFAITE et dure 4 minutes : chaque animation est une fonction du temps modulo 240 s (fréquences entières, particules déterministes), donc aucun saut au moment où ça reboucle.
- Touche R : enregistre exactement une boucle en 1920×1080, 60 fps, et télécharge le fichier vidéo (mp4 si possible, sinon webm).
- Touche S : capture PNG en 1080p. Touche F ou double-clic : plein écran. Le curseur se cache quand on ne bouge pas la souris.
- Optimise pour tenir 60 fps : sprites pré-rendus, halos en cache, et un canvas avec l'option willReadFrequently.
```

<details><summary>English translation</summary>

```text
Make me an animated pixel-art diorama of Paris at night, to serve as the looping background for a 10-hour lofi video on YouTube. Everything in a single HTML file (canvas + JavaScript, no library).

MOOD AND COLORS
Go all in on the warm / cold contrast: a rainy midnight-blue and purple night, with pockets of warm light. The golden Eiffel Tower, lit windows, street lamps, a café.

THE SCENE (from back to front)
- A gradient sky with ordered dithering (pixel-art style dithering), a moon with a halo, and several layers of clouds drifting slowly, lit by the moon from above and by the city from below.
- The Eiffel Tower in the center, golden, with its lattice structure, its 3 platforms and its antenna. Its beacon rotates and sweeps the sky. It sparkles regularly (white dots blinking all over), and a red light blinks at the very top.
- In the background, a line of Parisian rooftops with windows that turn on and off, the golden dome of Les Invalides and the white Sacré-Cœur on its hill.
- A quay with plane trees and street lamps.
- The Seine, with rippling reflections of the tower and the lampposts, long trails of golden light, rain rings on the water, and a lit bateau-mouche crossing from time to time.
- On the left, in the foreground, a Haussmann building: wet zinc roof, a chimney that smokes and spits sparks, a cat in a dormer window moving its tail, a candlelit window that flickers, a TV flickering blue, a wrought-iron balcony, a café with a red striped awning and a « CAFÉ » neon sign that sputters now and then.
- On the right, a Parisian street lamp with a warm halo, which sometimes flickers.
- At the very bottom, a wrought-iron railing with planters.

EFFECTS
- Rain at 3 depths. The drops turn orange when they pass through a light, and they splash on the ledges, the awning and the railing.
- BANKNOTES FALLING FROM THE SKY: 100 €, 50 € and 20 € notes, at several depths. They flutter like leaves (they sway, spin, flip over and shine when they face the viewer).
- Smoke drifting with the wind, sparks, flickering lights, and 2 subtle lightning flashes in the clouds per loop.

TECHNIQUE (important)
- Internal rendering is 480×270, scaled ×4 without smoothing (nearest neighbor), to get a perfectly sharp 1920×1080 in full screen.
- The loop is PERFECT and lasts 4 minutes: every animation is a function of time modulo 240 s (integer frequencies, deterministic particles), so there is no jump when it loops back.
- R key: records exactly one loop at 1920×1080, 60 fps, and downloads the video file (mp4 if possible, otherwise webm).
- S key: 1080p PNG capture. F key or double-click: full screen. The cursor hides when the mouse isn't moving.
- Optimize to hold 60 fps: pre-rendered sprites, cached halos, and a canvas with the willReadFrequently option.
```

</details>

[Original post ↗](https://x.com/minosdevs/status/2103112945341251920) · Prompt posted in [this reply](https://x.com/minosdevs/status/2103112948478570675).

---

### Infinite zoom through vintage objects

<a href="https://x.com/koldo2k/status/2103129343253778767"><img src="https://pbs.twimg.com/amplify_video_thumb/2103123431558348801/img/Y0JXLfCRvHmqUs6I.jpg" alt="Infinite zoom through vintage objects" width="480"></a>

[@koldo2k](https://x.com/koldo2k) · 2026-09-24 · 🔖 933 · ▶ 67.5k · `Pipeline` · Magnific · Kling

A 20-second seamless infinite-zoom loop that flies through vintage objects into new landscapes in a newspaper-collage look; images, Kling animation and music come via the Magnific MCP.

```text
Build a looping "infinite zoom" animation, After Effects style: the camera
travels from landscape to landscape by flying through vintage objects.

LOOK: vintage collage realistic photo landscapes + black & white newspaper
cutout objects (halftone, white paper border, soft shadow). Film grain,
vignette, light flicker.

WORLDS (loop): snowy mountains → pocket watch (swinging on its chain) →
sea cliffs → box camera lens → desert dunes → magnifying glass →
misty lake → hand mirror → back to start.
Extras: floating hat, phone, umbrella, gramophone, key; a 1950s man walking
toward the watch; a whale swimming across the cliffs sky.

HOW:
- Generate everything via the Magnific MCP (Seedream 5 Pro landscapes,
  GPT 2.5 transparent cutouts, depth maps, Kling 2.5 animation, Lyria 3
  music). List the generations + credit cost and wait for my OK first.
- Split each landscape into 3 depth layers from its depth map and fill the
  hidden areas. Parallax: layer scale = camera^Z, Z between 0.45 and 1.22.
- Each portal's glass holds the next world; cut seamlessly when it fills
  the frame.
- Constant speed: exponential zoom to a fixed point, each segment's duration
  proportional to log(zoom). Verify the cuts frame by frame.
- Man & whale: generate on pure green (#00B140), animate in place with
  Kling, key out every frame, build a seamless loop (ping-pong if needed).
- Cutouts animate at 15 fps (on twos).
- 20 s loop, 1920×1080, 30 fps. Music: 96 BPM, cut to exactly 8 bars = 20 s.

DELIVER: an interactive artifact (viewer, AE-style timeline, music +
MP4 download) and a rendered MP4 with music under 30 MB.
Show me screenshots before each expensive step.
```

<details><summary>中文译文</summary>

```text
做一个循环的「无限缩放」动画，After Effects 风格：镜头穿过一件件复古物件，从一片风景飞到另一片风景。

外观：复古拼贴风格的写实照片风景 + 黑白报纸剪贴物件（半色调网点、白色纸边、柔和阴影）。胶片颗粒、暗角、光线闪烁。

世界（循环）：雪山 → 怀表（挂在表链上摆动）→ 海崖 → 箱式相机镜头 → 沙漠沙丘 → 放大镜 → 雾湖 → 手镜 → 回到开头。
点缀：漂浮的帽子、电话、雨伞、留声机、钥匙；一个 1950 年代的男人朝怀表走去；一头鲸鱼游过海崖上方的天空。

做法：
- 所有东西都通过 Magnific MCP 生成（Seedream 5 Pro 生成风景，GPT 2.5 生成透明底剪贴物件，深度图，Kling 2.5 做动画，Lyria 3 做音乐）。先列出要生成的内容和点数花费，等我确认后再开始。
- 根据深度图把每片风景拆成 3 个深度层，并补全被遮住的区域。视差：图层缩放 = camera^Z，Z 在 0.45 到 1.22 之间。
- 每个「传送门」的玻璃里装着下一个世界；当它填满画面时无缝切换。
- 匀速：朝一个固定点做指数缩放，每段的时长与 log(zoom) 成正比。逐帧检查切换点。
- 男人和鲸鱼：在纯绿色（#00B140）背景上生成，用 Kling 原地做动画，逐帧抠像，做成无缝循环（需要的话来回播放）。
- 剪贴物件以 15 fps 动（一拍二）。
- 20 s 循环，1920×1080，30 fps。音乐：96 BPM，剪成正好 8 小节 = 20 s。

交付：一个交互式 artifact（查看器、AE 风格的时间线、音乐 + MP4 下载），以及一个带音乐、小于 30 MB 的渲染好的 MP4。
每个花钱的步骤之前，先给我看截图。
```

</details>

<sub>Author: 1,500 Magnific credits in total.</sub>

<sub>Also rendered from this prompt by: [@koldo2k](https://x.com/koldo2k/status/2103129347791986942)</sub>

[Original post ↗](https://x.com/koldo2k/status/2103129343253778767) · Prompt posted in [this reply](https://x.com/koldo2k/status/2103129347791986942).

---

### Word-seeded cosmic genesis animation

<a href="https://x.com/MiaAI_lab/status/2103837519615774895"><img src="https://pbs.twimg.com/amplify_video_thumb/2103835194968973312/img/vTWjv7AbUxDEVaTy.jpg" alt="Word-seeded cosmic genesis animation" width="480"></a>

[@MiaAI_lab](https://x.com/MiaAI_lab) · 2026-09-26 · 🔖 747 · ▶ 75.3k · `One-shot` · Web Audio

A real-time audiovisual piece where a typed word seeds a universe of shader-drawn stars, galaxy and planet, with live Web Audio music and no asset files.

```text
Build me something when people see it, they will say "Wow". Must be immersive, when people see it, they will be stunned by what they see.

This can be a video, or anything else you can think of.

Be creative. Go wild. Dig deep.

No AI slop. Something unique, think outside of the box. Think big. Think amazing. Something no other model done before.

Be proud. Show your best. Don't disappoint.
```

<details><summary>中文译文</summary>

```text
给我做一个东西，让人看到时会说「Wow」。必须有沉浸感，让人看到时被眼前的画面震住。

它可以是一段视频，也可以是你能想到的任何别的东西。

要有创意。放开了做。往深里挖。

不要 AI 垃圾。要独特，跳出框框思考。往大处想。往惊艳处想。做一个其他模型从没做过的东西。

要有骄傲感。拿出你最好的水平。别让我失望。
```

</details>

<sub>Author: one run.</sub>

[Original post ↗](https://x.com/MiaAI_lab/status/2103837519615774895) · Prompt posted in [this reply](https://x.com/MiaAI_lab/status/2103837523952763081).

---

### Morphing journey from creature to cosmos

<a href="https://x.com/leo_xiaolei/status/2102724347446305104"><img src="https://pbs.twimg.com/amplify_video_thumb/2102724181070839808/img/tpN8vCDfQk3W-WYg.jpg" alt="Morphing journey from creature to cosmos" width="480"></a>

[@leo_xiaolei](https://x.com/leo_xiaolei) · 2026-09-23 · 🔖 140 · ▶ 18.5k · `Spec` · Canvas · Three.js

A 30-second hand-drawn-style Canvas film where each scene morphs into the next, from creature to neurons, prism, sunflower, galaxy, black hole and earthrise, following a reference video.

```text
你现在是 Claude Opus 5.5，作为资深创意编程工程师（Creative Coder）、动态设计师（Motion Designer）与前端动画工程师。
你的任务是复现我所提供的参考视频中的视觉语言、节奏律动、转场逻辑以及整体氛围质感。
核心目标不是做一个常规网页。
核心目标是使用代码构建一部全程序化生成、具备电影质感且能够自动播放的动画短片。
最终成片应呈现出精致的手作动态设计（Motion Design）质感，而非一堆网页组件的拼接。
1. 项目目标
基于参考视频，构建一部时长 25–30 秒的程序化动画短片。
整段动画需串联多个视觉意象：
可爱角色
→ 神经元 / 电流脉冲结构
→ 三棱镜与彩虹色散
→ 几何色彩构型
→ 向日葵
→ 螺旋星系
→ 黑洞
→ 宇宙隧道
→ 地球升起（地出）
→ 回归角色
最核心的要求：
绝对不要做成互相割裂的幻灯片切换。
每一个场景都必须自然地在视觉上形变过渡至下一个场景。
运用手段包括：
形状渐变（Morphing）
粒子过渡（Particle transitions）
缩放过渡（Scale transitions）
镜头推进（Camera pushes）
径向展开过渡（Radial transitions）
溶解渗透（Dissolves）
实体到实体的几何形变（Object-to-object transformations）
色彩连续性（Color continuity）
运动动量延续（Motion continuity）
整部动画应当呈现为一次连贯流动的“意识流”。
2. 技术栈
技术选用：
Vite
TypeScript
HTML Canvas 2D
requestAnimationFrame
确定性时间轴系统（Deterministic timeline system）
程序化图形生成（Procedural graphics）
可复用的场景模块
仅在对以下视觉实现有实质性帮助时，才允许引入 Three.js：
星系
黑洞
地球
镜头景深
切勿无端引入重型依赖库。
除非有不可替代的理由，否则避免使用 React。
这是一项动画短片工程，而非 UI 应用。
3. 画布参数设定
设计基准分辨率：1920 × 1080
画面宽高比：16:9
目标帧率：30 FPS
动画必须支持自适应响应式缩放，同时严格保持 16:9 的设计坐标系。
必须正确处理 devicePixelRatio，确保动画在高分屏（Retina / High-DPI）上清晰锐利。
4. 视觉风格
参考范本具有插画风科普动画的质感。
目标视觉特征：
手绘质感
微带瑕疵的不规则形状
细微的线条抖动感（Line wobble）
柔和的肌理纹理
有机自然而非机械生硬的几何体
灵动俏皮却不失高级感
干净通透的构图
清晰鲜明的剪影造型
克制但极具表现力的配色方案
避免出现：
泛滥的通用 SaaS 插画风
扁平化企业图标感
冗余的 UI 界面元素
拟真写实风格（Photorealism）
赛博朋克美学
过度的霓虹光污染
千篇一律的 AI 生成式渐变
带有素材库库感的素材
5. 配色导向
主背景色：
暖奶油色 / 米白色
例如：#F2E8CF
深色宇宙场景：
深海蓝
暗紫色
近乎纯黑的夜空蓝
点缀高光色：
橙色
向日葵黄
紫罗兰
青色
洋红
柔红
克制且克制地使用渐变色。
色彩在不同场景间应保持过渡流动，而非突兀瞬变。
6. 肌理与质感
生成细腻的程序化纸张质感。
可选实现路径：
低透明度的随机噪点
背景亮度的细微不均
轻微的颗粒感叠加层（Grain overlay）
质感需清晰可感知，但绝不能喧宾夺主。
禁止加载体积庞大的纸张实拍贴图资源。
尽量全部采用程序化计算生成。
7. 动画时间轴
搭建统一的中控时间轴系统。
时间参考规划：
0.0s – 4.0s：角色登场
4.0s – 7.5s：神经元 / 电流脉冲网络
7.5s – 10.0s：三棱镜 / 光线色散
10.0s – 13.5s：色彩几何 → 向日葵
13.5s – 17.0s：向日葵 → 螺旋星系
17.0s – 20.5s：星系 → 黑洞
20.5s – 23.5s：黑洞 → 宇宙隧道 / 光柱
23.5s – 27.0s：地出（Earth Rise）
27.0s – 30.0s：回归角色
以上时间分配非死板硬性规定，若有助于增强视觉韵律与节奏感，可按需微调。
8. 场景 01 — 角色
时长： 约 0–4 秒。
绘制一个简洁可爱的矩形橙色小生物。
特征：
圆角矩形身体
小短腿
极简的面部特征
轻微不对称的手绘轮廓线条
亲和灵动的性格表现
动画细节：
小生物从画外缓缓走向画面中央。
行走动画需包含：
身体起伏颠簸（Bounce）
双腿交替摆动
轻微的身体倾角晃动
细腻的挤压与拉伸（Squash and stretch）
避免机械僵硬的匀速运动。
充分应用缓动曲线（Easing）与次级跟随动作（Secondary motion）。
场景尾声：
小生物对身旁浮现的事物产生反应。
该反应动作将直接触发下一阶段的转场。
9. 角色 → 神经元转场
不要生硬剪辑。
过渡方案：
角色身旁亮起一个微小的光点。
光点逐渐扩散放大。
细小的分支线开始从中抽枝蔓延。
镜头向前推近。
在逐渐膨胀铺展的网络对比下，角色身形显现得越来越小。
最终，神经元脉络结构铺满整个屏幕。
10. 场景 02 — 神经网络
时长： 约 4–7.5 秒。
具象化一种介于以下元素之间的视觉形态：
神经元 / 生物电 / 分支生物形态 / 闪电脉冲。
使用程序化分形/分支算法生成。
节点伴随脉冲呼吸。
信号流沿各个分支游走传导。
要求：
动态电脉冲流动
有机自然的分支几何体
微小的飞溅火花粒子
线条粗细富于节奏变化
兼具可控的随机感
切勿做成千篇一律的机器学习拓扑网络拓扑图。
它应当充满生物活力与能量感。
11. 神经元 → 三棱镜转场
选中其中一条极为明亮的电脉冲分支。
让这条分支逐渐拉直伸展。
流动其中的能量凝聚为一束纯净的白色光束。
神经网络的其余部分逐渐消隐在暗色背景中。
白光光束横穿画面。
精准投射射入一座三角形三棱镜。
12. 场景 03 — 三棱镜
时长： 约 7.5–10 秒。
绘制一个手绘透明感的三棱镜。
白光自一侧射入。
经三棱镜折射并色散为：
红、橙、黄、绿、青、蓝、紫。
不要只画死板固定的彩虹线。
需制作动态效果：
光束到达的冲击动态
三棱镜受光泛出的辉光
色散铺开的过程
细微的折射光线游移
柔和的光晕泛光（Bloom）
展开的光谱将作为承接后续画面的关键转场媒介。
13. 三棱镜 → 色彩几何
折射出的彩虹光束发生弯曲。
逐步转化为同心圆弧。
圆弧相互嵌套，化作多层旋转的同心圆环。
镜头向视觉中心推近。
三棱镜自然消隐退出视野。
14. 场景 04 — 色彩光环
时长： 约 10–11.5 秒。
构建层层嵌套的彩色同心圆环。
运动方式：
缓慢旋转
正反方向交错旋转
微弱的呼吸式缩放
有机微动的抖动摆动（Wobble）
圆环线条需带有轻微的手作不完美质感。
避免数学上绝对冷硬工整的圆周。
15. 光环 → 向日葵
缓慢改变圆环的几何拓扑结构。
外侧圆环渐变分离为独立的花瓣。
中心圆环转化为密布的向日葵葵花籽花盘。
黄色逐渐占据视觉主导。
整个演化形变过程需清晰可见。
避免使用透明度淡入淡出（Crossfade）的偷懒手法。
让观者能够直观看到一种几何形态如何演变为另一种生命形态。
16. 场景 05 — 向日葵
时长： 约 11.5–14 秒。
生成一朵风格化的程序化向日葵。
视觉构成：
明亮的金黄花瓣
温暖橙黄的花心
深色螺旋状排列的花籽
隐约可见的纤细花茎或植物形态
动画表现：
花瓣舒展盛放
轻柔的生命呼吸感
整体微微旋转
籽粒螺旋排列运动
若条件允许，葵花籽可采用斐波那契数列 / 黄金角分布算法生成。
17. 向日葵 → 螺旋星系
这将是整部短片视觉张力最强的转场之一。
向日葵中心加速旋转。
外围花瓣逐渐剥离脱散。
每一片花瓣解构为一颗发光的星尘粒子。
中心的花籽阵列向外螺旋扩张。
色调柔和渐次推移：
黄色
→ 橙色
→ 紫色
→ 深蓝
整朵向日葵无缝蜕变为一座旋转的旋涡星系。
切忌使用简单的画面叠化淡出。
18. 场景 06 — 螺旋星系
时长： 约 14–17 秒。
构建一座程序化生成的旋涡星系。
要求：
在性能允许的前提下布置成千上万个微型粒子
采用对数螺线 / 旋臂分布规律
极度明亮致密的星系核心
错落点缀的背景繁星
呈现深邃的空间纵深感
镜头缓慢向前推进
整体缓慢转动
粒子需拥有丰富的透明度梯次与大小半径。
避免机械匀质的死板星点分布。
使用带有固定种子（Seeded Random）的随机算法，确保每次播放呈现的画面细节完全一致。
19. 星系 → 黑洞
星系中心区域的自转角速度逐渐加快。
中央区域急剧暗沉塌缩。
周围粒子开始加速环绕运转。
沿切线方向将运动的粒子微微拉伸拖尾。
中央的纯黑视界向外扩张。
整个星系逐步转化为狂暴的吸积盘。
20. 场景 07 — 黑洞
时长： 约 17–20.5 秒。
构建一座风格化的黑洞。
要素：
吞噬一切的纯黑球体核心
炽热发光的吸积盘
橙金交织的内层强光
紫蓝晕染的外围辉光
沿弯曲引力轨迹运动的粒子流
可选实现：做近似引力透镜效果的视觉扭曲。
无需苛求物理层面上严格精确的广义相对论模拟。
以呈现上乘的视觉美感为第一优先级。
镜头向视界面缓慢平稳推近。
21. 黑洞 → 宇宙隧道
镜头彻底穿透坠入中心黑暗。
吸积盘受透视拉伸拉长为同心光环。
周围星尘被径向拉伸成向外散射的放射线。
营造出跃入时空隧道的穿梭沉浸感。
22. 场景 08 — 宇宙隧道
时长： 约 20.5–23.5 秒。
构建由同心发光环或粒子光环构成的深邃通道。
镜头高速向前飞行穿梭。
重点注意：
严禁使用老套庸俗的科幻“超空间跃迁（Hyperspace）”特效。
严格维系短片一贯的插画手绘风味。
临近该段尾声：
通道中央骤然凝聚为一束笔直刺目的白色垂直光柱。
23. 隧道 → 地球转场
这道垂直光柱横向延展放平。
其底边下沉拉平，化作一条地平线。
地平线下方的大片幽黑转化为静谧的月球表面。
一抹深邃纯净的幽蓝辉光在地平线后方缓缓漫溢升腾。
24. 场景 09 — 地出（Earth Rise）
时长： 约 23.5–27 秒。
呈现一幅电影质感的大幅画面：一颗蔚蓝星球自幽暗的月球地平线后缓缓升起。
地球细节包含：
泛着光晕的蔚蓝大气层
高度概括简化的云气流动
提炼简化的陆地轮廓
细腻柔和的外缘辉光
除非绝对必要，否则严禁使用外部实拍 NASA 图片贴图。
优先采用纯代码程序化 / 矢量风格化方式渲染。
月表前景保持绝大部分深邃剪影。
匹配极度舒缓沉稳的运镜节奏。
此处应作为整部影片中最空灵宁静的高光时刻。
25. 地球 → 角色转场
镜头快速向地球表面的一处极亮星斑推近。
那抹幽蓝辉光凝聚为一颗极小的球形光点。
光球进一步缩小。
背景底色褪去深黑，无缝褪回最初温润的暖奶油色。
光点轻盈落在了最初那只小生物的身旁。
镜头缓缓拉远回撤。
26. 尾声终幕
画面回归最初那只橙色小生物。
小生物转过头，注视着身旁落下的微光小点。
反应动作建议：
眨一眨眼睛
露出微笑

轻轻雀跃蹦跳一下
```

<details><summary>English translation</summary>

```text
You are now Claude Opus 5.5, acting as a senior Creative Coder, Motion Designer and front-end animation engineer.
Your task is to reproduce the visual language, rhythm, transition logic and overall atmosphere and texture of the reference video I provide.
The core goal is not to make an ordinary web page.
The core goal is to use code to build a fully procedurally generated, cinematic animated short that plays automatically.
The final film should have the refined feel of handcrafted Motion Design, not a pile of web components stitched together.
1. Project goal
Based on the reference video, build a procedural animated short 25–30 seconds long.
The whole animation must string together several visual images:
A cute character
→ Neurons / electrical pulse structure
→ Prism and rainbow dispersion
→ Geometric color composition
→ Sunflower
→ Spiral galaxy
→ Black hole
→ Cosmic tunnel
→ Earthrise
→ Back to the character
The most important requirement:
Absolutely do not make it a series of disconnected slide transitions.
Every scene must visually morph naturally into the next.
Techniques include:
Morphing
Particle transitions
Scale transitions
Camera pushes
Radial transitions
Dissolves
Object-to-object transformations
Color continuity
Motion continuity
The whole animation should feel like one continuous, flowing "stream of consciousness".
2. Tech stack
Technology choices:
Vite
TypeScript
HTML Canvas 2D
requestAnimationFrame
Deterministic timeline system
Procedural graphics
Reusable scene modules
Three.js may be brought in only when it substantially helps with these visuals:
Galaxy
Black hole
Earth
Camera depth of field
Never pull in heavy dependencies for no reason.
Avoid React unless there is an irreplaceable reason.
This is an animated short film project, not a UI application.
3. Canvas settings
Design base resolution: 1920 × 1080
Aspect ratio: 16:9
Target frame rate: 30 FPS
The animation must support adaptive responsive scaling while strictly keeping the 16:9 design coordinate system.
devicePixelRatio must be handled correctly so the animation stays crisp on high-density (Retina / High-DPI) screens.
4. Visual style
The reference has the feel of an illustrated popular-science animation.
Target visual traits:
Hand-drawn feel
Slightly imperfect, irregular shapes
Subtle line wobble
Soft textures
Organic rather than mechanically rigid geometry
Playful yet still premium
Clean, airy composition
Clear, strong silhouettes
A restrained but highly expressive palette
Avoid:
Overused generic SaaS illustration style
Flat corporate-icon feel
Redundant UI elements
Photorealism
Cyberpunk aesthetics
Excessive neon light pollution
Cookie-cutter AI-generated gradients
Anything that looks like stock assets
5. Color direction
Main background:
Warm cream / off-white
e.g. #F2E8CF
Dark cosmic scenes:
Deep navy
Dark purple
Near-black night-sky blue
Accent highlights:
Orange
Sunflower yellow
Violet
Cyan
Magenta
Soft red
Use gradients with restraint, real restraint.
Colors should flow across scenes rather than switching abruptly.
6. Texture and material
Generate a delicate procedural paper texture.
Possible approaches:
Low-opacity random noise
Subtle unevenness in background brightness
A light grain overlay
The texture should be clearly perceptible but must never steal the show.
Do not load large photographed paper texture assets.
Generate everything procedurally as far as possible.
7. Animation timeline
Build a single central timeline system.
Reference timing plan:
0.0s – 4.0s: Character enters
4.0s – 7.5s: Neuron / electrical pulse network
7.5s – 10.0s: Prism / light dispersion
10.0s – 13.5s: Color geometry → sunflower
13.5s – 17.0s: Sunflower → spiral galaxy
17.0s – 20.5s: Galaxy → black hole
20.5s – 23.5s: Black hole → cosmic tunnel / light pillar
23.5s – 27.0s: Earthrise (Earth Rise)
27.0s – 30.0s: Back to the character
These timings are not rigid rules; adjust them as needed if that strengthens the visual rhythm and pacing.
8. Scene 01 — Character
Duration: about 0–4 seconds.
Draw a simple, cute rectangular little orange creature.
Features:
Rounded-rectangle body
Short little legs
Minimal facial features
Slightly asymmetric hand-drawn outline
A friendly, lively personality
Animation details:
The creature walks slowly from off-screen to the center of the frame.
The walk must include:
Body bounce
Alternating leg swings
A slight body tilt sway
Subtle squash and stretch
Avoid mechanical, rigid constant-speed motion.
Make full use of easing curves and secondary motion.
End of the scene:
The creature reacts to something appearing beside it.
That reaction directly triggers the next transition.
9. Character → neurons transition
No hard cut.
Transition plan:
A tiny point of light lights up beside the character.
The point gradually spreads and grows.
Thin branch lines begin to sprout and spread from it.
The camera pushes forward.
Against the expanding network, the character looks smaller and smaller.
Finally, the neuron structure fills the whole screen.
10. Scene 02 — Neural network
Duration: about 4–7.5 seconds.
Visualize a form somewhere between these:
neurons / bioelectricity / branching organic forms / lightning pulses.
Generate it with a procedural fractal / branching algorithm.
Nodes pulse and breathe.
Signal flows travel along each branch.
Requirements:
Dynamic electrical pulse flow
Organic, natural branching geometry
Tiny splashing spark particles
Line thickness with rhythmic variation
Controlled randomness
Never make it a cookie-cutter machine-learning network topology diagram.
It should be full of biological vitality and energy.
11. Neurons → prism transition
Pick one extremely bright pulse branch.
Let that branch gradually straighten and stretch out.
The energy flowing in it condenses into a pure white beam of light.
The rest of the neural network fades into the dark background.
The white beam crosses the frame.
It shoots precisely into a triangular prism.
12. Scene 03 — Prism
Duration: about 7.5–10 seconds.
Draw a hand-drawn, see-through prism.
White light enters from one side.
The prism refracts and disperses it into:
red, orange, yellow, green, cyan, blue, violet.
Don't just draw stiff, static rainbow lines.
Animate:
The impact as the beam arrives
The prism's glow as it catches the light
The dispersion spreading out
Subtle drifting of the refracted rays
Soft Bloom
The spread-out spectrum is the key transition medium into what follows.
13. Prism → color geometry
The refracted rainbow beams bend.
They gradually turn into concentric arcs.
The arcs nest into one another, becoming multiple layers of rotating concentric rings.
The camera pushes toward the visual center.
The prism naturally fades out of view.
14. Scene 04 — Color rings
Duration: about 10–11.5 seconds.
Build nested layers of colored concentric rings.
Motion:
Slow rotation
Alternating clockwise and counter-clockwise rotation
Faint breathing scale
Small organic Wobble
The ring lines should have a slight handmade imperfection.
Avoid mathematically perfect, cold, exact circles.
15. Rings → sunflower
Slowly change the geometric topology of the rings.
The outer rings gradually separate into individual petals.
The center rings turn into a dense sunflower seed head.
Yellow gradually takes over the frame.
The whole evolution must be clearly visible.
Avoid the lazy trick of an opacity Crossfade.
Let the viewer see directly how one geometric form evolves into a living form.
16. Scene 05 — Sunflower
Duration: about 11.5–14 seconds.
Generate a stylized procedural sunflower.
Visual makeup:
Bright golden petals
A warm orange-yellow center
Dark seeds arranged in spirals
A faintly visible slender stem or plant form
Animation:
Petals unfolding into bloom
A gentle, living breath
A slight overall rotation
Spiral motion of the seed arrangement
If possible, generate the seeds with a Fibonacci / golden-angle distribution.
17. Sunflower → spiral galaxy
This will be one of the most visually intense transitions in the whole short.
The sunflower's center spins faster.
The outer petals gradually peel off and scatter.
Each petal breaks down into a glowing stardust particle.
The central seed array expands outward in a spiral.
The hues shift softly, step by step:
Yellow
→ Orange
→ Purple
→ Deep blue
The whole sunflower transforms seamlessly into a rotating spiral galaxy.
Never use a simple cross-dissolve fade.
18. Scene 06 — Spiral galaxy
Duration: about 14–17 seconds.
Build a procedurally generated spiral galaxy.
Requirements:
Thousands of tiny particles, as far as performance allows
A logarithmic spiral / spiral-arm distribution
An extremely bright, dense galactic core
Scattered background stars
A deep sense of spatial depth
The camera slowly pushes forward
The whole thing slowly rotates
Particles need a rich range of opacities and sizes.
Avoid a mechanical, uniform, rigid distribution of stars.
Use a random algorithm with a fixed seed (Seeded Random) so every playback shows exactly the same details.
19. Galaxy → black hole
The rotation speed of the galaxy's central region gradually increases.
The center rapidly darkens and collapses.
Surrounding particles start orbiting faster.
Stretch moving particles slightly along the tangent into trails.
The pure black horizon at the center expands outward.
The whole galaxy gradually turns into a violent accretion disk.
20. Scene 07 — Black hole
Duration: about 17–20.5 seconds.
Build a stylized black hole.
Elements:
A pure black spherical core that swallows everything
A blazing, glowing accretion disk
Intense orange-gold light on the inner layer
Purple-blue glow bleeding at the outer edge
Particle streams moving along curved gravitational paths
Optional: an approximate gravitational-lensing visual distortion.
No need for a strictly physically accurate general-relativity simulation.
Visual beauty comes first.
The camera pushes slowly and steadily toward the event horizon.
21. Black hole → cosmic tunnel
The camera plunges all the way through into the central darkness.
Perspective stretches the accretion disk into concentric rings of light.
The surrounding stardust stretches radially into outward-scattering rays.
Create an immersive feeling of leaping into a space-time tunnel.
22. Scene 08 — Cosmic tunnel
Duration: about 20.5–23.5 seconds.
Build a deep passage made of concentric glowing rings or particle rings.
The camera flies forward at high speed.
Important:
Strictly no cliché, cheesy sci-fi "Hyperspace" jump effects.
Keep the short's consistent illustrated, hand-drawn flavor.
Near the end of this segment:
The center of the tunnel suddenly condenses into a straight, dazzling vertical pillar of white light.
23. Tunnel → Earth transition
This vertical pillar of light stretches out sideways and lies flat.
Its bottom edge sinks and flattens into a horizon line.
The large dark area below the horizon turns into a quiet lunar surface.
A deep, pure blue glow slowly spills and rises from behind the horizon.
24. Scene 09 — Earthrise (Earth Rise)
Duration: about 23.5–27 seconds.
Present a large cinematic frame: a blue planet slowly rising from behind the dark lunar horizon.
Earth details include:
A glowing blue atmosphere
Highly simplified cloud flow
Simplified continent outlines
A delicate, soft rim glow
Unless absolutely necessary, do not use external real NASA photo textures.
Prefer pure code, procedural / vector-stylized rendering.
Keep the lunar foreground mostly a deep silhouette.
Match it with extremely slow, calm camera movement.
This should be the most ethereal, serene high point of the whole film.
25. Earth → character transition
The camera quickly pushes toward a very bright spot of light on the Earth's surface.
That deep blue glow condenses into a tiny spherical point of light.
The light ball shrinks further.
The background loses its deep black and seamlessly fades back to the original warm cream color.
The point of light lands lightly beside the little creature from the start.
The camera slowly pulls back.
26. Finale
The frame returns to the orange little creature from the start.
The creature turns its head and looks at the tiny point of light that has landed beside it.
Suggested reactions:
Blink
Smile

Give a light little hop
```

</details>

<sub>Inputs: Reference video</sub>

[Original post ↗](https://x.com/leo_xiaolei/status/2102724347446305104)

---

### The best water simulation it can make

<a href="https://x.com/Avenoxai/status/2102500841097756743"><img src="https://pbs.twimg.com/amplify_video_thumb/2102500422355185664/img/lZxF7e1Imu3jot_Z.jpg" alt="The best water simulation it can make" width="480"></a>

[@Avenoxai](https://x.com/Avenoxai) · 2026-09-22 · 🔖 124 · ▶ 39.9k · `One-shot`

A water simulation made live on stream from a one-line Turkish prompt; the post shows one of the three simulations Opus produced.

```text
Bana yapabildiğin en iyi su simülasyonunu yap
```

<details><summary>English translation</summary>

```text
Make me the best water simulation you can
```

</details>

[Original post ↗](https://x.com/Avenoxai/status/2102500841097756743)

---

### Ray-marched film of a pelican riding a bicycle

<a href="https://x.com/AxtonLiu/status/2103119648271290566"><img src="https://pbs.twimg.com/amplify_video_thumb/2103119572568313856/img/vedd97bTOFX7F0Qg.jpg" alt="Ray-marched film of a pelican riding a bicycle" width="480"></a>

[@AxtonLiu](https://x.com/AxtonLiu) · 2026-09-24 · 🔖 57 · ▶ 10k · `Brief`

A 38-second pelican-on-a-bicycle film for which Opus wrote its own GPU ray-marching renderer; pier, sea, sky and music all come from code, 1140 frames.

```text
每次一个新的模型出来呢，大家都让它去画 “鹈鹕骑自行车” 来判断这个模型的空间能力，基本上都是用 HTML、SVG 来画动画。当我实在看得都有审美疲劳了，我希望你能画一个最复杂、最精细、最精美的 “鹈鹕骑自行车”的动画视频，你可以用任何的技术，不用着急，画一天都可以。
```

<details><summary>English translation</summary>

```text
Every time a new model comes out, everyone asks it to draw a “pelican riding a bicycle” to judge its spatial ability, and it is basically always an animation drawn with HTML and SVG. I am honestly tired of seeing them, so I want you to draw the most complex, most detailed, most beautiful “pelican riding a bicycle” animation video. You can use any technique. No rush, you can spend a whole day drawing it.
```

</details>

<sub>Author: generated from one prompt in one go.</sub>

[Original post ↗](https://x.com/AxtonLiu/status/2103119648271290566)

---

### Real-time fireworks and light particle show

<a href="https://x.com/FornYapayZeka/status/2102888241443795431"><img src="https://pbs.twimg.com/amplify_video_thumb/2102871387123724288/img/VWZ6gVvt5QbO7k5x.jpg" alt="Real-time fireworks and light particle show" width="480"></a>

[@FornYapayZeka](https://x.com/FornYapayZeka) · 2026-09-23 · 🔖 36 · ▶ 5.3k · `Brief`

A 38-second real-time fireworks and glowing particle show built only in code, where Opus picks the setting, art direction and a replayable finale.

```text
Yapabileceğin en etkileyici havai fişek veya ışıklı parçacık gösterisini üret. Ortamı ve sanat yönünü sen seç. Tek tip küçük patlamaları çoğaltmak yerine ritmi, derinliği, ışığın çevreye etkisini ve unutulmaz bir final anını tasarla. Gösteri canlı çalışsın; kullanıcı finali tekrar oynatabilsin.

Yaratıcı seçimler senin: sahne, sanat yönü, kamera, mekanik, teknoloji ve etkileşimi önceden belirlenmiş sıradan kalıplara sıkıştırma. İlk akla gelen sıradan web demosuyla yetinme: önce kendi alanında birkaç fikri kısaca tart, videoda en güçlü görünecek özgün olanı seç, sonra onu çalışan bir ürüne dönüştür. Konuyu olduğundan kolay gösteren dekoratif taklit kabul edilmez. Sinematik ve estetik seçimler sonuçta görülsün.
```

<details><summary>English translation</summary>

```text
Produce the most impressive fireworks or luminous particle show you can make. Choose the setting and the art direction yourself. Instead of multiplying identical small explosions, design the rhythm, the depth, the effect of the light on its surroundings, and an unforgettable finale moment. The show should run live; the user should be able to replay the finale.

The creative choices are yours: do not squeeze the scene, art direction, camera, mechanics, technology and interaction into predetermined ordinary patterns. Do not settle for the first ordinary web demo that comes to mind: first briefly weigh a few ideas in your own field, pick the original one that will look strongest on video, then turn it into a working product. A decorative imitation that makes the subject look easier than it is will not be accepted. Let the cinematic and aesthetic choices be visible in the result.
```

</details>

[Original post ↗](https://x.com/FornYapayZeka/status/2102888241443795431) · Prompt posted in [this reply](https://x.com/FornYapayZeka/status/2102888242295242975).

---

### Meteor airburst flattening a forest

<a href="https://x.com/FornYapayZeka/status/2102971287224135914"><img src="https://pbs.twimg.com/amplify_video_thumb/2102873199868342272/img/XvykHznZiFho8-eo.jpg" alt="Meteor airburst flattening a forest" width="480"></a>

[@FornYapayZeka](https://x.com/FornYapayZeka) · 2026-09-24 · 🔖 15 · ▶ 3.4k · `Brief`

A replayable all-code simulation: a meteor explodes over a forest, a pressure model decides which of 240,000 trees fall, then a satellite damage map appears.

```text
Yapabileceğin en etkileyici patlama efektini ve onu taşıyacak özgün sahneyi üret. Ölçeği, ortamı ve görsel dili sen seç. Patlamanın başlangıcı, kuvvetin yayılması ve ardında bıraktığı değişim izlenebilir olsun; tek karelik parlama veya rastgele parçacık yağmuru yeterli değil. Kullanıcı bunu tekrar başlatabilsin ve etkisini farklı açıdan görebilsin.

Yaratıcı seçimler senin: sahne, sanat yönü, kamera, mekanik, teknoloji ve etkileşimi önceden belirlenmiş sıradan kalıplara sıkıştırma. İlk akla gelen sıradan web demosuyla yetinme: önce kendi alanında birkaç fikri kısaca tart, videoda en güçlü görünecek özgün olanı seç, sonra onu çalışan bir ürüne dönüştür. Konuyu olduğundan kolay gösteren dekoratif taklit kabul edilmez. Sinematik ve estetik seçimler sonuçta görülsün.
```

<details><summary>English translation</summary>

```text
Produce the most impressive explosion effect you can, and an original scene to carry it. Choose the scale, the setting and the visual language yourself. The start of the explosion, the spread of the force and the change it leaves behind should all be traceable; a single-frame flash or a random shower of particles is not enough. The user should be able to restart it and see its effect from a different angle.

The creative choices are yours: do not squeeze the scene, art direction, camera, mechanics, technology and interaction into predefined ordinary templates. Do not settle for the ordinary web demo that comes to mind first: first briefly weigh a few ideas in your own domain, pick the original one that will look strongest in the video, then turn it into a working product. A decorative imitation that makes the subject look easier than it is will not be accepted. Let the cinematic and aesthetic choices show in the result.
```

</details>

[Original post ↗](https://x.com/FornYapayZeka/status/2102971287224135914) · Prompt posted in [this reply](https://x.com/FornYapayZeka/status/2102971287891009707).

---

### Rocket launch scene, four-model comparison

<a href="https://x.com/EnvolDev/status/2103144263735562388"><img src="https://pbs.twimg.com/amplify_video_thumb/2103144186962960386/img/tmFHMZ2kO2IT-auI.jpg" alt="Rocket launch scene, four-model comparison" width="480"></a>

[@EnvolDev](https://x.com/EnvolDev) · 2026-09-24 · 🔖 11 · ▶ 7.8k · `One-shot`

A rocket launch animation from a four-word prompt, shown side by side with the GPT-6 Astra, Sol and Luna results.

```text
Build a rocket launch.
```

<details><summary>中文译文</summary>

```text
做一个火箭发射。
```

</details>

<sub>Author: Opus 5.5 finished in about 10 minutes.</sub>

[Original post ↗](https://x.com/EnvolDev/status/2103144263735562388)

---

### Night train crossing a mountain viaduct

<a href="https://x.com/Artless101/status/2102598487170822281"><img src="https://pbs.twimg.com/amplify_video_thumb/2102598400742924288/img/pwUVM1tgSfP1dueM.jpg" alt="Night train crossing a mountain viaduct" width="480"></a>

[@Artless101](https://x.com/Artless101) · 2026-09-23 · 🔖 10 · ▶ 5.1k · `Spec` · Three.js · WebGL · Web Audio

A procedural Three.js night scene of a burgundy train looping over a stone viaduct, with four cameras, lighting presets and Web Audio ambience.

```text
Create a polished, fully interactive 3D artwork called "Nocturne - The Highland Night Train" using Three.js and WebGL. Deliver the entire experience as one standalone HTML file that opens directly in Chrome. Generate the models, materials and textures procedurally, and embed dependencies so the final file can also work offline. Start from scratch and give the scene its own visual identity.

ART DIRECTION
An elegant burgundy night express crosses a monumental curved stone viaduct above a deep alpine valley. Dense conifer forests, a winding river, distant cottages and rugged snow-covered mountains surround the railway. Use a cinematic, carefully detailed miniature style, with cool moonlight, deep blue shadows and warm golden carriage windows. The result should feel like a finished interactive artwork, with thoughtful composition and readable details.

THE TRAIN
Build a convincing diesel locomotive and four passenger carriages. Use deep burgundy paint, cream stripes, brass handrails and charcoal roofs. Model rounded body panels, cab windows, front lamps, radiator grilles, roof fans, exhaust, walkways, steps, buffers, couplings, bogies, wheel flanges and suspension details. Include window frames, curtains and subtle passenger silhouettes. Keep windows and decorative parts visibly outside the body surfaces, without intersections or flickering.

RAILWAY AND MOVEMENT
Create a continuous elliptical railway loop supported by a tall masonry viaduct. Construct actual open arches, piers, individual arch stones, parapets, rails and sleepers. Add procedural stone variation and subtle surface relief. Supports must meet the terrain and the track must have no gaps.

Move the train at a believable, steady speed using an arc-length-parameterized route. Position and orient every carriage independently. Keep the wheels aligned with the rails and make bogies follow the track correctly through turns. Couplings must remain connected without overlapping carriages. Add restrained suspension movement, rotating wheels and exhaust that drifts away into world space.

ENVIRONMENT AND LIGHTING
Use thousands of efficiently instanced conifers with varied heights, shapes and colors. Sculpt irregular mountain ridges with snow on the upper slopes. Add atmospheric depth, a starry sky, a moon halo and a softly feathered headlight beam through the mist. Use warm windows, controlled bloom, soft shadows and subtle color grading. Preserve detail in the train and bridge instead of crushing them into black silhouettes.

INTERACTION
Provide four smoothly transitioning cameras: Cinematic, Train, Window Seat and Free Orbit. Let users rotate and zoom freely. Keep useful framing on both desktop and mobile.

Add distinctly different Moonlight, Blue Hour and First Light presets. Include play/pause, speed controls, a horn button, sound on/off, volume and an option to hide the interface. Use a restrained English-only interface with elegant typography and unobtrusive controls.

AUDIO AND QUALITY
Synthesize quiet railway ambience with Web Audio: a low engine rumble, gentle wheel rhythm, wind and a distant-sounding horn. Start audio only after a user interaction and respect the volume control.

Balance visual richness with smooth performance using instancing, geometry batching and sensible rendering limits. Test the finished HTML in desktop Chrome, capture screenshots, inspect the console and fix visible or technical issues. Verify every control, camera transitions, a complete train circuit, mobile resizing and direct offline opening. Return the final HTML file.
```

<details><summary>中文译文</summary>

```text
用 Three.js 和 WebGL 创作一件精致、完全可交互的 3D 艺术作品，名为“Nocturne - The Highland Night Train”。把整个体验做成一个能在 Chrome 中直接打开的独立 HTML 文件。模型、材质和纹理都用程序化方式生成，并内嵌依赖，让最终文件也能离线运行。从零开始，给场景一个独特的视觉风格。

美术方向
一列优雅的酒红色夜间快车驶过一座横跨深邃高山河谷的巨型弧形石拱高架桥。四周是茂密的针叶林、蜿蜒的河流、远处的小屋和嶙峋的雪山。采用电影感、细节考究的微缩模型风格，冷色月光、深蓝阴影、温暖的金色车窗。成品要像一件完成度很高的交互艺术品，构图用心，细节清晰可读。

列车
做一台逼真的柴油机车和四节客车车厢。使用深酒红色涂装、奶油色条纹、黄铜扶手和炭灰色车顶。建模圆润的车身面板、驾驶室车窗、前灯、散热格栅、车顶风扇、排气口、走道、踏板、缓冲器、车钩、转向架、轮缘和悬挂细节。加上窗框、窗帘和隐约的乘客剪影。车窗和装饰件要明显位于车身表面之外，不能穿插或闪烁。

铁路与运动
建一条连续的椭圆形环线铁路，由一座高大的砖石高架桥支撑。构建真正镂空的拱、桥墩、单块拱石、护墙、钢轨和枕木。加入程序化的石材变化和细微的表面起伏。桥墩要接到地面，轨道不能有缺口。

让列车以可信、平稳的速度沿按弧长参数化的路线行驶。每节车厢独立定位和定向。车轮要与钢轨对齐，转弯时转向架要正确跟随轨道。车钩必须保持连接，车厢不能互相重叠。加入克制的悬挂起伏、转动的车轮，以及飘散到世界空间中的尾气。

环境与光照
用数千棵高效实例化的针叶树，高度、形状和颜色各不相同。塑造不规则的山脊，高坡上覆盖积雪。加入大气纵深、星空、月晕，以及一道穿过薄雾、边缘柔和的车头灯光束。使用温暖的车窗光、受控的泛光（bloom）、柔和阴影和细腻的调色。保留列车和桥梁的细节，不要把它们压成一片黑色剪影。

交互
提供四个可平滑切换的镜头：Cinematic、Train、Window Seat 和 Free Orbit。用户可以自由旋转和缩放。在桌面端和移动端都保持合适的取景。

加入差异明显的 Moonlight、Blue Hour 和 First Light 预设。包含播放/暂停、速度控制、鸣笛按钮、声音开关、音量，以及隐藏界面的选项。界面克制、只用英文，字体优雅，控件不突兀。

音频与质量
用 Web Audio 合成安静的铁路环境音：低沉的引擎轰鸣、轻柔的车轮节奏、风声和听起来很远的汽笛。只在用户交互后才开始播放音频，并遵循音量控制。

用实例化、几何体合批和合理的渲染上限，在视觉丰富度和流畅性能之间取得平衡。在桌面版 Chrome 中测试完成的 HTML，截图、检查控制台，修复可见或技术上的问题。验证每个控件、镜头切换、列车完整跑一圈、移动端缩放和直接离线打开。返回最终的 HTML 文件。
```

</details>

[Original post ↗](https://x.com/Artless101/status/2102598487170822281) · Prompt posted in [this reply](https://x.com/Artless101/status/2102598632595701827).

---

### Pirate ship sailing a sunset ocean

[@vib3coded](https://x.com/vib3coded) · 2026-09-22 · 🔖 5 · ▶ 660 · `Spec`

A stylized real-time 3D scene of a pirate ship crossing a sunset ocean, with foam, wake and rigging, delivered as one HTML file the model tests itself.

```text
Create from scratch a fully interactive 3D scene of a pirate ship sailing across a dynamic ocean at sunset. The visual style should be cinematic and stylized rather than photorealistic, while still being exceptionally rich, detailed, polished, and visually sophisticated. Build the ship, ocean, sky, lighting, materials, sails, rigging, cannons, small structural details, sea foam, wake, particles, animation, camera work, composition, atmospheric depth, and color grading. The final result should feel like a premium, high-production 3D artwork, not a prototype, technical demo, or low-quality scene. Start from a completely blank page. Do not reuse or depend on any previous project or scene. You may create the assets yourself or use reliable, trusted, open-source assets and libraries when necessary. Mandatory requirements: No text of any kind may appear anywhere inside the scene. No titles, names, logos, descriptions, credits, labels, or control instructions in any language. Deliver the entire project as one final standalone page file that can be opened directly in a web browser, with assets embedded inside it as much as reasonably possible. The ocean, ship, sails, and camera must all be animated naturally and smoothly. Avoid artificial slow motion or sluggish movement. The ship should feel like it is genuinely moving through the water. Do not rely on primitive geometric shapes as the finished result. Build a visually convincing and detailed pirate ship, including a carefully shaped hull, masts, sails, rigging, ropes, cannons, railings, lanterns, deck structures, and clearly visible small-scale details. Lighting must reveal the ship's geometry and materials clearly. Create a rich sunset atmosphere, deep ocean shading, reflections, convincing sea foam, and a detailed sailing wake behind and around the vessel. Maintain a strong balance between visual quality and real-time performance, preserving smooth interaction and animation without making an obvious sacrifice in quality. Automatically use the most appropriate skills, tools, libraries, techniques, and available assets needed to achieve the best result. Do not wait for me to specify which technologies to use. Actually test the finished result in a desktop web browser. Capture visual screenshots, inspect the browser console for errors, and fix every visible or technical issue you find, including distorted geometry, black screens, failed asset loading, broken animation, poor composition, rendering artifacts, or camera problems. At the end, verify that the final file opens and works directly, that the scene contains no text whatsoever, and that there are no remaining runtime or loading errors. Then finish the task with only a brief response.
```

<details><summary>中文译文</summary>

```text
从零开始创建一个完全可交互的 3D 场景：一艘海盗船在日落时分驶过动态的海面。视觉风格要有电影感、风格化，而不是照片级写实，但仍然要极其丰富、细致、精致，视觉上足够讲究。船、海洋、天空、光照、材质、船帆、索具、火炮、细小的结构细节、海浪泡沫、尾迹、粒子、动画、运镜、构图、大气纵深和调色都要做出来。最终效果应该像一件高品质、高制作水准的 3D 艺术作品，而不是原型、技术演示或粗糙的场景。从一张完全空白的页面开始。不要复用或依赖任何之前的项目或场景。你可以自己制作素材，必要时也可以使用可靠、可信的开源素材和库。强制要求：场景中任何地方都不能出现任何文字。不要标题、名字、logo、说明、署名、标签，也不要任何语言的操作提示。整个项目以一个最终的独立页面文件交付，能直接在网页浏览器中打开，素材尽可能内嵌在文件里。海面、船、船帆和镜头都必须自然流畅地动起来。避免刻意的慢动作或拖沓的运动。船要让人感觉真的在水中前行。不要拿简单几何体当最终成品。做一艘视觉上可信、细节丰富的海盗船，包括精心塑形的船体、桅杆、船帆、索具、绳索、火炮、栏杆、灯笼、甲板结构，以及清晰可见的小尺度细节。光照必须把船的几何形状和材质清楚地展现出来。营造浓郁的日落氛围、深邃的海洋明暗、倒影、逼真的海浪泡沫，以及船身后方和四周细致的航行尾迹。在画面质量和实时性能之间保持好平衡，保证交互和动画流畅，又不明显牺牲质量。自动选用最合适的 skill、工具、库、技术和可用素材来达到最佳效果。不要等我指定用什么技术。真正在桌面网页浏览器里测试最终成果。截取画面截图，检查浏览器控制台里的错误，修复你发现的所有视觉或技术问题，包括几何变形、黑屏、素材加载失败、动画出错、构图不佳、渲染瑕疵或镜头问题。最后，确认最终文件能直接打开并正常运行，场景里完全没有文字，也没有残留的运行时或加载错误。然后只用简短的回复结束任务。
```

</details>

[Original post ↗](https://x.com/vib3coded/status/2102534606121746589)

---

### Particle-illustration Santa Monica beach

<a href="https://x.com/ishuagra02/status/2102920408743678129"><img src="https://pbs.twimg.com/amplify_video_thumb/2102920337184694272/img/7oyIS-xiio7Eiutr.jpg" alt="Particle-illustration Santa Monica beach" width="480"></a>

[@ishuagra02](https://x.com/ishuagra02) · 2026-09-24 · 🔖 3 · ▶ 902 · `One-shot`

A 3D Santa Monica beach drawn with thousands of glowing specks and ribbon strokes that shifts with the time of day; Opus also made its promo video.

```text
Create a stylistic 3D environment of a busy Santa Monica beach that adapts to the time of day. The art style must be a particle illustration, which uses thousands of tiny glowing specks rather than solid fills with flowing ribbon strokes behind figures to suggest motion.
```

<details><summary>中文译文</summary>

```text
创建一个风格化的 3D 环境：一片热闹的圣莫尼卡海滩，会随一天中的时段变化。画风必须是粒子插画，用成千上万个发光的小点代替实心填充，并在人物身后加上流动的飘带笔触来表现动感。
```

</details>

<sub>Author: 2–3 more prompts on top of this one.</sub>

[Original post ↗](https://x.com/ishuagra02/status/2102920408743678129) · Prompt posted in [this reply](https://x.com/ishuagra02/status/2102920888261742726).

---

### Self-running 3D Rube Goldberg machine

<a href="https://x.com/leogao25/status/2102544078927741369"><img src="https://pbs.twimg.com/amplify_video_thumb/2102543614786043904/img/4rK2k4JOTpApKivu.jpg" alt="Self-running 3D Rube Goldberg machine" width="480"></a>

[@leogao25](https://x.com/leogao25) · 2026-09-22 · 🔖 2 · ▶ 1.2k · `Spec` · Three.js

A 15–20 second looping three.js Rube Goldberg machine with hand-written physics and a cinematic follow camera, screen-recorded at 1280×720.

```text
Build a 3D Rube Goldberg machine that runs itself, as a single self-contained index.html in the current directory.

The chain, in order:
1. A marble is released at the top and rolls down a series of zig-zag ramps.
2. It knocks over a line of at least 12 dominoes.
3. The last domino tips a seesaw, which launches a small ball into a hanging bucket.
4. The bucket's weight pulls it down; its rope runs over a pulley and yanks a bell, which visibly swings.
5. The same motion raises a flag up a pole. The flag reaching the top is the finish.

Rules:
- Write the physics yourself: no physics library. Every motion after the marble is released must come from your simulation (rigid bodies, collisions, constraints, rope/pulley). No keyframed animation or tweened motion of any machine part.
- You may load three.js from a CDN for rendering. Nothing else external: no images, models, or fonts.
- It must run with no user input: start automatically on page load, use a cinematic camera that follows the action, and complete the whole chain in about 15–20 seconds. After the flag is up, hold for 2 seconds, then reset and replay.
- Deterministic: fixed timestep and no unseeded randomness, so every run looks the same.
- Fill the browser window. It will be screen-recorded at 1280×720.
- No on-screen text or UI of any kind.
- Make it look good: lighting, shadows, materials, and a setting that makes it feel like a real contraption.
```

<details><summary>中文译文</summary>

```text
构建一个能自己运行的 3D 鲁布·戈德堡机械，做成当前目录下的单个自包含 index.html。

连锁反应依次为：
1. 一颗弹珠从顶部释放，沿一系列之字形坡道滚下。
2. 它撞倒一排至少 12 块的多米诺骨牌。
3. 最后一块骨牌压翻跷跷板，把一个小球弹进悬挂的桶里。
4. 桶的重量让它下坠；绳子绕过滑轮，猛拉一个铃铛，铃铛明显摆动。
5. 同一个动作把旗子沿旗杆升起。旗子升到顶就是终点。

规则：
- 物理自己写：不用物理库。弹珠释放后的每个动作都必须来自你的模拟（刚体、碰撞、约束、绳索/滑轮）。机械的任何部件都不能用关键帧动画或补间动画。
- 可以从 CDN 加载 three.js 用于渲染。其他外部资源一概不用：不用图片、模型或字体。
- 必须无需用户输入就能运行：页面加载后自动开始，用跟随动作的电影感镜头，整条连锁反应在大约 15–20 秒内完成。旗子升起后停留 2 秒，然后重置并重播。
- 确定性：固定时间步长，不用未设种子的随机数，保证每次运行看起来都一样。
- 铺满浏览器窗口。它会以 1280×720 录屏。
- 画面上不要有任何文字或 UI。
- 要好看：灯光、阴影、材质，以及一个让它像真实装置的场景。
```

</details>

<sub>Effort: high · Author: $14.28 and 62 minutes, 119 turns in Claude Code.</sub>

<sub>Also rendered from this prompt by: [@leogao25](https://x.com/leogao25/status/2102544081863717153)</sub>

[Original post ↗](https://x.com/leogao25/status/2102544078927741369) · Prompt posted in [this reply](https://x.com/leogao25/status/2102544081863717153).

---

### Voxel soccer goal animation in Three.js

<a href="https://x.com/AGI_FromWalmart/status/2102739444256383089"><img src="https://pbs.twimg.com/amplify_video_thumb/2102739314178400256/img/CzvxEdPB8dkuikUB.jpg" alt="Voxel soccer goal animation in Three.js" width="480"></a>

[@AGI_FromWalmart](https://x.com/AGI_FromWalmart) · 2026-09-23 · ▶ 210 · `Brief` · Three.js

A short voxel-style Three.js animation in one HTML file: a blocky player dribbles past two defenders and scores, followed by celebration particles.

```text
Create a single HTML file with Three.js (CDN) for a simple voxel-style soccer animation. A blocky player dribbles past 2 defenders and scores a spectacular goal with celebration particles. Colorful stadium look. Output ONLY the full HTML code.
```

<details><summary>中文译文</summary>

```text
用 Three.js（CDN）写一个单 HTML 文件，做一段简单的体素风足球动画。一个方块小人带球过掉 2 名后卫，打进一记精彩进球，并伴有庆祝粒子。球场要色彩丰富。只输出完整的 HTML 代码。
```

</details>

[Original post ↗](https://x.com/AGI_FromWalmart/status/2102739444256383089)

---

### Rocket launch from an ocean platform at dawn

[@Artless101](https://x.com/Artless101) · 2026-09-25 · ▶ 128 · `Spec` · Three.js · WebGL

A 46-second Three.js launch from an ocean platform through stage separation to satellite deployment, with a scrubber and a UI that hides for recording.

```text
Create a cinematic, highly detailed, interactive 3D rocket launch from an ocean platform at dawn. Deliver the complete project in one HTML file that opens directly in Chrome. Use Three.js + WebGL and procedural assets. Embed assets wherever practical; a reliable CDN may be used for the rendering library.

ART DIRECTION
Create a dramatic transition from a dark, blue-violet ocean before sunrise to warm sunlight above the atmosphere. Use convincing proportions, detailed materials, atmospheric depth, and carefully composed camera angles. The result should feel like a polished miniature spaceflight film.
ROCKET AND LAUNCH PLATFORM
Build a convincing multistage rocket with a shaped nose cone, panel seams, structural rings, interstage connections, engine nozzles, and a payload fairing that separates into two halves.

Create a detailed floating launch platform with a support tower, retracting strongback, service arms, railings, ladders, pipes, equipment, floodlights, and blinking warning beacons. Keep all structures physically connected and correctly positioned.
LAUNCH SEQUENCE
Create an approximately 46-second sequence:

Establishing camera move around the platform.

Service arms and strongback retract.
Engines ignite, illuminating the rocket, platform, and nearby water.
Smoke spreads across the deck as the rocket lifts off and accelerates.
The camera follows the climb from the atmosphere toward space.
The first stage separates and falls away.
The second-stage engine ignites.
The fairing halves separate, revealing a satellite.
The engine shuts down, the satellite deploys, and its solar panels unfold.
Finish with an orbital view of the satellite against Earth’s curved horizon and sunrise.
Compress the flight timeline for presentation while maintaining coherent motion. Avoid sudden position changes, intersecting components, or disconnected effects.
OCEAN, ATMOSPHERE, AND EFFECTS
Use animated shader-driven ocean waves with Fresnel reflections and warm engine-light reflections. Create layered exhaust with a bright core, softer outer flame, and drifting smoke particles.
Smoke should expand, fade, and respond to wind. Exhaust must remain attached to the correct engine through staging. Transition smoothly from atmospheric haze to a dark star field and Earth’s illuminated limb.

CAMERA AND INTERACTION
Use smooth cinematic camera transitions: wide establishing view, low-angle ignition shot, ascent tracking, stage separation, and satellite close-up. Keep the main subject visible in both portrait and landscape layouts.

Include play/pause, replay, and a scrubber with event markers. Seeking must reconstruct the correct rocket configuration, particle state, camera position, and lighting. Replaying must reset the entire sequence cleanly.
Keep the interface minimal and unobtrusive. Allow it to be hidden for recording.

TECHNICAL QUALITY
Use frame-rate-independent animation and efficient particle systems. Reuse geometry and materials where appropriate, handle resizing correctly, and balance visual detail with smooth performance.

Test the final HTML in a desktop browser. Inspect the console and capture screenshots at ignition, liftoff, staging, and satellite deployment. Fix loading errors, clipping, geometry problems, broken seeking, and poor camera framing before delivering the file.
```

<details><summary>中文译文</summary>

```text
创建一个电影感强、细节丰富、可交互的 3D 火箭发射场景：黎明时分，火箭从海上平台升空。把完整项目做成一个能在 Chrome 里直接打开的 HTML 文件。使用 Three.js + WebGL 和程序化素材。能内嵌的素材尽量内嵌；渲染库可以走可靠的 CDN。

美术方向
从日出前幽暗的蓝紫色海面，戏剧性地过渡到大气层之上的温暖阳光。比例要可信，材质细节丰富，有大气纵深感，镜头角度精心构图。成片要像一部精致的微缩航天电影。
火箭与发射平台
做一枚可信的多级火箭：有造型的头锥、面板接缝、结构环、级间连接段、发动机喷管，以及能分成两半的载荷整流罩。

做一个细节丰富的海上浮动发射平台，带支撑塔、可收回的起竖臂、服务臂、栏杆、梯子、管道、设备、泛光灯和闪烁的警示信标。所有结构都要在物理上连在一起、位置正确。
发射流程
做一段约 46 秒的序列：

围绕平台的开场运镜。

服务臂和起竖臂收回。
发动机点火，照亮火箭、平台和附近的海水。
火箭离台加速，烟雾在甲板上铺开。
镜头跟随火箭爬升，从大气层飞向太空。
第一级分离并坠落。
第二级发动机点火。
整流罩两半分离，露出卫星。
发动机关机，卫星释放，太阳能板展开。
最后以轨道视角收尾：卫星背后是地球弧形的地平线和日出。
为了呈现效果可以压缩飞行时间线，但运动要连贯。避免位置突变、部件互相穿插或特效脱节。
海洋、大气与特效
用着色器驱动的动态海浪，带菲涅尔反射和发动机暖光的倒影。尾焰要分层：明亮的内核、较柔和的外焰和飘散的烟雾粒子。
烟雾要扩散、淡出，并受风影响。级间分离时，尾焰必须始终连着正确的发动机。从大气雾霾平滑过渡到黑暗的星空和被照亮的地球边缘。

镜头与交互
使用流畅的电影化镜头切换：大远景开场、低机位点火镜头、上升跟拍、级间分离、卫星特写。竖屏和横屏布局下都要让主体留在画面里。

加入播放/暂停、重播，以及带事件标记的进度条。拖动进度时，必须正确重建火箭构型、粒子状态、镜头位置和光照。重播必须把整段序列干净地重置。
界面保持简洁、不碍眼。允许把界面隐藏起来方便录屏。

技术质量
使用与帧率无关的动画和高效的粒子系统。适当复用几何体和材质，正确处理窗口缩放，在视觉细节和流畅性能之间取得平衡。

在桌面浏览器里测试最终的 HTML。检查控制台，并在点火、升空、级间分离和卫星释放时截图。交付文件前，修好加载错误、穿模、几何问题、进度拖动失灵和不好的镜头构图。
```

</details>

[Original post ↗](https://x.com/Artless101/status/2103303449831964679)

---

<sub>Last updated 2026-09-27.</sub>
