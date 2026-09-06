# Profile artwork and sources

The profile uses a flower-based visual identity, quiet CSS animations, and published product imagery. SVG files are self-contained and do not run JavaScript or load fonts from third-party services. Animations stop when the viewer requests reduced motion.

## Flower

- `flower-avatar.png`: the original photograph supplied by Vimalinx, used byte-for-byte in both profile banners. The flower and its photographic background are retained together within a circular avatar frame; no flower extraction, background removal, generated replacement, or soft edge mask is used.
- `profile-hero.svg` and `profile-hero-mobile.svg`: typography, circular photo framing, gentle movement, and animated orbital accents. The mobile asset is selected at widths up to 600px.
- The original photograph is also linked in full at the bottom of the profile.
- The earlier generated `flower-study.webp` is no longer displayed.

## Project imagery

- LocalRouter screenshots are from its [published documentation](https://github.com/vimalinx/LocalRouter/tree/main/docs/images). They show an isolated demonstration environment with fictional sample data, not live usage or account information. The slideshow presents the original images without changing their UI content.
- `agentseat-hero.svg` is the [project's published brand illustration](https://github.com/vimalinx/AgentSeat/blob/main/assets/brand/agentseat-hero.svg). It is not an application screenshot.
- `ecosystem.svg` is a capability illustration. Its flowing dots are decorative and do not indicate a live execution, integration test, or service status.

Original project assets remain subject to the terms of their source repositories.

## Rebuild

```sh
python3 scripts/build_profile.py
```

Requires only Python's standard library. The builder reads the existing image assets and generates the four SVG files. It makes no model or network calls.
