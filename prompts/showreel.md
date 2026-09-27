# 🎬 Showreels and Motion Design

[← Back to the list](../README.md) · **English** · [简体中文](../zh-CN/prompts/showreel.md)

Showreels, abstract motion graphics, UI motion and kinetic type. The genre that started the trend. 48 prompts, most saved first.

### One-shape UI morph loop synced to music

<a href="https://x.com/twoclipping/status/2103273003555402193"><img src="https://pbs.twimg.com/amplify_video_thumb/2103272964967804928/img/DTuQzS4NOGKMbTDA.jpg" alt="One-shape UI morph loop synced to music" width="480"></a>

[@twoclipping](https://x.com/twoclipping) · 2026-09-24 · 🔖 19.4k · ▶ 933.8k · `Template` · Playwright · ffmpeg · Python

A square UI motion loop where one shape morphs through button, player, slider, tabs, chart and ⌘K on a 120 BPM grid, rendered with Playwright and ffmpeg motion blur.

```text
<inputs>
Ask me for: 8 to 12 UI states I want the shape to become (e.g. button, loader, player, slider, toggle, tabs, chart, command palette, toast), pure black and white or one accent color, and a royalty-free song around 120 BPM (e.g. Mixkit, free for commercial use).
</inputs>

<direction>
Dribbble-level UI motion. One shape, never cut: every state is the same element morphing its size, radius and color while its content swaps with a short blur. A cursor drives every change with real clicks and drags. Light warm-gray canvas, black and white components, one clean UI font (Geist). Springs everywhere, a tiny overshoot at most. The camera zooms so each state fills the frame. The last frame is the first frame, so it loops.
Banned: bouncy easing, particle bursts, glows, gradients on UI chrome, mismatched icon strokes, dead time, anything that looks like a template.
</direction>

<structure>
120 BPM, 7 bars, something happens on every beat.
Button → loader → check → dynamic island → music player with a play/pause morph → scrub the progress bar → it becomes a volume slider that stretches when dragged past max → a toggle flips on the beat → the knob becomes a liquid tab indicator → the tabs open into a chart that draws itself, with a tooltip on hover → it collapses into ⌘K → type to filter → enter → toast → back to the button.
</structure>

<build>
1. One HTML file, square 1440x1440. Every style is computed from time inside seek(t): no CSS transitions, no timers, no state carried between frames.
2. Springs are closed-form step responses. A value that changes target many times is the sum of one spring per change, so it stays a pure function of time.
3. The tab indicator's two edges ride different springs, so the leading edge stretches ahead of the trailing one. Same trick for the toggle knob.
4. Drags are direct manipulation: while the cursor is held, the value is computed from its position. On release it springs back from wherever it was.
5. Analyze the song with numpy for the beat grid and start on a downbeat. Place every UI sound by its measured peak.
6. Render with Playwright: 4 subframes per frame, blended with ffmpeg tmix for motion blur at 60fps.
7. Render one frame per beat before the full render. Fix anything off the grid, cramped or hard to read.
</build>

<gotchas>
Never put will-change on anything the camera scales or the text renders blurry. Text that swaps inside a morphing container needs its own enter and exit timing or it overlaps. Make the last frame identical to the first, cursor position and speed included, or the loop stutters.
</gotchas>

<start>
Ask me for the inputs, then show me the state list on the beat grid before you write any code.
</start>
```

<details><summary>中文译文</summary>

```text
<inputs>
先问我要：8 到 12 个我希望这个形状变成的 UI 状态（例如按钮、加载器、播放器、滑块、开关、标签页、图表、命令面板、提示条），纯黑白还是一种强调色，以及一首 120 BPM 左右的免版税歌曲（例如 Mixkit，可免费商用）。
</inputs>

<direction>
Dribbble 水准的 UI 动效。只有一个形状，全程不切镜：每个状态都是同一个元素在改变尺寸、圆角和颜色，内容借一个短暂的模糊完成切换。每次变化都由光标通过真实的点击和拖拽驱动。浅暖灰画布，黑白组件，一种干净的 UI 字体（Geist）。处处用弹簧动画，最多只有一点点过冲。镜头缩放，让每个状态都填满画面。最后一帧就是第一帧，所以能循环。
禁止：弹跳缓动、粒子爆发、辉光、UI 外框上的渐变、图标描边粗细不一、空档时间、任何看起来像模板的东西。
</direction>

<structure>
120 BPM，7 小节，每一拍都有事发生。
按钮 → 加载器 → 对勾 → 灵动岛 → 带播放/暂停变形的音乐播放器 → 拖动进度条 → 它变成音量滑块，拖过最大值时会被拉长 → 开关踩着节拍翻转 → 开关的圆钮变成液态的标签指示条 → 标签页展开成一张自己画出来的图表，悬停时有提示框 → 它收拢成 ⌘K → 输入筛选 → 回车 → 提示条 → 回到按钮。
</structure>

<build>
1. 一个 HTML 文件，正方形 1440x1440。所有样式都在 seek(t) 里由时间算出：不用 CSS 过渡，不用定时器，帧与帧之间不保留任何状态。
2. 弹簧用闭式阶跃响应。一个值如果多次改变目标，就等于每次改变各对应一个弹簧的叠加，这样它仍然是时间的纯函数。
3. 标签指示条的两条边各用不同的弹簧，所以前沿会比后沿先拉伸出去。开关圆钮也用同样的技巧。
4. 拖拽是直接操控：光标按住时，数值由光标位置算出；松开后，从当时所在的位置弹回。
5. 用 numpy 分析歌曲得到节拍网格，从一个强拍开始。每个 UI 音效按它实测的峰值位置来放。
6. 用 Playwright 渲染：每帧 4 个子帧，用 ffmpeg tmix 混合，得到 60fps 的动态模糊。
7. 完整渲染前，先每拍渲染一帧。把偏离网格、太挤或难以看清的地方都修好。
</build>

<gotchas>
镜头会缩放的元素一律不要加 will-change，否则文字会渲染发虚。在变形容器里切换的文字需要各自的进场和退场时间，不然会重叠。让最后一帧和第一帧完全一致，包括光标的位置和速度，否则循环会卡顿。
</gotchas>

<start>
先问我要输入，然后在写任何代码之前，先把状态列表排在节拍网格上给我看。
</start>
```

</details>

<sub>Inputs: Music</sub>

<sub>Also rendered from this prompt by: [@RaphaelAubryy](https://x.com/RaphaelAubryy/status/2103401350897823974), [@sanjeevn72](https://x.com/sanjeevn72/status/2103456358125457691), [@demonugc](https://x.com/demonugc/status/2103526713208525162), [@xingbugengming](https://x.com/xingbugengming/status/2103495844414837126)</sub>

[Original post ↗](https://x.com/twoclipping/status/2103273003555402193)

---

### Showreel with Blender 3D and self-made soundtrack

<a href="https://x.com/shneural/status/2103151003272962130"><img src="https://pbs.twimg.com/amplify_video_thumb/2103149570440024064/img/QKgvRP_unggJVH6M.jpg" alt="Showreel with Blender 3D and self-made soundtrack" width="480"></a>

[@shneural](https://x.com/shneural) · 2026-09-24 · 🔖 6.2k · ▶ 1.7M · `One-shot` · Blender · Python

The one-sentence showreel prompt in stock Claude Code on max: Opus chose to add a Blender 3D section and sequenced its own 128 BPM soundtrack.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒、充满动感的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。
```

</details>

<sub>Author: about 1.5 hours before rendering; $81 at API prices, about 3% of the weekly limit on Max 20x.</sub>

<sub>Also rendered from this prompt by: [@stephanlivera](https://x.com/stephanlivera/status/2103315922098470926), [@kenn](https://x.com/kenn/status/2103337314021937232), [@RaphaelAubryy](https://x.com/RaphaelAubryy/status/2103416909857190360), [@waiting4asi_](https://x.com/waiting4asi_/status/2103417955568767433), [@itsuki_dev](https://x.com/itsuki_dev/status/2103438087204618392), [@ajith_io](https://x.com/ajith_io/status/2103449416325890146), [@sudo_kiran](https://x.com/sudo_kiran/status/2103463886372696074), [@toddsaunders](https://x.com/toddsaunders/status/2103486372715864429), [@himanshutwtxs](https://x.com/himanshutwtxs/status/2103495232637882858), [@fionntobin](https://x.com/fionntobin/status/2103510776690479597), [@LeonKohli](https://x.com/LeonKohli/status/2103517696038191220), [@safarkhanshuvo](https://x.com/safarkhanshuvo/status/2103520091552059752) +32</sub>

[Original post ↗](https://x.com/shneural/status/2103151003272962130)

---

### Motion designer résumé reel on max effort

<a href="https://x.com/darel023/status/2103424524297420829"><img src="https://pbs.twimg.com/amplify_video_thumb/2103424396299845632/img/rGis5XitfBgZGtnY.jpg" alt="Motion designer résumé reel on max effort" width="480"></a>

[@darel023](https://x.com/darel023) · 2026-09-25 · 🔖 1.1k · ▶ 66k · `Brief`

A 15-second motion design résumé reel on max effort: a hook in the first second, then typography, shape play, camera moves and colour shifts, paced as if cut to music.

```text
You're a world-class motion designer, and this is your 15-second résumé reel. Make it dynamic and confident: open with a striking hook in the first second, build through a sequence of distinct techniques (typography, shape play, camera moves, colour shifts), and land on a clean, memorable final frame. Pacing should feel like it's cut to music. Go crazy.
```

<details><summary>中文译文</summary>

```text
你是世界级的动效设计师，这是你的 15 秒简历作品集。要有动感、有自信：第一秒就用一个抓人的钩子开场，接着依次展示一系列不同的技法（字体排印、形状玩法、镜头运动、色彩变化），最后落在一个干净、令人难忘的结束画面上。节奏要像是卡着音乐剪出来的。放开了做。
```

</details>

<sub>Effort: max · Author: about 1 hour on max effort.</sub>

[Original post ↗](https://x.com/darel023/status/2103424524297420829)

---

### Mobile game reward animation template

<a href="https://x.com/op7418/status/2104085484347818226"><img src="https://pbs.twimg.com/amplify_video_thumb/2104085291439144961/img/iAeJM8TyuCSzDBKb.jpg" alt="Mobile game reward animation template" width="480"></a>

[@op7418](https://x.com/op7418) · 2026-09-27 · 🔖 899 · ▶ 65.1k · `Template` · Three.js · GSAP · Canvas · Web Audio

A template for mobile-game reward animations like opening a chest or ranking up: a toon-shaded Three.js object, five staged beats, GSAP timelines and Web Audio sound.

```text
帮我做一个原创的手游「高光时刻」动效：[主体，例如：开宝箱 / 段位晋升 / 成就解锁 / Boss 掉落 / 角色升级]。
做成一个可以直接打开的单文件网页（HTML + CSS + JS），点一下就能完整播放，效果对标商业手游的结算 / 奖励演出。

【世界观与风格】
- 原创美术，不要模仿任何现有游戏的 IP、角色或 Logo。
- 卡通手游风：高饱和配色，统一的深色描边（例如 #1A1033），圆润厚重的造型。
- 配色随等级升级：[等级阶梯，例如：普通绿 → 稀有蓝 → 史诗紫 → 传说金]。每升一级都要切换主色、光效颜色和背景色调。
- 标题用圆胖的游戏字体（如 Titan One / Lilita One），描黑边，加投影；文字逐字「砸」进画面，带回弹。

【主体物：做成真 3D】
- 用 Three.js 建模，不要用平面 SVG 贴图。要有厚度、倒角，以及符合主体的结构细节（木板缝、铆钉、包边、宝石切面、锁扣等）；木板缝这类细节用真实几何体拼出来，不要贴黑线条。
- 着色用卡通分阶（MeshToonMaterial 加 3～4 阶的渐变贴图），配三种灯光：主光、天光、等级色的轮廓光。
- 描边用后期边缘检测：渲染法线图 + 深度图，再用着色器画线。外轮廓粗、零件交界细，粗细全程一致；另外做 1.5 倍超采样和多重采样抗锯齿。
  不要用「放大一圈的黑色背面」那种描边，那样粗细不均、转角会断。
  深度判断的阈值要放宽，接缝主要靠法线判断，否则斜着看的表面会冒出细碎斜纹。
- 活动部件要真实运动，比如箱盖绕铰链翻开、奖章绕竖轴旋转。
- 待机时主体缓慢左右转动，让人看到侧面和厚度，同时轻微上下浮动；脚下要有随高度变化的柔和投影。

【如果画面里有 2D 插画（卡面、奖励图标、角色）】
- 三层卡通着色：底色、成块的阴影色、高光色，不要只用一层渐变。
- 线条分粗细：外轮廓粗，内部结构线细。
- 每个角色或物件要有自己的表情和姿态，不要所有东西共用同一张脸。
- 脚下画投影，让主体「站」在画面里；背景按属性区分图案，不要全用同一套放射线。

【演出节奏：五个阶段，缺一不可】
1. 预备：主体待机浮动，每隔几秒抖一下提示可以点击，底部显示「点击」提示。
2. 升级：每点一次，主体跳起、在空中转一圈、落地时压扁再回弹；同时切换到下一等级的颜色，闪一下光，冒一圈粒子，标题更新。
3. 蓄力（约 1 秒）：主体越抖越剧烈，缝隙透出光，四周粒子往中心吸，音效音调持续上升；最后一刻猛地压扁。
4. 爆发：从爆点向外扩散的泛光闪白、屏幕震动、镜头往前一推、多层冲击波、细长流光迸射、闪光星点、金币和宝石（带旋转）。高等级的爆发要明显更强。彩带只在最高潮用一次，不要满屏彩带。
5. 揭晓与结算：
   - 奖励卡片从主体里沿弧线飞出，落位时带超调和晃动收尾，数字滚动计数。
   - 稀有物品带彩虹流光边框和「NEW!」角标。
   - 点击领取后，金币和宝石沿贝塞尔曲线飞进右上角的余额，每到一个余额就跳一下。

【揭晓舞台：让主角独占画面】
- 最高稀有度揭晓时，其他元素收起或淡出，背后换成一层干净的渐变幕布加缓慢旋转的柔光，不要让主角压在杂乱的背景上。
- 幕布出现时，把场景里的其他 3D 物件隐藏掉，否则后期描边会把它们的轮廓线画在幕布上。
- 主角的外发光要放在主体背后，只从边缘溢出，不能盖在主体前面把它糊成一片白。
- 可以加一圈围绕主角盘旋的星尘拖尾，但轨道必须完整在主角轮廓外侧，不能从主体正面扫过。

【光效：必须柔和，不能有硬边】
- 背景光芒：用带渐变过渡的 conic-gradient，不要一刀切的色块边缘；叠 2～3 层不同密度、不同转速的光。
- 光柱：由 5～7 道带模糊的光束呈扇形散开，亮度各自轻微闪动；根部加一团柔光核心，光里有光尘缓慢上飘。
- 闪白：从爆点向外的径向泛光（mix-blend-mode: screen），强度不超过 0.8，不要整屏纯白过曝。
- 粒子：每个火花都带一圈低透明度的外晕；冲击波用三层描边（宽而淡、中等、细而亮）。

【材质与界面】
- 边框、名牌、按钮要有材质感：金属拉丝渐变、左上亮右下暗的倒角光、内阴影；按稀有度换镶嵌件（钢铆钉 → 银框宝石 → 金框钻石加小王冠）。
- 小卡片上不要塞小字数值；详细数值放到揭晓时的信息面板里，面板里的数字滚动上涨，并弹出「▲+数值」。
- 画在 Canvas 上的贴图，分辨率至少是屏幕上最大显示尺寸的 1.5 倍，否则放大时会发虚。

【动画原则】
- 用 GSAP 时间线编排。所有动作都要有挤压拉伸、超调和弹性回弹，不要匀速。
- 粒子系统用 Canvas 2D 自己写：重力、阻力、生命周期、叠加混合，以及「吸入」「曲线飞行」「环绕」三种运动。
- 不要用 CSS 3D 透视去翻转大尺寸元素，放大加侧翻时会被投影成铺满屏幕的平面，3D 翻转一律放在 WebGL 里做。
- 所有「抖动」「呼吸」类的循环补间，在状态切换时要先取消再归零，避免它比停止指令晚一帧结束，又把值设回去。

【音效】
- 全部用 Web Audio 实时合成，不用音频文件：跳起、落地、升级和弦、蓄力上升音、爆炸低频加噪声、弹出音、计数滴答、金币叮当、胜利号角。
- 第一次点击时才初始化音频；右上角放静音开关。

【界面与工程】
- 顶部 HUD：模式切换、金币和宝石余额、静音按钮。
- 手机宽度也要能用；遵守「减少动态效果」设置（关闭震屏，减少粒子）。
- 动画状态机要严谨：动画播放中忽略点击，不能出现点击被吞或状态错乱。
- 目标 60fps。第一次打开时就是完整的待机画面，不能是空白。

【交付前自检】
在蓄力、爆发、揭晓、结算这几个时刻各截一张图，逐张检查：
- 主角有没有被光晕、粒子或文字挡住？
- 有没有过曝成一片白？
- 背景是否杂乱，有没有穿帮的描边线？
- 小字是否能看清？
- 结算后是否还有东西在不该动的时候继续抖动？

最后告诉我：每个阶段的时长，以及哪些参数可以调整演出强度。
```

<details><summary>English translation</summary>

```text
Make me an original mobile game "highlight moment" animation: [subject, e.g. opening a chest / rank promotion / achievement unlocked / boss drop / character level-up].
Build it as a single web page file that opens directly (HTML + CSS + JS); one click plays the whole thing, and the effect should match the result / reward sequences of commercial mobile games.

[World and style]
- Original art. Do not imitate the IP, characters or logos of any existing game.
- Cartoon mobile game style: highly saturated colors, a consistent dark outline (e.g. #1A1033), round and chunky shapes.
- The color scheme upgrades with the tier: [tier ladder, e.g. common green → rare blue → epic purple → legendary gold]. Every tier-up switches the main color, the glow color and the background tone.
- Titles use a round, chunky game font (such as Titan One / Lilita One), with a black outline and a drop shadow; the text "slams" into the frame letter by letter with a bounce.

[Main object: make it real 3D]
- Model it in Three.js, not with flat SVG textures. It needs thickness, bevels, and structural details that fit the object (plank seams, rivets, edge trims, gem facets, latches, etc.); details like plank seams are built from real geometry, not painted-on black lines.
- Shading uses toon steps (MeshToonMaterial with a 3–4 step gradient map), with three lights: a key light, a sky light, and a rim light in the tier color.
- Outlines come from post-process edge detection: render a normal map + depth map, then draw lines with a shader. Thick outer silhouette, thin lines where parts meet, consistent thickness throughout; also add 1.5x supersampling and multisample anti-aliasing.
  Don't use the "scaled-up black backface" outline; its thickness is uneven and it breaks at corners.
  Loosen the depth threshold and rely mainly on normals for seams, or surfaces seen at an angle will sprout fine diagonal streaks.
- Moving parts must really move, e.g. the chest lid swings open on its hinge, the medal spins around its vertical axis.
- When idle, the object slowly turns left and right so we can see its sides and thickness, while gently bobbing up and down; underneath there is a soft shadow that changes with its height.

[If the frame has 2D illustrations (card faces, reward icons, characters)]
- Three-tone cartoon shading: base color, blocky shadow color, highlight color; don't use a single gradient.
- Vary line weight: thick outer outlines, thin inner structure lines.
- Each character or object has its own expression and pose; don't let everything share the same face.
- Draw a shadow underneath so the subject "stands" in the frame; backgrounds use different patterns by attribute, don't use the same radial lines everywhere.

[Pacing: five stages, none can be skipped]
1. Ready: the object idles and floats, shakes every few seconds to hint that it can be clicked, and a "点击" hint shows at the bottom.
2. Tier-up: each click makes the object jump, spin once in the air, squash on landing and bounce back; at the same time it switches to the next tier's color, flashes, pops a ring of particles, and the title updates.
3. Charge (about 1 second): the object shakes harder and harder, light leaks through the gaps, surrounding particles are sucked toward the center, and the sound effect keeps rising in pitch; at the last moment it squashes hard.
4. Burst: a bloom flash spreading out from the burst point, screen shake, a camera push-in, layered shockwaves, thin streaks of light shooting out, sparkle stars, coins and gems (spinning). Higher-tier bursts must be clearly stronger. Confetti is used only once, at the very climax; no screen full of confetti.
5. Reveal and payout:
   - Reward cards fly out of the object along an arc, settle with overshoot and a wobble, and the numbers roll up.
   - Rare items get a rainbow shimmering border and a "NEW!" corner badge.
   - After tapping to claim, coins and gems fly along Bézier curves into the balance at the top right, and the balance bumps each time one arrives.

[Reveal stage: let the hero own the frame]
- When the highest rarity is revealed, the other elements retract or fade out, and behind it comes a clean gradient backdrop with slowly rotating soft light; don't put the hero on a cluttered background.
- When the backdrop appears, hide the other 3D objects in the scene, or the post-process outline will draw their contour lines onto the backdrop.
- The hero's outer glow goes behind the object and only spills from the edges; it must not sit in front of the object and blur it into a white blob.
- You can add a ring of stardust trails circling the hero, but the orbit must stay fully outside the hero's silhouette and never sweep across the front of the object.

[Light effects: must be soft, no hard edges]
- Background rays: use conic-gradient with gradient transitions, not color blocks with knife-cut edges; stack 2–3 layers with different density and rotation speed.
- Light pillars: 5–7 blurred beams fanning out, each flickering slightly in brightness; add a soft glowing core at the base, with light dust slowly drifting up in the light.
- Flash: a radial bloom from the burst point (mix-blend-mode: screen), strength no more than 0.8; don't overexpose the whole screen to pure white.
- Particles: every spark has a low-opacity halo; shockwaves use three stroke layers (wide and faint, medium, thin and bright).

[Materials and UI]
- Frames, nameplates and buttons need a sense of material: brushed-metal gradients, bevel light bright at the top-left and dark at the bottom-right, inner shadows; the inlays change with rarity (steel rivets → silver frame with gems → gold frame with diamonds plus a small crown).
- Don't cram small numbers onto the small cards; put detailed stats in the info panel at reveal time, where the numbers roll up and a "▲+value" pops out.
- Textures drawn on Canvas must be at least 1.5x the largest on-screen display size, or they will look blurry when scaled up.

[Animation principles]
- Orchestrate with GSAP timelines. Every motion has squash and stretch, overshoot and elastic bounce-back; nothing moves at constant speed.
- Write the particle system yourself in Canvas 2D: gravity, drag, lifetime, additive blending, and three motion types: "suck in", "curved flight" and "orbit".
- Don't use CSS 3D perspective to flip large elements; when scaled up and turned sideways they get projected into a flat plane filling the screen. Do every 3D flip in WebGL.
- For all looping "shake" and "breathing" tweens, kill them and reset to zero first when switching state, so they don't finish a frame after the stop command and set the value back.

[Sound]
- Synthesize everything in real time with Web Audio, no audio files: jump, landing, tier-up chord, rising charge tone, explosion low end plus noise, pop, count ticks, coin clinks, victory fanfare.
- Initialize audio only on the first click; put a mute toggle at the top right.

[UI and engineering]
- Top HUD: mode switch, coin and gem balances, mute button.
- It must also work at phone width; respect the "reduce motion" setting (turn off screen shake, fewer particles).
- The animation state machine must be rigorous: ignore clicks while an animation plays; no swallowed clicks or broken states.
- Target 60fps. On first open it must already show the full idle scene, not a blank screen.

[Self-check before delivery]
Take one screenshot each at the charge, burst, reveal and payout moments, and check them one by one:
- Is the hero blocked by glow, particles or text?
- Is anything overexposed into a white blob?
- Is the background cluttered, are there stray outline lines?
- Can the small text be read?
- After payout, is anything still shaking when it shouldn't be?

Finally tell me: how long each stage lasts, and which parameters adjust the intensity of the sequence.
```

</details>

<sub>Also rendered from this prompt by: [@op7418](https://x.com/op7418/status/2104085539419021491)</sub>

[Original post ↗](https://x.com/op7418/status/2104085484347818226) · Prompt posted in [this reply](https://x.com/op7418/status/2104085539419021491).

---

### Kinetic type bumper for a creator brand

<a href="https://x.com/techhalla/status/2103411244468498547"><img src="https://pbs.twimg.com/amplify_video_thumb/2103409564657885184/img/yzB3EAzZHx4veQ_X.jpg" alt="Kinetic type bumper for a creator brand" width="480"></a>

[@techhalla](https://x.com/techhalla) · 2026-09-25 · 🔖 329 · ▶ 30.4k · `Spec`

A 20-second looping 1080×1080 kinetic-typography bumper for TechHalla in black, magenta and acid green, with per-glyph springs, mask wipes and print misregistration, built in one HTML file.

```text
You are a world-class motion designer doing a 20.00s kinetic identity bumper for TechHalla — an AI creator known for stealable workflows, not vibes. This piece must feel like the best designer in the room made a street-poster that moves. Showreel stakes: if this is weak, you don’t get hired.

DURATION: exactly 20.00 seconds. LOOPABLE: frame 0 == frame last (position, opacity, cursor if any).
FORMAT: one HTML file, 1080×1080 (square, X-native). 60fps.
PALETTE (strict):
- bg # 0A0A0A
- magenta # FF2BD6
- acid green # B8FF00
- white # F5F5F5 only for primary readable type when needed
No other hues. No gradients on UI chrome. Magenta/green may misregister (print offset) by 2–4px on impact frames only.

TYPE SYSTEM (use all three; never one font for everything):
1) Display / scream: Archivo Black (or equivalent ultra-condensed black) — 1–4 words max
2) Urban grotesque: Syne ExtraBold — secondary hits, stacked lines
3) Mono / “prompt code”: IBM Plex Mono Medium — small labels, timestamps, fake prompt crumbs
Tracking: display −40 to −80; mono +20. Optical kerning. No cute script fonts.

MESSAGE (locked — do not soften, do not add filler slogans):
Beat hits in this exact order:
1. STOP SCROLLING
2. AI VIDEO ISN’T EXPENSIVE
3. BAD PROMPTING IS
4. WORKFLOWS > WISHES
5. STEAL THE PROMPT
6. @ TECHHALLA
Supporting crumbs (mono, ≤18 chars, never full sentences): JSON · H3 · SEEDANCE · 0 KEYFRAMES · MAGNIFIC · COPY/PASTE

NARRATIVE ARC (20s):
0.0–2.5s  COLD OPEN — “STOP SCROLLING” slams in from below with spring overshoot; magenta smear trail; acid green baseline ticks across like a waveform.
2.5–6.5s  THESIS A — “AI VIDEO ISN’T EXPENSIVE” locks to a poster grid (baseline grid 8px). Letters scramble (seeded Fisher–Yates per glyph) then snap on the beat.
6.5–10.5s THESIS B — “BAD PROMPTING IS” replaces it via mask wipe through the letterforms (the outgoing line is the mask). Magenta/green channel split on the cut.
10.5–14.5s PROOF FLASH — rapid kinetic stack: WORKFLOWS > WISHES, then mono crumbs orbit a central block like a terminal. One fake “prompt block” types 3 lines max, then gets crossed by an acid green strikethrough that becomes a underline for STEAL THE PROMPT.
14.5–17.5s BRAND LOCK — @ TECHHALLA centers; display weight. A thick magenta bar and a thin acid green rule form an L-bracket mark (custom, not a logo download).
17.5–20.0s SETTLE / LOOP — hold lockup; micro-breath (scale 1.000→1.012→1.000); last frame == first ready for loop.

CONCRETE TECHNIQUES (required — implement, don’t approximate):
1. seek(t) pure function of time. No CSS transitions. No setInterval. No React state across frames.
2. Springs = closed-form step responses. Stack one spring per target change so motion stays deterministic.
3. Kinetic type: per-glyph spring (y, opacity, blur). Stagger = 1/16 note at 120 BPM (125ms).
4. Print misregistration: on accent frames only, duplicate text layer offset (±2–4px) in magenta and acid green at 40% opacity.
5. Mask reveal: destination text revealed by animating a path mask derived from the outgoing word’s outlines.
6. Camera: one orthographic camera; only punch-in (1.0→1.08) and horizontal smash-pans timed to beats — never random drift.
7. Motion blur: render 4 subframes per frame, blend (tmix-style).
8. Beat grid: 120 BPM, downbeat at t=0. Something must land on every beat for the first 16 beats; after that, every other beat is ok.
9. Pre-pass: before full render, export one still per major beat (8 frames). Fix cramped type, orphan words, low contrast — then render.

BANNED:
Generic AI clichés (brains, robots, neural nets, sparkles), soft gradients, bouncy cartoon easing, particle explosions, stock “futuristic HUD”, long paragraphs, narrator essay energy, Canva-deck energy, extra slogans beyond the locked message, purple/blue neon, glassmorphism.
```

<details><summary>中文译文</summary>

```text
你是一位世界级的动效设计师，正在为 TechHalla 做一支 20.00 秒的动态标识片头（kinetic identity bumper）。TechHalla 是一位 AI 创作者，以“可以直接拿走的工作流”而不是空谈氛围出名。这支片子必须让人觉得是全场最强的设计师做了一张会动的街头海报。按作品集的标准来：如果做得弱，你就拿不到这份工作。

时长：精确 20.00 秒。可循环：第 0 帧 == 最后一帧（位置、不透明度，如有光标也包括光标）。
格式：一个 HTML 文件，1080×1080（方形，适配 X）。60fps。
配色（严格）：
- 背景 # 0A0A0A
- 洋红 # FF2BD6
- 荧光绿 # B8FF00
- 白色 # F5F5F5，仅在需要时用于主要的可读文字
不允许其他色相。UI 外框不用渐变。洋红/绿色只可在冲击帧上错位 2–4px（印刷套印偏移）。

字体系统（三种都要用，绝不一种字体用到底）：
1) 展示 / 呐喊：Archivo Black（或同类超窄超粗字体）——最多 1–4 个词
2) 城市怪诞体：Syne ExtraBold——次级重音、堆叠的行
3) 等宽 / “提示词代码”：IBM Plex Mono Medium——小标签、时间码、伪提示词碎片
字距：展示字 −40 到 −80；等宽 +20。视觉字偶距。不要花哨的手写体。

