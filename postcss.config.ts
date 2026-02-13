// 此文件不支持热更新，修改后需要重启生效
export default {
  plugins: {
    'autoprefixer': {},

    // https://github.com/wswmsword/postcss-mobile-forever
    'postcss-mobile-forever': {
      viewportWidth: 1920,
      appSelector: '#main-page',
    },
  },
}
