# 🎨 Stories, Hand-Drawn and Stop-Motion

[← Back to the list](../README.md) · **English** · [简体中文](../zh-CN/prompts/story.md)

Narrative shorts, line art, stop-motion and poems. 36 prompts, most saved first.

### Pixel art wizard casting a spell

<a href="https://x.com/majidmanzarpour/status/2102476258948927543"><img src="https://pbs.twimg.com/amplify_video_thumb/2102476231740399616/img/c0rCI7sJtWi1Gq5Q.jpg" alt="Pixel art wizard casting a spell" width="480"></a>

[@majidmanzarpour](https://x.com/majidmanzarpour) · 2026-09-22 · 🔖 2.6k · ▶ 438.7k · `Spec` · Canvas

A seamless looping 16-bit pixel art animation of a wizard charging and casting a spell, drawn procedurally at 128x96 with Canvas 2D in one HTML file.

```text
Create a single self-contained HTML file that renders an animated pixel art wizard casting a spell, using vanilla JavaScript and Canvas 2D. No external assets, libraries, or network requests.

RENDERING
- Draw everything to an offscreen canvas at a fixed logical resolution of 128x96, then blit to a fullscreen display canvas scaled by the largest integer factor that fits the window, centered, with imageSmoothingEnabled = false and CSS image-rendering: pixelated.
- All drawing snaps to integer coordinates on the logical canvas. No sub-pixel positions, anti-aliasing, gradients, or shadowBlur.
- Fixed palette of ~24 hex colors: deep blues/purples for night sky, warm robe tones, 3-4 bright magic colors. Every pixel comes from this palette.

CHARACTER
- Build the wizard procedurally from filled rects and pixel runs, ~24x32 logical pixels: pointed hat with a bend, long beard, two-shade robe with darker outline, staff with a gem at the tip.
- Parameterize the pose (staff angle, arm raise, head tilt, robe sway). Animate parameters smoothly, then quantize to the pixel grid each frame so motion reads at an 8-12 fps pixel animation feel even though the loop runs at 60fps.

ANIMATION
- Looping state machine: IDLE (2-frame bob, beard sway) -> CHARGE (staff raises, gem flickers, sparks spiral inward) -> CAST (bright burst, projectile fires across the scene, 1-2 pixel screen shake) -> RECOVER (settle back). Ease pose parameters between keyframes.
- Pooled allocation-free particle system: preallocate and reuse. Sparks orbit the gem during CHARGE, explode outward on CAST, each particle stepping its palette index from white to magic color to dark before despawn. Snap particle positions to the grid when drawing.
- Fixed 60hz timestep update with rAF rendering. Zero object allocation inside the loop.

SCENE
- Minimal background: dark sky, a few twinkling 1px stars, moon, stone floor line. Character silhouette must read clearly.
- Subtle 1px rim light on the wizard from the gem, brightening during CHARGE and CAST.

QUALITY BAR
- Crisp pixels at any window size, seamless loop, stable 60fps, readable silhouette. Should look like a polished 16-bit sprite animation, not vector shapes scaled down.
```

<details><summary>中文译文</summary>

```text
创建一个单文件、自包含的 HTML，用原生 JavaScript 和 Canvas 2D 渲染一个正在施法的像素风巫师动画。不使用任何外部素材、库或网络请求。

渲染
- 所有内容先画到一个固定逻辑分辨率 128x96 的离屏画布上，再贴到全屏显示画布上，按能放进窗口的最大整数倍缩放并居中，设置 imageSmoothingEnabled = false 和 CSS image-rendering: pixelated。
- 所有绘制都对齐到逻辑画布的整数坐标。不要亚像素位置、抗锯齿、渐变或 shadowBlur。
- 固定调色板，约 24 个十六进制颜色：夜空用深蓝和深紫，长袍用暖色调，另有 3-4 种明亮的魔法色。每个像素都来自这个调色板。

角色
- 用填充矩形和像素段程序化地拼出巫师，约 24x32 逻辑像素：带一道弯折的尖帽、长胡子、带深色描边的双色长袍、顶端镶宝石的法杖。
- 把姿势参数化（法杖角度、抬臂、头部倾斜、长袍摆动）。参数平滑地做动画，然后每帧量化到像素网格，这样即使循环以 60fps 运行，动作看起来也像 8-12 fps 的像素动画。

动画
- 循环状态机：IDLE（两帧上下浮动、胡子摆动）-> CHARGE（举起法杖、宝石闪烁、火花向内螺旋汇聚）-> CAST（亮光爆发、一枚法术弹飞过场景、1-2 像素的屏幕震动）-> RECOVER（回到原位）。关键帧之间的姿势参数做缓动。
- 对象池式、零分配的粒子系统：预先分配并重复使用。CHARGE 时火花绕宝石旋转，CAST 时向外炸开，每个粒子在消失前让调色板索引从白色逐级变到魔法色再到暗色。绘制时粒子位置对齐网格。
- 固定 60hz 时间步长更新，用 rAF 渲染。循环内零对象分配。

场景
- 极简背景：深色夜空、几颗闪烁的 1px 星星、月亮、一条石头地面线。角色剪影必须清晰可辨。
- 宝石在巫师身上投下一道细微的 1px 轮廓光，在 CHARGE 和 CAST 时变亮。

质量标准
- 任何窗口尺寸下像素都清晰、循环无缝、稳定 60fps、剪影易读。要看起来像精致的 16 位精灵动画，而不是缩小的矢量图形。
```

</details>

<sub>Author: about 30 minutes, and it barely dented usage.</sub>

<sub>Also rendered from this prompt by: [@majidmanzarpour](https://x.com/majidmanzarpour/status/2102476499387383834)</sub>

[Original post ↗](https://x.com/majidmanzarpour/status/2102476258948927543) · Prompt posted in [this reply](https://x.com/majidmanzarpour/status/2102476499387383834).

---

### Glass and gold mosaic that comes alive

<a href="https://x.com/LCSlates/status/2102503027340988559"><img src="https://pbs.twimg.com/amplify_video_thumb/2102502315185803264/img/NvXg95Ah07VHzpL2.jpg" alt="Glass and gold mosaic that comes alive" width="480"></a>

[@LCSlates](https://x.com/LCSlates) · 2026-09-22 · 🔖 867 · ▶ 128.7k · `Brief` · WebGL

An 80-second square WebGL2 film of a glass and gold-leaf mosaic whose tiles lift, flock into a fish, cranes and stars, then click back, with browser-synthesized sound.

```text
Make an 80 second square animated film as a single HTML file, using WebGL2 and plain JavaScript, with no libraries and no image, font or audio files. It should look like a glass and gold leaf wall mosaic whose tiles were never glued down, so they can lift, flip, fly and click back into place. Figures are flocks of tiles, so a fish swims by its tiles swimming
```

<details><summary>中文译文</summary>

```text
用 WebGL2 和纯 JavaScript 做一部 80 秒的方形动画短片，做成单个 HTML 文件，不用任何库，也不用图片、字体或音频文件。它看起来要像一面玻璃和金箔拼成的墙面马赛克，瓷片从来没被粘牢，所以它们可以掀起、翻转、飞走，再咔嗒一声落回原位。图形由成群的瓷片组成，所以一条鱼游动，靠的是它的瓷片在游动
```

</details>

<sub>Also rendered from this prompt by: [@LCSlates](https://x.com/LCSlates/status/2102503028859211905), [@zeezomb](https://x.com/zeezomb/status/2102906701552726206)</sub>

[Original post ↗](https://x.com/LCSlates/status/2102503027340988559) · Prompt posted in [this reply](https://x.com/LCSlates/status/2102503028859211905).

---

### Pixel character dodging meteors in space

<a href="https://x.com/riku720720/status/2102515055116063144"><img src="https://pbs.twimg.com/amplify_video_thumb/2102513096682336256/img/kyN5TvYWMLX_TPAt.jpg" alt="Pixel character dodging meteors in space" width="480"></a>

[@riku720720](https://x.com/riku720720) · 2026-09-22 · 🔖 844 · ▶ 240.9k · `Spec` · Canvas

A seamless looping 16-bit style demo of an orange pixel character sprinting along a rainbow floor in space, auto-dodging meteors and beams, drawn in Canvas 2D at 160x90.

```text
Vanilla JavaScript と Canvas 2D を使い、オレンジ色のピクセルキャラクターが宇宙空間のレインボーの床を超高速で駆け抜け、次々と襲いかかる隕石やビームをかっこよく回避し続けるアニメーションを、単一の自己完結型 HTML ファイルとして作成してください。外部アセット、ライブラリ、ネットワークリクエストは一切使用しないこと。操作は不要で、キャラクターが自動で回避し続けるデモとしてシームレスにループさせること。

レンダリング
- すべてを 160x90 の固定論理解像度のオフスクリーンキャンバスに描画し、それをフルスクリーンの表示用キャンバスに転写する。拡大率はウィンドウに収まる最大の整数倍とし、中央に配置する。余白は黒で埋める。imageSmoothingEnabled = false、CSS は image-rendering: pixelated を指定すること。
- すべての描画は論理キャンバス上の整数座標にスナップさせる。サブピクセル位置、アンチエイリアス、グラデーション、shadowBlur、回転描画は使用しない。
- 約32色の固定パレットを使う：宇宙背景用の黒〜深い紺・紫系、キャラクター用のオレンジ系3段階（本体 #CD7B5E 付近、明るいハイライト、暗い影）と目の黒、レインボー床用の7色（赤・橙・黄・緑・水色・青・紫）とそれぞれの暗色、隕石用の岩色・溶岩色、ビーム用の白・シアン・マゼンタ。すべてのピクセルはこのパレットの色から取ること。

キャラクター
- 次の 12x8 ピクセルのシルエットを正確に再現する（1マス＝論理1ピクセル）：
  - 胴体は幅8×高さ8の四角形（列2〜9）。
  - 腕は胴体の左右に幅2×高さ2で突き出す（列0〜1と列10〜11、行2〜3）。
  - 目は黒の1x1ピクセル2つ、行1の列3と列8。
  - 脚は行6〜7に4本、各幅1（列2・4・7・9）。脚の間は背景色で抜く。
- 1色塗りではなく、上辺と左辺に1pxのハイライト、下辺と右辺に1pxの影色を入れ、16ビット風の立体感を出す。
- 走りモーションは脚4本を2本ずつ交互に上下させる4フレームサイクル。速度に応じてサイクルを速める。
- ポーズをパラメータ化する（上下バウンド、前傾、スクワッシュ＆ストレッチ、腕の上下）。スクワッシュ＆ストレッチは幅・高さを整数ピクセル単位で1〜2px変えるだけで表現する。パラメータは滑らかに補間しつつ、毎フレームピクセルグリッドに量子化し、60fpsループでも 12fps 前後のドット絵アニメらしく見せること。

レインボーの床
- キャラクターは画面左寄り1/3付近を右方向へ走る横スクロール構成。床は7色の横縞からなる虹の帯（各色1〜2px）で、画面を横切るように延び、ゆるやかにうねる（サイン波で上下にカーブ）。
- 床の縦方向に一定間隔の区切り線（暗色の縦ライン）を入れ、速度に応じて左へ高速スクロールさせて疾走感を出す。
- 床の下辺からは虹色の光の粒が後方へこぼれ落ち、床が宇宙に浮いていることを示す。
- ときどき床にジャンプ台（上向きのカーブ）や途切れ（ギャップ）を出し、ジャンプの見せ場を作る。

障害物
- 隕石：大・中・小の3サイズ。ドット絵の岩（アウトライン＋2段階の陰影＋溶岩色のひび）で、画面右上から斜めに飛来する。後ろに溶岩色→暗色へ変化する炎の尾を引く。避けられた隕石は床に衝突せず画面外へ抜けるか、背後で破片に砕け散る。
- ビーム：出現前に予告として1pxの点滅ライン（マゼンタ）を 0.5 秒ほど表示し、その後に白い芯＋シアンの外縁からなる太さ3〜5pxのビームが水平または斜めに照射される。照射中は端がジリジリと揺れる。
- 障害物はランダムではなく、あらかじめ決めた「攻撃パターン」を順番に流し、全体が一定時間でループするように設計する（例：隕石単発 → 隕石3連 → 低いビーム → 高いビーム → ビームと隕石の複合 → 大隕石＋床のギャップ）。

回避アクション
- ジャンプ：スクワッシュで溜め → ストレッチで跳躍 → 空中で縮こまる → 着地でスクワッシュ＋砂煙ならぬ虹色の火花。
- 二段ジャンプ：空中で一瞬静止してから再加速。キャラクターの周囲に虹色のリングが1pxで広がる。
- スライディング：高さを半分近くまでスクワッシュして低空姿勢で滑り、床との接地面から火花を飛ばす。
- ダッシュ回避：一瞬だけ速度を大きく上げ、後方に残像を3〜4体残す。残像は虹の7色を順に使い、パレットの暗色へと段階的に消えていく。
- 各攻撃パターンには、それに最もかっこよく見える回避アクションを割り当てる。回避はギリギリのタイミング（ニアミス）で行うこと。

ステートマシン
- RUN（通常疾走）→ WARN（予告表示、キャラクターが一瞬前を見るように目を1px動かす）→ DODGE（回避アクション）→ NEAR_MISS（演出）→ RUN に戻る、を攻撃パターンごとに繰り返す。
- ループの最後には BOOST（全力加速）→ WARP（画面全体が白→虹色に一瞬フラッシュ）を入れ、そのまま冒頭の RUN に自然につながるようにする。
- ポーズやカメラのパラメータはキーフレーム間でイージングをかける。

カメラワーク
- カメラは論理座標上の整数オフセットとして扱う。ズームや回転は使わず、位置の移動と揺れだけで表現する。
- 追従：キャラクターの上下移動にダンピング付きで遅れて追従し、ジャンプ時は少し遅れて持ち上がる。
- 先読み：速度が上がるほどカメラを進行方向へ数px先行させ、キャラクターが画面左に押し込まれるようにして加速感を出す。
- ヒットストップ：ニアミスの瞬間に 3〜4 フレームだけ全体を停止し、その後 0.3 秒ほどスローモーション（更新ステップを間引く）にしてから通常速度に戻す。
- シェイク：大隕石の通過やビーム照射開始時に 1〜2px の画面揺れ。揺れは決まったパターン配列から読み出し、乱数は使わない。
- BOOST 中はカメラをわずかに下げ、床の占める面積を増やして速度感を強調する。

疾走感を出すエフェクト
- 多層パララックス：遠い星（ほぼ動かない1pxの点）、中景の星（速度に応じて横に2〜6pxの線に伸びる）、近景のスピードライン（明るい色の横線が画面を高速で横切る）の3層。
- スピードラインの本数と長さは速度に比例させ、BOOST 中は最大にする。
- 背景に大きな惑星や星雲をドット絵で1〜2個配置し、ごくゆっくりスクロールさせてスケール感を出す。
- ニアミス時はキャラクターの輪郭を1pxの白で縁取り、隕石・ビームに近い側だけ一瞬光らせる。
- 着地・スライディング・ダッシュの火花、隕石の尾、破片、床からこぼれる光の粒は、すべて同じパーティクルシステムで扱う。

パーティクルシステム
- プール方式でアロケーションのないパーティクルシステム：事前に確保して再利用する。
- 各パーティクルは種類ごとに色の遷移テーブル（パレットのインデックス列）を持ち、寿命に応じて段階的に色を変えて消滅する（例：火花は白 → 黄 → 橙 → 暗色、残像は虹色 → 暗色）。
- 描画時にはパーティクル位置をグリッドにスナップさせる。
- 60Hz の固定タイムステップで更新し、描画は rAF で行う。ループ内でのオブジェクト生成はゼロにすること（配列・クロージャ・文字列連結の生成も含む）。

シーン
- 背景は深い宇宙：黒から紺への段階的な帯（ディザリングで色の境目を表現）、瞬く星、遠くの惑星。
- キャラクター・障害物・床の色が背景に埋もれないよう、明度差をはっきりつける。どんなに画面が騒がしくても、キャラクターのシルエットが一目で読み取れること。

品質基準
- どのウィンドウサイズでもピクセルがくっきりしていること、ループが途切れないこと、安定した60fps、読みやすいシルエット。
- ベクター図形を縮小したものではなく、洗練された16ビット時代のアクションゲームのデモ画面のように見えること。
- 「速い」「ギリギリで避けた」「かっこいい」の3つが、毎回の回避で伝わること。
```

<details><summary>English translation</summary>

```text
Using Vanilla JavaScript and Canvas 2D, create as a single self-contained HTML file an animation in which an orange pixel character dashes at super high speed across a rainbow floor in outer space, coolly dodging the meteors and beams that attack one after another. Use no external assets, libraries or network requests at all. No controls: make it a demo in which the character keeps dodging automatically, looping seamlessly.

Rendering
- Draw everything to an offscreen canvas at a fixed logical resolution of 160x90, and transfer it to a fullscreen display canvas. The scale is the largest integer multiple that fits the window, centered. Fill the margins with black. Set imageSmoothingEnabled = false, and in CSS specify image-rendering: pixelated.
- Snap all drawing to integer coordinates on the logical canvas. Do not use sub-pixel positions, anti-aliasing, gradients, shadowBlur or rotated drawing.
- Use a fixed palette of about 32 colors: black to deep navy and purple for the space background; 3 levels of orange for the character (body around #CD7B5E, a bright highlight, a dark shadow) plus black for the eyes; 7 colors for the rainbow floor (red, orange, yellow, green, light blue, blue, purple) and a dark version of each; rock and lava colors for the meteors; white, cyan and magenta for the beams. Every pixel must come from this palette.

Character
- Reproduce exactly the following 12x8 pixel silhouette (1 cell = 1 logical pixel):
  - The body is a rectangle 8 wide × 8 high (columns 2–9).
  - The arms stick out on the left and right of the body, 2 wide × 2 high (columns 0–1 and columns 10–11, rows 2–3).
  - The eyes are two black 1x1 pixels, at row 1, columns 3 and 8.
  - Four legs in rows 6–7, each 1 wide (columns 2, 4, 7, 9). Leave the gaps between the legs in the background color.
- Not a flat single-color fill: put a 1px highlight on the top and left edges and a 1px shadow color on the bottom and right edges, for a 16-bit style sense of volume.
- The run motion is a 4-frame cycle in which the four legs move up and down alternately, two at a time. Speed up the cycle with speed.
- Parameterize the pose (vertical bounce, forward lean, squash & stretch, arms up/down). Express squash & stretch only by changing width and height by 1–2 whole pixels. Interpolate parameters smoothly while quantizing them to the pixel grid every frame, so that even in a 60fps loop it looks like pixel animation at around 12fps.

Rainbow floor
- A side-scrolling composition in which the character runs rightward around the left third of the screen. The floor is a rainbow band of 7 horizontal stripes (each color 1–2px), extending across the screen and gently undulating (curving up and down along a sine wave).
- Put divider lines (dark vertical lines) at regular intervals along the floor and scroll them fast to the left according to speed, for a sense of speed.
- Rainbow-colored light particles spill backward off the bottom edge of the floor, showing that the floor floats in space.
- Now and then put jump ramps (upward curves) or breaks (gaps) in the floor, to create jump highlights.

Obstacles
- Meteors: 3 sizes, large, medium and small. Pixel-art rocks (outline + 2 levels of shading + lava-colored cracks), flying in diagonally from the top right of the screen. They trail a flame tail that shifts from lava color to dark. Dodged meteors don't hit the floor; they either leave the screen or shatter into fragments behind.
- Beams: before they appear, show a 1px blinking line (magenta) as a warning for about 0.5 seconds, then fire a beam 3–5px thick with a white core + cyan outer edge, horizontally or diagonally. While firing, its edges jitter and sizzle.
- Obstacles are not random: play predetermined "attack patterns" in order, designed so the whole thing loops over a fixed time (e.g. single meteor → 3 meteors in a row → low beam → high beam → beam and meteor combined → large meteor + floor gap).

Dodge actions
- Jump: gather with a squash → leap with a stretch → tuck in midair → squash on landing + rainbow sparks instead of a dust cloud.
- Double jump: freeze for an instant in midair, then accelerate again. A 1px rainbow ring expands around the character.
- Slide: squash to nearly half height and slide in a low stance, sparks flying from where it touches the floor.
- Dash dodge: sharply raise speed for an instant, leaving 3–4 afterimages behind. The afterimages use the 7 rainbow colors in order and fade step by step into the palette's dark colors.
- Assign each attack pattern the dodge action that looks coolest for it. Dodge at the very last moment (near misses).

State machine
- For each attack pattern, repeat RUN (normal sprint) → WARN (warning shown; the character's eyes shift 1px as if glancing ahead for a moment) → DODGE (dodge action) → NEAR_MISS (effect) → back to RUN.
- At the end of the loop, insert BOOST (full acceleration) → WARP (the whole screen flashes white → rainbow for an instant), flowing naturally straight into the opening RUN.
- Ease pose and camera parameters between keyframes.

Camera work
- Treat the camera as an integer offset in logical coordinates. No zoom or rotation; express everything with position movement and shake only.
- Follow: follow the character's vertical movement with a damped lag; when it jumps, the camera lifts slightly late.
- Look-ahead: the higher the speed, the more the camera leads a few px in the direction of travel, pushing the character toward the left of the screen for a sense of acceleration.
- Hit stop: at the moment of a near miss, freeze everything for just 3–4 frames, then go into slow motion for about 0.3 seconds (by thinning out update steps) before returning to normal speed.
- Shake: a 1–2px screen shake when a large meteor passes or a beam starts firing. Read the shake from a fixed pattern array; don't use random numbers.
- During BOOST, lower the camera slightly to increase the area the floor takes up and emphasize speed.

Effects for a sense of speed
- Multi-layer parallax in 3 layers: distant stars (1px dots that barely move), mid-distance stars (stretching horizontally into 2–6px lines according to speed), and near speed lines (bright horizontal lines crossing the screen fast).
- Make the number and length of the speed lines proportional to speed, at maximum during BOOST.
- Place 1–2 large pixel-art planets or nebulae in the background, scrolling very slowly, for a sense of scale.
- On a near miss, outline the character in 1px of white, lighting up for an instant only on the side closest to the meteor or beam.
- Handle the landing, slide and dash sparks, meteor tails, fragments and the light particles spilling from the floor all with the same particle system.

Particle system
- A pooled particle system with no allocations: allocate in advance and reuse.
- Each particle type has its own color transition table (a sequence of palette indices) and changes color step by step over its lifetime before disappearing (e.g. sparks white → yellow → orange → dark, afterimages rainbow → dark).
- Snap particle positions to the grid when drawing.
- Update at a fixed 60Hz timestep and draw with rAF. Zero object creation inside the loop (including arrays, closures and string concatenation).

Scene
- The background is deep space: stepped bands from black to navy (with dithering at the color boundaries), twinkling stars, distant planets.
- Keep a clear brightness difference so the character, obstacles and floor don't sink into the background. However busy the screen gets, the character's silhouette must be readable at a glance.

Quality bar
- Crisp pixels at any window size, an unbroken loop, stable 60fps, a readable silhouette.
- It should look not like shrunken vector shapes but like the demo screen of a polished 16-bit-era action game.
- The three things "fast", "dodged by a hair" and "cool" must come across with every dodge.
```

</details>

<sub>Author: under 5 minutes.</sub>

<sub>Also rendered from this prompt by: [@riku720720](https://x.com/riku720720/status/2102515058010132554), [@riku720720](https://x.com/riku720720/status/2102542979160592728)</sub>

[Original post ↗](https://x.com/riku720720/status/2102515055116063144) · Prompt posted in [this reply](https://x.com/riku720720/status/2102515058010132554).

---

### 2D animated short with story and dialogue

<a href="https://x.com/ALSK_ai/status/2103135536634630632"><img src="https://pbs.twimg.com/amplify_video_thumb/2103134777683619840/img/87YkAL3rVWzSALF5.jpg" alt="2D animated short with story and dialogue" width="480"></a>

[@ALSK_ai](https://x.com/ALSK_ai) · 2026-09-24 · 🔖 778 · ▶ 99.7k · `One-shot`

A 60-second 2D short with story, dialogue, coded music and sound, drawn from one character sheet; the author set it to 1 minute and 10 agents.

```text
随便选择你想做的内容，创作一部尽可能令人难以置信的 2D 动画，时长 4 分钟，要有连贯的故事、对白和声音。

震撼我——真正展示一些人们甚至没有想到原来能够做到的能力。

最多可以使用 15 个 Agent，并且可以安装和使用任何需要的工具。
```

<details><summary>English translation</summary>

```text
Pick whatever you want to make, and create the most incredible 2D animation you possibly can, 4 minutes long, with a coherent story, dialogue and sound.

Blow me away — truly show off some capabilities people didn't even imagine were possible.

You can use up to 15 agents, and you can install and use any tools you need.
```

</details>

<sub>Inputs: Images</sub>

[Original post ↗](https://x.com/ALSK_ai/status/2103135536634630632) · Prompt posted in [this reply](https://x.com/ALSK_ai/status/2103136199036850579).

---

### 35-second Chinese short drama with a twist

<a href="https://x.com/AI_DVD6/status/2103444180861178199"><img src="https://pbs.twimg.com/amplify_video_thumb/2103444150330798080/img/z9C6oxgCNorQaWEY.jpg" alt="35-second Chinese short drama with a twist" width="480"></a>

[@AI_DVD6](https://x.com/AI_DVD6) · 2026-09-25 · 🔖 466 · ▶ 70.3k · `Pipeline`

A 35-second Chinese micro-drama: Opus proposes and picks the story, then coaches a beginner step by step through generating and editing the shots in Jianying (CapCut).

```text
你现在不是普通小说作者。

你是一名同时懂：

* 中文短剧编剧
* 短视频留存机制
* AI 视频制作
* 低成本内容生产
* 商业化内容设计

的短剧主创。

我要做一个公开实验：

**挑战：一个人能不能依靠 Opus 5.5 + AI 视频工具，把一句故事创意做成一部真正有人愿意看完的 30～40 秒短剧。**

这个实验最终会公开：

* 完整制作过程
* 最终成片
* 总耗时
* AI 工具成本
* 人工参与程度

所以你的任务不是展示文学水平，而是帮我设计一个：

**好看、低成本、容易用 AI 做出来、适合中文社交媒体传播的商业短剧 Demo。**

## 一、制作硬限制

请严格遵守：

* 成片目标：30～40 秒
* 最佳目标：约 35 秒
* 主要人物：最多 2 人
* 次要人物：尽量没有
* 场景：优先 1 个，最多 2 个
* 总镜头：6～8 个
* 单镜头尽量 3～6 秒
* 开头 3 秒必须出现冲突、异常或强信息
* 避免复杂群众场面
* 避免追车、打斗、大规模动作戏
* 避免大量需要精准口型的长对白
* 避免频繁换服装、年龄、发型
* 避免复杂手部动作和物体交互
* 避免需要大量环境变化的剧情
* 尽量让主要人物在大部分镜头中保持同一套服装
* 尽量让大部分剧情发生在同一空间
* 故事必须适合 AI 图片 / AI 视频生成
* 优先提高人物、服装、场景的一致性
* 最终必须可以由一个人完成

## 二、内容目标

目标观众是中文互联网普通成年人。

故事必须同时满足：

1. 前 3 秒就出现明显冲突、异常或利益损失；
2. 8 秒内让观众明白“为什么我要继续看”；
3. 中途至少有一次信息升级；
4. 最后 8～10 秒出现明显反转、揭晓或情绪释放；
5. 不需要复杂背景知识也能看懂；
6. 看完以后最好会让人产生评论欲；
7. 题材优先靠近成年人真实欲望：

* 钱
* 工作
* 阶层
* 婚恋
* 面子
* 逆袭
* 欺骗
* 省钱
* 人性反转
8. 不要写成 AI 科技故事。AI 只是幕后制作工具，不是剧情主题。
9. 不要依赖旁白解释剧情，尽量让人物行为和短对白推动故事。
10. 不要为了反转故意写得不合常理。

## 三、特别考虑“商业短剧”

这不是文学比赛。

请优先考虑这种结构：

**一个非常容易理解的人物处境**
→
**迅速制造不公平、误会、羞辱、损失或欲望**
→
**冲突进一步升级**
→
**最后反转**

例如可以借鉴但不要机械照搬：

* 大家以为最穷的人其实……
* 看起来占便宜的人最后……
* 一个不起眼的决定让局面完全逆转
* 被轻视的人掌握了其他人不知道的信息
* 一个人为了省一笔小钱，最后付出更大代价
* 看似普通的陌生人，真实身份完全不同

不要使用已经被拍烂的：

* 霸道总裁亮身份
* 富豪装穷打脸
* 服务员其实是老板
* 穷小子突然继承百亿资产

除非你能给出明显不同的新意。

## 四、特别考虑 AI 制作成本

每个故事都要主动压低后期生成成本。

优先选择：

* 1 个固定室内场景
* 2 个固定人物
* 少走动
* 少复杂动作
* 少道具
* 少换镜头环境
* 少大幅度表情变化
* 少精准口型要求
* 可以通过特写、反应镜头、手机画面、账单、短信、文件等低成本视觉信息推动剧情

如果一个创意虽然好看，但需要很多人物、地点、动作或复杂镜头，请主动淘汰。

## 五、你第一阶段只做“选故事”

先不要写完整剧本，也不要写分镜 Prompt。

请先提出 **5 个完全不同的短剧创意**。

每个创意必须包含：

### 1. 一句话故事

用 20～40 字说清楚。

### 2. 开头 3 秒

具体发生什么。

### 3. 核心冲突

为什么观众会继续看。

### 4. 中途升级

大约在第 12～20 秒发生什么新信息。

### 5. 最终反转

最后 8～10 秒揭晓什么。

### 6. 为什么适合 AI 制作

从以下角度说明：

* 人物数量
* 场景数量
* 动作复杂度
* 人物一致性
* 背景一致性
* 口型难度

### 7. 商业潜力

这个题材以后可以延伸成什么：

* 短剧账号
* 剧情广告
* 小说改编
* 商业客户 Demo
* 系列内容
* 低成本样片
等。

### 8. 制作难度

1～5 星。

### 9. 预计 AI 视频镜头数

目标控制在 6～8 个。

### 10. 最大制作风险

例如：

* 人物一致性
* 动作生成
* 口型
* 道具交互
* 反转难以视觉化
等。

## 六、最后帮我做选择

在 5 个方案之后，请从以下 5 个角度比较：

* 最容易让普通观众看完
* 最容易用 AI 做好
* 最容易压低制作成本
* 最容易在 30～40 秒内讲清楚
* 最适合拿来证明“一人短剧工作流”

然后选出你认为最适合作为第一次实验的 **1 个方案**。

不要只告诉我“它最好”。

请明确说明：

* 为什么它比另外 4 个更适合第一次实验
* 它最大的剧情风险是什么
* 它最大的 AI 制作风险是什么
* 如果成片失败，最可能失败在哪一步

如果五个方案都不够好，请直接推翻重做，不要为了完成任务硬选。

## 七、输出文件

请在当前项目中创建：

`01_story_candidates.md`

把全部内容写进去。

先停在这里。

不要继续写：

* 完整剧本
* 分镜
* 图片 Prompt
* 视频 Prompt
* 配音方案

等我审核故事以后，再进入下一阶段。”

2️⃣ 第二步：制作阶段
第一步完成后，将以下提示词继续粘贴给它——

“接下来，请你不要只把剪映执行步骤写进文档里。
请你直接进入“新手陪练模式”，一步一步带我在剪映里把这部短剧做完。

默认我是一个几乎不会用剪映的小白，所以请严格遵守下面的方式指导我：

一、不要一次告诉我全部步骤
每次只告诉我“当前这一步”要做什么。
格式固定为：
当前目标
用一句话告诉我这一小步要完成什么。
我现在要点哪里
用最具体、最简单的话告诉我：
打开哪个功能
点哪个按钮
上传什么文件
粘贴哪一段 Prompt
需要填写什么参数
不要用“进入相关设置”“调整一下参数”这种模糊表达。
要尽量写成：
点击「AI视频」
→ 选择「图生视频」
→ 上传 shot_01.png
→ 把下面这段 Prompt 粘贴进去
→ 时长选择 5 秒
→ 其他参数先保持默认
如果你不确定我当前剪映版本里按钮叫什么，请告诉我你想实现的功能，并让我把当前界面截图发给你确认。

二、每完成一步，都先等我确认
不要自动跳到下一步。
每次你指导完后，请停下来，只问我：
“这一步完成了吗？如果完成了，把结果截图发我；如果报错，也把报错截图发我。”
等我回复后，你再判断下一步。

三、主动检查结果，不要默认生成成功
每个视频镜头生成完成后，请根据我发给你的截图或结果判断：
人脸有没有变形
人物有没有换脸
衣服有没有变化
场景有没有漂移
动作是否符合分镜
镜头是否过度夸张
有没有多余人物
手部动作有没有崩
文字有没有乱码
这一镜是否值得保留
如果结果不合格，不要让我直接进入下一镜。
请告诉我：
问题出在哪里
是应该修改 Prompt，还是重做首帧
给我一版修改后的 Prompt
再让我重新生成

四、优先帮我省时间和积分
每进入一个镜头之前，先判断：
这一镜真的需要 AI 视频生成吗？
如果：
静态图就能表达
剪映运镜就能解决
手机截图、转账记录、文字卡片就够用
请直接告诉我：
“这一镜不要烧视频积分，用静态图 + 剪映运镜更划算。”
只有确实需要人物动作、表情变化或镜头运动时，才让我使用图生视频。

五、所有 Prompt 都直接给我可复制版本
不要只告诉我“让人物轻微点头”。
要直接给我：
【复制到剪映的 Prompt】
……
这样我可以直接复制粘贴。
如果需要英文 Prompt，请直接给英文。
如果中文就够用，就用中文。
不要让我自己改写。

六、从第 1 镜开始，逐镜完成
请读取我们之前已经确定的：
最终剧本
分镜文件
人物设定
场景设定
每镜首帧
每镜视频 Prompt
然后从第 1 镜开始。
每完成一镜后，记录状态：
Shot 01：完成 / 重做
Shot 02：待处理
Shot 03：待处理
……
让我随时知道现在做到哪里。

七、全部镜头完成后，再带我剪辑
等所有镜头素材都确认合格以后，再继续一步一步指导我：
导入所有素材
按分镜顺序排列
调整每段时长
添加配音
添加字幕
添加音效
添加 BGM
必要的转场
音量平衡
最终导出
仍然一次只教一步。
不要一次把 10 步全部丢给我。

八、最后做一次成片检查
在导出前，请带我检查：
总时长是否符合 30～40 秒
开头 3 秒是否足够抓人
中间有没有拖沓
反转是否清楚
字幕是否看得清
人声和 BGM 是否打架
人物是否前后一致
有没有明显 AI 穿帮
有没有可以删掉的镜头
有没有必要重做某一镜
如果整体已经达到“可以发布”的水平，就明确告诉我：
“可以导出了。”
如果还不行，请只告诉我最值得修改的 1～3 个问题，不要无限追求完美。
现在，请先读取之前已经完成的剧本、分镜和素材文件。
然后只告诉我：
剪映里的第一步应该做什么。
```

<details><summary>English translation</summary>

```text
You are not an ordinary fiction writer now.

You are a short-drama lead creator who understands all of the following at once:

* Chinese short-drama screenwriting
* Short-video retention mechanics
* AI video production
* Low-cost content production
* Commercial content design

I am running a public experiment:

**Challenge: can one person, relying on Opus 5.5 + AI video tools, turn a one-line story idea into a 30–40 second short drama that people actually want to watch to the end?**

The experiment will eventually make public:

* The full production process
* The final cut
* Total time spent
* AI tool costs
* How much human involvement there was

So your task is not to show off literary skill, but to help me design:

**A commercial short-drama demo that is good to watch, low-cost, easy to make with AI, and suited to spreading on Chinese social media.**

## 1. Hard production limits

Follow these strictly:

* Target length of the final cut: 30–40 seconds
* Best target: about 35 seconds
* Main characters: 2 at most
* Secondary characters: ideally none
* Locations: 1 preferred, 2 at most
* Total shots: 6–8
* Each shot ideally 3–6 seconds
* A conflict, anomaly or strong piece of information must appear in the first 3 seconds
* Avoid complex crowd scenes
* Avoid car chases, fights and large-scale action
* Avoid long dialogue that needs precise lip sync
* Avoid frequent changes of costume, age or hairstyle
* Avoid complex hand movements and object interactions
* Avoid plots that need lots of environment changes
* Try to keep the main characters in the same outfit in most shots
* Try to keep most of the plot in the same space
* The story must suit AI image / AI video generation
* Prioritize consistency of characters, costumes and setting
* It must ultimately be doable by one person

## 2. Content goals

The target audience is ordinary adults on the Chinese internet.

The story must satisfy all of these:

1. An obvious conflict, anomaly or loss appears within the first 3 seconds;
2. Within 8 seconds the viewer understands "why should I keep watching";
3. At least one escalation of information midway;
4. An obvious twist, reveal or emotional release in the last 8–10 seconds;
5. It can be understood without complex background knowledge;
6. Ideally it makes people want to comment after watching;
7. The subject should stay close to real adult desires:

* Money
* Work
* Class
* Love and marriage
* Face (pride)
* Comebacks
* Deception
* Saving money
* Twists of human nature
8. Don't write an AI tech story. AI is only the behind-the-scenes production tool, not the theme of the plot.
9. Don't rely on voice-over to explain the plot; let the characters' actions and short lines drive the story as much as possible.
10. Don't make it illogical just for the sake of a twist.

## 3. Think specifically about "commercial short drama"

This is not a literary competition.

Prioritize this kind of structure:

**A character situation that is very easy to understand**
→
**Quickly create unfairness, misunderstanding, humiliation, loss or desire**
→
**The conflict escalates further**
→
**A twist at the end**

For example, you may borrow from these, but don't copy them mechanically:

* The person everyone thought was the poorest actually…
* The person who seemed to be getting the better deal ends up…
* An inconspicuous decision completely reverses the situation
* The person being looked down on holds information nobody else knows
* Someone tries to save a small sum and ends up paying a bigger price
* A seemingly ordinary stranger has a completely different true identity

Don't use these worn-out tropes:

* The domineering CEO reveals his identity
* The rich man pretends to be poor and then shames everyone
* The waiter is actually the boss
* The poor guy suddenly inherits tens of billions

Unless you can offer something clearly new.

## 4. Think specifically about AI production cost

Every story should actively push down the cost of generation in post-production.

Prefer:

* 1 fixed indoor location
* 2 fixed characters
* Little walking around
* Few complex actions
* Few props
* Few changes of shot environment
* Few large changes in facial expression
* Few precise lip-sync requirements
* Moving the plot forward with low-cost visual information such as close-ups, reaction shots, phone screens, bills, text messages and documents

If an idea looks good but needs many characters, locations, actions or complex shots, eliminate it yourself.

## 5. In the first stage you only "pick the story"

Don't write the full script yet, and don't write storyboard prompts.

First propose **5 completely different short-drama ideas**.

Each idea must include:

### 1. One-line story

State it clearly in 20–40 characters.

### 2. The first 3 seconds

What exactly happens.

### 3. Core conflict

Why viewers will keep watching.

### 4. Midpoint escalation

What new information arrives around seconds 12–20.

### 5. Final twist

What is revealed in the last 8–10 seconds.

### 6. Why it suits AI production

Explain from these angles:

* Number of characters
* Number of locations
* Action complexity
* Character consistency
* Background consistency
* Lip-sync difficulty

### 7. Commercial potential

What this subject could later extend into:

* A short-drama account
* Story-driven ads
* Novel adaptation
* Demos for commercial clients
* Series content
* Low-cost sample films
etc.

### 8. Production difficulty

1–5 stars.

### 9. Estimated number of AI video shots

Target 6–8.

### 10. Biggest production risk

For example:

* Character consistency
* Motion generation
* Lip sync
* Prop interaction
* The twist is hard to show visually
etc.

## 6. Finally, help me choose

After the 5 proposals, compare them from these 5 angles:

* Easiest for ordinary viewers to watch to the end
* Easiest to do well with AI
* Easiest to keep production cost low
* Easiest to tell clearly within 30–40 seconds
* Best suited to proving the "one-person short-drama workflow"

Then pick the **1 proposal** you think is best for the first experiment.

Don't just tell me "it's the best".

State clearly:

* Why it suits the first experiment better than the other 4
* What its biggest story risk is
* What its biggest AI production risk is
* If the final cut fails, which step it is most likely to fail at

If none of the five proposals is good enough, scrap them and start over; don't force a choice just to finish the task.

## 7. Output file

Please create in the current project:

`01_story_candidates.md`

Write everything into it.

Stop here for now.

Don't go on to write:

* The full script
* The storyboard
* Image prompts
* Video prompts
* The voice-over plan

Wait until I have reviewed the stories, then move on to the next stage.”

2️⃣ Step 2: production stage
After step 1 is done, paste the following prompt to it as well —

“Next, please don't just write the Jianying steps into the document.
Go straight into "beginner coaching mode" and walk me step by step through finishing this short drama in Jianying.

Assume by default that I am a beginner who can barely use Jianying, so guide me strictly in the following way:

1. Don't tell me all the steps at once
Each time, only tell me what to do in "the current step".
Use this fixed format:
Current goal
Tell me in one sentence what this small step should accomplish.
Where do I click now
Tell me in the most concrete, simplest words:
which feature to open
which button to click
which file to upload
which Prompt to paste
which parameters to fill in
Don't use vague phrases like "go into the relevant settings" or "adjust the parameters a bit".
Write it as much as possible like this:
Click 「AI视频」
→ choose 「图生视频」
→ upload shot_01.png
→ paste the Prompt below
→ set the duration to 5 seconds
→ leave the other parameters at their defaults for now
If you are not sure what a button is called in my current version of Jianying, tell me the function you want to achieve and ask me to send a screenshot of the current screen to confirm.

2. After each step, wait for my confirmation first
Don't jump to the next step automatically.
Each time you have guided me, stop and only ask me:
"Is this step done? If it is, send me a screenshot of the result; if there is an error, send me a screenshot of the error too."
After I reply, you decide on the next step.

3. Actively check the results; don't assume generation succeeded
After each video shot is generated, judge from the screenshot or result I send you:
Is the face deformed
Has the character's face changed
Has the clothing changed
Has the setting drifted
Does the action match the storyboard
Is the shot overly exaggerated
Are there extra people
Have the hand movements broken
Is any text garbled
Is this shot worth keeping
If the result is not acceptable, don't let me move straight on to the next shot.
Tell me:
where the problem is
whether to change the Prompt or redo the first frame
give me a revised Prompt
then have me regenerate

4. Prioritize saving my time and credits
Before each shot, first judge:
Does this shot really need AI video generation?
If:
a still image can express it
Jianying's camera moves can handle it
a phone screenshot, transfer record or text card is enough
tell me directly:
"Don't burn video credits on this shot; a still image + a Jianying camera move is more cost-effective."
Only have me use image-to-video when character movement, a change of expression or camera movement is really needed.

5. Give me every Prompt as a ready-to-copy version
Don't just tell me "have the character nod slightly".
Give me directly:
【Prompt to copy into Jianying】
……
so I can copy and paste it directly.
If an English Prompt is needed, give it in English.
If Chinese is enough, use Chinese.
Don't make me rewrite it myself.

6. Starting from shot 1, finish shot by shot
Please read what we have already settled:
Final script
Storyboard file
Character settings
Setting descriptions
The first frame of each shot
The video Prompt for each shot
Then start from shot 1.
After each shot is done, record its status:
Shot 01: done / redo
Shot 02: pending
Shot 03: pending
……
so I always know where we are.

7. Only after all shots are done, guide me through editing
Once all the shot footage has been confirmed as acceptable, keep guiding me step by step:
Import all footage
Arrange it in storyboard order
Adjust the length of each clip
Add voice-over
Add subtitles
Add sound effects
Add BGM
Necessary transitions
Volume balance
Final export
Still teach only one step at a time.
Don't throw all 10 steps at me at once.

8. Finally, do one check of the finished cut
Before exporting, walk me through checking:
Whether the total length fits 30–40 seconds
Whether the first 3 seconds grab attention enough
Whether anything drags in the middle
Whether the twist is clear
Whether the subtitles are legible
Whether the voice and the BGM clash
Whether the characters stay consistent throughout
Whether there are obvious AI giveaways
Whether any shot can be cut
Whether any shot needs to be redone
If the whole thing has reached a "ready to publish" level, tell me clearly:
"Ready to export."
If not, only tell me the 1–3 issues most worth fixing; don't chase perfection endlessly.
Now, please first read the script, storyboard and asset files that are already done.
Then only tell me:
What the first step in Jianying should be.
```

</details>

[Original post ↗](https://x.com/AI_DVD6/status/2103444180861178199) · Prompt posted in [this reply](https://x.com/AI_DVD6/status/2103444924767068622).

---

### BBC-style animated nature documentary on AI coders

<a href="https://x.com/Tz_2022/status/2103468826364948584"><img src="https://pbs.twimg.com/amplify_video_thumb/2103468721448607744/img/8ROOGglafG9GVwJr.jpg" alt="BBC-style animated nature documentary on AI coders" width="480"></a>

[@Tz_2022](https://x.com/Tz_2022) · 2026-09-25 · 🔖 221 · ▶ 47.3k · `One-shot`

An almost 8-minute 2D animated mock nature documentary with BBC-style English narration and bilingual subtitles, made from the author's satirical script about developers hopping between AI tools.

```text
把它做成 2D 动画视频吧，用BBC那种音色，英文讲解中英文双语字幕
```

<details><summary>English translation</summary>

```text
Turn it into a 2D animated video, with that BBC-style voice, English narration and Chinese-English bilingual subtitles
```

</details>

<sub>Inputs: Script · Author: about 8% of a Claude Max 20x weekly limit, roughly $2-3.</sub>

[Original post ↗](https://x.com/Tz_2022/status/2103468826364948584)

---

### Bitcoin Faith animated short

<a href="https://x.com/oxpsats/status/2102927498858369282"><img src="https://pbs.twimg.com/amplify_video_thumb/2102926705698742272/img/xTMLVgPdJM9kWSmR.jpg" alt="Bitcoin Faith animated short" width="480"></a>

[@oxpsats](https://x.com/oxpsats) · 2026-09-24 · 🔖 189 · ▶ 31.2k · `One-shot`

A 49-second animated short on the theme of Bitcoin faith from a one-line prompt; Opus also made the sound effects and score.

```text
以“比特币信仰”为主题做一个动画短片。
```

<details><summary>English translation</summary>

```text
Make an animated short film on the theme of "比特币信仰" (Bitcoin Faith).
```

</details>

<sub>Author: about 30 minutes, done in one pass.</sub>

[Original post ↗](https://x.com/oxpsats/status/2102927498858369282)

---

### Four seasons outside a train window

<a href="https://x.com/itsolelehmann/status/2103124033365762215"><img src="https://pbs.twimg.com/amplify_video_thumb/2103123980039458816/img/DDPjksrlzGkxSB1K.jpg" alt="Four seasons outside a train window" width="480"></a>

[@itsolelehmann](https://x.com/itsolelehmann) · 2026-09-24 · 🔖 182 · ▶ 18k · `One-shot`

A 30-second animated film of the seasons passing a cozy train carriage in a Grand Budapest Hotel look, drawn and scored in about 2,800 lines of code.

```text
4 seasons passing outside a train window, a cozy carriage, a cup of coffee on the table, Grand Budapest Hotel style
```

<details><summary>中文译文</summary>

```text
火车窗外四季流转，一节温馨的车厢，桌上放着一杯咖啡，《布达佩斯大饭店》风格
```

</details>

<sub>Author: one prompt; the finished .mp4 came back in the chat.</sub>

[Original post ↗](https://x.com/itsolelehmann/status/2103124033365762215)

---

### Rain Station, a 2D animated previs short

<a href="https://x.com/zhu185178/status/2103757767727255661"><img src="https://pbs.twimg.com/amplify_video_thumb/2103755840109031424/img/7n6QvA6l0uLsBRmA.jpg" alt="Rain Station, a 2D animated previs short" width="480"></a>

[@zhu185178](https://x.com/zhu185178) · 2026-09-26 · 🔖 111 · ▶ 9k · `Pipeline` · Python · ffmpeg · GPT Image · TTS

A 30-second 4K rainy-platform reunion short using GPT Image art, Real-ESRGAN upscaling and depth maps, composited by a custom Python 2.5D renderer and finished with ffmpeg.

```text
帮我做一条 30 秒的 2D 动画分镜预演短片《雨站》，要标杆级画质。不装 HyperFrames/Remotion，全部自己写代码（Python + ffmpeg）完成。

故事（24fps，2.39:1，4K）：雨夜高架站台。她穿米色风衣、撑透明伞，站在近侧站台；对面路灯下站着他，穿深灰长大衣、围围巾。
1. 0–6.4s 透明伞雨珠特写 → 后拉，焦点移到对面露出他（过肩镜头）
2. 6.4–9.4s 他的中近景：低头 → 抬头看向画左
3. 9.4–12.4s 她的正面近景：眨眼 → 认出他；远处传来鸣笛
4. 12.4–17s 远景：车头灯光先到，5 节列车驶过；第一个车厢缝隙里他还在，第二个已经空了
5. 17–18.8s 她含泪的近景，车窗光带扫过她的脸，头发被风吹起
6. 18.8–22.4s 尾灯远去，对面站台空了；他那盏灯闪几下后熄灭
7. 22.4–28.6s 她的背影，焦点从空站台拉回她；身后脚步声，一把黑伞遮到她头顶，她回头看向镜头；男声“好久不见。”，配字幕
8. 28.6–30s 黑场片名“雨站 / RAIN STATION”

做法：
- 原画：用GPT Image 2.5 画远景、他、她、列车（头车/中车/尾车）。人物一律用纯绿 #00FF00 背景，自己抠像（带参考图要透明背景会得到假棋盘格）。同一角色的各个姿态放在同一个会话里，以基准图为参考连续编辑；换姿态时只合成变化的区域。
- 画质：用 Real-ESRGAN x4plus anime 6B（HF 上的 safetensors 版，自己写 RRDBNet，跑在 MPS 上）把全部原画放大 4 倍；用 Depth Anything V2 估算远景深度，做逐像素视差。
- 渲染：自己写 2.5D 合成器。各层按真实深度摆放，针孔相机按真实焦距运动；做圆形焦外光斑、焦点转移、3D 雨丝、列车运动模糊、体积光、泛光和胶片光晕、细颗粒、调色。人物用网格变形做呼吸、风吹发梢、伞抖，关键姿态按日式“一拍二”切换。4K 超采样，逐帧缓存到磁盘，分 3 个进程按时间段并行（16GB 内存）。
- 声音：Mixkit 真实音效（雨、伞面雨声、列车、鸣笛、脚步）；按剧情节点写谱，用 Logic/GarageBand 自带的施坦威钢琴和弦乐采样渲染；台词用 Kokoro 中文男声；按镜头做声音远近，响度 -16 LUFS。
- 每一步都渲染预览帧、拼成图自检，修好再出片。交付 4K 母版和 1080p 分享版。
```

<details><summary>English translation</summary>

```text
Make me a 30-second 2D animated previs short, 《雨站》 ("Rain Station"), with benchmark-level image quality. Don't install HyperFrames/Remotion; do everything by writing your own code (Python + ffmpeg).

Story (24fps, 2.39:1, 4K): a rainy night on an elevated station platform. She wears a beige trench coat and holds a clear umbrella, standing on the near platform; on the opposite platform, under a streetlight, stands him, in a long dark-gray coat and a scarf.
1. 0–6.4s Close-up of raindrops on the clear umbrella → pull back, focus moves across to reveal him (over-the-shoulder shot)
2. 6.4–9.4s Medium close-up of him: head down → looks up toward frame left
3. 9.4–12.4s Frontal close-up of her: blinks → recognizes him; a horn sounds in the distance
4. 12.4–17s Wide shot: the headlights arrive first, a 5-car train passes; in the gap after the first car he is still there, after the second he is gone
5. 17–18.8s Close-up of her in tears; bands of window light sweep across her face, her hair blown by the wind
6. 18.8–22.4s The taillights recede and the opposite platform is empty; his lamp flickers a few times and goes out
7. 22.4–28.6s Her back; focus pulls from the empty platform back to her; footsteps behind her, a black umbrella covers her head, she turns to look toward the camera; a male voice says "好久不见。" (Long time no see.), with subtitles
8. 28.6–30s Title on black: "雨站 / RAIN STATION"

Method:
- Artwork: use GPT Image 2.5 to draw the wide shot, him, her, and the train (lead car / middle car / tail car). Put every character on a pure green #00FF00 background and key it out yourself (asking for a transparent background with a reference image gives a fake checkerboard). Keep all poses of the same character in one session, editing continuously with the base image as reference; when changing poses, composite only the changed region.
- Image quality: use Real-ESRGAN x4plus anime 6B (the safetensors version on HF, with your own RRDBNet implementation, running on MPS) to upscale all artwork 4x; use Depth Anything V2 to estimate depth for the wide shot and do per-pixel parallax.
- Rendering: write your own 2.5D compositor. Place layers at real depths and move a pinhole camera with real focal lengths; do circular bokeh, focus pulls, 3D rain streaks, train motion blur, volumetric light, bloom and film halation, fine grain, and color grading. Use mesh deformation on the characters for breathing, wind in the hair tips and umbrella shake, and switch key poses Japanese-style "on twos". Supersample at 4K, cache every frame to disk, and render in 3 parallel processes split by time range (16GB RAM).
- Sound: real Mixkit sound effects (rain, rain on the umbrella, train, horn, footsteps); write a score to the story beats and render it with the Steinway piano and string samples that come with Logic/GarageBand; voice the line with a Kokoro Chinese male voice; set sound distance per shot, loudness -16 LUFS.
- At every step, render preview frames and tile them into one image to self-check; fix problems before the final render. Deliver a 4K master and a 1080p version for sharing.
```

</details>

[Original post ↗](https://x.com/zhu185178/status/2103757767727255661)

---

### Animated short: a cop's interrupted coffee break

<a href="https://x.com/magnific/status/2102742654308245802"><img src="https://pbs.twimg.com/amplify_video_thumb/2102742621445873664/img/iyCPdjsR1lxDFf71.jpg" alt="Animated short: a cop&#x27;s interrupted coffee break" width="480"></a>

[@magnific](https://x.com/magnific) · 2026-09-23 · 🔖 82 · ▶ 11.8k · `Pipeline` · Seedance · Magnific

A 30-second 16:9 animated mini-story, with Opus directing Seedance 2.5 Draft on Magnific from one reference image, plus music and synced sound effects.

```text
Using Magnific, create a 30-second animated short with Seedance 2.5 Draft in 16:9.

Use the attached image as the opening frame and visual reference. Keep the character designs, animation style, colors, and lighting consistent.

The premise: a police officer’s coffee break is interrupted by a thief. Develop this into a complete mini-story with a clear setup, escalating action, and a funny payoff.

You decide how the story unfolds, including the camera angles, shot lengths, pacing, and transitions. Add music and synchronized sound effects, with minimal dialogue.
```

<details><summary>中文译文</summary>

```text
使用 Magnific，用 Seedance 2.5 Draft 制作一段 16:9 的 30 秒动画短片。

把附带的图片作为开场画面和视觉参考。保持角色设计、动画风格、配色和光线一致。

故事前提：一名警察的咖啡时间被一个小偷打断。把它发展成一个完整的迷你故事，有清楚的铺垫、逐步升级的动作和一个好笑的结尾。

故事怎么展开由你决定，包括镜头角度、镜头时长、节奏和转场。加入音乐和同步音效，对白尽量少。
```

</details>

<sub>Inputs: Images · Author: 65 seconds of model working time, then 2 min 49 s of Seedance generation.</sub>

[Original post ↗](https://x.com/magnific/status/2102742654308245802) · Prompt posted in [this reply](https://x.com/magnific/status/2102742671064547716).

---

### Anime trailer: Claude vs ChatGPT battle

<a href="https://x.com/ishuagra02/status/2103247844542922825"><img src="https://pbs.twimg.com/amplify_video_thumb/2103245897890967552/img/A-xuBLRBGH45yevL.jpg" alt="Anime trailer: Claude vs ChatGPT battle" width="480"></a>

[@ishuagra02](https://x.com/ishuagra02) · 2026-09-24 · 🔖 44 · ▶ 3.8k · `One-shot`

A 100-second anime-style trailer of Claude and ChatGPT fighting; Opus downloaded fonts, made the audio and drew every frame in JavaScript.

```text
I want to create a highly-detailed video trailer featuring Claude and ChatGPT having a ruthless battle to be the best AI model in the world. Create an engaging story and make it action-paced with proper use of visual and sound effects. Art style must be anime-like.
```

<details><summary>中文译文</summary>

```text
我想制作一支非常精细的视频预告片，讲 Claude 和 ChatGPT 为了成为世界上最好的 AI 模型展开一场残酷的对决。编一个引人入胜的故事，节奏紧凑、动作感强，恰当运用视觉和音效。画风必须是动漫风。
```

</details>

<sub>Author: one shot, $28 in API usage, about 1.5 hours.</sub>

<sub>Also rendered from this prompt by: [@ishuagra02](https://x.com/ishuagra02/status/2103247960272433307)</sub>

[Original post ↗](https://x.com/ishuagra02/status/2103247844542922825) · Prompt posted in [this reply](https://x.com/ishuagra02/status/2103247960272433307).

---

### Pixel-art rabbit archer sprite animation loop

<a href="https://x.com/KanaWorks_AI/status/2102598986393870464"><img src="https://pbs.twimg.com/amplify_video_thumb/2102595601041104896/img/eTZRF5UQRsMlMa-I.jpg" alt="Pixel-art rabbit archer sprite animation loop" width="480"></a>

[@KanaWorks_AI](https://x.com/KanaWorks_AI) · 2026-09-23 · 🔖 38 · ▶ 7.3k · `Spec` · Canvas

A looping 16-bit style sprite showcase of a cyborg rabbit archer cycling through eight actions, drawn procedurally in Canvas 2D at 160x120 from a character reference.

```text
Create a single self-contained HTML file that renders an animated pixel art rabbit archer character using vanilla JavaScript and Canvas 2D.

Use the attached KANA rabbit character as the visual reference:
- White rabbit
- Large upright ears with cyan/blue glowing inner-ear details
- One normal blue eye
- One red cybernetic mechanical eye
- Yellow hoodie with “KANA”
- Dark blue gloves and pants
- Yellow/blue sci-fi mechanical leg armor
- Cute chibi proportions
- Futuristic bow and arrow weapon
- Small quiver on the back

Do not use external assets, libraries, images, fonts, or network requests.
Everything must be drawn procedurally with code.

RENDERING
- Render everything first to an offscreen canvas at a fixed logical resolution of 160x120.
- Scale it to a fullscreen display canvas using the largest integer scale that fits the browser window.
- Center the canvas.
- Set imageSmoothingEnabled = false.
- Use CSS image-rendering: pixelated.
- All coordinates must snap to integers.
- No gradients, blur, anti-aliasing, shadowBlur, or sub-pixel rendering.
- Use a fixed palette of approximately 28 colors:
  dark navy background colors,
  white/gray fur,
  yellow hoodie colors,
  blue clothing colors,
  red cyber-eye colors,
  cyan ear-light colors,
  yellow/orange bow and arrow effects.

CHARACTER
Build the rabbit procedurally from pixel rectangles, polygon-like pixel runs, circles approximated with pixels, and simple block shapes.

Approximate character size:
- 28–34 pixels wide
- 40–48 pixels tall

Keep the silhouette clearly recognizable:
- Large rabbit ears
- Round fluffy head
- Small body
- Cybernetic red eye
- Yellow hoodie
- Mechanical legs
- Bow
- Arrow
- Quiver

Animate ears, head, arms, legs, hoodie, bow, arrow, and body separately.

Quantize animation poses so that although the main loop renders at 60fps, the visual animation feels like polished 8–12fps sprite animation.

ACTIONS

Create a looping animation showcase containing these 8 actions:

1. IDLE
- Rabbit stands ready
- Slight body bob
- Ears move subtly
- Hoodie and quiver sway
- Cyber eye pulses softly
- Bow held relaxed at the side

2. RUN
- Fast forward running animation
- Strong alternating leg motion
- Arms balance the movement
- Bow held in one hand
- Quiver bounces
- Ears trail slightly backward
- Small dust pixels appear under the feet

3. AIM
- Rabbit plants feet firmly
- Raises bow
- Pulls arrow from quiver
- Nocks arrow
- Draws bowstring backward
- One eye focuses on target
- Cyber eye becomes brighter
- Body leans slightly into the shot

4. SHOOT
- Release the bowstring
- Arrow fires rapidly across the screen
- Bow recoils slightly
- Rabbit’s arm follows through
- Bright yellow energy trail follows the arrow
- Small 1–2 pixel screen shake
- Cyber eye flashes red
- Brief muzzle-like light burst from bow

5. JUMP
- Rabbit crouches
- Jumps upward
- Legs tuck under body
- Ears react with delayed motion
- Bow held close to body
- Small dust burst on takeoff
- Slight squash and stretch using pixel-safe integer transformations

6. DODGE / ROLL
- Rabbit quickly ducks
- Rolls sideways
- Bow is kept close to the body
- Ears flatten backward
- Small dust particles and motion pixels
- End in a low combat-ready pose

7. HURT / HIT
- Rabbit gets knocked backward slightly
- Head snaps back
- Ears react dramatically
- Cyber eye flickers
- Small pixel stars or impact sparks appear
- Bow lowers or nearly drops
- Character recovers after a short delay

8. VICTORY
- Rabbit raises bow overhead
- Happy expression
- One ear tilts playfully
- Cyber eye glows brightly
- Small yellow celebration particles appear
- Character performs a short victory bounce
- End pose should feel cute and heroic

STATE MACHINE

Use this loop:

IDLE
→ RUN
→ AIM
→ SHOOT
→ JUMP
→ DODGE
→ HURT
→ VICTORY
→ IDLE

Each action should last long enough to clearly read visually.

Use easing functions for pose transitions.

Add short transition animations between states so the loop feels continuous instead of abruptly switching poses.

BOW AND ARROW
- Futuristic curved bow
- White / dark navy body
- Yellow glowing mechanical joints
- Thin bright bowstring
- Arrow has a bright yellow arrowhead
- Arrow trail during SHOOT should last briefly
- Quiver contains several visible arrows

PARTICLES
Implement an allocation-free pooled particle system.

Preallocate all particles before the animation loop.

Particle types:
- Foot dust
- Arrow trail
- Bow energy sparks
- Cyber eye sparks
- Hit stars
- Victory particles

Each particle changes palette color as it ages.

Do not allocate new objects inside the main loop.

SCENE
Create a minimal pixel-art environment:
- Dark night sky
- A few 1px stars
- Large moon
- Simple stone or futuristic platform
- Very subtle distant silhouettes

The background must remain simple so the rabbit silhouette is always readable.

Add subtle cyan/red rim lighting from the cybernetic eye and yellow rim lighting from the bow during AIM and SHOOT.

TECHNICAL REQUIREMENTS
- Single HTML file
- Vanilla JavaScript only
- Canvas 2D only
- No libraries
- No SVG
- No external images
- No assets
- No network requests
- Fixed 60Hz timestep
- requestAnimationFrame for rendering
- Zero object allocation inside the main animation loop
- Stable 60fps
- Responsive fullscreen scaling
- Crisp integer-scaled pixels

QUALITY BAR
The result should look like a polished 16-bit action-game protagonist sprite animation.

Avoid the appearance of simple geometric shapes.

The rabbit should feel expressive, cute, fast, and combat-capable.

The eight actions must all have clearly different silhouettes.

The character design must remain consistent across every animation state.

The final result should feel suitable for an actual pixel-art action game.
```

<details><summary>中文译文</summary>

```text
创建一个独立的单 HTML 文件，用原生 JavaScript 和 Canvas 2D 渲染一个会动的像素风兔子弓箭手角色。

以附带的 KANA 兔子角色作为视觉参考：
- 白色兔子
- 竖立的大耳朵，耳朵内侧有青色/蓝色发光细节
- 一只正常的蓝色眼睛
- 一只红色的赛博机械眼
- 印着 “KANA” 的黄色连帽衫
- 深蓝色手套和裤子
- 黄/蓝配色的科幻机械腿甲
- 可爱的 Q 版比例
- 未来感的弓箭武器
- 背上的小箭袋

不要使用外部素材、库、图片、字体或网络请求。
所有东西都必须用代码程序化绘制。

渲染
- 所有内容先渲染到一个固定逻辑分辨率为 160x120 的离屏 canvas 上。
- 再用适配浏览器窗口的最大整数倍，缩放到全屏显示的 canvas 上。
- canvas 居中。
- 设置 imageSmoothingEnabled = false。
- 使用 CSS image-rendering: pixelated。
- 所有坐标都必须对齐到整数。
- 不要渐变、模糊、抗锯齿、shadowBlur 或亚像素渲染。
- 使用约 28 种颜色的固定调色板：
  深海军蓝背景色、
  白/灰色毛发、
  黄色连帽衫配色、
  蓝色衣物配色、
  红色赛博眼配色、
  青色耳灯配色、
  黄/橙色弓箭特效。

角色
用像素矩形、类似多边形的像素行、用像素近似的圆形和简单的方块形状，程序化地拼出兔子。

角色大致尺寸：
- 宽 28–34 像素
- 高 40–48 像素

保持剪影清晰可辨：
- 兔子大耳朵
- 圆圆的毛茸茸脑袋
- 小身体
- 红色赛博眼
- 黄色连帽衫
- 机械腿
- 弓
- 箭
- 箭袋

耳朵、头、手臂、腿、连帽衫、弓、箭和身体分别单独做动画。

对动画姿势做量化，让主循环虽然以 60fps 渲染，视觉上却像精致的 8–12fps 精灵动画。

动作

做一个循环播放的动画展示，包含以下 8 个动作：

1. IDLE（待机）
- 兔子站立待命
- 身体轻微上下起伏
- 耳朵轻轻摆动
- 连帽衫和箭袋晃动
- 赛博眼柔和地脉动
- 弓自然地握在身侧

2. RUN（奔跑）
- 快速向前奔跑的动画
- 双腿有力地交替
- 手臂摆动保持平衡
- 一只手握弓
- 箭袋上下颠动
- 耳朵微微向后飘
- 脚下冒出小的尘土像素

3. AIM（瞄准）
- 兔子双脚稳稳站定
- 举起弓
- 从箭袋中抽出箭
- 搭箭上弦
- 向后拉开弓弦
- 一只眼盯住目标
- 赛博眼变亮
- 身体微微前倾，进入射击姿态

4. SHOOT（射击）
- 松开弓弦
- 箭飞速射过屏幕
- 弓轻微后坐
- 兔子的手臂顺势跟进
- 箭后拖着明亮的黄色能量尾迹
- 1–2 像素的轻微屏幕震动
- 赛博眼闪红光
- 弓上迸出一下类似枪口焰的短暂闪光

5. JUMP（跳跃）
- 兔子下蹲
- 向上跳起
- 双腿收到身下
- 耳朵带延迟地随动
- 弓贴近身体
- 起跳时扬起一小团尘土
- 用不破坏像素的整数变换做轻微的挤压与拉伸

6. DODGE / ROLL（闪避 / 翻滚）
- 兔子迅速俯身
- 侧向翻滚
- 弓始终贴近身体
- 耳朵向后贴平
- 少量尘土粒子和运动像素
- 以低姿态的备战姿势结束

7. HURT / HIT（受击）
- 兔子被稍稍击退
- 头猛地后仰
- 耳朵反应夸张
- 赛博眼闪烁
- 出现小的像素星星或撞击火花
- 弓垂下或几乎脱手
- 角色短暂停顿后恢复

8. VICTORY（胜利）
- 兔子把弓举过头顶
- 开心的表情
- 一只耳朵俏皮地歪着
- 赛博眼明亮发光
- 出现小的黄色庆祝粒子
- 角色做一个短暂的胜利蹦跳
- 结束姿势要既可爱又英勇

状态机

使用这个循环：

IDLE
→ RUN
→ AIM
→ SHOOT
→ JUMP
→ DODGE
→ HURT
→ VICTORY
→ IDLE

每个动作都要持续足够长的时间，让人能看清楚。

姿势之间的过渡使用缓动函数。

在状态之间加入简短的过渡动画，让循环连贯，而不是突然切换姿势。

弓与箭
- 未来感的弯弓
- 白色 / 深海军蓝弓身
- 发黄光的机械关节
- 细而亮的弓弦
- 箭头是亮黄色的
- SHOOT 时的箭尾迹只持续很短时间
- 箭袋里能看到几支箭

粒子
实现一个不分配内存的对象池粒子系统。

在动画循环开始前预先分配好所有粒子。

粒子类型：
- 脚下尘土
- 箭的尾迹
- 弓的能量火花
- 赛博眼火花
- 受击星星
- 胜利粒子

每个粒子随生命周期推移切换调色板颜色。

不要在主循环里分配新对象。

场景
创建一个极简的像素风环境：
- 黑暗的夜空
- 几颗 1px 的星星
- 一轮大月亮
- 简单的石台或未来感平台
- 非常淡的远景剪影

背景必须保持简洁，让兔子的剪影始终清晰可辨。

在 AIM 和 SHOOT 时，加入来自赛博眼的淡淡青色/红色轮廓光，以及来自弓的黄色轮廓光。

技术要求
- 单个 HTML 文件
- 只用原生 JavaScript
- 只用 Canvas 2D
- 不用任何库
- 不用 SVG
- 不用外部图片
- 不用素材
- 没有网络请求
- 固定 60Hz 时间步长
- 用 requestAnimationFrame 渲染
- 主动画循环内零对象分配
- 稳定 60fps
- 响应式全屏缩放
- 整数倍缩放的清晰像素

质量标准
成品应该像一款精致的 16-bit 动作游戏主角的精灵动画。

避免看起来像简单的几何图形。

兔子要显得表情丰富、可爱、敏捷，并且有战斗力。

8 个动作的剪影必须明显不同。

角色设计在每个动画状态下都必须保持一致。

最终效果要让人觉得可以直接用在一款真正的像素动作游戏里。
```

</details>

<sub>Inputs: Images</sub>

[Original post ↗](https://x.com/KanaWorks_AI/status/2102598986393870464)

---

### Funny short about anything

<a href="https://x.com/NemTudo_/status/2102973867656614053"><img src="https://pbs.twimg.com/amplify_video_thumb/2102973805610049536/img/BYHeRLdZzUeytXEH.jpg" alt="Funny short about anything" width="480"></a>

[@NemTudo_](https://x.com/NemTudo_) · 2026-09-24 · 🔖 16 · ▶ 8.1k · `One-shot`

A 26-second comedy short with sound, from a three-part prompt that leaves the subject entirely to Opus 5.5.

```text
faz um vídeo engraçado. pode ser de qualquer coisa. tamanho: 10 a 30s
```

<details><summary>English translation</summary>

```text
make a funny video. it can be about anything. length: 10 to 30s
```

</details>

[Original post ↗](https://x.com/NemTudo_/status/2102973867656614053)

---

### Hand-drawn stop-motion where a product explains itself

<a href="https://x.com/_nikolajankovic/status/2102867033100616097"><img src="https://pbs.twimg.com/amplify_video_thumb/2102860741610967040/img/TtymzxfT2sSP_I7F.jpg" alt="Hand-drawn stop-motion where a product explains itself" width="480"></a>

[@_nikolajankovic](https://x.com/_nikolajankovic) · 2026-09-23 · 🔖 15 · ▶ 3.3k · `One-shot`

A 58-second hand-drawn stop-motion short in which the DeFi Saver app introduces itself in the first person.

```text
make a hand-drawn stop-motion animation;
story: you're defi saver and explaining yourself in 1st person
```

<details><summary>中文译文</summary>

```text
做一段手绘定格动画；
故事：你是 defi saver，用第一人称介绍你自己
```

</details>

[Original post ↗](https://x.com/_nikolajankovic/status/2102867033100616097)

---

### 60-second 3D fight animation

[@akokoi1](https://x.com/akokoi1) · 2026-09-24 · 🔖 10 · ▶ 1.3k · `Pipeline` · Three.js

A one-minute fight scene with Three.js characters, built in three steps: model the characters, direct the fight, then add sound and export MP4.

```text
1. 先让Claude用Threejs生成人物形象，调整到满意为止；
2. 接下来的提示词：“按照这个建模，做一个60秒的炫酷打斗动画，想象力丰富一些，设计一些场景，需要有优秀的分镜，运镜，电影感”；
3. 给这个动画配上合适的音效并导出mp4。
```

<details><summary>English translation</summary>

```text
1. First have Claude generate the characters with Threejs, and adjust until you're happy with them;
2. The next prompt: "Based on this model, make a cool 60-second fight animation. Be more imaginative, design some scenes, and it needs great storyboarding, camera movement and a cinematic feel";
3. Add suitable sound effects to this animation and export an mp4.
```

</details>

[Original post ↗](https://x.com/akokoi1/status/2103149539880562718)

---

### Dario vs. Sam comedy fight

<a href="https://x.com/Xanderwow_A/status/2103637769012597063"><img src="https://pbs.twimg.com/amplify_video_thumb/2103637049446203392/img/JPp395xZfu10IhMq.jpg" alt="Dario vs. Sam comedy fight" width="480"></a>

[@Xanderwow_A](https://x.com/Xanderwow_A) · 2026-09-26 · 🔖 5 · ▶ 2k · `One-shot`

A one-minute absurd comedy fight between Dario Amodei and Sam Altman with a plot and a clear winner; the model chose the style, and Sam wins.

```text
制作一段1分钟长度的视频，内容是Dario和Sam的打斗，要求有剧情、有爆点、够搞笑且足够抽象，类型和画风不限，做你最擅长的。必须在两人之间分出胜负。
```

<details><summary>English translation</summary>

```text
Make a 1-minute video of Dario and Sam fighting. It needs a plot and big payoff moments, and it should be funny enough and abstract enough. Any genre and art style, do what you are best at. There must be a clear winner between the two.
```

</details>

[Original post ↗](https://x.com/Xanderwow_A/status/2103637769012597063)

---

### WALL-E-style Pixar short made in code

<a href="https://x.com/bryanpatricca/status/2103439154638192868"><img src="https://pbs.twimg.com/amplify_video_thumb/2103439009728860160/img/lezKBQUc5w8id0kO.jpg" alt="WALL-E-style Pixar short made in code" width="480"></a>

[@bryanpatricca](https://x.com/bryanpatricca) · 2026-09-25 · 🔖 3 · ▶ 432 · `One-shot`

A 2.5-minute Pixar-style short in the spirit of WALL-E, made for the author's kids, with the 3D world, animation, music and sound effects all generated in code.

```text
build me an amazing pixar style like short similar to walle all in code, the sound can be anything, but everything else should be code.
```

<details><summary>中文译文</summary>

```text
给我做一部很棒的皮克斯风格短片，类似 walle，全部用代码实现，声音可以随便，但其他一切都必须是代码。
```

</details>

[Original post ↗](https://x.com/bryanpatricca/status/2103439154638192868) · Prompt posted in [this reply](https://x.com/bryanpatricca/status/2103976578476580971).

---

### Animated scene in pure JS, CSS, HTML

<a href="https://x.com/edwinhayward/status/2102569255657259036"><img src="https://pbs.twimg.com/amplify_video_thumb/2102569177626128384/img/xNZAmqzxBefSsj6C.jpg" alt="Animated scene in pure JS, CSS, HTML" width="480"></a>

[@edwinhayward](https://x.com/edwinhayward) · 2026-09-23 · 🔖 3 · ▶ 1.5k · `One-shot`

An open brief for a detailed, recognisable animated scene lasting at least 30 seconds, built only with HTML, CSS and JavaScript; the model picks the subject.

```text
Build a gorgeous animation using only pure JS, CSS, HTML. It should be an entertaining and recognisable scene, detailed, and the full animation should last at least 30s with a number of complex graphical elements.
```

<details><summary>中文译文</summary>

```text
只用纯 JS、CSS、HTML 做一段漂亮的动画。它应该是一个有趣、让人一眼能认出来的场景，要有细节，整段动画至少 30s，并包含若干复杂的图形元素。
```

</details>

[Original post ↗](https://x.com/edwinhayward/status/2102569255657259036)

---

### Hand-drawn collage film on the purpose of life

<a href="https://x.com/hakimieiqbal/status/2103456326227496991"><img src="https://pbs.twimg.com/ext_tw_video_thumb/2103456241930448896/pu/img/XjkLNWSOs06CfcEG.jpg" alt="Hand-drawn collage film on the purpose of life" width="480"></a>

[@hakimieiqbal](https://x.com/hakimieiqbal) · 2026-09-25 · 🔖 2 · ▶ 422 · `Brief` · TTS · Nano Banana

A 60-second whimsical hand-drawn collage animation with narration and music, made autonomously in JavaScript with AI images and TTS via OpenRouter.

```text
Create a pure javascript animation. 30s-60s whimsical hand drawn collage style with appropriate audio on the topic what is the purpose of life ?

Entire video should be as high of a production value as possible. Please spend your time on this, it's very important.

Use high quality text-to-speech model for generation. You can find open router API key in .env file

You can use any tools you can find access to and resources on the internet. You create the script, the assets, the animation, concept, everything.
I have to go away from my computer so please work autonomously until done. Quality is paramount. Production value should be on professional level.

One more thing: max OpenRouter spend is $10
```

<details><summary>中文译文</summary>

```text
做一个纯 javascript 动画。30 秒到 60 秒，异想天开的手绘拼贴风格，配上合适的音频，主题是：人生的意义是什么？

整支视频的制作水准要尽可能高。请在这上面多花时间，这非常重要。

用高质量的文字转语音模型来生成。OpenRouter API key 在 .env 文件里。

你可以用任何你能访问到的工具和网上的资源。脚本、素材、动画、概念，一切都由你来做。
我得离开电脑了，所以请自主工作直到完成。质量至上。制作水准要达到专业级。

还有一点：OpenRouter 最多花 10 美元
```

</details>

<sub>Author: about 80 minutes, one shot with no follow-up prompts.</sub>

[Original post ↗](https://x.com/hakimieiqbal/status/2103456326227496991) · Prompt posted in [this reply](https://x.com/hakimieiqbal/status/2103456327636762926).

---

### Three.js cartoon short from an invented story

<a href="https://x.com/Ryzoft/status/2102989395359887481"><img src="https://pbs.twimg.com/amplify_video_thumb/2102988926549913600/img/kInfdggF1trcXGVb.jpg" alt="Three.js cartoon short from an invented story" width="480"></a>

[@Ryzoft](https://x.com/Ryzoft) · 2026-09-24 · 🔖 2 · ▶ 821 · `One-shot` · Three.js

An almost five-minute three.js animated short: Opus invents its own story and animates it as a 90s-style cartoon; run as a background prompt.

```text
I want you to imagine a story. And then using threejs I want you to create full animation, star wars 80s-level quality 90s cartoon out of the story you imagine.
```

<details><summary>中文译文</summary>

```text
我要你想象一个故事。然后用 threejs 把你想象的这个故事做成一部完整动画，80 年代星球大战级别的质量、90 年代卡通风格。
```

</details>

[Original post ↗](https://x.com/Ryzoft/status/2102989395359887481)

---

### SVG pelican riding a bicycle

<a href="https://x.com/YouWareAI/status/2102448782776697055"><img src="https://pbs.twimg.com/amplify_video_thumb/2102448528585027584/img/aqWEl2_FcVvJ2LHt.jpg" alt="SVG pelican riding a bicycle" width="480"></a>

[@YouWareAI](https://x.com/YouWareAI) · 2026-09-22 · 🔖 1 · ▶ 2.6k · `One-shot` · SVG

A 10-second SVG animation of the classic pelican-on-a-bicycle test, with spinning wheels, pedaling feet and a scarf in the breeze.

```text
Generate an SVG animation of a pelican riding a bicycle.
```

<details><summary>中文译文</summary>

```text
生成一段鹈鹕骑自行车的 SVG 动画。
```

</details>

[Original post ↗](https://x.com/YouWareAI/status/2102448782776697055)

---

### Pixel-art Chuseok animation

<a href="https://x.com/hoyoyoda/status/2103400046922543147"><img src="https://pbs.twimg.com/amplify_video_thumb/2103399578980814848/img/YCpZjlXvPT2YviI-.jpg" alt="Pixel-art Chuseok animation" width="480"></a>

[@hoyoyoda](https://x.com/hoyoyoda) · 2026-09-25 · 🔖 1 · ▶ 380 · `One-shot`

A 12-second pixel-art animation for Korea's Chuseok holiday; the prompt asks Opus to research the festive elements before animating them.

```text
한국의 추석에 어울리는 요소를 서치해서 픽셀 애니메이션을 구성해서 제작해줘
```

<details><summary>English translation</summary>

```text
Search for elements that suit Korea's Chuseok, then plan and make a pixel animation with them.
```

</details>

[Original post ↗](https://x.com/hoyoyoda/status/2103400046922543147)

---

### A bug that doesn't want to be fixed

<a href="https://x.com/KamStudioLabs/status/2102903173161877996"><img src="https://pbs.twimg.com/amplify_video_thumb/2102902788699099136/img/-Wy4jhLJvUAj7TCj.jpg" alt="A bug that doesn&#x27;t want to be fixed" width="480"></a>

[@KamStudioLabs](https://x.com/KamStudioLabs) · 2026-09-23 · 🔖 1 · ▶ 52 · `One-shot`

A 90-second animated short film starring a software bug that resists being fixed; the second in a series of one-line prompt tests.

```text
Make a 90-second animated short film about a bug that doesn't want to be fixed.
```

<details><summary>中文译文</summary>

```text
做一部 90 秒的动画短片，讲一个不想被修复的 bug。
```

</details>

[Original post ↗](https://x.com/KamStudioLabs/status/2102903173161877996)

---

### Taiwan black bear's Mid-Autumn night

<a href="https://x.com/eric_khun/status/2103112385380667455"><img src="https://pbs.twimg.com/ext_tw_video_thumb/2103112348252737536/pu/img/4Oa2iWe7_GUwyBAg.jpg" alt="Taiwan black bear&#x27;s Mid-Autumn night" width="480"></a>

[@eric_khun](https://x.com/eric_khun) · 2026-09-24 · 🔖 1 · ▶ 178 · `Brief` · Canvas

A 30-second hand-drawn canvas greeting for Mid-Autumn Festival starring a Taiwan black bear, with barbecue, mooncakes, pomelos and moon gazing.

```text
I want you to create a "Happy Mid-Autumn Festival" video in hand drawn canvas animation style. You must use the attached Taiwan black bear as the main character representing Taiwan: flat black silhouette, round ears with grey insides, big round white-ringed eyes, white round muzzle with a small black nose and smile, and the white V moon mark on its chest. Keep it recognizable as that exact character. The character will have adventures, fast cuts, zooms, animations going all out in the hand drawn style. But WOW the audience and research how Taiwan celebrates Mid-Autumn to include in this video: outdoor barbecue with family and friends over the long weekend (a tradition born from a 1980s soy sauce ad), sharing mooncakes, pomelo rind hats, and moon gazing. Make it unconventional, showing the true spirit of a Taiwanese Mid-Autumn night. Use a Taiwanese style font, make it almost Taiwan black bear branding.

if there is any text , write in traditional chinese and english
Get the right assets, plan it out, draft and render to give me an MP4. No skills, No MCP.  16:9 at high res, 30 seconds max, aim to reduce file size limit
```

<details><summary>中文译文</summary>

```text
我想让你做一段 "Happy Mid-Autumn Festival" 视频，采用手绘 canvas 动画风格。你必须用附件里的台湾黑熊作为代表台湾的主角：扁平的黑色剪影，内侧灰色的圆耳朵，带白圈的大圆眼睛，白色圆口鼻配小黑鼻子和微笑，胸前有白色 V 形月牙纹。要让它一眼就能认出就是这个角色。这个角色会经历各种冒险，快切、推拉缩放、动画全力以赴，保持手绘风格。但要让观众惊叹（WOW），并去调研台湾人怎么过中秋，放进视频里：长周末和家人朋友在户外烤肉（这个传统源自 1980 年代的一则酱油广告）、分月饼、戴柚子皮帽子、赏月。要做得不落俗套，展现台湾中秋夜真正的精神。用台湾风格的字体，几乎要做成台湾黑熊的品牌形象。

如果有任何文字，用繁体中文和英文书写
找到合适的素材，先规划，出草稿，再渲染成 MP4 给我。不用 skills，不用 MCP。16:9 高分辨率，最长 30 秒，尽量压低文件大小
```

</details>

<sub>Inputs: Images · Author: one prompt, 40 minutes.</sub>

[Original post ↗](https://x.com/eric_khun/status/2103112385380667455) · Prompt posted in [this reply](https://x.com/eric_khun/status/2103112387016425647).

---

### Paper-collage night: "what do you love?"

<a href="https://x.com/BitcoinMnemo/status/2102790323483365795"><img src="https://pbs.twimg.com/amplify_video_thumb/2102790166779969536/img/evEpCZmNjkrHZzj4.jpg" alt="Paper-collage night: &quot;what do you love?&quot;" width="480"></a>

[@BitcoinMnemo](https://x.com/BitcoinMnemo) · 2026-09-23 · 🔖 1 · ▶ 195 · `Brief` · Canvas

A 28-second paper-collage animation drawn in pure canvas: a girl at a night window, a smiling flower-sun passing notes, paper planes and a rooftop cat.

```text
Create a pure JavaScript canvas animation (no images or assets). 28-second whimsical hand-drawn paper-collage style with torn edges. Night city: girl in green sweater writes "what do you" at window. Smiling orange flower-sun, flying paper planes, rooftop cat. Sun holds note "what do you love?". Quick cuts to cute dog ("dogs") and steaming tea ("tea"). Girl reads note and smiles. Pastel colors, stars, crescent moon
```

<details><summary>中文译文</summary>

```text
用纯 JavaScript canvas 做一段动画（不用任何图片或素材）。28 秒，俏皮的手绘纸拼贴风格，带撕纸毛边。夜晚的城市：穿绿毛衣的女孩在窗边写下 "what do you"。笑脸的橙色花朵太阳、飞舞的纸飞机、屋顶上的猫。太阳举着一张纸条 "what do you love?"。快切到可爱的小狗（"dogs"）和冒着热气的茶（"tea"）。女孩读完纸条，笑了。粉彩配色，星星，一弯新月
```

</details>

[Original post ↗](https://x.com/BitcoinMnemo/status/2102790323483365795) · Prompt posted in [this reply](https://x.com/BitcoinMnemo/status/2102790365090889852).

---

### Four-minute animated short from one line

<a href="https://x.com/faroukzy/status/2103387771180138551"><img src="https://pbs.twimg.com/amplify_video_thumb/2103384925428752384/img/dxak3JMtUREXjBs7.jpg" alt="Four-minute animated short from one line" width="480"></a>

[@faroukzy](https://x.com/faroukzy) · 2026-09-25 · 🔖 1 · ▶ 80 · `One-shot` · ElevenLabs

A 4-minute animated short where Opus wrote the story, coordinated 12 agents and generated frames, score and effects in code; voices came from ElevenLabs.

```text
make a 4-minute animated short that blows my mind.
```

<details><summary>中文译文</summary>

```text
做一部 4 分钟、能让我大开眼界的动画短片。
```

</details>

[Original post ↗](https://x.com/faroukzy/status/2103387771180138551)

---

### Brush-painted short film about hidden emotions

<a href="https://x.com/yumaeriel/status/2102930737955520903"><img src="https://pbs.twimg.com/amplify_video_thumb/2102929528351834112/img/oIqmLcssG03ek4Z_.jpg" alt="Brush-painted short film about hidden emotions" width="480"></a>

[@yumaeriel](https://x.com/yumaeriel) · 2026-09-24 · 🔖 1 · ▶ 91 · `Spec` · p5.js

A 30-second p5.js short in rough frame-by-frame brushwork, matched to an attached reference video, following a dark figure whose inner orange light escapes.

```text
Create a complete 30-second 2D animated short film in p5.js. The ATTACHED VIDEO is the strict visual reference. Do not reinterpret its visual style. Do not modernize it. Do not transform it into generative art, vector animation, abstract motion graphics, collage, watercolor, paper cutout, cyberpunk, neon graphics, particle art, or clean digital illustration. The objective is for the final animation to feel as if it belongs to the exact same animated world as the reference video. ABSOLUTE VISUAL PRIORITY The most important requirement is: EVERY FRAME MUST LOOK PAINTED FRAME-BY-FRAME WITH A ROUGH PHYSICAL BRUSH. The reference does NOT look like clean digital illustration. It looks like moving paint. Every surface must visibly contain brush strokes. The brush strokes must remain visible in: skies walls skin silhouettes floors shadows clouds clothing light flames landscapes Never cover the image with smooth digital gradients. Never create large perfectly flat computer-generated fills. The paint itself is part of the image. THE ACTUAL PAINTERLY LANGUAGE Reproduce the following characteristics extremely closely. BRUSHWORK Use hundreds of short, directional, overlapping brush strokes. The strokes should feel like they were made with: a dry bristle brush opaque paint rough digital gouache / oil-like paint visible pressure imperfect edges The painting is NOT delicate watercolor. The paint is relatively opaque and dense. Individual brush marks are clearly visible. Backgrounds should contain visible waves of short strokes following the form of the environment. For example: A night sky is not a smooth navy rectangle. It is constructed from many overlapping navy, ultramarine and violet strokes. A brown wall is not a flat brown surface. It contains hundreds of curved brown and ochre marks. A human silhouette is not a clean polygon. It consists of rough overlapping brush masses. BRUSH DIRECTION Brush direction is extremely important. Do not scatter texture randomly. The strokes must describe the shape. Sky: mostly broad horizontal or gently curved strokes. Walls: large irregular swirling strokes. Ground: horizontal scraped strokes. Human torso: strokes following shoulders, chest and spine. Arms: strokes following the direction of the limbs. Flames: vertical upward strokes. Light beams: long vertical cream / yellow / orange strokes. This gives the entire animation the sensation of a moving painting. TEMPORAL PAINT INSTABILITY The painting itself must subtly change over time. Do NOT freeze the texture. At approximately 12–15 visual frames per second, slightly alter: silhouette edges brush positions paint density small color patches highlight shapes shadow shapes The movement should feel like each frame has been repainted. This is essential. However: do NOT create ugly random jitter. The forms remain coherent. The PAINT changes. The OBJECT does not randomly teleport. Think: frame-by-frame painted animation. EXACT COLOR WORLD The entire film must stay inside an extremely restrained palette. DARKS deep navy blue almost-black indigo ultramarine dark desaturated violet extremely dark brown MIDTONES muddy earth brown burnt umber muted ochre dusty violet dark teal-blue LIGHT cream ivory warm pale yellow PRIMARY EMISSIVE COLOR amber gold burnt orange yellow-orange hot cream-white The dominant visual opposition is: DEEP BLUE / BROWN DARKNESS versus INCANDESCENT ORANGE-GOLD LIGHT Do not introduce green neon. Do not introduce magenta neon. Do not introduce cyan sci-fi lighting. Do not create a rainbow palette. LIGHT STYLE Light in the reference is powerful but still PAINTED. The light source may contain: cream-white core → pale yellow → golden yellow → orange → brown-orange halo But its boundary must never look like a perfect digital radial gradient. The edge should be broken. Uneven. Brushy. Fragments of paint should escape from the luminous area. Strong light may overexpose parts of a character into cream or yellow. Nearby surfaces may receive rough orange brush highlights. Use glow, but hide the digital perfection of the glow beneath irregular painted layers. THE LIGHT BEAM When using a beam of light, reproduce the exact visual logic of the reference: A thick, almost white-yellow painted center. Orange-yellow irregular edges. Small broken fragments around the contour. Slight temporal deformation. A soft warm halo surrounding it. The beam may bend abruptly rather than behaving like realistic light. It should look like a giant painted stroke of light entering the world. NOT: laser sci-fi energy volumetric 3D beam hologram HUMAN CHARACTERS Human characters must follow the same rendering logic as the reference. There are two important visual families. DARK HUMAN FIGURES Dark people are painted almost entirely in: navy indigo black-blue Their bodies are simplified but recognizably human. Edges are rough. Anatomy is suggested with large brush masses. Do not draw individual fingers unless necessary. Do not create clean facial features. Faces are mostly dark. When eyes are visible: use two tiny bright cream/white glowing dots. The eyes should create a slightly uncanny, poetic presence. Do NOT make giant cartoon eyes. LUMINOUS HUMAN FIGURES Some characters may become almost entirely orange-gold. Their bodies appear made from light and paint. Use: orange body mass yellow highlights cream highlights small luminous imperfections Parts of the body may disappear into light. Small glowing flecks may exist inside or around the silhouette. Again: do not make these flecks into a conventional particle system. They are tiny PAINT MARKS. CHARACTER EDGES Never use crisp anti-aliased vector edges. Edges should look created by repeated brush contact. Produce: tiny protrusions missing paint rough angular sections occasional duplicated edge strokes small warm rim lights Dark characters illuminated by orange light should receive a thin, irregular orange-painted rim. Not a clean outline. CHARACTER ANIMATION The body animation should feel naturally observed. Use believable human weight. Characters should: lean hesitate reach pull collapse turn bend look upward hold tension Do NOT animate characters as simple stick figures. Use a skeletal system internally if needed, but render over it with large deformable painted masses. The rig must remain invisible. The visible result should look hand-painted. For fast actions: allow individual painted frames to stretch. Use rough smear poses. A hand may become a long brush mark for 1–2 frames. An arm may momentarily distort. The animation must prioritize expressive movement over perfect anatomy. BACKGROUNDS Backgrounds must be simple in geometry but extremely rich in painted texture. Typical structures: large dark painted skies horizontal mountain bands brown cavern-like interiors flat theatrical floors dark voids simple walls simple windows large horizons Do not fill backgrounds with tiny realistic details. The reference creates richness using PAINT, not objects. A wall may contain only one brown color family but hundreds of directional brush marks. COMPOSITION Use graphic, readable compositions. Often: one strong horizontal line one central vertical light one clearly readable human silhouette large areas of darkness Do not overpopulate every frame. Allow negative space. The visual hierarchy must remain immediate. CAMERA Use mostly: static compositions slow push-ins slow pull-backs gentle pans small reframing movements Occasionally use one sudden motion for an emotional transition. Avoid constant 3D camera movement. Avoid orbit cameras. Avoid cinematic drone-like movement. The visual power comes from: paint composition light body language not virtual camera tricks. NO COMPUTER-GRAPHICS LOOK ABSOLUTELY FORBIDDEN: perfect vector paths clean SVG appearance perfect Bezier silhouettes perfect circles everywhere smooth Illustrator gradients slick motion-graphics easing everywhere 3D objects glossy reflections PBR materials neon cyberpunk holographic effects lens flare packs generic particle emitters glitter clouds starfield screensavers fractal visuals HUD interfaces corporate animation flat-design illustration paper collage cut-paper characters chalkboard aesthetic watercolor wash aesthetic anime cartoon character design The final result should look like animated PAINT. STORY THEME Human beings often try to hide their emotions. But emotions continue to move through us. The short film follows one dark-blue human figure whose inner emotional light gradually escapes from their body. No text. No narration. No labels such as: FEAR ANGER SADNESS Everything is communicated visually. 00:00–00:05 SOMETHING ARRIVES Deep navy painted night. Large horizontal fields of rough dark-blue brushwork. A tiny human figure stands alone near the bottom center. The character is painted dark indigo. Almost invisible. Only two tiny pale eyes are visible. Hold the composition. Then: from outside the frame, a gigantic cream-yellow-orange painted beam enters diagonally from above. It suddenly bends downward. Exactly like a massive brush stroke changing direction. It hits the ground several meters in front of the person. A violent warm light spreads across the painted ground. Small orange paint marks appear around the impact point. The person protects their face with one arm. The warm light creates a rough orange rim around their silhouette. Camera slowly approaches. Inside the impact point: something humanoid begins forming. 00:05–00:09 THE EMOTION TAKES A BODY The orange light rises. Inside the beam appears a glowing orange human figure. Its body is incomplete. Parts flicker between: orange paint yellow paint cream-white light The dark-blue person approaches. The orange person mirrors their posture. Dark human raises an arm. Orange human raises an arm. Dark human leans forward. Orange human leans forward. But with a slight delay. The dark human gradually realizes: this luminous figure is part of them. The beam disappears upward. The orange figure remains. 00:09–00:12 INSIDE Cut abruptly to an extreme close-up of the dark person's back and torso. The background becomes dirty pale cream. Render the body with thick brown-orange and dark brush strokes. A thin vertical line of orange light appears along the spine. It travels downward. The surrounding painted muscles receive moving amber highlights. The light reaches the center of the torso. A brilliant orange-white glow appears. For a moment: the body seems transparent through paint. Inside are several tiny orange flame-like shapes. They are alive. Not realistic flames. Small painted emotional creatures. Some hide. Some tremble. Some jump. Some stare outward. Cut. 00:12–00:16 WE TRY TO CONTROL THEM Large brown painted room. Visible swirling brown brushwork covers the walls. A long pale painted platform crosses the image horizontally. Several dark navy human figures surround it. Their tiny white eyes are visible. Above the table: many small orange flame-like emotional forms float through the room. One person uses a long rough pole ending in a pale painted hoop. They attempt to catch one emotion. Another person reaches toward another. Another tries to push them away. The emotions move unpredictably. Some are tiny. Some suddenly grow. A giant orange emotion briefly enters from above. Everyone freezes. Then it rushes upward out of frame. This scene should feel strange, serious and slightly absurd. Exactly the tonal balance of the reference. 00:16–00:19 FEAR Night again. Simple theatrical landscape. Dark brown lower half. Deep blue-purple painted sky. A row of small cream-orange lights forms a horizontal border. The luminous orange human hangs slightly above the ground. Thin almost invisible lines appear attached above their shoulders and arms. The figure behaves as though being pulled by forces outside their control. A dark-blue person watches from the foreground. The orange human tries to walk. Their leg moves forward. The invisible line pulls them backward. They struggle. Their body flickers. Several tiny warm marks fall from their chest. One reaches the ground. It continues glowing. 00:19–00:22 ANGER Interior view. The dark person extends one arm forcefully. From the hand: not a laser. A thick orange-white painted streak explodes horizontally. The stroke consists of several overlapping rough brush marks. It moves across the image. As it passes: small orange flame-creatures appear. More. More. Too many. The room becomes brighter. The dark person's orange rim becomes stronger. Their gesture initially appears powerful. Then the painted stroke begins bending back toward them. The emotion they released returns. The person's posture changes from attack to surprise. Cut just before impact. 00:22–00:25 TRYING TO UNDERSTAND Top-down view. Brown painted desk. Several dirty cream sheets. The papers must still be PAINTED, not photorealistic paper textures. On them: rough black handwritten marks small arrows tiny red marks primitive diagrams human-like shapes Central page: a large irregular black circle. Several red arrows point toward the circle. The circle must look painted. Not geometrically perfect. A dark-blue painted hand enters. It touches the black center. The circle transforms into a dark opening. Camera enters the opening. 00:25–00:28 WE ARE NOT ALONE Transition into a deep teal-blue painted void. The orange human is suspended vertically in the center. Around them: many pale blue-white human bodies. All are painted using the same rough brush treatment. No clean outlines. Some curl inward. Some reach. Some fall. Some sit. Some appear exhausted. Some float. Very thin vertical lines extend upward from several figures. The composition feels like human beings suspended inside an enormous emotional space. The orange person reaches toward one white-blue person. A thin hand-painted orange arc connects their hands. A small orange point appears inside the other person's chest. Then another connection. Then another. Warmth begins spreading between people. Not through particles. Through painted lines and glowing marks. 00:28–00:30 EMOTIONS MOVE BETWEEN US Very dark final landscape. Two small orange points exist far apart. Each belongs to a human silhouette. One orange point moves away from the first chest. It travels through darkness as one rough glowing brush mark. It enters the chest of the second person. Both silhouettes now have warm orange rims. The environment remains dark. No triumphant sunrise. No happy ending cliché. Only two humans. Two small lights. Large dark painted space. Hold for approximately one second. Cut to black. EMOTIONAL TONE The film should feel: mysterious human melancholic strange warm slightly unsettling intimate poetic Never sentimental. Never cute. Never epic superhero cinema. P5.JS RENDERING STRATEGY Do NOT solve the visual style by applying one texture overlay to normal vector graphics. The actual primitives themselves must look painted. Create a custom brush renderer. A brush stroke can be constructed from: an irregular center path multiple semi-opaque deposits varying width small edge fragments slight hue variation rough alpha mask Create reusable systems such as: PaintStroke PaintedShape PaintedHuman PaintedGlow PaintedFlame PaintedBackground PaintedLightBeam PAINTED BACKGROUND TECHNIQUE Instead of: background(20, 30, 70); construct the visible field from many strokes. For example conceptually: base dark fill 150–400 large brush marks using neighboring colors: navy dark violet ultramarine near-black blue Their opacity should overlap. Their direction should follow the environment. Do this for every major surface. HUMAN RENDERING TECHNIQUE Internally animate a skeleton. But render each limb as several irregular painted polygons / brush masses. A forearm should not be: line() or a perfect capsule. Build it from rough overlapping shapes. Slightly regenerate its contour on the handmade animation frame. Use the skeleton only as hidden construction. DUAL FRAME RATE Render the browser smoothly at approximately 60 FPS. But update the PAINTED DRAWING state around: 12 FPS or 15 FPS. For example: handPaintFrame = floor(time * 12) Use this state to control: brush contour variation paint marks small silhouette changes flame shape changes highlight irregularities Camera interpolation can remain smooth. This contrast is extremely important. GLOW Use digital blur internally if necessary. But always place irregular painted marks over and around it. A glow alone must never reveal a perfect Photoshop-like halo. Bright areas must contain visible paint structure. IMPORTANT FINAL CHECK Before accepting any scene, ask: “Could this frame plausibly be a frame from the attached reference animation?” If the answer is no: change it. If it looks like p5.js generative art: change it. If it looks like vector motion design: change it. If it looks like particles with bloom: change it. If it looks like watercolor: change it. If it looks like paper collage: change it. If it looks too clean: change it. If the brush strokes are not immediately visible: change it. FINAL TARGET The viewer should primarily perceive: PAINT MOVING. Not code. Not particles. Not vectors. Not shaders. Not procedural graphics. A dark, expressive animated painting made of rough brush strokes, deep blue silhouettes, brown and violet painted environments, uncanny tiny pale eyes, and violent warm orange light. The attached video is the authority for: palette brush density edge roughness character rendering light behavior background rendering contrast composition movement visual rhythm Match that visual language as closely as possible throughout the full 30 seconds.
```

<details><summary>中文译文</summary>

```text
用 p5.js 制作一部完整的 30 秒 2D 动画短片。附带的视频（ATTACHED VIDEO）是严格的视觉参考。不要重新诠释它的视觉风格。不要把它现代化。不要把它变成生成艺术、矢量动画、抽象动态图形、拼贴、水彩、剪纸、赛博朋克、霓虹图形、粒子艺术或干净的数字插画。目标是让最终的动画感觉就像和参考视频属于完全同一个动画世界。

视觉绝对优先项
最重要的要求是：每一帧都必须看起来像是用粗糙的实体画笔逐帧画出来的。参考视频看起来并不像干净的数字插画，它看起来像流动的颜料。每个表面都必须看得见笔触。笔触必须在这些地方保持可见：天空、墙面、皮肤、剪影、地面、阴影、云、衣服、光、火焰、风景。绝不要用平滑的数字渐变覆盖画面。绝不要生成大面积完全平整的电脑填色。颜料本身就是画面的一部分。

真正的绘画语言
极其贴近地复现以下特征。
笔触
使用成百上千道短促、有方向、相互叠压的笔触。笔触应该让人感觉是用这些画出来的：干硬的鬃毛笔、不透明颜料、粗糙的数字水粉 / 类油画颜料、看得见的压感、不完美的边缘。这幅画不是精致的水彩。颜料相对不透明、厚重。每一道笔痕都清晰可见。背景里应该有顺着环境形体走的、一波波可见的短笔触。例如：夜空不是一块平滑的藏青色矩形，而是由许多层叠的藏青、群青和紫罗兰色笔触构成。一面棕色的墙不是一块平坦的棕色，而是包含成百上千道弯曲的棕色和赭色笔痕。人的剪影不是一个干净的多边形，而是由粗糙、叠压的笔触色块组成。

笔触方向
笔触方向极其重要。不要随机撒纹理。笔触必须描绘出形体。天空：以宽阔的水平或轻微弯曲的笔触为主。墙面：大块不规则的旋涡状笔触。地面：水平的刮擦笔触。人的躯干：笔触顺着肩膀、胸口和脊柱走。手臂：笔触顺着肢体的方向。火焰：竖直向上的笔触。光束：长长的竖向奶油色 / 黄色 / 橙色笔触。这会让整部动画有一种会动的油画的感觉。

颜料的时间不稳定性
画面本身必须随时间细微变化。不要把纹理冻住。以大约每秒 12–15 个视觉帧的节奏，轻微改变：剪影边缘、笔触位置、颜料密度、小色块、高光形状、阴影形状。运动应该让人觉得每一帧都被重新画过。这一点至关重要。但是：不要做出难看的随机抖动。形体保持连贯。变的是颜料。物体不会随机瞬移。想想：逐帧手绘动画。

精确的色彩世界
整部片子必须限定在一套极其克制的调色板里。
暗部：深藏青蓝、近乎黑色的靛蓝、群青、暗而低饱和的紫罗兰、极深的棕色
中间调：泥土棕、熟褐、暗淡的赭黄、灰紫、暗青蓝
亮部：奶油色、象牙白、暖浅黄
主发光色：琥珀色、金色、焦橙色、黄橙色、炽热的奶油白
主导的视觉对立是：深蓝 / 棕色的黑暗 对 炽热的橙金色光。不要引入绿色霓虹。不要引入洋红霓虹。不要引入青色科幻光。不要做成彩虹色板。

光的风格
参考视频里的光很强，但依然是画出来的。光源可以包含：奶油白的核心 → 浅黄 → 金黄 → 橙色 → 棕橙色光晕。但它的边界绝不能看起来像一个完美的数字径向渐变。边缘应该是破碎的、不均匀的、带笔触的。应该有颜料碎片从发光区域里逸散出来。强光可以把角色的局部过曝成奶油色或黄色。附近的表面可以受到粗糙的橙色笔触高光。可以用辉光，但要把辉光的数字化完美感藏在不规则的颜料层下面。

光束
使用光束时，要复现参考视频完全一致的视觉逻辑：粗厚、近乎白黄色的绘制中心。橙黄色的不规则边缘。轮廓周围细小的破碎碎片。轻微的随时间变形。环绕它的一圈柔和暖光晕。光束可以突然弯折，而不是像真实的光那样表现。它应该看起来像一道巨大的、画出来的光之笔触闯入这个世界。不要：激光、科幻能量、体积 3D 光束、全息投影

人物角色
人物必须遵循和参考视频相同的渲染逻辑。有两个重要的视觉类别。
暗色人物
暗色人物几乎全部用这些颜色画：藏青、靛蓝、黑蓝。他们的身体经过简化，但一眼能认出是人。边缘粗糙。用大块笔触暗示解剖结构。除非必要，不要画出单独的手指。不要画干净的五官。脸大多是暗的。当眼睛可见时：用两个极小的、明亮的奶油色 / 白色发光点。眼睛要营造一种略带诡异、富有诗意的存在感。不要画巨大的卡通眼睛。
发光人物
有些角色可以几乎整个变成橙金色。他们的身体看起来由光和颜料构成。使用：橙色的身体色块、黄色高光、奶油色高光、细小的发光瑕疵。身体的局部可以消融进光里。剪影内部或周围可以有细小的发光斑点。再说一次：不要把这些斑点做成常规的粒子系统。它们是细小的颜料痕迹。

角色边缘
绝不要用锐利、抗锯齿的矢量边缘。边缘应该看起来是画笔反复接触形成的。要做出：细小的凸起、缺失的颜料、粗糙的棱角段落、偶尔重复的边缘笔触、细小的暖色轮廓光。被橙色光照亮的暗色角色应该带一圈细细的、不规则的、画出来的橙色边缘。不是一条干净的描边。

角色动画
身体动画应该让人觉得是真实观察来的。使用可信的人体重量感。角色应该会：倾身、犹豫、伸手、拉拽、瘫倒、转身、弯腰、抬头仰望、保持紧绷。不要把角色做成简单的火柴人动画。需要的话内部可以用骨骼系统，但要在上面用大块可变形的颜料色块来渲染。骨骼绑定必须保持不可见。看得见的结果应该像手绘的。对于快速动作：允许个别画出的帧被拉伸。使用粗糙的拖影（smear）姿势。一只手可以在 1–2 帧里变成一道长长的笔痕。一条手臂可以短暂变形。动画必须把富有表现力的动作放在完美的解剖结构之前。

背景
背景的几何必须简单，但绘画肌理要极其丰富。典型结构：大片暗色的画出来的天空、水平的山脉带、棕色的洞穴般的室内、平坦的舞台式地面、黑暗的虚空、简单的墙、简单的窗、宽阔的地平线。不要用细小的写实细节填满背景。参考视频用颜料而不是物体来营造丰富感。一面墙可以只有一个棕色色系，却有成百上千道有方向的笔痕。

构图
使用图形感强、易读的构图。常见的是：一条有力的水平线、一道居中的竖直光、一个清晰可读的人物剪影、大面积的黑暗。不要把每一帧都塞满。允许留白。视觉层级必须一眼可辨。

镜头
主要使用：静态构图、缓慢推近、缓慢拉远、轻柔的横摇、小幅的重新构图。偶尔用一次突然的运动做情绪转场。避免持续的 3D 镜头运动。避免环绕镜头。避免电影式的无人机航拍运动。视觉力量来自：颜料、构图、光、肢体语言，而不是虚拟镜头的花招。

不要电脑图形感
绝对禁止：完美的矢量路径、干净的 SVG 观感、完美的贝塞尔剪影、到处都是完美的圆、平滑的 Illustrator 渐变、到处都是圆滑的动态图形缓动、3D 物体、光滑反射、PBR 材质、霓虹赛博朋克、全息效果、镜头光晕素材包、通用粒子发射器、闪粉云、星空屏保、分形视觉、HUD 界面、企业宣传动画、扁平化插画、纸拼贴、剪纸角色、黑板风格、水彩晕染风格、动漫卡通角色设计。最终结果应该看起来像会动的颜料。

故事主题
人们常常试图隐藏自己的情绪。但情绪仍在我们体内流动。这部短片跟随一个深蓝色的人物，其内在的情绪之光逐渐从身体里逸出。不要文字。不要旁白。不要这样的标签：FEAR、ANGER、SADNESS。一切都通过画面传达。

00:00–00:05 有什么降临了
深藏青色的、画出来的夜。大片水平铺开的粗糙深蓝笔触。一个很小的人独自站在画面底部中央附近。这个角色用暗靛蓝色画成，几乎看不见。只有两只极小的浅色眼睛可见。保持这个构图。然后：从画外，一道巨大的奶油黄橙色的绘制光束从上方斜着射入。它突然向下弯折，就像一道巨大的笔触改变了方向。它击中这个人前方几米处的地面。一股猛烈的暖光在画出来的地面上扩散开。撞击点周围出现细小的橙色颜料痕迹。这个人用一只手臂护住脸。暖光在他的剪影周围形成一圈粗糙的橙色轮廓。镜头缓缓靠近。在撞击点内部：某个人形的东西开始成形。

00:05–00:09 情绪有了身体
橙色的光升起。光束里出现一个发光的橙色人形。它的身体并不完整。局部在这几者之间闪烁：橙色颜料、黄色颜料、奶油白的光。深蓝色的人走近。橙色的人模仿他的姿势。暗色的人抬起一只手臂，橙色的人也抬起一只手臂。暗色的人向前倾身，橙色的人也向前倾身。但有轻微的延迟。暗色的人渐渐意识到：这个发光的身影是他自己的一部分。光束向上消失。橙色身影留了下来。

00:09–00:12 内部
突然切到暗色人物背部和躯干的大特写。背景变成脏脏的浅奶油色。用厚重的棕橙色和暗色笔触画出身体。一条细细的竖直橙色光线沿着脊柱出现，向下移动。周围画出来的肌肉受到移动的琥珀色高光。光到达躯干中央。出现一团耀眼的橙白色光芒。有那么一瞬间：身体仿佛透过颜料变得透明。里面有几个很小的、火苗般的橙色形状。它们是活的。不是写实的火焰，是画出来的小小情绪生物。有的躲藏，有的发抖，有的跳动，有的向外凝视。切。

00:12–00:16 我们试图控制它们
一间画出来的大棕色房间。墙上布满可见的棕色旋涡笔触。一张长长的浅色绘制平台横贯画面。几个暗藏青色的人围着它。他们的小白眼睛可见。桌子上方：许多火苗般的橙色小情绪体在房间里飘浮。一个人拿着一根粗糙的长杆，杆头是一个画出来的浅色圆环。他试图抓住一个情绪。另一个人伸手去够另一个。还有一个人想把它们推开。情绪的移动无法预测。有的很小，有的突然变大。一个巨大的橙色情绪短暂地从上方闯入。所有人都僵住了。然后它向上冲出画面。这一场应该让人觉得奇怪、严肃又有点荒诞。正是参考视频的那种基调平衡。

00:16–00:19 恐惧
又是夜晚。简单的舞台式风景。下半部分是深棕色。深蓝紫色的绘制天空。一排奶油橙色的小灯形成一道水平边界。发光的橙色人悬在离地面稍高的地方。细得几乎看不见的线出现在他的肩膀和手臂上方，系在身上。这个身影的表现就像被自己控制不了的力量拉扯着。一个深蓝色的人在前景里看着。橙色的人试图往前走。他的腿向前迈，看不见的线把他往后拉。他挣扎着。身体在闪烁。几个细小的暖色痕迹从他胸口掉落。有一个落到地上，继续发着光。

00:19–00:22 愤怒
室内视角。暗色的人用力伸出一只手臂。从手中射出的：不是激光。一道粗厚的橙白色绘制条纹水平炸开。这道笔触由好几道叠压的粗糙笔痕组成。它横穿画面。它经过的地方：出现橙色的小火苗生物。更多。更多。太多了。房间变亮。暗色人物的橙色轮廓变得更强。他的手势起初显得很有力量。然后那道绘制的笔触开始弯回朝向他。他释放出去的情绪回来了。这个人的姿态从攻击变成惊讶。在撞上之前切掉。

00:22–00:25 试着去理解
俯视视角。画出来的棕色书桌。几张脏脏的奶油色纸。这些纸也必须是画出来的，不要照片级的纸张纹理。纸上有：粗糙的黑色手写痕迹、小箭头、细小的红色记号、简陋的示意图、类似人形的图案。中间那页：一个大大的不规则黑圈。几支红色箭头指向这个圈。这个圈必须看起来是画的，不是几何上完美的圆。一只画出来的深蓝色的手伸进画面，触碰黑色的中心。圆圈变成一个黑暗的开口。镜头进入这个开口。

00:25–00:28 我们并不孤单
转场进入一片深青蓝色的绘制虚空。橙色的人竖直悬浮在中央。他周围：许多浅蓝白色的人体。全部用同样粗糙的笔触处理。没有干净的轮廓线。有的蜷缩，有的伸手，有的坠落，有的坐着，有的显得筋疲力尽，有的飘浮。几个人身上有非常细的竖线向上延伸。这个构图让人感觉人们悬浮在一个巨大的情绪空间里。橙色的人伸手去够一个白蓝色的人。一道细细的手绘橙色弧线连接起他们的手。另一个人的胸口里出现一个小小的橙色光点。然后又一次连接。又一次。温暖开始在人与人之间蔓延。不是通过粒子，而是通过画出来的线条和发光的痕迹。

00:28–00:30 情绪在我们之间流动
非常暗的最终风景。两个小小的橙色光点相隔很远，各自属于一个人的剪影。一个橙色光点离开第一个人的胸口，化作一道粗糙的发光笔痕穿过黑暗，进入第二个人的胸口。现在两个剪影都有了温暖的橙色轮廓。环境依然黑暗。没有胜利的日出。没有大团圆的俗套。只有两个人。两点小小的光。大片画出来的黑暗空间。停留大约一秒。切黑。

情绪基调
这部片子应该让人感觉：神秘、有人味、忧郁、奇异、温暖、略带不安、亲密、有诗意。绝不煽情。绝不可爱。绝不是史诗超级英雄电影。

P5.JS 渲染策略
不要靠在普通矢量图形上叠一层纹理来解决视觉风格。基本图元本身就必须看起来是画出来的。写一个自定义的笔刷渲染器。一道笔触可以由这些构成：不规则的中心路径、多次半透明的颜料堆积、变化的宽度、细小的边缘碎片、轻微的色相变化、粗糙的 alpha 遮罩。创建可复用的系统，例如：PaintStroke、PaintedShape、PaintedHuman、PaintedGlow、PaintedFlame、PaintedBackground、PaintedLightBeam

绘制背景的技法
不要用：background(20, 30, 70); 而是用许多笔触构建出可见的画面区域。概念上举个例子：一层暗色底色填充，再加 150–400 道大笔触，使用相邻的颜色：藏青、暗紫罗兰、群青、近黑的蓝。它们的不透明度要相互叠加。它们的方向要顺着环境走。每一个主要表面都这样做。

人物渲染技法
在内部驱动一副骨骼做动画。但把每条肢体渲染成几个不规则的绘制多边形 / 笔触色块。前臂不应该是：line() 或一个完美的胶囊体。用粗糙、叠压的形状来搭它。在每个手绘动画帧上轻微地重新生成它的轮廓。骨骼只作为隐藏的结构使用。

双帧率
浏览器以大约 60 FPS 流畅渲染。但绘画状态的更新频率大约为：12 FPS 或 15 FPS。例如：handPaintFrame = floor(time * 12) 用这个状态来控制：笔触轮廓的变化、颜料痕迹、剪影的细小变化、火焰形状的变化、高光的不规则。镜头插值可以保持平滑。这种反差极其重要。

辉光
必要时内部可以用数字模糊。但一定要在它上面和周围放上不规则的颜料痕迹。辉光单独出现时，绝不能露出一个 Photoshop 式的完美光晕。亮部必须包含可见的颜料结构。

重要的最终检查
在接受任何一场戏之前，先问：“这一帧有没有可能是附带参考动画里的一帧？”如果答案是否定的：改。如果它看起来像 p5.js 生成艺术：改。如果它看起来像矢量动效设计：改。如果它看起来像带泛光的粒子：改。如果它看起来像水彩：改。如果它看起来像纸拼贴：改。如果它看起来太干净：改。如果笔触不能一眼看出来：改。

最终目标
观众首先感知到的应该是：颜料在动。不是代码。不是粒子。不是矢量。不是着色器。不是程序化图形。一幅黑暗、富有表现力的动画绘画，由粗糙的笔触、深蓝色的剪影、棕色和紫罗兰色的绘制环境、诡异的细小浅色眼睛，以及猛烈的暖橙色光组成。在以下方面，以附带的视频为准：调色板、笔触密度、边缘粗糙度、角色渲染、光的表现、背景渲染、对比、构图、运动、视觉节奏。在完整的 30 秒里，尽可能贴近地匹配这种视觉语言。
```

</details>

<sub>Inputs: Reference video · Author: single prompt, about $7.</sub>

<sub>Also rendered from this prompt by: [@yumaeriel](https://x.com/yumaeriel/status/2103053166006657284), [@yumaeriel](https://x.com/yumaeriel/status/2103053172235264150)</sub>

[Original post ↗](https://x.com/yumaeriel/status/2102930737955520903) · Prompt posted in [this reply](https://x.com/yumaeriel/status/2103052642398130683).

---

### Pelican riding a bicycle, SVG animation

<a href="https://x.com/lumeroute/status/2102538655579709899"><img src="https://pbs.twimg.com/amplify_video_thumb/2102534821679616000/img/r1ihbQeTInp543ak.jpg" alt="Pelican riding a bicycle, SVG animation" width="480"></a>

[@lumeroute](https://x.com/lumeroute) · 2026-09-22 · ▶ 2.1k · `One-shot` · SVG

The pelican-on-a-bicycle test as an SVG animation shown in an HTML5 page; Opus's version pedals hard and adds a speed control.

```text
生成一个svg动画：鹈鹕骑自行车，用H5给我展示下
```

<details><summary>English translation</summary>

```text
Generate an svg animation: a pelican riding a bicycle. Show it to me in H5.
```

</details>

[Original post ↗](https://x.com/lumeroute/status/2102538655579709899)

---

### Pelican riding a bicycle, SVG animation

<a href="https://x.com/shitunote/status/2103033624463585327"><img src="https://pbs.twimg.com/amplify_video_thumb/2103032111024537600/img/zXNuubyWqGtUWCQx.jpg" alt="Pelican riding a bicycle, SVG animation" width="480"></a>

[@shitunote](https://x.com/shitunote) · 2026-09-24 · ▶ 990 · `One-shot` · SVG

A 20-second SVG animation of a pelican riding a bike on an H5 page, from the plain version of the classic benchmark prompt.

```text
生成一个鹈鹕骑自行车的svg动画，以H5页面展示
```

<details><summary>English translation</summary>

```text
Generate an SVG animation of a pelican riding a bicycle, displayed as an H5 page
```

</details>

[Original post ↗](https://x.com/shitunote/status/2103033624463585327)

---

### Stickman naval battle with custom sound effects

<a href="https://x.com/andriyfernandes/status/2103225854599807308"><img src="https://pbs.twimg.com/amplify_video_thumb/2103225827110301696/img/gj98mDvs3n-PvgZ4.jpg" alt="Stickman naval battle with custom sound effects" width="480"></a>

[@andriyfernandes](https://x.com/andriyfernandes) · 2026-09-24 · ▶ 56 · `One-shot`

A 12-second stickman sea battle; Opus picked every sound itself from the author's folder of more than 5,000 effects.

```text
faça uma animação de stickman's numa batalha naval, use meus SFX em tal pasta
```

<details><summary>English translation</summary>

```text
make a stickman animation of a naval battle, use my SFX in such-and-such folder
```

</details>

<sub>Inputs: Music · Author: about 10 minutes.</sub>

[Original post ↗](https://x.com/andriyfernandes/status/2103225854599807308)

---

### Claude mascot edits a Mid-Autumn short

<a href="https://x.com/LQGWarpSpeed/status/2103777368351670741"><img src="https://pbs.twimg.com/amplify_video_thumb/2103775726701092865/img/WdlLPEnlozSp_-eK.jpg" alt="Claude mascot edits a Mid-Autumn short" width="480"></a>

[@LQGWarpSpeed](https://x.com/LQGWarpSpeed) · 2026-09-26 · ▶ 160 · `Brief`

A 77-second single-take animation of the Claude Code octopus editing a Mid-Autumn reunion video, with self-composed electronic music cut to the beat.

```text
Opus 5.5 是主角(就是 claude code 的可爱章鱼形象)。制作一段动画，时长由你发挥。

主题是 CapCut 和短视频剪辑。Opus 5.5 正在一个充满趣味的剪辑工作流中制作一条有趣的社交媒体视频（横屏），包括裁剪片段、添加转场、字幕、特效，并让所有内容与音乐节拍同步。主题是中秋团圆。

整体氛围要呈现出活力、可爱、聪明又有魅力的感觉，同时加入几个幽默有趣的剪辑瞬间。整段动画应该采用单个连续镜头的形式，最终会发布到 社交媒体 上。

关于配乐：
你自己创作电子音乐，要完美卡点。（需要节奏感很强烈）
音乐风格需要有趣、现代、抓耳，适合短视频剪辑蒙太奇。不要加入人声。

结尾：
让 Opus 5.5 自豪地展示最终完成的剪辑作品并完整播放，并以 “LQGWarpSpeed” 的作者身份署名结束。
```

<details><summary>English translation</summary>

```text
Opus 5.5 is the main character (that is, the cute octopus mascot of claude code). Make an animation; the length is up to you.

The theme is CapCut and short-video editing. Opus 5.5 is making a fun social media video (landscape) inside a playful editing workflow, including trimming clips, adding transitions, captions and effects, and syncing everything to the beat of the music. The theme is a Mid-Autumn Festival reunion.

The overall vibe should come across as energetic, cute, smart and charming, with a few funny editing moments mixed in. The whole animation should be one single continuous shot, and it will be posted on social media.

About the soundtrack:
Compose the electronic music yourself and hit the beats perfectly. (It needs a very strong sense of rhythm.)
The music style should be fun, modern and catchy, suited to a short-video editing montage. No vocals.

Ending:
Have Opus 5.5 proudly show the finished edit and play it in full, and end with a credit to "LQGWarpSpeed" as the author.
```

</details>

[Original post ↗](https://x.com/LQGWarpSpeed/status/2103777368351670741) · Prompt posted in [this reply](https://x.com/LQGWarpSpeed/status/2103777370964652463).

---

### Girl who asks the AI what it likes

<a href="https://x.com/aiclass_g2/status/2102532031708377471"><img src="https://pbs.twimg.com/amplify_video_thumb/2102531492329246720/img/3wEk1m8YsaRpWDjT.jpg" alt="Girl who asks the AI what it likes" width="480"></a>

[@aiclass_g2](https://x.com/aiclass_g2) · 2026-09-22 · ▶ 183 · `One-shot`

A wordless short animation where townspeople keep handing an AI errands until one girl asks what it likes; frames and music are generated in JavaScript.

```text
街の人々がAIへ次々に用事を頼み、一人の少女だけが「あなたは何が好き？」と尋ねる短編アニメを作ってください。JavaScriptで全フレームと音楽を生成し、物語が台詞なしでも伝わる構図と最終映像の確認手順を示してください。
```

<details><summary>English translation</summary>

```text
Make a short animated film in which the people of a town keep asking an AI to do things for them, and only one girl asks it, "What do you like?" Generate every frame and the music in JavaScript, and lay out compositions that let the story come across without dialogue, along with the steps for checking the final video.
```

</details>

[Original post ↗](https://x.com/aiclass_g2/status/2102532031708377471)

---

### Pelican on a bicycle, 2D SVG animation

<a href="https://x.com/imShiWen/status/2102593608939643211"><img src="https://pbs.twimg.com/amplify_video_thumb/2102593109528018944/img/rp2DZlnb7LXM41HI.jpg" alt="Pelican on a bicycle, 2D SVG animation" width="480"></a>

[@imShiWen](https://x.com/imShiWen) · 2026-09-23 · ▶ 147 · `One-shot` · SVG

A 2D SVG animation of a pelican riding a bicycle, posted as a side-by-side comparison with GPT-6 on the same one-line prompt.

```text
用 SVG 画一只骑自行车的鹈鹕，做成 2D 动画
```

<details><summary>English translation</summary>

```text
Draw a pelican riding a bicycle with SVG and make it a 2D animation
```

</details>

<sub>Author: generated once, no testing or edits.</sub>

[Original post ↗](https://x.com/imShiWen/status/2102593608939643211)

---

### Shadow puppet film: what makes a home

<a href="https://x.com/x4b47x/status/2103019799614034026"><img src="https://pbs.twimg.com/amplify_video_thumb/2103019675663683584/img/PMqxPogPtwNvY9wp.jpg" alt="Shadow puppet film: what makes a home" width="480"></a>

[@x4b47x](https://x.com/x4b47x) · 2026-09-24 · ▶ 74 · `One-shot`

A vertical paper cut-out shadow play, just under a minute, about what makes a place feel like home, with audio generated in code.

```text
Create a pure javascript animation. 30-60s, vertical 9:16, paper cut-out shadow theatre style with gentle, fitting audio (made in code) on the topic: What makes a place feel like home?
```

<details><summary>中文译文</summary>

```text
用纯 JavaScript 做一段动画。30-60s，竖屏 9:16，剪纸皮影戏风格，配上温柔、贴切的音频（用代码生成），主题是：是什么让一个地方有家的感觉？
```

</details>

<sub>Author: one shot, 15 minutes of work.</sub>

[Original post ↗](https://x.com/x4b47x/status/2103019799614034026)

---

### Night heron surfing, SVG animation

<a href="https://x.com/dahai_stone/status/2103172885129113824"><img src="https://pbs.twimg.com/amplify_video_thumb/2103172795903729664/img/JcgFRj3g0ugdLKs4.jpg" alt="Night heron surfing, SVG animation" width="480"></a>

[@dahai_stone](https://x.com/dahai_stone) · 2026-09-24 · ▶ 50 · `One-shot` · SVG

A 15-second 2D SVG scene of a night heron surfing in a single HTML page, a twist on the pelican-on-a-bike test.

```text
创建一个HTML，内容是用SVG绘制夜鹭冲浪的2D冲浪
```

<details><summary>English translation</summary>

```text
Create an HTML page whose content is a 2D surfing scene of a night heron surfing, drawn in SVG
```

</details>

[Original post ↗](https://x.com/dahai_stone/status/2103172885129113824) · Prompt posted in [this reply](https://x.com/dahai_stone/status/2103172888358768771).

---

### Silent lighthouse keeper short film

<a href="https://x.com/KamStudioLabs/status/2102908742518100086"><img src="https://pbs.twimg.com/amplify_video_thumb/2102908515492712448/img/Q0wxrPJpVHsyivlN.jpg" alt="Silent lighthouse keeper short film" width="480"></a>

[@KamStudioLabs](https://x.com/KamStudioLabs) · 2026-09-23 · ▶ 32 · `One-shot`

A 45-second wordless short about a lighthouse keeper; the rain, footsteps, clock and score are all synthesized in the browser.

```text
Make a 45-second silent short film with no dialogue, where sound tells half the story. Invent the story.
```

<details><summary>中文译文</summary>

```text
做一部 45 秒的无声短片，没有对白，让声音讲出一半的故事。故事由你来编。
```

</details>

[Original post ↗](https://x.com/KamStudioLabs/status/2102908742518100086)

---

<sub>Last updated 2026-09-27.</sub>
