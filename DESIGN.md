---
name: Ethos Minimalist Portfolio
colors:
  surface: '#f8f9ff'
  surface-dim: '#d0dbed'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e6eeff'
  surface-container-high: '#dee9fc'
  surface-container-highest: '#d9e3f6'
  on-surface: '#121c2a'
  on-surface-variant: '#44474c'
  inverse-surface: '#27313f'
  inverse-on-surface: '#eaf1ff'
  outline: '#75777d'
  outline-variant: '#c4c6cd'
  surface-tint: '#515f74'
  primary: '#303e51'
  on-primary: '#ffffff'
  primary-container: '#475569'
  on-primary-container: '#bbcae1'
  inverse-primary: '#b9c7df'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#4d3a1c'
  on-tertiary: '#ffffff'
  tertiary-container: '#665131'
  on-tertiary-container: '#e2c59d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d5e3fc'
  primary-fixed-dim: '#b9c7df'
  on-primary-fixed: '#0d1c2e'
  on-primary-fixed-variant: '#3a485b'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#fcdeb4'
  tertiary-fixed-dim: '#dfc29a'
  on-tertiary-fixed: '#281901'
  on-tertiary-fixed-variant: '#574325'
  background: '#f8f9ff'
  on-background: '#121c2a'
  surface-variant: '#d9e3f6'
typography:
  display:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-mobile:
    fontFamily: Geist
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h1:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.25'
    letterSpacing: -0.01em
  h2:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  h3:
    fontFamily: Geist
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.02em
  caption:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.4'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 0.5rem
  sm: 1rem
  md: 1.5rem
  lg: 2.5rem
  xl: 4rem
  section: 8rem
  gutter: 24px
  margin-mobile: 20px
  max-width: 1120px
---

## Brand & Style
This design system is built for professionals who value clarity, intentionality, and a "human-made" touch. The brand personality is grounded and understated, prioritizing content over decorative flourish. 

The visual style is **Refined Minimalism**. It avoids the sterility of pure black-and-white by utilizing soft off-whites and deep charcoal slates. The emotional response should be one of immediate trust and calm, achieved through ample whitespace, precise typography, and a lack of aggressive visual effects. High-quality execution is signaled through subtle border treatments and a rhythmic layout rather than complex gradients or motion.

## Colors
The palette is built on a foundation of "Slates" to maintain a professional, calm atmosphere. 

- **Primary:** A muted slate blue (#475569) used sparingly for interactive elements and accents.
- **Light Mode:** Uses an off-white background (#F9FAFB) to reduce eye strain compared to pure white. Cards are pure white (#FFFFFF) with 1px slate-gray borders (#E2E8F0).
- **Dark Mode:** Employs a deep navy-charcoal (#0F172A) for the base layer, with surface elements stepping up to a lighter charcoal (#1E293B) to create depth without relying on heavy shadows.
- **Text:** High contrast but not absolute. Dark charcoal (#1F2937) for light mode and soft white (#F8FAFC) for dark mode ensures maximum legibility.

## Typography
The system uses **Geist** for its technical precision and humanist clarity. The hierarchy is designed for long-form reading and clear scanning of portfolio projects.

- **Headlines:** Use semi-bold weights with slightly tighter letter spacing for a modern, editorial feel. 
- **Body Text:** Set with generous line heights (1.6) to improve readability and contribute to the "calm" brand feeling.
- **Scale:** On mobile devices, the display size scales down to 36px to prevent awkward word breaks while maintaining visual impact.
- **Monospace lean:** Geist's subtle technical influence makes it ideal for showcasing process, metadata, or technical skills in a portfolio context.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy on desktop to ensure content remains centered and focused, transitioning to a fluid model for tablet and mobile.

- **Rhythm:** A 4px baseline grid ensures consistent vertical rhythm.
- **Desktop:** 12-column grid with a 1120px max-width, 24px gutters, and 64px (xl) margins.
- **Tablet:** 8-column grid with 40px (lg) margins.
- **Mobile:** 4-column grid with 20px margins.
- **Vertical Spacing:** Sections are separated by significant whitespace (8rem/128px) to allow each project or thought to breathe independently.

## Elevation & Depth
This design system prioritizes **Tonal Layers** and **Low-contrast Outlines** over heavy shadows.

- **Hierarchy:** Depth is communicated primarily through subtle background shifts. The background is the lowest layer; cards sit one level above.
- **Borders:** In light mode, use a 1px border (#E2E8F0). In dark mode, use a 1px border (#334155). 
- **Shadows:** Use only one "Ambient" shadow style for hover states: `0 10px 30px -10px rgba(0,0,0,0.05)`. This should be nearly imperceptible, serving only to lift the element slightly on interaction.
- **Flatness:** Interactive elements like buttons and inputs should remain flat, using color fills rather than gradients or bevels.

## Shapes
The shape language is **Soft (Level 1)**. 

Elements use a 0.25rem (4px) base radius. This provides a professional "architectural" feel—more approachable than sharp corners, but more serious than highly rounded or pill-shaped containers. 

- **Cards/Containers:** Use `rounded-lg` (8px).
- **Buttons/Inputs:** Use base `rounded` (4px).
- **Badges:** Use `rounded-xl` (12px) for a subtle "pill" distinction from structural components.

## Components
- **Buttons:** Primary buttons use a solid slate (#475569) fill with white text. Secondary buttons use a transparent background with a 1px border. Focus states must be a clear 2px offset ring.
- **Cards:** White or charcoal backgrounds with 1px borders. Padding inside cards should be generous (24px to 32px) to maintain the minimalist aesthetic.
- **Badges/Chips:** Used for skills or project tags. Small font size (12px), semi-bold, with a light gray background in light mode and a deep slate background in dark mode. No borders.
- **Input Fields:** Minimalist design with only a bottom border (2px) or a very light 4-sided stroke. Focus state changes the stroke color to the primary accent.
- **Lists:** Use custom bullet points (small squares or dashes) in the primary slate color to reinforce the "human-made" and precise feel of the portfolio.
- **Project Grid:** Images should have the same 8px corner radius as cards, with a subtle 1px inner stroke to ensure edge definition against light backgrounds.