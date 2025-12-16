import Client from 'ssh2-sftp-client'
import { existsSync, readFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)
// 脚本在 build/scripts/，需要回到项目根目录
const rootDir = join(__dirname, '../..')

// SFTP配置
const config = {
  host: '47.236.196.237',
  port: 22,
  username: 'root',
  privateKey: readFileSync(join(rootDir, 'SG-OUT.pem')),
  remotePath: '/home/future-harvest-web/dist',
  localPath: join(rootDir, 'dist'),
}

async function deploy() {
  const sftp = new Client()

  try {
    console.log('正在连接到服务器...')
    await sftp.connect(config)

    console.log('连接成功，开始上传文件...')

    // 检查本地dist目录是否存在
    if (!existsSync(config.localPath)) {
      throw new Error(`本地目录不存在: ${config.localPath}`)
    }

    // 先删除远程目录的所有文件（完全替换）
    try {
      console.log('正在清理远程目录...')
      const files = await sftp.list(config.remotePath)
      for (const file of files) {
        const remoteFile = `${config.remotePath}/${file.name}`.replace(/\/+/g, '/')
        if (file.type === 'd') {
          await sftp.rmdir(remoteFile, true)
        }
        else {
          await sftp.delete(remoteFile)
        }
      }
      console.log('远程目录清理完成')
    }
    catch (error) {
      // 如果目录不存在，尝试创建
      if (error.code === 2 || error.message.includes('No such file')) {
        console.log('远程目录不存在，将自动创建...')
        await sftp.mkdir(config.remotePath, true)
      }
      else {
        console.log('清理远程目录时出错:', error.message)
      }
    }

    // 上传整个dist目录
    console.log(`正在上传 ${config.localPath} 到 ${config.remotePath}...`)
    await sftp.uploadDir(config.localPath, config.remotePath)

    console.log('✅ 部署成功！')
  }
  catch (error) {
    console.error('❌ 部署失败:', error.message)
    require('node:process').exit(1)
  }
  finally {
    await sftp.end()
  }
}

deploy()
