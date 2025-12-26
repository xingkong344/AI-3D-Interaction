#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
启动本地HTTP服务器，用于访问基于Three.js的3D虚拟伙伴应用
"""

import http.server
import socketserver
import webbrowser
import os
import sys

# 服务器配置
PORT = 8000
HOST = "localhost"

# 确保在正确的目录中运行
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 创建HTTP服务器
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print(f"\n3D虚拟伙伴Web应用已启动！")
    print(f"服务器地址: http://{HOST}:{PORT}")
    print(f"请在浏览器中访问上述地址")
    print(f"按 Ctrl+C 停止服务器\n")
    
    try:
        # 自动打开浏览器
        webbrowser.open(f"http://{HOST}:{PORT}")
        
        # 启动服务器
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        sys.exit(0)