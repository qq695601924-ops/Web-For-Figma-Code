/**
 * @name 配置文件
 */

/** 应用名称 */
export const APP_NAME = import.meta.env.VITE_APP_NAME || 'vexora'

/** 邮箱 */
export const EMAIL = ['sales@vexora.tech', 'support@vexora.tech']

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
    name: 'Features',
    selector: 'why-section',
  },
  {
    name: 'Pricing',
    selector: 'services-section',
  },
  {
    name: 'Careers',
    selector: 'business-focus',
  },
  {
    name: 'Help',
    selector: 'question-section',
  },
]
