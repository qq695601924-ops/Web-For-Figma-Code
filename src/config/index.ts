/**
 * @name 配置文件
 */

/** 应用名称 */
export const APP_NAME = import.meta.env.VITE_APP_NAME || 'Optivolve Digital'

/** 邮箱 */
export const EMAIL = ['partnership@optivolvedigital.com', 'it@optivolvedigital.com', 'customerservices@optivolvedigital.com']

/** 地址 */
export const ADDRESS = '---'

/** 版权所有 */
export const COPYRIGHT = '© 2025 Optivolve Digital. All rights reserved.'

/** 页脚品牌名 */
export const FOOTER_BRAND = 'SeguroCash'

/** 客服邮箱（页脚展示与复制） */
export const SUPPORT_EMAIL = 'soporte@segurocash.com'

/** 页脚版权文案 */
export const FOOTER_COPYRIGHT = '© 2023, All Rights Reserved'

/** Google Play 下载链接 */
export const GOOGLE_PLAY_URL = 'https://play.google.com/store/apps/details?id=com.seguro.cash.rapido&hl=en-gb&gl=ng'

export interface MenuItem {
  name: string
  path: string
  selector?: string
}

/** 菜单列表 */
export const menuList: MenuItem[] = [
  { name: 'Inicio', path: '/inicio' },
  { name: 'Seguridad', path: '/seguridad' },
  { name: 'Ayuda', path: '/ayuda' },
  { name: 'Sobre Nosotros', path: '/sobre-nosotros' },
]