文案（锁定——不要弱化，不要加凑数的口号）：
按以下精确顺序出现：
1. STOP SCROLLING
2. AI VIDEO ISN’T EXPENSIVE
3. BAD PROMPTING IS
4. WORKFLOWS > WISHES
5. STEAL THE PROMPT
6. @ TECHHALLA
辅助碎片（等宽，≤18 个字符，绝不用完整句子）：JSON · H3 · SEEDANCE · 0 KEYFRAMES · MAGNIFIC · COPY/PASTE

叙事弧线（20 秒）：
0.0–2.5s  冷开场——“STOP SCROLLING” 带弹簧过冲从下方砸入；洋红拖影；荧光绿基线像波形一样横向跳过。
2.5–6.5s  论点 A——“AI VIDEO ISN’T EXPENSIVE” 锁定到海报网格上（8px 基线网格）。字母先打乱（每个字形用带种子的 Fisher–Yates），再踩拍归位。
6.5–10.5s 论点 B——“BAD PROMPTING IS” 通过穿过字形的蒙版擦除替换上一句（出场的那行字本身就是蒙版）。切换时洋红/绿色通道分离。
10.5–14.5s 证据闪现——快速的动态堆叠：WORKFLOWS > WISHES，然后等宽碎片像终端一样绕着中央方块旋转。一个伪“提示词块”最多打出 3 行，然后被一条荧光绿删除线划掉，这条线再变成 STEAL THE PROMPT 的下划线。
14.5–17.5s 品牌锁定——@ TECHHALLA 居中；展示字重。一条粗洋红条和一条细荧光绿线组成 L 形括号标记（自定义，不是下载的 logo）。
17.5–20.0s 收束 / 循环——停在锁定画面；微呼吸（缩放 1.000→1.012→1.000）；最后一帧 == 第一帧，可直接循环。

