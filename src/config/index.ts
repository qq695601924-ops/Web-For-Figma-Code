/**
 * @name 配置文件
 */

/** 应用名称 */
export const APP_NAME = import.meta.env.VITE_APP_NAME || 'Vexora'

/** 邮箱 */
export const EMAIL = ['sales@vexora.com', 'support@vexora.com']

/** 地址 */
export const ADDRESS = '---'

/** 版权所有 */
export const COPYRIGHT = '© 2025 Vexora Technologies. All rights reserved.'

export interface MenuItem {
  name: string
  selector?: string
}

/** 菜单列表 */
export const menuList: MenuItem[] = [
  {
    name: 'Home',
    selector: 'banner-section',
  },
  {
    name: 'Advantages',
    selector: 'why-section',
  },
  {
    name: 'Services',
    selector: 'services-section',
  },
  {
    name: 'Global Reach',
    selector: 'map-section',
  },
  {
    name: 'About',
    selector: 'about-section',
  },
]
