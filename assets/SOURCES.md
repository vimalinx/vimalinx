# Profile artwork and sources

The profile uses a flower-based visual identity, quiet CSS animations, and published product imagery. SVG files are self-contained and do not run JavaScript or load fonts from third-party services. Animations stop when the viewer requests reduced motion.

## Flower

- `flower-avatar.png`: the original flower image supplied by Vimalinx for this profile.
- `flower-study.webp`: a photographic interpretation extracted from that image with the built-in image generation tool, then exported as WebP. It is a derived asset, not a pixel-identical cutout. The original is retained separately.
- `profile-hero.svg` and `profile-hero-mobile.svg`: typography, layout, image masking, slow flower movement, and animated orbital accents. The mobile asset is selected at widths up to 600px.

First generation prompt:

> Use case: precise-object-edit. Edit target: the supplied photograph of a single pale white/lavender flower on pavement. Extract ONLY the large central five-petal flower as a clean photorealistic cutout on a genuinely transparent alpha background. Preserve its exact asymmetrical petal shapes, orientation, white and lavender coloration, wrinkles and veins, natural lighting, central delicate filaments and yellow pollen, and photographic character. Remove pavement, shadows cast on pavement, surrounding green buds/leaves and all unrelated objects. Do not invent or beautify a different flower; keep this particular flower recognizable. All five petals and delicate stamens must remain complete, no clipping. Center the flower with about 8% transparent margin on all sides, square canvas. No text, no border, no opaque/colored backdrop, no checkerboard baked into image, no additional flowers. Intended asset: a layered animated GitHub profile hero.

The first result had an opaque checkerboard background, so it was not used in the profile. The selected image uses this correction prompt:

> Precise background correction of this exact image. Keep this exact five-petal flower, every petal outline, orientation, stamens, texture and natural white/lavender colors unchanged. Replace the entire gray-and-white checkerboard background with perfectly uniform very dark plum-black, RGB hex #111016. Remove the checkerboard completely including every gap between petals and stamens. Do NOT simulate transparency. Do NOT add glow, shadows, pattern, stars, text, leaves or new objects. Maintain a generous empty dark margin around the flower, roughly 12% padding each side; complete flower visible, no clipping. This is a photographic asset for a GitHub profile banner. The background should be an absolutely solid flat #111016.

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