具体技法（必须实现，不许近似）：
1. seek(t) 是时间的纯函数。不用 CSS transitions。不用 setInterval。帧之间不保留 React state。
2. 弹簧 = 闭式阶跃响应。每次目标变化叠加一个弹簧，让运动保持确定性。
3. 动态文字：每个字形一个弹簧（y、不透明度、模糊）。错开间隔 = 120 BPM 下的十六分音符（125ms）。
4. 印刷套印错位：只在重音帧上，复制文字层，以洋红和荧光绿、40% 不透明度偏移（±2–4px）。
5. 蒙版揭示：用从出场单词轮廓得到的路径蒙版做动画，揭示目标文字。
6. 摄像机：一台正交相机；只允许推近（1.0→1.08）和踩拍的横向猛摇——绝不随机漂移。
7. 运动模糊：每帧渲染 4 个子帧并混合（tmix 风格）。
8. 节拍网格：120 BPM，t=0 为强拍。前 16 拍每一拍都必须有东西落下；之后隔一拍即可。
9. 预渲染：完整渲染前，每个主要节拍导出一张静帧（8 帧）。修掉拥挤的排版、孤字、低对比度——然后再渲染。

禁止：
AI 陈词滥调（大脑、机器人、神经网络、闪光）、柔和渐变、弹跳的卡通缓动、粒子爆炸、素材库式“未来感 HUD”、长段落、旁白式散文腔、Canva 幻灯片腔、锁定文案之外的额外口号、紫/蓝霓虹、毛玻璃（glassmorphism）。
```

</details>

<sub>Author: 14 minutes in total: 8 thinking, 2 building the HTML, 4 fixing and rendering.</sub>

[Original post ↗](https://x.com/techhalla/status/2103411244468498547) · Prompt posted in [this reply](https://x.com/techhalla/status/2103411247618146715).

---

### Showreel with a code-synthesized, beat-synced soundtrack

<a href="https://x.com/prasenx/status/2103538744695693512"><img src="https://pbs.twimg.com/amplify_video_thumb/2103537567853666304/img/0aV5KGQ8E6aPmgLx.jpg" alt="Showreel with a code-synthesized, beat-synced soundtrack" width="480"></a>

[@prasenx](https://x.com/prasenx) · 2026-09-25 · 🔖 100 · ▶ 13k · `Brief`

The showreel prompt extended with a fully code-synthesized soundtrack, cuts locked to the beat and a 1080p 60fps MP4 output; made in Cursor.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.

compose the soundtrack yourself, fully synthesized in code. no samples, no audio files, no VST instruments. every cut and transition must land on the beat.

1920x1080, 60fps. render the final video with the music mixed in as an MP4 and tell me where it's saved.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。

自己创作配乐，完全用代码合成。不用采样、不用音频文件、不用 VST 音源。每个剪辑点和转场都必须踩在拍子上。

1920x1080，60fps。把混入音乐的最终视频渲染成 MP4，并告诉我保存在哪里。
```

</details>

<sub>Author: one prompt.</sub>

