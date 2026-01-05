import {
  defineConfig,
  presetAttributify,
  presetIcons,
  presetMini,
} from 'unocss'
import transformerDirectives from '@unocss/transformer-directives'

import presetWind3 from '@unocss/preset-wind3'
// https://unocss.dev/presets/rem-to-px
import presetRemToPx from '@unocss/preset-rem-to-px'

export default defineConfig({
  presets: [
    presetWind3(),
    presetAttributify,
    presetIcons(),
    presetRemToPx({
      baseFontSize: 4,
    }),
    presetMini(),
  ],
  transformers: [
    transformerDirectives(),
  ],
  shortcuts: {
    // 只在移动端显示
    'mobile-only': 'md:hidden',
    // 只在 PC 端显示
    'pc-only': 'hidden md:block',
    // 移动端间距
    'mobile-px-100': 'md:px-0 px-100',
    'mobile-py-50': 'md:py-0 py-50',
    'mobile-py-100': 'md:py-0 py-100',
  },
})
