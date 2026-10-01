# glyph-peek

看清文字里每个 Unicode 码位：码点、类别、标准名称和字符本身。适合排查隐藏字符、组合符号、emoji 和相似字形。

## 使用

需要 Python 3.8+，只用标准库，不联网。

```sh
python glyph_peek.py "A 中 🌊"
```

Windows 上也可以运行：

```powershell
py .\glyph_peek.py "A 中 🌊"
```

输出序号按 Unicode 码位计数；一个看起来完整的 emoji 可能由多个码位组成。字符名称来自当前 Python 版本附带的 Unicode 数据库。

## 许可

MIT，见 [LICENSE](LICENSE)。
## Linux x86_64 下载

- [单文件版](https://github.com/506058115-cmd/glyph-peek/releases/download/v1.0.0/glyph-peek-linux-x86_64-onefile.tar.gz)
- [目录版](https://github.com/506058115-cmd/glyph-peek/releases/download/v1.0.0/glyph-peek-linux-x86_64-onedir.tar.gz)
- [v1.0.0 Release 页面](https://github.com/506058115-cmd/glyph-peek/releases/tag/v1.0.0)

压缩包附带构建信息和依赖许可证；Release 另附 SHA-256 校验文件。产物在 WSL Ubuntu 24.04（Python 3.12.3、PyInstaller 6.22.2）中构建，目标为 GNU/Linux x86_64。较旧的发行版可能需要兼容的 glibc。
