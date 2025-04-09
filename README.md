# 🔍 BP-Release-Analyzer

This project, is intended to be capable of split '.BPRelease' files, in order to get specific contents from each release, and also, analyze it's content in order to notify the user if their release is acomplishing the good practices of Blue Prism

---

## 🚧 Status

Right now, this analyzer is capable of Trimming both Objects and Processes from the release, but not clean at all.
That means, that the content is removed, but there's a chance of trash descriptions and tags are not deleted, which will cause the release not to work correctly.

---

## ⚙️ Requeriments

- [Python 3.8+](https://www.python.org/downloads/)
- OS with console access (CMD as preference)

---

## 🚀 How to use it

1. Clone the repository or download it as ZIP.
2. CD until you're in the directory where 'main.py' is.
3. Execute 'python main.py' and follow the instructions.

Note: This version is still unstable, so please, delete your Processes and Objects in order.
Ex: "1, 1, 1, 3". "3, 6, 1, 2" Can cause exceptions.

---
