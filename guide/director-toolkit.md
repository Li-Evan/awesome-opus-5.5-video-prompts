# Director's Toolkit

[← Back to the list](../README.md) · **English** · [简体中文](../zh-CN/guide/director-toolkit.md)

## Quick Start

Opus 5.5 does not output video. It writes code that draws every frame (HTML Canvas, SVG, Three.js, Remotion, HyperFrames, Manim), renders the frames in a headless browser and stitches them into an MP4 with ffmpeg. That is why it is great at motion graphics, explainers and launch films, and why a change is a one-line edit and a re-render instead of a new roll of the dice.

1. Open Claude Code (or the Claude app) with Opus 5.5 and set effort to high or max.
2. Give it a renderer so it can produce a real MP4: `npx skills add heygen-com/hyperframes` or `npx skills add remotion-dev/skills`. You need Node 22+, Chrome and ffmpeg.
3. Start in an empty folder, paste a prompt from this list, and swap in your own subject, brand and assets.
4. Ask for one still frame per scene before the full render, then give notes like a director (see the vocabulary below).

## The Six-Step Director Workflow

Adapted from a thread by @rexan_wong, who reverse-engineered dozens of "one prompt" videos. [↗](https://x.com/rexan_wong/status/2103707054108299437)

### 1. Pick a reference

Choose one or two videos whose pacing and type you want and tell Opus to match them. Naming a style beats describing one. Without a reference it falls back to centered text on a gradient with everything fading in.

### 2. Install a renderer

HyperFrames or Remotion lets it write each scene as code and render straight to MP4. Every frame is exact, and a change edits one line instead of starting over.

### 3. Use real parts

Give it your real screenshots, logo and UI components instead of letting it invent buttons and cards. Invented UI is where a video starts to look cheap.

### 4. Dump all the context, ask for three storyboards

Brand, colors, fonts, screenshots, the reference and a quick braindump of the video you see. Three storyboard variants let you choose a direction instead of polishing its first idea.

### 5. Approve stills before motion

Ask for one still per scene. Fixing a storyboard takes seconds; fixing a finished render means re-rendering.

### 6. Give notes like a director

The first render is usually most of the way there. "Make it better" gets random changes; camera words get exactly the change you want.

## Anatomy of a Pro Prompt

Structure from the open template shared by @twoclipping, the most saved prompt in this list (19k+ bookmarks). [↗](https://x.com/twoclipping/status/2103273003555402193)

| Section | What goes in it |
|---|---|
| `<inputs>` | What Opus should ask you for before it starts, such as brand name, 8 to 12 photos or UI states, and a royalty-free track around 120 BPM. |
| `<direction>` | The look in one paragraph, plus a banned list (crossfades, glows, particles, holds over one second, anything that looks like a template). The banned list does more work than the style words. |
| `<structure>` | A beat grid and a scene chain, for example "120 BPM, 54 beats, something happens on every beat", with each scene growing out of the previous one. |
| `<build>` | Engineering rules that make it renderable, such as one HTML file, every value computed from time inside seek(t), closed-form springs, beat analysis, and subframe motion blur. |
| `<gotchas>` | Known failure modes to avoid, such as blurry text under a scaled camera, overlapping text swaps, and loops that stutter on the last frame. |
| `<start>` | What to do first, usually "ask me for the inputs, then show me the plan before writing code". |

## Director's Vocabulary

Say these instead of "make it better". Each one maps to a concrete change Opus can make in code.

| Term | When you want | Say |
|---|---|---|
| `push in` | Emphasize one element | Push in on the button over 0.8s. |
| `pull out` | Reveal the whole picture | Start tight on the chart, then pull out to the full page. |
| `hard cut on the beat` | Scene changes that hit the music | Hard cut here, landing on beat 17. |
| `match cut / morph` | Scenes that flow into each other | The circle in this shot becomes the logo in the next one. |
| `one continuous take` | No slideshow feeling | Never cut. Every scene is built out of the previous one. |
| `hold` | Give people time to read | Hold this line for 1.5s before it moves. |
| `slow to 0.7x` | Calm down a frantic cut | Slow every zoom to 0.7x. |
| `stagger` | Stop elements popping in all at once | Bring the cards in one by one, 80ms apart. |
| `ease-out / spring` | Less mechanical motion | Use a spring with a tiny overshoot, no bouncy easing. |
| `parallax` | Add depth to a flat frame | Move the foreground faster than the background. |
| `rack focus / depth of field` | Make the focal point obvious | Blur the background and keep only the product sharp. |
| `mask reveal` | Classy text entrances | Text rises out of a mask line instead of fading in. |
| `kinetic typography` | Words that carry the rhythm | Animate the voiceover word by word, locked to the waveform. |
| `whip pan` | Energetic transition | Whip pan left into the next scene with motion blur. |
| `speed ramp` | Make a key moment land | Ramp down to 0.3x right before the drop, then snap back. |
| `screen-studio zoom` | Product demos that follow the action | Zoom to fill the frame wherever the cursor clicks; scale the cursor with it. |
| `seamless loop` | A clip that can loop on a landing page | Make the last frame identical to the first, cursor position and speed included. |
| `beat grid` | Everything in sync with the music | Analyze the song for beats first and put one change on every beat. |

## The "One-Shot Slop" Checklist

Score your first render against these before you ask for changes. The seven symptoms are from @DavidKPiano; the fixes are ours. [↗](https://x.com/DavidKPiano/status/2103919227853783445)

| Symptom | Fix |
|---|---|
| Pacing is far too fast. | Slow every move to 0.7x and hold key text for at least a second. |
| Too many effects. | Add a banned list (glows, particles, crossfades, gradients) to the prompt. |
| No cohesion, with movement in every direction. | Pick one axis of motion per scene, or ask for one continuous take. |
| No focal point. | Name the one thing each scene is about and push in on it. |
| The same generic easing everywhere. | Ask for springs with a tiny overshoot, and vary timing between elements. |
| No choreography. | Give it a beat grid and assign one change to each beat. |
| Motion without meaning. | Tell it what each motion should explain, such as "the bar grows to show revenue doubling". |
