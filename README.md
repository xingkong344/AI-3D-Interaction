# 3D Virtual Companion

一个基于Three.js的3D虚拟伙伴Web应用，支持多种AI服务提供商，可与用户进行交互对话，具有3D场景和角色渲染功能。

## 项目概述

该项目已从Panda3D迁移到Web-based解决方案，使用Three.js作为3D引擎，提供更广泛的兼容性和更现代的用户体验。

## 技术栈

- **3D渲染**: Three.js
- **前端框架**: HTML5 + CSS3 + JavaScript
- **AI服务**: 支持豆包、OpenAI、DeepSeek等多种AI提供商
- **开发语言**: Python (仅用于启动本地服务器)

## 功能特性

✅ 支持多种AI服务提供商（豆包、OpenAI、DeepSeek）
✅ 3D可视化界面和角色渲染
✅ 实时聊天功能，支持输入框和发送按钮
✅ 支持手动输入OpenAI模型名称
✅ 支持自定义OpenAI API基础地址
✅ 测试模型模式，无需API密钥即可运行
✅ 相机控制功能（缩放、旋转）
✅ 设置面板，支持保存和加载配置
✅ 响应式设计，聊天框固定在底部
✅ 支持Blender和MMD模型加载

## 项目结构

```
your_project_folder/
 │
 ├── index.html           # 主页面，包含Three.js 3D应用和聊天界面
 ├── run_web.py           # 本地HTTP服务器启动脚本
 ├── README.md            # 项目说明文档
 └── LICENSE              # 许可证文件
```

## 快速开始

### 1. 安装Python

确保您的系统已安装Python 3.6或更高版本。您可以从[Python官方网站](https://www.python.org/)下载并安装。

### 2. 克隆或下载项目

将项目文件下载到本地目录。

### 3. 启动本地服务器

在项目目录下运行以下命令启动本地HTTP服务器：

```bash
python run_web.py
```

### 4. 访问应用

服务器启动后，会自动在浏览器中打开应用，或者您可以手动访问：

```
http://localhost:8000
```

## 使用说明

### 1. 与虚拟伙伴交互

- **发送消息**: 在聊天输入框中输入消息，然后点击"发送"按钮或按回车键
- **查看回复**: AI的回复将显示在聊天记录中
- **重置场景**: 按Ctrl+R快捷键重置3D场景和聊天记录

### 2. 3D场景控制

- **鼠标滚轮**: 缩放场景
- **鼠标左键拖拽**: 旋转视角
- **鼠标右键拖拽**: 平移场景

### 3. 设置配置

1. 点击"设置"标签切换到设置面板
2. **AI提供商**: 选择您要使用的AI服务提供商（豆包、OpenAI、DeepSeek）
3. **API密钥**: 输入您的API密钥
4. **AI模型**: 
   - 对于豆包和DeepSeek，从下拉菜单中选择模型
   - 对于OpenAI，您可以手动输入模型名称
5. **OpenAI API基础地址**: 自定义OpenAI兼容API的基础地址
6. **模型路径**: 输入3D模型文件路径（支持GLTF/GLB或PMX/PMD格式）
7. **使用测试模型**: 启用后使用本地测试模型，无需API密钥
8. 点击"保存设置"保存配置
9. 点击"加载模型"加载指定路径的3D模型

## 配置说明

### AI提供商配置

#### 豆包
- **API密钥**: 从[豆包开发者平台](https://www.doubao.com/)获取
- **支持模型**: doubao-pro-32k

#### OpenAI
- **API密钥**: 从[OpenAI官方网站](https://platform.openai.com/)获取
- **支持模型**: 可以手动输入任何OpenAI兼容模型，如gpt-3.5-turbo、gpt-4、gpt-4o等
- **API基础地址**: 默认为https://api.openai.com/v1，可自定义为其他OpenAI兼容API

#### DeepSeek
- **API密钥**: 从[DeepSeek开发者平台](https://platform.deepseek.com/)获取
- **支持模型**: deepseek-chat、deepseek-coder

### 测试模式

启用"使用测试模型"选项后，应用将使用内置的测试回复，无需API密钥即可运行。这对于演示和测试非常有用。

## 模型支持

该应用支持以下3D模型格式：

- **Blender模型**: GLTF/GLB格式
- **MMD模型**: PMX/PMD格式

## 浏览器兼容性

该应用支持所有现代浏览器：

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## 许可证

本项目采用GPL许可证。

## 致谢

感谢以下开源项目和服务提供商：

### 3D渲染
- **[Three.js](https://threejs.org/)**: 强大的WebGL 3D库

### AI服务
- **[豆包](https://www.doubao.com/)**: 提供高质量的中文AI服务
- **[OpenAI](https://openai.com/)**: 提供强大的GPT系列模型
- **[DeepSeek](https://www.deepseek.com/)**: 提供先进的AI模型

### 其他开源库
- **[Python](https://www.python.org/)**: 用于启动本地服务器

## 联系方式

如果您在使用过程中遇到问题，或有任何建议，欢迎通过以下方式联系：

- 提交Issue
- 参与项目贡献

---

**享受与3D虚拟伙伴的对话吧！** 🚀