[Original post ↗](https://x.com/prasenx/status/2103538744695693512) · Prompt posted in [this reply](https://x.com/prasenx/status/2103706945123487925).

---

### Showreel of advanced motion design techniques

<a href="https://x.com/lukasersil/status/2103742861971726495"><img src="https://pbs.twimg.com/amplify_video_thumb/2103741580578295808/img/ZX8e_CdESlqGSX-y.jpg" alt="Showreel of advanced motion design techniques" width="480"></a>

[@lukasersil](https://x.com/lukasersil) · 2026-09-26 · 🔖 99 · ▶ 7.8k · `Brief`

A 15-second motion showreel covering kinetic type, 3D, fluid sims and particles, made at max effort; the post also shows a version using the author's brand kit.

```text
Create a bold, dynamic 15-second motion graphics showreel that feels like the ultimate portfolio piece of an exceptionally talented motion designer. Showcase a wide range of advanced techniques: kinetic typography, smooth transitions, 2D and 3D animation, abstract geometry, fluid simulations, particles, distortion, creative masking, compositing, lighting, depth, and seamless camera movement. Keep the pacing fast, confident, and visually surprising, with every shot transitioning naturally into the next. Make it feel meticulously art-directed rather than like a random collection of effects. Push the creativity, polish, timing, and visual impact as far as possible. This should feel like the opening reel that gets a motion designer hired.
```

<details><summary>中文译文</summary>

```text
制作一段大胆、动感的 15 秒动态图形作品集，让人感觉这是一位极其出色的动效设计师的终极代表作。展示多种高阶技法：动态文字排版、流畅转场、2D 与 3D 动画、抽象几何、流体模拟、粒子、扭曲变形、创意遮罩、合成、光照、景深，以及无缝的镜头运动。节奏要快、自信、视觉上出人意料，每个镜头都自然过渡到下一个。要让它看起来经过精心的美术指导，而不是一堆特效的随意拼凑。把创意、打磨、节奏把控和视觉冲击力推到极限。它应该像一支能让动效设计师拿到工作的开场作品集。
```

</details>

<sub>Effort: max</sub>

[Original post ↗](https://x.com/lukasersil/status/2103742861971726495)

---

### 90-second showreel with its own piano score

<a href="https://x.com/kloss_xyz/status/2103557735086428547"><img src="https://pbs.twimg.com/amplify_video_thumb/2103557605553840129/img/uicU8-1TW2yOf3SA.jpg" alt="90-second showreel with its own piano score" width="480"></a>

[@kloss_xyz](https://x.com/kloss_xyz) · 2026-09-25 · 🔖 72 · ▶ 43.9k · `Brief`

A 90-second 16:9 motion design showreel with sound design and a piano score Opus composed itself, exported as a 1080p MP4.

```text
make a dynamic 16:9 aspect ratio 90-second motion graphics video that shows exactly what an incredible motion designer you are and your true creative limits, like it's your showreel for a résumé. use s tier sound design, no synth. go all out. compose your own original and viral piano score. export it as a 1080p mp4 for social media.
```

<details><summary>中文译文</summary>

```text
制作一段 16:9 画幅、90 秒的动态图形视频，准确展示你是多么出色的动效设计师，以及你真正的创意极限，就像简历里的作品集一样。用 S 级的声音设计，不要合成器。拿出全部本事。自己创作一首原创、有传播力的钢琴配乐。导出为适合社交媒体的 1080p mp4。
```

</details>

[Original post ↗](https://x.com/kloss_xyz/status/2103557735086428547) · Prompt posted in [this reply](https://x.com/kloss_xyz/status/2103560107921723834).

---

### 15-second motion graphics with a designer's taste

<a href="https://x.com/ChatGptAstra/status/2103834787647807540"><img src="https://pbs.twimg.com/amplify_video_thumb/2103834731167264768/img/cHxyp922JQDILh2G.jpg" alt="15-second motion graphics with a designer&#x27;s taste" width="480"></a>

[@ChatGptAstra](https://x.com/ChatGptAstra) · 2026-09-26 · 🔖 60 · ▶ 9k · `One-shot`

A 15-second abstract motion graphics piece from a single Chinese sentence that asks only for a motion designer's refined taste.

```text
以动态设计师的高级审美，制作一段动态的15秒动态图形视频
```

<details><summary>English translation</summary>

```text
With the refined taste of a motion designer, make a dynamic 15-second motion graphics video
```

</details>

[Original post ↗](https://x.com/ChatGptAstra/status/2103834787647807540)

---

### Job-application showreel for a motion agency

<a href="https://x.com/hanifproduktif/status/2103404901451829311"><img src="https://pbs.twimg.com/media/HTDLjf6awAAE1aR.jpg" alt="Job-application showreel for a motion agency" width="480"></a>

[@hanifproduktif](https://x.com/hanifproduktif) · 2026-09-25 · 🔖 51 · ▶ 4.6k · `One-shot`

A 15-second showreel framed as Opus applying for a motion designer job at an agency, made directly in Claude.

```text
You are applying as a motion designer in my agency. Make 15s video to showcase your skills and capabilities. Send me a showreel
```

<details><summary>中文译文</summary>

```text
你正在应聘我公司的动效设计师。做一段 15 秒的视频，展示你的技能和能力。把作品集发给我
```

</details>

[Original post ↗](https://x.com/hanifproduktif/status/2103404901451829311)

---

### "Overthinking" concept film from style references

<a href="https://x.com/gizakdag/status/2103566030916239768"><img src="https://pbs.twimg.com/amplify_video_thumb/2103565216839602176/img/57KPQXjy3tJoHg0n.jpg" alt="&quot;Overthinking&quot; concept film from style references" width="480"></a>

[@gizakdag](https://x.com/gizakdag) · 2026-09-25 · 🔖 48 · ▶ 9k · `One-shot`

A 15-second abstract motion film on the idea of overthinking, guided by the author's own attached style-reference graphics.

```text
Make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it’s your showreel exploring the concept of “Overthinking,” inspired by the attached graphics.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像一部探讨 “Overthinking”（过度思考）这一概念的作品集，灵感来自附带的图形。
```

</details>

<sub>Inputs: Images</sub>

[Original post ↗](https://x.com/gizakdag/status/2103566030916239768)

---

### Showreel tied to a designer's portfolio

<a href="https://x.com/monokern/status/2103489794143613142"><img src="https://pbs.twimg.com/amplify_video_thumb/2103489704490385409/img/t2fbfQ5hJS6eRo97.jpg" alt="Showreel tied to a designer&#x27;s portfolio" width="480"></a>

[@monokern](https://x.com/monokern) · 2026-09-25 · 🔖 42 · ▶ 4.7k · `One-shot`

A 15-second motion and sound design showreel conceptually tied to the author's portfolio, made in a Claude Code cloud session with access to the portfolio repo.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out. make it conceptually connected to my portfolio at http://monokern.design
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。让它在概念上和我在 http://monokern.design 的作品集呼应
```

</details>

<sub>Inputs: Brand kit · Effort: xhigh · Author: about $13 and about 1 hour from prompt to final MP4, including about 20 minutes of rendering.</sub>

[Original post ↗](https://x.com/monokern/status/2103489794143613142) · Prompt posted in [this reply](https://x.com/monokern/status/2103491467402493975).

---

### Psychedelic motion design showreel

<a href="https://x.com/monokern/status/2103563538828832979"><img src="https://pbs.twimg.com/amplify_video_thumb/2103563440631476224/img/DjAROE6KswcU3o4s.jpg" alt="Psychedelic motion design showreel" width="480"></a>

[@monokern](https://x.com/monokern) · 2026-09-25 · 🔖 34 · ▶ 3.3k · `One-shot`

A 20-second psychedelic, hypnotic showreel from one prompt on xhigh effort; Opus 5.5 also did the sound design.

```text
make a dynamic 20-second motion graphics video that shows what an incredible motion designer you are, psychedelic and hypnotic. make it feel like a showreel piece. go all out.
```

<details><summary>中文译文</summary>

```text
制作一段 20 秒的动态图形视频，展示你是多么出色的动效设计师，要迷幻、催眠。让它像作品集里的一件作品。拿出全部本事。
```

</details>

<sub>Author: about an hour and a half of rendering, $14 total.</sub>

[Original post ↗](https://x.com/monokern/status/2103563538828832979)

---

### Topic showreel template with brand colors

<a href="https://x.com/polydao/status/2103783134206566862"><img src="https://pbs.twimg.com/amplify_video_thumb/2103693209062842368/img/u5o0IpLmvX0atbtS.jpg" alt="Topic showreel template with brand colors" width="480"></a>

[@polydao](https://x.com/polydao) · 2026-09-26 · 🔖 19 · ▶ 3.4k · `Template`

A fill-in version of the résumé showreel prompt with slots for length, topic and brand colors, sound synced to cuts; run in Claude Code on max.

```text
Make a dynamic [24]-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a resume. Go all out.

Only about [TOPIC]. Style: [BRAND COLORS], sound synced to the cuts.
```

<details><summary>中文译文</summary>

```text
制作一段 [24] 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。

只围绕 [TOPIC]。风格：[BRAND COLORS]，声音与剪辑点同步。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/polydao/status/2103783134206566862)

---

### Motion designer showreel from a one-line greeting

<a href="https://x.com/zheke/status/2103418664854622583"><img src="https://pbs.twimg.com/amplify_video_thumb/2103410712672362496/img/2kYVCf-MSUHsrL34.jpg" alt="Motion designer showreel from a one-line greeting" width="480"></a>

[@zheke](https://x.com/zheke) · 2026-09-25 · 🔖 19 · ▶ 6.2k · `One-shot`

A 15-second motion design piece from a one-line prompt that simply asks Opus 5.5 to show off as a motion designer.

```text
Hello Opus 5.5 show me what an incredible motion designer you are.
```

<details><summary>中文译文</summary>

```text
你好 Opus 5.5，给我看看你是多么出色的动效设计师。
```

</details>

[Original post ↗](https://x.com/zheke/status/2103418664854622583)

---

### Poster breaking out of its own frame

<a href="https://x.com/pankajkumar_dev/status/2103502614134718609"><img src="https://pbs.twimg.com/amplify_video_thumb/2103501360423649280/img/eGvjdiAFv9ygWCj2.jpg" alt="Poster breaking out of its own frame" width="480"></a>

[@pankajkumar_dev](https://x.com/pankajkumar_dev) · 2026-09-25 · 🔖 16 · ▶ 3.6k · `One-shot`

A 30-second motion design piece where a poster breaks out of its frame, with camera moves and a self-composed soundtrack synced to the beat.

```text
create a motion design video of a poster breaking out of its own frame.
```

<details><summary>中文译文</summary>

```text
制作一段动效视频，内容是一张海报冲出它自己的画框。
```

</details>

<sub>Also rendered from this prompt by: [@sahilvermaai](https://x.com/sahilvermaai/status/2103725292095189237)</sub>

[Original post ↗](https://x.com/pankajkumar_dev/status/2103502614134718609)

---

### Portfolio-piece motion graphics reel

<a href="https://x.com/AIStockSavvy/status/2103482258774483320"><img src="https://pbs.twimg.com/amplify_video_thumb/2103482178684272640/img/KS8d_HOuDfWMzpEB.jpg" alt="Portfolio-piece motion graphics reel" width="480"></a>

[@AIStockSavvy](https://x.com/AIStockSavvy) · 2026-09-25 · 🔖 13 · ▶ 5.5k · `One-shot`

A 15-second motion graphics reel framed as the best piece in a dream-job portfolio; the author also gave Opus a few website screenshots.

```text
Create a bold, dynamic 15-second motion graphics video that showcases your best motion design skills as if it’s the highlight of your portfolio for a dream job. Bring sharp timing, smooth transitions, and standout visuals. Push your creativity and make every second count.
```

<details><summary>中文译文</summary>

```text
制作一段大胆、有冲击力的 15 秒动态图形视频，展示你最好的动效设计功力，就像它是你为梦想工作准备的作品集里的压轴之作。要有利落的节奏、流畅的转场和抢眼的画面。把创意推到极限，让每一秒都有价值。
```

</details>

<sub>Inputs: Screenshots</sub>

[Original post ↗](https://x.com/AIStockSavvy/status/2103482258774483320)

---

### Futuristic particle and kinetic type reel

<a href="https://x.com/kopert0x/status/2103872213812158914"><img src="https://pbs.twimg.com/amplify_video_thumb/2103870430138277888/img/25Ch3D6Ck8-uA9er.jpg" alt="Futuristic particle and kinetic type reel" width="480"></a>

[@kopert0x](https://x.com/kopert0x) · 2026-09-26 · 🔖 12 · ▶ 549 · `One-shot`

A 15-second, 60fps reel of 3D particle fields, kinetic type and cuts synced to the beat.

```text
Make this even more insane and futuristic, with such intricate details that when I watch it, it feels like 'damn, what have they done, it's like we had Adobe do it'
```

<details><summary>中文译文</summary>

```text
把它做得更疯狂、更有未来感，细节要精细到我看的时候会觉得“天哪，他们这是做了什么，简直像请 Adobe 做的”
```

</details>

<sub>Author: 31 minutes of reasoning and $4.20 in tokens.</sub>

[Original post ↗](https://x.com/kopert0x/status/2103872213812158914) · Prompt posted in [this reply](https://x.com/kopert0x/status/2103872310675439629).

---

### Motion designer showreel on max effort

<a href="https://x.com/rendesr/status/2103395846578676116"><img src="https://pbs.twimg.com/amplify_video_thumb/2103395348689670144/img/oKCJi4CPL3rwwgaw.jpg" alt="Motion designer showreel on max effort" width="480"></a>

[@rendesr](https://x.com/rendesr) · 2026-09-25 · 🔖 12 · ▶ 1.1k · `One-shot`

A 15-second résumé-style motion graphics showreel made on Opus 5.5 at max effort, from a reworded take on the viral showreel prompt.

```text
Make a dynamic 15 second motion graphics video that shows off what an incredible motion designer you are. Imagine it's your showreel for a resume!
```

<details><summary>中文译文</summary>

```text
做一段 15 秒的动态图形视频，秀一秀你是多么厉害的动效设计师。想象这是你简历里附的作品集！
```

</details>

[Original post ↗](https://x.com/rendesr/status/2103395846578676116)

---

### Beat-synced morphing UI element template

<a href="https://x.com/diamai_/status/2104191375809954126"><img src="https://pbs.twimg.com/amplify_video_thumb/2104182227026251776/img/OOPwBWLIP1t2MHCW.jpg" alt="Beat-synced morphing UI element template" width="480"></a>

[@diamai_](https://x.com/diamai_) · 2026-09-27 · 🔖 11 · ▶ 314 · `Template` · Python · Playwright · ffmpeg

A 30-second square video where one UI element morphs through 8–12 states on the beat, rendered with Playwright subframes for motion blur.

```text
Make me a 30-second motion design video in code, 1080x1080, 60 fps. The music is [path to your track].

First measure the track with numpy. Find the BPM, the beat times and the drop, then cut 30 seconds starting on its first downbeat. If the song ends too soon after it, pick an earlier drop.

The video is one UI element that never cuts. It morphs through 8-12 states of [your app or idea], for example an input field, a button, a loader, a card, a slider, a toggle, a timer, a toast, a chart, and back to the input. Each change lands on a beat, and each state stays on screen for at least 2 beats so people can read it. The last frame must equal the first for a clean loop. Nothing should move at t=0, and every spring should settle before the end. Move the cursor with left and top, since Chrome draws scaled elements slightly differently after an animation.

Style rules:
- one flat background, black and white components, one font (Geist)
- no gradients, glows, particles or bouncy easing
- a cursor clicks or drags before every change
- the camera zooms so each state fills most of the frame
- content inside the element swaps with a 0.15 s blur

Build it as one HTML page where every style is a pure function of time in http://window.seek(t). Animate with closed-form damped springs (damping around 0.75, about 3% overshoot), one spring per target change, summed.

Before writing any code, show me the list of states on the beat grid and wait for my OK. After the code, render one frame per beat as a contact sheet and hold until I approve it.

For the final render, drive the page with Playwright, take 4 subframes per frame, blend them with ffmpeg tmix for motion blur, then add the music cut and export H.264.
```

<details><summary>中文译文</summary>

```text
给我做一段 30 秒的代码动效视频，1080x1080，60 fps。音乐是 [path to your track]。

先用 numpy 测量这首曲子。找出 BPM、节拍时间点和 drop，然后从第一个强拍开始截取 30 秒。如果在那之后歌曲太快结束，就选一个更早的 drop。

视频是一个从不切镜的 UI 元素。它在 [your app or idea] 的 8-12 个状态之间变形，例如输入框、按钮、加载器、卡片、滑块、开关、计时器、toast 提示、图表，再回到输入框。每次变化都落在节拍上，每个状态至少在屏幕上停留 2 拍，让人看得清。最后一帧必须和第一帧相同，以便无缝循环。t=0 时什么都不应该在动，每个弹簧都要在结束前稳定下来。用 left 和 top 移动光标，因为 Chrome 在动画之后绘制缩放元素会有细微差异。

风格规则：
- 单一纯色背景，黑白组件，一种字体（Geist）
- 不要渐变、辉光、粒子或弹跳缓动
- 每次变化前都有光标点击或拖拽
- 镜头缩放，让每个状态占满大部分画面
- 元素内部内容切换时带 0.15 s 的模糊

把它做成一个 HTML 页面，每个样式都是 http://window.seek(t) 里关于时间的纯函数。用闭式阻尼弹簧做动画（阻尼约 0.75，约 3% 过冲），每次目标变化一个弹簧，叠加求和。

写任何代码之前，先把状态列表排在节拍网格上给我看，等我确认。写完代码后，每拍渲染一帧拼成联系表，等我批准后再继续。

最终渲染时，用 Playwright 驱动页面，每帧取 4 个子帧，用 ffmpeg tmix 混合出运动模糊，再加上剪好的音乐，导出 H.264。
```

</details>

<sub>Inputs: Music · Author: the render took under 2 minutes on an M3 MacBook.</sub>

[Original post ↗](https://x.com/diamai_/status/2104191375809954126) · Prompt posted in [this reply](https://x.com/diamai_/status/2104195085508157697).

---

### Showreel centerpiece motion graphics

<a href="https://x.com/samuel_spitz/status/2103544855276503053"><img src="https://pbs.twimg.com/amplify_video_thumb/2103539685092151296/img/yzD9s1r5Jd0p0Rdi.jpg" alt="Showreel centerpiece motion graphics" width="480"></a>

[@samuel_spitz](https://x.com/samuel_spitz) · 2026-09-25 · 🔖 10 · ▶ 1.5k · `One-shot`

A 15-second highlight reel Opus 5.5 made of itself, from a reworded version of the viral showreel prompt.

```text
Create a motion graphics video that feels like the centerpiece of a world-class designer’s showreel. Treat it as your résumé: showcase your full range, push the craft as far as possible. Go all out.
```

<details><summary>中文译文</summary>

```text
制作一段动态图形视频，让它像世界级设计师作品集里的核心作品。把它当作你的简历：展示你的全部能力，把手艺推到极致。拿出全部本事。
```

</details>

[Original post ↗](https://x.com/samuel_spitz/status/2103544855276503053)

---

### Python-rendered 3D cube and type reel

<a href="https://x.com/Dannnnnok/status/2103846630088716687"><img src="https://pbs.twimg.com/amplify_video_thumb/2103781198417788928/img/wGOsQjt4SWpmNrE4.jpg" alt="Python-rendered 3D cube and type reel" width="480"></a>

[@Dannnnnok](https://x.com/Dannnnnok) · 2026-09-26 · 🔖 9 · ▶ 232 · `Brief` · Python

A 20-second, 60fps reel with every frame and the music written in Python: a from-scratch 3D renderer with 784 cubes and a morphing font.

```text
I’m curious to see how strong you are as a motion designer. To prove it, create a polished 15-second animated graphic video that showcases your motion design skills. This piece will be presented to 10,000 people on X, so make it visually compelling, professional, and memorable. Take full creative freedom and make the strongest result you can
```

<details><summary>中文译文</summary>

```text
我很好奇你作为动效设计师到底有多强。为了证明这一点，请制作一段精致的 15 秒动画图形视频，展示你的动效设计能力。这件作品会展示给 X 上的 10,000 人看，所以要让它视觉上有吸引力、专业、令人难忘。你拥有完全的创作自由，做出你能做到的最强结果
```

</details>

<sub>Author: one chat, about an hour.</sub>

[Original post ↗](https://x.com/Dannnnnok/status/2103846630088716687) · Prompt posted in [this reply](https://x.com/Dannnnnok/status/2103847239885939019).

---

### Vertical motion designer showreel

<a href="https://x.com/ndhabarde11/status/2103832593355686104"><img src="https://pbs.twimg.com/amplify_video_thumb/2103832375251857408/img/POE7BUc-Fyjb1Rml.jpg" alt="Vertical motion designer showreel" width="480"></a>

[@ndhabarde11](https://x.com/ndhabarde11) · 2026-09-26 · 🔖 4 · ▶ 339 · `One-shot`

The widely shared showreel prompt with "in portrait mode" added, giving a vertical 15-second motion graphics reel.

```text
make a dynamic 15-second motion graphics video in portrait mode that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的竖屏动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。
```

</details>

[Original post ↗](https://x.com/ndhabarde11/status/2103832593355686104)

---

### Japanese version of the showreel prompt

<a href="https://x.com/uroborosu_ai/status/2103763635424407915"><img src="https://pbs.twimg.com/amplify_video_thumb/2103763023878135808/img/Ta8u-9BUEmzxUVHD.jpg" alt="Japanese version of the showreel prompt" width="480"></a>

[@uroborosu_ai](https://x.com/uroborosu_ai) · 2026-09-26 · 🔖 2 · ▶ 405 · `One-shot`

The widely shared 15-second showreel prompt written in Japanese; the author's result is a shogunate-themed video, though the shared prompt names no subject.

```text
あなたがどれほど素晴らしいモーションデザイナーかを示す、ダイナミックな15秒のモーショングラフィックスビデオを作成してください。履歴書用のショーリールのような感じで、全力でやって。
```

<details><summary>English translation</summary>

```text
Create a dynamic 15-second motion graphics video that shows how incredible a motion designer you are. Make it feel like a showreel for a résumé, and go all out.
```

</details>

<sub>Also rendered from this prompt by: [@_topi_003](https://x.com/_topi_003/status/2104086342204592443)</sub>

[Original post ↗](https://x.com/uroborosu_ai/status/2103763635424407915) · Prompt posted in [this reply](https://x.com/uroborosu_ai/status/2103774050644607142).

---

### Kinetic typography speech: Build the Floor

<a href="https://x.com/Gdgtify/status/2103458245213929495"><img src="https://pbs.twimg.com/amplify_video_thumb/2103442907357233152/img/Yob1ZkvwuXtjuzFW.jpg" alt="Kinetic typography speech: Build the Floor" width="480"></a>

[@Gdgtify](https://x.com/Gdgtify) · 2026-09-25 · 🔖 2 · ▶ 631 · `Spec` · SVG · Canvas

A 20-second 1080×1080 kinetic-type film where a five-line speech's words become lintel, supports and platform, as a deterministic, seamlessly looping SVG/Canvas HTML.

```text
Create a 20.00-second kinetic spoken-word film titled “BUILD THE FLOOR.”  Treat this as an original miniature speech staged entirely through typography. Every line changes the architecture of the frame. The final declaration must stand on something the earlier words physically constructed.  Deliver one self-contained HTML file, 1080×1080, targeting 60fps, using SVG and/or Canvas. Embed all required assets.  ART DIRECTION Background #102820. Paper # F4E9D5. Structural accent # F2B544. A literary editorial world with the scale and confidence of a public monument. Use a high-contrast serif for the speech, a heavy grotesque for load-bearing words, and a restrained monospace for small timing marks. No distressed protest-poster clichés, megaphones, flags, crowds, microphones, or stock footage.  ORIGINAL SPEECH — EXACT WORDS, EXACT ORDER “We were told to wait.” “So we learned the weight of waiting.” “Then one voice made room.” “Then another.” “Now the floor belongs to us.”  Do not attribute these words to any real person. No extra slogans. The complete speech must be understandable without audio.  CENTRAL VISUAL RULE Words have assigned architectural roles. WAIT is a lintel. WAITING is a suspended load. VOICE is a support. ROOM is an opening. FLOOR is a platform. These roles must emerge from the actual letterforms, not from separate illustrations placed behind text.  STORYBOARD 0.00–3.00 “We were told to wait.” The sentence occupies a narrow horizontal opening beneath a massive WAIT. The opening slowly compresses while the sentence remains readable. The pressure comes from the layout, not camera shake.  3.00–6.50 “So we learned the weight of waiting.” Reveal the sentence in spoken phrase groups. WAITING lowers on two fine vertical rules. Those rules become suspension cables. A baseline bends under the visual load using a controlled vector deformation.  6.50–10.00 “Then one voice made room.” VOICE enters vertically and rotates into a structural support. It lifts one end of the baseline. The counter of the O in ROOM becomes an aperture. The next composition is revealed through that aperture.  10.00–12.50 “Then another.” A second support arrives. The tilted structure levels. This is the first moment of perfect horizontal alignment in the film. Use a brief stillness to make the change feel earned.  12.50–16.00 “Now the floor belongs to us.” Earlier structural words assemble into a platform. The final sentence settles onto it. US receives emphasis through shared alignment and scale, never through a separate flashy effect.  16.00–18.00 Hold the complete declaration. A slight release of tension travels through the supporting rules. No new text. No restless decorative motion.  18.00–20.00 The camera tracks beneath the completed platform. Its underside fills the frame and becomes the opening WAIT lintel. Under full occlusion, return hidden elements to their initial positions. Reveal the exact opening composition.  CHOREOGRAPHY Do not force the speech onto a dance beat. Use a cue sheet based on phrases, pauses, and emphasis. Phrase reveals should follow reading order. Allow at least one 400ms moment of absolute stillness. Use critically damped motion for settling loads. Use controlled elastic deformation for the baseline only. Make the changes in available space carry the emotional progression.  TYPE IMPLEMENTATION Use actual glyph paths for structural words. Preserve counters and legibility during deformation. For transitions between unrelated words, use occlusion or matched structural edges; do not interpolate arbitrary path points. Keep the currently spoken phrase readable before it becomes architecture.  ENGINEERING Implement window. seek(t) as a deterministic scene renderer. No accumulated physics, autonomous CSS transitions, or changing random values. Use time-remapping curves and analytic transforms. Use a 20-second periodic timeline with render(0)=render(20). Provide fixed-step access at n/60 for 1200 export frames. Audio is optional and off by default; no browser speech synthesis or autoplay dependency.  QUALITY GATE Inspect eight representative frames. Check that the speech reads in the correct order. Check that structural transformations never destroy a line before the audience can read it. Check the final platform is visibly assembled from earlier elements. Return the complete HTML implementation.
```

<details><summary>中文译文</summary>

```text
制作一段 20.00 秒的动态口语短片，标题为 “BUILD THE FLOOR”。把它当作一段原创的微型演讲，完全用字体排印来演出。每一句都改变画面的结构。最后的宣言必须站在前面的文字实际搭建起来的东西上。交付一个自包含的 HTML 文件，1080×1080，目标 60fps，使用 SVG 和/或 Canvas。嵌入所有需要的素材。

艺术指导：背景 #102820。纸色 # F4E9D5。结构强调色 # F2B544。一个文学编辑风格的世界，带着公共纪念碑的尺度和自信。演讲正文用高对比衬线体，承重的词用粗重的 grotesque 无衬线体，小的时间标记用克制的等宽字体。不要做旧的抗议海报套路、扩音器、旗帜、人群、麦克风或素材库画面。

原创演讲——原词、原顺序：“We were told to wait.” “So we learned the weight of waiting.” “Then one voice made room.” “Then another.” “Now the floor belongs to us.” 不要把这些话归到任何真实人物名下。不加额外口号。整段演讲在没有声音时也必须能看懂。

核心视觉规则：文字被分配了建筑角色。WAIT 是门楣。WAITING 是悬挂的重物。VOICE 是支柱。ROOM 是开口。FLOOR 是平台。这些角色必须从真实的字形里长出来，而不是在文字后面另放插图。

故事板：
0.00–3.00 “We were told to wait.” 这句话占据一个巨大 WAIT 下方的狭窄水平开口。开口慢慢收窄，而句子始终可读。压迫感来自版式，而不是镜头抖动。
3.00–6.50 “So we learned the weight of waiting.” 按口语的短语分组显示这句话。WAITING 挂在两条细竖线上缓缓下降。这两条线变成吊索。一条基线在视觉重量下弯曲，用受控的矢量形变实现。
6.50–10.00 “Then one voice made room.” VOICE 竖着进入，旋转成一根结构支柱。它抬起基线的一端。ROOM 中 O 的字怀变成一个孔洞。下一个构图通过这个孔洞揭示出来。
10.00–12.50 “Then another.” 第二根支柱到来。倾斜的结构回到水平。这是全片第一次完全水平对齐。用短暂的静止让这个变化显得来之不易。
12.50–16.00 “Now the floor belongs to us.” 之前的结构词拼成一个平台。最后一句落在平台上。US 通过共同的对齐和尺度得到强调，绝不用单独的花哨特效。
16.00–18.00 完整的宣言停留。一丝张力的释放传过支撑线。不加新文字。不要躁动的装饰性动效。
18.00–20.00 镜头在完成的平台下方跟移。平台底面充满画面，变成开头的 WAIT 门楣。在完全遮挡时，把隐藏的元素复位到初始位置。揭示出与开头完全一致的构图。

编排：不要把演讲硬套在舞曲节拍上。按短语、停顿和重音做一张提示表。短语按阅读顺序出现。至少留一个 400ms 的绝对静止。沉降的重物用临界阻尼运动。受控的弹性形变只用于基线。让可用空间的变化承载情绪的推进。

字体实现：结构词使用真实的字形路径。形变时保留字怀和可读性。不相关的词之间的转场用遮挡或对齐的结构边缘；不要随意插值路径点。当前说出的短语在变成建筑之前要保持可读。

工程：把 window. seek(t) 实现为确定性的场景渲染器。不要累积的物理、自动运行的 CSS 过渡或变化的随机值。使用时间重映射曲线和解析变换。使用 20 秒的周期时间线，render(0)=render(20)。以 n/60 提供固定步长访问，共 1200 个导出帧。音频可选，默认关闭；不依赖浏览器语音合成或自动播放。

质量关卡：检查八个有代表性的帧。检查演讲按正确顺序可读。检查结构变换绝不会在观众读完一句之前把它毁掉。检查最后的平台明显是由前面的元素拼成的。返回完整的 HTML 实现。
```

</details>

[Original post ↗](https://x.com/Gdgtify/status/2103458245213929495)

---

### 3D badge unlock animation from Figma

<a href="https://x.com/BThreeAgency/status/2103739079745827092"><img src="https://pbs.twimg.com/amplify_video_thumb/2103737876165054464/img/Nzr3PQ_8Q6MS6kl_.jpg" alt="3D badge unlock animation from Figma" width="480"></a>

[@BThreeAgency](https://x.com/BThreeAgency) · 2026-09-26 · 🔖 1 · ▶ 302 · `Brief` · Figma

A mobile badge-unlock screen animated from a Figma frame: the 3D badge tilts toward the cursor with physics, then bursts into gold particles.

```text
Using the linked Figma frame build a badge unlock screen. Match the design exactly. Use the file's assets, lighting, type and layout and add only the motion. Animate the badge so it feels premium and celebratory. Build its scene and then celebrate with gold particles. Treat the badge as a solid 3D object that tilts toward the
cursor following the rules of physics. Keep it fast and smooth, it should not be bouncy.
```

<details><summary>中文译文</summary>

```text
用链接里的 Figma 画框做一个徽章解锁界面。严格还原设计稿。沿用文件里的素材、光影、字体和布局，只加动效。让徽章的动画显得高级、有庆祝感。先搭好它的场景，再用金色粒子庆祝。把徽章当作一个实心 3D 物体，让它按物理规律朝光标倾斜。要快、要顺滑，不要有弹跳感。
```

</details>

<sub>Inputs: Images</sub>

[Original post ↗](https://x.com/BThreeAgency/status/2103739079745827092)

---

### No-questions 15-second showreel

<a href="https://x.com/levabashidze/status/2103786742520184909"><img src="https://pbs.twimg.com/amplify_video_thumb/2103785942251122689/img/XwGFgbyIqZiYWhGQ.jpg" alt="No-questions 15-second showreel" width="480"></a>

[@levabashidze](https://x.com/levabashidze) · 2026-09-26 · 🔖 1 · ▶ 46 · `One-shot`

The viral showreel prompt plus "dont ask just make", run at max effort for a 15-second motion graphics reel.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out. dont ask just make
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。别问，直接做。
```

</details>

[Original post ↗](https://x.com/levabashidze/status/2103786742520184909)

---

### Code-only 15-second motion showreel

<a href="https://x.com/johnsavage_ai/status/2103600308010041677"><img src="https://pbs.twimg.com/amplify_video_thumb/2103600085913235456/img/0J2hUhiaTZIPSLbJ.jpg" alt="Code-only 15-second motion showreel" width="480"></a>

[@johnsavage_ai](https://x.com/johnsavage_ai) · 2026-09-25 · 🔖 1 · ▶ 468 · `One-shot`

The viral showreel prompt with one extra rule, "use only code", producing a 15-second motion graphics résumé piece.

```text
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a resume. go all out. use only code
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事。只用代码。
```

</details>

[Original post ↗](https://x.com/johnsavage_ai/status/2103600308010041677)

---

### Looping showreel of one person's life cycle

<a href="https://x.com/loicRambo/status/2103428454355980558"><img src="https://pbs.twimg.com/media/HTEsm9uXMAEANp0.jpg" alt="Looping showreel of one person&#x27;s life cycle" width="480"></a>

[@loicRambo](https://x.com/loicRambo) · 2026-09-25 · 🔖 1 · ▶ 147 · `Brief`

A 20-second looping motion-design showreel following one person from childhood through the 9-to-5, family and old age to death and back.

```text
make a dynamic 20-second motion graphics and animation video that shows what an incredible motion designer and animator you are, like it's your showreel for a résumé. make it about the cycle of life showing the same individual going from childhood to adolescence to the 9-5 cycle, to family life to elder life and death, then cutting ready to loop to the beginning.  go all out , use whatever you need.
```

<details><summary>中文译文</summary>

```text
做一段 20 秒、有活力的动态图形与动画视频，展示你是多么出色的动效设计师和动画师，就像简历里的作品集一样。主题是生命的循环：同一个人从童年到青春期，到朝九晚五的循环，到家庭生活，再到晚年和死亡，然后剪回开头，可以循环播放。拿出全部本事，需要什么就用什么。
```

</details>

[Original post ↗](https://x.com/loicRambo/status/2103428454355980558)

---

### 10-second motion designer showreel

<a href="https://x.com/bhanujraj/status/2103496403544928454"><img src="https://pbs.twimg.com/amplify_video_thumb/2103496092612751360/img/WFdxO7iAjK81i15p.jpg" alt="10-second motion designer showreel" width="480"></a>

[@bhanujraj](https://x.com/bhanujraj) · 2026-09-25 · 🔖 1 · ▶ 52 · `One-shot`

A 10-second take on the popular résumé-showreel prompt, which the author found on X and ran unchanged apart from the length.

```text
make a dynamic 10-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out
```

<details><summary>中文译文</summary>

```text
制作一段 10 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事
```

</details>

[Original post ↗](https://x.com/bhanujraj/status/2103496403544928454) · Prompt posted in [this reply](https://x.com/bhanujraj/status/2103496503419613231).

---

### Samurai routine in a fiery display

<a href="https://x.com/chrisjdimarco/status/2103232192847524106"><img src="https://pbs.twimg.com/amplify_video_thumb/2103231768958509057/img/SMHCU_iFp1ClIn5P.jpg" alt="Samurai routine in a fiery display" width="480"></a>

[@chrisjdimarco](https://x.com/chrisjdimarco) · 2026-09-24 · ▶ 353 · `One-shot`

An 18-second pure JavaScript animation of a samurai performing a routine on one spot, cycling through poses amid fire effects.

```text
make a samurai dude in only javascript and have him doing a routine in a single spot going through various seriously impressive poses and motions and positions in a fiery awesome display
```

<details><summary>中文译文</summary>

```text
只用 JavaScript 做一个武士小哥，让他在原地打一套动作，摆出各种非常厉害的姿势、动作和架势，呈现一场火光四射的酷炫表演
```

</details>

[Original post ↗](https://x.com/chrisjdimarco/status/2103232192847524106)

---

### Code-driven animation render recipe

<a href="https://x.com/xelandre__/status/2103473030160687413"><img src="https://pbs.twimg.com/amplify_video_thumb/2103471876106272768/img/oiQSyZ1k6Cpf6nPd.jpg" alt="Code-driven animation render recipe" width="480"></a>

[@xelandre__](https://x.com/xelandre__) · 2026-09-25 · ▶ 138 · `One-shot` · Playwright · ffmpeg

A one-sentence render recipe: time-driven HTML/JS frames captured with Playwright and joined by ffmpeg into an MP4 with motion blur and synthesized sound.

```text
Code-driven animation: an HTML/JS page where every frame is calculated from the time, captured frame by frame with headless Chrome (Playwright), then assembled with ffmpeg into an MP4 with motion blur and code-generated sound.
```

<details><summary>中文译文</summary>

```text
代码驱动的动画：一个 HTML/JS 页面，每一帧都由时间计算得出，用无头 Chrome（Playwright）逐帧截取，再用 ffmpeg 合成为带运动模糊和代码生成音效的 MP4。
```

</details>

[Original post ↗](https://x.com/xelandre__/status/2103473030160687413)

---

### Poké Ball morphing through Pokédex UI states

<a href="https://x.com/TheGrootDev/status/2103516567824966114"><img src="https://pbs.twimg.com/amplify_video_thumb/2103516534241120256/img/la4WoyATEbAUArza.jpg" alt="Poké Ball morphing through Pokédex UI states" width="480"></a>

[@TheGrootDev](https://x.com/TheGrootDev) · 2026-09-25 · ▶ 131 · `Spec` · Playwright · ffmpeg

A 14-second square UI motion loop in which one Poké Ball morphs through Pokédex states on a 120 BPM beat grid, rendered with Playwright and ffmpeg motion blur.

```text
<inputs>
Ask me for: my featured Pokémon or starter trio, 8–12 Pokémon-themed UI states, and a royalty-free song around 120 BPM with a playful adventure or electronic feel. Confirm that the song’s license permits the intended use.Default palette: warm off-white, black, and Poké Ball red. Pokémon artwork keeps its original colors.
</inputs>

<direction>
A Pokémon-inspired UI motion film with Dribbble-level polish. Imagine a beautifully designed modern Pokédex: playful, precise, and instantly http://recognizable.One shape, never cut: a Poké Ball continuously morphs into every interface component by changing its size, radius, and color. Its central button, dividing line, and outer shell become the controls and structure of each new state. Content swaps with a short blur and carefully separated enter/exit timing.

A visible cursor drives every interaction with clicks, drags, and hover gestures. Use a light warm-gray canvas, clean Geist typography, consistent icon strokes, and crisp Pokémon artwork.

Use tightly damped springs with only a tiny overshoot. The camera smoothly reframes each state so the interface stays large and readable. The ending returns exactly to the opening Poké Ball for a seamless loop.

Banned: excessive bouncing, particle bursts, glows, gradients on UI chrome, mismatched icon strokes, dead time, generic dashboard layouts, abrupt scene changes, and unrelated floating elements.
</direction>

<structure>
120 BPM, 4/4 time, 7 bars: 28 beats, approximately 14 seconds. Something intentional happens on every http://beat.Bar 1 — Poké Ball activation

1. A closed Poké Ball sits centered; the cursor approaches.
2. The cursor clicks its central button.
3. The button becomes a circular scanning loader.
4. The scan resolves into a check, and the shell stretches into a compact Pokédex.

Bar 2 — Pokémon discovery
5. The Pokédex expands to reveal the featured Pokémon.
6. Its name, number, and type appear in a quick stagger.
7. The cursor clicks the cry/play control.
8. The control morphs into pause while a compact waveform animates.

Bar 3 — Trainer controls
9. The waveform flattens into a volume slider.
10. The cursor drags its Poké Ball-shaped knob to maximum.
11. Dragging beyond maximum elastically stretches the slider.
12. On release, it settles and compresses into a shiny-mode toggle.

Bar 4 — Pokémon details
13. The cursor flips shiny mode; the artwork changes to the correct shiny variant.
14. The toggle knob stretches into a liquid tab indicator.
15. The cursor selects “Stats.”
16. The card opens into a clean Pokémon stat chart.

Bar 5 — Stats to search
17. Stat bars draw themselves in sync with the beat.
18. The cursor hovers over a bar; a readable tooltip appears.
19. The chart retracts into the same container.
20. The container compresses into a Pokédex search field.

Bar 6 — Find and select
21. The search field expands into a command palette.
22. A short Pokémon name is typed; matching results filter.
23. The cursor selects a result, revealing its miniature artwork and type.
24. Enter confirms; the palette folds into an “Added to team” toast.

Bar 7 — Return to the Poké Ball
25. The toast’s confirmation mark becomes the Poké Ball’s central button.
26. The toast contracts; its edges become the circular shell.
27. The red upper half, white lower half, and black dividing line settle into place.
28. The cursor returns along a smooth path, matching the opening position and velocity as the loop wraps.

Use the chosen Pokémon consistently throughout. Keep visible text brief enough to read at this pace.
</structure>

<build>
1. Build one self-contained HTML file with a square 1440×1440 composition. Compute every animated style from time inside seek(t): no CSS transitions, timers, or state carried between frames.
2. Keep one persistent outer element throughout the sequence. Its internal artwork, labels, and controls may change, but the main silhouette must visibly connect every state.
3. Use closed-form spring step responses. For repeated target changes, sum one spring response per change so animation remains a pure function of time.
4. Give the tab indicator’s two edges different springs so the leading edge stretches ahead of the trailing edge. Apply the same technique to the toggle knob.
5. Make drags direct manipulation: while held, values follow cursor position. On release, use a closed-form spring matching the release position and velocity.
6. Analyze the supplied song with numpy to estimate the beat grid, verify the downbeat, and align the sequence. If the tempo differs from 120 BPM, adapt the timing to the actual music.
7. Use licensed UI sounds and align their measured transient peaks with clicks, confirmations, and morph accents.
8. Render with Playwright at four subframes per output frame. Blend each group of four with ffmpeg into a 60fps video for motion blur.
9. Render one preview frame per beat before the full video. Fix anything cramped, unreadable, visually disconnected, or off the beat grid.
10. Package artwork and fonts inside the HTML so rendering does not depend on network requests.
</build><gotchas>
Never put will-change on anything the camera scales; text can become blurry.Give outgoing and incoming content separate timing so labels never overlap during a morph.

Use accurate Pokémon artwork, names, types, shiny colors, and stats. Do not invent variants or stretch character artwork when the container changes shape.

Keep the main container recognizable through every transition. Pokémon artwork is content inside the morphing interface, not a replacement for the persistent shape.

Match the loop boundary exactly: geometry, content, camera, cursor position, and cursor velocity. Export the interval [0, duration) without duplicating the endpoint frame. Make the audio loop cleanly too.
</gotchas>

<start>
Ask me for the inputs, then show me the proposed Pokémon state list on the 28-beat grid before writing any code.
</start>
```

<details><summary>中文译文</summary>

```text
<inputs>
向我要这些：我的主打宝可梦或御三家、8–12 个宝可梦主题的 UI 状态，以及一首 120 BPM 左右、带俏皮冒险感或电子感的免版税歌曲。确认这首歌的授权允许预期用途。默认配色：暖米白、黑色和精灵球红。宝可梦原画保留原本的颜色。
</inputs>

<direction>
一部受宝可梦启发的 UI 动效短片，达到 Dribbble 级的精致度。想象一台设计精美的现代宝可梦图鉴：俏皮、精准、一眼就能认出来。一个形状，全程不切镜：精灵球通过改变大小、圆角和颜色，连续变形成每一个界面组件。它的中央按钮、分割线和外壳变成每个新状态的控件和结构。内容切换时带一个短暂的模糊，入场和出场的时间要仔细错开。

一个可见的光标用点击、拖拽和悬停手势驱动每一次交互。使用浅暖灰画布、干净的 Geist 字体、统一的图标描边，以及清晰锐利的宝可梦原画。

使用阻尼很紧、只带一点点过冲的弹簧。镜头平滑地为每个状态重新取景，让界面始终够大、看得清。结尾精确回到开场的精灵球，形成无缝循环。

禁止：过度弹跳、粒子爆发、辉光、UI 外框上的渐变、不统一的图标描边、空白时间、千篇一律的仪表盘布局、突兀的场景切换，以及无关的漂浮元素。
</direction>

<structure>
120 BPM，4/4 拍，7 小节：28 拍，约 14 秒。每一拍都要有刻意安排的动作。第 1 小节 — 激活精灵球

1. 一个闭合的精灵球居中；光标靠近。
2. 光标点击它的中央按钮。
3. 按钮变成一个圆形扫描加载器。
4. 扫描完成变成对勾，外壳拉伸成一个小巧的宝可梦图鉴。

第 2 小节 — 发现宝可梦
5. 图鉴展开，露出主打宝可梦。
6. 它的名字、编号和属性快速错落出现。
7. 光标点击叫声/播放控件。
8. 控件变形为暂停，同时一段小巧的波形动起来。

第 3 小节 — 训练家控件
9. 波形压平成一个音量滑块。
10. 光标把精灵球形状的滑钮拖到最大。
11. 拖过最大值时，滑块被弹性拉长。
12. 松手后，它回稳并压缩成一个闪光模式开关。

第 4 小节 — 宝可梦详情
13. 光标打开闪光模式；原画换成正确的闪光版本。
14. 开关滑钮拉伸成一个液态的标签页指示器。
15. 光标选中“Stats”。
16. 卡片展开成一张干净的宝可梦能力值图表。

第 5 小节 — 从能力值到搜索
17. 能力值条随节拍自己画出来。
18. 光标悬停在一根条上；出现一个清晰可读的提示框。
19. 图表缩回同一个容器。
20. 容器压缩成图鉴的搜索框。

第 6 小节 — 查找与选择
21. 搜索框展开成一个命令面板。
22. 输入一个简短的宝可梦名字；匹配结果随之筛选。
23. 光标选中一个结果，露出它的小图和属性。
24. 回车确认；面板折叠成一条“Added to team”提示。

第 7 小节 — 回到精灵球
25. 提示里的确认标记变成精灵球的中央按钮。
26. 提示框收缩；它的边缘变成圆形外壳。
27. 红色上半部、白色下半部和黑色分割线归位。
28. 光标沿一条平滑路径返回，在循环衔接处与开场的位置和速度一致。

全程统一使用选定的宝可梦。画面上的文字要足够简短，保证在这个节奏下读得完。
</structure>

<build>
1. 做一个自包含的 HTML 文件，画面为 1440×1440 的正方形。所有动画样式都在 seek(t) 里由时间算出：不用 CSS transition、不用定时器，帧与帧之间不保留状态。
2. 整个序列始终保留一个持久的外层元素。内部的原画、标签和控件可以变，但主体轮廓必须在视觉上把每个状态连起来。
3. 使用闭式解的弹簧阶跃响应。目标值多次改变时，每次改变叠加一个弹簧响应，让动画保持为时间的纯函数。
4. 给标签页指示器的两条边用不同的弹簧，让前沿先于后沿拉伸。开关滑钮也用同样的手法。
5. 拖拽要做成直接操控：按住时数值跟随光标位置。松手时，用一个与松手时位置和速度相匹配的闭式弹簧。
6. 用 numpy 分析提供的歌曲，估算节拍网格，核对强拍，并对齐整个序列。如果速度不是 120 BPM，就按实际音乐调整时间。
7. 使用有授权的 UI 音效，把它们实测的瞬态峰值对齐到点击、确认和变形的重音上。
8. 用 Playwright 渲染，每个输出帧 4 个子帧。用 ffmpeg 把每 4 个一组混合成 60fps 视频，得到运动模糊。
9. 渲染完整视频之前，先每拍渲染一张预览帧。修掉任何拥挤、看不清、视觉上断开或不在节拍网格上的地方。
10. 把原画和字体打包进 HTML，让渲染不依赖网络请求。
</build><gotchas>
绝不要给任何被镜头缩放的元素加 will-change，否则文字可能变糊。出场和入场的内容要分开计时，保证变形过程中标签永不重叠。

使用准确的宝可梦原画、名字、属性、闪光配色和能力值。不要编造变体，容器变形时也不要拉伸角色原画。

每次过渡都要让主容器保持可辨认。宝可梦原画是变形界面里的内容，不是那个持久形状的替代品。

循环边界要精确匹配：几何形状、内容、镜头、光标位置和光标速度。导出区间 [0, duration)，不要重复终点帧。音频也要能干净地循环。
</gotchas>

<start>
先向我要这些输入，然后在写任何代码之前，给我看在 28 拍网格上拟定的宝可梦状态列表。
</start>
```

</details>

<sub>Inputs: Music · Author: made in the Claude app with some back-and-forth follow-ups.</sub>

[Original post ↗](https://x.com/TheGrootDev/status/2103516567824966114) · Prompt posted in [this reply](https://x.com/TheGrootDev/status/2103517147783946448).

---

### 30-second Hollywood-grade showreel with sound design

<a href="https://x.com/kraithz/status/2103537329306546252"><img src="https://pbs.twimg.com/amplify_video_thumb/2103536987957346304/img/_VxjT1uGcLrEaheH.jpg" alt="30-second Hollywood-grade showreel with sound design" width="480"></a>

[@kraithz](https://x.com/kraithz) · 2026-09-25 · ▶ 74 · `One-shot`

A 30-second motion graphics showreel with its own sound design, made entirely in code without MCP servers or extra skills.

```text
Make a dynamic 30-second motion graphics video that shows what an incredible motion designer you are, like a showreel for your resume to show dominance among top Hollywood motion designers.

You also come up with your own sound design.

Go all out, don't hold back, and show me how incredible you can be at the peak of your creativity and design perspective.
```

<details><summary>中文译文</summary>

```text
制作一段 30 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集，要在好莱坞顶级动效设计师中力压群雄。

音效设计也由你自己来想。

拿出全部本事，别保留，让我看看你在创意和设计眼光的巅峰状态能有多厉害。
```

</details>

[Original post ↗](https://x.com/kraithz/status/2103537329306546252) · Prompt posted in [this reply](https://x.com/kraithz/status/2103537545262850430).

---

### 15-second motion reel from a nine-word prompt

<a href="https://x.com/ghinaiya_nirmal/status/2103540656182308943"><img src="https://pbs.twimg.com/amplify_video_thumb/2103539852624977920/img/gk61oC7kXA7am_rG.jpg" alt="15-second motion reel from a nine-word prompt" width="480"></a>

[@ghinaiya_nirmal](https://x.com/ghinaiya_nirmal) · 2026-09-25 · ▶ 70 · `One-shot`

A 15-second motion reel that Opus 5.5 designed, animated and scored from a nine-word prompt, with no After Effects involved.

```text
make your own 15-second motion reel. go all out
```

<details><summary>中文译文</summary>

```text
做一段属于你自己的 15 秒动效短片。拿出全部本事
```

</details>

[Original post ↗](https://x.com/ghinaiya_nirmal/status/2103540656182308943)

---

### 10-second motion designer showreel

<a href="https://x.com/VanshWTFFF/status/2103644352794992798"><img src="https://pbs.twimg.com/amplify_video_thumb/2103644169562710016/img/iNpSJDw0xBCmXHYm.jpg" alt="10-second motion designer showreel" width="480"></a>

[@VanshWTFFF](https://x.com/VanshWTFFF) · 2026-09-26 · ▶ 22 · `One-shot`

A 10-second take on the viral showreel prompt without "go all out", run on max effort.

```text
make a dynamic 10 second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a resume.
```

<details><summary>中文译文</summary>

```text
制作一段 10 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。
```

</details>

<sub>Author: 1 h 12 min.</sub>

[Original post ↗](https://x.com/VanshWTFFF/status/2103644352794992798)

---

### Showreel prompt with a render recipe

<a href="https://x.com/aichrislee/status/2103878567540961335"><img src="https://pbs.twimg.com/ext_tw_video_thumb/2103878498657996800/pu/img/A4lto6DEv-5V1tsE.jpg" alt="Showreel prompt with a render recipe" width="480"></a>

[@aichrislee](https://x.com/aichrislee) · 2026-09-26 · ▶ 115 · `Brief` · Playwright · ffmpeg

The résumé showreel prompt extended with a 1920x1080, 30 fps spec and a render recipe: one HTML file, Playwright frames, ffmpeg stitch.

```text
Make a dynamic 15-second motion graphics video that shows off everything you can do as a motion designer. Treat it like the showreel for a job you really want. Go all out: something moves every second, big type, bold color, real camera moves, no slow fades.

16:9, 1920x1080, 30 fps. Build it as one HTML file where every frame is a pure function of time, then render every frame with Playwright and stitch them into an MP4 with ffmpeg.

Do not ask me any questions. Just build it and give me the MP4.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你作为动效设计师能做的一切。把它当作你非常想要的一份工作的作品集。拿出全部本事：每一秒都有东西在动，大字号，大胆的颜色，真实的镜头运动，不要慢吞吞的淡入淡出。

16:9，1920x1080，30 fps。做成一个 HTML 文件，每一帧都是时间的纯函数，然后用 Playwright 渲染每一帧，再用 ffmpeg 拼接成 MP4。

不要问我任何问题。直接做出来，把 MP4 给我。
```

</details>

<sub>Author: took 36 minutes.</sub>

[Original post ↗](https://x.com/aichrislee/status/2103878567540961335)

---

### India and cricket themed motion showreel

<a href="https://x.com/mango0_s/status/2103612491922293019"><img src="https://pbs.twimg.com/amplify_video_thumb/2103612228834324480/img/UfvMlHB7mHfkhjqB.jpg" alt="India and cricket themed motion showreel" width="480"></a>

[@mango0_s](https://x.com/mango0_s) · 2026-09-25 · ▶ 111 · `One-shot`

A 20-second showreel variant themed on India and cricket, made by adding three words to the viral motion designer prompt.

```text
make a dynamic 20-second motion graphics video that shows what an incredible motion designer you are, indian and cricket . make it feel like a showreel piece. go all out.
```

<details><summary>中文译文</summary>

```text
制作一段 20 秒的动态图形视频，展示你是多么出色的动效设计师，主题是印度和板球。让它像一件作品集作品。拿出全部本事。
```

</details>

[Original post ↗](https://x.com/mango0_s/status/2103612491922293019)

---

### Open-ended show-off motion graphic

<a href="https://x.com/nolkeeg/status/2103841917603635633"><img src="https://pbs.twimg.com/amplify_video_thumb/2103841849345552384/img/9xfY8JXjxbL4LSwv.jpg" alt="Open-ended show-off motion graphic" width="480"></a>

[@nolkeeg](https://x.com/nolkeeg) · 2026-09-26 · ▶ 96 · `Brief`

A 45-second motion graphic where Opus 5.5 picks the style and subject itself, told not to use memories or skills and to beat GPT 6.

```text
Please do not reference any previous memories or skills. I've been seeing all of these motion graphics examples on X of people making cool videos with opus 5.5. So - I want you to just show off for me. You pick the design style, the look, subject etc. I just want to be extremely impressed by the motion graphic video that you create. I want you to destroy GPT 6 when it comes to motion graphics video - because astra just wants to give me a stupid glorified powerpoint presentation.
```

<details><summary>中文译文</summary>

```text
请不要参考任何之前的记忆或技能。我在 X 上看到很多人用 opus 5.5 做出很酷的动态图形视频。所以——我希望你尽情给我炫一下技。设计风格、视觉、主题等都由你来选。我只想被你做的动态图形视频狠狠惊艳到。我希望你在动态图形视频上碾压 GPT 6——因为 astra 只会给我一个愚蠢的、美化过的 powerpoint 演示。
```

</details>

<sub>Effort: high</sub>

[Original post ↗](https://x.com/nolkeeg/status/2103841917603635633)

---

### Software engineer showreel from a portfolio

<a href="https://x.com/TomWebwalker/status/2103875264815964468"><img src="https://pbs.twimg.com/ext_tw_video_thumb/2103875243869659136/pu/img/wRcOl6VKOy8hmTWh.jpg" alt="Software engineer showreel from a portfolio" width="480"></a>

[@TomWebwalker](https://x.com/TomWebwalker) · 2026-09-26 · ▶ 55 · `One-shot` · Canvas · ffmpeg · Python

A 15-second showreel of the author's career drawn from their portfolio site: canvas frames rendered at 1080p60 with headless Chromium and ffmpeg, cut to 128 BPM.

```text
make a dynamic 15-second motion graphics video that shows what an incredible software engineer you are, like it's your showreel for a résumé. go all out.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的软件工程师，就像简历里的作品集一样。拿出全部本事。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/TomWebwalker/status/2103875264815964468) · Prompt posted in [this reply](https://x.com/TomWebwalker/status/2103875265898184709).

---

### 15-second self-intro for a recruiter

<a href="https://x.com/blushpetal795/status/2103744870041170220"><img src="https://pbs.twimg.com/amplify_video_thumb/2103744827301220352/img/_M_R6GNGd-5fbI1o.jpg" alt="15-second self-intro for a recruiter" width="480"></a>

[@blushpetal795](https://x.com/blushpetal795) · 2026-09-26 · ▶ 53 · `One-shot`

A 15-second motion graphics self-introduction pitched at a recruiter, a variation on the popular résumé showreel prompt.

```text
Make a dynamic 15-second motion graphics video of me introducing myself to a recruiter. Use all the motion design skills you have, like it's your showreel for a resume. Go all out.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，内容是我向招聘官介绍自己。用上你所有的动效设计本事，就像简历里的作品集一样。拿出全部本事。
```

</details>

[Original post ↗](https://x.com/blushpetal795/status/2103744870041170220)

---

### Emmy-style title sequence for a fictional thriller

<a href="https://x.com/abhinayguptha/status/2103565090721259981"><img src="https://pbs.twimg.com/amplify_video_thumb/2103564849188069376/img/w4D7_UKSw3SlXVJB.jpg" alt="Emmy-style title sequence for a fictional thriller" width="480"></a>

[@abhinayguptha](https://x.com/abhinayguptha) · 2026-09-25 · ▶ 46 · `One-shot`

A 20-second main title sequence for an invented Netflix thriller; Opus came up with the concept, credits, animation, music and sound effects in code.

```text
Make a 20-second title sequence for a Netflix thriller that doesn't exist yet. Make it feel like it won an Emmy for main title design.
```

<details><summary>中文译文</summary>

```text
为一部还不存在的 Netflix 惊悚剧做一段 20 秒的片头。要让它看起来像拿过艾美奖最佳片头设计。
```

</details>

[Original post ↗](https://x.com/abhinayguptha/status/2103565090721259981) · Prompt posted in [this reply](https://x.com/abhinayguptha/status/2103565092940108214).

---

### 15-second motion designer showreel

<a href="https://x.com/Shinskinakamoto/status/2103580532852589043"><img src="https://pbs.twimg.com/amplify_video_thumb/2103580286726656000/img/i47FU523zhRtWrEB.jpg" alt="15-second motion designer showreel" width="480"></a>

[@Shinskinakamoto](https://x.com/Shinskinakamoto) · 2026-09-25 · ▶ 37 · `One-shot`

A community run of the viral showreel prompt, retyped with small wording changes, producing a 15-second motion graphics reel.

```text
Make a dynamic 15 second motion graphics video that shows what an incredible motion designer you are, like its your showreel for a resume, go all out!
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集，拿出全部本事！
```

</details>

<sub>Also rendered from this prompt by: [@codeSTACKr](https://x.com/codeSTACKr/status/2103656229717328129), [@motiondsgnr](https://x.com/motiondsgnr/status/2103692944771313960)</sub>

[Original post ↗](https://x.com/Shinskinakamoto/status/2103580532852589043)

---

### Motion showreel branded for Based Agency

<a href="https://x.com/dansushik/status/2103547478482289121"><img src="https://pbs.twimg.com/amplify_video_thumb/2103547336722989056/img/weExtcRRny0a6U-P.jpg" alt="Motion showreel branded for Based Agency" width="480"></a>

[@dansushik](https://x.com/dansushik) · 2026-09-25 · ▶ 31 · `One-shot`

The viral 15-second showreel prompt with one added clause that brands the whole reel for Based Agency.

```text
make a dynamic 15 second motion graphics video that shows what an incredible motion designer you are, like its your showreel for a resume. go all out, and brand it for Based Agency.
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形视频，展示你是多么出色的动效设计师，就像简历里的作品集一样。拿出全部本事，并把它做成 Based Agency 的品牌风格。
```

</details>

<sub>Inputs: Brand kit</sub>

[Original post ↗](https://x.com/dansushik/status/2103547478482289121) · Prompt posted in [this reply](https://x.com/dansushik/status/2103547616055492702).

---

### UI motion designer 15-second showreel

<a href="https://x.com/michael_uxe/status/2103577403138429016"><img src="https://pbs.twimg.com/amplify_video_thumb/2103575612623634432/img/R_8vO4N9GmMapNYW.jpg" alt="UI motion designer 15-second showreel" width="480"></a>

[@michael_uxe](https://x.com/michael_uxe) · 2026-09-25 · ▶ 26 · `Brief`

A 15-second UI motion showreel cut like a music edit: instant hook, typography, shapes, camera and color changes, then a clean finale.

```text
You're a world-class UI motion designer, and this is your 15-second showreel. Go wild with a confident, music-driven edit: open with an instant hook, cycle through diverse techniques (typography, shapes, camera, colors), and land on a clean, memorable finale.
```

<details><summary>中文译文</summary>

```text
你是世界级的 UI 动效设计师，这是你的 15 秒作品集。放开手脚，用自信、跟着音乐走的剪辑：开场立刻抓人，轮番使用多种技法（字体排版、图形、镜头、色彩），最后落在一个干净、令人难忘的结尾。
```

</details>

[Original post ↗](https://x.com/michael_uxe/status/2103577403138429016) · Prompt posted in [this reply](https://x.com/michael_uxe/status/2103580274911236119).

---

### 30-second showreel built from a résumé

<a href="https://x.com/soroucsh/status/2103986528527765885"><img src="https://pbs.twimg.com/amplify_video_thumb/2103986329868550144/img/d2UTgencL-Sfv5uX.jpg" alt="30-second showreel built from a résumé" width="480"></a>

[@soroucsh](https://x.com/soroucsh) · 2026-09-26 · ▶ 26 · `One-shot`

A 30-second personal showreel of the author's skills, generated from their résumé with an adapted version of the showreel prompt.

```text
make a dynamic 30-second motion graphics video that shows what an incredible motion designer you are for me for my skills, like it's your showreel for a résumé. go all out.  based on my resume and instructions i gave you.
```

<details><summary>中文译文</summary>

```text
制作一段 30 秒的动态图形视频，展示你是多么出色的动效设计师，为我、为我的技能而做，就像简历里的作品集一样。拿出全部本事。依据我的简历和我给你的说明。
```

</details>

<sub>Inputs: Data</sub>

[Original post ↗](https://x.com/soroucsh/status/2103986528527765885)

---

### Portfolio video from the portfolio's own assets

<a href="https://x.com/kikelopezdesign/status/2103527289619173471"><img src="https://pbs.twimg.com/amplify_video_thumb/2103527163571949568/img/Cf_UADyCJ6Qm5dBX.jpg" alt="Portfolio video from the portfolio&#x27;s own assets" width="480"></a>

[@kikelopezdesign](https://x.com/kikelopezdesign) · 2026-09-25 · ▶ 20 · `One-shot`

A 20-second video about a designer's personal portfolio, made from scratch with nothing but the portfolio's own assets.

```text
Make a 20 second video about my portfolio from scratch, using only the portfolio's own resources
```

<details><summary>中文译文</summary>

```text
从零开始做一段 20 秒的视频介绍我的作品集，只用作品集自己的素材
```

</details>

<sub>Inputs: Brand kit · Author: 7 minutes in total.</sub>

[Original post ↗](https://x.com/kikelopezdesign/status/2103527289619173471)

---

### Showreel ad for a demanding jury

<a href="https://x.com/yumaeriel/status/2103794772926144729"><img src="https://pbs.twimg.com/amplify_video_thumb/2103794296264515585/img/9cf4SBDQO-orGfcL.jpg" alt="Showreel ad for a demanding jury" width="480"></a>

[@yumaeriel](https://x.com/yumaeriel) · 2026-09-26 · ▶ 6 · `One-shot`

A 15-second motion graphics ad framed as a submission to a very demanding jury, a variation on the résumé showreel prompt.

```text
Create a dynamic 15-second motion graphics ad that showcases the full extent of your talent as a motion designer. The jury is extremely demanding, so don’t hold back—be bold, original, and show everything you’re capable of. Push your creativity and technical skills to the absolute limit. Go all out!
```

<details><summary>中文译文</summary>

```text
制作一段 15 秒的动态图形广告，全面展示你作为动效设计师的才华。评委要求极高，所以别有所保留——大胆、原创，把你能做的都拿出来。把你的创意和技术推到极限。拿出全部本事！
```

</details>

[Original post ↗](https://x.com/yumaeriel/status/2103794772926144729)

---

<sub>Last updated 2026-09-27.</sub>
